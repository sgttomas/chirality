# Independent review brief — restart-admission repair

Type 2 independent reviewer, Claude Fable 5.1, medium reasoning, no delegation.
Read-only source review on the integration checkout
`/Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335`.
Read AGENTS.md, then RUN_LOG.md section "Successor takeover: restart-admission
repair completed", this directory's BRIEF.md, HANDOFF.md (including "Successor
completion") and FINAL_SOURCE_HASHES.json.

Subject: the two most recent commits on HEAD (repair plus one test-only
correction). Review `git diff bad09b9d2..HEAD -- projects/chirality-runtime`
together with the complete final files:
- packages/daemon/src/codex-admitted-launcher.ts (factory refreshHostAdmission)
- packages/daemon/src/codex-supervisor.ts (refreshHostAdmission,
  refreshHostAdmissionIdle, acquire prologue, close)
- packages/daemon/src/hosted-private-composition.ts (publicAdmission.live)
- packages/daemon/src/runtime-conformance-v2-admission.ts (issuers, unchanged)
- packages/daemon/src/host-account-authority.ts (lease semantics, unchanged)
- packages/daemon/src/hosted-bootstrap.ts status() (consumer of live())
- tests/runtime-conformance-v2-admission.test.ts (new renewal tests)

Questions to answer with evidence (file:line):
1. Can any superseded admission, preparation or queued candidate become valid
   or be used after a host replacement? Can renewal accept a different
   account, epoch, project, policy, consent, release or daemon generation?
2. Races: acquire awaits renewal before registering in `acquiring`; close()
   during renewal; two acquires plus a status poll during renewal; renewal
   while a worker entry is being retired. Identify any path that publishes a
   worker or launches a candidate on a stale preparation.
3. Fail-closed posture: does any renewal failure get swallowed on a path that
   then proceeds to launch? (live() intentionally swallows renewal failures and
   returns the durable-binding result; confirm that no launch depends on it.)
4. Does the change relax authentication, code-signature, seal, payload or
   supplier policy anywhere? Expected answer: no; show why.
5. Are the tests real (real issuers/factory/supervisor, synthetic lease
   carrier only) and do they cover the stated negatives? Name gaps.

Run only: `npx tsc -b --pretty false` and
`npx vitest run tests/runtime-conformance-v2-admission.test.ts tests/codex-admitted-launcher.test.ts tests/codex-supervisor.test.ts tests/hosted-private-composition.test.ts tests/hosted-bootstrap-integration.test.ts tests/custody-config-status.test.ts`
from `projects/chirality-runtime`. No other suites, no build, sign, launch,
GUI, network, supplier, keychain or trial App/userdata access. Never read
anything under `/Users/ryan/Library/Application Support/Chirality Trial*` or
`/private/tmp/chirality-*`. Do not edit product or test files; do not commit.

Return: write `INDEPENDENT_REVIEW.md` in this directory with verdict PASS or
FAIL, each finding with severity, file:line and a concrete failure scenario,
and the exact commands run with their pass/fail counts. Then reply with a
short summary of the verdict and any blocking findings.
