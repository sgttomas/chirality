# Datasheet: DEL-01-02 Reliance Boundary Register

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-01-02 |
| DeliverableName | Reliance Boundary Register |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | REQ_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Current lifecycle source | `_STATUS.md` |
| Draft pass | P1/P2 |
| Primary artifact | `docs/harness/reliance_boundary_register.md` |
| Supporting artifacts | enforcement matrix and test index embedded in `docs/harness/reliance_boundary_register.md` |

## Attributes

### Source State

| RefID | Source | Status | Use in this datasheet |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH | Product intent, authority, reliance-boundary and professional-boundary rules |
| REF-002 | `docs/CONTRACT.md` | MATCH | Binding invariants and enforcement expectations |
| REF-003 | `docs/SPEC.md` | MATCH | Runtime structures, API/file contracts, hooks, settings, validation IDs |
| REF-004 | `docs/TYPES.md` | MATCH | Vocabulary and type targets |
| REF-005 | `docs/PLAN.md` | MATCH | Runtime roadmap and R0 reliance-boundary deliverable expectations |
| REF-006 | `docs/PRD.md` | MATCH | Current product requirements and approved vNext scope under D-APP-38 corpus `v1` |
| REF-007 | `AGENT_SOFTWARE_DECOMP.md` | MATCH | Decomposition discipline and no-invention constraints |

### Decomposition Traceability

| Trace item | Value |
|---|---|
| Scope description | Map every P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundary to a concrete enforcement surface. |
| CoversScopeItems | SOW-037, SOW-045, SOW-054, SOW-057, SOW-074 |
| SupportsObjectives | OBJ-002, OBJ-005, OBJ-009 |
| Directional objective context | ASSUMPTION: OBJ-002, OBJ-005, and OBJ-009 are relevant because the decomposition entry explicitly lists them for DEL-01-02. |

### Boundary Taxonomy

| Boundary ID | Boundary | Product-critical semantic | Primary enforcement surface | Source support |
|---|---|---|---|---|
| RB-ENGINE | Runtime engine contract | SDK APIs must not define public Chirality semantics. | `AgentEnginePort` / `RuntimeEngineContract`; engine conformance tests; adapter boundary | REF-001 §2.8-2.10; REF-002 K-ENGINE-1/K-ENGINE-4; REF-006 FR-122/FR-123 |
| RB-AUDIT | Runtime audit mirror | Accepted turns and runtime outcomes must be recoverable in Chirality terms. | `.chirality/sessions/<sessionId>/events.jsonl`; `HarnessEvent` schema; replay tests | REF-001 §2.7-2.9; REF-002 K-EVENT-4; REF-003 §8.4/§19.3; REF-006 FR-072-FR-074/FR-121 |
| RB-PERMISSION | Permission decisions | Tool and runtime permissions are structured, persisted, and governed by capability-forward policy with explicit hard-deny precedence. | `ChiralityPermissionOverlay`; `HarnessPermissionDecision`; `tool.permission` events | REF-002 K-PERM-1/K-PERM-3; REF-003 §15; REF-004 §8; REF-006 FR-087-FR-092 |
| RB-FILESYSTEM | Filesystem writes and roots | Writes must stay inside the active project root and must not mutate instruction-root assets. | Path containment helpers; `PreToolUse` hooks; MCP wrappers; symlink write rejection | REF-001 §2.7/§5; REF-002 K-ROOT-2/K-PATH-2/K-PATH-3; REF-003 §15.2; REF-006 FR-095/FR-097 |
| RB-LIFECYCLE | Deliverable lifecycle and gates | `_STATUS.md` is canonical and human gates are non-delegable. | Status parser; status transition API/MCP; approval SHA checks for human-gate states | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-003 lifecycle sections; REF-001 §3 |
| RB-TRANSCRIPT | SDK transcript separation | SDK transcripts are secondary and must not displace the Chirality audit mirror. | SDK session linkage metadata; local `SessionStore`/`CLAUDE_CONFIG_DIR` where reliable; residual-risk register entry when default SDK paths remain | REF-001 §2.8-2.10; REF-002 K-SDK-3; REF-003 §8.4/§12.4; REF-006 FR-118/FR-121/KG-024 |
| RB-SETTINGS | SDK settings isolation | Shipped builds must not load ambient user/global or local Claude Code settings. | `settingSources: []`; `SdkOptionsBuilder` tests; release verification | REF-001 §4.2/§5; REF-002 K-SDK-1; REF-003 §12.2; REF-006 FR-117/KG-022 |
| RB-SUBAGENT | Subagent delegation | Type 2 child runs cannot expand authority or inherit unsafe tool posture. | `evaluateSubagentGovernance`; subagent hooks; restricted child tools/cwd; child run records | REF-002 K-SEAL-1/K-SUBAGENT-1/K-SUBAGENT-2; REF-003 §15.2; REF-004 subagent terms; REF-006 FR-101/FR-102/KG-027 |
| RB-HUMAN-GATE | Human authority | No agent, SDK, tool, runtime event, or validator can approve, certify, sign, seal, issue, or externally validate work for reliance. | Human approval workflow; status transition policy; UI/document copy; release checks | REF-001 §3; REF-002 K-AUTH-1/K-BIND-1/K-GATE-1/K-PROF-1; REF-006 KG-015 |
| RB-TOOL-SURFACE | Tool exposure | Tool availability must be deterministic and permission-filtered; `allowedTools` alone is not a restriction boundary. | Tool resolver; `disallowedTools`; mode policy; `canUseTool`; hooks; tests | REF-002 K-TOOL-1/K-TOOL-2/K-PERM-3; REF-003 §14.3; REF-006 FR-078-FR-083/KG-023 |
| RB-HOOKS | Hook lifecycle and fail-closed behavior | Hook failures block write, shell, domain, and subagent actions. | SDK hook callbacks mapped through Chirality hooks; hook events; failure triage | REF-002 K-HOOK-1; REF-003 §15.2; REF-004 §8.5; REF-006 FR-093-FR-095 |
| RB-REDACTION | Secrets and sensitive runtime records | API keys and secret variants must not be persisted in logs, events, SDK transcripts if avoidable, or tool artifacts. | SafeStorage/env precedence; redaction helper; run logger tests; event/log redaction | REF-002 K-EVENT-6/K-KEY-1; REF-003 §12.3; REF-006 FR-075 |
| RB-FALLBACK | SDK fallback | A governed fallback/custom-runtime path remains necessary if an SDK behavior cannot satisfy a critical boundary. | R0/R1 first-adapter probe; fallback criteria; conformance suite; reliance-boundary register residual-risk entries | REF-001 §2.8-2.10; REF-002 K-ENGINE-5; REF-006 FR-126/KG-030 |

## Conditions

| Condition | Value |
|---|---|
| P0 boundary rule | P0 reliance boundaries cannot be prompt-only or opaque SDK-default-only. |
| Register coverage rule | The register must identify ownership for product-critical semantics and record the enforcement surface type. |
| Settings isolation condition | Shipped SDK options use `settingSources: []`; `user` and `local` setting sources are not used in shipped builds. |
| Permission condition | Permission decisions are recorded as `allow`, `deny`, or application-level `ask`; deny rules override allow decisions. |
| Transcript condition | SDK transcripts may support resume/debugging but `.chirality/sessions/<sessionId>/events.jsonl` remains canonical unless imported into `HarnessEvent` form. |
| Human-gate condition | Reliance-affecting approval remains human-only and evidence-bound. |
| Authority-corpus condition | Authority-doc references, including REF-006 `docs/PRD.md`, are reconciled to D-APP-38 corpus `v1` at this source state. |
| Source trace acceptance condition | Register rows that cite `docs/PRD.md` must cite REF-006 and should be rechecked if a later authority-corpus audit reports drift. |
| Register artifact condition | ADQ-02 generated `docs/harness/reliance_boundary_register.md` as CHECKING-stage evidence, not issuance or dependency closure. |
| Implementation-surface completion condition | Exact module paths, hook/check names, and validation file names remain `TBD` until downstream runtime and Section 9 deliverables produce inspectable artifacts. |

## Construction

### Minimum Register Fields

| Field | Purpose | Status |
|---|---|---|
| BoundaryID | Stable identifier for each reliance boundary | Required |
| BoundaryCategory | Audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, engine, tool-surface, hook, redaction, fallback | Required |
| ProductSemantic | Chirality-owned behavior being protected | Required |
| SourceRefs | Evidence locations from directive, contract, spec, PRD, types, plan, and decomposition | Required |
| EnforcementOwner | Chirality code, SDK option, SDK hook/callback, MCP wrapper, human gate, release check, prompt support, or mixed | Required |
| EnforcementSurface | Concrete module/API/file/test/check where enforcement is expected | Required; `TBD` until implemented |
| PromptOnlyAllowed | Must be `NO` for P0 boundaries | Required |
| SDKDefaultOnlyAllowed | Must be `NO` for P0 boundaries | Required |
| ValidationID | Section 9 or other test/check ID | Required where available; otherwise `TBD` |
| ResidualRisk | Known unresolved risk or source-state warning | Required when applicable |
| DecisionStatus | `TBD`, `PROPOSED`, `ACCEPTED`, or `CONFLICT` | Required |

### Deferred Completion Fields

| Deferred field | Current handling | Closure evidence required |
|---|---|---|
| ResponsibleParty | `TBD` by scaffold policy until human assignment. | Human-maintained ownership update in deliverable status/context or accepted downstream ownership record. |
| Exact enforcement file paths | ADQ-02 register rows name current inspectable runtime paths where present and preserve `TBD` where downstream modules do not yet exist. | Downstream implementation paths or register rows verified against produced modules and hooks. |
| Exact validation file/test names | Current implemented Section 9 IDs are listed in the ADQ-02 register test index; future IDs remain `TBD` where not yet produced. | Section 9 validation additions or accepted test index entries. |
| PRD-derived rows | May be drafted from REF-006 under D-APP-38 corpus `v1` with current `MATCH` status. | Re-run D-APP-38 reconciliation if an authority document changes before issue-readiness reliance. |
| SDK transcript/storage decision | Residual risk until R0/R1 probe evidence is available. | Accepted first-adapter probe result naming transcript placement or mirroring policy. |

### Candidate Validation Index

| Validation ID | Boundary coverage |
|---|---|
| `section9.runtime_engine_contract` | RB-ENGINE, RB-FALLBACK |
| `section9.adapter_turn_engine_event_log` | RB-AUDIT, RB-TRANSCRIPT |
| `section9.adapter_message_mapper` | RB-ENGINE, RB-AUDIT |
| `section9.session_event_replay` | RB-AUDIT |
| `section9.reliance_boundary_register` | Future/TBD validator ID; ADQ-02 generated the document artifact and cross-check table but did not add this ID to the current Section 9 script. |
| `section9.settingsources_isolation` | RB-SETTINGS |
| `section9.sdk_session_link_resume` | Future/TBD session-linkage validator ID; not implemented in the current Section 9 script. |
| `section9.permission_overlay_hard_deny_precedence` | RB-PERMISSION, RB-TOOL-SURFACE |
| `section9.tool_runtime_read_file` | RB-TOOL-SURFACE, RB-FILESYSTEM |
| `section9.chirality_mcp_status_dependencies` | RB-LIFECYCLE, RB-TOOL-SURFACE |
| `section9.path_containment_hook` | RB-FILESYSTEM, RB-HOOKS |
| `section9.instruction_root_protection_hook` | RB-FILESYSTEM, RB-HOOKS |
| `section9.tool_result_budget` | RB-AUDIT, RB-REDACTION |
| `section9.context_compaction_boundary` | RB-AUDIT, RB-HOOKS |
| `section9.subagent_governance_hook` | RB-SUBAGENT, RB-HOOKS |

## References

- REF-001: `docs/DIRECTIVE.md`, especially §§2.7-2.11, §3, §4.2, and §5.
- REF-002: `docs/CONTRACT.md`, especially K-AUTH, K-BIND, K-GATE, K-PROF, K-ENGINE, K-RELIANCE, K-SDK, K-EVENT, K-PERM, K-HOOK, K-STATUS, K-WRITE, K-SEAL, K-SUBAGENT, K-KEY.
- REF-003: `docs/SPEC.md`, especially §§8.4, 9, 10, 12, 14, 15, and 19.3.
- REF-004: `docs/TYPES.md`, especially runtime, permission, hook, SDK, subagent, and validation terms.
- REF-005: `docs/PLAN.md`, especially R0/R1 reliance-boundary deliverables and acceptance.
- REF-006: `docs/PRD.md`, especially §§8.12-8.16 and §15, under D-APP-38 corpus `v1` MATCH status.
- REF-007: `AGENT_SOFTWARE_DECOMP.md`, especially no-invention and scope-boundary protocol.
