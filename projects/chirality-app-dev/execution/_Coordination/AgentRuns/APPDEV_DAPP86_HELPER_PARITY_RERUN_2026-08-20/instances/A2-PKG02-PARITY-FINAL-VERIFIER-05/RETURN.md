# A2-PKG02-PARITY-FINAL-VERIFIER-05 return

Verdict: `REJECT_FINAL_RECORDS_V5`

Scope: fresh read-only verification of the exact final run-root bytes after
Closeout Amendment 04. One mandatory registered-proof binding fails. No repair,
product execution, package execution, UI action, deliverable action, receipt
action, launcher action, or Git action was performed. This `RETURN.md` is V5's
sole write. V5 did not create `STATUS.json`.

## Blocking finding

`F1 — STALE PACKAGED-UI PROOF HASH IN REGISTERED_CHECKS.json`

`REGISTERED_CHECKS.json` result `packaged-ui-smoke` declares
`proof_ref: PACKAGED_UI_SMOKE.md` and `proof_sha256`
`38ee41bc01415f21311136bd344a4d48e1ab836e9504906749168e4cbd837ed0`.
The current referenced file instead hashes to
`2149fa1fabf6c0e7ce655be77222d0d21a27cd2f124c8efade2776b4abed8fab`.
The latter is also the hash correctly recorded for all four packaged-UI rows
in the current 40-row `EVIDENCE_INDEX.csv`.

This is consistent with Amendment 04 having whitespace-normalized
`PACKAGED_UI_SMOKE.md` without refreshing this one registered proof field, but
V5 makes no repair. Thirteen of fourteen declared proof, original-content, and
ledger hash fields recompute successfully; this field is the sole mismatch.
Because the sealed brief requires every declared proof hash to recompute, the
final records cannot receive `ACCEPT_FINAL_RECORDS_V5`.

## Frozen bytes, index, JSON, and child status

All 21 frozen key hashes match exactly:

| Artifact | Checked SHA-256 |
| --- | --- |
| `EVIDENCE_INDEX.csv` | `f8e854d1cdc1255b931481e9c65fdb24557cad78168d44b5cc8628c5d6360f1d` |
| Manager `RETURN.md` | `9f6d785e7c82fcf4ef71a91474f40d2a1c58eb50034749a4aa4cd1f57a0e88e8` |
| `REGISTERED_CHECKS.json` | `319440676d888be24ff509ac54b857555f640430a2195ba5173bf5a778db9d99` |
| `RUNTIME_EVENTS.jsonl` | `7d07b3a44b7b1dd68ef29e67e75da63278a518c14f827a77fbaf3f52fbb47f80` |
| `RUNTIME_SUMMARY.json` | `9b7bc6fe10c6153c882b9be0685e27140c06f87290f18cbbe6f909ec14e8d2a1` |
| `STATUS.md` | `faaa54a033842a82c8abe5b11ce1dea4f8d73790846ce26db0e1a3e7b9d3c719` |
| `HANDOFF_STATE.md` | `338dca525519e2d44affb72ecdac1dc968b9bb1239b07f848e72e107242dd869` |
| `CLOSEOUT_AMENDMENT_01.md` | `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7` |
| `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md` | `fd1313ea4c972ece9362e11f60a71e487c4e9f1f7c0e5872322dc1d5b8b46663` |
| `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md` | `a6a8731601bcd0945e102b4c39841aeadae78b2a2fe4a525aa5126d1b1d0c4bf` |
| `CLOSEOUT_AMENDMENT_04_WHITESPACE_AND_EVIDENCE_MATERIALIZATION.md` | `50189a6644260857debcd1365bda8a7fc8a06ecf032bc31c7797e53c17327f16` |
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

`EVIDENCE_INDEX.csv` parses with exactly six columns and 40 data rows. All 40
artifact paths resolve inside the run root, and all 40 indexed hashes match.
All 11 run-root JSON files parse, as do all 21 JSONL events.

E1 and V1-V4 all use `chirality-agent-instance-status/v1`, are terminal, and
bind their exact current return hashes. Their preserved statuses and outcomes
are E1 `BLOCKED` / `BLOCKED / PARTIAL`, V1 `SUCCESS` /
`ACCEPT_BLOCKED_FAN_IN`, V2 `SUCCESS` / `ACCEPT_AMENDED_FAN_IN`, V3
`BLOCKED` / `REJECT_REPAIRED_FAN_IN`, and V4 `SUCCESS` /
`ACCEPT_REPAIRED_FAN_IN_V4`. Appending the one Amendment-04-removed surplus
EOF newline to the current E1 return reconstructs its pre-normalization hash
`9a85bd10197cc398b694add6ff98f01ad4f104e3769668dfec89a495dc2238c9`,
confirming that return's stated byte-only normalization.

## Registered checks, telemetry, and calibrated claims

Apart from F1, `REGISTERED_CHECKS.json` correctly binds branch
`codex/app-dapp86-helper-parity-rerun-20260820`, HEAD
`89758a32634ee6cedbd1dbadf35e3728fb48d2eb`, and tree
`fe8ece104dd281e3219bd95fa8b121437d524520`; status is
`BLOCKED_PARTIAL`. Packaged UI is `BLOCKED`; premerge, release-quality, and
secret-scan are `NOT_RUN`; `waivers` is `[]`. All four gzip proof hashes and
their four declared original-content hashes match, as do the fixture,
Amendment-04, runtime-summary, and runtime-ledger hash declarations. F1 is the
only declared-hash failure.

Repository-schema reconciliation of `RUNTIME_EVENTS.jsonl` yields exactly 21
events, eight sessions, eight STARTs, eight FINISHes, and zero unmatched
sessions. Event IDs are unique, every event uses
`chirality-runtime-event/v1`, and recomputed counts, durations, final outcomes,
retry counts, and remediation counts match `RUNTIME_SUMMARY.json`. The summary
uses `chirality-runtime-summary/v1` and is `PASS` only for ledger completeness.
V3 and V4 are records-only verification sessions and Amendment 04 is a
records-only remediation session; none is product execution. Closeout remains
`BLOCKED / PARTIAL`.

Manager `RETURN.md`, `STATUS.md`, and `HANDOFF_STATE.md` consistently preserve
V3's rejected provenance and V4's accepted Amendment-03 disposition. They state
no parity closure, no established distinct-helper trigger, no rerun authority,
N2 held, waivers none, launcher untouched after the recorded write, and both
network/package retry authorization and successful-command provenance
`UNKNOWN`.

The four packaged UI observations and packaged replay remain unproved. The
daemon fixture is partial daemon-side evidence only: two canonical events, one
transcript item, zero malformed events, terminal status `completed`. The
verification invocation omitted `CHIRALITY_SKIP_CLI_LAUNCHER=1`; no distinct
helper is established, and no network or package retry authorization is
inferred.

## Evidence, manifests, gzip, launcher, and containment

All 509 source-manifest rows and all 446 packaged-app manifest rows
independently revalidate against their current target files. Four deterministic
gzip mappings pass in full:

| Gzip evidence | Gzip SHA-256 | Decompressed original SHA-256 |
| --- | --- | --- |
| `build.log.gz` | `dd6a973726f1f61395d038577b16ff75fad2bf246d63aab7d7ee09025d4945f5` | `f964c5833323869b36b68102a71e7dc717346a9ac6365cf86ef378479228becd` |
| `desktop-pack.log.gz` | `b8056db8bde1e8e18f8fc887af0680f1f5710cd3dc103d8c506e78d804d21faa` | `5675bdbb162f9463b3500f883e5524a8e511df982e4bcc626f34b20a08186513` |
| `focused-tests.log.gz` | `84a667c1fd77e1b883af8d3de98954c4e299ef446ad3b1d37f03a48b8e08930c` | `1aae3ff66b7afd86d99c54eef10aa12f34e726ad1ab7f48da00a039126f7db46` |
| `typecheck.log.gz` | `2bee31acfe5afe23d0b26c161ef1cc6ed88b8bf68ecb590b29ec4fa48b90e61d` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` |

All four decompressions reproduce the exact original byte hashes, and all four
plaintext `.log` candidates are absent. The 14 retained non-gzip executor
evidence files remain consistent with the current index and historical
verifier provenance: 13 are byte-identical to V4's recorded hashes, while
`CLEANUP_CONTAINMENT.md` has only Amendment 04's declared whitespace
normalization and now matches the indexed SHA-256
`51e1425f74f35c6643d531e88443ad64c45c4697866f9308e30450ad9ad894b2`.

The launcher at `/Users/ryan/.local/bin/chirality` remains mode `-rwx------`,
size `1114`, inode `45468523`, mtime `2026-08-20T15:26:36-0600`, and SHA-256
`f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
V5 did not alter it.

HEAD, tree, and branch match the frozen identities, and the staged diff is
empty. Every non-ignored untracked path is inside the run root. The only
tracked outside-run-root diff is
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`. Amendment 03 identifies
Receipt 183 as parent-owned state; V5 excludes it from WI/child attribution and
makes no judgment on its semantics. No other WI/child-attributable
outside-run-root effect was found.

## Candidate whitespace and no-repair disposition

Before this return, `git diff --no-index --check /dev/null <file>` produced
zero whitespace findings across all 53 run-root files, including the V5 brief
and four binary gzip files. After writing this return, V5 repeated the same
candidate-equivalent traversal across all 54 run-root files; it again produced
zero findings, including for this return.

No frozen artifact was modified, no raw evidence was normalized or rewritten,
and no repair was attempted. V3 remains preserved rejected provenance; V4
remains the accepted Amendment-03 record disposition. The sole blocker is F1.
