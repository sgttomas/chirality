# Dependencies: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Descriptive mirror of `Dependencies.csv` (2026-09-22; no formal edge or basis change):

- `DEP-10-04-001` — OTHER; Domain Engine Future Boundary; SATISFIED.
- `DEP-10-04-002` — OTHER; OpenPipeStress fixture profile; SATISFIED.
- `DEP-10-04-003` — OTHER; Future domain-engine boundary objective; SATISFIED.
- `DEP-10-04-004` — CONSTRAINT; Accepted PKG-10 amendment or explicit human authorization; PENDING.
- `DEP-10-04-005` — PREREQUISITE; Accessible source corpus for domain profile validation; SATISFIED.
- `DEP-10-04-006` — PREREQUISITE; ResponsibleParty assignment; SATISFIED.
- `DEP-10-04-007` — PREREQUISITE; Concrete future test path and adapter manifest location; SATISFIED.
- `DEP-10-04-008` — PREREQUISITE; Dependency extraction and project graph validation; SATISFIED.

## Declared Downstream

No downstream-directed row is recorded in this local structured register; this does not assert absence of consumers elsewhere.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run:
  - Runtime overrides: `SCOPE=DEL-10-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
  - Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used.
  - Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
  - `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`; execution docs were read as `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`.
  - Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
  - PKG-10 future-boundary/gated posture preserved; no current-release domain-engine work or implementation dependency was activated.
  - Existing declared dependency lists remain `TBD`; no declared edges were promoted without evidence.
  - `[WARNING] SOURCE_HASH_MISMATCH`: `_REFERENCES.md` reports `docs/PRD.md` REF-006 as `HASH_MISMATCH`; this run preserved the warning and used only the allowed local derivative documents plus decomposition authority.
  - `[WARNING] FUTURE_AMENDMENT_TBD`: accepted PKG-10 amendment or explicit human authorization remains a required upstream gate.
  - `[WARNING] RESPONSIBLE_PARTY_TBD`: `ResponsibleParty` remains `TBD`.
  - `[WARNING] TEST_PATH_TBD`: concrete future test path and adapter manifest location remain `TBD`.
  - `[WARNING] PROJECT_GRAPH_VALIDATION_TBD`: project-level FULL_GRAPH validation remains pending after local register creation.
- 2026-07-10 D-APP-53 reconciliation (plan DRQ-09; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): rows re-verified against the live tree. Closed `PENDING -> SATISFIED`: DEP-10-04-001/-002/-003 (anchors live in decomposition) and -005 (source corpus REF-002..REF-006 all `MATCH` in `_REFERENCES.md`). Annotate-only per plan §3.5, stay PENDING: DEP-10-04-004 (accepted PKG-10 amendment — owner call; D-APP-50/51/52 and D-T0-06 exist but their amendment status is not this loop's to rule; F-APP-3 reaffirmed) and DEP-10-04-006 (ResponsibleParty — owner act; still TBD in `_CONTEXT.md`/`Datasheet.md`). Left open with reasons: DEP-10-04-007 (test paths now exist but no source assigns a domain-engine adapter manifest location) and DEP-10-04-008 (fresh FULL_GRAPH DepClosure snapshot over the reconciled registers pending plan DRQ-11). Dated corrections: the 2026-05-20 `SOURCE_HASH_MISMATCH` warning is resolved — `_REFERENCES.md` line 12 now records REF-006 `docs/PRD.md` Status MATCH (SHA `ac35fba4...`); `TEST_PATH_TBD` is now partial (tests exist, manifest location does not). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. No lifecycle transition (F-APP-4).

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-10-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 | ACTIVE | SATISFIED |
| DEP-10-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-070 | ACTIVE | SATISFIED |
| DEP-10-04-003 | ANCHOR | OTHER | UPSTREAM | OBJ-010 | ACTIVE | SATISFIED |
| DEP-10-04-004 | EXECUTION | CONSTRAINT | UPSTREAM | TBD | ACTIVE | PENDING |
| DEP-10-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002; REF-003; REF-004; REF-005; REF-006 | ACTIVE | SATISFIED |
| DEP-10-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | D-APP-59 | ACTIVE | SATISFIED |
| DEP-10-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | D-APP-58 | ACTIVE | SATISFIED |
| DEP-10-04-008 | EXECUTION | PREREQUISITE | UPSTREAM | Dependencies.csv; CURRENT_FULL_GRAPH_AUDIT | ACTIVE | PENDING |

## Lifecycle Summary

Current structured-register mirror: 1 PENDING, 7 SATISFIED. Lifecycle labels and SatisfactionStatus are distinct; the complete formal register remains unchanged. Earlier run summaries below describe their dated basis.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:24-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH; FUTURE_AMENDMENT_TBD; RESPONSIBLE_PARTY_TBD; TEST_PATH_TBD; PROJECT_GRAPH_VALIDATION_TBD | ANCHOR=3; EXECUTION=5; TOTAL=8 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | located; anchors re-verified | 4 rows SATISFIED; -004/-006 annotate-only (owner-gated); -007/-008 left open with reasons; SOURCE_HASH_MISMATCH resolved (REF-006 MATCH); linter PASS 0/0 | ANCHOR=3; EXECUTION=5; TOTAL=8 |

## Historical D-APP-56 R5 P45 register summary (2026-07-12)

- **Source:** UPD-157
- **Current counts:** ACTIVE 8; RETIRED 0; PENDING=3; SATISFIED=5.
- **Correction:** DEP-10-04-008 is SATISFIED against D53A; four prior PENDING rows are now three.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- **2026-07-16 (D-APP-58):** DEP-10-04-007 is SATISFIED — docs/SPEC.md §18 now assigns the adapter-manifest location convention `_DomainEngines/profiles/<profileId>.adapter.yaml` / `domain-engine-adapter-manifest/v1` (agent selection under owner-delegated latitude; ruling record `execution/_Coordination/_DECISIONS/D-APP-58_RULING_2026-07-16.md`); the four test paths stand per D-APP-53. Manifest instances do not yet exist and remain engine-side/bridge future scope. Three prior PENDING rows are now two (DEP-10-04-004, DEP-10-04-006 — both owner acts).

- **2026-07-16 (delegated judgment, loop Receipt-56):** DEP-10-04-004 amendment judgment discharged — agent decision under owner-delegated latitude (in-session direction, Ryan Tufts): D-APP-50/D-APP-51/D-APP-52 and D-T0-06 do not constitute the accepted PKG-10 amendment (each expressly excludes fixture implementation and tier-0 authoring); no accepted amendment exists and no current activation need requires one. The row remains PENDING/ACTIVE as the truthful future-activation gate; affirmative closure requires a future owner act. Two prior PENDING rows are now one judged-and-held gate (DEP-10-04-004) plus one open owner act (DEP-10-04-006).

- **2026-07-17 (D-APP-59):** DEP-10-04-006 is SATISFIED — the owner confirmed ResponsibleParty Ryan Tufts for DEL-10-04, including the validation-evidence-owner role (owner self-binding act, agent-proposed slate item S2; ruling record `execution/_Coordination/_DECISIONS/D-APP-59_RULING_2026-07-17.md`). Identification surfaces updated in `_CONTEXT.md` and `ScopeOfWork.md`. Remaining open register state: DEP-10-04-004 held PENDING as the truthful future-activation gate per the Receipt-56 delegated judgment; all other rows SATISFIED.

## Current evidence navigation — 2026-09-22

Current contract carrier: `ScopeOfWork.md`; former Datasheet/Specification/Procedure/Guidance labels and old line anchors in formal rows are retained historical evidence locators. Current generic type source is `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`, consumed as `@chirality/runtime-contracts`; D-APP-118 retires the App facade. Retained registry/proposal tests are not proof of live Codex exposure. Formal row evidence/pin/LastSeen changes require the owning dependency reconciliation and are outside this record repair.

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=8; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.

### Additional formal dependency refresh — 2026-09-22

Reviewed postimages in `DDEPEND_PREVIEW_1004_GRAPH.csv`; current rows: ACTIVE=8, RETIRED=0. Historic statements and quotes remain in row Notes. Changed satisfaction is recorded only where explicit in preview; no unrun check is asserted.
