# A2-PKG02-PARITY-FINAL-VERIFIER-06 return

Verdict: `ACCEPT_FINAL_RECORDS_V6`

Scope: fresh read-only verification of the exact pre-V6-finalization run-root
bytes after Agent 0's authorized one-field V5 remediation. Every required
check passed. No repair, product execution, package execution, daemon action,
UI action, deliverable action, receipt action, launcher action, or Git action
was performed. This `RETURN.md` is V6's sole write. V6 did not create
`STATUS.json`.

## Frozen identities, index, JSON, and terminal children

All 19 frozen key hashes match exactly:

| Artifact | Checked SHA-256 |
| --- | --- |
| `EVIDENCE_INDEX.csv` | `747d6f3f5361ea04929785808409f3e541aacf6f0d6767fba8c6aecba064750e` |
| Manager `RETURN.md` | `56b65af527cbc0196f441dc0447cfbb1d41e16759d1ded66dfaa8f06c4da4de2` |
| `REGISTERED_CHECKS.json` | `157b059d918e944033711abd1803dba13b533f3310d91f3d525d90f1d982c4c6` |
| `RUNTIME_EVENTS.jsonl` | `6d5c97601aabcb16758f2006cb54b5eefc45afdef1c407aa256173a555560e0e` |
| `RUNTIME_SUMMARY.json` | `a0766bb2d8a0110a44cc1264a3916f0eabab76ca8f43403d6022f93766cb4d83` |
| `STATUS.md` | `4f7a9490f9ba08709f22ab1e854be4cfd10bb1661a07114194afb10e09e9389b` |
| `HANDOFF_STATE.md` | `d285d01cc8c5e03850e52f6e9797409f386792542af670ac33e94e43d594eb33` |
| V5 `RETURN.md` | `54658dbbf634280575132821db1ecdc7a487829c5811c3034c66abcc0a92d19d` |
| V5 `STATUS.json` | `bebd2aeb89be96bf3c2bb662679896c14ba7e0caa958eb6e4a1a3dfd6eb987e0` |
| E1 `RETURN.md` | `408eae1a1e14baafd93228f07222aebe62d78823d7ec18ac8b09c7771aa6904c` |
| E1 `STATUS.json` | `ba5a0bc42b44a699ca081efd429c7bdc271cd9a9f789b22f575a4fb39401f079` |
| V1 `RETURN.md` | `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21` |
| V1 `STATUS.json` | `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1` |
| V2 `RETURN.md` | `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e` |
| V2 `STATUS.json` | `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832` |
| V3 `RETURN.md` | `2ca7810a2a48667ae1f63b4350f300918334edfbc183fb1acb11e5e128bdce87` |
| V3 `STATUS.json` | `38bf6fd267d7f5d3be229e8db73e3dad5fa4bb87aa000a0c5deac66396d3ecfe` |
| V4 `RETURN.md` | `1f0bc86087a86f535276e7467d3feed55755a4953929a2bc42b950ab0f0033d5` |
| V4 `STATUS.json` | `79322f0ef6b33cbca6a133d7862a51a59455ed36c1b715e1d4cab7fc2126d713` |

The source identities also remain exact: HEAD
`89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, tree
`fe8ece104dd281e3219bd95fa8b121437d524520`, and branch
`codex/app-dapp86-helper-parity-rerun-20260820`.

`EVIDENCE_INDEX.csv` parses with exactly six columns and 42 data rows. All 42
artifact paths resolve inside the run root, and all 42 current hashes match.
All 12 run-root JSON files parse, as do all 25 records in the sole JSONL file.

E1 and V1-V5 all use `chirality-agent-instance-status/v1`, are terminal, bind
their exact current returns, and preserve the following statuses and outcomes:

| Child | Status | Outcome |
| --- | --- | --- |
| E1 | `BLOCKED` | `BLOCKED / PARTIAL` |
| V1 | `SUCCESS` | `ACCEPT_BLOCKED_FAN_IN` |
| V2 | `SUCCESS` | `ACCEPT_AMENDED_FAN_IN` |
| V3 | `BLOCKED` | `REJECT_REPAIRED_FAN_IN` |
| V4 | `SUCCESS` | `ACCEPT_REPAIRED_FAN_IN_V4` |
| V5 | `BLOCKED` | `REJECT_FINAL_RECORDS_V5` |

V3 and V5 remain preserved rejected provenance; V4 remains the accepted
Amendment-03 record disposition. V6 does not reinterpret any prior verdict.

## Registered checks and calibrated claims

All 14 declared registered bindings recompute: nine of nine `proof_sha256`,
four of four `proof_content_sha256`, and one of one `ledger_sha256`. In
particular, `packaged-ui-smoke.proof_sha256` now equals the current
`PACKAGED_UI_SMOKE.md` SHA-256
`2149fa1fabf6c0e7ce655be77222d0d21a27cd2f124c8efade2776b4abed8fab`.

`REGISTERED_CHECKS.json` remains `BLOCKED_PARTIAL`. Packaged UI remains
`BLOCKED`; premerge, release-quality, and secret-scan remain `NOT_RUN`; and
`waivers` remains empty. The manager return, run status, handoff state,
registered checks, and evidence index remain mutually consistent: no parity
closure, no established distinct-helper trigger, no rerun authority, parent
N2 held, waivers none, launcher untouched after its recorded write, and both
network-retry authorization and successful-package-command provenance
`UNKNOWN`.

The four packaged UI observations and packaged replay remain unproved. The
daemon fixture remains partial daemon-side evidence only: two canonical
events, one transcript item, zero malformed events, and terminal status
`completed`. The verification invocation omitted
`CHIRALITY_SKIP_CLI_LAUNCHER=1`; no distinct helper, retry authorization, or
successful package command is inferred.

## Telemetry, gzip, manifests, launcher, and containment

Independent reconciliation of `RUNTIME_EVENTS.jsonl` yields exactly 25 events,
10 sessions, 10 STARTs, 10 FINISHes, 25 unique event IDs, and zero unmatched
sessions. Recomputed event/category/outcome/reason counts, durations, final
outcomes, retries, and remediations match `RUNTIME_SUMMARY.json`. V3, V4, V5,
Amendment 04, and Amendment 05 are records-only verification/remediation, not
product execution. Summary status `PASS` applies only to ledger completeness;
closeout calibration remains `BLOCKED / PARTIAL`.

All four deterministic-gzip evidence mappings pass:

| Gzip evidence | Gzip SHA-256 | Decompressed original SHA-256 |
| --- | --- | --- |
| `build.log.gz` | `dd6a973726f1f61395d038577b16ff75fad2bf246d63aab7d7ee09025d4945f5` | `f964c5833323869b36b68102a71e7dc717346a9ac6365cf86ef378479228becd` |
| `desktop-pack.log.gz` | `b8056db8bde1e8e18f8fc887af0680f1f5710cd3dc103d8c506e78d804d21faa` | `5675bdbb162f9463b3500f883e5524a8e511df982e4bcc626f34b20a08186513` |
| `focused-tests.log.gz` | `84a667c1fd77e1b883af8d3de98954c4e299ef446ad3b1d37f03a48b8e08930c` | `1aae3ff66b7afd86d99c54eef10aa12f34e726ad1ab7f48da00a039126f7db46` |
| `typecheck.log.gz` | `2bee31acfe5afe23d0b26c161ef1cc6ed88b8bf68ecb590b29ec4fa48b90e61d` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` |

All four decompressions reproduce the declared original byte hashes, and all
four plaintext `.log` candidates are absent. Independent manifest checks pass
for all 509 of 509 source rows and all 446 of 446 package rows.

The launcher at `/Users/ryan/.local/bin/chirality` remains mode `-rwx------`,
size `1114`, inode `45468523`, mtime `2026-08-20T15:26:36-0600`, and SHA-256
`f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
V6 did not alter it.

The staged diff is empty. Every non-ignored untracked path is inside the run
root. The only tracked outside-run-root diff is
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`. Under Amendment 03,
parent-owned Receipt 183 is excluded from WI/child attribution. V6 makes no
semantic judgment on it. No other WI/child-attributable outside-run-root effect
was found.

## Candidate whitespace and no-repair disposition

Before this return, `git diff --no-index --check /dev/null <file>` produced
zero candidate-whitespace findings across all 56 run-root files, including the
V6 brief and four binary gzip files. After writing this return, V6 repeated the
same whole-candidate traversal across all 57 run-root files; it again produced
zero findings, including for this return.

No frozen artifact was modified, no raw evidence was normalized or rewritten,
and no repair was attempted. No product, package, daemon, or UI execution was
performed. V3 and V5 remain preserved rejected provenance, V4 remains the
accepted Amendment-03 record disposition, and every V6 acceptance requirement
passes.
