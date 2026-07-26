# NOTICE — `AGENT_AUDIT_DECOMP.md` / `AGENT_SCOPE_CHANGE.md` changed; two unruled drifts in this loop's coverage emission, 2026-07-25

Routed to this surface under `AGENTS.md`'s agent-index change-notice rule. This
loop references `agents/AGENT_SCOPE_CHANGE.md` in
`_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md`, `loop/LOOP_RECEIPTS.md`,
and `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`, and its
`coverage_summary.json` emissions are governed by `agents/AGENT_AUDIT_DECOMP.md`.

**This is coordination, not authority.** The chirality-app-dev loop adopts,
amends, or declines under its own instruments and cadence.

**No hash gate fires.** No `_REFERENCES.md` Authoritative Source Corpus row in
this loop targets any file changed by this tranche, so corpus-drift detection
would not have surfaced the change.

## What changed

1. **Variant Section Binding, both agent files** — sections are now bound **by
   heading text, never by section number**, using an explicit normalization
   (strip `## `, strip a leading `N.`/`NA.`, trim, case-fold) and rank order
   (exact → prefix → substring), with earliest-heading tie-break plus reported
   ambiguity, and halt-and-report when no rank hits. The four wrong SOFTWARE
   citations (Packages §3, Deliverables §4, Scope Ledger §5, Change Log §8) are
   gone. This loop's
   `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` was
   one of the three documents the spec was verified against; it is the case that
   forced the substring rank, because its `## 12. Decision Log / Change Log`
   merges two alternation members into one heading.
2. **`AGENT_AUDIT_DECOMP.md` IssueLog schema** — `CheckNumber` is redeclared
   **`string`** over `1`–`9`, `9b`, `10`, `11`. It was `integer` / `1–11`, which
   could not express the `9b` sub-check and undercounted the 12 checks the SPEC
   actually runs.
3. **`AGENT_AUDIT_DECOMP.md` `coverage_summary.json` template** — gained
   `deliverables_without_objective_mapping` and
   `in_ledger_rows_without_objective_mapping`; the mis-indented
   `derivative_package_status` key was aligned.
4. Also in the tranche, not currently referenced by this loop: the
   `scope-of-work` skill contract (INIT/CONVERT branching, upstream-ID
   blockquote citation rule, matrix row semantics),
   `tools/query/count_workspace_state.sh` (two counting defects fixed),
   `tools/validation/validate_semantic_pipeline_scope.py` (`--step init`, allowing
   `ScopeOfWork.md` + `_STATUS.md`), and
   `tools/scope_of_work/derive_review_checklist.py` (stderr warning for
   multi-AC/multi-VER matrix rows; derived JSON byte-identical).

   Note on citations (corrected after refutation): 54 files in this loop cite
   `validate_semantic_pipeline_scope.py`, and **48 of them use the correct
   repo-root absolute path**
   (`…/chirality/tools/validation/validate_semantic_pipeline_scope.py`); the
   remainder cite it by bare filename or relative path. Exactly **one** file
   records a project-local path —
   `PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/_run_records/TASK_RUN_2026-05-24_1510.md`
   — and it is a **truthful `NOT_RUN` record**, listing under `## Missing` that
   that path "was not present". It is not a broken citation and needs no repair.
   An earlier draft of this notice claimed all 54 cited a non-existent
   project-local path; that claim was false and is withdrawn.

## Follow-on for this loop — two items need a ruling

While reconciling the emitted `coverage_summary.json` corpus against the
template, two divergences were found in
`execution/_Evaluation/DecompCoverage/COV_SCA_APP_004_POSTCHANGE_2026-07-23_2027/coverage_summary.json`
and **deliberately left unfixed**, because each could be either a template gap
or a non-conforming emission and the packet declined to decide silently:

1. **`repository_topology`** (an object carrying `packages`, `deliverables`,
   `objectives`, `scope_items`, `ledger_rows`) is emitted but absent from the
   template entirely. The proposal's recommendation is to **adopt** it into the
   template as an optional object.
2. **`"closure_readiness": "READY_FOR_IMPLEMENTATION_HANDOFF"`** is outside the
   template's declared `PASS|WARN|FAIL` enum. The proposal's recommendation is
   to treat this as a **bad emission** — a lifecycle value written into a
   three-way verdict field — and **not** to widen the enum.

No exact-text change was made for either. The owner's ruling is pending. The
snapshot itself is an immutable historical artifact and is not reopened by this
notice; what is open is whether the template should change.

Related: the root cause is that **no tool generates `coverage_summary.json`** —
it is authored free-hand from the prose template, so the template is
simultaneously the specification and the only enforcement. Five emissions across
two loops produced four distinct divergences. A
`tools/validation/validate_coverage_summary.py` is now unblocked (the schema had
to be made correct first, which this tranche did) but is not built.

## Other follow-on

- **P7's new deriver warning fires on five accepted contracts in this loop.**
  Measured in this run by running the patched `derive_review_checklist.py` over
  every `ScopeOfWork.md` in `projects/chirality-app-dev/execution` and counting
  stderr warnings — all five are in
  `PKG-06_Permissioned_Tools_MCP_and_Hooks`, one row each:
  `DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping`,
  `DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation`,
  `DEL-06-03_Initial_Chirality_MCP_Read_Tools`,
  `DEL-06-04_Write_Edit_Surface_and_Path_Hooks`,
  `DEL-06-05_Bash_Governance_and_Timeout_Policy` (5 contracts / 5 rows).

  **No failure and no re-run is implied.** Derived checklist JSON is
  byte-identical to before the warning existed. The warning fires on *shape*
  (a row with multiple `AC-*` and multiple `VER-*`); **new QA item 20 is
  violated only where the row's verification set exceeds the union of those
  criteria's own methods**, so each of these five rows may still conform. Item
  20 asks for a **per-row disposition** — conforming, or split the row — at the
  next occasion this loop touches these contracts.

  **These five sit OUTSIDE the PEC B3 "accepted-as-conservative" disposition.**
  That disposition (`projects/pec/execution/_Coordination/WAVE_D-PEC-63/BATCH_B3_FANIN.md`
  §3.1) is a **PEC-loop instrument** covering PEC contracts only; it carries no
  authority here and is not offered as cover. **The disposition of these five
  rows is chirality-app-dev's own to make**, under its own instruments and
  cadence.
- No corrective act is requested for any accepted chirality-app-dev artifact.
- Future AUDIT_DECOMP runs should write `CheckNumber` as a string in the
  declared set, and will bind decomposition sections by heading text.

Full record: `plans/helps_humans_tooling_consolidation_2026-07-25/APPLIED_2026-07-25.md`.
Proposals: same directory, `P1_*.md` … `P7_*.md`, approved by the owner
2026-07-25.
