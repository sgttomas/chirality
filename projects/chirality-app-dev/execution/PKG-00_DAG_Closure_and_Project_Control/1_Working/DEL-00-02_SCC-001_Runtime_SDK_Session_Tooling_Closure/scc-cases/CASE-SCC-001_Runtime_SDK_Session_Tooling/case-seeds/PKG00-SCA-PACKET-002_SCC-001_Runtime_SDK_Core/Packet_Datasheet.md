# Packet Datasheet: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

## Identity

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-002 |
| PacketTitle | SCC-001 Runtime SDK Core |
| SCC_ID | SCC-001 |
| DecompositionVariant | SOFTWARE |
| PacketStatus | READY_FOR_HUMAN_REVIEW |
| DerivativePackage | Yes |
| AcceptedUpstreamSnapshot | `CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431` |

## SCC Baseline

DepClosure reports SCC-001 as an 18-node strict SCC in the runtime, SDK, session, and tooling area. This packet focuses on the requested runtime SDK core subset, not the full SCC-001 node set.

Focused affected deliverables:

`DEL-03-01`; `DEL-03-02`; `DEL-03-03`; `DEL-03-04`; `DEL-04-01`; `DEL-04-02`; `DEL-04-03`; `DEL-04-04`; `DEL-04-05`

Focused bidirectional pairs:

| Pair | Current Packet Reading |
|---|---|
| DEL-03-01 <-> DEL-03-04 | Runtime contract conformance and interrupt terminal outcome handling are mutually referenced. |
| DEL-03-01 <-> DEL-04-01 | SDK probe evidence and product-owned runtime contract expectations are mutually referenced. |
| DEL-03-03 <-> DEL-03-04 | SSE/API compatibility and interrupt terminal handling are mutually referenced. |
| DEL-03-03 <-> DEL-04-03 | Browser-facing UI events and SDK message mapping are mutually referenced. |
| DEL-04-02 <-> DEL-04-04 | SDK options/settings and persona composition exchange interface inputs. |

## Evidence Inventory

Primary evidence is indexed in `Evidence_Index.csv`. Owning product registers identify concrete candidate rows such as `DEP-03-01-003`, `DEP-03-01-006`, `DEP-03-04-006`, `DEP-03-03-007`, `DEP-03-03-009`, `DEP-04-03-009`, `DEP-04-02-007`, and `DEP-04-04-004`.

## Current Rulings

| Topic | Ruling |
|---|---|
| Focus rows | TBD until SCOPE_CHANGE or RECONCILIATION selects row-level rulings. |
| Dependency-edge treatment | Insufficient by itself because several rows encode interface evidence or handoff evidence rather than hard sequencing. |
| Product-register mutation | Out of scope for this packet. |
| Closure verdict | TBD; requires later accepted amendments and DepClosure rerun. |
