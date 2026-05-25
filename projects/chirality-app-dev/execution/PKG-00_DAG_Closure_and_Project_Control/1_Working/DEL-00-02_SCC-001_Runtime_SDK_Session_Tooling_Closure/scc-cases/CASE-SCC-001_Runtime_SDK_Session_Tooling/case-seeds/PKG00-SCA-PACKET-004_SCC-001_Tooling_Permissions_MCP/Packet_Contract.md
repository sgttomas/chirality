# Packet Contract: PKG00-SCA-PACKET-004

## Identity

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-004 |
| Title | SCC-001 Tooling Permissions MCP |
| SCC | SCC-001 |
| Variant | SOFTWARE |
| RequestedBy | WORKING_ITEMS |
| Scope | PKG-00 control deliverable packet for later human-gated SCOPE_CHANGE intake |

## Authority Limits

This packet is a derivative staging artifact. It consumes accepted upstream decomposition and DepClosure evidence, plus affected deliverable dependency registers, but it is not authoritative decomposition truth and is not a dependency ruling.

This packet does not update product deliverables, `Dependencies.csv`, decomposition files, `_ScopeChange`, `_Reconciliation`, or coordination files. It does not initiate SCOPE_CHANGE. A human must explicitly initiate SCOPE_CHANGE before any proposed action can be treated as an intake request.

## Consumption Rules

- Treat all actions in `Proposed_SCA_Actions.csv` as conservative proposals.
- Treat `TBD` entries as unresolved rulings, not implicit approvals.
- Use `Evidence_Index.csv` as the local evidence map for every proposed action.
- Re-read the cited upstream DepClosure snapshot and affected dependency registers before executing any later amendment.
- Preserve snapshot discipline: later phases must cite accepted upstream snapshots and record a new immutable snapshot where the owning workflow requires it.

## SCOPE_CHANGE Gate Mapping

| Gate | Packet Use |
|---|---|
| Intake | Seed a human-reviewed SCOPE_CHANGE request using `SCOPE_CHANGE_INIT.md`. |
| Evidence | Verify SCC-001 and bidirectional-pair evidence against the cited DepClosure snapshot. |
| Impact | Review affected PKG-06 deliverables and surfaces in `Affected_Surfaces.csv`. |
| Amendment | Decide whether decomposition text, dependency semantics, or handoff state need amendment. |
| Closure | Record accepted rulings only in the authorized SCOPE_CHANGE workflow. |

## Non-Goals

- No dependency-row mutation.
- No SCC closure assertion.
- No project-wide blocker determination.
- No implementation change to permission overlay, SDK tools, MCP tools, hooks, or compaction behavior.
- No replacement of the accepted decomposition authority.
