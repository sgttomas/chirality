# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0f (SCA-004 Gate-5 second attempt: applied validator, scratch rehearsal, byte-copy execution, closure lane)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0f of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`; the G0 and R1–R4 records are already transcribed in Receipts 114–118 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R5
ruling, after the Phase-0e attempt stopped at its identity fence (Receipt
118). Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R5 record is the owner's direction of record for this tranche; R4-A and R4-C
stand.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `3bb3d50550b9fbdbdea67f41fa2ed108024cb43b` (PR #630). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Gate_5_Application_Append.diff` `336405845dde5a3ae406b46c750c38a88c1b366f69bdaa74b4078679e04fe6a8`; `Gate_5_Applied_Preview.md` `eb4a9236e7b6d007ebf11aff75bc3e86884d7158d7b753933b3130d523423d03`; `Gate_5_Validation.json` `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`; `validate_gate5_package.py` `8dd6e92577fceba1693e6c1605c9863d33c97002ea47e36a3f05d724d7a157e3`; `Gate_5_Brief.md` `7f0ab64a16d70c7b48c7f51ed4bbfc3bbd5569bed3fdd05343de1ffe2b7d01de`; `Gate_5_Pointer_Candidate.md` `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`; `Decision_Log.md` `c0e45e18b06ee2f415552aee10c6053e5dd887649bb3dc5accf6411943a23375`; `Handoff_State.md` `86825f84d6c9e7c6b38efe98319b67fb000676f37027d0c89b666216c3ab1d12`; `Propagation_Plan.md` `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`.
- The seven `Gate_3_Candidate/` files carry exactly the R3-A SHA-256 values (`0696190d…`, `2cdf1e68…`, `54287bad…`, `b65da0f8…`, `9fcfa2a5…`, `750aed6c…`, `316185be…`); the seven `Gate_5_Applied_Candidate/` files carry exactly the R4-A applied identities (`546b6e4c…`, `2cdf1e68…`, `63e6fa6b…`, `b65da0f8…`, `9fcfa2a5…`, `750aed6c…`, `bdd6bc08…`; full values in the R4 record).
- Live revision 1.2, restored after Phase 0e and to be replaced by this tranche: `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; `chirality_root_deliverable_register_v1_0.csv` `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`; `chirality_root_scope_ledger_v1_0.csv` `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`; `chirality_root_objective_register_v1_0.csv` `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55`; `chirality_root_prd_coverage_forward_v1_0.csv` `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84`; `chirality_root_trace_reverse_v1_0.csv` `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0`; `chirality_root_coverage_telemetry_v1_0.md` `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282`.
- `execution/_ScopeChange/_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (unchanged by this tranche; R4-C).
- Gate-1 `AUDIT_DECOMP` baseline `Evidence/AUDIT_DECOMP/coverage_summary.json` `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45` (preserved).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched).
- `execution/_Coordination/HANDOFF_STATE.md` `16fe2090fd96e2a2033e4cfd48806cd233296e0a336632b4bdd1f9710608b7e9`.
- Last Root receipt is 118. This tranche writes Receipt 119.
- `plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Execute SCA-004 Gate 5 exactly once under R5-A, with the materialization
method corrected to byte copy, a post-application validator added first, and
a recorded scratch rehearsal gating the live act. The seven live
decomposition surfaces become the R4-A applied identities;
`Gate_5_Application_Record.md` records every before/after SHA; the closure
lane of `Propagation_Plan.md` §6 items 1–6 runs and is recorded; the applied
state returns to the owner for Gate-5 confirmation. No pointer, folder, SOW,
`_STATUS.md`, lifecycle, dependency, estimate, schedule, graph, TM, tool,
runtime, or App surface changes. No hold is lifted.

## Nodes (N=1, two ordered stages; Agent 2 instance with a sealed brief under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0F_2026-08-<DD>/instances/<NODE>/`)

The sealed brief must name the byte-level method verbatim from R5-A (1) and
state that patch editing, editor tools, `apply_patch`, or any re-expression
of the approved diffs is forbidden for the seven live writes. The Agent 2 must
have shell access for `cp`, `shasum`, and `git apply`; if it does not, stop
before any write and report.

### N1 — SCOPE_CHANGE: Gate-5 applied validator, rehearsal, execution, closure lane
Write targets, exactly: `execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py` (new), `…/Gate_5_Rehearsal_Record.md` (new), `…/Gate_5_Applied_Validation.json` (new); the seven live files under `execution/_Decomposition/`; `…/Gate_5_Application_Record.md` (new); `…/Evidence/AUDIT_DECOMP_POST_GATE5/` (new folder); `…/Decision_Log.md` and `…/Handoff_State.md`. Every other SCA-004 file is approved or published bytes and is not rewritten.
Pre-write: reverify every bound-input SHA above; fresh `validate_gate5_package.py` PASS 64/64 with `Gate_5_Validation.json` byte-identical; if anything differs, stop and report.

Stage A — validator and rehearsal (no live write):
1. `validate_gate5_applied.py` — deterministic, reproducible, writes `Gate_5_Applied_Validation.json`; checks, at minimum: the seven live files equal the R4-A applied identities byte-for-byte; applied-state structural checks on the live files — 53 deliverables, PKG-02 12, PKG-04 11, packages 6, scope items 104, objectives 7, deliverable-ID set, scope/objective mappings, forward 85 rows, reverse 59 rows, all identical to `Gate_5_Applied_Candidate/`; every new row parented and mapped; every objective supported; zero unmapped IN items; `Gate_3_Candidate/`, `Gate_5_Applied_Candidate/`, the append, preview, brief, inventory, and `validate_gate5_package.py` unchanged at their basis SHAs; `_LATEST.md` unchanged; no `execution/PKG-*/1_Working/DEL-02-07..12` or `DEL-04-11` folder exists; no `_STATUS.md`, SOW, or `_DEPENDENCIES.md` changed versus the branch basis. It must not depend on `live_basis_untouched` or `candidate_ids_absent_from_live_register`. Record its check count.
2. Rehearsal in a scratch worktree outside the governed checkout (e.g., `git worktree add --detach <scratch> HEAD`): `/bin/cp` the seven `Gate_3_Candidate/` files to the scratch live paths → `shasum -a 256` all seven (require R3-A) → `git apply --unidiff-zero --check` then `git apply --unidiff-zero` of the append from the scratch root → `shasum -a 256` all seven (require R4-A) → run `validate_gate5_applied.py` against the scratch (require PASS, zero failures) → remove the scratch worktree. Record every command and every observed hash in `Gate_5_Rehearsal_Record.md`. The governed checkout's seven live files remain at revision 1.2 through Stage A; verify and record that.
Gate between stages: Stage A passes only if intermediate = R3-A (7/7), final = R4-A (7/7), and the applied validator is PASS with zero failures. If not, stop here: no live write; record the blocker in the rehearsal record and Handoff_State; close out with the receipt.

Stage B — the live act (once):
3. `/bin/cp` the seven `Gate_3_Candidate/` files to their live paths; `shasum -a 256`; require R3-A 7/7. On any mismatch: restore the seven revision-1.2 bytes (`git checkout -- execution/_Decomposition/`), verify, stop, report.
4. From repository root: `git apply --unidiff-zero --check` then `git apply --unidiff-zero` of `Gate_5_Application_Append.diff`; `shasum -a 256`; require R4-A 7/7. On any mismatch: restore, verify, stop, report.
5. `Gate_5_Application_Record.md`: per-file before (1.2) → after (applied) SHA table; R4-A, R4-B, R5-A references with the R4 and R5 record SHAs; the exact commands used; rehearsal-record SHA; validator result; Git-effect slot `TBD` (never inferred); statement that `_LATEST.md` is unchanged by R4-C.
6. Closure lane (`Propagation_Plan.md` §6 items 1–6), each recorded with its output: (1) applied live hashes reverified against R4-A; (2) `validate_gate5_applied.py` against the live files — PASS, zero failures (the pre-application `validate_gate5_package.py` and the protected Phase-0c `validate_gate3_candidate.py` are not run against the applied live state; say so and why); (3) post-application scoped `AUDIT_DECOMP` backcheck into `Evidence/AUDIT_DECOMP_POST_GATE5/`, compared to the Gate-1 baseline `2210e77f…`; expected 53 / PKG-02 12 / PKG-04 11 / 6 / 104 / 7, zero unmapped IN items, zero unmapped objectives, zero untraced reverse units; (4) `git diff --name-only` against the branch basis ⊆ the write targets above; (5) all ten DEL-02-06 bindings `HELD_UNAVAILABLE`, cited by file and line; (6) derivative disposition table (current vs stale: PREPARATION INIT ×7, DEL-02-06 `_CONTEXT.md` edit list, dependency extraction, estimates, schedule, `WORK_GRAPH.json`/`DAG.md`, `AUDIT_DEP_CLOSURE`, pointer).
7. `Decision_Log.md`: append `G5-APPEND-APPROVED-001` (R4-A verbatim), `G5-AUTHORIZED-001` (R4-B verbatim), `G5-POINTER-DEFERRED-001` (R4-C verbatim), `G5-ATTEMPT-1-STOPPED-001` (Phase-0e stop, citing Receipt 118 and the return's observed identities), `G5-REAUTHORIZED-001` (R5-A verbatim), and `G5-EXECUTED-001` with the application-record and rehearsal-record SHAs; `Gate 5 (application)` → `EXECUTED_AWAITING_OWNER_CONFIRMATION`.
8. `Handoff_State.md`: status `AWAITING_OWNER_GATE_5_CONFIRMATION`; blockers: owner confirmation; pointer ruling (R4-C); Git-effect backfill after merge; later propagation acts per item 6(6); TM-ROOT-106/122 unchanged as G1 blockers.
Check surface: Stage A rehearsal record complete with 7/7 + 7/7 + PASS; the seven live SHAs equal R4-A exactly; `validate_gate5_applied.py` PASS on live; backcheck counts as expected; `git diff --name-only origin/main..HEAD` ⊆ write targets plus run tree, coordination handoff, and receipt; `_LATEST.md`, every `_STATUS.md`, every live folder, and the TM register byte-identical; fresh review with zero actionable findings. A closure-lane failure after a successful Stage B is recorded and returned, never silently reverted.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, `execution/_ScopeChange/_LATEST.md`, any `_STATUS.md`, `execution/PKG-*/1_Working/**` folders (no INIT; no DEL-02-06 `_CONTEXT.md` edit yet), SOWs, `_DEPENDENCIES.md`, estimates, schedules, `WORK_GRAPH.json`/`DAG.md` regeneration, `AUDIT_DEP_CLOSURE`, the Gate-1 `Evidence/AUDIT_DECOMP/` baseline, the Task Management register, `tools/**`, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface. Approved and published SCA-004 bytes are read-only; the seven live files are writable only by Stage B's exact method.

## Failure rule
Unlimited repair with fresh re-review for Stage A artifacts and for evidence
and record writes. Stage B is executed once; an identity mismatch restores
revision 1.2 and stops. Never widen the write set; if a needed write falls
outside it, report and stop.

## Closeout
One tranche, one branch `codex/root-v3-phase0f-2026-08-<DD>`, one PR to
`main`. Append Receipt 119 to `execution/_Coordination/LOOP_RECEIPTS.md`
after the fact, in-PR, with: this steer and
`plans/steers/chirality_app_v3_root_ruling_record_r5_2026-08-23.md` as
CHAT_TRANSCRIPTION (record both SHA-256 values); the write set; every cited
SHA/commit; the rehearsal hashes; the per-file before→after live SHA table;
`Gate_5_Applied_Validation.json` and backcheck results; validator outputs
including the CI-form G4 output (expected: zero instruction-surface paths);
`execution/_Coordination/HANDOFF_STATE.md` updated. Run before pushing:
`validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies the applied live bytes against R4-A before endorsement; Gate-5
confirmation and the pointer ruling return to the owner as separate acts, and
the Git-effect slots are backfilled by a later recorded act after merge.
