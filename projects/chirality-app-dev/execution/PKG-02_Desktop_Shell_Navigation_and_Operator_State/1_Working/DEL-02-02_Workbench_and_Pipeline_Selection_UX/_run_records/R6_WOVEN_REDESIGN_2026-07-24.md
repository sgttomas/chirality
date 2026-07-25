# R6 Woven Dialogue Visual Redesign & IA Consolidation — DEL-02-02

- Date: 2026-07-24
- Run: `APPDEV_WOVEN_REDESIGN_2026-07-24`
- Basis: `TRB-APPDEV-WOVEN-REDESIGN-2026-07-24`
  (`execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/ADOPTED_BRIEF.md`),
  adopted by the owner in-session 2026-07-24 with defaults D1–D4
  (`.../ORCHESTRATION_PLAN.md` §Adopted authority). Authority basis of record
  remains D-APP-74 / SCA-APP-004 (RULED 2026-07-23) and D-APP-36.
- Reconciliation scope: per adopted default D4, this record also reconciles the
  PR #323 Woven Dialogue implementation (merge `403f228f4`, implementation
  commit `7941722f6`, evidence
  `execution/_Coordination/AgentRuns/APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/`)
  against this deliverable.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record.

## What landed for DEL-02-02

**PR #323 (merge `403f228f4`).** Work was implemented as an honest projection
that displays only admitted items and shows absent plan or task evidence as
absent rather than inferred; Agents was implemented as a projection over
canonical recorded sessions with exact recorded parentage, with detached,
unresolved, and cyclic records kept visible in a separate unsafe-relationship
group carrying their exact recorded parent identifiers and availability status.
Agent cards expose source, currency, observation time, diagnostics, approval
and return references, and recorded model selection in non-overstated labels.
Narrow layouts place Dialogue before Navigator in reading and focus order.
Pipeline dispatch received an inert compatibility description only — no
execution or delegation behavior was added
(`.../APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/PACKAGE_RETURNS.md`
§PKG-02, §PKG-08; `.../REVIEW.md`).

**This tranche (branch `feat/woven-redesign`).**

| Commit | Content bearing on DEL-02-02 |
|---|---|
| `b6c6784f3` | Stage B1 — Artifacts ceases to be a navigator surface: `'document'` removed from the `WovenSurface`/`FocusedDialogueSurface` unions and the navigator entry list; `DocumentView` re-mounts as a Documents block (`workbench-card workbench-documents-block`, `aria-label="Documents"`) last in `.workbench-layout` with the navigator note reading "Documents, evidence & contracts"; `DocumentView` itself and the legacy sidebar Document/Files tabs untouched |
| `2afcd8474` | Stage A — the calm-editorial token layer and compact top bar that the re-hosted Workbench and Pipeline surfaces render inside; running badges moved off `--accent` onto `--slate` so semantic state colour is never the interaction accent |
| `b17ab9d39` | Stage B2 — coordination/activity presentation restyled through the `/* Stage B2 */` `globals.css` section (tokens only, single zero-deletion EOF hunk) alongside the navigator session groups |
| `04d3b4f5f` | Stage C — Documents-block object-card provenance treatment (B1 styling debt discharged, CSS-only, nested `DocumentView` de-boxed); 861–1180px responsive band; rail headers wrap; reduced-motion policy |
| `af52af478` / `787e18146` | Rounds 6–7 — AA token remedy and the `Source` provenance-label track widening in the replay/coordination surfaces |
| `1cfd3e293` | Merge of `main` into `feat/woven-redesign` |

Presentation-only discipline was independently checked: the Work projection
still emits zero `<button>` elements and no approval/assignment language, the
exact-string `<option>` and submit-button assertions in the workbench and
pipeline tests are unchanged, the exact `disabled=""` count of 4 holds, and no
`role="tab"` was introduced into `CoordinationPanel`/`ActivityShelf`
(`.../instances/AGENT1-VALIDATOR/ROUND2_REVIEW.md` item 2;
`.../ROUND4_REVIEW.md` §ARIA; `.../instances/V1-INVARIANT-SWEEP/RETURN.md`).

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/instances/B1-IA-FOLD-LOGO/RETURN.md`
  (fold return; workbench test + `vi.mock(document-view)` + 2 new tests;
  typecheck / vitest 952-4 PASS)
- `.../instances/C-DEFECT-POLISH/RETURN.md` (Documents-block styling,
  responsive band, dark parity; vitest 984-4 / typecheck / build PASS)
- `.../instances/AGENT1-VALIDATOR/ROUND2_REVIEW.md`, `.../ROUND4_REVIEW.md`,
  `.../ROUND5_REVIEW.md` (validation of the B1, B2 and C diffs)
- `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` + `.../evidence/`:
  `workbench-{light,dark}-{900,1180,1440}.png`,
  `workbench-documents-light-1440.png`,
  `pipeline-{light,dark}-{900,1180,1440}.png`,
  `coordination-work-*` and `coordination-agents-*` at all three widths in both
  themes, `route-workbench-*` / `route-pipeline-*` deep-link frames
- `.../instances/V2-RENDER-EVIDENCE/RETURN.md` (Documents block confirmed
  correct; zero horizontal overflow in all 48 matrix frames)

## Residuals recorded in `_STATUS.md` `## Remaining`

1. The navigator's "All sessions (N)" presentation diverges from the approved
   mockup's per-group counts: N is the total per Working Root over the full
   recency list including unattributed sessions. Ratified as the only reading
   that honours the unattributed-only-under-All rule (B2 deviation 1), and
   routed to the owner as the one visible IA divergence — the owner may choose
   to re-style it (`.../instances/B2-NAV-SESSIONS/RETURN.md`;
   `.../AGENT1-VALIDATOR/ROUND4_REVIEW.md` note 2).
2. The expanded "All sessions" label does not invert when the group is
   expanded, although `aria-expanded` is correct (V2 finding F-4; component
   label logic, deliberately not reopened post-verification).
3. `formatSessionWhen` omits the year, leaving cross-year timestamps ambiguous
   (round-4 note; cosmetic).
4. Packaged Desktop smoke evidence for the re-hosted Workbench and Pipeline
   surfaces (not run this tranche).

## Other notes of record

- First run after merge shows every navigator mode group empty until new
  sessions are tagged, which is the expected consequence of adopted default D2
  (client-side surface attribution creates no retroactive truth). V2 captured
  that state deliberately and labelled it expected
  (`.../AGENT1-VALIDATOR/ROUND4_REVIEW.md` note 3;
  `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md`).
- Gate figures cited here were measured before the `1cfd3e293` upstream merge;
  the authoritative post-merge full-gate run is owned by Agent 0 at closeout.
