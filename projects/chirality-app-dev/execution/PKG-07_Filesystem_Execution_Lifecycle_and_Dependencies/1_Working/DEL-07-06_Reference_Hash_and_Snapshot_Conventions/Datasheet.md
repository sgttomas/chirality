# Datasheet: DEL-07-06 Reference Hash and Snapshot Conventions

## Identification

| Field | Value |
|---|---|
| Package ID | PKG-07 |
| Package Name | Filesystem Execution, Lifecycle, and Dependencies |
| Deliverable ID | DEL-07-06 |
| Deliverable Name | Reference Hash and Snapshot Conventions |
| Responsible Party | TBD |
| Type | DOC_UPDATE |
| Context Envelope | S |
| Decomposition Variant | SOFTWARE_DECOMP v3.2 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | Preserve deterministic tools/scripts, reference hash behavior, immutable snapshots, and SHA approval conventions without reactivating retired scope. | `_CONTEXT.md` Deliverable Scope; decomposition DEL-07-06 row |
| Covered scope items | SOW-032 deterministic tools/scripts, SOW-033 immutable snapshots, SOW-034 CHANGE/publication SHA checks. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SSOW and SOW-to-deliverable rows |
| Supported objectives | OBJ-006 filesystem project truth; OBJ-009 professional boundary and reliance-boundary ownership. | `_CONTEXT.md` Traceability; decomposition Objectives |
| Anticipated artifacts | Snapshot/runbook notes; hash bypass convention; CHANGE/SHA checklist. | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-07-06 row |
| Reference hash bypass record | Deliverable folders may include `HASH_VERIFICATION_BYPASS.jsonl`; hash bypasses require human approval and durable bypass records. | `docs/SPEC.md` Sections 3.1 and 5.3 |
| Snapshot convention | Snapshot-producing workflows should write timestamped immutable folders and may update `_LATEST.md` pointers. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1; `docs/PRD.md` FR-062 with REF-006 hash warning |
| Approval evidence convention | Human approvals bind to specific content evidence, normally a git SHA; human-gate lifecycle transitions require approval SHA evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 and K-STATUS-2; `docs/SPEC.md` Section 4.3 |
| Reference tool continuity | Accepted reference hash tooling and dependency-linter behavior remain in scope; retired hardening scope must not be reintroduced by runtime event logging. | `docs/CONTRACT.md` K-REF-1; `docs/PLAN.md` Section 9 |

## Conditions

| Condition | Handling | Source |
|---|---|---|
| `docs/PRD.md` source state | REF-006 is locally accessible but `_REFERENCES.md` reports `HASH_MISMATCH`; this run treats it as a source-state warning per brief. PRD-only statements remain review-aware until hash reconciliation or acceptance. | `_REFERENCES.md` REF-006; task brief |
| Unknown owner | `ResponsibleParty` remains `TBD` until assigned by a human. | `_CONTEXT.md` Source Authority |
| Retired scope boundary | Do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run records, or staleness propagation as current commitments. | `docs/PLAN.md` Section 9; `docs/PRD.md` Section 6.4 and KG-012 with REF-006 hash warning |
| Human authority | No agent, SDK, tool, runtime event, validator, or adapter can author binding approval records. | `docs/CONTRACT.md` K-AUTH-1; `docs/DIRECTIVE.md` Section 2.4 |

## Construction

| Component | Expected Content | Source |
|---|---|---|
| Snapshot/runbook notes | Rules for timestamped immutable snapshot folders, optional `_LATEST.md` pointer updates, non-overwrite of accepted snapshots, and source-state warnings. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
| Hash bypass convention | When reference hash verification is bypassed, record human approval and durable evidence in deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` where applicable. | `docs/SPEC.md` Sections 3.1 and 5.3 |
| CHANGE/SHA checklist | Checklist confirming candidate content evidence, approval token/SHA, HEAD recheck before approved actions, and continued human-only authority. | `docs/DIRECTIVE.md` Sections 2.2 and 2.4; `docs/PRD.md` FR-063 with REF-006 hash warning |
| Tool continuity notes | Notes confirming deterministic project tools/scripts remain indexed and locally executable when present. Exact registry membership is `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |

## References

| RefID | Source | Sections Used | Source State |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Sections 2.1, 2.2, 2.4, 2.5 | MATCH |
| REF-002 | `docs/CONTRACT.md` | K-AUTH-1, K-AUTH-2, K-BIND-1, K-STATUS-1, K-STATUS-2, K-SNAP-1, K-REF-1 | MATCH |
| REF-003 | `docs/SPEC.md` | Sections 2, 3.1, 4.3, 5.3 | MATCH |
| REF-004 | `docs/TYPES.md` | Sections 1-2, 3.3 | MATCH |
| REF-005 | `docs/PLAN.md` | Section 9 | MATCH |
| REF-006 | `docs/PRD.md` | Sections 6.4, 8.10, 10.8, 15 | HASH_MISMATCH source-state warning |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH |
