# D-APP-85 — PROPOSAL: Post-Pilot `Remaining` Truth Reconciliation

Status: `PROPOSAL / AWAITING_RULING`

DecisionID: `D-APP-85`

Prepared: `2026-08-02`

PreparedBy: `HELPS_HUMANS`, managed by `HELP_HUMAN`

PreparationBasis:
`codex/appdev-postpilot-status-reconcile@e5fe7e66cca66836f49980f50ad32816c8b96861`
(the clean live branch, equal to `main` and `origin/main` when preparation
began).

This is an agent-authored proposal, not authority. It neither adopts the
read-only PROJECT_SETUP orientation return that triggered this check nor treats
the implementation evidence below as permission to edit project truth. Only an
owner ruling recorded in a D-APP-85 ruling record can activate the proposed
run. No discovery or repair has been executed.

## Decision request

```text
DecisionID: D-APP-85
RequestedBy: HELPS_HUMANS
Question: Should App-dev activate a narrowly scoped, two-gate RECONCILIATION run to determine whether 18 exact post-pilot `## Remaining` claim blocks still state current executable truth?
Options: Option A activates read-only evidence verification only and stops at Gate 2 with an exact repair/no-change manifest; Option B genuinely defers activation, discovery, and repair.
Recommendation: Option A. This recommendation is non-binding.
Evidence: This packet §§1–11; the 18 live `_STATUS.md` claim blocks in §3; D-APP-55 and D-APP-73; SCA-APP-003 accepted closure evidence; the shared-runtime G1–G5 returns; DEL-08-03 implementation/test evidence; AGENT_RECONCILIATION and the shared concordance method.
DownstreamBlocked: Every target-status, dependency, memory, run-record, completion-log, receipt, or other truth-surface edit; any repair; any closure claim; and Git closeout for such work.
```

## 1. Why a ruling is required

The live evidence creates a credible possibility that several `## Remaining`
claims still describe work that landed during or after the bounded shared-
runtime/local-agent pilot, and that the DEL-08-03 claim may not reflect all
current implementation and test evidence. That possibility is evidence, not a
finding of record.

`agents/AGENT_RECONCILIATION.md` requires a committed activation ruling,
activated scope, pinned method, and run pointer on the shared baseline before
discovery. Its discovery phases are read-only. Its R5 repairs require a later
human or engineering decision. D-APP-55 established the same separation for
App-dev: discovery does not authorize repair, and repair remains behind a human
gate. Therefore neither PROJECT_SETUP, HELP_HUMAN, HELPS_HUMANS, nor a future
RECONCILIATION worker may silently “tidy” these rows.

The problem is claim-level concordance, not a known mechanical replacement.
No distinct ordinary-maintenance option is offered: without a verified exact
manifest it would either bypass the activation and repair gates or reproduce
Option A under a less accurate workflow name. An owner may later direct a
bounded non-program repair only after supplying or accepting exact replacement
bytes and their evidence; that is not the present state.

## 2. Evidence is not authority

The following accepted evidence justifies verification but predetermines no
claim disposition:

| Evidence surface | What it evidences | What it does not authorize |
|---|---|---|
| `execution/_ScopeChange/SCA-APP-003_2026-07-22_Shared_Runtime_Local_Agent_Pilot/Closure_Repair_001.md` | PR #317 merged the validated runtime, Desktop, CLI, PEC seam, packaging, pilot, security, regression, and export work at `f090238f46a939c534f88d16aa65b67236427ed1`. | No status repair, lifecycle transition, release, PEC production use, or future-runtime milestone. |
| `execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-003_2026-07-23_1312/Scope_Closure_Report.md` and the owner-accepted pointer | SCA-APP-003 closed `CLOSED_WITH_OBSERVATIONS` for the bounded pilot. | No blanket statement that every affected deliverable residual was discharged. |
| `execution/_Coordination/AgentRuns/SHARED_RUNTIME_LOCAL_AGENT_PILOT_2026-07-22/RETURN_G1_RUNTIME.md` | Shared contracts/core/daemon/client/CLI, session/project registries, turn coordination, residency, lazy migration, and governed delegation were implemented and tested. | No authority to remove a conjunct whose current evidence is incomplete. |
| Same run: `RETURN_G2_PEC.md`, `RETURN_G3_INTEGRATION.md`, `RETURN_G4_SECURITY_REVIEW.md`, and `RETURN_G5_VALIDATION.md` | PEC seam, Desktop cutover, manifests/export, security remediation, packaging, live pilot, and broad validation completed within their recorded boundaries. | No PEC production authority, release, lifecycle acceptance, or post-hoc status disposition. |
| `frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`, `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`, and the Woven Dialogue run records | Current DEL-08-03-adjacent bytes and tests cover taxonomy, option states, admitted scope, inert intent, and query preservation. | No automatic conclusion that every DEL-08-03 conjunct is complete; admitted-source projection and lifecycle-separation evidence must be checked independently. |

Every Gate-1 discovery row must cite current implementation and current
verification at the frozen source state. Historical returns are leads and
provenance; they are not substitutes for current-state verification.

## 3. Exact candidate claim population

The activation scope is exactly the 18 top-level `Remaining` claim blocks
below. Paths are relative to `projects/chirality-app-dev/`. Line spans are
locator aids at the preparation basis; identity is the named path plus the
exact top-level bullet and all of its continuation/nested-annotation bytes at
the Gate-1 merge basis. Every row is `CANDIDATE_FOR_VERIFICATION`: discovery,
not this packet, determines aligned, stale, restate, remove, or no-change state.

| Claim | Deliverable | Candidate state | Exact live claim block | Verification question only |
|---|---|---|---|---|
| C01 | DEL-01-01 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth/_STATUS.md:11` | Project-manifest registration and checkout/user-data authority separation. |
| C02 | DEL-01-02 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register/_STATUS.md:11`–`:12` | Daemon/socket/store/residency/role/export reliance boundaries. |
| C03 | DEL-02-05 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_STATUS.md:11` | Credential-owner, daemon/provider/model status, and explicit-activation conjuncts. |
| C04 | DEL-03-02 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking/_STATUS.md:11` | Sole-daemon orchestration, locking, concurrency, restart, and no-duplicate-owner claims. |
| C05 | DEL-03-03 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter/_STATUS.md:11` | Socket API, thin proxies, routes, SSE, and replay semantics. |
| C06 | DEL-03-04 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-04_Interrupt_Cancel_and_Terminal_Outcome_Handling/_STATUS.md:11` | Interrupt/cancel, terminal ownership, restart recovery, drain, and single-outcome claims. |
| C07 | DEL-04-01 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_STATUS.md:11` | Packaged GUI/daemon/CLI root-runtime loading and attribution. |
| C08 | DEL-04-05 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_STATUS.md:11` | Exact oMLX control, identity, redirect/fallback, drain, and `NO_MODEL` conjuncts. |
| C09 | DEL-05-01 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration/_STATUS.md:11` | Central JSON/JSONL sessions and lazy non-destructive legacy reads/migration. |
| C10 | DEL-05-02 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL/_STATUS.md:11` | Daemon/project/Agent-1/residency events and redacted transition evidence. |
| C11 | DEL-06-03 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_STATUS.md:11` | One declared read tool, required local child, containment, and evidence. |
| C12 | DEL-08-03 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/_STATUS.md:11`–`:26` | Whole claim and annotation against current dispatch, projection, and lifecycle-separation evidence. |
| C13 | DEL-08-04 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_STATUS.md:11` only | Direct Agent-1 invocation, required Pi Agent-2 child, review, and missing-delegation behavior. |
| C14 | DEL-08-05 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/_STATUS.md:11` | Named child-run identity, permission, evidence, and manager-acceptance fields. |
| C15 | DEL-09-02 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions/_STATUS.md:11` | Named shared-runtime and PEC conformance checks. |
| C16 | DEL-09-03 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion/_STATUS.md:11` | Named failure, authorization, concurrency, migration, restart, pilot, and PEC test classes. |
| C17 | DEL-09-06 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md:11` only | Permissions, project authorization, no-TCP, credential isolation, and residency transport. |
| C18 | DEL-10-01 | `CANDIDATE_FOR_VERIFICATION` | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_STATUS.md:12` only | PEC registration plus profile/RBAC/data/human/scratch-demo fences. |

Exact exclusions from the population:

- DEL-01-02 lines 13–18 (future PEC v2 seam) remain an unrelated sibling.
- DEL-05-04 lines 11–32 are excluded in full because they form part of the
  unselected UI/API parity-evidence bundle. This packet does not select,
  activate, verify, or repair that bundle.
- DEL-08-04 line 12 (decision-replay artifact) remains an unrelated sibling.
- DEL-09-06 line 12 (R4-P49 packaging/release evidence) remains an unrelated
  sibling.
- DEL-10-01 line 13 (future domain-engine advancement) remains an unrelated
  sibling.
- DEL-03-01 is excluded because Receipt 103 already narrowed the superseded
  SCA-APP-003 residual to facade retirement.
- DEL-09-04 is excluded because later daemon-service reconciliation already
  narrowed its earlier SCA-APP-003 packaging residual and recorded the
  surviving work.
- Every other `## Remaining` claim in the 53-deliverable corpus is outside
  scope. Discovery may hash it for preservation but may not disposition it.

## 4. Option A — activate the narrow two-gate run (recommended)

Option A activates RECONCILIATION only for C01–C18 and accepts the calibration
conventions in §5. It authorizes a read-only, source-state-bound run through
calibration, inventory, claim verification, synthesis, and a fresh adversarial
fan-in. The terminal Gate-1 product is an exact repair/no-change manifest for
owner review.

Option A does **not** authorize any target-corpus edit. The run must stop at
Gate 2 even if every disposition appears obvious. No `_STATUS.md`,
`_DEPENDENCIES.md`, `Dependencies.csv`, `MEMORY.md`, deliverable `_run_records`,
`plans/PLAN_COMPLETION_LOG.md`, `loop/LOOP_RECEIPTS.md`, source, test, or other
truth-surface byte may change before the owner accepts the exact manifest.

Benefits:

- verifies every conjunct against current bytes rather than historical
  summaries;
- permits `NO_CHANGE` and partial-restatement outcomes instead of forcing
  closure;
- uses one bounded activation and one later exact repair gate;
- preserves an auditable reason for every changed or unchanged row.

Costs and risks:

- requires a main-merged activation tranche before dispatch;
- creates a small immutable evidence package even if every row is `NO_CHANGE`;
- may surface additional work, but such findings are evidence only and cannot
  expand C01–C18 without a new owner act.

## 5. Gate-1 frozen method and calibration conventions

The activation ruling must pin the merge commit carrying the ruling/register
flip and the following method surfaces at that commit:

- `docs/DELIVERABLE_CONCORDANCE_METHOD.md`;
- `agents/AGENT_RECONCILIATION.md`;
- `loop/WORKPLAN_2026-07-18b_app_dev_loop.md`; and
- this D-APP-85 packet as the project-specific narrow-run addendum.

The owner’s Option-A ruling accepts these exact conventions for this bounded
run so a separate scale-out gate is unnecessary:

1. One top-level bullet is one candidate claim block. Continuation lines and
   nested annotations belong to that block; excluded sibling bullets do not.
2. Each conjunct is independently inventoried. A whole bullet may be removed
   only if every conjunct is currently evidenced or the accepted manifest
   supplies exact narrower replacement text for surviving work.
3. Allowed Gate-1 dispositions are `EXACT_REMOVE_CANDIDATE`,
   `EXACT_RESTATE_CANDIDATE`, `NO_CHANGE`, and `ESCALATE_AUTHORITY_OR_EVIDENCE`.
   They are recommendations, never owner rulings.
4. Historical run returns are evidence leads. Current implementation and
   current verification at the frozen source state are required for an aligned
   behavioral disposition.
5. Tests prove only the behavior they cover. A green suite does not discharge
   an uncovered conjunct.
6. Gate wording is not removed merely because its named implementation tranche
   once ran; the underlying claim must be dispositioned.
7. All unrelated sibling residuals are byte-preserved. A source change during
   discovery marks affected rows `STALE_INPUT` and stops their disposition.
8. Discovery changes no lifecycle state, `Checking Approval SHA`, authority,
   decomposition, dependency truth, source, runtime, release, issuance, or
   professional-reliance state.
9. Any discovered scope, authority, lifecycle, or dependency change is routed
   to its owning workflow and shown as `ESCALATE`, not repaired in this run.
10. No outcome means “the deliverable,” package, pilot, or corpus is complete.

Calibration starts with C02, C12, and C18 because they span a multi-conjunct
shared-runtime claim, a claim with a nested historical annotation, and a
cross-project authority boundary. If any accepted convention is inadequate or
any new addendum is required, the run stops and returns to the owner rather
than silently scaling. If calibration passes without an addendum, the remaining
15 rows may proceed as one bounded discovery wave.

## 6. Required Gate-1 outputs

The activated run root must be a new immutable path under
`execution/_Reconciliation/DeliverableConcordance/` and contain at least:

- `RUN_BASIS.md` with the activation merge SHA, candidate-path hashes,
  accepted authority/decomposition/dependency pointers, overlap check, and
  method hashes;
- `CONVENTIONS.md` reproducing §5 and the calibration result;
- `CANDIDATE_CLAIM_LEDGER.csv` with one row per conjunct and exact evidence;
- `CURRENT_EVIDENCE_INDEX.csv` distinguishing authority, implementation,
  tests, historical evidence, and unknowns;
- `UNRELATED_REMAINING_PRESERVATION.csv` covering all excluded siblings and
  out-of-scope deliverables by path/hash;
- `EXACT_REPAIR_NO_CHANGE_MANIFEST.csv` with all C01–C18 represented exactly
  once, including before hash, recommended disposition, exact replacement
  bytes or `NONE`, evidence references, required authority, and checks;
- a fresh read-only Agent-2 adversarial return over all 18 claims, every
  non-`NO_CHANGE` disposition, every unknown, replacement-text exactness, and
  the preservation manifest; and
- `GATE_2_HANDOFF.md` containing the manifest SHA-256, exact owner token, open
  questions, rerun triggers, and the explicit stop state.

No target repair belongs in this derivative evidence root.

Agent-2 execution is file-read-only with no Bash, write, edit, network, native
Pi tools, or delegation. H1 under D-APP-84 grants no Bash now. Any tool need
outside the allowed read surface returns to the RECONCILIATION parent.

## 7. Gate 2 and later authorized mechanics

Gate 2 is a second owner decision over the immutable exact manifest. The Gate-2
handoff must render a token of this form, substituting the actual content hash:

```text
APPROVE D-APP-85 GATE 2 MANIFEST <sha256>: EXECUTE ONLY THE ENUMERATED REPAIRS; RETAIN ALL NO-CHANGE AND PRESERVATION ROWS.
```

The owner may amend, partially accept, or decline the manifest. Silence,
validation, a commit, a push, or an agent recommendation is not acceptance.

Only after a Gate-2 ruling may RECONCILIATION execute the enumerated R5 repair
tranche through one serialized integration owner. The accepted manifest must
name every writable file. `_STATUS.md` is the expected primary surface;
dependency, memory, deliverable run-record, completion-log, or receipt writes
occur only when the manifest gives a row-specific reason and exact treatment.
No “usual associated files” inference is allowed.

After repair, a fresh read-only backcheck must:

1. re-extract every changed claim against the final source basis;
2. prove exact equality to the accepted repair population;
3. prove excluded siblings and all out-of-scope residuals unchanged;
4. reproduce the no-change rows and unresolved escalations;
5. verify lifecycle and every `Checking Approval SHA` unchanged;
6. verify the six D-APP-81 historical relations remain `UNKNOWN`;
7. verify D-APP-84 Root conditions, H1 no-Bash, and parity non-selection remain;
8. append one governed loop receipt only after the repair/backcheck is accepted;
   and
9. route routine Git closeout through CHANGE after the coherent tranche is
   owner-approved.

Neither Gate 2 nor later repair creates release, issuance, lifecycle, authority,
decomposition, runtime, source, professional-reliance, or blanket-closure
effect unless a separate owning decision expressly says so.

## 8. Option B — defer (genuine no-action option)

Do not activate D-APP-85. Leave C01–C18 and every sibling byte unchanged. Do
not create a reconciliation run, discovery derivative, repair manifest,
receipt, or implementation task. The PROJECT_SETUP return remains non-
authoritative orientation evidence and may be rechecked in a later session.

Deferral does not affirm that the live claims are true or stale. It simply
leaves the possible mismatch unresolved and preserves the current executable
work surface.

## 9. Preserved boundaries

Both options preserve all of the following unless a later owning decision says
otherwise:

- every unrelated sibling and out-of-scope `Remaining` residual;
- D-APP-84’s Root-conditioned B1/V1/P1/X1/H1/R1 posture, including **H1 grants
  no Bash now** and the need for Root decisions, DEL-02-06 activation, generic
  implementation, and a later App SCOPE_CHANGE;
- the unselected UI/API parity-evidence option in
  `execution/_Coordination/APP_NEXT_WORK_SLATE_2026-07-29.md`;
- the six D-APP-81 clause-6 historical relations as `UNKNOWN`, including the
  DEL-08-03 relation; this run must not infer their historical basis;
- both Task Management registers byte-for-byte; no harvest, promotion,
  disposition, or direct register write follows from this packet;
- all lifecycle states and all `Checking Approval SHA` values;
- authority, decomposition, accepted scope-change snapshots and pointers,
  runtime/source/frontend behavior, dependency truth, release, issuance,
  publication, and professional reliance; and
- the rule that evidence coherence is not deliverable, package, pilot, or
  corpus closure.

## 10. On-ruling mechanics

If Option A is selected:

1. transcribe the exact owner token into a D-APP-85 ruling record;
2. change only the D-APP-85 register row to `RULED / ACTIVATION_PENDING_MAIN`
   and name the prospective run pointer;
3. commit and merge the ruling/register tranche to `main` through CHANGE;
4. re-derive that local `main` and `origin/main` contain the merge and freeze
   the merge SHA, method hashes, candidate hashes, dependency pointer, and
   overlap state in `RUN_BASIS.md`;
5. if any C01–C18 block changed from the packet basis, stop for revalidation;
   otherwise dispatch RECONCILIATION for calibration and read-only discovery;
6. perform fresh adversarial Agent-2 verification and return the exact Gate-2
   manifest without target writes;
7. stop for the owner’s Gate-2 ruling;
8. after an accepted Gate-2 manifest only, execute the exact repair, fresh
   backcheck, one receipt, and then CHANGE closeout.

If Option B is selected, record the deferral in the ruling/register surfaces
only. Do not dispatch RECONCILIATION and do not append a loop receipt merely
for this proposal packet.

## 11. Exact ruling tokens

Option A:

```text
APPROVE D-APP-85 OPTION A: ACTIVATE THE NARROW READ-ONLY RECONCILIATION RUN AND STOP AT GATE 2.
```

Option B:

```text
DEFER D-APP-85 OPTION B: NO ACTIVATION, DISCOVERY, OR REPAIR.
```

Any rider must be stated explicitly. The recommendation is Option A and is not
an owner ruling.
