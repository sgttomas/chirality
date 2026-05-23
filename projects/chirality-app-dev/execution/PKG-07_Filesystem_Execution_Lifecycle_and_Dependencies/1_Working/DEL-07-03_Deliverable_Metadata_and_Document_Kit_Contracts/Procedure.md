# Procedure: DEL-07-03 Deliverable Metadata and Document Kit Contracts

## Purpose

Define the working procedure for producing and verifying the DEL-07-03 backend feature slice: scanner/validator support for deliverable metadata files, canonical memory, semantic placeholders, and four-document kit buckets. Sources: `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row.

## Prerequisites

| Prerequisite | Status or source |
|---|---|
| Accepted decomposition entry for DEL-07-03 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / DEL-07-03 row |
| Governing file layout and lifecycle contract | `docs/SPEC.md` / Sections 3, 4, 5 |
| Product requirements for filesystem execution model | `docs/PRD.md` / Sections 8.8, 8.9, 10.8; HASH_MISMATCH warning in `_REFERENCES.md` |
| Vocabulary for deliverables, artifacts, and lifecycle states | `docs/TYPES.md` / Sections 1.2, 1.3, lifecycle state table |
| Governance posture for roots, memory, evidence, and conflicts | `docs/DIRECTIVE.md` / Sections 2.5, 2.6, 2.7; `docs/CONTRACT.md` / K-ROOT, K-CONFLICT |
| Declared upstream dependencies | TBD - no accepted dependency edges have been extracted yet. Source: `_DEPENDENCIES.md` / Declared Upstream |
| Implementation location | TBD |
| Scanner output schema | TBD |

## Steps

1. Confirm scope and source contracts.
   - Read DEL-07-03 context, references, and decomposition row.
   - Carry the `docs/PRD.md` HASH_MISMATCH as a warning until the reference record is corrected or a human-approved bypass exists.

2. Define fixture cases.
   - Include valid `OPEN` baseline, initialized four-doc kit, missing metadata file, missing recommended document kit file, prohibited `_MEMORY.md`, optional `_SEMANTIC_LENSING.md` absence, and optional `HASH_VERIFICATION_BYPASS.jsonl` presence.
   - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.

3. Implement or update deliverable folder detection.
   - Detect `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` deliverable folders with `_STATUS.md`.
   - Keep path handling within working-root containment.
   - Source basis: `docs/PRD.md` / FR-047 and FR-050.

4. Implement metadata file validation.
   - Require `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, and `_REFERENCES.md`.
   - Recognize `_SEMANTIC.md` as part of the minimum PREPARATION fileset.
   - Distinguish required, recommended, optional, and prohibited files in output.
   - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / FR-048 and Section 10.8.

5. Implement document kit detection.
   - Detect `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as document kit buckets.
   - Tie missing-kit findings to lifecycle state where available: missing kit in `OPEN` differs from missing kit after `INITIALIZED`.
   - Source basis: `docs/SPEC.md` / Section 3.1 and Section 4.2; `docs/PRD.md` / FR-049.

6. Implement memory contract checks.
   - Accept `MEMORY.md` as canonical when present.
   - Reject or flag `_MEMORY.md` as prohibited for this project profile.
   - Source basis: `docs/SPEC.md` / Section 3.1 and Section 5.4.

7. Implement semantic placeholder checks.
   - Recognize `_SEMANTIC.md` as baseline.
   - Recognize `_SEMANTIC_LENSING.md` as optional.
   - Source basis: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.

8. Preserve responsibility boundaries.
   - Do not implement lifecycle transition authorization in this slice except as read/report behavior; DEL-07-04 owns transitions.
   - Do not implement `Dependencies.csv` parser/writer behavior beyond optional-file recognition; DEL-07-05 owns dependency register behavior.
   - Source basis: decomposition / PKG-07 deliverable rows.

9. Add tests and run verification.
   - Add metadata scanner tests, document kit detection tests, and `_MEMORY.md` rejection tests.
   - Add path/root containment fixtures if this code accepts filesystem paths.
   - Exact test command is TBD until implementation location is selected.

## Verification

| Check | Expected result |
|---|---|
| Required metadata files complete | Validator reports required metadata present |
| Required metadata file missing | Validator reports missing canonical metadata file |
| `_SEMANTIC.md` missing from PREPARATION baseline | Validator reports baseline semantic placeholder issue; severity TBD |
| Four document kit complete | Validator detects all four knowledge buckets |
| Four document kit partial | Validator reports missing bucket names |
| `MEMORY.md` present | Validator accepts canonical memory file |
| `_MEMORY.md` present | Validator rejects or flags prohibited file |
| `_SEMANTIC_LENSING.md` absent | Validator does not fail solely for optional absence |
| PRD hash mismatch present in references | Output/report preserves source warning |
| Instruction-root path supplied to write-capable path handling | Write operation is blocked or not available from this slice |

## Records

Maintain the following records for closure:

- Source references and hash warning notes used by implementation.
- Scanner/validator implementation diff.
- Fixture list and test results.
- Any unresolved `TBD` values from this procedure, especially implementation location, scanner output schema, and severity policy.
- Evidence that `_MEMORY.md` rejection was tested.
