# Guidance: DEL-01-02 Reliance Boundary Register

## Purpose

The Reliance Boundary Register exists to prevent product-critical Chirality semantics from drifting into prompt-only instruction, opaque SDK defaults, transient runtime state, or undocumented human assumptions. It should make the enforcement ownership of each boundary inspectable before implementation choices harden.

The register is especially important because Chirality intentionally privileges the Claude Agent SDK as a runtime substrate while keeping product semantics, auditability, permission decisions, working-root policy, lifecycle rules, subagent governance, and professional-boundary language under Chirality ownership.

## Principles

### 1. Register Product Semantics, Not Vendor Mechanics

Use Chirality terms for public behavior and canonical records. SDK tool names, message names, session IDs, transcript paths, hook names, and permission modes may appear as adapter metadata, but they should not become the register's primary semantics.

### 2. P0 Boundaries Need Enforceable Surfaces

For P0 audit, permission, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries, prompt text can support user understanding but cannot be the enforcement surface. Each P0 row should name a concrete code path, hook, option, MCP wrapper, validation check, release check, or human gate.

### 3. Deny-First Means Deny Overrides All Allows

The register should treat deny rules as the controlling policy for dangerous actions. A row that relies only on `allowedTools`, default SDK behavior, or persona instruction should be marked incomplete until paired with mode policy, `disallowedTools`, `canUseTool`, hooks, path checks, or equivalent Chirality-owned enforcement.

### 4. Canonical Audit Is Chirality-Owned

SDK transcripts can help with resume/debugging, but the canonical runtime audit mirror is the Chirality event log unless SDK content is imported into `HarnessEvent` form. The register should call out transcript placement and mirror reliability as residual risk until empirically proven.

### 5. Human Authority Is Not Runtime Automatable

No runtime event, validation pass, agent output, or SDK callback can approve, sign, seal, issue, certify, transmit, or externally validate professional work. Human-gate rows should focus on preserving evidence-bound review and preventing misleading product copy or state transitions.

### 6. Unknowns Stay Visible

If a module, validation ID, SDK behavior, transcript location, or release check does not yet exist, use `TBD` or a residual-risk note. Do not smooth over gaps by assuming later implementation will satisfy the boundary.

## Considerations

### Source-State Handling

`docs/PRD.md` is accessible and contains detailed runtime requirements and known gaps. D-APP-38 corpus
`v1` reconciled the authority-doc reference corpus, and current `_REFERENCES.md` records REF-006
`docs/PRD.md` as `MATCH`.

Rows that depend on PRD content should cite REF-006 and the current corpus version. Future
authority-doc edits must rerun the D-APP-38 reconciliation flow before issue-readiness reliance is
claimed.

### Boundary Granularity

Rows should be fine-grained enough that a reviewer can answer:

- What product semantic is protected?
- What could go wrong if this boundary is delegated to SDK defaults or prompt text?
- Which component enforces it?
- Which test or human review proves it?
- What residual risk remains?

Rows should not be so granular that every implementation function becomes its own governance item. Use one boundary row per product-critical semantic, then point to multiple enforcement surfaces when needed.

For required register fields, use mandatory completion criteria rather than advisory wording: each row must name the protected product semantic, source evidence, enforcement owner, enforcement surface, prompt-only posture, SDK-default-only posture, validation evidence or `TBD`, residual risk, and decision status.

### Current Implementation Surfaces And Path Maintenance

Keep concrete register paths synchronized with the inspectable tree. Use `TBD` only for a genuinely absent or unassigned surface, and retain a downstream closure path for every such entry.

| Surface | Current implementation path |
|---|---|
| `AgentEnginePort` | `frontend/packages/harness-contract/src/agent-engine-port.ts` |
| `RuntimeEngineContract` | `frontend/src/lib/harness/agent-runtime-contract.ts` |
| `TurnEngine` | `frontend/src/lib/harness/turn-engine.ts` |
| `SdkOptionsBuilder` | `frontend/src/lib/harness/sdk-options-builder.ts` |
| `ChiralityPermissionOverlay` | `frontend/src/lib/harness/permission-overlay.ts` |
| `ChiralityHooks` / hook runner | `frontend/src/lib/harness/chirality-hooks.ts` |
| `evaluateSubagentGovernance` bridge | `frontend/src/lib/harness/subagent-governance.ts` |

### Residual Risk Topics

Track these explicitly until closed:

- SDK API drift and message/category changes.
- SDK settings leakage if project/user/local setting sources are accidentally enabled.
- SDK transcript placement outside the working root.
- SDK permission semantics being necessary but insufficient.
- SDK subagents inheriting powerful parent permissions.
- Thin-wrapper drift where product identity becomes SDK-shaped.
- Authority-doc corpus drift if a future edit changes `docs/PRD.md` or another corpus source without rerunning D-APP-38 reconciliation.
- Section 9 validation IDs or test file names still being candidate labels rather than implemented checks.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| SDK leverage vs. product-owned semantics | Use SDK mechanics where verified, but keep public contracts, events, permissions, and records in Chirality terms. |
| Early register completeness vs. implementation uncertainty | Draft all required boundary rows now; use `TBD` for exact implementation files until downstream deliverables exist. |
| Human gate clarity vs. runtime automation | Automate evidence capture and state-transition checks, but keep binding approval human-only. |
| Prompt support vs. hard enforcement | Prompt support is acceptable as an explanatory layer, not as the enforcement surface for P0 boundaries. |
| Local audit mirror vs. SDK transcript richness | Keep Chirality JSONL canonical; link or mirror SDK transcripts only as secondary artifacts. |

## Examples

### Example Register Row Pattern

| Field | Example |
|---|---|
| BoundaryID | RB-SETTINGS |
| BoundaryCategory | settings |
| ProductSemantic | Shipped builds must not load ambient user/global or local Claude Code settings. |
| SourceRefs | `docs/SPEC.md` §12.2; `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` FR-117 under the current D-APP-38 corpus snapshot |
| EnforcementOwner | Chirality code + SDK option + release validation |
| EnforcementSurface | `SdkOptionsBuilder` sets `settingSources: []`; settings isolation test; release verification |
| PromptOnlyAllowed | NO |
| SDKDefaultOnlyAllowed | NO |
| ValidationID | `section9.settingsources_isolation` |
| ResidualRisk | SDK option behavior must be empirically confirmed on pinned SDK version. |
| DecisionStatus | TBD until implementation and probe pass |

### Example Incomplete Row

| Field | Example |
|---|---|
| BoundaryID | RB-SUBAGENT |
| Incomplete signal | Enforcement surface says only "tell subagents not to write outside scope." |
| Required correction | Add `evaluateSubagentGovernance`, restricted child tools/cwd, hook evidence, and child run record validation. |

## Closed Source-State Note

Historical conflict `CONF-RBR-001` is superseded by the current D-APP-38 corpus snapshot: `_REFERENCES.md` now records
REF-006 `docs/PRD.md` as `MATCH`. That source-state reconciliation did not by itself generate the
reliance-boundary register or satisfy dependency rows; it only removed the stale PRD hash blocker from
the local-kit wording.

## Generated Artifact Note

ADQ-02 generated `docs/harness/reliance_boundary_register.md` with the central row register, embedded
enforcement matrix, current Section 9 test index, and future/TBD validation-ID notes. This is
CHECKING-stage evidence only; it does not mutate `_STATUS.md`, satisfy dependency rows, or authorize
issuance, release readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance.

## Assumptions and TBDs

| ID | Item | Disposition |
|---|---|---|
| ASSUMPTION-RBR-001 | The decomposition-listed objectives OBJ-002, OBJ-005, and OBJ-009 are directionally relevant to DEL-01-02. | Supported by DEL-01-02 decomposition row; not an extra hard requirement beyond cited source requirements. |
| TBD-RBR-001 | Exact implementation file paths for runtime contract, permissions, hooks, settings, event log, and subagent bridge. | RESOLVED for the currently named surfaces above; keep their register citations current and use `TBD` only for a genuinely absent or unassigned future surface. |
| TBD-RBR-002 | Exact SDK transcript storage/mirroring decision. | Resolve after R1 first-adapter probe and session linkage work. |
| TBD-RBR-003 | Final Section 9 validation file/test names. | Current implemented IDs are indexed in `docs/harness/reliance_boundary_register.md`; future `section9.reliance_boundary_register` and `section9.sdk_session_link_resume` remain TBD. |
| TBD-RBR-004 | Generated-register completion evidence. | ADQ-02 generated and cross-checked `docs/harness/reliance_boundary_register.md`; future validator automation remains downstream. |

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-100/101/102 supersede the earlier future/TBD cells: `section9.sdk_session_link_resume` and `section9.domain_profile_validation` are implemented and registered under their ruled scopes; Bash is mode-gated with live default `ask` and workspace-write auto-allow only after hooks, not flatly denied by default.
