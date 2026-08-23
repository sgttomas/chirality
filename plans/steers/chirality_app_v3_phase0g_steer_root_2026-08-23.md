# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0g (SCA-004 closure: R6 transcription, pointer application, Git-effect backfill)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0g of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md`; the G0 and R1–R5 records are already transcribed in Receipts 114–119 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R6
ruling. Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R6 record is the owner's direction of record for this tranche: R6-A confirms
Gate 5, R6-B approves the pointer with three named fills, R6-C authorizes the
Git-effect backfill.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `6d4438d8d3a580b65d6d50ad497dadfe07f177f2` (PR #633). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- The seven live files under `execution/_Decomposition/` carry exactly the R4-A applied identities (`546b6e4c…`, `2cdf1e68…`, `63e6fa6b…`, `b65da0f8…`, `9fcfa2a5…`, `750aed6c…`, `bdd6bc08…`; full values in the R4 record).
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Decision_Log.md` `90aa5da58be6ac97a7eec60762ac9f685d275dd80caaf694e7795496a1d5d0b1`; `Handoff_State.md` `c99e7ea86d636577c329920cbb8e6d472d67996b25a2714a203d45b1e10f9d0d` (status `AWAITING_OWNER_GATE_5_CONFIRMATION`); `Gate_5_Application_Record.md` `31207f122e9d64b4734a701cae364b2456df65d0605b2b1d0c6880ce5595760a`; `Gate_5_Rehearsal_Record.md` `ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532`; `Gate_5_Applied_Validation.json` `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`; `validate_gate5_applied.py` `281cfa29f66cf73dc3ab28c85029386e940f3109807862fbb18ae4f86036f63b`; `Gate_5_Pointer_Candidate.md` `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`; backcheck `Evidence/AUDIT_DECOMP_POST_GATE5/coverage_summary.json` `70ed91a848c762d9afb778423220c53408e1e4d2273a4a8aa7d5d81fd25359e9`.
- `execution/_ScopeChange/_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (replaced by this tranche under R6-B).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched).
- `execution/_Coordination/HANDOFF_STATE.md` `6fa6c9f5b19b81ea6fc0a1f5abfc693b821abc8b46d1890c6efe662f0aa28db1`.
- Last Root receipt is 119. This tranche writes Receipt 120.
- `plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Close SCA-004: transcribe R6, apply the owner-approved `_LATEST.md` pointer
with exactly the three named fills, backfill the Git-effect and reference
slots from the recorded chain, and set the SCA handoff to closed-confirmed.
No decomposition byte changes (the seven live files are read-only in this
tranche). No folder, SOW, `_STATUS.md`, lifecycle, dependency, estimate,
schedule, graph, TM, tool, runtime, or App surface changes. No hold is
lifted.

## Nodes (N=1; Agent 2 instance with a sealed brief under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0G_2026-08-<DD>/instances/<NODE>/`)

### N1 — SCOPE_CHANGE: R6 transcription, pointer application, backfill
Write targets, exactly: `execution/_ScopeChange/_LATEST.md`; `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md`, `…/Handoff_State.md`, `…/Gate_5_Application_Record.md` (slot fills only). Everything else in the SCA folder and the live decomposition is read-only.
Pre-write: reverify every bound-input SHA above; rerun `validate_gate5_applied.py` (PASS, zero failures; the JSON's recorded absolute root path may differ and is not a drift signal — leave the committed JSON unchanged); if anything else differs, stop and report.
Produce:
1. `_LATEST.md` — the exact fenced replacement block from `Gate_5_Pointer_Candidate.md`, with exactly three fills per R6-B: application-append approval reference → R4-A (record SHA `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a`); Gate-5 confirmation reference → R6-A (record SHA of the pasted R6 file); Git effect → merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2` (content `4ad3fea7ef9e397852913c08e533e1846e264134`, PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`). Show in the receipt a diff of the final pointer against the candidate's fenced block proving only those slots differ.
2. `Gate_5_Application_Record.md` — fill the `TBD` Git-effect and reference slots only, per R6-C, with the values above plus R4-B, R5-A, R6-A references; one-line diffs in the receipt.
3. `Decision_Log.md` — append `G5-CONFIRMED-001` (R6-A verbatim), `G5-POINTER-APPLIED-001` (R6-B verbatim with the final pointer SHA-256), `G5-BACKFILL-001` (R6-C verbatim); `Gate 5 (application)` → `CONFIRMED_BY_OWNER_R6-A`; fill its `TBD` slots per R6-C.
4. `Handoff_State.md` — four-state form, status `CLOSED_CONFIRMED_PROPAGATION_PENDING`; remaining work: the Propagation_Plan later acts (PREPARATION INIT ×7, DEL-02-06 `_CONTEXT.md` edit list, dependency extraction, estimates, schedule, `WORK_GRAPH.json`/`DAG.md`, `AUDIT_DEP_CLOSURE`); blockers: TM-ROOT-106/122 unchanged as G1 blockers; ten holds held.
Check surface: the seven live decomposition files and every other SCA-004 file byte-identical to their basis SHAs except the four write targets; the final `_LATEST.md` differs from the candidate's fenced block only at the three named slots; `validate_gate5_applied.py` PASS; every fill traceable to a recorded act named in R6; fresh review with zero actionable findings.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, the seven live decomposition files, all other SCA-004 files (including `Gate_3_Candidate/`, `Gate_5_Applied_Candidate/`, validators, validation JSONs, rehearsal record, pointer candidate), any `_STATUS.md`, `execution/PKG-*/1_Working/**` folders (no INIT), SOWs, `_DEPENDENCIES.md`, estimates, schedules, `WORK_GRAPH.json`/`DAG.md`, audit snapshots, the Task Management register, `tools/**`, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface.

## Failure rule
Unlimited repair with fresh re-review. Never widen the write set; if a needed
write falls outside it, report and stop.

## Closeout
One tranche, one branch `codex/root-v3-phase0g-2026-08-<DD>`, one PR to
`main`. Append Receipt 120 to `execution/_Coordination/LOOP_RECEIPTS.md`
after the fact, in-PR, with: this steer and
`plans/steers/chirality_app_v3_root_ruling_record_r6_2026-08-23.md` as
CHAT_TRANSCRIPTION (record both SHA-256 values); the write set; every cited
SHA/commit; the pointer-vs-candidate diff; the one-line backfill diffs;
validator outputs including the CI-form G4 output (expected: zero
instruction-surface paths); `execution/_Coordination/HANDOFF_STATE.md`
updated. Run before pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies the final pointer and backfill diffs before endorsement.
