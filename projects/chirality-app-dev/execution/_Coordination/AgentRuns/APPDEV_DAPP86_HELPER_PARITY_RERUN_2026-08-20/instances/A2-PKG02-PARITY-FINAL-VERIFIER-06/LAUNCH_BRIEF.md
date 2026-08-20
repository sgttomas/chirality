# Sealed launch brief — A2-PKG02-PARITY-FINAL-VERIFIER-06

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`

ParentInstanceID: `WI-PKG02-DAPP86-RERUN-01-AMEND05`

InstanceID: `A2-PKG02-PARITY-FINAL-VERIFIER-06`

Role: fresh read-only Agent 2 final-record verifier

Source HEAD: `89758a32634ee6cedbd1dbadf35e3728fb48d2eb`

Source tree: `fe8ece104dd281e3219bd95fa8b121437d524520`

Branch: `codex/app-dapp86-helper-parity-rerun-20260820`

## Objective

Verify the exact pre-V6-finalization run-root bytes after Agent 0's authorized
one-field V5 remediation. This is the final run-local verifier; no V7 will be
dispatched. Preserve V3 and V5 rejected provenance and V4 accepted provenance.
Do not repair anything and do not execute product, package, daemon, or UI work.

## Frozen key hashes

- `EVIDENCE_INDEX.csv`: `747d6f3f5361ea04929785808409f3e541aacf6f0d6767fba8c6aecba064750e`
- Manager `RETURN.md`: `56b65af527cbc0196f441dc0447cfbb1d41e16759d1ded66dfaa8f06c4da4de2`
- `REGISTERED_CHECKS.json`: `157b059d918e944033711abd1803dba13b533f3310d91f3d525d90f1d982c4c6`
- `RUNTIME_EVENTS.jsonl`: `6d5c97601aabcb16758f2006cb54b5eefc45afdef1c407aa256173a555560e0e`
- `RUNTIME_SUMMARY.json`: `a0766bb2d8a0110a44cc1264a3916f0eabab76ca8f43403d6022f93766cb4d83`
- `STATUS.md`: `4f7a9490f9ba08709f22ab1e854be4cfd10bb1661a07114194afb10e09e9389b`
- `HANDOFF_STATE.md`: `d285d01cc8c5e03850e52f6e9797409f386792542af670ac33e94e43d594eb33`
- V5 `RETURN.md`: `54658dbbf634280575132821db1ecdc7a487829c5811c3034c66abcc0a92d19d`
- V5 `STATUS.json`: `bebd2aeb89be96bf3c2bb662679896c14ba7e0caa958eb6e4a1a3dfd6eb987e0`
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

1. Recompute every frozen key hash.
2. Parse `EVIDENCE_INDEX.csv` as exactly six columns and 42 data rows. Resolve
   every `Artifact` under the run root and require 42/42 current hashes.
3. Parse every run-root JSON and JSONL record. Verify E1 and V1-V5 terminal
   statuses bind exact current returns and outcomes. Preserve V3
   `REJECT_REPAIRED_FAN_IN`, V4 `ACCEPT_REPAIRED_FAN_IN_V4`, and V5
   `REJECT_FINAL_RECORDS_V5` without reinterpretation.
4. Verify all 14 declared registered-check hash fields: nine `proof_sha256`,
   four `proof_content_sha256`, and one `ledger_sha256`. In particular,
   `packaged-ui-smoke.proof_sha256` must equal current `PACKAGED_UI_SMOKE.md`
   SHA-256 `2149fa1fabf6c0e7ce655be77222d0d21a27cd2f124c8efade2776b4abed8fab`.
5. Confirm registered status remains `BLOCKED_PARTIAL`, packaged UI is
   `BLOCKED`, premerge/release-quality/secret-scan are `NOT_RUN`, and waivers
   are empty.
6. Reconcile telemetry through V5: 25 events, 10 sessions, 10 STARTs, 10
   FINISHes, zero unmatched sessions. V3/V4/V5 and Amendment 04/05 must be
   records-only verification/remediation, not product execution. Summary
   calibration must remain `BLOCKED / PARTIAL`.
7. Verify all four deterministic gzip hashes and decompressed original-content
   hashes from Amendment 04; require the four plaintext log candidates absent.
8. Independently verify all 509 source-manifest rows and all 446 package
   manifest rows.
9. Confirm manager return, status, handoff, registered checks, and index agree:
   no parity closure, no established distinct-helper trigger, no rerun, N2
   held, waivers none, network retry authorization and successful package
   command provenance `UNKNOWN`, and launcher untouched after its recorded
   write.
10. Verify `/Users/ryan/.local/bin/chirality` remains SHA-256
    `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
11. Apply Amendment 03 containment: all WI/child-attributable writes must be
    inside the run root. Exclude parent-owned Receipt 183 from WI attribution
    and make no semantic judgment on it.
12. Run `git diff --no-index --check /dev/null <file>` over every run-root
    file. Require zero candidate-whitespace findings. After writing your
    return, repeat the check so this brief and your return are included.
13. Perform no repair and no product, package, UI, deliverable, receipt,
    launcher, or Git mutation. The manager will perform one unavoidable
    post-return finalization to add V6 terminal status/telemetry and refresh
    dependent final hashes for an independent Agent 0 review.

## Permissions and return

Repository-wide read is allowed. Your sole write is:

`instances/A2-PKG02-PARITY-FINAL-VERIFIER-06/RETURN.md`

Do not create `STATUS.json`; the manager will create it after your return. Do
not modify this brief or any frozen artifact. Use verdict
`ACCEPT_FINAL_RECORDS_V6` only if every required check passes; otherwise use
`REJECT_FINAL_RECORDS_V6`. Include exact counts, key hashes, 14/14 registered
bindings, candidate-whitespace result, gzip/manifests/launcher/containment
results, preserved V3/V5 provenance, and an explicit no-repair statement.
