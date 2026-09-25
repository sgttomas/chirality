# Pre/Post Comparison — COV_SCA005_PRECHANGE_2026-09-23_2139 → COV_SCA005_POSTCHANGE_2026-09-25_1344

This is the formal comparison mode of method Step 12. The prior
`coverage_summary.json` hashes to
`61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f`, verified.
It equals `SCA-005_2026-09-23_2139/Pre_Change_Coverage.json`.

## Basis

| | PRECHANGE | POSTCHANGE |
|---|---|---|
| Decomposition | revision 1.4 `current_basis` `7cca5cdb…5c81` | revision 1.5 `candidate_pending_checkpoint_3` `37ea1084…a6cc` |
| ScopeLedger / Deliverables | `2103afa2…9e25` / `49f90448…6b72` | `83152a94…fd9df` / `b8628fc4…3d65a` |
| ContextBudgetQA / Companion_Inventory | `5c8d3099…2bef` / `18793e15…ec23` | `2a194105…eb0df` / `7c8a24a8…6ef8` |
| PRD | v2.2 | v2.3 `fff27a66…fdc32` |
| Pointers | revision 1.4 / SCA-004 | unchanged (revision 1.4 / SCA-004; A6 deferred to acceptance) |
| Git basis | `d61981ee2` | `5d2770350` (A1–A3 application) |

## Topology

| Metric | PRECHANGE | POSTCHANGE | Delta |
|---|---|---|---|
| Packages | 11 | 11 | 0 |
| Deliverable rows | 64 | 66 (62 active / 4 RETIRED) | +2 rows (DEL-02-08, DEL-02-09); 4 retired in place |
| Deliverable folders | 64 | 64 | 0 (A4 deferred; retired folders retained) |
| Objectives | 6 | 6 | 0 |
| Scope items / ledger rows | 94 | 96 | +2 (SOW-095, SOW-096) |
| Ledger IN / OUT / TBD | 72 / 14 / 8 | 70 / 18 / 8 | IN −2, OUT +4 (+SOW-095/096 IN; SOW-029/035/037/087 IN → OUT deferred) |
| Per-package IN (PKG-00..10) | 3/8/7/7/6/3/7/6/6/7/12 | 3/8/9/7/6/3/6/3/6/7/12 | PKG-02 +2; PKG-06 −1; PKG-07 −3 |
| Active envelopes S/M/L/XL | 28/34/2/0 (all 64 rows active) | 28/32/2/0 (active; all 66 rows 29/35/2/0) | S +1 (DEL-02-09) −1 (DEL-06-04 retired) = 0; M +1 (DEL-02-08) −3 (DEL-07-02/04/05 retired) = −2; no existing row changed envelope |
| Open / resolved issues | 10 / 3 | 10 / 3 | 0 |
| Vocabulary terms | — | 26 | not measured in PRECHANGE |
| Register validator (strict) | 64 registers / 255 rows / 64 declared / 0 errors / 0 warnings (exit 0) | 64 / 255 / 66 declared / 0 errors / 2 DRB-008 warnings (exit 1) | +2 DRB-008 (A4 deferral) |
| Dependency closure | 119 edges / 64 nodes / 0 SCC / isolated DEL-00-03, DEL-01-05 (WORKING_ITEMS run, SCA-005 Handoff_State step 22) | 119 / 64 / 0 SCC / 0 bidirectional pairs / same isolated / hub DEL-03-01 | 0 (B3 not opened) |

PRECHANGE per-package IN counts and envelopes were recomputed from the revision-1.4
registers at `2b0572fe0` (`ScopeLedger.csv` `2103afa2…9e25`, `Deliverables.csv`
`49f90448…6b72`; both equal the PRECHANGE-audited hashes). No deliverable
present in both revisions changed its `ContextEnvelope`.

## Coverage percentages

| Metric | PRECHANGE | POSTCHANGE |
|---|---|---|
| forward_coverage_partitions_pct | 100.0 | 100.0 |
| forward_coverage_production_units_pct | 100.0 | 96.9697 (64/66) |
| reverse_coverage_pct | 100.0 | 100.0 |
| context_fidelity_pct | 100.0 (64/64) | 100.0 (64/64 matched folders) |
| artifact_presence_pct | 4.6875 (3/64) | 4.5455 (3/66 declared); 4.6875 on the folder-matched basis |
| objective_coverage_pct | 100.0 | 100.0 |
| deliverables_without_objective_mapping | 9 | 4, all retired by design (active: 0) |
| in_ledger_rows_without_objective_mapping | 11 | 0 |
| Objective IN items (OBJ-001..006) | 22/12/13/11/9/9 | 27/14/16/13/9/9 |
| Objective supporting deliverables | 20/12/12/10/7/9 | 25/14/14/11/7/9 |
| Context provenance revision | 64 at 1.4 | 22 at 1.5 (A2) / 42 at 1.4 |
| `_REFERENCES.md` revision | 64 at 1.4 | 64 at 1.4 |
| package_shape_conformance | PASS | PASS |
| active_snapshot_status | PASS | PASS |
| handoff_state_status | PASS | WARN (COV-072 count defect) |
| objective_evidence_integrity | PASS | PASS |

## Lifecycle and contract distribution

| State | PRECHANGE | POSTCHANGE |
|---|---|---|
| INITIALIZED | 26 | 26 |
| OPEN | 32 | 28 |
| CHECKING | 4 | 4 |
| IN_PROGRESS | 2 | 2 |
| RETIRED | 0 | 4 (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05; A3) |
| Contracts SOW_V1 / NONE / ambiguous | 32 / 32 / 0 | 32 / 32 / 0 (NONE = 28 OPEN + 4 RETIRED) |

## Issue counts

| | PRECHANGE | POSTCHANGE |
|---|---|---|
| BLOCKER | 0 | 2 (both EXPECTED_CONSEQUENCE, Check 2) |
| WARNING | 3 | 6 (3 PRE-EXISTING Check 6; 2 EXPECTED_CONSEQUENCE Check 8; 1 DEFECT Check 10) |
| INFO | 69 | 74 (59 PRE-EXISTING; 15 EXPECTED_CONSEQUENCE) |
| overall_status / closure_readiness | WARNINGS / WARN | BLOCKERS / FAIL (WARN excluding expected consequences) |

Per-check INFO: Check 6 58 → 58; Check 7 9 → 6; Check 10 2 → 10.

## Regressions, improvements, methodology

- **Regressions (new BLOCKER/WARNING).**
  - COV-001 and COV-002 (Check 2 BLOCKER) and COV-070 and COV-071 (Check 8
    WARNING) all stem only from the owner-deferred A4 folders.
    `EXPECTED_CONSEQUENCE` under the group-2 DECISION.md.
  - COV-072 (Check 10 WARNING) is a `DEFECT`: the accepted plan's and the
    brief's "40" stale-context count should be 42.
- **Improvements.**
  - Six PRECHANGE Check-7 INFO findings are resolved by the owner's
    TM-PEC-023 selections: COV-062, 063, 064, 066, 069 and 070.
  - The IN-row objective residue fell from 11 to 0.
  - Three unmapped-residue INFO findings became retired-row by-design INFO:
    COV-065, 067 and 068 became POST COV-065, 066 and 067.
- **Methodology changes.**
  - Check 8 is read as folder-backed (D-6). PRECHANGE had no folderless
    declared unit, so this changes no PRECHANGE result.
  - `artifact_presence_pct` now uses the declared denominator, with the
    folder basis stated alongside (D-15).
  - Derivative-currency observations are logged as Check-10
    `DERIVATIVE_SURFACE` INFO (D-10). PRECHANGE put provenance in narrative
    only.
  - Otherwise the method, the section binding, the folder-local artifact rule
    and the lifecycle reading are unchanged from PRECHANGE.

## Per-finding delta

The counts are 62 carried, 6 resolved, 4 changed and 16 new, which accounts
for all 72 PRECHANGE and all 82 POSTCHANGE findings. PRECHANGE IDs are its own
`COV-nnn`, and POSTCHANGE IDs are this snapshot's. Check-6 rows marked
`CARRIED` are the same absent anticipated set on the same deliverable. The
four retired deliverables' rows are marked "reason changed".

| Prior | Prior sev | Check | Entity | Post | Post sev | Delta |
| COV-001 | INFO | 6 | DEL-00-02 | COV-003 | INFO | CARRIED |
| COV-002 | INFO | 6 | DEL-01-01 | COV-004 | INFO | CARRIED |
| COV-003 | INFO | 6 | DEL-01-02 | COV-005 | INFO | CARRIED |
| COV-004 | WARNING | 6 | DEL-01-03 | COV-006 | WARNING | CARRIED |
| COV-005 | INFO | 6 | DEL-01-04 | COV-007 | INFO | CARRIED |
| COV-006 | WARNING | 6 | DEL-01-05 | COV-008 | WARNING | CARRIED |
| COV-007 | INFO | 6 | DEL-01-06 | COV-009 | INFO | CARRIED |
| COV-008 | INFO | 6 | DEL-02-01 | COV-010 | INFO | CARRIED |
| COV-009 | INFO | 6 | DEL-02-02 | COV-011 | INFO | CARRIED |
| COV-010 | INFO | 6 | DEL-02-03 | COV-012 | INFO | CARRIED |
| COV-011 | INFO | 6 | DEL-02-04 | COV-013 | INFO | CARRIED |
| COV-012 | INFO | 6 | DEL-02-05 | COV-014 | INFO | CARRIED |
| COV-013 | INFO | 6 | DEL-02-06 | COV-015 | INFO | CARRIED |
| COV-014 | INFO | 6 | DEL-02-07 | COV-016 | INFO | CARRIED |
| COV-015 | INFO | 6 | DEL-03-01 | COV-017 | INFO | CARRIED |
| COV-016 | INFO | 6 | DEL-03-02 | COV-018 | INFO | CARRIED |
| COV-017 | INFO | 6 | DEL-03-03 | COV-019 | INFO | CARRIED |
| COV-018 | INFO | 6 | DEL-03-04 | COV-020 | INFO | CARRIED |
| COV-019 | INFO | 6 | DEL-03-05 | COV-021 | INFO | CARRIED |
| COV-020 | INFO | 6 | DEL-03-06 | COV-022 | INFO | CARRIED |
| COV-021 | INFO | 6 | DEL-04-01 | COV-023 | INFO | CARRIED |
| COV-022 | INFO | 6 | DEL-04-02 | COV-024 | INFO | CARRIED |
| COV-023 | INFO | 6 | DEL-04-03 | COV-025 | INFO | CARRIED |
| COV-024 | INFO | 6 | DEL-04-04 | COV-026 | INFO | CARRIED |
| COV-025 | INFO | 6 | DEL-04-05 | COV-027 | INFO | CARRIED |
| COV-026 | INFO | 6 | DEL-05-01 | COV-028 | INFO | CARRIED |
| COV-027 | INFO | 6 | DEL-05-02 | COV-029 | INFO | CARRIED |
| COV-028 | INFO | 6 | DEL-06-01 | COV-030 | INFO | CARRIED |
| COV-029 | INFO | 6 | DEL-06-02 | COV-031 | INFO | CARRIED |
| COV-030 | INFO | 6 | DEL-06-03 | COV-032 | INFO | CARRIED |
| COV-031 | INFO | 6 | DEL-06-04 | COV-033 | INFO | CARRIED (retired; reason changed) |
| COV-032 | INFO | 6 | DEL-06-05 | COV-034 | INFO | CARRIED |
| COV-033 | INFO | 6 | DEL-06-06 | COV-035 | INFO | CARRIED |
| COV-034 | INFO | 6 | DEL-07-01 | COV-036 | INFO | CARRIED |
| COV-035 | INFO | 6 | DEL-07-02 | COV-037 | INFO | CARRIED (retired; reason changed) |
| COV-036 | INFO | 6 | DEL-07-03 | COV-038 | INFO | CARRIED |
| COV-037 | INFO | 6 | DEL-07-04 | COV-039 | INFO | CARRIED (retired; reason changed) |
| COV-038 | INFO | 6 | DEL-07-05 | COV-040 | INFO | CARRIED (retired; reason changed) |
| COV-039 | INFO | 6 | DEL-08-01 | COV-041 | INFO | CARRIED |
| COV-040 | WARNING | 6 | DEL-08-02 | COV-042 | WARNING | CARRIED |
| COV-041 | INFO | 6 | DEL-08-03 | COV-043 | INFO | CARRIED |
| COV-042 | INFO | 6 | DEL-08-04 | COV-044 | INFO | CARRIED |
| COV-043 | INFO | 6 | DEL-08-05 | COV-045 | INFO | CARRIED |
| COV-044 | INFO | 6 | DEL-09-01 | COV-046 | INFO | CARRIED |
| COV-045 | INFO | 6 | DEL-09-02 | COV-047 | INFO | CARRIED |
| COV-046 | INFO | 6 | DEL-09-03 | COV-048 | INFO | CARRIED |
| COV-047 | INFO | 6 | DEL-09-04 | COV-049 | INFO | CARRIED |
| COV-048 | INFO | 6 | DEL-09-05 | COV-050 | INFO | CARRIED |
| COV-049 | INFO | 6 | DEL-09-06 | COV-051 | INFO | CARRIED |
| COV-050 | INFO | 6 | DEL-09-07 | COV-052 | INFO | CARRIED |
| COV-051 | INFO | 6 | DEL-10-02 | COV-053 | INFO | CARRIED |
| COV-052 | INFO | 6 | DEL-10-03 | COV-054 | INFO | CARRIED |
| COV-053 | INFO | 6 | DEL-10-04 | COV-055 | INFO | CARRIED |
| COV-054 | INFO | 6 | DEL-10-05 | COV-056 | INFO | CARRIED |
| COV-055 | INFO | 6 | DEL-10-06 | COV-057 | INFO | CARRIED |
| COV-056 | INFO | 6 | DEL-10-07 | COV-058 | INFO | CARRIED |
| COV-057 | INFO | 6 | DEL-10-08 | COV-059 | INFO | CARRIED |
| COV-058 | INFO | 6 | DEL-10-09 | COV-060 | INFO | CARRIED |
| COV-059 | INFO | 6 | DEL-10-10 | COV-061 | INFO | CARRIED |
| COV-060 | INFO | 6 | DEL-10-11 | COV-062 | INFO | CARRIED |
| COV-061 | INFO | 6 | DEL-10-12 | COV-063 | INFO | CARRIED |
| COV-062 | INFO | 7 | DEL-00-02 | - | - | RESOLVED: SupportsObjectives now OBJ-003 (amendment 1, TM-PEC-023) |
| COV-063 | INFO | 7 | DEL-03-05 | - | - | RESOLVED: SupportsObjectives now OBJ-001 (TM-PEC-023) |
| COV-064 | INFO | 7 | DEL-05-01 | - | - | RESOLVED: SupportsObjectives now OBJ-004 (TM-PEC-023) |
| COV-065 | INFO | 7 | DEL-07-02 | COV-065 | INFO | CHANGED: unmapped residue -> retired-row by-design INFO |
| COV-066 | INFO | 7 | DEL-07-03 | - | - | RESOLVED: SupportsObjectives now OBJ-003 (TM-PEC-023) |
| COV-067 | INFO | 7 | DEL-07-04 | COV-066 | INFO | CHANGED: unmapped residue -> retired-row by-design INFO |
| COV-068 | INFO | 7 | DEL-07-05 | COV-067 | INFO | CHANGED: unmapped residue -> retired-row by-design INFO |
| COV-069 | INFO | 7 | DEL-08-05 | - | - | RESOLVED: SupportsObjectives now OBJ-001;OBJ-003 (TM-PEC-023) |
| COV-070 | INFO | 7 | DEL-10-08 | - | - | RESOLVED: SupportsObjectives now OBJ-001 (TM-PEC-023 row 9) |
| COV-071 | INFO | 10 | SCA-004 | COV-074 | INFO | CARRIED |
| COV-072 | INFO | 10 | SCA-005 | COV-075 | INFO | CHANGED: empty candidate folder -> A5 mid-completion |
| - | - | 2 | DEL-02-08 | COV-001 | BLOCKER | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 2 | DEL-02-09 | COV-002 | BLOCKER | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 7 | DEL-06-04 | COV-064 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 7 | OBJ-001 | COV-068 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 7 | OBJ-002 | COV-069 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 8 | SOW-095 | COV-070 | WARNING | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 8 | SOW-096 | COV-071 | WARNING | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | SCA-005 | COV-072 | WARNING | NEW (DEFECT) |
| - | - | 10 | SCA-004 | COV-073 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-* (22 A2 mirrors) | COV-076 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-* (42 not in A2) | COV-077 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-* (64) | COV-078 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-09-05 | COV-079 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | COV-080 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-02-08; DEL-02-09 | COV-081 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | 32 SOW_V1 contracts | COV-082 | INFO | NEW (EXPECTED_CONSEQUENCE) |
