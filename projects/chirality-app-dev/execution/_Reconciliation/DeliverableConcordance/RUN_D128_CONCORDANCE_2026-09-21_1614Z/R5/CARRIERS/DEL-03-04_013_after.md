### CLM-005 — Interrupt and durable terminal evidence

Explicit user interruption must reach the active Runtime turn, release turn ownership on termination, and preserve a truthful terminal outcome. Accepted input and attachment references must remain recoverable after failure. A disconnected renderer stops receiving frames; disconnection by itself must not cancel the turn or release active-turn ownership. Reattachment must expose the continuing or completed turn consistently.

Malformed-tail tolerance, unique event identity, append-only records, and the surviving secret-protection requirement remain verification obligations. No compatibility mapper or legacy SDK test substitutes for evidence on the live Codex path; the redaction gap is retained under P-12.

Verification hooks: `projects/chirality-runtime/tests/app-owned-composition.test.ts`, `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/daemon.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

