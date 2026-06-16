# Gate 1 Acceptance — chirality-app-dev

Snapshot: `GATE1_20260616T005236Z`
Status: **ACCEPTED**
Acceptance token: `GATE1_ACCEPT_20260616`
Accepted by: operator (ryan@chirality.ai), 2026-06-16

Phase 1 (Intake) accepted as the intended chirality-app-dev DOMAIN_DECOMP intake,
including operator rulings on OI-001..OI-008:
- OI-001 RESOLVED — frontend/src atomized as one grouped unit SRC-FRONTEND-SRC.
- OI-002/003/004/008 ACCEPTED.
- OI-005 RECORDED (cross-repo @repo -> projects/chirality-app-dev).
- OI-006 ACCEPTED_OPTION_A — leave duplicate DEL-00-02 packets; rely on ContentHash dedup at Gate 2.
- OI-007 ACCEPTED_STAGE_PHASE_2 — Phase 2 atomization runs in staged batches.

## Frozen accepted metrics
- Manifest file rows: 836 (835 atomizable components + 1 index-only)
- Atomizable source units: 96 (53 deliverable, 26 governance, 12 product docs, 3 frontend docs, 1 frontend-src, 1 root)
- Sections: 7,996 | Dispatch units: 162 | Failures: 0
- Source manifest SHA-256: a9296fa7d27be114a0514d62c669c8f226e9f1f8cdb06a542d4cc4af6c044456

## Next gate
Gate 1.5-S skeleton review (asset sub-gates and 1.5-P prefilter N/A for this
markdown-only corpus) on structure-mode HTML under source_review_html/.

---
SUPERSEDED 2026-06-16: Gate 1 reopened. Deliverable admission trimmed to the
4 canonical KT docs (DEC-006); manifest 836->441 rows, in-scope sections
7,996->2,874. This snapshot is not a basis for downstream work.
