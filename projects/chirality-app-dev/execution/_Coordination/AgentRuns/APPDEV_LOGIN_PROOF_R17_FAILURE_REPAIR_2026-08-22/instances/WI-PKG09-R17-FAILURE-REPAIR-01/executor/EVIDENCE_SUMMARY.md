# A2-PKG09-R17-EXECUTE-01 evidence summary

## Boundary

- Accepted basis / current HEAD:
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`.
- Work remained under `projects/chirality-app-dev/`.
- No build, package, network/provider, R18 execution/mutation, proof, GUI,
  LaunchAgent/operator, launcher, signing, deployment, Git integration, or
  private-root action ran. Only the amendment-authorized read-only
  absence/non-symlink check targeted the proposed R18 path.
- The owner-preserved private proof root was not traversed or inspected.

## Public failed-evidence verification

- Directory mode: `0700`; exactly six regular files.
- File modes: six of six `0600`.
- Exact file SHA-256 values match the six values frozen in the brief and R17.
- Selected JSON fields confirm non-claiming `PREPARED`, same-revision
  summary/evidence `FAIL`, login-session transition, `RunAtLoad`, error
  `Loaded job has ambiguous process identity`, and the recorded cleanup
  refusal/residuals.
- Count-only log scans: `daemon.stderr.log` and `desktop-daemon.log` each have
  80 `runtime.daemon.initialize_failed` matches and 80 matched
  `listen EINVAL .../runtime-data/runtime/control.sock` signatures;
  `daemon.stdout.log` has zero of each.
- Bounded filename/content scan counts: forbidden private filenames `0`,
  capture-state schema `0`, credential/token-name category `0`, private-key
  category `0`, and login-session digest-salt category `0`.
- No log body or private state was printed or copied into the repository.
- Independently computed socket path sizes: R16 `119`, R13 `111`, and the
  proposed future R18 socket `67` UTF-8 bytes. The exact future root
  `/private/tmp/ch-r18-91499728-51dd` is 33 bytes, was confirmed absent and not
  a symlink by a bounded read-only check, and leaves a 36-byte socket-path
  margin. It was not created, staged as R18, or queried internally.

## Check results

| Command/check | Result |
|---|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS |
| focused login-proof + socket/runtime-host suites | PASS — 65/65 |
| `npm run typecheck` | PASS |
| first sandboxed `npm test` | diagnostic only — 21 local loopback/Unix socket `EPERM` failures |
| exact `npm test` rerun with local socket permission | PASS — 1,258 passed / 4 skipped |
| APP-HOLD integrity scan | PASS |
| practitioner-harness `self-check` | PASS at existing calibrated baseline |
| `python3 -m pytest -q tools/practitioner_harness` | PASS — 350/350 |
| App loop receipt validator | PASS; receipt ledger unchanged |
| candidate whitespace including untracked files | PASS |
| `git diff --check` / `git diff --cached --check` | PASS / PASS |
| App-only containment / index | PASS / empty |

The sandboxed full-suite result is not a product failure. Its exact rerun with
the required local test-socket capability passed without network or provider
use.

## Recommendation conclusions

1. Recommend a later separately authorized short, permission-contained,
   symlink-safe per-user socket location after a threat model and migration
   tests; no relocation is implemented.
2. Recommend a later separately authorized crash-loop guard, backoff, or
   proof-specific KeepAlive posture; no plist or product policy is changed.
