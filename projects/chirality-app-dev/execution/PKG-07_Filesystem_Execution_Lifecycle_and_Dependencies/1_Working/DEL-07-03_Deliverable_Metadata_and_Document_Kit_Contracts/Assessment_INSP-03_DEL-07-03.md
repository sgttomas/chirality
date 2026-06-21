# Assessment INSP-03: DEL-07-03 Deliverable Metadata and Document Kit Contracts

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-07-03 |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `210b5b7427471fc307ecbf6eecaab78ebf08398b` |
| Spec source | `Specification.md` lines 1-101 |

## ADQ-07 Superseding Note - 2026-06-21

ADQ-07 implements the G2 scanner gap recorded below. Current evidence is
`Evidence_ADQ-07_Document_Kit_Metadata_Scanner.md`: `scanDeliverableDocumentKitContract` now emits
read-only findings for required metadata, `_SEMANTIC.md` PREPARATION baseline absence, four-document
kit absence, canonical `MEMORY.md` visibility, prohibited `_MEMORY.md`, optional deliverable-local
files, `_REFERENCES.md` hash/source-state warnings, and unknown/unsupported reference states. The
project deliverables API exposes these results as additive `deliverableContracts` output while
preserving the existing deliverable roster shape. This note does not change lifecycle state, satisfy
dependency rows, or make issuance/release/professional claims.

## Scope

DEL-07-03 covers deliverable-local metadata and document-kit contract scanning: identifying deliverable folders, required metadata files, four-document kit buckets, canonical memory, warning output, and API-consumable scanner results.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-07-03-REQ-001 | PARTIAL | `frontend/src/lib/workspace/filesystem.ts` lines 288-290 and 473-560; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | Deliverable folders are identified by folder/status evidence and exposed through the project deliverables API, but this is not a full contract validator. |
| DEL-07-03-REQ-002 | FAIL | `frontend/src/lib/workspace/filesystem.ts` lines 321-365 and 473-560. | The scanner maps present files to knowledge types; it does not require the canonical metadata set or report incomplete sets. |
| DEL-07-03-REQ-003 | TBD | `Specification.md` lines 24-35. | The spec still requires a baseline file this project no longer needs per owner instruction. No semantic files were read, generated, or validated for this assessment. |
| DEL-07-03-REQ-004 | PARTIAL | `frontend/src/lib/workspace/filesystem.ts` lines 321-365; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | Four-document kit files are classified into knowledge buckets when present, but incomplete/absent kit validation is not implemented. |
| DEL-07-03-REQ-005 | PARTIAL | `frontend/src/lib/workspace/filesystem.ts` lines 87-149 and 321-365; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | `MEMORY.md` is recognized as a knowledge type. Requiredness and canonical-memory validation are not proven. |
| DEL-07-03-REQ-006 | FAIL | `Specification.md` lines 30-31; no rejecting implementation found in inspected scanner paths. | No `_MEMORY.md` rejection path or fixture was found. |
| DEL-07-03-REQ-007 | TBD | `Specification.md` lines 31-32. | Optional semantic-lens behavior was not assessed because the project instruction says semantic files are not needed. |
| DEL-07-03-REQ-008 | PASS | `frontend/src/lib/workspace/filesystem.ts` lines 399-560; `frontend/src/app/api/project/deliverables/route.ts` lines 8-27; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 173-181. | The project deliverables scan stays under the normalized project root and is read-only. |
| DEL-07-03-REQ-009 | FAIL | `frontend/src/lib/workspace/filesystem.ts` lines 473-560; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | Source/hash warnings and unknown unsupported conditions are not surfaced in scanner output. |
| DEL-07-03-REQ-010 | PARTIAL | `frontend/src/app/api/project/deliverables/route.ts` lines 8-27; `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147. | API output is consumable by the project deliverables route, but the full scanner contract is not implemented or fixture-locked. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| G2: deliverable metadata/document-kit validator is not implemented. | High | `frontend/src/lib/workspace/filesystem.ts` lines 321-365 and 473-560. | Add a contract scanner that emits required/optional/prohibited/warning findings without changing existing route shapes unless accepted. |
| Required metadata and document-kit missing-state fixtures are absent. | High | `frontend/src/__tests__/api/project/deliverables-route.test.ts` lines 95-147 covers mapping, not validation findings. | Add complete/partial/absent metadata and document-kit fixtures. |
| Canonical memory policy is only partially represented. | Medium | `frontend/src/lib/workspace/filesystem.ts` lines 87-149. | Add explicit acceptance for `MEMORY.md` and rejection for the disabled underscored variant. |
| Source/hash warnings are not surfaced by scanner output. | Medium | `frontend/src/lib/workspace/filesystem.ts` lines 473-560. | Add warning findings for REF-006 and unknown unsupported conditions. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. G2 remains open as a roadmap/code gap.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Implement a deliverable contract scanner with findings for required metadata, document-kit state, canonical memory, prohibited files, source warnings, and unknown conditions. | code/test | M | FIT | Resolve project-specific minimum metadata set, excluding unneeded semantic files. |
| Add fixtures for complete, incomplete, optional-file, warning, and prohibited-file states. | test | M | FIT | Accepted scanner finding schema. |
| Preserve current API shape or explicitly version any new scanner output. | code/test | S | FIT | Consumer route decision. |

## Issuance-Gate-Process Observations

DEL-07-03 is one of the least complete PKG-07 deliverables. Current code can discover deliverables and classify present files, but it does not yet validate the filesystem contract needed for issuance.
