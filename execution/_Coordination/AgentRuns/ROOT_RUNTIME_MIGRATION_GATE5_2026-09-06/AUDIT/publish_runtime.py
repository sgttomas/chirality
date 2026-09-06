from pathlib import Path
import json,csv,hashlib,datetime
R=Path('/Users/ryan/.codex/worktrees/341e/chirality');RUN=R/'execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06';E=R/'projects/chirality-runtime/execution';O=E/'_Evaluation/DecompCoverage/SCA005_MIGRATION_POST';O.mkdir(parents=True,exist_ok=False);x=json.loads((RUN/'AUDIT/runtime_measured.json').read_text());assert not x['failures']
def write(n,s):(O/n).write_text(s.rstrip()+'\n')
def csvw(n,h,rs):
 with(O/n).open('w',newline='') as f:w=csv.writer(f,lineterminator='\n');w.writerow(h);w.writerows(rs)
for p in E.glob('PKG-*/1_Working/DEL-*/Dependencies.csv'):x['inputs'][str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
dep=E/'_Evaluation/DepClosure/SCA005_MIGRATION_POST';x['inputs'][str((dep/'ARTIFACTS.sha256').relative_to(R))]=hashlib.sha256((dep/'ARTIFACTS.sha256').read_bytes()).hexdigest()
write('Brief.md','''# Runtime destination post-initialization audit brief

Parent HELP_HUMAN /root dispatch; Agent 2 AUDIT_DECOMP, native and instruction-asserted, no delegation. GPT-6; exact serving ID unavailable. Agent 0 role is not mechanically enforced.

SOFTWARE / ALL, execution root projects/chirality-runtime/execution; authority is the accepted Gate3 V3 exact subject (commit1aadcc61b2739fdca25c4b07259655836516baa4) and actual Gate3/4 owner records published at main8209bc54e0d133b19437c93b184cd50ba3d43489. Candidate-era payload labels are immutable provenance; actual approval/reference wrappers control acceptance status only.

Read actual AGENTS/AUDIT_DECOMP, approved Gate4 derivative/output scopes, prior baseline, copied accepted registers, all seven initialized contracts/metadata, and current derivative evidence. Parent released destination audit after actual guarded initialization; Root cutover is a separate later audit. Check seven qualified carriers,66 requirements,4objectives,1scope row and all104 source accounting. No activation or owner confirmation.

Write only this new immutable approved snapshot plus run AUDIT evidence. No source/tool/Git/pointer changes. Source preservation and output hashes are required. User reserves pointer moves; override AUDIT_DECOMP pointer publication step. Return findings, not acceptance.''')
write('Decomp_Coverage_Report.md','''# Runtime destination post-initialization coverage

**Structural coverage PASS:183 actual checks, zero failures. Overall WARNINGS** because the independent dependency tool reports an explicitly calibrated dialect limitation. This audit does not confirm Gate5, effective transfer, feature activation, remaining effort or release.

Accepted upstream is SCA005 Gate3 V3, with actual Gate3/4 approvals published through PR727 merge8209bc54e0d133b19437c93b184cd50ba3d43489. The live destination payloads equal approved hashes. Seven new contracts and metadata were independently measured after ordinary guarded OPEN→INITIALIZED. All seven have the chirality-runtime qualifier in the accepted registry; source Root IDs remain separate history.

| Core check | Verdict | Measured evidence |
|---|---|---|
| 1 Package coverage | PASS | One exact PKG-02_Runtime_Product folder. |
| 2 Deliverable coverage | PASS | Seven declared exact folders and metadata sets. |
| 3 Reverse coverage | PASS | No undeclared package or deliverable folders. |
| 4 ID consistency | PASS | Full slugs and qualified source/successor identities agree; no fabricated zero-padded predecessors. |
| 5 Context fidelity | PASS | All names, types, descriptions, human/manager responsibility, package and M envelopes match register. |
| 6 Artifacts/contracts | PASS for initialization; INFO for production | Seven live common resolver checks return valid SOW_V1. Forty anticipated outputs remain future production; initialization is not output completion. |
| 7 Objective mapping | PASS | Four objectives all map to all seven existing carriers. All local objective references equal accepted register. |
| 8 Ledger integrity | PASS | One inherited SOW-104 maps to one package/seven carriers/four objectives;66 unique qualified numbered requirements conserved, no duplicates. The approved cross-scope successor map accounts for all104 Root rows;104 is not the runtime ledger denominator. |
| 9 Derivative parity | SKIPPED variant-owned check | DOMAIN-specific; SOFTWARE publication hash and mapping checks performed separately. Dependency extraction and independent closure have actual evidence below. |
| 9b Package shape | PASS | Working surface names authoritative registers and derived preview artifacts. _AUTHORITY and PRD_AUTHORITY resolve exact accepted payloads and copied source contracts. No derived preview accepted as current audit. |
| 10 Snapshot/handoff | WARNING, bounded | No runtime _ScopeChange pointer is required or moved by this phase. Actual migration wrapper states approved publication, temporary Root custody and pending Gate5/effect. Dependency closure retains DEP-AUD-001 tool dialect warning; estimate/ordering are reconstructed evidence awaiting owner disposition. |
| 11 Lifecycle | PASS | Seven INITIALIZED; zero activated/IN_PROGRESS/ISSUED. |

`Checks.json`, matrix, contract and requirement CSVs record actual measurements. Numbered requirement conservation uses66 unique qualified IDs and seven exact full source hashes, not the count of repeated adjacent paragraphs in the immutable inherited trace. Source and successor SOW differences are the approved ownership/locus interpretation and initialization formatting/evidence references: no exclusions, security conditions, REQ-027 first-activation limit or nine holds are waived. No source SOW was rewritten.

Dependency closure: `projects/chirality-runtime/execution/_Evaluation/DepClosure/SCA005_MIGRATION_POST/ARTIFACTS.sha256`, seal835e20315704cc10d9c58ede44a80fc573169a707c6dbd77dc20b4b05355c702. Its actual independent topology is7registers,54rows (42anchors/12mirrors),6unique runtime fan-ins plus2separate governance edges, with no real missing target, isolate or cycle. The generic tool's seven false isolates are preserved and full-ID aliases were independently checked. DEP-AUD-001 remains an unresolved tool-discovery/normalization warning; it is not a source-graph blocker and is not silently converted to raw-tool PASS.

Current estimate and ordering evidence reside under runtime `_Estimates/SCA005_SUCCESSOR/` and `_Coordination/SCA005_SCHEDULE_BASIS/`; accepted historical1012hours split920runtime/92governance is a preserved basis, not current remaining effort. Their new owner acceptance remains pending. Broader Root canon/export/receiving-loop reconciliation and Root post-state audit are outside this destination snapshot.

Historical baseline findings remain intact: four SCA004 filename gaps follow the exact accepted historical-gap disposition, not retrospective repairs. Six of its seven production warnings relate to inherited runtime source contracts; those bytes remain historical while the new six successor contracts now pass current schema. The seventh, Root DEL04-11, remains a governance-successor responsibility. Forty anticipated runtime production outputs are not inferred complete.

Rerun after any accepted payload, SOW, metadata, dependency or authority-state change. Retain DEP-AUD-001 in final Gate5 disposition. This is derivative evidence and cannot replace accepted decomposition or owner confirmation.''')
issues=[['COV-001','10','WARNING','DERIVATIVE_SURFACE','Dependency audit','DEP-AUD-001','Generic dependency tool dialect warning; independent exact-ID topology PASS, warning remains for disposition','SCA005 approved DERIVATIVE_RECONCILIATION.csv',str(dep.relative_to(R))]]
for r in x['matrix']:r['ArtifactCoverage']='0/anticipated (not yet production)'
write('RUN_SUMMARY.md','''# Runtime post-initialization return

RUN_STATUS = WARNINGS. Structural checks183/183 PASS; one inherited dependency-audit tool-dialect warning, no new structural blockers. Topology1package/7deliverables/4objectives/1scope row/66requirements; approved source104map complete. Seven INITIALIZED; no activation.

Derivative evidence only, SCA005 Gate3/4 accepted basis. Gate5/effective-transfer/pointer/release not confirmed. Existing historical findings preserved. Parent owns remaining Gate5 fan-in and DEP-AUD-001 disposition. Rerun on any pinned source change.''')
write('Decision_Log.md','''# Decisions

Use actual owner records to interpret unchanged candidate-era approved payloads. Keep historical source identities qualified separately from destination identities. Resolve fields by semantic names, preserving full slugs. Count66 unique qualified requirements and pinned complete contracts. Use actual live SOW resolver, not prior reviewer PASS alone. Read destination status after parent release; Root post-state is not inferred. Preserve dependency raw warning and authoritative registry calibration together. Pointer step withheld under user owner-only instruction. No source/tool/Git edits or child delegation. Snapshot sealed only after actual initialization and dependency closure evidence arrived.''')
write('QA_Report.md','''# QA

PASS:183 checks zero failures; seven unique matrix rows;66 unique inherited requirement identities; all recorded authority and metadata/source hashes verified live immediately before seal. Actual dependency audit seal pinned. Current resolver reports all7SOW_V1 valid; all7statuses INITIALIZED. LF CSV outputs. No file outside approved new snapshot/run evidence scope written.

Limits: production-output completion, numeric remaining effort, feature behavior, host registration, acceptance/effective act and independent Root retirement are not claimed. Dependency dialect finding remains a warning despite correct independently measured topology.''')
summary={'run_label':'SCA005_MIGRATION_POST_RUNTIME','timestamp':x['timestamp'],'decomp_variant':'SOFTWARE','scope':'ALL','expected_source_snapshot':'execution/_ScopeChange/SCA-005_2026-09-05_2344/FINAL_INTEGRATION_V3/COMBINED_ARTIFACTS.sha256','expected_handoff_phase':'Gate5 application audit; owner confirmation pending','decomposition_path':'projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md','decomposition_revision':'1.0 accepted exact Gate3 subject','repository_topology':x['topology'],'partitions_declared':1,'partitions_found':1,'production_units_declared':7,'production_units_found':7,'forward_coverage_partitions_pct':100,'forward_coverage_production_units_pct':100,'reverse_coverage_pct':100,'context_fidelity_pct':100,'objective_coverage_pct':100,'artifact_presence_pct':0,'artifact_measurement':'40 anticipated production outputs not completed by initialization','deliverables_without_objective_mapping':0,'in_ledger_rows_without_objective_mapping':0,'package_shape_conformance':'PASS','derivative_package_status':'WARN','active_snapshot_status':'SKIPPED','handoff_state_status':'WARN','objective_evidence_integrity':'PASS','issues_blocker':0,'issues_warning':1,'issues_info':0,'check_count':12,'lifecycle_distribution':{'INITIALIZED':7},'overall_status':'WARNINGS','closure_readiness':'WARN','structural_checks_passed':183,'gate5_confirmed':False,'effective_transfer_confirmed':False,'concrete_labels':{'partition':'Package','production_unit':'Deliverable'}}
write('coverage_summary.json',json.dumps(summary,indent=2));write('Checks.json',json.dumps(x['checks'],indent=2));csvw('Decomp_Coverage_Matrix.csv',list(x['matrix'][0]),[list(m.values()) for m in x['matrix']]);csvw('Decomp_Coverage_IssueLog.csv',['IssueID','CheckNumber','Severity','EntityType','ConcreteLabel','EntityID','Description','DecompositionRef','FilesystemRef'],issues);csvw('Production_Contracts.csv',['DeliverableID','Format','Valid','Issues'],x['formats']);csvw('Requirement_Conservation.csv',['SourceIdentity','SuccessorIdentity','SourceSHA256','Present'],x['requirements']);csvw('INPUT_HASHES.csv',['Path','SHA256'],sorted(x['inputs'].items()))
for path,h in x['inputs'].items():assert hashlib.sha256((R/path).read_bytes()).hexdigest()==h,path
csvw('ARTIFACT_HASHES.csv',['Path','SHA256'],[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(O.iterdir()) if p.is_file() and p.name!='ARTIFACT_HASHES.csv']);print('SEALED',O)
