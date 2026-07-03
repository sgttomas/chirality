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
  **[EXECUTED Loop 1 at `4968ed485`; brief HUMAN_ADOPTED, awaiting owner
  review→CLOSED. Loop 2 verified no lawful in-fence agent work remains — all
  residue is human-shaped or gate-blocked.]**
- **app-dev DEL-10-01 refinement** (loop-1 brief
  `TRB-chirality-app-dev-DEL-10-01-2026-07-02`, CANDIDATE): same cross-reference
  pattern (Guidance.md:59-63) + dependency-closure annotation
  (Assessment_INSP-03_DEL-10-01.md:38,46). ResponsibleParty and doc-only issuance
  basis are human-shaped — excluded.
  **[EXECUTED Loop 1 at `9a29c0372`; brief HUMAN_ADOPTED, awaiting owner
  review→CLOSED. Same Loop 2 residual verdict as DEL-10-03.]**
- **PKG-10 status-history wording repair** (INSP-03 High, ON-STRATEGY, size S:
  Assessment_INSP-03_DEL-10-03.md:37,52; Assessment_INSP-03_DEL-10-01.md:36) —
  in-fence with the two briefs above; wording only, no state advance.
  **[DONE Loop 1 — MEMORY.md forward-corrections in both deliverables.]**
- **PLAN_cross_tier.md reconciliation** (`_DomainEngines/bridge/BRIDGE_2026-06-21_
  tier0-prep/PLAN_cross_tier.md:40-41`, self-declared PROPOSAL): row 40 still says
  "blocked by D-T0-01" (ruled; REF-008 pin landed), row 41 bundles the headless CLI
  entrypoint into the DEC-042 prep lane (DEC-042 does not sanction it). Lawful under
  the bridge/** write lane; needs owner green-light on scope.
  **[DONE Loop 1 at `d0b53d851`; the reconciled who-does-what rows now sit at
  PLAN_cross_tier.md:47-48 (line drift from the :40-41 cited above).]**

### Lawful now — piping lane (piping's own track unless the owner pulls it into this loop)

- **DEC-055 codification append** (SOFTWARE_DECOMP.md §12; highest entry DEC-054 at
  :624): the D-28 ruling exists (owner O-A 2026-07-01, packet §7); the §12 entry is a
  recording action per packet §8. Never edit DEC-041 (:611) in place.
  **[DONE Loop 1 at `a0c50e5aa` — DEC-055 at SOFTWARE_DECOMP.md:625; D-28 register
  row points at it; DEC-041 untouched.]**
- **D-21 packet preparation** (piping `_REGISTER.md:45` NOT_PREPARED (held); D-27
  prerequisite RULED at :51; `docs/PLAN.md:84`): prep permitted, adoption held.
  **[EXECUTED Loop 2 — PR #14 (`loop2/d21-packet-prep`): packet + register row
  → AWAITING_RULING (adoption held). Owner: review/merge, then rule D-21.]**
- **DEC-042 design/spec items 1–2** (SOFTWARE_DECOMP.md:612): proposal→apply bridge +
  OperationSet→Plan schema extension; candidate-generation + schema-reconciliation
  design. Item 3 (retrieval index) is DONE per DEC-043 (:613) — do not re-plan.
  **[EXECUTED Loop 2 — PR #15 (`loop2/dec042-design-docs`): two design docs in
  piping `plans/` under DEC-042's fence-free prep sanction (no deliverable created —
  where the designs land, DEL-16-05 via decomposition or DEL-16-01 amendment,
  stays the owner's choice, presented in both docs). Note: the app-dev harness has
  NO formal Plan type today; the OperationSet→Plan extension is a piping-side
  envelope with the app-dev half left OPEN.]**
- **Publish piping DEL-10-03 result schemas** (profile TBDs at
  open_pipe_stress.yaml:81,88,101,115 cite them; shapes live only in Rust today):
  lawful piping-loop deliverable work over its own governed lane.
  **[DONE Loop 1 at `a0c50e5aa` — `schemas/operation_outcome.schema.json` +
  `schemas/rule_check_run_result.schema.json` + stdlib contract tests; the profile
  hook fields themselves stay TBD pending the owner tier-0 CHANGE (queue item 2).]**
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

0. ~~**Merge PRs #17–#20** + fill the `Ruling SHA: TBD` fields.~~ DONE
   2026-07-02: owner merged all four (merge commits `1dccf54fd` #17 /
   `6c975774c` #18 / `f7c9e95b3` #19 / `f9626fa32` #20); post-merge tree
   verified — self-check INFO=8/NA=1/REVIEW=23/WARN=2, drift 0/154, pytest
   239 passed. D-APP-45/46 ruling SHAs bound to `6c975774c` (PR #18 publication
   commit) in both records and register rows, owner-confirmed, at `940caa108`.
   (D-APP-44's own long-standing `ruling SHA TBD` left as-is — not in scope;
   flagged as optional future cleanup.)
   Newly unlocked lanes to direct WHEN the owner resumes development (parked
   pending the loop-reflection): (i) the D-21 SCA propagation workflow
   (PRD v0.2 supersession/delta + plan revision carrying Annex A + stage-token
   re-keying — authorized by DEC-056, not yet executed, piping lane); (ii) the
   package-extraction tranche (D-APP-46 Option A — next loop's headline brief);
   (iii) tier-0 CHANGE candidates now stale: profile `:143` gate line (piping
   D-21 cleared) and piping register footer prose (~:64-65, :82 still say
   "D-21 remains held").
1. ~~Adopt/decline the loop-1 CANDIDATE briefs~~ DONE 2026-07-02 (both adopted,
   fences verified ACTIVE at `abafd4d24`). ~~Remaining brief lifecycle acts:
   HUMAN_REVIEWED → CLOSED on both~~ DONE 2026-07-02 (owner in-session sign-off
   R4; recorded on PR #18, verify-adoption terminal posture confirmed).
2. **Tier-0 CHANGE**: point the ADOPTED profile's four result-schema hook fields
   (`open_pipe_stress.yaml:81,88,101,115` `TBD # DEL-10-03`) at the schemas published
   2026-07-02 (`projects/chirality-piping/schemas/operation_outcome.schema.json`,
   `rule_check_run_result.schema.json`). Owner act; unblocked by Loop 1.
   **Loop 2 prepared it to one-commit readiness: PR #16 carries the CHANGE packet
   (exact before/after per line; the :101 n/a nuance presented as your choice;
   validator re-run steps; SHA-binding commit text). Note the packet's tasking
   correction: :143 needs NO edit (it is the live-binding gate line, not the
   schema-TBD line — this queue item's own ":143" framing in earlier drafts was
   imprecise); the consequential comment edit is at :72-74.**
3. ~~Rule D-APP-46 (keystone) and D-APP-45 when ready.~~ DONE 2026-07-02
   (in-session: D-APP-46 Option A "I approve …"; D-APP-45 "I approve your
   recommendation." — both recorded on PR #18 per the D-APP-44 pattern;
   Ruling SHAs bind at merge).
4. ~~Direct whether the remaining piping-lane backlog (DEC-042 items 1–2 design
   docs; D-21 packet prep) runs in the next loop iteration or in piping's own
   sessions.~~ DIRECTED 2026-07-02 (owner, in-session: "execute all items, working
   in parallel when write scopes are mutually exclusive") and EXECUTED same day —
   PRs #14 (D-21 packet), #15 (DEC-042 items 1–2 design docs), #16 (tier-0 CHANGE
   prep). Remaining owner acts on this item: review/merge the three PRs; confirm
   at D-21 ruling time the packet's §2 read that your direction superseded
   DEC-042's "no packet is prepared while held" clause for PREPARATION only; and
   choose where the DEC-042 designs land if adopted (new design deliverable via
   decomposition vs DEL-16-01 Spec amendment — both docs present the options
   without choosing).
5. ~~Harness defects surfaced by Loop 1 (spin-off task chip created)~~ DONE
   2026-07-02 (owner-merged PR #13 at `d925b0b51`, fix `7da70fbf5`): evidence
   records now self-label `authority_class: generated_view` (GEN-3 clean with
   evidence present, live at `evidence_records.py:150` / `cmd_self_check.py:492`);
   GEN-5 strips brief-format trailing parentheticals (the 8 brief-format WARNs are
   gone). Verified by Loop 2 measurements: self-check exit 0, WARN back to the 3
   pre-existing; pytest 239 (+3 regression tests).
6. Maintenance calls surfaced by evidence runs: the three pre-existing WARN
   `UNRESOLVED_SOURCE_REF`s (CHANGE_HANDOFF.md:27, D-T0-06:7, D-GOV-07:26 — the first
   two reference the removed DRAFT profile; D-T0-06 is fixture-adjacent) and
   PROFILE_STATUS.md's stale `open_pipe_stress.DRAFT.yaml` name — owner/CHANGE lane,
   not agent-writable. Also: piping DEL-10-03 `_STATUS.md` header/history mismatch
   (K-CONFLICT-1 human call). **Loop 2 additions: PR #16 §4 carries ready-to-apply
   proposals for each of these (with fixture-adjacent cautions and
   record-immutability defaults). New environment fact from Loop 2 worktree runs:
   the WARN=3 self-check baseline holds only where untracked artifacts exist on
   disk — a fresh clone/worktree measures WARN=8, because four refs in the two
   committed adopted briefs point at gitignored `_harness_generated/` paths and
   CHANGE_HANDOFF.md:41 cites the empty untracked proposals dir. PR #16 §3
   documents it with an optional fix; fresh-checkout readers should expect 8.**

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
  Execution (same day, main-direct at owner direction): adoption recorded and both
  fences verified ACTIVE at `abafd4d24` (first adopted briefs in this repo's
  history). Piping lane at `a0c50e5aa`: published
  `schemas/operation_outcome.schema.json` + `schemas/rule_check_run_result.schema.json`
  (derived field-by-field from the operation_applier / rule_check_runner Rust sources,
  which govern) + stdlib contract tests; appended `DEC-055` to SOFTWARE_DECOMP.md §12
  per the D-28 packet §8 mechanism (DEC-041 untouched) and pointed the D-28 register
  note at it. App-dev DEL-10-03 tranche at `4968ed485`: result-schema TBDs closed by
  cross-reference, adapter/record TBDs narrowed with residuals explicit, INSP-03
  status-wording repaired as a MEMORY forward-correction (`_STATUS.md` needed no
  change — already qualified). App-dev DEL-10-01 tranche at `9a29c0372`:
  Guidance cross-reference note, `_DEPENDENCIES.md` annotate-only satisfaction
  evidence for the three anchors (CSV untouched). Bridge lane (this commit):
  PLAN_cross_tier.md rows 40–41 reconciled (tier-1 DONE markers; entrypoint
  unbundled from the DEC-042 lane). Checks: scope-check clean both tranches
  (5/5 and 3/3 in-fence, 0 prohibited); run-validations + evidence-check 3/3 both
  briefs; closeout digests produced; piping pytest full suite passed; harness
  pytest 236 passed; drift 92/154 flat; self-check exit 0 after deleting the
  scratch evidence records (rebuildable; D-GOV-01). New harness defects surfaced
  and queued (owner-action queue items 5–6). Deferred to next loop: DEC-042
  items 1–2 design docs; D-21 packet prep (pending owner direction on lane).

- **2026-07-02 — Loop 2.** Discover: main `054f9f4db` clean, five commits past the
  Loop 1 close (`d0b53d851`) — owner-merged PR #13 harness fix (`7da70fbf5`) plus
  three owner LOOP_INIT.md bridge commits; full-diff confirms NO register,
  decision, profile, or governed-record changes in that range, so no new rulings
  landed. Measurements: status ×3 no severities (app-dev 53 / piping 101 status
  files; tier-0 contradiction pointer 5); drift 92/154 flat vs recorded 92/101;
  self-check exit 0 with REVIEW=23 (pins exact vs Loop 1: 2/1/0/1 + GEN-8 19
  files), INFO=9, WARN=3 — the 8 brief-format GEN-5 WARNs are gone and evidence
  records self-label for GEN-3, i.e. queue item 5 is discharged by PR #13
  (verified at `evidence_records.py:150` / `cmd_self_check.py:492`); pytest 239
  passed (+3 = PR #13's regression tests); `next`: app-dev 53 CHECKING, piping
  8 CHECKING / 92 IN_PROGRESS / 1 ISSUED. Spot-verify: 7-agent sweep (registers,
  Loop 1 outputs, adopted-fence residuals, DEC-042 lane, D-21 packet scope,
  readiness §1, completeness critic) — zero substantive refutations; both briefs
  still HUMAN_ADOPTED (owner review→CLOSED pending); profile hook fields still
  TBD ×4 (queue item 2 open); D-APP-45/46 AWAITING_RULING (app-dev register
  :56-57); D-21 NOT_PREPARED (held) (piping register :45). Deltas vs the maps
  (recorded here, maps never edited): (1) readiness §7 "9 RULED tier-0 register
  rows" is a MISCOUNT — the live register has exactly 8 (D-T0-01..08 at
  `_DomainEngines/_DECISIONS/_REGISTER.md:7-14`); the ninth "RULED" match is the
  register's title line. (2) readiness §1.1 cites the FM-04 record under
  `_DomainEngines/proposals/open_pipe_stress/` — that directory is empty; the live
  FM records sit under `bridge/BRIDGE_2026-06-21_tier0-prep/framework_maintenance/`.
  (3) PLAN_cross_tier who-does-what rows drifted to :47-48 (map cites :40-41);
  substance of the Loop 1 reconciliation holds. (4) readiness §1.3's "DEC-055
  still pending" is cleared (Loop 1 appended it; live at SOFTWARE_DECOMP.md:625).
  (5) piping DEL-10-03 header/history mismatch unchanged (IN_PROGRESS `_STATUS.md:3`
  vs CHECKING history :15 — known drift-92 class, K-CONFLICT-1 human call).
  Select: NO lawful agent tranche exists outside the owner gates this iteration —
  the two adopted fences are fully discharged (every remaining residual is
  human-shaped or gate-blocked: ResponsibleParty, issuance basis/INSP-04,
  _SEMANTIC_LENSING HumanRuling=TBD rows, SatisfactionStatus judgments, profile
  hook fields in a prohibited path), the tier-0 proposals lane is empty by design,
  and both open backlog items are piping-lane pending queue-item-4 direction.
  Loop 2 instead sharpened the gate: D-21 packet prep is execution-ready (one new
  file `execution/_Coordination/_DECISIONS/D-21_prd_scope_change_v0_2_milestone_set.md`
  on the D-28 packet skeleton — PROPOSAL disclaimer; §2 verified-facts checked
  cold; §4 options adopt-v0.2-set / decline-terminate-at-R5 / adopt-delta; §7
  Human Ruling left OPEN; §8 mechanism DEC append + register row NOT_PREPARED→
  AWAITING_RULING; content = v0.2 scope delta (R6/R7 + inserted R3 from
  `docs/_ScopeChange/OpenPipeStress_PRD_v0.2.md`) + the mandatory
  traceability-breaking FR crosswalk (flat FR-001..025 → FR-MOD/KNOW/GUI/SOL/RULE/
  CMP/HAND/AGENT/REP per `plans/PLAN_2026-06-17_prd_completion.md:263`); prerequisite
  D-27 RULED; adoption hold intact); DEC-042 items 1–2 have NO owning deliverable
  (no PKG-16 Spec scopes them; no design artifact exists; DEL-16-05 slot free) —
  owner scoping act required on top of lane direction. Gate: STOPPED — no piping-lane
  writes, no briefs generated (nothing deliverable-shaped exists to fence: the D-21
  packet is coordination-level; DEC-042 items lack a deliverable). Work done this
  iteration (bridge lane, this commit): backlog rows executed in Loop 1 marked
  DONE; queue item 5 marked DONE (PR #13); queue item 4 sharpened with the
  execution-ready D-21 scope and the DEC-042 scoping sub-decision. Owner-action
  queue after this loop: items 1–4 and 6 open. Next iteration unlocks on any of:
  item 4 direction (D-21 packet prep executes immediately; DEC-042 items 1–2 once
  scoped), item 2 tier-0 CHANGE (closes the profile's four hook TBDs against the
  published schemas), D-APP-45/46 rulings (keystone: F3 sequence + DEC-041
  automation), or brief review→CLOSED (item 1 lifecycle completion).
  Gate outcome (same day): owner directed in-session — "Consider the dependencies
  and plan to execute all items, working in parallel when write scopes are
  mutually exclusive." Read as: queue-item-4 lane direction granted (piping-lane
  backlog runs in this loop); all agent-executable items proceed; owner-only acts
  (rulings, adoption, CHANGE application, brief CLOSED) stay owner-side as
  prepared packets.
  Execution (same day, branch-first + PR per protocol step 4 — Loop 1's
  main-direct grant was not assumed to extend): three parallel worktree branches
  with mutually exclusive write scopes, each implement→adversarial-review(→fix)
  verified, all three clean with zero BLOCKER/MAJOR findings (~115 citations
  cold-checked by independent reviewers). (1) PR #14 `loop2/d21-packet-prep`
  (`3b03430cb`): D-21 SCOPE_CHANGE packet on the D-28 skeleton — §7 Human Ruling
  literally OPEN, adoption hold intact; Annex A complete FR crosswalk, all 25 flat
  v0.1 FRs → v0.2 successors with dual citations (12 DIRECT / 7 SPLIT / 2 MERGE /
  2 NARROWED / 3 UNMAPPED, explained); register row 45 → AWAITING_RULING (adoption
  held) per the register's own precedented vocabulary (D-28 pre-ruling row doesn't
  exist in history — it landed RULED — so precedent taken from rows D-15..D-26 and
  D-28 §8's own token usage); piping pytest 369 passed in-worktree. Packet §2
  records the owner direction as superseding DEC-042's "no packet is prepared
  while held" clause for PREPARATION only — flagged for confirmation at ruling.
  (2) PR #15 `loop2/dec042-design-docs` (`adfebfcff`): DEC-042 items 1–2 design
  docs in piping `plans/` under the fence-free prep sanction; substantive
  discovery recorded in doc 1: the app-dev harness has NO formal Plan/step type
  today, so the OperationSet→Plan extension is a piping-side envelope with the
  app-dev half labeled OPEN; both docs state the three live gates and leave the
  landing spot (decomposition vs DEL-16-01 amendment) to the owner. (3) PR #16
  `loop2/tier0-change-prep` (`dd6dfb951`): tier-0 CHANGE packet for queue item 2 —
  exact before/after for :81/:88 → operation_outcome.schema.json, :115 →
  rule_check_run_result.schema.json, :101 as a reasoned owner choice, plus the
  :72-74 header-comment edit; ADOPTED profile byte-identical on the branch.
  Tasking correction caught in-execution (K-INVENT-1, tree governs): profile :143
  is the live-binding gate line, NOT a schema-TBD line — no :143 edit proposed;
  this entry corrects the Select paragraph's ":143 open_issues" framing above.
  New environment fact: fresh worktrees measure self-check WARN=8 (not 3) —
  four committed-brief refs point at gitignored `_harness_generated/` paths and
  CHANGE_HANDOFF.md:41 cites the untracked empty proposals dir; all three
  branches verified finding-neutral against a same-environment baseline (byte-
  identical finding sets), and the WARN=3 main-checkout baseline still holds.
  Checks: per-worktree harness self-check exit 0 ×3 (finding-neutral); piping
  pytest 369 passed (PR #14 worktree); CI governance-harness workflow green on
  all three PRs; scope containment re-verified by reviewers AND by the main loop
  (diffs: exactly 2 + 2 + 1 files, no overlaps). Owner queue after execution:
  item 1 (brief review→CLOSED), item 2 (apply PR #16's CHANGE after merge),
  item 3 (D-APP-45/46), item 4 residue (merge PRs #14/#15/#16; confirm the
  prep-supersession read at D-21 ruling; choose the DEC-042 design landing spot),
  item 6 (PR #16 §4 proposals; fresh-clone WARN=8 note). Owner merges — never
  self-merge (protocol step 5); this close-out commit rides main in the bridge
  lane like Loop 1's and c0934ca61 before it.
  Rulings round (same day, owner in-session): owner directed push→merge→rule;
  main pushed (`054f9f4db..7eabe0ff2`), PRs #14/#15/#16 owner-merged
  (`4f6846565`/`6d893e9eb`/`3e965f021`), merged tree self-check clean at the
  exact WARN=3 baseline. Owner then ruled the full slate: R1 D-21 = O-A with
  the §5 rider + sub-confirmation (i), §7 fill confirmed; R2 tier-0 CHANGE
  approved with :101 Option A + version bump, execution explicitly delegated;
  R3 DEC-042 designs stay in plans/ until R7 has weight; R4 briefs signed off;
  R5 D-APP-46 Option A + D-APP-45 recommendation approved; R6 (a)(b) adopted,
  (c)(d) defaults, (e) optional taken, (f) ruled "all shall be IN_PROGRESS"
  class-wide. Executed across five mutually-exclusive-scope branches (every
  one implement→adversarial-review clean, zero BLOCKER/MAJOR): PR #17
  `loop2/tier0-change-apply` (profile hooks bound ×4, :101 Option A,
  profile_version 0.1-DRAFT→0.2, validator VALID; CHANGE_HANDOFF:27 +
  PROFILE_STATUS + .gitkeep maintenance; D-T0-06/D-GOV-07 byte-untouched per
  defaults; live-pin fix `ca071b64f` after CI caught the regenerated
  validation report's transient worktree path — re-validated from the
  canonical checkout path, pin exactly-one ABS_PATH_IN_EVIDENCE holds). PR #18
  `loop2/rulings-record` (briefs CLOSED ×2, verify-adoption terminal posture
  confirmed; D-APP-46 + D-APP-45 RULED per the D-APP-44 pattern, Ruling SHAs
  TBD-until-merge). PR #19 `loop2/d21-ruled` (§7 filled per D-28 post-ruling
  precedent; DEC-056 appended at SOFTWARE_DECOMP.md:626; register row 45
  RULED; SCA propagation authorized NOT executed). PR #20
  `loop2/status-class-correction` (the R6(f) class ruling executed: 92
  reversal history entries authored — parser-verified as IN_PROGRESS
  assertions — Decision_Log at LIFECYCLE_CORRECTION_2026-07-02_2050 mirroring
  the 2026-05-11 precedent, _LATEST repointed, adapter baseline re-measured
  0/101; drift 92→0 over 154 files, reviewer re-derived the mismatch set
  byte-identical; conscious live-pin update 92/101→0/101 +
  prose_bullet_v1/README refresh in the same PR so CI is self-consistent).
  D-GOV-07:26 forward note per R6(d) default: the WARN stands as
  accepted-known; the decision record is not edited — this Loop Log entry is
  the forward note. Gate posture after this round: live-binding ×4 → piping
  D-21 CLEARED (DEC-056); tier-0 adoption already cleared; remaining two —
  app-dev F3 and DEC-041 automation — both route through the now-greenlit
  package extraction (D-APP-46 Option A). Owner acts remaining: merge
  PRs #17–#20 + fill the two Ruling SHAs (queue item 0); direct the SCA
  propagation and the extraction tranche when ready.
