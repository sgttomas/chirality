import { mkdtemp, mkdir, writeFile, rename, symlink, link, rm } from "node:fs/promises";
import * as fs from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it, vi } from "vitest";
import { GovernedAgent1RunCoordinator, type GovernedAgent1RunOptions } from "../packages/core/src/agent1-run-coordinator.js";
import type { RuntimeToolDefinition } from "@chirality/runtime-contracts";
vi.mock("node:fs/promises", async (importOriginal) => ({ ...await importOriginal<typeof import("node:fs/promises")>() }));
const roots: string[] = [];
afterEach(async () => { vi.restoreAllMocks(); await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true, force: true }))); });
async function fixture() {
  const temp = await fs.realpath(await mkdtemp(join(tmpdir(), "bound-core-"))); roots.push(temp);
  const root = join(temp, "project"); await mkdir(join(root, "docs"), { recursive: true });
  const path = join(root, "docs", "file.txt"); await writeFile(path, "approved content");
  const events: any[] = [];
  const coordinator = new GovernedAgent1RunCoordinator({
    protectedPaths: [join(root, "control"), join(root, "transcripts")],
    sessions: { appendEvent: async (_project: string, event: any) => { events.push(event); return event; } }
  } as unknown as GovernedAgent1RunOptions);
  const bind = (relativePath = "docs/file.txt", projectRoot = root) => (coordinator as unknown as {
    readFileTool(input: object): Promise<{ tool: RuntimeToolDefinition; receipt: { completed(): boolean } }>;
  }).readFileTool({ projectId: "project", projectRoot, sessionId: "child", turnId: "turn", relativePath });
  return { root, temp, path, events, bind };
}
const signal = () => new AbortController().signal;
describe("governed bound read identity", () => {
  it("completes the actual receipt without persisting raw content", async () => {
    const f = await fixture(); const { tool, receipt } = await f.bind(); expect(receipt.completed()).toBe(false);
    expect(await tool.execute({}, signal())).toEqual({ path: "docs/file.txt", content: "approved content" });
    expect(receipt.completed()).toBe(true);
    expect(f.events.map(event => event.type)).toEqual(["tool.permission", "tool.started", "tool.completed"]);
    expect(JSON.stringify(f.events)).not.toContain("approved content");
  });
  it.each(["../outside", "/etc/passwd", "docs", "control/secret", "transcripts/secret"])("rejects path %s", async relativePath => {
    const f = await fixture();
    for (const directory of ["control", "transcripts"]) { await mkdir(join(f.root, directory)); await writeFile(join(f.root, directory, "secret"), "secret"); }
    await expect(f.bind(relativePath)).rejects.toThrow(); expect(f.events).toEqual([]);
  });
  it.each(["symlink", "hardlink", "oversize"])("rejects %s at authorization", async kind => {
    const f = await fixture();
    if (kind === "oversize") await writeFile(f.path, Buffer.alloc(1048577));
    else if (kind === "hardlink") await link(f.path, join(f.root, "alias"));
    else { await rename(f.path, f.path + ".saved"); await symlink(f.path + ".saved", f.path); }
    await expect(f.bind()).rejects.toThrow();
  });
  it.each(["leaf", "directory", "root", "rewrite", "inode", "oversize"])("rejects %s replacement after binding", async kind => {
    const f = await fixture(); const { tool, receipt } = await f.bind();
    if (kind === "rewrite") await writeFile(f.path, "changed content!");
    else if (kind === "oversize") await writeFile(f.path, Buffer.alloc(1048577));
    else if (kind === "inode") { await rename(f.path, f.path + ".saved"); await writeFile(f.path, "approved content"); }
    else { const target = kind === "leaf" ? f.path : kind === "directory" ? join(f.root, "docs") : f.root;
      await rename(target, target + ".saved"); await symlink(target + ".saved", target); }
    await expect(tool.execute({}, signal())).rejects.toThrow();
    expect(receipt.completed()).toBe(false); expect(f.events.map(event => event.type)).not.toContain("tool.completed");
    expect(f.events.at(-1).type).toBe("tool.failed");
  });
  it.each(["after-open", "during-read", "abort"])("rejects %s race on the actual handle", async kind => {
    const f = await fixture(); const { tool, receipt } = await f.bind(); const controller = new AbortController(); const actualOpen = fs.open;
    vi.spyOn(fs, "open").mockImplementation(async (...args: Parameters<typeof fs.open>) => {
      const handle = await actualOpen(...args);
      if (kind === "after-open") { await rename(f.path, f.path + ".saved"); await writeFile(f.path, "approved content"); }
      else { const actualRead = handle.read.bind(handle);
        vi.spyOn(handle, "read").mockImplementation((async (...readArgs: any[]) => {
          const result = await (actualRead as any)(...readArgs);
          if (kind === "abort") controller.abort(); else await writeFile(f.path, "changed content!");
          return result;
        }) as typeof handle.read);
      }
      return handle;
    });
    await expect(tool.execute({}, controller.signal)).rejects.toThrow();
    expect(receipt.completed()).toBe(false); expect(f.events.map(event => event.type)).not.toContain("tool.completed");
  });
  it("rejects nonempty arguments and invalid UTF-8", async () => {
    const f = await fixture(); const first = await f.bind();
    await expect(first.tool.execute({ path: "other" }, signal())).rejects.toThrow(); expect(first.receipt.completed()).toBe(false);
    await writeFile(f.path, Buffer.from([0xff])); const second = await f.bind();
    await expect(second.tool.execute({}, signal())).rejects.toThrow(); expect(second.receipt.completed()).toBe(false);
  });
});

import { CodexAgent1ManagerPort } from "../packages/daemon/src/codex-manager.js";
it('drains actual manager callback timeout before terminal and rejects late overwrite', async () => {
 const realTimeout = globalThis.setTimeout;
 const timer = vi.spyOn(globalThis,'setTimeout').mockImplementation(((fn:any,ms:any,...args:any[])=>realTimeout(fn,ms===120000 ? 30 : ms,...args)) as any);
 let unblock!:()=>void; const blocked = new Promise<void>(resolve=>unblock=resolve);
 let active=false, interrupted=0, polls=0; const records:any[]=[]; const sessions = new Map<string,any>();
 const channel:any={ startManager:async()=>({workerId:'w',generation:'g',pid:1,state:'running'}), nextManager:async()=> { if(polls++) throw Error('unexpected'); return {kind:'callback',callId:'c',threadId:'t',turnId:'u',name:'delegate_agent',args:{sealedBrief:'read'}};}, replyManager:async()=>{}, retire:async()=>{} };
 const manager = new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'});
 const coordinator:any = new GovernedAgent1RunCoordinator({
 projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['codex-app-server','pi']})},
 resolveManagerSelection:async()=>({adapterId:'codex-app-server',providerId:'openai',model:'hosted'}), manager,
 sessions:{create:async(input:any)=>{const s={...input,sessionId:input.role,projectRoot:'/fixture'};sessions.set(s.sessionId,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},
 tools:{bind:async()=>async()=>{}},
 turns:{interrupt:async()=>{interrupted++;unblock();},async *run(){active=true;try {await blocked;yield {type:'chat:complete',data:{text:'late child'}};yield {type:'process:exit',data:{exitCode:0}};}finally{active=false;}}}
 } as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];
 coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));
 coordinator.persistAgentProgress=async()=>{};
 coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 try {
 const events=[];for await(const e of coordinator.run('p',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(e);
 expect(events.at(-1)).toMatchObject({type:'process:exit',data:{exitCode:1}});
 expect(records.at(-1).status).toBe('failed');expect(active).toBe(false);expect(interrupted).toBeGreaterThan(0);
 unblock();await new Promise(resolve=>realTimeout(resolve,10));
 expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child.status).not.toBe('completed');
 } finally {unblock();timer.mockRestore();}
});

it('bounds an uncooperative child drain and fences late callback evidence', async () => {
 const realTimeout = globalThis.setTimeout;
 const timer = vi.spyOn(globalThis,'setTimeout').mockImplementation(((fn:any,ms:any,...args:any[])=>realTimeout(fn,ms===120000 ? 30 : ms,...args)) as any);
 let unblock!:()=>void; const blocked = new Promise<void>(resolve=>unblock=resolve);
 let active=false, interrupted=0, polls=0; const records:any[]=[]; const sessions = new Map<string,any>();
 const channel:any={ startManager:async()=>({workerId:'w',generation:'g',pid:1,state:'running'}), nextManager:async()=> { if(polls++) throw Error('unexpected'); return {kind:'callback',callId:'c',threadId:'t',turnId:'u',name:'delegate_agent',args:{sealedBrief:'read'}};}, replyManager:async()=>{}, retire:async()=>{} };
 const manager = new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'});
 const coordinator:any = new GovernedAgent1RunCoordinator({
 hookDrainTimeoutMs:20, projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['codex-app-server','pi']})},
 resolveManagerSelection:async()=>({adapterId:'codex-app-server',providerId:'openai',model:'hosted'}), manager,
 sessions:{create:async(input:any)=>{const s={...input,sessionId:input.role,projectRoot:'/fixture'};sessions.set(s.sessionId,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},
 tools:{bind:async()=>async()=>{}},
 turns:{interrupt:async()=>{interrupted++;},async *run(){active=true;try {await blocked;yield {type:'chat:complete',data:{text:'late child'}};yield {type:'process:exit',data:{exitCode:0}};}finally{active=false;}}}
 } as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];
 coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));
 coordinator.persistAgentProgress=async()=>{};
 coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 try {
 const events=[];for await(const e of coordinator.run('p',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(e);
 expect(events.at(-1)).toMatchObject({type:'process:exit',data:{exitCode:1}});
 expect(records.at(-1).status).toBe('failed');expect(active).toBe(true);expect(records.at(-1).reconciliationRequired).toBe(true);expect(interrupted).toBeGreaterThan(0);
 unblock();await new Promise(resolve=>realTimeout(resolve,10));
 expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child.status).not.toBe('completed');
 } finally {unblock();timer.mockRestore();}
});

it('drains a manager that returns early while delegation is still active', async () => {
 const realTimeout = globalThis.setTimeout;
 const timer = vi.spyOn(globalThis,'setTimeout').mockImplementation(((fn:any,ms:any,...args:any[])=>realTimeout(fn,ms===120000 ? 30 : ms,...args)) as any);
 let unblock!:()=>void; const blocked = new Promise<void>(resolve=>unblock=resolve);
 let active=false, interrupted=0, polls=0; const records:any[]=[]; const sessions = new Map<string,any>();
 const channel:any={ startManager:async()=>({workerId:'w',generation:'g',pid:1,state:'running'}), nextManager:async()=> { if(polls++) throw Error('unexpected'); return {kind:'callback',callId:'c',threadId:'t',turnId:'u',name:'delegate_agent',args:{sealedBrief:'read'}};}, replyManager:async()=>{}, retire:async()=>{} };
 const manager = { async *execute(_session:any,_request:any,hooks:any) { void hooks.delegate({sealedBrief:'read'}).catch(()=>undefined); while (!active) await new Promise(resolve=>realTimeout(resolve,1)); } };
 const coordinator:any = new GovernedAgent1RunCoordinator({
 projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['codex-app-server','pi']})},
 resolveManagerSelection:async()=>({adapterId:'codex-app-server',providerId:'openai',model:'hosted'}), manager,
 sessions:{create:async(input:any)=>{const s={...input,sessionId:input.role,projectRoot:'/fixture'};sessions.set(s.sessionId,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},
 tools:{bind:async()=>async()=>{}},
 turns:{interrupt:async()=>{interrupted++;unblock();},async *run(){active=true;try {await blocked;yield {type:'chat:complete',data:{text:'late child'}};yield {type:'process:exit',data:{exitCode:0}};}finally{active=false;}}}
 } as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];
 coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));
 coordinator.persistAgentProgress=async()=>{};
 coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 try {
 const events=[];for await(const e of coordinator.run('p',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(e);
 expect(events.at(-1)).toMatchObject({type:'process:exit',data:{exitCode:1}});
 expect(records.at(-1).status).toBe('failed');expect(active).toBe(false);expect(interrupted).toBeGreaterThan(0);
 unblock();await new Promise(resolve=>realTimeout(resolve,10));
 expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child.status).not.toBe('completed');
 } finally {unblock();timer.mockRestore();}
});


it('keeps authoritative terminal immutable when an issued progress write finishes after drain timeout', async () => {
 const realTimeout = globalThis.setTimeout;
 const timer = vi.spyOn(globalThis,'setTimeout').mockImplementation(((fn:any,ms:any,...args:any[])=>realTimeout(fn,ms===120000 ? 30 : ms,...args)) as any);
 let unblock!:()=>void; const blocked = new Promise<void>(resolve=>unblock=resolve);
 let active=false, interrupted=0, polls=0; const records:any[]=[]; const sessions = new Map<string,any>();
 const channel:any={ startManager:async()=>({workerId:'w',generation:'g',pid:1,state:'running'}), nextManager:async()=> { if(polls++) throw Error('unexpected'); return {kind:'callback',callId:'c',threadId:'t',turnId:'u',name:'delegate_agent',args:{sealedBrief:'read'}};}, replyManager:async()=>{}, retire:async()=>{} };
 const manager = new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'});
 const coordinator:any = new GovernedAgent1RunCoordinator({
 hookDrainTimeoutMs:20, projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['codex-app-server','pi']})},
 resolveManagerSelection:async()=>({adapterId:'codex-app-server',providerId:'openai',model:'hosted'}), manager,
 sessions:{create:async(input:any)=>{const s={...input,sessionId:input.role,projectRoot:'/fixture'};sessions.set(s.sessionId,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},
 tools:{bind:async()=>async()=>{}},
 turns:{interrupt:async()=>{interrupted++;},async *run(){active=true;try {await blocked;yield {type:'chat:complete',data:{text:'late child'}};yield {type:'process:exit',data:{exitCode:0}};}finally{active=false;}}}
 } as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];
 const output = (await fixture()).temp;
 coordinator.writeAgentRun=async(_p:any,_r:any,record:any,filename:string)=>{if(filename.startsWith('progress-')) await blocked; await fs.writeFile(join(output,filename),JSON.stringify(record));};
 coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 try {
 const events=[];for await(const e of coordinator.run('p',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(e);
 expect(events.at(-1)).toMatchObject({type:'process:exit',data:{exitCode:1}});
 const terminal = await fs.readFile(join(output,'run.json'),'utf8'); expect(JSON.parse(terminal)).toMatchObject({status:'failed',reconciliationRequired:true});expect(active).toBe(false);
 unblock();await new Promise(resolve=>realTimeout(resolve,10));
 expect(await fs.readFile(join(output,'run.json'),'utf8')).toBe(terminal); const progress=(await fs.readdir(output)).filter(name=>name.startsWith('progress-'));expect(progress).toHaveLength(1);expect(JSON.parse(await fs.readFile(join(output,progress[0]!), 'utf8'))).toMatchObject({status:'running',child:{status:'launched'}});
 } finally {unblock();timer.mockRestore();}
});

it('reserves child admission synchronously across concurrent callbacks',async()=>{
 const sessions=new Map<string,any>();let childCreates=0,turns=0;const records:any[]=[];
 const manager={async *execute(_s:any,_r:any,hooks:any){const children=await Promise.all([hooks.delegate({sealedBrief:'first'}),hooks.delegate({sealedBrief:'second'})]);await hooks.review({childSessionId:children[1].childSessionId,decision:'accepted',rationale:'actual child'});}};
 const coordinator:any=new GovernedAgent1RunCoordinator({projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['stub','pi']})},resolveManagerSelection:async()=>({adapterId:'stub',providerId:'controlled',model:'manager'}),manager,
 sessions:{create:async(input:any)=>{const id=input.role==='agent2'?'child'+(++childCreates):'manager';const s={...input,sessionId:id,projectRoot:'/fixture'};sessions.set(id,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},tools:{bind:async()=>async()=>{}},turns:{interrupt:async()=>{},async *run(){turns++;yield {type:'process:exit',data:{exitCode:0}};}}} as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));coordinator.persistAgentProgress=async()=>{};coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 const events=[];for await(const event of coordinator.run('project',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(event);
 expect(childCreates).toBeLessThanOrEqual(1);expect(turns).toBeLessThanOrEqual(1);expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child?.sessionId).not.toBe('child2');
});

it('rejects review and successful finalization of a failed child without a completed return',async()=>{
 const sessions=new Map<string,any>();let childCreates=0,turns=0;const records:any[]=[];
 const manager={async *execute(_s:any,_r:any,hooks:any){await hooks.delegate({sealedBrief:'first'}).catch(()=>{});await hooks.review({childSessionId:'child1',decision:'accepted',rationale:'no completed return'});}};
 const coordinator:any=new GovernedAgent1RunCoordinator({projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['stub','pi']})},resolveManagerSelection:async()=>({adapterId:'stub',providerId:'controlled',model:'manager'}),manager,
 sessions:{create:async(input:any)=>{const id=input.role==='agent2'?'child'+(++childCreates):'manager';const s={...input,sessionId:id,projectRoot:'/fixture'};sessions.set(id,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},tools:{bind:async()=>async()=>{}},turns:{interrupt:async()=>{},async *run(){turns++;yield {type:'process:exit',data:{exitCode:1}};}}} as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));coordinator.persistAgentProgress=async()=>{};coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 const events=[];for await(const event of coordinator.run('project',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(event);
 expect(childCreates).toBe(1);expect(turns).toBe(1);expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child.sessionId).toBe('child1');expect(records.at(-1).child.status).toBe('failed');
});

it('consumes a failed child attempt and never permits a second admission',async()=>{
 const sessions=new Map<string,any>();let childCreates=0,turns=0;const records:any[]=[];
 const manager={async *execute(_s:any,_r:any,hooks:any){await hooks.delegate({sealedBrief:'first'}).catch(()=>{});await hooks.delegate({sealedBrief:'retry'});}};
 const coordinator:any=new GovernedAgent1RunCoordinator({projects:{requireAuthorized:async()=>({canonicalRoot:'/fixture',enabledAdapterIds:['stub','pi']})},resolveManagerSelection:async()=>({adapterId:'stub',providerId:'controlled',model:'manager'}),manager,
 sessions:{create:async(input:any)=>{const id=input.role==='agent2'?'child'+(++childCreates):'manager';const s={...input,sessionId:id,projectRoot:'/fixture'};sessions.set(id,s);return s;},get:async(_p:any,id:any)=>sessions.get(id),update:async(s:any)=>sessions.set(s.sessionId,s),appendEvent:async(_p:any,e:any)=>e,persistEvent:async()=>{}},
 residency:{status:async()=>({phase:'READY',managedModelId:'local',epoch:{epochId:'e'}})},tools:{bind:async()=>async()=>{}},turns:{interrupt:async()=>{},async *run(){turns++;yield {type:'process:exit',data:{exitCode:1}};}}} as any);
 coordinator.listManagerDefinitions=async()=>[{agentId:'WORKING_ITEMS',agentType:1}];coordinator.persistAgentRun=async(_p:any,_r:any,record:any)=>records.push(structuredClone(record));coordinator.persistAgentProgress=async()=>{};coordinator.readFileTool=async()=>({tool:{},receipt:{completed:()=>true}});
 const events=[];for await(const event of coordinator.run('project',{brief:'run',approvalReference:'approved',localModel:'local',readOnlyTool:{name:'read_file',relativePath:'file'}}))events.push(event);
 expect(childCreates).toBe(1);expect(turns).toBe(1);expect(records.at(-1).status).toBe('failed');expect(records.at(-1).child.sessionId).toBe('child1');expect(records.at(-1).child.status).toBe('failed');
});
