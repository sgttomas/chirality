# Unregistered-root taxonomy repair

Frozen bounded repair against source `6e1e093006bea8ece5a624fdb4bba291a181262d`; TASK / Type 2, gpt-6-astra medium, no delegation. Parent independently confirmed CI returned 409 for the unregistered-root create. Source traced it to a fail-closed compatibility regression: Runtime PROJECT_NOT_FOUND became hosted registration:required, then the routing facade discarded that distinction and threw generic WORKING_ROOT_CONFLICT/409. No create or registration was admitted.

Changed only these frontend surfaces:

- `src/lib/runtime-client/daemon-harness-port.ts`: registration:required now throws WORKING_ROOT_INACCESSIBLE/404. A registered result without the expected binding remains WORKING_ROOT_CONFLICT/409; underlying verification failures retain their codes. No registration or session creation was introduced.
- `src/__tests__/lib/runtime-daemon-harness-port.test.ts`: actual HTTP create route + global registry + project-scoped port + real hosted bootstrap adapter regression. Unregistered root returns 404/inaccessible; a mismatched advertised registration returns 409/conflict. Neither path calls project initialization, session creation, scoped-client creation, or binding installation. Existing authorized-root creation still succeeds afterward.
- `scripts/validate-harness-section8.mjs`: the same existing fail-closed assertion now includes HTTP status and an allowlisted uppercase error-type token (or UNKNOWN). It does not include the raw payload. Expected statuses/types are unchanged.

Checks: 32 focused runtime-daemon-harness-port tests PASS; `npm run typecheck` PASS (frontend and Electron); `node --check scripts/validate-harness-section8.mjs` PASS. No full suites repeated locally and no live App/Runtime/profile calls, credential reads, build, commit or push performed. Prior supplied CI evidence remains separate from these focused checks.

APP-HOLD-1 dispatch `APP_V3_USER_JOURNEYS_20260912:ROOT_TAXONOMY`, DEL-03-01: ALLOW/CLEAR, no active holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan `90ced3878baee8d3bae542d3488168e54c90be82bfa32030aa3d0fe872e99321`.

Handoff: source/tests frozen for parent's separate medium review and CI rerun. Local repair complete; independent review/CI acceptance remain open. This return is derivative implementation evidence, not publication approval.
