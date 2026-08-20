# A2-PKG02-PARITY-INTEGRATED-VERIFIER-04 return

Verdict: `ACCEPT_REPAIRED_FAN_IN_V4`

Scope: fresh evidence-only verification of the exact frozen run-root bytes
under `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md`. All required
checks passed. This accepts only a truthful `BLOCKED / PARTIAL` records
fan-in; it does not accept parity, a distinct-helper trigger, a rerun,
release readiness, or any product, deliverable, lifecycle, waiver, network,
launcher-restoration, receipt, or Git effect.

## Frozen-byte verification

All 18 required frozen artifacts exist and match exactly:

| Artifact | Checked SHA-256 |
|---|---|
| Manager `RETURN.md` | `3c68a8d060e13e4e7c9d085e172ff6bcb95b1e4eb3255073bc8d028a13a9270b` |
| `CLOSEOUT_AMENDMENT_01.md` | `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7` |
| `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md` | `6ada335fab940c9c9265a37fa2d042fba94beff8a8f0a66df1a28c9d12e812a8` |
| `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md` | `27f7fb008ffee1d2f7561ee53be39734b262e29cf37d5eb51c16da1195a8df51` |
| `EVIDENCE_INDEX.csv` | `9cc9a80452c5b684d453adf23986f937eebbe582a2a67023fa27fc74f199fbf1` |
| `STATUS.md` | `127f5b9b0c02842571c3f22d5a3b7432c507def9af421c7622387599b919e3af` |
| `HANDOFF_STATE.md` | `da113537fa4999ef15a864ee4d1777ab9646c6b75c2363d576929deb8b5c772c` |
| `REGISTERED_CHECKS.json` | `a99a5b6d9b83fecc43f35707f120c668271c018174886193ac876e2e7b1259b0` |
| `RUNTIME_SUMMARY.json` | `738d5889e9ba81f1cda64779e23a1afcdb2e7ebdd3195febd3a2548847ab851c` |
| E1 `RETURN.md` | `9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9` |
| E1 `STATUS.json` | `b175bf31f92883f52e11fe6cdae32fa01b6a8e559cdcdd2e905bf85b2ef9256e` |
| V1 `RETURN.md` | `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21` |
| V1 `STATUS.json` | `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1` |
| V2 `RETURN.md` | `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e` |
| V2 `STATUS.json` | `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832` |
| V3 `LAUNCH_BRIEF.md` | `a85c2459a9761dabffe348776b56fb0724ff4799c9a39952d8e0950e938b0bd8` |
| V3 `RETURN.md` | `2ca7810a2a48667ae1f63b4350f300918334edfbc183fb1acb11e5e128bdce87` |
| V3 `STATUS.json` | `38bf6fd267d7f5d3be229e8db73e3dad5fa4bb87aa000a0c5deac66396d3ecfe` |

All ten pre-return run-root `.json` files parse. E1, V1, V2, and V3 use
`chirality-agent-instance-status/v1`, are terminal, and bind their exact
immutable returns and outcomes: `BLOCKED / PARTIAL`,
`ACCEPT_BLOCKED_FAN_IN`, `ACCEPT_AMENDED_FAN_IN`, and
`REJECT_REPAIRED_FAN_IN`, respectively. V3's brief, rejected return, and
terminal status remain byte-preserved; V4 neither rewrites nor erases that
provenance.

## Index, registered checks, and telemetry

- `EVIDENCE_INDEX.csv` parses as six columns and exactly 22 data rows. All
  22 artifacts resolve within the run root and all 22 hashes match.
- `REGISTERED_CHECKS.json` uses
  `chirality-software-check-evidence/v1` and binds branch
  `codex/app-dapp86-helper-parity-rerun-20260820`, HEAD
  `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, and tree
  `fe8ece104dd281e3219bd95fa8b121437d524520`. Its six directly hashed proof
  references match. Packaged UI is `BLOCKED`; premerge, release-quality, and
  secret-scan are `NOT_RUN`, never PASS. `waivers` is empty.
- Manager `RETURN.md` binds `RUNTIME_SUMMARY.json` by exact path and SHA-256
  `738d5889e9ba81f1cda64779e23a1afcdb2e7ebdd3195febd3a2548847ab851c`,
  and uses PASS only for ledger completeness. It explicitly records waivers
  as none.
- Independent reconciliation of `RUNTIME_EVENTS.jsonl` yields 15 events,
  five STARTs, five FINISHes, five matched sessions, and zero unmatched
  sessions, exactly agreeing with the summary.

## Claim, raw-evidence, and manifest calibration

The closeout remains `BLOCKED / PARTIAL`: parity closure is false; no distinct
helper trigger is established; no rerun is authorized; the launcher is
untouched after the recorded application write; and network-retry
authorization plus successful-package-command provenance remain `UNKNOWN`.
Live source exposes `CHIRALITY_SKIP_CLI_LAUNCHER` and states that daemon mode
uses the same bundle relaunched with `--runtime-daemon`. The package contains
the main app and four ordinary Electron helper apps, with no daemon-specific
helper app.

All 18 retained executor evidence files match the exact hashes preserved by
V2/V3. E1, V1, and V2 returns remain byte-identical. The source manifest
independently revalidates 509/509 rows, and the packaged-app manifest
independently revalidates 446/446 rows.

The current launcher remains mode `-rwx------`, size `1114`, inode `45468523`,
mtime `2026-08-20T15:26:36-0600`, and SHA-256
`f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
It was not altered.

## Amendment 03 containment disposition

HEAD, tree, and branch match the frozen identities; the staged diff is empty.
All non-ignored untracked repository paths are within this run root. The only
tracked outside-run-root diff observed is
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`. Under Agent 0's governing
Amendment 03 disposition, that Receipt 183 diff is parent-owned lawful fan-in
state, is excluded from package-manager/child attribution, and receives no
semantic judgment from V4. No other current outside-run-root repository write
attributable to `WI-PKG02-DAPP86-RERUN-01` or its children was found. The
separately recorded launcher write remains the truthful execution blocker and
was not repeated, repaired, restored, or otherwise changed by V4.

No repair, test, build, app, daemon, UI, network, receipt, product,
deliverable, launcher, or Git mutation was performed. This `RETURN.md` is the
verifier's sole write. No `STATUS.json` was created.
