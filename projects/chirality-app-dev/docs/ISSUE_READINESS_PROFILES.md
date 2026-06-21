# ISSUE-READINESS EVIDENCE PROFILES - Chirality App Dev

**Status:** Draft governance support surface
**Date:** 2026-06-20
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** per-deliverable `CHECKING -> ISSUED` issue-readiness evidence (lifecycle gate), not release publication
**Decision basis:** D-APP-34 (Option B - modify the gate with evidence profiles), D-APP-36 (Option B - UI render-test bar / AMD-01), D-APP-37 (Option A - PKG-10 doc-only profile)

## 1. Purpose

This document codifies the issue-readiness evidence required before a deliverable may be proposed for a
`CHECKING -> ISSUED` transition. It implements the D-APP-34 ruling: keep the human, SHA-bound lifecycle
states (`CHECKING`, `ISSUED`) and add per-class evidence profiles plus an issue-readiness package. It
complements `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and the lifecycle
invariants in `docs/CONTRACT.md` (`K-AUTH-1`, `K-AUTH-2`, `K-GATE-1`) and `docs/SPEC.md`.

Defining these profiles does not issue any deliverable, publish a release, approve lifecycle issuance,
certify professional work, seal or authenticate work product, declare code compliance, or authorize
external distribution. `CHECKING` and `ISSUED` remain non-delegable human gates. `ISSUED` still
requires a fresh human approval SHA bound to the then-current content (not the inspection-entry SHA).

## 2. How a Profile Is Used

1. Every `CHECKING -> ISSUED` proposal selects the applicable profile by deliverable class (Section 3).
2. The proposer assembles the profile's required evidence into an issue-readiness package, extending the
   `Assessment_INSP-03_DEL-XX-YY.md` artifact already in each deliverable folder.
3. A human authority reviews the package and, if accepting, records the `ISSUED` transition with a fresh
   approval SHA bound to the then-current content.
4. Cross-cutting rulings are consumed as already-resolved inputs, not rediscovered per deliverable:
   UI render-test bar (D-APP-36, Section 4), PKG-10 doc-only basis (D-APP-37, Section 5), and
   source-state / reference integrity (D-APP-35 and the reconciliation model under D-APP-38, Section 6).

## 3. Evidence Profiles (D-APP-34 Option B)

| Profile | Applies to | Required evidence before `ISSUED` |
|---|---|---|
| Runtime/source | Runtime, API, MCP, hooks, lifecycle, provider, session, tool, and UI-logic deliverables | Current source/test evidence, focused tests, stale-spec reconciliation, dependency disposition, skipped-check rationale. |
| UI/product | Desktop shell, matrix, sidebar, workbench/pipeline, and visual-interaction deliverables | Runtime/source evidence **plus** the AMD-01 render/browser evidence bar (Section 4). |
| Governance/control | Control-plane, policy, boundary, and documentation deliverables | Source-state caveats resolved or explicitly deferred, dependency rows disposed, stale local-kit wording reconciled, no runtime/release claim. |
| Validation/release | Packaging, CI, security, network, release, and validation deliverables | Current command artifacts, full-suite or scoped-release rationale, packaged/build/security evidence where required. |
| Future-boundary/doc-only | PKG-10 and future fenced-domain documents | Human-ruling basis for doc-only acceptance, explicit non-implementation language, future-amendment blockers preserved, no solver/professional/release claim. |

Mixed-class deliverables assemble the union of applicable profiles. A required evidence item may be
explicitly deferred only with a recorded human rationale.

## 4. UI/Product Render-Test Bar (D-APP-36 / AMD-01)

- UI/product deliverables require **component-level render tests** covering user-facing controls, state,
  and disabled/active behavior.
- Browser/screenshot or browser-level checks are required **only** where layout, viewport, visual
  overlap, or interaction risk is high.
- Logic/API tests remain useful but are **not sufficient by themselves** for UI/product issue readiness.
- Browser E2E is **not** required for every UI/product deliverable.
- Apply this bar when reconciling PKG-02 and UI-facing PKG-08 deliverables.

## 5. Future-Boundary / Doc-Only Profile (D-APP-37)

PKG-10 and future fenced-domain documents use the doc-only acceptance profile: a human-ruling basis for
doc-only acceptance, explicit non-implementation language, preserved future-amendment blockers, and no
solver / professional / release claim. Doc-only acceptance does not activate R7 domain-engine
implementation, protected-path mutation, the OperationProposal runtime workflow, or solver integration;
those remain behind a separate governed amendment.

## 6. Source-State and Reference Integrity

A deliverable's authority-doc references (`DIRECTIVE`/`CONTRACT`/`SPEC`/`TYPES`/`PLAN`/`PRD` and the
external decomposition reference) must be reconciled to the current corpus version before issue. The
reference-integrity model is **D-APP-38 Option D (hybrid)**: the tool
`execution/_Reconciliation/References/reconcile_authority_corpus.py` recomputes authority-doc hashes
against versioned snapshots in `AUTHORITY_CORPUS.json`. Corpus `v1` was established 2026-06-20 and all
deliverable authority-doc references were reconciled to it (0 `HASH_MISMATCH`); this also executed the
D-APP-35 PRD refresh as a special case. Authority-doc edits are permitted and trigger a corpus version
bump (`bump`), after which `apply` re-reconciles deliverables; until a deliverable is re-reconciled, its
per-row `ExpectedSHA256` keeps it bound to its prior corpus version so drift stays visible (`audit`). A
deliverable is issue-ready on reference grounds only when `audit` shows it reconciled to the current
corpus version, or a deferral is recorded.

## 7. Boundaries

- This document authorizes no `CHECKING -> ISSUED` transition.
- It does not approve release readiness, publication, certification, sealing, authentication,
  code-compliance acceptance, professional approval, provider expansion, or domain-engine activation.
- It does not change any deliverable's current lifecycle state.
- All `docs/PLAN.md` Section 11 fences and the CONTRACT **K-ENGINE-6** strategic posture remain in force.

## 8. Status

Draft governance support surface, activated as the issue-readiness evidence basis per D-APP-34, D-APP-36,
and D-APP-37. `ISSUED` transitions remain deferred until a deliverable's profile package is assembled and
a human records a fresh approval SHA bound to the then-current content.
