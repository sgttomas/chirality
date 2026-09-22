# Dependencies: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Current extracted upstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-02-001, DEP-04-02-002, DEP-04-02-003, DEP-04-02-004, DEP-04-02-005, DEP-04-02-006, DEP-04-02-007, DEP-04-02-008, DEP-04-02-009, DEP-04-02-010

## Declared Downstream

Current extracted downstream rows are recorded in `Dependencies.csv`; preserve their individual status and satisfaction. DEP-04-02-011

## Extracted Dependency Register

Descriptive mirror of current `Dependencies.csv`; no formal field is changed.

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-04-02-001 | ANCHOR | OTHER | UPSTREAM | PKG-04 | ACTIVE | SATISFIED |
| DEP-04-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-016 | ACTIVE | SATISFIED |
| DEP-04-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-045 | ACTIVE | SATISFIED |
| DEP-04-02-004 | ANCHOR | OTHER | UPSTREAM | SOW-047 | ACTIVE | SATISFIED |
| DEP-04-02-005 | ANCHOR | OTHER | UPSTREAM | SOW-052 | ACTIVE | SATISFIED |
| DEP-04-02-006 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-04-01 | RETIRED | SATISFIED |
| DEP-04-02-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-04 | ACTIVE | TBD |
| DEP-04-02-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-02 | ACTIVE | TBD |
| DEP-04-02-009 | EXECUTION | INTERFACE | UPSTREAM | PKG-06 | ACTIVE | TBD |
| DEP-04-02-010 | EXECUTION | INTERFACE | UPSTREAM | TBD | ACTIVE | TBD |
| DEP-04-02-011 | EXECUTION | HANDOVER | DOWNSTREAM | TBD | ACTIVE | TBD |

Counts: ACTIVE=11; satisfaction SATISFIED=6, TBD=5.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- Defaults applied: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=AUTO`, `EXECUTION_DOC_ORDER=AUTO`.
- Chosen anchor document: `Datasheet.md`.
- Chosen execution documents: `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Source-state warning: `_REFERENCES.md` reports `docs/PRD.md` as `HASH_MISMATCH`; PRD-backed statements remain warning-bearing evidence and do not override matching higher-authority sources.
- Validator warning: `tools/validation/validate_id_format.sh` expects three-digit IDs such as `DEL-000-00` and `PKG-000`, so it rejects accepted decomposition IDs such as `DEL-04-02` and `PKG-04`; authoritative decomposition IDs were preserved unchanged.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: one ACTIVE `IMPLEMENTS_NODE` parent anchor exists.
- Conservative unresolveds retained: runtime engine contract integration target and runtime/event max-turn consumer remain `TargetType=UNKNOWN`, `TargetRefID=TBD`.
- 2026-07-18 WI-PKG04-01 handover-evidence pass (D-APP-60 exercise; agent decision under owner-delegated latitude): `DEP-04-02-006` closed `SATISFIED` — the recorded need (first-adapter probe/version decision before exact SDK TypeScript option fields are frozen) is delivered by the pinned `@anthropic-ai/claude-agent-sdk@0.3.150` / `@anthropic-ai/sdk@0.93.0`, `sdk-options-builder.ts`, and `sdk-options-builder.test.ts`; producer row `DEP-04-01-010` closed in the same pass. Citation note: the row's `Procedure.md > Prerequisites` source now lives at `ScopeOfWork.md` CLM-017 Prerequisites per owner commit `fe4bdee53` (2026-07-13 ScopeOfWork-v1 migration); the kit's CLM-017 prerequisite wording still reads TBD and is reported as a kit/register divergence for the next owner-authorized kit pass. See DEL-04-01 `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md` section A.

## Run History

| Timestamp | Mode | Strictness | Decomposition Path | Decomposition Status | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|---|
| 2026-05-20T19:35:54-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | FOUND | PRD hash mismatch; semantic outputs skipped by human ruling; ID-format helper rejects accepted two-digit project IDs; two execution targets remain UNKNOWN/TBD | ANCHOR=5; EXECUTION=6; TOTAL=11 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| TBD | 5 |

## Downstream Handoff Notes

Not applicable. `CONSUMER_CONTEXT=NONE`.

## Current descriptive index — 2026-09-22

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Current consumer/verification locus: Runtime `packages/daemon/src/codex-supervisor.ts`, `codex-effective-home.ts`, `tests/codex-supervisor.test.ts`, `tests/codex-effective-home.test.ts`; historical App `frontend/src/lib/harness/sdk-options-builder.ts` and `frontend/src/__tests__/lib/sdk-options-builder.test.ts`. The current topology is application-owned Runtime; older daemon/SDK file names and retired kit-file citations in dated Run Notes are historical source references, not fresh implementation prerequisites. A proposed change to a formal row, satisfaction or accepted dependency basis must be applied by its owner; this index does not enact it.

## Current evidence-locator refresh — 2026-09-22

5 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=10; RETIRED=1; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_THREE_INTERFACES.csv`; current rows: ACTIVE=10, RETIRED=1. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
