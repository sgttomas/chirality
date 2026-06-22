# PLAN - Inspection-Orphan Remediation Queue

**Status:** ACTIVE (governing queue). Authorized by owner directive 2026-06-21.
**Persona:** WORKING_ITEMS
**Authority basis:** D-APP-39 (autonomous pull-and-execute, autonomous commit+push, governance
no-self-rule gate) + the owner's 2026-06-21 directive to incorporate the inspection-orphan addendum into
the coordination/development-loop documents and open it for implementation.
**Backlog source:** `plans/artifacts/insp05_roadmap_addendum_2026-06-21_inspection_orphans.md`
(`ORN-01`..`ORN-13`).
**Mode:** pull-and-execute — the same discipline as the now-exhausted D-APP-39 autonomous development
queue (`plans/PLAN_2026-06-20_autonomous_development_queue.md`), applied to a new backlog.

## 1. Purpose

Schedule the in-scope, non-fenced gaps that the INSP-05 synthesis compressed out and the prior autonomous
queue never captured (pre-issuance hardening). None of these disturb the resting state or regress shipped
work; the post-run audit confirmed `tsc` clean, 551/551 `vitest`, and all four hard fences held. This
queue continues the D-APP-39 autonomous posture on the authorized addendum backlog.

## 2. Eligibility Model

Each item is `AUTONOMOUS` unless it crosses a **hard fence** or requires a **new decision**. The fences
and gate are identical to the autonomous-queue plan §2 (as tightened 2026-06-21):

**Hard fences (always HUMAN-GATED):**
1. Provider/network expansion beyond the Anthropic path. *(Reconciled by D-APP-44, ruled 2026-06-21: now
   an owner-permitted, default-closed provider/residency configuration per tier-0 D-T0-04 — not a
   categorical deny; absent an explicit owner config the Anthropic loopback default stands and the harness
   never auto-egresses. See `execution/_Coordination/_DECISIONS/D-APP-44_RULING_2026-06-21.md`.)*
2. Release/distribution posture — signing, notarization, publication, external distribution, or any
   release-readiness / professional / certification / sealing / authentication / code-compliance claim.
3. R7 domain-engine implementation; PKG-10 stays future-boundary/doc-only.
4. Any `CHECKING -> ISSUED` deliverable issuance.

**Decision latitude (initiative expected).** Within the hard fences, resolve design forks yourself under
the owner's standing steer — favor the most stable, consistent long-term outcome; no
backward-compatibility preference; cleanup is acceptable. Make the call, proceed, and note it in the
tranche closeout as a WORKING_ITEMS decision with its rationale; do not stop to ask. Default to deciding,
not escalating — the owner would rather ratify a sound call after the fact than rule on a trivial fork up
front. Two limits hold:

1. **Truthful attribution.** Record agent decisions as the agent's own. Never attribute a choice to the
   owner that the owner did not make, never write a `*_RULING_*.md` or a `RULED` register row asserting an
   owner ruling that did not occur, and never claim a human approval or approval-SHA you do not hold
   (K-AUTH). `*_RULING_*` files and `RULED` rows remain the owner's instrument; agent decisions are
   recorded in the closeout, not there.
2. **Escalate only the genuinely material or hard-to-reverse:** a hard-fence question; a strategy-level
   (K-ENGINE-6) fork; a costly or irreversible public-contract or data-migration change; or a fork you
   cannot confidently resolve under the standing steer. Raise those as a `PROPOSAL` packet, mark the item
   `BLOCKED` for an owner ruling, and keep the queue moving on everything else.

A fenced sub-part of an otherwise-eligible item is split: the eligible portion proceeds; the fenced
portion is deferred with a note. (`ORN-01` CI plumbing runs existing checks and makes no release-readiness
claim — it does not cross fence #2.)

## 3. Selection Rule

1. **Verify-first for REPORTED items.** `ORN-05`..`ORN-13` are inspection-surfaced but were not
   overseer-verified. Before executing any REPORTED item, re-confirm it is still open in current
   source/tests/evidence (recompute; do not trust this table). **Drop any already-closed item** and record
   the screen-out (precedent: the addendum §6 screened out the Section 9 validator-ID mismatch, already
   reconciled by ADQ-04). Roughly 1 in 4 spot-checks was a false positive, so expect some drops.
2. `ORN-01`..`ORN-04` are VERIFIED/CORRECTED (confirmed open) and may be executed directly.
3. **Execute `ORN-01` (CI enforcement) first** — it is the meta-gate that makes every other gate
   enforceable on a PR.
4. Otherwise pick the highest-priority `READY`, `AUTONOMOUS` item whose prerequisites are met; execute,
   validate, commit+push.
5. The hard fences and the §2 decision-latitude limits stand. Never revive a completed/closed/superseded
   plan; never invent work outside this backlog and the addendum.

## 4. Validation Gates (must pass before commit)

- **Runtime/UI items:** `tsc` typecheck; `vitest` (full suite or a cited scope with rationale);
  `next build` / `desktop:pack` / `harness:validate:premerge` where the change warrants; the D-APP-36
  component/render bar for UI items. Honor the validation/server isolation rule (stop the dev server
  before build/pack/premerge).
- **Governance/docs items:** `git diff --check`; reference/link existence; stale-pointer search; the
  D-APP-38 reconciliation tool (`reconcile_authority_corpus.py status|bump|apply`) whenever an authority
  document changes.
- **CI item (`ORN-01`):** prove the new CI steps actually run the checks (typecheck, vitest,
  instruction-root integrity, release-quality wrapper) and that the summary-artifact path matches the
  spec; CI plumbing only — no release-readiness claim.
- **Recompute, do not trust recorded metadata.** Verify against the filesystem, tests, and live tools.

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

## 7. Backlog (transposed from the addendum; see it for full detail)

Status: `READY` = eligible and unblocked. Verification: VERIFIED / CORRECTED = confirmed open;
REPORTED = re-verify per §3.1 before executing.

| ID | Item | Source DEL | Type | Size | Severity | Verification | Status |
|---|---|---|---:|---|---|---|---|
| ORN-01 | Wire CI to enforce the gates (typecheck + vitest + instruction-root integrity + release-quality wrapper); resolve the stable-summary path conflict | DEL-09-01/05 | validation/CI | M | HIGH | VERIFIED | READY (do first) |
| ORN-02 | Sanitize the blocked-URL log at `electron/main.ts:119` (no raw `details.url`) | DEL-09-06 | code/security | S | MEDIUM | VERIFIED | READY |
| ORN-03 | Restore/realign the UI-polish acceptance source (`docs/ui/UI_POLISH_EXECUTION_PLAN.md` absent → DEL-02-04 REQ-014) | DEL-02-04 | docs/UI | S | MEDIUM | VERIFIED | READY |
| ORN-04 | Mirror the read-path symlink guard on the dependency write path (defense-in-depth) | DEL-07-05 | code | S | LOW/MED | CORRECTED | READY |
| ORN-05 | Working-root `/api/working-root/validate` parity + route tests | DEL-07-01 | code/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-06 | Permission-invariant test: SDK options always include `canUseTool` + `hooks` where write/shell tools exposed | DEL-06-01 | test | S | MEDIUM | REPORTED | READY (verify first) |
| ORN-07 | Register retire-vs-delete diff vs `previousRows` in `register-writer.ts` | DEL-07-05 | code/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-08 | Runtime error-taxonomy ownership (PKG-03/04/05) + `api-key-settings` render test | DEL-02-05 | code/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-09 | Client-disconnect durable cancellation persistence + accepted raw-input recovery + SSE fixture index | DEL-03-03/04 | code/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-10 | Section 9 summary/manifest maturity (warnings/blockers/evidence manifest) + compaction-boundary fixtures | DEL-09-02 | validation/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-11 | Consolidated runtime redaction-path matrix | DEL-05-03 | security/test | M | MEDIUM | REPORTED | READY (verify first) |
| ORN-12 | Failed-send retry end-to-end (draft + attachment across API failure) | DEL-09-06 | UI/test | S | MEDIUM | REPORTED | READY (verify first) |
| ORN-13 | Refresh CODEV-001 first-adapter probe record to cite landed ADQ-04/ADQ-15 evidence (hard closure partly dependency-row-gated) | DEL-04-01/02/03 | docs/evidence | M | MEDIUM | REPORTED | READY (verify first) |

The agent re-derives readiness at selection time (recompute; do not trust this table if the filesystem
disagrees). Items excluded from this tranche (issuance, dependency rows, R7, provider/release posture,
D-APP-42 Option C, separate-ruling items) are listed in the addendum §5 and stay out of scope.

## 8. Boundaries / Out of Scope

The four hard fences (§2) and the governance no-self-rule gate stand. No reviving
completed/closed/superseded plans. Keep the public UIEvent contract, permission plane, and provider
posture intact unless an item explicitly and eligibly changes them within fence limits. CONTRACT
K-ENGINE-6 applies to every item — standalone-harness or Claude Code / Pi / Codex parity work is
OFF-STRATEGY.

## 9. Finalization

When the eligible queue is empty (all items `DONE`, `BLOCKED` on decisions, or dropped as already-closed),
record closeout in `plans/PLAN_COMPLETION_LOG.md`, leave any decision/blocker queue for the owner, and
stop. New work beyond this backlog requires a roadmap update or a human directive.
