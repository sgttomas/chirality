# Guidance: DEL-07-03 Deliverable Metadata and Document Kit Contracts

## Purpose

DEL-07-03 exists to make deliverable-local filesystem contracts machine-readable and testable. It turns the SPEC/PRD deliverable folder contract into backend scanner and validator behavior for metadata files, document kit buckets, canonical memory, and semantic placeholders. Sources: `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row; `docs/PRD.md` / FR-047 through FR-049.

## Principles

1. Preserve filesystem truth.
   - The working root is the mutable project-truth location; instruction-root mutation is outside ordinary execution. Source: `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3.

2. Prefer explicit file contracts over inference.
   - Required metadata files, document kit files, optional files, and prohibited `_MEMORY.md` are named in SPEC/PRD. Scanner behavior should reflect those named contracts before adding heuristics. Source: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.

3. Keep lifecycle meaning separate from file presence.
   - `OPEN` means the minimum viable fileset exists; `INITIALIZED` means the document kit has been drafted or initialized. The scanner can report presence and state, but DEL-07-04 owns transition enforcement. Source: `docs/SPEC.md` / Section 4.2 and Section 4.3; decomposition / DEL-07-04 row.

4. Treat memory strictly.
   - `MEMORY.md` is canonical deliverable-local working memory; `_MEMORY.md` is disabled in this project profile. A permissive fallback to `_MEMORY.md` would contradict the source contract. Source: `docs/SPEC.md` / Section 5.4; `docs/PRD.md` / Section 10.8.

5. Surface uncertainty.
   - Hash mismatches, missing files, unsupported optional states, and unknown severity choices should remain visible as warnings, `TBD`, assumptions, or conflicts rather than being normalized away. Source: `docs/DIRECTIVE.md` / Section 2.5; `docs/CONTRACT.md` / K-CONFLICT-1.

## Considerations

- Severity policy is partly source-defined and partly implementation-defined. Required metadata files are clearly required, document kit files are "SHOULD when initialized", and optional files are not required. Exact scanner severity levels are TBD until the implementation schema is selected. Sources: `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8.
- `docs/PRD.md` is an authoritative local source for requirements, but `_REFERENCES.md` records a HASH_MISMATCH for REF-006. Use PRD requirements with the warning attached until a human updates or bypasses the hash record. Source: `_REFERENCES.md` / REF-006; `docs/SPEC.md` / Section 5.3.
- The deliverable should not absorb sibling package responsibilities. Status transition authorization belongs to DEL-07-04; dependency register parsing and writing belongs to DEL-07-05. Source: decomposition / PKG-07 rows.
- If scanner results feed `/api/working-root/scope` or `/api/project/deliverables`, keep route shapes stable unless the implementation task explicitly includes API contract changes. Source: `docs/SPEC.md` / Section 17.2; `docs/PLAN.md` / Current Baseline.
- ASSUMPTION: The scanner should return structured findings that distinguish missing required files, missing recommended files, optional-file absence, prohibited-file presence, and source/hash warnings. This follows the source contracts but the exact data model is TBD.
- Pass 3 normalization keeps the distinction between source-backed categories and implementation-selected enum names. B-001 is addressed by using required metadata, preparation baseline, lifecycle-conditioned document kit, canonical memory, prohibited memory, optional files, source/hash warning, and unknown unsupported condition as the working vocabulary; final enum names remain TBD until implementation.
- C-001 is not locally resolvable in this deliverable. REF-006 remains a HASH_MISMATCH in `_REFERENCES.md`, so PRD-derived rows stay warning-qualified until a human or source-state owner accepts, corrects, or bypasses that reference state.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Strict failure vs warning for missing document kit files | Treat missing document kit files as a condition tied to lifecycle state: expected when initialized, not necessarily invalid for `OPEN`. Exact severity TBD. | `docs/SPEC.md` / Section 3.1 and Section 4.2 |
| Required vs optional semantic files | `_SEMANTIC.md` is part of the minimum PREPARATION fileset; `_SEMANTIC_LENSING.md` is optional. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
| Memory compatibility vs project profile | Do not add compatibility support for `_MEMORY.md`; reject it for this profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4 |
| Scanner ownership vs lifecycle ownership | Scanner may report state and file presence; lifecycle transition logic stays with the status API/tool slice. | `docs/SPEC.md` / Section 4.3; decomposition / DEL-07-04 |
| Local requirements vs hash warning | Use local PRD content as requested source material but carry the HASH_MISMATCH warning in output evidence. | `_REFERENCES.md` / REF-006 |

## P3 Disposition Guidance

| Item | Guidance disposition |
|---|---|
| A-001 | Rejected for this P3 text pass as an implementation binding: implementation location and owning backend surface remain TBD until the implementation slice selects files. |
| B-001 | Incorporated as normalized category vocabulary, with exact enum names and severity levels still TBD. |
| C-001 | Surfaced as a source-state blocker: REF-006 HASH_MISMATCH remains warning-qualified and requires owner action outside this deliverable. |
| D-001 | Converted to closure evidence requirements for implementation files, fixtures, and commands; exact paths remain TBD. |
| D-002 | Reconciled as current-state language: extracted ACTIVE rows exist, while declared upstream/downstream dependency sections remain unaccepted/TBD. |
| F-001 | Incorporated as minimum result-field guidance; final scanner schema remains TBD. |
| F-002 | Converted to fixture/severity evidence requirements. |
| X-001 | Converted to required implementation test evidence. |
| X-002 | Converted to warning-propagation test evidence. |
| E-001 | Incorporated with F-001 as the minimum scanner result model. |
| E-002 | Reframed as an API compatibility assumption requiring implementation proof before closure. |

## Examples

| Scenario | Expected scanner/validator disposition | Source |
|---|---|---|
| Deliverable folder has `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `_SEMANTIC.md`, but no document kit, and status is `OPEN` | Valid PREPARATION baseline; document kit not yet initialized. | `docs/SPEC.md` / Section 3.1 and Section 4.2 |
| Deliverable folder has status `INITIALIZED` but is missing `Specification.md` | Report missing document kit bucket. Exact severity TBD. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / FR-049 |
| Deliverable folder contains `_MEMORY.md` | Reject or flag as prohibited for this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4 |
| Deliverable folder lacks `_SEMANTIC_LENSING.md` | Do not fail solely for that absence; it is optional. | `docs/SPEC.md` / Section 3.1 |

## Source Warning Notes

No source-content conflicts requiring human ruling were identified in Pass 1/2. Source warning: `docs/PRD.md` is listed as HASH_MISMATCH in `_REFERENCES.md` and should be reconciled by the owning workflow.
