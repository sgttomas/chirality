# Pre/Post Comparison — COV_SCA005_POSTCHANGE_2026-09-25_1344 → COV_SCA005_POSTSETUP_2026-09-25_1606

This is the formal comparison mode of method Step 12. The prior
`coverage_summary.json` hashes to
`912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb`, verified.
It equals `SCA-005_2026-09-23_2139/Post_Change_Coverage.json`.

## Basis

| | POSTCHANGE (prior) | POSTSETUP (this run) |
|---|---|---|
| Decomposition | revision 1.5 `candidate_pending_checkpoint_3` `37ea1084…a6cc` | revision 1.5 `current_basis` `dc2b8479…9660` (front-matter lines 5 and 8 changed by A6; body identical) |
| Registers | ScopeLedger `83152a94…fd9df`, Deliverables `b8628fc4…3d65a`, ContextBudgetQA `2a194105…eb0df`, Companion_Inventory `7c8a24a8…6ef8` | unchanged |
| PRD | v2.3 `fff27a66…fdc32` | unchanged |
| Pointers | revision 1.4 / SCA-004 (A6 pending acceptance) | revision 1.5 / SCA-005 (A6 done at checkpoint-3 acceptance) |
| SCA-005 snapshot | candidate, mid-A5 | active, complete, `CLOSED_FOR_SCOPE_CHANGE_ONLY` |
| Deliverable tree | Lane A1–A3 applied; A4 deferred; B3 not opened | + D-PEC-93 option A: 31 product paths (A4 folders; B3 retirements, new edges, mirrors) |
| Git basis | `5d2770350` | `995af4f36` |

The only deliverable-tree difference between the two audited commits is the
31 D-PEC-93 product paths (`git diff --name-status 5d2770350 HEAD`).

## Topology

| Metric | POSTCHANGE | POSTSETUP | Delta |
|---|---|---|---|
| Packages | 11 | 11 | 0 |
| Deliverable rows | 66 (62 active / 4 retired) | 66 (62 / 4) | 0 |
| Deliverable folders | 64 | 66 | +2 (DEL-02-08, DEL-02-09) |
| Objectives | 6 | 6 | 0 |
| Scope items / ledger rows | 96 (70 / 18 / 8) | 96 (70 / 18 / 8) | 0 |
| Per-package IN (PKG-00..10) | 3/8/9/7/6/3/6/3/6/7/12 | same | 0 |
| Active envelopes S/M/L/XL | 28/32/2/0 | 28/32/2/0 | 0 |
| Register validator (strict) | 64 registers / 255 rows / 0 errors / 2 DRB-008 warnings (exit 1) | 66 / 263 / 0 / 0 (exit 0) | +2 registers, +8 rows; DRB-008 ×2 cleared |
| Dependency rows ANCHOR / EXECUTION | 136 / 119 (all ACTIVE) | 140 / 123 (ACTIVE 132 / 111; RETIRED 8 / 12) | +4 / +4 rows; 20 retired, 0 deleted |
| Dependency closure | 119 edges / 64 nodes / 0 SCC / 0 bidirectional / isolated DEL-00-03, DEL-01-05 / hub DEL-03-01 (24) | 111 / 66 / 0 / 0 / isolated DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05 / hub DEL-03-01 (25) | −8 edges, +2 nodes, +4 isolated |
| ACTIVE rows to retired DELs / in retired registers | 1 (`DEP-09-05-005`) / 18 | 0 / 0 | cleared |

## Coverage percentages

| Metric | POSTCHANGE | POSTSETUP |
|---|---|---|
| forward_coverage_partitions_pct | 100.0 | 100.0 |
| forward_coverage_production_units_pct | 96.9697 (64/66) | 100.0 (66/66) |
| reverse_coverage_pct | 100.0 | 100.0 |
| context_fidelity_pct | 100.0 (64/64) | 100.0 (66/66) |
| artifact_presence_pct | 4.5455 (3/66) | 4.5455 (3/66) |
| objective_coverage_pct | 100.0 | 100.0 |
| deliverables_without_objective_mapping | 4 (retired, by design) | 4 (retired, by design) |
| in_ledger_rows_without_objective_mapping | 0 | 0 |
| Objective supporters folder-backed (OBJ-001..006) | 23/12/14/11/7/9 of 25/14/14/11/7/9 | 25/14/14/11/7/9 of 25/14/14/11/7/9 |
| Context provenance revision | 22 at 1.5 / 42 at 1.4 | 24 at 1.5 / 42 at 1.4 |
| `_REFERENCES.md` revision | 64 at 1.4 | 64 at 1.4 / 2 at 1.5 |
| package_shape_conformance | PASS | PASS |
| active_snapshot_status | PASS (SCA-004 active) | PASS (SCA-005 active) |
| handoff_state_status | WARN (count defect) | PASS |
| objective_evidence_integrity | PASS | PASS |

## Lifecycle and contract distribution

| State | POSTCHANGE | POSTSETUP |
|---|---|---|
| INITIALIZED | 26 | 26 |
| OPEN | 28 | 30 (+ DEL-02-08, DEL-02-09) |
| CHECKING | 4 | 4 |
| IN_PROGRESS | 2 | 2 |
| RETIRED | 4 | 4 |
| Contracts SOW_V1 / NONE / ambiguous | 32 / 32 / 0 | 32 / 34 / 0 |

## Issue counts

| | POSTCHANGE | POSTSETUP |
|---|---|---|
| BLOCKER | 2 (both EXPECTED_CONSEQUENCE, Check 2) | 0 |
| WARNING | 6 (3 PRE-EXISTING Check 6; 2 EXPECTED_CONSEQUENCE Check 8; 1 DEFECT Check 10) | 3 (PRE-EXISTING Check 6) |
| INFO | 74 | 70 (59 PRE-EXISTING; 11 EXPECTED_CONSEQUENCE) |
| overall_status / closure_readiness | BLOCKERS / FAIL | WARNINGS / WARN |

Per-check INFO: Check 6 58 → 60; Check 7 6 → 4; Check 10 10 → 6.

## Regressions, improvements, methodology

- **Regressions (new BLOCKER or WARNING).** None.
- **Improvements.** 14 prior findings resolved: both Check-2 blockers and
  both Check-8 warnings (the A4 folders), the two folderless-objective INFO
  rows, the three pre-B3 INFO rows (B3), the count defect (recorded
  correction), and four pointer and snapshot INFO rows (checkpoint-3
  acceptance and A6, which occurred between the two runs).
- **New findings (all INFO).** COV-015 and COV-016 (new `OPEN` folders
  without artifacts); COV-071 (closure-tool isolated units, planned);
  COV-072 (evidence-quote currency; condition present at the prior state,
  first measured here, not caused by D-PEC-93); COV-073 (SCA-005 snapshot and
  pointers still describe the pre-act state).
- **Methodology changes.**
  - Evidence-quote currency is newly measured (D-11, D-12). The prior run
    did not test it, so COV-072 is new as a finding but `PRE-EXISTING` as a
    condition.
  - A supplementary `_DEPENDENCIES.md` EdgeID mirror check was added. The
    prior run listed the retired folders' mirrors as not audited.
  - Otherwise the method, section binding, folder-local artifact rule,
    Check-8 folder reading and lifecycle reading are unchanged.

## Per-finding delta

The counts are 67 carried, 1 changed, 14 resolved and 5 new, which accounts
for all 82 POSTCHANGE and all 73 POSTSETUP findings. POSTCHANGE IDs are its
own `COV-nnn`, and POSTSETUP IDs are this snapshot's. From DEL-03-01 onward
the Check-6 IDs coincide; before it they shift by 2. Every mapped pair has the
same check, severity and entity (checked by `mapcheck.py`).

| Prior | Prior sev | Check | Entity | New | New sev | Delta |
|---|---|---|---|---|---|---|
| COV-001 | BLOCKER | 2 | DEL-02-08 | - | - | RESOLVED: folder PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ created by D-PEC-93 (A4) |
| COV-002 | BLOCKER | 2 | DEL-02-09 | - | - | RESOLVED: folder PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ created by D-PEC-93 (A4) |
| COV-003 | INFO | 6 | DEL-00-02 | COV-001 | INFO | CARRIED |
| COV-004 | INFO | 6 | DEL-01-01 | COV-002 | INFO | CARRIED |
| COV-005 | INFO | 6 | DEL-01-02 | COV-003 | INFO | CARRIED |
| COV-006 | WARNING | 6 | DEL-01-03 | COV-004 | WARNING | CARRIED |
| COV-007 | INFO | 6 | DEL-01-04 | COV-005 | INFO | CARRIED |
| COV-008 | WARNING | 6 | DEL-01-05 | COV-006 | WARNING | CARRIED |
| COV-009 | INFO | 6 | DEL-01-06 | COV-007 | INFO | CARRIED |
| COV-010 | INFO | 6 | DEL-02-01 | COV-008 | INFO | CARRIED |
| COV-011 | INFO | 6 | DEL-02-02 | COV-009 | INFO | CARRIED |
| COV-012 | INFO | 6 | DEL-02-03 | COV-010 | INFO | CARRIED |
| COV-013 | INFO | 6 | DEL-02-04 | COV-011 | INFO | CARRIED |
| COV-014 | INFO | 6 | DEL-02-05 | COV-012 | INFO | CARRIED |
| COV-015 | INFO | 6 | DEL-02-06 | COV-013 | INFO | CARRIED |
| COV-016 | INFO | 6 | DEL-02-07 | COV-014 | INFO | CARRIED |
| COV-017 | INFO | 6 | DEL-03-01 | COV-017 | INFO | CARRIED |
| COV-018 | INFO | 6 | DEL-03-02 | COV-018 | INFO | CARRIED |
| COV-019 | INFO | 6 | DEL-03-03 | COV-019 | INFO | CARRIED |
| COV-020 | INFO | 6 | DEL-03-04 | COV-020 | INFO | CARRIED |
| COV-021 | INFO | 6 | DEL-03-05 | COV-021 | INFO | CARRIED |
| COV-022 | INFO | 6 | DEL-03-06 | COV-022 | INFO | CARRIED |
| COV-023 | INFO | 6 | DEL-04-01 | COV-023 | INFO | CARRIED |
| COV-024 | INFO | 6 | DEL-04-02 | COV-024 | INFO | CARRIED |
| COV-025 | INFO | 6 | DEL-04-03 | COV-025 | INFO | CARRIED |
| COV-026 | INFO | 6 | DEL-04-04 | COV-026 | INFO | CARRIED |
| COV-027 | INFO | 6 | DEL-04-05 | COV-027 | INFO | CARRIED |
| COV-028 | INFO | 6 | DEL-05-01 | COV-028 | INFO | CARRIED |
| COV-029 | INFO | 6 | DEL-05-02 | COV-029 | INFO | CARRIED |
| COV-030 | INFO | 6 | DEL-06-01 | COV-030 | INFO | CARRIED |
| COV-031 | INFO | 6 | DEL-06-02 | COV-031 | INFO | CARRIED |
| COV-032 | INFO | 6 | DEL-06-03 | COV-032 | INFO | CARRIED |
| COV-033 | INFO | 6 | DEL-06-04 | COV-033 | INFO | CARRIED |
| COV-034 | INFO | 6 | DEL-06-05 | COV-034 | INFO | CARRIED |
| COV-035 | INFO | 6 | DEL-06-06 | COV-035 | INFO | CARRIED |
| COV-036 | INFO | 6 | DEL-07-01 | COV-036 | INFO | CARRIED |
| COV-037 | INFO | 6 | DEL-07-02 | COV-037 | INFO | CARRIED |
| COV-038 | INFO | 6 | DEL-07-03 | COV-038 | INFO | CARRIED |
| COV-039 | INFO | 6 | DEL-07-04 | COV-039 | INFO | CARRIED |
| COV-040 | INFO | 6 | DEL-07-05 | COV-040 | INFO | CARRIED |
| COV-041 | INFO | 6 | DEL-08-01 | COV-041 | INFO | CARRIED |
| COV-042 | WARNING | 6 | DEL-08-02 | COV-042 | WARNING | CARRIED |
| COV-043 | INFO | 6 | DEL-08-03 | COV-043 | INFO | CARRIED |
| COV-044 | INFO | 6 | DEL-08-04 | COV-044 | INFO | CARRIED |
| COV-045 | INFO | 6 | DEL-08-05 | COV-045 | INFO | CARRIED |
| COV-046 | INFO | 6 | DEL-09-01 | COV-046 | INFO | CARRIED |
| COV-047 | INFO | 6 | DEL-09-02 | COV-047 | INFO | CARRIED |
| COV-048 | INFO | 6 | DEL-09-03 | COV-048 | INFO | CARRIED |
| COV-049 | INFO | 6 | DEL-09-04 | COV-049 | INFO | CARRIED |
| COV-050 | INFO | 6 | DEL-09-05 | COV-050 | INFO | CARRIED |
| COV-051 | INFO | 6 | DEL-09-06 | COV-051 | INFO | CARRIED |
| COV-052 | INFO | 6 | DEL-09-07 | COV-052 | INFO | CARRIED |
| COV-053 | INFO | 6 | DEL-10-02 | COV-053 | INFO | CARRIED |
| COV-054 | INFO | 6 | DEL-10-03 | COV-054 | INFO | CARRIED |
| COV-055 | INFO | 6 | DEL-10-04 | COV-055 | INFO | CARRIED |
| COV-056 | INFO | 6 | DEL-10-05 | COV-056 | INFO | CARRIED |
| COV-057 | INFO | 6 | DEL-10-06 | COV-057 | INFO | CARRIED |
| COV-058 | INFO | 6 | DEL-10-07 | COV-058 | INFO | CARRIED |
| COV-059 | INFO | 6 | DEL-10-08 | COV-059 | INFO | CARRIED |
| COV-060 | INFO | 6 | DEL-10-09 | COV-060 | INFO | CARRIED |
| COV-061 | INFO | 6 | DEL-10-10 | COV-061 | INFO | CARRIED |
| COV-062 | INFO | 6 | DEL-10-11 | COV-062 | INFO | CARRIED |
| COV-063 | INFO | 6 | DEL-10-12 | COV-063 | INFO | CARRIED |
| COV-064 | INFO | 7 | DEL-06-04 | COV-064 | INFO | CARRIED |
| COV-065 | INFO | 7 | DEL-07-02 | COV-065 | INFO | CARRIED |
| COV-066 | INFO | 7 | DEL-07-04 | COV-066 | INFO | CARRIED |
| COV-067 | INFO | 7 | DEL-07-05 | COV-067 | INFO | CARRIED |
| COV-068 | INFO | 7 | OBJ-001 | - | - | RESOLVED: OBJ-001's 25 supporters all folder-backed |
| COV-069 | INFO | 7 | OBJ-002 | - | - | RESOLVED: OBJ-002's 14 supporters all folder-backed |
| COV-070 | WARNING | 8 | SOW-095 | - | - | RESOLVED: SOW-095 resolves to the DEL-02-08 folder |
| COV-071 | WARNING | 8 | SOW-096 | - | - | RESOLVED: SOW-096 resolves to the DEL-02-09 folder |
| COV-072 | WARNING | 10 | SCA-005 | - | - | RESOLVED: every current handoff surface carries 42; SCA-005 RUN_SUMMARY.md records the evidence correction (D-13) |
| COV-073 | INFO | 10 | SCA-004 | - | - | RESOLVED: A6 at checkpoint-3 acceptance; pointers name revision 1.5 / SCA-005; decomposition equals dc2b8479…9660 |
| COV-074 | INFO | 10 | SCA-004 | - | - | RESOLVED: SCA-004 no longer active; the SCA-004-era stale pointer fields are gone and _Decomposition/_LATEST.md cites the 2026-08-09 repair closeout |
| COV-075 | INFO | 10 | SCA-005 | - | - | RESOLVED: SCA-005 snapshot complete (A5); it is now the active snapshot |
| COV-076 | INFO | 10 | DEL-* (22 A2 mirrors) | - | - | RESOLVED: the 1.5 current_basis claim became true at checkpoint-3 acceptance |
| COV-077 | INFO | 10 | DEL-* (42 not in A2) | COV-068 | INFO | CARRIED |
| COV-078 | INFO | 10 | DEL-* (64) | COV-069 | INFO | CHANGED: 64 -> 64 of 66 (2 new packets at revision 1.5) |
| COV-079 | INFO | 10 | DEL-09-05 | - | - | RESOLVED: DEP-09-05-005 Status=RETIRED (B3) |
| COV-080 | INFO | 10 | DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | - | - | RESOLVED: 0 ACTIVE rows remain in the four retired registers (B3) |
| COV-081 | INFO | 10 | DEL-02-08; DEL-02-09 | - | - | RESOLVED: strict validator 0 errors / 0 warnings, exit 0 |
| COV-082 | INFO | 10 | 32 SOW_V1 contracts | COV-070 | INFO | CARRIED |
| - | - | 6 | DEL-02-08 | COV-015 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 6 | DEL-02-09 | COV-016 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | DEL-00-03; DEL-01-05; DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | COV-071 | INFO | NEW (EXPECTED_CONSEQUENCE) |
| - | - | 10 | 19 ACTIVE EXECUTION rows (10 registers) | COV-072 | INFO | NEW (PRE-EXISTING) |
| - | - | 10 | SCA-005 | COV-073 | INFO | NEW (EXPECTED_CONSEQUENCE) |
