# Independent root taxonomy review

Verdict: PASS; no actionable findings in the frozen three-file repair over
`0392eadea67cf5d386c14bf374f4d02bd806ad0b`.

TASK Type 2, gpt-6-astra medium, delegated-harness-native child of the campaign
parent, independent of the repair author; no delegation. Reviewed the complete
three-file diff, ROOT_TAXONOMY_REPAIR.md, and directly relevant HTTP route,
registry, and hosted-binding implementation. No unchanged campaign diff was
re-reviewed.

`registration: required` represents an unresolved project registration after
the hosted adapter handles PROJECT_NOT_FOUND. Mapping that result to
WORKING_ROOT_INACCESSIBLE/404 restores the intended refusal taxonomy without
registering a project, installing a client, or creating a session. Verification
exceptions still propagate, and a registered result without its expected bound
port retains WORKING_ROOT_CONFLICT/409.

The new regression exercises the actual POST route and registry with the real
hosted adapter and mocked Runtime transport. It checks both inaccessible and
conflicting roots, absence of initialization/creation/installation, and retained
authorized-root creation. This is meaningful boundary coverage; it is not a
live HTTP-server or Runtime integration run. The section-8 diagnostic preserves
the existing required status/type checks and reports only status plus a bounded
uppercase error token, not raw payload content.

SHA-256 basis, paths relative to the reviewed checkout:

| File | SHA-256 |
|---|---|
| projects/chirality-app-dev/frontend/src/lib/runtime-client/daemon-harness-port.ts | `43c82c0b17fdaa3e6120df1a13ce32709b4c90441bd7d3574fba905c72346303` |
| projects/chirality-app-dev/frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts | `65252b9b8be980e4ec17c71a1ce54469a39309c8772b4c2c1c059c4d1b6a57c4` |
| projects/chirality-app-dev/frontend/scripts/validate-harness-section8.mjs | `260ac7c4978aa801e5644e52306772528642336434a5b9cd31dc0707e213429e` |

Confirmed that 0392eadea adds only the previously reviewed public-export test
path to APP-JOURNEYS-CORE-WORKFLOW-20260913.yaml; that declaration does not alter
substantive instructions.

No tests, builds, live actions, protected-state reads, or Git mutations were
performed by this reviewer. The author's 32 focused test passes, typechecks,
and syntax check remain author evidence; parent owns CI acceptance. This return
is the sole write and records independent review, not release approval.
