# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0c (SCA-004 Gate 3 + Gate 4 drafting; D-GOV-34/35 SHA backfill)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0c of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md`; the G0 and R1 records are already transcribed in Receipts 114 and 115 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R2
ruling. Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R2 record is the owner's direction of record for N1; N2 is routine
record-keeping the owner authorizes by carrying this steer.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `d6861ae8251e2a81078577d4496e949735ff199d` (PR #623). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3` (post D-GOV-35 application).
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Brief.md` `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`; `Impact_Assessment.md` `ff370baaa72a871c2bf7f4c0ade0b41966f414ab8e3f1fb5ae1efe4ba91ed3d3`; `Decision_Log.md` `bfc184ff50af1f2ba9b9d18ab9d035f9abbaaadd41eae9e99660fcbb51f494dc`; `Handoff_State.md` `971c63bbda66c420f3ffaf581967a9675ae82260a081e3caaaa373cb73e4947c`; `Parsed_Actions.csv` `a89b77dc1ce478f7ea5bbc3ebb12706d69e93876e6a7f4cca0cfd5ea5a9e738b`; `WORK_GRAPH.json` `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`; `Evidence/AUDIT_DECOMP/coverage_summary.json` `2210e77f989f29c11e005d7fe89944e2e0f0fe265e0a514f53042aaa89de9e45`.
- Bound decomposition inputs (the Gate-2 assessment's "reverify before Gate-3 drafting" set): `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` (revision 1.2); `chirality_root_deliverable_register_v1_0.csv` `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`; `chirality_root_scope_ledger_v1_0.csv` `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`; `chirality_root_objective_register_v1_0.csv` `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55`; `chirality_root_prd_coverage_forward_v1_0.csv` `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84`; `chirality_root_trace_reverse_v1_0.csv` `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0`; `chirality_root_coverage_telemetry_v1_0.md` `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282`.
- `execution/_ScopeChange/_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (unchanged by this tranche).
- Candidate IDs `DEL-02-07`..`DEL-02-12` and `DEL-04-11` occur in no live register row and no live folder.
- `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` `a21ba1fe6cc7277384b90755d9f925d61990ce7bdbee3794ce06b271a34fccc2` (CandidateSHA/PublicationSHA/EffectiveSHA `TBD`); `D-GOV-34_change_clean_basis_lane_routine.md` `99180dc091ab4b425b9bd8ccf15d7bbaf7527d33aec90ffa41153abb7048faf1` (same slots `TBD`).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live: OPEN=11, DEFERRED=8; untouched by this tranche).
- Last Root receipt is 115. This tranche writes Receipt 116.
- `plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Draft — never apply — the exact SCA-004 Gate-3 amendment candidate and the
Gate-4 propagation plan so the owner can approve exact bytes; and backfill the
D-GOV-34 and D-GOV-35 decision records' Git-act SHA slots. No decomposition
truth, register, pointer, folder, SOW, lifecycle, dependency, estimate,
schedule, tool, runtime, or App surface changes. Gate 5 is not executed. The
ten `HELD_UNAVAILABLE` bindings stay held.

## Nodes (N=2, write-disjoint; Agent 2 instances with sealed briefs under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0C_2026-08-<DD>/instances/<NODE>/`)

### N1 — SCOPE_CHANGE: SCA-004 Gate 3 exact candidate + Gate 4 propagation plan (drafting only)
Write target: `execution/_ScopeChange/SCA-004_2026-08-22_1749/` only (SCA-002 convention: one evolving snapshot folder).
Pre-write: reverify every bound-input SHA above; if any differs, stop and report (do not redraft on drifted inputs). Rerun the scoped `AUDIT_DECOMP` baseline only if an input drifted.
Produce, in the SCA-002 form:
- `Gate_3_Candidate/` — exact candidate copies of the working surface and the three companion registers (deliverable, scope ledger, objective), plus recomputed forward trace, reverse trace, and telemetry, for all eight accepted actions: DEL-02-06 narrowed to the standing integration/release-assurance carrier (SOW-104 and OBJ-001/002/004/007 continuity explicit; REQ-027 untouched); DEL-02-07..12 under PKG-02 and DEL-04-11 (`TEST_SUITE`) under PKG-04, each with name, description, Type, Context Envelope, anticipated artifacts, objective set, and write locus; exact SOW-104 remapping; the exact SOW-041/SOW-053 allocation decision for DEL-04-11; count parity 46→53 deliverables, PKG-02 6→12, PKG-04 10→11, packages 6, scope items 104, objectives 7.
- `Gate_3_Exact_Amendment.diff` — the full diff from the bound inputs to the candidate.
- `Amendment_Preview.md` — frontmatter (`gate: 3`, `status: awaiting_gate_3_approval`, `accepted_basis` revision 1.2 at its SHA), diff-style sections per `AGENT_SCOPE_CHANGE.md` Gate 3 (change-register entry; Deliverables before→after; Scope Ledger; objective mappings; coverage/telemetry recompute; derivative classification), ending with the Gate-3 question.
- `build_gate3_candidate.py`, `validate_gate3_candidate.py`, `Gate_3_Validation.json` — deterministic, reproducible; checks must include: candidate IDs collision-free and unmaterialized; every new row parented (PKG-02/PKG-04 only); package discipline and artifact-kind granularity preserved; zero IN scope items without mapping; zero objectives without support; every new deliverable mapped to ≥1 objective and ≥1 scope item; DEL-02-06 retains SOW-104 and its four objectives; forward/reverse trace consistent with registers; telemetry counts equal the projected counts; `_LATEST.md` untouched.
- `Propagation_Plan.md` + `Amendment_Actions.csv` (Gate 4, limited to the approved write scope): PREPARATION INIT briefs for the seven new folders (`_CONTEXT.md`, `_STATUS.md` `OPEN`, `_REFERENCES.md`, `_DEPENDENCIES.md`); DEL-02-06 `_CONTEXT.md` edit list; dependency extraction, estimate snapshot, and scheduling advisories; graph re-derivation + AUDIT_DEP_CLOSURE rerun after folders are live; post-application AUDIT_DECOMP backcheck against the Gate-1 baseline; the closure-validation lane kept separate from Gate-5 writes; `_LATEST.md` pointer treatment stated as requiring its own accepted authority.
- `Decision_Log.md` — append `G2-ACCEPTED-001` (R2-A verbatim with the three subject SHAs), `Gate 3 (amendment)` → `PENDING_OWNER_APPROVAL`, `Gate 4 (propagation)` → `PENDING_OWNER_APPROVAL`.
- `Handoff_State.md` — four-state form, status `AWAITING_OWNER_GATE_3_APPROVAL`; blockers updated.
Check surface: `validate_gate3_candidate.py` PASS with zero failures and the check count recorded; live working surface, all six companion/trace/telemetry files, `_LATEST.md`, every `_STATUS.md`, and `Brief.md`/`Gate_1_Validation.md`/`Parsed_Actions.csv`/`WORK_GRAPH.json`/`DAG.md` byte-identical to the basis SHAs; no folder under `execution/PKG-*/1_Working/` created; Gate 5 not executed.

### N2 — Decision-record SHA backfill (HELPS_HUMANS lane): D-GOV-34 and D-GOV-35
Write targets, exactly: `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md`, `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md`, the two records' rows in `docs/governance_harness/_DECISIONS/_REGISTER.md` if they carry SHA or status text, and one new live manifest `docs/governance_harness/tranche_manifests/ROOT-DGOV34-DGOV35-SHA-BACKFILL-2026-08-<DD>.yaml` (schema v1; basis = current `main`; `instruction_surface_paths` = the files this node changes plus the manifest; `m2_gate` human-gated-pr, `self_merge: false`, authorization = this steer section verbatim; `m6_notice: pending`, `routed_to: []`; `derivative_disposition: deferred` for `exports/chirality-app/**`).
Values: D-GOV-35 `CandidateSHA` `294e846bc762b96ac780d49f0137f61eb4dde779` (N1 commit of PR #622), `PublicationSHA` `ade6ecf33d4e10dab1441aeedb240061e140ff1b` (PR #622 head), `EffectiveSHA` `8deca1489a3e5921288f71d4960d555e183a6f3f` (merge of PR #622); status line → `RULED — APPLIED 2026-08-22; EFFECTIVE 8deca1489…`. D-GOV-34: derive the three SHAs from Receipt 113/114 and the `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21` run's publication evidence, citing the receipt lines; if any slot cannot be established from recorded evidence, leave it `TBD` and say so — do not infer.
Check surface: each record changes only its declared SHA/status slots (show as one-line diffs); **G4 in the CI form** `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` PASS; `validate_agent_instructions.py`, `validate_instruction_entrypoints.py` pass; `AGENTS.md` and `agents/**` untouched; `validate_candidate_whitespace.py --base-ref origin/main` clean.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**` beyond N2's named files, the live decomposition working surface and all companion/trace/telemetry files, `execution/_ScopeChange/_LATEST.md`, any `_STATUS.md`, `execution/PKG-*/1_Working/**` (no new folders), `execution/_Coordination/_TaskManagement/REGISTER.csv` (candidates to a harvest file only), `runtime/**`, `projects/**`, `plans/**`, `tools/**`, `.github/**`, `exports/**`. No Gate 5, no PREPARATION dispatch, no SOW creation, no spike, no artifact download (C1 not granted), no pin change (B4), no sync/rebase without owner authorization, no merge.

## Failure rule
Unlimited repair with fresh re-review per node. A node that cannot complete
returns its handoff state with blockers instead of narrowing silently. Never
widen a node's write set; if a needed write falls outside it, report and stop
that node.

## Closeout
One tranche, one branch `codex/root-v3-phase0c-2026-08-<DD>`, one PR to
`main`, commits in order N1 → N2. Append Receipt 116 to
`execution/_Coordination/LOOP_RECEIPTS.md` after the fact, in-PR, with: this
steer and `plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md`
as CHAT_TRANSCRIPTION (record its SHA-256); per-node write sets; every cited
SHA/commit; `Gate_3_Validation.json` result and check count; validator outputs
including the CI-form G4 output; `execution/_Coordination/HANDOFF_STATE.md`
updated. Run before pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies before endorsement; Gate 3 and Gate 4 approvals return to the
owner as separate acts against the exact published bytes.
