# Plan — chirality-app-dev whole-corpus Deliverable Concordance (post-v3 reconciliation)

## Context

The App shipped as v3.0.1 (`main` = `fd002217f`) after a push steered by a dependency graph,
an evolving owner declaration of "done", and in-session code judgments — without reference to
the deliverables folders. Agents still propagated some carrier notes into them, so the corpus
is unevenly updated rather than uniformly stale. Development is paused pending an
owner-steered reconciliation. This plan deploys the repo's `reconciliation` workflow **as
written** over all 54 App deliverables (11 packages, ~1,733 file-local `CLM-NNN` claims), with
the owner ruling at R4 on which side changes. It is a four-way comparison: deliverable text ·
code · recorded v3 direction · unrecorded judgment (visible only as "it shipped").

Expected outputs: deliverable text repairs, a scope-change handoff package (retire / merge /
create deliverables), a code-defect list, and regenerated `## Remaining` sections. No
lifecycle transition, issuance, hold change, release claim, or DAG rebuild.

## Fixed parameters (owner-directed)

- Roles: HELP_HUMAN (Agent 0, this session) → one WORKING_ITEMS manager per package → TASK
  workers. TASK never delegates. Mechanism: Claude Code harness-native descendants (D-GOV-35),
  nested spawn verified. All agents Opus 5 / high (owner presets the session; children inherit;
  recorded as owner-reported, plus actual model per dispatch).
- Max 16 concurrent agents including Agent 0; cap is a brief parameter the owner may change
  between sub-batches.
- Source state: current `main`, pinned by SHA (no `v3.0.1` tag exists). Runtime project
  `projects/chirality-runtime/{packages,tests}` is a read-only evidence root; its execution
  tree is not read; gate status comes only from App surfaces.
- MR-1..MR-11 enter R0 as candidate conventions.

## Step 0 — Orientation prompt for the piping session (Agent 0 direct; first action)

Before anything else, Agent 0 writes a self-contained prompt the owner can paste into a
separate session that will run the same kind of reconciliation over
`projects/chirality-piping/`. Delivered in chat in a copyable block (and saved to the
scratchpad, not the repo). It orients; it does not prescribe piping particulars.

Content:
- Role and posture: HELP_HUMAN / Agent 0, read `AGENTS.md`, `agents/AGENT_HELP_HUMAN.md`, then
  the piping project's own `AGENTS.md` and `loop/`; preferred 0/1/2 topology (one
  WORKING_ITEMS manager per package, TASK workers, TASK never delegates); owner's model/effort
  and concurrency directions are given by the owner in that session.
- The undertaking: run `workflows/reconciliation/` as written under kernel
  `docs/DELIVERABLE_CONCORDANCE_METHOD.md`; code is evidence, not authority; discovery is
  read-only; owner rules direction-of-change at R4; activation is a register decision merged
  to `main` before any dispatch.
- The refined concept from this session: four-way comparison (deliverable text · code ·
  recorded owner direction · unrecorded judgment); forward and reverse passes with the
  anti-anchoring two-sealed-pass worker design; authority tiering (local design vs governance
  invariant); direction records classed CONTEXT unless governing; cause-clustered R4 packets;
  structural outcomes route to `scope-change`; resumability and commit discipline; frozen
  scratch worktree for evidence and gate transcripts.
- What to discover rather than assume (listed as questions): piping's corpus size and
  deliverable format, its prior concordance runs and their run-local conventions, its decision
  register and next ID, its adoption plan, professional-boundary / validation-provenance /
  ISSUED-baseline layers that the kernel says must not be flattened, its registered checks,
  its hold mechanisms, **active concurrent work** on piping `main`, and whether/how the owner's
  development there departed from the deliverables.
- Pointers, not answers: the App run's plan of record (this plan's content, summarised) and
  the closed July piping run folder as a local template.
- First deliverable of that session: an assessment + questions to the owner, not dispatch.

## Stage P — Activation (Agent 0 direct; nothing is dispatched before merge)

Write scope: `execution/_Coordination/_DECISIONS/`, `_REGISTER.md`, a new AgentRuns folder,
and the 54 `_STATUS.md` seed lines (below).

1. Branch from `main`. Create `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-<date>-CONCORDANCE/`
   with `OWNER_DIRECTION.md` (verbatim, hashed owner quotes from this session — pattern:
   `AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md`), `WORK_GRAPH.json`,
   and a delegation/model attribution record.
2. Draft **D-APP-128** PROPOSAL packet + ruling-record skeleton + register row, modelled on
   `D-APP-55_PACKET_CONCORDANCE_ACTIVATION_2026-07-11.md` / `D-APP-55_RULING_2026-07-11.md`.
   The packet puts these to the owner:
   - Scope: whole corpus, 54 deliverables (recommended; owner already indicated).
   - Method pin by SHA: kernel `docs/DELIVERABLE_CONCORDANCE_METHOD.md` Rev 1 +
     `workflows/reconciliation/**` + the project adoption record
     `projects/chirality-app-dev/plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`
     **with a named delta list** (SOW_V1 format, claim key `DEL-xx-yy#CLM-NNN`, two evidence
     roots, reverse pass, schema = July 19-column header + named extensions to be ruled at R0).
   - Bootstrap seeding per kernel §6: one `(gated: D-APP-128)` `## Remaining` line in each of
     the 54 `_STATUS.md` (recommended: follow the kernel; waiver must be an explicit ruling clause).
   - Authority classes for v3 direction sources (GOVERNING / CONTEXT / EXCLUDED) — see R0.
   - D-APP-116..119 (still AWAITING_RULING): rule now, or park so their claim populations
     become HELD rows.
   - Overlap permission: R1 deterministic inventories may run while the R0 gate is pending.
   - R0 calibration sample (below) and the one-frozen-transcript-pair substitution for MR-3.
3. Owner rules → transcribe ruling → PR → fresh-context read-only review of the PR diff (a
   closeout act on the packet, not concordance dispatch) → CI → merge to `main`.
   **No concordance work is dispatched before this merge.**

## Stage R0 — Freeze, calibrate, owner gate

Run folder: `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_<date>/`.
All discovery writes stay inside it and the AgentRuns folder (briefs, state log, scripts included).

1. **Frozen source state.** Pin (`main` SHA, runtime tree SHA). Create one detached scratch
   worktree at that SHA outside the repo (scratchpad). All worker reading and both gate
   transcripts happen there so `npm ci` / `tsc -b` never contaminate the evidence tree.
   At every sub-batch boundary, diff deliverables/frontend/runtime paths against the freeze;
   mark affected rows `STALE_INPUT` and rerun only those.
2. **`RUN_BASIS.md`** (template: July `RUN_BASIS.md`): activation, method pin + delta, source
   state, census (54; 53 IN_PROGRESS, DEL-09-07 OPEN), concurrent-work check, fences
   (F-APP-1..5), write boundaries, evidence roots, and the **authority and reliability map**:
   - GOVERNING: `docs/PRD.md`, DIRECTIVE/CONTRACT/SPEC/TYPES, decomposition v3_2 + accepted
     SCAs, RULED register rows (flagging RULED-but-not-applied: D-APP-104, 107, 121–123, 125, 126),
     D-GOV-43.
   - CONTEXT (never changes a Disposition; feeds R3 clustering only):
     `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` §3, §10;
     `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`; ruling records a1–a15 / r1–r18;
     SCA-APP-008 (unaccepted, partly superseded); `APP_V3_*` AgentRuns.
   - Known basis defects to carry as findings, not fix: differing `decomposition_basis` pins
     across SoWs; stale "pointer not moved" text in the current DepClosure snapshot.
3. **Gate transcripts** (needs owner OK for network `npm ci`): runtime `npm ci` → `npm run build`
   → typecheck → `vitest run`; then frontend `npm ci` → `npm run typecheck` → `npx vitest run`.
   Record in the July format (`R1_INVENTORY/GATE_TRANSCRIPT_W1_fac46e33f.md`), one per project.
   Workers cite them and never run suites.
4. **Done-declaration candidate.** One TASK assembles `V3_DONE_DECLARATION_CANDIDATE.md`, every
   line cited to the release plan §3.2/§10.1, G0 amendments, and later rulings. Owner
   confirms/edits at the R0 gate; confirmation is recorded as a register ruling and merged
   before R2. Until then it is CONTEXT.
5. **Candidate conventions** (`CONVENTIONS.md`): MR-1, 2, 5, 7, 8, 10 as written; MR-3 →
   frozen transcript pair; MR-4/MR-9 → expected moot, use contract claim IDs (confirm);
   MR-6 → owner-accepted runtime split; MR-11 → generalised "ruled decision stands over
   untranscribed corpus wording". Extensions: `DirectionEvidence`; `AuthorityTier`
   (LOCAL_DESIGN | PRD | GOVERNANCE_INVARIANT); controlled `CauseTag` vocabulary;
   `SelectableUnderCurrentLoop` → `MechanicallyUnblocked` (explicit kernel-column mapping);
   a disposition rule for agent-propagated notes asserting state no claim owns;
   capability-row granularity for the reverse pass; the oversize threshold (below).
6. **Calibration** under one manager: 8 deliverables — DEL-01-01 (governance invariants,
   largest SoW), DEL-02-05 (shell redesign carrier), DEL-03-01 (runtime contract, code now in
   chirality-runtime), one PKG-04 or PKG-06 deliverable whose code moved wholly to runtime,
   one PKG-08 agent-suite deliverable, DEL-09-07 (only OPEN), one PKG-10 doc-only, one known
   carrier-note-polluted deliverable; **one of them audited double-blind by two workers** to
   measure disposition variance; plus **one reverse-pass code area** (lib/harness).
   Fresh evidence-only verifier. Report in the July `R0_CALIBRATION_REPORT.md` shape.
7. **R0 owner gate:** conventions, done declaration, D-APP-116..119 handling, scale-out.
   No deliverable is edited.

## Stage R1 — Inventory (read-only)

- **R1a deterministic scripts** (Agent 0 or one TASK; scripts live in the run folder):
  `DELIVERABLE_INVENTORY`, `REMAINING_INVENTORY`, `CLAIM_INDEX` (every `### CLM-NNN` heading,
  keyed `DEL#CLM`; the 100%-coverage checklist), `DECISION_INDEX` (127 rows + applied-ness),
  `VERIFICATION_INDEX` (236 frontend + 45 runtime test files), `IMPLEMENTATION_SURFACES`
  (every file in both roots — July covered frontend only, 155 files), `DIRECTION_RECORD_INDEX`,
  and a per-deliverable **claim→candidate-paths hint file** (grep over identifiers, test names,
  DEL-ID mentions). Also the structural validator (19-column + extensions, vocabularies,
  MR-1/MR-2 rules, key uniqueness).
- **R1b reverse pass** — 11 disjoint code areas, one TASK each, under 2 managers, sampled
  verifier: electron host/IPC · build/packaging/proof scripts · `src/app` routes+API ·
  `src/lib/harness` · shell UI+view-model · woven-dialogue · workspace/pipeline/workbench/portal ·
  settings/consent/lifecycle/runtime-client/contract facade · runtime core+cli+daemon ·
  runtime contracts+client+engines · packaged instruction bundle (Root-owned sources; findings
  route to Root). Output `SURFACES/<area>_capabilities.csv`: capability, paths, covering tests.
  **No candidate-owner column** (avoids anchoring R2).

## Stage R2 — Package concordance (rolling pool, not barrier waves)

- Slots: Agent 0 + 2–3 package managers + workers + 1 rolling verifier slot ≤ 16. Default:
  2 managers × up to 6 workers + verifier(s). Managers take the next package when theirs closes.
- Order (package graph is cyclic, so order by leverage): PKG-01, 03, 04 first (universal
  upstream + the runtime-extraction cluster, so its lessons land early) → 07, 05, 06 → 02, 08 →
  09, 10 → PKG-00 last (control/DAG depends on everyone's findings).
- Per package: APP-HOLD preflight
  `python3 execution/_Scripts/app_hold.py check --operation dispatch ...` stored with the brief;
  one owning ledger worker per deliverable. **Two sealed passes per worker:** (1) forward — SoW
  claims vs code using only the hint file, conventions, authority map, transcripts; (2) after
  the forward rows are sealed, the worker receives the R1b capability rows and answers each
  `CLAIMED_BY <DEL#CLM>` | `PARTIAL` | `NOT_MINE`. R3, not workers, owns the final UNMAPPED set.
- Oversize deliverables (threshold calibrated in R0, e.g. >45 claims or >35 KB): the **manager**
  first dispatches read-only evidence-gathering TASKs per code slice; their fragments feed the
  single owning worker (TASK does not delegate).
- Validator after every sub-batch; verifier dispatched as soon as a package's ledgers validate
  (all non-ALIGNED + self-flagged rows + aligned sample + sampled `CLAIMED_BY` links); verifier
  never edits; defective ledgers rerun by a fresh worker; contested rows stay visible.
- Manager context discipline: returns are one line per deliverable (path, row count,
  disposition histogram, validator verdict); managers never read CSVs; a manager past ~7
  deliverables is replaced by a fresh one starting from `RUN_STATE.jsonl`.
- Outputs: `WAVES/PKG-XX/<DEL>_claims.csv`, `<DEL>_notes.md`, `PKG-XX_VERIFICATION.md`;
  `PACKAGE_SUMMARIES/` derived by script.

## Stage R3 — Synthesis (one synthesis manager + themed TASKs)

Merged `CLAIM_CONCORDANCE.csv`; deterministic coverage QA (100% of `CLAIM_INDEX` dispositioned;
100% of capability rows accounted = claimed or UNMAPPED; summaries reproduce; July C1–C13
analogue); `UNMAPPED_IMPLEMENTATION.csv`; clustering **by `CauseTag`** (e.g. A2 topology,
Codex-only engine, shell redesign, runtime extraction, facade deprecation);
`CROSS_PACKAGE_FINDINGS.csv` (ownership, shared surfaces, register defects, RULED-not-applied);
independent stratified spot check (~9% + all high-risk, July `R3_SPOT_CHECK.md` design).

## Stage R4 — Owner decision gate

~15–20 cluster packets + an exceptions list, each carrying its full affected-claim population;
ordered by cause cluster, then `AuthorityTier`. Options per packet: change deliverable ·
change code · accepted divergence · structural (→ `scope-change`) · governance amendment.
Ruling recorded as **D-APP-129** and merged. Affected repair paths stop until ruled.

## Stage R5 — Authorized repairs only

Per-package managers, per-deliverable workers, write scope = that DEL folder. Deliverable text
under its ruling; `## Remaining` regenerated through its owning contract; structural outcomes
leave as a scope-change handoff package; code defects recorded as Remaining items only where
D-APP-129 names them (any code fix is a separate `software-bounded-implementation` brief with
`software-code-review`). Completed / held / deferred rows accounted exactly.

## Stage R6 — Backcheck and close

New immutable `BACKCHECK/<id>/`: changed-claim re-extraction with multiset equality to the
repair manifest, rider/assessment audit, held-and-deferred audit, containment audit (tracked,
untracked, ignored), 54-row `REMAINING_WORK_CENSUS.csv` (explicit `NONE` rows), `HANDOFF.md`;
bootstrap Remaining lines closed; register closure note. Closure = evidence coherence only.

## Cross-cutting: resumability, commits, review, usage

- `RUN_STATE.jsonl` (append-only: phase, package, deliverable, status, brief hash, output hash,
  validator verdict) + `RESUME.md` a cold Agent 0 can follow in five minutes; `WORK_GRAPH.json`
  updated at each fan-in. Briefs stored under `BRIEFS/` and idempotent ("if the ledger exists
  and validates, return the census only"); workers write whole files with a terminal sentinel.
- Only Agent 0 commits — after every validated sub-batch. Full fresh-context review on the
  P, R0, R3/R4, R5 and R6 PRs; R2 sub-batch commits rely on validator + verifier. Merges under
  the standing Git authorization once CI and review are clean; `chirality-change` checklist.
- Check session usage before each sub-batch; below a margin, drain and do not launch.
- Registered checks for `execution/**` changes: `harness-pytest`, `harness-self-check`,
  `app-hold-integrity` via `tools/software_workflow/run_registered_checks.py`.

## Verification

- Stage P: packet/ruling/register diff reviewed; CI green; ruling on `main` before any dispatch.
- R0: validator passes on calibration ledgers; double-blind variance reported; owner gate recorded.
- R1–R3: coverage equalities hold by script (claims 100%, capability rows 100%, keys unique,
  summaries reproduce); spot-check verdict census; zero writes outside run + AgentRuns folders
  (`git status` incl. ignored paths).
- R5–R6: multiset equality; 54-row census; registered checks pass; handoff names upstream
  snapshot, derivative, repaired source basis, blockers, rerun triggers.
