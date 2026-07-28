# SCA-APP-006 Decision Log

| Date | Gate | Actor | Decision | State |
|---|---:|---|---|---|
| 2026-07-27 | Preparation | SCOPE_CHANGE | Prepared conditional intake on `684979863ff8d2d94ea69d20b299f31a22de4180`; made no repository write and reserved no identifier. | `HISTORICAL_INPUT` |
| 2026-07-27 | Basis | SCOPE_CHANGE | Refreshed against accepted `main@4214915d9fcfecdc2952626421bf50b0e5f7845b`; decomposition, PRD, CONTRACT, prior SCA pointer, and local namespace reproduced the conditional basis. | `CURRENT_BASIS_VERIFIED` |
| 2026-07-27 | 1 | Ryan Tufts | Selected `OD6-G1-P1`, `OD6-G2-I1`, and `OD6-G2-M1-A`; confirmed SCA-APP-006 Gate 1; expressly authorized `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` as an authoritative SCOPE_CHANGE write surface; required stable IDs and package/deliverable topology to remain unchanged. | `CONFIRMED` |
| 2026-07-27 | 1 | Ryan Tufts | Explicitly withheld Gate 2, exact register rows, exact amendments, propagation, ScopeOfWork edits, repinning, APP-HOLD-1 changes, implementation, and Git closeout. | `BOUNDARY_RECORDED` |
| 2026-07-27 | 1 | SCOPE_CHANGE | Assigned `SCA-APP-006` after rescanning the App-local namespace; parsed 12 atomic actions; assigned the next App-local decision candidate `DEC-022`; found no parent-closure action. | `VALIDATED` |
| 2026-07-27 | 1 | Read-only Agent 2 rescan | Reproduced the 81-ID/48-family invariant census, exactly seven bidirectional mapping differences, all topology counts and source identities, and every A001–A012 target. It also found four carried stale PKG-02 package-description fields in the enumerated candidate Gate-4 `DEL-02-05/_CONTEXT.md` surface. | `PASS_WITH_CARRIED_METADATA_DRIFT` |
| 2026-07-27 | 1 | AUDIT_DECOMP | Fresh all-scope pre-change audit found 10/10 packages, 51/51 deliverables, 51/51 contexts and valid SOW contracts, 78 ledger rows, 10/10 objectives, 0 blockers, 55 warnings, and 2 information findings. | `WARNINGS_NO_BLOCKER` |
| 2026-07-27 | 1 | Read-only Agent 2 adversary | Independently reproduced all load-bearing Gate-1 facts and found no BLOCK or REVIEW. Its one wording warning was accepted: three records now describe `DEL-02-05/_CONTEXT.md` as an enumerated candidate Gate-4 metadata surface rather than implying propagation authority. | `PASS_AFTER_WORDING_CORRECTION` |
| 2026-07-27 | 2 | SCOPE_CHANGE | Prepared an evidence-linked impact assessment for owner review without accepting it. | `PREPARED` |
| 2026-07-27 | 2 | Ryan Tufts | Accepted `Impact_Assessment.md` at SHA-256 `44eaf7f8773bfd5f311058e392ea11266136abfdb9fed126a6374eb2e57ad670`; authorized exact Gate-3 candidate preparation only and withheld every candidate byte, propagation, application, downstream repair, implementation, and Git act. | `ACCEPTED` |
| 2026-07-27 | 3 basis | SCOPE_CHANGE | Refreshed to accepted `main@c487b7dd57a378e2f74417118e78e7f61a161629`; the App decomposition, PRD, CONTRACT, and prior tracked SCA pointer are byte-identical to the Gate-2 basis. | `CURRENT_BASIS_VERIFIED` |
| 2026-07-27 | 3 | Read-only Agent 2 mapper | Produced 81 exact invariant rows in all 48 CONTRACT families with closed enums, evidence anchors, 45 App / 22 Root / 14 explicit unknown semantic owners, and no unresolved topology reference. | `RETURN_ADMITTED_FOR_INTEGRATION` |
| 2026-07-27 | 3 | Read-only Agent 2 drafter | Produced an applyable exact decomposition patch covering the authorized text envelope. | `RETURN_ADMITTED_FOR_INTEGRATION` |
| 2026-07-27 | 3 | SCOPE_CHANGE | Rebased every candidate register row to the integrated candidate decomposition SHA, reproduced the patch, and ran the SCA-local validator and traceability comparator. | `PREPARED_NOT_ACCEPTED` |
| 2026-07-27 | 3 | Read-only Agent 2 adversary | Found that the mapper's 22 Root-owned rows cited the nonexistent D-GOV-28 `#Outcome` anchor. SCOPE_CHANGE corrected the integrated candidate rows to the record's actual `#Effects` anchor and strengthened the validator; the sealed mapper return remains unchanged. | `CORRECTION_APPLIED_PENDING_RECHECK` |
| 2026-07-27 | 3 | Read-only Agent 2 adversary | Blocked an integration-time proposal to rename `DEL-02-05` because accepted Gate 2 expressly preserved every deliverable name. SCOPE_CHANGE removed the rename and retained only the authorized description, artifact, mapping, and note changes. | `BLOCK_CLOSED_PENDING_RECHECK` |
| 2026-07-27 | 3 | Read-only Agent 2 adversary | Rechecked the corrected bytes, closed the name and reproducibility defects, found no new BLOCK or REVIEW, and issued conditional admission pending the mechanical final hash freeze only. | `CONDITIONAL_ADMIT` |

## Exact owner ruling

The exact owner text is preserved verbatim in `Brief.md` under “Exact owner
confirmation.” It is the authoritative in-session provenance for Gate 1.

## Current gate boundary

Gate 2 is accepted. Gate 3 is prepared but not accepted. No decomposition,
companion-register, deliverable-context, contract, hold, implementation, or
Git change has been approved or applied.
