# Application-owned dynamic tools

Owner direction in dev - app, 2026-09-20 UTC: “we need to work on those dynamic tools now. They will be application specific. SWBPIPE is the first app to receive tools that's why you found the response you didi.” Additional steer: application-specific workflows and skills may be necessary or advantageous.

Runtime-only implementation branch codex/runtime-application-tools at baseline 485051eac923c759238948a54cd7bb094eee4899. Write scope projects/chirality-runtime/**. No Piping, Root, App source or instruction writes; no release or live SWBPIPE client adoption. Piping peer lead 01a0bc58-e7c0-7f11-a2ca-7b00e261014e acknowledged this split. That lead alone edits the shared Piping coordination note and retains its B3 controller/UI/native work. No ports/native/CUA claimed; Piping reserves 5173–5175 and 5183–5186. Request a slot before native work/builds that affect their benchmarks.

## Intended result

Runtime accepts application-owned dynamic-tool descriptions for a new conversation, supplies them to stock Codex, routes actual calls to the authenticated owning application, and returns application results. Runtime owns transport and call lifecycle; applications own domain validation, basis tokens, human review and commits. Existing clients with no tool registration retain current behavior.

SWBPIPE's proposed first tools: inspect_selection, preview_operations, submit_proposal, get_proposal_status (flat swbpipe_* names are compatible). First slice has no agent-facing Apply. Piping's adapter preserves the original inspection basis (workspace generation, project/workspace identity, revision AND canonical hash), returns explicit queued/stale/cancelled/busy/unavailable results, and validates basis again at UI acceptance. Undo to equal content must invalidate old proposals. Include delayed/duplicate delivery, project switch and stale-before-arrival tests when Piping implements its adapter. Existing offline intake silently captures queue-time basis and is not itself the live adapter.

## Protocol evidence

A separate TASK, gpt-6-astra medium, generated experimental TS from the installed stock Codex0.154.0 binary into /tmp/chirality-dynamic-protocol.lQYbNO/ts. No model turn, user configuration or authentication was used. Binary SHA256 4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc.

DynamicToolSpec is a discriminated function or namespace spec. thread/start takes dynamicTools; thread/resume does not. Definitions persist upstream in rollout metadata. Runtime already initializes experimentalApi:true. Calls carry original threadId, turnId, callId, nullable namespace, tool and arguments; JSON-RPC request ID is distinct. Responses contain success and contentItems (inputText/inputImage/inputAudio). Native descendant inheritance remains unqualified; preserve actual caller IDs if routing observed descendants. Do not claim mock coverage establishes native inheritance.

Official reference: https://learn.chatgpt.com/docs/app-server (dynamic tool calls and thread persistence).

## Work sequence

1. Define additive Runtime contracts and immutable per-session catalog storage; authenticated application binding and explicit dispatch/results channel.
2. Implement registry lifecycle, Codex registration/call routing, daemon/client API and cancellation/reconnect behavior with controlled integration tests.
3. Document the application adapter boundary and provide an executable controlled first-consumer example/test without adopting SWBPIPE as a live Runtime client.
4. Fresh independent review, registered Runtime build/typecheck/full tests, affected App compatibility checks as read-only validation, then normal PR/CI/merge under standing Git grant. No product release in this tranche.

Tool-use skills and reusable workflows remain application-owned guidance through existing discovery. Runtime does not gain Piping domain rules. Owner-scoped adoption prerequisites identified by the Piping lead (D-58/DEC-091 and F-PIP-1/F-PIP-4) remain separate from this reusable mechanism.

## Coordination and current state

Implementation is present in portable contracts, SessionStore catalog persistence, the app-tool registry, CodexSupervisor, daemon/client routes and app-owned composition. Pinned-protocol assessment complete. Owner and peer scopes acknowledged. The ordinary system Python lacks PyYAML; the old temporary Python command also failed the entry status/drift invocation. Resolve that local interpreter setup before recording those checks as passed. Historical Runtime daemon/admission holds are superseded by D-GOV-43/SCA-004 as recorded in the dated current handoff; do not resurrect them.


## Implemented and checked

- Application tool catalog is stored separately beside session.json under the existing session mutation lock. First registration precedes boot/first turn. Used tool-free sessions and catalog changes are refused; matching persisted catalogs can rebind volatile handlers.
- Host-only PUT/GET/DELETE application-tools plus GET calls and POST invocation result share the existing authenticated socket. Ordinary project clients cannot register or complete application calls. There is no handler URL/path registration or separate listener.
- Application-specific schemas/results remain application-owned. Runtime validates bounded JSON/descriptor identity and carries original caller identifiers, without interpreting Piping operations or granting human Apply.
- Registry author application_tool_registry and supervisor author dynamic_tools_supervisor were separate TASK instances, gpt-6-astra medium. Each wrote disjoint files. Parent validated and integrated returns, including repairs for unregistered-session active-state leakage, terminal duplicate completion acknowledgment, and per-child/request cancellation reaching the actual registry.
- Typecheck passed. Full Runtime suite: 42 files, 401 tests passed with two workers. Targeted composition covers the real client/socket/store/registry/supervisor with a controlled provider: ordinary consecutive turns, host-only authorization, descriptor injection, original caller identity, observer disconnect, result dedupe, Stop, replay and service restart/rebinding.
- Exact stock offline thread/start accepted a function descriptor under network denial with no account/model turn. Frames: /tmp/chirality-offline-tools-wgz874c1/protocol.json. Zero-turn resume reported no rollout, so persistence and native descendant inheritance are not established by that probe. Relevant controlled regression coverage does not replace a future live consumer qualification.
- The fresh temporary Python environment /tmp/chirality-runtime-tools-python resolved missing PyYAML. Runtime entry status/drift then passed, with 7/7 historical status consistency and no mismatches. D-GOV-43 supersession remains the substantive current reading of those legacy counts.
- Piping's peer clarified DEC-051 permits owner-configured provider transmission without a new app opt-in/residency gate. This implementation introduces no such gate. D-58/DEC-091 and DEC-042 successor/client adoption and live binding remain with Piping. Its B3/B3A/B3B work and native slot remain untouched.

Next: fresh independent full-diff review, affected fixes/backchecks if needed, required PR CI (including App compatibility), and normal merge. No release or real SWBPIPE activation. Application-specific skill/workflow authoring remains with the Piping lead after the initial ad hoc journey is proved; Runtime supports existing discovery and does not author a second domain instruction system.

## Independent review and repair

Fresh read-only application_tools_independent_review used gpt-6-astra high under the owner's standing bounded exception for consequential concurrency review. Its full da95ec194 diff review found one P1: a tool request resolved while awaiting initial provider-turn identity could dispatch after adoption because cancellation tracking began too late. Scope validation passed; no other confirmed defect. Direct unsupported user-data mutation did not justify restoring retired tamper/admission machinery.

The separate supervisor author reserved cancellation ownership before that await and made the resumed continuation inert after cancellation. Six real-registry regressions cover request resolution, provider exit, interrupt, abort, retirement and close before primary adoption; each prevents late dispatch. Parent inspected the exact repair. The author reports 83 affected tests and Runtime typecheck passed. Independent backcheck of the repaired committed candidate is next, followed by required CI. No source push or merge preceded that review boundary.

The Piping lead reviewed the proposed interface and reported no consumer-fit blocker, separately from independent code review or Piping adoption. It will derive workspace identity from trusted binding context, preserve basis/revision/hash and proposal status in Piping, return queued promptly from submit, and retain domain receipts independently of transient Runtime call records. Its B3 and native reservations continue.
