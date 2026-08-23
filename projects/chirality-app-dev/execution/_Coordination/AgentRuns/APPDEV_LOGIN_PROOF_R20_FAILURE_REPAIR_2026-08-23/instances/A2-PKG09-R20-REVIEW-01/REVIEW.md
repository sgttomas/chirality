# REVIEW — A2-PKG09-R20-REVIEW-01

Verdict: `BLOCKED`

Role: genuinely fresh delegated-harness-native ephemeral-generalist Agent 2;
role not mechanically enforced. Role entry, freshness, and K-SUBAGENT
non-delegation evidence are `instruction-asserted`; no descendants were
created.

## Frozen candidate reviewed

The review consumed the owner direction, activation/plan/amendment,
implementer disposition, sealed review and implementation briefs,
implementer root cause/checks/return, root and App `AGENTS.md`, the ratified
software workflow profile, 100% of the tracked source/test diff, the complete
fixture, and relevant surrounding source including the runtime's actual
operator-token creation path.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs` | 51,763 | `604f2e189b167c9691eae33b28fc2b3a70352b6222abb1924f36252dd1493b45` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | 49,577 | `2d791913022671beb1c4f9e59cd104cba7f96521f784476a0798c9682511eab0` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt` | 3,049 | `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` |

- Tracked two-file diff: 416 insertions, 21 deletions; SHA-256
  `82279894cfd7ace2ca5fd4283464314857504d09942d07e37926f5050525db29`.
- Accepted implementer `RETURN.md` SHA-256:
  `42792a87dfb8660e06aad4d74745ce62f03ece7efd72af6482bd02adeca9550e`.
- Authorized source fixture and repository fixture are both regular,
  non-symlink 3,049-byte files, have the required identical SHA-256, and
  compare byte-for-byte equal.
- Independent fixture parse: `state=running`, `pid=34924`, `runs=1`,
  `lastExitCode=undefined`, `neverExited=true`; program suffix and exact
  two-element daemon argument vector match.
- Actual operator-token source is the runtime `AuthRegistry` client named
  `operator`, whose token file resolves beneath the proof user-data runtime
  at `runtime/auth/tokens/operator.token`. No token value was read or recorded.

## Actionable findings

### F-01 — HIGH — PASS-only copy deletion can create a false FAIL after runtime deletion

Evidence: script lines 1316-1327 delete `failed-logs` while the summary still
has its initial `FAIL` status. A deletion error is appended to
`cleanup.errors`; lines 1328-1348 then keep the final status `FAIL`. By that
point lines 895-912 have already removed runtime data. The delete may also
have partially removed the two copies before throwing. The resulting non-PASS
can therefore have neither its private runtime logs nor two intact preserved
copies. This directly contradicts the amendment that copied logs are removed
only if final status becomes `PASS` and that every non-PASS retains them.

Repair: remove the circular outcome transition. Determine and commit final
proof status before any PASS-only deletion, and ensure a deletion problem
cannot retroactively convert that status to FAIL after runtime removal. A
staging/atomic-publication design is preferable: capture both logs before
runtime removal, publish both only for a final FAIL, and discard staging only
after PASS is irrevocable. Add a deterministic deletion-failure test that
proves no false FAIL or partial non-PASS evidence loss is possible.

### F-02 — HIGH — nested symlinks and read races can bypass token/log containment

Evidence: `assertCleanupTargets` checks only the top-level `runtimeRoot`
(lines 516-522). `preserveFailureLogs` then `lstat`s only the terminal log and
token paths (lines 709-756) and later reopens them by pathname. It never
validates that `runtime/logs` and `runtime/auth/tokens` are real directories
contained beneath the owned runtime root, and it does not bind the `lstat`
identity to the bytes read. A symlinked ancestor or a replacement between
check and read can therefore select a different token, make the scan miss the
actual operator token, or copy unrelated private files into `failed-logs`.
There are no focused tests for nested log/token symlinks.

Repair: revalidate the runtime root immediately before preservation; require
canonical, non-symlink directory ancestors contained beneath it; open each
token/log file without following the final symlink and bind validation and
read to the same file descriptor (`fstat` plus appropriate ownership/mode
checks). On any containment or identity ambiguity, copy neither and retain the
runtime root. Add tests for symlinked `logs`, `auth`, and `tokens` ancestors
and final-file substitution/refusal.

### F-03 — HIGH — two missing logs are treated as safe and runtime data is removed

Evidence: when both fixed log files are absent, lines 717-719 return
`copied=false`, `privateOnly=false`, with no error. Lines 895-909 may then
unlink the plist and remove all runtime data. If proof observation or a later
check is non-PASS, the final evidence has no `failed-logs` and no private
runtime root. One missing log correctly fails closed, but two missing logs do
not. The focused fixture always creates both logs, so this route is untested.

Repair: distinguish install-attempt cleanup (where a daemon may never have
created logs) from capture. During capture, absence of either or both required
logs must be an explicit preservation failure that prevents runtime removal.
Add separate zero-log and one-log capture tests, including proof-observation
failure and a later default-protection failure.

### F-04 — MEDIUM — a present but empty last-exit field is accepted

Evidence: line 565 recognizes only `last exit code = (.+)`. A present empty or
whitespace-only field is therefore silently treated as an absent optional
field; `parseCleanupLaunchctlJob` returns `lastExitCode=undefined` and
`neverExited=false` instead of throwing. An independent parser probe confirmed
both empty variants are accepted, while `+1`, `NaN`, case-changed sentinel,
and sentinel-with-suffix variants throw. This violates “every other
noninteger last-exit form throws.” The malformed-form test omits empty values.

Repair: recognize field presence independently of value, then reject an empty
or whitespace-only value before the exact sentinel/integer branch. Add both
empty variants to the malformed table.

### F-05 — MEDIUM — job-still-loaded preservation lacks an independent test

Evidence: the new bootout-failure test leaves both the job loaded and process
alive after a nonzero bootout, while the process-alive test covers an absent
job. No test sets the existing `bootoutRemovesJob` control false with a
successful bootout and a stopped process. Thus the distinct owner-required
“job remains loaded” gate and its ordering are not isolated, even though the
source's final state check appears to refuse destructive cleanup.

Repair: add the successful-bootout/job-still-loaded/process-absent case and
assert refusal reporting, no plist unlink, no runtime removal, and intact
failed-log copies.

## Checks independently run

| Check | Result |
|---|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS, exit 0 |
| exact focused Vitest file | PASS, 1 file / 64 tests, exit 0, duration 2.12 s |
| `npm run typecheck` | PASS, exit 0 |
| source/target fixture regularity, size, SHA-256, and `cmp` | PASS |
| independent exact fixture parse and argument identity | PASS |
| `git diff --check` | PASS |
| App-only change containment | PASS; 19 current paths, no violations |
| `WORK_GRAPH.json` and `RUNTIME_EVENTS.jsonl` parsing | PASS |
| Git index | PASS; 0 staged paths |

Only App paths are dirty. The candidate inventory is exactly the two tracked
frontend files, the one untracked fixture, and this run-root coordination
package. No full suite, build, package, network, Git integration, proof/GUI,
launchd/default-operator action, prohibited private-root traversal, Desktop
evidence access, source repair, or token read was performed.

## Gate result

Phase-A source review is `BLOCKED`. Do not release CHANGE or Phase B. Return
F-01 through F-05 to a bounded repair cycle and require a genuinely fresh
reviewer over newly frozen hashes.
