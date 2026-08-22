# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 0 (WP-01 Root half)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 0 of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-22 and updated with the
owner's G0 rulings of the same day. Paste whole, together with the attached
`plans/steers/chirality_app_v3_g0_record_2026-08-22.md`. Transcribe both verbatim into the closeout receipt as
CHAT_TRANSCRIPTION. The G0 record is the owner's direction of record; where it
is marked AMENDS PLAN it supersedes Revision 3.1's text.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `13201dfe7dc3b97c9aa36f6305cae604b48ef80f` (PR #615).
- `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` SHA-256
  `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` (Revision 3.1,
  non-governing; input, never authority).
- `plans/chirality_app_v3_release_plan_review_round_3_2026-08-22.html` SHA-256
  `447d407fe38c395d39e3481debc0d8c16317bbffe441a2c269eb194921aace95`.
- `AGENTS.md` SHA-256 `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- `docs/governance_harness/_DECISIONS/D-GOV-14_pr188_review_closure.md` SHA-256
  `9d6dd7e4fdf96219c74a6fc728f441ecc2eabbde9bc141b5cc40d909e088f74e`.
- `execution/_ScopeChange/_LATEST.md` SHA-256
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`
  (latest applied snapshot SCA-002; SCA-003 closed zero-action) — SCA-004 is the next ID.
- Last Root receipt is 113. This tranche writes Receipt 114.
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Create the governed Root basis for the v3 release pathway without lifting any
hold: a D-GOV proposal packet for the delegated-harness-native delegation class,
a DEL-02-03 M2 tranche *preparation*, and the SCA-004 Gate-1 assessment carrying
the refreshed objective-relative DAG. Nothing in this tranche amends
`AGENTS.md`, `docs/CONTRACT.md`, `docs/PRD_ROOT.md`, any deliverable `_STATUS.md`,
the `_LATEST.md` pointer, or DEL-02-06. The ten `HELD_UNAVAILABLE` bindings
(plan §8.3) remain held.

## Nodes (N=3, write-disjoint; Agent 2 instances with sealed briefs under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE0_2026-08-<DD>/instances/<NODE>/`)

### N1 — HELPS_HUMANS: D-GOV-35 proposal packet (delegated-harness-native class)
Write target: `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-<DD>_delegated_harness_native_class/` only.
Produce:
- `README.md` — status `PROPOSED — AWAITING OWNER RULING`, SHA table of every file in the folder.
- `D-GOV-35.proposed.md` — decision text that (a) supersedes D-GOV-14 item 7's
  "managed child sessions are the sole executable app-harness delegation path"
  by adding a second class, *delegated-harness-native* (Codex App Server
  descendants inside the hard outer envelope), (b) preserves managed children
  as the sole *Chirality-managed* path, (c) permits untyped primary native entry
  (G0 A1), (d) states native descendants are not automatically Agent 2 (G0 A2),
  (e) records the **parity requirement**: Agent 0/1/2 role entry is always
  offered for Codex sessions, and when G-ROLE cannot mechanically prove
  non-delegation the explicit Agent 2/TASK mode is still offered, labelled
  "role not mechanically enforced", with its governed-workflow evidence marked
  instruction-asserted — i.e. for this class K-SUBAGENT non-delegation is
  instruction+config asserted, not mechanism-proven (G0 A3, verbatim owner text
  quoted in the proposal), (f) resolves TM-ROOT-126's prose-concordance concern
  against `docs/WORKFLOW_COMPONENT_STANDARD.md` in the same text, (g) names
  K-SUBAGENT-1/2/3, the D-APP-68 transcription, DEL-08-04's SOW, and
  `projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts:205-213`
  (blob SHA-256 `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c`)
  as the surfaces the ruling would touch — the code change is App WP-06 work and
  is *not* made here.
- `AGENTS.proposed.patch` — inactive zero-context patch to the "Delegation and
  Entry Rules" section of `AGENTS.md` (heading at line 80) at the SHA above.
  Must pass `git apply --check` and must NOT be applied.
- `IMPACT.md` — conformance statement against `docs/WORKFLOW_COMPONENT_STANDARD.md`
  and `docs/DECOMPOSITION_STANDARD.md`; list of downstream pinned/mirrored
  surfaces per the agent-index change-notice rule (corpus snapshots and
  SHA-pinned mirrors in App and Piping).
Check surface: `git apply --check` passes; `AGENTS.md` byte-identical to basis;
`tools/validation/validate_agent_instructions.py` and
`tools/validation/validate_instruction_entrypoints.py` pass unchanged;
`tools/validation/validate_candidate_whitespace.py --base-ref origin/main` clean.

### N2 — DEL-02-03 M2 tranche preparation
Write target: `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/` only.
Produce a preparation package (no lifecycle change, no `AGENTS.md` write):
- draft instruction-tranche manifest with `basis` = `13201dfe7dc3b97c9aa36f6305cae604b48ef80f`;
  verify it resolves as a commit with `git cat-file -t` and say so (TM-ROOT-127);
- the exact `AGENTS.md` delta *by reference to N1's patch SHA* (no duplicated bytes);
- draft routed notices to the App and Piping coordination surfaces stating what
  would change in `AGENTS.md` and the follow-on each loop would carry (drafts
  stay inside this run folder; routed only after the D-GOV-35 ruling);
- the validator list the application tranche must run;
- `HANDOFF_STATE.md` with status `PREPARED — BLOCKED ON D-GOV-35 RULING`.
Check surface: `tools/validation/validate_instruction_tranche_manifest.py` on the
draft manifest; DEL-02-03 `ScopeOfWork.md` SHA-256 still
`e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`; `_STATUS.md` untouched.

### N3 — SCOPE_CHANGE: SCA-004 Gate-1 assessment + release-pathway DAG
Write targets: `execution/_ScopeChange/SCA-004_2026-08-<DD>_<HHMM>/` and one notice
`execution/_Coordination/NOTICE_2026-08-<DD>_ROOT_SCA-004_V3_RELEASE_PATHWAY_DAG.md`.
Produce (assessment only; `_LATEST.md` untouched; status `AWAITING_OWNER_ACCEPTANCE`):
- `Brief.md`, `Impact_Assessment.md` covering the plan's Root-side items as
  amended by the G0 record: Root/App K-CONTROL-1 second purpose-limited socket;
  K-ROLE-2 role-posture digest; K-NET-1 enumerated OpenAI service endpoints
  **plus the three per-root command-network postures (G0 A7)**; Root runtime API
  v2 (attributed approval request/decision, managed-network prompts routed with
  the grouping caveat — no longer denied); HarnessEvent schema v2 closed union
  with four terminals; `DelegatedHarnessProcessSupervisorPort`,
  `WorkerRetirementCoordinatorPort`, `HostedEngineConsentPort`; **restart
  semantics per G0 A4: terminalize active turns, `thread/resume` under
  root/account/policy-digest continuity, fresh thread otherwise** (dispositions
  TM-ROOT-108); `runtime/packages/cli/src/launch-agent.ts` two-job renderer
  (dispositions TM-ROOT-042's bundling question as carried to G-HELPER per
  G0 B2); a Root loop receipt validator (none exists — scope it); the
  `source_identity` binding at G0.5 (dispositions TM-ROOT-035); TM-ROOT-107 as
  the ancestor concern this SCA answers; DEL-02-06 ten-binding matrix keyed by
  SOW REQ-027 and its exclusion block; TM-ROOT-106 and TM-ROOT-122 named as
  G1 blockers only (G0 B4 — no pin amendment here).
- `WORK_GRAPH.json` + `DAG.md`: objective-relative dependency graph for the
  release pathway over Root deliverables, with cross-loop edges to App as
  *notice edges* (never foreign writes). List every SCC with a proposed move
  (decompose / invert / merge / cut; cut/merge flagged human-gated);
  cycle-participating edges non-gating until resolved (`docs/CYCLE_DRIVEN_RESOLUTION.md`).
- Dispatch `AUDIT_DEP_CLOSURE` over the graph; include its return.
- `Handoff_State.md` in the SCA-003 four-state form.
- The routed notice to App: names the notice edges, the held-binding matrix,
  the G0 amendments App must mirror (A3/A4/A7), and that SCA-APP-008 is expected
  to reciprocate; coordination, not authority.
Check surface: `WORK_GRAPH.json` parses; every node id resolves to a live Root
deliverable folder or a named App notice edge; AUDIT_DEP_CLOSURE return present
with verdict; `execution/_ScopeChange/_LATEST.md` SHA unchanged.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/CONTRACT.md`, `docs/PRD_ROOT.md`, `docs/SPEC.md`,
`docs/TYPES.md`, any `_STATUS.md`, `execution/_ScopeChange/_LATEST.md`,
`execution/_Coordination/_TaskManagement/REGISTER.csv` (candidates go in a
harvest file only), `execution/PKG-02_*/1_Working/DEL-02-06_**`, `runtime/**`,
`projects/**`, `plans/**`, `tools/**`, `.github/**`. No spike execution, no
artifact download (G0 C1 is not yet granted), no pin changes (G0 B4), no
sync/rebase without owner authorization, no merge.

## Failure rule
Unlimited repair with fresh re-review per node. A node that cannot complete
returns its handoff state with blockers instead of narrowing silently. Never
widen a node's write set; if a needed write falls outside it, report and stop
that node.

## Closeout
One tranche, one branch `codex/root-v3-phase0-2026-08-<DD>`, one PR to `main`,
commits in dependency order N1 → N2 → N3. Append Receipt 114 to
`execution/_Coordination/LOOP_RECEIPTS.md` after the fact, in-PR, with: this
steer and `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` as CHAT_TRANSCRIPTION (record its SHA-256);
per-node write sets; every cited SHA/commit; validator outputs;
`execution/_Coordination/HANDOFF_STATE.md` counts updated. Run before pushing:
`validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py` (N2 draft), `tools/taskmgmt/taskmgmt.py
validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`.
Do not merge. If `main` advances, request sync authorization from the owner
and record it in the receipt. HELP_HUMAN byte-verifies before endorsement.
