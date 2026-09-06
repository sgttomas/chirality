import { createHmac } from 'node:crypto';
import { createConnection } from 'node:net';
import { PassThrough } from 'node:stream';
import { mkdtemp, realpath, rm } from 'node:fs/promises';
import { join } from 'node:path';
import { afterEach, expect, it } from 'vitest';
import { CodexAgent1ManagerPort, ManagerMailbox } from '../packages/daemon/src/codex-manager.js';
import { createControlledCodexSupervisorForTests } from '../packages/daemon/src/codex-supervisor.js';
import { startSupervisorServer, SupervisorClient } from '../packages/daemon/src/supervisor-server.js';
import type { RuntimeSessionRecord } from '@chirality/runtime-contracts';
const cleanups: (()=>Promise<void>)[] = [];
afterEach(async()=>{ for(const cleanup of cleanups.splice(0).reverse()) await cleanup(); });
async function setup(mode = 'tools') {
 const root = await realpath(await mkdtemp('/tmp/manager-port-')); cleanups.push(()=>rm(root,{recursive:true,force:true}));
 const received: any[] = [];
 const supervisor = createControlledCodexSupervisorForTests({ identity:{ canonicalRoot:root,cwd:root,accountId:'fixture',accountEpoch:1,policyDigest:'fixture-policy'},model:'fixture-model',requestTimeoutMs:1000,turnTimeoutMs:3000,
 launch:async()=>{
  const stdin=new PassThrough(),stdout=new PassThrough(); let buffer='';
  const send=(r:unknown)=>stdout.write(JSON.stringify(r)+'\n');
  const finish=()=>{send({method:'item/completed',params:{threadId:'thread',turnId:'turn',item:{id:'message',type:'agentMessage',text:'reviewed'}}});send({method:'turn/completed',params:{threadId:'thread',turn:{id:'turn',status:'completed'}}});};
  stdin.on('data',bytes=>{buffer+=bytes.toString();let newline;while((newline=buffer.indexOf('\n'))>=0){const r=JSON.parse(buffer.slice(0,newline));buffer=buffer.slice(newline+1);received.push(r);
   if(r.method==='initialize')send({id:r.id,result:{userAgent:'controlled'}});
   if(r.method==='account/read')send({id:r.id,result:{requiresOpenaiAuth:true,account:{type:'fixture'}}});
   if(r.method==='thread/start')send({id:r.id,result:{thread:{id:'thread'}}});
   if(r.method==='turn/start'){send({id:r.id,result:{turn:{id:'turn',status:'inProgress'}}}); setImmediate(()=> mode==='text' ? finish() : send({id:91,method:'item/tool/call',params:{threadId:'thread',turnId:'turn',callId:'delegate-call',tool:'delegate_agent',arguments:{sealedBrief:'Read the approved file'}}}));}
   if(r.id===91 && r.result)send({id:92,method:'item/tool/call',params:{threadId:'thread',turnId:'turn',callId:'review-call',tool:'review',arguments:{childSessionId:'child',decision:'accepted',rationale:'Verified actual return'}}});
   if(r.id===92 && r.result)finish();
  }});
  return {pid:12345,transport:{stdin,stdout,async close(){stdin.destroy();stdout.destroy();}}};
 }}); cleanups.push(()=>supervisor.close());
 const server=await startSupervisorServer({socketPath:join(root,'control.sock'),supervisor});cleanups.push(()=>server.close());
 const channel=new SupervisorClient({socketPath:join(root,'control.sock'),credential:server.credential});
 const session={sessionId:'fixture-manager-session',projectId:'project',role:'agent1',projectRoot:root,engineSelection:{adapterId:'codex-app-server',providerId:'openai',model:'fixture-model'}} as RuntimeSessionRecord;
 return {root,supervisor,channel,session,received,server};
}
it('executes JSONL callback tools across authenticated private channel',async()=>{
 const {channel,session,received,supervisor}=await setup(); const calls:string[]=[];
 const manager=new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'Actual instruction package fixture'});
 const events=[];
 for await(const event of manager.execute(session,{brief:'Delegate and review',approvalReference:'approved'}, {
  delegate:async input=>{calls.push(input.sealedBrief);return {childSessionId:'child',returnText:'read result',model:'local',residencyEpoch:'epoch'};},
  review:async input=>{calls.push(input.decision);}
 },new AbortController().signal))events.push(event);
 expect(calls).toEqual(['Read the approved file','accepted']);expect(events).toEqual([{type:'chat:complete',data:{text:'reviewed'}}]);
 expect(received.find(r=>r.method==='thread/start').params.dynamicTools.map((t:any)=>t.name)).toEqual(['delegate_agent','review']);
 expect(received.find(r=>r.id===91&&r.result).result.success).toBe(true);expect(await supervisor.inventory()).toEqual([]);
});
it('cannot turn plain text into delegation or review',async()=>{
 const {channel,session}=await setup('text');let calls=0;
 for await(const _ of new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'}).execute(session,{brief:'delegate',approvalReference:'approved'},{delegate:async()=>{calls++;throw Error();},review:async()=>{calls++;}},new AbortController().signal)){}
 expect(calls).toBe(0);
});
it('fences private manager acquisition by canonical root and model',async()=>{
 const {channel,root}=await setup();
 await expect(channel.startManager('bad',JSON.stringify({canonicalRoot:'/foreign',model:'fixture-model',prompt:'hello'}))).rejects.toThrow();
 await expect(channel.startManager('bad',JSON.stringify({canonicalRoot:root,model:'other',prompt:'hello'}))).rejects.toThrow();
});
it('rejects foreign, duplicate, cancelled and concurrent mailbox operations',async()=>{
 const mailbox=new ManagerMailbox(),controller=new AbortController();
 const pending=mailbox.tools[0]!.handler({sealedBrief:'x'},{threadId:'t',turnId:'u',callId:'c',signal:controller.signal});
 expect((await mailbox.next()).kind).toBe('callback');
 const reply={callId:'c',threadId:'t',turnId:'u',result:{success:true,contentItems:[{type:'inputText',text:'return'}]}};
 expect(()=>mailbox.reply(JSON.stringify({...reply,turnId:'foreign'}))).toThrow();mailbox.reply(JSON.stringify(reply));await expect(pending).resolves.toMatchObject({success:true});expect(()=>mailbox.reply(JSON.stringify(reply))).toThrow();
 const cancelled=mailbox.tools[0]!.handler({sealedBrief:'x'},{threadId:'t',turnId:'u',callId:'d',signal:controller.signal});controller.abort();await expect(cancelled).rejects.toThrow('cancelled');
 const polling=mailbox.next();await expect(mailbox.next()).rejects.toThrow('Concurrent');mailbox.finish('done');await polling;
});

it('binds callback reply bytes to HMAC and worker generation', async()=>{
 const {root,channel,server}=await setup();
 const h=await channel.startManager('manager',JSON.stringify({canonicalRoot:root,model:'fixture-model',prompt:'tools'}));
 await expect(channel.nextManager(h.workerId,'stale')).rejects.toThrow();
 const call=await channel.nextManager(h.workerId,h.generation);if(call.kind!=='callback')throw Error('Missing callback');
 const input=JSON.stringify({callId:call.callId,threadId:call.threadId,turnId:call.turnId,result:{success:true,contentItems:[{type:'inputText',text:'actual'}]}});
 const r={owner:server.credential.owner,epoch:server.credential.epoch,op:'manager-reply',workerId:h.workerId,generation:h.generation,input};
 const token=createHmac('sha256',server.credential.token).update(JSON.stringify([r.owner,r.epoch,r.op,r.workerId,r.generation,r.input])).digest('hex');
 const answer=await new Promise<string>((resolve,reject)=>{const socket=createConnection(join(root,'control.sock'));let output='';socket.on('error',reject);socket.on('connect',()=>socket.write(JSON.stringify({...r,input:input.replace('actual','forged'),token})+'\n'));socket.on('data',b=>output+=b.toString());socket.on('end',()=>resolve(output));});
 expect(JSON.parse(answer).ok).toBe(false);
 await expect(channel.replyManager(h.workerId,'stale',input)).rejects.toThrow();
 await channel.replyManager(h.workerId,h.generation,input);
 await expect(channel.replyManager(h.workerId,h.generation,input)).rejects.toThrow();
 await channel.retire(h.workerId,h.generation);
 await expect(channel.nextManager(h.workerId,h.generation)).rejects.toThrow();
});
it('cancels a pending daemon callback and retires its supervisor-owned actor',async()=>{
 const {channel,session,supervisor}=await setup();const controller=new AbortController();
 const run=async()=>{for await(const _ of new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'}).execute(session,{brief:'delegate',approvalReference:'approved'},{delegate:()=>{setImmediate(()=>controller.abort());return new Promise(()=>{});},review:async()=>{}},controller.signal)){} };
 await expect(run()).rejects.toMatchObject({code:'INTERRUPTED'});expect(await supervisor.inventory()).toEqual([]);
});
it('preserves governed callback failure instead of treating provider text as success',async()=>{
 const {channel,session}=await setup();
 const run=async()=>{for await(const _ of new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions'}).execute(session,{brief:'delegate',approvalReference:'approved'},{delegate:async()=>{throw new Error('denied');},review:async()=>{}},new AbortController().signal)){} };
 await expect(run()).rejects.toThrow('denied');
});

it('bounds a stuck callback and retires its manager actor without fabricating success',async()=>{
 const {channel,session,supervisor}=await setup();
 const manager=new CodexAgent1ManagerPort({channel,loadInstructions:async()=> 'instructions',callbackTimeoutMs:10});
 const run=async()=>{for await(const _ of manager.execute(session,{brief:'delegate',approvalReference:'approved'},{delegate:()=>new Promise(()=>{}),review:async()=>{}},new AbortController().signal)){} };
 await expect(run()).rejects.toMatchObject({code:'ENGINE_UNAVAILABLE',message:'Manager callback timed out'});
 expect(await supervisor.inventory()).toEqual([]);
 // Coordinator owns draining the governed hook; a port timeout never proves child teardown.
});
it('does not permit an unbounded manager callback timeout',()=>{
 for(const callbackTimeoutMs of [0,-1,NaN,Infinity,120001]) expect(()=>new CodexAgent1ManagerPort({channel:{} as any,loadInstructions:async()=> 'instructions',callbackTimeoutMs})).toThrow();
});
