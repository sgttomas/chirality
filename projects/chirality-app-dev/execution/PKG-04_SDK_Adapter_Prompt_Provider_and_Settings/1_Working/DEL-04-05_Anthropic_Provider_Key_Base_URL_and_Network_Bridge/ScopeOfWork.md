---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-05
package_id: PKG-04
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-019, SOW-020, SOW-021]
package_objective_refs: [OBJ-004, OBJ-008]
---

# Scope of Work — DEL-04-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-04-05` in service of project scope [SOW-019, SOW-020, SOW-021] and package objectives [OBJ-004, OBJ-008].

- **OUT-001** — App account/network conformance and structural-redaction evidence for Codex-owned credentials, scoped login/logout, other-client isolation, current renderer/service transports and user-selected command network policy; legacy Anthropic key/URL fixtures remain compatibility evidence.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-04-05 |
> | DeliverableName | Anthropic Provider Key, Base URL, and Network Bridge |
> | PackageID | PKG-04 |
> | PackageName | SDK Adapter, Prompt, Provider, and Settings |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | SECURITY_CONTROL |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | ScopeItems | SOW-019, SOW-020, SOW-021 |
> | Objectives | OBJ-004, OBJ-008 |
>
> Source: `_CONTEXT.md` "Identity", "Traceability"; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` row `DEL-04-05`.
>

### CLM-003 — Attributes

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-004 — Conditions

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-005 — Construction

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Unfinished delivery: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

### CLM-006 — References

> ##### References
>
> | RefID | Source | SectionRef | Status |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` | Sections 1.4, 1.9; K-ENGINE-2, K-ENGINE-4, K-EVENT-6, K-NET-1, K-KEY-1 | HISTORICAL_MATCH |
> | REF-003 | `docs/SPEC.md` | Sections 12.1-12.4, 16.2-16.3 | HISTORICAL_MATCH |
> | REF-005 | `docs/PLAN.md` | Sections 6.3-6.4; R1 implementation targets | HISTORICAL_MATCH |
> | REF-006 | `docs/PRD.md` | Section 8.5 FR-030 through FR-035; FR-075; NFR-002 through NFR-003; NFR-028 through NFR-030 | HISTORICAL_MATCH status — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-019 through SOW-021; OBJ-004, OBJ-008; row `DEL-04-05` | accepted decomposition reference |


Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin. Current applicability: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-008 — Scope

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

### CLM-009 — Requirements

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

The following source-ID crosswalk preserves the original requirement population. Current fulfillment is evaluated against the obligations above and the named live checks below; superseded SDK mechanisms remain historical evidence and never substitute for live verification.

| Requirement ID | Current requirement / explicit historical applicability |
|---|---|
| DEL-04-05-RQ-001 | Codex owns current credential acquisition/custody in the effective home; the historical Anthropic environment/key precedence is compatibility evidence. |
| DEL-04-05-RQ-002 | Credentials are not project truth and must not appear in project files, event/log/artifact payloads or visible diagnostics. |
| DEL-04-05-RQ-003 | The App must not read/copy/relay Codex credentials. The retained safeStorage store does not authorize current Codex custody. |
| DEL-04-05-RQ-004 | Expose only safe account/status metadata; do not disclose secret values through renderer or IPC. |
| DEL-04-05-RQ-005 | Use Codex account login/cancel/logout methods; active-turn SDK environment handoff is historical compatibility behavior. |
| DEL-04-05-RQ-006 | Apply the current K-NET-1 transport boundary; the fixed Anthropic production base URL is historical compatibility policy. |
| DEL-04-05-RQ-007 | Reject invalid App-owned transport requests with safe typed outcomes before unauthorized execution; do not impose retired supplier endpoint validation on native Codex. |
| DEL-04-05-RQ-008 | Retain renderer outbound guarding and secret-free policy diagnostics under current K-NET-1. |
| DEL-04-05-RQ-009 | Native command network follows the selected Codex configuration/sandbox. App-owned service/update transports remain within their accepted scope. |
| DEL-04-05-RQ-010 | No new Chirality provider/remote MCP/plugin integration is authorized here. Preserve native user Codex configuration/resources without treating those as a new App integration grant. |
| DEL-04-05-RQ-011 | Provide truthful typed current provider/native failure outcomes with safe retry/debug context; the old fixed SDK taxonomy is compatibility evidence. |
| DEL-04-05-RQ-012 | Redact current error details before persistence/display; do not require every native failure to become the retired SDK_FAILURE type. |
| DEL-04-05-RQ-013 | Keep provider/native integration behind the application-owned Runtime interface, with App routes as clients rather than a second runtime. |
| DEL-04-05-RQ-014 | Preserve upstream identities and full payloads after structural redaction under D-GOV-43 while distinguishing operational data from project authority. |
| DEL-04-05-RQ-015 | Use the shared-configuration Codex home with private authentication separation; Claude settingSources isolation remains compatibility history. |
| DEL-04-05-RQ-016 | Maintain candidate-bound account/network/redaction fixtures and S-8 evidence for the actual live App/Runtime path. |
| DEL-04-05-RQ-017 | Only redacted safe metadata may cross event/UI/logging/diagnostic boundaries; raw native preservation does not waive secret protection. |

Verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Evidence locations: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. These are hooks and source locations, not newly executed results.

### CLM-010 — Standards

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-011 — Verification

Required current checks: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Named evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

### CLM-012 — Documentation

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Unfinished delivery: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

### CLM-013 — Pass 3 Enrichment Disposition

> ##### Pass 3 Enrichment Disposition
>
> | ItemID | Disposition | Specification Impact | Source Reread Evidence |
> |---|---|---|---|
> | F-001 | converted to TBD | Exact provider wrapper, key handoff test, base URL/network test, and redaction fixture paths remain required artifacts, but final paths cannot be filled until the owning implementation selects them. | `_CONTEXT.md` "Anticipated Artifacts"; decomposition row `DEL-04-05`; `Specification.md` "Documentation". |
> | D-001 | already covered | The `Source-State Warning` remains a final-acceptance blocker for PRD-derived provider-policy rows rather than a specification fact to resolve in P3. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.5; `Specification.md` "Source-State Warning". |
> | D-003 | converted to TBD | Final SDK error object shapes remain TBD pending the accepted SDK package/version probe; the requirement keeps the stable classification classes without freezing SDK object shapes. | `docs/PRD.md` Section 8.5 FR-034; `docs/CONTRACT.md` K-ENGINE-4; `Specification.md` "Documentation". |
> | E-001 | converted to TBD | Redaction evidence is required for logs, events, SDK/provider errors, stderr/debug output, and tool artifacts, but no completed fixture or validation artifact is present in this deliverable folder. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PRD.md` FR-075; `Specification.md` "Verification". |
>

### CLM-014 — Source-State Warning

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

- **AC-001** — The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-016 — Purpose

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

### CLM-017 — Prerequisites

Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

Current implementation/adoption evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Selection boundary: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-018 — Steps

1. Establish the current candidate, source and actual dependency state. Read `Dependencies.csv` and its current descriptive `_DEPENDENCIES.md` index for extracted edges and their actual satisfaction. Historical setup TBDs do not mean no register exists. This record does not change formal edges, gates or satisfaction.
2. Apply the current scope: Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.
3. Implement only within the owning App/Runtime boundary, preserving these requirements: The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.
4. Verify verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.
5. Retain inputs, source/candidate identity, commands, output and limitations; update Remaining only for backchecked outcomes.

Locus and checks: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

Gate: Current bounded App/Runtime implementation brief, APP-HOLD-1 and affected checks; any actual accepted-scope change retains its owning decision.

### CLM-019 — Verification

Required current checks: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Named evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. Historical test outcomes retain their actual path and candidate; no new product result is claimed here.

Unfulfilled checks: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

### CLM-020 — Records

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

Record the current implementation/consumer and named verification locations: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8. Retained SDK modules are historical/compatibility evidence, not a second live Runtime.

Record actual source, candidate, safe metadata, check result and missing evidence for: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

Unfinished delivery: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

### CLM-021 — Pass 3 Evidence Closure

> ##### Pass 3 Evidence Closure
>
> | ItemID | Disposition | Procedure Impact | Source Reread Evidence |
> |---|---|---|---|
> | D-001 | already covered | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/PRD.md` Section 8.5; `Procedure.md` "Human Rulings Needed". — reconciled under D-APP-38 |
> | D-002 | converted to TBD | Node/SDK network enforcement remains an implementation-specific decision. The procedure requires the implementation owner to record the selected mechanism and residual risk instead of assuming SDK internals expose direct hooks. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1; `Procedure.md` Steps 7 and 11. |
> | X-001 | converted to TBD | Validation record references for redaction fixture output, SDK stderr/debug redaction, and policy-denial metadata remain TBD until tests run and artifacts exist. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PLAN.md` Section 6.3; `Procedure.md` "Verification" and "Records". |
> | X-002 | converted to TBD | Evidence that Node/SDK provider calls do not broaden network scope must be produced by the selected wrapper, environment restriction, tests, or probes; no completed evidence exists in this deliverable folder. | `docs/SPEC.md` Section 16.3; `docs/PRD.md` Section 12.2 required checks; `Procedure.md` Steps 7 and 10. |
> | E-001 | converted to TBD | Audit evidence for absence of cleartext key material across logs, events, SDK errors, stderr/debug output, and tool artifacts remains required but unproduced. | `docs/CONTRACT.md` K-EVENT-6 and K-KEY-1; `docs/PRD.md` FR-075 and NFR-002; `Procedure.md` "Verification" and "Records". |
>

### CLM-022 — Human Rulings Needed

Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

Applicable prior decisions: D-GOV-43/A2; D-APP-127; D-APP-131 execution (b); D-APP-132 where applicable. Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

No repeated owner decision is needed for the settled topology, native policy, event preservation, credential custody or D-APP-132 dispositions. Actual accepted-scope changes retain their owning decision. Unresolved delivery and evidence: Complete candidate-bound S-8 and current network/account bridge conformance, including synthetic-secret checks at every App/Runtime sink. Determine any retained Anthropic-store cleanup only in a separately bounded implementation; no credential copying or new provider scope.

- **VER-001** — Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

**Dated source-state record (2026-07-12):** The former D-APP-56/D-APP-38 MATCH finding describes that snapshot only. Source assertions refer to their identified historical snapshot; a past MATCH label is not a present hash verdict. Use the current `_REFERENCES.md` authority-corpus reconciliation; manager D-APP-38 adoption updates authority-reference hashes, while lifecycle/decomposition approval identities remain unchanged. A reliance check alone does not authorize a further re-pin.

### CLM-024 — Purpose

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy.

### CLM-025 — Principles

> ##### Principles
>

### CLM-026 — Preserve Chirality Ownership

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-027 — Treat Keys as Convenience State, Not Project Truth

> ###### Treat Keys as Convenience State, Not Project Truth
>
> API keys are runtime convenience state. They must not be written into the working root, document kit, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. Tests should prove both positive behavior, such as correct source precedence, and negative behavior, such as absence from project files and emitted records.
>
> Sources: `docs/CONTRACT.md` K-KEY-1; `docs/SPEC.md` Sections 12.3 and 16.2.
>

### CLM-028 — Fail Closed on Provider Boundary Violations

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-029 — Keep Network Scope Narrow

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-030 — Redact at Every Boundary

> ###### Redact at Every Boundary
>
> Redaction should apply before details cross from provider/SDK internals into `HarnessEvent`, `UIEvent`, run logs, fixtures, or diagnostics. A provider wrapper should be suspicious of SDK errors and stderr/debug text because upstream message shapes can drift.
>
> Sources: `docs/CONTRACT.md` K-EVENT-6; `docs/PLAN.md` Section 6.3; `docs/PRD.md` FR-075 and KG-021.
>

### CLM-031 — Considerations

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-032 — Trade-offs

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

### CLM-033 — Examples

> ##### Examples
>
> Supported examples from available sources:
>
> - Key precedence example: if a UI safeStorage key exists, it is used before `ANTHROPIC_API_KEY`; if no UI key exists, `ANTHROPIC_API_KEY` is used before `CHIRALITY_ANTHROPIC_API_KEY`. Source: `docs/SPEC.md` Section 12.3.
> - Safe status example: API key status may report `ui`, `env`, or `none`; it must not report the key. Source: `docs/SPEC.md` Section 16.2.
> - Base URL example: `https://api.anthropic.com` with empty or 443 port and no credentials is accepted; non-Anthropic hosts, embedded credentials, or non-443 ports are rejected. Source: `docs/PRD.md` Section 8.5 FR-032.
> - Network example: renderer outbound requests are restricted to loopback and Anthropic API path; broader remote MCP/plugin/network access is future scope. Source: `docs/SPEC.md` Section 16.3.
>

### CLM-034 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | TBD | No source conflict identified during P1/P2 drafting. | TBD | TBD | TBD | TBD | TBD |
>

### CLM-035 — Open Items

Protect credential custody, safe account presentation and the current App network boundary. Codex is the sole MVP engine and credential custodian. Anthropic key precedence, safeStorage, URL validation and SDK_FAILURE classifiers are compatibility evidence, not the current login contract.

The App must never read, copy or relay Codex credentials; login/cancel/logout use Codex account methods in the Chirality effective home and leave other clients unchanged. Renderer traffic and update/service transports conform to current K-NET-1; command network follows user-selected Codex configuration/sandbox. Log only redacted policy/error metadata. Per-root consent, hosted admission and Root DEL-02-09/10 readiness gates are retired by D-APP-127. Structural redaction before every sink remains required.

Named verification: Verify scoped login/logout, other-client credential independence, no credentials in renderer/IPC/events/logs/artifacts, current renderer/transport policy and command policy passthrough. Record actual error outcomes without requiring the retired SDK error taxonomy. Evidence: Runtime `packages/daemon/src/codex-effective-home.ts`, `codex-supervisor.ts`, `tests/codex-effective-home.test.ts`, `tests/codex-supervisor.test.ts`; App `frontend/electron/main.ts`; re-platform `NATIVE_CHECKLIST.md` S-8.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 SOW-020 SOW-021 OBJ-004 OBJ-008 | CLM-009  | AC-001 | VER-001 | Current candidate-bound conformance and named verification; historical path limits and unmet outcomes explicit |
