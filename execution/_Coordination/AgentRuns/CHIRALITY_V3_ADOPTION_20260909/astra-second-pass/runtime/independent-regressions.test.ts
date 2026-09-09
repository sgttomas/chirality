import { mkdir, mkdtemp, readFile, writeFile, rm, symlink } from "node:fs/promises";
import { createHash } from "node:crypto";
import { join, resolve } from "node:path";
import { describe, expect, it } from "vitest";
import type { AgentEnginePort, AgentEngineRunInput, OmlxControlPort } from "@chirality/runtime-contracts";
import { AuthRegistry, EngineRegistry, ProjectRegistry, ResidencyCoordinator, RuntimeService, SessionStore, TurnCoordinator } from "@chirality/runtime-core";
const evidenceRoot = '/private/tmp/chirality-v3-adoption-20260909/execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/astra-second-pass/runtime';
async function drain(source: AsyncIterable<unknown>) { for await (const event of source) {} }
async function setup(startTurn: AgentEnginePort["startTurn"], nativePlan?: any, successor?: Partial<Pick<AgentEnginePort, "preflight" | "prepareContextSuccessor" | "cancelContextSuccessor">>) {
  const directory = await mkdtemp(join(evidenceRoot, "fixture-"));
  const projectRoot = join(directory, "project");
  const runtime = join(directory, "runtime");
  await mkdir(join(projectRoot, ".chirality", "workflows", "fixture-method"), { recursive: true });
  await writeFile(join(projectRoot, "AGENTS.md"), "# Fixture project\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "fixture-method", "WORKFLOW.md"), "---\nname: fixture-method\ndescription: Runtime API fixture method.\n---\n\n# Method body\nExact fixture instructions.\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "fixture-method", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELP_HUMAN"] })}\n`, "utf8");
  await mkdir(join(projectRoot, ".chirality", "workflows", "lazy-method"), { recursive: true });
  await writeFile(join(projectRoot, ".chirality", "workflows", "lazy-method", "WORKFLOW.md"), "---\nname: lazy-method\ndescription: Dynamically loaded fixture.\n---\n\nLAZY_METHOD_EXACT\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "lazy-method", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELP_HUMAN"] })}\n`, "utf8");
  await mkdir(join(projectRoot, ".chirality", "workflows", "lazy-method", "resources"), { recursive: true });
  await writeFile(join(projectRoot, ".chirality", "workflows", "lazy-method", "resources", "note.md"), "LAZY_RESOURCE_EXACT\n", "utf8");
  await mkdir(join(projectRoot, ".chirality", "workflows", "manager-method"), { recursive: true });
  await writeFile(join(projectRoot, ".chirality", "workflows", "manager-method", "WORKFLOW.md"), "---\nname: manager-method\ndescription: Manager routed fixture.\n---\n\nMANAGER_BODY_MUST_NOT_BE_SUPPLIED\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "manager-method", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELPS_HUMANS"] })}\n`, "utf8");
  await mkdir(join(projectRoot, ".chirality", "workflows", "restricted-method"), { recursive: true });
  await writeFile(join(projectRoot, ".chirality", "workflows", "restricted-method", "WORKFLOW.md"), "---\nname: restricted-method\ndescription: Restricted dynamic fixture.\n---\n\nRESTRICTED_BODY\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "restricted-method", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELP_HUMAN"], tools: { capabilities: ["bash"], commands: ["git status"] } })}\n`, "utf8");
  await mkdir(join(projectRoot, ".chirality", "workflows", "manager-readonly"), { recursive: true });
  await writeFile(join(projectRoot, ".chirality", "workflows", "manager-readonly", "WORKFLOW.md"), "---\nname: manager-readonly\ndescription: Read-only manager fixture.\n---\n\nREAD_ONLY_MANAGER_BODY\n", "utf8");
  await writeFile(join(projectRoot, ".chirality", "workflows", "manager-readonly", "execution.json"), `${JSON.stringify({ schema_version: 1, compatible_roles: ["HELPS_HUMANS"], tools: { capabilities: ["read"] } })}\n`, "utf8");
  const manifestPath = join(projectRoot, "chirality.project.json");
  await writeFile(manifestPath, `${JSON.stringify({ schemaVersion: "chirality.project/v2", projectId: "v3-api", displayName: "v3 API", workingRoot: ".", instructionRoot: { mode: "runtime" }, defaultExecutionRoot: ".", profiles: { domain: [], capability: [], dataBoundary: [] }, enabledAdapterIds: ["stub"], embeddedUi: { declared: false } })}\n`, "utf8");
  const instructionRoot = join(directory, "instructions");
  await mkdir(join(instructionRoot,"agents"),{recursive:true});
  for (const path of ["AGENTS.md","agents/registry.json","agents/AGENT_HELP_HUMAN.md","agents/AGENT_HELPS_HUMANS.md","agents/AGENT_WORKING_ITEMS.md","agents/AGENT_TASK.md"]) await writeFile(join(instructionRoot,path),await readFile(resolve(process.cwd(),"../..",path)));

  const projects = new ProjectRegistry(runtime, { CHIRALITY_INSTRUCTION_ROOT: instructionRoot });
  const sessions = new SessionStore(runtime, projects);
  const engines = new EngineRegistry();
  engines.register({ descriptor: { adapterId: "stub", providerId: "stub", capabilities: { credentials: false, tools: true, attachments: true, interruption: true, durableResume: true, compaction: true } }, subject: "stub", async preflight() {}, startTurn, async interrupt() {}, ...successor });
  const control: OmlxControlPort = { async listStatus() { return []; }, async load() {}, async unload() {} };
  const residency = new ResidencyCoordinator(control, runtime);
  const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(runtime), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} }, undefined, undefined, undefined, { async resolve({ agentType }) { return { role: agentType === 0 ? "agent0" : "agent1", engineSelection: { adapterId: "stub", providerId: "stub", model: "fixture" } }; } }, nativePlan);
  const registered = await service.registerProject(manifestPath, "test", "v3-api-test");
  return { directory, projectRoot, runtime, projects, sessions, service };
}


const successorHooks={
 async prepareContextSuccessor(request:any) {const continuationText=request.continuationContext.transcript;return {preparationId:`probe-successor-${Date.now()}`,adapterId:"stub",providerId:"stub",predecessorEngineSessionId:request.predecessorEngineSessionId,continuationText,continuationSha256:createHash("sha256").update(continuationText).digest("hex"),targetBasisId:request.toBasisPreview.id,targetReference:`${request.toBasisPreview.id}:${request.toBasisPreview.sha256}`};},async cancelContextSuccessor(){}
};
function provider(inputs:AgentEngineRunInput[],load=false):AgentEnginePort["startTurn"] {return async function*(input) {
 inputs.push(input);yield {type:"session:init",data:{engineSessionId:input.contextSuccessor?"new-provider-span":input.session.engineSessionId??"old-provider-span",adapterId:"stub",providerId:"stub",model:"fixture"}};
 if(load&&inputs.length===1) await input.runtimeTools!.find(t=>t.name==="chirality_load_method")!.execute({methods:[{kind:"workflow",name:"manager-readonly"}]},new AbortController().signal);
 yield {type:"process:exit",data:{exitCode:0}};
};}
describe("Independent Runtime repaired-behavior checks",()=>{
 it("retains dynamic method restrictions until explicit safe removal",async()=>{
  const inputs:AgentEngineRunInput[]=[];const f=await setup(provider(inputs,true),undefined,successorHooks);
  const session=await f.service.createSession({projectId:"v3-api",roleId:"HELPS_HUMANS"});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"load",opts:{tools:["read"]}}));
  expect((await f.sessions.get("v3-api",session.sessionId)).selectedMethods).toContainEqual(expect.objectContaining({name:"manager-readonly"}));
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"must not widen",opts:{tools:["bash"]}}));
  expect(inputs).toHaveLength(1);
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"continue read-only",opts:{tools:["read"]}}));
  expect(inputs).toHaveLength(2);expect(inputs[1].contextSuccessor).toBeUndefined();
  expect(inputs[1].instructionContext!.supplied.some(e=>e.content.includes("READ_ONLY_MANAGER_BODY"))).toBe(true);
  await f.service.replaceSelectedMethods("v3-api",session.sessionId,{methods:[],boundaryConfirmed:true});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"deliberately stopped",opts:{tools:["bash"]}}));
  expect(inputs).toHaveLength(3);expect(inputs[2].contextSuccessor).toBeDefined();expect(inputs[2].opts.tools).toContain("bash");
  expect(inputs[2].instructionContext!.supplied.some(e=>e.content.includes("READ_ONLY_MANAGER_BODY"))).toBe(false);
 });
 it("rejects body drift, then permits explicit same-reference refresh through successor",async()=>{
  const inputs:AgentEngineRunInput[]=[];const f=await setup(provider(inputs),undefined,successorHooks);
  const methods=[{kind:"workflow" as const,name:"fixture-method"}];const session=await f.service.createSession({projectId:"v3-api",selectedMethods:methods});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"first"}));
  const path=join(f.projectRoot,".chirality/workflows/fixture-method/WORKFLOW.md");await writeFile(path,(await readFile(path,"utf8")).replace("Exact fixture instructions.","REVISED_EXACT_BODY"));
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"unapproved refresh"}));expect(inputs).toHaveLength(1);
  await f.service.replaceSelectedMethods("v3-api",session.sessionId,{methods,boundaryConfirmed:true});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"approved refresh"}));expect(inputs).toHaveLength(2);expect(inputs[1].contextSuccessor).toBeDefined();
  expect(inputs[1].instructionContext!.supplied.some(e=>e.content.includes("REVISED_EXACT_BODY"))).toBe(true);
 });
 it("rejects automatically loaded project instructions outside their authorized root",async()=>{
  const f=await setup(provider([]));const session=await f.service.createSession({projectId:"v3-api"});
  const outside=join(f.directory,"outside-project.txt");await writeFile(outside,"OUTSIDE_SENTINEL");await rm(join(f.projectRoot,"AGENTS.md"));await symlink(outside,join(f.projectRoot,"AGENTS.md"));
  await expect(f.service.resolveSelectedContext("v3-api",session.sessionId,{roleId:"HELP_HUMAN",interactionMode:"chat",permissionMode:"ask",methods:[]})).rejects.toBeDefined();
 });
 it("rejects source drift after successor preparation before provider execution",async()=>{
  const inputs:AgentEngineRunInput[]=[];const f=await setup(provider(inputs),undefined,successorHooks);const session=await f.service.createSession({projectId:"v3-api"});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"first"}));
  await f.service.replaceSelectedMethods("v3-api",session.sessionId,{methods:[{kind:"workflow",name:"fixture-method"}],boundaryConfirmed:true});
  const path=join(f.projectRoot,".chirality/workflows/fixture-method/WORKFLOW.md");await writeFile(path,(await readFile(path,"utf8")).replace("Exact fixture instructions.","CHANGED_AFTER_PREPARATION"));
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"continue"}));expect(inputs).toHaveLength(1);
  expect((await f.sessions.instructionBases.history("v3-api",session.sessionId)).some(x=>x.type==="provider-span.continued")).toBe(false);
 });
 it("rejects policy-only source widening until explicit refresh",async()=>{
  const inputs:AgentEngineRunInput[]=[];const f=await setup(provider(inputs));const session=await f.service.createSession({projectId:"v3-api",roleId:"HELPS_HUMANS",selectedMethods:[{kind:"workflow",name:"manager-readonly"}]});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"first",opts:{tools:["read"]}}));
  await writeFile(join(f.projectRoot,".chirality/workflows/manager-readonly/execution.json"),JSON.stringify({schema_version:1,compatible_roles:["HELPS_HUMANS"],tools:{capabilities:["read","bash"]}}));
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"must not widen",opts:{tools:["bash"]}}));expect(inputs).toHaveLength(1);
 });
 it("keeps explicit permission controls separate from source drift",async()=>{
  const inputs:AgentEngineRunInput[]=[];const f=await setup(provider(inputs));const session=await f.service.createSession({projectId:"v3-api",roleId:"HELPS_HUMANS",permissionMode:"ask"});
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"first",opts:{tools:["read"]}}));
  await drain(f.service.turns.run("v3-api",session.sessionId,{message:"read-only now",permissionMode:"readOnly",opts:{tools:["read"]}}));
  expect(inputs).toHaveLength(2);expect(inputs[1].contextSuccessor).toBeUndefined();expect(inputs[1].opts.mode).toBe("readOnly");
 });
});

it("keeps a coherent dynamic baseline after concurrent method loads",async()=>{
 const inputs:AgentEngineRunInput[]=[];
 const f=await setup(async function*(input){
  inputs.push(input); yield {type:"session:init",data:{engineSessionId:"parallel-span",adapterId:"stub",providerId:"stub",model:"fixture"}};
  if(inputs.length===1){const loader=input.runtimeTools!.find(t=>t.name==="chirality_load_method")!;await Promise.all(["fixture-method","lazy-method"].map(name=>loader.execute({methods:[{kind:"workflow",name}]},new AbortController().signal)));}
  yield {type:"process:exit",data:{exitCode:0}};
 });
 const session=await f.service.createSession({projectId:"v3-api"});
 await drain(f.service.turns.run("v3-api",session.sessionId,{message:"parallel loads",opts:{tools:[]}}));
 expect((await f.sessions.get("v3-api",session.sessionId)).selectedMethods).toHaveLength(2);
 await drain(f.service.turns.run("v3-api",session.sessionId,{message:"continue both",opts:{tools:[]}}));
 expect(inputs).toHaveLength(2);
});
