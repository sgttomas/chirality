# ORN-08 Runtime Error Taxonomy Ownership Evidence

**Date:** 2026-07-10
**Status:** Implementation reconciliation evidence

## Finding

The typed harness error taxonomy has a current product-owned canonical surface. It is not owned by the
API-key settings component and does not require a new cross-package type:

- `frontend/packages/harness-contract/src/types.ts` exports `HarnessErrorType` and
  `HarnessErrorResponse`; this is the public harness-contract seam.
- `frontend/packages/harness-contract/src/errors.ts` owns `HarnessError`, validation of known error
  types, and fail-closed normalization of unknown failures to `SDK_FAILURE`.
- `frontend/src/lib/harness/http.ts` serializes that contract at API boundaries.
- PKG-03 runtime code (`turn-engine.ts`, `session-manager.ts`) selects product/runtime error types and
  terminal outcomes.
- PKG-04 adapter code (`anthropic-agent-sdk-manager.ts`, `sdk-message-mapper.ts`) maps and redacts
  provider/SDK failures into product-owned errors and terminal event metadata.
- PKG-05 session/event storage persists the resulting product-owned event records; it does not define
  the public error enum.
- DEL-02-05 UI code (`error-display.ts`) consumes `HarnessErrorType` and maps selected codes to
  actionable copy, retaining a typed fallback for unmapped codes.

## Disposition

DEL-02-05 consumes the canonical `@chirality/harness-contract` error type and may add presentation copy
without redefining runtime taxonomy. Provider-native names and messages remain adapter metadata and are
subject to the existing redaction boundary.

This evidence resolves the ownership question in DEL-02-05 R10 against current implementation truth.
It does not mutate or satisfy `Dependencies.csv`, change the public error union, issue the deliverable,
or make a release-readiness or professional claim. Dependency-row reconciliation remains outside the
inspection-orphan queue as recorded in its exclusions.

## Verification pointers

- `frontend/src/__tests__/lib/harness-error-display.test.ts`
- `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`
- `frontend/src/__tests__/api/harness/routes.test.ts`
- `frontend/src/__tests__/lib/sdk-message-mapper.test.ts`
