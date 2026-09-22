### CLM-005 — Runtime lifecycle and App transport boundary

The App delegates execution to its application-owned Runtime service. Runtime owns turn admission and the one-active-turn-per-session invariant, releases active-turn ownership after a terminal outcome, and preserves accepted input and terminal evidence. HTTP and Desktop surfaces validate and transport requests and stream results; they do not create an independent runtime or acquire an App-local substitute lock.

Requests bind registered project identity/root, role, permission and delegation policy, runtime options, content and attachment references. Interrupt and cancellation handling remains coordinated with DEL-03-04. A renderer disconnect unsubscribes from the stream and must not interrupt the running turn. Public event handling preserves Codex notifications under the accepted protocol rather than promising the former closed SDK event vocabulary.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. Remaining binding and delegation-policy findings retain their own gates in `_STATUS.md`; the wording does not certify them complete.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

