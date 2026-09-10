import { createHash } from "node:crypto";
import { chmod, mkdir, mkdtemp, open, readFile, readdir, realpath, rename, rm, stat, writeFile } from "node:fs/promises";
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
import { installHostedReleaseAnchorV2, installHostedReleaseAnchorV2ControlledForTests, observeHostedReleaseTrialSealV1ControlledForTests, prepareHostedReleaseGovernanceV2, type AcceptedHostedReleaseProvisioningV2 } from "../packages/daemon/src/hosted-release-provisioner.js";

const roots:string[]=[];
const sha=(value:string|Buffer)=>createHash("sha256").update(value).digest("hex");
const artifact=(relativePath:string,bytes:Buffer)=>({relativePath,size:bytes.length,sha256:sha(bytes)});
const OWNER_NAMES=["login-purpose-record.json","login-purpose-acceptance.json","login-owner-act","worker-purpose-record.json","worker-purpose-acceptance.json","worker-owner-act"] as const;

function support(entries:RuntimePayloadEntryV2[]):RuntimeSupportProfileV2{
  const map=new Map(entries.filter((entry):entry is Extract<RuntimePayloadEntryV2,{type:"file"}>=>entry.type==="file").map(entry=>[entry.relativePath,entry]));
  const without={schema:"chirality-runtime-support-profile/v2" as const,macosProductVersion:"26.6.2",macosBuildVersion:"25G83",architecture:"arm64" as const,electronVersion:"43.2.0",nodeVersion:"24.13.0",nodeModuleAbi:"145",napiVersion:"10",osMeasurement:{executablePath:"/usr/bin/sw_vers" as const,executableSha256:sha("sw"),executableSize:2},sandboxExec:{path:"/usr/bin/sandbox-exec" as const,sha256:sha("sandbox"),size:7},nativeAdmission:{contract:"chirality-native-admission/v1" as const,sha256:map.get("native/chirality_native_admission.node")!.sha256,size:map.get("native/chirality_native_admission.node")!.size,napiVersion:"6"},supplier:{version:"1.2.3",sha256:map.get("supplier/codex")!.sha256,size:map.get("supplier/codex")!.size,appServerProtocolDigest:sha("protocol"),authorityContract:"chirality.local-admission-authority/1.0" as const,identityContract:"chirality-supplier-account-identity/1" as const},compiler:{outerPolicySchema:"chirality-codex-outer-policy/v2" as const,nativePolicyIdentityVersion:10 as const,sourceDigest:sha("compiler"),parameterSchemaDigest:runtimePolicyParameterSchemaDigestV2()},immutableSystemRoots:["/System","/usr"],kernelHelperContractDigest:sha("kernel")};
  return {...without,profileDigest:sha(`${JSON.stringify(without)}\n`)};
}

async function fixture(options:{variant?:string;secondProfile?:boolean;recordProfiles?:"subset"|"duplicate"|"unknown";trial?:boolean;trialMutation?:"limb"|"prerequisite"|"expired"}={}){
  const base=await realpath(await mkdtemp(join(tmpdir(),"prov-v2-")));roots.push(base);
  const resources=join(base,"Resources"),runtime=join(base,"runtime"),accepted=join(base,"accepted");
  await mkdir(resources);await mkdir(runtime,{mode:0o700});await chmod(runtime,0o700);await mkdir(accepted,{mode:0o700});await chmod(accepted,0o700);
  const payloadFiles=new Map<string,Buffer>([["app.asar",Buffer.from("app")],["instruction-root/instruction-bundle-manifest.json",Buffer.from("bundle")],["native/chirality_native_admission.node",Buffer.from("native")],["runtime-cli/chirality-cli.mjs",Buffer.from("cli")],["runtime-cli/chirality-cli.mjs.map",Buffer.from("map")],["runtime-contracts/runtime-policy-parameters-v2.json",encodeRuntimePolicyParameterDeclarationV2()],["supplier/codex",Buffer.from("supplier")]]);
  for(const[path,bytes]of payloadFiles){await mkdir(join(resources,path,".."),{recursive:true});await writeFile(join(resources,path),bytes);}
  await chmod(join(resources,"supplier/codex"),0o755);
  const entries:RuntimePayloadEntryV2[]=[...['instruction-root','native','runtime-cli','runtime-contracts','supplier'].map(relativePath=>({relativePath,type:'directory' as const})),...[...payloadFiles].map(([relativePath,bytes])=>({...artifact(relativePath,bytes),type:'file' as const}))].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath));
  const profile=support(entries),secondWithout={...profile,macosBuildVersion:"25G84"};delete (secondWithout as Partial<RuntimeSupportProfileV2>).profileDigest;const secondProfile={...secondWithout,profileDigest:sha(`${JSON.stringify(secondWithout)}\n`)} as RuntimeSupportProfileV2;
  const supportProfiles=(options.secondProfile?[profile,secondProfile]:[profile]).sort((a,b)=>compareRuntimeUtf8V2(a.profileDigest,b.profileDigest));
  const manifest:RuntimePayloadManifestV2={schema:"chirality-runtime-payload-manifest/v2",dependencyResolutionDigest:sha("deps"),roots:["app.asar","instruction-root","native","runtime-cli","runtime-contracts","supplier"].sort(compareRuntimeUtf8V2),supportProfiles,entries};
  const manifestBytes=encodeRuntimePayloadManifestV2(manifest);await writeFile(join(resources,"runtime-payload-manifest.json"),manifestBytes);
  const declaredProfiles=options.recordProfiles==="duplicate"?[profile.profileDigest,profile.profileDigest]:options.recordProfiles==="unknown"?[sha("unknown-profile")]:[profile.profileDigest];
  const owner=Buffer.from(`accepted-owner-act${options.variant??""}`),common={sourceDigest:profile.compiler.sourceDigest,payloadDigest:sha(manifestBytes),supportProfileDigests:declaredProfiles,policyContractDigest:profile.compiler.parameterSchemaDigest,supplyProfileDigest:sha(`${JSON.stringify(profile.supplier)}\n`),issuedAt:"2026-01-01T00:00:00.000Z",expiresAt:"2099-01-01T00:00:00.000Z"};
  const limbs=(names:readonly string[])=>Object.fromEntries(names.map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]));
  const loginRecord=Buffer.from(JSON.stringify({schema:"chirality-codex-login-purpose-release/v2",evidenceClass:"exact-account-free-login-purpose-observed",...common,backend:{credentialStore:"keyring",plaintextFallback:false},methods:["account/login/start","account/login/cancel","account/read","model/list"],modelExecution:false,limbs:limbs(["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"])}));
  const workerNames=["effective-policy","primary.read","primary.file-change","primary.shell-write","primary.network","primary.process","primary.environment","primary.approval","primary.role","descendant.read","descendant.file-change","descendant.shell-write","descendant.network","descendant.process","descendant.environment","descendant.approval","descendant.role","owner-live-native-delegation"];
  const pending=Object.fromEntries(workerNames.map(name=>[name,{status:"pending-human-trial"}]));
  if(options.trialMutation==="limb")(pending[workerNames[0]!] as {status:string}).status="passed";
  const prerequisites=Object.fromEntries(["signed-payload-and-supply","trusted-app-and-account-host","native-enforcement-and-retirement","connected-source-contract"].map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]));
  if(options.trialMutation==="prerequisite")delete prerequisites["connected-source-contract"];
  const workerCommon=options.trialMutation==="expired"?{...common,expiresAt:"2026-01-02T00:00:00.000Z"}:common;
  const workerRecord=Buffer.from(JSON.stringify(options.trial?{schema:"chirality-codex-worker-purpose-release/v3",evidenceClass:"exact-local-human-trial-authorized",...workerCommon,limbs:pending,trialScope:"local-human-functional-trial",prerequisites}:{schema:"chirality-codex-worker-purpose-release/v2",evidenceClass:"exact-worker-purpose-observed",...workerCommon,limbs:limbs(workerNames)}));
  const acceptance=(record:Buffer,gateIdentity:string)=>Buffer.from(JSON.stringify({schema:"chirality-runtime-conformance-acceptance/v1",status:"accepted",recordSha256:sha(record),sourceDigest:profile.compiler.sourceDigest,activationId:"release-v2",gateIdentity,ownerActSha256:sha(owner),ownerReference:"accepted owner act",expiresAt:"2099-01-01T00:00:00.000Z"}));
  const governance=new Map<string,Buffer>([[OWNER_NAMES[0],loginRecord],[OWNER_NAMES[1],acceptance(loginRecord,"D36")],[OWNER_NAMES[2],owner],[OWNER_NAMES[3],workerRecord],[OWNER_NAMES[4],acceptance(workerRecord,"WORKER-V2")],[OWNER_NAMES[5],owner]]);
  const packagedRoot=join(resources,"runtime-governance","v2");await mkdir(packagedRoot,{recursive:true});
  for(const[name,bytes]of governance){await writeFile(join(accepted,name),bytes,{mode:0o600});await chmod(join(accepted,name),0o600);await writeFile(join(packagedRoot,name),bytes);}
  const inventory:RuntimeArtifactInventoryV2={schema:"chirality-runtime-artifact-inventory/v2",payloadManifest:artifact("runtime-payload-manifest.json",manifestBytes) as RuntimeArtifactInventoryV2["payloadManifest"],governance:OWNER_NAMES.map(name=>artifact(`runtime-governance/v2/${name}`,governance.get(name)!)) as unknown as RuntimeArtifactInventoryV2["governance"]};
  const inventoryBytes=encodeRuntimeArtifactInventoryV2(inventory);await writeFile(join(resources,"runtime-artifact-inventory-v2.json"),inventoryBytes);
  const input:AcceptedHostedReleaseProvisioningV2={runtimeDirectory:runtime,resourcesRoot:resources,acceptedGovernanceRoot:accepted,expectedOuterInventorySha256:sha(inventoryBytes),login:{activationId:"release-v2",gateIdentity:"D36"},worker:{activationId:"release-v2",gateIdentity:"WORKER-V2"}};
  const executablePath=join(base,"Chirality.app","Contents","MacOS","Chirality"),effectivePeerRequirement='identifier "com.chirality.app" and cdhash H"1234567890abcdef1234567890abcdef12345678"';
  const code=(path:string)=>({path,cdHash:"1234567890abcdef1234567890abcdef12345678",designatedRequirement:'identifier "com.chirality.app" and anchor apple generic',identifier:"com.chirality.app",teamIdentifier:"TESTTEAM01"});
  const signedIdentity={schema:"chirality.host-account-signed-peer-identity-binding/v1" as const,predicate:{schema:"chirality.host-account-signing-predicate/v1" as const,serviceName:"com.chirality.app.runtime.account-host",bundleId:"com.chirality.app",teamId:"TESTTEAM01",peerRequirement:'identifier "com.chirality.app" and anchor apple generic'},effectivePeerRequirement,subject:code(executablePath),outer:code(join(base,"Chirality.app")),fuses:"electron-runtime-fuses-verified" as const,asarIntegrity:"electron-asar-integrity-verified" as const};
  if(options.trial){const observationRoot=join(base,"observation");await mkdir(observationRoot,{mode:0o700});await chmod(observationRoot,0o700);const observationPath=join(observationRoot,"trial.json"),observation=Buffer.from(JSON.stringify({schema:"chirality-runtime-trial-seal-observation/v1",outerInventorySha256:sha(inventoryBytes),payloadDigest:sha(manifestBytes),mainCodeDirectoryHash:signedIdentity.subject.cdHash,peerRequirementSha256:sha(effectivePeerRequirement),checks:Object.fromEntries(["signed-app","fuses-and-asar","signed-peer-identity-binding"].map(name=>[name,{attempted:true,passed:true,evidenceSha256:sha(name)}]))}));await writeFile(observationPath,observation,{mode:0o600});await chmod(observationPath,0o600);input.trial={observationPath,expectedObservationSha256:sha(observation),executablePath};}
  return {base,resources,runtime,accepted,profile,secondProfile,input,signedIdentity};
}

beforeEach(()=>{vi.useFakeTimers();vi.setSystemTime(new Date("2026-09-10T12:00:00.000Z"));});
afterEach(async()=>{vi.useRealTimers();vi.restoreAllMocks();while(roots.length)await rm(roots.pop()!,{recursive:true,force:true});});

async function syncFailureAt(call:number):Promise<ReturnType<typeof vi.spyOn>>{
  const sample=await open(tmpdir(),"r"),prototype=Object.getPrototypeOf(sample),original=prototype.sync;await sample.close();let count=0;
  return vi.spyOn(prototype,"sync").mockImplementation(async function(this:unknown){count++;if(count===call)throw new Error(`sync-failure-${call}`);return original.call(this);});
}

describe("controlled owner release-anchor provisioner",()=>{
  it("assembles the exact six governed inputs from explicit owner acts and factual evidence",async()=>{
    const f=await fixture(),evidence=Object.fromEntries(["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"].map(name=>[name,sha(`login:${name}`)])),prerequisites=Object.fromEntries(["signed-payload-and-supply","trusted-app-and-account-host","native-enforcement-and-retirement","connected-source-contract"].map(name=>[name,sha(`worker:${name}`)]));
    const input={payloadDigest:sha(await readFile(join(f.resources,"runtime-payload-manifest.json"))),supportProfile:f.profile,issuedAt:"2026-09-10T00:00:00.000Z",expiresAt:"2026-09-11T00:00:00.000Z",ownerReference:"OWNER_TRIAL_DIRECTION.md#sha256=d52aa1c4cd33f5d86592edc34ddc7e6e859702d23ca38e8f50d859598d002ac7",login:{activationId:"trial-login",gateIdentity:"D36" as const,ownerAct:Buffer.from("login owner act\n"),evidence},worker:{activationId:"trial-worker",gateIdentity:"WORKER-TRIAL",ownerAct:Buffer.from("worker owner act\n"),prerequisites}};
    const files=prepareHostedReleaseGovernanceV2(input as any);expect(Object.keys(files).sort()).toEqual([...OWNER_NAMES].sort());
    const worker=JSON.parse(files["worker-purpose-record.json"].bytes.toString("utf8"));expect(worker).toMatchObject({schema:"chirality-codex-worker-purpose-release/v3",trialScope:"local-human-functional-trial",limbs:{"effective-policy":{status:"pending-human-trial"}},prerequisites:{"connected-source-contract":{attempted:true,passed:true,evidenceSha256:prerequisites["connected-source-contract"]}}});
    const acceptance=JSON.parse(files["worker-purpose-acceptance.json"].bytes.toString("utf8"));expect(acceptance).toMatchObject({recordSha256:files["worker-purpose-record.json"].sha256,ownerActSha256:files["worker-owner-act"].sha256,ownerReference:input.ownerReference});
    expect(()=>prepareHostedReleaseGovernanceV2({...input,worker:{...input.worker,prerequisites:{...prerequisites,"connected-source-contract":"0"}}} as any)).toThrow("worker prerequisite evidence");
  });

  it("derives canonical trial observation bytes only from verified payload and successful static identity checks",async()=>{
    const f=await fixture(),inspect=vi.fn(async()=>f.signedIdentity),observed=await observeHostedReleaseTrialSealV1ControlledForTests({resourcesRoot:f.resources,executablePath:join(f.base,"Chirality.app","Contents","MacOS","Chirality")},inspect);
    expect(inspect).toHaveBeenCalledOnce();expect(observed.bytes.at(-1)).toBe(10);expect(observed.sha256).toBe(sha(observed.bytes));
    expect(JSON.parse(observed.bytes.toString("utf8"))).toEqual(observed.observation);
    expect(observed.observation).toMatchObject({outerInventorySha256:f.input.expectedOuterInventorySha256,payloadDigest:expect.stringMatching(/^[a-f0-9]{64}$/),mainCodeDirectoryHash:f.signedIdentity.subject.cdHash,peerRequirementSha256:sha(f.signedIdentity.effectivePeerRequirement),checks:{"signed-app":{attempted:true,passed:true,evidenceSha256:expect.stringMatching(/^[a-f0-9]{64}$/)},"fuses-and-asar":{attempted:true,passed:true},"signed-peer-identity-binding":{attempted:true,passed:true}}});
    const evidence=(schema:string,value:unknown)=>sha(`${JSON.stringify({schema,evidence:value})}\n`);
    expect(observed.observation.checks["signed-app"].evidenceSha256).toBe(evidence("chirality-runtime-trial-signed-app-evidence/v1",{subject:f.signedIdentity.subject,outer:f.signedIdentity.outer}));
    expect(observed.observation.checks["fuses-and-asar"].evidenceSha256).toBe(evidence("chirality-runtime-trial-fuses-and-asar-evidence/v1",{fuses:f.signedIdentity.fuses,asarIntegrity:f.signedIdentity.asarIntegrity,outerInventorySha256:observed.observation.outerInventorySha256,payloadDigest:observed.observation.payloadDigest}));
    expect(observed.observation.checks["signed-peer-identity-binding"].evidenceSha256).toBe(evidence("chirality-runtime-trial-signed-peer-identity-binding-evidence/v1",{predicate:f.signedIdentity.predicate,effectivePeerRequirement:f.signedIdentity.effectivePeerRequirement,subject:f.signedIdentity.subject}));
    await expect(observeHostedReleaseTrialSealV1ControlledForTests({resourcesRoot:f.resources,executablePath:join(f.base,"Chirality.app","Contents","MacOS","Chirality")},async()=>{throw new Error("static inspection failed");})).rejects.toThrow("static inspection failed");
  });

  it("publishes the exact external trial observation and v3 anchor without changing qualified v2",async()=>{
    const f=await fixture({trial:true}),inspect=vi.fn(async()=>f.signedIdentity),installed=await installHostedReleaseAnchorV2ControlledForTests(f.input,inspect);
    expect(installed).toMatchObject({disposition:"created",trialObservationSha256:f.input.trial!.expectedObservationSha256});
    expect(inspect).toHaveBeenCalledTimes(2);expect(inspect).toHaveBeenCalledWith({executablePath:f.input.trial!.executablePath,resourcesPath:f.resources});
    expect(JSON.parse(await readFile(installed.anchorPath,"utf8"))).toMatchObject({schema:"chirality-runtime-release-anchor/v3",postSealObservationSha256:f.input.trial!.expectedObservationSha256});
    expect(await readFile(installed.trialObservationPath!)).toEqual(await readFile(f.input.trial!.observationPath));
  });

  it.each(["limb","prerequisite","expired"] as const)("rejects invalid trial purpose %s before publication",async trialMutation=>{
    const f=await fixture({trial:true,trialMutation});await expect(installHostedReleaseAnchorV2ControlledForTests(f.input,async()=>f.signedIdentity)).rejects.toThrow();
    await expect(readFile(join(f.runtime,"release-authority","v2","release-anchor.json"))).rejects.toMatchObject({code:"ENOENT"});
  });

  it("rejects a trial observation that does not match the maintained signed subject",async()=>{
    const f=await fixture({trial:true}),changed={...f.signedIdentity,subject:{cdHash:"0".repeat(40)}};
    await expect(installHostedReleaseAnchorV2ControlledForTests(f.input,async()=>changed)).rejects.toThrow("does not match signed subject");
  });

  it("publishes deterministic canonical bytes and the real loader consumes them without granting P2",async()=>{
    const f=await fixture(),first=await installHostedReleaseAnchorV2(f.input),bytes=await readFile(first.anchorPath);
    expect(first.disposition).toBe("created");expect(bytes.at(-1)).toBe(10);expect(first.anchorSha256).toBe(sha(bytes));
    await expect(installHostedReleaseAnchorV2(structuredClone(f.input))).resolves.toMatchObject({disposition:"already-identical",anchorSha256:first.anchorSha256});
    let failure:unknown;const loaded=await loadPackagedHostedReleaseBasisControlledForTests({resourcesRoot:f.resources,runtimeDirectory:f.runtime,embeddedRuntime:{electron:"43.2.0",node:"24.13.0",modules:"145",napi:"10",architecture:"arm64"}},async()=>f.profile,error=>{failure=error;});
    if(loaded.status!=="ready")throw failure;expect(isControlledPackagedReleaseBasisForTests(loaded.basis)).toBe(true);
    await expect(startHostedPackagedPrivateBootstrapRuntimeHost({bootstrap:{enabled:true,runtimeDirectory:f.runtime,daemonSocket:join(f.runtime,"daemon.sock"),instructionRoot:loaded.basis.instructionRoot,nativeAddonPath:loaded.basis.nativeAddonPath},basis:loaded.basis,executablePath:join(f.base,"Chirality.app","Contents","MacOS","Chirality")})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
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
    const {parseProvisionHostedReleaseArguments,runProvisionHostedReleaseAnchorV2,parseObserveHostedReleaseTrialSealArguments,runObserveHostedReleaseTrialSealV1,parseObserveAccountFreeLoginArguments,runObserveAccountFreeLoginV2}=await import("../tools/provision-hosted-release-anchor-v2.mjs");
    const parsed=parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2"]);
    expect(parsed).toMatchObject({resourcesRoot:"/Applications/Chirality.app/Contents/Resources",runtimeDirectory:"/private/runtime",acceptedGovernanceRoot:"/private/accepted",login:{gateIdentity:"D36"}});
    const trial=parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2","--trial-observation","/private/accepted-trial/trial.json","--expected-trial-observation-sha256","b".repeat(64),"--trial-executable","/Applications/Chirality.app/Contents/MacOS/Chirality"]);
    expect(trial).toMatchObject({trial:{observationPath:"/private/accepted-trial/trial.json",expectedObservationSha256:"b".repeat(64),executablePath:"/Applications/Chirality.app/Contents/MacOS/Chirality"}});
    expect(()=>parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2","--trial-observation","/private/accepted-trial/trial.json","--expected-trial-observation-sha256","b".repeat(64)])).toThrow("Usage:");
    const install=vi.fn(async(input:unknown)=>({input}));await runProvisionHostedReleaseAnchorV2(["--app","/Applications/Chirality.app","--runtime-directory","/private/runtime","--accepted-governance-root","/private/accepted","--expected-outer-inventory-sha256","a".repeat(64),"--login-activation-id","release-v2","--worker-activation-id","release-v2","--worker-gate-identity","WORKER-V2"],install);expect(install).toHaveBeenCalledWith(parsed);
    const observedInput=parseObserveHostedReleaseTrialSealArguments(["--app","/Applications/Chirality.app"]);expect(observedInput).toEqual({resourcesRoot:"/Applications/Chirality.app/Contents/Resources",executablePath:"/Applications/Chirality.app/Contents/MacOS/Chirality"});
    const observe=vi.fn(async()=>({bytes:Buffer.from("observation\n")}));await expect(runObserveHostedReleaseTrialSealV1(["--app","/Applications/Chirality.app"],observe)).resolves.toEqual({bytes:Buffer.from("observation\n")});expect(observe).toHaveBeenCalledWith(observedInput);
    const ownerRoot=await realpath(await mkdtemp(join(tmpdir(),"account-free-owner-tool-")));roots.push(ownerRoot);const recipePath=join(ownerRoot,"recipe.json"),evidence=Object.fromEntries([["signatureEvidenceSha256","signature"],["sourceCorrespondenceEvidenceSha256","source"],["xpcRecordSha256","xpc"],["groupedRecordSha256","grouped"]].map(([field,value])=>[field,{path:join(ownerRoot,`${field}.json`),bytes:Buffer.from(value)}]));
    for(const value of Object.values(evidence)){await writeFile(value.path,value.bytes,{mode:0o600});await chmod(value.path,0o600);}const recipe={schema:"chirality-account-free-login-observation-recipe/v1",runId:"11111111-1111-4111-8111-111111111111",nativeAddon:Object.fromEntries(Object.entries(evidence).map(([field,value])=>[field,sha(value.bytes)]))};await writeFile(recipePath,JSON.stringify(recipe),{mode:0o600});await chmod(recipePath,0o600);
    const accountFreeArgs=["--runtime-directory",join(ownerRoot,"runtime"),"--resources-root",join(ownerRoot,"candidate","Resources"),"--recipe",recipePath,"--signature-evidence",evidence.signatureEvidenceSha256.path,"--source-correspondence-evidence",evidence.sourceCorrespondenceEvidenceSha256.path,"--xpc-record",evidence.xpcRecordSha256.path,"--grouped-record",evidence.groupedRecordSha256.path];
    expect(parseObserveAccountFreeLoginArguments(accountFreeArgs)).toEqual({runtimeDirectory:join(ownerRoot,"runtime"),resourcesPath:join(ownerRoot,"candidate","Resources"),recipePath,evidencePaths:{signatureEvidenceSha256:evidence.signatureEvidenceSha256.path,sourceCorrespondenceEvidenceSha256:evidence.sourceCorrespondenceEvidenceSha256.path,xpcRecordSha256:evidence.xpcRecordSha256.path,groupedRecordSha256:evidence.groupedRecordSha256.path}});
    const accountFreeObserve=vi.fn(async(input:unknown)=>({schema:"chirality-account-free-login-observation-result/v1",input}));await runObserveAccountFreeLoginV2(accountFreeArgs,accountFreeObserve);
    expect(accountFreeObserve).toHaveBeenCalledWith({runtimeDirectory:join(ownerRoot,"runtime"),resourcesPath:join(ownerRoot,"candidate","Resources"),evidencePaths:{signatureEvidenceSha256:evidence.signatureEvidenceSha256.path,sourceCorrespondenceEvidenceSha256:evidence.sourceCorrespondenceEvidenceSha256.path,xpcRecordSha256:evidence.xpcRecordSha256.path,groupedRecordSha256:evidence.groupedRecordSha256.path},recipe});
    expect(()=>parseObserveAccountFreeLoginArguments(["--runtime-directory","relative","--resources-root","/private/Resources","--recipe","/private/recipe.json"])).toThrow("Usage:");
    expect(()=>parseObserveHostedReleaseTrialSealArguments(["--app","relative.app"])).toThrow("Usage:");
    expect(()=>parseProvisionHostedReleaseArguments(["--app","/Applications/Chirality.app","--app","/Applications/Other.app"])).toThrow("Usage:");
  });

  it("writes six create-only private files from one explicit governance recipe",async()=>{
    const f=await fixture(),recipePath=join(f.base,"governance-recipe.json"),outputDirectory=join(f.base,"prepared-six"),loginNames=["exact-supplier","keyring-backend","plaintext-fallback-absent","process-containment","storage-isolation","provider-network","bounded-protocol-purpose","retirement"],workerNames=["signed-payload-and-supply","trusted-app-and-account-host","native-enforcement-and-retirement","connected-source-contract"];
    const recipe={payloadDigest:sha(await readFile(join(f.resources,"runtime-payload-manifest.json"))),supportProfile:f.profile,issuedAt:"2026-09-10T00:00:00.000Z",expiresAt:"2026-09-11T00:00:00.000Z",ownerReference:"OWNER_TRIAL_DIRECTION.md#sha256=d52aa1c4cd33f5d86592edc34ddc7e6e859702d23ca38e8f50d859598d002ac7",login:{activationId:"trial-login",gateIdentity:"D36",ownerActPath:join(f.accepted,"login-owner-act"),evidence:Object.fromEntries(loginNames.map(name=>[name,sha(name)]))},worker:{activationId:"trial-worker",gateIdentity:"WORKER-TRIAL",ownerActPath:join(f.accepted,"worker-owner-act"),prerequisites:Object.fromEntries(workerNames.map(name=>[name,sha(name)]))}};await writeFile(recipePath,JSON.stringify(recipe),{mode:0o600});await chmod(recipePath,0o600);
    const {runPrepareHostedReleaseGovernanceV2}=await import("../tools/provision-hosted-release-anchor-v2.mjs"),result=await runPrepareHostedReleaseGovernanceV2(["--recipe",recipePath,"--output",outputDirectory],prepareHostedReleaseGovernanceV2);expect(Object.keys(result.files).sort()).toEqual([...OWNER_NAMES].sort());
    for(const name of OWNER_NAMES){expect((await stat(join(outputDirectory,name))).mode&0o777).toBe(0o600);expect(sha(await readFile(join(outputDirectory,name)))).toBe(result.files[name].sha256);}
    await expect(runPrepareHostedReleaseGovernanceV2(["--recipe",recipePath,"--output",outputDirectory],prepareHostedReleaseGovernanceV2)).rejects.toThrow();
  });
});
