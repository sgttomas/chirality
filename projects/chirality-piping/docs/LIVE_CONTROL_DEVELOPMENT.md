# Development live control

This optional macOS carrier connects a local JSON CLI to the running Piping workspace controller. It exposes `inspect`, `preview`, `submit` and `status`. Apply remains the app's existing local review action. Neither attachment authorization nor operation metadata verifies a Codex or human identity. Actual human single and batch witnesses remain separate from automated tests.

## Start and attach

Build the CLI from the Piping project directory:

```sh
cargo build --manifest-path apps/desktop/src-tauri/Cargo.toml --features live-control-cli --bin swbpipe-control
```

Start the ordinary development desktop with `SWBPIPE_LIVE_CONTROL=1` in its environment. On successful startup stderr reports only the absolute attachment descriptor path. Without this exact opt-in the bridge is disabled. Unavailable optional setup disables the bridge with a fixed diagnostic and keeps the desktop usable. Other hosts have no listener; the CLI returns `unsupported_host`. Only the configured main webview can register, reply or unregister. The local-main capability grants exactly `core:event:allow-listen` and `core:event:allow-unlisten` to `webviews:["main"]`, with no remote origin or window-wide grant. Both native events use the explicit `WebviewWindow` main target and the frontend subscribes with the matching target. Tauri also admits `Any` listeners to targeted events, so target routing alone is not a confidentiality boundary; local-main capability admission and source/registration/dispatch checks remain necessary. No event emit, filesystem or shell permission is granted.

Use that path explicitly on every CLI invocation. Keep the descriptor private; do not paste its contents, capability, or a socket request envelope into logs, issue reports, chat or evidence. The descriptor and socket live in a randomly named private directory under `/private/tmp`; the directory is mode 0700 and both entries mode 0600. The CLI rejects unsafe permissions, symlinks, invalid descriptor shapes, wrong protocol and non-socket endpoints. The descriptor's keys are `protocol_version`, `app_instance_id`, `socket_path` and `capability`. The CLI adds fresh request correlation and attachment authorization itself.

`swbpipe-control help` and `swbpipe-control describe` work without an app and return JSON. Every request command takes one params JSON object on stdin and returns one newline-terminated response JSON object on stdout. Errors exit nonzero. Do not close the socket's write side early in a custom client: EOF signals disconnect/cancellation. The CLI handles this itself.

## Narrow domain examples

Set `ATTACHMENT` to the emitted path and `CONTROL` to the built CLI. These are shell variables, not persisted workspace defaults. First discover the app's current workspace:

```sh
printf '%s\n' '{"scope":"workspace"}' | "$CONTROL" --attachment "$ATTACHMENT" inspect
```

Use the actual returned opaque workspace and explicit node IDs:

```json
{"scope":"nodes","workspace":"<returned workspace>","node_ids":["<node ID>"]}
```

Inspect returns node coordinates, source length unit, and an opaque coherent basis. Feed that workspace and basis into `preview`; retain decimal input strings and the exact inspected project length unit:

```json
{"workspace":"<returned workspace>","basis":"<returned basis>","changes":[{"target":{"object_type":"Node","ref":"<node ID>"},"field_path":"position.x","before":"100","after":"125","unit":"<inspected length unit>","dimension":"length"}]}
```

The numeric strings here are invented examples. Replace them with the intended before/after values. For a batch, append ordered changes to the same array. One-member and multi-member previews use the same atomic engine route. Only `Node position.x` length edits are admitted; caller operation IDs, source/author/acceptance fields and other changes are rejected. Preview cannot mutate model/history or establish acceptance.

Submit a passed preview with a caller-selected stable idempotency key:

```json
{"workspace":"<original workspace>","preview_ref":"<returned preview>","idempotency_key":"<stable unique proposal key>"}
```

Submit reports `queued` only after the actual queue entry is observed in a committed controller render. Review and Apply in the app; then query `status`:

```json
{"workspace":"<original workspace>","ticket":"<returned ticket>"}
```

A committed receipt binds the observed model/hash/history/queue/result transition. Its `origin.request_id` identifies the **preview invocation that created the proposal**, not a subsequent submit, status or retry invocation. Its acceptance route is `local_review_apply`, with identity verification not performed and professional approval false. The receipt's `session_state_only_not_yet_saved` boundary describes commit time, not whether a later Save occurred. Raw engine acceptance/runtime strings do not replace this observed receipt.

## Recovery and limits

On uncertain submit, retry **the original workspace, preview and idempotency key**. Do not generate a replacement key. Historical status and same-key recovery remain available in the same running controller even after workspace replacement. Native transport passes those responses through without current-workspace filtering. Controller restart/remount expires handles or requires unknown-outcome reconciliation; the registry is not durable and proposals are not replayed by Save/Open/Create.

States are `queued`, `committed`, `rejected`, `withdrawn`, `expired` and `outcome_unknown`. Queue clearing after observed publication is withdrawn. Cancellation before publication is reported only when the controller confirms absence. Socket timeout/disconnect does not prove the proposal never happened. Hashing a receipt may temporarily return `not_ready`.

| Limit | Value |
|---|---:|
| UTF-8 frame, including newline | 1,048,576 bytes |
| Attachment descriptor | 16,384 bytes |
| Native admitted connections/requests | 16 |
| Native request deadline | 30 seconds |
| Explicit node IDs per inspect | 128 |
| Ordered preview changes | 64 |
| Controller previews | 256 |
| Controller idempotency associations | 1,024 |

The controller retains one current coherent inspection basis and reuses it while revision/hash are unchanged; stale inspection bases are retired. Frozen preview snapshots and historical ticket recovery are independent of that current inspection cell. The inspect result exposes `max_node_ids` and `max_changes`. Capacity rejects new work without discarding promised recovery records. There is no preview wall-clock TTL. The carrier rejects malformed envelopes, unsupported protocols/methods, unsafe attachments, wrong app/capability and oversized frames. Controller errors additionally describe stale basis, wrong workspace, unknown preview/ticket, key conflict, publication cancellation or expiry. Every error includes `code`, `message`, `retryable`, and `next_action`; follow its reconciliation guidance. No arbitrary internal exception payload is returned.

Normal shutdown cancels outstanding dispatches against their original registration and removes only process-owned endpoint objects. A crash can leave a private stale directory; a later app does not reuse it. A stale descriptor does not restore controller outcomes. Stop the owning development process and establish ownership before manually deleting stale private files.

## Development checks and boundaries

Cargo explicitly selects `openpipestress-desktop` as the default binary. The CLI requires the `live-control-cli` feature; its entrypoint imports only shared wire code and never starts the desktop. The existing desktop main and `--self-test-saved-edited-load` route remain unchanged. Actual Tauri package selection and the packaged self-test must still be witnessed on each qualified candidate.

Focused checks, only in a released test/build lane:

```sh
cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --lib live_control
cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --test live_control_transport
cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --features live-control-cli --bin swbpipe-control --test live_control_cli
```

Maintained synthetic carrier fixtures live at `apps/desktop/src-tauri/tests/fixtures/live-control-wire-v1.json`. They prove wire shape and opaque historical transport, not domain validity, canonical hash truth, native connected integration or human Apply. Native I1/I2, real-engine/controller checks, actual package checks and actual-human H1/H2 remain distinct evidence requirements. No engineering acceptance, solver qualification, embedded Runtime or product release follows from this development carrier.

## Complete invented exchanges

These params and full success envelopes illustrate exact public field names. All identifiers, coordinates, hashes and outcomes are invented schema examples, **not engine execution evidence**. Zero/one hash strings are placeholders and must never be submitted as trusted evidence. Real references are minted by the running controller. The CLI adds the private transport authorization; no capability is shown. The final status example assumes the user cleared the published queue entry.

`inspect` stdin:

```json
{"scope":"workspace"}
```

stdout:

```json
{"protocol_version":1,"request_id":"example-request-1","app_instance_id":"example-app","result":{"workspace":"example-workspace","identity":{"app_instance_id":"example-app","controller_session_id":"example-controller","workspace_id":"example-workspace","project_generation":1,"project_id":"example-project"},"readiness":"ready","selection":[],"supported":{"object_type":"Node","field_path":"position.x","operation_kind":"modify","change_kind":"set_field","dimension":"length","length_unit":"mm"},"limits":{"max_node_ids":128,"max_changes":64}}}
```

`inspect` stdin:

```json
{"scope":"nodes","workspace":"example-workspace","node_ids":["node:example"]}
```

stdout:

```json
{"protocol_version":1,"request_id":"example-request-2","app_instance_id":"example-app","result":{"workspace":"example-workspace","identity":{"app_instance_id":"example-app","controller_session_id":"example-controller","workspace_id":"example-workspace","project_generation":1,"project_id":"example-project"},"basis":"example-basis","basis_identity":{"app_instance_id":"example-app","controller_session_id":"example-controller","workspace_id":"example-workspace","project_generation":1,"project_id":"example-project","model_revision":3,"model_hash":{"algorithm":"sha256","canonicalization":"rfc8785_jcs","payload_scope":"model_payload","payload_ref":"example-project","value":"0000000000000000000000000000000000000000000000000000000000000000","hash_status":"computed_local_preview"}},"nodes":[{"id":"node:example","label":"Example node","position":{"x":100,"y":0,"z":0}}],"length_unit":"mm"}}
```

`preview` stdin:

```json
{"workspace":"example-workspace","basis":"example-basis","changes":[{"target":{"object_type":"Node","ref":"node:example"},"field_path":"position.x","before":"100","after":"125","unit":"mm","dimension":"length"}]}
```

stdout:

```json
{"protocol_version":1,"request_id":"example-preview-request","app_instance_id":"example-app","result":{"workspace":"example-workspace","preview_ref":"example-preview","basis":"example-basis","basis_identity":{"app_instance_id":"example-app","controller_session_id":"example-controller","workspace_id":"example-workspace","project_generation":1,"project_id":"example-project","model_revision":3,"model_hash":{"algorithm":"sha256","canonicalization":"rfc8785_jcs","payload_scope":"model_payload","payload_ref":"example-project","value":"0000000000000000000000000000000000000000000000000000000000000000","hash_status":"computed_local_preview"}},"validation":"passed","outcome":{"schema_version":"0.1.0","document_kind":"openpipestress.desktop.operation_batch_outcome","batch_id":"example-batch","mode":"validate_only","application_route":"structured_operation_batch","input_model_unchanged":true,"validation":{"schema_validation":"passed","batch_validation_status":"passed","diff_preview_status":"generated","application_status":"not_applied"},"simulation_disposition":"validation_only_discarded","diagnostics":[],"operation_outcomes":[{"index":0,"operation_id":"example-operation","change_id":"example-change","target_object_type":"Node","target_ref":"node:example","change_kind":"set_field","validation":{"schema_validation":"passed","reference_validation":"passed","unit_validation":"passed","before_state_validation":"passed","diff_preview_status":"generated"},"diff_preview":[{"entity_ref":"node:example","object_type":"Node","change_kind":"set_field","field_path":"position.x","before":"100","after":"125","unit":"mm","dimension":"length"}],"diagnostics":[],"simulation_status":"validated_on_temporary_state"}],"initial_model_hash":{"algorithm":"sha256","canonicalization":"rfc8785_jcs","payload_scope":"model_payload","payload_ref":"example-project","value":"0000000000000000000000000000000000000000000000000000000000000000","hash_status":"computed_local_preview"},"initial_backend_hash":"sha256:0000000000000000000000000000000000000000000000000000000000000000","input_backend_hash":"sha256:0000000000000000000000000000000000000000000000000000000000000000","batch_hash":"sha256:1111111111111111111111111111111111111111111111111111111111111111","submitted_operations":[{"operation_id":"example-operation","operation_kind":"modify","operation_status":"proposed","author_type":"agent","source":{"source_ref":"local_json_cli:example-controller:example-preview-request","source_channel":"local_json_cli","source_role":"external_agent_proposal"},"target":{"object_type":"Node","ref":"node:example"},"change":{"change_id":"example-change","change_kind":"set_field","field_label":"Node X coordinate","field_path":"position.x","before":"100","after":"125","unit":"mm","dimension":"length","source_note":"External local JSON proposal; explicit local review required."},"validation":{"schema_validation":"not_run","constraint_validation":"not_run","unit_validation":"not_run","diff_preview_status":"not_generated","application_status":"not_applied"},"audit_boundary":{"mutation_route":"structured_operations_only","direct_model_mutation_allowed":false,"requires_user_acceptance":true,"mutates_accepted_model_state":false},"professional_boundary":{"human_review_required":true,"software_makes_compliance_claim":false,"software_makes_certification_claim":false,"software_makes_sealing_claim":false,"software_makes_approval_claim":false,"software_makes_authentication_claim":false},"rationale":"Proposed Node coordinate edit for local review."}],"submitted_operations_trust":"untrusted_submitted_metadata_not_validation_evidence","submitted_initial_model_hash":{"algorithm":"sha256","canonicalization":"rfc8785_jcs","payload_scope":"model_payload","payload_ref":"example-project","value":"0000000000000000000000000000000000000000000000000000000000000000","hash_status":"computed_local_preview"},"applied_model":null,"applied_model_backend_hash":null,"acceptance":null,"professional_boundary":{"human_review_required":true,"software_makes_compliance_claim":false,"software_makes_certification_claim":false,"software_makes_sealing_claim":false,"software_makes_approval_claim":false,"software_makes_authentication_claim":false},"audit_boundary":{"mutation_route":"structured_operations_only","direct_model_mutation_allowed":false,"requires_user_acceptance":true,"input_model_mutated_in_place":false,"applied_model_is_new_document":false,"agent_runtime_binding":"held_D58","source_identity_verification":"not_performed_asserted_metadata_only"}}}}
```

`submit` stdin:

```json
{"workspace":"example-workspace","preview_ref":"example-preview","idempotency_key":"example-stable-key"}
```

stdout:

```json
{"protocol_version":1,"request_id":"example-request-4","app_instance_id":"example-app","result":{"workspace":"example-workspace","ticket":"example-ticket","state":"queued","reason":null,"receipt":null}}
```

`status` stdin:

```json
{"workspace":"example-workspace","ticket":"example-ticket"}
```

stdout:

```json
{"protocol_version":1,"request_id":"example-request-5","app_instance_id":"example-app","result":{"workspace":"example-workspace","ticket":"example-ticket","state":"withdrawn","reason":"ui_clear","receipt":null}}
```
