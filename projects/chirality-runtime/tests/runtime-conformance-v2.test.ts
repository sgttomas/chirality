import { createHash } from "node:crypto";
import { mkdtemp, mkdir, realpath, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { afterEach, describe, expect, it } from "vitest";
import {
  compareRuntimeUtf8V2, decodeRuntimePayloadManifestV2, encodeRuntimeArtifactInventoryV2,
  encodeRuntimePayloadManifestV2, encodeRuntimePolicyParameterDeclarationV2,
  observeRuntimeSupportProfileFromPayloadV2, observeRuntimeSupportProfileV2, runtimePolicyParameterSchemaDigestV2, verifyPackagedRuntimeBasisV2,
  runtimeStageCPolicyParameterSchemaDigest, RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,
  type RuntimeArtifactInventoryV2, type RuntimePayloadEntryV2, type RuntimePayloadManifestV2,
  type RuntimeSupportProfileV2
} from "../packages/core/src/runtime-conformance-v2.js";

const created: string[] = [];
const hash = (value: string | Buffer) => createHash("sha256").update(value).digest("hex");
const artifact = (relativePath: string, bytes: Buffer) => ({ relativePath, size: bytes.length, sha256: hash(bytes) });

function profile(entries: RuntimePayloadEntryV2[]): RuntimeSupportProfileV2 {
  const files = new Map(entries.filter((entry): entry is Extract<RuntimePayloadEntryV2,{type:"file"}> => entry.type === "file").map(entry => [entry.relativePath, entry]));
  const without = {
    schema: "chirality-runtime-support-profile/v2" as const, macosProductVersion: "26.6.2", macosBuildVersion: "25G83", architecture: "arm64" as const,
    electronVersion: "43.2.0", nodeVersion: "24.13.0", nodeModuleAbi: "145", napiVersion: "10",
    osMeasurement: { executablePath: "/usr/bin/sw_vers" as const, executableSha256: hash("sw"), executableSize: 2 },
    sandboxExec: { path: "/usr/bin/sandbox-exec" as const, sha256: hash("sandbox"), size: 7 },
    nativeAdmission: { contract: "chirality-native-admission/v1" as const, sha256: files.get("native/chirality_native_admission.node")!.sha256, size: files.get("native/chirality_native_admission.node")!.size, napiVersion: "6" },
    supplier: { version: "1.2.3", sha256: files.get("supplier/codex")!.sha256, size: files.get("supplier/codex")!.size, appServerProtocolDigest: hash("protocol"), authorityContract: "chirality.local-admission-authority/1.0" as const, identityContract: "chirality-supplier-account-identity/1" as const },
    compiler: { outerPolicySchema: "chirality-codex-outer-policy/v2" as const, nativePolicyIdentityVersion: 10 as const, sourceDigest: hash("compiler"), parameterSchemaDigest: runtimePolicyParameterSchemaDigestV2() },
    immutableSystemRoots: ["/System","/usr"], kernelHelperContractDigest: hash("kernel")
  };
  return { ...without, profileDigest: hash(`${JSON.stringify(without)}\n`) };
}

async function fixture(delayFile=false): Promise<{ root: string; manifest: RuntimePayloadManifestV2 }> {
  const root = await realpath(await mkdtemp(join(tmpdir(), "runtime-v2-"))); created.push(root);
  const files = new Map<string,Buffer>([
    ["app.asar",Buffer.from("app")], ["instruction-root/instruction-bundle-manifest.json",Buffer.from("bundle")],
    ["native/chirality_native_admission.node",Buffer.from("native")], ["runtime-cli/chirality-cli.mjs",Buffer.from("cli")],
    ["runtime-cli/chirality-cli.mjs.map",Buffer.from("map")], ["runtime-contracts/runtime-policy-parameters-v2.json",encodeRuntimePolicyParameterDeclarationV2()],
    ["supplier/codex",Buffer.from("supplier")]
  ]);
  if(delayFile)files.set("zz-delay",Buffer.alloc(32*1024*1024,7));
  for (const [path, bytes] of files) { await mkdir(join(root, path, ".."), { recursive: true }); await writeFile(join(root, path), bytes); }
  const directories = ["instruction-root","native","runtime-cli","runtime-contracts","supplier"].map(relativePath => ({ relativePath, type: "directory" as const }));
  const entries: RuntimePayloadEntryV2[] = [...directories, ...[...files].map(([relativePath, bytes]) => ({ ...artifact(relativePath,bytes), type: "file" as const }))].sort((a,b) => compareRuntimeUtf8V2(a.relativePath,b.relativePath));
  const roots = [...new Set(entries.map(entry=>entry.relativePath.split("/")[0]!))].sort(compareRuntimeUtf8V2);
  const support = profile(entries);
  const manifest: RuntimePayloadManifestV2 = { schema: "chirality-runtime-payload-manifest/v2", dependencyResolutionDigest: hash("deps"), roots, supportProfiles: [support], entries };
  const manifestBytes = encodeRuntimePayloadManifestV2(manifest); await writeFile(join(root,"runtime-payload-manifest.json"),manifestBytes);
  const governancePaths = ["runtime-governance/v2/login-purpose-record.json","runtime-governance/v2/login-purpose-acceptance.json","runtime-governance/v2/login-owner-act","runtime-governance/v2/worker-purpose-record.json","runtime-governance/v2/worker-purpose-acceptance.json","runtime-governance/v2/worker-owner-act"] as const;
  const governance = [] as Array<{relativePath:typeof governancePaths[number];size:number;sha256:string}>;
  for (const path of governancePaths) { const bytes=Buffer.from(`governance:${path}`); await mkdir(join(root,path,".."),{recursive:true}); await writeFile(join(root,path),bytes); governance.push(artifact(path,bytes) as typeof governance[number]); }
  const inventory: RuntimeArtifactInventoryV2 = { schema:"chirality-runtime-artifact-inventory/v2",payloadManifest:artifact("runtime-payload-manifest.json",manifestBytes) as RuntimeArtifactInventoryV2["payloadManifest"],governance:governance as unknown as RuntimeArtifactInventoryV2["governance"] };
  await writeFile(join(root,"runtime-artifact-inventory-v2.json"),encodeRuntimeArtifactInventoryV2(inventory));
  return { root, manifest };
}

afterEach(async()=>{while(created.length)await rm(created.pop()!,{recursive:true,force:true});});

describe("Runtime conformance v2 canonical basis",()=>{
  it("encodes one canonical byte representation independent of caller key insertion order",async()=>{
    const {manifest}=await fixture();
    const reordered={ entries:manifest.entries, supportProfiles:manifest.supportProfiles, roots:manifest.roots, dependencyResolutionDigest:manifest.dependencyResolutionDigest, schema:manifest.schema } as RuntimePayloadManifestV2;
    expect(encodeRuntimePayloadManifestV2(reordered)).toEqual(encodeRuntimePayloadManifestV2(manifest));
    expect(decodeRuntimePayloadManifestV2(encodeRuntimePayloadManifestV2(reordered))).toEqual(manifest);
  });
  it("verifies the complete fixed partition and rejects an unknown sibling",async()=>{
    const {root}=await fixture();
    await expect(verifyPackagedRuntimeBasisV2({resourcesRoot:root})).resolves.toMatchObject({resourcesRoot:root});
    await writeFile(join(root,"unknown"),"x");
    await expect(verifyPackagedRuntimeBasisV2({resourcesRoot:root})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
  });
  it("rejects the reserved v1 inventory name in a v2 closure",async()=>{
    const {manifest}=await fixture(),legacy={relativePath:"runtime-artifact-inventory.json",type:"file" as const,size:3,sha256:hash("{}\n")};
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,roots:[...manifest.roots,legacy.relativePath].sort(compareRuntimeUtf8V2),entries:[...manifest.entries,legacy].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath))})).toThrow();
  });
  it("rejects a changed payload byte and noncanonical manifest bytes",async()=>{
    const {root,manifest}=await fixture();
    await writeFile(join(root,"supplier/codex"),"changed");
    await expect(verifyPackagedRuntimeBasisV2({resourcesRoot:root})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    const noncanonical=Buffer.from(`${JSON.stringify(manifest,null,2)}\n`);
    expect(()=>decodeRuntimePayloadManifestV2(noncanonical)).toThrow();
  });
  it("rejects phantom roots, undeclared parents, and a false addon N-API contract",async()=>{
    const {manifest}=await fixture();
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,roots:[...manifest.roots,"phantom"].sort(compareRuntimeUtf8V2)})).toThrow();
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,entries:manifest.entries.filter(entry=>entry.relativePath!=="instruction-root")})).toThrow();
    const badProfile={...manifest.supportProfiles[0]!,nativeAdmission:{...manifest.supportProfiles[0]!.nativeAdmission,napiVersion:"10"}};
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,supportProfiles:[badProfile]})).toThrow();
  });
  it("accepts a one-GiB payload declaration without allocating it and rejects the next byte",async()=>{
    const {manifest}=await fixture(),large={relativePath:"supplier/large.data",type:"file" as const,size:RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES,sha256:hash("large")};
    const supportWithout={...manifest.supportProfiles[0]!,supplier:{...manifest.supportProfiles[0]!.supplier,size:RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES}};delete (supportWithout as Partial<RuntimeSupportProfileV2>).profileDigest;
    const support={...supportWithout,profileDigest:hash(`${JSON.stringify(supportWithout)}\n`)} as RuntimeSupportProfileV2;
    const atLimit={...manifest,supportProfiles:[support],entries:[...manifest.entries,large].sort((a,b)=>compareRuntimeUtf8V2(a.relativePath,b.relativePath))};
    expect(()=>encodeRuntimePayloadManifestV2(atLimit)).not.toThrow();
    expect(()=>encodeRuntimePayloadManifestV2({...atLimit,entries:atLimit.entries.map(entry=>entry.relativePath===large.relativePath?{...large,size:RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES+1}:entry)})).toThrow();
    const oversizedWithout={...support,supplier:{...support.supplier,size:RUNTIME_V2_MAX_PAYLOAD_ARTIFACT_BYTES+1}};delete (oversizedWithout as Partial<RuntimeSupportProfileV2>).profileDigest;
    const oversized={...oversizedWithout,profileDigest:hash(`${JSON.stringify(oversizedWithout)}\n`)} as RuntimeSupportProfileV2;
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,supportProfiles:[oversized]})).toThrow();
  });
  it("keeps native-10 and native-11 support profiles explicitly distinct",async()=>{
    const {manifest}=await fixture(),ten=manifest.supportProfiles[0]!;
    const elevenWithout={...ten,compiler:{...ten.compiler,nativePolicyIdentityVersion:11 as const,parameterSchemaDigest:runtimeStageCPolicyParameterSchemaDigest()}};delete (elevenWithout as Partial<RuntimeSupportProfileV2>).profileDigest;
    const eleven={...elevenWithout,profileDigest:hash(`${JSON.stringify(elevenWithout)}\n`)} as RuntimeSupportProfileV2;
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,supportProfiles:[eleven]})).not.toThrow();
    const mismatch={...eleven,compiler:{...eleven.compiler,parameterSchemaDigest:runtimePolicyParameterSchemaDigestV2()}};
    expect(()=>encodeRuntimePayloadManifestV2({...manifest,supportProfiles:[mismatch]})).toThrow();
    expect(eleven.profileDigest).not.toBe(ten.profileDigest);
  });
  it("rejects a caller-nominated embedded runtime and payload mutation during verification",async()=>{
    const {root,manifest}=await fixture(true);
    await expect(observeRuntimeSupportProfileV2({embeddedRuntime:{electron:"0.0.0",node:"0.0.0",modules:"0",napi:"0",architecture:"arm64"},basis:{resourcesRoot:root,inventoryPath:"",payloadManifestPath:"",inventorySha256:"0".repeat(64),payloadDigest:"0".repeat(64),payload:manifest,inventory:{} as never},supplierVersion:"1.2.3",appServerProtocolDigest:"0".repeat(64),immutableSystemRoots:["/System"]})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    let mutated=false;const pending=verifyPackagedRuntimeBasisV2({resourcesRoot:root});const mutation=new Promise<void>(resolve=>setTimeout(()=>{void writeFile(join(root,"app.asar"),"changed").then(()=>{mutated=true;resolve();});},2));
    await expect(pending).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});await mutation;expect(mutated).toBe(true);
  });
  it("uses one support derivation for a frozen pre-governance snapshot and the full accepted basis",async()=>{
    if(process.platform!=="darwin"||process.arch!=="arm64")return;
    const {root}=await fixture(),basis=await verifyPackagedRuntimeBasisV2({resourcesRoot:root});
    const versions=process.versions as Record<string,string|undefined>,prior=versions.electron;Object.defineProperty(versions,"electron",{value:"43.2.0",configurable:true});
    try{
      const common={embeddedRuntime:{electron:"43.2.0",node:process.versions.node,modules:process.versions.modules!,napi:process.versions.napi!,architecture:"arm64"},supplierVersion:"1.2.3",appServerProtocolDigest:hash("protocol"),immutableSystemRoots:["/System","/usr"],nativePolicyIdentityVersion:11 as const};
      const pre=await observeRuntimeSupportProfileFromPayloadV2({...common,resourcesRoot:root,payloadEntries:basis.payload.entries});
      const full=await observeRuntimeSupportProfileV2({...common,basis});expect(pre).toEqual(full);
      await expect(observeRuntimeSupportProfileFromPayloadV2({...common,resourcesRoot:root,payloadEntries:basis.payload.entries.map(entry=>entry.relativePath==="supplier/codex"&&entry.type==="file"?{...entry,sha256:"0".repeat(64)}:entry)})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
      await writeFile(join(root,"app.asar"),"changed-compiler-byte");await expect(observeRuntimeSupportProfileFromPayloadV2({...common,resourcesRoot:root,payloadEntries:basis.payload.entries})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
    }finally{Object.defineProperty(versions,"electron",{value:prior,configurable:true});}
  });
  it("rejects governance drift while the complete payload observation is in flight",async()=>{
    const {root}=await fixture(true);let mutated=false;
    const pending=verifyPackagedRuntimeBasisV2({resourcesRoot:root});
    const mutation=new Promise<void>(resolve=>setTimeout(()=>{void writeFile(join(root,"runtime-governance/v2/login-purpose-record.json"),"changed").then(()=>{mutated=true;resolve();});},10));
    await expect(pending).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});await mutation;expect(mutated).toBe(true);
  });
});
