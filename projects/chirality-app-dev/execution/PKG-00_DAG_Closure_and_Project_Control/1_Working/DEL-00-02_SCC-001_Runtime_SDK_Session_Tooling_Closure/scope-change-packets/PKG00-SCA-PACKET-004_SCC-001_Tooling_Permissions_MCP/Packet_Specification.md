# Packet Specification: PKG00-SCA-PACKET-004

## Proposed Amendment Requirements

1. Preserve deny-first permission overlay ownership in DEL-06-01 while clarifying that read tool resolution, MCP wrapper metadata, write/edit path hooks, and hook lifecycle mirrors are adjacent integration surfaces, not substitutes for permission policy.
2. Classify the packet-relevant SCC-001 bidirectional pairs as hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only using existing dependency schema fields.
3. Keep read-first sequencing explicit: SDK read tools and initial Chirality MCP read tools may be exposed before write/edit/bash capability, but exposure does not bypass the permission overlay.
4. Keep write/edit capability gated by project-root containment, instruction-root block, symlink rejection, exact edit preconditions, provenance hooks, and accepted permission results.
5. Keep hook lifecycle and compaction mirror integration tied to HarnessEvent/JSONL event contracts, terminal outcome behavior, and validation handoff without embedding path-enforcement ownership in DEL-06-06.

## Proposed Action Candidates

The action candidates are listed in `Proposed_SCA_Actions.csv`. They use `MODIFY` for clarification-oriented amendments and `TBD` where the action depends on a human or SCOPE_CHANGE ruling.

## Acceptance Criteria For Later SCOPE_CHANGE

- Each accepted action cites current evidence and records any replacement or superseding snapshot.
- No action treats this packet as a direct edit authority.
- Any dependency-row changes, if approved later, are performed only by the authorized dependency or SCOPE_CHANGE workflow.
- Any decomposition amendment preserves accepted PKG-06 deliverable ownership unless SCOPE_CHANGE explicitly approves a different ownership boundary.
- PRD-only implementation details remain warning-qualified until REF-006 source-state reconciliation is resolved.

## Invariant Checks

| Invariant | Required Treatment |
|---|---|
| Permission overlay is authoritative for allow/deny decisions | Preserve DEL-06-01 as the policy owner. |
| `allowedTools` is not a restriction boundary by itself | Keep overlay, hooks, callbacks, and event persistence in scope. |
| MCP tools are not bypasses | Route `mcp__chirality__*` through the same permission, hook, redaction, and event policy. |
| Read tools precede write/edit/bash capability | Keep DEL-06-02 and DEL-06-03 read-first boundaries explicit. |
| Write/edit needs path hooks | Preserve DEL-06-04 containment and precondition ownership. |
| Compaction and hook lifecycle are audit events | Preserve DEL-06-06 mirror ownership and event-contract dependency. |

## Unresolved Specification Items

- Exact dependency rows requiring amendment: TBD.
- Whether pair evidence should be treated as duplicate reciprocal evidence or co-development-only for each edge: TBD.
- Exact implementation paths and test fixture names: TBD.
