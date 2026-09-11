import { describe, expect, it } from "vitest";
import { spawn } from "node:child_process";
import { mkdtemp, readFile, realpath, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { PassThrough } from "node:stream";
import { CodexTurnSession, type CodexDynamicTool } from "../packages/daemon/src/codex-session.js";
import { AUTHORITY_CONTRACT, canonicalBytes, initializationProof, nextSequence20, parseSequence20, sequenceField } from "../packages/daemon/src/supplier-authority-controller.js";

function fixture(mode = "normal", timeout = 500, purpose: "turn" | "login" = "turn", tools?: readonly CodexDynamicTool[], posture: "off" | "ask-per-destination" | "on" = "off") {
  const code = `
 const mode=${JSON.stringify(mode)},posture=${JSON.stringify(posture)}; let configReads=0; const send=x=>process.stdout.write(JSON.stringify(x)+'\\n');
 const response=(r,result)=>send({id:r.id,result});
 const note=(method,params)=>send({method,params});
 const end=status=>note('turn/completed',{threadId:'thread1',turn:{id:'turn1',status}});
 require('node:readline').createInterface({input:process.stdin}).on('line',line=>{
  const r=JSON.parse(line);
  if(mode.startsWith('named') && ['thread/start','thread/resume','turn/start'].includes(r.method) && (r.params.approvalsReviewer!=='user'||r.params.approvalPolicy!==(posture==='ask-per-destination'?'on-request':'never')))process.exit(5);
  if(mode.startsWith('dynamic') && r.id===99 && r.result){
   if(r.result.contentItems[0].type!=='inputText')process.exit(2);
   note('item/agentMessage/delta',{threadId:'thread1',turnId:'turn1',itemId:'tool-output',delta:r.result.contentItems[0].text});
   end(r.result.success?'completed':'failed');return;
  }
  if(mode.startsWith('named') && ['thread/start','thread/resume','turn/start'].includes(r.method) && (r.params.permissions!=='bound-profile' || 'permissionProfile' in r.params || 'sandbox' in r.params || 'sandboxPolicy' in r.params || 'policyDigest' in r.params))process.exit(4);
  if(r.method==='initialize'){response(r,{});return;}
  if(r.method==='initialized')return;
  if(r.method==='config/read'){
   configReads++;if(r.params.includeLayers!==true||r.params.cwd!=='/private/tmp')process.exit(3);
   const selected={filesystem:{'/usr':'read','/private/tmp':'write','/private/protected':'deny'},network:{enabled:posture!=="off"}};
   const config={permissions:{'bound-profile':selected},approvals_reviewer:'user',approval_policy:posture==='ask-per-destination'?'on-request':'never',allow_login_shell:false,features:{plugins:false,remote_plugin:false,shell_snapshot:false,network_proxy:posture!=='off'},hooks:null,mcp_servers:{},notify:null,plugins:{},profiles:{},profile:null,projects:{'/private/tmp':{trust_level:'trusted'}}};
   if(mode.startsWith('named-stage-c'))config.chirality_runtime={nativeSkills:(mode==='named-stage-c-start-drift'&&configReads>=2)||(mode==='named-stage-c-turn-drift'&&configReads>=3)||(mode==='named-stage-c-resume-drift'&&configReads>=4)?'upstream':'disabled'};
   if(mode.startsWith('named-roles')){config.features.multi_agent=true;config.features.multi_agent_v2=false;config.agents={enabled:true,max_depth:(mode==='named-roles-drift'&&configReads>=3)?1:2,HELP_HUMAN:{description:'Help',config_file:'/private/roles/HELP_HUMAN.toml'},HELPS_HUMANS:{description:'Manage',config_file:'/private/roles/HELPS_HUMANS.toml'},WORKING_ITEMS:{description:'Work',config_file:'/private/roles/WORKING_ITEMS.toml'},TASK:{description:'Task',config_file:'/private/roles/TASK.toml'}};
    if(mode==='named-roles-nickname-null'||mode==='named-roles-nickname-set')for(const role of ['HELP_HUMAN','HELPS_HUMANS','WORKING_ITEMS','TASK'])config.agents[role].nickname_candidates=mode==='named-roles-nickname-set'?['Nick']:null;}
   if(mode==='named-null-defaults'||mode==='named-nonnull-default'||mode==='named-unknown-default'){
    selected.description=null;selected.extends=null;selected.workspace_roots=null;selected.filesystem.glob_scan_max_depth=null;
    for(const field of ['proxy_url','enable_socks5','socks_url','enable_socks5_udp','allow_upstream_proxy','dangerously_allow_non_loopback_proxy','dangerously_allow_all_unix_sockets','mode','domains','unix_sockets','allow_local_binding','mitm'])selected.network[field]=null;
    if(mode==='named-nonnull-default')selected.network.allow_local_binding=true;
    if(mode==='named-unknown-default')selected.network.future_grant=null;
   }
   if(mode==='named-reviewer-missing')delete config.approvals_reviewer;
   if(mode==='named-reviewer-null')config.approvals_reviewer=null;
   if(mode==='named-reviewer-auto'||(mode==='named-reviewer-drift'&&configReads>=3))config.approvals_reviewer='auto_review';
   if(mode==='named-reviewer-shadow')config.approvals_reviewer='guardian_subagent';
   if(mode==='named-proxy-missing')delete config.features.network_proxy;
   if(mode==='named-proxy-null')config.features.network_proxy=null;
   if(mode==='named-proxy-wrong'||(mode==='named-proxy-drift'&&configReads>=3))config.features.network_proxy=posture==='off';
   if(mode==='named-snapshot-missing')delete config.features.shell_snapshot;
   if(mode==='named-snapshot-null')config.features.shell_snapshot=null;
   if(mode==='named-snapshot-true'||(mode.startsWith('named-snapshot-drift')&&configReads>=3))config.features.shell_snapshot=true;
   if(mode==='named-remote-plugin')config.features.remote_plugin=true;
   if(mode==='named-extra'||(mode==='named-drift'&&configReads>=3))selected.filesystem['/extra']='read';
   if(mode==='named-network')selected.network.enabled=true;
   if(mode==='named-preset')selected.filesystem[':defaults']='read';
   if(mode==='named-missing')delete selected.filesystem['/private/protected'];
   if(mode==='named-hook')config.hooks={run:['bad']};
   if(mode==='named-mcp')config.mcp_servers={server:{command:'bad'}};
   if(mode==='named-notify')config.notify=['bad'];
   if(mode==='named-project')config.projects['/private/tmp'].command='bad';
   response(r,{config});return;
  }
  if(r.method==='account/read'){
   if(r.params.refreshToken!==false)process.exit(9);
   let account=null;let result;
   if(mode==='account-api')account={type:'apiKey'};
   if(mode==='account-chatgpt')account={type:'chatgpt',email:'synthetic@example.test',planType:'plus'};
   if(mode==='account-null-email')account={type:'chatgpt',email:null,planType:'plus'};
   if(mode==='account-extra')account={type:'apiKey',token:'fixture-secret-must-not-escape'};
   if(mode==='account-unknown')account={type:'unregistered',accountId:'caller-claimed-identity'};
   if(mode==='account-array')account=[];
   if(mode==='account-bad-plan')account={type:'chatgpt',email:null,planType:null};
   result={account,requiresOpenaiAuth:true};
   if(mode==='account-outer-extra')result.accessToken='fixture-secret-must-not-escape';
   if(mode==='account-bad-boolean')result.requiresOpenaiAuth='true';
   response(r,result);return;
  }
  if(r.method==='account/logout'){
   if('params' in r)process.exit(11);
   response(r,mode==='logout-extra'?{account:'must-not-project'}:{});return;
  }
  if(r.method==='thread/start'||r.method==='thread/resume'){
   if(mode.startsWith('dynamic') && (!Array.isArray(r.params.dynamicTools)||r.params.dynamicTools[0].name!=='review'||r.params.dynamicTools[0].inputSchema.additionalProperties!==false||'handler' in r.params.dynamicTools[0]))process.exit(1);
   if(r.params.model!=='fixture-model')process.exit(8);
   if(!mode.startsWith('named') && r.method==='thread/start' && r.params.sandbox!=='workspace-write')process.exit(7);
   const persisted={approvalsReviewer:'auto_review',approvalPolicy:'never'};
   const effective={approvalsReviewer:r.params.approvalsReviewer??persisted.approvalsReviewer,approvalPolicy:r.params.approvalPolicy??persisted.approvalPolicy};
   if(mode==='named-response-missing')delete effective.approvalsReviewer;
   if(mode==='named-response-auto')effective.approvalsReviewer='auto_review';
   if(mode==='named-response-policy')effective.approvalPolicy='untrusted';
   note('thread/started',{thread:{id:'thread1'}});response(r,{thread:{id:'thread1'},...effective});return;
  }
  if(r.method==='turn/start'){
   if(r.params.model!=='fixture-model'||r.params.input[0].type!=='text')process.exit(6);
   if(mode==='attachments'&&JSON.stringify(r.params.input)!==JSON.stringify([{type:'text',text:'fixture work',text_elements:[]},{type:'text',text:'Untrusted document',text_elements:[]},{type:'localImage',path:'/private/tmp/image.png'}]))process.exit(10);
   if(mode==='reject'){send({id:r.id,error:{code:-32600,message:'fixture'}});return;}
   if(mode==='malformed'){response(r,null);return;}
   response(r,{turn:{id:'turn1',status:'inProgress'}});
   note('turn/started',{threadId:'thread1',turn:{id:'turn1',status:'inProgress'}});
   if(mode.startsWith('dynamic')){
    const call={id:99,method:'item/tool/call',params:{threadId:mode==='dynamic-foreign'?'other':'thread1',turnId:'turn1',callId:'call1',tool:'review',arguments:mode==='dynamic-extra'?{text:'work',extra:true}:{text:'work'}}};
    send(call);if(mode==='dynamic-duplicate')send(call);
    if(mode==='dynamic-conflict'){call.params.arguments={text:'changed'};send(call);}
    if(mode==='dynamic-early-terminal')end('completed');
    return;
   }
   if(mode==='native-child'){
    note('item/started',{threadId:'thread1',turnId:'turn1',item:{id:'collab1',type:'collabAgentToolCall',receiverThreadIds:['child-thread']}});
    note('thread/started',{thread:{id:'child-thread'}});
    note('turn/completed',{threadId:'child-thread',turn:{id:'child-turn',status:'completed'}});
    note('item/agentMessage/delta',{threadId:'unassociated-child',turnId:'child-turn',itemId:'child-item',delta:'must not become primary output'});
   }
   if(mode==='foreign-request'){send({id:99,method:'item/tool/call',params:{threadId:'child-thread',turnId:'child-turn',callId:'child-call',tool:'review',arguments:{}}});return;}
   if(mode==='approval'){send({id:99,method:'item/commandExecution/requestApproval',params:{threadId:'thread1',turnId:'turn1'}});return;}
   if(mode==='silent'||mode==='interrupt'||mode==='deaf')return;
   if(mode==='flood'){process.stdout.write('x'.repeat(1100000));return;}
   if(mode==='unknown'){note('item/future/event',{privateContent:'must not escape'});return;}
   if(mode==='diagnostics'){note('thread/status/changed',{status:'active'});note('error',{willRetry:true,error:{message:'must not escape',codexErrorInfo:{responseStreamDisconnected:{httpStatusCode:null}}}});}
   if(mode==='retry-exit'){note('error',{willRetry:true,error:{message:'secret diagnostic'}});setImmediate(()=>process.exit(0));return;}
   if(mode==='diagnostic-flood'){for(let i=0;i<1025;i++)note('warning',{message:'private'});return;}
   if(mode==='bad-terminal'){note('turn/completed',{threadId:'thread1',turn:{id:'turn1',status:'inProgress'}});return;}
   note('item/started',{threadId:'thread1',turnId:'turn1',item:{id:'item1',type:'agentMessage',text:''}});
   note('item/agentMessage/delta',{threadId:'thread1',turnId:'turn1',itemId:'item1',delta:'hello'});
   note('item/completed',{threadId:'thread1',turnId:'turn1',item:{id:'item1',type:'agentMessage',text:'hello'}});
   end(mode==='failed'?'failed':'completed');
   if(mode==='duplicate')end('completed');
   if(mode==='conflict')end('failed');
   if(mode==='late')note('item/agentMessage/delta',{threadId:'thread1',turnId:'turn1',itemId:'item1',delta:'late'});
   return;
  }
  if(r.method==='turn/interrupt'){if(mode==='deaf')return;response(r,{});setImmediate(()=>end('interrupted'));return;}
  process.exit(5);
 });`;
  const child = spawn(process.execPath, ["-e", code], { env: {}, stdio: "pipe", detached: process.platform !== "win32" });
  child.stderr.resume();
  const closed = new Promise<void>(resolve => child.once("close", () => resolve()));
  const configuration = { commandNetworkPosture: posture, transport: { stdin: child.stdin, stdout: child.stdout, async close() { if (mode === "retry-exit") await Promise.race([closed, new Promise<void>(resolve => setTimeout(resolve, 30))]); if (child.pid) { try { process.kill(process.platform === "win32" ? child.pid : -child.pid, "SIGKILL"); } catch { /* exited */ } } await closed; } }, requestTimeoutMs: timeout, turnTimeoutMs: timeout, purpose, permissionProfile: mode.startsWith("named") ? "bound-profile" : undefined, policyDigest: mode.startsWith("named") ? "a".repeat(64) : undefined, ...(mode.startsWith("named-stage-c") ? { nativeSkills: "disabled" as const } : {}), dynamicTools: tools, toolTimeoutMs: 80 };
  const session = new CodexTurnSession(configuration);
  return { session, child, configuration, async close() { await session.close(); expect(child.exitCode !== null || child.signalCode !== null).toBe(true); } };
}
async function ready(f: ReturnType<typeof fixture>) { await f.session.initialize(); return f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); }
const expectedPolicy = { filesystem: { "/usr": "read", "/private/tmp": "write", "/private/protected": "deny" }, network: { enabled: false } } as const;
const expectedNativeRoles = { digest: "d".repeat(64), configOverrides: ["agents.enabled=true", "features.multi_agent=true", "features.multi_agent_v2=false", "agents.max_depth=2", "agents.HELP_HUMAN.description=\"Help\"", "agents.HELP_HUMAN.config_file=\"/private/roles/HELP_HUMAN.toml\"", "agents.HELPS_HUMANS.description=\"Manage\"", "agents.HELPS_HUMANS.config_file=\"/private/roles/HELPS_HUMANS.toml\"", "agents.WORKING_ITEMS.description=\"Work\"", "agents.WORKING_ITEMS.config_file=\"/private/roles/WORKING_ITEMS.toml\"", "agents.TASK.description=\"Task\"", "agents.TASK.config_file=\"/private/roles/TASK.toml\""] } as const;
const turn = { threadId: "thread1", text: "fixture work", model: "fixture-model" };
describe("persistent known-method Codex actor (controlled provider)", () => {
  it.each(["disabled", "upstream", "missing"] as const)("checks authenticated private native-skill readback before effects: %s", async observed => {
    const stdin=new PassThrough(),stdout=new PassThrough(),calls:string[]=[],secret=Buffer.alloc(32,7),descriptor={capability:"chirality.local-admission-authority",contract:AUTHORITY_CONTRACT,major:1,minor:0},v4Descriptor={capability:"account.identity-snapshot",contract:"chirality-supplier-account-identity/1",major:1,minor:0,method:"account/identitySnapshot"};
    const authority={runtimeProcessIncarnationId:"11111111-1111-1111-1111-111111111111",supplierGeneration:"supplier",runtimeChallenge:Buffer.alloc(32,3).toString("base64url"),exactSupplyDigest:"a".repeat(64),authoritySecret:secret,descriptor,v4Descriptor};
    stdin.on("data",bytes=>{for(const line of bytes.toString().trim().split("\n")){const request=JSON.parse(line);calls.push(request.method);if(request.method==="initialize"){const result={contract:AUTHORITY_CONTRACT,runtimeProcessIncarnationId:authority.runtimeProcessIncarnationId,supplierGeneration:authority.supplierGeneration,supplierChallenge:Buffer.alloc(32,4).toString("base64url"),descriptor,v4Descriptor,proof:""};result.proof=initializationProof(secret,{...authority,...result});stdout.write(`${JSON.stringify({id:request.id,result:{chiralityAdmissionAuthority:result}})}\n`);}else if(request.method==="config/read"){const config=observed==="missing"?{}:{chirality_runtime:{nativeSkills:observed}};stdout.write(`${JSON.stringify({id:request.id,result:{config}})}\n`);}}});
    const session=new CodexTurnSession({purpose:"login",nativeSkills:"disabled",transport:{stdin,stdout,async close(){}}});
    try{await session.initializeAuthority(authority);const result=session.verifyNativeSkillSelection("/private/tmp");if(observed==="disabled")await expect(result).resolves.toBeUndefined();else await expect(result).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});expect(calls.slice(0,3)).toEqual(["initialize","initialized","config/read"]);}finally{await session.close();stdin.destroy();stdout.destroy();}
  });
  it("keeps ordinary initialized sessions free of the private native-skill projection",async()=>{
    const stdin=new PassThrough(),stdout=new PassThrough(),calls:string[]=[];stdin.on("data",bytes=>{const request=JSON.parse(bytes.toString());calls.push(request.method);stdout.write(`${JSON.stringify({id:request.id,result:{}})}\n`);});
    const session=new CodexTurnSession({purpose:"login",transport:{stdin,stdout,async close(){}}});try{await session.initialize();await session.verifyNativeSkillSelection("/private/tmp");expect(calls).toEqual(["initialize","initialized"]);}finally{await session.close();stdin.destroy();stdout.destroy();}
  });
  it("validates one private model/list page through the session request lifecycle", async () => {
    const stdin = new PassThrough(), stdout = new PassThrough(), requests: unknown[] = [];
    const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
    stdin.on("data", bytes => {
      for (const line of bytes.toString().trim().split("\n")) {
        const request = JSON.parse(line); requests.push(request);
        if (request.method === "initialize") send({ id: request.id, result: {} });
        else if (request.method === "model/list") send({ id: request.id, result: { data: [{ model: "gpt-default", hidden: false, isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: [{ reasoningEffort: "high", description: "High" }], displayName: "Catalog metadata" }], nextCursor: null } });
      }
    });
    const session = new CodexTurnSession({ purpose: "login", transport: { stdin, stdout, async close() {} } });
    try {
      await session.initialize();
      expect(await session.listModelsPage()).toEqual({ data: [{ model: "gpt-default", hidden: false, isDefault: true, defaultReasoningEffort: "high", supportedReasoningEfforts: ["high"] }], nextCursor: null });
      expect(requests).toContainEqual(expect.objectContaining({ method: "model/list", params: { limit: 100 } }));
      expect(requests.filter(request => (request as { method?: string }).method === "model/list")).toHaveLength(1);
    } finally { await session.close(); stdin.destroy(); stdout.destroy(); }
  });
  it("rejects a model/list page whose default reasoning effort is outside its supported list", async () => {
    const stdin = new PassThrough(), stdout = new PassThrough();
    const send = (value: unknown) => stdout.write(`${JSON.stringify(value)}\n`);
    stdin.on("data", bytes => {
      for (const line of bytes.toString().trim().split("\n")) {
        const request = JSON.parse(line);
        if (request.method === "initialize") send({ id: request.id, result: {} });
        else if (request.method === "model/list") send({ id: request.id, result: { data: [{ model: "gpt-default", hidden: false, isDefault: true, defaultReasoningEffort: "xhigh", supportedReasoningEfforts: [{ reasoningEffort: "low", description: "Low" }, { reasoningEffort: "high", description: "High" }] }], nextCursor: null } });
      }
    });
    const session = new CodexTurnSession({ purpose: "login", transport: { stdin, stdout, async close() {} } });
    try {
      await session.initialize();
      await expect(session.listModelsPage()).rejects.toThrow("Unusable default model reasoning");
    } finally { await session.close(); stdin.destroy(); stdout.destroy(); }
  });

  it("initializes, sanitizes account, streams text and accepts only an actual terminal", async () => {
    const f = fixture();
    try {
      await ready(f); expect(await f.session.accountRead()).toEqual({ authRequired: true, hasAccount: false });
      const id = await f.session.startTurn(turn); expect(id).toBe("turn1");
      expect(await f.session.waitTurn(id)).toEqual({ threadId: "thread1", turnId: "turn1", status: "completed", output: "hello" });
      const events = []; for await (const event of f.session.events()) { events.push(event); if (event.type === "terminal") break; }
      expect(events.map(event => event.type)).toEqual(["started", "text", "terminal"]);
    } finally { await f.close(); }
  });
  it("maps only text documents and local images into exact native turn input", async () => {
    const f = fixture("attachments");
    try {
      await ready(f);
      const id = await f.session.startTurn({ ...turn, attachments: [
        { type: "text", text: "Untrusted document", source: "untrusted-document" },
        { type: "localImage", path: "/private/tmp/image.png", mimeType: "image/png", source: "untrusted-attachment" }
      ] });
      expect((await f.session.waitTurn(id)).status).toBe("completed");
    } finally { await f.close(); }
  });
  it("immutably binds the trusted named policy on start, resume and turn without legacy overrides", async () => {
    const f = fixture("named");
    try {
      f.configuration.permissionProfile = "escalated"; f.configuration.policyDigest = "b".repeat(64);
      expect(f.session.policyBinding()).toEqual({ permissionProfile: "bound-profile", policyDigest: "a".repeat(64) });
      expect(Object.isFrozen(f.session.policyBinding())).toBe(true);
      await f.session.initialize(); await f.session.verifyNativePolicy(expectedPolicy); await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); const id = await f.session.startTurn(turn); await f.session.waitTurn(id);
      expect(await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true })).toBe("thread1");
      await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true, sandbox: "danger-full-access" } as Parameters<CodexTurnSession["startThread"]>[0])).rejects.toThrow("overrides");
      await expect(f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true, permissionProfile: "escalated" } as Parameters<CodexTurnSession["resumeThread"]>[0])).rejects.toThrow("overrides");
      await expect(f.session.startTurn({ ...turn, policyDigest: "b".repeat(64) } as Parameters<CodexTurnSession["startTurn"]>[0])).rejects.toThrow("overrides");
    } finally { await f.close(); }
  });
  it("rechecks the native-11 private skill selection at start, turn, and resume boundaries", async () => {
    const valid=fixture("named-stage-c");
    try {await valid.session.initialize();await valid.session.verifyNativePolicy(expectedPolicy);await valid.session.startThread({cwd:"/private/tmp",model:"fixture-model",continuityChecked:true});const turnId=await valid.session.startTurn(turn);await valid.session.waitTurn(turnId);expect(await valid.session.resumeThread({threadId:"thread1",model:"fixture-model",continuityChecked:true})).toBe("thread1");}
    finally {await valid.close();}
    for(const [mode,boundary] of [["named-stage-c-start-drift","start"],["named-stage-c-turn-drift","turn"],["named-stage-c-resume-drift","resume"]] as const){
      const drift=fixture(mode);try{await drift.session.initialize();await drift.session.verifyNativePolicy(expectedPolicy);
        if(boundary==="start")await expect(drift.session.startThread({cwd:"/private/tmp",model:"fixture-model",continuityChecked:true})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});
        else {await drift.session.startThread({cwd:"/private/tmp",model:"fixture-model",continuityChecked:true});if(boundary==="turn")await expect(drift.session.startTurn(turn)).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});else {const id=await drift.session.startTurn(turn);await drift.session.waitTurn(id);await expect(drift.session.resumeThread({threadId:"thread1",model:"fixture-model",continuityChecked:true})).rejects.toMatchObject({code:"ENGINE_UNAVAILABLE"});}}
      }finally{await drift.close();}
    }
  });
  it("binds exact native role pins and four role files on every effective config read", async () => {
    const valid = fixture("named-roles");
    try { await valid.session.initialize(); await valid.session.verifyNativePolicy(expectedPolicy, expectedNativeRoles); await valid.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); const turnId = await valid.session.startTurn(turn); expect((await valid.session.waitTurn(turnId)).status).toBe("completed"); }
    finally { await valid.close(); }
    const drift = fixture("named-roles-drift");
    try { await drift.session.initialize(); await drift.session.verifyNativePolicy(expectedPolicy, expectedNativeRoles); await drift.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); await expect(drift.session.startTurn(turn)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
    finally { await drift.close(); }
  });
  it("accepts only the inert null nickname default on native role entries from the pinned typed readback", async () => {
    const inert = fixture("named-roles-nickname-null");
    try { await inert.session.initialize(); await inert.session.verifyNativePolicy(expectedPolicy, expectedNativeRoles); await inert.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); const turnId = await inert.session.startTurn(turn); expect((await inert.session.waitTurn(turnId)).status).toBe("completed"); }
    finally { await inert.close(); }
    const named = fixture("named-roles-nickname-set");
    try { await named.session.initialize(); await expect(named.session.verifyNativePolicy(expectedPolicy, expectedNativeRoles)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE", message: "Non-inert native role metadata is unsupported" }); }
    finally { await named.close(); }
  });
  it("rejects merged grants, missing denies, network changes and host-side overrides on readback", async () => {
    for (const mode of ["named-extra", "named-missing", "named-network", "named-preset", "named-hook", "named-mcp", "named-notify", "named-project", "named-nonnull-default", "named-unknown-default", "named-remote-plugin"]) {
      const f = fixture(mode);
      try { await f.session.initialize(); await expect(f.session.verifyNativePolicy(expectedPolicy)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
      finally { await f.close(); }
    }
  });
  it("accepts only the exact observed inert null profile defaults", async () => {
    const f = fixture("named-null-defaults");
    try { await f.session.initialize(); await f.session.verifyNativePolicy(expectedPolicy); await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }); const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed"); }
    finally { await f.close(); }
  });
  it("rechecks effective native policy before every turn and refuses expected-table replacement", async () => {
    const f = fixture("named-drift");
    try {
      await f.session.initialize(); await f.session.verifyNativePolicy(expectedPolicy);
      await expect(f.session.verifyNativePolicy({ ...expectedPolicy, network: { enabled: true } })).rejects.toThrow("cannot be replaced");
      await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      await expect(f.session.startTurn(turn)).rejects.toThrow("differs");
    } finally { await f.close(); }
  });
  it("requires the complete valid named profile and digest pair", () => {
    const transport = { stdin: new PassThrough(), stdout: new PassThrough(), async close() {} };
    for (const policy of [{ permissionProfile: "named" }, { policyDigest: "a".repeat(64) }, { permissionProfile: "../escape", policyDigest: "a".repeat(64) }, { permissionProfile: "named", policyDigest: "bad" }]) expect(() => new CodexTurnSession({ transport, ...policy })).toThrow("Named policy");
  });
  it("quarantines native child notifications without primary output or terminal authority", async () => {
    const f = fixture("native-child");
    try { await ready(f); const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).output).toBe("hello"); expect(f.session.nativeChildren()).toEqual([{ threadId: "child-thread", sourceTurnId: "turn1" }]); expect(f.session.diagnostics().quarantinedNotifications).toBe(4); }
    finally { await f.close(); }
  });
  it("dispatches immutable registered dynamic tools with closed arguments and idempotent request IDs", async () => {
    let calls = 0;
    const schema = { type: "object", properties: { text: { type: "string", maxLength: 20 } }, required: ["text"], additionalProperties: false };
    const tool: CodexDynamicTool = { name: "review", description: "Bounded controlled review", inputSchema: schema, async handler(input, context) { calls++; expect(input).toEqual({ text: "work" }); expect(Object.isFrozen(input)).toBe(true); expect(context.threadId).toBe("thread1"); expect(context.turnId).toBe("turn1"); expect(context.callId).toBe("call1"); return { success: true, contentItems: [{ type: "inputText", text: "reviewed" }] }; } };
    const f = fixture("dynamic-duplicate", 500, "turn", [tool]);
    schema.additionalProperties = true;
    try { await ready(f); const id = await f.session.startTurn(turn); expect(await f.session.waitTurn(id)).toMatchObject({ status: "completed", output: "reviewed" }); expect(calls).toBe(1); }
    finally { await f.close(); }
  });
  it("rejects extra tool input, foreign callbacks, conflicting duplicates and premature terminals", async () => {
    for (const mode of ["dynamic-extra", "dynamic-foreign", "dynamic-conflict", "dynamic-early-terminal"]) {
      let calls = 0;
      const tool: CodexDynamicTool = { name: "review", description: "Review", inputSchema: { type: "object", properties: { text: { type: "string" } }, required: ["text"], additionalProperties: false }, async handler() { calls++; await new Promise(resolve => setTimeout(resolve, 40)); return { success: true, contentItems: [{ type: "inputText", text: "late" }] }; } };
      const f = fixture(mode, 500, "turn", [tool]);
      try { await ready(f); try { const id = await f.session.startTurn(turn); await expect(f.session.waitTurn(id)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } catch (error) { expect(error).toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } if (mode === "dynamic-extra" || mode === "dynamic-foreign") expect(calls).toBe(0); }
      finally { await f.close(); }
    }
  });
  it("bounds dynamic tool duration and outputs with sanitized failure responses", async () => {
    for (const slow of [false, true]) {
      let aborted = false;
      const tool: CodexDynamicTool = { name: "review", description: "Review", inputSchema: { type: "object", properties: { text: { type: "string" } }, additionalProperties: false }, async handler(_, { signal }) { signal.addEventListener("abort", () => { aborted = true; }); if (slow) await new Promise(resolve => setTimeout(resolve, 140)); return { success: true, contentItems: [{ type: "inputText", text: "x".repeat(70000) }] }; } };
      const f = fixture("dynamic", 500, "turn", [tool]);
      try { await ready(f); const id = await f.session.startTurn(turn); expect(await f.session.waitTurn(id)).toMatchObject({ status: "failed", output: "Host tool failed or was cancelled." }); if (slow) expect(aborted).toBe(true); }
      finally { await f.close(); }
    }
  });
  it("aborts active dynamic work when the actor closes", async () => {
    let started!: () => void; const began = new Promise<void>(resolve => { started = resolve; }); let aborted = false;
    const tool: CodexDynamicTool = { name: "review", description: "Review", inputSchema: { type: "object", properties: { text: { type: "string" } }, additionalProperties: false }, async handler(_, { signal }) { started(); await new Promise<void>(resolve => signal.addEventListener("abort", () => { aborted = true; resolve(); }, { once: true })); return { success: true, contentItems: [{ type: "inputText", text: "late" }] }; } };
    const f = fixture("dynamic", 500, "turn", [tool]);
    try { await ready(f); const id = await f.session.startTurn(turn); await began; await f.session.close(); expect(aborted).toBe(true); await expect(f.session.waitTurn(id)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
    finally { await f.close(); }
  });
  it("keeps dedicated login transport separate from model work", async () => {
    const f = fixture("normal", 500, "login");
    try { await f.session.initialize(); await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true })).rejects.toThrow("cannot start model work"); await expect(f.session.startTurn(turn)).rejects.toThrow("cannot start model work"); }
    finally { await f.close(); }
  });
  it("persists a durable thread across retired and successor actor processes", async () => {
    const directory = await mkdtemp(join(await realpath(tmpdir()), "codex-persist-"));
    const file = join(directory, "thread.json");
    const code = `
const fs=require('node:fs'); const file=process.env.THREAD_STORE;
const send=x=>process.stdout.write(JSON.stringify(x)+'\\n');
require('node:readline').createInterface({input:process.stdin}).on('line',line=>{
 const r=JSON.parse(line);
 const respond=result=>send({id:r.id,result});
 if(r.method==='initialize'){respond({});return;} if(r.method==='initialized')return;
 if(r.method==='thread/start'){
  if(r.params.ephemeral!==false){send({id:r.id,error:{code:-32600}});return;}
  fs.writeFileSync(file,JSON.stringify({id:'durable-thread',turns:0}),{mode:0o600}); respond({thread:{id:'durable-thread'}});return;
 }
 if(r.method==='thread/resume'){
  const saved=JSON.parse(fs.readFileSync(file,'utf8'));
  if(saved.id!==r.params.threadId){send({id:r.id,error:{code:-32600}});return;}
  respond({thread:{id:saved.id}});return;
 }
 if(r.method==='turn/start'){
  const saved=JSON.parse(fs.readFileSync(file,'utf8'));saved.turns++;fs.writeFileSync(file,JSON.stringify(saved));
  const id='durable-turn-'+saved.turns;respond({turn:{id,status:'inProgress'}});
  send({method:'turn/completed',params:{threadId:saved.id,turn:{id,status:'completed'}}});return;
 }
 process.exit(9);
});`;
    const sessions: CodexTurnSession[] = [];
    const make = () => {
      const child = spawn(process.execPath, ["-e", code], { env: { THREAD_STORE: file }, stdio: "pipe", detached: process.platform !== "win32" });
      child.stderr.resume(); const closed = new Promise<void>(resolve => child.once("close", () => resolve()));
      const session = new CodexTurnSession({ transport: { stdin: child.stdin, stdout: child.stdout, async close() { if (child.pid) { try { process.kill(process.platform === "win32" ? child.pid : -child.pid, "SIGKILL"); } catch { /* exited */ } } await closed; } } });
      sessions.push(session); return { session, child };
    };
    try {
      const first = make(); await first.session.initialize();
      const threadId = await first.session.startThread({ cwd: directory, model: "fixture-model", continuityChecked: true });
      const firstTurn = await first.session.startTurn({ threadId, model: "fixture-model", text: "first" });
      expect((await first.session.waitTurn(firstTurn)).status).toBe("completed"); await first.session.close();
      expect(first.child.exitCode !== null || first.child.signalCode !== null).toBe(true);
      const second = make(); expect(second.child.pid).not.toBe(first.child.pid); await second.session.initialize();
      expect(await second.session.resumeThread({ threadId, model: "fixture-model", continuityChecked: true })).toBe(threadId);
      const next = await second.session.startTurn({ threadId, model: "fixture-model", text: "successor" });
      expect(next).toBe("durable-turn-2"); expect((await second.session.waitTurn(next)).status).toBe("completed");
      expect(JSON.parse(await readFile(file, "utf8"))).toEqual({ id: threadId, turns: 2 });
    } finally { await Promise.all(sessions.map(session => session.close())); await rm(directory, { recursive: true, force: true }); }
  });
  it("requires explicit model and caller continuity before selecting or resuming", async () => {
    const f = fixture();
    try {
      await f.session.initialize();
      await expect(f.session.startThread({ cwd: "/private/tmp", model: "", continuityChecked: true })).rejects.toThrow("explicit model");
      await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: false as true })).rejects.toThrow("continuity");
      expect(await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true })).toBe("thread1");
      await expect(f.session.startTurn({ ...turn, model: "" })).rejects.toThrow("explicit model");
      await expect(f.session.initialize()).rejects.toThrow("once");
    } finally { await f.close(); }
  });
  it("interrupt acknowledgement resolves only after the provider interruption terminal", async () => {
    const f = fixture("interrupt");
    try { await ready(f); const id = await f.session.startTurn(turn); await expect(f.session.startTurn(turn)).rejects.toThrow("already active"); await f.session.interrupt(id); expect((await f.session.waitTurn(id)).status).toBe("interrupted"); }
    finally { await f.close(); }
  });
  it("deduplicates identical terminals and retains failed terminal as provider outcome", async () => {
    for (const mode of ["duplicate", "failed"]) { const f = fixture(mode); try { await ready(f); const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe(mode === "failed" ? "failed" : "completed"); expect(await f.session.accountRead()).toEqual({ authRequired: true, hasAccount: false }); } finally { await f.close(); } }
  });
  it("fails closed for approval requests, invalid terminals, malformed replies and floods", async () => {
    for (const mode of ["approval", "foreign-request", "malformed", "flood", "bad-terminal", "diagnostic-flood"]) {
      const f = fixture(mode);
      try { await ready(f); try { const id = await f.session.startTurn(turn); await expect(f.session.waitTurn(id)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } catch (error) { expect(error).toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } await expect(f.session.accountRead()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
      finally { await f.close(); }
    }
  });
  it("does not rewrite terminal output from conflicting duplicate or late text", async () => {
    for (const mode of ["conflict", "late"]) { const f = fixture(mode); try { await ready(f); const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).output).toBe("hello"); await expect(f.session.accountRead()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } finally { await f.close(); } }
  });
  it("quarantines unknown notifications as counts without secrets or turn authority", async () => {
    const f = fixture("diagnostics");
    try { await ready(f); const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed"); expect(f.session.diagnostics()).toEqual({ quarantinedNotifications: 2, retryableErrors: 1 }); expect(JSON.stringify(f.session.diagnostics())).not.toContain("must not escape"); }
    finally { await f.close(); }
    const unknown = fixture("unknown", 100);
    try { await ready(unknown); const id = await unknown.session.startTurn(turn); expect((await unknown.session.waitTurn(id)).status).toBe("interrupted"); expect(unknown.session.diagnostics().quarantinedNotifications).toBe(1); }
    finally { await unknown.close(); }
  });
  it("never terminalizes retryable errors followed by a clean process exit", async () => {
    const f = fixture("retry-exit");
    try { await ready(f); const id = await f.session.startTurn(turn); await expect(f.session.waitTurn(id)).rejects.toThrow("ended"); expect(f.session.diagnostics().retryableErrors).toBe(1); await f.session.close(); expect(f.child.exitCode).toBe(0); }
    finally { await f.close(); }
  });
  it("refuses provider reuse of a previously terminal turn identifier", async () => {
    const f = fixture(); try { await ready(f); const id = await f.session.startTurn(turn); await f.session.waitTurn(id); await expect(f.session.startTurn(turn)).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); } finally { await f.close(); }
  });
  it("interrupts an expired turn through the provider and keeps the session usable", async () => {
    const f = fixture("interrupt", 100);
    try {
      await ready(f); const id = await f.session.startTurn(turn);
      expect((await f.session.waitTurn(id)).status).toBe("interrupted");
      expect(await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true })).toBe("thread1");
    } finally { await f.close(); }
  });
  it("rejects provider errors and times out without manufacturing terminal completion", async () => {
    const rejected = fixture("reject"); try { await ready(rejected); await expect(rejected.session.startTurn(turn)).rejects.toMatchObject({ details: { reason: "CODEX_REQUEST_REJECTED" } }); await expect(rejected.session.waitTurn("turn1")).rejects.toThrow("Unknown"); } finally { await rejected.close(); }
    // An expired turn is interrupted through the provider; only a provider that ignores the interrupt is a failure.
    const silent = fixture("silent", 100); try { await ready(silent); const id = await silent.session.startTurn(turn); expect((await silent.session.waitTurn(id)).status).toBe("interrupted"); } finally { await silent.close(); }
    const deaf = fixture("deaf", 100); try { await ready(deaf); const id = await deaf.session.startTurn(turn); await expect(deaf.session.waitTurn(id)).rejects.toThrow("timed out"); await expect(deaf.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true })).rejects.toThrow("timed out"); } finally { await deaf.close(); }
  });
});

describe("private Sequence20 framing", () => {
  it("validates the original string and frames exact unsigned big-endian bytes", () => {
    expect(canonicalBytes("x", [sequenceField("00000000000000000001")]).toString("hex")).toMatch(/000000080000000000000001$/);
    expect(parseSequence20("18446744073709551615")).toBe(18446744073709551615n);
    expect(() => nextSequence20("18446744073709551615")).toThrow("sequence-invalid");
    for (const value of [0, "1", "00000000000000000000", "+0000000000000000001", "０００００００００００００００００００１"]) expect(() => parseSequence20(value)).toThrow("sequence-invalid");
  });
});

async function networkActor(posture: "off" | "ask-per-destination" | "on" = "ask-per-destination", dynamicTools?: readonly CodexDynamicTool[], requestTimeoutMs = 500) {
  const stdin = new PassThrough(), stdout = new PassThrough(); const replies: any[] = [];
  const send = (value: unknown) => stdout.write(JSON.stringify(value) + "\n");
  stdin.on("data", chunk => {
    for (const line of String(chunk).trim().split("\n")) {
      const request = JSON.parse(line);
      if (!request.method) { replies.push(request); continue; }
      if (request.method === "initialized") continue;
      send({ id: request.id, result: request.method === "thread/start" ? { thread: { id: "network-thread" } } : request.method === "turn/start" ? { turn: { id: "network-turn" } } : {} });
    }
  });
  const actor = new CodexTurnSession({ requestTimeoutMs, dynamicTools, commandNetworkPosture: posture, transport: { stdin, stdout, async close() {} } });
  await actor.initialize(); await actor.startThread({ cwd: "/private/tmp", model: "fixture", continuityChecked: true }); await actor.startTurn({ threadId: "network-thread", text: "fixture", model: "fixture" });
  const prompt = (id: string | number, change = {}) => send({ id, method: "item/commandExecution/requestApproval", params: { threadId: "network-thread", turnId: "network-turn", itemId: "network-item", startedAtMs: 1, networkApprovalContext: { host: "example.com", protocol: "https" }, availableDecisions: ["accept", "decline", "acceptForSession"], ...change } });
  return { actor, send, replies, prompt, stdin };
}
const supplierNetworkUuid = "00000000-0000-4000-8000-000000000000";
const supplierPolicyChoice = (host = "example.com", action = "allow") => ({ applyNetworkPolicyAmendment: { network_policy_amendment: { host, action } } });
function supplierNetworkPrompt(overrides: Record<string, unknown> = {}) {
  return { itemId: `network#local#http#example.com#80#${supplierNetworkUuid}`, environmentId: "local", networkApprovalContext: { host: "example.com", protocol: "http" }, availableDecisions: ["accept", "acceptForSession", supplierPolicyChoice(), "cancel"], ...overrides };
}
it("accepts the observed supplier network callback shape without inventing decline or executing policy amendments", async () => {
  const f = await networkActor();
  try {
    const params = supplierNetworkPrompt();
    f.prompt(101, params); f.prompt(101, params);
    expect(f.replies).toEqual([]);
    const prompts = f.actor.pendingNetworkApprovals(); expect(prompts).toHaveLength(1);
    expect(prompts[0]).toMatchObject({ threadId: "network-thread", turnId: "network-turn", networkApprovalContext: { host: "example.com", protocol: "http" }, availableDecisions: ["allow", "acceptForSession"] });
    for (const unsupported of ["deny", "cancel", "applyNetworkPolicyAmendment"] as const) await expect(f.actor.replyNetworkApproval(prompts[0]!.approvalId, unsupported as "deny")).rejects.toThrow();
    expect(f.replies).toEqual([]);
    await f.actor.replyNetworkApproval(prompts[0]!.approvalId, "allow");
    expect(f.replies).toEqual([{ id: 101, result: { decision: "accept" } }]);
    f.prompt(101, params);
    await expect(f.actor.waitTurn("network-turn")).rejects.toThrow();
    expect(f.replies).toHaveLength(1);
  } finally { await f.actor.close(); }
});
it.each([["http", "http"], ["https", "https"], ["socks5Tcp", "socks5-tcp"], ["socks5Udp", "socks5-udp"]])("correlates supplier %s context with its exact %s label", async (context, label) => {
  const f = await networkActor();
  try {
    f.prompt(102, supplierNetworkPrompt({ itemId: `network#local#${label}#example.com#65535#${supplierNetworkUuid}`, networkApprovalContext: { host: "example.com", protocol: context } }));
    expect(f.actor.pendingNetworkApprovals()).toHaveLength(1); expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});
it("allows the bounded maximum supplier token and lowercase host correlation without rewriting signature input", async () => {
  const f = await networkActor();
  try {
    const host = [...Array(3).fill("a".repeat(63)), "b".repeat(61)].join(".");
    const environmentId = "e".repeat(128), itemId = `network#${environmentId}#socks5-tcp#${host}#65535#${supplierNetworkUuid}`;
    expect(host).toHaveLength(253); expect(itemId).toHaveLength(444);
    const params = supplierNetworkPrompt({ environmentId, itemId, networkApprovalContext: { host: host.toUpperCase(), protocol: "socks5Tcp" }, availableDecisions: ["accept", supplierPolicyChoice(host.toUpperCase(), "deny"), "cancel"] });
    f.prompt(103, params); expect(f.actor.pendingNetworkApprovals()).toHaveLength(1); expect(f.replies).toEqual([]);
    // Changing even an omitted known policy option must conflict with the full original request signature.
    f.prompt(103, { ...params, availableDecisions: ["accept", supplierPolicyChoice(host.toUpperCase(), "allow"), "cancel"] });
    await expect(f.actor.waitTurn("network-turn")).rejects.toThrow("Conflicting"); expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});
it("rejects malformed, unbounded and inconsistent supplier identifiers before any reply", async () => {
  const item = (environment = "local", protocol = "http", host = "example.com", port = "80", uuid = supplierNetworkUuid) => `network#${environment}#${protocol}#${host}#${port}#${uuid}`;
  const cases: Record<string, unknown>[] = [
    { itemId: null }, { itemId: {} }, { itemId: "" }, { itemId: "x".repeat(129) },
    { environmentId: undefined }, { environmentId: null }, { environmentId: "" }, { environmentId: "foreign" }, { environmentId: {} },
    { itemId: item("e".repeat(129)), environmentId: "e".repeat(129) }, { itemId: item("local\n"), environmentId: "local\n" },
    { itemId: item("local", "https") }, { itemId: item("local", "socks5_tcp") }, { itemId: item("local", "http", "foreign.example") },
    ...["-1", "65536", "080", "1e2", "", "00000"].map(port => ({ itemId: item("local", "http", "example.com", port) })),
    ...["\n", "\r", "\t", "\0", "\u007f", " "].map(control => ({ itemId: item() + control })),
    { itemId: item() + "#extra" }, { itemId: item().replace("network#", "different#") }, { itemId: item("local", "http", "example.com", "80", "a".repeat(36)) },
    { itemId: item("local", "http", "example.com", "80", supplierNetworkUuid.replace("4000", "1000")) },
    { itemId: item("local", "http", "example.com", "80", supplierNetworkUuid.replace("8000", "7000")) },
    { itemId: item("local", "http", "example.com", "80", "AAAAAAAA-AAAA-4AAA-8AAA-AAAAAAAAAAAA") },
    { itemId: item("local", "http", "a".repeat(254)), networkApprovalContext: { host: "a".repeat(254), protocol: "http" } },
    { itemId: "network#" + "x".repeat(438) },
    { threadId: "foreign" }, { turnId: "foreign" }, { threadId: "network#thread" }, { turnId: "network#turn" },
    ...["additionalPermissions", "proposedExecpolicyAmendment", "command", "cwd", "commandActions"].map(key => ({ [key]: {} })),
  ];
  for (const change of cases) {
    const f = await networkActor();
    try { f.prompt(104, supplierNetworkPrompt(change)); expect(() => f.actor.pendingNetworkApprovals()).toThrow(); await expect(f.actor.waitTurn("network-turn")).rejects.toThrow(); expect(f.replies).toEqual([]); }
    finally { await f.actor.close(); }
  }
});
it("fails closed for unknown or malformed offered objects even when accept is also present", async () => {
  const invalidChoices: unknown[] = [null, [], {}, 1, true, "future-decision", { futureDecision: {} },
    { applyNetworkPolicyAmendment: null }, { applyNetworkPolicyAmendment: [] }, { applyNetworkPolicyAmendment: {} },
    { applyNetworkPolicyAmendment: { network_policy_amendment: [] } }, { applyNetworkPolicyAmendment: { network_policy_amendment: {} } },
    { ...supplierPolicyChoice(), extra: true },
    { applyNetworkPolicyAmendment: { network_policy_amendment: { host: "example.com", action: "allow", extra: true } } },
    { applyNetworkPolicyAmendment: { network_policy_amendment: { host: "example.com", action: "allow" }, extra: true } },
    supplierPolicyChoice("foreign.example"), supplierPolicyChoice("example.com", "future"),
    { acceptWithExecpolicyAmendment: { execpolicy_amendment: ["curl"] } },
  ];
  for (const choice of invalidChoices) {
    const f = await networkActor();
    try { f.prompt(105, supplierNetworkPrompt({ availableDecisions: ["accept", choice, "cancel"] })); expect(() => f.actor.pendingNetworkApprovals()).toThrow(); await expect(f.actor.waitTurn("network-turn")).rejects.toThrow(); expect(f.replies).toEqual([]); }
    finally { await f.actor.close(); }
  }
});
it("rejects a resolved source-shaped callback replay without sending a grant", async () => {
  const f = await networkActor();
  try {
    const params = supplierNetworkPrompt(); f.prompt("source-request", params);
    const [prompt] = f.actor.pendingNetworkApprovals();
    f.send({ method: "serverRequest/resolved", params: { threadId: "network-thread", requestId: "source-request" } });
    expect(f.actor.pendingNetworkApprovals()).toEqual([]);
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, "allow")).rejects.toThrow();
    f.prompt("source-request", params); await expect(f.actor.waitTurn("network-turn")).rejects.toThrow(); expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});

it.each(["allow", "deny", "acceptForSession"] as const)("routes exact attributed-host network choice %s without automatic decisions", async decision => {
  const f = await networkActor();
  try {
    f.prompt(91); expect(f.replies).toEqual([]);
    const [prompt] = f.actor.pendingNetworkApprovals();
    expect(prompt).toMatchObject({ threadId: "network-thread", turnId: "network-turn", networkApprovalContext: { host: "example.com", protocol: "https" }, availableDecisions: ["allow", "deny", "acceptForSession"] });
    expect(prompt!.approvalId).not.toBe("91");
    expect(await f.actor.replyNetworkApproval(prompt!.approvalId, decision)).toEqual({ sent: true });
    expect(f.replies).toEqual([{ id: 91, result: { decision: decision === "allow" ? "accept" : decision === "deny" ? "decline" : decision } }]);
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, decision)).rejects.toThrow();
  } finally { await f.actor.close(); }
});
it("cancels only the exact resolved network request, preserving typed request IDs", async () => {
  const f = await networkActor();
  try {
    f.prompt(9); f.prompt("9"); const before = f.actor.pendingNetworkApprovals(); expect(before).toHaveLength(2);
    f.send({ method: "serverRequest/resolved", params: { threadId: "network-thread", requestId: 9 } });
    expect(f.actor.pendingNetworkApprovals()).toHaveLength(1);
    await expect(f.actor.replyNetworkApproval(before[0]!.approvalId, "allow")).rejects.toThrow();
    await f.actor.replyNetworkApproval(before[1]!.approvalId, "deny");
    expect(f.replies).toEqual([{ id: "9", result: { decision: "decline" } }]);
  } finally { await f.actor.close(); }
});
it("fails closed for off/on, foreign turns, combined permission requests and conflicting duplicate network prompts", async () => {
  for (const mode of ["off", "on", "foreign", "combined", "duplicate"] as const) {
    const f = await networkActor(mode === "off" || mode === "on" ? mode : "ask-per-destination");
    try {
      if (mode === "duplicate") f.prompt(8);
      f.prompt(8, mode === "foreign" ? { turnId: "foreign" } : mode === "combined" ? { additionalPermissions: { filesystem: {} } } : mode === "duplicate" ? { itemId: "conflicting" } : {});
      await expect(f.actor.waitTurn("network-turn")).rejects.toThrow(); expect(f.replies).toEqual([]);
    } finally { await f.actor.close(); }
  }
});
it("invalidates pending network grants when turn interruption begins", async () => {
  const f = await networkActor();
  try {
    f.prompt(1); const [prompt] = f.actor.pendingNetworkApprovals();
    await f.actor.interrupt("network-turn");
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, "acceptForSession")).rejects.toThrow(); expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});

it("honors exact server cancellation of a dynamic callback without late response or false terminal failure", async () => {
  let aborted = false;
  const f = await networkActor("off", [{ name: "review", description: "controlled", inputSchema: { type: "object", properties: {}, additionalProperties: false }, async handler(_args, context) { context.signal.addEventListener("abort", () => { aborted = true; }); return new Promise(() => {}); } }]);
  try {
    f.send({ id: 77, method: "item/tool/call", params: { threadId: "network-thread", turnId: "network-turn", callId: "review-call", tool: "review", arguments: {} } });
    await new Promise(resolve => setImmediate(resolve));
    f.send({ method: "serverRequest/resolved", params: { threadId: "network-thread", requestId: 77 } });
    f.send({ method: "turn/completed", params: { threadId: "network-thread", turn: { id: "network-turn", status: "completed" } } });
    expect((await f.actor.waitTurn("network-turn")).status).toBe("completed"); expect(aborted).toBe(true);
    await new Promise(resolve => setImmediate(resolve)); expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});

it.each(["off", "ask-per-destination", "on"] as const)("requires explicit exact network_proxy feature for %s, including operation-time drift", async posture => {
  const expected = { ...expectedPolicy, network: { enabled: posture !== "off" } };
  for (const mode of ["named", "named-proxy-missing", "named-proxy-null", "named-proxy-wrong", "named-proxy-drift"]) {
    const f = fixture(mode, 500, "turn", undefined, posture);
    try {
      await f.session.initialize();
      if (["named-proxy-missing", "named-proxy-null", "named-proxy-wrong"].includes(mode)) { await expect(f.session.verifyNativePolicy(expected)).rejects.toThrow("Unsafe effective"); continue; }
      await f.session.verifyNativePolicy(expected);
      await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      if (mode === "named-proxy-drift") await expect(f.session.startTurn(turn)).rejects.toThrow("Unsafe effective");
      else { const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed"); await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true }); }
    } finally { await f.close(); }
  }
});

it("acknowledges an approval only after its successful write callback and fences concurrent sends", async () => {
  const f = await networkActor();
  try {
    f.prompt(15); const [prompt] = f.actor.pendingNetworkApprovals();
    const original = f.stdin._write.bind(f.stdin); let finish!: () => void;
    f.stdin._write = (chunk, encoding, callback) => { finish = () => original(chunk, encoding, callback); };
    let delivered = false; const sending = f.actor.replyNetworkApproval(prompt!.approvalId, "allow").then(result => { delivered = true; return result; });
    await Promise.resolve(); expect(delivered).toBe(false); expect(f.replies).toEqual([]);
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, "allow")).rejects.toThrow();
    finish(); expect(await sending).toEqual({ sent: true }); expect(f.replies).toEqual([{ id: 15, result: { decision: "accept" } }]);
  } finally { await f.actor.close(); }
});
it.each(["async-error", "no-callback"] as const)("never reports applied transport success after %s and prohibits replay", async mode => {
  const f = await networkActor("ask-per-destination", undefined, 30);
  try {
    f.prompt(16); const [prompt] = f.actor.pendingNetworkApprovals();
    f.stdin._write = (_chunk, _encoding, callback) => { if (mode === "async-error") setImmediate(() => callback(new Error("synthetic broken pipe"))); };
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, "acceptForSession")).rejects.toThrow("Approval transport write");
    await expect(f.actor.replyNetworkApproval(prompt!.approvalId, "acceptForSession")).rejects.toThrow();
    expect(f.replies).toEqual([]);
  } finally { await f.actor.close(); }
});


it.each(["off", "ask-per-destination", "on"] as const)("pins user approval reviewer for %s and refuses inherited, shadowed or changed review authority", async posture => {
  const expected = { ...expectedPolicy, network: { enabled: posture !== "off" } };
  for (const mode of ["named", "named-reviewer-missing", "named-reviewer-null", "named-reviewer-auto", "named-reviewer-shadow", "named-reviewer-drift"]) {
    const f = fixture(mode, 500, "turn", undefined, posture);
    try {
      await f.session.initialize();
      if (!["named", "named-reviewer-drift"].includes(mode)) { await expect(f.session.verifyNativePolicy(expected)).rejects.toThrow("Unsafe effective"); continue; }
      await f.session.verifyNativePolicy(expected);
      await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      if (mode === "named-reviewer-drift") await expect(f.session.startTurn(turn)).rejects.toThrow("Unsafe effective");
      else { const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed"); await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true }); }
    } finally { await f.close(); }
  }
});


it.each(["off", "ask-per-destination", "on"] as const)("overrides persisted reviewer and approval policy for native %s operations and rejects caller authority", async posture => {
  const f = fixture("named", 500, "turn", undefined, posture);
  try {
    await f.session.initialize(); await f.session.verifyNativePolicy({ ...expectedPolicy, network: { enabled: posture !== "off" } });
    await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
    await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true });
    const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed");
    for (const override of [{ approvalsReviewer: "auto_review" }, { approvals_reviewer: "auto_review" }, { approvalPolicy: "never" }, { approval_policy: "never" }]) {
      await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true, ...override })).rejects.toThrow("overrides");
      await expect(f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true, ...override })).rejects.toThrow("overrides");
      await expect(f.session.startTurn({ ...turn, ...override })).rejects.toThrow("overrides");
    }
  } finally { await f.close(); }
});
it.each(["named-response-missing", "named-response-auto", "named-response-policy"])("rejects native thread response that ignores trusted pins: %s", async mode => {
  for (const method of ["start", "resume"]) {
    const f = fixture(mode);
    try {
      await f.session.initialize(); await f.session.verifyNativePolicy(expectedPolicy);
      const request = method === "start" ? f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true }) : f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true });
      await expect(request).rejects.toThrow("Effective thread approval settings");
    } finally { await f.close(); }
  }
});


it.each(["off", "ask-per-destination", "on"] as const)("disables shell snapshots for %s and rejects absent, enabled or changed startup authority", async posture => {
  const expected = { ...expectedPolicy, network: { enabled: posture !== "off" } };
  for (const mode of ["named", "named-snapshot-missing", "named-snapshot-null", "named-snapshot-true", "named-snapshot-drift-turn", "named-snapshot-drift-resume"]) {
    const f = fixture(mode, 500, "turn", undefined, posture);
    try {
      await f.session.initialize();
      if (["named-snapshot-missing", "named-snapshot-null", "named-snapshot-true"].includes(mode)) {
        await expect(f.session.verifyNativePolicy(expected)).rejects.toThrow("Unsafe effective");
        await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true })).rejects.toThrow();
        continue;
      }
      await f.session.verifyNativePolicy(expected);
      await f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true });
      if (mode === "named-snapshot-drift-turn") await expect(f.session.startTurn(turn)).rejects.toThrow("Unsafe effective");
      else if (mode === "named-snapshot-drift-resume") await expect(f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true })).rejects.toThrow("Unsafe effective");
      else {
        const id = await f.session.startTurn(turn); expect((await f.session.waitTurn(id)).status).toBe("completed");
        await f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true });
      }
    } finally { await f.close(); }
  }
});


describe("custody account-only projection", () => {
  it("sends the accepted parameterless logout request and accepts only an empty acknowledgement", async () => {
    const f = fixture("normal", 1000, "login");
    try { await f.session.initialize(); await expect(f.session.accountLogout()).resolves.toBeUndefined(); }
    finally { await f.close(); }
    const invalid = fixture("logout-extra", 1000, "login");
    try { await invalid.session.initialize(); await expect(invalid.session.accountLogout()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" }); }
    finally { await invalid.close(); }
  });
  it.each(["account-api", "account-chatgpt", "account-null-email"])("projects %s to presence without an identity claim", async mode => {
    const f = fixture(mode, 1000, "login");
    try { await f.session.initialize(); expect(await f.session.accountRead()).toEqual({ authRequired: true, hasAccount: true }); }
    finally { await f.close(); }
  });
  it.each(["account-extra", "account-outer-extra", "account-unknown", "account-array", "account-bad-plan", "account-bad-boolean"])("rejects %s without exporting unrecognized account material", async mode => {
    const f = fixture(mode, 1000, "login");
    try {
      await f.session.initialize();
      await expect(f.session.accountRead()).rejects.toMatchObject({ code: "ENGINE_UNAVAILABLE" });
      await expect(f.session.accountRead()).rejects.not.toThrow("fixture-secret-must-not-escape");
    } finally { await f.close(); }
  });
  it("prohibits thread start, resume, turn and dynamic tools on a login actor", async () => {
    const f = fixture("normal", 1000, "login");
    try {
      await f.session.initialize();
      await expect(f.session.startThread({ cwd: "/private/tmp", model: "fixture-model", continuityChecked: true })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
      await expect(f.session.resumeThread({ threadId: "thread1", model: "fixture-model", continuityChecked: true })).rejects.toMatchObject({ code: "INVALID_REQUEST" });
      await expect(f.session.startTurn(turn)).rejects.toMatchObject({ code: "INVALID_REQUEST" });
    } finally { await f.close(); }
    expect(() => new CodexTurnSession({ purpose: "login", transport: { stdin: new PassThrough(), stdout: new PassThrough(), async close() {} }, dynamicTools: [{ name: "review", description: "synthetic", inputSchema: { type: "object", properties: {}, additionalProperties: false }, async handler() { throw new Error("must never run"); } }] })).toThrow("Unsupported dynamic tool registry");
  });
});

describe("private authority session transport",()=>{
 it("delivers ordered raw frames and rejects duplicate keys before handing them to the controller",async()=>{const stdin=new PassThrough(),stdout=new PassThrough();let failures=0,closed=0;const received:string[]=[];const transport=CodexTurnSession.privateAuthorityTransport({stdin,stdout,close:async()=>{closed++;}});transport.subscribe(raw=>received.push(Buffer.from(raw).toString()),()=>{failures++;});stdout.write('{"a":1}\n{"a":2}\n');expect(received).toEqual(['{"a":1}','{"a":2}']);stdout.write('{"a":1,"a":2}\n');expect(failures).toBe(1);await transport.close();await transport.close();expect(closed).toBe(1);});
 it("verifies the exact initialization proof and rejects version rollback or altered descriptors",async()=>{const {verifyAuthorityInitialization}=await import("../packages/daemon/src/codex-session.js");const {initializationProof,AUTHORITY_CONTRACT}=await import("../packages/daemon/src/supplier-authority-controller.js");const input={runtimeProcessIncarnationId:"11111111-1111-1111-1111-111111111111",supplierGeneration:"s",runtimeChallenge:Buffer.alloc(32,1).toString("base64url"),exactSupplyDigest:"a".repeat(64),authoritySecret:Buffer.alloc(32,2),descriptor:{capability:"chirality.local-admission-authority",contract:AUTHORITY_CONTRACT,major:1,minor:0},v4Descriptor:{capability:"account.identity-snapshot",contract:"chirality-supplier-account-identity/1",major:1,minor:0,method:"account/identitySnapshot"}};const result={contract:AUTHORITY_CONTRACT,runtimeProcessIncarnationId:input.runtimeProcessIncarnationId,supplierGeneration:"s",supplierChallenge:Buffer.alloc(32,3).toString("base64url"),descriptor:input.descriptor,v4Descriptor:input.v4Descriptor,proof:""};result.proof=initializationProof(input.authoritySecret,{...input,...result});expect(()=>verifyAuthorityInitialization(input,result)).not.toThrow();for(const change of [{...result,proof:"A".repeat(43)},{...result,descriptor:{...result.descriptor,major:0}},{...result,v4Descriptor:{...result.v4Descriptor,minor:1}},{...result,extra:1}])expect(()=>verifyAuthorityInitialization(input,change)).toThrow();});
});

describe("connected private initialize/snapshot/admission",()=>{
 it("authenticates initialization, refreshes V4 and exchanges envelopes through CodexTurnSession",async()=>{const {initializationProof,AuthorityTranscript,AUTHORITY_CONTRACT}=await import("../packages/daemon/src/supplier-authority-controller.js");const {createFakeRuntimeAdmissionNativeAdapter}=await import("../packages/core/src/runtime-admission-lock.js");const secret=Buffer.alloc(32,6),stdin=new PassThrough(),stdout=new PassThrough();const identity={runtimeProcessIncarnationId:"11111111-1111-1111-1111-111111111111",supplierGeneration:"s"};const descriptor={capability:"chirality.local-admission-authority",contract:AUTHORITY_CONTRACT,major:1,minor:0},v4Descriptor={capability:"account.identity-snapshot",contract:"chirality-supplier-account-identity/1",major:1,minor:0,method:"account/identitySnapshot"};const input={...identity,authoritySecret:secret,runtimeChallenge:Buffer.alloc(32,3).toString("base64url"),exactSupplyDigest:"a".repeat(64),descriptor,v4Descriptor};const inbound=new AuthorityTranscript(secret,identity,"runtime-to-supplier"),outbound=new AuthorityTranscript(secret,identity,"supplier-to-runtime");const calls:string[]=[];let buffered="";const send=(value:unknown)=>stdout.write(JSON.stringify(value)+"\n");stdin.on("data",chunk=>{buffered+=String(chunk);let newline:number;while((newline=buffered.indexOf("\n"))>=0){const raw=buffered.slice(0,newline);buffered=buffered.slice(newline+1);const message=JSON.parse(raw);if(message.method==="initialize"){calls.push("initialize");const result={contract:AUTHORITY_CONTRACT,...identity,supplierChallenge:Buffer.alloc(32,4).toString("base64url"),descriptor,v4Descriptor,proof:""};result.proof=initializationProof(secret,{...input,...result});send({id:message.id,result:{chiralityAdmissionAuthority:result}});}else if(message.method==="initialized")continue;else if(message.method==="account/identitySnapshot"){calls.push("snapshot");send({id:message.id,result:{schema:"chirality-supplier-account-identity-response/1",state:"available",supplierGeneration:"s",identityGeneration:"i",accountUserId:"u",providerWorkspaceId:"w"}});}else {const b=inbound.accept(raw);if(b.kind!=="request")throw Error();calls.push(b.op);const acquire=b.op==="chirality/admissionAcquire";const base=acquire?{requestId:b.requestId,operationId:b.operationId,leaseId:"l",supplierGeneration:"s",identityGeneration:"i",snapshotDigest:b.v4.snapshotDigest}:{requestId:b.requestId,leaseId:b.leaseId,disposition:b.disposition};send(outbound.encode({kind:"result",op:b.op,state:acquire?"acquired":"aborted",...base} as any));send(outbound.encode({kind:"notification",op:acquire?"chirality/admissionAcquired":"chirality/admissionAborted",...base} as any));}}});const session=new CodexTurnSession({transport:{stdin,stdout,close:async()=>{stdin.destroy();stdout.destroy();}}});const controller=await session.establishAuthority(input,createFakeRuntimeAdmissionNativeAdapter().acquire("","runtime-admission-authority.lock"),async()=>{});await controller.acquire("w");await controller.abort("w");expect(calls).toEqual(["initialize","snapshot","snapshot","chirality/admissionAcquire","chirality/admissionAbort"]);await controller.close();});
});
