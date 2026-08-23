# AUDIT_DECOMP decision log

| ID | Decision | Basis / effect |
|---|---|---|
| AUD-DEC-001 | Apply the human-authorized output-location override. | The sealed brief overrides the agent default snapshot root and pointer behavior. All outputs are confined to `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP/`; nothing under `execution/_Evaluation/` and no `_LATEST.md` pointer is created or modified. Audit semantics are unchanged. |
| AUD-DEC-002 | Treat the main document and named companion registers as the canonical SOFTWARE working package. | The main decomposition §3 explicitly labels the working surface and authoritative companion registers. Machine truth for deliverables and ledger rows is read from the two bound CSV inputs. |
| AUD-DEC-003 | Scope partitions to the parents of the three scoped deliverables. | This produces three scoped package rows while preserving whole-repository topology separately. It avoids presenting the scoped run as an all-repository scan. |
| AUD-DEC-004 | Count five relevant objectives. | The scoped deliverables cite `OBJ-001`, `OBJ-002`, `OBJ-003`, `OBJ-004`, and `OBJ-007`. All mappings resolve; duplicate references to `OBJ-003` count once. |
| AUD-DEC-005 | Do not count `ScopeOfWork.md` as a produced anticipated artifact. | The contract describes future outputs but its filename does not match any anticipated production artifact. Exact artifact presence is therefore 0/5, 0/3, and 0/3. At `INITIALIZED`, the eleven absences remain INFO under Check 6. |
| AUD-DEC-006 | Treat Check 9 as `SKIPPED`. | Derivative-package parity is not variant-owned by a SOFTWARE audit. Package-shape Check 9b still runs and passes. |
| AUD-DEC-007 | Treat SCA-002's application append as the current handoff state. | The append is later than the preserved drafting section and agrees with `_LATEST.md` and the live decomposition revision. No overclaim or active-snapshot contradiction is present. |
| AUD-DEC-008 | Return a non-blocking `OK` verdict with `PASS` closure-readiness for coverage only. | There are 0 BLOCKER, 0 WARNING, and 11 INFO findings. This verdict does not interpret SCA-004 Gate 1 or authorize a later gate. |

No assumptions were used to repair missing or ambiguous source truth. No prior
run label was supplied, so optional comparison mode is not applicable.
