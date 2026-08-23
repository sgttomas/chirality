# Fresh evidence-only review — A2-PKG09-R17-REVIEW-01

## Verdict

`PASS`

The frozen executor candidate satisfies the sealed 12-item matrix. No repair,
delegation, proof act, R18 staging, build/package action, operator/default-job
query, private-root traversal, or Git action was performed by this review.
R17 remains executed-and-failed evidence; DEL-09-04 remains `IN_PROGRESS` and
unproved.

## Frozen identities

All eight frozen SHA-256 identities match the sealed brief:

| Surface | SHA-256 |
|---|---|
| proof harness | `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52` |
| focused harness test | `9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595` |
| runtime host | `39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7` |
| runtime-host socket test | `78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8` |
| R17 | `4e7ebda1e161e93629e5fb7e9f657447a48189882b2d342d6c287dfd914d28f7` |
| DEL status | `d308d4c38c33b087a5aa40b820d22661e15a811558bc388637fc39d0330491c7` |
| executor evidence | `0675197fed51a5508533ac9174ad82d3bbe225d3424f089b87d1008362cf90ef` |
| executor return | `248a49942101fd42b30228c85efb25f152731a6156b3a6b4aff808b333cc21af` |

The complete control-surface hashes and deterministic graph/event validation
are retained in `candidate-hashes.log`.

## Mandatory matrix

1. **Basis, containment, and governance — PASS.** Branch
   `codex/app-login-proof-r17-repair`, `HEAD`, `origin/main`, and merge-base all
   resolve to exact basis `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.
   The real index has zero staged paths. All tracked and untracked candidate
   paths are under `projects/chirality-app-dev/`. The transcription, plan,
   four-node/three-edge acyclic serialized graph, activation, manager preflight,
   executor/reviewer briefs, both amendments, and five runtime events parse and
   agree. Runtime events contain the one governed executor dispatch and no
   reviewer or nested Agent 2 delegation.

2. **Preserved public evidence and secret boundary — PASS.** The enclosing
   directory is mode `0700`, has exactly six entries, all six are regular
   non-symlink files at mode `0600`, and all six owner-supplied SHA-256 values
   match. Selected JSON fields only establish `PREPARED` with
   `proofClaimed: false`, then summary/evidence `FAIL` at source revision
   `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`. Count-only scans found 80
   `runtime.daemon.initialize_failed` and 80 matched
   `listen EINVAL .../runtime-data/runtime/control.sock` signatures in each of
   `daemon.stderr.log` and `desktop-daemon.log`, and zero in stdout. Bounded
   forbidden-filename, capture-state-schema, credential/token-name,
   private-key, and login-session-digest-salt file counts are all zero. No log
   body or private state was printed or copied. The private root's existence bit
   alone remains true; its contents were not enumerated, read, or otherwise
   inspected.

3. **R17 failed-proof semantics — PASS.** R17 lines 18–25 keep capture nonzero,
   `runs = 16`, and manual residual bootout owner-attributed. Lines 27–80 keep
   public JSON/log and current-host observations independent. It records the
   exact false-claim, session transition, `RunAtLoad`, exact ambiguity error,
   cleanup refusal/residuals, and 80/80 log evidence without crediting job
   discovery or proof. An independent current check found the exact proof plist
   absent and the exact proof service absent with exit 113 and the exact
   two-line not-found classification. The private root was not traversed. No
   statement upgrades R17 to accepted proof.

4. **Socket lengths and sole future proposal — PASS.** Independent UTF-8 byte
   counts are R16 full socket `119`, R13 hypothetical full socket `111`, and
   macOS lexical maximum `103` (`sun_path[104]` including NUL). The controlling
   proposal `/private/tmp/ch-r18-91499728-51dd` is absent and not a symlink,
   root length `33`, full socket length `67`, and margin `36`. It is the sole
   controlling value in R17/status/current run surfaces; the longer value occurs
   only as explicitly superseded Amendment 01 history. No R18 root, staging,
   procedure, prepare, capture, or proof artifact was created.

5. **Prepare guard — PASS.** The harness measures the exact lexical joined path
   with `Buffer.byteLength(..., 'utf8')` and rejects `>103` on macOS
   (`run-packaged-launchagent-login-proof.mjs:90-101`). In the production path,
   source-revision validation and the guard at lines 1198–1200 precede symlink
   inspection, `lstat`, root creation, home/LaunchAgents/app/plist inspection,
   commands, job actions, install, and mutation. Tests at lines 463–554 use
   real path strings and filesystem-facing state for 103 acceptance, 104 ASCII
   and Unicode rejection, R16 119, R13 111, zero commands, absent candidate
   home, and absent newly generated rejected roots. Accepted paths continue
   through the pre-existing symlink and containment validations.

6. **Cleanup fail-closure — PASS.** Target validation requires the exact
   non-default proof label/service, expected plist and runtime roots, and
   regular non-symlink targets (harness lines 502–529). The launchctl parser
   requires an exact service wrapper and unambiguous state/program/argv/PID/run/
   last-exit fields and rejects invalid/ambiguous PID values (lines 532–619).
   Plist bytes must parse to the exact label, `RunAtLoad`, and exact packaged
   runtime argv; launchctl program/argv must match the same packaged executable
   (lines 622–665). Pid-less cleanup requires a recognized non-running state,
   positive runs, and nonzero last exit before skipping `lsof`; a present PID
   requires exact `running` and strict executable inspection (lines 666–690).
   Bootout occurs only after those checks (lines 704–733). Focused tests cover
   exact `runs = 16` pid-less bootout/cleanup without `lsof`, both PID/state
   refusal directions, missing arguments/program, mismatched service/program/
   argv/plist label/RunAtLoad, ambiguous argv/plist/process identities, failed
   process inspection, and no bootout on every negative. Existing proof-label
   validation forbids `com.chirality.runtime`, so no new path can target the
   default operator job.

7. **Runtime-host guard — PASS.** The production entry point remains
   no-argument `startRuntimeHost()` and uses actual `process.platform`; there is
   no production caller-controlled platform argument. It constructs the
   unchanged `app.getPath('userData')/runtime/control.sock`, measures exact UTF-8
   bytes, and emits only measured/max counts (runtime-host lines 64–74 and
   502–505). Rejection precedes all runtime environment mutation, credential/
   daemon construction, and `listen` (line 505 before lines 506 onward). Tests
   cover exact 103/104 ASCII and Unicode behavior, non-macOS behavior, actual
   `process.platform` mocking/restoration, and zero `RuntimeDaemon`
   construction on rejection.

8. **R17/status posture — PASS.** R17 and status hashes match the freeze. R17
   declares `EXECUTED AND FAILED — NO PROOF ACCEPTED`, immutable failed evidence,
   and the exact failed source revision while distinguishing the current
   uncommitted/unbuilt repair candidate and accepted branch basis. `_STATUS.md`
   changes only the Remaining/history account needed for R17, preserves
   `IN_PROGRESS`, approval/lifecycle fields, and the unproved state, and makes
   no proof, lifecycle, signing, distribution, release, or reliance claim.

9. **Recommendations — PASS.** R17 lines 163–193 recommend, for a separately
   authorized later tranche only, a short per-user permission/ownership/mode/
   ancestor/symlink-safe socket location while recording collision, stale
   cleanup, client-discovery, environment, and migration tradeoffs. It also
   recommends a later KeepAlive guard/backoff/proof-specific posture and states
   the recovery-versus-restart/log-churn/service-instability tradeoff. The
   runtime socket location remains unchanged, `KeepAlive=always` remains the
   existing proof posture, and no plist/backoff/product policy is changed.

10. **Syntax and frontend checks — PASS.** `node --check` passed. The complete
    focused harness/runtime-host set passed `65/65`. `npm run typecheck` passed.
    The sandboxed full suite reproduced only the expected 21 local loopback/
    Unix-socket `EPERM` failures (`1,237 passed / 4 skipped` otherwise). The
    exact `npm test` rerun with permission limited to local test sockets passed
    `1,258 passed / 4 skipped` across `153 passed / 1 skipped` files. No
    external network/provider permission or use occurred.

11. **Governance and hygiene checks — PASS.** APP-HOLD integrity passed for all
    53 contracts. Practitioner self-check exited zero at the current calibrated
    baseline (`INFO=14`, `NOT_APPLICABLE=1`, `REVIEW=4`, `WARN=40`). Full
    practitioner pytest passed `350/350`. The App receipt validator passed and
    ledger SHA-256 remained
    `ba7757bcc34772cf27df47e58be573b276d206ec410587a77ecffe6252be62b2`.
    Candidate whitespace, per-new-file no-index whitespace, `git diff --check`,
    cached check, JSON/JSONL parsing, App-only containment, and empty real index
    all pass after review-log ANSI/trailing-blank normalization.

12. **Prohibited-act audit — PASS.** The frozen dirty-path set contains only the
    authorized App source/tests, R17/status, governed run package, executor
    returns, and this review. It contains no build/package/dist, R18 procedure,
    plist, launcher, operator, signing, deployment, distribution, or release
    artifact. Runtime telemetry and executor evidence record no prohibited act.
    This reviewer performed only source/evidence reads, the exact proof
    plist/service absence checks, the proposed-root absence/non-symlink check,
    local deterministic tests, local-socket-only test rerun, and writes under
    this review directory. It did not run prepare/capture/logout/login, GUI,
    bootstrap/kickstart, mutate launchd/plist/operator/launcher/private-root,
    use network/providers, build/package/rebuild, or stage/commit/push/PR/merge.

## Checks and evidence logs

| Evidence | Result |
|---|---|
| `evidence-checks.log` | exact basis/public modes/hashes/selected JSON/count-only logs/secret counts/current absence/path lengths PASS |
| `candidate-hashes.log` | all frozen and control hashes; graph/events PASS |
| `focused-tests-65.log` | 65/65 PASS |
| `typecheck.log` | PASS |
| `full-frontend-sandbox.log` | expected local-bind diagnostic only: 21 EPERM |
| `full-frontend-local-sockets.log` | 1,258 passed / 4 skipped |
| `app-hold.log` | 53-contract integrity PASS |
| `practitioner-self-check.log` | exit 0 at calibrated baseline |
| `practitioner-pytest.log` | 350/350 PASS |
| `receipt-validator.log` | PASS; ledger hash unchanged |
| `final-hygiene.log` | first-pass audit retained; generated-log whitespace normalized and final pass recorded below |

## Blockers and rerun triggers

- Blockers: none.
- Any change to a frozen source/test/R17/status/executor identity requires
  affected checks, hashes, whitespace, and a new fresh review.
- Any change to the public-evidence hashes/modes/counts, exact proof plist or
  service state, proposed-root state, branch/HEAD/origin-main basis, or index/
  containment state requires the corresponding matrix checks to rerun.
- Any later R18, build/package, Git integration, or owner proof act requires
  separate authorization and is not covered by this PASS.
