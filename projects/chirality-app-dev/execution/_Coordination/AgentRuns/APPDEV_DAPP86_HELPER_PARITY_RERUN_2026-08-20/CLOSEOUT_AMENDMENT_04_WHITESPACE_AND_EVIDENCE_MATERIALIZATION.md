# Closeout Amendment 04 — candidate whitespace and evidence materialization

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`

This records-only amendment responds to the final integrated review. It does
not rerun product, package, daemon, or UI behavior and does not change the
overall `BLOCKED / PARTIAL` result, establish parity or the distinct-helper
trigger, release N2, authorize a rerun, waive a gate, or alter the launcher.

## Lossless raw-log materialization

Four captured validation logs carried candidate-whitespace findings. Their
exact original bytes were compressed with deterministic `gzip -n`; the
plaintext candidates were removed. Decompressing each `.gz` reproduces the
listed original SHA-256 exactly.

| Original path | Original SHA-256 | Deterministic gzip path | Gzip SHA-256 |
| --- | --- | --- | --- |
| `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/build.log` | `f964c5833323869b36b68102a71e7dc717346a9ac6365cf86ef378479228becd` | `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/build.log.gz` | `dd6a973726f1f61395d038577b16ff75fad2bf246d63aab7d7ee09025d4945f5` |
| `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/desktop-pack.log` | `5675bdbb162f9463b3500f883e5524a8e511df982e4bcc626f34b20a08186513` | `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/desktop-pack.log.gz` | `b8056db8bde1e8e18f8fc887af0680f1f5710cd3dc103d8c506e78d804d21faa` |
| `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/focused-tests.log` | `1aae3ff66b7afd86d99c54eef10aa12f34e726ad1ab7f48da00a039126f7db46` | `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/focused-tests.log.gz` | `84a667c1fd77e1b883af8d3de98954c4e299ef446ad3b1d37f03a48b8e08930c` |
| `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/typecheck.log` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` | `instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/validation/typecheck.log.gz` | `2bee31acfe5afe23d0b26c161ef1cc6ed88b8bf68ecb590b29ec4fa48b90e61d` |

The original hashes cited in earlier verifier returns remain historical facts
about the decompressed raw bytes. Current proof references and the evidence
index use the `.gz` paths and gzip hashes, with original content hashes retained
as explicit integrity fields.

## Authored-record normalization

Candidate-only Markdown/JSON whitespace was normalized without changing
claims: trailing spaces were removed and surplus blank EOF lines were reduced
to one terminating newline. This affected the following authored records:

- `ACTIVATION.md`
- `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md`
- `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md`
- `ORCHESTRATION_PLAN.md`
- `PACKAGED_UI_SMOKE.md`
- `REAL_DAEMON_REPLAY.md`
- `WORK_GRAPH.json`
- E1 `LAUNCH_BRIEF.md` and `RETURN.md`
- E1 `evidence/CLEANUP_CONTAINMENT.md`
- V1, V2, V3, and V4 `LAUNCH_BRIEF.md` files identified by the whitespace audit

V1 through V4 returns and their terminal verdicts remain unchanged. E1's
terminal status is refreshed only to bind the whitespace-normalized return
hash. V3 remains rejected provenance; V4 remains the accepted record-verifier
disposition under Amendment 03.

## Candidate check

The frozen candidate must produce no output for this check over every file:

`git diff --no-index --check /dev/null <file>`

Binary gzip evidence is included in the traversal and produces no whitespace
finding. V5 must independently repeat the complete candidate-root check and
the four gzip decompression/hash comparisons.
