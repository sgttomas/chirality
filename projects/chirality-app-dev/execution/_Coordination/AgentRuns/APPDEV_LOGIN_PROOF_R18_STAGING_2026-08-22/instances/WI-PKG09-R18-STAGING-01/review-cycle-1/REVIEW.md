# A2-PKG09-R18-REVIEW-CYCLE-1 fresh evidence review

Verdict: `VALIDATED_PASS`

The repaired R18 Tranche A candidate has no unresolved actionable finding.
The exact five-file whitespace repair is byte-for-byte reproducible from its
deterministic preimages, the owner-directed full-suite cure is accepted from
retained evidence without rerun, and the complete frontend candidate is
unchanged across the diagnostic and cure. The sandbox diagnostic remains
**not PASS** and is correctly classified
`ENVIRONMENT_SANDBOX_SOCKET_DENIAL`.

This reviewer did not run `npm test`, any focused test, typecheck, package or
build command, instruction-root generation, network command/tool, or proof
action. No reviewed byte was modified. `review-1/REVIEW.md` remains the
immutable historical pre-repair verdict.

## Basis and review input

- Branch/HEAD: `codex/app-login-proof-r18-staging` /
  `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`.
- Exact parents:
  `166efa82748133e90674be62304b81f8a0a8c1b4` and
  `b143444bd497eae1b1b638670a33e6df756d9084`.
- Index at review start and close: empty.
- Pre-review run-root inventory: 79 files, which is the cure executor's 78-file
  terminal inventory plus the later frozen fresh-review brief.
- Pre-review full porcelain inventory: 86 file entries, comprising two
  tracked modifications and 84 untracked files; all are under
  `projects/chirality-app-dev/`. The sole reviewer output makes the terminal
  counts 80 run-root files and 87 App-contained porcelain entries.
- Historical review SHA-256:
  `3dd9e7377c8ceb5c8237aee6837431d872b86335605b2c87cfc800a3d46e21bc`.

## Required matrix

| # | Review gate | Result |
|---:|---|---|
| 1 | five-file deterministic preimage, normalization, and substantive-equivalence proof | PASS, 5/5 |
| 2 | candidate/new-file whitespace, tracked diff, JSON, inventory, containment, and empty index | PASS |
| 3 | frozen implementation/package hashes and evidence-only supply-freeze boundary | PASS |
| 4 | retained sandbox diagnostic classification and counts | PASS as `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`; diagnostic remains not PASS |
| 5 | retained exact one-command cure evidence, cwd, permission boundary, exit, and counts | PASS |
| 6 | complete pre/post frontend candidate equality and no intervening source/test/package change | PASS |
| 7 | retained unrestricted evidence accepted without reviewer rerun | PASS |
| 8 | R18 and DEL-09-04 status accuracy, including future PR confirmation | PASS |
| 9 | TM candidate remains harvest-only | PASS |
| 10 | R19/proof/lifecycle/release/Git-action fences | PASS |
| 11 | retained proportional gates and current deterministic hygiene | PASS |

## Whitespace repair lineage

`PREIMAGE_SHASUMS256.txt` validates all five compressed preimages. Each gzip
header has flags 0 and mtime 0, confirming the `gzip -n` deterministic form.
Decompression reproduces every frozen preimage hash. Independently applying
only carriage-return deletion, trailing horizontal-whitespace deletion, and
surplus terminal-LF deletion followed by exactly one final LF reproduces each
current target byte-for-byte:

| Target relative to run root | Pre SHA-256 / bytes | Post SHA-256 / bytes | Exact deletion | Equality |
|---|---|---|---|---|
| `instances/WI-PKG09-R18-STAGING-01/executor-3/REQUEST_STATE.md` | `3902379feebe7c13ec67bbe642e42e0e6a9bb37939b82a854f1076a021d235aa` / 743 | `c54c2465a2d9dfa765d756a97a0b8c35306441eceae011bdc46e7f736aace778` / 742 | one surplus EOF LF | PASS |
| `instances/WI-PKG09-R18-STAGING-01/executor-3/shasums256.response-headers.sanitized.txt` | `8fcdc127011282e75e8d0a3bbd118ab733f723c3f6a4c04cad5e4f017375668f` / 5,234 | `f0754892c2fa8df1a9c59f14679f3abe1ea7e068999bcc230fc136a2ade6c6a1` / 5,188 | 43 CR, two trailing horizontal bytes, one surplus EOF LF | PASS |
| `instances/WI-PKG09-R18-STAGING-01/review-1/focused-tests.log` | `580ad49f26036c10c70fb6b13fea8e4e8fb0d7244112d0c70885834cdc55338b` / 261 | `d7d1868010e9b1785f594bed19b7f6e93be7f446c6c7198cfece92c74aa9edb6` / 260 | one surplus EOF LF | PASS |
| `instances/WI-PKG09-R18-STAGING-01/review-1/full-vitest.log` | `7e0907732af579802a927d09028b301cc167b1ec83fc490e7d1fc61bd1220dab` / 9,888 | `8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19` / 9,887 | one surplus EOF LF | PASS |
| `instances/WI-PKG09-R18-STAGING-01/review-1/typecheck.log` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` / 136 | `b1a67869986e76e171a01d5f562874d6b55653c9b53cea7c552d8949510a8483` / 135 | one surplus EOF LF | PASS |

No line order, textual token, or interior blank line changed. All five targets
end with exactly one LF. Repair evidence hashes are:

- `LINEAGE.md`:
  `645eade5cef7d23448b32a5b97ae390ccc5f87a9c51f483fe1b01ae150371977`;
- `CHECKS.md`:
  `5310607ddc78d6a6a716394de1b6522af06b337ab4ff2d82e1b45ec4fcf47b92`;
- `RETURN.md`:
  `40a87326c7bb2ce5451d027e00579850b88113eacece14fa3a746d80d9d4bb28`;
- `PREIMAGE_SHASUMS256.txt`:
  `8e934e1601cf16440f833ea61d511645ed9a49d3d885e333abe4d7a569d8f954`.

## Candidate equality and implementation boundary

The five frontend candidate hashes exactly match both cure freezes and the
frozen implementation:

| Path | SHA-256 |
|---|---|
| `frontend/scripts/verify-electron-dist.mjs` | `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457` |
| `frontend/scripts/pack-electron-with-supply.mjs` | `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db` |
| `frontend/src/__tests__/scripts/verify-electron-dist.test.ts` | `c9c4af600a703afa995f8316ee04eb3160d72ef7f8cba8ec2ce53c7f952cb38d` |
| `frontend/src/__tests__/scripts/pack-electron-with-supply.test.ts` | `a66af130420412e5a3d9cf48856c1b416234fea5aa78e14e3867b4adfd7664e2` |
| `frontend/package.json` | `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc` |

`frontend/package-lock.json` remains unchanged at
`717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`.
An independent reconstruction using the tracked package diff followed by the
four no-index new-file diffs is exactly 16,238 bytes and byte-identical to
`candidate.pre.diff`, SHA-256
`12d4ccf9e4de7b0924cfdbf7af6db2e3da9fcf2761eaa5cc49f9dd20d8568b1e`.
This proves complete pre/post frontend candidate equality. The diagnostic
occurred on the same frozen hashes; no source, test, package-script, or lock
change intervened.

The package script still verifies the supply first, invokes the argv-safe
wrapper, preserves the dependency and instruction-root gates, and leaves
`desktop:dist` unchanged. The implementation remains an evidence-only,
non-adopted supply-freeze tranche; it is not a package identity, proof
procedure, or proof acceptance.

## Diagnostic and cure evidence

The retained ordinary-sandbox diagnostic is 9,887 bytes with SHA-256
`8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19`.
Its terminal summary is exit 1, four failed test files, 21 failed tests, 1,246
passed, and 4 skipped. The failed-test inventory is confined to four existing
runtime/provider fixture files. The log shows the common TCP
`listen EPERM 127.0.0.1` cause for the provider groups and three Unix
`control.sock` `listen EPERM` causes for daemon groups; the later
`Server is not running` text is the documented cleanup consequence of the
denied listen. None of those four files imports or invokes either R18 supply
script. The run is therefore accurately classified
`ENVIRONMENT_SANDBOX_SOCKET_DENIAL` and remains **not PASS**.

The sealed cure brief, pre-run freeze, post-run freeze, exact exit file, log,
checks, and executor return consistently record exactly one later command:
`npm test`, from `projects/chirality-app-dev/frontend`, with execution-tool
elevation only for local loopback/Unix-socket binding and no network request,
URL, or network tool. `npm-test.exit-status.txt` contains `0` and has SHA-256
`9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
The retained complete normalized output is 485 bytes, SHA-256
`f7313d0e79460d09de5b09f055e75c7a7fc8d9561a6ed238ce1a4ae6bf68cb92`,
and reports 155 test files passed / 1 skipped and 1,267 tests passed / 4
skipped. Pre/post source hashes and the complete candidate diff are identical.
No second test is recorded or authorized. This reviewer accepts that evidence
without rerunning outside the sandbox.

Cure evidence hashes are:

- `PRE_RUN_FREEZE.md`:
  `37ae752b0692a04819a9c2628861c29d4f6cae62851952e902899e40d208efe9`;
- `POST_RUN_FREEZE.md`:
  `29f990a2aa189ff6687e04fb00d483857d50c995c7a73048fb889e2c33a3a68f`;
- `CHECKS.md`:
  `91d62eb2db23cfed1a1612e9fb843b7e4bfd612614d7aeb32a4a1c16932d2f65`;
- `RETURN.md`:
  `cb5b2c9a04db04647aae20112d7681f84ac3bce9898eea1eb83b0a63d82f1fdb`.

## Records, harvest, and fences

- R18 SHA-256:
  `f7ac51f841c87d8f56ed96b2dc8efcad7a25954eabcf492e072a8e8c2a44e303`.
- DEL-09-04 `_STATUS.md` SHA-256:
  `cafdd98b81e73705b642928b46e1240fd0a8b5f42caa2208fa11547983deba1a`.
- TM candidate SHA-256:
  `2ad6e115196082f52d0763f87161bde1b237847ed265e7be401b0f7ef0c3e284`.

R18 and `_STATUS.md` accurately preserve both runs, their distinct
classification, exact counts, the no-source-change proof, evidence-only and
non-adopted package posture, and DEL-09-04 `IN_PROGRESS`/unproved state. They
state the PR pre-merge release-quality wrapper's `full_test` plus typecheck
only as future independent confirmation not yet observed. R19 remains a
separate post-merge owner-authorized act.

The TM document is explicitly `HARVESTED ONLY — NOT PROMOTED OR
DISPOSITIONED`; it contains no implementation, Action Item row, promotion,
ruling, priority, authority, disposition, acceptance, or lifecycle effect.

The candidate and retained execution evidence contain no R19/proof procedure
or proof act, prepare/capture, logout/login, bootstrap/kickstart, operator job
mutation, signing, notarization, deployment, distribution, publication,
release-readiness claim, Receipt 189, staging, commit, push, PR, or merge.

## Hygiene and retained proportional gates

- `git diff --check`: PASS.
- Staged-equivalent `git diff --no-index --check` over all 79 untracked
  textual files at review input: PASS, 79/79. The other five untracked files
  are the deterministic gzip preimages.
- Run-root JSON parse: PASS, 8/8.
- App-only full porcelain containment: PASS, 86/86 at review input and 87/87
  after this bounded reviewer output.
- Empty index: PASS.
- APP-HOLD retained scan: PASS, 53 contracts, held count 0, register match
  true; SHA-256
  `f39d3ffdb2ad410fe32420e0919ccdb7ee7c74ac3aef85e889e74ec16a14723d`.
- DEL-09-04 reliance check: `ALLOW` / `NOT_HELD`; SHA-256
  `76dd3a863c9237ea48a213fcec5300a6abf5e8213eebd4c346c4856ed54a3495`.
- Retained practitioner pytest: PASS, 350/350; SHA-256
  `833377099f98a92f9293dbbd3354a3a84cc88aa50a27237333c925ce55e15ff8`.
- Retained practitioner self-check: exit 0 at the calibrated non-blocking
  baseline; actual SHA-256
  `67ac9305b5be5cc2b71e1c2a9b5f3b5bfb32173e09f50d91007a04ec71d54f28`.
- Prior-ledger receipt validator: PASS and ledger unchanged; SHA-256
  `f8409bcfe80bcd62109d9f6b58ab81437528f88c6d1d2c0f474b86268fcca924`.
- Retained production verifier, package-lock consistency, and
  instruction-root integrity logs remain unchanged at respectively
  `5af72fdf79d96a79f68b7d81b118f437d266c0b73e803ac6b8e567cba1ce20ae`,
  `e9313dd7224771d4b9d5f9d0e545a3a83f5b7590e5ffde22cbde7834fdad3c06`,
  and `fc655ba608e142a236b03f3a52d6d5e31fb02f4d39d51f02328ae50e63c15bfa`.

The immutable historical `review-1/REVIEW.md` transcribed the self-check hash
with the production-verifier digest's suffix. Direct hashing proves the
self-check value above; the log predates and was not modified by repair or
cure. This current review supplies the corrected digest without rewriting the
historical review. The transcription has no effect on the retained self-check
result and leaves no unresolved evidence ambiguity.

## Checks actually run

The reviewer used only read-only inspection and this one bounded review write:

- `git status --short`, full `--porcelain=v1 -z --untracked-files=all`,
  `git diff --cached --name-only`, `git rev-parse HEAD`, parent inspection,
  `git diff --check`, path-limited `git diff`, and no-index diff/checks;
- `shasum -a 256`, manifest verification from the manifest directory,
  `wc`, `stat`, `find`, `rg`, `sed`, `tail`, and `jq`;
- read-only Python byte checks for gzip headers/decompression, normalization
  equivalence and deletion counts, JSON parsing, porcelain containment,
  staged-equivalent whitespace, and exact in-memory candidate-diff
  reconstruction.

An initial manifest check was invoked from the repository root and therefore
reported only relative-path open failures; rerunning the same check from the
manifest directory passed 5/5. Neither invocation changed state.

No prohibited test, package/build, network, instruction-root, receipt-write,
Git integration, or proof command was run.

## Terminal return

`VALIDATED_PASS`

Manager fan-in may accept the repaired R18 Tranche A candidate. The retained
sandbox diagnostic remains not PASS; the owner-authorized cure is the passing
full-suite evidence. Any later implementation/package byte change requires
affected deterministic checks and a new fresh review. PR pre-merge
`full_test` plus typecheck remains future independent confirmation, and R19
remains separate.
