import { createHash } from "node:crypto";
import { chmod, cp, mkdir, mkdtemp, readFile, readdir, realpath, rename, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it, vi } from "vitest";
import {
  compareRuntimeUtf8V2, encodeRuntimeArtifactInventoryV2, encodeRuntimePayloadManifestV2,
  encodeRuntimePolicyParameterDeclarationV2, runtimePolicyParameterSchemaDigestV2,
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

const roots:string[]=[];const sha=(value:string|Buffer)=>createHash("sha256").update(value).digest("hex");
const file=(relativePath:string,bytes:Buffer)=>({relativePath,size:bytes.length,sha256:sha(bytes)});
function support(entries:RuntimePayloadEntryV2[]):RuntimeSupportProfileV2{
  const map=new Map(entries.filter((entry):entry is Extract<RuntimePayloadEntryV2,{type:"file"}>=>entry.type==="file").map(entry=>[entry.relativePath,entry]));
  const without={schema:"chirality-runtime-support-profile/v2" as const,macosProductVersion:"26.6.2",macosBuildVersion:"25G83",architecture:"arm64" as const,electronVersion:"43.2.0",nodeVersion:"24.13.0",nodeModuleAbi:"145",napiVersion:"10",osMeasurement:{executablePath:"/usr/bin/sw_vers" as const,executableSha256:sha("sw"),executableSize:2},sandboxExec:{path:"/usr/bin/sandbox-exec" as const,sha256:sha("sandbox"),size:7},nativeAdmission:{contract:"chirality-native-admission/v1" as const,sha256:map.get("native/chirality_native_admission.node")!.sha256,size:map.get("native/chirality_native_admission.node")!.size,napiVersion:"6"},supplier:{version:"1.2.3",sha256:map.get("supplier/codex")!.sha256,size:map.get("supplier/codex")!.size,appServerProtocolDigest:sha("protocol"),authorityContract:"chirality.local-admission-authority/1.0" as const,identityContract:"chirality-supplier-account-identity/1" as const},compiler:{outerPolicySchema:"chirality-codex-outer-policy/v2" as const,nativePolicyIdentityVersion:10 as const,sourceDigest:sha("compiler"),parameterSchemaDigest:runtimePolicyParameterSchemaDigestV2()},immutableSystemRoots:["/System","/usr"],kernelHelperContractDigest:sha("kernel")};return {...without,profileDigest:sha(`${JSON.stringify(without)}\n`)};
}
async function createFixture(){
  const base=await realpath(await mkdtemp(join(tmpdir(),"hosted-v2-")));roots.push(base);const resources=join(base,"Resources"),runtime=join(base,"runtime");await mkdir(resources);await mkdir(runtime,{mode:0o700});
  const files=new Map<string,Buffer>([["app.asar",Buffer.from("app")],["instruction-root/instruction-bundle-manifest.json",Buffer.from("bundle")],["native/chirality_native_admission.node",Buffer.from("native")],["runtime-cli/chirality-cli.mjs",Buffer.from("cli")],["runtime-cli/chirality-cli.mjs.map",Buffer.from("map")],["runtime-contracts/runtime-policy-parameters-v2.json",encodeRuntimePolicyParameterDeclarationV2()],["supplier/codex",Buffer.from("supplier")]]);
  for(const [path,bytes]of files){await mkdir(join(resources,path,".."),{recursive:true});await writeFile(join(resources,path),bytes);}
  const entries:RuntimePayloadEntryV2[]=[...["instruction-root","native","runtime-cli","runtime-contracts","supplier"].map(relativePath=>({relativePath,type:"directory" as const})),...[...files].map(([relativePath,bytes])=>({...file(relativePath,bytes),type:"file" as const}))].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath));
  const profile=support(entries),manifest:RuntimePayloadManifestV2={schema:"chirality-runtime-payload-manifest/v2",dependencyResolutionDigest:sha("deps"),roots:["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"].sort(compareRuntimeUtf8V2),supportProfiles:[profile],entries};
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
  return {resources,runtime,profile};
}
afterEach(async()=>{vi.restoreAllMocks();while(roots.length)await rm(roots.pop()!,{recursive:true,force:true});});

describe("packaged hosted release basis",()=>{
  it("loads the complete accepted filesystem basis through the isolated support observer",async()=>{
    const fixture=await createFixture(),observe=vi.fn(async()=>fixture.profile);
    let failure:unknown;const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},observe,error=>{failure=error;});
    if(result.status!=="ready")throw failure;
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    expect(observe).toHaveBeenCalledOnce();expect(isControlledPackagedReleaseBasisForTests(result.basis)).toBe(true);expect(Object.isFrozen(result.basis.verified.payload.entries)).toBe(true);expect(Object.isFrozen(result.basis.login)).toBe(true);
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({bootstrap:{enabled:true,runtimeDirectory:fixture.runtime,daemonSocket:join(fixture.runtime,"daemon.sock"),instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath},basis:result.basis})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
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
    await expect(startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests({bootstrap,basis:result.basis},async input=>{
      observed=validateHostedPrivateCompositionOptions(input.privateComposition);
      throw new RuntimeError("ENGINE_UNAVAILABLE","Host account authority is unavailable",503);
    })).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    const composition=observed as ReturnType<typeof validateHostedPrivateCompositionOptions>;
    expect(composition.releaseV2?.basis).toBe(result.basis);
    expect(composition).toMatchObject({runtimeDirectory:fixture.runtime,supplierExecutablePath:result.basis.supplierExecutablePath,nativeAddonPath:result.basis.nativeAddonPath,
      instructionRoot:result.basis.instructionRoot,commandNetworkPosture:"off",compatibility:{compatibilityIdentity:"root-runtime-1",contractBasisSha256:"6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2"},turnTimeoutMs:600_000});
    expect(composition).not.toHaveProperty("model");expect(composition).not.toHaveProperty("consentVersion");expect(composition).not.toHaveProperty("managedAuth");
  });
  it.each([undefined, {}, { login: {} }, { schema: "chirality-hosted-packaged-release-basis/v2", login: { recordPath: "/fabricated" } }])("rejects malformed or fabricated packaged starter basis coarsely", async basis => {
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({ bootstrap: { enabled: true, runtimeDirectory: "/runtime", daemonSocket: "runtime.sock", instructionRoot: "/instructions", nativeAddonPath: "/native.node" }, basis: basis as any })).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
  });
  it("connects the issued basis through the real private composition and fails at missing P2 before staging",async()=>{
    const fixture=await createFixture(),projectRoot=join(fixture.runtime,"..","project");await mkdir(projectRoot,{mode:0o700});
    const result=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:fixture.resources,runtimeDirectory:fixture.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>fixture.profile);
    expect(result.status).toBe("ready");if(result.status!=="ready")return;
    const lease=createFakeRuntimeAdmissionNativeAdapter().acquire(fixture.runtime,"controlled-release.lock"),stageSupplier=vi.fn(async()=>{throw new Error("supplier staging must remain unreachable");});
    const unreachable=async()=>{throw new Error("downstream private effect must remain unreachable");};
    const adapters:ControlledHostedPrivateCompositionAdapters={revalidateReleaseBasis:revalidateControlledPackagedReleaseBasisForTests,acquireLease:async()=>lease,stageSupplier,
      prepareNativeRoles:unreachable,bindRuntimeReadRoot:unreachable,validateLoginStartup:unreachable,createLogin:()=>{throw new Error("login creation must remain unreachable");},preparePolicy:unreachable,
      createLauncherFactory:()=>{throw new Error("launcher creation must remain unreachable");},admitHosted:unreachable,logout:unreachable,openBindingStore:unreachable};
    const bootstrap={enabled:true as const,runtimeDirectory:fixture.runtime,daemonSocket:"control.sock",instructionRoot:result.basis.instructionRoot,nativeAddonPath:result.basis.nativeAddonPath};
    let privateFailure:unknown;
    const host=await startHostedPackagedPrivateBootstrapRuntimeHostControlledForTests({bootstrap,basis:result.basis},input=>startControlledHostedPrivateBootstrapRuntimeHostForTests(input,{
      createBindings:async options=>{const bindings=await createControlledHostedBootstrapPrivateBindingsForTests(options,adapters);return Object.freeze({...bindings,async createCeremony(ceremonyInput){try{return await bindings.createCeremony(ceremonyInput);}catch(error){privateFailure=error;throw error;}}});},
      startHost:(boot,bindings)=>startControlledHostedBootstrapRuntimeHostForTests(boot,bindings!)
    }));
    try{
      const client=new RuntimeClient({socketPath:host.socketPath,tokenFile:host.bootstrapTokenFile}),registered=await client.initializeHostedBootstrapProject({projectRoot});
      await client.grantHostedProviderNetworkConsent(registered.projectId);
      await expect(client.startHostedBootstrapLogin(registered.projectId)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
      expect(privateFailure).toMatchObject({code:"ENGINE_UNAVAILABLE",details:{reason:"HOST_ACCOUNT_AUTHORITY_UNAVAILABLE"}});
      expect(stageSupplier).not.toHaveBeenCalled();expect(lease.held).toBe(true);
    }finally{await host.stop();}
    expect(lease.held).toBe(false);
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
