# SCA-004 Gate-5 applied-state preview

Status: `DRAFT — NOT APPLIED`

This preview is the result of applying `Gate_5_Application_Append.diff` to
the exact seven R3-A-approved Gate-3 candidate files. It is not live
decomposition truth and carries no Gate-5 execution authority.

## Approved candidate → applied identity

| Surface | Approved candidate SHA-256 | Applied SHA-256 |
|---|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| `chirality_root_deliverable_register_v1_0.csv` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| `chirality_root_scope_ledger_v1_0.csv` | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| `chirality_root_objective_register_v1_0.csv` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| `chirality_root_trace_reverse_v1_0.csv` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| `chirality_root_coverage_telemetry_v1_0.md` | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

## Slot-by-slot before → after

| Slots | Before | After |
|---|---|---|
| WS-001..WS-005 | SCA-004 Gate-3 candidate title/revision/run/amendment/status; not approved/applied; revision 1.2 live | v1.3 accepted current basis; R3-A/R3-B; append approval, Gate-5 authorization, and Git effect `TBD`; later backfill; pointer authority pending |
| WS-006 | seven SCA-004 candidate responsibility rows | seven applied SCA-004 responsibility rows |
| WS-007 | `v1.3 SCA-004 candidate / 2026-08-23` | `v1.3 applied revision 1.3 / 2026-08-23` |
| WS-008 | OI-011 current-status candidate-row wording | applied-revision wording; assignment unchanged |
| WS-009 | DEC-025 candidate/drafting-only posture | DEC-025 applied posture with R3 approvals and `TBD` application/Git slots |
| WS-010 | Gate-3 candidate change-log entry | applied revision 1.3 entry; pointer authority and downstream exclusions retained |
| SL-001 | `This candidate's bidirectional traceability registers...` | `Applied revision 1.3's bidirectional traceability registers...` |
| SL-002 | present run is a candidate and accepts nothing | applied revision 1.3 itself materializes no folder and changes no export boundary |
| TEL-001..TEL-003 | candidate revision/status/header cells | applied revision 1.3 with R3 approvals, `TBD` Gate-5/Git slots, and pointer authority pending |
| TEL-004..TEL-005 | candidate scope/objective/package inverse prose | applied scope/objective/package inverse prose |
| TEL-006 | seven SCA-004 candidate rows | seven applied SCA-004 rows |

`Gate_5_Slot_Inventory.md` gives every exact locator and the exact one-line
before/after text. `Gate_5_Application_Append.diff` is the controlling exact
slot-by-slot byte representation for multi-line replacements.

## Structural identity statement

Outside the inventoried slots, the approved and applied candidates are
byte-identical. Counts remain exactly 53 deliverables, PKG-02=12,
PKG-04=11, 6 packages, 104 scope items, and 7 objectives. IDs, row sets,
parent-package distribution, scope/objective mappings, and forward/reverse
trace content are unchanged. The append lifts no hold; all ten DEL-02-06
bindings remain `HELD_UNAVAILABLE`.

## Validator reproduction boundary

The protected Phase-0c `validate_gate3_candidate.py` is reproduced only in a
clean scratch Phase-0c layout with Gate-5 artifacts absent; that unmodified
run returns 98/98 and cannot rewrite the protected live validation JSON. The
applied preview is checked by the status-inverted applied-state equivalent:
98/98 with only current-posture assertions and the two inventoried
scope-ledger Notes cells adjusted. All structural mapping, trace, count,
basis, and containment checks remain the Phase-0c checks.
