# AUTHOR-DEL-10-03 Evidence

## Bound basis

- Run: `SOW-STAGE2-EXEC-20260712-01`
- Deliverable: `APP / PKG-10 / DEL-10-03`
- Live source: `projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow`
- Decomposition: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0`
- Scope/objective: `SOW-069` / `OBJ-010`
- Migration authority: `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`
- Source lifecycle: `IN_PROGRESS`; non-`ISSUED`; live format `LEGACY_FOUR_DOC`; zero live `ScopeOfWork.md`.

The exact `A3_MANIFEST.tsv` row was confirmed before conversion. The workspace copies of the four production documents, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `Dependencies.csv` were byte-equal to the live files before conversion and remained byte-equal after all substantive checks.

## Frozen input hashes

| File | SHA-256 |
|---|---|
| `Datasheet.md` | `564a44d3ff6c2c6fff5306f4a07ca8256b990592ee92d7c57bffef1918a265f7` |
| `Specification.md` | `35c79c7a4553519de17eb0688d120916d2ff8259eb5a73664aaf8d8f5bf6c279` |
| `Guidance.md` | `8642c650e66577428402748a4927331221bd1dc5aeccaa0ffc964c6e7aebdef9` |
| `Procedure.md` | `37da42c72bfb1110f7a10aeab0ff8324b8b315024171fc62ed7f386db69942fe` |
| `_STATUS.md` | `0635a06b6f84a37fb634813fabd092f5064ab330527e7855ff17c28fb66ed472` |
| `_CONTEXT.md` | `2d9e34de616404c3bab0fcd95fefc4fd798084aeb36811a4379862d74954c1bc` |
| `_REFERENCES.md` | `39cfa5962b10fa5bc9b6560aa504b5c83ab5963a195f1d8dbe3129ce8c69786b` |
| `_DEPENDENCIES.md` | `64472518c823791130c01968d9fcdbf9bb9c83a993ac2d89ca09dded6900b4a3` |
| `Dependencies.csv` | `4a98318da160142d3b2ceeda1c88b5134e88d0146924883e3bf2a7777f3c875c` |

## Outputs and deterministic checks

| Artifact/check | Result |
|---|---|
| Workspace and candidate `ScopeOfWork.md` | byte-identical; SHA-256 `2f8abf603425a53161f41d0b67b9c590832af3daee97794de876430340c6b677` |
| Format resolution | valid authorized `MIGRATION_DUAL`; no issues |
| Claim map | PASS; 30 rows |
| Source coverage | PASS; 341/341 lines, 30 `PRESERVED` ranges |
| Parity | PASS; 30/30 checks; no silent drop or text mismatch |
| Checklist run 1 / run 2 | byte-identical; SHA-256 `f182f4ca046159559b846bce57c2bd3221d405409ec3d505e5b210a1d4eb3a15`; one exact `AC-001` linked to `VER-001` |
| HTML run 1 / run 2 | byte-identical; SHA-256 `df41981c2097acdfeafdc4052a2862fb4aa6abd18749c74dca9ff9dbc161c454` |
| HTML safety | no script, form, JavaScript URI, HTTP(S) resource, or external `src`/`href` reference |
| Source/control preservation | PASS; all nine copied inputs remain byte-equal to live |

## Fail-closed fixtures

- Partial legacy kit plus candidate: validator returned `INVALID`; checklist returned nonzero without its requested output.
- Complete dual format without migration authority: validator returned `AMBIGUOUS`; checklist returned nonzero without its requested output.
- Complete byte-exact dual format with a leading-space-padded authority: validator returned `AMBIGUOUS`; checklist returned nonzero without its requested output.
- Fixture directories, validator JSON/stderr, and checklist stderr are retained. The fixtures were constructed correctly without mutating candidate or authoritative source bytes, and no malformed positive result was misclassified as negative evidence.

See `FAIL_CLOSED_FIXTURES.tsv` for the exact disposition of each attempt.

## Separate verdicts

- `SCHEMA_VERDICT: PASS` — the candidate validates as `chirality-deliverable-sow/v1` under exact isolated migration authority, with closed IDs and matrix references.
- `CONTENT_AUTHORITY_VERDICT: PASS` — `OUT-001`, `AC-001`, and `VER-001` are bounded to deliverable identity, `SOW-069`, `OBJ-010`, exact legacy-source preservation, proposal-only status, and the source-defined human gate. No operation approval, protected-path mutation, solver reliance, lifecycle meaning, or semantic obligation was authored.
- `PRESERVATION_VERDICT: PASS` — all 341 source lines are preserved with current source hashes; copied control files and `_STATUS.md` remain byte-identical; candidate copy is exact.
- `SUBSTRATE_VERDICT: PASS` — all registered deterministic Python tools executed natively and returned the required positive and fail-closed results.

No project, Git, lifecycle, H1/H2, issuance, release, retirement, integration, or sibling surface was written.
