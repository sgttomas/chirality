import * as fs from 'node:fs/promises';
import {constants} from 'node:fs';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import ts from '/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/node_modules/typescript/lib/typescript.js';
const file='/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/tests/exact-network-runtime-conformance.test.ts';
const source=await fs.readFile(file,'utf8');const extracted=source.slice(source.indexOf('function diagnosticRecord'),source.indexOf('function diagnosticMetadata'))+source.slice(source.indexOf('const auditDigest'),source.indexOf("it('audits host interruption"));
const functions=extracted.slice(0,extracted.indexOf("it('requires the actual interrupt"))+extracted.slice(extracted.indexOf('async function auditInterruptedApproval'));
const c=vm.createContext({...fs,constants,join,createHash,process,Buffer});vm.runInContext(ts.transpileModule(functions,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS}}).outputText+';this.api={auditInterruptedApproval,auditDigest,readCancellationAuditRecord,verifyInterruptAcknowledgement};',c);
const scratch='/private/tmp/runtime-conformance-resume-20260906/review-approval-public-cancel';await fs.mkdir(scratch,{recursive:true,mode:0o700});const base=await fs.mkdtemp(join(scratch,'audit-'));const broker=join(base,'broker'),approvals=join(broker,'approvals'),retirement=join(broker,'retirement');await fs.mkdir(approvals,{recursive:true,mode:0o700});await fs.mkdir(retirement,{mode:0o700});
const binding={canonicalRoot:join(base,'project'),cwd:join(base,'project'),accountId:'fixture',accountEpoch:1,policyDigest:'fixture-policy',sessionId:'review-turn',turnId:'review-turn',workerGeneration:'review-generation'};
const request={requestId:'12345678-1234-4abc-8def-123456789abc',binding,networkApprovalContext:{host:'example.com',protocol:'http'},requestedBy:'trusted-codex-supervisor',requestedAt:'2026-09-06T00:00:00Z',consentDigest:'fixture',caveat:'fixture'};
const basis={turnId:'review-turn',identity:Object.fromEntries(['canonicalRoot','cwd','accountId','accountEpoch','policyDigest'].map(k=>[k,binding[k]])),state:'prepared'};
const terminal={turnId:'review-turn',workerId:'review-turn',generation:'review-generation',outcome:'interrupted',recordedAt:'2026-09-06T00:00:01Z'};
const save=(directory,name,value)=>fs.writeFile(join(directory,name),JSON.stringify(value),{mode:0o600});
const cases=[];
try{await save(approvals,request.requestId+'.request.json',request);for(const [name,change] of [['valid',{}],['contradictory-prepared-terminal',{terminal:{outcome:'failed'}}],['invalid-role-digest',{rolePolicyDigest:'bad'}],['nonstring-role-digest',{rolePolicyDigest:1}],['invalid-prepared-thread',{threadId:'invalid#thread'}],['nonstring-prepared-thread',{threadId:1}]]){const prepared={...basis,...change};await save(retirement,'review-turn.prepared.json',prepared);await save(retirement,'review-turn.terminal.json',{basisDigest:c.api.auditDigest(prepared),terminal});const result=await c.api.auditInterruptedApproval(broker,request);cases.push({name,complete:result.complete});}}finally{await fs.rm(base,{recursive:true,force:true});}
if(cases.some((value,index)=>value.complete !== (index===0))) throw new Error('Independent audit accepted malformed basis or rejected valid basis');
const ack={interrupted:true,turnId:'review-turn',workerGeneration:'review-generation'};
const ackCases=[];
for(const [name,value] of [['valid',ack],['missing',{}],['null',null],['false',{...ack,interrupted:false}],['truthy',{...ack,interrupted:'true'}],['foreign',{...ack,turnId:'foreign'}],['stale',{...ack,workerGeneration:'stale'}],['extra',{...ack,extra:true}]]) { let accepted=false;try { c.api.verifyInterruptAcknowledgement(value,'review-turn','review-generation');accepted=true; }catch{}ackCases.push({name,accepted}); }
if(ackCases.some((value,index)=>value.accepted!==(index===0))) throw new Error('Independent ACK regression failed');
console.log(JSON.stringify({ackCases,sourceSha256:createHash('sha256').update(source).digest('hex'),cases,actualSupplierExecuted:false}));
