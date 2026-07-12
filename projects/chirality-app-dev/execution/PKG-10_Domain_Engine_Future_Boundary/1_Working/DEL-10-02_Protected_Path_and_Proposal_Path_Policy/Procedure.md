# Procedure: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define a repeatable procedure for producing and reviewing the protected path and proposal path policy without activating domain-engine implementation. The procedure preserves the future-boundary posture of PKG-10 and keeps protected domain-engine model truth separate from agent-writable proposal outputs.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Deliverable context for DEL-10-02 | Available in `_CONTEXT.md`. |
| Decomposition entry for DEL-10-02 and SOW-068 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
| Domain invariants | Available in `docs/CONTRACT.md` §1.10. |
| Future domain requirements | Available in `docs/PRD.md` §8.17 and §10.10, with REF-006 hash status: MATCH treated as source status. — reconciled under D-APP-38 |
| Future profile vocabulary | Available in `docs/TYPES.md` §11. |
| Declared upstream dependencies | Extracted dependency register exists in `_DEPENDENCIES.md`; declared upstream/downstream sections remain TBD. P3 disposition: B-002 already covered as deferred closure input. |
| ResponsibleParty | TBD. |

## Steps

1. Confirm the work remains future-boundary scope.
   - Check that the policy does not implement current-release domain operation execution or activate `/api/domain/*` endpoints.
   - Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.

2. Define policy terms from authoritative vocabulary.
   - Use `Protected path` as an authoritative domain-engine artifact path not directly writable by agents.
   - Use `Proposal path` as an agent-writable folder for proposed changes, summaries, or review aids.
   - Source: `docs/TYPES.md` §11.3.

3. State the protected write quarantine.
   - Require direct agent writes to protected domain paths to be denied or routed through the future approved adapter / operation workflow.
   - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110.

4. State the proposal write allowance.
   - Permit agents to write proposals, summaries, and review aids to declared proposal paths.
   - Do not treat those outputs as accepted protected state.
   - Source: `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3.

5. State the accepted mutation path.
   - Require an approved adapter or operation workflow and explicit human gate before protected domain state changes.
   - Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.

6. Capture hook implications without over-specifying implementation.
   - Record that future enforcement must distinguish protected paths from proposal paths and fail closed for direct protected writes.
   - Mark exact hook API, path glob syntax, and adapter manifest behavior as TBD unless supplied by a future accepted profile contract.
   - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-108.

7. Add boundary-notice requirements.
   - Confirm the policy prevents domain-engine outputs from being represented as professional approval, code compliance, external validation, or solver truth owned by Chirality.
   - Source: `docs/PRD.md` §8.17 FR-115; `docs/CONTRACT.md` §1.10 K-DOMAIN-4.

8. Review examples.
   - Include only category examples supported by sources unless profile-specific path patterns are later accepted.
   - Mark concrete OpenPipeStress or engine-specific paths as TBD.
   - Source: `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3.

## Verification

| Check | Pass Criteria |
|---|---|
| Future-boundary check | No current-release domain engine execution is activated or implied. |
| Terminology check | Protected/proposal path definitions match `docs/TYPES.md` §11.3. |
| Write-quarantine check | Protected domain paths are not agent-writable in policy text. |
| Proposal-path check | Agent-writable outputs are limited to proposals, summaries, and review aids. |
| Human-gate check | Accepted protected-state mutation requires explicit human acceptance. |
| Boundary-copy check | No text says Chirality approves, validates, certifies, or owns solver truth. |
| TBD check | Concrete path patterns, hook implementation details, and engine-specific examples remain TBD where unsupported. |
| Future fixture check | Future verification records include categories for direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate once profile syntax and workflow are accepted. P3 disposition: F-002 incorporated. |

## Records

- Protected/proposal path policy: `Specification.md`.
- Hook implications and TBDs: `Specification.md`, `Guidance.md`.
- Examples and conflicts: `Guidance.md`.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- Dependency register: `_DEPENDENCIES.md` includes extracted active rows, while human-declared upstream/downstream sections remain TBD; closure must not treat those extracted rows as human-declared acceptance.
- Future workflow owner: TBD - the owner who defines the approved adapter or operation workflow that can convert proposals into protected-state changes is not named in accessible sources. P3 disposition: D-002 converted to closure-relevant TBD.
