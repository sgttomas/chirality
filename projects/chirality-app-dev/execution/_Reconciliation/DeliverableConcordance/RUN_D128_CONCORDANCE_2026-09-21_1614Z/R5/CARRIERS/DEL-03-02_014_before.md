### Current responsibility

`DEL-03-02 Thin TurnEngine and Session Locking` (BACKEND_FEATURE_SLICE, applied decomposition row L318):

Keep App `/api/harness/*` and Desktop surfaces as daemon clients, bind
project/persona/mode/delegation-policy/options requests, and verify daemon-owned
session lifecycle and one-active-turn behavior.

Applied row notes: App backend-integration slice; generic TurnEngine and lock
ownership remain Root-owned; the stored delegation-policy field is Root-owned
(SOW-083, OI-008).

Applied row outputs: Daemon-client turn proxy; App session integration tests;
daemon locking/lifecycle conformance evidence.

