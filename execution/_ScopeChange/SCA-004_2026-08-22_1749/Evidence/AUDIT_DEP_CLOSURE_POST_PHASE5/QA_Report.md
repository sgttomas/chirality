# QA report — post-Phase-5 dependency closure

## Coverage and schema

- Live applied register: 53 unique deliverables in six packages; exact graph parity.
- Authoritative Root source: eight current `_DEPENDENCIES.md` containers at their accepted Phase-3 identities.
- Parsed declarations: 16 reciprocal/local rows, deduplicated to nine Root relationships; every declaration retains grounding evidence.
- Legacy coverage: 45 containers remain `NOT_RUN_YET`; this is the same bounded warning as Phase 3, not an unresolved violation.
- Generic `Dependencies.csv` is not used because the Phase-5 steer explicitly preserves Root `_DEPENDENCIES.md` truth.

## Integrity and deterministic comparison

- All relationship endpoints resolve to live register IDs.
- Eight gating relationships are acyclic; one validator relationship and two App notice/fan-in edges are non-gating.
- Graph node, membership-edge, dependency-edge, gating, notice-edge, and SCC classifications match Phase 3 exactly.
- Closure verdict and bounded warnings match Phase 3 exactly.
- Current repaired Phase-3 N1 return bytes and current N2 return bytes are pinned.
- Accepted estimate and sealed schedule packages are context only and did not supply edges.
- No cut, merge, decompose, or invert move was proposed or performed.
- Earlier evidence and deliverable files were read-only.

## Fresh review

`PASS_ZERO_ACTIONABLE_FINDINGS`: input identities reproduce; coverage counts, relationship counts, SCCs, warnings, and Phase-3 comparison are internally consistent; no authority, scope, or whitespace defect found.
