# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0e (SCA-004 Gate-5 execution and closure lane)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0e of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`; the G0, R1, R2, and R3 records are already transcribed in Receipts 114–117 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R4
ruling. Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R4 record is the owner's direction of record for this tranche: R4-A approves
the append bytes, R4-B authorizes one Gate-5 execution, R4-C defers the
pointer.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `4fbbb57999f1acf390fc2218a78b1a30249fd600` (PR #628). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Gate_5_Application_Append.diff` `336405845dde5a3ae406b46c750c38a88c1b366f69bdaa74b4078679e04fe6a8`; `Gate_5_Applied_Preview.md` `eb4a9236e7b6d007ebf11aff75bc3e86884d7158d7b753933b3130d523423d03`; `Gate_5_Slot_Inventory.md` `79929dfd8a299904d95fa0ab83b7b044452528ecf6e39bc57717675e39928e22`; `Gate_5_Validation.json` `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`; `validate_gate5_package.py` `8dd6e92577fceba1693e6c1605c9863d33c97002ea47e36a3f05d724d7a157e3`; `Gate_5_Brief.md` `7f0ab64a16d70c7b48c7f51ed4bbfc3bbd5569bed3fdd05343de1ffe2b7d01de`; `Gate_5_Pointer_Candidate.md` `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`; `Decision_Log.md` `c0e45e18b06ee2f415552aee10c6053e5dd887649bb3dc5accf6411943a23375`; `Handoff_State.md` `86825f84d6c9e7c6b38efe98319b67fb000676f37027d0c89b666216c3ab1d12` (status `AWAITING_OWNER_GATE_5_APPEND_APPROVAL`); `Gate_3_Exact_Amendment.diff` `0724668f6fb85189f4c3ee142a21cef938c8dd47373be543d8b108c8e934637b`; `Propagation_Plan.md` `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`.
- The seven `Gate_3_Candidate/` files carry exactly the R3-A SHA-256 values; the seven `Gate_5_Applied_Candidate/` files carry exactly the R4-A applied identities.
- Live revision 1.2, to be replaced by this tranche and nothing else under `execution/_Decomposition/`: `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; `chirality_root_deliverable_register_v1_0.csv` `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`; `chirality_root_scope_ledger_v1_0.csv` `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`; `chirality_root_objective_register_v1_0.csv` `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55`; `chirality_root_prd_coverage_forward_v1_0.csv` `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84`; `chirality_root_trace_reverse_v1_0.csv` `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0`; `chirality_root_coverage_telemetry_v1_0.md` `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282`.
- `execution/_ScopeChange/_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (unchanged by this tranche; R4-C).
- Gate-1 `AUDIT_DECOMP` baseline `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP/coverage_summary.json` `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45` (preserved; the backcheck writes a new folder).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched by this tranche).
- `execution/_Coordination/HANDOFF_STATE.md` `7a88c6f5d8d36ec4242428cc1442ba483f17ca55508f8e6ba82f2ef1504be164`.
- Last Root receipt is 117. This tranche writes Receipt 118.
- `plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Execute SCA-004 Gate 5 exactly once, exactly as `Gate_5_Brief.md` steps 1–9
prescribe and R4-B authorizes: the seven live decomposition surfaces become
the R4-A applied identities; `Gate_5_Application_Record.md` records every
before/after SHA; the closure-validation lane of `Propagation_Plan.md` §6
items 1–6 runs and is recorded; the applied state returns to the owner for
Gate-5 confirmation. No pointer, folder, SOW, `_STATUS.md`, lifecycle,
dependency, estimate, schedule, graph, TM, tool, runtime, or App surface
changes. No hold is lifted; the ten `HELD_UNAVAILABLE` bindings stay held.

## Nodes (N=1; Agent 2 instance with a sealed brief under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0E_2026-08-<DD>/instances/<NODE>/`)

### N1 — SCOPE_CHANGE: Gate-5 application and closure lane
Write targets, exactly: the seven live files under `execution/_Decomposition/` named in the basis gate; `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md` (new); `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DECOMP_POST_GATE5/` (new folder for the post-application backcheck; the Gate-1 `Evidence/AUDIT_DECOMP/` baseline is not overwritten); `Decision_Log.md` and `Handoff_State.md` in the SCA folder. Every other SCA-004 file, including `Gate_3_Candidate/`, `Gate_5_Applied_Candidate/`, the append, preview, brief, inventory, validators, and validation JSONs, is approved bytes and is not rewritten.
Pre-write: reverify every bound-input SHA above and run `validate_gate5_package.py` fresh (PASS, zero failures, `Gate_5_Validation.json` byte-identical); if anything differs, stop and report — no partial application.
Sequence (the brief's steps, restated as check surfaces):
1. Copy the seven exact `Gate_3_Candidate/` files to their live paths; hash and require equality with the seven R3-A SHAs.
2. From repository root, `git apply --unidiff-zero --check` then `git apply --unidiff-zero` of `Gate_5_Application_Append.diff`; hash the seven live files and require exact equality with the R4-A applied identities (`546b6e4c…`, `2cdf1e68…`, `63e6fa6b…`, `b65da0f8…`, `9fcfa2a5…`, `750aed6c…`, `bdd6bc08…`). Any mismatch: revert the seven files to revision 1.2 bytes, stop, and report.
3. `Gate_5_Application_Record.md`: per-file before (1.2) → after (applied) SHA table; R4-A and R4-B references with the R4 record SHA; validator result; Git-effect slot `TBD` (D-GOV-34 backfill convention; never inferred); explicit statement that `_LATEST.md` is unchanged by R4-C.
4. Closure lane (`Propagation_Plan.md` §6 items 1–6), each recorded with its output: (1) applied live hashes reverified against R4-A; (2) applied-state Gate-3 equivalent via `validate_gate5_package.py` against the live files — PASS 98/98 (the protected Phase-0c `validate_gate3_candidate.py` is not run against the applied live state; say so); (3) post-application scoped `AUDIT_DECOMP` backcheck into `Evidence/AUDIT_DECOMP_POST_GATE5/`, compared to the Gate-1 baseline `coverage_summary.json` `2210e77f…`, expected applied topology 53 deliverables, PKG-02=12, PKG-04=11, packages=6, scope items=104, objectives=7, zero unmapped IN items, zero unmapped objectives, zero untraced reverse units; (4) `git diff --name-only` against the branch basis shows only the write targets above — no folder, SOW, `_STATUS.md`, or `_DEPENDENCIES.md` created or changed; (5) all ten DEL-02-06 bindings `HELD_UNAVAILABLE`, cited by file and line; (6) derivative disposition table: which derivatives are current, which are stale and await their later acts (PREPARATION INIT ×7, DEL-02-06 `_CONTEXT.md` edit list, dependency extraction, estimates, schedule, `WORK_GRAPH.json`/`DAG.md`, `AUDIT_DEP_CLOSURE`, pointer).
5. `Decision_Log.md`: append `G5-APPEND-APPROVED-001` (R4-A verbatim with the append and applied SHAs), `G5-AUTHORIZED-001` (R4-B verbatim), `G5-POINTER-DEFERRED-001` (R4-C verbatim), and `G5-EXECUTED-001` with the application-record SHA; `Gate 5 (application)` → `EXECUTED_AWAITING_OWNER_CONFIRMATION`.
6. `Handoff_State.md`: four-state form, status `AWAITING_OWNER_GATE_5_CONFIRMATION`; blockers: owner Gate-5 confirmation; pointer ruling (R4-C); Git-effect backfill after merge; the later propagation acts listed in item 4(6); TM-ROOT-106/122 unchanged as G1 blockers.
Check surface: the seven live SHAs equal R4-A exactly; `validate_gate5_package.py` applied-state PASS; backcheck counts as expected; `git diff --name-only origin/main..HEAD` ⊆ the write targets plus run tree, coordination handoff, and receipt; `_LATEST.md`, every `_STATUS.md`, every live folder, and the TM register byte-identical; fresh review with zero actionable findings. If any closure-lane item fails, do not revert the application silently: record the failure in the application record and handoff state, stop, and return the blocker — reversal is the owner's call.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, `execution/_ScopeChange/_LATEST.md`, any `_STATUS.md`, `execution/PKG-*/1_Working/**` folders (no INIT; no DEL-02-06 `_CONTEXT.md` edit yet), SOWs, `_DEPENDENCIES.md`, estimates, schedules, `WORK_GRAPH.json`/`DAG.md` regeneration, `AUDIT_DEP_CLOSURE`, the Gate-1 `Evidence/AUDIT_DECOMP/` baseline, the Task Management register, `tools/**`, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface. The approved SCA-004 bytes named above are read-only.

## Failure rule
Unlimited repair with fresh re-review for evidence and record writes. The
application itself (steps 1–2) is executed once against exact identities; a
mismatch reverts to revision 1.2 bytes and stops. Never widen the write set;
if a needed write falls outside it, report and stop.

## Closeout
One tranche, one branch `codex/root-v3-phase0e-2026-08-<DD>`, one PR to
`main`. Append Receipt 118 to `execution/_Coordination/LOOP_RECEIPTS.md`
after the fact, in-PR, with: this steer and
`plans/steers/chirality_app_v3_root_ruling_record_r4_2026-08-23.md` as
CHAT_TRANSCRIPTION (record both SHA-256 values); the write set; every cited
SHA/commit; the per-file before→after live SHA table; `Gate_5_Validation.json`
and backcheck results; validator outputs including the CI-form G4 output
(expected: zero instruction-surface paths); `execution/_Coordination/HANDOFF_STATE.md`
updated. Run before pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies the applied live bytes against R4-A before endorsement; Gate-5
confirmation and the pointer ruling return to the owner as separate acts, and
the Git-effect slots are backfilled by a later recorded act after merge.
