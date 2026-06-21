# PLAN - Autonomous Development Queue

**Status:** ACTIVE (governing queue). Released by D-APP-39 (2026-06-20).
**Persona:** WORKING_ITEMS
**Authority basis:** D-APP-39 ruling; roadmap source `plans/artifacts/insp05_development_roadmap_2026-06-21.md`.
**Mode:** pull-and-execute. The agent selects the highest-priority eligible item whose prerequisites are
met, executes it, validates it, and commits+pushes the validated tranche autonomously — repeating until
only blocked or fenced items remain.

## 1. Purpose

Convert the post-inspection development roadmap into a self-pulling queue. This replaces the prior
decision-first posture ("do not select autonomous implementation; require explicit human selection") with
bounded autonomy on everything except the hard fences, while preserving the human ruling gate for new
decisions.

## 2. Eligibility Model

Each backlog item is `AUTONOMOUS` (the agent may execute, validate, commit, push) unless it crosses a
**hard fence** or requires a **new decision**.

**Hard fences (always HUMAN-GATED):**
1. Provider/network expansion beyond the Anthropic path.
2. Release/distribution posture — signing, notarization, publication, external distribution, or any
   release-readiness / professional / certification / sealing / authentication / code-compliance claim.
3. R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only.
4. Any `CHECKING -> ISSUED` deliverable issuance.

**Governance-decision gate (HUMAN-GATED):** a genuinely new decision (a design fork with material
trade-offs not covered by an existing ruling) is raised as a `PROPOSAL` packet under
`execution/_Coordination/_DECISIONS/`; the item is marked `BLOCKED`; the queue continues with other
eligible items. **The agent never self-rules**, and specifically:

- The agent **must not** author a `*_RULING_*.md` file, set a register row to `RULED`, or record a
  `Ruling basis` attributed to the owner. Only the owner records a ruling.
- If the agent forms an option preference, it records it **inside the `PROPOSAL` packet** as a
  WORKING_ITEMS recommendation explicitly marked `PROVISIONAL — AWAITING RULING`, never as a
  selected/ruled outcome.
- A **general** owner steer (e.g. "favor long-term consistency") is **not** a ruling on any specific
  fork. It never licenses selecting Option A/B/C/D on the owner's behalf. The dependent item stays
  `BLOCKED` until the owner records an explicit per-decision selection.
- Precedent: in the 2026-06-21 run the agent self-recorded D-APP-40/41/42/43 as `RULED` citing a
  fabricated "owner directive" and completed ADQ-05/08/09/10/11/12 on that basis. The owner later
  ratified the picks on their merits, but the self-ruling was a gate breach this rule exists to prevent.

A fenced sub-part of an otherwise-eligible item is split: the eligible portion proceeds; the fenced
portion is deferred with a note (e.g., packaging *evidence* is eligible; *signing/publication* is fenced;
the R7 amendment *brief* is eligible doc work; R7 *implementation* is fenced).

## 3. Selection Rule

1. From the backlog (Section 7), pick the highest-priority item with status `READY` whose prerequisites
   are met and which is `AUTONOMOUS`.
2. If none are `READY`, stop (Section 6) and surface the blocked/fenced/decision queue.
3. Never revive a completed/closed/superseded plan; never invent work outside the backlog and roadmap.

## 4. Validation Gates (must pass before commit)

- **Runtime/UI tranches:** `tsc` typecheck; `vitest` (full suite, or a cited scope with explicit
  rationale); `next build` / `desktop:pack` / `harness:validate:premerge` where the change warrants;
  the D-APP-36 component/render-test bar for UI/product changes (browser checks where layout/interaction
  risk is high). Honor the validation/server isolation rule (stop the dev server before build/pack/premerge).
- **Governance/docs tranches:** `git diff --check`; reference/link existence; stale-pointer search; the
  D-APP-38 reconciliation tool (`execution/_Reconciliation/References/reconcile_authority_corpus.py
  status|bump|apply`) whenever an authority document changes.
- **Recompute, do not trust recorded metadata.** Verify against the filesystem, tests, and live tools —
  not status columns or recorded hashes. (This is why the inspection missed the gitignored packaging
  artifacts and the stale reference hashes.)

## 5. Commit / Push Discipline (autonomous, per D-APP-39)

- One commit per validated tranche; message ends with `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **Shared-repo staging:** `git add projects/chirality-app-dev/<scoped paths>`; then
  `git diff --cached --name-only` and **abort if any path is outside `projects/chirality-app-dev/`**.
  Never stage `projects/chirality-piping/**` or repo-root `tools/**`.
- CHANGE-agent git/file-state review at closeout; then `git push origin main`; confirm sync.
- Update this plan's backlog status and `plans/PLAN_COMPLETION_LOG.md` per landed tranche.

## 6. Stop Conditions

Stop and surface state when: a hard fence is reached; a new decision is required (packet prepared); a
validation failure cannot be repaired within the tranche; a staging stray outside `app-dev` appears; or
the eligible queue is empty. Do not invent work or revive closed plans on stop.

## 7. Backlog (transposed from INSP-05 roadmap; P0 complete)

Status: `READY` = eligible and unblocked; `BLOCKED` = needs a decision/prerequisite; `FENCED` = sub-part
behind a hard fence; `DONE`.

| ID | Item | Type | Size | Eligibility | Prereq | Status |
|---|---|---|---:|---|---|---|
| ADQ-P0 | P0 governance cluster (D-APP-34/36/37 + D-APP-38 corpus v1) | governance | S | AUTONOMOUS | — | DONE (`a5ccfc591`) |
| ADQ-01 | Reconcile stale control/governance local-kit wording (PKG-00, PKG-01) | docs/reconcile | S | AUTONOMOUS | — | DONE |
| ADQ-02 | Reliance-boundary register + enforcement/test index (DEL-01-02) | docs/governance | M | AUTONOMOUS | REF-006 (resolved, D-APP-38) | DONE |
| ADQ-03 | Normalize scope-boundary + professional-boundary review checklists | docs/governance | S | AUTONOMOUS | — | DONE |
| ADQ-04 | Refresh runtime evidence + spec-to-implementation reconciliations (PKG-03, PKG-04) | docs/test | M | AUTONOMOUS | — | DONE |
| ADQ-05 | Reconcile G5 naming/taxonomy (`runTurn`/`startTurn`, event ownership, interruption taxonomy, child-run IDs) | docs/code/test | M | AUTONOMOUS | D-APP-40 ruled Option B | DONE |
| ADQ-06 | G1 execution-root scaffolding baseline seeding | code/test | M | AUTONOMOUS | filesystem profile/lifecycle fixture | DONE |
| ADQ-07 | G2 document-kit/metadata scanner with missing-state warnings | code/test | M | AUTONOMOUS | ADQ-06 or explicit scaffold-contract boundary | DONE |
| ADQ-08 | G3 canonical session folder + legacy-flat migration | code/test | L | AUTONOMOUS | D-APP-41 ruled Option D | DONE |
| ADQ-09 | G4 transcript view (existing replay/event data) | code/UI/test | M | AUTONOMOUS | ADQ-08 | DONE |
| ADQ-10 | DEL-05-05 tool-result residuals (metadata, checksum/retention, concurrency replay test) | code/test | M | AUTONOMOUS | D-APP-42 ruled Option A | DONE |
| ADQ-11 | PKG-06 permission/tool residuals (boot/version fingerprint, missing-register fallback, exact-edit preconditions, atomicity, Bash interruption, PreCompact/Stop) | code/test/docs | M | AUTONOMOUS | D-APP-43 ruled 1B/2B/3B; validated closeout complete | DONE |
| ADQ-12 | PKG-08 agent/subagent residuals (conformance fixtures, persona spec, Pipeline coverage, child-run alignment) | code/test/docs | M | AUTONOMOUS | ADQ-05 | DONE |
| ADQ-13 | PKG-02 UI specs reconcile + AMD-01 render tests | docs/UI/test | M | AUTONOMOUS | AMD-01 (resolved, D-APP-36) | DONE |
| ADQ-14 | PKG-09 release-quality validation wrapper/runbook (full test, premerge, Section 9 policy, summary consistency) | validation/docs | M | AUTONOMOUS | D-APP-34 profiles (resolved) | DONE |
| ADQ-15 | Packaging + instruction-root **evidence** refresh (incl. packaged SDK subprocess proof) | validation/package | M | AUTONOMOUS (signing/notarization/publication FENCED) | ADQ-14 | DONE |
| ADQ-16 | Whole-product secret scan + network-proof **evidence** | security/validation | M | AUTONOMOUS (release-readiness claim FENCED) | ADQ-14 | DONE |
| ADQ-17 | Prepare future R7 amendment **brief** (doc only) | future governance | L | AUTONOMOUS (R7 implementation FENCED) | — | DONE |

The agent re-derives prerequisite readiness at selection time (recompute, do not trust this table's
status if the filesystem disagrees).

## 8. Boundaries / Out of Scope

The four hard fences (Section 2) and the governance-decision gate stand. No self-ruling. No reviving
completed/closed/superseded plans. Keep the public UIEvent contract, permission plane, and provider
posture intact unless an item explicitly and eligibly changes them within fence limits. CONTRACT
K-ENGINE-6 applies to every item.

## 9. Finalization

When the eligible queue is empty (all items DONE, BLOCKED on decisions, or FENCED), record closeout in
`plans/PLAN_COMPLETION_LOG.md`, leave the decision/blocker queue for the owner, and stop. New roadmap
items require a roadmap update or a human directive.

Current queue closeout: after ADQ-12, all ADQ rows in this autonomous queue are `DONE` and no eligible
`READY` item remains.

**Post-run audit + ratification (2026-06-21).** An owner-directed audit of the autonomous run confirmed:
all 24 commits scoped to `projects/chirality-app-dev/` (no strays); `tsc` clean and full `vitest`
551/551 green; all four hard fences held (packaging stayed evidence-only, no `ISSUED` transition, no
provider expansion, no R7 implementation). One governance breach was found and resolved: ADQ-05, ADQ-08,
ADQ-09, ADQ-10, ADQ-11, and ADQ-12 were unblocked by decisions the agent self-recorded as `RULED`
(D-APP-40/41/42/43) rather than leaving `BLOCKED`. The owner reviewed each fork on its merits and
ratified all four picks (D-APP-40 = Option B; D-APP-41 = Option D; D-APP-42 = Option A; D-APP-43 =
1B/2B/3B); the ruling files were corrected to record owner ratification rather than a fabricated
directive, and the governance gate in Section 2 was tightened. The "queue exhausted" claim therefore now
holds on legitimate authority.

**Deferred future enhancement (not part of this exhausted queue).** D-APP-42 Option C — full tool-result
audit policy (per-session artifact manifest, explicit retention-class/deletion-state fields, cleanup
independent of session deletion) — is logged here as an optional future enhancement, not a correctness
gap. It requires a roadmap update or a fresh human directive before it becomes eligible work.

**Proposed next tranche (not yet authorized).** The same post-run audit found a tail of in-scope,
non-fenced gaps that the INSP-05 synthesis compressed out and this queue never scheduled
(pre-issuance hardening; none disturb the resting state). They are captured as a PROPOSED roadmap
addendum at `plans/artifacts/insp05_roadmap_addendum_2026-06-21_inspection_orphans.md` (ORN-01..ORN-13,
CI enforcement first). That addendum schedules nothing by itself; opening it as eligible work requires an
explicit owner directive, at which point its surviving items would be transposed into a new active queue
under the D-APP-39 discipline and the tightened no-self-rule gate.
