import { createHash } from "node:crypto";
import { constants } from "node:fs";
import { link, lstat, mkdir, open, realpath, rm } from "node:fs/promises";
import { dirname, isAbsolute, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";
import {
  matchRuntimeSupportProfileV2, observePackagedRuntimeBasisIdentityV2, observeRuntimeSupportProfileV2, verifyPackagedRuntimeBasisV2,
  type EmbeddedRuntimeVersionsV2, type RuntimeArtifactEntryV2, type RuntimeSupportProfileV2,
  type VerifiedPackagedRuntimeBasisV2
} from "@chirality/runtime-core/runtime-conformance-v2";
import { type HostedBootstrapRuntimeBootInput, type HostedBootstrapRuntimeHost } from "./hosted-bootstrap.js";
import { startHostedPrivateBootstrapRuntimeHost } from "./hosted-private-entry.js";
import type { RuntimeDaemonLogger } from "./runtime-daemon.js";
import { inspectRuntimePurposeAcceptanceV2,inspectRuntimePurposeReleaseV2 } from "./runtime-conformance-v2-admission.js";
import { inspectHostAccountSignedPeerIdentity, revalidateObservedSignedAppFiles, type VerifiedHostAccountPackagedIdentity } from "./host-account-release.js";

/**
 * Supplier request budget for the packaged release. The first `thread/start`
 * in a fresh Codex home runs schema migrations and MCP startup; a request
 * budget below that cost fails the session and revokes the account.
 */
export const PACKAGED_REQUEST_TIMEOUT_MS = 90_000;
/** Turn budget; expiry interrupts the turn through the provider rather than failing the session. */
export const PACKAGED_TURN_TIMEOUT_MS = 1_800_000;
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
  schema: "chirality-runtime-release-anchor/v2" | "chirality-runtime-release-anchor/v3";
  outerInventorySha256: string;
  login: HostedReleaseAnchorPurposeV2;
  worker: HostedReleaseAnchorPurposeV2;
  postSealObservationSha256?: string;
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
  const v3=!!value&&typeof value==="object"&&!Array.isArray(value)&&(value as Record<string,unknown>).schema==="chirality-runtime-release-anchor/v3";
  if(!exactKeys(value,v3?["schema","outerInventorySha256","login","worker","postSealObservationSha256"]:["schema","outerInventorySha256","login","worker"])
    ||!["chirality-runtime-release-anchor/v2","chirality-runtime-release-anchor/v3"].includes(String(value.schema))||!digest(value.outerInventorySha256)||(v3&&!digest(value.postSealObservationSha256)))throw unavailable("INVALID_RELEASE_ANCHOR");
  return {schema:value.schema as HostedReleaseAnchorV2["schema"],outerInventorySha256:value.outerInventorySha256,login:inspectPurpose(value.login),worker:inspectPurpose(value.worker),...(v3?{postSealObservationSha256:value.postSealObservationSha256 as string}:{})};
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

async function verifyPurposeAcceptance(input:{purpose:Purpose;basis:HostedPackagedPurposeBasisV2;payloadDigest:string;profile:RuntimeSupportProfileV2}):Promise<Readonly<{disposition:"qualified"|"local-human-trial";ownerReference:string}>>{
  const [recordSource,acceptanceSource,ownerAct]=await Promise.all([stablePrivateFile(input.basis.recordPath),stablePrivateFile(input.basis.acceptancePath),stablePrivateFile(input.basis.ownerActPath)]);
  if(recordSource.sha256!==input.basis.recordSha256||acceptanceSource.sha256!==input.basis.acceptanceSha256||ownerAct.sha256!==input.basis.ownerActSha256)throw unavailable("PRIVATE_RELEASE_SNAPSHOT_CHANGED");
  let record:unknown,acceptance:unknown;try{record=JSON.parse(recordSource.bytes.toString("utf8"));acceptance=JSON.parse(acceptanceSource.bytes.toString("utf8"));}catch{throw unavailable("PURPOSE_RELEASE_INVALID");}
  const inspected=inspectRuntimePurposeReleaseV2({purpose:input.purpose,record,expected:{payloadDigest:input.payloadDigest,supportProfile:input.profile}});
  const accepted=inspectRuntimePurposeAcceptanceV2({purpose:input.purpose,acceptance,expected:{recordSha256:recordSource.sha256,sourceDigest:inspected.sourceDigest,ownerActSha256:ownerAct.sha256,activationId:input.basis.activationId,gateIdentity:input.basis.gateIdentity}});
  return Object.freeze({disposition:inspected.disposition,ownerReference:accepted.ownerReference});
}
function deepFreeze<T>(value:T):Readonly<T>{if(value&&typeof value==="object"){for(const child of Object.values(value as Record<string,unknown>))deepFreeze(child);Object.freeze(value);}return value;}

type TrialSealInspector=(input:{executablePath:string;resourcesPath:string})=>Promise<VerifiedHostAccountPackagedIdentity>;
async function inspectTrialSeal(input:{path:string;expectedSha256:string;outerInventorySha256:string;payloadDigest:string;executablePath:string;resourcesPath:string},inspect:TrialSealInspector){
  const source=await stablePrivateFile(input.path);
  if(source.sha256!==input.expectedSha256)throw unavailable("TRIAL_SEAL_OBSERVATION_CHANGED");
  let value:unknown;try{value=JSON.parse(source.bytes.toString("utf8"));}catch{throw unavailable("TRIAL_SEAL_OBSERVATION_INVALID");}
  const names=["signed-app","fuses-and-asar","signed-peer-identity-binding"] as const;
  if(!exactKeys(value,["schema","outerInventorySha256","payloadDigest","mainCodeDirectoryHash","peerRequirementSha256","checks"])
    ||value.schema!=="chirality-runtime-trial-seal-observation/v1"||value.outerInventorySha256!==input.outerInventorySha256||value.payloadDigest!==input.payloadDigest
    ||typeof value.mainCodeDirectoryHash!=="string"||!/^[a-f0-9]{40}$/.test(value.mainCodeDirectoryHash)||!digest(value.peerRequirementSha256)||!exactKeys(value.checks,names))throw unavailable("TRIAL_SEAL_OBSERVATION_INVALID");
  for(const name of names){const check=value.checks[name];if(!exactKeys(check,["attempted","passed","evidenceSha256"])||check.attempted!==true||check.passed!==true||!digest(check.evidenceSha256))throw unavailable("TRIAL_SEAL_OBSERVATION_INVALID");}
  const identity=await inspect({executablePath:input.executablePath,resourcesPath:input.resourcesPath});
  if(value.mainCodeDirectoryHash!==identity.subject.cdHash||value.peerRequirementSha256!==hash(identity.effectivePeerRequirement))throw unavailable("TRIAL_SEAL_SUBJECT_MISMATCH");
  return Object.freeze({observation:Object.freeze({path:input.path,sha256:source.sha256,mainCodeDirectoryHash:value.mainCodeDirectoryHash,peerRequirementSha256:value.peerRequirementSha256}),observedFiles:Object.freeze([...(identity.observedFiles??[])])});
}

async function loadBasis(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2;executablePath?:string},observe:typeof observeRuntimeSupportProfileV2,issuance:"production"|"controlled-test",hooks?:{captureFailure?:(error:unknown)=>void;beforeFinalRevalidation?:()=>Promise<void>;inspectSignedPeerIdentity?:TrialSealInspector}):Promise<HostedPackagedReleaseLoadResult>{
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
      try{const observed=await observe({embeddedRuntime:input.embeddedRuntime,basis:verified,supplierVersion:candidate.supplier.version,appServerProtocolDigest:candidate.supplier.appServerProtocolDigest,immutableSystemRoots:candidate.immutableSystemRoots,nativePolicyIdentityVersion:candidate.compiler.nativePolicyIdentityVersion});if(observed.profileDigest===candidate.profileDigest)observedCandidates.push(observed);}catch{}
    }
    if(observedCandidates.length!==1)throw unavailable("UNSUPPORTED_RUNTIME");
    const supportProfile=matchRuntimeSupportProfileV2(observedCandidates[0]!,verified.payload.supportProfiles);
    const basisDigest=hash(JSON.stringify({anchorSha256:anchorSource.sha256,inventorySha256:verified.inventorySha256,payloadDigest:verified.payloadDigest,profileDigest:supportProfile.profileDigest}));
    const releaseBasisRoot=join(input.runtimeDirectory,"release-basis");await ensurePrivateDirectoryExact(releaseBasisRoot);const snapshotRoot=join(releaseBasisRoot,basisDigest);await ensurePrivateDirectoryExact(snapshotRoot);await assertPrivateChain(input.runtimeDirectory,snapshotRoot);
    const login=await snapshotPurpose({resourcesRoot:verified.resourcesRoot,snapshotRoot,purpose:"login",anchor:anchor.login,entries:verified.inventory.governance});
    const worker=await snapshotPurpose({resourcesRoot:verified.resourcesRoot,snapshotRoot,purpose:"worker",anchor:anchor.worker,entries:verified.inventory.governance});
    const loginRelease=await verifyPurposeAcceptance({purpose:"login",basis:login,payloadDigest:verified.payloadDigest,profile:supportProfile});
    const workerRelease=await verifyPurposeAcceptance({purpose:"worker",basis:worker,payloadDigest:verified.payloadDigest,profile:supportProfile});
    if(loginRelease.disposition!=="qualified"||(anchor.schema==="chirality-runtime-release-anchor/v3")!==(workerRelease.disposition==="local-human-trial"))throw unavailable("RELEASE_DISPOSITION_MISMATCH");
    const observationPath=join(anchorRoot,"trial-seal-observation.json"),inspect=hooks?.inspectSignedPeerIdentity??inspectHostAccountSignedPeerIdentity;
    const trialSealObservation=workerRelease.disposition==="local-human-trial"
      ? (await inspectTrialSeal({path:observationPath,expectedSha256:anchor.postSealObservationSha256!,outerInventorySha256:verified.inventorySha256,payloadDigest:verified.payloadDigest,executablePath:input.executablePath??"",resourcesPath:verified.resourcesRoot},inspect)).observation
      : undefined;
    await hooks?.beforeFinalRevalidation?.();
    // The payload bytes were hashed once above. The final pass rechecks every packaged entry by filesystem identity
    // only, the same boundary the issued-basis registry applies afterwards; the bundle's code signature carries byte integrity.
    const finalAnchor=await stablePrivateFile(anchorPath);
    if(finalAnchor.sha256!==anchorSource.sha256||await observePackagedRuntimeBasisIdentityV2(verified)!==verified.identityDigest)throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
    const finalVerified=verified;
    const finalLogin=await snapshotPurpose({resourcesRoot:finalVerified.resourcesRoot,snapshotRoot,purpose:"login",anchor:anchor.login,entries:finalVerified.inventory.governance}),finalWorker=await snapshotPurpose({resourcesRoot:finalVerified.resourcesRoot,snapshotRoot,purpose:"worker",anchor:anchor.worker,entries:finalVerified.inventory.governance});
    if(JSON.stringify(finalLogin)!==JSON.stringify(login)||JSON.stringify(finalWorker)!==JSON.stringify(worker))throw unavailable("PACKAGED_RELEASE_BASIS_CHANGED");
    const finalLoginRelease=await verifyPurposeAcceptance({purpose:"login",basis:finalLogin,payloadDigest:finalVerified.payloadDigest,profile:supportProfile});const finalWorkerRelease=await verifyPurposeAcceptance({purpose:"worker",basis:finalWorker,payloadDigest:finalVerified.payloadDigest,profile:supportProfile});
    if(finalLoginRelease.disposition!==loginRelease.disposition||finalWorkerRelease.disposition!==workerRelease.disposition)throw unavailable("RELEASE_DISPOSITION_CHANGED");
    const finalTrialSeal=trialSealObservation?await inspectTrialSeal({path:observationPath,expectedSha256:anchor.postSealObservationSha256!,outerInventorySha256:finalVerified.inventorySha256,payloadDigest:finalVerified.payloadDigest,executablePath:input.executablePath!,resourcesPath:finalVerified.resourcesRoot},inspect):undefined;
    const finalTrialSealObservation=finalTrialSeal?.observation;
    if(JSON.stringify(finalTrialSealObservation??null)!==JSON.stringify(trialSealObservation??null))throw unavailable("TRIAL_SEAL_OBSERVATION_CHANGED");
    const basis=deepFreeze(structuredClone({schema:"chirality-hosted-packaged-release-basis/v2" as const,basisDigest,verified:finalVerified,supportProfile,instructionRoot:join(verified.resourcesRoot,"instruction-root"),nativeAddonPath:join(verified.resourcesRoot,"native/chirality_native_admission.node"),supplierExecutablePath:join(verified.resourcesRoot,"supplier/codex"),preNativeFilesystemObservation:{runtimeDirectory:input.runtimeDirectory,anchorRoot,evidence:"canonical-owner-mode-chain-observed" as const},login:finalLogin,worker:finalWorker,workerDisposition:workerRelease.disposition,...(finalTrialSealObservation?{trialSealObservation:finalTrialSealObservation}:{})}));
    // Single-boundary trial-seal revalidation: the signed-app inspection (codesign, fuses, asar) ran at issuance; afterwards the
    // small observation record is re-read and every signed-app file it was bound to is compared by filesystem identity.
    const revalidateTrialSeal=finalTrialSeal?async()=>{
      const current=await stablePrivateFile(observationPath);if(current.sha256!==finalTrialSeal.observation.sha256)throw unavailable("TRIAL_SEAL_OBSERVATION_CHANGED");
      await revalidateObservedSignedAppFiles(finalTrialSeal.observedFiles,"TRIAL_SEAL_SUBJECT_CHANGED");
    }:undefined;
    await registerIssuedPackagedReleaseBasisV2(basis,{issuance,resourcesRoot:finalVerified.resourcesRoot,runtimeDirectory:input.runtimeDirectory,anchorRoot,anchorPath,anchorSha256:finalAnchor.sha256,
      inventorySha256:finalVerified.inventorySha256,payloadDigest:finalVerified.payloadDigest,profileDigest:supportProfile.profileDigest,basisDigest,login:basis.login,worker:basis.worker,workerDisposition:basis.workerDisposition,...(basis.trialSealObservation?{trialSealObservation:basis.trialSealObservation,revalidateTrialSeal}:{})});
    return {status:"ready",basis};
  }catch(error){
    hooks?.captureFailure?.(error);
    const code=(error as NodeJS.ErrnoException).code;if(code==="ENOENT")return {status:"unavailable",reason:"missing-release-basis"};
    const reason=(error as RuntimeError).details?.reason;return {status:"unavailable",reason:reason==="UNSUPPORTED_RUNTIME"?"unsupported-runtime":"invalid-release-basis"};
  }
}

/** Pure filesystem/support verification. It must complete before any native addon or XPC authority mechanism is loaded. */
export function loadPackagedHostedReleaseBasis(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2;executablePath?:string}):Promise<HostedPackagedReleaseLoadResult>{return loadBasis(input,observeRuntimeSupportProfileV2,"production");}

type PackagedStartInput={bootstrap:BootstrapEnabled;basis:Readonly<HostedPackagedReleaseBasisV2>;executablePath:string;/** Host diagnostic sink forwarded unchanged to the private entry; absent means discarded. */logger?:RuntimeDaemonLogger};
type PrivateStarter=(input:Parameters<typeof startHostedPrivateBootstrapRuntimeHost>[0])=>Promise<HostedBootstrapRuntimeHost>;
async function startPackaged(input:PackagedStartInput,revalidate:(basis:Readonly<HostedPackagedReleaseBasisV2>)=>Promise<void>|void,start:PrivateStarter):Promise<HostedBootstrapRuntimeHost>{
  if(!input||input.bootstrap?.enabled!==true||!input.basis||typeof input.basis!=="object")throw unavailable("PACKAGED_BOOTSTRAP_BASIS_MISMATCH");
  if(!canonical(input.executablePath))throw unavailable("PACKAGED_BOOTSTRAP_BASIS_MISMATCH");
  await revalidate(input.basis);
  if(input.basis.supportProfile.compiler.nativePolicyIdentityVersion!==11)throw unavailable("STAGE_C_COMPILER_UNAVAILABLE");
  if(input.bootstrap.runtimeDirectory!==dirname(dirname(dirname(input.basis.login.recordPath)))||input.bootstrap.instructionRoot!==input.basis.instructionRoot||input.bootstrap.nativeAddonPath!==input.basis.nativeAddonPath)throw unavailable("PACKAGED_BOOTSTRAP_BASIS_MISMATCH");
  return start({bootstrap:{...input.bootstrap,artifactInventory:undefined},...(input.logger===undefined?{}:{logger:input.logger}),privateComposition:{runtimeDirectory:input.bootstrap.runtimeDirectory,
    supplierExecutablePath:input.basis.supplierExecutablePath,nativeAddonPath:input.basis.nativeAddonPath,instructionRoot:input.basis.instructionRoot,
    compatibility:{compatibilityIdentity:"root-runtime-1",contractBasisSha256:"6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2"},
    commandNetworkPosture:"off",protectedPaths:[input.bootstrap.runtimeDirectory,join(input.bootstrap.runtimeDirectory,"release-authority"),join(input.bootstrap.runtimeDirectory,"release-basis")],
    immutableReadRoots:[...input.basis.supportProfile.immutableSystemRoots],requestTimeoutMs:PACKAGED_REQUEST_TIMEOUT_MS,turnTimeoutMs:PACKAGED_TURN_TIMEOUT_MS,releaseV2:{basis:input.basis},hostAccount:{executablePath:input.executablePath,resourcesPath:input.basis.verified.resourcesRoot}}});
}

/** Packaged startup consumes only a current loader-issued basis and derives the fixed private v2 composition. */
export function startHostedPackagedPrivateBootstrapRuntimeHost(input:PackagedStartInput):Promise<HostedBootstrapRuntimeHost>{
  return startPackaged(input,assertIssuedPackagedReleaseBasisV2,startHostedPrivateBootstrapRuntimeHost);
}

/** Source-test seam. It is deliberately omitted from every package export surface and never issues a production-consumable basis. */
export function loadPackagedHostedReleaseBasisControlledForTests(input:{resourcesRoot:string;runtimeDirectory:string;embeddedRuntime:EmbeddedRuntimeVersionsV2;executablePath?:string},observe:typeof observeRuntimeSupportProfileV2,captureFailure?:(error:unknown)=>void,beforeFinalRevalidation?:()=>Promise<void>,inspectSignedPeerIdentity?:TrialSealInspector):Promise<HostedPackagedReleaseLoadResult>{return loadBasis(input,observe,"controlled-test",{captureFailure,beforeFinalRevalidation,inspectSignedPeerIdentity});}
export { isControlledPackagedReleaseBasisForTests } from "./hosted-packaged-release-state.js";
/** Native-free source-test seam. It is absent from package exports and cannot promote a controlled basis. */
export function startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests(input:PackagedStartInput,start:PrivateStarter):Promise<HostedBootstrapRuntimeHost>{
  return startPackaged(input,revalidateControlledPackagedReleaseBasisForTests,start);
}
