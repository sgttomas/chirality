# Packet Datasheet: PKG00-SCA-PACKET-004

## Baseline

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-004 |
| PacketTitle | SCC-001 Tooling Permissions MCP |
| SCC_ID | SCC-001 |
| DepClosure Snapshot | `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |
| Decomposition Authority | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Focus Rows | TBD |

## SCC Evidence Summary

DepClosure evidence identifies SCC-001 as an 18-node runtime/SDK/session/tooling SCC. The focused packet surface covers the PKG-06 subset: `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`, and `DEL-06-06`.

The current bidirectional-pair evidence includes these packet-relevant pairs:

| Pair | Packet Concern |
|---|---|
| DEL-06-01 <-> DEL-06-02 | Permission overlay versus SDK read tool resolver exposure. |
| DEL-06-01 <-> DEL-06-03 | Permission overlay versus in-process Chirality MCP read tools. |
| DEL-06-01 <-> DEL-06-04 | Permission overlay versus write/edit gate and path hook results. |
| DEL-06-04 <-> DEL-06-06 | Write/edit hook enforcement versus hook lifecycle and compaction mirror evidence. |

## Affected Deliverables

| Deliverable | Decomposition Role | Current Local State |
|---|---|---|
| DEL-06-01 | ChiralityPermissionOverlay and Mode Mapping | SEMANTIC_READY |
| DEL-06-02 | SDK Read Tool Surface and Tool Validation | SEMANTIC_READY |
| DEL-06-03 | Initial Chirality MCP Read Tools | SEMANTIC_READY |
| DEL-06-04 | Write/Edit Surface and Path Hooks | SEMANTIC_READY |
| DEL-06-06 | Hook Lifecycle and Compaction Mirror | SEMANTIC_READY |

## Evidence Inventory

| EvidenceID | Short Description |
|---|---|
| E-001 | Decomposition PKG-06 and DEL-06-01 through DEL-06-06 scope rows. |
| E-002 | DepClosure SCC summary identifying SCC-001 membership. |
| E-003 | DepClosure bidirectional-pair evidence for PKG-06 pairs. |
| E-004 | SCC triage recommendation to classify SCC-001 edges without inventing new dependency types. |
| E-005 | DEL-06-01 dependency register rows for permission overlay interfaces. |
| E-006 | DEL-06-02 dependency register rows for read surface dependency on overlay and MCP definitions. |
| E-007 | DEL-06-03 dependency register rows for MCP read tools and permission/event integration. |
| E-008 | DEL-06-04 dependency register rows for write/edit path hooks and lifecycle handoff. |
| E-009 | DEL-06-06 dependency register rows for hook lifecycle, JSONL event dependency, and compaction mirror. |
| E-010 | Affected deliverable statuses showing SEMANTIC_READY without dependency closure. |

## Open Rulings

- Whether SCC-001 pair treatment can be resolved by dependency-row classification alone or requires decomposition amendment: TBD.
- Exact runtime event writer/session JSONL append API owner for permission and MCP tool events: TBD.
- Exact status lifecycle API owner for MCP status read behavior: TBD.
- Exact hook lifecycle mapper module path, payload fields, and validation fixture paths: TBD.
- REF-006 `docs/PRD.md` hash mismatch disposition for PRD-only tool, write, hook, and compaction details: TBD.
