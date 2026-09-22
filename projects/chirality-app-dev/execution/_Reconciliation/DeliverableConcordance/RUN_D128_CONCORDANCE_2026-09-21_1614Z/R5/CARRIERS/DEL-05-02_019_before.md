### Current acceptance obligations

1. Root-owned daemon `HarnessEvent` records are consumed for App audit and replay surfaces without owning the generic schema or writer.
2. `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and `proposal.declined` are additive candidates against the closed schema v2 (K-EVENT-3) and are consumed only after Root DEL-02-10 acceptance is routed back (OI-008).
3. Accepted-turn and terminal-event persistence conformance is verified with malformed-tail tolerance preserved.

