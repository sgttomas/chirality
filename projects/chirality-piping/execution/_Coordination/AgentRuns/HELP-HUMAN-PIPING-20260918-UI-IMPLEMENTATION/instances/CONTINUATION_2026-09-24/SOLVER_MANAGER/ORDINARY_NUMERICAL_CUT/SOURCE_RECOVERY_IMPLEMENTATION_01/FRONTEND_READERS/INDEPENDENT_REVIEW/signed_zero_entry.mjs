import {readFileSync,writeFileSync} from 'node:fs';
import {runPreviewMechanics,hasNativeMechanicsInvocation,retainedNativeMechanicsInvocation,buildAnalysisRunPreview} from "/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/apps/desktop/src/services/previewService.ts";
import {numericalResultStanding} from "/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/apps/desktop/src/features/results/numericalResultQuality.ts";
import {sourceBlockStanding} from "/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/apps/desktop/src/features/results/sourceBlockRecovery.ts";
import {buildCurrentSessionInputManifest} from "/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/apps/desktop/src/services/inputManifestService.ts";
const request=JSON.parse(readFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/fixtures/product_preview/source_blocks/ui/n05-dense_scrutiny.request.json",'utf8'));
const raw=JSON.parse(readFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/fixtures/product_preview/source_blocks/ui/n05-dense_scrutiny.raw.json",'utf8'));
import {buildReportPackageRequest} from "/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/apps/desktop/src/features/report/reportPackageRequest.ts";
const observed=[];let reportObservation;
globalThis.window={__TAURI_INTERNALS__:{}};
for(const initialNegativeZero of [false,true]) {
 const model=structuredClone(request.model);if(initialNegativeZero)model.nodes[0].position.x=-0;
 let sent;
 globalThis.__reviewInvoke=async(name,args)=>{if(name!=='run_preview_mechanics_with_solver_mode')throw new Error('Unexpected IPC '+name);sent=args;return structuredClone(raw);};
 const source=await runPreviewMechanics(model,'dense_scrutiny');
 const native=hasNativeMechanicsInvocation(source,model,'dense_scrutiny');
 const captured=retainedNativeMechanicsInvocation(source,model);
 const originalStanding=numericalResultStanding(source,model);
 const capturedStanding=captured ? sourceBlockStanding(source,captured.request.model):null;
 const manifest=await buildCurrentSessionInputManifest({model,solver:{solver_name:source.producer.component_name,solver_version:source.producer.component_version,solver_build_ref:'independent-review-genuine-pair-mocked-transport',solver_mode:'dense_scrutiny',settings:{}},active_rule_packs:[],external_assets:[]});
 if(!initialNegativeZero){
  const analysisRun=await buildAnalysisRunPreview(source,{inputManifest:manifest});
  try{
   const packet=await buildReportPackageRequest({model,result:source,analysisRun,inputManifest:manifest,projectSummary:null,comparison:null,ruleCheckAggregate:null});
   const rawSupports=source.results.filter(r=>r.kind==='support_reaction_component_v2');
   const exported=packet.result_envelopes.flatMap(e=>e.result_sets.flatMap(s=>s.values));
   reportObservation={returned:true,rawSupportCount:rawSupports.length,supports:rawSupports.map(r=>({id:r.id,rawMetadata:r.metadata,exported:exported.find(x=>x.result_id===r.id)})),envelopeKeys:Object.keys(packet.result_envelopes[0]),hasSourceReceipt:JSON.stringify(packet).includes('source_block_recovery'),envelopeHasProducerOrSemanticIdentity:['producer','semantic_contract','semantic_contract_ref'].some(k=>Object.hasOwn(packet.result_envelopes[0],k))};
   writeFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/GENUINE_SOURCE_REPORT_REQUEST.json",JSON.stringify(packet,null,2)+'\n');
  }catch(e){reportObservation={returned:false,error:String(e)};}
 }
 observed.push({initialNegativeZero,callerStillNegativeZero:Object.is(model.nodes[0].position.x,-0),sentNegativeZero:Object.is(sent.model.nodes[0].position.x,-0),actualRequestEqualsUnchangedProducerRequest:JSON.stringify(Object.keys(request).sort())===JSON.stringify(['materials','model'])&&JSON.stringify({model:sent.model,materials:[]})===JSON.stringify({model:request.model,materials:request.materials}),native,originalStanding,capturedStanding,manifestModelNegativeZero:Object.is(manifest.manifest.model_basis.model_payload.nodes[0].position.x,-0)});
}
const result={scope:'Actual frontend functions bundled without behavioral substitution, real existing Rust-WASM hashing/units, unchanged genuine producer pair, only native invoke mocked; no new solve or native witness.',observed,reportObservation};
writeFileSync("/private/tmp/piping-source-recovery-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT/SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS/INDEPENDENT_REVIEW/SIGNED_ZERO_NODE_OBSERVATIONS.json",JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
if(!observed.every(x=>x.actualRequestEqualsUnchangedProducerRequest&&x.native&&x.capturedStanding?.eligible))process.exitCode=2;
else if(!observed.every(x=>x.originalStanding.eligible))process.exitCode=1;
