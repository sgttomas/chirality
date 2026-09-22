### CLM-005 — Engine boundary and conformance

The App must consume the Runtime-owned engine boundary for the sole qualified MVP engine, Codex. Turn inputs preserve the active session, registered project root, selected role, permission policy, resolved runtime options, content and attachment references, and cancellation semantics required by the accepted contract. Contract-module filenames, interface signatures and former shim paths are implementation evidence, rather than an additional App implementation mandate.

The surviving request/session correctness obligations must be mapped to current verification, including D-GOV-43 S-1–S-8 where applicable. D-GOV-43 retires vanished-purpose gates and avoids duplicate checks for the same condition; the legacy suite as a whole is not a new blanket admission gate. Deterministic stub and retained SDK tests establish only their own subjects. P-08 remains a bounded coverage-mapping residual: identify genuinely uncovered live-Codex obligations for accepted turns, terminal outcomes, capabilities, applicable tool handling and secret protection; do not declare equivalence without that mapping.

Verification hooks: `projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/lib/engine-conformance.test.ts`. The last is retained compatibility/test evidence and is not a live-Codex qualification witness.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

