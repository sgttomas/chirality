# Native source-ready handback

TASK `/root/live_manager/native`, parent `/root/live_manager`. Source/test authoring in the isolated checkout only; no descendants or Git mutation. Product release was received after both wire ACKs. Exact wire remains `91f4910026bcceffc98c669a4d2487539ad63cc878822061e6cc1b40c98c40ce`. Instruction/source origins were recorded in ACK.md; subsequent manager source-authoring and fixture/binding messages governed this bounded work.

## Implemented source

- Shared exact-envelope serde DTOs, limits, structured safe errors, random IDs, bounded NDJSON, auth/method checks and private descriptor validation.
- Optional macOS Unix carrier with exclusive private endpoint, finite connection/dispatch admission, original-registration cancellation, native dispatch correlation, replacement/duplicate/stale reply rejection, main-webview invoke binding and targeted events. Domain bodies and historical workspace receipts remain opaque.
- CLI with offline help/describe, explicit attachment, fresh request ID, bounded input/output, correlated responses, structured nonzero errors, no Apply and unsupported-host guards.
- Narrow Cargo/lib wiring: feature-gated CLI, explicit desktop default, opt-in setup and shutdown. Optional setup failure cleans/disables bridge and keeps desktop usable. Main source, Tauri config and Cargo.lock are unchanged.
- Authored wire/registry/socket-pair/descriptor/CLI fixture tests and development guidance. Manager-owned canonical fixture revision 2 copied byte-for-byte into maintained native test fixtures; no permanent test depends on dated AgentRuns paths.

Disabled register keys are the agreed `{enabled:false,app_instance_id:null,registration_id:null,controller_session_id:<requested>}`. Enabled keys use native strings. Listener-first frontend buffering during async register is frontend-owned; native reserves registration before dispatch and never rewrites its IDs.

## Checks actually performed

`rustfmt --edition 2021` on new Rust source/tests completed successfully (format/parser check only). `git diff --check` over modified existing lib.rs/Cargo.toml completed successfully. Read-only source inspection covered security/lifecycle/correlation and preserved desktop seams. No Cargo compile, tests, build, native app, browser, endpoint, CUA, npm or process/resource execution was performed by this TASK. No socket has been opened. Old PID9925 and preferences remain untouched.

ROOT's later controlled compile/test resource release was relayed with a manager sequencing hold. This writer is awaiting an explicit Cargo execution slot; source readiness is not behavior or compile proof. Manager requested jobs <=2 and serial heavy commands.

## Planned focused commands

Run from the Piping project root under manager-assigned target directory and slot:

```sh
CARGO_BUILD_JOBS=2 cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --lib live_control
CARGO_BUILD_JOBS=2 cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --test live_control_transport
CARGO_BUILD_JOBS=2 cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --features live-control-cli --bin swbpipe-control --test live_control_cli
CARGO_BUILD_JOBS=2 cargo build --manifest-path apps/desktop/src-tauri/Cargo.toml --features live-control-cli --bin swbpipe-control
```

Controlled test Unix sockets are process-owned fixtures with cleanup. A later granted packaged-app check must verify actual target selection, disabled startup and the preserved saved/edited-load self-test. Main-webview/Tauri connected I1/I2 and actual-human H1/H2 remain outstanding and unavailable under this slot. Controlled fixtures cannot close those gates. No source-wide independent review, engineering acceptance, Runtime qualification or release is claimed.

Canonical fixture SHA-256: `6a35f885b5175ab9ee5c8ae9ea2290cfe118512b6476b59ff986f0aace1af8dc` (maintained copy byte equality checked).

## Product identities

Paths relative to projects/chirality-piping:

| File | SHA-256 |
|---|---|
| `apps/desktop/src-tauri/src/live_control.rs` | `4e41f4337d733ce893dc874d6cd49a111d711a673d0e8f1b9bdf537b0ca277b5` |
| `apps/desktop/src-tauri/src/live_control_wire.rs` | `7de038550e4f288423927f70e564c0ea6ac443914d13443356e7cce6fd0fdae5` |
| `apps/desktop/src-tauri/src/bin/swbpipe-control.rs` | `728cf2acb27b46564c7b67c08c6c12ca81b767bde70e8eef056ea931291c8107` |
| `apps/desktop/src-tauri/src/lib.rs` | `9bf20ec511f761eb4549a5b3ad051f1de72866f79b90593c9700320ef6f41979` |
| `apps/desktop/src-tauri/Cargo.toml` | `ad7ee4d05b548c22e3ad2bf0cbf9ae98a78e525f62d694bd8e7a1ed15f00f18c` |
| `apps/desktop/src-tauri/tests/live_control_transport.rs` | `482d1516366fa6f6fe51c04989be501d44589e81141310eed3abeefb94bb3c0b` |
| `apps/desktop/src-tauri/tests/live_control_cli.rs` | `2580b515e7d40b531e48777e663b60da85860d7f0d7efed48bfafcf32b0cfc8f` |
| `apps/desktop/src-tauri/tests/fixtures/live-control-wire-v1.json` | `6a35f885b5175ab9ee5c8ae9ea2290cfe118512b6476b59ff986f0aace1af8dc` |
| `docs/LIVE_CONTROL_DEVELOPMENT.md` | `e9db6a37088bc8fcbf5cfdb5f42889451c30a57b1eb3ea19b2dd15b299714b60` |
| `apps/desktop/src-tauri/src/main.rs` (unchanged) | `03c5b9f8fc8812114d1a7db1b1e2c5c9f2ce6c7bbf0f000565fbb872e7a1d5ca` |
| `apps/desktop/src-tauri/tauri.conf.json` (unchanged) | `b3de0965f205e1ed34f07744939314c9ac40dd00af2ee8c0de336c6e2bfba5d0` |
| `apps/desktop/src-tauri/Cargo.lock` (unchanged) | `8b68e437515761bf5877a485cc99c52947bac386595f0182f5dcbc17732c71af` |

## Source-only fixture reliability repair

Manager requested bounded CLI fixture lifetime before Cargo scheduling. Added nonblocking accept with a five-second deadline and early-exit diagnostics, bounded CLI exit polling, read/write deadlines, redacted structured failure diagnostics, and RAII process kill/reap plus private-directory cleanup on unwind. No tests/builds executed for this repair; rustfmt completed.

## Source-only describe and guidance polish

Describe now includes each method purpose, exact params/result shapes, complete admission limits and preview-origin request-ID semantics. The guide contains complete invented params/result exchanges for both inspect modes and preview/submit/status, with full synthetic existing preview outcome and no capability. Manager confirmed the additional 1024 inspection-basis admission limit; frozen inspect result limits remain unchanged. Source-only describe assertions added; rustfmt completed. No tests/builds executed.

## Subsequent executed validation

The initial source-only state above is historical. The manager subsequently released a serialized Cargo slot. See RETURN.md, RUNS.json, FINAL_SOURCE.json and raw logs for actual results. The earlier 1024-inspection-basis description was removed after manager corrected the final frontend policy to one current coherent basis; frozen preview/ticket histories are independent.
