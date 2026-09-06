import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import ts from '/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/node_modules/typescript/lib/typescript.js';
const base = '/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/';
const files = ['tests/exact-network-conformance.test.ts','tests/exact-network-runtime-conformance.test.ts'];
let checks = 0;
for (const file of files) {
 const text = readFileSync(base+file,'utf8');
 const helper = text.slice(text.indexOf('function diagnosticRecord'),text.indexOf("it('records closed callback"));
 const js = ts.transpileModule(helper,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS}}).outputText;
 const c = vm.createContext({Buffer,createHash});
 vm.runInContext(js+';this.api={diagnosticCallback,diagnosticFailure,diagnosticId,observeDiagnosticFailure};',c);
 const a = c.api;
 const secret = 'review-secret-unbounded-'+ 'x'.repeat(4000);
 for (const value of [secret,{[secret]:secret},[secret],null,123,false]) {
  const evidence = a.diagnosticCallback({method:secret,params:{[secret]:secret,threadId:secret,turnId:secret,itemId:secret,environmentId:secret,reason:secret,command:secret,availableDecisions:[value],networkApprovalContext:{host:secret,protocol:secret,[secret]:secret}}},'example.com',{});
  const serialized=JSON.stringify(evidence); assert(!serialized.includes(secret)); assert(serialized.length<4000); checks++;
 }
 const offered=['accept','acceptForSession','cancel'];
 const result=a.diagnosticCallback({method:'item/commandExecution/requestApproval',params:{availableDecisions:offered}},'example.com',{});
 assert.equal(JSON.stringify(offered),'["accept","acceptForSession","cancel"]');
 assert.equal(JSON.stringify(result.availableDecisions.choices),'[{"tag":"accept"},{"tag":"acceptForSession"},{"tag":"cancel"}]'); checks++;
 assert.equal(a.diagnosticCallback({params:{availableDecisions:['accept','accept']}},'example.com',{}).availableDecisions.duplicates,true); checks++;
 assert.equal(a.diagnosticId('foreign','primary').matchesObservedPrimary,false); checks++;
 for (const originalError of [new Error(secret),null,123,{message:'Unknown approval decision',code:'ENGINE_UNAVAILABLE',details:{reason:'CODEX_PROTOCOL_FAILURE',secret}}]) {
  let calls=0; const args=[];
  const wrapped=a.observeDiagnosticFailure(async (...values)=>{calls++;args.push(...values);throw originalError},()=>{throw new Error('observer failure')});
  try { await wrapped('owned-worker','exact-generation'); assert.fail('failure was swallowed'); } catch(error) { assert.equal(error,originalError); }
  assert.equal(calls,1); assert.deepEqual(args,['owned-worker','exact-generation']); checks++;
 }
}
console.log(JSON.stringify({files:files.length,independentAdversarialChecks:checks,result:'PASS',execution:'extracted pure diagnostic functions only; no supplier/network/provider'}));
