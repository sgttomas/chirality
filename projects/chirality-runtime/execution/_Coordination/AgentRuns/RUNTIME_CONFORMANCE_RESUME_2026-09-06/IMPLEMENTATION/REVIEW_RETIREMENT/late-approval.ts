import { mkdtemp, realpath, rm } from "node:fs/promises";
import { join } from "node:path";
import { DelegatedRuntime } from "/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/packages/core/src/delegated-runtime.ts";
import { WorkerRetirementCoordinator } from "/Users/ryan/.codex/worktrees/341e/chirality/projects/chirality-runtime/packages/core/src/worker-retirement.ts";
function gate() { let resolve, reject; const promise=new Promise((a,b)=>{resolve=a; reject=b}); void promise.catch(()=>{}); return {resolve,reject,promise}; }
const root=await realpath(await mkdtemp("/private/tmp/runtime-conformance-resume-20260906/REVIEW_RETIREMENT/state-"));
const identity={canonicalRoot:root,cwd:root,accountId:"controlled",accountEpoch:1,policyDigest:"controlled"};
const compatibility={compatibilityIdentity:"root-runtime-1",contractBasisSha256:"a".repeat(64)};
const finished=gate(), pollingStarted=gate(), polling=gate(); let calls=0, live;
const supervisor={
 async acquire(workerId){live={workerId,generation:"controlled-generation",pid:0,state:"running"};return {...live}},
 async inventory(){return live?[{...live}]:[]}, async reconnect(){return {...live}},
 async wait(){return finished.promise}, async retire(){calls++; live=undefined},
 async pendingNetworkApprovals(){pollingStarted.resolve();return polling.promise}, async replyNetworkApproval(){}
};
const retirement=new WorkerRetirementCoordinator({directory:join(root,"journal")});
const runtime=new DelegatedRuntime({daemonId:"review",projects:new Map([["p",{identity,compatibility,supervisor,retirement,consent:{async read(){return {identity,posture:"off"}}},approvals:{},approvalForwardingEnabled:true,evidenceClass:"controlled-worker"}]])});
try {
 const preflight=await runtime.preflight("p","turn:t");
 const result=runtime.turn("p",{turnId:"t",prompt:"controlled",compatibility,preflight}); void result.catch(()=>{});
 await pollingStarted.promise;
 finished.reject(new Error("wait failed"));
 try{await result}catch(e){console.log("turn error:",e.message)}
 console.log("before late polling failure:",JSON.stringify({calls,record:await retirement.read("t")}));
 polling.reject(new Error("late approval snapshot failure"));
 await new Promise(r=>setImmediate(r));
 console.log("after late polling failure:",JSON.stringify({calls,retirementMapSize:runtime.turnRetirements.size}));
 if(calls!==1)process.exitCode=1;
}finally{await rm(root,{recursive:true,force:true})}
