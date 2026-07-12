# R2 Wave-1 Notes — DEL-02-03 Working Root File Tree and Scope Scan UI

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A whole corpus)
- **Deliverable:** DEL-02-03, PKG-02 Desktop Shell, Navigation, and Operator State
- **Source state (binding):** `frontend/` at `fac46e33f` (byte-identical through HEAD `052b3c2b2`; verified by orchestrator). Behavioral rows cite `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped) + named test/case (MR-3).
- **Method:** pinned plan §§5–8 @ `551f84ef6`; R2_METHOD_ADDENDUM MR-1..MR-11; run-local AUTHORITY_MAP.
- **Epistemic status:** evidence artifact, not authority. Dispositions are agent classifications for human review; no ruling, lifecycle action, or work selection is made here.

## 1. Claim census

23 claim rows in `DEL-02-03_claims.csv`.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 14 |
| EXCLUSION | 4 |
| IMPLEMENTED_UNMAPPED | 2 |
| ACCEPTANCE | 1 |
| REGISTER_DEFECT | 1 |
| REMAINING_WORK | 1 |

By Disposition:

| Disposition | Count | Rows |
|---|---:|---|
| ALIGNED | 18 | REQ-001..014, EXC-001/002/004, REMAINING-1 |
| IMPLEMENTED_UNDOCUMENTED | 2 | UNMAPPED-1 (file-tree auto-refresh), UNMAPPED-2 (symlink leaf handling) |
| STALE_SPECIFICATION | 2 | ACC-001 (PRD hash-mismatch condition, overtaken by D-APP-35/38); EXC-003 (dependency-deferral wording, overtaken by the 2026-05-20 extraction; accepted from fan-in, see §6) |
| REMAINING_STATE_MISMATCH | 1 | REGISTER-1 (register-internal dependency-edge metadata lag) |

Derived summary (not a deliverable verdict): the DEL-02-03 four-document kit is
current and matches implementation for all 14 requirements; INSP-03's 14 PASS
ratings are re-derived as STILL CURRENT at `fac46e33f` (no post-INSP-03 spec
rewrite occurred, so MR-9 old-REQ mapping is not needed — assessment IDs map
1:1). The discordant surfaces are (a) the PRD hash-mismatch condition still
carried in the kit though `_REFERENCES.md` now reads MATCH (ACC-001), (b) the
kit's dependency-deferral wording contradicted by the live 9-row register
(EXC-003, with the register-internal stub contradiction at REGISTER-1), and
(c) two material live behaviors with no owning requirement (auto-refresh,
symlink handling).

Verification texture worth flagging to R3 (corrected at fan-in, see §6):
component render coverage (renderToStaticMarkup) **does exist** for the
pipeline/portal widget half of this deliverable —
`frontend/src/__tests__/components/pipeline-surface.test.ts` (lines 63-81
category controls and TASK split selectors; 83-114 deep-link consumption with
target preselected; 116-144 stale deep-link reset during initial render) and
`frontend/src/__tests__/components/agent-matrix-panel.test.ts` (lines 40-47
deliverable launch rows with pkg::id keys). INSP-03 Gap 2 ("Component/browser
render coverage is still not settled", Medium) persists only for the
working-root half: FileTreePanel, the ShellFrame working-root bar, and
clear-disables states have no render test. D-APP-36 (UI render-test bar) is
cited as `(context)` on those render-gap rows; whether route/helper coverage
satisfies UI acceptance for them is the open governance question (INSP-03
Issuance-Gate-Process Observations).

Dependency re-verification (plan §5): all 9 `Dependencies.csv` rows re-read live
and consistent with the register's own metrics and the INSP-03 Dependency
Closure Note (3 ANCHOR NOT_APPLICABLE + 6 EXECUTION TBD). The 6 EXECUTION rows
legitimately remain `SatisfactionStatus=TBD`.

## 2. Least-confident rows (mandatory self-flagging)

The fan-in verifier should recheck these plus all non-ALIGNED rows
(ACC-001, EXC-003, UNMAPPED-1, UNMAPPED-2, REGISTER-1).

- **REQ-003 (ALIGNED, MEDIUM).** Clearing root disables root-dependent actions.
  The projectRoot dependency is enforced structurally (workspace-provider clear +
  file-tree-panel reset + pipeline-surface guards) but **no named test** exercises
  clear-disables. **Alternative reading that flips it:** STALE_VERIFICATION — the
  spec's promised state test (Verification line 58) does not exist; a strict
  reader treats the missing coverage as the operative defect. I chose ALIGNED to
  avoid manufacturing a finding whose repair is one small component test, matching
  the R0 calibration's ALIGNED-with-MEDIUM tolerance for structurally-enforced but
  unasserted behavior.
- **REQ-005 (ALIGNED, MEDIUM).** Skipped directories. `SKIP_DIRECTORY_NAMES` is
  exactly the six named dirs and is filtered in buildTree/scan, but **no fixture
  test** proves a `.git`/`node_modules` dir is absent from output (the spec's
  stated verification approach, line 60). **Alternative:** STALE_VERIFICATION on
  the same grounds as REQ-003.
- **REQ-007 (ALIGNED, MEDIUM).** Scope scan presents deliverables + knowledge
  types. Deliverable/knowledge data path is tested via `deliverables-route.test.ts`
  (scanProjectDeliverables) and the selector render via `pipeline-surface.test.ts`
  lines 63-81 (evidence strengthened at fan-in, see §6), but the
  `/api/working-root/scope` route and `scanProjectScopes` themselves remain
  untested. **Alternative:** PARTIALLY_IMPLEMENTED if a reader treats the untested
  scope route as a distinct unverified surface; I read the requirement as
  satisfied by the tested deliverables/knowledge data and render paths the UI
  consumes.
- **EXC-003 (STALE_SPECIFICATION, HIGH — flipped at fan-in, see §6).**
  "Dependency extraction … Dependencies.csv creation is deferred." The UI-scope
  exclusion (no extraction UI) is genuinely true and matches REQ-014, but
  `Dependencies.csv` exists (9 rows, extracted 2026-05-20), so the deferral
  clause flatly asserts a now-false state. Originally filed ALIGNED with the
  wording defect split out to REGISTER-1; the fan-in verifier refuted that split
  on MR-8 ("kit text flatly asserting a now-false state → STALE_SPECIFICATION")
  and the R0 calibration precedent DEL-02-01-EXC-004 (structurally identical,
  disposed STALE_SPECIFICATION HIGH). Accepted: the Spec line 19 and Procedure
  line 15 repairs are homed here; REGISTER-1 is narrowed to the
  `_DEPENDENCIES.md`-internal contradiction, which independently sustains it.
- **REQ-009 (ALIGNED, MEDIUM) — cross-deliverable surface overlap.** The
  routing evidence is the OPERATIVE Deliverable Rows launcher in
  `agent-matrix.tsx` (lines 129-130, 229-246). The DEL-02-01 R0 calibration
  flagged that **same launcher** as its UNMAPPED-3 (IMPLEMENTED_UNDOCUMENTED,
  unmapped to DEL-02-01). Here INSP-03 maps it to DEL-02-03 REQ-009. **This is a
  genuine two-deliverable claim on one surface** — an R3 synthesis item (plan §3
  R3: "same implementation surface claimed by incompatible deliverables"). Not
  resolvable at claim level; recorded for R3.
- **UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED, MEDIUM) — ownership uncertainty.**
  Symlink non-traversal is a filesystem-tree-API traversal behavior. It may belong
  to the PKG-07 workspace-tree-API owner rather than the DEL-02-03 UI slice, in
  which case it is out-of-scope-here rather than unmapped. INSP-03 nonetheless
  cited filesystem.ts as DEL-02-03 evidence (REQ-004/005/006), so I recorded it on
  this surface with an explicit R3 ownership note. **Alternative:** drop from
  DEL-02-03 if R3 assigns the tree/scan traversal contract to a PKG-07 deliverable.

## 3. Register-defect summary (MR-5)

- **REGISTER-1 (REMAINING_STATE_MISMATCH; narrowed at fan-in, see §6).**
  `_DEPENDENCIES.md` pre-extraction "Declared Upstream/Downstream: TBD - no
  declared dependency edges" stubs (lines 14-18) internally contradict the same
  file's populated "Extracted Dependency Register" section / Lifecycle Summary
  (9 ACTIVE) and the live 9-row `Dependencies.csv`. Pure register-internal
  metadata lag; the register data itself is internally consistent and matches
  the INSP-03 closure note. The parallel Specification/Procedure kit wording is
  homed at EXC-003 (STALE_SPECIFICATION). R5 doc-repair candidate; the 6
  EXECUTION rows correctly stay `TBD`.

Note (not a register row): `Dependencies.csv` uses `AnchorType=NOT_APPLICABLE`
on the 6 EXECUTION rows — this is the register's normal convention for
non-anchor rows (matches the DepClosure baseline), not a defect. Test fixtures in
`task-scope-selection.test.ts` and `deliverables-route.test.ts` use a third
package-folder label variant (`PKG-02_Desktop_UI_Workflow`) distinct from both
the dispatch label and the scaffold folder; this is an arbitrary fixture string,
label-agnostic by construction (`buildDeliverableCompositeKey`), and not a
product defect.

## 4. Open conflict not expressible as a claim row

`Guidance.md` CONFLICT-001 / Pass-3 A-001 (dispatch package-folder label
`PKG-02_Desktop_UI_and_Local_Experience` vs the scaffold folder
`PKG-02_Desktop_Shell_Navigation_and_Operator_State`) remains an open,
already-documented human-ruling item in the deliverable's Conflict Table. It maps
to no requirement/acceptance/exclusion and this run does not resolve it; stable
IDs `PKG-02`/`DEL-02-03` govern per the deliverable's own proposed authority. It
is preserved (per ACC-001 RemainingWork) rather than given its own row.

## 5. Method deviations

None. The 19-column §6 header, §7 dispositions plus the MR-5 REGISTER_DEFECT
extension, MR-1 assessment tokens, MR-2 (only REMAINING-1 = YES), MR-3/MR-10
verification citation forms, MR-4 (Datasheet restatements folded into REQ rows;
the single datasheet-distinct condition — the PRD source warning — emitted as
ACC-001), MR-6 (RemainingGate verbatim `UNGATED`/`NONE_RECORDED`), MR-7
governance-vs-context on LatestDecision, and MR-8/MR-11 tie-breaks were all
applied as written. No `DEFERRED_AGENT_WORKFLOW` or `AUTHORITY_CONFLICT` arose:
nothing in this deliverable required judging an agent instruction, and the one
hard precedence question (kit hash-mismatch vs refreshed `_REFERENCES.md`) is
resolved by AUTHORITY_MAP precedence note 1 + the D-APP-35/38 rulings (MR-11), not
left to choose.

## 6. Fan-in reconciliation record (2026-07-11)

Fan-in verification returned one REFUTED verdict and two factual corrections;
all three were re-verified against the tree by this row owner and **accepted**
(nothing contested):

1. **EXC-003 flipped ALIGNED → STALE_SPECIFICATION (HIGH).** Verifier basis:
   MR-8 is binding on flatly-false kit text, and the owner-adopted R0
   calibration disposed the structurally identical DEL-02-01-EXC-004 as
   STALE_SPECIFICATION HIGH. Accepted; the Spec line 19 + Procedure line 15
   repairs are now homed at EXC-003, and REGISTER-1 was narrowed to the
   `_DEPENDENCIES.md`-internal stub contradiction (which independently
   sustains it). Census tables above reflect the post-fan-in state.
2. **Render-coverage claim corrected.** My original notes asserted no
   component/browser render test exists for any DEL-02-03 UI surface; this was
   factually wrong — `pipeline-surface.test.ts` and `agent-matrix-panel.test.ts`
   (renderToStaticMarkup) cover pipeline widgets, TASK scope selectors,
   deep-link consumption/reset, and OPERATIVE deliverable rows (re-verified:
   cases at lines 63/83/116 and 40 respectively). VerificationEvidence on
   REQ-007/REQ-008/REQ-009 was strengthened accordingly; dispositions
   unchanged (ALIGNED). INSP-03 Gap 2 persists only for FileTreePanel, the
   ShellFrame working-root bar, and clear-disables states.
3. **REQ-003 citation fixed.** pipeline-surface.tsx line 417 is inside
   `canSubmitTransition` (lines 416-420); the scaffold guard is line 472.
   ImplementationEvidence cell corrected (re-verified against the file).
