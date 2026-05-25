# Packet Datasheet: SCC-001 Session Audit Records

## Identification

| Field | Value |
|---|---|
| PacketID | PKG00-SCA-PACKET-003 |
| SCC_ID | SCC-001 |
| FocusRows | TBD |
| BidirectionalPairs | DEL-03-04<->DEL-05-02; DEL-04-05<->DEL-05-03; DEL-05-02<->DEL-05-03 |
| ReadinessTarget | READY_FOR_HUMAN_REVIEW |

## SCC Baseline

DepClosure evidence records SCC-001 as an 18-node strict-cycle set. The requested packet subset focuses on six affected deliverables and three bidirectional pairs. The packet uses the accepted snapshot as evidence only and does not update graph state.

## Affected Deliverables

| Deliverable | Role In Packet | Evidence |
|---|---|---|
| DEL-03-04 | Interrupt, cancel, failure cleanup, and terminal outcome semantics. | E-006; E-007 |
| DEL-04-05 | Provider key/base URL/network bridge and provider-boundary error redaction. | E-006; E-009 |
| DEL-05-01 | Canonical session folder, legacy session migration, SDK session link, transcript placement. | E-006; E-011 |
| DEL-05-02 | HarnessEvent schema, accepted-turn and terminal-event JSONL, session event placement. | E-006; E-008 |
| DEL-05-03 | Redacted run logging, secret hygiene, redaction before persistence. | E-006; E-010 |
| DEL-05-05 | ToolResultStore, session artifacts, output budget policy, artifact references. | E-006; E-012 |

## Evidence Inventory

Evidence is indexed in `Evidence_Index.csv`. The core evidence set is:

- DepClosure SCC and bidirectional-pair files for SCC-001.
- The SOFTWARE v3.2 decomposition authority.
- Affected product deliverable dependency registers.
- Affected deliverable context/status surfaces confirming scope identity and current SEMANTIC_READY state.

## Unresolved Fields

- `FOCUS_ROWS`: TBD in the brief.
- Terminal taxonomy ruling for interruption versus cancellation metadata: TBD.
- Exact SDK transcript placement and store linkage details: TBD.
- Final redaction helper/run logger module paths and configured-secret schema: TBD.
- ToolResultStore implementation location and budget policy parameters: TBD.

## Substantiation Boundary

This datasheet substantiates packet structure, affected surfaces, and evidence pointers. It does not substantiate row-level rulings, a SCOPE_CHANGE amendment, SCC closure, or project-wide blocker state.
