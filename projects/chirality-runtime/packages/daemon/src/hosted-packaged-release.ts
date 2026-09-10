import { createHash } from "node:crypto";
import { constants } from "node:fs";
import { link, lstat, mkdir, open, realpath, rm } from "node:fs/promises";
import { dirname, isAbsolute, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import {
  matchRuntimeSupportProfileV2, observeRuntimeSupportProfileV2, verifyPackagedRuntimeBasisV2,
  type EmbeddedRuntimeVersionsV2, type RuntimeArtifactEntryV2, type RuntimeSupportProfileV2,
  type VerifiedPackagedRuntimeBasisV2
} from "@chirality/runtime-core/runtime-conformance-v2";
import { type HostedBootstrapRuntimeBootInput, type HostedBootstrapRuntimeHost } from "./hosted-bootstrap.js";
import { startHostedPrivateBootstrapRuntimeHost } from "./hosted-private-entry.js";
import { inspectRuntimePurposeAcceptanceV2,inspectRuntimePurposeReleaseV2 } from "./runtime-conformance-v2-admission.js";
import {
  assertIssuedPrivateDirectoryChainV2,
  assertIssuedPackagedReleaseBasisV2,
  isControlledPackagedReleaseBasisForTests,
  readIssuedPrivateFileV2,
  registerIssuedPackagedReleaseBasisV2,
  revalidateControlledPackagedReleaseBasisForTests,
  revalidateIssuedPackagedReleaseBasisV2,
  type HostedPackagedPurposeBasisV2,
  type HostedPackagedReleaseBasisV2,
  type HostedReleaseAnchorPurposeV2
} from "./hosted-packaged-release-state.js";

export type { HostedPackagedPurposeBasisV2, HostedPackagedReleaseBasisV2, HostedReleaseAnchorPurposeV2 } from "./hosted-packaged-release-state.js";

type BootstrapEnabled = Extract<HostedBootstrapRuntimeBootInput,{enabled:true}>;
type Purpose = "login" | "worker";
export interface HostedReleaseAnchorV2 {
  schema: "chirality-runtime-release-anchor/v2";
  outerInventorySha256: string;
  login: HostedReleaseAnchorPurposeV2;
  worker: HostedReleaseAnchorPurposeV2;
}
export type HostedPackagedReleaseLoadResult =
  | { status:"ready"; basis:Readonly<HostedPackagedReleaseBasisV2> }
  | { status:"unavailable"; reason:"missing-release-basis"|"invalid-release-basis"|"unsupported-runtime" };

const hash=(value:string|Buffer)=>createHash("sha256").update(value).digest("hex");
const digest=(value:unknown):value is string=>typeof value==="string"&&/^[a-f0-9]{64}$/.test(value);
const unavailable=(reason:string)=>new RuntimeError("ENGINE_UNAVAILABLE","Packaged hosted Runtime release basis is unavailable",503,{reason});
function canonical(path:string):boolean{return isAbsolute(path)&&resolve(path)===path&&!/[\x00-\x1f]/.test(path);}
function exactKeys(value:unknown,names:readonly string[]):value is Record<string,unknown>{return !!value&&typeof value==="object"&&!Array.isArray(value)&&Object.keys(value).length===names.length&&names.every(name=>Object.hasOwn(value,name));}
async function ensurePrivateDirectoryExact(path:string):Promise<void>{
  try{await mkdir(path,{mode:0o700});}catch(error){if((error as NodeJS.ErrnoException).code!=="EEXIST")throw error;}
  const info=await lstat(path);if(!info.isDirectory()||info.isSymbolicLink()||info.uid!==(process.getuid?.()??-1)||(info.mode&0o777)!==0o700||await realpath(path)!==path)throw unavailable("PRIVATE_RELEASE_DIRECTORY_UNSAFE");
}
const assertPrivateChain=assertIssuedPrivateDirectoryChainV2;
const stablePrivateFile=readIssuedPrivateFileV2;
async function stablePackagedFile(path:string,maximum=1_048_576):Promise<{bytes:Buffer;sha256:string}>{
  if(!canonical(path)||await realpath(path)!==path)throw unavailable("INVALID_PACKAGED_GOVERNANCE");const file=await open(path,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);
  try{const before=await file.stat({bigint:true});if(!before.isFile()||before.nlink!==1n||before.size>BigInt(maximum))throw unavailable("INVALID_PACKAGED_GOVERNANCE");const parts:Buffer[]=[];let total=0,position=0;const buffer=Buffer.alloc(65_536);for(;;){const {bytesRead}=await file.read(buffer,0,Math.min(buffer.length,Number(before.size)+1-total),position);if(!bytesRead)break;total+=bytesRead;position+=bytesRead;if(total>Number(before.size)||total>maximum)throw unavailable("CHANGED_PACKAGED_GOVERNANCE");parts.push(Buffer.from(buffer.subarray(0,bytesRead)));}const bytes=Buffer.concat(parts,total),after=await file.stat({bigint:true}),pathInfo=await lstat(path,{bigint:true});for(const key of ["dev","ino","size","mtimeNs","ctimeNs"] as const)if(before[key]!==after[key]||before[key]!==pathInfo[key])throw unavailable("CHANGED_PACKAGED_GOVERNANCE");if(bytes.length!==Number(before.size)||await realpath(path)!==path)throw unavailable("CHANGED_PACKAGED_GOVERNANCE");return {bytes,sha256:hash(bytes)};}finally{await file.close();}
}
function inspectPurpose(value:unknown):HostedReleaseAnchorPurposeV2{
  if(!exactKeys(value,["recordSha256","acceptanceSha256","ownerActSha256","activationId","gateIdentity"])||!digest(value.recordSha256)||!digest(value.acceptanceSha256)||!digest(value.ownerActSha256)||typeof value.activationId!=="string"||!value.activationId.trim()||typeof value.gateIdentity!=="string"||!value.gateIdentity.trim())throw unavailable("INVALID_RELEASE_ANCHOR");
  return value as unknown as HostedReleaseAnchorPurposeV2;
}
function inspectAnchor(value:unknown):HostedReleaseAnchorV2{
  if(!exactKeys(value,["schema","outerInventorySha256","login","worker"])||value.schema!=="chirality-runtime-release-anchor/v2"||!digest(value.outerInventorySha256))throw unavailable("INVALID_RELEASE_ANCHOR");
  return {schema:value.schema,outerInventorySha256:value.outerInventorySha256,login:inspectPurpose(value.login),worker:inspectPurpose(value.worker)};
}
const governanceNames:Record<Purpose,readonly[string,string,string]>={
  login:["login-purpose-record.json","login-purpose-acceptance.json","login-owner-act"],
  worker:["worker-purpose-record.json","worker-purpose-acceptance.json","worker-owner-act"]
};
async function snapshotPurpose(input:{resourcesRoot:string;snapshotRoot:string;purpose:Purpose;anchor:HostedReleaseAnchorPurposeV2;entries:readonly RuntimeArtifactEntryV2[]}):Promise<HostedPackagedPurposeBasisV2>{
  const names=governanceNames[input.purpose],expected=[input.anchor.recordSha256,input.anchor.acceptanceSha256,input.anchor.ownerActSha256];
  const targets:string[]=[];
  for(let index=0;index<names.length;index++){
    const relativePath=`runtime-governance/v2/${names[index]}`,entry=input.entries.find(item=>item.relativePath===relativePath);
    if(!entry||entry.sha256!==expected[index])throw unavailable("ANCHOR_GOVERNANCE_MISMATCH");
    const sourcePath=join(input.resourcesRoot,relativePath);
    const destination=join(input.snapshotRoot,names[index]!);let temporary:string|undefined;
    try{
      const {bytes,sha256}=await stablePackagedFile(sourcePath);
      if(sha256!==expected[index])throw unavailable("ANCHOR_GOVERNANCE_MISMATCH");
      await ensurePrivateDirectoryExact(dirname(destination));
      try{const existing=await stablePrivateFile(destination);if(existing.sha256!==expected[index])throw unavailable("PRIVATE_RELEASE_SNAPSHOT_CONFLICT");}
      catch(error){if((error as NodeJS.ErrnoException).code!=="ENOENT")throw error;temporary=`${destination}.${process.pid}.${hash(bytes).slice(0,16)}.tmp`;const output=await open(temporary,constants.O_WRONLY|constants.O_CREAT|constants.O_EXCL|constants.O_NOFOLLOW,0o600);try{await output.writeFile(bytes);await output.sync();}finally{await output.close();}try{await link(temporary,destination);}catch(linkError){if((linkError as NodeJS.ErrnoException).code!=="EEXIST")throw linkError;}await rm(temporary,{force:true});temporary=undefined;}
      if((await stablePrivateFile(destination)).sha256!==expected[index])throw unavailable("PRIVATE_RELEASE_SNAPSHOT_CONFLICT");targets.push(destination);
    }finally{if(temporary)await rm(temporary,{force:true});}
  }
  return Object.freeze({recordSha256:expected[0]!,acceptanceSha256:expected[1]!,ownerActSha256:expected[2]!,activationId:input.anchor.activationId,gateIdentity:input.anchor.gateIdentity,recordPath:targets[0]!,acceptancePath:targets[1]!,ownerActPath:targets[2]!});
}

async function verifyPurposeAcceptance(input:{purpose:Purpose;basis:HostedPackagedPurposeBasisV2;payloadDigest:string;profile:RuntimeSupportProfileV2}):Promise<void>{
  const [recordSource,acceptanceSource,ownerAct]=await Promise.all([stablePrivateFile(input.basis.recordPath),stablePrivateFile(input.basis.acceptancePath),stablePrivateFile(input.basis.ownerActPath)]);
  if(recordSource.sha256!==input.basis.recordSha256||acceptanceSource.sha256!==input.basis.acceptanceSha256||ownerAct.sha256!==input.basis.ownerActSha256)throw unavailable("PRIVATE_RELEASE_SNAPSHOT_CHANGED");
  let record:unknown,acceptance:unknown;try{record=JSON.parse(recordSource.bytes.toString("utf8"));acceptance=JSON.parse(acceptanceSource.bytes.toString("utf8"));}catch{throw unavailable("PURPOSE_RELEASE_INVALID");}
  const inspected=inspectRuntimePurposeReleaseV2({purpose:input.purpose,record,expected:{payloadDigest:input.payloadDigest,supportProfile:input.profile}});
  inspectRuntimePurposeAcceptanceV2({purpose:input.purpose,acceptance,expected:{recordSha256:recordSource.sha256,sourceDigest:inspected.sourceDigest,ownerActSha256:ownerAct.sha256,activationId:input.basis.activationId,gateIdentity:input.basis.gateIdentity}});
}
function deepFreeze<T>(value:T):Readonly<T>{if(value&&typeof value==="object"){for(const child of Object.values(value as Record<string,unknown>))deepFreeze(child);Object.freeze(value);}return value;}

async function loadBasis(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2},observe:typeof observeRuntimeSupportProfileV2,issuance:"production"|"controlled-test",hooks?:{captureFailure?:(error:unknown)=>void;beforeFinalRevalidation?:()=>Promise<void>}):Promise<HostedPackagedReleaseLoadResult>{
  try{
    if(!canonical(input.resourcesRoot)||!canonical(input.runtimeDirectory))throw unavailable("INVALID_PACKAGED_RELEASE_INPUT");
    const anchorRoot=join(input.runtimeDirectory,"release-authority","v2"),anchorRootInfo=await lstat(anchorRoot);
    await assertPrivateChain(input.runtimeDirectory,anchorRoot);
    if(!anchorRootInfo.isDirectory()||anchorRootInfo.uid!==(process.getuid?.()??-1)||(anchorRootInfo.mode&0o077)!==0||await realpath(anchorRoot)!==anchorRoot)throw unavailable("INVALID_RELEASE_ANCHOR_CUSTODY");
    const anchorPath=join(anchorRoot,"release-anchor.json"),anchorSource=await stablePrivateFile(anchorPath);
    const anchor=inspectAnchor(JSON.parse(anchorSource.bytes.toString("utf8"))),verified=await verifyPackagedRuntimeBasisV2({resourcesRoot:input.resourcesRoot});
    if(verified.inventorySha256!==anchor.outerInventorySha256)throw unavailable("ANCHOR_INVENTORY_MISMATCH");
    const observedCandidates:RuntimeSupportProfileV2[]=[];
    for(const candidate of verified.payload.supportProfiles){
      try{const observed=await observe({embeddedRuntime:input.embeddedRuntime,basis:verified,supplierVersion:candidate.supplier.version,appServerProtocolDigest:candidate.supplier.appServerProtocolDigest,immutableSystemRoots:candidate.immutableSystemRoots});if(observed.profileDigest===candidate.profileDigest)observedCandidates.push(observed);}catch{}
    }
    if(observedCandidates.length!==1)throw unavailable("UNSUPPORTED_RUNTIME");
    const supportProfile=matchRuntimeSupportProfileV2(observedCandidates[0]!,verified.payload.supportProfiles);
    const basisDigest=hash(JSON.stringify({anchorSha256:anchorSource.sha256,inventorySha256:verified.inventorySha256,payloadDigest:verified.payloadDigest,profileDigest:supportProfile.profileDigest}));
    const releaseBasisRoot=join(input.runtimeDirectory,"release-basis");await ensurePrivateDirectoryExact(releaseBasisRoot);const snapshotRoot=join(releaseBasisRoot,basisDigest);await ensurePrivateDirectoryExact(snapshotRoot);await assertPrivateChain(input.runtimeDirectory,snapshotRoot);
    const login=await snapshotPurpose({resourcesRoot:verified.resourcesRoot,snapshotRoot,purpose:"login",anchor:anchor.login,entries:verified.inventory.governance});
    const worker=await snapshotPurpose({resourcesRoot:verified.resourcesRoot,snapshotRoot,purpose:"worker",anchor:anchor.worker,entries:verified.inventory.governance});
    await verifyPurposeAcceptance({purpose:"login",basis:login,payloadDigest:verified.payloadDigest,profile:supportProfile});
    await verifyPurposeAcceptance({purpose:"worker",basis:worker,payloadDigest:verified.payloadDigest,profile:supportProfile});
    await hooks?.beforeFinalRevalidation?.();
    const finalAnchor=await stablePrivateFile(anchorPath),finalVerified=await verifyPackagedRuntimeBasisV2({resourcesRoot:input.resourcesRoot});
    if(finalAnchor.sha256!==anchorSource.sha256||finalVerified.inventorySha256!==verified.inventorySha256||finalVerified.payloadDigest!==verified.payloadDigest)throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
    const finalLogin=await snapshotPurpose({resourcesRoot:finalVerified.resourcesRoot,snapshotRoot,purpose:"login",anchor:anchor.login,entries:finalVerified.inventory.governance}),finalWorker=await snapshotPurpose({resourcesRoot:finalVerified.resourcesRoot,snapshotRoot,purpose:"worker",anchor:anchor.worker,entries:finalVerified.inventory.governance});
    if(JSON.stringify(finalLogin)!==JSON.stringify(login)||JSON.stringify(finalWorker)!==JSON.stringify(worker))throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
    await verifyPurposeAcceptance({purpose:"login",basis:finalLogin,payloadDigest:finalVerified.payloadDigest,profile:supportProfile});await verifyPurposeAcceptance({purpose:"worker",basis:finalWorker,payloadDigest:finalVerified.payloadDigest,profile:supportProfile});
    const basis=deepFreeze(structuredClone({schema:"chirality-hosted-packaged-release-basis/v2" as const,basisDigest,verified:finalVerified,supportProfile,instructionRoot:join(verified.resourcesRoot,"instruction-root"),nativeAddonPath:join(verified.resourcesRoot,"native/chirality_native_admission.node"),supplierExecutablePath:join(verified.resourcesRoot,"supplier/codex"),preNativeFilesystemObservation:{runtimeDirectory:input.runtimeDirectory,anchorRoot,evidence:"canonical-owner-mode-chain-observed" as const},login:finalLogin,worker:finalWorker}));
    await registerIssuedPackagedReleaseBasisV2(basis,{issuance,resourcesRoot:finalVerified.resourcesRoot,runtimeDirectory:input.runtimeDirectory,anchorRoot,anchorPath,anchorSha256:finalAnchor.sha256,
      inventorySha256:finalVerified.inventorySha256,payloadDigest:finalVerified.payloadDigest,profileDigest:supportProfile.profileDigest,basisDigest,login:basis.login,worker:basis.worker});
    return {status:"ready",basis};
  }catch(error){
    hooks?.captureFailure?.(error);
    const code=(error as NodeJS.ErrnoException).code;if(code==="ENOENT")return {status:"unavailable",reason:"missing-release-basis"};
    const reason=(error as RuntimeError).details?.reason;return {status:"unavailable",reason:reason==="UNSUPPORTED_RUNTIME"?"unsupported-runtime":"invalid-release-basis"};
  }
}

/** Pure filesystem/support verification. It must complete before any native addon or XPC authority mechanism is loaded. */
export function loadPackagedHostedReleaseBasis(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2}):Promise<HostedPackagedReleaseLoadResult>{return loadBasis(input,observeRuntimeSupportProfileV2,"production");}

type PackagedStartInput={bootstrap:BootstrapEnabled;basis:Readonly<HostedPackagedReleaseBasisV2>};
type PrivateStarter=(input:Parameters<typeof startHostedPrivateBootstrapRuntimeHost>[0])=>Promise<HostedBootstrapRuntimeHost>;
async function startPackaged(input:PackagedStartInput,revalidate:(basis:Readonly<HostedPackagedReleaseBasisV2>)=>Promise<void>|void,start:PrivateStarter):Promise<HostedBootstrapRuntimeHost>{
  if(!input||input.bootstrap?.enabled!==true)throw unavailable("PACKAGED_BOOTSTRAP_BASIS_MISMATCH");
  await revalidate(input.basis);
  if(input.bootstrap.runtimeDirectory!==dirname(dirname(dirname(input.basis.login.recordPath)))||input.bootstrap.instructionRoot!==input.basis.instructionRoot||input.bootstrap.nativeAddonPath!==input.basis.nativeAddonPath)throw unavailable("PACKAGED_BOOTSTRAP_BASIS_MISMATCH");
  return start({bootstrap:{...input.bootstrap,artifactInventory:undefined},privateComposition:{runtimeDirectory:input.bootstrap.runtimeDirectory,
    supplierExecutablePath:input.basis.supplierExecutablePath,nativeAddonPath:input.basis.nativeAddonPath,instructionRoot:input.basis.instructionRoot,
    compatibility:{compatibilityIdentity:"root-runtime-1",contractBasisSha256:"6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2"},
    commandNetworkPosture:"off",protectedPaths:[input.bootstrap.runtimeDirectory,join(input.bootstrap.runtimeDirectory,"release-authority"),join(input.bootstrap.runtimeDirectory,"release-basis")],
    immutableReadRoots:[...input.basis.supportProfile.immutableSystemRoots],turnTimeoutMs:600_000,releaseV2:{basis:input.basis}}});
}

/** Packaged startup consumes only a current loader-issued basis and derives the fixed private v2 composition. */
export function startHostedPackagedPrivateBootstrapRuntimeHost(input:PackagedStartInput):Promise<HostedBootstrapRuntimeHost>{
  return startPackaged(input,assertIssuedPackagedReleaseBasisV2,startHostedPrivateBootstrapRuntimeHost);
}

/** Source-test seam. It is deliberately omitted from every package export surface and never issues a production-consumable basis. */
export function loadPackagedHostedReleaseBasisControlledForTests(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2},observe:typeof observeRuntimeSupportProfileV2,captureFailure?:(error:unknown)=>void,beforeFinalRevalidation?:()=>Promise<void>):Promise<HostedPackagedReleaseLoadResult>{return loadBasis(input,observe,"controlled-test",{captureFailure,beforeFinalRevalidation});}
export { isControlledPackagedReleaseBasisForTests } from "./hosted-packaged-release-state.js";
/** Native-free source-test seam. It is absent from package exports and cannot promote a controlled basis. */
export function startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests(input:PackagedStartInput,start:PrivateStarter):Promise<HostedBootstrapRuntimeHost>{
  return startPackaged(input,revalidateControlledPackagedReleaseBasisForTests,start);
}
