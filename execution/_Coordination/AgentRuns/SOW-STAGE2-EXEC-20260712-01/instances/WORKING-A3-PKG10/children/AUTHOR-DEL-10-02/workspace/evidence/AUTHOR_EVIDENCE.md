# AUTHOR-DEL-10-02 Evidence

## Bound basis

- Run: `SOW-STAGE2-EXEC-20260712-01`
- Deliverable: `APP / PKG-10 / DEL-10-02`
- Live source: `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy`
- Decomposition: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0`
- Scope/objective: `SOW-068` / `OBJ-010`
- Migration authority: `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`
- Source lifecycle: `IN_PROGRESS`; non-`ISSUED`; live format `LEGACY_FOUR_DOC`; zero live `ScopeOfWork.md`.

The exact `A3_MANIFEST.tsv` row was confirmed before conversion. The workspace copies of the four production documents, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `Dependencies.csv` were byte-equal to the live files before conversion and remained byte-equal after all substantive checks.

## Frozen input hashes

| File | SHA-256 |
|---|---|
| `Datasheet.md` | `f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d` |
| `Specification.md` | `9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7` |
| `Guidance.md` | `95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8` |
| `Procedure.md` | `a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c` |
| `_STATUS.md` | `0fffc59600f592f0979d9193606f263aed95eca19a00b939cd8c71d7a86ad2bf` |
| `_CONTEXT.md` | `9276a56db2e943eca3c23386b973e935b6c8f22ed2a8262b7b65892803bf7f7e` |
| `_REFERENCES.md` | `54e2a2061da4fc1911e325a3a73734823048d1cffd8d088e8baef2cf55e5a526` |
| `_DEPENDENCIES.md` | `601caabb146ab00aaacd3f2b3e5b6ba46c3a1e549fa43e375c22e2b4f2912f52` |
| `Dependencies.csv` | `bda035243a1c22c759027772d51981386f22feeab2921095864d2fec7b46d119` |

## Outputs and deterministic checks

| Artifact/check | Result |
|---|---|
| Workspace and candidate `ScopeOfWork.md` | byte-identical; SHA-256 `204721c5221d1311ff94c93fa60ff3292d715ad2ab146032c7d6ba71f85582bb` |
| Format resolution | valid authorized `MIGRATION_DUAL`; no issues |
| Claim map | PASS; 27 rows |
| Source coverage | PASS; 282/282 lines, 27 `PRESERVED` ranges |
| Parity | PASS; 27/27 checks; no silent drop or text mismatch |
| Checklist run 1 / run 2 | byte-identical; SHA-256 `37c90e2609ba14d96d29089155200b8c8a13effdd624f25ad3729d08b472db77`; one exact `AC-001` linked to `VER-001` |
| HTML run 1 / run 2 | byte-identical; SHA-256 `ba262980d8cd88b02353e926b0dcf3a249a7931d39dd09b6589db73e1a75251f` |
| HTML safety | no script, form, JavaScript URI, HTTP(S) resource, or external `src`/`href` reference |
| Source/control preservation | PASS; all nine copied inputs remain byte-equal to live |

## Fail-closed fixtures

- Partial legacy kit plus candidate: validator returned `INVALID`; checklist returned nonzero without its requested output.
- Complete dual format without migration authority: validator returned `AMBIGUOUS`; checklist returned nonzero without its requested output.
- The first padded-authority fixture attempt was malformed: it changed a fixture source byte but supplied the exact unpadded authority, so validation and checklist correctly succeeded. That result and emitted checklist are retained as evidence; it is not treated as a negative-test PASS.
- Corrected fixture-only rerun supplied a leading-space-padded authority while leaving candidate and authoritative source bytes unchanged. Validator returned `AMBIGUOUS`; checklist returned nonzero without `NEGATIVE_PADDED_CORRECTED_CHECKLIST.json`.

See `FAIL_CLOSED_FIXTURES.tsv` for the exact disposition of each attempt.

## Separate verdicts

- `SCHEMA_VERDICT: PASS` — the candidate validates as `chirality-deliverable-sow/v1` under exact isolated migration authority, with closed IDs and matrix references.
- `CONTENT_AUTHORITY_VERDICT: PASS` — `OUT-001`, `AC-001`, and `VER-001` are bounded to deliverable identity, `SOW-068`, `OBJ-010`, and exact legacy-source preservation. No new protected-path write, proposal approval, domain operation, lifecycle, or semantic obligation was authored.
- `PRESERVATION_VERDICT: PASS` — all 282 source lines are preserved with current source hashes; copied control files and `_STATUS.md` remain byte-identical; candidate copy is exact.
- `SUBSTRATE_VERDICT: PASS` — all registered deterministic Python tools executed natively and returned the required positive and corrected fail-closed results.

No project, Git, lifecycle, H1/H2, issuance, release, retirement, integration, or sibling surface was written.
