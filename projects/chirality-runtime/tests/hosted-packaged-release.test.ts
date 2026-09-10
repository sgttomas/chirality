import { createHash } from "node:crypto";
import { chmod, cp, mkdir, mkdtemp, readFile, readdir, realpath, rename, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { request as httpRequest } from "node:http";
import { afterEach, describe, expect, it, vi } from "vitest";
import {
  compareRuntimeUtf8V2, encodeRuntimeArtifactInventoryV2, encodeRuntimePayloadManifestV2,
  encodeRuntimePolicyParameterDeclarationV2, runtimePolicyParameterSchemaDigestV2, runtimeStageCPolicyParameterSchemaDigest,
  type RuntimeArtifactInventoryV2, type RuntimePayloadEntryV2, type RuntimePayloadManifestV2,
  type RuntimeSupportProfileV2
} from "../packages/core/src/runtime-conformance-v2.js";
import {
  isControlledPackagedReleaseBasisForTests, loadPackagedHostedReleaseBasis,
  loadPackagedHostedReleaseBasisControlledForTests, startHostedPackagedPrivateBootstrapRuntimeHost,
  startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests
} from "../packages/daemon/src/hosted-packaged-release.js";
import { revalidateControlledPackagedReleaseBasisForTests } from "../packages/daemon/src/hosted-packaged-release-state.js";
import { validateHostedPrivateCompositionOptions } from "../packages/daemon/src/hosted-private-composition.js";
import { RuntimeError } from "../packages/contracts/src/errors.js";
import { RuntimeClient } from "../packages/client/src/client.js";
import { createFakeRuntimeAdmissionNativeAdapter } from "../packages/core/src/runtime-admission-lock.js";
import { startControlledHostedBootstrapRuntimeHostForTests } from "../packages/daemon/src/hosted-bootstrap.js";
import { startControlledHostedPrivateBootstrapRuntimeHostForTests } from "../packages/daemon/src/hosted-private-entry.js";
import { createControlledHostedBootstrapPrivateBindingsForTests, type ControlledHostedPrivateCompositionAdapters } from "../packages/daemon/src/hosted-private-composition.js";
import { HostAccountAuthority } from "../packages/daemon/src/host-account-authority.js";
import { MainHostAccountClient, type HostAccountClientNativeAdmission } from "../packages/daemon/src/host-account-client.js";
import { createHostAccountRequestProof, hostAccountBodyDigest, hostAccountRequest } from "../packages/daemon/src/host-account-protocol.js";

const roots:string[]=[];const sha=(value:string|Buffer)=>createHash("sha256").update(value).digest("hex");
const file=(relativePath:string,bytes:Buffer)=>({relativePath,size:bytes.length,sha256:sha(bytes)});
const appExecutable=(resources:string)=>join(resources,"..","MacOS","Chirality");
async function rawAccountRequest(socketPath:string,path:string,headers:Record<string,string>,body=""):Promise<number>{return new Promise((resolve,reject)=>{const request=httpRequest({socketPath,path,method:body?"POST":"GET",headers},response=>{response.resume();response.on("end",()=>resolve(response.statusCode??0));});request.on("error",reject);if(body)request.write(body);request.end();});}
function support(entries:RuntimePayloadEntryV2[],nativePolicyIdentityVersion:10|11=11):RuntimeSupportProfileV2{
  const map=new Map(entries.filter((entry):entry is Extract<RuntimePayloadEntryV2,{type:"file"}>=>entry.type==="file").map(entry=>[entry.relativePath,entry]));
  const without={schema:"chirality-runtime-support-profile/v2" as const,macosProductVersion:"26.6.2",macosBuildVersion:"25G83",architecture:"arm64" as const,electronVersion:"43.2.0",nodeVersion:"24.13.0",nodeModuleAbi:"145",napiVersion:"10",osMeasurement:{executablePath:"/usr/bin/sw_vers" as const,executableSha256:sha("sw"),executableSize:2},sandboxExec:{path:"/usr/bin/sandbox-exec" as const,sha256:sha("sandbox"),size:7},nativeAdmission:{contract:"chirality-native-admission/v1" as const,sha256:map.get("native/chirality_native_admission.node")!.sha256,size:map.get("native/chirality_native_admission.node")!.size,napiVersion:"6"},supplier:{version:"1.2.3",sha256:map.get("supplier/codex")!.sha256,size:map.get("supplier/codex")!.size,appServerProtocolDigest:sha("protocol"),authorityContract:"chirality.local-admission-authority/1.0" as const,identityContract:"chirality-supplier-account-identity/1" as const},compiler:{outerPolicySchema:"chirality-codex-outer-policy/v2" as const,nativePolicyIdentityVersion,sourceDigest:sha("compiler"),parameterSchemaDigest:nativePolicyIdentityVersion===11?runtimeStageCPolicyParameterSchemaDigest():runtimePolicyParameterSchemaDigestV2()},immutableSystemRoots:["/System","/usr"],kernelHelperContractDigest:sha("kernel")};return {...without,profileDigest:sha(`${JSON.stringify(without)}\n`)};
}
async function createFixture(nativePolicyIdentityVersion:10|11=11){
  const base=await realpath(await mkdtemp(join(tmpdir(),"hosted-v2-")));roots.push(base);const resources=join(base,"Resources"),runtime=join(base,"runtime");await mkdir(resources);await mkdir(runtime,{mode:0o700});
  const files=new Map<string,Buffer>([["app.asar",Buffer.from("app")],["instruction-root/instruction-bundle-manifest.json",Buffer.from("bundle")],["native/chirality_native_admission.node",Buffer.from("native")],["runtime-cli/chirality-cli.mjs",Buffer.from("cli")],["runtime-cli/chirality-cli.mjs.map",Buffer.from("map")],["runtime-contracts/runtime-policy-parameters-v2.json",encodeRuntimePolicyParameterDeclarationV2()],["runtime-contracts/host-account-signing-predicate.json",Buffer.from(JSON.stringify({schema:"chirality.host-account-signing-predicate/v1",serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"TESTTEAM01",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'}))],["supplier/codex",Buffer.from("supplier")]]);
  for(const [path,bytes]of files){await mkdir(join(resources,path,".."),{recursive:true});await writeFile(join(resources,path),bytes);}
  await chmod(join(resources,"supplier/codex"),0o700);
  const entries:RuntimePayloadEntryV2[]=[...["instruction-root","native","runtime-cli","runtime-contracts","supplier"].map(relativePath=>({relativePath,type:"directory" as const})),...[...files].map(([relativePath,bytes])=>({...file(relativePath,bytes),type:"file" as const}))].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath));
  const profile=support(entries,nativePolicyIdentityVersion),manifest:RuntimePayloadManifestV2={schema:"chirality-runtime-payload-manifest/v2",dependencyResolutionDigest:sha("deps"),roots:["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"].sort(compareRuntimeUtf8V2),supportProfiles:[profile],entries};
  const manifestBytes=encodeRuntimePayloadManifestV2(manifest);await writeFile(join(resources,"runtime-payload-manifest.json"),manifestBytes);
  const owner=Buffer.from("owner-act"),supplyDigest=sha(`${JSON.stringify(profile.supplier)}\n`),limb=(names:readonly string[])=>Object.fromEntries(names.map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]));
  const common={sourceDigest:profile.compiler.sourceDigest,payloadDigest:sha(manifestBytes),supportProfileDigests:[profile.profileDigest],policyContractDigest:profile.compiler.parameterSchemaDigest,supplyProfileDigest:supplyDigest,issuedAt:new Date(Date.now()-1000).toISOString(),expiresAt:new Date(Date.now()+60_000).toISOString()};
  const loginRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-login-purpose-release/v2",evidenceClass:"exact-account-free-login-purpose-observed",...common,backend:{credentialStore:"keyring",plaintextFallback:false},methods:["account/login/start","account/login/cancel","account/read","model/list"],modelExecution:false,limbs:limb(["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"])}));
  const workerNames=["effective-policy","primary.read","primary.file-change","primary.shell-write","primary.network","primary.process","primary.environment","primary.approval","primary.role","descendant.read","descendant.file-change","descendant.shell-write","descendant.network","descendant.process","descendant.environment","descendant.approval","descendant.role","owner-live-native-delegation"];
  const workerRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-worker-purpose-release/v2",evidenceClass:"exact-worker-purpose-observed",...common,limbs:limb(workerNames)}));
  const acceptance=(record:Buffer,gateIdentity:string)=>Buffer.from(JSON.stringify({schema:"chirality-runtime-conformance-acceptance/v1",status:"accepted",recordSha256:sha(record),sourceDigest:profile.compiler.sourceDigest,activationId:"release-v2",gateIdentity,ownerActSha256:sha(owner),ownerReference:"owner-act",expiresAt:new Date(Date.now()+60_000).toISOString()}));
  const loginAcceptance=acceptance(loginRecord,"D36"),workerAcceptance=acceptance(workerRecord,"WORKER-V2");
  const governance=new Map<string,Buffer>([["runtime-governance/v2/login-purpose-record.json",loginRecord],["runtime-governance/v2/login-purpose-acceptance.json",loginAcceptance],["runtime-governance/v2/login-owner-act",owner],["runtime-governance/v2/worker-purpose-record.json",workerRecord],["runtime-governance/v2/worker-purpose-acceptance.json",workerAcceptance],["runtime-governance/v2/worker-owner-act",owner]]);
  for(const[path,bytes]of governance){await mkdir(join(resources,path,".."),{recursive:true});await writeFile(join(resources,path),bytes);}
  const inventory:RuntimeArtifactInventoryV2={schema:"chirality-runtime-artifact-inventory/v2",payloadManifest:file("runtime-payload-manifest.json",manifestBytes) as RuntimeArtifactInventoryV2["payloadManifest"],governance:[...governance].map(([path,bytes])=>file(path,bytes)) as unknown as RuntimeArtifactInventoryV2["governance"]};
  const inventoryBytes=encodeRuntimeArtifactInventoryV2(inventory);await writeFile(join(resources,"runtime-artifact-inventory-v2.json"),inventoryBytes);
  const anchorRoot=join(runtime,"release-authority","v2");await mkdir(anchorRoot,{recursive:true,mode:0o700});await chmod(join(runtime,"release-authority"),0o700);await chmod(anchorRoot,0o700);
  const anchor={schema:"chirality-runtime-release-anchor/v2",outerInventorySha256:sha(inventoryBytes),login:{recordSha256:sha(loginRecord),acceptanceSha256:sha(loginAcceptance),ownerActSha256:sha(owner),activationId:"release-v2",gateIdentity:"D36"},worker:{recordSha256:sha(workerRecord),acceptanceSha256:sha(workerAcceptance),ownerActSha256:sha(owner),activationId:"release-v2",gateIdentity:"WORKER-V2"}};
  await writeFile(join(anchorRoot,"release-anchor.json"),JSON.stringify(anchor),{mode:0o600});await chmod(join(anchorRoot,"release-anchor.json"),0o600);
  return {resources,runtime,profile,common,workerNames,owner,inventory,anchor};
}
afterEach(async()=>{vi.restoreAllMocks();while(roots.length)await rm(roots.pop()!,{recursive:true,force:true});});

describe("packaged hosted release basis",()=>{
  it("loads the complete accepted filesystem basis through the isolated support observer",async()=>{
    const fixture=await createFixture(),observe=vi.fn(async()=>fixture.profile);
    let failure:unknown;const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},observe,error=>{failure=error;});
    if(result.status!=="ready")throw failure;
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    expect(observe).toHaveBeenCalledOnce();expect(observe).toHaveBeenCalledWith(expect.objectContaining({nativePolicyIdentityVersion:11}));expect(isControlledPackagedReleaseBasisForTests(result.basis)).toBe(true);expect(Object.isFrozen(result.basis.verified.payload.entries)).toBe(true);expect(Object.isFrozen(result.basis.login)).toBe(true);
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({bootstrap:{enabled:true,runtimeDirectory:fixture.runtime,daemonSocket:join(fixture.runtime,"daemon.sock"),instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath},basis:result.basis,executablePath:appExecutable(fixture.resources)})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });
  it("keeps a valid historical native-10 profile readable but unavailable for Stage C startup",async()=>{
    const fixture=await createFixture(10),observe=vi.fn(async()=>fixture.profile);
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},observe);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    expect(observe).toHaveBeenCalledWith(expect.objectContaining({nativePolicyIdentityVersion:10}));
    const start=vi.fn();
    await expect(startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests({bootstrap:{enabled:true,runtimeDirectory:fixture.runtime,daemonSocket:join(fixture.runtime,"daemon.sock"),instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath},basis:result.basis,executablePath:appExecutable(fixture.resources)},start)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE",details:{reason:"STAGE_C_COMPILER_UNAVAILABLE"}});
    expect(start).not.toHaveBeenCalled();
  });
  it("retains and revalidates the signed-peer observation for one worker trial basis",async()=>{
    const fixture=await createFixture();
    const workerRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-worker-purpose-release/v3",evidenceClass:"exact-local-human-trial-authorized",...fixture.common,trialScope:"local-human-functional-trial",
      limbs:Object.fromEntries(fixture.workerNames.map(name=>[name,{status:"pending-human-trial"}])),prerequisites:Object.fromEntries(["signed-payload-and-supply","trusted-app-and-account-host","native-enforcement-and-retirement","connected-source-contract"].map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]))}));
    const workerAcceptance=Buffer.from(JSON.stringify({schema:"chirality-runtime-conformance-acceptance/v1",status:"accepted",recordSha256:sha(workerRecord),sourceDigest:fixture.profile.compiler.sourceDigest,activationId:"release-v2",gateIdentity:"WORKER-V2",ownerActSha256:sha(fixture.owner),ownerReference:"trial-owner-act",expiresAt:new Date(Date.now()+60_000).toISOString()}));
    await writeFile(join(fixture.resources,"runtime-governance/v2/worker-purpose-record.json"),workerRecord);await writeFile(join(fixture.resources,"runtime-governance/v2/worker-purpose-acceptance.json"),workerAcceptance);
    const governance=fixture.inventory.governance.map(entry=>entry.relativePath.endsWith("worker-purpose-record.json")?file(entry.relativePath,workerRecord):entry.relativePath.endsWith("worker-purpose-acceptance.json")?file(entry.relativePath,workerAcceptance):entry) as RuntimeArtifactInventoryV2["governance"];
    const inventoryBytes=encodeRuntimeArtifactInventoryV2({...fixture.inventory,governance});await writeFile(join(fixture.resources,"runtime-artifact-inventory-v2.json"),inventoryBytes);
    const effectivePeerRequirement='(identifier "com.chirality.app" and anchor apple generic) and cdhash H"1234567890abcdef1234567890abcdef12345678"';
    const observation=Buffer.from(JSON.stringify({schema:"chirality-runtime-trial-seal-observation/v1",outerInventorySha256:sha(inventoryBytes),payloadDigest:fixture.common.payloadDigest,mainCodeDirectoryHash:"1234567890abcdef1234567890abcdef12345678",peerRequirementSha256:sha(effectivePeerRequirement),checks:Object.fromEntries(["signed-app","fuses-and-asar","signed-peer-identity-binding"].map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]))}));
    const anchorRoot=join(fixture.runtime,"release-authority","v2");await writeFile(join(anchorRoot,"trial-seal-observation.json"),observation,{mode:0o600});await chmod(join(anchorRoot,"trial-seal-observation.json"),0o600);
    const anchor={...fixture.anchor,schema:"chirality-runtime-release-anchor/v3",outerInventorySha256:sha(inventoryBytes),worker:{...fixture.anchor.worker,recordSha256:sha(workerRecord),acceptanceSha256:sha(workerAcceptance)},postSealObservationSha256:sha(observation)};
    await writeFile(join(anchorRoot,"release-anchor.json"),JSON.stringify(anchor),{mode:0o600});
    const inspect=vi.fn(async()=>({schema:"chirality.host-account-signed-peer-identity-binding/v1" as const,predicate:{} as any,effectivePeerRequirement,subject:{path:appExecutable(fixture.resources),cdHash:"1234567890abcdef1234567890abcdef12345678",designatedRequirement:"designated",identifier:"com.chirality.app",teamIdentifier:"TESTTEAM01"},outer:{path:join(fixture.resources,"..",".."),cdHash:"1234567890abcdef1234567890abcdef12345678",designatedRequirement:"designated",identifier:"com.chirality.app",teamIdentifier:"TESTTEAM01"},fuses:"electron-runtime-fuses-verified" as const,asarIntegrity:"electron-asar-integrity-verified" as const}));
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,executablePath:appExecutable(fixture.resources),embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile,undefined,undefined,inspect);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    expect(result.basis.workerDisposition).toBe("local-human-trial");expect(result.basis.trialSealObservation).toMatchObject({sha256:sha(observation),mainCodeDirectoryHash:"1234567890abcdef1234567890abcdef12345678"});
    await revalidateControlledPackagedReleaseBasisForTests(result.basis);expect(inspect).toHaveBeenCalledTimes(4);
    await writeFile(join(anchorRoot,"trial-seal-observation.json"),"changed",{mode:0o600});
    await expect(revalidateControlledPackagedReleaseBasisForTests(result.basis)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });
  it("keeps a missing fixed anchor coarse on controlled and production paths",async()=>{
    const fixture=await createFixture();await rm(join(fixture.runtime,"release-authority","v2","release-anchor.json"));
    const input={resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"} as const};
    await expect(loadPackagedHostedReleaseBasisControlledForTests(input,async()=>fixture.profile)).resolves.toEqual({status:"unavailable",reason:"missing-release-basis"});
    await expect(loadPackagedHostedReleaseBasis(input)).resolves.toEqual({status:"unavailable",reason:"missing-release-basis"});
  });
  it("derives the fixed private v2 composition from the same nominal basis before the absent authority gate",async()=>{
    const fixture=await createFixture();
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    let observed:Parameters<typeof validateHostedPrivateCompositionOptions>[0];
    const bootstrap={enabled:true as const,runtimeDirectory:fixture.runtime,daemonSocket:join(fixture.runtime,"daemon.sock"),instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath};
    await expect(startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests({bootstrap,basis:result.basis,executablePath:appExecutable(fixture.resources)},async input=>{
      observed=validateHostedPrivateCompositionOptions(input.privateComposition);
      throw new RuntimeError("ENGINE_UNAVAILABLE","Host account authority is unavailable",503);
    })).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    const composition=observed as ReturnType<typeof validateHostedPrivateCompositionOptions>;
    expect(composition.releaseV2?.basis).toBe(result.basis);
    expect(composition.hostAccount).toEqual({executablePath:appExecutable(fixture.resources),resourcesPath:fixture.resources});
    expect(composition).toMatchObject({runtimeDirectory:fixture.runtime,supplierExecutablePath:result.basis.supplierExecutablePath,nativeAddonPath:result.basis.nativeAddonPath,
      instructionRoot:result.basis.instructionRoot,commandNetworkPosture:"off",compatibility:{compatibilityIdentity:"root-runtime-1",contractBasisSha256:"6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2"},turnTimeoutMs:600_000});
    expect(composition).not.toHaveProperty("model");expect(composition).not.toHaveProperty("consentVersion");expect(composition).not.toHaveProperty("managedAuth");
  });
  it.each([undefined, {}, { login: {} }, { schema: "chirality-hosted-packaged-release-basis/v2", login: { recordPath: "/fabricated" } }])("rejects malformed or fabricated packaged starter basis coarsely", async basis => {
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({ bootstrap: { enabled: true, runtimeDirectory: "/runtime", daemonSocket: "runtime.sock", instructionRoot: "/instructions", nativeAddonPath: "/native.node" }, basis: basis as any, executablePath: "/Applications/Chirality.app/Contents/MacOS/Chirality" })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("connects one main client ceremony and signed HTTP account path to the packaged daemon",async()=>{
    const fixture=await createFixture(),projectRoot=join(fixture.runtime,"..","project");await mkdir(projectRoot,{mode:0o700});
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    const lease=createFakeRuntimeAdmissionNativeAdapter().acquire(fixture.runtime,"controlled-release.lock"),stageSupplier=vi.fn(async()=>{throw new Error("supplier staging must remain unreachable");});
    const unreachable=async()=>{throw new Error("downstream private effect must remain unreachable");};
    let serverCallbacks:any,clientCallbacks:any,observedNonce:Buffer|undefined,observedGrant:any;
    const createServer=vi.fn((input:any)=>{serverCallbacks=input;return{ping:async(_connectionId:string,value:{requestId:string;sequence:bigint})=>value,closeConnection:async()=>{},close:async()=>{}}});
    const adapters:ControlledHostedPrivateCompositionAdapters={revalidateReleaseBasis:revalidateControlledPackagedReleaseBasisForTests,
      createAccountHost:async auth=>new HostAccountAuthority({runtimeDirectory:fixture.runtime,auth,expectedEuid:process.geteuid?.()??process.getuid?.()??0,
        signingPredicate:{schema:"chirality.host-account-signing-predicate/v1",serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"ABCDEFGHIJ",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'},
        nativeAdmission:{createHostXpcServer:createServer}}),acquireLease:async()=>lease,stageSupplier,
      prepareNativeRoles:unreachable,bindRuntimeReadRoot:unreachable,validateLoginStartup:unreachable,createLogin:()=>{throw new Error("login creation must remain unreachable");},preparePolicy:unreachable,
      createLauncherFactory:()=>{throw new Error("launcher creation must remain unreachable");},admitHosted:unreachable,logout:unreachable,openBindingStore:unreachable};
    const bootstrap={enabled:true as const,runtimeDirectory:fixture.runtime,daemonSocket:"control.sock",instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath};
    let privateFailure:unknown;
    const host=await startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests({bootstrap,basis:result.basis,executablePath:appExecutable(fixture.resources)},input=>startControlledHostedPrivateBootstrapRuntimeHostForTests(input,{
      createBindings:async options=>{const bindings=await createControlledHostedBootstrapPrivateBindingsForTests(options,adapters);return Object.freeze({...bindings,async createCeremony(ceremonyInput){try{return await bindings.createCeremony(ceremonyInput);}catch(error){privateFailure=error;throw error;}}});},
      startHost:(boot,bindings)=>startControlledHostedBootstrapRuntimeHostForTests(boot,bindings!)
    }));
    try{
      const legacy=new RuntimeClient({socketPath:host.socketPath,tokenFile:host.bootstrapTokenFile}),registered=await legacy.initializeHostedBootstrapProject({projectRoot});
      for(const request of [
        ()=>legacy.hostedBootstrapStatus(registered.projectId),
        ()=>legacy.grantHostedProviderNetworkConsent(registered.projectId),
        ()=>legacy.startHostedBootstrapLogin(registered.projectId),
        ()=>legacy.cancelHostedBootstrapLogin(registered.projectId),
        ()=>legacy.signOutHostedProject(registered.projectId)
      ]) await expect(request()).rejects.toMatchObject({code:"UNAUTHORIZED"});
      await expect(rawAccountRequest(host.socketPath,hostAccountRequest("status",registered.projectId).route,{"x-chirality-account-proof":"partial"})).resolves.toBe(401);
      const nativeAdmission:HostAccountClientNativeAdmission={createHostXpcClient(input){clientCallbacks=input;return{
        async provision(request){const challenge=await serverCallbacks.onCeremonyOpen({connectionId:"same-socket",requestId:request.requestId});const finish=await request.onChallenge(challenge);observedNonce=Buffer.from(finish.hostNonce);observedGrant=await serverCallbacks.onCeremonyFinish({connectionId:"same-socket",...finish});return{...observedGrant,bearer:Buffer.from(observedGrant.bearer)};},
        async close(){await serverCallbacks.onInvalidated({connectionId:"same-socket",reason:"invalidated"});}
      };}};
      const client=new MainHostAccountClient({socketPath:host.socketPath,signingPredicate:{schema:"chirality.host-account-signing-predicate/v1",serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"ABCDEFGHIJ",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'},expectedEuid:process.geteuid?.()??process.getuid?.()??0,nativeAdmission});
      await client.start();
      await expect(client.status(registered.projectId)).resolves.toMatchObject({projectId:registered.projectId,ceremony:"consent-required"});
      await expect(client.grantProviderNetworkConsent(registered.projectId)).resolves.toMatchObject({projectId:registered.projectId,ceremony:"ready-to-start"});
      const status=hostAccountRequest("status",registered.projectId),wrong=hostAccountRequest("grant-provider-network-consent",registered.projectId),counter=3;
      const proof=createHostAccountRequestProof(observedNonce!,{method:status.method,route:status.route,canonicalBodyDigest:hostAccountBodyDigest(status.canonicalBody),counter,generation:observedGrant.generation});
      const headers={authorization:`Bearer ${observedGrant.bearer.toString("base64url")}`,"content-type":"application/json","x-chirality-account-counter":String(counter),"x-chirality-account-generation":observedGrant.generation,"x-chirality-account-proof":proof};
      await expect(rawAccountRequest(host.socketPath,wrong.route,headers,wrong.canonicalBody)).resolves.toBe(401);
      await expect(rawAccountRequest(host.socketPath,status.route,headers)).resolves.toBe(200);
      await expect(rawAccountRequest(host.socketPath,status.route,headers)).resolves.toBe(401);
      await serverCallbacks.onInvalidated({connectionId:"same-socket",reason:"invalidated"});clientCallbacks.onInvalidated({reason:"invalidated"});
      await expect(client.status(registered.projectId)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
      await client.close();
      expect(privateFailure).toBeUndefined();
      expect(stageSupplier).not.toHaveBeenCalled();expect(lease.held).toBe(true);
    }finally{await host.stop();}
    expect(createServer).toHaveBeenCalledOnce();
    expect(JSON.parse(await readFile(join(fixture.runtime,"auth","account-host.json"),"utf8"))).toMatchObject({schemaVersion:"chirality.host-account-journal/v1"});
    expect(lease.held).toBe(false);
  });
  it("fences a pending real bootstrap login when the same-socket P2 lease is invalidated",async()=>{
    const base=await realpath(await mkdtemp(join(tmpdir(),"host-account-cancel-")));roots.push(base);const runtime=join(base,"runtime"),projectRoot=join(base,"project");await mkdir(runtime,{mode:0o700});await mkdir(projectRoot);
    let serverCallbacks:any,clientCallbacks:any,cancelled=0,closed=0,releaseStart!:(value:{loginId:string;authUrl:string})=>void;let connection=0;
    const authorityFactory=async(auth:any)=>new HostAccountAuthority({runtimeDirectory:runtime,auth,expectedEuid:process.geteuid?.()??process.getuid?.()??0,
      signingPredicate:{schema:"chirality.host-account-signing-predicate/v1",serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"ABCDEFGHIJ",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'},
      nativeAdmission:{createHostXpcServer(input){serverCallbacks=input;return{ping:async(_id:string,value:any)=>value,closeConnection:async()=>{},close:async()=>{}};}}});
    const host=await startControlledHostedBootstrapRuntimeHostForTests({enabled:true,runtimeDirectory:runtime,daemonSocket:"runtime.sock",instructionRoot:resolve(process.cwd(),"../..")},{
      createAccountHost:authorityFactory,
      async createCeremony(){return{start:()=>new Promise(resolve=>{releaseStart=resolve;}),async status(){return{state:"pending" as const};},async cancel(){cancelled++;releaseStart?.({loginId:"cancelled",authUrl:"https://example.test/cancelled"});},async close(){closed++;}};}
    });
    try{
      const legacy=new RuntimeClient({socketPath:host.socketPath,tokenFile:host.bootstrapTokenFile}),registered=await legacy.initializeHostedBootstrapProject({projectRoot});
      const connect=()=>new MainHostAccountClient({socketPath:host.socketPath,signingPredicate:{schema:"chirality.host-account-signing-predicate/v1",serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"ABCDEFGHIJ",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'},expectedEuid:process.geteuid?.()??process.getuid?.()??0,
        nativeAdmission:{createHostXpcClient(input){clientCallbacks=input;const id=`pending-${++connection}`;return{async provision(request){const challenge=await serverCallbacks.onCeremonyOpen({connectionId:id,requestId:request.requestId});const finish=await request.onChallenge(challenge);const grant=await serverCallbacks.onCeremonyFinish({connectionId:id,...finish});return{...grant,bearer:Buffer.from(grant.bearer)};},async close(){await serverCallbacks.onInvalidated({connectionId:id,reason:"invalidated"});}};}}});
      const client=connect();await client.start();await client.grantProviderNetworkConsent(registered.projectId);
      const pending=client.startLogin(registered.projectId);await expect.poll(()=>typeof releaseStart).toBe("function");
      await serverCallbacks.onInvalidated({connectionId:"pending-1",reason:"invalidated"});clientCallbacks.onInvalidated({reason:"invalidated"});
      await expect(pending).rejects.toBeDefined();expect(cancelled).toBeGreaterThan(0);expect(closed).toBeGreaterThan(0);
      const fresh=connect();await fresh.start();await expect(fresh.status(registered.projectId)).resolves.toMatchObject({projectId:registered.projectId,admission:"unavailable"});await fresh.close();
    }finally{await host.stop();}
  });
  it("rejects changed accepted bytes before issuing a basis",async()=>{
    const fixture=await createFixture();await writeFile(join(fixture.resources,"runtime-governance/v2/login-purpose-acceptance.json"),"changed");
    await expect(loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile)).resolves.toEqual({status:"unavailable",reason:"invalid-release-basis"});
  });
  it("rejects an unsafe Runtime ancestor before snapshot publication",async()=>{
    const fixture=await createFixture();await chmod(fixture.runtime,0o755);
    await expect(loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile)).resolves.toEqual({status:"unavailable",reason:"invalid-release-basis"});
  });
  it("rejects a private snapshot changed across final origin revalidation",async()=>{
    const fixture=await createFixture(),input={resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"} as const};
    const result=await loadPackagedHostedReleaseBasisControlledForTests(input,async()=>fixture.profile,undefined,async()=>{const [digest]=await readdir(join(fixture.runtime,"release-basis"));await writeFile(join(fixture.runtime,"release-basis",digest!,"login-purpose-acceptance.json"),"changed");});
    expect(result).toEqual({status:"unavailable",reason:"invalid-release-basis"});
  });
  it("retains one nominal basis while allowing unrelated Runtime directory activity",async()=>{
    const fixture=await createFixture();
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    await writeFile(join(fixture.runtime,"unrelated-session-state"),"unrelated");
    await expect(revalidateControlledPackagedReleaseBasisForTests(result.basis)).resolves.toBeUndefined();
    await expect(revalidateControlledPackagedReleaseBasisForTests(structuredClone(result.basis))).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    const other=await createFixture(),otherResult=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:other.resources,runtimeDirectory:other.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>other.profile);
    expect(otherResult.status).toBe("ready");if(otherResult.status!=="ready")return;
    await expect(revalidateControlledPackagedReleaseBasisForTests(Object.freeze({...result.basis,login:otherResult.basis.login}))).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });
  it.each(["runtime-contracts/host-account-signing-predicate.json","native/chirality_native_admission.node"])("rejects a changed accepted %s in the live pre-native revalidation",async relativePath=>{
    const fixture=await createFixture();
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    await writeFile(join(fixture.resources,relativePath),"changed-after-issuance");
    await expect(revalidateControlledPackagedReleaseBasisForTests(result.basis)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });
  it("rejects same-byte replacement of the anchor, snapshot, and packaged origin",async()=>{
    const replace=async(path:string)=>{const bytes=await readFile(path),temporary=`${path}.replacement`;await writeFile(temporary,bytes,{mode:0o600});await chmod(temporary,0o600);await rename(temporary,path);};
    for(const target of ["anchor","snapshot","origin","origin-root"] as const){
      const fixture=await createFixture();
      const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
      expect(result.status).toBe("ready");if(result.status!=="ready")continue;
      if(target==="anchor")await replace(join(fixture.runtime,"release-authority","v2","release-anchor.json"));
      else if(target==="snapshot")await replace(result.basis.login.recordPath);
      else if(target==="origin")await replace(join(fixture.resources,"app.asar"));
      else {const previous=`${fixture.resources}.previous`;await rename(fixture.resources,previous);await cp(previous,fixture.resources,{recursive:true,preserveTimestamps:true});}
      await expect(revalidateControlledPackagedReleaseBasisForTests(result.basis)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    }
  });
  it("does not recreate a missing issued snapshot during read-only revalidation",async()=>{
    const fixture=await createFixture();
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    await rm(result.basis.worker.acceptancePath);
    await expect(revalidateControlledPackagedReleaseBasisForTests(result.basis)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    await expect(readFile(result.basis.worker.acceptancePath)).rejects.toMatchObject({code:"ENOENT"});
  });
});
