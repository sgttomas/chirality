# Datasheet: DEL-09-03 Unit and Integration Test Expansion

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-03 |
| DeliverableName | Unit and Integration Test Expansion |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | TEST_SUITE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope | Focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-09 row for DEL-09-03 |
| Anticipated artifacts | Jest/API/integration tests; fixtures; regression cases. | `_CONTEXT.md` Anticipated Artifacts |
| Covered SOW items | SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029. | `_CONTEXT.md` Traceability; decomposition SOW table |
| Supported objectives | OBJ-002, OBJ-003, OBJ-006, OBJ-008. | `_CONTEXT.md` Traceability; decomposition objective table |
| Test command context | `npm run test` is the local unit/API test gate. | `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 |
| Validation adjacency | Section 8 and Section 9 validation are adjacent validation surfaces, but this deliverable is scoped to unit/API/integration test expansion rather than authoring the Section 9 runner itself. | `docs/PRD.md` Sections 12.3-12.6; decomposition rows DEL-09-02 and DEL-09-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| PRD source warning | Expected PRD hash `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`; observed `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Treated as source status per dispatch. | `_REFERENCES.md`; TASK dispatch |
| Dependency register output | `Dependencies.csv` must not be created by this run. Dependency extraction remains deferred until later workflow. | TASK dispatch; `_DEPENDENCIES.md` InitialPopulationRule |
| Source-grounding rule | Unsupported facts remain `TBD`, `ASSUMPTION`, or conflict entries. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
| Lifecycle state | Initial state was `OPEN`; safe transition target after non-empty four-document initialization is `INITIALIZED`. | `_STATUS.md`; `docs/SPEC.md` Section 4 |

## Construction

| Test Area | Required Coverage Target | Source |
|---|---|---|
| TurnEngine lifecycle | Unit-test `TurnEngine.runTurn()` without HTTP and verify accepted-turn persistence, UI event yield, canonical event persistence, permissions/tool exposure linkage, interrupt/cancel handling, and terminal outcomes. | `docs/SPEC.md` Section 10; `docs/PRD.md` FR-070, FR-123, Section 12.5 |
| SSE compatibility | Integration-test `/api/harness/turn` as a transport adapter that preserves browser-facing SSE event names and terminates correctly. | `docs/SPEC.md` Sections 10.4 and 11; `docs/PRD.md` Sections 9.1, 9.3, 12.6 |
| Event replay | Test append-only `events.jsonl` serialization/replay, malformed trailing JSONL tolerance, valid-prior-event preservation, and transcript reconstruction inputs. | `docs/SPEC.md` Sections 9.1-9.4; `docs/CONTRACT.md` K-EVENT-4 and K-EVENT-5; `docs/PRD.md` FR-073, FR-076 |
| Attachments | Test server-side attachment resolver path validation, regular-file checks, symlink rejection, extension allowlist, readability, file-size budget, total-byte budget, and partial/all-failure behavior. | `docs/SPEC.md` Section 16.1; `docs/CONTRACT.md` K-ATTACH-1; `docs/PRD.md` FR-064 |
| Status lifecycle | Test `_STATUS.md` parser and forward-only, actor-authorized transitions including approval SHA requirements for human gates. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 and K-STATUS-2; `docs/PRD.md` FR-052 through FR-054 |
| Dependencies | Test `Dependencies.csv` v3.1 parser/validator/writer behavior, provenance fields, host deliverable consistency, row retirement, and legacy normalization. | `docs/SPEC.md` Section 6; `docs/CONTRACT.md` K-DEP-1, K-DEP-2, K-PROV-1; `docs/PRD.md` FR-055 through FR-057 |
| Interrupts/cancellation | Test interrupt endpoint behavior, cancellation cleanup, lock release, and terminal cancellation/failure persistence. | `docs/PRD.md` FR-071, FR-073, Section 12.6; `docs/SPEC.md` Sections 10.1-10.2 |
| Denied actions | Test deny precedence, `dontAsk`, `readOnly`, denied writes, denied Bash, unknown tools, hook fail-closed behavior, and permission event persistence where runtime event support exists. | `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` K-PERM-1 through K-PERM-5, K-BASH-1, K-HOOK-1; `docs/PRD.md` FR-081, FR-087 through FR-092 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `docs/CONTRACT.md` Sections 1.5-1.9
- `docs/SPEC.md` Sections 4, 6, 9-11, 14-16, 17
- `docs/TYPES.md` Sections 7, 8, 12
- `docs/PRD.md` Sections 8.9, 8.11-8.16, 9, 12.3-12.6
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-09 and SOW mapping rows
