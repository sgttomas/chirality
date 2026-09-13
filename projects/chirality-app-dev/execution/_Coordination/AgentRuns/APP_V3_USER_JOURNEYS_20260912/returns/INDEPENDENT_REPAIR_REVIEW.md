# Independent repair review

Verdict: **PASS — no actionable finding in the reviewed repair candidate.** Prior findings F1–F3 are closed for source-review purposes at `266c121bb32f9a22c072e7fb3b3f650b290bcdc6`. This does not establish owner acceptance, native qualification, journey completion, or release approval.

Reviewer: TASK / Type 2, gpt-6-astra high, continuing independent reviewer `/root/candidate_independent_review` under parent `/root`. The parent extended the same bounded expert-review exception and authorized only this separate return. No delegation, product repair, Git mutation, build, full-suite rerun, live UI/API/model/account action, or protected-state access. The original historical review remains unchanged.

## Subject and coverage

Reviewed the full **34-file** diff `4031c6c54f76760baaaf3d92e2db83819ce3a8ac` → `266c121bb32f9a22c072e7fb3b3f650b290bcdc6` in `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`. Read every changed file, repair returns, prior review, and connecting source. Coverage includes the additive receipt API, local recovery and UI, native evidence reconciliation, routing, approval classification, all affected tests, reconnect fixture cleanup, three timing-fixture calibrations, and campaign evidence. The exact changed-file inventory follows below.

This follow-up composes with the prior complete 98-file review of `6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f` → `4031c6c54f76760baaaf3d92e2db83819ce3a8ac`. It did not merely check the reported finding lines. Prior review SHA-256: `66eb07887415bb187888c9937bd01c41077ba72ac9bdb39ab18a2e4a04f73d5d`. Root/App/Runtime/TASK/software-code-review instruction origins and hashes remain as recorded there; this repair diff changes none of those instructions. The follow-up purpose and narrower write target are supplied by the parent's recorded native follow-up message.

## Finding dispositions and connecting behavior

**F1 closed.** `harness-event-views.ts` classifies the same five approval methods supported by the supervisor, including both legacy names. The live reader consumes that shared classifier, so inline and attention subscribers receive the rows. The old permission fallback still suppresses native requestId-bearing approvals, preserving one actionable card. Tests exercise both legacy methods on both surfaces, owner-session answer payload and disappearance after resolution. The answer path remains the existing authorized Runtime request reply; no permission default or policy change was introduced.

**F2 closed.** The user can explicitly Check delivery for each unresolved operation. App retains operation ID, expected Runtime turn and original text before the first browser request; reload can recover identity from local storage or canonical steering events. Local saved status is not used as proof of receipt. Multiple operations retain distinct check actions and same-text uncertainty guards.

Traced Check delivery through `checkHarnessSteeringReceipt` → App receipt route → explicit session-routed `steerReceipt` → project-scoped client → authorized daemon receipt route → `NativeSteering.receipt`. The request has only operation/expected-turn identity. This is a distinct endpoint: it has no path to dispatch, state-based submission or intent creation. Missing intent returns unknown even while a turn is active. Therefore a browser failure before original intent cannot turn Check delivery into a new input submission.

Runtime validates the recorded target and original payload, waits for an in-flight original outcome before reconciling, preserves explicit rejection, and matches only primary-thread native userMessage identity/content/turn evidence. Late confirmation appends accepted evidence through the existing journal/publication path. No echo remains unknown; lookup works after turn completion or manager recreation. The App validates response identity, clears only a matching current draft, updates its recorded steering message after the live observer ends, and keeps accepted receipt state from being downgraded by a later unknown update. Session checks prevent a late receipt response from changing another chat's composer/messages. Read-only receipt checking does not alter Stop, create a new turn, or reload instructions.

Inspected tests cover the no-intent/non-dispatch case, wrong identity, rejected/unknown/accepted states, primary-versus-child echo, late/idle/recreated-manager confirmation, in-flight ordering, route encoding/authorization/body constraints, durable identity recovery and reload after pre-intent transport loss. These controls substantiate the repair rather than treating an unchanged disabled button as resolution.

**F3 closed.** Uncached scoped probes defer only WORKING_ROOT_CONFLICT and WORKING_ROOT_INACCESSIBLE and continue to another verified port or authoritative recovery. The successful owner still passes its own project/session verification. Ownership consistency checks are outside the deferred-error catch. Cached owner checks, actual-owner drift, authentication/authorization and transport errors remain enforcing failures. The deferred error is retained if no verified owner can be found. Tests exercise unrelated A drift/inaccessibility with uncached B children, actual B drift with no turn dispatch, fatal authorization failure, old-folder receipt routing and restart recovery.

## Other changed files

Reconnect fixtures now provide controlled browser timers and unmount renderers before deleting globals; the added assertion checks one continuing poll after reconnect and no poll after unmount. The two 15-second filesystem test limits leave their complete-bundle content/integrity assertions unchanged. The Pi success fixture alone receives a two-second operation deadline; the helper's short hung-stream deadline and timeout tests remain intact. These are bounded test-environment calibrations, not weakened production timeout checks.

Campaign records distinguish historical baseline runs, source repair, controlled checks, independent artifact review and remaining native qualification. The newly committed historical review still states changes required for its original candidate; this separate return closes those findings only for the repaired revision. No blanket native-success inference is made from test totals or artifact quality.

## Verification and limits

APP-HOLD-1 reliance check at `266c121bb32f9a22c072e7fb3b3f650b290bcdc6`: ALLOW, all CLEAR/NOT_HELD for DEL-02-01, DEL-02-02, DEL-02-04, DEL-03-01, DEL-03-03. Entry `APP_V3_USER_JOURNEYS_20260912:INDEPENDENT_REPAIR_REVIEW`; register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `24fec92c47f90aa157a82cf1cba03eabcb63e3f44d524e0213839f47dda019a1`.

No duplicate suites were run by this reviewer. Inspected controlled tests and repair evidence; parent reports full frontend 2218 pass / four skip, integrated typecheck pass, and 11 focused new Runtime receipt/route checks following the prior 352-test Runtime run. The prior Runtime total remains evidence for the prior candidate, not an independently rerun full suite on this repair.

Residual limits: receipt identity persistence is best-effort when browser storage is unavailable; missing canonical intent is deliberately unknown. Native descendants remain subject to the disclosed primary-observer lifetime. Rotating cross-folder attention retains its existing polling latency. These are not new actionable source findings in this diff. Real browser focus/rendering, supplier behavior, authentication, journey outputs and packaged release checks remain with the parent and must be claimed from their actual evidence.

## Handoff

Independent source repair review is complete and suitable for manager fan-in. No unresolved actionable review finding remains for `266c121bb32f9a22c072e7fb3b3f650b290bcdc6` when composed with the prior full review and these dispositions. This is a derivative review of immutable Git snapshots; no authority pointer was moved. Parent owns remaining native journeys, consolidated validation and qualified release handoff. Re-review materially changed source or affected integration behavior after this frozen candidate.

## Exact repair coverage manifest

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/RUN_LOG.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/INDEPENDENT_CANDIDATE_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CHAT_ATTENTION_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CROSS_FOLDER_SESSION_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/INDEPENDENT_CANDIDATE_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/J04_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_F1_F2_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_F1_F2_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_RUNTIME_IMPLEMENTATION.md`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/daemon-proxy-boundary.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/fake-daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/turn-route-attachments.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-turn-attach.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/live-session-requests.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/prepare-packaged-instruction-root.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`
- `projects/chirality-app-dev/frontend/src/app/api/harness/session/[id]/turn/steer/receipt/route.ts`
- `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/request-card.tsx`
- `projects/chirality-app-dev/frontend/src/lib/harness/client.ts`
- `projects/chirality-app-dev/frontend/src/lib/runtime-client/daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-views.ts`
- `projects/chirality-app-dev/frontend/src/lib/shell/steering-receipts.ts`
- `projects/chirality-runtime/packages/client/src/client.ts`
- `projects/chirality-runtime/packages/contracts/src/protocol.ts`
- `projects/chirality-runtime/packages/daemon/src/native-steering.ts`
- `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts`
- `projects/chirality-runtime/tests/daemon.test.ts`
- `projects/chirality-runtime/tests/native-steering.test.ts`
