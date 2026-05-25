# Packet Rationale: SCC-001 Session Audit Records

## Source-Grounded Reading

SCC-001 remains a broad runtime/SDK/session/tooling cycle in the accepted DepClosure snapshot. The requested packet narrows attention to session audit records: terminal outcomes, session folder storage, `HarnessEvent` JSONL, redacted logging, replay/transcript linkage, and tool-result artifacts.

The evidence does not justify packet-side row edits. It does justify SCOPE_CHANGE intake preparation because the cited bidirectional pairs reflect real interface tension among durable audit events, lifecycle outcomes, redaction, and artifact storage.

## Why Edge Treatment Alone Is Insufficient

The three focus pairs cross product ownership boundaries:

- DEL-03-04 needs terminal outcomes and interrupt/cancel semantics that DEL-05-02 must persist.
- DEL-04-05 emits provider and SDK failure details that DEL-05-03 must redact.
- DEL-05-02 designs event payloads that DEL-05-03 must constrain before persistence.

A row-only ruling could hide the design invariant. The safer SCOPE_CHANGE-compatible approach is to clarify ownership and invariants, then classify edges after the human accepts the intended boundary.

## Risks

- Treating SDK transcripts as canonical product truth would conflict with the decomposition's Chirality-owned audit boundary.
- Treating redaction as a later cleanup step could allow secrets into persistent records or artifacts.
- Treating tool-result artifacts as plain event payloads could flood chat/model context and weaken replay determinism.
- Resolving terminal taxonomy without a human ruling could collapse interruption and cancellation semantics incorrectly.

## Alternatives Rejected For This Packet

- Direct dependency-register edits: outside packet authority.
- Removing reciprocal edges from SCC-001: not supported without SCOPE_CHANGE ruling.
- Declaring graph closure from packet evidence: outside packet authority.
- Deferring all work: rejected because current evidence is sufficient to prepare a bounded intake package.

