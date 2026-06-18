# Research Note - gap pkg10 (PKG-10 Domain Engine Future Boundary)

Status: DERIVATIVE_RESEARCH_PACKET

## Question

Assess PKG-10 (Domain Engine Future Boundary), deliverables DEL-10-01..DEL-10-05. For each: what does the Specification require, what is its status, what is its implementationReality judged against the LIVE tree, and what concretely remains to advance it IN_PROGRESS -> CHECKING -> ISSUED?

## Accepted Basis

Live execution tree + git HEAD of projects/chirality-app-dev. Governing docs: docs/PLAN.md §R7, docs/CONTRACT.md §1.10 (K-DOMAIN-1..4), docs/SPEC.md §18, docs/TYPES.md §11, and the D-APP decisions register. Retrieval snapshot SRCIDX_20260616T043733Z used for discovery only (STALE).

## Short Answer

PKG-10 is the roadmap R7 future-boundary package and is, by design, DOCUMENTATION/CONTRACT scope, NOT runtime implementation. All five deliverables are at IN_PROGRESS with a 2026-06-16 HUMAN note "active code implementation underway." That note is contradicted by the live tree: grep across frontend/src and frontend/__tests__ finds ZERO occurrences of DomainEngineProfile, OperationProposal, OpenPipeStress, protectedPath, proposalPath, or boundaryNotice, and there is no /api/domain route. There is also no D-APP ruling authorizing R7/PKG-10 implementation (D-APP-14 explicitly keeps domain tools "gated on the R7 domain-profile amendment"; PLAN/SPEC/CONTRACT all forbid current-release implementation). So implementationReality for CODE is NONE for every deliverable; the DOCUMENT/contract artifacts (four-doc set + dependency registers + semantic/lensing) are SUBSTANTIAL. The gap to ISSUED is governance and document-acceptance, not code: none of the 53 deliverables (here, these 5) has any consolidated Evidence file or any 2_Checking/3_Issued advance, and the R7 fence must not be crossed without the human R7 amendment.

## Evidence

See Evidence_Map.csv (EV-001..EV-012). Load-bearing anchors (all LIVE_TREE):
- EV-001/EV-002 (:RUN) — no PKG-10 code or /api/domain route in the live tree.
- EV-003 docs/PLAN.md:277 "R7 ... Future Amendment"; EV-005 docs/SPEC.md:843-854 "must not be implemented as current-release scope"; EV-004 docs/CONTRACT.md §1.10 future-scope invariants; EV-006 docs/TYPES.md §11 future vocabulary (matches the Datasheet TS shape).
- EV-007 D-APP-14 ruling: domain tools gated on the R7 amendment; EV-008 (:RUN) register D-APP-01..18 has no R7/PKG-10 authorization.
- EV-009 all five _STATUS IN_PROGRESS + HUMAN "active code implementation underway" note (conflicts with EV-001/002/007/008).
- EV-010 four-doc completeness + registers; EV-011 dependency rows record future-gate prerequisites as PENDING/TBD.
- EV-012 (:RUN) docs/PRD.md live hash 6987492b... differs from BOTH REF-006 expected and observed-at-authoring — PRD drifted again.

## Interpretation

PKG-10's deliverable docs are faithful, source-grounded DRAFTS of a future contract (profile shape, protected/proposal path policy, OperationProposal record + human gate, validation/OpenPipeStress fixture spec, boundary-notice copy). They correctly preserve TBD where sources do not define detail and correctly state future-boundary posture. They are NOT current-release code, and they should not be — that is the design. The only true defect is the _STATUS narrative ("active code implementation underway"), which misrepresents the live state and could mislead a downstream sequencer into thinking R7 has begun. Advancement to ISSUED for a future-boundary, document-only package needs (a) a defined doc-acceptance basis (an Evidence file recording doc-completeness, source-grounding, TBD-preservation), (b) the PRD source-hash refresh/acceptance gate cleared, and (c) the human-gated CHECKING->ISSUED transition. None of these require — and none may presume — the R7 implementation fence being opened.

## Caveats

See HANDOFF_STATE.md. Freshness STALE; negative claims bounded to searched roots; doc-completeness judged at spec/directory level not line-by-line across all 20 doc files; PRD not line-diffed.

## Open Questions

- Is the 2026-06-16 "active code implementation underway" status note an error, or does it signal intent that requires the R7 amendment first? (AC-001)
- What is the accepted doc-only acceptance basis for a future-boundary deliverable so it can reach CHECKING/ISSUED without code? (AC-003)

## Handoff / Next Action

Route AC-001 + AC-002 to SCOPE_CHANGE, AC-003 to DOMAIN_DECOMP. Do not open the R7 fence. RESEARCHER recommends only; the human rules.
