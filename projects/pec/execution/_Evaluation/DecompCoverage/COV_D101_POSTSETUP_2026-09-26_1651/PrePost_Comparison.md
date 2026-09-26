# Pre/Post Comparison — COV_SCA006_POSTCHANGE_2026-09-26_0051 → COV_D101_POSTSETUP_2026-09-26_1651

Prior run: `COV_SCA006_POSTCHANGE_2026-09-26_0051` (`coverage_summary.json`
`b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0`, issue log
`37f4f6dc730cebfec173ca965c5afe00b5c506afbec5cb67f4f1e498087026d3`). It audited
revision 1.6 before acceptance at commit `5e0169f5e`. This run audits revision
1.6 `current_basis` plus the D-PEC-101 poststate at `43b60687b`.

## What changed between the two audited trees

Changes to audited product paths between `5e0169f5e` and the audited HEAD,
by source. The accepted scope-change and pointer records are listed
separately.

| Source | Product effect observed |
|---|---|
| SCA-006 checkpoint 3 (A1, A5, A6) | Decomposition front matter set to `current_basis` (`3ef0412a…` → `9374c21f…`); registers and PRD unchanged; both pointers moved to revision 1.6 / SCA-006; SCA-006 snapshot completed |
| `D-PEC-96` (registry v2) | `v2/**` registry files; DEL-01-06 `MEMORY.md` (header only) and `_run_records/D-PEC-96_REGISTRY_V2/`; no lifecycle, SOW or decomposition change |
| `D-PEC-98` (first SOWs, add-on S) | `ScopeOfWork.md` created for DEL-02-08 and DEL-02-09; both `OPEN` → `INITIALIZED` |
| `D-PEC-99` (Remaining retirement) | `## Remaining` sections removed from 57 `_STATUS.md`; no lifecycle change |
| `D-PEC-101` K1 | 2 folders (12 files) created; 4 `Dependencies.csv` and 16 `_DEPENDENCIES.md` modified; 22 rows added, 2 refreshed |
| `D-PEC-101` K4 + C | 63 `_CONTEXT.md` and 66 `_REFERENCES.md` re-pinned; 2 covers bullets corrected |

## Headline metrics

| Metric | Prior | This run |
|---|---|---|
| Forward deliverable coverage | 97.06 % (66/68) | 100 % (68/68) |
| Context fidelity | 100 % (66/66) | 100 % (68/68) |
| Contexts / references at revision 1.6 (PRD v2.4) | 3 / 0 | 68 / 68 |
| Registers / rows / ACTIVE EXECUTION | 66 / 263 / 111 | 68 / 285 / 127 |
| ACTIVE EXECUTION quotes verbatim | 109/111 | 127/127 |
| IN items fully traced | 70/74 | 74/74 |
| Strict validator | 0 E; 2 DRB-008 (tool `a1544dc4…`) | 0 E; 26 XRG-013; 0 DRB-008 (tool `869df1d5…`) |
| Closure | 111 edges / 66 nodes / 0 SCC / 6 isolated | 127 / 68 / 0 / same 6 |
| Lifecycle | 26 I / 30 O / 4 C / 2 IP / 4 R | 28 I / 30 O / 4 C / 2 IP / 4 R |
| Contracts | 32 SOW_V1 / 34 NONE | 34 SOW_V1 / 34 NONE |
| Issues (B / W / I / EC) | 0 / 3 / 71 / 12 | 0 / 3 / 73 / 2 |

## Dispositions the brief asks for

| Prior | Condition | Disposition | New ID | Attributed to |
|---|---|---|---|---|
| COV-003 | DEL-08-06 folder absent (EC) | RESOLVED | — | D-PEC-101 K1 |
| COV-004 | DEL-10-13 folder absent (EC) | RESOLVED | — | D-PEC-101 K1 |
| COV-073 | SOW-099 → folderless DEL-08-06 (EC) | RESOLVED | — | D-PEC-101 K1 |
| COV-074 | SOW-100 → folderless DEL-10-13 (EC) | RESOLVED | — | D-PEC-101 K1 |
| COV-075 | DEP-09-06-003 quote not verbatim (EC) | RESOLVED | — | D-PEC-101 K1 (B3) |
| COV-076 | DEP-10-03-003 quote not verbatim (EC) | RESOLVED | — | D-PEC-101 K1 (B3) |
| COV-077 | 63 contexts at revision 1.5 (EC) | RESOLVED | — | D-PEC-101 K4 |
| COV-078 | 66 references at revision 1.5 / PRD v2.3 (EC) | RESOLVED | — | D-PEC-101 K4 + C |
| COV-080 | No register traces SOW-097..100 (EC) | RESOLVED | — | D-PEC-101 K1 (B2) |
| COV-008 | DEL-01-03 Check-6 WARNING | CARRIED (identical text) | COV-006 | PRE-EXISTING |
| COV-010 | DEL-01-05 Check-6 WARNING | CARRIED (identical text) | COV-008 | PRE-EXISTING |
| COV-046 | DEL-08-02 Check-6 WARNING | CARRIED (identical text) | COV-044 | PRE-EXISTING |

## Per-finding delta (every prior ID)

`CARRIED` means the same severity and identical description text. `CHANGED`
means the severity is the same but the text changed; no severity changed in
this run. Attribution uses the brief's classes: `EXPECTED_CONSEQUENCE` rows
cite `D-PEC-101`; every other row is `PRE-EXISTING`; no row is `DEFECT`.

| Prior ID | Check | Prior severity | Entity | Disposition | New ID | New severity | Attribution / note |
|---|---|---|---|---|---|---|---|
| COV-001 | 1 | INFO | PKG-00..PKG-10 (11) | CHANGED | COV-001 | INFO | PRE-EXISTING (condition unchanged; description re-worded for this run) |
| COV-002 | 1 | INFO | _Aggregation, _Estimates, _Sources | CHANGED | COV-002 | INFO | PRE-EXISTING (condition unchanged; description re-worded for this run) |
| COV-003 | 2 | EXPECTED_CONSEQUENCE | DEL-08-06 | RESOLVED | — | — | D-PEC-101 K1: folder PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ exists (6 files, OPEN); structure tool PASS; no DRB-008 |
| COV-004 | 2 | EXPECTED_CONSEQUENCE | DEL-10-13 | RESOLVED | — | — | D-PEC-101 K1: folder PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ exists (6 files, OPEN); structure tool PASS; no DRB-008 |
| COV-005 | 6 | INFO | DEL-00-02 | CARRIED | COV-003 | INFO | unchanged condition and text |
| COV-006 | 6 | INFO | DEL-01-01 | CARRIED | COV-004 | INFO | unchanged condition and text |
| COV-007 | 6 | INFO | DEL-01-02 | CARRIED | COV-005 | INFO | unchanged condition and text |
| COV-008 | 6 | WARNING | DEL-01-03 | CARRIED | COV-006 | WARNING | unchanged condition and text |
| COV-009 | 6 | INFO | DEL-01-04 | CARRIED | COV-007 | INFO | unchanged condition and text |
| COV-010 | 6 | WARNING | DEL-01-05 | CARRIED | COV-008 | WARNING | unchanged condition and text |
| COV-011 | 6 | INFO | DEL-01-06 | CHANGED | COV-009 | INFO | PRE-EXISTING (description adds the D-PEC-96 v2-bytes note) |
| COV-012 | 6 | INFO | DEL-02-01 | CARRIED | COV-010 | INFO | unchanged condition and text |
| COV-013 | 6 | INFO | DEL-02-02 | CARRIED | COV-011 | INFO | unchanged condition and text |
| COV-014 | 6 | INFO | DEL-02-03 | CARRIED | COV-012 | INFO | unchanged condition and text |
| COV-015 | 6 | INFO | DEL-02-04 | CARRIED | COV-013 | INFO | unchanged condition and text |
| COV-016 | 6 | INFO | DEL-02-05 | CARRIED | COV-014 | INFO | unchanged condition and text |
| COV-017 | 6 | INFO | DEL-02-06 | CARRIED | COV-015 | INFO | unchanged condition and text |
| COV-018 | 6 | INFO | DEL-02-07 | CARRIED | COV-016 | INFO | unchanged condition and text |
| COV-019 | 6 | INFO | DEL-02-08 | CHANGED | COV-017 | INFO | PRE-EXISTING (now INITIALIZED with SOW_V1 under D-PEC-98) |
| COV-020 | 6 | INFO | DEL-02-09 | CHANGED | COV-018 | INFO | PRE-EXISTING (now INITIALIZED with SOW_V1 under D-PEC-98) |
| COV-021 | 6 | INFO | DEL-03-01 | CARRIED | COV-019 | INFO | unchanged condition and text |
| COV-022 | 6 | INFO | DEL-03-02 | CARRIED | COV-020 | INFO | unchanged condition and text |
| COV-023 | 6 | INFO | DEL-03-03 | CARRIED | COV-021 | INFO | unchanged condition and text |
| COV-024 | 6 | INFO | DEL-03-04 | CARRIED | COV-022 | INFO | unchanged condition and text |
| COV-025 | 6 | INFO | DEL-03-05 | CARRIED | COV-023 | INFO | unchanged condition and text |
| COV-026 | 6 | INFO | DEL-03-06 | CARRIED | COV-024 | INFO | unchanged condition and text |
| COV-027 | 6 | INFO | DEL-04-01 | CARRIED | COV-025 | INFO | unchanged condition and text |
| COV-028 | 6 | INFO | DEL-04-02 | CARRIED | COV-026 | INFO | unchanged condition and text |
| COV-029 | 6 | INFO | DEL-04-03 | CARRIED | COV-027 | INFO | unchanged condition and text |
| COV-030 | 6 | INFO | DEL-04-04 | CARRIED | COV-028 | INFO | unchanged condition and text |
| COV-031 | 6 | INFO | DEL-04-05 | CARRIED | COV-029 | INFO | unchanged condition and text |
| COV-032 | 6 | INFO | DEL-05-01 | CARRIED | COV-030 | INFO | unchanged condition and text |
| COV-033 | 6 | INFO | DEL-05-02 | CARRIED | COV-031 | INFO | unchanged condition and text |
| COV-034 | 6 | INFO | DEL-06-01 | CARRIED | COV-032 | INFO | unchanged condition and text |
| COV-035 | 6 | INFO | DEL-06-02 | CARRIED | COV-033 | INFO | unchanged condition and text |
| COV-036 | 6 | INFO | DEL-06-03 | CARRIED | COV-034 | INFO | unchanged condition and text |
| COV-037 | 6 | INFO | DEL-06-04 | CARRIED | COV-035 | INFO | unchanged condition and text |
| COV-038 | 6 | INFO | DEL-06-05 | CARRIED | COV-036 | INFO | unchanged condition and text |
| COV-039 | 6 | INFO | DEL-06-06 | CARRIED | COV-037 | INFO | unchanged condition and text |
| COV-040 | 6 | INFO | DEL-07-01 | CARRIED | COV-038 | INFO | unchanged condition and text |
| COV-041 | 6 | INFO | DEL-07-02 | CARRIED | COV-039 | INFO | unchanged condition and text |
| COV-042 | 6 | INFO | DEL-07-03 | CARRIED | COV-040 | INFO | unchanged condition and text |
| COV-043 | 6 | INFO | DEL-07-04 | CARRIED | COV-041 | INFO | unchanged condition and text |
| COV-044 | 6 | INFO | DEL-07-05 | CARRIED | COV-042 | INFO | unchanged condition and text |
| COV-045 | 6 | INFO | DEL-08-01 | CARRIED | COV-043 | INFO | unchanged condition and text |
| COV-046 | 6 | WARNING | DEL-08-02 | CARRIED | COV-044 | WARNING | unchanged condition and text |
| COV-047 | 6 | INFO | DEL-08-03 | CARRIED | COV-045 | INFO | unchanged condition and text |
| COV-048 | 6 | INFO | DEL-08-04 | CARRIED | COV-046 | INFO | unchanged condition and text |
| COV-049 | 6 | INFO | DEL-08-05 | CARRIED | COV-047 | INFO | unchanged condition and text |
| COV-050 | 6 | INFO | DEL-09-01 | CARRIED | COV-049 | INFO | unchanged condition and text |
| COV-051 | 6 | INFO | DEL-09-02 | CARRIED | COV-050 | INFO | unchanged condition and text |
| COV-052 | 6 | INFO | DEL-09-03 | CARRIED | COV-051 | INFO | unchanged condition and text |
| COV-053 | 6 | INFO | DEL-09-04 | CARRIED | COV-052 | INFO | unchanged condition and text |
| COV-054 | 6 | INFO | DEL-09-05 | CARRIED | COV-053 | INFO | unchanged condition and text |
| COV-055 | 6 | INFO | DEL-09-06 | CARRIED | COV-054 | INFO | unchanged condition and text |
| COV-056 | 6 | INFO | DEL-09-07 | CARRIED | COV-055 | INFO | unchanged condition and text |
| COV-057 | 6 | INFO | DEL-10-02 | CARRIED | COV-056 | INFO | unchanged condition and text |
| COV-058 | 6 | INFO | DEL-10-03 | CARRIED | COV-057 | INFO | unchanged condition and text |
| COV-059 | 6 | INFO | DEL-10-04 | CARRIED | COV-058 | INFO | unchanged condition and text |
| COV-060 | 6 | INFO | DEL-10-05 | CARRIED | COV-059 | INFO | unchanged condition and text |
| COV-061 | 6 | INFO | DEL-10-06 | CARRIED | COV-060 | INFO | unchanged condition and text |
| COV-062 | 6 | INFO | DEL-10-07 | CARRIED | COV-061 | INFO | unchanged condition and text |
| COV-063 | 6 | INFO | DEL-10-08 | CARRIED | COV-062 | INFO | unchanged condition and text |
| COV-064 | 6 | INFO | DEL-10-09 | CARRIED | COV-063 | INFO | unchanged condition and text |
| COV-065 | 6 | INFO | DEL-10-10 | CARRIED | COV-064 | INFO | unchanged condition and text |
| COV-066 | 6 | INFO | DEL-10-11 | CARRIED | COV-065 | INFO | unchanged condition and text |
| COV-067 | 6 | INFO | DEL-10-12 | CARRIED | COV-066 | INFO | unchanged condition and text |
| COV-068 | 7 | INFO | OBJ-001 | RESOLVED | — | — | D-PEC-101 K1: OBJ-001's 27 supporters are all folder-backed |
| COV-069 | 7 | INFO | DEL-06-04 | CARRIED | COV-068 | INFO | unchanged condition and text |
| COV-070 | 7 | INFO | DEL-07-02 | CARRIED | COV-069 | INFO | unchanged condition and text |
| COV-071 | 7 | INFO | DEL-07-04 | CARRIED | COV-070 | INFO | unchanged condition and text |
| COV-072 | 7 | INFO | DEL-07-05 | CARRIED | COV-071 | INFO | unchanged condition and text |
| COV-073 | 8 | EXPECTED_CONSEQUENCE | SOW-099 | RESOLVED | — | — | D-PEC-101 K1: SOW-099 resolves to the DEL-08-06 folder |
| COV-074 | 8 | EXPECTED_CONSEQUENCE | SOW-100 | RESOLVED | — | — | D-PEC-101 K1: SOW-100 resolves to the DEL-10-13 folder |
| COV-075 | 9 | EXPECTED_CONSEQUENCE | DEP-09-06-003 | RESOLVED | — | — | D-PEC-101 K1 (B3): DEP-09-06-003 EvidenceQuote refreshed to the whole revision-1.6 DEL-08-01 cell; verbatim; LastSeen 2026-09-26 |
| COV-076 | 9 | EXPECTED_CONSEQUENCE | DEP-10-03-003 | RESOLVED | — | — | D-PEC-101 K1 (B3): DEP-10-03-003 refreshed likewise; verbatim |
| COV-077 | 9 | EXPECTED_CONSEQUENCE | DEL-* (63 of 66 _CONTEXT.md) | RESOLVED | — | — | D-PEC-101 K4: 68/68 _CONTEXT.md provenance ends at revision 1.6 (current_basis, SCA-006 successor): 63 re-pinned, 3 A2 mirrors, 2 born at 1.6 by K1 |
| COV-078 | 9 | EXPECTED_CONSEQUENCE | DEL-* (66 of 66 _REFERENCES.md) | RESOLVED | — | — | D-PEC-101 K4 with add-on C: 68/68 _REFERENCES.md name revision 1.6 and PRD v2.4, none 1.5 or v2.3; every active covers bullet equals its register cell (DEL-04-03, DEL-08-03 corrected by C) |
| COV-079 | 9 | EXPECTED_CONSEQUENCE | DEL-04-03; DEL-08-01; DEL-08-03 | RESOLVED | — | — | SCA-006 checkpoint-3 acceptance: revision 1.6 is current_basis, so the A2 mirrors' tails are true (not a D-PEC-101 effect) |
| COV-080 | 9 | EXPECTED_CONSEQUENCE | DEL-04-03; DEL-08-03 | RESOLVED | — | — | D-PEC-101 K1 (B2): DEP-04-03-005 -> SOW-097, DEP-08-03-005 -> SOW-098, DEP-08-06-002 -> SOW-099, DEP-10-13-002 -> SOW-100; 74/74 IN items traced by every deliverable they name |
| COV-081 | 9 | INFO | 32 SOW_V1 contracts | CHANGED | COV-073 | INFO | PRE-EXISTING (count changed by D-PEC-98) |
| COV-082 | 9 | INFO | DEL-00-03; DEL-01-05; DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | CHANGED | COV-074 | INFO | PRE-EXISTING (topology extended by D-PEC-101) |
| COV-083 | 9 | INFO | SOW-094; DEL-01-06; vocabulary 'feed profile' | CHANGED | COV-075 | INFO | PRE-EXISTING (D-PEC-96 applied since) |
| COV-084 | 10 | EXPECTED_CONSEQUENCE | SCA-005 (accepted predecessor); revision 1.5 pointer | RESOLVED | — | — | SCA-006 checkpoint-3 acceptance and A6: both pointers name revision 1.6 / SCA-006 and their basis hashes equal the live bytes (not a D-PEC-101 effect); the new, different staleness against the D-PEC-101 poststate is COV-077 of this run |
| COV-085 | 10 | EXPECTED_CONSEQUENCE | SCA-006 (candidate) | RESOLVED | — | — | SCA-006 A5: active snapshot complete (Post_Change_Coverage.json, RUN_SUMMARY.md present) |
| COV-086 | 10 | INFO | SCA-005 | RESOLVED | — | — | SCA-005 is now the historical predecessor and its snapshot is complete; the method raises no finding for a complete historical snapshot, and its stale-conservative files are no longer active truth |
| — | 6 | — | DEL-08-06 | NEW | COV-048 | INFO | D-PEC-101 (new folder) |
| — | 6 | — | DEL-10-13 | NEW | COV-067 | INFO | D-PEC-101 (new folder) |
| — | 8 | — | 26 OUT/TBD scope items (18 OUT, 8 TBD) | NEW | COV-072 | INFO | PRE-EXISTING (newly measured; validator change) |
| — | 9 | — | _COORDINATION.md Notes (human-owned) L225-227 | NEW | COV-076 | EXPECTED_CONSEQUENCE | D-PEC-101 (pending authorized step) |
| — | 10 | — | _Decomposition/_LATEST.md; _ScopeChange/_LATEST.md; SCA-006 snapshot | NEW | COV-077 | EXPECTED_CONSEQUENCE | D-PEC-101 |
| — | 10 | — | SCA-006 | NEW | COV-078 | INFO | PRE-EXISTING (edition drift; first audited as active) |

Counts: CARRIED 64, CHANGED 8, RESOLVED 14, NEW 6; prior rows 86, new rows 78
