# Dependencies: DEL-10-02 Protected Path and Proposal Path Policy

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Descriptive mirror of `Dependencies.csv` (2026-09-22; no formal edge or basis change):

- `DEP-10-02-001` — OTHER; Protected/proposal paths for domain engines; SATISFIED.
- `DEP-10-02-002` — OTHER; Preserve future domain-engine compatibility without turning domain solvers into Chirality core; SATISFIED.
- `DEP-10-02-003` — PREREQUISITE; DomainEngineProfile Contract Draft; SATISFIED.
- `DEP-10-02-004` — INTERFACE; OperationProposal Record and Human Gate Workflow; NOT_APPLICABLE.
- `DEP-10-02-005` — CONSTRAINT; Concrete path glob syntax and hook API; TBD.

## Declared Downstream

No downstream-directed row is recorded in this local structured register; this does not assert absence of consumers elsewhere.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run on 2026-05-20 used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Source documents scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selected: `Datasheet.md`.
- Execution doc order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: available at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Future-boundary warning: PKG-10 is gated; extracted rows do not activate domain-engine work or current-release domain operation execution.
- Source warning: `_REFERENCES.md` reports REF-006 `docs/PRD.md` hash mismatch; retained as a source warning only and not used to invent edges.
- Unknowns preserved: concrete protected/proposal path glob syntax, exact hook API, and adapter manifest behavior remain `TBD`/`UNKNOWN`.
- 2026-07-10 D-APP-53 reconciliation (plan DRQ-07; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): `DEP-10-02-003` moved `TBD -> SATISFIED` on live contract evidence (canon `agents/AGENT_DOMAIN_ENGINE.md@77a327727`; type mirror `frontend/packages/harness-contract/src/domain-profile.ts`; ADOPTED instance `_DomainEngines/profiles/open_pipe_stress.yaml`, D-T0-06). `DEP-10-02-005` stays OPEN per plan §3.5 (no live evidence for glob syntax/hook API; annotated, `LastSeen` bumped). Correction (dated, history retained): the tables below previously still showed `DEP-10-02-004` as ACTIVE with Status counts ACTIVE 5 / RETIRED 0, stale since its 2026-05-24 retirement under RUL-SCC-002-004 — now synced to the CSV (ACTIVE 4 / RETIRED 1). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-10-02-001 | ANCHOR | OTHER | UPSTREAM | SOW-068 | ACTIVE | `Datasheet.md` §Identification |
| DEP-10-02-002 | ANCHOR | OTHER | UPSTREAM | OBJ-010 | ACTIVE | `Datasheet.md` §Identification |
| DEP-10-02-003 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-10-01 | ACTIVE | `Datasheet.md` §Conditions |
| DEP-10-02-004 | EXECUTION | INTERFACE | UPSTREAM | DEL-10-03 | RETIRED | `Specification.md` §Requirements DEL-10-02-REQ-006 (retired 2026-05-24, RUL-SCC-002-004) |
| DEP-10-02-005 | EXECUTION | CONSTRAINT | UPSTREAM | UNKNOWN / TBD | ACTIVE | `Procedure.md` §Steps step 6 |

### Counts

| Dimension | Value | Count |
|---|---|---:|
| DependencyClass | ANCHOR | 2 |
| DependencyClass | EXECUTION | 3 |
| DependencyType | OTHER | 2 |
| DependencyType | PREREQUISITE | 1 |
| DependencyType | INTERFACE | 1 |
| DependencyType | CONSTRAINT | 1 |
| Status | ACTIVE | 4 |
| Status | RETIRED | 1 |

## Lifecycle Summary

Current structured-register mirror: 1 NOT_APPLICABLE, 3 SATISFIED, 1 TBD. Lifecycle labels and SatisfactionStatus are distinct; the complete formal register remains unchanged. Earlier run summaries below describe their dated basis.

## Run History

| Timestamp | Mode | Strictness | Decomposition | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T21:07:20-0600 | UPDATE | CONSERVATIVE | available | 5 | REF-006 hash mismatch; future-boundary/gated scope; concrete path and hook details TBD |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | available; anchors re-verified | 4 | DEP-10-02-003 SATISFIED; DEP-10-02-005 left open (no live glob/hook evidence); summary synced to DEP-10-02-004 RETIRED; REF-006 now MATCH; linter PASS 0/0 |

## Current evidence navigation — 2026-09-22

Current contract carrier: `ScopeOfWork.md`; former Datasheet/Specification/Procedure/Guidance labels and old line anchors in formal rows are retained historical evidence locators. Current generic type source is `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`, consumed as `@chirality/runtime-contracts`; D-APP-118 retires the App facade. Retained registry/proposal tests are not proof of live Codex exposure. Formal row evidence/pin/LastSeen changes require the owning dependency reconciliation and are outside this record repair.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.
