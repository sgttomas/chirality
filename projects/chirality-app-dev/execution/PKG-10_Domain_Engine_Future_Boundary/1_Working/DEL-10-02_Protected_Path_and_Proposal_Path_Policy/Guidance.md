# Guidance: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-10-02 exists to define a future security boundary for domain-engine filesystem interaction: agents may write proposals, summaries, and review aids, but they must not write protected domain-engine model truth. This supports OBJ-010 while keeping PKG-10 in future-boundary scope. Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17.

## Principles

1. **Future-boundary first.** Treat this policy as compatibility design for a governed future amendment, not as permission to activate domain-engine execution now. Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.
2. **Protected truth stays protected.** Protected paths hold authoritative domain-engine artifacts and are not directly writable by agents. Source: `docs/TYPES.md` §11.3; `docs/CONTRACT.md` §1.10 K-DOMAIN-2.
3. **Proposals are non-binding work products.** Proposal paths may hold proposed changes, summaries, or review aids, but they do not become accepted protected domain state without the future workflow. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
4. **Accepted mutation needs a gate.** Any accepted mutation of protected domain state must flow through an approved adapter or operation workflow and explicit human gate. Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.
5. **Chirality does not become the solver.** Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106.
6. **Boundary copy matters.** Domain-engine outputs must not be presented as professional approval, code compliance, external validation, or solver truth owned by Chirality. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115.

## Considerations

- Policy should be profile-driven once `DomainEngineProfile` exists; the accessible sources name `protectedPaths` and `proposalPaths` fields but do not define concrete path glob syntax. Source: `docs/TYPES.md` §11.1.
- Hook implications are policy-level in the current source set. CONTRACT names path hooks and operation workflow as enforcement surfaces, but the exact hook API for domain paths is TBD. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2.
- OpenPipeStress is only a potential first fixture profile. Avoid hardcoding OpenPipeStress assumptions into Chirality core policy. Source: `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3.
- REF-006 `docs/PRD.md` has a hash status: MATCH in `_REFERENCES.md`; dispatch instruction says to treat that MATCH as a source status. (reconciled under D-APP-38).
- Concrete protected/proposal path examples stay category-level because `DomainEngineProfile` exposes `protectedPaths` and `proposalPaths` fields but the accessible sources do not define accepted glob syntax or per-engine path patterns. P3 disposition: C-001 already covered and made explicit; X-002 remains a future documentation slot.
- Final publication wording should continue to say proposal artifacts are review aids only: they do not become accepted protected domain state without the future approved workflow and explicit human gate. P3 disposition: E-002 incorporated as closure wording guidance.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Proposal usability vs protected-state safety | Permit agent-authored proposals and summaries, but deny direct protected model writes. | `docs/PRD.md` §8.17 FR-110, FR-111 |
| Generic profile policy vs engine-specific convenience | Keep policy generic until profile contract and fixture adoption are accepted. | `docs/PRD.md` §8.17 FR-107, FR-114 |
| Prompt guidance vs runtime enforcement | Do not rely on prompt text alone for protected path denies; future implementation needs profile/path/hook enforcement. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| Review velocity vs human authority | Require explicit human acceptance before applying domain operations. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |

## Examples

Supported example categories:

- Agent writes a proposed domain change package, summary, or review aid to a proposal path. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
- Agent direct write to a protected model path is denied or routed to a proposal workflow. Source: `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10.
- OpenPipeStress may be represented as a future fixture profile if adopted, but concrete OpenPipeStress path examples are TBD. Source: `docs/PRD.md` §8.17 FR-114.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | PRD source hash status: MATCHes expected reference hash, but dispatch instruction says to treat it as source status. | `_REFERENCES.md` REF-006 | Dispatch brief | All PRD-grounded sections | Use local `docs/PRD.md` as accessible source with warning recorded. | TBD — reconciled under D-APP-38 |
| CT-002 | Concrete protected/proposal path examples are requested as anticipated artifacts, but accessible sources define only categories and fields, not specific path patterns. | `_CONTEXT.md` Anticipated Artifacts | `docs/TYPES.md` §11.1/§11.3; `docs/PRD.md` §8.17 | Examples, requirements, procedure | Mark concrete patterns TBD until `DomainEngineProfile` contract/future amendment supplies them. | TBD |
| CT-003 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | `docs/PRD.md` §8.17 and §10.10 | PRD-grounded requirements, closure language | Keep A-001 and E-001 visible as a source-warning conflict until a human accepts or replaces the PRD snapshot. | TBD |
| CT-004 | No accountable owner is named for accepting or replacing the REF-006 PRD snapshot before final policy closure. | `_REFERENCES.md` REF-006 | `_CONTEXT.md` Source Authority | Source warning closure | Treat D-001 as a human-ruling TBD; do not close the PRD source warning by agent judgment. | TBD |
