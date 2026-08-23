# R20 proof-repair chain — Task Management row maintenance and closure echo

Date: `2026-08-23`

Invoking loop: App (`projects/chirality-app-dev`)

Mode: mandatory federation preflight, owner-directed row maintenance,
staleness check, and closure echo. This is a register-service record only. It
does not accept proof, create a release claim, or amend any deliverable,
procedure, runtime, package, or product policy.

## Owner authority

The invoking owner direction is transcribed at
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_CLOSEOUT_2026-08-23/CHAT_TRANSCRIPTION.md`
(SHA-256
`9d9237f6671e24c8eb3f72a5cf71b21221aa4aeb09b16f5efae60f581200dba9`).
Its exact Task Management grant is:

> Close or update the relevant Task Management rows for the proof-failure
> repair chain per your register conventions (candidates already recorded:
> parser fixtures, umask/uid portability, KeepAlive crash-loop hazard routing
> to G-HELPER).

The same direction records an owner-reported R20 `PASS`, expressly forbids an
acceptance or release claim, and leaves the separately gated DEL-09-04 lanes
in progress. This Task Management act relies on the quoted direction only for
row/candidate maintenance; the proof bytes and deliverable status remain owned
by DEL-09-04 and its ordinary closeout.

## Mandatory federation preflight

The deterministic command

```text
python3 tools/taskmgmt/taskmgmt.py federation --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv
```

returned `COMPLETE` before row maintenance:

- four canonical tracked live registers and their four tracked archives were
  discovered, read, and validated (`PEC`, `ROOT`, `APP`, `PIP`);
- status totals were PEC `OPEN=16, DEFERRED=1, CLOSED=1`, Root
  `OPEN=11, DEFERRED=8`, App `OPEN=9, DEFERRED=3, CLOSED=1`, and Piping
  `OPEN=11, DEFERRED=23`;
- all live and archive validations passed; there were zero invalid or
  unreadable registers and zero unresolved ambiguities;
- the helper reported 55 typed-field findings, of which 30 were presented for
  the non-Root App invocation: one `FOREIGN_LINK_TO_LOCAL`, 26
  `LOCAL_LINK_TO_FOREIGN`, one `REMOTE_CLOSED_LOCAL_OPEN`, 23
  `LOCAL_CLOSED_REMOTE_OPEN`, and four `MISSING_NOTICE` observations. None is
  a relationship for the three proof-repair candidates reviewed below;
- excluded by design were untracked lookalikes, tracked paths outside the
  sanctioned coordination shapes, archives/exports/fixtures/evaluation copies
  as live inputs, generated projections, `Notes` prose, and all inferred
  promotion, priority, elevation, closure, or disposition effects; and
- the helper proved zero register writes. The generated
  `.candidates/federation.json` is gitignored, derivative, and non-authoritative.

Coverage is therefore `COMPLETE`; there are no invalid inputs or operational
errors limiting this local maintenance act.

## Candidate and row findings

### 1. Target-OS host-output parser fixtures

The existing candidate
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/TM_CANDIDATE_TARGET_OS_HOST_OUTPUT_FIXTURES.md`
(SHA-256
`45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`)
states `HARVESTED ONLY` and expressly creates no register row or disposition.
The R19 cleanup-parser defect was repaired and the owner now reports that R20
executed with `PASS`, which is closure echo for that concrete failure chain.
It does not decide the candidate's broader proposed project-wide staging gate
for every `launchctl`, `stat`, and `ps` parser.

Disposition: **candidate retained, harvest-only; no row created or closed**.

### 2. Permission-guard fixture modes and host identity

The existing candidate
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/TM_CANDIDATE_PERMISSION_GUARD_FIXTURE_MODES.md`
(SHA-256
`3f5a2ef33053f66031150b41b0f3c9b39b1157a9076442b6a22e8983f3d80734`)
expressly creates no Task Management row. It records the completed test-only
mode and UID portability repairs and preserves the broader prospective
question: whether permission-guard suites must pin modes, sweep
UID/GID/path/home assumptions, and use Linux CI as the host-identity arbiter
before future proof staging.

Disposition: **candidate retained, harvest-only; no row created or closed**.
The concrete PR #632 portability repairs are complete, but that implementation
fact is not a human disposition of the broader candidate.

### 3. `KeepAlive=always` crash-loop hazard

The R17 manager return
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/MANAGER_RETURN.md`
(SHA-256
`9e5dc1ebb941eef431a71d920dcb8f6f596b692ec30373a348048b3eb2548a49`)
recommends a separately authorized review of a bounded guard, backoff, or
proof-specific restart posture. Its executor evidence summary at
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22/instances/WI-PKG09-R17-FAILURE-REPAIR-01/executor/EVIDENCE_SUMMARY.md`
(SHA-256
`0675197fed51a5508533ac9174ad82d3bbe225d3424f089b87d1008362cf90ef`).
It characterizes restart/log churn and unstable service as a recommendation
only; no plist or product policy changed.

The current owner direction names `G-HELPER` as the route for this surviving
hazard. That routing note is retained without inferring that G-HELPER has
ruled, accepted, prioritized, or scheduled it. No existing App row carries
this exact hazard, and the direction does not authorize minting a row.

Disposition: **candidate retained for later G-HELPER owner triage; no row
created or closed**.

The existing `TM-APP-030` row is not reused as this carrier. Its concern is the
distinct daemon/helper bundle-identity decision. The G0 record
`plans/steers/chirality_app_v3_g0_record_2026-08-22.md` (SHA-256
`86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`)
does direct that distinct row to resolve at G-HELPER, but neither that text nor
this closeout authorizes conflating bundle identity with the crash-loop
hazard. `TM-APP-030` therefore remains byte-identical and `OPEN`.

## Exact register delta

No live or archived row is changed. No candidate was previously promoted, and
the owner direction does not authorize promotion. Inventing a row merely to
close it would violate K-TM-3 and K-TM-5.

- `REGISTER.csv` before and after: SHA-256
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`;
  13 rows (`OPEN=9`, `DEFERRED=3`, `CLOSED=1`).
- `REGISTER_CLOSED.csv` before and after: SHA-256
  `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6`;
  31 archived rows.

## Staleness and closure echo

- The exact source file underlying `TM-APP-030` remains SHA-256
  `dcfd8289ec78e31c933993e460deaca00ad3a69e536a3646479ed7c334da7ed8`,
  matching its `SourceSha`; no staleness change was found for the only nearby
  live row examined.
- The two committed R20 candidates and R17 hazard evidence exist at the exact
  hashes cited above. No stale or missing evidence was found in this scoped
  review.
- Closure echo: the concrete R17/R19/R20 proof-failure repair chain is reported
  complete by the owner-executed R20 PASS, while all three broader candidates
  remain outside the register and undecided. This is not proof acceptance and
  not a claim that their policy concerns are resolved.
- Escalation/routing residue: only the retained `KeepAlive=always` candidate is
  named for later G-HELPER owner triage. No notice, handoff, foreign-register
  write, priority, schedule, or automatic receiving row is created here.

## Receipt breadcrumb

For the tranche's single ordinary Receipt 194, record: TASK_MANAGEMENT ran
mandatory and closeout federation with `COMPLETE` coverage; reviewed three
proof-repair candidates; changed zero live rows and zero archive rows; retained
the parser-fixture and mode/UID/path portability candidates as harvest-only;
retained the `KeepAlive=always` hazard for later G-HELPER owner triage without
claiming a ruling; validated the App register; and wrote this report plus the
unique run return. The breadcrumb creates no duty, priority, acceptance, or
release effect.
