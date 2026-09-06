import { WorkerRetirementCoordinator } from "../../../../../../../packages/core/dist/worker-retirement.js";
import {mkdtemp,rm,realpath} from "node:fs/promises";import {join} from "node:path";
const root=await realpath(process.cwd());const directory=await mkdtemp(join(root,"execution/_Coordination/AgentRuns/RUNTIME_EXECUTION_2026-09-06/IMPLEMENTATION/REVIEW/FINAL_INTEGRATION/race-"));
try{const c=new WorkerRetirementCoordinator({directory});const identity={canonicalRoot:root,cwd:root,accountId:"review",accountEpoch:1,policyDigest:"fixture"};let unreadable=0;const errors=[];
for(let i=0;i<30;i++){const turnId="race"+i;await c.prepare({turnId,identity,state:"prepared"});await Promise.allSettled([c.associateThread(turnId,"thread"+i),c.terminalize({turnId,workerId:turnId,generation:"generation",outcome:"completed",recordedAt:new Date().toISOString()})]);try{await c.read(turnId)}catch(e){unreadable++;errors.push(e.message)}}
console.log(JSON.stringify({iterations:30,unreadable,errors:[...new Set(errors)]},null,2));}finally{await rm(directory,{recursive:true,force:true})}
