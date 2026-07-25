# Woven Dialogue Redesign Handoff State

Status: `APPDEV_WOVEN_REDESIGN_IMPLEMENTATION_COMPLETE_PENDING_OWNER_MERGE`

Run: `APPDEV_WOVEN_REDESIGN_2026-07-24`
Branch: `feat/woven-redesign` (off `main@403f228f4`; upstream `main` merged at
`1cfd3e293`)
Date: 2026-07-24

Terminal state of this run: all seven stage/round commits are landed on the
branch, both independent verification instances returned green after their
findings were remedied, and the closeout records are written. The owner's merge
of the pull request is the remaining terminal integration act. This file is a
handoff state, not a lifecycle decision, a release-readiness claim, a
certification, or a professional approval.

## Accepted upstream basis

- `ADOPTED_BRIEF.md` — `TRB-APPDEV-WOVEN-REDESIGN-2026-07-24`, adopted by the
  owner in-session 2026-07-24 ("Adop the brief as-is. Proceed accordingly.")
  with defaults D1–D4, and with the calm-editorial direction ratified as the
  default setting and light mode as the primary target.
- `ORCHESTRATION_PLAN.md` v1, frozen before dispatch (posture MIXED; selection
  authority HUMAN for scope/models, AGENT_0 for the stage graph).
- Authority instruments of record: D-APP-74 / SCA-APP-004 (RULED 2026-07-23)
  for the target IA, and D-APP-36 for the render-evidence bar.
- Prior implementation basis reconciled under adopted default D4: PR #323
  (merge `403f228f4`, implementation commit `7941722f6`), whose evidence lives
  only in
  `execution/_Coordination/AgentRuns/APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/`.

## Derivative-package status

Everything below is derivative of that accepted basis and cites it; none of it
is decomposition truth or an authoritative snapshot.

- **V2 browser-evidence package** —
  `instances/V2-RENDER-EVIDENCE/EVIDENCE.md` plus `instances/V2-RENDER-EVIDENCE/evidence/`
  (70 PNG + 10 JSON, DPR-2). Current as of round 7 for the pre-upstream-merge
  tree; see the delta re-shoot requirement below. The declared fixture
  pass-through for `session/list` and `session/:id/events` is recorded in
  `EVIDENCE.md` §1.1 and bounds every session-bearing frame.
- **V1 invariant sweep** — `instances/V1-INVARIANT-SWEEP/RETURN.md`
  (`CONFIRMED 6/6`, one AA defect raised and remedied in round 6).
- **Stage returns and validations** — `instances/{A-TOKENS-CHROME,B1-IA-FOLD-LOGO,B2-NAV-SESSIONS,C-DEFECT-POLISH}/RETURN.md`
  and `instances/AGENT1-VALIDATOR/ROUND1..7_REVIEW.md`.
- **This run's closeout records** — the per-deliverable run records
  `R6_WOVEN_REDESIGN_2026-07-24.md` (DEL-02-01, DEL-02-02, DEL-02-04, DEL-08-03)
  and `R1_WOVEN_REDESIGN_2026-07-24.md` (DEL-05-04, DEL-08-02), the rewritten
  `## Remaining` sections in those six `_STATUS.md` files, the
  `plans/PLAN_COMPLETION_LOG.md` entry dated 2026-07-24, and the KG-033 update
  in `docs/PRD.md`.

On any disagreement, the adopted brief and the instance returns govern over
these derivative summaries.

## Closure verdict

Implementation complete; validation green; owner merge pending.

- Implementation: stages 0, A, B1 (+B3), B2 and C all landed and validated,
  with rounds 5–7 integration-owner remedies (`--ink-faint` AA, light
  `--accent` AA, disclosure clipping, composer placeholder, provenance-label
  track).
- Validation reproduced at each fan-in: typecheck pass; vitest 984 passed with
  4 skipped; production build pass; `git diff --check` clean; zero external
  network requests; all changed paths inside `projects/chirality-app-dev/**`.
- No lifecycle state changed anywhere. All six affected deliverables remain
  `IN_PROGRESS` with their `Authorization Basis`, `Directive` and
  `Checking Approval SHA` untouched.
- The legacy loop-first UI was not retired; that remains a separate owner
  decision after parity, per D-APP-74 and ADOPTED_BRIEF §1.

## Rerun requirements

- **Post-merge full gate run — owned by Agent 0.** Every figure in ROUND1–7 and
  in the V1/V2 returns was measured before `1cfd3e293` brought upstream PRs
  #324–#327 onto the branch. `npm run test`, `npm run typecheck`,
  `npm run build` and `npm run validate:release-quality` are to be re-run on the
  merged tree, with `frontend/artifacts/harness/release-quality/latest/summary.json`
  (+ section9) cited. `npm run harness:validate:premerge` is conditional per
  ADOPTED_BRIEF §6; if skipped, the skip and its reason are recorded explicitly
  rather than waived.
- **V2 delta re-shoot** on the post-merge tree: the three selected-chip states
  affected by the round-6 token change, the top bar and dialogue at 900px in
  both themes, and the replay provenance line from round 7.

## Remaining blockers

1. **Owner merge of the pull request** — the terminal integration act; nothing
   downstream of this run proceeds without it.
2. **Packaged Desktop evidence** for the redesigned shell and the re-hosted
   Workbench/Pipeline and navigator-selection surfaces; not run in this
   tranche, recorded in the DEL-02-01, DEL-02-02 and DEL-08-02 `## Remaining`
   sections.
3. **Named residuals**, each recorded against its owning deliverable:
   - true runtime-connectivity indicator for the top-bar status dot, which
     currently reports working-root state (DEL-02-01);
   - `.icns` / electron-builder packaged application icon, adopted D3 residual,
     cross-referenced to DEL-09-04 (DEL-02-01);
   - `metadata.icons` satisfied through the `src/app/icon.svg` file convention —
     record-only, no code owed (DEL-02-01);
   - "All sessions (N)" divergence from the approved mockup's per-group counts;
     the expanded label not inverting (V2 F-4); the omitted session year
     (DEL-02-02);
   - schema-version discipline for future workspace-state fields (DEL-02-04);
   - replay transcript-item rendering unevidenced against a real daemon session
     (DEL-05-04);
   - mock-only `[data-legacy]` contract in `woven-dialogue-route.test.tsx`
     (DEL-08-02);
   - dispatch validation evidence unchanged; the DEL-08-03 item is annotated as
     satisfied for presentation only.

## Notes carried for the receiving agent

- An authority-reference corpus bump follows the KG-033 edit in `docs/PRD.md`;
  no corpus tooling was run by this run's record-keeping.
- ADOPTED_BRIEF §4 cites a permission `role="alertdialog"`/`aria-modal`
  contract that the code deliberately does not use (`role="region"`, test-
  asserted; `aria-modal` lives in `file-picker.tsx`). Brief-text defect only.
- §3.1 token-table deltas against the adopted brief: `--ink-faint` light
  `#786F5F` / dark `#8F8570`; `--accent` light `#99552F`; undeclared derived
  `--shade` dark `#060504`.
- Chat-evidence transcription of the owner's in-session directions
  (ADOPTED_BRIEF §1 row 3, §7) and the versioned `LOOP_RECEIPTS.md` receipt with
  its validator re-run are Agent 0 closeout acts, not performed by this record
  pass.
- `instances/V2-RENDER-EVIDENCE/EVIDENCE.md` names its tree of record as
  `83a3a4733`, a commit that is no longer an ancestor of the branch; the
  equivalent round-6 commit on `feat/woven-redesign` is `af52af478`.

## Post-verification delta (V2b re-shoot, post-787e18146/1cfd3e293)

- **F-1 FIXED** (disclosure band 861–1024: panel in-viewport at 861/900/955/1024/1025; pixel correction to ROUND7_REVIEW: in-band panel is full-bleed to the header padding box, content inset by its own 17px padding — correct CSS, verdict unchanged).
- **F-2 FIXED** (placeholder ellipsizes; geometry unchanged).
- **F-3 NOT FIXED — cosmetic, non-blocking, measured no-op:** the round-7 track change frees nothing because the label track's max-content is set by `Malformed records skipped` (≈9.09rem), not `Disclosure`. Overflow backstop holds at all widths. Measured fix candidate (not applied, residual): fixed `4.5rem` label track yields one line at 1440/1180. Owner: replay-lens presentation residual.
- **F-7 (new, pre-existing, cosmetic):** replay provenance value column collapses (~14px) at ≈861–1000px, stacking values over many lines; archived `replay-light-900.png` already showed it (its §2.1 "OK" is corrected by the V2b delta section). Same residual owner as F-3.
- Render-integrity gate note: dev-overlay adds a second stylesheet (`__nextjs-Geist` @font-face) in dev; app CSS remains exactly one LINK sheet — the §2 gate wording, read literally, would now fail in dev.
