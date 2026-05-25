# Packet Procedure: PKG00-SCA-PACKET-001

## Intake Procedure

1. Human reviewer reads `Packet_Contract.md` and confirms this packet is only an intake seed.
2. Human reviewer explicitly decides whether to initiate SCOPE_CHANGE for SCC-002.
3. If initiated, SCOPE_CHANGE uses `SCOPE_CHANGE_INIT.md` as the seed request and imports the packet evidence index.
4. SCOPE_CHANGE confirms the accepted upstream snapshot and decomposition authority before any amendment work.

## Gate-by-Gate Use

| Gate | Procedure |
|---|---|
| Intake | Confirm SCC_ID is SCC-002, affected deliverables are DEL-10-02 and DEL-10-03, and focus rows are DEP-10-02-004 and DEP-10-03-006. |
| Source Review | Read evidence rows EVID-001 through EVID-011 before accepting or rejecting any action candidate. |
| Impact Assessment | Use `Affected_Surfaces.csv` to decide whether the change is limited to dependency interpretation, product text clarification, decomposition amendment, or a combination. |
| Amendment Drafting | Use `Proposed_SCA_Actions.csv`; preserve TBD where the evidence does not determine the ruling. |
| Dependency Ruling | Decide row-by-row whether DEP-10-02-004 and DEP-10-03-006 remain active, are satisfied, are converted, or require a decomposition-level amendment. |
| Closure Review | Confirm any accepted mutation was performed by the authorized workflow and recorded outside this packet. |

## Row-Specific Procedure

### DEP-10-03-006

1. Start from the DepClosure recommendation that this row is the likely true sequencing edge.
2. Check whether DEL-10-02's current policy text is sufficient to satisfy DEL-10-03's prerequisite.
3. If not sufficient, preserve the row as pending or TBD according to SCOPE_CHANGE ruling.
4. If sufficient, require a source-cited rationale before any later register update.

### DEP-10-02-004

1. Start from the DepClosure reading that this row is opposite-direction interface evidence.
2. Check whether it represents a true upstream dependency, a non-blocking interface, downstream handoff evidence, duplicate reciprocal evidence, or a row needing retirement.
3. Do not waive or retire it without source citation.
4. Record unresolved disposition as `TBD`.

## Records Required After Human-Initiated SCOPE_CHANGE

- SCOPE_CHANGE intake record naming this packet.
- Impact assessment with accepted evidence refs.
- Proposed amendment or explicit no-amendment rationale.
- Human ruling for each focus row.
- If accepted by the owning workflow, changed product files or registers in their own authorized locations.
- Closure state and handoff state emitted by SCOPE_CHANGE, not by this packet.
