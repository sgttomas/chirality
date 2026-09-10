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


import {RuntimeMethodService} from "/private/tmp/chirality-v3-adoption-20260909/projects/chirality-runtime/packages/core/src/runtime-method-service.ts";
const qa={adapterId:"stub",providerId:"stub",qualificationId:"historical-a",admissionSha256:"a".repeat(64),evidenceClass:"native-adapter-qualified" as const};
const qb={...qa,qualificationId:"current-b",admissionSha256:"b".repeat(64)};
function rev(number:number,q=qa){return {revision:number,sourceEvent:{qualificationState:"qualified" as const,eventId:`native-${number}`,occurredAt:"2026-09-09T00:00:00Z",qualification:q,plan:{title:`Recorded plan ${number}`}}};}
async function planFixture(){let qualification=qa;let available=true;let fail=false;let revisions=[rev(1)];let providerCalls=0;
 const registry={async capability(){if(fail)throw new Error("current registry offline");return available?{schemaVersion:"chirality.native-plan-capability/v3",status:"qualified",qualification}:{schemaVersion:"chirality.native-plan-capability/v3",status:"unavailable",reason:"No current qualified adapter"};},async revisions(){if(fail)throw new Error("current registry offline");return {schemaVersion:"chirality.native-plan-revisions/v3",status:"qualified",qualification,revisions};}};
 const f=await setup(async function*(){providerCalls++;yield {type:"process:exit",data:{exitCode:0}};},registry);const session=await f.service.createSession({projectId:"v3-api"});
 await f.service.listNativePlanRevisions("v3-api",session.sessionId);
 return {...f,session,setUnavailable(){available=false},setB(){qualification=qb;revisions=[rev(1),rev(2,qb)]},setOffline(){fail=true},providerCalls:()=>providerCalls};
}
it("exports admitted history after unavailable capability and real store/service recreation",async()=>{const f=await planFixture();f.setUnavailable();
 await f.service.exportNativePlan("v3-api",f.session.sessionId,{revision:1,targetRelativePath:"plans/while-unavailable.json"});
 const restarted=new RuntimeMethodService(f.projects,new SessionStore(f.runtime,f.projects),new EngineRegistry());
 expect(await restarted.getNativePlanCapability("v3-api",f.session.sessionId)).toMatchObject({status:"unavailable"});
 expect((await restarted.listNativePlanRevisions("v3-api",f.session.sessionId)).revisions).toEqual([rev(1)]);
 await restarted.exportNativePlan("v3-api",f.session.sessionId,{revision:1,targetRelativePath:"plans/after-restart.json"});
 expect(JSON.parse(await readFile(join(f.projectRoot,"plans/after-restart.json"),"utf8"))).toEqual(rev(1).sourceEvent.plan);
 await drain(f.service.runSessionTurn("v3-api",f.session.sessionId,{message:"native stays blocked",interactionMode:"native-plan"}));expect(f.providerCalls()).toBe(0);
});
it("retains old qualification while admitting a new revision under current qualification",async()=>{const f=await planFixture();f.setB();
 const history=await f.service.listNativePlanRevisions("v3-api",f.session.sessionId);expect(history.revisions).toEqual([rev(1),rev(2,qb)]);
 await f.service.exportNativePlan("v3-api",f.session.sessionId,{revision:1,targetRelativePath:"plans/old-under-new.json"});
 expect(JSON.parse(await readFile(join(f.projectRoot,"plans/old-under-new.json"),"utf8"))).toEqual(rev(1).sourceEvent.plan);
});
it("retains validated historical export during current registry failure",async()=>{const f=await planFixture();f.setOffline();
 expect((await f.service.listNativePlanRevisions("v3-api",f.session.sessionId)).revisions).toEqual([rev(1)]);
 await f.service.exportNativePlan("v3-api",f.session.sessionId,{revision:1,targetRelativePath:"plans/while-offline.json"});
});
it("rejects caller-supplied trusted markers with valid recomputed hashes and persisted content tampering",async()=>{const f=await planFixture();const revision=rev(2);
 const digest=(v:any)=>createHash("sha256").update(JSON.stringify(v)).digest("hex");
 await expect(f.sessions.instructionBases.appendHistory("v3-api",f.session.sessionId,{type:"native-plan.revised",revision,provenance:"trusted-native-plan-registry",revisionSha256:digest(revision),qualificationSha256:digest(revision.sourceEvent.qualification)} as any)).rejects.toBeDefined();
 const path=join(f.runtime,"projects/v3-api/sessions",f.session.sessionId,"instruction-history.jsonl");const lines=(await readFile(path,"utf8")).trimEnd().split("\n");const record=JSON.parse(lines.at(-1)!);record.revision.sourceEvent.plan={title:"tampered"};lines[lines.length-1]=JSON.stringify(record);await writeFile(path,lines.join("\n")+"\n");
 const restarted=new RuntimeMethodService(f.projects,new SessionStore(f.runtime,f.projects),new EngineRegistry());
 await expect(restarted.listNativePlanRevisions("v3-api",f.session.sessionId)).rejects.toBeDefined();
 await expect(restarted.exportNativePlan("v3-api",f.session.sessionId,{revision:1,targetRelativePath:"plans/tampered.json"})).rejects.toBeDefined();
});
