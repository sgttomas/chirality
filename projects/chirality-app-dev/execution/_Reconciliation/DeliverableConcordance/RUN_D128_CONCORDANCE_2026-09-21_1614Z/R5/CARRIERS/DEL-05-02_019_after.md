### Current acceptance obligations

1. Runtime event records are consumed for App audit and replay without creating a second generic schema or writer.
2. The App preserves the accepted offer/accept/adjust/decline proposal audit meaning where that interaction is supported. Former `proposal.*` candidates and Root DEL-02-10 approval are historical implementation and ownership evidence; they do not restrict the open Codex event stream. Unfulfilled proposal behavior stays in Remaining.
3. Accepted-turn and terminal-event persistence conformance is verified with malformed-tail tolerance preserved; unknown Codex notifications remain inspectable and the surviving secret-protection obligation remains visible.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

