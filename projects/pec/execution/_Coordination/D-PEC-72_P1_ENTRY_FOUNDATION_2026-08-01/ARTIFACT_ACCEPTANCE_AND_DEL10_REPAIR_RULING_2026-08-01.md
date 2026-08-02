# D-PEC-72 artifact acceptance and DEL-10-01 repair ruling

**Status:** RULED — EXACT THREE-ACT APPROVAL

**Date:** 2026-08-01

**Owner:** Ryan Tufts

## Owner approval

The owner ruled as follows, reproduced verbatim in full:

```text
APPROVE:

1. DEL-00-01 AC-007 — ACCEPT.

I accept artifacts/v2/ADRs.md at SHA-256
f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5
as fit for DEL-00-01. I confirm ports-and-adapters / hexagonal
isolation as PEC v2’s selected core-isolation style and confirm
that no governed act depends on PEC-held state.

This accepts these artifact bytes only. It does not advance
DEL-00-01 to ISSUED, close C-05, authorize P1, or impose this
architecture on another loop.

2. DEL-00-03 AC-011 — ACCEPT.

I accept artifacts/v2/SPEC.md at SHA-256
8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315
as the PEC v2 SPEC of record born from PRD v2.2 and accepted
SOFTWARE_DECOMP revision 1.3 at 11a494e9a.

I confirm the single-objective attribution to OBJ-001 with its
recorded LOW-confidence qualification; the full-objective-set and
OBJ-006 alternatives remain considered but unadopted.

This accepts these artifact bytes only. It does not advance
DEL-00-03 to ISSUED, close C-05, or authorize P1.

3. DEL-10-01 RF-001 — REVISE.

Authorize WORKING_ITEMS to normalize only present-tense candidate,
REVIEW-pending, and acceptance-pending status prose in
artifacts/STEP0_COST_BASELINE_METHOD.md and
artifacts/STEP0_COST_BASELINE.md into acceptance-neutral authority
prose.

Do not change the measurement method, values, telemetry,
classification, criteria, citations, scope, lifecycle, C-05, or
P1 state. Rerun SELF_CHECK against the resulting hashes.

This disposition and repair authorization do not accept DEL-10-01
or advance its lifecycle.
```

## Authorized effects and fences

1. `DEL-00-01` AC-007 accepts only
   `artifacts/v2/ADRs.md` at SHA-256
   `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`.
   It confirms the selected PEC v2 isolation style and graceful-absence
   boundary. It does not advance lifecycle, close C-05, open P1, or bind
   another loop.
2. `DEL-00-03` AC-011 accepts only
   `artifacts/v2/SPEC.md` at SHA-256
   `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`.
   It confirms the retained LOW-confidence `OBJ-001` attribution and leaves
   the named alternatives unadopted. It does not advance lifecycle, close
   C-05, or open P1.
3. `DEL-10-01` RF-001 is dispositioned `REVISE`. The authorized repair is
   limited to acceptance-neutral normalization of present-tense candidate,
   REVIEW-pending, and acceptance-pending status prose in
   `artifacts/STEP0_COST_BASELINE_METHOD.md` and
   `artifacts/STEP0_COST_BASELINE.md`. Measurement method, values, telemetry,
   classification, criteria, citations, scope, lifecycle, C-05, and P1 state
   may not change. SELF_CHECK must rerun against the resulting hashes. This
   ruling does not accept DEL-10-01 or advance its lifecycle.

No other artifact, finding, lifecycle transition, C-05 disposition, P1 act,
implementation, release, or cross-loop architecture mandate is authorized.
