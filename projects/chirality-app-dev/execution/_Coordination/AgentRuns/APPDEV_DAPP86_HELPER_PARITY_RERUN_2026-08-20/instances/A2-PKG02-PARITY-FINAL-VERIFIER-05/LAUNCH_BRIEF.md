# Sealed launch brief — A2-PKG02-PARITY-FINAL-VERIFIER-05

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`

ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01-AMEND04`

InstanceID: `A2-PKG02-PARITY-FINAL-VERIFIER-05`

Role: fresh read-only Agent 2 final-record verifier

Source HEAD: `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`

Source tree: `fe8ece104dd281e3219bd95fa8b121437d524520`

Branch: `codex/app-dapp86-helper-parity-rerun-20260820`

## Objective

Verify the exact final run-root bytes after Closeout Amendment 04. This is a
records-only verification, not product execution. Preserve every prior V1-V4
verdict and status, including V3's rejected provenance and V4's accepted
Amendment-03 disposition. Do not repair anything.

## Frozen key hashes

- `EVIDENCE_INDEX.csv`: `f8e854d1cdc1255b931481e9c65fdb24557cad78168d44b5cc8628c5d6360f1d`
- Manager `RETURN.md`: `9f6d785e7c82fcf4ef71a91474f40d2a1c58eb50034749a4aa4cd1f57a0e88e8`
- `REGISTERED_CHECKS.json`: `319440676d888be24ff509ac54b857555f640430a2195ba5173bf5a778db9d99`
- `RUNTIME_EVENTS.jsonl`: `7d07b3a44b7b1dd68ef29e67e75da63278a518c14f827a77fbaf3f52fbb47f80`
- `RUNTIME_SUMMARY.json`: `9b7bc6fe10c6153c882b9be0685e27140c06f87290f18cbbe6f909ec14e8d2a1`
- `STATUS.md`: `faaa54a033842a82c8abe5b11ce1dea4f8d73790846ce26db0e1a3e7b9d3c719`
- `HANDOFF_STATE.md`: `338dca525519e2d44affb72ecdac1dc968b9bb1239b07f848e72e107242dd869`
- `CLOSEOUT_AMENDMENT_01.md`: `989bdbb79c03378b398931c1010a1ba061ad62c12d188e91db5be9a0a164b6b7`
- `CLOSEOUT_AMENDMENT_02_INTEGRATED_REVIEW.md`: `fd1313ea4c972ece9362e11f60a71e487c4e9f1f7c0e5872322dc1d5b8b46663`
- `CLOSEOUT_AMENDMENT_03_V4_CONTAINMENT_DISPOSITION.md`: `a6a8731601bcd0945e102b4c39841aeadae78b2a2fe4a525aa5126d1b1d0c4bf`
- `CLOSEOUT_AMENDMENT_04_WHITESPACE_AND_EVIDENCE_MATERIALIZATION.md`: `50189a6644260857debcd1365bda8a7fc8a06ecf032bc31c7797e53c17327f16`
- E1 `RETURN.md`: `408eae1a1e14baafd93228f07222aebe62d78823d7ec18ac8b09c7771aa6904c`
- E1 `STATUS.json`: `ba5a0bc42b44a699ca081efd429c7bdc271cd9a9f789b22f575a4fb39401f079`
- V1 `RETURN.md`: `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21`
- V1 `STATUS.json`: `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1`
- V2 `RETURN.md`: `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e`
- V2 `STATUS.json`: `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832`
- V3 `RETURN.md`: `2ca7810a2a48667ae1f63b4350f300918334edfbc183fb1acb11e5e128bdce87`
- V3 `STATUS.json`: `38bf6fd267d7f5d3be229e8db73e3dad5fa4bb87aa000a0c5deac66396d3ecfe`
- V4 `RETURN.md`: `1f0bc86087a86f535276e7467d3feed55755a4953929a2bc42b950ab0f0033d5`
- V4 `STATUS.json`: `79322f0ef6b33cbca6a133d7862a51a59455ed36c1b715e1d4cab7fc2126d713`

## Required verification

1. Recompute every frozen key hash above.
2. Parse `EVIDENCE_INDEX.csv` as exactly six columns and 40 data rows. Resolve
   every `Artifact` under the run root and recompute all 40 hashes.
3. Parse every run-root JSON and every JSONL event. Confirm E1 and V1-V4
   terminal statuses use `chirality-agent-instance-status/v1`, bind the exact
   current return hashes, and preserve their exact outcomes. E1's return change
   must be limited to the Amendment-04 surplus-EOF normalization. V3 must
   remain `REJECT_REPAIRED_FAN_IN`; V4 must remain
   `ACCEPT_REPAIRED_FAN_IN_V4`.
4. Confirm `REGISTERED_CHECKS.json` binds exact branch/HEAD/tree, has status
   `BLOCKED_PARTIAL`, records packaged UI `BLOCKED`, records premerge,
   release-quality, and secret-scan as `NOT_RUN`, and has waivers `[]`.
   Recompute every proof hash and original-content hash it declares.
5. Confirm manager `RETURN.md`, `STATUS.md`, and `HANDOFF_STATE.md` consistently
   state final overall `BLOCKED / PARTIAL`, V4 accepted, V3 preserved, no
   parity closure, no established distinct-helper trigger, no rerun authority,
   N2 held, waivers none, package retry authorization and successful-command
   provenance `UNKNOWN`, and launcher untouched after the recorded write.
6. Reconcile `RUNTIME_EVENTS.jsonl` through the repository runtime-telemetry
   schema/tool. Require 21 events, 8 sessions, 8 STARTs, 8 FINISHes, and zero
   unmatched sessions. Confirm V3, V4, and Amendment 04 are identified as
   records-only verification/remediation, not product execution, and summary
   calibration remains `BLOCKED / PARTIAL`.
7. Verify Amendment 04's four deterministic gzip mappings. Require each gzip
   hash to match, `gzip -cd` to reproduce the exact original content hash, and
   all four plaintext `.log` candidates to be absent. Do not normalize or
   rewrite any raw evidence.
8. Independently revalidate all 509 source-manifest rows and all 446
   packaged-app manifest rows. Confirm retained non-gzip raw evidence remains
   consistent with the current 40-row index and historical verifier returns.
9. Confirm claim calibration: the four packaged UI observations and packaged
   replay remain unproved; daemon fixture is partial only; the invocation
   omitted `CHIRALITY_SKIP_CLI_LAUNCHER=1`; no distinct helper is established;
   no network/package retry authorization is inferred.
10. Verify the launcher at `/Users/ryan/.local/bin/chirality` remains SHA-256
    `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
    Do not alter it.
11. Apply Amendment 03 containment exactly: every WI/child-attributable write
    must remain inside the run root. Exclude parent-owned Receipt 183 from WI
    attribution and make no judgment on its semantics. Report any other
    attributable outside-run-root effect.
12. Run the candidate-equivalent whitespace check over every run-root file:
    `git diff --no-index --check /dev/null <file>`. Require zero findings. After
    writing your return, repeat it so your own return and this brief are also
    included and whitespace-clean.
13. Confirm no product, package, UI, deliverable, receipt, launcher, or Git
    mutation is performed by V5. Preserve all prior verifier provenance.

## Permissions and return

Repository-wide read is allowed. Your sole write is:

`instances/A2-PKG02-PARITY-FINAL-VERIFIER-05/RETURN.md`

Do not create `STATUS.json`; the manager will create it after your return. Do
not modify this brief or any previously frozen artifact. Use verdict
`ACCEPT_FINAL_RECORDS_V5` only if every required check passes; otherwise use
`REJECT_FINAL_RECORDS_V5` and identify exact blockers. Include exact counts,
hashes, candidate-whitespace result, containment disposition, gzip integrity,
launcher identity, and an explicit no-repair statement.
