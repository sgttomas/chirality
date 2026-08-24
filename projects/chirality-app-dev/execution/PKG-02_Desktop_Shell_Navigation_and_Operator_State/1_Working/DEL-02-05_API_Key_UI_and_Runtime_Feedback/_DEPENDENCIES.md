# Dependencies: DEL-02-05 API Key UI and Runtime Feedback

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been declared by a human.

## Declared Downstream

TBD - no accepted dependency edges have been declared by a human.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | TargetType | Target | Status | Evidence |
|---|---|---|---|---|---|---|---|
| DEP-02-05-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-02 Woven Dialogue Shell, Navigation, and Operator State | ACTIVE | `_CONTEXT.md` Identity; applied decomposition PKG-02 |
| DEP-02-05-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-013 Typed runtime errors | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition SOW ledger |
| DEP-02-05-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-019 App credential UI and packaged-daemon single-owner safeStorage conformance | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition SOW ledger |
| DEP-02-05-004 | EXECUTION | PREREQUISITE | UPSTREAM | DELIVERABLE | DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge | ACTIVE | `ScopeOfWork.md` CLM-016; applied decomposition DEL-04-05 |
| DEP-02-05-005 | EXECUTION | INTERFACE | UPSTREAM | DOCUMENT | `@chirality/harness-contract` typed error taxonomy | ACTIVE | `ScopeOfWork.md` CLM-010; `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md` |
| DEP-02-05-006 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE | `ScopeOfWork.md` CLM-010; applied decomposition DEL-03-03 |
| DEP-02-05-007 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-023 Attachment UI and recovery | ACTIVE | `ScopeOfWork.md` traceability; applied decomposition SOW ledger |
| DEP-02-05-008 | EXECUTION | INTERFACE | UPSTREAM | EXTERNAL | Root-owned `HostedEngineConsentPort` | ACTIVE | applied decomposition DEL-02-05 |
| DEP-02-05-009 | EXECUTION | CONSTRAINT | UPSTREAM | EXTERNAL | accepted Root/App account/consent contract; G3; G-CSP; G4 | ACTIVE | applied decomposition DEL-02-05 |
| DEP-02-05-010 | EXECUTION | ENABLES | DOWNSTREAM | DELIVERABLE | DEL-09-06 Network, Key, Attachment, and Renderer Security Checks | ACTIVE | `ScopeOfWork.md` D-APP-80 note; applied decomposition DEL-09-06 |

Counts:

- ACTIVE rows: 10
- RETIRED rows: 0
- ANCHOR rows: 4
- EXECUTION rows: 6
- UNKNOWN targets: 0

## Run Notes

- Run timestamp: 2026-08-24T00:54:31-0600.
- Runtime overrides: `SCOPE=DEL-02-05`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Instruction root: `/Users/ryan/.codex/worktrees/ef5e/chirality`, supplied by the supervising runtime in additive `V2_INSTRUCTION_ROOT_RUNTIME_DECLARATION.md` after an initial missing-environment preflight; the sealed task scope and method were unchanged.
- Decomposition path: `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Decomposition SHA-256: `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` (exact post-application basis).
- Source docs used for row evidence: `_CONTEXT.md`, `ScopeOfWork.md`, `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md`, `_REFERENCES.md`, and the exact post-application decomposition. Assessment and semantic records were read only as scoped context and do not supply row evidence.
- Anchor doc choice: `ScopeOfWork.md` purpose/traceability plus `_CONTEXT.md` identity; the exact decomposition validates PKG-02, DEL-02-05, SOW-013, SOW-019, and SOW-023.
- Execution doc order: `ScopeOfWork.md`, `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md`, then the applied decomposition for target resolution and newly applied carrier interfaces.
- Stable IDs DEP-02-05-001 through DEP-02-05-007 are preserved. DEP-02-05-004 is conservatively resolved to DEL-04-05 for its credential/safeStorage slice; DEP-02-05-006 is resolved to DEL-03-03; DEP-02-05-005 normalizes legacy `TargetType=ARTIFACT` to canonical `DOCUMENT`.
- DEP-02-05-008 and DEP-02-05-009 record the newly applied account/consent interface and live-claim gates exactly as stated by the decomposition. Their Root-owned target locations remain `TBD`; no Root path is invented.
- DEP-02-05-010 records the explicit DEL-09-06 validation handoff as information/evidence flow, not a schedule gate.
- A2-B / E-018 posture: no row was emitted for DEL-05-04 feedback to DEL-02-05 because the permitted scoped sources contain no explicit DEL-05-04 information-transfer statement. The accepted SCC ordering remains non-gating and was not silently linearized.
- `[WARNING] ID_FORMAT_VALIDATOR_MISMATCH`: the generic validator rejects live decomposition IDs `DEL-02-05`, `PKG-02`, `DEP-02-05-001`, and `SOW-013` because it expects three-digit package/deliverable and four-digit SOW shapes. The exact live decomposition identities are preserved; `OBJ-001` passes.
- Parent anchor check: PASS - exactly one ACTIVE `IMPLEMENTS_NODE` anchor.
- Source-preservation check: scoped source documents, current v19 `_REFERENCES.md`, and the decomposition were not modified by this TASK.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T19:30:46-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` present | TARGET_UNRESOLVED; ID_FORMAT_VALIDATOR_MISMATCH; SOURCE_WARNING; TRACEABILITY_DELTA | ANCHOR=3; EXECUTION=3; TOTAL=6 |
| 2026-07-12 | UPDATE / reconciliation annotation | CONSERVATIVE | decomposition v3.2 | none current; earlier warnings retained as dated history | ANCHOR=4; EXECUTION=3; TOTAL=7 |
| 2026-08-24T00:54:31-0600 | UPDATE | CONSERVATIVE | applied SHA `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` | E-018 not emitted: no scoped source evidence | ANCHOR=4; EXECUTION=6; TOTAL=10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 4 |
| PENDING | 5 |
| SATISFIED | 1 |

Closure state:

- Required derivative package regenerated: `Dependencies.csv` v3.1.
- Required dependency index refreshed: `_DEPENDENCIES.md`.
- Remaining blockers: Root-owned account/consent target location is intentionally unresolved; the accepted contract and G3/G-CSP/G4 remain live-claim gates.

## Downstream Handoff Notes

- Consumer context: `RECONCILIATION`.
- Reconciliation should treat DEP-02-05-008 and DEP-02-05-009 as Root-owned interface/constraint evidence with unresolved App-local target paths, not as application or gate-satisfaction claims.
- Reconciliation should keep the DEL-05-04-to-DEL-02-05 E-018 SCC move non-gating unless a later accepted source adds an explicit information-flow edge.

## Historical Register Annotations

- D-APP-56 R5 P40 (2026-07-12): REF-006 is MATCH under D-APP-38; any HASH_MISMATCH token retained in dated history is provenance, not current state.
- D-APP-56 R5 P45 (2026-07-12): UPD-112 added stable anchor DEP-02-05-007 from the explicit SOW-023 decomposition mapping.
