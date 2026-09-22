---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-02
package_id: PKG-01
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-037, SOW-045, SOW-054, SOW-057, SOW-074]
package_objective_refs: [OBJ-002, OBJ-005, OBJ-009]
---

# Scope of Work — DEL-01-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-01-02` in service of project scope [SOW-037, SOW-045, SOW-054, SOW-057, SOW-074] and package objectives [OBJ-002, OBJ-005, OBJ-009].

- **OUT-001** — The source-grounded reliance-boundary register, enforcement matrix, and test index.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-01-02 Reliance Boundary Register

> #### Datasheet: DEL-01-02 Reliance Boundary Register
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-01-02 |
> | DeliverableName | Reliance Boundary Register |
> | PackageID | PKG-01 |
> | PackageName | Product Governance and Reliance Boundaries |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | REQ_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | Current lifecycle source | `_STATUS.md` |
> | Draft pass | P1/P2 |
> | Primary artifact | `docs/harness/reliance_boundary_register.md` |
> | Supporting artifacts | enforcement matrix and test index embedded in `docs/harness/reliance_boundary_register.md` |
>

### CLM-003 — Attributes

> ##### Attributes
>

### CLM-004 — Source State

> ###### Source State
>
> | RefID | Source | Status | Use in this datasheet |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | MATCH | Product intent, authority, reliance-boundary and professional-boundary rules |
> | REF-002 | `docs/CONTRACT.md` | SNAPSHOT-BOUND v23 | Binding invariants and enforcement expectations |
> | REF-003 | `docs/SPEC.md` | SNAPSHOT-BOUND v23 | Runtime structures, API/file contracts, hooks, settings, validation IDs |
> | REF-004 | `docs/TYPES.md` | MATCH | Vocabulary and type targets |
> | REF-005 | `docs/PLAN.md` | MATCH | Runtime roadmap and R0 reliance-boundary deliverable expectations |
> | REF-006 | `docs/PRD.md` | SNAPSHOT-BOUND v23 | Current product requirements and approved vNext scope under the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance) |
> | REF-007 | `workflows/software-decomp/WORKFLOW.md` | MATCH | Decomposition discipline and no-invention constraints |
>

### CLM-005 — Decomposition Traceability

> ###### Decomposition Traceability
>
> | Trace item | Value |
> |---|---|
> | Scope description | Map every P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundary to a concrete enforcement surface. |
> | CoversScopeItems | SOW-037, SOW-045, SOW-054, SOW-057, SOW-074 |
> | SupportsObjectives | OBJ-002, OBJ-005, OBJ-009 |
> | Directional objective context | ASSUMPTION: OBJ-002, OBJ-005, and OBJ-009 are relevant because the decomposition entry explicitly lists them for DEL-01-02. |
>

### CLM-006 — Boundary Taxonomy

> ###### Boundary Taxonomy
>
> | Boundary ID | Boundary | Product-critical semantic | Primary enforcement surface | Source support |
> |---|---|---|---|---|
> | RB-ENGINE | Runtime engine contract | Codex is the sole MVP engine and qualification target; preserve full protocol and Chirality human-authority boundaries. | Runtime delegated engine adapter and codex-supervisor; conformance evidence must identify the live adapter. | D-GOV-43; D-APP-127; D-APP-131 P-20 |
> | RB-AUDIT | Runtime audit mirror | Accepted turns and outcomes must remain recoverable, including unfamiliar Codex notifications; audit is non-authoritative. | Runtime userData session/event store and replay routes; full-event preservation and replay checks. | K-EVENT-4 as amended; D-GOV-43 |
> | RB-PERMISSION | Permission decisions | Honor the user-selected Codex sandbox/approval policy and answer every server request; record decisions and attribution. | Runtime codex-supervisor and App request presentation; policy/approval tests. No legacy Chirality deny overlay is claimed on native tools. | D-GOV-43; D-APP-127 |
> | RB-FILESYSTEM | Filesystem writes and roots | Record actual conditional Codex enforcement; Full access grants no normative authority. Preserve ordinary-project instruction-root integrity and domain protection obligations. | Codex policy and App root/proposal/packaging checks; live instruction protection and symlink verification remain open. | D-GOV-43; D-APP-132; K-ROOT/K-PATH surviving controls |
> | RB-LIFECYCLE | Deliverable lifecycle and gates | `_STATUS.md` is canonical and human gates are non-delegable. | Status parser; status transition API/MCP; approval SHA checks for human-gate states | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-003 lifecycle sections; REF-001 §3 |
> | RB-TRANSCRIPT | Transcript separation | Runtime audit remains canonical and non-authoritative; Codex thread/rollout data is secondary execution evidence. | Runtime session store plus Codex effective home; resume/link/replay checks. Legacy CLAUDE_CONFIG_DIR is compatibility evidence. | K-EVENT-4; D-GOV-43 |
> | RB-SETTINGS | Shared configuration | Use the user’s shared Codex configuration/resources without a Chirality veto; Codex owns native discovery. Keep authentication separated and credentials custodied by Codex. | Effective Codex home and S-8 account-isolation verification. settingSources is historical Claude compatibility. | D-GOV-43 items 3/6; D-APP-127 |
> | RB-SUBAGENT | Delegation | Children receive bounded authority and their actual parentage, supplied basis, scope, observed decisions and returns are recorded; native descendants do not gain authority by inheritance. | Current Runtime delegation/native child records and role/context checks; do not assert legacy hook/seal enforcement on the live path. | D-GOV-35/43; D-APP-131; D-APP-132 |
> | RB-HUMAN-GATE | Human authority | No agent, SDK, tool, runtime event, or validator can approve, certify, sign, seal, issue, or externally validate work for reliance. | Human approval workflow; status transition policy; UI/document copy; release checks | REF-001 §3; REF-002 K-AUTH-1/K-BIND-1/K-GATE-1/K-PROF-1; REF-006 KG-015 |
> | RB-TOOL-SURFACE | Tool exposure | Runtime validates Chirality application-tool registration/calls; native tools follow user-selected Codex policy. Preserve applicable deterministic exposure and PKG-10 domain-stage controls. | Runtime application-tools and codex-supervisor; App tool-pool ordering and live policy tests remain distinct. | D-APP-132 P-01; D-GOV-43 |
> | RB-HOOKS | Action safeguards | Preserve applicable action-denial and failure guarantees at current owning interfaces. Do not claim that legacy SDK hooks run on the Codex path. | Codex approvals/sandbox and current application-tool validation; verify each retained domain/App denial at its actual surface. | D-GOV-43; D-APP-127/132 |
> | RB-REDACTION | Secret hygiene | Structurally redact configured secrets before every persistence/presentation sink while retaining full inspectable events. Codex credential custody does not satisfy event redaction. | Runtime event/session sinks, App logs and artifacts; live redaction gap remains open. | K-EVENT-6; D-APP-131 P-12 |
> | RB-FALLBACK | Engine qualification | Codex is the sole MVP qualification target; no alternative adapter is required or qualified by legacy fallback tests. Preserve current conformance gaps. | Runtime Codex conformance mapping and current named checks; historical SDK probe evidence remains history. | D-GOV-43; D-APP-131 P-20 |
>

### CLM-007 — Conditions

> ##### Conditions
>
> | Condition | Value |
> |---|---|
> | P0 boundary rule | P0 reliance boundaries cannot be prompt-only or opaque SDK-default-only. |
> | Register coverage rule | The register must identify ownership for product-critical semantics and record the enforcement surface type. |
> | Settings isolation condition | Shared Codex configuration and native discovery follow D-GOV-43; authentication isolation is separately verified by S-8. |
> | Permission condition | Record and answer Codex requests under the user-selected policy; no legacy deny-first overlay is implied for native tools. |
> | Transcript condition | SDK transcripts may support resume/debugging but the Runtime-owned userData session/event store (K-EVENT-4; project-local `.chirality/sessions` is legacy compatibility) remains canonical unless imported into `HarnessEvent` form. |
> | Human-gate condition | Reliance-affecting approval remains human-only and evidence-bound. |
> | Authority-corpus condition | Authority-doc references, including REF-006 `docs/PRD.md`, are reconciled to the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance) at this source state. |
> | Source trace acceptance condition | Register rows that cite `docs/PRD.md` must cite REF-006 and should be rechecked if a later authority-corpus audit reports drift. |
> | Register artifact condition | ADQ-02 generated `docs/harness/reliance_boundary_register.md` as CHECKING-stage evidence, not issuance or dependency closure. |
> | Implementation-surface completion condition | Legacy surfaces and validation IDs exist; current Codex enforcement and result coverage must be mapped explicitly. Absent live proof remains an open gap. |
>

### CLM-008 — Construction

> ##### Construction
>

### CLM-009 — Minimum Register Fields

> ###### Minimum Register Fields
>
> | Field | Purpose | Status |
> |---|---|---|
> | BoundaryID | Stable identifier for each reliance boundary | Required |
> | BoundaryCategory | Audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, engine, tool-surface, hook, redaction, fallback | Required |
> | ProductSemantic | Chirality-owned behavior being protected | Required |
> | SourceRefs | Evidence locations from directive, contract, spec, PRD, types, plan, and decomposition | Required |
> | EnforcementOwner | Current Codex host policy, App-owned Runtime control, application-tool validation, human gate or release check, with actual enforcement limits; historical SDK options/hooks/MCP wrappers are separately labelled compatibility evidence | Required |
> | EnforcementSurface | Concrete module/API/file/test/check where enforcement is expected | Required; `TBD` until implemented |
> | PromptOnlyAllowed | Must be `NO` for P0 boundaries | Required |
> | SDKDefaultOnlyAllowed | Must be `NO` for P0 boundaries | Required |
> | ValidationID | Section 9 or other test/check ID | Required where available; otherwise `TBD` |
> | ResidualRisk | Known unresolved risk or source-state warning | Required when applicable |
> | DecisionStatus | `TBD`, `PROPOSED`, `ACCEPTED`, or `CONFLICT` | Required |
>

### CLM-010 — Deferred Completion Fields

> ###### Deferred Completion Fields
>
> | Deferred field | Current handling | Closure evidence required |
> |---|---|---|
> | ResponsibleParty | `TBD` by scaffold policy until human assignment. | Human-maintained ownership update in deliverable status/context or accepted downstream ownership record. |
> | Exact enforcement file paths | Legacy ADQ-02 paths exist; classify their applicability and map current Runtime/Codex surfaces. | Live-path implementation and test evidence with candidate identity |
> | Exact validation file/test names | Current implemented Section 9 IDs are listed in the ADQ-02 register test index; future IDs remain `TBD` where not yet produced. | Section 9 validation additions or accepted test index entries. |
> | PRD-derived rows | May be drafted from REF-006 under the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance) with snapshot-bound `MATCH` status. | Re-run D-APP-38 reconciliation if an authority document changes before issue-readiness reliance. |
> | SDK transcript/storage decision | Codex thread/rollout records are secondary; Runtime userData events are canonical. | Current resume/link/replay checks; no retired first-adapter probe gate |
>

### CLM-011 — Candidate Validation Index

> ###### Candidate Validation Index
>
> | Validation ID | Boundary coverage |
> |---|---|
> | `section9.runtime_engine_contract` | RB-ENGINE, RB-FALLBACK |
> | `section9.adapter_turn_engine_event_log` | RB-AUDIT, RB-TRANSCRIPT |
> | `section9.adapter_message_mapper` | RB-ENGINE, RB-AUDIT |
> | `section9.session_event_replay` | RB-AUDIT |
> | `section9.reliance_boundary_register` | Implemented register schema/inventory check; see contract-pins.manifest.ts. It does not qualify live Codex enforcement. |
> | `section9.settingsources_isolation` | RB-SETTINGS |
> | `section9.sdk_session_link_resume` | Implemented compatibility linkage check (UPD-100); live Codex linkage/resume requires separate current evidence. |
> | `section9.permission_overlay_hard_deny_precedence` | RB-PERMISSION, RB-TOOL-SURFACE |
> | `section9.tool_runtime_read_file` | RB-TOOL-SURFACE, RB-FILESYSTEM |
> | `section9.chirality_mcp_status_dependencies` | RB-LIFECYCLE, RB-TOOL-SURFACE |
> | `section9.path_containment_hook` | RB-FILESYSTEM, RB-HOOKS |
> | `section9.instruction_root_protection_hook` | RB-FILESYSTEM, RB-HOOKS |
> | `section9.tool_result_budget` | RB-AUDIT, RB-REDACTION |
> | `section9.context_compaction_boundary` | RB-AUDIT, RB-HOOKS |
> | `section9.subagent_governance_hook` | RB-SUBAGENT, RB-HOOKS |
> | `section9.domain_profile_validation` | Implemented closed compatibility profile validation (UPD-102); grants no live binding or apply exposure. |
>

### CLM-012 — References

> ##### References
>
> - REF-001: `docs/DIRECTIVE.md`, especially §§2.7-2.11, §3, §4.2, and §5.
> - REF-002: `docs/CONTRACT.md`, especially K-AUTH, K-BIND, K-GATE, K-PROF, K-ENGINE, K-RELIANCE, K-SDK, K-EVENT, K-PERM, K-HOOK, K-STATUS, K-WRITE, K-SEAL, K-SUBAGENT, K-KEY.
> - REF-003: `docs/SPEC.md`, especially §§8.4, 9, 10, 12, 14, 15, and 19.3.
> - REF-004: `docs/TYPES.md`, especially runtime, permission, hook, SDK, subagent, and validation terms.
> - REF-005: `docs/PLAN.md`, especially R0/R1 reliance-boundary deliverables and acceptance.
> - REF-006: `docs/PRD.md`, especially §§8.12-8.16 and §15, under the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance) MATCH status.
> - REF-007: `workflows/software-decomp/WORKFLOW.md`, especially no-invention and scope-boundary protocol.
>

### CLM-013 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; that Bash/hook posture is historical compatibility evidence; current shell actions follow Codex user-selected policy (D-GOV-43).

## Completion and Reliance Basis — Epistemology

### CLM-014 — Specification: DEL-01-02 Reliance Boundary Register

> #### Specification: DEL-01-02 Reliance Boundary Register
>

### CLM-015 — Scope

> ##### Scope
>
> DEL-01-02 defines the requirements for a Reliance Boundary Register that maps product-critical Chirality semantics to concrete enforcement surfaces. The register covers P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, runtime-engine, tool-surface, hook, redaction, and fallback boundaries.
>
> This specification covers the content and verification expectations for `docs/harness/reliance_boundary_register.md`, the enforcement matrix, and the test index. It does not implement the runtime modules themselves except to name the expected enforcement surfaces and validation hooks those modules must satisfy.
>

### CLM-016 — In Scope

> ###### In Scope
>
> - Boundary taxonomy and stable boundary identifiers.
> - Mapping from governance/source requirements to enforcement owner and enforcement surface.
> - Explicit identification of product-owned versus SDK-provided behavior.
> - P0 checks that prevent prompt-only or opaque SDK-default-only enforcement.
> - Residual-risk entries where SDK behavior, transcript placement, or source-state evidence is not yet verified.
> - Validation index entries for Section 9 runtime validation IDs where available.
>

### CLM-017 — Out of Scope

> ###### Out of Scope
>
> - Implementing `AgentEnginePort`, `TurnEngine`, `SdkOptionsBuilder`, permission overlay, MCP tools, hooks, event store, or subagent bridge.
> - Claiming acceptance of unresolved first-adapter probe items.
> - Treating authority-doc references as current after a future authority-doc edit without rerunning the D-APP-38 reconciliation flow.
> - Issuing professional approval or external validation.
>

### CLM-018 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | RBR-001 | The register shall identify each P0 reliance boundary with a stable `BoundaryID`, category, product semantic, source references, enforcement owner, enforcement surface, validation ID, residual risk, and decision status. | REF-002 K-RELIANCE-1; REF-006 FR-124 | Review generated register schema and row completeness. |
> | RBR-002 | No P0 boundary shall be marked enforceable by prompt text alone. | REF-001 §2.9; REF-002 K-RELIANCE-2/K-PERM-2; REF-006 FR-124 | Check `PromptOnlyAllowed=NO` for every P0 row; flag exceptions as `CONFLICT`. |
> | RBR-003 | No P0 boundary shall rely on opaque SDK defaults alone. | REF-001 §2.9; REF-002 K-RELIANCE-2; REF-006 FR-125 | Check enforcement owner/surface for Chirality code, verified SDK callback/hook, MCP wrapper, release check, or human gate. |
> | RBR-004 | The register shall identify Codex as the sole MVP engine and preserve current Runtime contract ownership. | D-GOV-43; D-APP-127 | Current Codex conformance mapping; legacy section9.runtime_engine_contract does not establish coverage. |
> | RBR-005 | Preserve the complete Codex event stream, including unfamiliar notifications, alongside known-event presentation. Presentation and persisted evidence remain distinct; redaction is separate. | D-GOV-43; D-APP-131 P-05/P-12 | Current raw-event/replay and redaction tests. |
> | RBR-006 | Accepted turns and terminal outcomes shall be persisted in an append-only Chirality audit mirror. | REF-001 §2.7-2.9; REF-002 K-EVENT-3/K-EVENT-4; REF-006 FR-072/FR-073 | `section9.adapter_turn_engine_event_log`; replay validation. |
> | RBR-007 | Runtime session/event records remain canonical; Codex threads/rollouts are secondary execution records, not project truth. | K-EVENT-4 as amended; D-GOV-43 | Current resume/replay linkage checks; legacy section9.sdk_session_link_resume exists but is not live-path proof. |
> | RBR-008 | The App shall use shared Codex configuration/resources and native discovery without vetoing user settings; Codex credentials remain isolated from other clients. | D-GOV-43 items 3/6; D-APP-127 | Effective-home and S-8 checks. |
> | RBR-009 | Persist structured approval requests, resolutions and actual attribution; answer every server request under the user-selected policy. | D-GOV-43 | Current Runtime request/response and App approval presentation tests. |
> | RBR-010 | Honor the selected Codex sandbox/approval policy, including Full access, without treating that policy as authority to issue work or cross governed domain scope. | D-GOV-43; D-APP-131 P-13 | Current policy mapping/approval tests and separate domain controls. |
> | RBR-011 | Application-tool exposure shall be validated by Runtime; native Codex tools follow the selected Codex policy. A tool list or mode label alone is not proof of a protected boundary. | D-APP-132 P-01 | Runtime application-tools tests; distinct live ordering and policy checks. |
> | RBR-012 | Preserve ordinary-project instruction-root integrity, App root/proposal denials and domain protections; record actual sandbox-dependent containment rather than universal native-tool prevention. | D-GOV-43; D-APP-132 | App packaging/instruction-root integrity and current negative write/symlink checks; missing enforcement remains open. |
> | RBR-013 | Verify applicable action-denial and failure guarantees at current App/Runtime interfaces. Legacy SDK hooks are compatibility mechanisms and are not claimed on the Codex path. | D-GOV-43; D-APP-127 | Current application-tool and policy failure tests; retained domain checks. |
> | RBR-014 | Shell execution shall follow the user-selected Codex policy; verify capture, interruption, persistence and recovery on that path. Retired Bash-default-deny gates do not qualify it. | D-GOV-43; D-APP-131 P-08 | Distinct current shell/turn/interrupt tests and applicable S-1–S-8. |
> | RBR-015 | Chirality application tools shall satisfy current Runtime validation, logging and secret-hygiene contracts. Native Codex tools retain their selected policy; no shared legacy hook layer is asserted. | D-GOV-43; D-APP-132 | application-tools/codex-application-tools tests plus unresolved sink-redaction checks. |
> | RBR-016 | Record actual delegated parentage, supplied basis, bounded scope, observed decisions and return linkage. Distinguish managed and native execution and actual enforcement limits. | D-GOV-35/43; D-APP-132 | Current delegation/context/replay evidence; optional per-attempt replay is not adopted. |
> | RBR-017 | `_STATUS.md` shall remain the canonical lifecycle state file and human-gate transitions shall require human evidence. | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-001 §3 | Status transition API/MCP tests; approval SHA checks. |
> | RBR-018 | No agent, SDK, tool, runtime event, validator, or domain adapter shall claim to approve, certify, sign, seal, issue, transmit, or externally validate professional work. | REF-001 §3; REF-002 K-AUTH-1/K-PROF-1 | UI/docs copy review; human-gate checklist. |
> | RBR-019 | Runtime events, logs, tool artifacts, provider errors, and SDK interaction metadata shall redact API keys and configured secret variants. | REF-002 K-EVENT-6/K-KEY-1; REF-003 §12.3; REF-006 FR-075 | Redaction tests; run logger tests; artifact inspection. |
> | RBR-020 | Preserve current Codex conformance failures as explicit gaps; legacy SDK-replacement probes do not require a second MVP engine. | D-GOV-43; D-APP-131 P-20 | Codex adapter conformance mapping and missing distinct checks. |
> | RBR-021 | The register shall record the current D-APP-38 corpus version for authority-doc references, including REF-006 `docs/PRD.md`. | `_REFERENCES.md`; D-APP-38 | Register metadata cites the current corpus snapshot and `MATCH` status. |
> | RBR-022 | The register shall distinguish current corpus-matched source support from any future drift or warning-limited source support in row-level traces where PRD content affects acceptance. | REF-001 §2.1/§2.7; REF-002 K-REF-1/K-INVENT-1; `_REFERENCES.md` REF-006 | Source trace review confirms PRD-cited rows cite REF-006 and the current corpus version, or preserve a drift warning if reconciliation later reports one. |
> | RBR-023 | Final acceptance shall include evidence that no P0 boundary is enforced only by prompt text or by opaque SDK defaults. | REF-001 §2.9; REF-002 K-RELIANCE-2; REF-006 FR-124/FR-125 | Generated register review includes explicit `PromptOnlyAllowed=NO`, `SDKDefaultOnlyAllowed=NO`, and non-empty enforcement-surface evidence for every P0 row. |
> | RBR-024 | Inspectable implementation file paths, hook names, check names, and validation files shall be recorded and kept current; only genuinely absent or unassigned surfaces may remain `TBD`, with a downstream closure path or accepted conflict entry. | REF-002 K-INVENT-1; REF-003 §19.3; decomposition DEL-03/DEL-04/DEL-06/DEL-09 rows | Register maintenance verifies each concrete path exists and each remaining `TBD` has a downstream closure path or accepted conflict entry. |
> | RBR-025 | After `docs/harness/reliance_boundary_register.md` is generated, each register row shall be cross-checked against this specification, the datasheet field schema, and the test index. | REF-003 §19.3; REF-005 R0/R1 acceptance notes | Review record shows all rows map to requirements, source references, validation IDs or `TBD`, and residual risks. |
>

### CLM-019 — Standards

> ##### Standards
>
> | Standard / authority | Applicability |
> |---|---|
> | `docs/DIRECTIVE.md` | Product intent, reliance-boundary principles, human authority, provider-neutral core. |
> | `docs/CONTRACT.md` | Binding invariant catalog; primary normative requirements for this specification. |
> | `docs/SPEC.md` | Runtime structures, settings, hooks, MCP, validation IDs, and API/file contracts. |
> | `docs/TYPES.md` | Terms and target type names used in the register. |
> | `docs/PLAN.md` | Runtime roadmap and R0/R1 reliance-boundary acceptance expectations. |
> | `docs/PRD.md` | Product requirements and risk register, reconciled as REF-006 under the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance). |
> | `workflows/software-decomp/WORKFLOW.md` | Decomposition discipline; no-invention and scope-boundary rules. |
>

### CLM-020 — Verification

> ##### Verification
>
> | Check | Expected evidence |
> |---|---|
> | Schema completeness | Every register row includes the fields listed in this `ScopeOfWork.md` CLM-009, "Minimum Register Fields." |
> | Coverage completeness | Rows exist for audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, runtime-engine, tool-surface, hooks, redaction, and fallback boundaries. |
> | Source traceability | Each row cites at least one governance/source reference and uses `location TBD` where exact implementation files are unavailable. |
> | P0 enforcement posture | P0 rows have `PromptOnlyAllowed=NO` and `SDKDefaultOnlyAllowed=NO`. |
> | Prompt/SDK-default exclusion evidence | Acceptance evidence identifies the actual verified current control and its limitations; historical SDK hooks do not qualify Codex native policy or current application controls. |
> | PRD source-state trace | Rows using REF-006 cite the current corpus-matched source state or explicitly preserve any future drift warning. |
> | Validation mapping | Rows map to implemented Section 9 validation IDs where available; SPEC/PRD-listed future IDs remain `TBD` until the Section 9 script implements them. |
> | Residual-risk surfacing | Authority-corpus drift, SDK transcript placement, SDK API drift, and inherited subagent permission risks are recorded instead of silently resolved. |
> | Cross-document consistency | Datasheet boundary IDs, Specification requirement IDs, Guidance principles, and Procedure verification steps use the same terminology. |
>

### CLM-021 — Documentation

> ##### Documentation
>
> The ADQ-02 work package includes:
>
> - `docs/harness/reliance_boundary_register.md`
> - embedded enforcement matrix
> - test index keyed to current Section 9 validation IDs and future/TBD IDs
> - residual-risk notes for current Codex conformance, policy, redaction and evidence gaps
> - authority-corpus version note for `docs/PRD.md` and any future drift warning
>

### CLM-022 — Open Items

> OI-RBR-001/005: v23 MATCH is historical; recompute drifted source support before current reliance.
> OI-RBR-002: exact legacy paths exist; live Codex/Runtime applicability and enforcement evidence remain open.
> OI-RBR-003: canonical Runtime store and secondary Codex transcript ownership are settled; current live linkage evidence remains required.
> OI-RBR-004: reliance_boundary_register, sdk_session_link_resume and domain_profile_validation IDs are implemented. Legacy coverage does not qualify current controls. Verification: frontend/scripts/harness-section9-manifest.json and frontend/src/__tests__/contract-pins.manifest.ts.

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; that Bash/hook posture is historical compatibility evidence; current shell actions follow Codex user-selected policy (D-GOV-43).

- **AC-001** — The conversion preserves and traces the legacy source content to the frozen project scope references [SOW-037, SOW-045, SOW-054, SOW-057, SOW-074] and package objective references [OBJ-002, OBJ-005, OBJ-009].

## Production and Verification Method — Praxeology

### CLM-024 — Procedure: DEL-01-02 Reliance Boundary Register

> #### Procedure: DEL-01-02 Reliance Boundary Register
>

### CLM-025 — Purpose

> ##### Purpose
>
> This procedure describes how to produce, review, and maintain the Reliance Boundary Register for DEL-01-02. It is a production workflow for the register artifact, enforcement matrix, and test index, not a runtime implementation procedure.
>

### CLM-026 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / source |
> |---|---|
> | Deliverable-local context | `_CONTEXT.md` read for identity, scope, anticipated artifacts, and traceability. |
> | Lifecycle state | Read from `_STATUS.md` (currently `IN_PROGRESS`); this procedure performs no transition. |
> | References | `_REFERENCES.md` read; REF-001 through REF-007, REF-009 and REF-010 are the reference inventory; recompute applicability and hashes. |
> | Dependency declarations | `_DEPENDENCIES.md` and `Dependencies.csv` read; formal row states remain in Dependencies.csv and are not changed here. |
> | Decomposition entry | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-01-02 row read. |
> | Reference integrity | the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance) records REF-006 `docs/PRD.md` as `MATCH`. |
> | Required source review | Directive, Contract, Spec, Types, Plan, PRD, and Software Decomp source slices reviewed. |
>

### CLM-027 — Steps

> ##### Steps
>

### CLM-028 — 1. Confirm Scope and Status

> ###### 1. Confirm Scope and Status
>
> 1. Read `_CONTEXT.md` and confirm:
>    - `DeliverableID = DEL-01-02`
>    - `DeliverableName = Reliance Boundary Register`
>    - `Type = REQ_SLICE`
>    - anticipated artifact includes `docs/harness/reliance_boundary_register.md`
> 2. Read `_STATUS.md`.
> 3. Proceed only if the current state permits drafting under the authorized overwrite set.
> 4. If current state is beyond the authorized set, stop and surface `SKIPPED_PROTECT_HUMAN_WORK`.
>

### CLM-029 — 2. Load Authoritative Source Slices

> ###### 2. Load Authoritative Source Slices
>
> 1. Read `_REFERENCES.md`.
> 2. Verify each listed source path is locally accessible.
> 3. Record hash status for every reference.
> 4. Confirm REF-006 `docs/PRD.md` matches the current D-APP-38 authority corpus.
> 5. Read source slices for:
>    - reliance-boundary definition and provider-neutral runtime ownership;
>    - invariant catalog entries for engine, audit, permission, settings, hooks, lifecycle, filesystem, subagent, human gates, redaction, fallback;
>    - runtime event, SDK option, hook, MCP, and validation requirements;
>    - decomposition SOW/OBJ/DEL traceability.
>

### CLM-030 — 3. Build Boundary Inventory

> ###### 3. Build Boundary Inventory
>
> 1. Create candidate rows for at least:
>    - runtime engine contract;
>    - runtime audit mirror;
>    - structured permission decisions;
>    - filesystem containment and instruction-root protection;
>    - lifecycle status and human gates;
>    - SDK transcript separation;
>    - shared Codex settings and separate authentication;
>    - subagent governance;
>    - deterministic tool surface and MCP wrappers;
>    - hook lifecycle and fail-closed behavior;
>    - secret redaction and key handling;
>    - Codex-only engine qualification and retained historical fallback evidence.
> 2. Assign stable `BoundaryID` values.
> 3. For each row, define the protected Chirality product semantic in Chirality terms.
> 4. Cite source references.
> 5. Mark exact implementation file paths as `TBD` where downstream deliverables have not produced them yet.
>

### CLM-031 — 4. Assign Enforcement Surfaces

> ###### 4. Assign Enforcement Surfaces
>
> For each boundary row:
>
> 1. Identify the current enforcement owner: Codex host for the user-selected sandbox/approval policy; App-owned Runtime for admission, records and application-tool validation; human for governed acceptance; release checks for package gates. Record actual host limits. Historical SDK options, callbacks and MCP wrappers remain compatibility surfaces, not assumed live enforcement owners.
> 2. Identify the concrete enforcement surface.
> 3. If the only surface is prompt support, mark the row incomplete for P0.
> 4. If the only evidence is an opaque supplier default or retained SDK fixture, mark the live P0 row incomplete.
> 5. Add residual-risk notes where actual Codex/Runtime behavior or sink-specific evidence is unverified.
>

### CLM-032 — 5. Attach Validation Evidence

> Map each live obligation to current candidate-bound evidence. The 16 implemented compatibility Section 9 IDs are runtime_engine_contract, adapter_turn_engine_event_log, adapter_message_mapper, session_event_replay, reliance_boundary_register, settingsources_isolation, sdk_session_link_resume, permission_overlay_hard_deny_precedence, tool_runtime_read_file, chirality_mcp_status_dependencies, path_containment_hook, instruction_root_protection_hook, tool_result_budget, context_compaction_boundary, subagent_governance_hook and domain_profile_validation (all prefixed section9.).
> Verification: frontend/scripts/harness-section9-manifest.json and contract-pins.manifest.ts. These IDs cite legacy evidence; instruction-root and dependency-register tests also touch live modules, but that does not establish live Codex permission/containment/lifecycle coverage. Record current Runtime/Codex checks separately and leave missing results open.

### CLM-033 — 6. Cross-Check Against Specification

> ###### 6. Cross-Check Against Specification
>
> 1. Verify every Datasheet boundary ID has a corresponding Specification requirement or verification entry.
> 2. Verify every Specification requirement is reflected in either the boundary matrix, test index, residual-risk notes, or open items.
> 3. Verify Guidance principles do not overstate accepted implementation state.
> 4. Verify no source-warning item has been silently converted into accepted truth.
> 5. Verify all unsupported details remain `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict entries.
> 6. Verify PRD-cited rows cite REF-006 and the current D-APP-38 corpus version, or explicitly preserve any future drift warning.
> 7. Verify no candidate Section 9 validation label is represented as an implemented test until the downstream validation deliverable supplies the file or test name.
>

### CLM-034 — 7. Produce Artifacts

> ###### 7. Produce Artifacts
>
> 1. Draft or update `docs/harness/reliance_boundary_register.md` from the schema and requirements in this `ScopeOfWork.md`, principally CLM-009 and CLM-018.
> 2. Create an enforcement matrix view suitable for implementation review.
> 3. Create a test index keyed by validation ID and boundary ID.
> 4. Carry forward:
>    - D-APP-38 corpus version and any authority-corpus drift warning;
>    - SDK transcript placement residual risk;
>    - SDK API drift residual risk;
>    - subagent inherited-permission residual risk;
>    - implementation-surface `TBD`s.
> 5. Record row-level completion criteria for any downstream `TBD`, including the expected source of closure evidence.
>

### CLM-035 — 8. Review and Close

> ###### 8. Review and Close
>
> 1. Run a consistency review across register rows, enforcement matrix, and test index.
> 2. Confirm there are no P0 rows with prompt-only or SDK-default-only enforcement.
> 3. Confirm human-gate and professional-boundary rows do not imply automated approval.
> 4. Confirm REF-006 is current under the recorded D-APP-38 v23 snapshot (historical hash result; recompute before current reliance), or preserve any future drift warning.
> 5. Confirm the generated register, enforcement matrix, and test index can be traced back to the datasheet fields and specification requirements.
> 6. Move the deliverable to the next lifecycle state only through the authorized status workflow.
>

### CLM-036 — Verification

> ##### Verification
>
> | Verification item | Pass condition |
> |---|---|
> | Scope confirmation | DEL-01-02 identity and scope match `_CONTEXT.md` and decomposition row. |
> | Source access | All listed sources are accessible, with REF-006 corpus status recorded. |
> | Boundary coverage | All required boundary categories have rows. |
> | Enforcement mapping | Each P0 row names a non-prompt-only and non-opaque-SDK-default enforcement surface. |
> | Validation mapping | Each row has a validation ID or `TBD` with residual-risk explanation. |
> | Human authority | No row states or implies automated professional approval, certification, issuance, or external validation. |
> | Cross-document consistency | Datasheet, Specification, Guidance, and Procedure use the same boundary IDs and terms. |
> | Source-state handling | REF-006 PRD usage cites D-APP-38 corpus status; future drift is warning-limited until reconciled. |
> | Generated-register closure | Downstream register rows are cross-checked against requirements, field schema, and test index before final acceptance. |
>

### CLM-037 — Records

> ##### Records
>
> | Record | Purpose |
> |---|---|
> | `ScopeOfWork.md` CLM-001–013 | Boundary taxonomy, source state, minimum fields, candidate validation index, and current-state reconciliation. |
> | `ScopeOfWork.md` CLM-014–023 | Normative requirements, verification expectations, documentation, and open-item posture. |
> | `ScopeOfWork.md` CLM-024–038 | Workflow for producing, validating, and maintaining the register. |
> | `ScopeOfWork.md` CLM-039–060 | Drafting principles, trade-offs, examples, source-state notes, and current implementation guidance. |
> | `docs/harness/reliance_boundary_register.md` | ADQ-02 generated register artifact with embedded enforcement matrix and test index. |
> | Enforcement matrix | Reviewable mapping of boundaries to owners/surfaces. |
> | Test index | Validation ID to boundary coverage map. |
> | TASK run records | Evidence of bounded drafting and source-state history. |
>

### CLM-038 — Remaining Blockers

> BLK-RBR-001: current source hashes and accepted-corpus applicability require recomputation; v23 closure is historical.
> BLK-RBR-002: legacy paths exist, but the current Codex enforcement matrix and evidence need completion.
> BLK-RBR-003: verify current Codex transcript linkage, replay and effective-home credential separation; retired SDK probes are not prerequisites.
> Structural redaction, trustworthy human-gate identity, ordinary-project instruction protection and live conformance remain delivery obligations. No test result or human review is inferred from record repair.

- **VER-001** — Verify current requirement traceability, source fidelity and named checks against this candidate. One-time conversion mapping/parity/render evidence remains historical (R5/CONVERSION_EVIDENCE_REVIEW.csv); it does not establish current behavioral qualification or personal human review.

## Governing Values and Decisions — Axiology

### CLM-039 — Guidance: DEL-01-02 Reliance Boundary Register

> #### Guidance: DEL-01-02 Reliance Boundary Register
>

### CLM-040 — Purpose

> ##### Purpose
>
> The Reliance Boundary Register exists to prevent product-critical Chirality semantics from drifting into prompt-only instruction, opaque SDK defaults, transient runtime state, or undocumented human assumptions. It should make the enforcement ownership of each boundary inspectable before implementation choices harden.
>
> The register is especially important because Codex is the sole MVP engine and qualification target under D-GOV-43. The register distinguishes user-selected Codex enforcement from Chirality-owned application controls and records actual gaps, while preserving human authority and non-binding runtime evidence.
>

### CLM-041 — Principles

> ##### Principles
>

### CLM-042 — 1. Register Product Semantics, Not Vendor Mechanics

> ###### 1. Register Product Semantics, Not Vendor Mechanics
>
> Use Chirality terms for public behavior and canonical records. SDK tool names, message names, session IDs, transcript paths, hook names, and permission modes may appear as adapter metadata, but they should not become the register's primary semantics.
>

### CLM-043 — 2. P0 Boundaries Need Enforceable Surfaces

> ###### 2. P0 Boundaries Need Enforceable Surfaces
>
> For P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries, prompt text can support user understanding but cannot be the enforcement surface. Each P0 row should name a concrete code path, hook, option, MCP wrapper, validation check, release check, or human gate.
>

### CLM-044 — 3. Deny-First Means Deny Overrides All Allows

> The user selects Codex sandbox and approval policy. Record that actual policy and its observed enforcement; do not infer a legacy Chirality deny-first overlay or universal protection from a mode label. Application-tool/domain controls and human authority retain their own scope. Verification: Runtime codex-supervisor policy/approval tests and live negative boundary checks (D-GOV-43; D-APP-132).

### CLM-045 — 4. Canonical Audit Is Chirality-Owned

> ###### 4. Canonical Audit Is Chirality-Owned
>
> SDK transcripts can help with resume/debugging, but the canonical runtime audit mirror is the Chirality event log unless SDK content is imported into `HarnessEvent` form. The register should call out transcript placement and mirror reliability as residual risk until empirically proven.
>

### CLM-046 — 5. Human Authority Is Not Runtime Automatable

> ###### 5. Human Authority Is Not Runtime Automatable
>
> No runtime event, validation pass, agent output, or SDK callback can approve, sign, seal, issue, certify, transmit, or externally validate professional work. Human-gate rows should focus on preserving evidence-bound review and preventing misleading product copy or state transitions.
>

### CLM-047 — 6. Unknowns Stay Visible

> ###### 6. Unknowns Stay Visible
>
> If a module, validation ID, SDK behavior, transcript location, or release check does not yet exist, use `TBD` or a residual-risk note. Do not smooth over gaps by assuming later implementation will satisfy the boundary.
>

### CLM-048 — Considerations

> ##### Considerations
>

### CLM-049 — Source-State Handling

> The preserved authority-corpus hash results are bound to their recorded snapshot (v23 in the discovery basis), not to current source bytes. Later drift is an active source warning until independently recomputed under D-APP-38. D-APP-131 applies settled D-GOV-43 decisions without a duplicate owner prompt; genuine normative amendments retain their governing process.

### CLM-050 — Boundary Granularity

> ###### Boundary Granularity
>
> Rows should be fine-grained enough that a reviewer can answer:
>
> - What product semantic is protected?
> - What could go wrong if this boundary is delegated to SDK defaults or prompt text?
> - Which component enforces it?
> - Which test or human review proves it?
> - What residual risk remains?
>
> Rows should not be so granular that every implementation function becomes its own governance item. Use one boundary row per product-critical semantic, then point to multiple enforcement surfaces when needed.
>
> For required register fields, use mandatory completion criteria rather than advisory wording: each row must name the protected product semantic, source evidence, enforcement owner, enforcement surface, prompt-only posture, SDK-default-only posture, validation evidence or `TBD`, residual risk, and decision status.
>

### CLM-051 — Current Implementation Surfaces And Path Maintenance

> Current contract source is @chirality/runtime-contracts in projects/chirality-runtime/packages/contracts; D-APP-118 retired @chirality/harness-contract and its dedicated rollback support. Runtime packages/core/src/delegated-engine-adapter.ts, delegated-runtime.ts and session-store.ts and packages/daemon/src/codex-supervisor.ts and application-tools.ts are current evidence loci. App frontend/src/lib/harness retains compatibility modules; their path existence is not live-path qualification. Keep exact current ownership and tests in docs/harness/reliance_boundary_register.md. Verification: current consumer census and per-boundary Runtime/App tests; absent result evidence remains open.

### CLM-052 — Residual Risk Topics

> Track current Codex pin/supplier drift, full-event persistence and sink redaction, policy-dependent filesystem enforcement, human-gate actor identity, delegated basis/return evidence, live conformance coverage and authority-corpus drift. Shared Codex settings and native transcript storage are accepted architecture, not settings leakage defects. Preserve unknown empirical results; do not revive retired SDK/Pi/Bash-default-deny prerequisites (D-GOV-43; D-APP-127/131/132).

### CLM-053 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | SDK leverage vs. product-owned semantics | Use the full Codex protocol and user-selected policy while preserving Chirality identity, current application controls and non-binding audit (D-GOV-43); verify actual current enforcement. |
> | Early register completeness vs. implementation uncertainty | Draft all required boundary rows now; use `TBD` for exact implementation files until downstream deliverables exist. |
> | Human gate clarity vs. runtime automation | Automate evidence capture and state-transition checks, but keep binding approval human-only. |
> | Prompt support vs. hard enforcement | Prompt support is acceptable as an explanatory layer, not as the enforcement surface for P0 boundaries. |
> | Local audit mirror vs. SDK transcript richness | Keep Chirality JSONL canonical; link or mirror SDK transcripts only as secondary artifacts. |
>

### CLM-054 — Examples

> ##### Examples
>

### CLM-055 — Example Register Row Pattern

> Example RB-SETTINGS row: protected semantic is shared Codex configuration/resources with separate authentication and Codex credential custody. Source: D-GOV-43 items 3/6 and D-APP-127. Enforcement owner: Codex and effective-home composition. Verification: S-8 and current configuration tests. PromptOnlyAllowed=NO; opaque-default-only evidence is insufficient. DecisionStatus records the accepted direction separately from outstanding empirical results.

### CLM-056 — Example Incomplete Row

> ###### Example Incomplete Row
>
> | Field | Example |
> |---|---|
> | BoundaryID | RB-SUBAGENT |
> | Incomplete signal | Enforcement surface says only "tell subagents not to write outside scope." |
> | Required correction | Record current delegation mechanism, supplied role/basis/scope, actual enforcement and child return evidence; verify the current Runtime/native path rather than cite legacy hooks. |
>

### CLM-057 — Closed Source-State Note

> CONF-RBR-001 was closed against the historical corpus. Later CONTRACT/SPEC/PRD drift reopens current source verification; the historical MATCH neither proves current bytes nor satisfies dependency or lifecycle gates.

### CLM-058 — Generated Artifact Note

> ##### Generated Artifact Note
>
> ADQ-02 generated `docs/harness/reliance_boundary_register.md` with the central row register, embedded
> enforcement matrix, current Section 9 test index, and future/TBD validation-ID notes. This is
> CHECKING-stage evidence only; it does not mutate `_STATUS.md`, satisfy dependency rows, or authorize
> issuance, release readiness, professional approval, certification, sealing, authentication, or
> code-compliance acceptance.
>

### CLM-059 — Assumptions and TBDs

> ASSUMPTION-RBR-001: objective trace remains the accepted decomposition row, with no extra scope inferred.
> TBD-RBR-001: legacy exact paths are known; current evidence mapping uses CLM-051 and retains missing live enforcement.
> TBD-RBR-002: Runtime canonical events and secondary Codex thread storage are settled; live linkage/replay evidence remains required.
> TBD-RBR-003: Section 9 linkage/domain/register IDs are implemented under their original scope; current Codex coverage remains separate.
> TBD-RBR-004: register schema, boundary inventory and index automation exists in frontend/src/__tests__/contract-pins.manifest.ts; old test-file locators need updating. Automation is not product or human acceptance.

### CLM-060 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; that Bash/hook posture is historical compatibility evidence; current shell actions follow Codex user-selected policy (D-GOV-43).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-037 SOW-045 SOW-054 SOW-057 SOW-074 OBJ-002 OBJ-005 OBJ-009 | CLM-014 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
