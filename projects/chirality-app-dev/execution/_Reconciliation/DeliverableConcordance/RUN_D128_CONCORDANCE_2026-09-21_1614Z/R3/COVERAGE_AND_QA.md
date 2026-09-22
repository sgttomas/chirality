# R3 coverage and QA — RUN_D128_CONCORDANCE_2026-09-21_1614Z

Built by `R3/_scripts/r3_qa.py` (deterministic). Inputs: `CLAIM_CONCORDANCE.csv`, `EXTENSION_CONCORDANCE.csv`, `REVERSE_CONCORDANCE.csv`, `REMAP_LOG.csv`, `_work/SEALED_ROWS.csv`, `R1_INVENTORY/CLAIM_INDEX.csv`, `R1_INVENTORY/EXTENSION_INDEX.csv`, `R2/SURFACES/*_capabilities.csv`, `R2/*/PACKAGE_SUMMARY.md`, `R2/EXT/EXT_SUMMARY.md`.

| Check | Verdict | Counts |
|---|---|---|
| Q1 CLAIM_INDEX units dispositioned | PASS | 1746 of 1746 (expected 1,746); missing 0 [] |
| Q2 EXTENSION_INDEX units dispositioned | PASS | 221 of 221 (expected 221); missing 0 [] |
| Q3 capabilities claimed or listed as unmapped (with reach and state) | PASS | 468 capability rows: 361 claimed/partial by >=1 deliverable, 107 in UNMAPPED_IMPLEMENTATION.csv; unmapped without stated reach/state: 0 []; reverse IDs not in any capability file: 0 [] |
| Q4 package summaries reproduce from the ledgers (sealed Disposition census) | PASS | 24 of 24 summaries reproduce |
| Q5 no duplicate keys | PASS | ClaimKey duplicates 0 []; reverse (CapabilityID, DeliverableID) duplicates 0 [] |
| Q6 REMAP_LOG reconciles the sealed census to the final census | PASS | 3568 rows replayed from sealed values through 1188 log lines; mismatches 0 [] |

## Q4 detail (per summary)

- PKG-00: 90 rows; reproduces
- PKG-01: 294 rows; reproduces
- PKG-02: 343 rows; reproduces
- PKG-03: 285 rows; reproduces
- PKG-04: 280 rows; reproduces
- PKG-05: 274 rows; reproduces
- PKG-06: 358 rows; reproduces
- PKG-07: 335 rows; reproduces
- PKG-08: 310 rows; reproduces
- PKG-09: 375 rows; reproduces
- PKG-10: 273 rows; reproduces
- EXT DEC: 46 rows; reproduces
- EXT DOC-ADDING_A_TOOL: 8 rows; reproduces
- EXT DOC-BUILDREL: 48 rows; reproduces
- EXT DOC-PRODAGENTS: 9 rows; reproduces
- EXT DOC-README: 7 rows; reproduces
- EXT DOC-RELIANCE: 51 rows; reproduces
- EXT DOC-RQGATES: 23 rows; reproduces
- EXT DOC-RQRUN: 7 rows; reproduces
- EXT DOC-RUNTIME_ENGINE_CONTRACT: 11 rows; reproduces
- EXT DOC-TOOL_CATALOG: 4 rows; reproduces
- EXT DOC-TRACEABILITY: 2 rows; reproduces
- EXT DOC-VALSTRAT: 22 rows; reproduces
- EXT SOW: 113 rows; reproduces

Method: for each package, every sealed Disposition count computed from the ledgers of record must appear in that Disposition's census row of `PACKAGE_SUMMARY.md`, and `Total rows:` (where stated) must match; for EXT, each ledger's `Disposition:` census line in `EXT_SUMMARY.md` §3 must equal the ledger.

## Q6 census (all rows: deliverable + EXT)

| Disposition | Sealed | Final | Delta |
|---|---:|---:|---:|
| ALIGNED | 893 | 890 | -3 |
| IMPLEMENTED_UNDOCUMENTED | 1 | 1 | +0 |
| DOCUMENTED_UNIMPLEMENTED | 120 | 114 | -6 |
| PARTIALLY_IMPLEMENTED | 445 | 441 | -4 |
| IMPLEMENTED_DIFFERENTLY | 216 | 207 | -9 |
| STALE_SPECIFICATION | 1077 | 1089 | +12 |
| STALE_ASSESSMENT | 8 | 8 | +0 |
| STALE_VERIFICATION | 35 | 35 | +0 |
| ACCEPTED_DIVERGENCE | 43 | 38 | -5 |
| RETIRED_BY_RULING | 49 | 49 | +0 |
| LIFECYCLE_REASSESSMENT_REQUIRED | 2 | 2 | +0 |
| REMAINING_STATE_MISMATCH | 128 | 116 | -12 |
| DEFERRED_AGENT_WORKFLOW | 1 | 1 | +0 |
| AUTHORITY_CONFLICT | 155 | 169 | +14 |
| UNKNOWN | 10 | 23 | +13 |
| NOT_AUDITABLE | 385 | 385 | +0 |
| **Total** | 3568 | 3568 | +0 |

The replay starts from each row's sealed Disposition and HumanDecisionNeeded and applies every REMAP_LOG line for those fields in order; each line's SealedValue must equal the replayed prior value (no silent change), and the end state must equal the final concordance cell.
