# Guidance: DEL-09-03 Unit and Integration Test Expansion

## Purpose

DEL-09-03 exists to make the vNext runtime, lifecycle, dependency, attachment, and permission behavior testable at focused unit/API/integration levels. The deliverable supports release readiness by expanding regression coverage for the named behaviors rather than by implementing those behaviors directly.

Sources: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 8.11-8.16 and 12.5-12.6; decomposition row for DEL-09-03.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Test product-owned contracts, not SDK defaults | Assertions should target `AgentEnginePort`, `TurnEngine`, browser `UIEvent`s, canonical `HarnessEvent`s, and permission decisions. SDK-specific values belong only in adapter metadata assertions. | `docs/SPEC.md` Section 10.3; `docs/PRD.md` FR-122 and FR-123 |
| Preserve browser compatibility | `/api/harness/turn` tests should protect stable SSE event names and route shape while allowing runtime internals to move behind TurnEngine. | `docs/SPEC.md` Sections 10.4 and 11; `docs/PRD.md` Section 9.3 |
| Make audit order observable | Accepted-turn persistence, terminal outcomes, replay tolerance, and redaction are audit requirements and should be asserted as ordered records where possible. | `docs/CONTRACT.md` K-EVENT-2 through K-EVENT-6 |
| Deny paths need first-class tests | Denied writes, denied Bash, unknown tools, failed hooks, `dontAsk`, and `readOnly` are not edge cases; they are product-critical boundaries. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-5, K-BASH-1, K-HOOK-1 |
| Fixture design should expose failure mode | Attachment, dependency, status, and JSONL fixtures should be small, named by failure condition, and reusable across unit/API tests. | `docs/SPEC.md` Sections 4, 6, 9, 16 |

## Considerations

- Prefer narrow tests around a single invariant when the invariant is explicitly source-defined, such as `_STATUS.md` forward-only transitions or `Dependencies.csv` required columns.
- Use integration tests when behavior depends on route cleanup, session locking, SSE termination, cancellation, or multiple services.
- Use unit tests for deterministic parsers, mappers, permission resolution, fixture validation, and event replay.
- Keep Section 9 validation IDs aligned with DEL-09-02; this deliverable can provide underlying unit/API/integration coverage, but authoring the runner/ID catalog belongs to DEL-09-02 unless a later human ruling changes scope.
- Treat the PRD hash mismatch as a warning, not a reason to discard PRD requirements, because the dispatch explicitly permits this handling.
- Mark unimplemented or phase-dependent coverage as `TBD` or `ASSUMPTION` in planning notes rather than creating tests that assert unavailable behavior.
- Treat missing implementation paths, fixture paths, and command output as closure evidence gaps, not as permission to invent paths. The implementation pass should replace those `TBD` values only after files and commands exist.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Broad matrix vs focused regression cases | Favor source-mapped regression cases for the named DEL-09-03 behaviors. Exhaustive cross-product matrices can be deferred unless a source requirement demands them. |
| Mocked engine vs real SDK adapter | Use stubs for deterministic product-owned contract tests; use SDK-backed adapter tests only where the source requirement is adapter conformance or SDK message mapping. |
| API route tests vs service tests | Keep route tests focused on request validation, locking, SSE encoding, cleanup, and stable shape. Put runtime policy assertions in TurnEngine/permission/event tests. |
| Current behavior vs future phase behavior | Tests for future phase behavior should be pending/TBD or fixture-ready until the corresponding implementation deliverable lands. |
| Minimum coverage vs unavailable surfaces | Require one implemented or explicitly deferred test decision for each DEL-09-03 behavior group, but keep future-phase surfaces marked `TBD` until the owning implementation exists. |

## Examples

| Example Test / Fixture | Expected Intent | Source |
|---|---|---|
| `turn-engine.accepted-before-query.test` | Assert accepted input is written before model/SDK execution begins. | `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` Section 12.6 |
| `sse.compatibility.events.test` | Assert browser-facing SSE event names remain stable. | `docs/SPEC.md` Section 11 |
| `session-events.malformed-tail.test` | Assert replay preserves valid prior events and reports malformed tail diagnostics. | `docs/SPEC.md` Section 9.2 |
| `attachments.symlink-budget.test` | Assert symlink rejection and byte-budget failures are server-side. | `docs/SPEC.md` Section 16.1 |
| `status-transition.human-gate-sha.test` | Assert `CHECKING`/`ISSUED` require approval SHA evidence and actor authorization. | `docs/SPEC.md` Section 4 |
| `dependencies-v31.provenance.test` | Assert active extracted rows require evidence fields or explicit `location TBD`. | `docs/SPEC.md` Section 6; `docs/CONTRACT.md` K-PROV-1 |
| `permissions.dontask-denied-write.test` | Assert denied writes do not execute under `dontAsk`. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 12.6 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONFLICT-001 | PRD reference hash mismatch: expected and observed SHA256 differ. | `_REFERENCES.md` REF-006 | TASK dispatch source-warning override | All source-grounded PRD references | Treat as source warning only for this run, per dispatch. | TBD |
