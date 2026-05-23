# Specification: DEL-07-03 Deliverable Metadata and Document Kit Contracts

## Scope

This deliverable covers backend support for scanning and validating deliverable-local filesystem contracts in PKG-07. The covered contracts are deliverable metadata files, canonical memory, semantic placeholders, and four-document kit buckets. Sources: `_CONTEXT.md` / Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / DEL-07-03 row.

In scope:

- Detect and validate deliverable metadata files against SPEC/PRD file inventory expectations.
- Detect the four-document kit as first-class knowledge buckets.
- Validate canonical memory behavior by accepting `MEMORY.md` and rejecting `_MEMORY.md` for this project profile.
- Recognize semantic baseline and optional semantic lens files.
- Provide test coverage for metadata scanners, document kit detection, and `_MEMORY.md` rejection.

Out of scope:

- UI presentation except scope scan results, per package exclusion. Source: `_CONTEXT.md` / Package Scope.
- Status transition enforcement beyond the file-contract checks in this deliverable; that is covered by DEL-07-04. Source: decomposition / PKG-07 rows.
- Dependency register read/write/lint behavior beyond recognizing optional `Dependencies.csv`; that is covered by DEL-07-05. Source: decomposition / PKG-07 rows.
- Human approval, checking, or issued-state authorization. Agents must not author binding approvals. Source: `docs/CONTRACT.md` / K-AUTH-1 and K-GATE-1.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-07-03-REQ-001 | The scanner shall identify deliverable folders by the valid `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` structure and the presence of `_STATUS.md`. | `docs/PRD.md` / FR-047; `docs/SPEC.md` / Section 3 | Unit tests with valid and invalid folder names and missing `_STATUS.md` fixtures |
| DEL-07-03-REQ-002 | The validator shall require `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md` as canonical metadata files for deliverable folders. | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 | Metadata scanner tests for complete and incomplete metadata sets |
| DEL-07-03-REQ-003 | The validator shall recognize `_SEMANTIC.md` as part of the minimum PREPARATION fileset. | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 | Fixture with missing `_SEMANTIC.md` reports the expected baseline warning or failure state; exact severity TBD |
| DEL-07-03-REQ-004 | The validator shall detect the document kit files `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as first-class knowledge buckets. | `docs/PRD.md` / FR-049 and Section 10.8; `docs/SPEC.md` / Section 3.1 | Document kit detection tests for all-present, partially-present, and absent kit states |
| DEL-07-03-REQ-005 | The validator shall treat `MEMORY.md` as the canonical deliverable-local working memory file when present. | `docs/SPEC.md` / Section 5.4; `docs/PRD.md` / Section 10.8 | Fixture asserting `MEMORY.md` is accepted as canonical memory |
| DEL-07-03-REQ-006 | The validator shall reject `_MEMORY.md` in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | `_MEMORY.md` rejection tests |
| DEL-07-03-REQ-007 | The validator shall recognize `_SEMANTIC_LENSING.md` and `HASH_VERIFICATION_BYPASS.jsonl` as optional deliverable-local files, not required PREPARATION files. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Fixture showing optional files do not make a valid folder invalid when absent |
| DEL-07-03-REQ-008 | The implementation shall preserve working-root containment and must not mutate the instruction root during ordinary project execution. | `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3; `docs/PRD.md` / FR-050 and FR-051 | Path containment tests; instruction-root protection fixtures where this scanner accepts paths |
| DEL-07-03-REQ-009 | Validation output shall surface source/hash warnings and unsupported or unknown conditions instead of silently treating them as accepted truth. | `docs/DIRECTIVE.md` / Section 2.5; `docs/CONTRACT.md` / K-CONFLICT-1; `_REFERENCES.md` / REF-006 | Fixture or unit test for reference warning reporting; exact output schema TBD |
| DEL-07-03-REQ-010 | ASSUMPTION: Scanner outputs should be consumable by `/api/working-root/scope` or adjacent working-root/project APIs without changing their public route shapes. | `docs/SPEC.md` / Section 17.2; `docs/PLAN.md` / current baseline; decomposition / DEL-07-03 anticipated artifacts | Integration test TBD after implementation location is selected |

## Scanner Finding Contract (P3)

This section records the Pass 3 contract shape needed for later implementation without selecting concrete files, public route changes, or final enum names. It responds to B-001, F-001, F-002, X-001, X-002, E-001, and E-002 from the current `_SEMANTIC_LENSING.md` worklist.

### Finding Categories

| Category | Applies to | Source basis | Severity posture |
|---|---|---|---|
| Required metadata | Missing `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, or `_REFERENCES.md` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Must be reported as invalid or blocking; exact enum name TBD |
| Preparation baseline | Missing `_SEMANTIC.md` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Must be reported as a baseline issue; exact severity TBD |
| Lifecycle-conditioned document kit | Missing `Datasheet.md`, `Specification.md`, `Guidance.md`, or `Procedure.md` | `docs/SPEC.md` / Section 3.1 and Section 4.2; `docs/PRD.md` / FR-049 | Warning or failure depends on lifecycle state; exact state-to-severity map TBD |
| Canonical memory | Present or missing `MEMORY.md` | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | Should be visible in output; exact requiredness TBD |
| Prohibited memory | Present `_MEMORY.md` | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 | Must be reported as prohibited for this profile |
| Optional files | Present or absent `Dependencies.csv`, `_SEMANTIC_LENSING.md`, or `HASH_VERIFICATION_BYPASS.jsonl` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 | Absence must not invalidate a folder solely by itself |
| Source/hash warning | Reference hash mismatch, bypass record, or unsupported source state | `_REFERENCES.md` / REF-006; `docs/CONTRACT.md` / K-CONFLICT-1 | Must remain visible as warning evidence |
| Unknown unsupported condition | File or state condition not covered by the accepted contract | `docs/CONTRACT.md` / K-INVENT-1 and K-CONFLICT-1 | Must surface as unknown/TBD, not silently accepted |

### Minimum Result Fields

Until an implementation-specific schema is accepted, scanner findings should preserve at least: `deliverableId`, `path`, `category`, `condition`, `lifecycleState`, `severity`, `sourceRef`, `evidence`, and `message`. The exact TypeScript type, API response shape, and persisted test fixture names remain TBD. If the scanner output is exposed through `/api/working-root/scope` or `/api/project/deliverables`, route shape compatibility must be proven by implementation tests rather than assumed from this document.

## Standards

| Standard or governing source | Applicability | Location |
|---|---|---|
| `docs/SPEC.md` | Primary physical file-layout, lifecycle, and deliverable-local contract source | Sections 3, 4, 5, 17.2 |
| `docs/PRD.md` | Product requirements for filesystem execution and deliverable folder layout | Sections 8.8, 8.9, 10.8; HASH_MISMATCH warning per `_REFERENCES.md` |
| `docs/TYPES.md` | Vocabulary for deliverables, artifacts, lifecycle states, and dependency classes | Sections 1.2, 1.3, lifecycle state table |
| `docs/CONTRACT.md` | Governance invariants for roots, authority, hidden truth, and conflicts | K-AUTH, K-ROOT, K-CONFLICT |
| `docs/DIRECTIVE.md` | Evidence posture, no hidden memory, root separation, provider-neutral governance | Sections 2.5, 2.6, 2.7 |
| `docs/PLAN.md` | Roadmap and local source policy | Control-Plane Boundary; Local Source Policy; PKG-07 roadmap |

## Verification

| Verification item | Required evidence | Related requirements |
|---|---|---|
| Metadata scanner fixtures | Passing tests for required metadata files, missing metadata files, and valid/invalid deliverable folder identities | REQ-001, REQ-002 |
| Semantic placeholder fixtures | Test or documented validator behavior for `_SEMANTIC.md` baseline and optional `_SEMANTIC_LENSING.md` | REQ-003, REQ-007 |
| Document kit detection fixtures | Passing tests for complete, partial, and absent four-document kits | REQ-004 |
| Memory contract fixtures | Passing test accepting `MEMORY.md` and rejecting `_MEMORY.md` | REQ-005, REQ-006 |
| Path/root governance fixtures | Tests showing project-root containment and instruction-root write protection are preserved where this code handles paths | REQ-008 |
| Warning propagation | Test or review evidence that reference hash warnings and unknowns remain visible | REQ-009 |
| API compatibility | Integration or route-level evidence once implementation binding is selected | REQ-010 |

### P3 Verification Additions

| Verification target | Required evidence before closure | Disposition |
|---|---|---|
| B-001 normalized categories and severity names | Test fixture expectations must use one category/severity vocabulary for required, baseline, recommended, optional, prohibited, warning, and unknown findings. | Converted to explicit TBD contract above |
| F-001 / E-001 scanner output schema | Accepted implementation type or schema and fixtures covering all finding categories. | Converted to minimum result fields; final schema TBD |
| F-002 severity behavior | Fixtures for missing `_SEMANTIC.md`, initialized missing document-kit files, optional-file absence, `_MEMORY.md`, and source/hash warnings. | Converted to required verification evidence |
| X-001 concrete tests | Passing test names, fixture paths, and command outputs from the implementation slice. | Deferred as closure evidence; exact paths/commands TBD |
| X-002 warning propagation | Test or review evidence preserving REF-006 HASH_MISMATCH and unknown unsupported conditions. | Converted to required verification evidence |
| E-002 API consumer contract | Integration evidence for `/api/working-root/scope` or an accepted adjacent API, if scanner output is exposed there. | Reframed as assumption pending implementation proof |

## Documentation

Required or expected artifacts for closure:

- Metadata scanner implementation.
- Document kit detection implementation.
- `_MEMORY.md` rejection tests.
- Test fixtures covering valid, incomplete, optional, and prohibited deliverable-local files.
- Documentation or inline contract comments for scanner output severity (`TBD` until implementation schema is selected).
- Evidence that `docs/PRD.md` HASH_MISMATCH was treated as a source warning for this drafting run.
