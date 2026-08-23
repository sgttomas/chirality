# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0d (SCA-004 R3 transcription; Gate-5 application package drafting)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0d of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md`; the G0, R1, and R2 records are already transcribed in Receipts 114–116 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R3
ruling. Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R3 record is the owner's direction of record for this tranche.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `b32ceb130351c1dc3a8dbbcbf9311a4a73dc350e` (PR #626). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Brief.md` `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`; `Impact_Assessment.md` `ff370baaa72a871c2bf7f4c0ade0b41966f414ab8e3f1fb5ae1efe4ba91ed3d3`; `Amendment_Preview.md` `ff7743554270aee177feed4226a4fa35fd503ce34760f69644176878bcffdca4`; `Gate_3_Exact_Amendment.diff` `0724668f6fb85189f4c3ee142a21cef938c8dd47373be543d8b108c8e934637b`; `Gate_3_Validation.json` `dc5fe4355322a96b7da61606fff7d8dd51943a7d606f132966705bfb70b9f129`; `build_gate3_candidate.py` `246453b5335580372f69b4beff411d990de42537d1f8ba93248fe518c1205f26`; `validate_gate3_candidate.py` `5a394c7bb53abb7cd4e58e34b712ed50eb1aef00306c95730489f728114d2ee1`; `Propagation_Plan.md` `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`; `Amendment_Actions.csv` `4e623bcc5e69d056f71d9ed860ff729a0dfc9b8d8c635e7dd23b3c6b10d2871d`; `Decision_Log.md` `a35f2e13a70561b207092ff46d409525a2b7d4ebd14f3b938d06f253da5e4aec`; `Handoff_State.md` `41cadc01f17642d8f8318bc18f60c39adecac40253351f5ac97ca85888178cfd` (status `AWAITING_OWNER_GATE_3_APPROVAL`).
- The seven approved `Gate_3_Candidate/` files carry exactly the SHA-256 values listed in R3-A; `validate_gate3_candidate.py` reruns PASS 98/98 and leaves `Gate_3_Validation.json` byte-identical.
- Live accepted basis revision 1.2, unchanged and not written by this tranche: `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; `chirality_root_deliverable_register_v1_0.csv` `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`; `chirality_root_scope_ledger_v1_0.csv` `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`; `chirality_root_objective_register_v1_0.csv` `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55`; `chirality_root_prd_coverage_forward_v1_0.csv` `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84`; `chirality_root_trace_reverse_v1_0.csv` `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0`; `chirality_root_coverage_telemetry_v1_0.md` `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282`.
- `execution/_ScopeChange/_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (unchanged by this tranche).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live: OPEN=11, DEFERRED=8; untouched by this tranche).
- `execution/_Coordination/HANDOFF_STATE.md` `7b3a5e3f727b5f2d55cd39c3f1ef4ffbe4a8e6f87a10d09fbc4af65ce5864bdf`.
- Last Root receipt is 116. This tranche writes Receipt 117.
- `plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Transcribe the owner's Gate-3 and Gate-4 approvals (R3-A, R3-B) into the
SCA-004 instruments, and draft — never apply — the exact Gate-5 application
package that satisfies CONDITION R3-B-1: the application append bytes, the
resulting applied-state file identities, a deterministic validator, and the
Gate-5 execution brief. The owner approves the append bytes and authorizes
Gate-5 execution afterwards as separate acts. No decomposition truth,
register, pointer, folder, SOW, lifecycle, dependency, estimate, schedule,
tool, runtime, or App surface changes. Gate 5 is not executed. The ten
`HELD_UNAVAILABLE` bindings stay held.

## Nodes (N=1; Agent 2 instance with a sealed brief under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0D_2026-08-<DD>/instances/<NODE>/`)

### N1 — SCOPE_CHANGE: R3 transcription + Gate-5 application package (drafting only)
Write target: `execution/_ScopeChange/SCA-004_2026-08-22_1749/` only (SCA-002 convention: one evolving snapshot folder). The seven `Gate_3_Candidate/` files, `Gate_3_Exact_Amendment.diff`, `Gate_3_Validation.json`, `Amendment_Preview.md`, `Propagation_Plan.md`, and `Amendment_Actions.csv` are approved bytes and are **not rewritten**; if any would need to change, stop and report.
Pre-write: reverify every bound-input SHA above; if any differs, stop and report.
Produce:
- `Decision_Log.md` — append `G3-APPROVED-001` (R3-A verbatim, with the seven candidate SHAs, diff SHA, validation SHA, preview SHA, and basis SHA) and `G4-APPROVED-001` (R3-B verbatim including CONDITION R3-B-1); `Gate 3 (amendment)` → `APPROVED_BY_OWNER_R3-A`; `Gate 4 (propagation)` → `APPROVED_BY_OWNER_R3-B_WITH_CONDITION_R3-B-1`; `Gate 5 (application)` → `PENDING_OWNER_AUTHORIZATION`.
- `Gate_5_Slot_Inventory.md` — the exhaustive list of every slot in the seven approved candidate files whose text asserts candidate-only, not-approved, not-applied, projected, or pending-approval status (working-surface title, Revision line, Run/Amendment lines, status blockquote, `Revision / Date` telemetry cell, change-log entry; telemetry header/status lines and revision cell; every CSV cell that says "candidate"), each with file, exact locator (line or row/column), and before/after text. Slots are text-status only; no row, mapping, count, ID, or trace content is a slot.
- `Gate_5_Application_Append.diff` — one zero-context patch over the exact approved candidate bytes (apply-checkable with `git apply --unidiff-zero --check` against a copy of `Gate_3_Candidate/` placed at the live paths) that rewrites only the inventoried slots into applied-state wording in the SCA-002 form: working-surface title `(v1.3 — ACCEPTED CURRENT BASIS)`; status blockquote recording Gate 3 approved R3-A, Gate 4 approved R3-B with condition, Gate-5 executed under an authorization reference left `TBD`, Git effect `TBD` (D-GOV-34 backfill convention: filled by a later recorded act, never inferred), and the `_LATEST.md` pointer state stated as "pointer treatment pending its own authority" unless a pointer act is authorized at the same time; telemetry status `applied revision 1.3`; CSV candidate notes → applied notes. Nothing else changes.
- `Gate_5_Applied_Candidate/` — the seven resulting files (approved candidate + append), and `Gate_5_Applied_Preview.md` with a per-file table: approved-candidate SHA-256 → applied SHA-256, plus the slot-by-slot before/after text, and the explicit statement that counts (53 / PKG-02 12 / PKG-04 11 / 6 / 104 / 7), IDs, mappings, and traces are byte-identical to the approved candidate outside the inventoried slots.
- `validate_gate5_package.py` + `Gate_5_Validation.json` — deterministic, reproducible; checks must include: approved candidate SHAs unchanged; `Gate_3_Exact_Amendment.diff` still reproduces the approved candidate from the live 1.2 basis; `Gate_5_Application_Append.diff` applied to the approved candidate reproduces `Gate_5_Applied_Candidate/` exactly; every hunk of the append lies inside an inventoried slot (no other line or cell differs); CSV row counts, ID sets, `ParentPackageID` distribution, scope/objective mappings, and trace unit counts identical between approved and applied candidates; the 98 Gate-3 checks rerun PASS against the applied candidate (or an applied-state equivalent with the status checks inverted, stated explicitly); zero failures.
- `Gate_5_Brief.md` — the exact sequence for the later, separately authorized Gate-5 act: reverify the seven live 1.2 basis SHAs and the seven approved candidate SHAs; copy the seven approved candidate files to their live paths; apply `Gate_5_Application_Append.diff`; verify the seven live SHAs equal `Gate_5_Applied_Preview.md`; record before/after SHAs in `Gate_5_Application_Record.md`; then the closure lane of `Propagation_Plan.md` §6 items 1–6; return applied state to the owner for Gate-5 confirmation (§6 item 7). The brief performs no PREPARATION INIT, no `_LATEST.md` write, no `_STATUS.md`, SOW, dependency, estimate, schedule, graph, audit-snapshot, TM, tool, runtime, or App act; it names those as later acts per the approved plan.
- `Gate_5_Pointer_Candidate.md` — proposed exact replacement bytes for `execution/_ScopeChange/_LATEST.md` identifying revision 1.3 / SCA-004 as the accepted basis once Gate 5 is confirmed, with `TBD` Git slots; drafting only — the live pointer is not written and the candidate states that it requires its own owner approval (plan §7).
- `Handoff_State.md` — four-state form, status `AWAITING_OWNER_GATE_5_APPEND_APPROVAL`; blockers: owner approval of `Gate_5_Application_Append.diff` bytes; owner authorization of Gate-5 execution; pointer authority; TM-ROOT-106/122 unchanged as G1 blockers.
Check surface: `validate_gate3_candidate.py` PASS 98/98 with `Gate_3_Validation.json` byte-identical; `validate_gate5_package.py` PASS with zero failures and the check count recorded; the seven approved candidate files, `Gate_3_Exact_Amendment.diff`, `Amendment_Preview.md`, `Propagation_Plan.md`, and `Amendment_Actions.csv` byte-identical to their basis SHAs; live working surface, all six companion/trace/telemetry files, `_LATEST.md`, every `_STATUS.md`, and the TM register byte-identical; `git apply --unidiff-zero --check` of the append against a scratch copy of the approved candidate at the live paths passes; fresh review with zero actionable findings.
Report in the receipt (no register write): a Task Management candidate that `AGENT_SCOPE_CHANGE.md` Gate-4 propagation plans must include the application-append treatment so that applied surfaces never self-describe as candidates (owner-gated `agents/**` change; routed to TASK_MANAGEMENT triage, not acted on here).

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, the live decomposition working surface and all companion/trace/telemetry files, `execution/_ScopeChange/_LATEST.md`, any `_STATUS.md`, `execution/PKG-*/1_Working/**` folders (no INIT), SOWs, `_DEPENDENCIES.md`, estimates, schedules, `WORK_GRAPH.json`/`DAG.md` regeneration, audit snapshots, the Task Management register, `tools/**`, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface. The approved Gate-3/Gate-4 bytes named above are read-only.

## Failure rule
Unlimited repair with fresh re-review. If the node cannot complete, it
returns its handoff state with blockers instead of narrowing silently. Never
widen the write set; if a needed write falls outside it, report and stop.

## Closeout
One tranche, one branch `codex/root-v3-phase0d-2026-08-<DD>`, one PR to
`main`. Append Receipt 117 to `execution/_Coordination/LOOP_RECEIPTS.md`
after the fact, in-PR, with: this steer and
`plans/steers/chirality_app_v3_root_ruling_record_r3_2026-08-23.md` as
CHAT_TRANSCRIPTION (record both SHA-256 values); the node write set; every
cited SHA/commit; `Gate_3_Validation.json` and `Gate_5_Validation.json`
results and check counts; the per-file approved→applied SHA table; validator
outputs including the CI-form G4 output (expected: zero instruction-surface
paths); `execution/_Coordination/HANDOFF_STATE.md` updated. Run before
pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies before endorsement; approval of the append bytes and
authorization of Gate-5 execution return to the owner as separate acts
against the exact published bytes.
