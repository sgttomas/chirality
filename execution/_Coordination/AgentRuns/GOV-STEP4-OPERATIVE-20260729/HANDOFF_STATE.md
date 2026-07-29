# Handoff — GOV-STEP4-OPERATIVE-20260729

Status: `READY_FOR_HUMAN_GATED_PR`

## State

- `ClosureVerdict`: `PROPAGATION_AUTHORED_AWAITING_PR_GATE`
- `DerivativePackage`: `NO` (operative-surface reconciliation plus
  records; the public export under `exports/chirality-app/` is a stale
  derivative, regeneration deferred per the tranche manifest)
- `AuthoritativeEffect`: applies already-ruled D-GOV-31 obligations;
  rules nothing new (K-AUTH-1)
- `GlobalBlocker`: SCA-002 acceptance dependency (below)

## Dependencies and blockers

1. **SCA-002 acceptance (blocking for merge).** The DEL-04-06
   `ScopeOfWork.md` / `_CONTEXT.md` reconciliation presumes the SCA-002
   decomposition amendment (SOW-042 restatement, drafted in a sibling
   SCOPE_CHANGE-owned run) is accepted by the owner BEFORE this tranche
   merges, so the deliverable contract, the scope ledger, and the live
   PRD D-8 row say the same thing. If SCA-002 is declined or deferred,
   the DEL-04-06 edits in this tranche must be re-cut before merge.
2. **Publication merge authorization.** This tranche's PR is human-gated;
   merge authorization is a separate owner act on the exact final branch
   HEAD. `self_merge: false`; no grant block is declared and none exists.
3. **Grant issuance (optional, owner-only).** GRANT-2026-07-29 is a
   candidate. It takes effect only on the owner's issuance token
   (`ISSUE GRANT-2026-07-29 cdd8844b — Ryan Tufts <date>`), which the
   supervising session presents against the file's SHA-256
   `cdd8844b42ca772aab96b5c942873eb4e7c957f0b262fba6daabc61834f2f38e`.
   Unissued, it binds nothing.

## What later phases consume

- Receipt 62 in `execution/_Coordination/LOOP_RECEIPTS.md` covers this
  tranche.
- The three routed M6 notices are the loops' coordination entry points;
  each loop repins/adopts/acknowledges (or declines) under its own
  instruments; stricter local merge discipline remains controlling until
  it does. M6 disposition: `routed` in the tranche manifest.
- The new `agents/AGENT_CHANGE.md` identity for downstream repins:
  SHA-256
  `f59e5455e1eeac687f69f091a74974fbfb2fb0a520fcb3bc7db8ab24529a4c77`.
- G4 `instruction-tranche-manifest/v1` now accepts an optional complete
  `m2_gate.merge_execution_grant` block (grant_record, granted_by,
  grant_date, expiry, approved_source_sha) as the registered home of the
  mandatory pre-merge pin; `self_merge: false` remains the default and
  `self_merge: true` without a complete block remains BLOCK.

## Remaining Step-4/5 work (not this run)

- Row 1: SOW-042 scope-ledger restatement — SCOPE_CHANGE sibling run
  (SCA-002), owner-gated.
- Export-package regeneration consuming post-merge bytes — next export
  release.
- Loop-side adoption/acknowledgment acts — each loop's own instruments.

## Post-commit record

- Tranche commit: recorded by the supervising session at fan-in (single
  commit on `gov/step4-operative-surfaces`; committed-HEAD whitespace
  validation run with
  `--base-ref ea3db3607fbcbb7ce5f65bab31268a7eca431adb`).
