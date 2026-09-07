# Hosted-status compatibility clarification

PROPOSED, NOT IMPLEMENTED OR RULED. This addendum corrects only the broad mixed-version fail-closed claims and rollout/evidence interpretation in the frozen 407000872059e492f367eabfc314d76b8a459503e3164d245fb3100b1af09abb source proposal. Exact new status/config schemas and nine-source/six-test-config write scope remain. All prior files are preserved. DECISION_TEXT.md below consolidates the compatibility choice with the one source activation; it preserves the standing-Git clarification from dbb19e404ecf8a7cb2636df55192cd924820610260080c6df3ea2d1d1ebc00b4.

## Recommendation and enforceable limits

Use an explicitly supported paired Runtime client/daemon rollout for hosted login status. Both mixed-version directions are unsupported, but rejection is asymmetric. Do not claim that merely naming mixed pairs unsupported makes them mechanically fail closed.

| Pair | Observable behavior and support |
|---|---|
| Updated client / updated daemon | Supported pair for the proposed versioned unavailable status, after synthetic validation and consumer review. New validator requires exact schema/fields and hostedReady:false. |
| Updated client / current daemon | New client validator rejects the old unversioned status. Test the exact rejected response and error; no status accepted or readiness inferred. |
| Current client / updated daemon | Current hostedLoginStatus returns requestJson without schema validation; requestJson parses successful JSON and casts it. It can silently accept the new body, including state:completed. This unsupported pair is **not detectable or rejectable by the current client**. |
| Current client / current daemon | Historical behavior remains historical; it supplies no validation of the new contract. |

At client.ts:502–504 the status GET carries no compatibility identity/preflight. requestJson at121–142 validates HTTP success, then `return value as T`. runtime-daemon.ts:286–300 authenticates credentials:write, project registry/root and configured login, but the GET does not identify the caller's status-schema version. Existing start/cancel preflight checks do not cover the separate status GET. An old and updated client can send the same authorized GET. The new daemon therefore cannot reliably distinguish and reject the old client under this existing request contract. Authorization, production admission refusal and hostedReady:false do not fix that status-compatibility gap. No handshake/header/endpoint or compatibility epoch change is invented here.

Paired rollout is an operational support/acceptance condition, not a new protocol guarantee: record exact Runtime client and daemon artifacts delivered together, inventory actual hosted-status callers, and do not accept an old/new pair as supported. Avoid enabling a hosted-status consumer until its deployed client/daemon pair and unavailable presentation are reviewed. If independent-version interoperability or daemon-side rejection of old status clients is required, stop and prepare an explicit additional wire contract and scope before implementation. That alternative is not silently bundled into this increment.

## Both-direction synthetic evidence within current scope

Add these cases to already allowed tests/custody-config-status.test.ts; no new source/test file or dependency is required. The existing first custody test command runs them. Use mocked request/response transport, synthetic authorization/project fixtures and no network/account/keyring/supplier effects.

1. Updated client plus updated daemon projection: exact new schema accepted, completed ceremony remains hostedReady:false, no inferred principal. Exercise malformed/extra/secret-bearing and ready-looking bodies through the new validator.
2. Updated client plus pinned old unversioned daemon body: deterministic rejection with the proposed existing INVALID_REQUEST classification. Preserve the old response shape as an explicit fixture.
3. Pinned old client semantics plus new body: faithfully reproduce its successful-JSON unchecked return using source-pinned baseline behavior; assert that the new body is accepted unchanged, **not rejected**. This is a compatibility limitation regression, not a passing fail-closed claim or proof of an old packaged binary. Do not load/execute an old supplier or install another client version.
4. Request symmetry: show old and new status GET requests under the existing method contract contain no status-version discriminator and that ordinary authorized new-daemon projection has no old-client rejection branch. Keep authorization-failure tests separate from version tests.

Return the four-case matrix, exact fixture/source pins, validator errors and paired artifact identities. Acceptance must preserve the old-client/new-daemon limitation and unsupported designation. A report saying both directions fail closed is a blocker. No extra source scope is needed for this plan; mechanical daemon rejection of old clients would require an additional reviewed request-contract change and is excluded.

## App future-port boundary

App PKG09 preliminary findings relayed by App lead through HELP_HUMAN report no current App src/electron/scripts/packages caller of hostedLoginStatus/startHostedLogin/authBindingSha256; the D122 controller has no live port. These are relayed App-owned findings, not independently re-audited here. D122 presentation work remains independent and is not blocked by this Runtime source increment.

AppAccountState's loggedOut/loggedIn-with-identity alternatives cannot losslessly represent completed ceremony plus unavailable identity/execution. A future live port must first obtain App-owned acceptance of explicit ceremony/availability semantics; do not map completion to loggedIn, invent a sentinel account/digest, or erase it into loggedOut as if no ceremony occurred. App consumer review before reliance must verify the actual paired Runtime artifacts and this state distinction. No App state/type/source edit is included. Bootstrap/global lifecycle and stable identity remain pending as in the original proposal.

Evidence is read-only source inspection and a future synthetic plan, not implementation or operational qualification. OpenAI GPT-6 exact serving ID unavailable; WORKING_ITEMS role instruction-asserted.
