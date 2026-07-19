---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-02
package_id: PKG-01
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
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
> | REF-002 | `docs/CONTRACT.md` | MATCH | Binding invariants and enforcement expectations |
> | REF-003 | `docs/SPEC.md` | MATCH | Runtime structures, API/file contracts, hooks, settings, validation IDs |
> | REF-004 | `docs/TYPES.md` | MATCH | Vocabulary and type targets |
> | REF-005 | `docs/PLAN.md` | MATCH | Runtime roadmap and R0 reliance-boundary deliverable expectations |
> | REF-006 | `docs/PRD.md` | MATCH | Current product requirements and approved vNext scope under the current D-APP-38 corpus snapshot |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH | Decomposition discipline and no-invention constraints |
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
> | RB-ENGINE | Runtime engine contract | SDK APIs must not define public Chirality semantics. | `AgentEnginePort` / `RuntimeEngineContract`; engine conformance tests; adapter boundary | REF-001 §2.8-2.10; REF-002 K-ENGINE-1/K-ENGINE-4; REF-006 FR-122/FR-123 |
> | RB-AUDIT | Runtime audit mirror | Accepted turns and runtime outcomes must be recoverable in Chirality terms. | `.chirality/sessions/<sessionId>/events.jsonl`; `HarnessEvent` schema; replay tests | REF-001 §2.7-2.9; REF-002 K-EVENT-4; REF-003 §8.4/§19.3; REF-006 FR-072-FR-074/FR-121 |
> | RB-PERMISSION | Permission decisions | Tool and runtime permissions are structured, persisted, and governed by capability-forward policy with explicit hard-deny precedence. | `ChiralityPermissionOverlay`; `HarnessPermissionDecision`; `tool.permission` events | REF-002 K-PERM-1/K-PERM-3; REF-003 §15; REF-004 §8; REF-006 FR-087-FR-092 |
> | RB-FILESYSTEM | Filesystem writes and roots | Writes must stay inside the active project root and must not mutate instruction-root assets. | Path containment helpers; `PreToolUse` hooks; MCP wrappers; symlink write rejection | REF-001 §2.7/§5; REF-002 K-ROOT-2/K-PATH-2/K-PATH-3; REF-003 §15.2; REF-006 FR-095/FR-097 |
> | RB-LIFECYCLE | Deliverable lifecycle and gates | `_STATUS.md` is canonical and human gates are non-delegable. | Status parser; status transition API/MCP; approval SHA checks for human-gate states | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-003 lifecycle sections; REF-001 §3 |
> | RB-TRANSCRIPT | SDK transcript separation | SDK transcripts are secondary and must not displace the Chirality audit mirror. | SDK session linkage metadata; local `SessionStore`/`CLAUDE_CONFIG_DIR` where reliable; residual-risk register entry when default SDK paths remain | REF-001 §2.8-2.10; REF-002 K-SDK-3; REF-003 §8.4/§12.4; REF-006 FR-118/FR-121/KG-024 |
> | RB-SETTINGS | SDK settings isolation | Shipped builds must not load ambient user/global or local Claude Code settings. | `settingSources: []`; `SdkOptionsBuilder` tests; release verification | REF-001 §4.2/§5; REF-002 K-SDK-1; REF-003 §12.2; REF-006 FR-117/KG-022 |
> | RB-SUBAGENT | Subagent delegation | Type 2 child runs cannot expand authority or inherit unsafe tool posture. | `evaluateSubagentGovernance`; subagent hooks; restricted child tools/cwd; child run records | REF-002 K-SEAL-1/K-SUBAGENT-1/K-SUBAGENT-2; REF-003 §15.2; REF-004 subagent terms; REF-006 FR-101/FR-102/KG-027 |
> | RB-HUMAN-GATE | Human authority | No agent, SDK, tool, runtime event, or validator can approve, certify, sign, seal, issue, or externally validate work for reliance. | Human approval workflow; status transition policy; UI/document copy; release checks | REF-001 §3; REF-002 K-AUTH-1/K-BIND-1/K-GATE-1/K-PROF-1; REF-006 KG-015 |
> | RB-TOOL-SURFACE | Tool exposure | Tool availability must be deterministic and permission-filtered; `allowedTools` alone is not a restriction boundary. | Tool resolver; `disallowedTools`; mode policy; `canUseTool`; hooks; tests | REF-002 K-TOOL-1/K-TOOL-2/K-PERM-3; REF-003 §14.3; REF-006 FR-078-FR-083/KG-023 |
> | RB-HOOKS | Hook lifecycle and fail-closed behavior | Hook failures block write, shell, domain, and subagent actions. | SDK hook callbacks mapped through Chirality hooks; hook events; failure triage | REF-002 K-HOOK-1; REF-003 §15.2; REF-004 §8.5; REF-006 FR-093-FR-095 |
> | RB-REDACTION | Secrets and sensitive runtime records | API keys and secret variants must not be persisted in logs, events, SDK transcripts if avoidable, or tool artifacts. | SafeStorage/env precedence; redaction helper; run logger tests; event/log redaction | REF-002 K-EVENT-6/K-KEY-1; REF-003 §12.3; REF-006 FR-075 |
> | RB-FALLBACK | SDK fallback | A governed fallback/custom-runtime path remains necessary if an SDK behavior cannot satisfy a critical boundary. | R0/R1 first-adapter probe; fallback criteria; conformance suite; reliance-boundary register residual-risk entries | REF-001 §2.8-2.10; REF-002 K-ENGINE-5; REF-006 FR-126/KG-030 |
>

### CLM-007 — Conditions

> ##### Conditions
>
> | Condition | Value |
> |---|---|
> | P0 boundary rule | P0 reliance boundaries cannot be prompt-only or opaque SDK-default-only. |
> | Register coverage rule | The register must identify ownership for product-critical semantics and record the enforcement surface type. |
> | Settings isolation condition | Shipped SDK options use `settingSources: []`; `user` and `local` setting sources are not used in shipped builds. |
> | Permission condition | Permission decisions are recorded as `allow`, `deny`, or application-level `ask`; deny rules override allow decisions. |
> | Transcript condition | SDK transcripts may support resume/debugging but `.chirality/sessions/<sessionId>/events.jsonl` remains canonical unless imported into `HarnessEvent` form. |
> | Human-gate condition | Reliance-affecting approval remains human-only and evidence-bound. |
> | Authority-corpus condition | Authority-doc references, including REF-006 `docs/PRD.md`, are reconciled to the current D-APP-38 corpus snapshot at this source state. |
> | Source trace acceptance condition | Register rows that cite `docs/PRD.md` must cite REF-006 and should be rechecked if a later authority-corpus audit reports drift. |
> | Register artifact condition | ADQ-02 generated `docs/harness/reliance_boundary_register.md` as CHECKING-stage evidence, not issuance or dependency closure. |
> | Implementation-surface completion condition | Exact module paths, hook/check names, and validation file names remain `TBD` until downstream runtime and Section 9 deliverables produce inspectable artifacts. |
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
> | EnforcementOwner | Chirality code, SDK option, SDK hook/callback, MCP wrapper, human gate, release check, prompt support, or mixed | Required |
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
> | Exact enforcement file paths | ADQ-02 register rows name current inspectable runtime paths where present and preserve `TBD` where downstream modules do not yet exist. | Downstream implementation paths or register rows verified against produced modules and hooks. |
> | Exact validation file/test names | Current implemented Section 9 IDs are listed in the ADQ-02 register test index; future IDs remain `TBD` where not yet produced. | Section 9 validation additions or accepted test index entries. |
> | PRD-derived rows | May be drafted from REF-006 under the current D-APP-38 corpus snapshot with current `MATCH` status. | Re-run D-APP-38 reconciliation if an authority document changes before issue-readiness reliance. |
> | SDK transcript/storage decision | Residual risk until R0/R1 probe evidence is available. | Accepted first-adapter probe result naming transcript placement or mirroring policy. |
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
> | `section9.reliance_boundary_register` | Future/TBD validator ID; ADQ-02 generated the document artifact and cross-check table but did not add this ID to the current Section 9 script. |
> | `section9.settingsources_isolation` | RB-SETTINGS |
> | `section9.sdk_session_link_resume` | Future/TBD session-linkage validator ID; not implemented in the current Section 9 script. |
> | `section9.permission_overlay_hard_deny_precedence` | RB-PERMISSION, RB-TOOL-SURFACE |
> | `section9.tool_runtime_read_file` | RB-TOOL-SURFACE, RB-FILESYSTEM |
> | `section9.chirality_mcp_status_dependencies` | RB-LIFECYCLE, RB-TOOL-SURFACE |
> | `section9.path_containment_hook` | RB-FILESYSTEM, RB-HOOKS |
> | `section9.instruction_root_protection_hook` | RB-FILESYSTEM, RB-HOOKS |
> | `section9.tool_result_budget` | RB-AUDIT, RB-REDACTION |
> | `section9.context_compaction_boundary` | RB-AUDIT, RB-HOOKS |
> | `section9.subagent_governance_hook` | RB-SUBAGENT, RB-HOOKS |
>

### CLM-012 — References

> ##### References
>
> - REF-001: `docs/DIRECTIVE.md`, especially §§2.7-2.11, §3, §4.2, and §5.
> - REF-002: `docs/CONTRACT.md`, especially K-AUTH, K-BIND, K-GATE, K-PROF, K-ENGINE, K-RELIANCE, K-SDK, K-EVENT, K-PERM, K-HOOK, K-STATUS, K-WRITE, K-SEAL, K-SUBAGENT, K-KEY.
> - REF-003: `docs/SPEC.md`, especially §§8.4, 9, 10, 12, 14, 15, and 19.3.
> - REF-004: `docs/TYPES.md`, especially runtime, permission, hook, SDK, subagent, and validation terms.
> - REF-005: `docs/PLAN.md`, especially R0/R1 reliance-boundary deliverables and acceptance.
> - REF-006: `docs/PRD.md`, especially §§8.12-8.16 and §15, under the current D-APP-38 corpus snapshot MATCH status.
> - REF-007: `AGENT_SOFTWARE_DECOMP.md`, especially no-invention and scope-boundary protocol.
>

### CLM-013 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; Bash is mode-gated with live default `ask` and workspace-write auto-allow only after hooks, not flatly denied by default.

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
> | RBR-004 | Runtime engine boundaries shall preserve `AgentEnginePort` / `RuntimeEngineContract` as product-owned and provider-neutral. | REF-001 §2.8-2.10; REF-002 K-ENGINE-1/K-ENGINE-4; REF-006 FR-122/FR-123 | `section9.runtime_engine_contract`; engine conformance suite review. |
> | RBR-005 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts and shall not become SDK-shaped except as adapter metadata. | REF-002 K-ENGINE-4; REF-003 §10.3; REF-006 FR-074/FR-116/FR-122 | Mapper tests; event-schema review; `section9.adapter_message_mapper`. |
> | RBR-006 | Accepted turns and terminal outcomes shall be persisted in an append-only Chirality audit mirror. | REF-001 §2.7-2.9; REF-002 K-EVENT-3/K-EVENT-4; REF-006 FR-072/FR-073 | `section9.adapter_turn_engine_event_log`; replay validation. |
> | RBR-007 | SDK transcripts shall be treated as secondary resume/debug artifacts unless explicitly imported into `HarnessEvent` form. | REF-001 §2.7-2.10; REF-002 K-SDK-3; REF-003 §8.4; REF-006 FR-121/KG-024 | Transcript-linkage tests remain `TBD`; register residual risk where default SDK paths remain. |
> | RBR-008 | Shipped SDK options shall use `settingSources: []`; `user` and `local` setting sources shall not be used in shipped builds. | REF-001 §4.2/§5; REF-002 K-SDK-1; REF-003 §12.2; REF-006 FR-117/KG-022 | `section9.settingsources_isolation`; release verification. |
> | RBR-009 | Permission decisions shall be structured, persisted, and recorded as `allow`, `deny`, or application-level `ask`. | REF-004 §8.2; REF-006 FR-087/FR-092; SOW-054 | `tool.permission` event tests; permission decision schema tests. |
> | RBR-010 | Deny rules shall override all allow decisions, including persona/session/operator allows and developer-local bypass. | REF-002 K-PERM-1; REF-006 FR-089 | `section9.permission_overlay_hard_deny_precedence`; targeted deny precedence tests. |
> | RBR-011 | `allowedTools` alone shall not be treated as a restriction boundary. | REF-002 K-PERM-3; REF-003 §14.3; REF-006 FR-081/KG-023 | SDK options builder tests showing restriction requires deny/mode/hook/callback policy. |
> | RBR-012 | Filesystem write/edit behavior shall enforce active project-root containment, instruction-root protection, and initial symlink write rejection. | REF-002 K-ROOT-2/K-PATH-2/K-PATH-3; REF-003 §15.2; REF-006 FR-095/FR-097 | `section9.path_containment_hook`; `section9.instruction_root_protection_hook`; write/edit tests. |
> | RBR-013 | Hook denials and hook failures shall fail closed for write, shell, domain, and subagent actions. | REF-002 K-HOOK-1; REF-003 §15.2; REF-006 FR-093-FR-095 | Hook lifecycle tests; denied action must not execute. |
> | RBR-014 | Bash shall remain denied by default until timeout, capture, storage, interrupt, and audit behavior are implemented and validated. | REF-002 K-BASH-1; REF-006 FR-100 | Bash deny/default tests; result-budget tests before enablement. |
> | RBR-015 | In-process Chirality MCP tools shall pass through the same permission, hook, redaction, and event logging policy as SDK built-ins. | REF-002 K-MCP-1; REF-003 §14.2; REF-006 FR-104/FR-119 | MCP wrapper tests; event and hook evidence. |
> | RBR-016 | Subagent execution shall fail closed unless governance, context sealing, approval reference, child tool restriction, and child cwd restriction pass. | REF-002 K-SEAL-1/K-SUBAGENT-1/K-SUBAGENT-2; REF-006 FR-101/FR-102/KG-027 | `section9.subagent_governance_hook`; child run record tests. |
> | RBR-017 | `_STATUS.md` shall remain the canonical lifecycle state file and human-gate transitions shall require human evidence. | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-001 §3 | Status transition API/MCP tests; approval SHA checks. |
> | RBR-018 | No agent, SDK, tool, runtime event, validator, or domain adapter shall claim to approve, certify, sign, seal, issue, transmit, or externally validate professional work. | REF-001 §3; REF-002 K-AUTH-1/K-PROF-1 | UI/docs copy review; human-gate checklist. |
> | RBR-019 | Runtime events, logs, tool artifacts, provider errors, and SDK interaction metadata shall redact API keys and configured secret variants. | REF-002 K-EVENT-6/K-KEY-1; REF-003 §12.3; REF-006 FR-075 | Redaction tests; run logger tests; artifact inspection. |
> | RBR-020 | The register shall preserve fallback criteria for SDK replacement if a product-critical boundary cannot be governed or verified. | REF-001 §2.8-2.10; REF-002 K-ENGINE-5; REF-006 FR-126/KG-030 | R0/R1 first-adapter probe review; fallback criteria row in register. |
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
> | `docs/PRD.md` | Product requirements and risk register, reconciled as REF-006 under the current D-APP-38 corpus snapshot. |
> | `AGENT_SOFTWARE_DECOMP.md` | Decomposition discipline; no-invention and scope-boundary rules. |
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
> | Prompt/SDK-default exclusion evidence | Acceptance evidence proves the row has a Chirality-owned, verified SDK callback/hook, MCP wrapper, release check, or human gate beyond prompt-only or opaque SDK-default behavior. |
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
> - residual-risk notes for unresolved first-adapter probe findings
> - authority-corpus version note for `docs/PRD.md` and any future drift warning
>

### CLM-022 — Open Items

> ##### Open Items
>
> | ID | Item | Status |
> |---|---|---|
> | OI-RBR-001 | Closed by the current D-APP-38 corpus snapshot; REF-006 currently matches. Reopen only if a future corpus audit reports drift. | CLOSED |
> | OI-RBR-002 | Fill exact implementation file paths for enforcement surfaces after the relevant runtime modules exist. | TBD |
> | OI-RBR-003 | Confirm SDK transcript placement decision after R1 probe. | TBD |
> | OI-RBR-004 | Current implemented Section 9 validation IDs are indexed in `docs/harness/reliance_boundary_register.md`; future `section9.reliance_boundary_register` and `section9.sdk_session_link_resume` remain TBD until validator/session-linkage work lands. | PARTIAL |
> | OI-RBR-005 | Generated register rows cite the current D-APP-38 corpus snapshot and distinguish current corpus-matched evidence from future drift warnings. | CLOSED |
>

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; Bash is mode-gated with live default `ask` and workspace-write auto-allow only after hooks, not flatly denied by default.

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
> | References | `_REFERENCES.md` read; REF-001 through REF-007 available. |
> | Dependency declarations | `_DEPENDENCIES.md` and `Dependencies.csv` read; extracted rows remain active/TBD dependency evidence. |
> | Decomposition entry | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-01-02 row read. |
> | Reference integrity | the current D-APP-38 corpus snapshot records REF-006 `docs/PRD.md` as `MATCH`. |
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
>    - SDK settings isolation;
>    - subagent governance;
>    - deterministic tool surface and MCP wrappers;
>    - hook lifecycle and fail-closed behavior;
>    - secret redaction and key handling;
>    - SDK fallback criteria.
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
> 1. Identify the enforcement owner:
>    - Chirality code;
>    - SDK option;
>    - SDK hook/callback;
>    - MCP wrapper;
>    - human gate;
>    - release check;
>    - prompt support;
>    - mixed.
> 2. Identify the concrete enforcement surface.
> 3. If the only surface is prompt support, mark the row incomplete for P0.
> 4. If the only surface is opaque SDK default behavior, mark the row incomplete for P0.
> 5. Add residual-risk notes where SDK behavior is not yet empirically verified.
>

### CLM-032 — 5. Attach Validation Evidence

> ###### 5. Attach Validation Evidence
>
> 1. Map rows to existing Section 9 validation IDs where available:
>    - `section9.runtime_engine_contract`
>    - `section9.adapter_turn_engine_event_log`
>    - `section9.adapter_message_mapper`
>    - `section9.session_event_replay`
>    - `section9.settingsources_isolation`
>    - `section9.permission_overlay_hard_deny_precedence`
>    - `section9.tool_runtime_read_file`
>    - `section9.chirality_mcp_status_dependencies`
>    - `section9.path_containment_hook`
>    - `section9.instruction_root_protection_hook`
>    - `section9.tool_result_budget`
>    - `section9.context_compaction_boundary`
>    - `section9.subagent_governance_hook`
> 2. Record SPEC/PRD-listed future validation IDs as `TBD` unless the current Section 9 script implements them:
>    - `section9.reliance_boundary_register`
>    - `section9.sdk_session_link_resume`
> 3. Use `TBD` for validation IDs not yet implemented or not yet named.
> 4. Add test index rows that connect each validation ID to one or more boundary IDs.
>

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
> 4. Confirm REF-006 is current under the current D-APP-38 corpus snapshot, or preserve any future drift warning.
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

> ##### Remaining Blockers
>
> | ID | Blocker | Required action |
> |---|---|---|
> | BLK-RBR-001 | REF-006 source-state | Closed by the current D-APP-38 corpus snapshot; reopen only if future authority-corpus status reports drift. |
> | BLK-RBR-002 | Exact implementation surfaces not yet complete | Downstream runtime implementation deliverables must fill file paths and tests. |
> | BLK-RBR-003 | SDK transcript and settings behavior require empirical probe | R0/R1 first-adapter probe and validation must confirm behavior before final acceptance. |

- **VER-001** — Deterministic validation, claim mapping, parity reporting, review-checklist derivation, and HTML-render checks, followed by human review.

## Governing Values and Decisions — Axiology

### CLM-039 — Guidance: DEL-01-02 Reliance Boundary Register

> #### Guidance: DEL-01-02 Reliance Boundary Register
>

### CLM-040 — Purpose

> ##### Purpose
>
> The Reliance Boundary Register exists to prevent product-critical Chirality semantics from drifting into prompt-only instruction, opaque SDK defaults, transient runtime state, or undocumented human assumptions. It should make the enforcement ownership of each boundary inspectable before implementation choices harden.
>
> The register is especially important because Chirality intentionally privileges the Claude Agent SDK as a runtime substrate while keeping product semantics, auditability, permission decisions, working-root policy, lifecycle rules, subagent governance, and professional-boundary language under Chirality ownership.
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

> ###### 3. Deny-First Means Deny Overrides All Allows
>
> The register should treat deny rules as the controlling policy for dangerous actions. A row that relies only on `allowedTools`, default SDK behavior, or persona instruction should be marked incomplete until paired with mode policy, `disallowedTools`, `canUseTool`, hooks, path checks, or equivalent Chirality-owned enforcement.
>

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

> ###### Source-State Handling
>
> `docs/PRD.md` is accessible and contains detailed runtime requirements and known gaps. D-APP-38 corpus
> `v1` reconciled the authority-doc reference corpus, and current `_REFERENCES.md` records REF-006
> `docs/PRD.md` as `MATCH`.
>
> Rows that depend on PRD content should cite REF-006 and the current corpus version. Future
> authority-doc edits must rerun the D-APP-38 reconciliation flow before issue-readiness reliance is
> claimed.
>

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

> ###### Current Implementation Surfaces And Path Maintenance
>
> Keep concrete register paths synchronized with the inspectable tree. Use `TBD` only for a genuinely absent or unassigned surface, and retain a downstream closure path for every such entry.
>
> | Surface | Current implementation path |
> |---|---|
> | `AgentEnginePort` | `frontend/packages/harness-contract/src/agent-engine-port.ts` |
> | `RuntimeEngineContract` | `frontend/src/lib/harness/agent-runtime-contract.ts` |
> | `TurnEngine` | `frontend/src/lib/harness/turn-engine.ts` |
> | `SdkOptionsBuilder` | `frontend/src/lib/harness/sdk-options-builder.ts` |
> | `ChiralityPermissionOverlay` | `frontend/src/lib/harness/permission-overlay.ts` |
> | `ChiralityHooks` / hook runner | `frontend/src/lib/harness/chirality-hooks.ts` |
> | `evaluateSubagentGovernance` bridge | `frontend/src/lib/harness/subagent-governance.ts` |
>

### CLM-052 — Residual Risk Topics

> ###### Residual Risk Topics
>
> Track these explicitly until closed:
>
> - SDK API drift and message/category changes.
> - SDK settings leakage if project/user/local setting sources are accidentally enabled.
> - SDK transcript placement outside the working root.
> - SDK permission semantics being necessary but insufficient.
> - SDK subagents inheriting powerful parent permissions.
> - Thin-wrapper drift where product identity becomes SDK-shaped.
> - Authority-doc corpus drift if a future edit changes `docs/PRD.md` or another corpus source without rerunning D-APP-38 reconciliation.
> - Section 9 validation IDs or test file names still being candidate labels rather than implemented checks.
>

### CLM-053 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | SDK leverage vs. product-owned semantics | Use SDK mechanics where verified, but keep public contracts, events, permissions, and records in Chirality terms. |
> | Early register completeness vs. implementation uncertainty | Draft all required boundary rows now; use `TBD` for exact implementation files until downstream deliverables exist. |
> | Human gate clarity vs. runtime automation | Automate evidence capture and state-transition checks, but keep binding approval human-only. |
> | Prompt support vs. hard enforcement | Prompt support is acceptable as an explanatory layer, not as the enforcement surface for P0 boundaries. |
> | Local audit mirror vs. SDK transcript richness | Keep Chirality JSONL canonical; link or mirror SDK transcripts only as secondary artifacts. |
>

### CLM-054 — Examples

> ##### Examples
>

### CLM-055 — Example Register Row Pattern

> ###### Example Register Row Pattern
>
> | Field | Example |
> |---|---|
> | BoundaryID | RB-SETTINGS |
> | BoundaryCategory | settings |
> | ProductSemantic | Shipped builds must not load ambient user/global or local Claude Code settings. |
> | SourceRefs | `docs/SPEC.md` §12.2; `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` FR-117 under the current D-APP-38 corpus snapshot |
> | EnforcementOwner | Chirality code + SDK option + release validation |
> | EnforcementSurface | `SdkOptionsBuilder` sets `settingSources: []`; settings isolation test; release verification |
> | PromptOnlyAllowed | NO |
> | SDKDefaultOnlyAllowed | NO |
> | ValidationID | `section9.settingsources_isolation` |
> | ResidualRisk | SDK option behavior must be empirically confirmed on pinned SDK version. |
> | DecisionStatus | TBD until implementation and probe pass |
>

### CLM-056 — Example Incomplete Row

> ###### Example Incomplete Row
>
> | Field | Example |
> |---|---|
> | BoundaryID | RB-SUBAGENT |
> | Incomplete signal | Enforcement surface says only "tell subagents not to write outside scope." |
> | Required correction | Add `evaluateSubagentGovernance`, restricted child tools/cwd, hook evidence, and child run record validation. |
>

### CLM-057 — Closed Source-State Note

> ##### Closed Source-State Note
>
> Historical conflict `CONF-RBR-001` is superseded by the current D-APP-38 corpus snapshot: `_REFERENCES.md` now records
> REF-006 `docs/PRD.md` as `MATCH`. That source-state reconciliation did not by itself generate the
> reliance-boundary register or satisfy dependency rows; it only removed the stale PRD hash blocker from
> the local-kit wording.
>

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

> ##### Assumptions and TBDs
>
> | ID | Item | Disposition |
> |---|---|---|
> | ASSUMPTION-RBR-001 | The decomposition-listed objectives OBJ-002, OBJ-005, and OBJ-009 are directionally relevant to DEL-01-02. | Supported by DEL-01-02 decomposition row; not an extra hard requirement beyond cited source requirements. |
> | TBD-RBR-001 | Exact implementation file paths for runtime contract, permissions, hooks, settings, event log, and subagent bridge. | RESOLVED for the currently named surfaces above; keep their register citations current and use `TBD` only for a genuinely absent or unassigned future surface. |
> | TBD-RBR-002 | Exact SDK transcript storage/mirroring decision. | Resolve after R1 first-adapter probe and session linkage work. |
> | TBD-RBR-003 | Final Section 9 validation file/test names. | Current implemented IDs are indexed in `docs/harness/reliance_boundary_register.md`; future `section9.reliance_boundary_register` and `section9.sdk_session_link_resume` remain TBD. |
> | TBD-RBR-004 | Generated-register completion evidence. | ADQ-02 generated and cross-checked `docs/harness/reliance_boundary_register.md`; future validator automation remains downstream. |
>

### CLM-060 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; Bash is mode-gated with live default `ask` and workspace-write auto-allow only after hooks, not flatly denied by default.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-037 SOW-045 SOW-054 SOW-057 SOW-074 OBJ-002 OBJ-005 OBJ-009 | CLM-014 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
