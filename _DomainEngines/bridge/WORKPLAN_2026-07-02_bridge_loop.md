# Bridge Work Loop — standing plan (app-dev ↔ piping tier-0 bridge)

> **Epistemic status: agent-authored plan — not authority.** Written at owner direction
> (Ryan Tufts, K-AUTH-1) on 2026-07-02. This plan never authorizes work: owner-adopted
> briefs and owner rulings do. Sources govern on any disagreement. This file is a
> PROTOCOL plus a coarse backlog; it deliberately does NOT spell out work ahead of
> time — each loop iteration re-derives state from the live tree. The Loop Log at the
> bottom is append-only; earlier entries are history, never edited.

## Owner intent (recorded 2026-07-02)

Execute the most comprehensive amount of bridge work available, as a series of loops,
across sessions. Each iteration discovers state fresh rather than following pre-spelled
direction; implementation proceeds organically as dependencies resolve. Staging is
retained only where the governance structure compels it.

## Why any staging remains (the compelling reasons)

1. **Adoption is a human act** (K-AUTH-1; D-GOV-04): every governed tranche requires an
   owner-adopted brief. No agent can pre-authorize N tranches; each loop therefore has
   an adoption gate.
2. **Live binding is gated ×4** (`_DomainEngines/profiles/open_pipe_stress.yaml:143`):
   tier-0 adoption (cleared) · app-dev F3 (D-T0-08 sequence, needs proven L2) ·
   piping D-21 (adoption held) · DEC-041 automation (needs consumable package).
   Three of four are owner rulings or unbuilt prerequisites — not agent work.
3. **Fences F1–F4** bound what any tranche may touch regardless of ambition.

The loop is therefore comprehensive over the *lawful surface at each iteration* — a
surface that widens as the owner rules. Nothing lawful is deferred by plan design;
work is deferred only by gates.

## The loop protocol (every iteration)

0. **Discover.** `git` state (expect main at or past this file's commit); harness
   `status` ×3, `drift --all`, `self-check`, `next`,
   `python3 -m pytest tools/practitioner_harness -q`
   (`PYTHONDONTWRITEBYTECODE=1` each); read this plan's Loop Log; re-read the
   readiness map (`_DomainEngines/bridge/READINESS_2026-07-02_bridge_tranche1.md`,
   esp. §1's naive-reading corrections — pointers to check, not conclusions to
   assume); check BOTH project decision registers + the tier-0 register for rulings
   newer than the last Loop Log entry. New rulings are how work unlocks — look for
   them every time. Compare measurements against the last Loop Log entry's recorded
   state; a differing measurement is a finding to report, not background.
1. **Select.** The widest lawful tranche(s) now. Principles, in order:
   (a) work that discharges a gate prerequisite beats work that doesn't;
   (b) owner-queued items (below) beat agent-inferred ones;
   (c) doc/design-level before any binding;
   (d) one brief per deliverable fence — don't split what one brief covers, never
       merge across fences.
2. **Brief.** `python3 tools/practitioner_harness/harness.py brief --project <p>
   --deliverable <id>` per selected deliverable → CANDIDATE(s); fill the objective
   (practitioner-proposed, grounded in cited files — K-INVENT-1).
3. **Gate.** STOP; owner adopts/declines: edit `state:` → HUMAN_ADOPTED, fill
   `adopted_by:`/`adopted_on:` (per `docs/governance_harness/human_actors.md`), move
   the file to a governed path OUTSIDE `_harness_generated/`, commit; agent confirms
   with `brief --verify-adoption <path>`. Record the outcome in the Loop Log.
4. **Execute** on a branch (branch-first + PR), inside the adopted fence + standing
   constraints below.
5. **Check.** `run-validations`, `scope-check` (PR diff range vs fence),
   `evidence-check`, `closeout-digest`; open PR; CI (governance-harness workflow)
   green; owner merges — never self-merge.
6. **Log.** Append a Loop Log entry: measurements, deltas observed, work done, what's
   newly unlocked, owner-action queue changes. Next iteration starts at 0.

## Standing constraints (all iterations)

- No F1/F2/F3/F4 crossing without the gating ruling: no DomainEngineProfile /
  OperationProposal source types in `frontend/src`, no domain MCP tools, no
  CHECKING→ISSUED (lifecycle advances are human-only), no release/publish, no
  provider/egress changes.
- No writes under `projects/chirality-piping/core/**`, `schemas/**`,
  `core/handoff/**`. Tier-0 control-root writes only under
  `_DomainEngines/proposals/open_pipe_stress/**` or `_DomainEngines/bridge/**`
  (profile `agent_writable_paths`).
- Never edit: the ADOPTED profile (tier-0 CHANGE only); the three owner-retained
  self-check fixtures (governance register item 3); DEC-041 prose / DEC-051's
  "staged for CHANGE" wording (immutable history); the readiness assessment (deltas
  go in Loop Log entries, not the record).
- Cross-reference, never invent (K-INVENT-1). Two deliverables share the id
  DEL-10-03 (app-dev "OperationProposal Record and Human Gate Workflow" vs piping
  "Local FEA handoff data contract") — always name the repo; never merge their rows.

## Backlog (coarse; re-derive at step 0 — locations are where state is recorded)

### Lawful now — bridge lane (app-dev / tier-0)

- **app-dev DEL-10-03 result-schema tranche** (loop-1 brief
  `TRB-chirality-app-dev-DEL-10-03-2026-07-02`, CANDIDATE): close/annotate the open
  result-schema TBDs (Specification.md:19,43,44,48,62,64,65;
  Procedure.md:14,15,40,71,81,83,85; Datasheet.md:44,54; Guidance.md) by
  cross-referencing piping Rust shapes — e.g. `OperationOutcome`,
  `projects/chirality-piping/core/model_operations/operation_applier/src/lib.rs:118-141`
  — per FM-04_OperationProposal_merge.md:54-59. Note direction: FM-04 cites the
  deliverable's 7 TBDs; no back-pointer exists inside the deliverable.
- **app-dev DEL-10-01 refinement** (loop-1 brief
  `TRB-chirality-app-dev-DEL-10-01-2026-07-02`, CANDIDATE): same cross-reference
  pattern (Guidance.md:59-63) + dependency-closure annotation
  (Assessment_INSP-03_DEL-10-01.md:38,46). ResponsibleParty and doc-only issuance
  basis are human-shaped — excluded.
- **PKG-10 status-history wording repair** (INSP-03 High, ON-STRATEGY, size S:
  Assessment_INSP-03_DEL-10-03.md:37,52; Assessment_INSP-03_DEL-10-01.md:36) —
  in-fence with the two briefs above; wording only, no state advance.
- **PLAN_cross_tier.md reconciliation** (`_DomainEngines/bridge/BRIDGE_2026-06-21_
  tier0-prep/PLAN_cross_tier.md:40-41`, self-declared PROPOSAL): row 40 still says
  "blocked by D-T0-01" (ruled; REF-008 pin landed), row 41 bundles the headless CLI
  entrypoint into the DEC-042 prep lane (DEC-042 does not sanction it). Lawful under
  the bridge/** write lane; needs owner green-light on scope.

### Lawful now — piping lane (piping's own track unless the owner pulls it into this loop)

- **DEC-055 codification append** (SOFTWARE_DECOMP.md §12; highest entry DEC-054 at
  :624): the D-28 ruling exists (owner O-A 2026-07-01, packet §7); the §12 entry is a
  recording action per packet §8. Never edit DEC-041 (:611) in place.
- **D-21 packet preparation** (piping `_REGISTER.md:45` NOT_PREPARED (held); D-27
  prerequisite RULED at :51; `docs/PLAN.md:84`): prep permitted, adoption held.
- **DEC-042 design/spec items 1–2** (SOFTWARE_DECOMP.md:612): proposal→apply bridge +
  OperationSet→Plan schema extension; candidate-generation + schema-reconciliation
  design. Item 3 (retrieval index) is DONE per DEC-043 (:613) — do not re-plan.
- **Publish piping DEL-10-03 result schemas** (profile TBDs at
  open_pipe_stress.yaml:81,88,101,115 cite them; shapes live only in Rust today):
  lawful piping-loop deliverable work over its own governed lane.
- **Ordinary Phase E/R5 work** (`docs/PLAN.md:84`; open decision rows D-06, D-10b,
  D-20, D-05b et al.).

### Owner-gated (each unlock widens the loop surface)

- **D-APP-46** (app-dev `_REGISTER.md:57`, AWAITING_RULING) — keystone: package
  extraction → consumable harness contract → proven L2 → opens the F3 sequence
  (D-T0-08) and the DEC-041 automation condition.
- **D-APP-45** (app-dev `_REGISTER.md:56`, AWAITING_RULING) — Flow-A contract version.
  D-28's binding rule is RULED (count from live `event-schema.ts`, 43 verified at
  source 2026-07-02) but pin EXECUTION stays gated (D-28 §5).
- **D-21 adoption** (held) — piping SCOPE_CHANGE packet, owner lane.
- **Headless CLI entrypoint** (open_pipe_stress.yaml:103-107, TOOLMAKER handoff,
  un-built; brief stub exists in BRIDGE_2026-06-21_tier0-prep/) — needs its own
  piping-loop decision; NOT lawful prep today.
- **root docs/CONTRACT.md ratification** (DRAFT; per-invariant D-GOV-05 table).
- **piping DEL-10-03 status header/history mismatch** (IN_PROGRESS vs History
  CHECKING) — which surface is right is a human call (K-CONFLICT-1); part of the
  known drift-92 class.

## Owner-action queue (standing — re-derive each loop)

1. Adopt/decline the loop-1 CANDIDATE briefs (see Gate step for the adoption acts).
2. Rule D-APP-46 (keystone) and D-APP-45 when ready.
3. Direct whether piping-lane backlog items enter this loop or stay in piping's own
   sessions.
4. Maintenance calls surfaced by evidence runs: three self-check WARN
   `UNRESOLVED_SOURCE_REF`s (CHANGE_HANDOFF.md:27, D-T0-06:7, D-GOV-07:26 — the first
   two reference the removed DRAFT profile; D-T0-06 is fixture-adjacent) and
   PROFILE_STATUS.md's stale `open_pipe_stress.DRAFT.yaml` name — owner/CHANGE lane,
   not agent-writable.

## Loop Log (append-only)

- **2026-07-02 — Loop 1** (session of record for this plan). Discover: main
  `78a592fbf` clean; drift 92/154 all piping, flat vs recorded 92/101; self-check
  exit 0, REVIEW pins exact (2/1/0/1, DRAFT_BASIS_RULED_CLOSED=7 INFO, GEN-8=19
  files), WARN=3 UNRESOLVED_SOURCE_REF (pre-existing, un-enumerated by prior
  baseline); pytest 236 passed (+1 vs baseline = PR #12's new
  `test_adapter_domain_engines.py` test). Spot-verify: 7-agent sweep, zero refuted;
  deltas: DEC-042 item 3 already built (DEC-043), D-APP-44 is RULED Option A (not
  open), no new rulings since the 2026-07-02 assessment; D-28's 43-count verified at
  source (`event-schema.ts`). Select+Brief: CANDIDATE briefs generated with
  practitioner objectives for app-dev DEL-10-03 and DEL-10-01
  (`_harness_generated/briefs/TRB-chirality-app-dev-DEL-10-0{3,1}-2026-07-02.md`).
  Gate: STOPPED awaiting owner adoption. No governed files changed except this plan
  file (bridge/** lane, owner-directed).
  Gate outcome (same day): owner adopted BOTH briefs in-session, directed this plan to
  ride main, granted repo-wide write scope for this loop, and pulled the piping-lane
  backlog into the loop "as appropriate" — execution proceeds in Loop 1; results
  appended below on close.
