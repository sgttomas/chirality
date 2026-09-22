### Current responsibility

`DEL-05-02 HarnessEvent Schema and Append-Only JSONL` (DATA_MODEL_CHANGE, applied decomposition row L337):

Consume Root-owned daemon `HarnessEvent` records for App audit/replay surfaces
and verify accepted-turn and terminal-event persistence without owning the
generic event schema or writer; consume the additive `proposal.*` event types
for replay and the proposal card once Root accepts them (SOW-082).

Applied row notes: App event-consumption and conformance slice; generic
persistence remains Root-owned.

Applied row outputs: App runtime-event compatibility fixtures; accepted-turn and
terminal persistence conformance tests; daemon evidence samples.

