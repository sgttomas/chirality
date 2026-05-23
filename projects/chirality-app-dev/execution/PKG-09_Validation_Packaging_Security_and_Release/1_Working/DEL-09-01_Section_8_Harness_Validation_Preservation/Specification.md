# Specification: DEL-09-01 Section 8 Harness Validation Preservation

## Scope

DEL-09-01 covers preservation of the existing Section 8 harness validation surface, current local checks, and stable premerge summary behavior for PKG-09. It includes test runner preservation tests and premerge summary checks.

Out of scope:

- Feature implementation except test fixtures and packaging glue. Source: `_CONTEXT.md` Package Scope.
- Section 9 runtime validation additions, except where Section 8 preservation must leave room for the Section 9 IDs listed by SPEC and PRD. Source: `docs/SPEC.md` Sections 19.2 and 19.3; `docs/PRD.md` Sections 12.3 and 12.4.
- New professional approval, code compliance, external validation, or solver-truth claims. Source: `docs/CONTRACT.md` K-PROF-1 and K-DOMAIN-4.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-09-01-REQ-001 | The frontend package must expose `harness:validate:section8` and `harness:validate:premerge` scripts. | `frontend/package.json` scripts | Inspect package scripts; execute wrapper in local/CI validation. |
| DEL-09-01-REQ-002 | Required local release-significant checks must include `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, and `npm run instruction-root:integrity` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 | Release checklist and CI/premerge run records cite command outcomes. |
| DEL-09-01-REQ-003 | The premerge wrapper must fail if `frontend/scripts/validate-harness-section8.mjs` is missing or unreadable. | `frontend/scripts/validate-harness-premerge.mjs` ensureReadableFile/scriptPath branch | Unit or script-level test covers missing script behavior, or wrapper execution proves readable script. |
| DEL-09-01-REQ-004 | The premerge wrapper must require these Section 8 IDs: `setup.server_reachable`, `regression.session_crud`, `section8.boot_error_taxonomy`, `section8.smoke_stream`, `section8.session_persistence_resume`, `section8.permissions_dontask`, `section8.interrupt_sigint`, `section8.sdk_native_stream`. | `frontend/scripts/validate-harness-premerge.mjs` REQUIRED_TEST_IDS; `frontend/scripts/validate-harness-section8.mjs` REQUIRED_CHECK_ORDER | Wrapper parses summary results and fails on missing IDs. |
| DEL-09-01-REQ-005 | The premerge wrapper must reject the legacy removed ID `regression.api_chat_reachability` if it appears in the summary. | `frontend/scripts/validate-harness-premerge.mjs` LEGACY_REMOVED_TEST_ID | Deterministic wrapper fixture or script-level test verifies legacy-ID rejection without relying only on an end-to-end CI run. |
| DEL-09-01-REQ-006 | `npm run harness:validate:premerge` must create or update `frontend/artifacts/harness/section8/latest/summary.json`. | `docs/PRD.md` FR-066; `frontend/scripts/validate-harness-premerge.mjs` stableArtifactPath; `.github/workflows/harness-premerge.yml` Verify stable summary artifact | Local command and CI workflow verify artifact readability. |
| DEL-09-01-REQ-007 | CI premerge validation must run the wrapper after server readiness and upload the stable summary artifact. | `.github/workflows/harness-premerge.yml` | Pull request or workflow dispatch run verifies readiness poll, wrapper execution, artifact check, and upload step. |
| DEL-09-01-REQ-008 | Section 8 validation must cover server reachability, session CRUD, boot error taxonomy, smoke stream ordering, session persistence/resume continuity, permissions under current validation markers, interrupt behavior, and SDK-native stream handling with no legacy parser regressions. | `docs/SPEC.md` Section 19.2; `docs/PRD.md` Section 12.3 | Required test IDs and summary content map to the listed behavior. |
| DEL-09-01-REQ-009 | Unknown or unsupported factual details in validation preservation documents must remain `TBD`, `ASSUMPTION`, or conflict entries rather than invented requirements. | `docs/CONTRACT.md` K-INVENT-1; `skills/four-documents/SKILL.md` source-grounding rule | Document review checks for unsupported claims. |
| DEL-09-01-REQ-010 | The PRD hash mismatch observed for this run must be recorded as a source warning only and must not block P1/P2 authoring. | Invoker runtime instruction; `_REFERENCES.md` REF-006 | Run record and documents record the warning without treating PRD as absent. |

## Standards

- `docs/SPEC.md` is authoritative for validation checklist surfaces and Section 8/9 validation IDs.
- `docs/PRD.md` is authoritative for product requirements and acceptance criteria, with the run-specific source warning that its observed SHA256 does not match `_REFERENCES.md`.
- `docs/CONTRACT.md` is authoritative for invariant K-VALIDATE-1 and no-invention discipline.
- `docs/TYPES.md` is authoritative for release and validation vocabulary.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` is authoritative for the DEL-09-01 package/deliverable assignment and SOW/objective mapping.

## Verification

| Requirement | Verification approach |
|---|---|
| DEL-09-01-REQ-001 through DEL-09-01-REQ-006 | Static review of `frontend/package.json` and validation scripts plus local execution of `npm run harness:validate:premerge` from `frontend/`; wrapper fixture tests should also cover missing required IDs and legacy-ID rejection deterministically. |
| DEL-09-01-REQ-007 | CI workflow run on pull request or manual dispatch. |
| DEL-09-01-REQ-008 | Compare required test IDs and Section 8 summary rows against SPEC/PRD behavior list. |
| DEL-09-01-REQ-009 | Human review of document kit and test changes for unsupported facts. |
| DEL-09-01-REQ-010 | Run record includes PRD hash warning and does not report PRD as inaccessible. |

Current acceptance evidence boundary: the provenance summary can show expected Section 8 summary shape and the eight-row ID set, but current acceptance requires fresh evidence from `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `npm run instruction-root:integrity`, and, for desktop release packaging context, `npm run desktop:dist`. This deliverable records those evidence expectations without asserting that the commands passed in the current working tree.

## Documentation

Required artifacts for this deliverable:

- Section 8 validation preservation tests.
- Premerge summary checks.
- Evidence of stable summary artifact generation at `frontend/artifacts/harness/section8/latest/summary.json`.
- CI artifact upload evidence for `harness-section8-summary`.
- Any residual `TBD`, `ASSUMPTION`, or source-warning notes carried forward into closure.
