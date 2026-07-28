# SCA-APP-006 Gate-3 Adversarial Backcheck

**Role:** sealed read-only Agent 2 adversary

**Date:** 2026-07-27

**Final substantive disposition:** `CONDITIONAL_ADMIT_PENDING_FINAL_HASH_FREEZE`

## Initial findings and disposition

| Finding | Severity | Finding | Disposition |
|---|---|---|---|
| G3-001 | BLOCK | The integration draft renamed `DEL-02-05` despite accepted Gate 2 explicitly preserving all deliverable names. | `CLOSED`: the original name is restored. Independent comparison finds zero deliverable-name, type, or envelope changes and zero scope-item status or package changes. |
| G3-002 | BLOCK | `Gate_3_Artifact_Hashes.sha256` was referenced but absent, so the candidate was not frozen. | `PENDING_MECHANICAL_CLOSE`: file this review, generate the hash manifest last, and verify every entry. No substantive candidate amendment is required. |
| G3-003 | REVIEW | The mapper return used nonexistent D-GOV-28 `#Outcome` anchors; the integrated correction was not initially reproducible from the sealed input. | `CLOSED`: `prepare_register_candidate.py` now performs a Root-row-only `#Outcome` to `#Effects` correction. Independent regeneration is byte-identical to register SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`. |

## Corrected-byte results

- candidate decomposition SHA-256:
  `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`;
- exact zero-context patch SHA-256:
  `5aac4f33c62a4cea99ae02cd2cbdbf0bde3e24fc9fd93fa7fbae54c2eda66733`;
- candidate register SHA-256:
  `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`;
- POSIX patch apply and `git apply --unidiff-zero`: PASS;
- integrated validator: `PASS_WITH_EXPLICIT_UNKNOWNS`;
- traceability comparator: PASS;
- invariant population: 81 exact IDs / 48 families;
- semantic owners: 45 App / 22 Root / 14 explicit unknown;
- topology and stable IDs: unchanged;
- accepted mismatch set: exactly seven scope IDs;
- candidate mismatch set: zero;
- supported relations deleted: zero;
- OUT scope activated: zero;
- `DEL-02-05` / `SOW-023`, `SOW-064`, `REF-006`, and `DEC-022`:
  within the accepted exact-amendment envelope;
- Gate-4, implementation, contract, repin, hold, lifecycle, and Git authority:
  not introduced.

No new BLOCK or REVIEW finding remained after correction. When G3-002's final
hash-freeze check passes without changing a substantive candidate byte, this
backcheck becomes `ADMIT`.
