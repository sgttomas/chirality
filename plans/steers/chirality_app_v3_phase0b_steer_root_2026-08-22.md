# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0b (D-GOV-35 application, SCA-004 Gate 2, TM-ROOT-107)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0b of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`; the G0 record `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` is already transcribed in Receipt 114 and is cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-22 from the owner's R1
rulings of the same day. Paste whole, together with the attached
`plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`.
Transcribe both verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The
R1 record is the owner's direction of record for this tranche.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `abf3c1bf5996cd9333ad706df14e62df32fbbf0f` (PR #620). Branch from current `main`.
- `AGENTS.md` SHA-256 `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/D-GOV-35.proposed.md` SHA-256 `924c1b098f1510bca9189e1ac06e4c2fd8e9d358a9fc3c4e42fdd04a53b69c88`;
  `AGENTS.proposed.patch` SHA-256 `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee` (literal `git apply --check` passes at the `AGENTS.md` SHA above);
  `IMPACT.md` SHA-256 `565e651963b08f74622ca0e0d32b66d6d301c3ef95c159867b4e41a6fbd98435`;
  `README.md` SHA-256 `c8e1b1cac088d8b34f16b8cbd77ee468178ad5d4030b3e8041aa26c97c4353c5`.
- `docs/WORKFLOW_COMPONENT_STANDARD.md` SHA-256 `5de31f552bea356629ad29af9bc664f33d49392d1c63fc2fb4dc70614abd7df9` (line 145: "- Agent 0 delegates only to named Agent 1 roles.");
  `docs/TYPES.md` SHA-256 `c97e1d73d6ea495bcfd4d632ee3a8c6ba8ff3caabd9fa2e57a245b78416335fe` (line 202: "- Agent 0 supervises only named Agent 1 managers.");
  `docs/DBM_Agent_Instruction_Architecture.md` SHA-256 `65ce988c96422c3bc3236e50cd0aae3a264fb11a9e24a1cef0d8991da0f24bbc` (line 31: "Agent 0 delegates only to named Agent 1 roles. Agent 1 delegates to Agent 2.").
- `docs/governance_harness/_DECISIONS/_REGISTER.md` SHA-256 `9250db21e6be962b46b28ee1085a218b1d111d2ed8c4b986e529402c077c9f8b`; D-GOV-14 SHA-256 `9d6dd7e4fdf96219c74a6fc728f441ecc2eabbde9bc141b5cc40d909e088f74e`.
- N2 draft manifest `…/_run_records/DEL-02-03-M2-PREP-001/ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml` SHA-256 `59f0ed42ce498a6d3fbed9148b70691a0e4ceda49e37c890ed8391c4861ef7da`; its `HANDOFF_STATE.md` SHA-256 `91ba1b5685c654851bd40aec187a8c3aceb8ff21cd877c793476612d217fb83c`; DEL-02-03 `ScopeOfWork.md` SHA-256 `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`; DEL-02-03 `_STATUS.md` SHA-256 `9fdd785881eef6ee4f210bcb381dedd757c5748f939743038541dd9e894cbdfa`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/`: `Brief.md` SHA-256 `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`; `Gate_1_Validation.md` `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14`; `WORK_GRAPH.json` `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`; `Handoff_State.md` `9a3193a2a55ab4a12d015d4ff859773233d063d0e4c566be04cb648cdc036c6a`.
- `execution/_ScopeChange/_LATEST.md` SHA-256 `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1` (unchanged by this tranche).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `cd0f1b96c500bcf7bc0886a0d5d20459129b10a86b4f106798a560432adcb5e9` (21 live: OPEN=13, DEFERRED=8; TM-ROOT-107 OPEN, ScaRef NONE; TM-ROOT-126 OPEN).
- Last Root receipt is 114. This tranche writes Receipt 115.
- `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Apply the owner's R1 rulings: mint the D-GOV-35 decision record and apply the
DEL-02-03 M2 instruction tranche (exact patch, three concordance sentences,
live manifest, routed notices, export deferral); refine SCA-004 to a Gate-2
impact assessment; apply the TM-ROOT-107 and TM-ROOT-126 dispositions through
routine Task Management. No hold lifts; the ten `HELD_UNAVAILABLE` bindings
stay held; no pin change; no App-loop write beyond the one routed notice.

## Nodes (N=3, write-disjoint; Agent 2 instances with sealed briefs under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0B_2026-08-<DD>/instances/<NODE>/`)

### N1 — D-GOV-35 decision record + DEL-02-03 M2 application (HELPS_HUMANS lane, CHANGE integration)
Write targets, exactly:
- `AGENTS.md` — apply `AGENTS.proposed.patch` with literal `git apply`; no other edit. Record the post-apply SHA-256.
- `docs/WORKFLOW_COMPONENT_STANDARD.md` line 145, `docs/TYPES.md` line 202, `docs/DBM_Agent_Instruction_Architecture.md` line 31 — replace each named sentence with the ruled hierarchy wording (R1-A recorded form); no other change to those files. The standard stays an external normative standard, not an agent.
- `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` — new, D-GOV-34 convention: `Status: RULED — APPLICATION TRANCHE PREPARED; PUBLICATION PENDING`, `HumanRuling` = R1-A verbatim ("[click] Approve as proposed" plus the recorded form), Date 2026-08-22, FramedBy this run, AcceptedBasis `main@abf3c1bf5…`, `Supersedes: D-GOV-14 item 7 (exclusivity sentence only)`, CandidateSHA/PublicationSHA/EffectiveSHA `TBD`, the eight ruled items copied from the proposal, the concordance obligation and its disposition in this tranche.
- `docs/governance_harness/_DECISIONS/_REGISTER.md` — one D-GOV-35 row in the existing row form.
- Proposal packet: append a status line to `README.md` and `D-GOV-35.proposed.md` pointing at the decision record (`RULED 2026-08-22 — see _DECISIONS/…`); packet bytes otherwise untouched; update the README SHA table for the two changed files.
- `docs/governance_harness/tranche_manifests/ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml` — finalized from the N2 draft: `basis` = current `main` at branch time (the draft's `13201dfe7…` stays cited as historical run-basis evidence, per TM-ROOT-127); `instruction_surface_paths` = every instruction-surface path this node changes, including `AGENTS.md`, the three docs, the decision record, the register, the two packet files, and this manifest; `m2_gate.authorization` = R1-B verbatim; `merge_gate: human-gated-pr`; `self_merge: false`; `m6_notice.disposition: routed` with the two notice paths below; `derivative_disposition: deferred` for `exports/chirality-app/**` with the R1-B rationale.
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md` and `projects/chirality-piping/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md` — finalized from the N2 drafts: pre/post `AGENTS.md` SHA-256, the two classes, the `instruction-asserted` boundary, the pinned/mirrored surfaces from `IMPACT.md`, each loop's follow-on (App: SCA-APP-008 / WP-06; Piping: local `AGENTS.md` semantic-mirror assessment); "coordination, not authority".
- `execution/PKG-02_…/DEL-02-03_…/_run_records/DEL-02-03-M2-APPLY-001/` — application evidence per `DEL-02-03-M2-PREP-001/VALIDATION_PLAN.md` (pre-gates reproduced, post-validators, hashes, notice paths); `DEL-02-03-M2-PREP-001/HANDOFF_STATE.md` status → `APPLIED — SEE DEL-02-03-M2-APPLY-001`; DEL-02-03 `_STATUS.md`: one History line only, `Current State` unchanged.
Check surface: post-apply `AGENTS.md` equals basis + patch exactly (reproduce by `git apply` on a scratch copy and compare hashes); the three concordance edits are single-sentence replacements (show each as a one-line diff); no file under `agents/**` changes; `tools/validation/validate_agent_instructions.py`, `validate_instruction_entrypoints.py` pass; **G4 in the CI form** `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` passes and the direct `validate_manifest` call on the finalized manifest returns `failures=[]`; both notice files exist at the declared paths; no other `projects/**` path changes; `validate_candidate_whitespace.py --base-ref origin/main` clean.

### N2 — SCOPE_CHANGE: SCA-004 Gate 2 impact assessment
Write target: `execution/_ScopeChange/SCA-004_2026-08-22_1749/` only (the amendment's single snapshot folder, SCA-002 convention).
Produce:
- `Decision_Log.md` — append the owner's Gate-1 acceptance verbatim (R1-C, with the three subject SHAs) as a `G1-ACCEPTED` row, then a `Gate 2 (impact)` row `PENDING_OWNER_ACCEPTANCE`.
- `Impact_Assessment.md` — rewritten as the Gate-2 assessment in the `AGENT_SCOPE_CHANGE.md` form: impact summary table (action → sections/files/workflows), derivative-package status table, derivative-surface classification (`DIRECT_EDIT | RECOMPUTE | NO_CHANGE` with authority basis), orphan-risk summary, estimate/schedule staleness, active snapshot/handoff impact, recommended reruns — for all eight parsed actions, carrying the G0 A3/A4/A7 amendments and the ten-binding matrix unchanged.
- `Handoff_State.md` — four-state form, status `AWAITING_OWNER_GATE_2_ACCEPTANCE`; blockers updated (D-GOV-35 now RULED; application in N1).
- `Evidence/` additions only as needed; re-run `AUDIT_DEP_CLOSURE` only if `WORK_GRAPH.json` bytes change (they should not).
Check surface: `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`, `WORK_GRAPH.json`, `DAG.md` byte-identical to the basis SHAs; `_LATEST.md` unchanged; no decomposition, register, or `_STATUS.md` byte changes; Gate 3 not opened.

### N3 — TASK_MANAGEMENT: TM-ROOT-107 and TM-ROOT-126 dispositions
Write targets: `execution/_Coordination/_TaskManagement/RULING_2026-08-<DD>_ROOT_TM107_TM126_SCA004_DGOV35.md` (new, in the `RULING_2026-08-21_ROOT_DEL0206_TRIGGER_PROMOTIONS.md` form, quoting R1-D verbatim with the R1 record SHA), `execution/_Coordination/_TaskManagement/REGISTER.csv` rows TM-ROOT-107 and TM-ROOT-126 only, `REGISTER_CLOSED.csv` via `tools/taskmgmt/taskmgmt.py archive` if the resulting states are owner-closed under the Task Management PRD vocabulary, and the counts in `execution/_Coordination/HANDOFF_STATE.md`.
Apply: TM-ROOT-107 → `SUPERSEDED_BY_SCOPE_CHANGE`, `ScaRef=SCA-004`, `EvidenceRef` = SCA-004 `Brief.md` with its SHA, `LastReviewed` = run date; TM-ROOT-126 → `RESOLVED_BY_DECISION`, `EvidenceRef` = the D-GOV-35 decision record path, `LastReviewed` = run date. No other row changes; TM-ROOT-035/042/108/106/122 untouched.
Check surface: `tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv` passes; exactly two rows differ from the basis register (plus archival relocation if applicable); counts in `HANDOFF_STATE.md` reconcile to the register.

## Not selectable in this tranche
`agents/**`, `docs/CONTRACT.md`, `docs/PRD_ROOT.md`, `docs/SPEC.md`, any `docs/**` path not named in N1, any `_STATUS.md` `Current State`, `execution/_ScopeChange/_LATEST.md`, the Root decomposition and companion registers, `execution/PKG-02_*/1_Working/DEL-02-06_**`, `runtime/**`, `projects/**` beyond the two notice files, `plans/**`, `tools/**`, `.github/**`, `exports/**` (deferral is recorded, not performed). No SCA-004 Gate 3, no folder/SOW creation for DEL-02-07..12 / DEL-04-11, no spike, no artifact download (C1 not granted), no pin change (B4), no sync/rebase without owner authorization, no merge.

## Failure rule
Unlimited repair with fresh re-review per node. A node that cannot complete
returns its handoff state with blockers instead of narrowing silently. Never
widen a node's write set; if a needed write falls outside it, report and stop
that node.

## Closeout
One tranche, one branch `codex/root-v3-phase0b-2026-08-<DD>`, one PR to
`main`, commits in dependency order N1 → N2 → N3. Append Receipt 115 to
`execution/_Coordination/LOOP_RECEIPTS.md` after the fact, in-PR, with: this
steer and `plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`
as CHAT_TRANSCRIPTION (record its SHA-256); per-node write sets; pre/post
`AGENTS.md` SHA-256; every cited SHA/commit; validator outputs including the
CI-form G4 output; `execution/_Coordination/HANDOFF_STATE.md` counts updated.
Run before pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies before endorsement; the D-GOV-35 record's PublicationSHA /
EffectiveSHA are backfilled by a later routine act after merge.
