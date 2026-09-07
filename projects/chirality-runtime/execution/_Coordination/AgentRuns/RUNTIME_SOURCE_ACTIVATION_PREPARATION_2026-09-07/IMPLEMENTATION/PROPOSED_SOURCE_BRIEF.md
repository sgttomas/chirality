# Proposed bounded source and synthetic increment

Candidate only; source remains unactivated. Baseline `bf204d8fd0bc55363b189a471e01461eb0cdf28a` (PR744); inspected source/test bytes equal prior `c8cf83dc7645ecb8291508aab22ec00f4bfbc0dd` and current main. This derivative proposal consumes the published DEL-02-06/09 SOWs and frozen wave1 capability findings, using the earlier NEXT_GRANT as its starting point. It narrows that earlier proposal to one coherent implementable increment; the settled custody choices are unchanged.

The increment removes credential-file identity claims, makes selected managed-auth configuration explicit, and reports truthful unavailable hosted readiness. It does not implement pre-folder bootstrap, global account switch/sign-out, or a working one-sign-in experience. Those requirements remain pending dependent contract work below. No supplier, account, keychain, live model, protected fixture, App, Root, Git publication or release operation is included.

## Exact candidate contract delta

Keep existing `/v2/projects/:projectId/login/start|status|cancel` routes and their authenticated control/admission checks. Do not introduce API v3, endpoints, terminal events or fake project registration. Propose replacing HostedLoginStatus's unversioned hash-bearing body with this exact minimal shape (all fields shown except loginId and hasAccount required):

```json
{
  "schema": "chirality-hosted-login-status/v2",
  "state": "completed",
  "loginId": "fixture-login-1",
  "hasAccount": true,
  "evidenceClass": "controlled-fixture",
  "binding": {
    "schema": "chirality-hosted-account-binding/v1",
    "state": "unavailable",
    "reason": "canonical-identity-producer-unavailable"
  },
  "hostedReady": false
}
```

State remains pending/completed/failed and denotes the bounded login ceremony only. Existing evidenceClass remains exact-supply-login/controlled-fixture; neither means qualification. `hasAccount` is supplier presence only. Optional loginId retains the existing bounded identifier rule; no auth URL is present in status (the existing start response still returns its validated official URL). Every state carries the same unavailable binding and hostedReady:false in this increment. Unknown/extra fields, missing version, raw authBindingSha256, mixed versions, caller verified identity, token/email/plan fields and any hostedReady:true are rejected by typed validators. No fabricated successful binding variant is introduced. Nonsecret stable identity remains unavailable even after a successful synthetic ceremony. Existing Runtime error codes remain: malformed config/client response INVALID_REQUEST, unavailable admission ENGINE_UNAVAILABLE, malformed internal login projection INTERNAL_FAILURE. No new public error taxonomy.

For hosted-validation standalone configuration only, propose schema `chirality-standalone-hosted/v2`, retaining current mandatory project/identity/compatibility/storage fields but replacing worker.authBindingSha256 with worker.managedAuth exactly `{ "backend": "keyring", "binding": { "schema": "chirality-hosted-account-binding/v1", "state": "unavailable", "reason": "canonical-identity-producer-unavailable" } }`. No verified state or caller identity can unlock admission. Other standalone modes retain chirality-standalone/v1 unchanged. Legacy hosted v1, mixed hash/new settings, file/auto backend and unknown fields fail closed. WorkerContinuity.accountId remains a declared continuity value, never a new verified principal. This is a proposed breaking hosted configuration/status change subject to the exact activation and client review; no silent migration or rewrite of accepted conformance evidence.

## Exact source write allowlist

Paths below are relative to `projects/chirality-runtime/`.

| File | Bounded implementation |
| --- | --- |
| packages/contracts/src/delegated.ts | Replace hosted status interface with the exact versioned unavailable status/binding contract above and shared bounded validator usable by daemon/client. No executable capability or successful producer type. |
| packages/daemon/src/codex-login.ts | Replace auth.json open/read/hash binding with unavailable nonsecret status. Use shared status contract. Explicit keyring launch configuration for the trusted login purpose only; construction remains inert. Preserve bounded cancellation/close and pending-completion race handling. Refuse production login before filesystem/account/keyring/process effects unless exact supplier/backend/trusted-auth-purpose qualification is independently established; existing verifyExactSupply alone is insufficient. No such qualifying basis is supplied in this increment, so production start remains unavailable; only the explicit controlled fixture seam runs. Do not invent an acceptance record or expose a newly usable keyring route. |
| packages/daemon/src/codex-session.ts | Strict account presence projection, with no invented identity RPC/field; preserve login-purpose prohibition on dynamic tools, thread start/resume and turn start. Validate/quarantine unrecognized data without exporting it. |
| packages/daemon/src/codex-containment.ts | Introduce an explicit trusted-login purpose discriminator for keyring config and its narrow auth-process securityd exception. Default/work/tool denial remains. Update hosted native configuration keyring literal and config digest inputs consistently while hosted launch remains unavailable. Pure configuration/profile construction can be tested with injected filesystem/platform seams; no sandbox or keyring invocation. |
| packages/daemon/src/codex-supervisor.ts | Remove auth-file identity reads and admission dependence on their hash. Enforce unavailable producer before production launch/account access on all ordinary and manager entry paths; no fixture-derived identity can satisfy production. Update config digest to include the new managedAuth schema/backend. Keep controlled fixture evidence distinct. Do not convert an unavailable result into accountDigest or bypass conformance. |
| packages/daemon/src/standalone.ts | Validate the exact hosted configuration replacement; wire login-purpose and unavailable managedAuth options. Preserve existing project-bound topology and local/controlled modes. No bootstrap mode in this increment. |
| packages/daemon/src/runtime-daemon.ts | Validate/project the exact shared status through the current authenticated route; keep start/cancel authorization unchanged. Reject legacy/mixed/internal secret-bearing status. |
| packages/daemon/src/supervisor-server.ts | Carry and validate the versioned safe status through existing login-status op; retain exact authenticated supervisor control surface. No new operation. |
| packages/client/src/client.ts | Validate hostedLoginStatus response instead of its current unchecked generic return. Reject old/mixed or ready-looking status. This is an explicit addition to the earlier allowlist, required for a coherent Runtime client contract. |

Do not edit packages/core/src/runtime-conformance.ts: preserve accepted schema and records. Unavailable production admission prevents use of any old account-file binding; changed source/config digests independently invalidate previous acceptance. Never feed the unavailable sentinel's digest as verified accountDigest. Do not edit codex-worker.ts: its offline/account-free probe remains offline with unchanged securityd denial. No hosted-auth-state.ts is created in this increment: an unwired synthetic global state store would not implement the pending lifecycle contract.

## Exact synthetic file/command allowlist

Edit `tests/codex-login.test.ts`, `tests/codex-session.test.ts`, `tests/codex-supervisor.test.ts`, `tests/standalone.test.ts`; add `tests/custody-config-status.test.ts` and `vitest.custody.config.ts`. The two additional existing test files are concrete fixture-maintenance deltas to the earlier list: both encode authBindingSha256; standalone currently accepts it, supervisor asserts auth-file validation. Replace those affected assertions with new schema/unavailable behavior, naming all changed/new cases in those two files with prefix `custody `. Do not edit or execute their unrelated tests. The new custody test covers mocked client/daemon/supervisor status paths and config/admission guards, plus pure purpose-scoped profile rendering. Read-only regression files are tests/hosted-consent.test.ts and tests/runtime-conformance.test.ts.

The explicit Vitest config must set workspace root here, setupFiles:[], globalSetup:[], no plugins or extra workspaces, and include exactly these seven files: custody-config-status, codex-login, codex-session, codex-supervisor, standalone, hosted-consent, runtime-conformance (each tests/*.test.ts). Inspect final tests/config/import hooks before any command. Standalone and supervisor custody-prefixed cases must mock process launch, platform/containment, credential/supply/registry effects as needed; their suite hooks must touch only owned synthetic temp data. If their inherited hooks cannot meet that condition, move the changed assertions to custody-config-status and exclude those files from execution; report that exact config change for activation review before running, never silently broaden. Never run their entire suites under this proposal.

After explicit source+synthetic activation only, from the Runtime workspace:

```sh
npm run typecheck --ignore-scripts
npm test --ignore-scripts -- --config vitest.custody.config.ts tests/custody-config-status.test.ts tests/codex-login.test.ts tests/codex-session.test.ts tests/hosted-consent.test.ts
npm test --ignore-scripts -- --config vitest.custody.config.ts tests/codex-supervisor.test.ts tests/standalone.test.ts --testNamePattern '^.*custody '
npm test --ignore-scripts -- --config vitest.custody.config.ts tests/runtime-conformance.test.ts --testNamePattern '^invalidates changed binding'
```

package.json currently resolves to tsc -b --pretty false and vitest run with no pre/post hooks. Existing package typecheck includes src, not tests, and emits packages/*/dist plus build-info: allow these as local verification outputs only. Missing dependencies stop validation; installation/package/version/lockfile changes are excluded. Login/session fixture child processes use process.execPath and inline JSONL scripts; only those fake processes and owned temporary files are permitted. Remove login fixture's obsolete need to create/read/hash synthetic auth.json. Hosted-consent cleanup is confined to its new root; its ambient-home case rejects without reading contents. Only the selected conformance case runs; inventory/protected/exact-supply suites remain excluded.

Acceptance: explicit keyring and no file/auto fallback in selected managed configuration; auth exception cannot be chosen by client or worker; default/worker securityd denial unchanged; root-private homes remain distinct; account-only login actor rejects model work; production login refuses the unqualified keyring purpose before effects, and every production worker admission rejects unavailable identity before launch/credential read; synthetic success never ready; late/cancelled completion cannot revive closed login; schema validation strips/rejects secret-bearing input; old/mixed status/config rejected; controlled/local modes preserved; old conformance cannot authorize changed source/config. Mocks prove Runtime logic only, not keyring ACLs, process boundaries, supplier identity, same-account A/B, remote revoke or one-sign-in UX.

## Remaining dependent contract work (same delivery objective)

Pre-folder bootstrap cannot be represented honestly by the present API: runtime-daemon.ts:286–292 requires project authorization, registry membership and delegated root; standalone.ts:18–33 requires project WorkerContinuity. Supervisor login is attached to a process supervisor and config digest. A subsequent exact contract proposal must specify an account-only namespace independent of project execution; authenticated Runtime control capability and its issuance/verification without an account/profile-as-proof; bootstrap status/admission scope; standalone lifetime/storage ownership; and projection into later independent A/B homes without token transfer. Do not choose an endpoint, fake canonical root or new enrollment in this increment. Existing login-purpose prohibition is useful but not bootstrap implementation.

Global hosted generation fencing needs a durable owner of all hosted contexts (bootstrap and root A/B), operations with authenticated account-wide versus folder-local scope, late refresh/completion rejection, worker/tool retirement completion, separately granted bounded revoke while auth context exists, auth retirement and cleanup outcome projection. Current SupervisorLoginPort has only start/status/cancel; it has no sign-out/revoke contract and current daemon/project wiring is root-bound. Specify those exact payloads, compatibility/continuity invalidation and failure responses before implementing hosted-auth-state or widening wiring. Ungranted/offline/impossible revoke yields local cleanup with remote unknown and no retention/replay. Local contexts remain unaffected. These settled requirements are deferred, not removed; no architecture overhaul or new queue is selected.

Stable managed identity remains a separate supplier/API evidence gap: C2/C3 registered producers do not expose the required stable account/user and selected workspace; AccountSessions declarations are not callable implementations. Accepted original capability remains unknown. No token decoding/export/hash/email workaround, custom adapter or supplier upgrade is selected. Approval work remains outside this tranche: default network choices lack decline and Runtime rejects distinct child origins; Stop is not Deny and parent IDs cannot substitute for child provenance.

## App/CLI compatibility and return

App continues on authenticated Runtime v2. Runtime client method signature now returns a validated versioned unavailable status. An updated App/CLI must present completed sign-in ceremony separately from unavailable hosted execution and must not use hasAccount/state/loginId as readiness; old integrations relying on authBindingSha256 need explicit compatibility review and must not silently interoperate. No App/CLI product source edits are granted. Return exact status/config before-after and synthetic responses for the App loop, the changed Runtime client surface, invalidation evidence, all changed file hashes and test results, and explicit producer/bootstrap/global-lifecycle/live-qualification blockers. A successful source increment adds truthful configuration/status behavior, not usable live sign-in capability.

Closure requires independent patch review, recorded synthetic results and affected consumer review before reliance; publication/acceptance, supplier eligibility and live qualification remain separately gated. Rerun preparation only for relied source/SOW/capability pin drift or a changed exact activation subject. This proposal requires one bounded source+synthetic activation; prior preparation is not that grant.
