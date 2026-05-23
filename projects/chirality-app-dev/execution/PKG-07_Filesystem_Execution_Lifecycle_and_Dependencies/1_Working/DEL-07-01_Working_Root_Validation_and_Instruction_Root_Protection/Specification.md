# Specification: DEL-07-01 Working Root Validation and Instruction Root Protection

## Scope

This deliverable specifies the security-control behavior for validating the active working root and protecting the release-managed instruction root during ordinary project execution.

In scope:

- Working-root validation for absolute path, existence, directory type, app read/write access, and instruction-root containment.
- Runtime path containment for tools and governed writes under the active project root.
- Instruction-root write protection for ordinary project execution.
- Initial symlink-write rejection where write/edit tools are governed by hooks.
- Root validation tests, path policy helpers, and instruction-root protection fixtures.

Out of scope:

- UI presentation except scope scan results, per `_CONTEXT.md` package exclusions.
- General write/edit governance beyond root/path policy. `DEL-06-04` covers the broader write/edit surface and path hooks in the decomposition.
- Instruction-root packaging completeness and release integrity beyond protection behavior. `DEL-08-01` and release verification deliverables cover packaging conformance.

## Terminology

Use these terms consistently in implementation notes and tests:

| Term | Meaning | Source |
|---|---|---|
| Working root | User-selected local filesystem root for mutable project execution state. | `docs/TYPES.md` Section 1.6; `docs/SPEC.md` Section 1.2 |
| `projectRoot` / active project root | Normalized runtime representation of the accepted working root. | `docs/TYPES.md` Section 1.6; `docs/SPEC.md` API/session sections |
| Instruction root | Release-managed app resource tree that ordinary execution must not mutate. | `docs/TYPES.md` Section 1.5; `docs/SPEC.md` Section 1.1 |
| Path containment | Policy that resolves tool/write paths against the active project root and rejects escapes. | `docs/CONTRACT.md` K-PATH-2; `docs/PRD.md` FR-050 |

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-07-01-001 | The working-root validator MUST reject non-absolute paths before a root is used for project execution. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2 |
| REQ-07-01-002 | The working-root validator MUST reject missing paths, non-directory paths, and paths the app cannot read and write. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2 |
| REQ-07-01-003 | The working-root validator MUST reject any working root inside the active instruction root. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` Section 1.2; `docs/CONTRACT.md` K-ROOT-1 |
| REQ-07-01-004 | Ordinary project execution MUST NOT mutate the instruction root. | `docs/DIRECTIVE.md` Section 2.7; `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
| REQ-07-01-005 | Runtime write/edit/tool paths MUST be resolved against the active project root and rejected when outside the allowed root. | `docs/PRD.md` FR-050, FR-097; `docs/CONTRACT.md` K-PATH-2 |
| REQ-07-01-006 | Writes under the instruction root MUST be blocked even when an SDK or developer-local permission mode would otherwise allow execution. | `docs/PRD.md` FR-051; `docs/TYPES.md` Section 8.2; `docs/PRD.md` permission mapping table |
| REQ-07-01-007 | Initial write policy MUST reject symlink writes unless a governed amendment and tests approve relaxation. | `docs/CONTRACT.md` K-PATH-3; `docs/SPEC.md` Section 15.2 |
| REQ-07-01-008 | Hook failures for write, shell, domain, and subagent actions MUST fail closed when they are part of path or instruction-root enforcement. | `docs/CONTRACT.md` K-HOOK-1 |
| REQ-07-01-009 | Path containment and instruction-root protection MUST be implemented in runtime code, hooks, and policy helpers, not only prompt text. | `docs/DIRECTIVE.md` Section 2.9; `docs/PRD.md` Section 3 |
| REQ-07-01-010 | Tests MUST cover valid and invalid working roots, instruction-root-contained roots, outside-project tool paths, instruction-root write attempts, and symlink write attempts. | `docs/PRD.md` FR-003, FR-050, FR-051, FR-095, FR-097 |
| REQ-07-01-011 | ASSUMPTION: The implementation should expose the validation behavior through `/api/working-root/validate` and reuse the same normalized root for tree, scan, chat session, scaffold, and contract APIs. | `docs/PRD.md` Section 7.1; `docs/SPEC.md` API endpoints table |

## Standards

| Standard or Contract | Applicability | Source |
|---|---|---|
| Chirality root separation contract | Governs instruction-root and working-root separation. | `docs/CONTRACT.md` Section 1.3 |
| Chirality filesystem/path contract | Governs working-root containment and symlink write policy. | `docs/CONTRACT.md` K-PATH-2, K-PATH-3 |
| Chirality hook contract | Governs fail-closed hook behavior and required containment/protection hooks. | `docs/CONTRACT.md` K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| Chirality API contract | Provides working-root validation and deliverable filesystem API surfaces. | `docs/SPEC.md` API endpoints table |
| Product requirements | Establish P0/P1 acceptance for validation, containment, instruction-root protection, and safe writes. | `docs/PRD.md` Sections 7.1, 8.9, 8.15; REF-006 HASH_MISMATCH warning applies |

## Verification

| Requirement IDs | Verification Approach | Evidence Record |
|---|---|---|
| REQ-07-01-001, REQ-07-01-002 | Unit tests for root validation input cases: relative path, missing path, file path, unreadable path, unwritable path, and valid directory. | Root validation test output; fixture list. |
| REQ-07-01-003, REQ-07-01-004, REQ-07-01-006 | Unit or integration tests with an instruction-root fixture and nested working-root/write-attempt cases. | Instruction-root protection fixture output. |
| REQ-07-01-005 | Unit tests for path helper resolution of project-relative, absolute-inside, absolute-outside, traversal, and normalized equivalent paths. | Path policy helper test output. |
| REQ-07-01-007 | Unit tests using symlink fixtures for write target rejection. | Symlink policy fixture output. |
| REQ-07-01-008, REQ-07-01-009 | Integration tests proving hooks fail closed and policy denials override permissive modes. | Hook failure triage and permission decision records. |
| REQ-07-01-010 | Test matrix review against required acceptance cases. | Coverage checklist stored with test fixtures. |
| REQ-07-01-011 | API test for `/api/working-root/validate` response shape and downstream normalized-root reuse. | API test output; ASSUMPTION remains pending until implementation design confirms reuse path. |
| REQ-07-01-001 through REQ-07-01-011 | Source-state review confirms PRD-dependent acceptance remains warning-bearing until REF-006 hash mismatch is accepted, corrected, or bypassed by explicit human ruling. | Review note or run record naming `_REFERENCES.md` REF-006 disposition. |

## Documentation

Required artifacts for this deliverable:

- Root validation tests.
- Path policy helpers.
- Instruction-root protection fixtures.
- Test coverage notes mapping fixtures to SOW-002 and SOW-027.
- Source-state note that `docs/PRD.md` was available but marked `HASH_MISMATCH` in `_REFERENCES.md`.

Documentation gaps:

- Code module names and final helper/API locations are TBD.
- Endpoint reuse through `/api/working-root/validate` and downstream normalized-root consumers remains an ASSUMPTION until implementation design confirms the concrete path.
- Final test command names and evidence record locations for root validation, path policy, instruction-root protection, hook failure, symlink fixtures, and PRD source-state review are TBD.
- Responsible party is TBD and must not be assigned without human action.

## Pass 3 Semantic Lensing Notes

| ItemID | Specification Disposition | Evidence |
|---|---|---|
| A-001 | converted to TBD | Documentation gaps explicitly retain unknown code module names, helper/API locations, and test file names rather than inventing implementation paths. |
| C-001 | already covered | `Standards`, `Verification`, and `Documentation` preserve the PRD HASH_MISMATCH warning as review-aware source state. |
| F-001 | incorporated | `Terminology` normalizes working root, `projectRoot` / active project root, instruction root, and path containment vocabulary for implementation use. |
| D-001 | converted to TBD | REQ-07-01-011 remains labeled ASSUMPTION and verification requires implementation confirmation of endpoint reuse. |
