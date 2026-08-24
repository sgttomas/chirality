# Dependencies: DEL-09-05 CI Artifact and Release Verification Workflow

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no human-declared upstream dependency edges have been accepted yet. Extracted upstream rows are recorded in `Dependencies.csv`.

## Declared Downstream

TBD - no human-declared downstream dependency edges have been accepted yet. No extracted downstream execution edge is emitted by this conservative refresh; the accepted E-032 feedback edge remains non-gating and is discussed in Run Notes.

## Extracted Dependency Register

Source register: `Dependencies.csv`

| Metric | Count |
|---|---:|
| Total rows | 15 |
| ACTIVE rows | 15 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 10 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 4 |
| Upstream execution rows | 10 |
| Downstream execution rows | 0 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-09-05-001 | ANCHOR | OTHER | UPSTREAM | DEL-09-05 decomposition node | ACTIVE |
| DEP-09-05-002 | ANCHOR | OTHER | UPSTREAM | SOW-035 Required local checks | ACTIVE |
| DEP-09-05-003 | ANCHOR | OTHER | UPSTREAM | SOW-036 Section 8/9 validation | ACTIVE |
| DEP-09-05-004 | ANCHOR | OTHER | UPSTREAM | SOW-072 macOS arm64 unsigned DMG release target | ACTIVE |
| DEP-09-05-005 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE |
| DEP-09-05-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-09-01 Section 8 Harness Validation Preservation | ACTIVE |
| DEP-09-05-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE |
| DEP-09-05-008 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-09-04 macOS DMG Packaging and Instruction Root Integrity | ACTIVE |
| DEP-09-05-009 | EXECUTION | INTERFACE | UPSTREAM | DEL-09-06 Network Key Attachment and Renderer Security Checks | ACTIVE |
| DEP-09-05-010 | EXECUTION | PREREQUISITE | UPSTREAM | Stable instruction-root integrity summary artifact | ACTIVE |
| DEP-09-05-011 | EXECUTION | PREREQUISITE | UPSTREAM | CI provider and workflow path | ACTIVE |
| DEP-09-05-012 | EXECUTION | CONSTRAINT | UPSTREAM | `docs/CONTRACT.md` K-KEY-1 | ACTIVE |
| DEP-09-05-013 | EXECUTION | CONSTRAINT | UPSTREAM | `docs/CONTRACT.md` K-NET-1 | ACTIVE |
| DEP-09-05-014 | EXECUTION | CONSTRAINT | UPSTREAM | `docs/CONTRACT.md` K-RELEASE-1 | ACTIVE |
| DEP-09-05-015 | EXECUTION | CONSTRAINT | UPSTREAM | G6a exact-candidate owner ruling for WP-11 | ACTIVE |

## Run Notes

- Run timestamp: 2026-05-20T21:02:12-0600.
- Mode: `UPDATE`.
- Strictness: `CONSERVATIVE`.
- Consumer context: `NONE`.
- Scope: `DEL-09-05`.
- Run root: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Decomposition status: located and used for anchor validation and deliverable target resolution.
- Source documents read: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, prior `_DEPENDENCIES.md`, and the decomposition authority.
- Source documents intentionally not read: `_SEMANTIC.md` per human ruling that semantic lensing and P3 enrichment are skipped and existing semantic outputs are invalid dependency evidence; `_STATUS.md` per narrowed dependency-recording source set.
- Anchor doc selected: `Datasheet.md`.
- Execution doc order selected: `Specification.md`, `Guidance.md`, `Procedure.md`.
- Existing `Dependencies.csv`: missing before this run; created with v3.1 schema.
- Existing declared dependency sections: preserved as `TBD` because no human-declared dependency edges were accepted.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] SUPERSEDED_SOURCE_NOTE`: the four authored documents contain older notes saying not to create `Dependencies.csv`; the current dependency-recording brief explicitly authorizes `Dependencies.csv`, `_DEPENDENCIES.md`, and run-record writes.
- `[WARNING] UNRESOLVED_TBD`: CI workflow path, upload artifact name and retention, release evidence location, `ResponsibleParty`, and some environment readiness checks remain `TBD`.
- `[WARNING] TARGET_TYPE_LIMIT`: OBJ-008 and file/artifact targets use `TargetType=UNKNOWN` where v3.1 has no OBJECTIVE, FILE, or ARTIFACT target enum.

### Gate-5 refresh — 2026-08-24T00:54:32-0600

- Mode: `UPDATE`.
- Strictness: `CONSERVATIVE`.
- Consumer context: `RECONCILIATION`.
- Scope: exactly `DEL-09-05`.
- Run root: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution`.
- Decomposition path: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Decomposition status: exact post-application SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; used for anchor validation and carrier constraints.
- Source documents read: `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, prior `Dependencies.csv`, prior `_DEPENDENCIES.md`, and the exact post-application decomposition.
- Source documents intentionally excluded from dependency evidence: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `_STATUS.md`, and `MEMORY.md`; they are not authoritative sources for this extraction refresh.
- Anchor doc selected: `ScopeOfWork.md` (`Identification`, `Attributes`, and `Purpose and Objective Traceability`).
- Execution doc order selected: `ScopeOfWork.md` (`Scope`, `Attributes`, `Conditions`, and `Requirements`), then the applied decomposition's `DEL-09-05` carrier row.
- Pass 1 result: one parent anchor and four trace anchors remain ACTIVE with stable IDs `DEP-09-05-001` through `DEP-09-05-005`.
- Pass 2 result: nine existing execution rows remain ACTIVE with stable IDs `DEP-09-05-006` through `DEP-09-05-014`; `DEP-09-05-015` records the newly applied explicit G6a exact-candidate constraint.
- Source evidence now points to current `ScopeOfWork.md` sections rather than the earlier split-document names. No source document or `_REFERENCES.md` was modified.
- `DEPENDENCY_NOTES`: the accepted `SCC-RUNBOOK-VALIDATION` disposition is `INVERT`; E-032 (`DEL-09-05` feedback to `DEL-09-06`) remains non-gating. The scoped source establishes the upstream DEL-09-06 security interface but does not explicitly establish a downstream artifact handover, so this conservative refresh does not invent a downstream register row from SCC ordering alone. The other generic cycle moves are decompose, merge, or cut; none is selected here, and merge/cut remain human-gated.
- WP-09 authoring and review remain separate from WP-11 release execution. `DEP-09-05-015` records that WP-11 requires the owner-named exact candidate at G6a and makes no signing, notarization, publication, distribution, release-readiness, lifecycle, or release-authority claim.
- `[WARNING] UNRESOLVED_TBD`: CI workflow path, upload artifact name and retention, release evidence location, `ResponsibleParty`, and some environment readiness checks remain `TBD`.
- `[WARNING] TARGET_TYPE_LIMIT`: OBJ-008, file/artifact targets, and G6a use `TargetType=UNKNOWN` where v3.1 has no OBJECTIVE, FILE, ARTIFACT, or GATE target.
- `[WARNING] ID_FORMAT_VALIDATOR_PROJECT_VARIANT`: `validate_id_format.sh` expects three-digit package/deliverable segments and rejects this project's canonical `PKG-09` / `DEL-09-05` forms. The existing IDs were preserved; the v3.1 dependency schema validator accepts all 15 rows.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T21:02:12-0600 | UPDATE | CONSERVATIVE | located: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PRD_HASH_MISMATCH; SUPERSEDED_SOURCE_NOTE; UNRESOLVED_TBD; TARGET_TYPE_LIMIT | 14 |
| 2026-08-24T00:54:32-0600 | UPDATE | CONSERVATIVE | exact post-application SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | UNRESOLVED_TBD; TARGET_TYPE_LIMIT; E-032_NON_GATING_NO_ROW; ID_FORMAT_VALIDATOR_PROJECT_VARIANT | 15 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 15 |

Closure state: Gate-5 dependency refresh completed locally; validation results are recorded in the 2026-08-24 TASK run record, and unresolved implementation details remain `TBD`.

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`.
- Consume the explicit upstream DEL-09-06 security interface (`DEP-09-05-009`) and G6a exact-candidate constraint (`DEP-09-05-015`) as current factual rows.
- Do not synthesize E-032 into a gating edge or infer a downstream handover from SCC ordering alone; its accepted feedback posture remains non-gating.
- Keep WP-09 runbook authoring/review separate from WP-11 execution. No release authority or readiness follows from this dependency refresh.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
