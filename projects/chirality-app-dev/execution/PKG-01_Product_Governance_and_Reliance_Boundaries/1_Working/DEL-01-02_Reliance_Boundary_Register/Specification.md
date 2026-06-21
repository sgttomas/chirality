# Specification: DEL-01-02 Reliance Boundary Register

## Scope

DEL-01-02 defines the requirements for a Reliance Boundary Register that maps product-critical Chirality semantics to concrete enforcement surfaces. The register covers P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, runtime-engine, tool-surface, hook, redaction, and fallback boundaries.

This specification covers the content and verification expectations for `docs/harness/reliance_boundary_register.md`, the enforcement matrix, and the test index. It does not implement the runtime modules themselves except to name the expected enforcement surfaces and validation hooks those modules must satisfy.

### In Scope

- Boundary taxonomy and stable boundary identifiers.
- Mapping from governance/source requirements to enforcement owner and enforcement surface.
- Explicit identification of product-owned versus SDK-provided behavior.
- P0 checks that prevent prompt-only or opaque SDK-default-only enforcement.
- Residual-risk entries where SDK behavior, transcript placement, or source-state evidence is not yet verified.
- Validation index entries for Section 9 runtime validation IDs where available.

### Out of Scope

- Implementing `AgentEnginePort`, `TurnEngine`, `SdkOptionsBuilder`, permission overlay, MCP tools, hooks, event store, or subagent bridge.
- Claiming acceptance of unresolved first-adapter probe items.
- Treating authority-doc references as current after a future authority-doc edit without rerunning the D-APP-38 reconciliation flow.
- Issuing professional approval or external validation.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| RBR-001 | The register shall identify each P0 reliance boundary with a stable `BoundaryID`, category, product semantic, source references, enforcement owner, enforcement surface, validation ID, residual risk, and decision status. | REF-002 K-RELIANCE-1; REF-006 FR-124 | Review generated register schema and row completeness. |
| RBR-002 | No P0 boundary shall be marked enforceable by prompt text alone. | REF-001 §2.9; REF-002 K-RELIANCE-2/K-PERM-2; REF-006 FR-124 | Check `PromptOnlyAllowed=NO` for every P0 row; flag exceptions as `CONFLICT`. |
| RBR-003 | No P0 boundary shall rely on opaque SDK defaults alone. | REF-001 §2.9; REF-002 K-RELIANCE-2; REF-006 FR-125 | Check enforcement owner/surface for Chirality code, verified SDK callback/hook, MCP wrapper, release check, or human gate. |
| RBR-004 | Runtime engine boundaries shall preserve `AgentEnginePort` / `RuntimeEngineContract` as product-owned and provider-neutral. | REF-001 §2.8-2.10; REF-002 K-ENGINE-1/K-ENGINE-4; REF-006 FR-122/FR-123 | `section9.runtime_engine_contract`; engine conformance suite review. |
| RBR-005 | Browser `UIEvent`s and persisted `HarnessEvent`s shall remain separate contracts and shall not become SDK-shaped except as adapter metadata. | REF-002 K-ENGINE-4; REF-003 §10.3; REF-006 FR-074/FR-116/FR-122 | Mapper tests; event-schema review; `section9.sdk_message_mapper`. |
| RBR-006 | Accepted turns and terminal outcomes shall be persisted in an append-only Chirality audit mirror. | REF-001 §2.7-2.9; REF-002 K-EVENT-3/K-EVENT-4; REF-006 FR-072/FR-073 | `section9.sdk_turn_engine_event_log`; replay validation. |
| RBR-007 | SDK transcripts shall be treated as secondary resume/debug artifacts unless explicitly imported into `HarnessEvent` form. | REF-001 §2.7-2.10; REF-002 K-SDK-3; REF-003 §8.4; REF-006 FR-121/KG-024 | Transcript-linkage tests; register residual risk where default SDK paths remain. |
| RBR-008 | Shipped SDK options shall use `settingSources: []`; `user` and `local` setting sources shall not be used in shipped builds. | REF-001 §4.2/§5; REF-002 K-SDK-1; REF-003 §12.2; REF-006 FR-117/KG-022 | `section9.settingsources_isolation`; release verification. |
| RBR-009 | Permission decisions shall be structured, persisted, and recorded as `allow`, `deny`, or application-level `ask`. | REF-004 §8.2; REF-006 FR-087/FR-092; SOW-054 | `tool.permission` event tests; permission decision schema tests. |
| RBR-010 | Deny rules shall override all allow decisions, including persona/session/operator allows and developer-local bypass. | REF-002 K-PERM-1; REF-006 FR-089 | `section9.permission_overlay_hard_deny_precedence`; targeted deny precedence tests. |
| RBR-011 | `allowedTools` alone shall not be treated as a restriction boundary. | REF-002 K-PERM-3; REF-003 §14.3; REF-006 FR-081/KG-023 | SDK options builder tests showing restriction requires deny/mode/hook/callback policy. |
| RBR-012 | Filesystem write/edit behavior shall enforce active project-root containment, instruction-root protection, and initial symlink write rejection. | REF-002 K-ROOT-2/K-PATH-2/K-PATH-3; REF-003 §15.2; REF-006 FR-095/FR-097 | `section9.path_containment_hook`; `section9.instruction_root_protection_hook`; write/edit tests. |
| RBR-013 | Hook denials and hook failures shall fail closed for write, shell, domain, and subagent actions. | REF-002 K-HOOK-1; REF-003 §15.2; REF-006 FR-093-FR-095 | Hook lifecycle tests; denied action must not execute. |
| RBR-014 | Bash shall remain denied by default until timeout, capture, storage, interrupt, and audit behavior are implemented and validated. | REF-002 K-BASH-1; REF-006 FR-100 | Bash deny/default tests; result-budget tests before enablement. |
| RBR-015 | In-process Chirality MCP tools shall pass through the same permission, hook, redaction, and event logging policy as SDK built-ins. | REF-002 K-MCP-1; REF-003 §14.2; REF-006 FR-104/FR-119 | MCP wrapper tests; event and hook evidence. |
| RBR-016 | Subagent execution shall fail closed unless governance, context sealing, approval reference, child tool restriction, and child cwd restriction pass. | REF-002 K-SEAL-1/K-SUBAGENT-1/K-SUBAGENT-2; REF-006 FR-101/FR-102/KG-027 | `section9.subagent_governance_hook`; child run record tests. |
| RBR-017 | `_STATUS.md` shall remain the canonical lifecycle state file and human-gate transitions shall require human evidence. | REF-002 K-STATUS-1/K-STATUS-2/K-GATE-1; REF-001 §3 | Status transition API/MCP tests; approval SHA checks. |
| RBR-018 | No agent, SDK, tool, runtime event, validator, or domain adapter shall claim to approve, certify, sign, seal, issue, transmit, or externally validate professional work. | REF-001 §3; REF-002 K-AUTH-1/K-PROF-1 | UI/docs copy review; human-gate checklist. |
| RBR-019 | Runtime events, logs, tool artifacts, provider errors, and SDK interaction metadata shall redact API keys and configured secret variants. | REF-002 K-EVENT-6/K-KEY-1; REF-003 §12.3; REF-006 FR-075 | Redaction tests; run logger tests; artifact inspection. |
| RBR-020 | The register shall preserve fallback criteria for SDK replacement if a product-critical boundary cannot be governed or verified. | REF-001 §2.8-2.10; REF-002 K-ENGINE-5; REF-006 FR-126/KG-030 | R0/R1 first-adapter probe review; fallback criteria row in register. |
| RBR-021 | The register shall record the current D-APP-38 corpus version for authority-doc references, including REF-006 `docs/PRD.md`. | `_REFERENCES.md`; D-APP-38 | Register metadata cites corpus `v1` and current `MATCH` status. |
| RBR-022 | The register shall distinguish current corpus-matched source support from any future drift or warning-limited source support in row-level traces where PRD content affects acceptance. | REF-001 §2.1/§2.7; REF-002 K-REF-1/K-INVENT-1; `_REFERENCES.md` REF-006 | Source trace review confirms PRD-cited rows cite REF-006 and the current corpus version, or preserve a drift warning if reconciliation later reports one. |
| RBR-023 | Final acceptance shall include evidence that no P0 boundary is enforced only by prompt text or by opaque SDK defaults. | REF-001 §2.9; REF-002 K-RELIANCE-2; REF-006 FR-124/FR-125 | Generated register review includes explicit `PromptOnlyAllowed=NO`, `SDKDefaultOnlyAllowed=NO`, and non-empty enforcement-surface evidence for every P0 row. |
| RBR-024 | Exact implementation file paths, hook names, check names, and validation files shall remain `TBD` until downstream deliverables produce inspectable artifacts. | REF-002 K-INVENT-1; REF-003 §19.3; decomposition DEL-03/DEL-04/DEL-06/DEL-09 rows | Open item review confirms each `TBD` has a downstream closure path or accepted conflict entry. |
| RBR-025 | After `docs/harness/reliance_boundary_register.md` is generated, each register row shall be cross-checked against this specification, the datasheet field schema, and the test index. | REF-003 §19.3; REF-005 R0/R1 acceptance notes | Review record shows all rows map to requirements, source references, validation IDs or `TBD`, and residual risks. |

## Standards

| Standard / authority | Applicability |
|---|---|
| `docs/DIRECTIVE.md` | Product intent, reliance-boundary principles, human authority, provider-neutral core. |
| `docs/CONTRACT.md` | Binding invariant catalog; primary normative requirements for this specification. |
| `docs/SPEC.md` | Runtime structures, settings, hooks, MCP, validation IDs, and API/file contracts. |
| `docs/TYPES.md` | Terms and target type names used in the register. |
| `docs/PLAN.md` | Runtime roadmap and R0/R1 reliance-boundary acceptance expectations. |
| `docs/PRD.md` | Product requirements and risk register, reconciled as REF-006 under D-APP-38 corpus `v1`. |
| `AGENT_SOFTWARE_DECOMP.md` | Decomposition discipline; no-invention and scope-boundary rules. |

## Verification

| Check | Expected evidence |
|---|---|
| Schema completeness | Every register row includes the fields listed in `Datasheet.md` "Minimum Register Fields." |
| Coverage completeness | Rows exist for audit, permission, filesystem, lifecycle, transcript, settings, subagent, human-gate, runtime-engine, tool-surface, hooks, redaction, and fallback boundaries. |
| Source traceability | Each row cites at least one governance/source reference and uses `location TBD` where exact implementation files are unavailable. |
| P0 enforcement posture | P0 rows have `PromptOnlyAllowed=NO` and `SDKDefaultOnlyAllowed=NO`. |
| Prompt/SDK-default exclusion evidence | Acceptance evidence proves the row has a Chirality-owned, verified SDK callback/hook, MCP wrapper, release check, or human gate beyond prompt-only or opaque SDK-default behavior. |
| PRD source-state trace | Rows using REF-006 cite the current corpus-matched source state or explicitly preserve any future drift warning. |
| Validation mapping | Rows map to Section 9 validation IDs where listed in `docs/SPEC.md`; missing IDs remain `TBD`. |
| Residual-risk surfacing | Authority-corpus drift, SDK transcript placement, SDK API drift, and inherited subagent permission risks are recorded instead of silently resolved. |
| Cross-document consistency | Datasheet boundary IDs, Specification requirement IDs, Guidance principles, and Procedure verification steps use the same terminology. |

## Documentation

The final work package should include:

- `docs/harness/reliance_boundary_register.md`
- enforcement matrix
- test index keyed to Section 9 validation IDs and other implementation checks
- residual-risk notes for unresolved first-adapter probe findings
- authority-corpus version note for `docs/PRD.md` and any future drift warning

## Open Items

| ID | Item | Status |
|---|---|---|
| OI-RBR-001 | Closed by D-APP-38 corpus `v1`; REF-006 currently matches. Reopen only if a future corpus audit reports drift. | CLOSED |
| OI-RBR-002 | Fill exact implementation file paths for enforcement surfaces after the relevant runtime modules exist. | TBD |
| OI-RBR-003 | Confirm SDK transcript placement decision after R1 probe. | TBD |
| OI-RBR-004 | Confirm exact Section 9 validation implementation IDs as runtime phases land. | TBD |
| OI-RBR-005 | Confirm generated register rows cite D-APP-38 corpus version and distinguish current corpus-matched evidence from any future drift warning. | TBD |
