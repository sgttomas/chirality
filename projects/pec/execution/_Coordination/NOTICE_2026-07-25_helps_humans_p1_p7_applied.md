# NOTICE — HELPS_HUMANS P1–P7 applied to repo-root contracts and tooling, 2026-07-25

Routed to this surface under `AGENTS.md`'s agent-index change-notice rule,
because this tranche changed files under `agents/`. **This is coordination, not
authority.** The PEC loop adopts, amends, or declines under its own instruments
and cadence. Nothing here rules on any PEC artifact.

**What happened.** The owner approved (2026-07-25, in chat) the seven exact-text
proposals in `plans/helps_humans_tooling_consolidation_2026-07-25/`, which were
the disposition of this loop's routed request
`REQUEST_2026-07-25_helps_humans_tooling_consolidation.md`. All seven are now
applied. Full record with hunks and command output:
`plans/helps_humans_tooling_consolidation_2026-07-25/APPLIED_2026-07-25.md`.
No item was blocked on drift.

## What changed, exactly

| Proposal | Files | Change |
|---|---|---|
| P1 | `skills/scope-of-work/SKILL.md`, `TOOL_POLICY.md`, `BRIEF_SCHEMA.md`, `QA_CHECKS.md` | INIT/CONVERT branches made explicit. SKILL Method steps 4–7 and TOOL_POLICY steps 3–5 now branch by mode; BRIEF_SCHEMA's write boundary now permits the `INIT` production target `{ScopePath}/ScopeOfWork.md`; `STATUS_POLICY`, `DECOMP_VARIANT`, `PHASE` declared as optional brief fields; QA item 3's hard-coded `IN_PROGRESS` replaced with "lifecycle state is unchanged"; QA item 4 reworded to "Working-contract"; a mode-scoping header added |
| P2 | `tools/query/count_workspace_state.sh` | Both counting defects fixed — deliverable count no longer includes `_run_records/` subdirectories, and state counts match only the `**Current State:**` line instead of the whole file including `## History` |
| P3 | `tools/validation/validate_semantic_pipeline_scope.py` (+ tests) | `--step init` added, allowing `ScopeOfWork.md` and `_STATUS.md` (plus the always-allowed `_run_records/`) |
| P4 | `agents/AGENT_AUDIT_DECOMP.md` | IssueLog `CheckNumber` redeclared `string` over `1`–`9`, `9b`, `10`, `11` (not integer `1–11`); `coverage_summary.json` template gained `deliverables_without_objective_mapping` and `in_ledger_rows_without_objective_mapping`; `derivative_package_status` indentation fixed |
| P5 | `agents/AGENT_AUDIT_DECOMP.md`, `agents/AGENT_SCOPE_CHANGE.md` | Variant Section Binding now binds **by heading text, never by section number**, with an explicit normalization + rank-order (exact → prefix → substring) spec. The four wrong SOFTWARE citations (Packages §3, Deliverables §4, Scope Ledger §5, Change Log §8) are gone. Change Register for SOFTWARE now names `Decision Log` **and/or** `Revision History`, read both when both exist |
| P6 | `skills/scope-of-work/SKILL.md`, `QA_CHECKS.md` | Upstream deliverable IDs must be cited inside a `> ` blockquote (marker at column 0–3) with an explicit carve-out sentence; new QA item 19 |
| P7 | `skills/scope-of-work/SKILL.md`, `QA_CHECKS.md`, `tools/scope_of_work/derive_review_checklist.py` (+ tests) | Matrix row semantics stated (a row's VER refs apply to every AC in the row); new QA item 20; the deriver now emits a stderr WARNING for multi-AC/multi-VER rows. **Derived checklist JSON is byte-identical** — QA item 18 and the 10 accepted contracts are unaffected |

Verified after application: `tools/validation/` 273 passed, `tools/scope_of_work/`
20 passed, `validate_skill_metadata.py` 45/45 valid,
`validate_agent_instructions.py` 33 files / 0 errors / 0 warnings.

## Follow-on for the PEC loop

1. **`count_workspace_state.sh` is now correct on this workspace.** Verified
   against `projects/pec/execution`: `Deliverables: 64`, `OPEN 32`,
   `INITIALIZED 32`, all others 0 — matching the loop's own census. The standing
   "never run `count_workspace_state.sh` post-transition" prohibitions recorded
   in D-PEC-63, D-PEC-64, the phase-2.2 wave plan, and the SCA-002
   propagation/impact documents **can now be retired**. That retirement is the
   PEC loop's call under its own instruments; this notice only states that the
   defect they worked around is gone.

   A fifth instance exists and is listed **for completeness, not for repair**:
   `_ScopeChange/SCA-002_2026-07-25_1042/Post_Change_Coverage.json` line 108
   carries `"count_workspace_state.sh deliberately not used (D-PEC-64 §4.4)"`.
   That is an **immutable emitted artifact** recording what the run did at the
   time; it is truthful as written and is not reopened. Only the live standing
   instruments above are candidates for retirement.
2. **The D-PEC-63 wave's INIT contracts are now retroactively conforming**
   rather than brief-excepted: the write target, the mode branches, and the
   `NO_STATUS_TOUCH` status posture are all stated in the skill contract. This
   is a strengthening, and the owner accepted it knowingly. No re-run of any
   accepted contract is required or implied.
3. **SCA-002 ran under the pre-P5 agent tables**, which cited SOFTWARE sections
   by wrong numbers. No corrective act is requested here. Any *future*
   AUDIT_DECOMP or SCOPE_CHANGE run against
   `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` will bind by
   heading text and should resolve correctly.
4. **The `SOFTWARE_DECOMP.md` internal `§` references remain correct — do not
   repair them.** This restates the correction already issued in
   `NOTICE_2026-07-25_helps_humans_oi013_response.md`. Lines 536, 635, and 651
   resolve correctly against their own document's headings; they are the control
   group that proved the agent tables wrong. Editing them to match the old
   tables would introduce the defect P5 removed.
5. **P7's deriver warning now fires on nine accepted PEC contracts — 21 matrix
   rows.** Measured in this run by running the patched
   `derive_review_checklist.py` over every `ScopeOfWork.md` in
   `projects/pec/execution` and counting stderr warnings:

   | Deliverable | Warning rows |
   |---|---|
   | `DEL-00-01_v2_first_ADRs_core_isolation_carried_postures` | 1 |
   | `DEL-00-03_v2_SPEC_seed` | 3 |
   | `DEL-01-01_Record_tier_schema_entity_model` | 2 |
   | `DEL-01-03_Store_bootstrap_content_minimal_guard` | 2 |
   | `DEL-01-04_Self_observability_logging` | 2 |
   | `DEL-01-05_Zero_dependency_locality_enforcement` | 5 |
   | `DEL-01-06_Loop_registry_local_config_default` | 2 |
   | `DEL-08-01_Unix_socket_server_token_scoped_access` | 1 |
   | `DEL-10-03_No_ruling_write_verification` | 3 |
   | **Total** | **21** |

   **The warning is not a failure and implies no re-run.** Derived checklist
   JSON is byte-identical to before the warning existed, so QA item 18 holds and
   no accepted contract is invalidated. The warning fires on *shape*
   (multi-AC × multi-VER); **new QA item 20 is violated only where a row's
   verification set is larger than the union of those criteria's own methods**.
   Each of the 21 rows may still conform. What item 20 asks for is a **per-row
   disposition** at the next occasion this loop touches these contracts —
   conforming, or split the row — not a corpus-wide revision.

   **Count discrepancy, stated rather than resolved:** this measurement finds
   **9** affected contracts; `WAVE_D-PEC-63/BATCH_B3_FANIN.md` §3.1 records "21
   multi-AC/multi-VER rows across **10 of the 12** previously accepted
   contracts". The row count agrees exactly (21); the contract count does not.
   Either the B3 back-scan miscounted contracts, or a row was split in a later
   revision batch (B6/B7 revised several of these contracts). **Neither number
   is adopted here.** The B3 "accepted-as-conservative, no revision ordered"
   disposition stands untouched; reconciling the count is the PEC loop's call.

6. **Future AUDIT_DECOMP `Decomp_Coverage_IssueLog.csv` emissions** should write
   `CheckNumber` as a string over `1`–`9`, `9b`, `10`, `11`. Existing snapshots
   are immutable historical artifacts and are not reopened; the invalid
   `CheckNumber=96` row shipped by SCA-002 is explained by the previously
   under-declared domain. Existing `coverage_summary.json` files from the two
   `pec` SCA-002 runs become **conforming** rather than undeclared, because the
   two additive fields they emitted are now in the template.

## The evidence-waiver convention — reported blessing, ruling still pending

The dispatching session reports the owner blessed the evidence-waiver
convention in chat on 2026-07-25 (the carry-forward directive). The durable
decision artifact is **D-PEC-65 §1**
(`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md`,
DRAFT v2, awaiting owner ruling); the blessing becomes fully artifact-backed at
that ruling. **The flag raised in
`NOTICE_2026-07-25_helps_humans_oi013_response.md` remains formally open until
then.**

The mechanism itself is unchanged by this tranche: sidecar
`Dependencies_EvidenceWaivers.csv`, `EVQ-003`/`EVQ-004` waivable, **`EVQ-001`
never waivable**, waivers themselves checked for staleness, thin rationale, and
malformation. **The validator, its tests, and its registry row were not
modified.**

Read against that pending ruling, the OI-013 closure gate is: **zero
`EVQ-001`**, and every `EVQ-003`/`EVQ-004` row either given a real locus and
quote **or** covered by a declared waiver with an attributed, substantive
rationale — so that "re-run to exit 0" is not read as an instruction to invent
a quote.

The repair of the 120 EXECUTION rows remains a PEC-loop act requiring its own
owner-ruled packet. Nothing in this tranche performs or authorizes it.

## Not applied — awaiting owner rulings that may matter to this loop

- **P4 §3** — two further `coverage_summary.json` drifts, both in the
  `chirality-app-dev` emission, are unruled: whether `repository_topology`
  becomes an optional template object, and whether
  `"closure_readiness": "READY_FOR_IMPLEMENTATION_HANDOFF"` is a bad emission
  (recommended) or an enum widening. A `validate_coverage_summary.py` is now
  unblocked but not built.
- **P6 Option 2** — the `DEL-NN-NN/REQ-NNN` qualified-ID form **is still not
  safe** and is not blessed. `common.py` still harvests it as a bare local
  reference, which fails validation. Blockquote citation (Option 1, now in the
  contract) is the only supported route.
- **P7 §3d** — the silent matrix row-drop warning is not applied; a malformed
  matrix row still produces a misleading downstream "AC has no links entry"
  error rather than an accurate upstream one.
- **P3's strict `init` guard** (fail closed when a production contract already
  exists) is deferred pending a test.
- **P1's TOOL_POLICY steps 6–8** still use CONVERT vocabulary ("clean production
  candidate") for what is, under INIT, simply the production contract. The
  proposal offered no exact replacement text, so none was invented.

**Write containment of the issuing run:** repo-root contract/tool files named
above, the application record, and this notice plus its two siblings. No
`_STATUS.md` anywhere, nothing under `projects/pec/execution/PKG-*`, no Git
operation.
