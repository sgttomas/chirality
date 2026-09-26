# Independent implementation review — changes required

Reviewer: `/root/live_manager/implementation_review`, nonimplementing TASK Type 2, parent `/root/live_manager`; delegated-harness-native execution, no descendants. Reviewed candidate `1811d70a129419d8d06502b61ef28bb2977a6d93` against complete diff base `2b31099233df5f3504959cdf8d9fbf90904ff938` in the assigned isolated checkout. This is implementation review, not the earlier wire review or an acceptance act.

**Disposition: not suitable for implementation fan-in as complete. Repair R1–R5, run affected checks in the subsequently released lane, and obtain independent backcheck on the actual repaired candidate.** R1 prevents the real native bridge from registering. R2–R5 are additional implementation defects established by source tracing; their proposed regressions were not executed by this reviewer.

## Candidate and scope evidence

All 54 changed working-tree files were byte-compared with the frozen candidate and matched. The 17 product/test/guide paths fall within N/F ownership, including the maintained fixture allowed by BINDING_CLARIFICATIONS.md; the remainder are the owned implementation evidence and unchanged activation copy. The repository scope validator returned PASS with no violations. No core, Runtime/App, main.rs, Tauri config, Cargo.lock, or unrelated source changed in this diff.

Recomputed wire SHA-256 is `91f4910026bcceffc98c669a4d2487539ad63cc878822061e6cc1b40c98c40ce`. Activation SHA-256 is `9fda39962acb516469ddcfa7898119e16a9104316b57ebb0d2a5e6b9356c6628`, and its bytes equal the file at ROOT commit `adc346bcc4a5685a5dd3adcec0589742ffe9a21d`. Forty-two recorded source/artifact/log SHA-256 comparisons passed. Instruction origins, skill origin, complete changed-path identities and consulted supplier sources are in `CONSULTED_SOURCES.json`.

Full Root AGENTS, canonical TASK, Piping AGENTS and software-code-review skill were read. No other role was activated. Scope validation was a read-only source check, not a product test. No tests, builds, npm, native application, socket, browser/CUA, network, primary checkout, index/Git mutation or PID9925 interaction occurred. Only this return and its consulted-source manifest were written.

## Actionable findings

### R1 — P1 — Grant the native event subscriptions required before registration

Location: `projects/chirality-piping/apps/desktop/src/services/liveControlBridge.ts:35–46`.

Trigger: start this candidate as an opted-in Tauri app. The first awaited `listen` invokes `plugin:event|listen`; it must succeed before `live_control_register` is called. The candidate has no capabilities directory/file, no inline configured capabilities, and no runtime capability addition. Its unchanged `build.rs` only calls `tauri_build::build()`. Both retained native build-output `capabilities.json` files and `gen/schemas/capabilities.json` contain `{}`.

The resolved supplier proves the consequence: `@tauri-apps/api` 2.11.0 `event.js:71–84` invokes that plugin command; Tauri 2.11.1 `src/webview/mod.rs:1823–1851` denies plugin commands without a resolved ACL, and `src/ipc/authority.rs:439–470` requires an allowed command matching the source. Tauri-codegen 2.6.1 `src/context.rs:402–417` loads the empty capabilities, with tauri-utils 2.9.1 `src/acl/mod.rs:353–375` supplying no implicit default grant. The bridge catch at lines 53–57 silently ends setup. The native socket can exist, but requests remain `not_ready` because no frontend registration ever occurs.

Repair: add the narrowly authorized local-main event listen/unlisten capability, using resolved permission identifiers and no broader default, remote, emit, file or shell grant. Parent supplied `REPAIR_SCOPE.md` during review authorizing that named extension; the source remained frozen. Verify generated ACL admission plus real listener/register/reply/unregister behavior when native resources are released. The mocked bridge tests cannot exercise Tauri ACL. The existing nativeMenu listener uses the same baseline dependency, but this finding concerns the newly introduced bridge's unconditional registration blocker; it does not claim this PR introduced the older menu issue.

### R2 — P2 — Settle a submit removed by Clear before first publication

Location: `projects/chirality-piping/apps/desktop/src/features/workspace/liveControlController.ts:450–469`; integration at `workspaceSession.ts:605–608` and existing `handleClearReviewQueue` at `workspaceSession.ts:1020–1035`.

Trigger: a submit reserves its ticket and schedules the React queue update, then Clear removes that entry before the first committed layout observation. The committed observer sees no token and unchanged generation/revision. Clear only advances the hook request epoch; it never marks the controller ticket cancelled. The ticket therefore has `published=false`, `cancelled=false`, no reason and an unresolved promise. None of the observer branches settles it, despite observed queue absence. Original and joined same-key submissions continue waiting. In the real carrier this unnecessarily reaches the 30-second transport deadline and uncertainty; without a subsequent abort/retirement the controller promise remains pending indefinitely.

Repair: explicitly identify admissions retired by Clear and carry that fact to the committed absence observer. Only after absence is observed return the pre-publication cancellation outcome; retain already observed queues as `withdrawn` and preserve observed commits. Regression: schedule submit and Clear in one controlled React publication interval, observe absence, and require both original and joined submissions to settle without a socket timeout. Also retain the existing post-publication disconnect and Clear assertions. Current tests cover AbortSignal cancellation and Clear after queued acknowledgement, not this trigger.

### R3 — P2 — Honor request invalidation while preview validation is awaiting

Location: `projects/chirality-piping/apps/desktop/src/features/workspace/liveControlController.ts:315–333`; the freshness predicate at lines 105–110 and `LiveSnapshot` omit the hook request epoch.

Trigger: begin an external preview, hold its engine validation response, and invoke local Clear while the model is unchanged. Clear increments `requestEpochRef`, intentionally retiring in-flight operation work. When the preview resolves, the live controller checks only workspace, model revision/hash and AbortSignal; neither of those changed. It issues a successful, submittable preview from the retired request, allowing the pending proposal to reappear when subsequently submitted. This is distinct from R2, which concerns a submit already awaiting queue publication.

The frozen wire's publication/recovery algorithm explicitly requires checking request epoch after awaits. Existing GUI batch preparation does check it at `workspaceSession.ts:1039–1045`; the new external path bypasses that boundary.

Repair: capture an invocation-owned request epoch and reject its asynchronous completion when the owning hook invalidates it. Do not erase historical ticket/commit recovery. Regression: delay real-engine preview completion across Clear, then require no passed/submittable reference and no queue/history/model mutation; a fresh request after Clear may proceed. Also retain model/project-change and cancellation checks. This finding does not assert any external Apply capability.

### R4 — P2 — Use explicit main-target delivery for native request and cancel events

Location: `projects/chirality-piping/apps/desktop/src-tauri/src/live_control.rs:336–339`.

Calling `window.emit(event, payload)` does not target that window. In the exact resolved Tauri 2.11.1 supplier, `Emitter::emit` (`src/lib.rs:933–949`) delegates to the global manager; `src/manager/mod.rs:534–549` emits to all webviews and native listeners. Consequently every dispatch/cancellation is broadcast, contrary to the acknowledged main-only event destination and the source-ready claim of targeted events. An additional eligible listener outside the registered main target receives proposal parameters and registration/dispatch identities. The present single configured window limits immediate reachability; no observed cross-window disclosure is claimed.

Repair: use the actual main-target emission API for both events, retain invoking-main checks, and align frontend listener targeting with the installed API. A narrow local-main ACL is also necessary: supplier event routing deliberately allows `Any` listeners, so a target label alone must not be advertised as a general confidentiality boundary. Backcheck the resolved sender/receiver target semantics and exercise main delivery with non-main admission denied; injected emitter closures in current tests do not verify this seam.

### R5 — P2 — Require the response correlation key to exist

Location: `projects/chirality-piping/apps/desktop/src-tauri/src/bin/swbpipe-control.rs:129–137`.

Trigger: the endpoint returns four keys consisting of `protocol_version:1`, the correct `app_instance_id`, a well-formed `error`, and an unknown field, omitting `request_id`. The length check passes. Serde JSON indexing of a missing key yields Null, so `response["request_id"].is_null()` accepts the missing field as the permitted explicit pre-correlation null. `validate_reply` subsequently sees only the extracted error and accepts it. The CLI forwards a malformed, uncorrelated envelope instead of rejecting unknown/missing fields as promised. The existing extra-field test only adds a fifth key to a complete success envelope and misses this substitution case.

Repair: validate the exact success/error key set and require an explicit `request_id` value that is either the expected string or, only on a structured error, explicit null. Add missing-request-id-plus-extra-key, missing-request-id-with-both-result/error, wrong-type, valid-null-error and normal correlated response regressions. Invalid responses must yield the existing safe uncertainty diagnostic, preserving original-submit retry guidance.

## Verification reviewed and practical limits

The final recorded TypeScript pass and 4-suite/33-test frontend pass match the supplied final source manifest. Test bodies support ordinary one/two-member Apply, one checkpoint, queue observation, same-key reservation/recovery, invalid later member rollback, stale basis, Clear after publication, immediate Undo/project switch while receipt hash waits, retained hash retry, and mocked bridge lifecycle. The initial TypeScript error and three bridge test-timing failures are retained; the final bodies preserve their assertions while using observed readiness/cleanup. These passes do not cover the Clear races above or real Tauri permission/target behavior.

Native evidence supports 8 filtered library tests, 6 transport tests, 3 CLI unit plus 3 CLI integration tests and the explicit feature-gated CLI build. The initial two bind EPERM failures are preserved and distinct from the supported escalated fixture pass. The fixture RAII repair and final identity changes are recorded. Library-tested production native source is unchanged in the later native manifest; the later CLI/fixture changes received their corresponding reruns. No protected oracle/tolerance/limit weakening was found. Two nonfatal desktop-library dead-code warnings remain.

Source tracing found no external Apply method or second authoritative model store. Native restores correlation independently of frontend payloads; capability bytes are not forwarded to the controller. Apply goes through the existing atomic engine and hook. The publication observer checks model/history/receipt/queue/result state before retaining an immutable after-model for independent canonical hashing. Same-key historical lookup precedes current-workspace/new-owner checks. Save/Open retain existing model/intent-context semantics; pending queue registry is not persisted or replayed. Explicit desktop default and CLI feature gating preserve main.rs's self-test entrypoint at source level.

Separate outstanding qualification remains: actual Tauri invoking-main registration/event/reply and CLI-to-controller path I1/I2; optional disabled startup; actual package/default target and packaged saved/edited-load self-test; long timeout/concurrent connection execution; unsupported-host compilation; relevant native Save/Open/normalized persistence, lost reply, restart/remount and old-handle reconciliation; broader registered checks, clean DEC-025 sweep and CI on ROOT's eventual integrated candidate. None is closed by this review or by aggregate component counts.

Actual-human H1/H2 single/ordered-batch review and Apply are still required and unperformed. No verified actor identity, engineering or Runtime qualification, usability acceptance, governed lifecycle acceptance, durable recovery or release is granted. Return to `/root/live_manager` for bounded repair/integration; ROOT retains programme graph, resource scheduling, push/PR/merge and later native/human witness coordination.
