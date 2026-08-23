# Fresh Review — N1 SCA-004 Gate 3 / Gate 4 drafts, cycle 2

Verdict: `FAIL — ONE ACTIONABLE FINDING`

Review basis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`

Review posture: fresh independent, read-only, non-delegating Agent-2 review.
No N1 output was repaired or modified.

This review does not approve Gate 3, approve Gate 4, open Gate 5, amend live
decomposition truth, materialize a deliverable, lift a hold, or confer
implementation, pointer, App-loop, publication, release, or merge authority.

## Actionable finding

### N1-R2-F1 — MEDIUM — `Amendment_Actions.csv` omits the required supersession-binding field

`agents/AGENT_SCOPE_CHANGE.md` defines the machine-readable
`Amendment_Actions.csv` schema with nine columns, including the required
boolean `SupersessionBindingPresent`. The Phase-0c steer also requires the N1
package to be produced in the SCA-002 form; SCA-002's live action register
uses that nine-column schema. The repaired SCA-004 register instead has the
older eight-column header:

```text
AmendmentID,ActionSeq,ActionType,EntityType,EntityID,Description,AffectedFiles,DownstreamReruns
```

and supplies no supersession disposition for any of its eight actions. This
leaves the Gate-4 machine action register structurally incomplete even though
the human-facing propagation plan is otherwise complete. The existing
85-check validator does not inspect the action-register schema, so its PASS
does not close this finding.

Bounded repair: add `SupersessionBindingPresent` as the ninth column and an
explicit governed value for each of the eight actions. On the current record,
all eight appear to be structural/allocation actions with no admitted-authority
fact supersession, so `NO` is the evidence-supported value unless the repair
finds a specific admitted-authority conflict. Revalidate the CSV shape and
update every affected hash/evidence claim, including the instance return.
Adding a deterministic schema assertion to the local validator is recommended
if the validator is intended to evidence the complete N1 package. Do not alter
live decomposition truth or widen the N1 write set.

## Cycle-1 findings — closure check

- `N1-R1-F1` is closed. An independent inverse derivation over every candidate
  forward, scope, objective, package, and deliverable row produced zero
  mismatches across 6 packages and 53 deliverables. The repaired reverse rows
  now include `OBJ-3` for DEL-01-04 and `OBJ-4` for DEL-03-01, DEL-03-06, and
  DEL-06-04; PKG-04 carries the E-2 consequence.
- `N1-R1-F2` is closed. The candidate rows explicitly carry the complete G0
  A3 semantics across DEL-02-07/09/10/12 and the complete A7 semantics across
  DEL-02-08/09/10/12, including labelled fallback, evidence calibration,
  instruction+config assertion, hard containment, all three per-root network
  postures, visible host/protocol, same-destination grouping caveat,
  explicit-user-act `acceptForSession`, separately enumerated OpenAI service
  endpoints, and exact-pin G-APPR proof.
- `N1-R1-F3` is closed. The fixed `DerivativePackageState` value is now
  `INCOMPLETE`, which is in the closed SCOPE_CHANGE vocabulary.

## Independent checks that passed

- Every bound live decomposition/register/trace/telemetry SHA-256 and
  `execution/_ScopeChange/_LATEST.md` reproduces the Phase-0c basis.
- `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`,
  `WORK_GRAPH.json`, `DAG.md`, `Impact_Assessment.md`, and the Gate-1
  AUDIT_DECOMP coverage summary remain byte-identical to their protected
  basis identities.
- A fresh deterministic build in an isolated temporary root reproduced all
  seven candidate SHA-256 identities and `Gate_3_Exact_Amendment.diff`
  byte-for-byte.
- Applying the exact diff with `--unidiff-zero` to isolated copies of the
  seven bound live files reproduced every candidate byte exactly.
- A separate isolated execution of `validate_gate3_candidate.py` reproduced
  `PASS: 85 checks, 0 failures`, and its JSON was byte-identical to the
  reviewed `Gate_3_Validation.json`.
- Independent full-register checks confirmed 53 unique deliverables, 104
  unique scope items, 7 supported objectives, 59 unique reverse units, zero
  unmapped IN rows, zero dangling/asymmetric scope or objective mappings, and
  exact objective-register/forward-register agreement.
- Projected topology is correct: PKG-02=12, PKG-04=11, other package counts
  unchanged, six packages total, and Context Envelopes S=14, M=38, L=1.
- The seven candidate IDs are collision-free and unmaterialized. Every new
  row is parented to PKG-02 or PKG-04, carries a complete bounded M envelope,
  uses an accepted software artifact-kind type, focuses on one primary
  artifact shape, and declares a non-authorizing write locus.
- DEL-02-06 retains SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, its
  standing integration/release-assurance role, and the ten-binding hold
  boundary. DEL-04-11 is a PKG-04 `TEST_SUITE` mapped exactly to SOW-041,
  SOW-053, and OBJ-003 under the recorded cross-package coverage rule.
- G0 A4 is exact in DEL-02-11: active-turn terminalization, conditional
  `thread/resume` under canonical-root/account/policy-digest continuity with
  canonical cwd, fresh-thread fallback, and no in-flight re-attach claim.
- R2-A is reproduced byte-verbatim in `Decision_Log.md`; Gate 3 and Gate 4
  remain separately `PENDING_OWNER_APPROVAL`.
- The Gate-3 preview ends with the required exact-amendment question. The
  Gate-4 plan names all seven PREPARATION INIT folders and four-file posture,
  the DEL-02-06 context edit list, dependency/estimate/schedule advisories,
  graph and audit reruns, a distinct closure-validation lane, pointer
  quarantine, rollback/stop rules, and a separate Gate-4 question.
- `git diff --check` and candidate-whitespace validation pass.
- No live decomposition, companion register, pointer, `_STATUS.md`, package
  folder, SOW, dependency, estimate, schedule, runtime, tool, App, hold, pin,
  or Gate-5 surface changed. Concurrent N2 governance-harness work is outside
  this review and was not touched.

## Disposition

N1 is not ready for HELP_HUMAN fan-in because its Gate-4 machine action
register is not schema-complete. Repair only N1-R2-F1, refresh the affected
evidence identities, and submit the complete package to a fresh independent
review. The exact Gate-3 candidate surfaces themselves otherwise passed this
cycle's independent reconstruction and semantic checks.
