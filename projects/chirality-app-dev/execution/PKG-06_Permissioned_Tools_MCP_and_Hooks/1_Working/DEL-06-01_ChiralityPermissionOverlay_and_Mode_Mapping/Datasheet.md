# Datasheet: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-06-01 |
| Deliverable name | ChiralityPermissionOverlay and Mode Mapping |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Type | SECURITY_CONTROL |
| Responsible party | TBD |
| Decomposition variant | SOFTWARE_DECOMP v3.2 |
| Context envelope | M |
| Scope items | SOW-054, SOW-055, SOW-056, SOW-058 |
| Objective context | OBJ-005 |
| Anticipated artifacts | Permission overlay module; decision records; readOnly/dontAsk/ask tests |

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` sections "PKG-06 Permissioned Tools, MCP, and Hooks" and scope ledger rows SOW-054 through SOW-058.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary control | `ChiralityPermissionOverlay` | `docs/PRD.md` Section 9.4, HASH_MISMATCH warning; decomposition glossary |
| Decision record | `HarnessPermissionDecision` with `allow`, `deny`, or application-level `ask` | `docs/TYPES.md` Section 8.2 |
| Decision sources | `sdk-option`, `sdk-callback`, `chirality-policy`, `hook`, `human`, `prompt-support` | `docs/TYPES.md` Section 8.2 |
| Permission modes in scope | `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, `bypass` | `docs/TYPES.md` Section 8.1; `docs/SPEC.md` Section 15.1 |
| Core precedence rule | Deny overrides allow | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/PRD.md` NFR-007, HASH_MISMATCH warning |
| Restriction boundary | `allowedTools` alone is not a restriction boundary | `docs/CONTRACT.md` Section 1.6 K-PERM-3; `docs/SPEC.md` Section 14.3; `docs/PRD.md` KG-023, HASH_MISMATCH warning |
| Interactive approval path | `canUseTool` mediates application approval; decision must be persisted before returning SDK allow/deny | `docs/SPEC.md` Section 15.1; decomposition row SOW-058 |
| Event obligation | Persist `tool.permission` events for governed tool attempts | `docs/PRD.md` R2 acceptance, HASH_MISMATCH warning; decomposition row SOW-056 |

## Conditions

| Condition | Constraint | Source |
|---|---|---|
| PRD source state | `docs/PRD.md` is accessible but has HASH_MISMATCH in `_REFERENCES.md`; PRD-derived details are treated as source-state-warning evidence, not as unqualified accepted truth. | `_REFERENCES.md` REF-006 |
| Read-only mode | Must not expose or allow write/edit/bash/network-capable actions. | `docs/CONTRACT.md` Section 1.6 K-PERM-4; `docs/TYPES.md` Section 8.1 |
| `dontAsk` mode | Denies unapproved actions without prompting; unapproved writes, shell, network, and unknown tools deny. | `docs/CONTRACT.md` Section 1.6 K-PERM-5; `docs/TYPES.md` Section 8.1 |
| `ask` mode | Application may request interactive approval for governed actions; SDK callback ultimately returns allow or deny. | `docs/TYPES.md` Sections 8.1 and 8.2 |
| `bypass` mode | Developer-local only, never shipped ordinary mode, and still subject to Chirality denies. | `docs/TYPES.md` Section 8.1; `docs/SPEC.md` Section 15.1 |
| Hook separation | DEL-06-01 covers permission policy and approval mediation; detailed hook implementation is assigned to DEL-06-04 and DEL-06-06. | `_CONTEXT.md`; decomposition PKG-06 rows |

## Construction

| Component | Construction note | Source |
|---|---|---|
| Overlay input | Session/persona/mode/tool/policy context needed to decide tool permission. Exact interface shape: TBD. | `docs/PRD.md` Section 9.4, HASH_MISMATCH warning; `docs/SPEC.md` Section 15.1 |
| Mode mapper | Maps Chirality modes to SDK posture plus overlay behavior. | `docs/SPEC.md` Section 15.1 |
| Deny evaluation | Any explicit deny from policy, path containment, hook, governance, SDK deny rule, or human gate blocks execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1 |
| Decision persistence | A structured permission decision is recorded before downstream execution or before returning an SDK approval result. | `docs/TYPES.md` Section 8.2; decomposition rows SOW-054 and SOW-058 |
| Event integration | Tool attempts emit permission/start/completion/failure events in the R2 scope. | `docs/PRD.md` R2 implementation targets, HASH_MISMATCH warning; `docs/TYPES.md` Section 7.3 later event categories |
| Tests | Include readOnly, dontAsk, and ask behavior tests. Exact test paths and fixtures: TBD. | `_CONTEXT.md`; decomposition DEL-06-01 anticipated artifacts |

## References

| RefID | Source | Use | Source state |
|---|---|---|---|
| REF-002 | `docs/CONTRACT.md` Section 1.6 | Binding permission, tool, MCP, hook, path, and bash invariants | MATCH |
| REF-003 | `docs/SPEC.md` Sections 14 and 15 | Tool names, MCP tools, tool surface rules, mode mapping, hook requirements | MATCH |
| REF-004 | `docs/TYPES.md` Section 8 | Permission modes, decision record, tool-surface terms | MATCH |
| REF-005 | `docs/PLAN.md` R2 and R3 | Sequencing and acceptance context | MATCH |
| REF-006 | `docs/PRD.md` Sections 9.4, R2, R3, NFR-007, KG-023 | Product requirements and implementation direction | HASH_MISMATCH warning |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Deliverable scope, SOW coverage, package boundaries | accepted v3.2 working surface |
