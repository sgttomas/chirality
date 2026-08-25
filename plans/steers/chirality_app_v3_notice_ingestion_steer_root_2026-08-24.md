# ROOT LOOP STEER — v3 notice ingestion: record the routed SCA-APP-008 Gate-5 notice — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (repository root `execution/`). The loop's instruments govern; this steer
> directs one bounded tranche under them. Authorizing ruling: R11
> (`chirality_app_v3_root_ruling_record_r11_2026-08-24.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together). This
> steer is the contract for one bounded act. Read it in full before any
> write.

## Basis gate (check before any write; stop and report if any line fails)

1. `origin/main` contains merge commits
   `d5e40b3c25fe527919f1d2d2a31ea97ce2835795` (PR #662, Gate 5),
   `4251530ec8a5d5b7abfc035cbdde63dab7fa80f3` (PR #665, pointer act), and
   `f60f3e42d53aaaae64858736ff7caae0c492d04a` (PR #666, R9 transcription).
   Work on a fresh branch `codex/root-notice-ingestion-2026-08-<DD>` from
   current `origin/main`. Record the exact basis commit.
2. Verify the routed notice source at
   `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/NOTICE_TO_ROOT_READY_TO_ROUTE.md`,
   SHA-256
   `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`.
   Reading this App path is authorized for verification and copying only; no
   App path may be written.
3. Verify the ratified Root contract `docs/CONTRACT.md`, SHA-256
   `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`.
4. Verify that
   `execution/_Coordination/NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md`
   does not yet exist.
5. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record R11 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.
6. If any check fails, stop and report. Do not repair, regenerate, or
   substitute.

## Authority context

A7-B produced the regenerated notice without routing it. R11-A routes the
exact bytes and authorizes this recording tranche. The notice is cross-loop
coordination, not authority: recording it adopts nothing, lifts no blocker,
and changes no Root contract, register, schedule, or lifecycle state. R11
supplies currency for three events completed after the notice bytes were
frozen (the Gate-5 merge, the pointer application, and the R9
transcription); record that currency in the receipt, not by editing the
notice.

## N1 — record the routed notice

1. Copy the exact source bytes to
   `execution/_Coordination/NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md`.
   The new file must be byte-identical to the source: SHA-256
   `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`.
   Copy the bytes; do not re-type, reflow, or annotate them.
2. Run a recorded Root/App contract-drift check as run evidence (not as a
   notice edit): verify that the ratified Root contract identity the notice
   cites matches the live `docs/CONTRACT.md` identity in the basis gate, and
   record whether any exact drift exists between the notice's Root-facing
   claims (single live control socket; exclusive daemon ownership of
   `{userData}/runtime` under K-RUNTIME-1; the design-gated
   DEL-02-07/WP-03 supervisor-socket pathway) and the live Root contract
   rows. If any exact divergence is found, record it precisely and stop for
   owner routing; repair nothing.
3. If the loop's instruments maintain a notice ledger or Task Management
   linkage for inbound notices, apply exactly the recording those instruments
   require for a received coordination notice, and nothing more. Adoption,
   amendment, or declination of the notice's content remains a separate Root
   act and is not performed in this tranche.

## Post-write validation

- Run candidate whitespace against the recorded basis commit; it must pass.
- Run CI-form G4 (this tranche touches no instruction surface, so no covering
  manifest is expected — if G4 demands one, stop and report).
- Confirm with `git status`/diff that exactly the write set below changed and
  nothing else.

## Receipt and return

- Append Receipt 128 to `execution/_Coordination/LOOP_RECEIPTS.md` following
  the ledger's receipt contract, incorporating this steer and R11 by
  immutable path and SHA-256, recording the routed-notice identity, the
  currency events named in R11, and the drift-check result.
- Record run evidence under
  `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-08-<DD>/`.
- Commit, push the branch, and open one unlabeled PR against `main`. Do not
  merge. The owner decides the merge separately.

## Write set, exactly

- The one new byte-identical notice copy named in N1.
- Any ledger or register row that the loop's own instruments require for
  recording a received coordination notice, applied exactly as those
  instruments direct (if none applies, write none).
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 128).
- New files strictly inside
  `execution/_Coordination/AgentRuns/ROOT_NOTICE_INGESTION_2026-08-<DD>/`.

Not selectable: `docs/CONTRACT.md` and every other root `docs/**` file; every
`execution/_ScopeChange/` snapshot file; any SOW, `_CONTEXT.md`,
`_STATUS.md`, or lifecycle file; `agents/**`, `tools/**`, `AGENTS.md`,
`exports/**`, `plans/**`, `skills/**`, `runtime/**`; anything under
`projects/**` (read-only verification of the notice source excepted) or
`_DomainEngines/**`.

## Sync rule

If `origin/main` advances mid-run, the standing routine-sync authorization
recorded in Receipt 125 permits one non-rewriting sync; record it, and stop
fail-closed if the sync changes any identity named in the basis gate.

## Rollback and abort

This tranche adds files and permitted ledger rows only. Any validation
failure, identity disagreement, drift finding, or unexpected write reverts
the additions on the branch (or abandons the branch), verifies that every
pre-existing surface remains byte-identical to the basis, and stops with a
report. A stop-and-report is a compliant outcome of this steer, not a
failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set for any reason; if the act appears to require a
write outside the set, stop and report — the owner decides. No authority is
inferred from this steer beyond the recording it names.
