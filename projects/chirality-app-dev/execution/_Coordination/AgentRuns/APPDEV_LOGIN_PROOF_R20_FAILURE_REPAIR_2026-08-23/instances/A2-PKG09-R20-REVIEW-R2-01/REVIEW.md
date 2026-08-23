# REVIEW — A2-PKG09-R20-REVIEW-R2-01

Verdict: `PASS`

No actionable finding remains in the frozen final Phase-A candidate. F-01
through F-05 are closed. Phase-A source review may fan in; Phase B and CHANGE
remain subject to their owning manager gates.

Role: genuinely fresh delegated-harness-native ephemeral-generalist Agent 2;
role not mechanically enforced. Role entry, freshness, and K-SUBAGENT
non-delegation evidence are `instruction-asserted`; no descendants were
created.

## Review basis and frozen inventory

I read the current root and App `AGENTS.md`, the ratified software workflow
profile, CHAT transcription, activation, plans v1-v3, graphs v1-v3, amendment,
immutable review 01, cycle-1 and cycle-2 repair evidence, the final sealed
review brief, and the review activation boundary. I independently inspected
100% of the tracked source/test diff, the complete repository fixture, and the
relevant runtime auth and LaunchAgent source.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs` | 56,144 | `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | 58,580 | `6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt` | 3,049 | `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` |
| immutable `instances/A2-PKG09-R20-REVIEW-01/REVIEW.md` | — | `0134c2db5a9255236171880b95f66a5d93292cd41f71be458dc853dc5636ef76` |
| frozen cycle-2 `RETURN.md` | — | `490a3134301b7970d1bab9e043c6fbbe218df43c1e9a84d24a244d4bb7b974f1` |

- Basis: branch `codex/app-login-proof-r20-repair`, HEAD
  `a702dd6ec5005b361c8c023b12b599a425e5e2b8`, frontend tree
  `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`.
- Tracked two-file diff: 754 insertions and 28 deletions. Script:
  `+311/-19`; test: `+443/-9`. Binary-diff SHA-256:
  `65ff7075146a0a3c11f16de2431e2d9d829979c11184b9bc7d2cc3b6086d752b`.
- Both authorized source and repository fixtures are regular, non-symlink,
  3,049-byte files with the required identical SHA-256 and compare
  byte-for-byte equal.
- APP-HOLD-1 reliance preflight returned `ALLOW`; register SHA-256
  `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`,
  scan fingerprint
  `c63c1e550908573512913d35b8e9e455cbc12c1e31d4d19c0014830eb4af3fe9`.

## Independent root-cause and closure review

The real fixture parses as `state=running`, `pid=34924`, `runs=1`,
`lastExitCode=undefined`, and `neverExited=true`. Its program resolves to the
packaged Chirality executable and its argument vector is exactly that
executable plus `--runtime-daemon`. The pre-repair parser's integer-only
last-exit handling therefore explains the R19 cleanup refusal; the bounded
sentinel repair addresses the observed source shape rather than relying on
the prompt assertion.

| Finding | Independent disposition |
|---|---|
| F-01 | `CLOSED`. Final PASS is computed and assigned before PASS-only failed-log removal. Removal failure cannot add a cleanup error or retroactively create FAIL. Every non-PASS path bypasses PASS-only removal, so its two successfully published copies remain intact; publication failure instead best-effort removes the partial destination and retains the private runtime root. |
| F-02 | `CLOSED`. The four remaining security helpers have distinct bounded roles: metadata/permission validation, dev/inode comparison, exact five-ancestor canonical containment and non-symlink validation, and held-descriptor snapshot reads. All three final paths use `O_RDONLY | O_NOFOLLOW`; descriptor `fstat` is bound to path `lstat`, all ancestors and final identities are revalidated after all opens, and only held descriptors are read. Post-read dev/inode/size/mtime/ctime stability is checked. Any missing, symlinked, raced, non-owned, writable-by-group/other, non-regular, or identity-ambiguous source copies neither and makes preservation private-only, which prohibits runtime removal. A direct macOS probe confirmed a final symlink open with `O_NOFOLLOW` returns `ELOOP`. No `/dev/fd` traversal remains. |
| F-03 | `CLOSED`. Prepare/install-attempt cleanup admits the justified both-logs-absent state before daemon materialization. Capture sets `requireFailureLogs=true`; zero or one missing required log is an explicit private-only preservation error and prevents runtime removal. Focused zero-log observation-failure and one-log later-default-protection cases exercise the distinction. |
| F-04 | `CLOSED`. Field presence is parsed independently of its value. Empty, whitespace-only, case-changed, suffixed, `NaN`, signed-plus, fractional, hexadecimal, and other noninteger forms reject; signed integers remain valid. Exact `(never exited)` alone maps to `lastExitCode=undefined` and `neverExited=true`. |
| F-05 | `CLOSED`. The successful-bootout/job-still-loaded/process-absent case independently asserts job-present refusal, reporting, no plist unlink, no runtime removal, and both intact copies. Separate cases cover mutation refusal and process-alive refusal. |

## Non-PASS, auth, protection, and security semantics

- Proof-observation failure publishes both token-free logs before allowed
  runtime removal and retains them because final status is FAIL.
- Unsafe cleanup state (`jobMutationRefused`, job present/unknown, or any
  observed proof PID alive) refuses both plist unlink and runtime removal.
- A later `defaultProtection` failure occurs only after preservation; it
  leaves the copies in place even when the now-safe private runtime root was
  removed. Default-protection inspection remains read-only and the proof
  mutation target remains the unique proof label, never
  `com.chirality.runtime`.
- Token/auth, source-path, identity, ownership, mode, missing-file,
  pre-existing-destination, and copy-write failures fail closed: copy neither,
  report private-only preservation, and retain runtime data.
- Runtime source confirms `AuthRegistry.ensureClient("operator", ...)` creates
  the real operator token at
  `<proof-user-data>/runtime/auth/tokens/operator.token` with mode `0600`.
  The candidate snapshots that exact fixed path with the two fixed daemon-log
  paths, scans both byte buffers for the trimmed base64url token, never copies
  or serializes the token, and writes copies only after both scans are clear.
  No actual operator token or private runtime byte was read during review or
  placed in repository evidence.
- The harness exposes no logout/login or default-operator mutation API. The
  review executed no proof, GUI, launchd/plist, default-operator, or private
  proof-root action.

## Complexity and test-quality disposition

The remaining `+311/-19` script surface is justified and bounded: exact
sentinel parsing; observed-PID/destructive-cleanup state; failure-log capture
and token gating; four small F-02 snapshot helpers; and final-status-aware
copy disposition. The final cycle removed the nonportable directory-FD helper
and reduced the script by ten inserted lines from cycle 1. No new module,
unrelated refactor, package, daemon, guard, or default-surface change exists.

The `+443/-9` test surface is likewise proportional to the required negative
matrix: verbatim fixture and malformed parser cases, PASS deletion failure,
zero/one missing logs, token copy-neither, three ancestor symlinks, final-file
substitution, later default failure, mutation refusal, process-alive refusal,
and independent job-still-loaded refusal. Tests use isolated temporary roots,
mock only command/process boundaries, exercise real filesystem symlinks and
held-file behavior on macOS, and remain contained. No reducible or unrelated
test block is actionable.

## Checks independently executed

| Check | Result |
|---|---|
| APP-HOLD-1 reliance preflight | PASS / `ALLOW` |
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS, exit 0, no output |
| exact focused Vitest file | PASS, exit 0; 1 file / 72 tests; duration 3.25 s |
| `npm run typecheck` | PASS, exit 0; frontend and Electron TypeScript configurations |
| fixture regularity, non-symlink status, size, SHA-256, and `cmp` | PASS |
| independent fixture parse, program, argument, sentinel, integer, and malformed probes | PASS |
| macOS `O_NOFOLLOW` final-symlink probe | PASS; `ELOOP` |
| source/test/fixture hashes and diff inventory | PASS; frozen identities unchanged |
| `git diff --check` | PASS, no output |
| App-only change containment | PASS, zero violations |
| work-graph JSON v1-v3 and runtime-events JSONL parsing | PASS; 3 graphs / 10 events |
| Git index | PASS; empty |

Only App paths are dirty. The reviewed frontend candidate inventory is exactly
the two tracked files plus the one untracked fixture; the remaining dirty
paths are this App-contained run package. No full suite, build, package,
network, Git integration, proof procedure, GUI, launchd/plist mutation,
default-operator query, prohibited private-root traversal, Desktop evidence
read, or source repair occurred.

## Gate result

Final Phase-A fresh review is `PASS` with no actionable finding. Release the
Phase-A fan-in to the owning WORKING_ITEMS manager. This review does not itself
authorize CHANGE, Phase B, build/package, proof execution, or publication.
