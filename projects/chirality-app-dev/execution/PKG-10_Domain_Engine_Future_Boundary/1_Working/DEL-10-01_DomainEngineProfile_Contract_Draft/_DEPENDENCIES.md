# Dependencies: DEL-10-01 DomainEngineProfile Contract Draft

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 21:02 dependency-extract run used inline overrides: `SCOPE=DEL-10-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor label/target validation.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- Source warning preserved: `_REFERENCES.md` records a PRD hash mismatch; no dependency row relies solely on PRD content.
- Future-boundary/gated warning: PKG-10 domain-engine work remains future platform scope and requires amendment before implementation. No implementation, endpoint, adapter, protected-path write, or engine-specific dependency was inferred.
- Conservative extraction warning: no EXECUTION rows were emitted because allowed sources did not explicitly state a deliverable-to-deliverable prerequisite, handoff, interface, constraint, or downstream consumer for DEL-10-01.
- 2026-07-02 satisfaction-evidence annotation (agent decision under `TRB-chirality-app-dev-DEL-10-01-2026-07-02`; INSP-03 "Dependency closure open" gap; annotate-only — `Dependencies.csv` rows NOT mutated, `SatisfactionStatus` stays `TBD`, satisfaction judgment is a human call):
  - `DEP-10-01-001` (IMPLEMENTS_NODE PKG-10): anchor verified structurally intact — `_CONTEXT.md` PackageID and decomposition §7/§8 PKG-10 both live; deliverable directory present under PKG-10.
  - `DEP-10-01-002` (TRACES_TO_REQUIREMENT SOW-066, future DomainEngineProfile compatibility): supporting evidence now exists — a concrete ADOPTED tier-0 profile instance (`_DomainEngines/profiles/open_pipe_stress.yaml`, D-T0-06) conforms to the canon this draft targets.
  - `DEP-10-01-003` (TRACES_TO_REQUIREMENT SOW-067, generic domain profile contract): supporting evidence now exists — framework canon `agents/AGENT_DOMAIN_ENGINE.md` @ `77a327727` (REF-008 pin) plus the result-schema refs published 2026-07-02 (`projects/chirality-piping/schemas/operation_outcome.schema.json`, `projects/chirality-piping/schemas/rule_check_run_result.schema.json`) narrow the contract's open hooks.
- 2026-07-10 D-APP-53 reconciliation (plan `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md` DRQ-06; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): the 2026-07-02 annotate-only restriction above ("satisfaction judgment is a human call") is SUPERSEDED — the owner's D-APP-53 ruling authorizes governed direct satisfaction reconciliation. All three anchor rows re-verified live and moved `TBD -> SATISFIED` (`ProposedMaturity=SEMANTIC_READY`, `LastSeen=2026-07-10`). Hygiene: stale `TargetLocation` "§11" pointers on DEP-10-01-002/-003 repaired to "§9 Scope Ledger" (live section numbering). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. No lifecycle transition; `_STATUS.md` stays CHECKING (F-APP-4).

## Extracted Dependency Register

Generated: 2026-05-20 21:02

| DependencyClass | DependencyType | Status | Count |
|---|---|---|---:|
| ANCHOR | OTHER | ACTIVE | 3 |
| EXECUTION | n/a | ACTIVE | 0 |

| DependencyID | Class | AnchorType | Direction | TargetType | TargetRefID | TargetName | Status |
|---|---|---|---|---|---|---|---|
| DEP-10-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | WBS_NODE | PKG-10 | Domain Engine Future Boundary | ACTIVE |
| DEP-10-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-066 | Future Domain Engine Profile compatibility | ACTIVE |
| DEP-10-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | REQUIREMENT | SOW-067 | Generic domain profile contract | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition Path | Decomposition Status | Active Anchors | Active Execution | Warnings |
|---|---|---|---|---|---:|---:|---|
| 2026-05-20 21:02 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | located | 3 | 0 | Semantic/P3 skipped; PRD hash mismatch preserved; future-boundary implementation inference skipped; no explicit execution edges found |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | located; anchors re-verified | 3 | 0 | 3 rows TBD -> SATISFIED; §11 TargetLocation pointers repaired; linter PASS 0/0 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 3 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 3 |

(Synced to CSV state 2026-07-10, D-APP-53 reconciliation; previously TBD 3.)

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.
