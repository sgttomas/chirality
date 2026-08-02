# Agent 2 Return V2 — Proposal-Amendment Convention

Status: `COMPLETE / READ_ONLY`

Basis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc` plus the live Revision 2
proposal worktree

This record persists the read-only child's terminal return at manager fan-in.
The child changed no file.

## Findings

- Retain DecisionID `D-APP-84` and status `AWAITING_RULING`; create no ruling
  record and infer no owner selection.
- Preserve the never-ruled Revision 1 packet byte-for-byte and bind it by exact
  SHA-256 from the separately named Revision 2 packet.
- Keep the original orchestration artifacts durable. Add versioned v2 plan,
  work-graph, manager return/status/handoff, brief amendment, child returns,
  and fresh adversarial review under the existing RunID.
- The decision register may change only its single D-APP-84 proposal row to
  point to current Revision 2 and an awaiting-owner placeholder.
- Do not update receipts, `_LATEST` pointers, authority, decomposition,
  runtime/frontend, Task Management, parity, historical-UNKNOWN, lifecycle, or
  Git state before a ruling and the later owning gates.

No file was changed by the child.
