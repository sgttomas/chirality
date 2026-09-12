# Incomplete repair handoff — stopped at parent boundary

Status: COMPLETED by successor, see "Successor completion" below; historical status was INCOMPLETE / UNREVIEWED. Parent explicitly stopped further product/test edits and new tests/builds for owner handoff. Preserve partial diff; do not interpret it as qualified source. No supplier/native/live account operation, payload rehash, packaging/signing or commit performed.

## Accepted basis and diagnosis

Upstream: R16_RESTART_ADMISSION/BRIEF.md, owner-observed post-GUI-relaunch failure in R16_FUNCTIONAL_FINDINGS.md, current Runtime source. This packet is derivative diagnostic evidence, not release acceptance. Exact live internal reason remains unknown; elapsed release expiry is an independent alternative to GUI replacement. No protected live state was read.

Source-established lifecycle defect: preparation captures P2 host lease; reconnect changes host client/connection identity within same daemon, making old preparation/instance invalid. Supervisor and launcher cache old objects; status.live previously checked durable account binding only. Synthetic in-memory probe lease-replacement-probe.mjs passed A valid → revoked rejected → B connected/old A rejected → new B-issued admission valid. It exercises real issuer/revalidator against synthetic in-memory HostAccountAuthority, no native ceremony. Old admissions must remain invalid.

## Partial implementation

- codex-admitted-launcher.ts: optional refreshHostAdmission(account), refuses closed/busy/active-launcher state; uses existing preparation and completion issuers against current source lease, validates release/policy, replaces future launcher preparation only. Old instances remain invalid. No new payload walk/hash.
- codex-supervisor.ts: single-flight refreshHostAdmission at idle boundary. Only HOST_AUTHORITY_NOT_LIVE can initiate renewal; other failures propagate. Rejects active entries/acquisition; cleans preadmitted candidate if present; compares full old/new inputs except hostAuthority; revalidates fresh admission; acquisition invokes refresh before acquiring.add.
- hosted-private-composition.ts: live() first checks durable account ID/epoch then v2 supervisor refresh/revalidation; updates current context and refuses closed/retired/signed-out readiness. v1 path remains unchanged.
- runtime-conformance-v2-admission.test.ts: added controlled real-issuer/factory/supervisor connecting regression. It is currently FAILING IN FIXTURE SETUP before testing implementation.

## Validation and commands

Initial Runtime npm run typecheck PASS after first production edits (exec session47865, completed0). Later minor v1 guard and new test not re-typechecked.

New test command: npx vitest run tests/runtime-conformance-v2-admission.test.ts -t 'renews an idle'. Session40316 completed exit1. Failure: synthetic basis lacks verified.payloadDigest (and needs supportProfile): purposeSourceFromBasis at runtime-conformance-v2-admission.ts336 throws Cannot read properties of undefined (reading payloadDigest), from test164. Eight unrelated tests skipped. This does NOT validate new renewal behavior. No active command remains. No new tests/builds were started after stop instruction.

## Required successor work

1. Correct synthetic release-basis fixture using existing same-file basis construction. Continue scoped connecting test through real issuer/factory/supervisor refresh. Test A disconnected refusal, B fresh success, old A rejection, active-work refusal, concurrent refresh, release expiry; add account/epoch/policy mismatch and disconnect-during-renewal negatives. Current test intends several but has not reached them.
2. Review asynchronous acquisition race introduced by await refresh before acquiring.add: repeat worker/closed/capacity checks after await as warranted, preserving preexisting cancellation and identity invariants. Review preadmitted cleanup failure ordering and factory publication safety on failed renewal; do not blindly accept partial changes.
3. Confirm live()/launch concurrent renewal behavior, no optimistic Ready during revocation, and actual next candidate identity/epoch checks. No need to relax expired releases, stale leases or payload seal policy.
4. Run focused existing launcher/supervisor/private-composition/admission tests and final Runtime tsc. Existing tests have NOT been run against this partial diff. Separate independent review required before checkpoint acceptance.
5. Runtime rebuild/typecheck output will need regeneration after final source corrections; final frontend typecheck against current Runtime dist also remains. No release packaging authorized by this partial handoff. Subsequent signed native GUI quit/relaunch with retained daemon, fresh same-account admission and real follow-up is required for closure; owner live failure cause still unconfirmed.

Write scope authorization extended by lead to these production targets and focused tests, superseding initial diagnosis-only brief. Current changes are not a new permission exception; stopping is the parent's explicit handoff boundary. No authoritative snapshot/pointer advanced.

## Successor completion (2026-09-12)

Completed by HELP_HUMAN successor on the integration checkout after PR #766.
Cause, final repair, tests and validation are recorded in RUN_LOG.md under
"Successor takeover: restart-admission repair completed". Final file hashes:
FINAL_SOURCE_HASHES.json. Required successor work items 1–4 above are done;
item 5 (native quit/relaunch verification with retained daemon) remains for the
next consolidated candidate. Independent review: INDEPENDENT_REVIEW.md.

Design decisions beyond the partial diff: renewal refusals are distinct
(retired / work active / unavailable); queued candidate retirement failures
block renewal; the supervisor rejects a renewal if its current admission
changed across the await; `acquire` rechecks cancellation after the renewal
await; `close()` awaits an in-flight renewal; composition `live()` no longer
throws or fences on a renewal failure because a relaunch that races the host
ceremony or a running turn must not retire the account binding — the durable
binding check is unchanged and the next launch either renews or fails closed.

## Native verification (Stage26/R17, 2026-09-12)

Item 5 closed. On the signed R17 App (source fb529591d) the lead quit the GUI
with both chats idle, retained daemon pid 27838, relaunched through the guarded
launcher, and the owner observed a real follow-up in the retained chat and a
real file read in the second chat complete without sign-in, account edits or
any admission fence (daemon log has no `hosted.admission.fenced`). See
../R17_FUNCTIONAL_FINDINGS.md. FINAL_SOURCE_HASHES.json status updated.
