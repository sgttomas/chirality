import { createHash } from "node:crypto";
import { chmod, mkdir, mkdtemp, open, readFile, readdir, realpath, rename, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  compareRuntimeUtf8V2, encodeRuntimeArtifactInventoryV2, encodeRuntimePayloadManifestV2,
  encodeRuntimePolicyParameterDeclarationV2, runtimePolicyParameterSchemaDigestV2,
  type RuntimeArtifactInventoryV2, type RuntimePayloadEntryV2, type RuntimePayloadManifestV2,
  type RuntimeSupportProfileV2
} from "../packages/core/src/runtime-conformance-v2.js";
import {
  isControlledPackagedReleaseBasisForTests, loadPackagedHostedReleaseBasisControlledForTests,
  startHostedPackagedPrivateBootstrapRuntimeHost
} from "../packages/daemon/src/hosted-packaged-release.js";
import { installHostedReleaseAnchorV2, type AcceptedHostedReleaseProvisioningV2 } from "../packages/daemon/src/hosted-release-provisioner.js";

const roots:string[]=[];
const sha=(value:string|Buffer)=>createHash("sha256").update(value).digest("hex");
const artifact=(relativePath:string,bytes:Buffer)=>({relativePath,size:bytes.length,sha256:sha(bytes)});
const OWNER_NAMES=["login-purpose-record.json","login-purpose-acceptance.json","login-owner-act","worker-purpose-record.json","worker-purpose-acceptance.json","worker-owner-act"] as const;

function support(entries:RuntimePayloadEntryV2[]):RuntimeSupportProfileV2{
  const map=new Map(entries.filter((entry):entry is Extract<RuntimePayloadEntryV2,{type:"file"}>=>entry.type==="file").map(entry=>[entry.relativePath,entry]));
  const without={schema:"chirality-runtime-support-profile/v2" as const,macosProductVersion:"26.6.2",macosBuildVersion:"25G83",architecture:"arm64" as const,electronVersion:"43.2.0",nodeVersion:"24.13.0",nodeModuleAbi:"145",napiVersion:"10",osMeasurement:{executablePath:"/usr/bin/sw_vers" as const,executableSha256:sha("sw"),executableSize:2},sandboxExec:{path:"/usr/bin/sandbox-exec" as const,sha256:sha("sandbox"),size:7},nativeAdmission:{contract:"chirality-native-admission/v1" as const,sha256:map.get("native/chirality_native_admission.node")!.sha256,size:map.get("native/chirality_native_admission.node")!.size,napiVersion:"6"},supplier:{version:"1.2.3",sha256:map.get("supplier/codex")!.sha256,size:map.get("supplier/codex")!.size,appServerProtocolDigest:sha("protocol"),authorityContract:"chirality.local-admission-authority/1.0" as const,identityContract:"chirality-supplier-account-identity/1" as const},compiler:{outerPolicySchema:"chirality-codex-outer-policy/v2" as const,nativePolicyIdentityVersion:10 as const,sourceDigest:sha("compiler"),parameterSchemaDigest:runtimePolicyParameterSchemaDigestV2()},immutableSystemRoots:["/System","/usr"],kernelHelperContractDigest:sha("kernel")};
  return {...without,profileDigest:sha(`${JSON.stringify(without)}\n`)};
}

async function fixture(options:{variant?:string;secondProfile?:boolean;recordProfiles?:"subset"|"duplicate"|"unknown"}={}){
  const base=await realpath(await mkdtemp(join(tmpdir(),"prov-v2-")));roots.push(base);
  const resources=join(base,"Resources"),runtime=join(base,"runtime"),accepted=join(base,"accepted");
  await mkdir(resources);await mkdir(runtime,{mode:0o700});await chmod(runtime,0o700);await mkdir(accepted,{mode:0o700});await chmod(accepted,0o700);
  const payloadFiles=new Map<string,Buffer>([["app.asar",Buffer.from("app")],["instruction-root/instruction-bundle-manifest.json",Buffer.from("bundle")],["native/chirality_native_admission.node",Buffer.from("native")],["runtime-cli/chirality-cli.mjs",Buffer.from("cli")],["runtime-cli/chirality-cli.mjs.map",Buffer.from("map")],["runtime-contracts/runtime-policy-parameters-v2.json",encodeRuntimePolicyParameterDeclarationV2()],["supplier/codex",Buffer.from("supplier")]]);
  for(const[path,bytes]of payloadFiles){await mkdir(join(resources,path,".."),{recursive:true});await writeFile(join(resources,path),bytes);}
  const entries:RuntimePayloadEntryV2[]=[...['instruction-root','native','runtime-cli','runtime-contracts','supplier'].map(relativePath=>({relativePath,type:'directory' as const})),...[...payloadFiles].map(([relativePath,bytes])=>({...artifact(relativePath,bytes),type:'file' as const}))].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath));
  const profile=support(entries),secondWithout={...profile,macosBuildVersion:"25G84"};delete (secondWithout as Partial<RuntimeSupportProfileV2>).profileDigest;const secondProfile={...secondWithout,profileDigest:sha(`${JSON.stringify(secondWithout)}\n`)} as RuntimeSupportProfileV2;
  const supportProfiles=(options.secondProfile?[profile,secondProfile]:[profile]).sort((a,b)=>compareRuntimeUtf8V2(a.profileDigest,b.profileDigest));
  const manifest:RuntimePayloadManifestV2={schema:"chirality-runtime-payload-manifest/v2",dependencyResolutionDigest:sha("deps"),roots:["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"].sort(compareRuntimeUtf8V2),supportProfiles,entries};
  const manifestBytes=encodeRuntimePayloadManifestV2(manifest);await writeFile(join(resources,"runtime-payload-manifest.json"),manifestBytes);
  const declaredProfiles=options.recordProfiles==="duplicate"?[profile.profileDigest,profile.profileDigest]:options.recordProfiles==="unknown"?[sha("unknown-profile")]:[profile.profileDigest];
  const owner=Buffer.from(`accepted-owner-act${options.variant??""}`),common={sourceDigest:profile.compiler.sourceDigest,payloadDigest:sha(manifestBytes),supportProfileDigests:declaredProfiles,policyContractDigest:profile.compiler.parameterSchemaDigest,supplyProfileDigest:sha(`${JSON.stringify(profile.supplier)}\n`),issuedAt:"2026-01-01T00:00:00.000Z",expiresAt:"2099-01-01T00:00:00.000Z"};
  const limbs=(names:readonly string[])=>Object.fromEntries(names.map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]));
  const loginRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-login-purpose-release/v2",evidenceClass:"exact-account-free-login-purpose-observed",...common,backend:{credentialStore:"keyring",plaintextFallback:false},methods:["account/login/start","account/login/cancel","account/read","model/list"],modelExecution:false,limbs:limbs(["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"])}));
  const workerRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-worker-purpose-release/v2",evidenceClass:"exact-worker-purpose-observed",...common,limbs:limbs(["effective-policy","primary.read","primary.file-change","primary.shell-write","primary.network","primary.process","primary.environment","primary.approval","primary.role","descendant.read","descendant.file-change","descendant.shell-write","descendant.network","descendant.process","descendant.environment","descendant.approval","descendant.role","owner-live-native-delegation"])}));
  const acceptance=(record:Buffer,gateIdentity:string)=>Buffer.from(JSON.stringify({schema:"chirality-runtime-conformance-acceptance/v1",status:"accepted",recordSha256:sha(record),sourceDigest:profile.compiler.sourceDigest,activationId:"release-v2",gateIdentity,ownerActSha256:sha(owner),ownerReference:"accepted owner act",expiresAt:"2099-01-01T00:00:00.000Z"}));
  const governance=new Map<string,Buffer>([[OWNER_NAMES[0],loginRecord],[OWNER_NAMES[1],acceptance(loginRecord,"D36")],[OWNER_NAMES[2],owner],[OWNER_NAMES[3],workerRecord],[OWNER_NAMES[4],acceptance(workerRecord,"WORKER-V2")],[OWNER_NAMES[5],owner]]);
  const packagedRoot=join(resources,"runtime-governance","v2");await mkdir(packagedRoot,{recursive:true});
  for(const[name,bytes]of governance){await writeFile(join(accepted,name),bytes,{mode:0o600});await chmod(join(accepted,name),0o600);await writeFile(join(packagedRoot,name),bytes);}
  const inventory:RuntimeArtifactInventoryV2={schema:"chirality-runtime-artifact-inventory/v2",payloadManifest:artifact("runtime-payload-manifest.json",manifestBytes) as RuntimeArtifactInventoryV2["payloadManifest"],governance:OWNER_NAMES.map(name=>artifact(`runtime-governance/v2/${name}`,governance.get(name)!)) as unknown as RuntimeArtifactInventoryV2["governance"]};
  const inventoryBytes=encodeRuntimeArtifactInventoryV2(inventory);await writeFile(join(resources,"runtime-artifact-inventory-v2.json"),inventoryBytes);
  const input:AcceptedHostedReleaseProvisioningV2={runtimeDirectory:runtime,resourcesRoot:resources,acceptedGovernanceRoot:accepted,expectedOuterInventorySha256:sha(inventoryBytes),login:{activationId:"release-v2",gateIdentity:"D36"},worker:{activationId:"release-v2",gateIdentity:"WORKER-V2"}};
  return {base,resources,runtime,accepted,profile,secondProfile,input};
}

beforeEach(()=>{vi.useFakeTimers();vi.setSystemTime(new Date("2026-09-10T12:00:00.000Z"));});
afterEach(async()=>{vi.useRealTimers();vi.restoreAllMocks();while(roots.length)await rm(roots.pop()!,{recursive:true,force:true});});

async function syncFailureAt(call:number):Promise<ReturnType<typeof vi.spyOn>>{
  const sample=await open(tmpdir(),"r"),prototype=Object.getPrototypeOf(sample),original=prototype.sync;await sample.close();let count=0;
  return vi.spyOn(prototype,"sync").mockImplementation(async function(this:unknown){count++;if(count===call)throw new Error(`sync-failure-${call}`);return original.call(this);});
}

describe("controlled owner release-anchor provisioner",()=>{
  it("publishes deterministic canonical bytes and the real loader consumes them without granting P2",async()=>{
    const f=await fixture(),first=await installHostedReleaseAnchorV2(f.input),bytes=await readFile(first.anchorPath);
    expect(first.disposition).toBe("created");expect(bytes.at(-1)).toBe(10);expect(first.anchorSha256).toBe(sha(bytes));
    await expect(installHostedReleaseAnchorV2(structuredClone(f.input))).resolves.toMatchObject({disposition:"already-identical",anchorSha256:first.anchorSha256});
    let failure:unknown;const loaded=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:f.resources,runtimeDirectory:f.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>f.profile,error=>{failure=error;});
    if(loaded.status!=="ready")throw failure;expect(isControlledPackagedReleaseBasisForTests(loaded.basis)).toBe(true);
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({bootstrap:{enabled:true,runtimeDirectory:f.runtime,daemonSocket:join(f.runtime,"daemon.sock"),instructionRoot:loaded.basis.instructionRoot,nativeAddonPath:loaded.basis.nativeAddonPath},basis:loaded.basis})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });

  it("allows concurrent identical publication through the fixed final-name race",async()=>{
    const f=await fixture(),results=await Promise.all([installHostedReleaseAnchorV2(f.input),installHostedReleaseAnchorV2(f.input)]);
    expect(results.map(result=>result.disposition).sort()).toEqual(["already-identical","created"]);expect(new Set(results.map(result=>result.anchorSha256)).size).toBe(1);
    const names=await readdir(join(f.runtime,"release-authority","v2"));expect(names).toEqual(["release-anchor.json"]);expect(sha(await readFile(join(f.runtime,"release-authority","v2","release-anchor.json")))).toBe(results[0]!.anchorSha256);
  });

  it("preserves exactly one winner when different valid anchors race",async()=>{
    const first=await fixture({variant:"-one"}),second=await fixture({variant:"-two"});second.input.runtimeDirectory=first.runtime;
    const settled=await Promise.allSettled([installHostedReleaseAnchorV2(first.input),installHostedReleaseAnchorV2(second.input)]),fulfilled=settled.filter((result):result is PromiseFulfilledResult<Awaited<ReturnType<typeof installHostedReleaseAnchorV2>>>=>result.status==="fulfilled"),rejected=settled.filter(result=>result.status==="rejected");
    expect(fulfilled).toHaveLength(1);expect(rejected).toHaveLength(1);expect(String((rejected[0] as PromiseRejectedResult).reason)).toContain("installed anchor conflicts");
    const anchor=await readFile(join(first.runtime,"release-authority","v2","release-anchor.json"));expect(sha(anchor)).toBe(fulfilled[0]!.value.anchorSha256);expect((await readdir(join(first.runtime,"release-authority","v2"))).filter(name=>name.endsWith(".tmp"))).toEqual([]);
  });

  it("accepts a purpose-scoped support-profile subset and leaves an unlisted observed profile unavailable",async()=>{
    const f=await fixture({secondProfile:true});await expect(installHostedReleaseAnchorV2(f.input)).resolves.toMatchObject({disposition:"created"});
    const loaded=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:f.resources,runtimeDirectory:f.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>f.secondProfile);
    expect(loaded).toEqual({status:"unavailable",reason:"invalid-release-basis"});
  });

  it.each(["duplicate","unknown"] as const)("rejects a %s purpose support-profile declaration",async recordProfiles=>{
    const f=await fixture({secondProfile:true,recordProfiles});await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("purpose support profile");
    await expect(readFile(join(f.runtime,"release-authority","v2","release-anchor.json"))).rejects.toMatchObject({code:"ENOENT"});
  });

  it("rejects owner-source drift even when the packaged closure is internally consistent",async()=>{
    const f=await fixture();await writeFile(join(f.accepted,"worker-owner-act"),"different-owner",{mode:0o600});await chmod(join(f.accepted,"worker-owner-act"),0o600);
    await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("packaged governance differs from accepted source");
    await expect(readFile(join(f.runtime,"release-authority","v2","release-anchor.json"))).rejects.toMatchObject({code:"ENOENT"});
  });

  it("never replaces a conflicting pre-existing anchor",async()=>{
    const f=await fixture(),root=join(f.runtime,"release-authority","v2"),anchor=join(root,"release-anchor.json");await mkdir(root,{recursive:true,mode:0o700});await chmod(join(f.runtime,"release-authority"),0o700);await chmod(root,0o700);await writeFile(anchor,"existing-conflict\n",{mode:0o600});await chmod(anchor,0o600);
    await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("installed anchor conflicts");expect(await readFile(anchor,"utf8")).toBe("existing-conflict\n");
  });

  it.each([[1,"ancestor"],[4,"final-link"],[5,"scratch-removal"]] as const)("does not report success when %s directory sync fails",async(call,label)=>{
    const f=await fixture();await syncFailureAt(call);await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow(`sync-failure-${call}`);
    vi.restoreAllMocks();
    if(label==="ancestor")await expect(readFile(join(f.runtime,"release-authority","v2","release-anchor.json"))).rejects.toMatchObject({code:"ENOENT"});
    else await expect(installHostedReleaseAnchorV2(f.input)).resolves.toMatchObject({disposition:"already-identical"});
  });

  it("removes scratch and reports failure when temporary-file sync fails",async()=>{
    const f=await fixture();await syncFailureAt(3);await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("sync-failure-3");vi.restoreAllMocks();
    const directory=join(f.runtime,"release-authority","v2");expect((await readdir(directory)).filter(name=>name.endsWith(".tmp"))).toEqual([]);await expect(readFile(join(directory,"release-anchor.json"))).rejects.toMatchObject({code:"ENOENT"});
  });

  it("detects growth through the declared-size-plus-one held read",async()=>{
    const f=await fixture(),sample=await open(f.runtime,"r"),prototype=Object.getPrototypeOf(sample),original=prototype.read;await sample.close();let changed=false;
    vi.spyOn(prototype,"read").mockImplementation(async function(this:unknown,...args:unknown[]){if(!changed){changed=true;await writeFile(join(f.accepted,"login-purpose-record.json"),"growth",{flag:"a"});}return original.apply(this,args);});
    await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("owner file changed while reading");
  });

  it("detects pathname replacement while holding the original source file",async()=>{
    const f=await fixture(),target=join(f.accepted,"login-purpose-record.json"),sample=await open(f.runtime,"r"),prototype=Object.getPrototypeOf(sample),original=prototype.read;await sample.close();let changed=false;
    vi.spyOn(prototype,"read").mockImplementation(async function(this:unknown,...args:unknown[]){if(!changed){changed=true;await rename(target,`${target}.old`);await writeFile(target,"replacement",{mode:0o600});await chmod(target,0o600);}return original.apply(this,args);});
    await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("owner file changed while reading");
  });

  it("revalidates external inputs after publication and preserves the installed accepted bytes on late failure",async()=>{
    const f=await fixture(),sample=await open(f.runtime,"r"),prototype=Object.getPrototypeOf(sample),original=prototype.sync;await sample.close();let count=0;
    vi.spyOn(prototype,"sync").mockImplementation(async function(this:unknown){count++;const result=await original.call(this);if(count===5){await writeFile(join(f.accepted,"worker-owner-act"),"late-change",{mode:0o600});await chmod(join(f.accepted,"worker-owner-act"),0o600);}return result;});
    await expect(installHostedReleaseAnchorV2(f.input)).rejects.toThrow("packaged governance differs from accepted source");
    expect(await readFile(join(f.runtime,"release-authority","v2","release-anchor.json"),"utf8")).toContain('"schema":"chirality-runtime-release-anchor/v2"');
  });

  it("exposes only the dedicated package subpath and keeps the owner tool out of daemon routes and bins",async()=>{
    const packageJson=JSON.parse(await readFile(join(process.cwd(),"packages/daemon/package.json"),"utf8"));
    expect(packageJson.exports["./hosted-release-provisioner"]).toEqual({types:"./dist/hosted-release-provisioner.d.ts",import:"./dist/hosted-release-provisioner.js"});
    expect(packageJson.bin).toEqual({"chirality-runtime-service":"dist/standalone-bin.js"});
    const {parseProvisionHostedReleaseArguments,runProvisionHostedReleaseAnchorV2}=await import("../tools/provision-hosted-release-anchor-v2.mjs");
    const parsed=parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2"]);
    expect(parsed).toMatchObject({resourcesRoot:"/Applications/Chirality.app/Contents/Resources",runtimeDirectory:"/private/runtime",acceptedGovernanceRoot:"/private/accepted",login:{gateIdentity:"D36"}});
    const install=vi.fn(async(input:unknown)=>({input}));await runProvisionHostedReleaseAnchorV2(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2"],install);expect(install).toHaveBeenCalledWith(parsed);
    expect(()=>parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--app","/Applications/Other.app"])).toThrow("Usage:");
  });
});
