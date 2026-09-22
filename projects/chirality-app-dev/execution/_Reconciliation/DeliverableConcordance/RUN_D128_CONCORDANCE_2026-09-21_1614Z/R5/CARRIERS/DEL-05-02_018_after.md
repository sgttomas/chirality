### Current responsibility

Consume Runtime-owned event records for App audit and replay without owning the generic writer. Preserve accepted-turn and terminal evidence and keep Codex notifications inspectable as received, including unfamiliar methods. The event vocabulary is open under D-GOV-43 and D-APP-127; the retired Root DEL-02-10 and closed schema are not current admission gates.

The App remains responsible for the accepted proposal interaction and its audit/replay meaning (SOW-082). Retiring the old schema gate does not certify proposal-event implementation or remove any unfulfilled user-facing guarantee.

Verification hooks: `frontend/src/__tests__/lib/harness-event-views-codex.test.ts`, `projects/chirality-runtime/tests/turn-hardening.test.ts`, and `projects/chirality-runtime/tests/app-owned-composition.test.ts`.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

