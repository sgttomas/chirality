# WORKING-A2-PKG04 Package Checks

Overall verdict: `PASS`.

## Frozen basis and scope

Dispatch main is `0af23f4709e1c95f6b2e0f19db80779bd4c968fa`; accepted row and
decomposition basis `b4d2c9ab2f089224ddd41c849bbd1e4dd22d91b4` is its ancestor;
migration authority is `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.
Exactly DEL-04-01 through DEL-04-05 remain IN_PROGRESS, non-ISSUED,
LEGACY_FOUR_DOC with zero live ScopeOfWork.md. Project paths remained read-only.

## Author/verifier fan-in

Five authors and five fresh independent verifier chains are terminal PASS and
manager-accepted, including evidence-only terminalization/remediation where
recorded in CHILD_INDEX.tsv.

| Member | Candidate SHA-256 | Mappings | Source lines | Author | Verifier |
|---|---|---:|---:|---|---|
| DEL-04-01 | `45157c90dfbb088b522d8299d5b9df5c06acb04dd61bc7c6610ff9c33685cd75` | 30 | 394 | PASS | PASS |
| DEL-04-02 | `15796b93739a7a3481c288aafc8550baae34a440b159f4d80adbe7698c17428d` | 31 | 376 | PASS, manifest R1 | PASS, run-record binding R1 |
| DEL-04-03 | `72c083f28a597583abf1b6e950f0ce0965221f9cd2fee0233408954336aaa100` | 27 | 314 | PASS | PASS, R1 unchanged |
| DEL-04-04 | `9d7a5de67db2b656f86246b1f2f466862ae60e53102d011be6910555afab15b6` | 30 | 284 | PASS, terminal metadata R1 | PASS, R1 repaired |
| DEL-04-05 | `1095591a196fb61fbfbe30aaa779e3eaeba99c27c79864da428a74ac70c25157` | 35 | 383 | PASS | PASS, R1 repaired |

Aggregate coverage is 153 mappings over all 1,751 source lines. Each
candidate directory contains exactly ScopeOfWork.md and resolves as SOW_V1.
Every verifier passed exact identity, schema, source map, parity, full line
coverage, conservative content authority, checklist identity/linkage, render
identity/safety, negative fixtures, replacement paths, containment, and the
four separate schema/content-authority/preservation/substrate verdicts.

## Project checks

The accepted registered profile passed harness-self-check, harness-pytest
(264 tests), frontend-typecheck, frontend-test (713 passed, 4 skipped), and
frontend-build. Its first frontend-premerge attempt failed only because no
local server was listening at the profile's `127.0.0.1:3000` endpoint. The
accepted stub-provider Next server was started temporarily and the same
registered frontend-premerge check then passed Section 8 (8/8) and report-only
Section 9 (16/16). The server was stopped and project dirty paths remained
zero. Both initial FAIL and closed rerun PASS records are retained.

## Replacement, rollback, portability, containment

- REPLACEMENT_MANIFEST.tsv has exactly 25 rows: one ADD ScopeOfWork.md and
  four DELETE legacy-production rows per member.
- ROLLBACK_MANIFEST.tsv is the exact 25-row inverse with identical paths and
  hashes. Neither manifest contains status/control paths.
- Generated evidence normalization is exactly reversible: 28 checkout and 6
  temp-root substitutions in the two check records, plus 28 checkout-root
  substitutions in nine TASK run records. All postimages and child bindings
  reproduce; details are in PROJECT_CHECK_NORMALIZATION.md.
- Sixteen immutable copied source/control literals are preserved and exactly
  inventoried. Generated evidence and candidates contain zero machine roots.
- All writes are contained to the authorized candidate/evidence scopes;
  project tracked/untracked dirty paths are zero.

Blockers, conflicts, unknowns, waivers, and human rulings needed: none. This
is a derivative candidate recommendation only; independent RECONCILIATION is
mandatory before any CHANGE integration.
