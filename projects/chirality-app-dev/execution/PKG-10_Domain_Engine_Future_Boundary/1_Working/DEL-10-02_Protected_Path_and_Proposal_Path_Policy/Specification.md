# Specification: DEL-10-02 Protected Path and Proposal Path Policy

## Scope

This deliverable specifies the future policy boundary separating domain-engine protected paths from agent-writable proposal paths for PKG-10. It covers SOW-068 and supports OBJ-010 by preserving future domain-engine compatibility without turning domain solvers into Chirality core.

In scope:

- Define protected path and proposal path semantics for future `DomainEngineProfile` integration.
- State the write-quarantine rule for protected domain-engine model truth.
- State that proposals, summaries, review aids, operation records, and human gates are separate from authoritative protected artifacts.
- Capture hook and workflow implications at policy level.

Out of scope:

- Current-release domain operation execution.
- Concrete OpenPipeStress implementation.
- Concrete filesystem path patterns for any specific engine profile.
- Direct implementation of `/api/domain/*` endpoints.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17; `docs/SPEC.md` §18.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-10-02-REQ-001 | The policy shall preserve PKG-10 as future-boundary scope and shall not activate current-release domain operation execution. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10; `docs/PRD.md` §8.17 |
| DEL-10-02-REQ-002 | The policy shall define protected paths as authoritative domain-engine artifact paths not directly writable by agents. | `docs/TYPES.md` §11.3 |
| DEL-10-02-REQ-003 | The policy shall define proposal paths as agent-writable folders for proposed changes, summaries, or review aids. | `docs/TYPES.md` §11.3 |
| DEL-10-02-REQ-004 | Protected domain paths shall be write-quarantined from direct agent and ordinary tool mutation. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| DEL-10-02-REQ-005 | Agents shall write proposals, summaries, and review aids rather than protected domain-engine model truth. | `docs/PRD.md` §8.17 FR-111; `docs/PLAN.md` R7 |
| DEL-10-02-REQ-006 | Any accepted mutation of domain state shall flow through an approved adapter or operation workflow and explicit human gate. | `docs/PRD.md` §10.10; `docs/SPEC.md` §18 |
| DEL-10-02-REQ-007 | The policy shall preserve separation between authoritative domain truth owned by the domain engine and Chirality records/proposals/human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106 |
| DEL-10-02-REQ-008 | The policy shall require boundary notices or equivalent copy so domain-engine outputs are not presented as professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 |
| DEL-10-02-REQ-009 | ASSUMPTION: Path policy enforcement should be expressed through future profile policy, path hooks, and operation workflow checks because those enforcement surfaces are named by CONTRACT. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2 |
| DEL-10-02-REQ-010 | Concrete path glob syntax, adapter manifest schema, and per-engine examples remain TBD until DEL-10-01 / future amendment defines the profile contract. | `docs/PRD.md` §8.17 FR-108; `docs/TYPES.md` §11.1 |
| DEL-10-02-REQ-011 | Future acceptance evidence shall include a proof slot showing that direct protected-path writes fail closed and cannot be performed by ordinary agent tools. P3 disposition: F-001 and X-001 incorporated as future evidence criteria. | `docs/CONTRACT.md` §1.6 K-PERM-2, §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| DEL-10-02-REQ-012 | Future acceptance evidence shall include proof slots for proposal-path write allowance and accepted mutation through an approved adapter or operation workflow plus explicit human gate. P3 disposition: F-002 and D-002 incorporated as future workflow evidence criteria. | `docs/PRD.md` §8.17 FR-111, FR-113; `docs/SPEC.md` §18 |

## Standards

| Standard / Source | Applicability |
|---|---|
| `docs/CONTRACT.md` §1.10 | Binding invariants K-DOMAIN-1 through K-DOMAIN-4. |
| `docs/PRD.md` §8.17 | Future domain compatibility requirements FR-106 through FR-115; REF-006 has a hash mismatch warning in `_REFERENCES.md`. |
| `docs/PRD.md` §10.10 | Future domain artifact categories and protected mutation route. |
| `docs/SPEC.md` §18 | Provisional endpoint boundary and future profile requirements. |
| `docs/TYPES.md` §11 | Vocabulary for `DomainEngineProfile`, `OperationProposal`, protected path, proposal path, deterministic adapter, boundary notice, and OpenPipeStress fixture. |
| `docs/PLAN.md` R7 | Roadmap placement and acceptance posture for future domain profiles and operation proposals. |

## Verification

| Requirement | Verification Approach |
|---|---|
| DEL-10-02-REQ-001 | Review text for future-boundary language and absence of implementation activation. |
| DEL-10-02-REQ-002, DEL-10-02-REQ-003 | Confirm definitions match `docs/TYPES.md` §11.3. |
| DEL-10-02-REQ-004, DEL-10-02-REQ-005 | Confirm policy distinguishes protected model truth from proposal/summarization outputs. |
| DEL-10-02-REQ-006 | Confirm accepted mutation route includes approved adapter or operation workflow and explicit human gate. |
| DEL-10-02-REQ-007, DEL-10-02-REQ-008 | Confirm professional-boundary and solver-truth separation language is present. |
| DEL-10-02-REQ-009 | Human review required because hook implementation detail is not fully specified in accessible source slices. |
| DEL-10-02-REQ-010 | Human review required when profile contract or engine-specific path patterns are drafted. |
| DEL-10-02-REQ-011 | Future validation fixture or equivalent review evidence confirms direct protected writes are denied or routed away from mutation and fail closed. |
| DEL-10-02-REQ-012 | Future validation fixture or equivalent review evidence confirms proposal-path writes remain allowed as non-binding artifacts and accepted mutation requires the approved route plus human gate. |

## Documentation

Required artifacts for this deliverable:

- Protected/proposal path policy.
- Hook implications.
- Examples.

Current documentation gaps:

- Concrete protected/proposal path pattern examples are TBD.
- Profile-specific adapter and manifest details are TBD.
- ResponsibleParty remains TBD by dispatch instruction and `_CONTEXT.md`.
- Future test fixture categories remain TBD until the governed `DomainEngineProfile` syntax and operation workflow are accepted: direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate. P3 disposition: F-002 and X-002 incorporated as future slots.
