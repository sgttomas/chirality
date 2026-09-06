import { DelegatedRuntime } from "../../../../../../packages/core/dist/delegated-runtime.js";
const compatibility = { compatibilityIdentity: "root-runtime-1", contractBasisSha256: "a".repeat(64) };
const identity = {canonicalRoot:process.cwd(),cwd:process.cwd(),accountId:"fixture",accountEpoch:1,policyDigest:"p"};
let grants=0, acquired=0, closeDone=false, acquiredAfterClose=false;
let release, entered; const gate=new Promise(r=>release=r); const reached=new Promise(r=>entered=r);
const binding={identity,compatibility,evidenceClass:"controlled-worker",consent:{grant:async()=>{grants++},read:async()=>{entered();await gate;return {posture:"off"}}},retirement:{read:async()=>undefined,prepare:async()=>{},terminalize:async x=>x},supervisor:{inventory:async()=>[],acquire:async id=>{acquired++;acquiredAfterClose=closeDone;return{workerId:id,generation:"g",pid:1,state:"running"}},wait:async()=>({exitCode:0,stdout:"ok"}),retire:async()=>{}}};
const runtime=new DelegatedRuntime({daemonId:"d",projects:new Map([["p",binding]])});
const preflight=await runtime.preflight("p","different-operation");preflight.operationId="consent";
await runtime.grantConsent("p",{compatibility,preflight,posture:"off",approvedBy:"review",explicitUserAct:true});
let malformedError;try{const p=await runtime.preflight("p","consent");await runtime.grantConsent("p",{compatibility:{compatibilityIdentity:{toString:0},contractBasisSha256:"a".repeat(64)},preflight:p,posture:"off",approvedBy:"review",explicitUserAct:true})}catch(e){malformedError={name:e.name,code:e.code??null}}
const turn=runtime.turn("p",{compatibility,preflight:await runtime.preflight("p","turn:t"),turnId:"t",prompt:"x"});await reached;await runtime.close();closeDone=true;release();await turn;
console.log(JSON.stringify({mutableNonceAccepted:grants===1,malformedError,acquired,acquiredAfterClose},null,2));
