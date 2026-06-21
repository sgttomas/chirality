# Evidence - ADQ-07 Document-Kit Metadata Scanner

Date: 2026-06-21

## Scope

This evidence records the ADQ-07 implementation of G2 deliverable metadata and document-kit scanning
for DEL-07-03. It covers read-only contract findings for required metadata, PREPARATION baseline
files, four-document kit files, canonical memory, prohibited `_MEMORY.md`, optional files, and
source-state warnings.

This evidence does not perform lifecycle transitions, satisfy dependency rows, issue deliverables,
change provider policy, or make release, professional, certification, sealing, authentication, or
code-compliance claims.

## Implemented Evidence

| Evidence Area | Artifact |
|---|---|
| Deliverable contract scanner | `frontend/src/lib/workspace/filesystem.ts` |
| Required metadata findings | `scanDeliverableDocumentKitContract` emits `required_metadata` / `missing_required_metadata` |
| PREPARATION baseline warning | `scanDeliverableDocumentKitContract` emits `preparation_baseline` / `missing_preparation_baseline` for `_SEMANTIC.md` |
| Four-document kit warnings | `scanDeliverableDocumentKitContract` emits `document_kit` / `missing_document_kit_file` |
| Canonical memory visibility | `scanDeliverableDocumentKitContract` emits `canonical_memory_present` or `canonical_memory_absent` info findings |
| Prohibited memory rejection | `scanDeliverableDocumentKitContract` emits `prohibited_file` / `prohibited_memory_file` for `_MEMORY.md` |
| Optional file recognition | Scanner result exposes optional states for `Dependencies.csv`, `_SEMANTIC_LENSING.md`, and `HASH_VERIFICATION_BYPASS.jsonl` |
| Source-state warning propagation | Scanner emits `source_hash_warning` and `unknown_unsupported_condition` findings from `_REFERENCES.md` and bypass records |
| API-consumable output | `/api/project/deliverables` now returns additive `deliverableContracts` scan results without changing the existing `deliverables` roster shape |

## Validation

| Command | Result |
|---|---|
| `npm run test -- src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts src/__tests__/api/project/deliverables-route.test.ts` | PASS: 6 tests |
| `npm run test` | PASS: 72 test files / 507 tests |
| `npm run typecheck` | PASS |
| `git diff --check` | PASS |
| `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` | PASS: no drift |

## Residuals

- Lifecycle-conditioned severity mapping for document-kit absence remains conservative: missing kit
  files currently emit warnings rather than human-gated closure decisions.
- The scanner exposes contract findings through `/api/project/deliverables`; UI presentation remains
  downstream work.
- This evidence does not close DEL-07-03 lifecycle state or dependency rows.
