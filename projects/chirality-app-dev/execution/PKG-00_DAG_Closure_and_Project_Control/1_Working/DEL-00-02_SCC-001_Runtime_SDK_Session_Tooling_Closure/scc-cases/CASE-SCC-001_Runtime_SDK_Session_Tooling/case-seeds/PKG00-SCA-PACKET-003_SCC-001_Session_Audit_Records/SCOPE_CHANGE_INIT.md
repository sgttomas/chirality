# SCOPE_CHANGE_INIT Seed: PKG00-SCA-PACKET-003

This file is a seed request only. It is not valid until a human explicitly initiates SCOPE_CHANGE.

## Proposed Request

Initiate SCOPE_CHANGE review for SCC-001 session audit records, focused on the interfaces among interrupt/cancel terminal outcomes, canonical session storage, `HarnessEvent` JSONL, redacted logging, transcript/replay linkage, and tool-result artifact records.

## Requested Scope

- SCC: SCC-001
- Packet: PKG00-SCA-PACKET-003
- Affected deliverables: DEL-03-04; DEL-04-05; DEL-05-01; DEL-05-02; DEL-05-03; DEL-05-05
- Focus pairs: DEL-03-04<->DEL-05-02; DEL-04-05<->DEL-05-03; DEL-05-02<->DEL-05-03

## Requested Review Questions

1. What terminal outcome taxonomy should DEL-03-04 expose to DEL-05-02 for durable audit records?
2. Which session folder, transcript linkage, and SDK store metadata belongs to DEL-05-01 versus DEL-05-02 or DEL-05-05?
3. Where must redaction occur before provider, SDK, event, replay, and tool-result records persist?
4. Which candidate dependency rulings should be accepted, revised, rejected, or deferred?

## Seed Evidence

Use `Evidence_Index.csv` in this packet. Preserve the cited DepClosure snapshot and product dependency registers as read-only evidence unless the later SCOPE_CHANGE workflow explicitly authorizes mutation.

