# CI failure diagnosis — read-only

The 15 failed tests are explained by test fixtures that were not migrated with the strict hosted contracts: fourteen fail at account presence projection before their target behavior; one combines an old successful status expectation with deliberately secret-bearing input that the new contract must reject. No production admission unlock or relaxed source validator is justified. This is source/log causal diagnosis, not a rerun or proof that no additional failures remain.

## Four fixture sites and minimal correction

| File / current line | Failure mapping | Smallest proposed correction |
|---|---|---|
| tests/codex-manager.test.ts:23 | Six: JSONL callback execution; plain-text nondelegation; HMAC reply binding; cancellation; governed callback failure; stuck callback bound | Change only synthetic account discriminator `type:'fixture'` to `type:'apiKey'`. Preserve requiresOpenaiAuth:true, fake stream transport, all callback/error/retirement/HMAC assertions. |
| tests/delegated-runtime.test.ts:407 | Four: explicit allow, deny, acceptForSession; provider cancellation | Change only synthetic account discriminator `type:"fixture"` to `type:"apiKey"`. Preserve advertised decisions, prompt IDs/context, explicit-user-act, wrong-generation rejection, forwarding/ack caveat, immutable resolution and retirement assertions. |
| tests/manager-approval-integration.test.ts:37 | Four: allow/deny/acceptForSession and cancelled/changed-consent authority | Same discriminator change only. Preserve dynamic-tool registry, approval-only route denial, compatibility mismatch, explicit-user-act, response and cleanup assertions. |
| tests/delegated-runtime.test.ts:256 and 263 | One: operator login without pre-existing account; bypass confined to login | Supply a valid unavailable v2 positive status fixture and update only the exact expected status body to that approved schema. Preserve every operator/client authorization, preflight confinement, start/cancel count and empty inventory assertion. Retain intentional providerSecret coverage in a separate malformed-status negative test; see below. |

CodexTurnSession.accountRead currently accepts only exact registered outer/account shapes and returns booleans. `fixture` is not an accepted account variant; the explicit controlled supervisor still calls accountRead before thread/turn start (codex-supervisor.ts:167–169). Therefore callback code and prompt notification code cannot run. The private channel intentionally hides generic errors as `supervisor request rejected`; changing callback expectations to that message would erase coverage rather than fix fixtures. Production paths still call requireHostedIdentity before launch, and no fixture principal becomes production evidence.

The literal `apiKey` here is an in-memory registered-shape fixture, not an API key, token, external account, or new authentication route. Do not enable allowUnauthenticatedModel, invent a principal, weaken accountRead, change advertised network decisions, or rewrite child IDs.

## Preserve the secret-bearing negative contract

The old line256 response has both missing v2 fields and providerSecret; line263 expects the old daemon to strip that extra field and succeed. Under the approved contract unknown status fields are rejected, not silently stripped. Literal preservation of that old exact-body assertion is incompatible with the accepted v2 schema. Preserve its security intent with two distinct tests:

1. Existing positive operator-login test: status is exactly `{schema:"chirality-hosted-login-status/v2",state:"pending",loginId:"fixture-login",evidenceClass:"controlled-fixture",binding:{schema:"chirality-hosted-account-binding/v1",state:"unavailable",reason:"canonical-identity-producer-unavailable"},hostedReady:false}`. Assert this complete body rather than replacing success with a generic failure.
2. New negative internal-status test: use the same otherwise-valid v2 body plus `providerSecret:"must-not-project"` as deliberately malformed input. Through the authorized operator status route, assert INTERNAL_FAILURE and ensure the error serialization/message never contains the secret value. Keep worker inventory empty and ordinary client status forbidden. Because the v2 fields are valid, this specifically tests extra-field rejection rather than accidentally failing only on missing schema.

Other legacy login status builders at delegated-runtime.test.ts:273,320,336,351 are not called by their current cases. Those tests exercise unsafe start URL or cancellation/start/stop behavior; source stopLogin invokes cancel and generation draining, not status. They are noncausal to these 15 failures. Leave them out of the minimal repair, or propose separate schema-only normalization explicitly; do not silently expand this repair.

## Three unhandled rejections

CI explicitly attributes all three to delegated-runtime's explicit allow, deny and acceptForSession cases. Each starts the turn promise at line420, then polls for a prompt, and attaches the meaningful await only at line429. Account/read failure rejects that promise before the poll/assertion reaches its await. The cancellation case immediately attaches `running.catch` at line436 and does not appear in the unhandled list. Manager approval fixture likewise attaches `void run.catch` at line60.

The smallest fixture discriminator fix is expected to remove the triggering early rejection, but that is not yet proven by execution. A narrow test-harness robustness addition is `void turn.catch(() => {});` immediately after creating the original turn promise; continue awaiting that same original promise and asserting its successful output later. This marks premature rejection observed without converting it to success. Do not remove the final await, use Promise.allSettled as a pass condition, globally ignore unhandled errors, increase timeout, or replace success assertions with failure. If three fixture fixes do not remove the causal failures, stop and inspect new evidence before considering source changes.

## Effects and verification boundary

No live files changed and no local tests, Git commands, builds, supplier/provider/account/keyring/protected operations ran. Pin checks and evidence writes are the only mutations, confined to AUTHOR.

For a later expressly bounded rerun: codex-manager uses PassThrough fake supplier transport and real owner-private Unix sockets/temp roots; no actual supplier process launches in its controlled launcher. Manager-approval-integration similarly uses fake streams plus local daemon/supervisor sockets, owned auth/project/consent/approval records and synthetic capability files. Delegated-runtime includes real Node controlled processes for other cases, sockets, owned private registries and journals; its four affected approval cases use PassThrough controlledApprovalWorker, while the affected operator-login fixture creates an inert ProcessSupervisor and asserts no workers. An entire-file run has broader controlled-process effects than selecting these failures. Core barrel imports can trigger the previously documented eager source/dependency inventory. No effect here establishes kernel containment, keyring ACLs, same-account homes or supplier qualification.

Acceptance for any repair: all existing approval, callback, cancellation, retirement and authorization assertions retained; only approved schema equality updated; explicit secret-bearing negative added; zero unhandled errors; original production before-effect refusal and malformed account/status negative checks still pass. All results await authorized implementation and execution.
