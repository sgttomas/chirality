### CLM-005 — Route and stream compatibility

Harness routes must remain thin, validated clients of the App-owned Runtime service. Their compatibility obligation concerns the supported App operations and inspectable outcomes, with live Codex notifications preserved through the full protocol. Compatibility does not require manufacturing every legacy SDK event name or translating away an unknown Codex notification.

The stream must preserve ordering and replay identity, expose failures, and permit detach/reattach without turning a renderer disconnect into a turn interrupt. Runtime owns turn coordination. Route presence alone does not establish operation completeness: the live scaffold route's missing composition remains a P-15 residual, and fake-port tests do not establish a live fixture capture.

Verification hooks: `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`, `frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`, and `projects/chirality-runtime/tests/daemon.test.ts`. `RouteAdapterTestIndex.md` and the R3 rows preserve missing-fixture evidence separately.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

