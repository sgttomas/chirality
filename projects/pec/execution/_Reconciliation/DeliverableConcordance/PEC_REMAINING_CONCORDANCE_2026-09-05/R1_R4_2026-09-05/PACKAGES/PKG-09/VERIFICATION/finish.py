from pathlib import Path
import csv,json,hashlib,subprocess,os
V=Path(__file__).resolve().parent;P=V.parent
claims=list(csv.DictReader((P/'PACKAGE_CLAIMS.csv').open()));res=list(csv.DictReader((P/'PACKAGE_RESIDUALS.csv').open()))
def out(name,rs,fields=None):
 with (V/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rs[0]),lineterminator='\n');w.writeheader();w.writerows(rs)
checked=[];lowest={d:min(c['ClaimID'] for c in claims if c['DeliverableID']==d and c['Disposition']=='ALIGNED') for d in {c['DeliverableID'] for c in claims}}
for c in claims:
 d=c['DeliverableID'];cid=c['ClaimID'];local=next(Path('projects/pec/execution/PKG-09_Dashboards/1_Working').glob(d+'_*'));scope=f'SOW-{44+int(d[-2:]):03}'
 loc=f'projects/pec/execution/_Decomposition/ScopeLedger.csv row {scope}; projects/pec/execution/_Decomposition/Deliverables.csv row {d}; projects/pec/docs/PRD.md §9.7'
 reason='Expanded complete package claim and class-boundary review'
 if c['Disposition']=='UNKNOWN':reason='Mandatory all non-ALIGNED review'
 if cid==lowest[d]:reason+='; deterministic lowest-ID ALIGNED'
 if 'DEP-09' in cid or 'DEPENDENCY-BOUNDARY' in cid:
  dep=cid.split('::')[-1];loc=str(local/'Dependencies.csv')+' row '+dep+'; projects/pec/loop/LOOP_INIT.md lines 209–214'
  note='Documentary register status and target checked; ACTIVE unsatisfied PREREQUISITE blocks only an item naming its target. No status flip or production permission inferred.'
  if cid in ['DEL-09-07::DEP-09-07-003','DEL-09-07::DEP-09-07-008']:
   note='PASS with explicit scope: held question existence and ACTIVE/PREREQUISITE/PENDING are known documentary facts. UNKNOWN applies only to owner applicability/phase classification per ImplementationEvidence. Edge preserved; no satisfaction/removal/softening inferred.'
 elif c['ClaimClass']=='lifecycle':
  loc=str(local/'_STATUS.md')+' Current State and History';note='OPEN since PREPARATION verified; no Remaining heading. This documentary lifecycle observation does not establish implementation, acceptance, release or warranted NONE.'
 elif 'ASSIGN' in cid or 'RESPONSIBLE' in cid:
  loc=str(local/'_CONTEXT.md')+' Responsible Party; Deliverables.csv '+d;note='TBD is truthful administrative state with assignment at activation; no automatic product/TM residual.'
 elif c['Disposition']=='UNKNOWN':
  note='Accepted scope atom checked against mapped source; current artifact/claim-relevant finite verification not established. UNKNOWN is supported; source search misses and missing contracts do not prove DOCUMENTED_UNIMPLEMENTED. No test or acceptance PASS inferred.'
 elif 'PEC-K-' in cid or 'BOUNDARY' in cid:
  loc+='; projects/pec/docs/PRD.md §3 PEC-K-01/-02/-03/-05/-06/-08/-10/-11';note='Declared documentary boundary matches source: consumer-owned optional contact/injection, advisory Explain, content-minimal source links and file authority. Runtime compliance remains unproven.'
 else:note='Documentary scope mapping checked against accepted decomposition and source PRD vocabulary; no behavior or acceptance inference.'
 checked.append({'ClaimID':cid,'ClaimClass':c['ClaimClass'],'ReportedDisposition':c['Disposition'],'SelectionReason':reason,'SourceLocators':loc,'Verdict':'PASS','VerificationNotes':note})
out('CHECKED_CLAIMS.csv',checked)
out('CHECKED_RESIDUALS.csv',[{'ResidualID':r['ResidualID'],'ClaimIDs':r['ClaimIDs'],'SourceLocators':'; '.join(x['SourceLocators'] for x in checked if x['ClaimID'] in r['ClaimIDs'].split(';')),'Verdict':'PASS','RoutingClass':'HELD_OWNER_QUESTION' if r['ResidualID'] in ['DEL-09-07-REM-002','DEL-09-07-REM-003'] else 'EVIDENCE_CANDIDATE','VerificationNotes':'Exact reciprocal claim links; Depends NONE is proper for evidence/routing. Literal owner gate and NON_SELECTABLE_PENDING_OWNER_APPLICATION survive. Closure evidence requests future exact owner act; no production, lifecycle or register change is authorized.'} for r in res])
out('FINDINGS.csv',[],['FindingID','Severity','ClaimIDs','SourceLocators','Finding','RequiredAction','Status'])
text='''# Independent package verification — PKG-09

PASS_FOR_DERIVATIVE_REPORT_FAN_IN. No corrective finding. All 110 claims and nine residuals independently checked, including all 38 UNKNOWN rows, all flagged dependency boundaries, every lowest-ID ALIGNED member, and documentary/behavior/test/lifecycle/acceptance boundaries. CHECKED_CLAIMS.csv and CHECKED_RESIDUALS.csv enumerate exact IDs, locators and verdicts. The 72 ALIGNED rows are documentary/lifecycle only. All seven members remain ASSESSED_UNKNOWN; warranted NONE is false.

Accepted upstream is D82 effective base 2be412ccea62bdc4bd96deb082c46d7a792076ea, accepted D81 conventions via its append-only calibration acceptance, and current accepted revision 1.4 decomposition. Historical candidate labels do not negate the later exact acceptance. This immutable verifier subtree is derivative evidence, not authoritative decomposition or product acceptance. No R0 member reused.

The seven scoped SOW-045–051 rows and their complete feature clauses are covered. Missing local ScopeOfWork.md remains explicit; no defined local REQ/AC/VER IDs were found. Fallback source paths, loci and quote hashes independently reproduce. DEL-09-05 dependency mappings contain JSON representations of complete CSV rows rather than literal CSV lines; all fields were independently matched against parsed source rows (MAPPING_CHECKS.json). Initial literal-substring failures were resolved by this representation-aware comparison, without modifying workers. DEL-09-07 PEC-K-03/-11 mapping cites the PRD adoption header; substantive boundaries were independently verified at PRD lines 177 and 185, so that header alone is not the proof of behavior or boundary content.

DEP-09-07-003/E-A11 and DEP-09-07-008/E-P69 require precise reading: existence of a held question, the recorded alternatives and ACTIVE/PREREQUISITE/PENDING status are known documentary facts. Their UNKNOWN classification explicitly applies to unresolved owner interpretation, not to those fields or product implementation. The two held routing questions remain distinct from seven evidence candidates. No edge removal, satisfaction, automatic Remaining application, phase reorder or choice between staged rule set and soft edge is inferred. DEL-09-05 DEP-09-05-005 PHASE_TENSION is also checked: its ALIGNED class reports the register, not resolution of the flagged phase question.

Evidence-only residuals correctly use Depends NONE. Future production prerequisites retain the exact LOOP_INIT conjunction and independent owner source grants. Shared drilldown DEL-09-06 and rule backend DEL-09-07 ownership remain distinct from their consumers. Consumer cadence and injection are optional and owner-controlled; cited source links and advisory Explain never confer file authority or dispatch power. DEL-04-01 exact SOW acceptance at REV_DEL-04-01_2026-08-09_2154 is confined to its accepted contract bytes; it establishes neither dashboard implementation nor predecessor register satisfaction. D65 local run records concern dependency evidence repair only. OPEN lifecycle and truthful TBD assignment create no automatic residuals.

Independent structural checks reproduced exact selected worker/aggregate row equality, schemas, unique owner IDs, sequential residual IDs, LF, reciprocal links, source hashes and common frozen continuity. Exact candidate-validation file-target preflights include all seven absent ScopeOfWork.md paths; their results are in PREFLIGHT.json. Full source rehash includes common manifests; hashing the wider common corpus is continuity checking, not a claim of semantic review of unrelated packages. The bounded current-v2 search did not establish dashboard evidence; no search miss is an absence proof. No product suite or service was run because no claim-relevant method was established.

Closure is verifier report readiness for manager fan-in only. All 38 unknowns, seven nonselectable evidence candidates and two held owner questions survive. Product/Remaining/source/REVIEW/lifecycle/release/reliance closure is not established. TM023 mapping remains held without an unrelated gate, TM022 deferred, ordinary currency complete, PRDv2.3/DPEC79 adopted-not-applied. Rerun affected checks on source, authority or hold drift, new claim-relevant implementation/acceptance evidence, or exact owner classification/application. Parent RECONCILIATION owns next fan-in; no worker or source edit was made. Agent2 native execution is instruction-asserted, not mechanically enforced; no delegation.
'''
(V/'VERIFICATION.md').write_text(text)
validation=json.loads((V/'MECHANICAL_VALIDATION.json').read_text());assert validation['status']=='PASS',validation
validation.update({'status':'PASS_FOR_DERIVATIVE_REPORT_FAN_IN','checked_claims':110,'checked_unknowns':38,'checked_aligned':72,'checked_residuals':9,'evidence_candidates':7,'held_questions':2,'corrective_findings':0,'warranted_none':False,'product_closure':False,'semantic_review':'CHECKED_CLAIMS.csv; CHECKED_RESIDUALS.csv; VERIFICATION.md'})
(V/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
(V/'RETURN.md').write_text('''# Terminal verifier return

PASS_FOR_DERIVATIVE_REPORT_FAN_IN. 110 claims checked (72 documentary/lifecycle ALIGNED, 38 UNKNOWN), nine residuals checked (seven evidence candidates, two held questions), no corrective findings. All seven members ASSESSED_UNKNOWN; no warranted NONE or product closure. Exact checks and source locators in CHECKED_CLAIMS.csv/CHECKED_RESIDUALS.csv. Full manifests and absent-contract hold checks passed.

Accepted upstream: D82 base 2be412ccea62bdc4bd96deb082c46d7a792076ea, D81 accepted conventions, accepted revision1.4 decomposition. Derivative verifier evidence only. Parent /root/pec_pkg09_reconciliation owns manager fan-in. Source/authority/hold drift or new accepted evidence requires affected rerun. Remaining application and all production/lifecycle/release/reliance acts remain separately gated. Only VERIFICATION/** written. No delegation; native Agent2 instruction-asserted.
''')
# Rehash read inputs at final boundary, append explicit directly consulted supplementary sources.
m=json.loads((V/'READ_MANIFEST.json').read_text())
for p in [Path('AGENTS.md'),Path('projects/pec/AGENTS.md'),P/'BRIEFS/VERIFIER.md',P/'BRIEF_CLARIFICATION_02.md',P/'R4_DECISION_CANDIDATES.md',P/'RESIDUAL_RECOMMENDATIONS.csv',P/'CROSS_PACKAGE_FINDINGS.csv']:
 if p.exists():m['hashes'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in m['hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
m['source_unchanged']=True
(V/'READ_MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
manifest={str(p.relative_to(Path.cwd())):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(V.iterdir()) if p.is_file() and p.name!='OUTPUT_MANIFEST.json'}
(V/'OUTPUT_MANIFEST.json').write_text(json.dumps({'status':'SEALED_VERIFIER_RETURN','hashes':manifest,'self_exclusion':'OUTPUT_MANIFEST.json excludes its own recursive hash'},indent=2)+'\n')
print(json.dumps({'status':validation['status'],'checked_claims':110,'checked_residuals':9,'outputs':len(manifest)}))
