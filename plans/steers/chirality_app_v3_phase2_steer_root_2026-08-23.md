# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 2 (seven SOW candidates for the SCA-004 carriers, drafting only)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 2 of the v3 release pathway. Target workspace: Root governance loop. Paste whole; transcribe verbatim into the closeout receipt as CHAT_TRANSCRIPTION. The owner authorizes this drafting tranche by carrying this steer; SOW acceptance returns to the owner as separate acts against the exact published bytes. Authority context: R3-B (Receipt 117) named SOW drafting/acceptance as a later separately gated WORKING_ITEMS act; R6-A (Receipt 120) confirmed revision 1.3; Phase 1 (Receipt 121) initialized the seven carrier folders.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 after PR #637 merged
(Receipt 121). This tranche DRAFTS the seven Scope-of-Work contracts and
returns them for owner acceptance. It accepts nothing itself. Dependency
extraction, estimates, scheduling, lifecycle transitions, implementation, and
activation remain later, separately gated acts and are NOT in this tranche.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `75c4e2ba401a6f5ad0c2f38846c39db6ab157405` (PR #637). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- Live decomposition is applied revision 1.3; `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` SHA-256 `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`; `execution/_ScopeChange/_LATEST.md` SHA-256 `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
- The seven Phase-1 carrier folders exist exactly as created by PR #637 content commit `dab470e2f0c7345f10c34bcce9e489eb68bf0541` (merge `75c4e2ba4…`): each contains exactly `_CONTEXT.md`, `_STATUS.md` (`OPEN`), `_REFERENCES.md`, `_DEPENDENCIES.md`, and no `ScopeOfWork.md`; all 28 files byte-identical to that commit.
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched by this tranche).
- `execution/_Coordination/HANDOFF_STATE.md` SHA-256 `b65fc69fce44acce562e445ceeb0be3c69a0134efe2273b7309f76574ccf0c1f`.
- Last Root receipt is 121. This tranche writes Receipt 122.

## Objective

Draft — never accept — one `ScopeOfWork.md` per SCA-004 carrier
(DEL-02-07..DEL-02-12, DEL-04-11), in the house SOW form, each explicitly
marked as a draft awaiting owner acceptance. `_STATUS.md` stays `OPEN`
everywhere. No dependency, estimate, schedule, lifecycle, graph, audit,
TM, tool, runtime, pin, or App surface changes. No hold is lifted; all ten
DEL-02-06 bindings remain `HELD_UNAVAILABLE`.

## Nodes (N=1; WORKING_ITEMS with Agent 2 instances under sealed briefs, one per SOW, under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE2_2026-08-<DD>/instances/<DEL-ID>/`)

### N1 — WORKING_ITEMS: seven SOW candidates
Write targets, exactly: `ScopeOfWork.md` (new) in each of the seven carrier folders. Nothing else in those folders or anywhere else is written.
Pre-write: reverify every bound-input SHA above; if anything differs, stop and report.
Each SOW must:
- Use the house form: frontmatter `schema: chirality-deliverable-sow/v1` with `deliverable_id`, `package_id`, `decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405`, `project_scope_refs`, `package_objective_refs` exactly as in the applied register row, plus `status: DRAFT_AWAITING_OWNER_ACCEPTANCE`; body sections Purpose and Objective Traceability; Deliverable Definition — Ontology; Completion and Reliance Basis — Epistemology; Production and Verification Method — Praxeology; Governing Values and Decisions — Axiology; Output and Evaluation Matrix (the DEL-02-06/DEL-04-09 house pattern).
- Ground every claim in accepted truth only: the applied register row (name, type, Context Envelope M, CoversScopeItems, SupportsObjectives, description, anticipated artifacts, anticipated write locus as planning note never authorization), the folder `_CONTEXT.md`, the approved `Propagation_Plan.md` §2 boundary note, and the G0 A3/A4/A7 carriage as allocated by the accepted amendment (A3 across DEL-02-07/09/10/12; A4 in DEL-02-11; A7 across DEL-02-08/09/10/12). No invented scope, interface, dependency, tool, or schedule content.
- Carry the standing constraints verbatim where they bind: DEL-02-07 — daemon remains sole runtime broker, authenticated private Unix socket, no TCP listener; DEL-02-08 — exact supply/protocol pinning without any pin amendment (TM-ROOT-106/122 stay G1 blockers), OpenAI service endpoints enumerated separately from command network; DEL-02-09 — root-private account/consent boundary, ambient `~/.codex` excluded, labelled fallback; DEL-02-10 — Root API v2, closed event union with only the four terminal identifiers, attributed approvals; DEL-02-11 — exactly-once terminalization, `thread/resume` only under recorded continuity, no in-flight re-attach claim; DEL-02-12 — conformance/source-identity/shared-release fan-in with all ten bindings held; DEL-04-11 — Root-specific deterministic receipt validator, `tools/**` implementation under separate M2 authority.
- State in Epistemology that completion claims require the deliverable's own accepted evidence and that nothing in the SOW lifts a hold, authorizes implementation, or creates dispatch authority; acceptance of the SOW itself is a separate owner act.
- Record each SOW's SHA-256 in its instance return and in the receipt.
Check surface: exactly seven new `ScopeOfWork.md` files and no other content change (`git diff --name-only` against the branch basis ⊆ the seven files plus run tree, coordination handoff, and receipt); every frontmatter field matches the applied register row exactly; every SOW carries `status: DRAFT_AWAITING_OWNER_ACCEPTANCE`; `_STATUS.md` files still say `OPEN`; fresh review per SOW (or one consolidated fresh review across the seven) with zero actionable findings; live practitioner-harness tests still pass (`python3 -m pytest tools/practitioner_harness/test_root_adoption.py tools/validation/test_validate_root_harness_adapter.py -q`) — if adding `ScopeOfWork.md` files trips a pinned harness baseline, stop and report the exact failure; do not repin without owner direction.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**`, `tools/**`, the seven live decomposition files, `execution/_ScopeChange/**`, any `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, or `_DEPENDENCIES.md`, DEL-02-06's folder entirely, estimates, schedules, `WORK_GRAPH.json`/`DAG.md`, audit snapshots, the Task Management register, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface.

## Failure rule
Unlimited repair with fresh re-review per SOW. A SOW that cannot be grounded
in accepted truth returns its gap as a blocker instead of inventing content.
Never widen the write set; if a needed write falls outside it, report and
stop.

## Closeout
One tranche, one branch `codex/root-v3-phase2-2026-08-<DD>`, one PR to
`main`. Append Receipt 122 to `execution/_Coordination/LOOP_RECEIPTS.md`
after the fact, in-PR, with: this steer as CHAT_TRANSCRIPTION (record its
SHA-256); the write set; the seven SOW SHA-256 values; validator outputs
including the CI-form G4 output (expected: zero instruction-surface paths);
`execution/_Coordination/HANDOFF_STATE.md` updated (Phase 2: seven SOW
drafts published, `AWAITING_OWNER_SOW_ACCEPTANCE`; remaining: acceptance,
dependency extraction, estimates, schedule, evidence reruns). Run before
pushing: `validate_candidate_whitespace.py --base-ref origin/main`,
`validate_agent_instructions.py`, `validate_instruction_entrypoints.py`,
`validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only`,
`tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`,
`git diff --check`. Do not merge. If `main` advances, request sync
authorization from the owner and record it in the receipt. HELP_HUMAN
byte-verifies before endorsement; the owner accepts, corrects, or declines
each SOW as a separate act against the exact published bytes.
