# V2-RENDER-EVIDENCE — D-APP-36 browser evidence log

**Instance:** V2-RENDER-EVIDENCE (Agent 2, opus-5) · **Run:** `APPDEV_WOVEN_REDESIGN_2026-07-24`
**Parent:** HELP_HUMAN (Agent 0) · **Sealed brief:** `instances/V2-RENDER-EVIDENCE/LAUNCH_BRIEF.md`
**Evidence format:** `projects/chirality-app-dev/docs/ui/UI_POLISH_EXECUTION_PLAN.md` → "Required evidence" (2): route, viewport, states exercised, outcome.

This log records observation only. It is not a lifecycle issuance, a certification,
or a release approval. Absence of a finding is not approval.

---

## 1. Capture conditions

| Item | Value |
|---|---|
| Tree under test | `feat/woven-redesign` @ **`83a3a4733`** — see §1.2 |
| Server | `npx next dev --port 3001` from `projects/chirality-app-dev/frontend` (dev server, per brief) |
| Browser engine | Electron 43.1.1 (Chromium) `BrowserWindow`, default `webPreferences`, `capturePage()` → PNG |
| Device pixel ratio | 2 (a 1440×900 CSS viewport yields a 2880×1800 PNG) |
| Window content size | width per capture × 900 CSS px |
| Working Root used | `/Users/ryan/dev/chirality` — set through the **real UI controls** (root-chip disclosure → path field via renderer key events → `Apply Path` → `POST /api/working-root/validate` 200). The repo root itself is rejected by design (`WORKING_ROOT_CONFLICT: projectRoot cannot point inside instruction root`). |
| Workspace state | `chirality.wovenWorkspace.v1` cleared before every run → every capture is a genuine first-run state |

### 1.1 Declared stub (read this before trusting any session-bearing capture)

No Chirality runtime daemon is available in this environment:
`GET /api/harness/session/list` returns `503 ENGINE_UNAVAILABLE: Chirality runtime daemon client is not configured`.

To exercise the navigator session lists and the replay lens at all, captures were taken
through a **local pass-through proxy on :3002** that forwards everything to the dev
server on :3001 except two endpoints, which return fixtures:

- `GET /api/harness/session/list` → 5 `SessionRecord`s (personas `HELP_HUMAN`, `WORKING_ITEMS`, `RECONCILIATION`, `CHANGE`, `RESEARCH`; `updatedAt` Jul 20–24 2026)
- `GET /api/harness/session/:id/events` → a 4-event fixture

**Every PNG except the `*-nostub` pair was taken through that proxy.** All application
code paths exercised are the real ones (`listHarnessSessions` → `requestHarnessJson` →
`buildNavigatorSessionGroups`; `createSelectedSessionReplayLoader` → `replaySessionEvents`);
only the two HTTP responses are substituted. The unstubbed, honest daemon-unavailable
state is captured separately in `navigator-{light,dark}-1440-nostub.png`.

Consequence to note: the replay lens reports `Transcript items shown 0` because the
fixture events do not match the transcript-derivation schema. The lens' READ-ONLY
framing, provenance block and event count render correctly; the transcript list itself is
not evidenced here.

### 1.2 HEAD moved mid-run — which commit these captures actually show

The brief named `04d3b4f5f` (Stage C) as the tree of record. While this instance was
capturing, a sibling landed **`83a3a4733` "round 6 — light accent token AA remedy
(V1 adversarial find)"** at 17:01:49, changing light `--accent` `#9C5730` → `#99552F`
(a 3/255 shift on one token) and committing this instance's then-in-progress evidence
files. The worktree HEAD is now `83a3a4733`.

Every shipped capture is from **after** that commit and reflects it:

- All matrix PNGs were written 17:03:11–17:05, after the round-6 edit reached disk; the
  Next dev server recompiles CSS per page load.
- The contrast pass (17:09) measured light `--accent` as `rgb(153, 85, 47)` = **`#99552F`**,
  i.e. the round-6 value, and the keyboard pass measured the focus outline as the same colour.
- Direct re-capture against the current tree after the run: `topbar-light-1440.png` and
  `navigator-light-1440.png` are **byte-identical** to the stored frames. Other re-captures
  differ only because the coordination Agents projection renders live `Observed:` timestamps
  and the panel view persists across scenes — not because of styling.

Stale frames from an earlier, broken dev-server state were deleted and the whole matrix
re-captured (see finding F-6).

---

## 2. Screenshot matrix — route, viewport, theme, states, outcome

Machine-readable per-capture records (including measured `bodyBackground`, `styleSheets`,
`data-theme` and page-overflow flags for every frame) are in
`evidence/_capture-log-matrix.json` and `evidence/_capture-log-extras.json`.

**Render-integrity gate applied to all 48 matrix frames:** `styleSheets == 1`,
`data-theme` equals the requested theme, and `document.scrollWidth <= innerWidth`.
All 48 passed. Measured `body` background was exactly `rgb(248,245,238)` (`--ground` light)
in the 24 light frames and `rgb(23,21,17)` (`--ground` dark, the round-3 `#171511`) in the
24 dark frames.

### 2.1 Core matrix — 8 surfaces × 2 themes × 3 widths = 48 PNGs

All at route `/` (the woven workspace shell; surfaces are in-shell, not separate routes).

| Surface (file prefix) | States exercised | Outcome |
|---|---|---|
| `topbar` | Compact top bar with the root-chip **disclosure open**: path field, `Apply Path`, `Choose Folder`, `Clear`, `Active root:` line, `Runtime & credentials` sub-disclosure | **OK at 1440 / 1180 · ISSUE at 900** (finding F-1) |
| `navigator` | Active group (`Dialogue`) expanded, `Workbench` + `Pipeline` collapsed (`aria-expanded` true/false/false verified per frame); per-mode group **empty**; `All sessions (5)` present; File Tree populated from the Working Root | OK |
| `dialogue` | Empty transcript + persona control + operator-mode select + Attachments block + composer input row — **the previously-overlapping arrangement** | OK (finding F-0 resolved, §4) |
| `workbench` | Focused workspace surface: Active Agent Context, Deliverable Contracts (empty `No deliverables found`), **Documents block** (Stage C) in its empty state | OK |
| `pipeline` | DECOMP*/PREP*/TASK*/AUDIT* lanes, selects, Dynamic Scope Scan | OK |
| `coordination-work` | Coordination panel, `Work` view active (`aria-pressed`), non-authority wording, empty projection | OK |
| `coordination-agents` | Coordination panel, `Agents` view active, recorded-session cards with `Role not recorded` / `status unknown` | OK |
| `replay` | `All sessions (5)` expanded → first session row selected → replay lens `REPLAY — READ-ONLY`, provenance (`Source`, `Observed`, `Disclosure EVIDENCE_ONLY`, `Currency UNKNOWN`, `Events 4`), `Return to primary dialogue` | OK (one cosmetic nit, finding F-3) |

Files: `<surface>-{light,dark}-{1440,1180,900}.png`.

### 2.2 Additional captures

| File | Route / viewport | States exercised | Outcome |
|---|---|---|---|
| `topbar-crop-{light,dark}-1440.png` | `/` 1440 | Compact bar, disclosure **closed** — 64px-tall crop | OK. Measured bar height **exactly 48px at all three widths** (`_geometry.json`). |
| `logo-{light,dark}-1440.png` | `/` 1440 | Close crop of the quincunx mark + wordmark on both bars | OK. On dark the cream tile reads clearly against `--ground #171511` (round-3 note satisfied); on light the tile is separated from the bar by its own hairline. |
| `navigator-allsessions-{light,dark}-1440.png` | `/` 1440 | `All sessions (5)` expanded → 5 rows, persona label + `Jul 20`–`Jul 24` | OK (one cosmetic nit, finding F-4) |
| `navigator-{light,dark}-1440-nostub.png` | `/` 1440, **no proxy, port 3001 direct** | Real daemon-unavailable state: `sessionsError` rendered in-group as `ENGINE_UNAVAILABLE: Chirality runtime daemon client is not configured` (`role="alert"`, `--danger`) | OK — error state is explicit, not silent |
| `navigator-system-1440-osdark.png`, `dialogue-system-1440-osdark.png` | `/` 1440, theme **Auto**, `nativeTheme.themeSource='dark'` | `data-theme="system"` + measured `body` bg `rgb(23,21,17)` | OK — Auto follows OS dark |
| `navigator-system-1440-oslight.png` | `/` 1440, theme **Auto**, `nativeTheme.themeSource='light'` | `data-theme="system"` + measured `body` bg `rgb(248,245,238)` | OK — Auto follows OS light |
| `navigator-light-1440-reducedmotion.png`, `dialogue-light-1440-reducedmotion.png` | `/` 1440, `--force-prefers-reduced-motion` | See §5 | OK |
| `legacy-{light,dark}-1440.png` | `/?legacy=1` 1440 | Legacy Portal loop shell + Agent Matrix sidebar under the new shared chrome | OK — loads, renders, inherits the compact bar and theme control |
| `route-chat-{light,dark}-1440.png` | `/chat` 1440 | Woven shell mounts on the deep-link route | OK |
| `route-workbench-{light,dark}-1440.png` | `/workbench` 1440 | Standalone workbench route | OK |
| `route-pipeline-{light,dark}-1440.png` | `/pipeline` 1440 | Standalone pipeline route | OK |
| `workbench-documents-light-1440.png` | `/` 1440 | Documents block close crop, **no Working Root** state (`Select a Working Root to view deliverable documents.`) | OK — single card border + one header rule; no doubled edge |

---

## 3. Explicit checks demanded by the brief

### 3.1 Brand `alt=""` decorative change

Measured in-page (`_a11y-checks-normal-motion.json` → `brand`):

```
brandImgAlt: ""            brandImgAltIsEmptyString: true
brandImgAriaHidden: null   wordmarkText: "Chirality"
brandRowAccessibleText: "Chirality"
```

The mark is correctly decorative (`alt=""`); the accessible name of the brand row comes
from the `.shell-wordmark` text, i.e. the wordmark. **OK.**

### 3.2 `prefers-reduced-motion` honoured

The stylesheet carries exactly one transition (`.woven-resize-handle::after`) and zero
`@keyframes`. Emulated with Chromium `--force-prefers-reduced-motion`:

| Measurement | Normal | Reduced (`matchMedia` reports `true`) |
|---|---|---|
| `.woven-resize-handle::after` `transition-duration` | `0.12s, 0.12s` | `1e-05s` |
| `.woven-resize-handle::after` `transition-property` | `background, transform` | `none` |
| `.woven-resize-handle::after` `animation-duration` | `0s` | `1e-05s` |
| `.woven-nav-item` `transition-duration` | `0s` | `1e-05s` |
| `html` `scroll-behavior` | `auto` | `auto` |

Evidence: `evidence/_a11y-checks-normal-motion.json`, `evidence/_a11y-checks-reduced-motion.json`.
The Stage C6 whole-document policy block is in force and covers the hover transform.
**OK.**

### 3.3 AA contrast — measured ratios, both themes

Ratios computed from **rasterised** colours (`color-mix()`-derived tokens serialise as
`color(srgb …)` in this engine, so each token was painted to a 1×1 canvas and the pixel
read back), WCAG 2.x relative-luminance formula. Full data:
`evidence/_a11y-checks-normal-motion.json` → `contrast`.

**Chip text on tints (the pairs the brief names):**

| Pair | Light | Dark | AA (4.5:1) |
|---|---|---|---|
| `--sage-ink` on `--sage-soft` | **5.54** | **7.64** | pass / pass |
| `--rose-ink` on `--rose-soft` | **5.29** | **7.44** | pass / pass |
| `--slate-ink` on `--slate-soft` | **6.05** | **6.79** | pass / pass |
| `--accent-ink` on `--accent-soft` | **5.52** | **5.55** | pass / pass |

**Surrounding pairs (spot-check, same pass):**

| Pair | Light | Dark |
|---|---|---|
| `--ink` on `--surface` / `--card` | 14.91 / 15.31 | 13.71 / 13.11 |
| `--ink-soft` on `--surface` / `--card` | 6.75 / 6.93 | 6.63 / 6.33 |
| `--ink-faint` on `--surface` / `--card` / `--ground` | 4.75 / **4.87** / **4.55** | 4.77 / **4.56** / 5.00 |
| `--cta-ink` on `--cta` | 12.52 | 11.57 |
| `--danger` / `--accent` on `--surface` | 6.73 / 5.45 | 5.18 / 5.30 |
| `--sage` / `--rose` / `--slate` on `--surface` | 4.59 / 4.46 / 5.18 | 7.61 / 6.89 / 6.53 |

**Rendered controls (not token probes) — computed `color` vs nearest opaque ancestor
background, measured on the live DOM.** Data: `evidence/_contrast-rendered-controls.json`.

| Rendered control | Light | Dark |
|---|---|---|
| Selected theme chip (`.shell-theme-option[aria-pressed="true"]`) | **4.58** | **4.61** |
| Active coordination tab (`.woven-coordination-tabs button.is-active`) | **4.58** | **4.61** |
| Active shell nav link (`.shell-nav-link--active`) | 5.45 | 5.30 |
| Active navigator group (`.woven-nav-item--active`) | 14.29 | 14.38 |

The selected-chip pair measures 4.58 light — corroborating the round-6 remedy's claim of
4.579 for that pair, independently and from the rendered DOM. (Caveat recorded in the JSON:
the active navigator group's highlight is painted as a `background-image` gradient, so the
walk resolves to the nearest opaque `backgroundColor` ancestor; the pairing passes with a
wide margin either way.)

**Every measured pair — token probes and rendered controls alike — clears 4.5:1 in both themes.** The round-5 `--ink-faint` remedy
(`#79715f` → `#8f8570` in dark) is confirmed effective: dark `--ink-faint` on `--card`
now measures 4.56. Recorded as a **margin note, not a failure**: three pairs sit within
0.10 of the threshold — light `--ink-faint` on `--ground` (4.55), dark `--ink-faint` on
`--card` (4.56), and `--rose` on light `--surface` (4.46 — this last is a *non-text*
stroke/marker token and is not used as body text, per the token contract) — plus the two
rendered accent chips at 4.58 (light) and 4.61 (dark). Any future tweak to `--ground`,
`--card`, `--ink-faint`, `--accent` or `--accent-soft` should be re-measured, because five
distinct pairs now sit inside a 0.11 band above the threshold.

### 3.4 Keyboard walk — navigator groups and theme control

Full transcript: `evidence/_a11y-checks-normal-motion.json` → `keyboard`.

| Step | Result |
|---|---|
| Focus first navigator group (`Dialogue`, active) | `BUTTON.woven-nav-item--active`, `aria-expanded="true"`, `:focus-visible` **true**, outline `rgb(153,85,47) solid 2px`, offset `2px` |
| **Enter** on active group | `aria-expanded` `true` → `false` (collapses) |
| **Enter** again | `aria-expanded` → `true` (re-expands) |
| Focus second group (`Workbench`, inactive) | `aria-expanded="false"`, focus-visible true, same outline |
| **Space** on inactive group | `[data-woven-surface]` → `"workbench"` (opens the surface) |
| Focus theme `LIGHT` | `aria-pressed="true"`, `data-theme-option="light"`, focus-visible true |
| **Tab** | moves to `DARK` (`aria-pressed="false"`), focus-visible true — the group is a plain tab sequence, not a roving-tabindex radiogroup |
| **Space** on `DARK` | `data-theme` → `"dark"`; pressed states `light=false, dark=true, system=false` |
| Focus first session row | `BUTTON.woven-navigator-session`, `aria-pressed="false"`, focus-visible true, same outline |
| **Enter** on session row | replay lens mounts: `REPLAY — READ-ONLY / Recorded session / Selected session: ses_9f21c4a7 / Return to primary dialogue` |

Focus is visible on every new control, order is usable, and Enter/Space operate every
new control. **OK.**

---

## 4. The Stage C composer-dock defect — proven fixed

Measured bounding boxes at all three widths, in the **true empty state** (no Working
Root — the state the defect was reported in) and with a root applied.

| Width | `.panel-body.chat-transcript` ↔ `.chat-composer-dock` | empty-state line ↔ dock | attachments header ↔ `.chat-input-row` | attachments empty line ↔ input row |
|---|---|---|---|---|
| 1440 | **no overlap**, 0px gap (adjacent) | clear, 415px gap | clear, 37px gap | clear, 9px gap |
| 1180 | **no overlap**, 0px gap | clear, 442px gap | clear, 37px gap | clear, 9px gap |
| 900 | **no overlap**, 0px gap | clear, 387px gap | clear, 37px gap | clear, 9px gap |

Mechanism confirmed: the transcript is `overflow-y: auto; min-height: 0px` inside the
flex column, so long content scrolls locally and cannot push into the statically-flowed
dock. Data: `evidence/_geometry.json`; visual: `dialogue-{light,dark}-{1440,1180,900}.png`.
**F-0 (the tranche's target defect) is resolved.**

Page-level overflow: `document.scrollWidth == innerWidth` in all 48 matrix frames and in
every geometry sample — no horizontal page scroll at any captured width.

---

## 5. Findings

### F-1 — BLOCKING (responsive): the root-chip disclosure panel is clipped off the left edge at 900px

**Where:** `frontend/src/app/globals.css:473-486` — `.working-root-bar { position: absolute; right: 0; width: min(680px, calc(100vw - 2.4rem)); }`, anchored to `.shell-root-disclosure` (`position: relative`).

**Measured** (`.working-root-bar` rect vs viewport):

| Viewport | chip right edge | panel left | panel right | verdict |
|---|---|---|---|---|
| 1440 | 1164 | 484 | 1164 | fits |
| 1180 | 904 | 224 | 904 | fits |
| **900** | **624** | **−56** | **624** | **56 CSS px clipped off-screen left** |

The width clamp does not help: at 900px `calc(100vw - 2.4rem)` = 861.6px, so `min()`
still resolves to 680px, and `right: 0` pins the panel to the *chip's* right edge (624px,
because the `WORKSPACE` nav and the theme control sit to the chip's right), pushing the
left edge to −56.

**Visible effect** (`topbar-light-900.png`, `topbar-dark-900.png`): the field label reads
`ING ROOT (\`PROJECTROOT\`)`, the path input's leading characters are cut, the primary
`Apply Path` button renders as `ly Path` with roughly half its hit area off-screen, the
`Active root:` line is cut to `root: …`, and the sub-disclosure reads
`me & credentials`. The controls remain partially operable but their labels are not
readable, which fails the stated acceptance check in
`docs/ui/UI_POLISH_EXECUTION_PLAN.md` ("labels and values remain readable at supported
widths") and the tranche's own responsive gate. The failure threshold is where the chip's
right edge falls below 680px — approximately **viewport < ~955px**; 1180 and 1440 are clean.

**Suggested direction (not applied — this instance is read-only):** clamp against the
viewport rather than the anchor, e.g. `right: auto; left: auto;` with a
`max-width: calc(100vw - 2.4rem)` plus a translate/`inset-inline` correction, or reduce
the panel to a stacked narrow layout under the existing `max-width: 1180px` media block.

### F-2 — Cosmetic: composer placeholder clipped at 900px

`dialogue-{light,dark}-900.png`: the composer placeholder renders as
`Send prompt as WORKING_ITEMS` with the trailing ellipsis cut at the input's right edge
(no `text-overflow` on the placeholder). Purely presentational; the field is fully usable.

### F-3 — Cosmetic: replay-lens provenance value wraps mid-token

`replay-{light,dark}-1440.png`: `Source  session:ses_9f21c4a7/events` wraps as
`…/even` / `ts`. A `overflow-wrap: anywhere` on that definition-list value (or a wider
value column) would break at the slash instead.

### F-4 — Cosmetic: "All sessions (N)" toggle label does not invert

`navigator-allsessions-*.png`: the disclosure correctly flips `aria-expanded` to `true`
and shows all 5 sessions, but the label stays `All sessions (5)` in both states. The
state is exposed to assistive tech; only the visible label is ambiguous.

### F-5 — Observation, not a defect: first-run empty per-mode groups

`navigator-{light,dark}-{1440,1180,900}.png` show every mode group reporting
`No recorded sessions for this surface.` while `All sessions (5)` is populated.
**This is the expected post-merge state under adopted D2** (client-side tag-forward;
no retroactive surface attribution is possible because `SessionRecord` carries no surface
field). It is recorded here so it is not later mistaken for a regression.

### F-6 — Observation: environment, not the tree

- No runtime daemon → persona roster and session list legitimately report
  `ENGINE_UNAVAILABLE`. The UI surfaces this explicitly in both the dialogue header and
  the navigator group (`role="alert"`), which is the correct behaviour.
- `[data-legacy]` was **not found** in the DOM at `/?legacy=1`; the legacy shell renders
  correctly and is functional. Whether that marker is still a required invariant is
  V1-INVARIANT-SWEEP's call, not this instance's — flagged for routing only.
- During this run a concurrent process replaced `frontend/.next` with a **production**
  build, which broke the running dev server (all `_next/static/*` → 404) and produced two
  unstyled frames. The dev server was restarted and **the entire matrix was re-captured
  from scratch**; every shipped PNG passed the §2 render-integrity gate. No stale frame
  survives in `evidence/`.

---

## 6. Limitations

1. **Stubbed session/replay data** (§1.1). The navigator's populated lists and the replay
   lens are evidenced against fixtures, not daemon-recorded sessions. `Transcript items
   shown 0` in the lens is a fixture artefact, so the replay **transcript list** is
   unevidenced.
2. **Dev-server rendering only.** `next build` output was not exercised for these
   screenshots.
3. **Single engine.** Electron/Chromium only; no Safari/Firefox/WebKit rendering.
4. **Static frames.** Streaming turns, permission `alertdialog`, interrupt, and
   turn-in-progress guarding (`selectionDisabled`) were not reachable without a daemon and
   are not evidenced.
5. **No lifecycle claim.** This log evidences rendering and interaction observations only.

---

## 7. Verdict

**PASS WITH ONE BLOCKING FINDING.**

The Stage A/B/C work renders correctly and completely across 7 surfaces × 2 themes ×
3 widths plus 21 supplementary captures. The tranche's target defect (composer-dock /
empty-state overlap) is **measurably fixed at every captured width**; the compact top bar
is exactly 48px; no frame shows page-level horizontal overflow; Auto theme follows the OS
in both directions; `prefers-reduced-motion` is fully honoured; the brand mark is
correctly decorative with the wordmark carrying the accessible name; every measured token
pair clears AA in both themes; and the navigator groups, theme control and session rows
are keyboard-operable with visible focus.

**F-1 must be resolved or explicitly accepted before this tranche closes**: at the 900px
breakpoint the root-chip disclosure — the control this tranche created to hold the entire
Working Root surface — is clipped 56px off the left edge of the viewport, rendering its
label, its path field's leading text, and half of its primary `Apply Path` button
unreadable. F-2 through F-4 are cosmetic and may be deferred.

---

# Delta re-shoot post-`787e18146`/`1cfd3e293`

**Instance:** V2B-DELTA-RESHOOT (Agent 2, opus-5) · **Run:** `APPDEV_WOVEN_REDESIGN_2026-07-24`
**Parent:** HELP_HUMAN (Agent 0) · Follow-on to §1–§7 above, which stand except where a
file is listed as replaced below.

Purpose: issue the **verdict of record** on F-1, F-2 and F-3 against the post-round-7,
post-merge tree, and replace only the frames those findings touched. Sections §1–§7 above
are unchanged and remain the record for every other frame.

## D.1 Capture conditions (delta)

| Item | Value |
|---|---|
| Tree under test | `feat/woven-redesign` @ **`1cfd3e293`** (merge of `main` into the branch; `787e18146` = round 7) |
| Server | `npx next dev --port 3001` from `projects/chirality-app-dev/frontend` — dev server only; `next build` was **not** run |
| Browser engine | Electron **43.1.1** (Chromium) `BrowserWindow`, `capturePage()` → PNG — same engine build as §1 |
| Device pixel ratio | 2 (unchanged from §1; a 900×900 CSS viewport yields an 1800×1800 PNG) |
| Theme | set through the **in-app control** every frame: real mouse-down/up on `.shell-theme-option[data-theme-option="…"]`, then `data-theme` re-read from `<html>` and asserted to equal the requested theme before capture |
| Working Root | `/Users/ryan/dev/chirality`, set through the **real UI**: root-chip disclosure → path field (renderer text insertion) → `Apply Path`; `Active root: /Users/ryan/dev/chirality`, `chirality.projectRoot` persisted, no `working-root-error` |
| Workspace state | `chirality.wovenWorkspace.v1` and `chirality.projectRoot` cleared before the run |
| Fixture pass-through | **identical approach to §1.1**, on `:3002` → `:3001`, substituting only `GET /api/harness/session/list` (5 `SessionRecord`s, personas `HELP_HUMAN`/`WORKING_ITEMS`/`RECONCILIATION`/`CHANGE`/`RESEARCH`, `updatedAt` Jul 20–24 2026) and `GET /api/harness/session/:id/events` (4 schema-valid `HarnessEvent`s that derive to zero transcript items, `session` omitted). Reproduces §1.1's observable state: lens `READY`, `Disclosure EVIDENCE_ONLY`, `Currency UNKNOWN`, `Events 4`, `Transcript items shown 0`. |
| Render-integrity gate | every delta frame: `data-theme` == requested theme; `body` background exactly `rgb(248,245,238)` light / `rgb(23,21,17)` dark; `document.scrollWidth <= innerWidth`. **All 14 frames passed.** |
| `styleSheets` count | **2**, not §2's 1. The second sheet is a Next.js **dev-overlay** `<style>` carrying 4 `@font-face` rules for `__nextjs-Geist` (`_delta-capture-log-*.json` → `render.styleSheetsDetail`). App CSS is still exactly one `LINK` (`/_next/static/css/app/layout.css`, 495 rules). Not an app-stylesheet regression. |

Machine-readable per-frame records:
`evidence/_delta-capture-log-topbar-dialogue-replay.json`,
`evidence/_delta-capture-log-bandedges-crops.json`,
`evidence/_delta-f3-provenance-diagnosis.json`.

## D.2 Files replaced and added

**Replaced (same filenames, stale frames overwritten):**

`topbar-light-900.png`, `topbar-dark-900.png`, `dialogue-light-900.png`,
`dialogue-dark-900.png`, `replay-light-1180.png`, `replay-dark-1180.png`,
`replay-light-1440.png`, `replay-dark-1440.png`

(The replay 1440 pair is included because F-3 was originally documented against it.)

**Added:**

| File | Why |
|---|---|
| `topbar-light-955.png` | inside the round-7 band; the width §5/F-1 named as the old failure threshold (~955px) |
| `topbar-light-1024.png` | **upper band edge** — last width where the round-7 media block applies |
| `topbar-light-861.png` | **lower band edge** — first width where the round-7 media block applies |
| `topbar-light-1025.png` | **first width above the band** — proves the un-modified chip-anchored path is still clean on the other side of the edge |
| `dialogue-composer-crop-light-900.png` | close crop carrying the F-2 verdict visually |
| `replay-provenance-crop-light-900.png` | close crop carrying finding **F-7** (below) |
| `_delta-capture-log-topbar-dialogue-replay.json`, `_delta-capture-log-bandedges-crops.json`, `_delta-f3-provenance-diagnosis.json` | per-frame measurements and the F-3 cascade diagnosis |

**Explicitly not re-shot, and why they are not stale:** `topbar-*-{1440,1180}` and
`dialogue-*-{1440,1180}` (outside the 861–1024 band; placeholder fits, so
`text-overflow` cannot manifest) and `replay-*-900` (round 7's F-3 declaration is a
measured no-op — see D.5 — so those frames are pixel-equivalent; the archived pair is in
fact the direct proof of F-7).

## D.3 F-1 — **FIXED**

Root-chip disclosure **open**, theme set through the in-app control, at four widths:

| Viewport | containing block | panel left | panel right | `Apply Path` | `Working Root (…)` label | `Active root:` line | page overflow |
|---|---|---|---|---|---|---|---|
| **861** (band floor) | `.shell-header` relative / `.shell-root-disclosure` static | **0** | **861** | 17 → 110.19 ✓ | 17 → 844, unclipped ✓ | 17 → 844, unclipped ✓ | none |
| **900** (the F-1 failure width) | same | **0** | **900** | 17 → 110.19 ✓ | 17 → 883, unclipped ✓ | 17 → 883, unclipped ✓ | none |
| **955** (old threshold) | same | **0** | **955** | 656.04 → 749.23 ✓ | 17 → 938, unclipped ✓ | 17 → 938, unclipped ✓ | none |
| **1024** (band ceiling) | same | **0** | **1024** | 725.04 → 818.23 ✓ | 17 → 1007, unclipped ✓ | 17 → 1007, unclipped ✓ | none |
| **1025** (first width above) | `.shell-root-disclosure` relative (unchanged path) | **69.27** | **749.27** | 450.3 → 543.49 ✓ | 86.27 → 732.27, unclipped ✓ | 86.27 → 732.27, unclipped ✓ | none |

**Verdict: FIXED.** At 900px the panel's left edge moved from **−56** (§5/F-1) to **0** —
fully in-viewport. Every control the finding named is now wholly inside the viewport with
no internal clipping (`scrollWidth <= clientWidth` on the label, the path input, all three
buttons, the `Active root:` line and the `Runtime & credentials` summary, at all four
in-band widths). Visually (`topbar-light-900.png`, `topbar-dark-900.png`): the label reads
`WORKING ROOT (\`PROJECTROOT\`)` in full, the path field shows `/Users/ryan/dev/chirality`
from its first character, `Apply Path` renders complete with its full hit area,
`Active root: /Users/ryan/dev/chirality` is complete, and the sub-disclosure reads
`▸ Runtime & credentials`. Both band edges are clean on **both** sides.

**One correction to `AGENT1-VALIDATOR/ROUND7_REVIEW.md` (does not change the verdict).**
That review states "panel left = page margin 18.4px and right 18.4px inside viewport at
1024/955/900/861". Measured here, the in-band panel is **flush to the viewport edges**:
`left: 0`, `right: viewport width`, computed `left: 0px; right: 0px`. This is correct CSS
behaviour, not a bug — an absolutely positioned box resolves `left`/`right` against its
containing block's **padding box**, which for `.shell-header` (`padding-inline: 18.4px`,
no border) starts at x=0; the header's own padding does not inset it. The panel's 18.4px
page-margin inset therefore does not exist; its content is inset 17px by the panel's own
`1rem` padding + 1px border, which is what keeps the labels readable. So the in-band
presentation is a **full-bleed band under the top bar**, edge-to-edge. Consistent with
the review's own accepted note that "the 976–1024 full-width panel presentation is
harmless" — recorded so the closing record matches the pixels.

## D.4 F-2 — **FIXED**

`dialogue-light-900.png`, `dialogue-dark-900.png`, and the close crop
`dialogue-composer-crop-light-900.png`:

| Measurement | Value (identical in both themes) |
|---|---|
| placeholder | `Send prompt as WORKING_ITEMS...` |
| computed `text-overflow` | **`ellipsis`** (round-7 rule in force) |
| computed `overflow` | `clip` |
| input content-box width | 215.8px |
| placeholder width in the input's own font | 228.4px |
| overflow | **12.6px → truncation is required, so the ellipsis is exercised, not merely declared** |
| input rect | 233.8 → 470.32, fully in viewport |
| page overflow | none (`scrollWidth == innerWidth == 900`) |

**Verdict: FIXED.** The field renders `Send prompt as WORKING_ITE…` — truncated early with
a clean ellipsis glyph inside the field, replacing §5/F-2's mid-glyph cut of
`…WORKING_ITEMS` at the input's right border. The composer dock geometry is unaffected
(`.panel-body.chat-transcript` bottom == `.chat-composer-dock` top == 668.86, no overlap),
so §4 still holds.

## D.5 F-3 — **NOT FIXED** (cosmetic, non-blocking; the applied remedy is a measured no-op)

Replay lens mounted the same way as §1.1 (`All sessions (5)` → first row → lens `READY`,
`EVIDENCE_ONLY`). Measured on the shipped tree:

| Viewport | label track | value track | `Source` line boxes | overflow |
|---|---|---|---|---|
| 1440 | 145.492px | 182.914px | **2 lines** — `session:ses_9f21c4a7/even` (178.21px) / `ts` (14.26px) | none |
| 1180 | 145.492px | 136.117px | **2 lines** — `session:ses_9f21c4a` (135.44px) / `7/events` (57.03px) | none |

The 1440 frame reproduces §5/F-3's reported symptom **character for character**
(`…/even` / `ts`).

**Why the remedy did nothing** (`_delta-f3-provenance-diagnosis.json`):

1. The round-7 declaration `grid-template-columns: minmax(4.5rem, max-content) minmax(0, 1fr)`
   is present and **wins the cascade** (it is the last of the matching rules).
2. Substituting the pre-round-7 value `minmax(7rem, auto)` **inline on the live DOM**
   yields byte-identical used tracks and byte-identical line boxes at 1440, 1180 **and**
   900. The change is a **no-op**.
3. Root cause of the no-op: the label track's `max-content` is set by the **longest** label,
   which is **`Malformed records skipped` = 145.49px (≈9.09rem)** — not `Disclosure`
   (55.76px), as `ROUND7_REVIEW.md` §F-3 states. Measured label max-contents:
   `Source` 36.91 · `Events` 35.78 · `Currency` 47.8 · `Observed` 51.08 ·
   `Disclosure` 55.76 · `Transcript items shown` 123.71 · **`Malformed records skipped` 145.49**.
   Lowering the *minimum* from 7rem (112px) to 4.5rem (72px) frees nothing, because
   `max-content` (145.49px) is the binding constraint and `auto` already resolved to the
   same 145.49px. No space was handed to the value track.
4. The `Source` string needs **192.47px** on one line. The value track is 182.91px at 1440
   and 136.12px at 1180 — short in both cases.

**What the review's mitigation claim does hold:** the value never overflows its column
(`scrollWidth == clientWidth` on the `dd`, `provenanceOverflows: false`, page
`scrollWidth == innerWidth`) at any measured width. The `overflow-wrap` backstop works.
So this is **cosmetic and non-blocking** — but it is **not fixed**, and the diagnosis in
`ROUND7_REVIEW.md` §F-3 is incorrect on which label sizes the track.

**Measured directions (transient probes only — nothing applied; this instance is read-only):**

| Label track | 1440 `Source` | 1180 `Source` | 900 `Source` |
|---|---|---|---|
| as shipped (`minmax(4.5rem, max-content)`) | 2 lines | 2 lines | **14 lines** |
| pre-round-7 (`minmax(7rem, auto)`) | 2 lines | 2 lines | **14 lines** |
| fixed `7rem` | **1 line** | 2 lines | 4 lines |
| fixed `4.5rem` | **1 line** | **1 line** | 3 lines |

A **fixed** (non-`minmax`) label track is what actually frees space, at the cost of letting
`Malformed records skipped` wrap in the label column. Alternatively, constraining the break
to `/` and `:` (i.e. dropping `overflow-wrap: anywhere` in favour of a break-opportunity
rule) would yield `session:ses_9f21c4a7` / `/events` instead of a mid-token split. Either
is a design call for the owning loop, not this instance's.

## D.6 F-7 — new finding, cosmetic/legibility, **pre-existing (not a round-7 regression)**

At **900px** the replay-lens provenance value column collapses to **14.62px** — roughly two
monospace characters — so *every* value renders as a vertical character stack:
`Source` over **14 lines**, `Observed` over 13, `Disclosure` over 5.
Evidence: `replay-provenance-crop-light-900.png`.

Mechanism: `.woven-replay-provenance` stays a 2-column grid down to 860px, and the
145.49px label track (D.5 §3) consumes almost the whole ~160px `dl`. Below 861px the
provenance collapses to one column and the problem disappears; the pathological band is
therefore roughly **861px–~1000px**.

**Pre-existing, not caused by round 7**, on two independent grounds: (a) substituting the
pre-round-7 declaration inline at 900px reproduces the identical 14-line stack; (b) the
**archived** §2.1 frame `replay-light-900.png` — captured before round 7 — already shows
the same collapsed column (there at ~3 characters per line). It was recorded as "OK" in
§2.1; that assessment is corrected here. No overflow, no lost information, keyboard and AT
paths unaffected — but at a supported width the provenance block is effectively unreadable.
Routed as a cosmetic finding for the owning loop's disposition; strictly worse than F-3 and
addressed by the same fixed-label-track direction (which reduces the 900px stack from 14
lines to 3–4).

## D.7 Delta verdict

| Finding | Verdict of record |
|---|---|
| **F-1** (blocking, disclosure clipped 56px off-screen at 900) | **FIXED** — panel left −56 → 0; every named control fully in-viewport and unclipped at 861 / 900 / 955 / 1024, and the un-modified path above the band (1025) is still clean |
| **F-2** (composer placeholder clipped at 900) | **FIXED** — `text-overflow: ellipsis` in force and exercised (12.6px overflow); renders `Send prompt as WORKING_ITE…` |
| **F-3** (replay `Source` wraps mid-token) | **NOT FIXED** — the round-7 declaration is a measured no-op; the wrap is unchanged at 1440 (`…/even` / `ts`) and 1180. Confined: no overflow at any width, so **cosmetic and non-blocking**. `ROUND7_REVIEW.md` §F-3's diagnosis (widest label = `Disclosure`) is incorrect |
| **F-4** | untouched, still residual (not re-examined) |
| **F-7** (new) | provenance value column collapses to ~2 characters at 900px; **pre-existing**, present in the archived pre-round-7 frame, cosmetic/legibility |

Limitations §6.1–§6.5 continue to apply to every delta frame: fixture-backed session list
and replay (transcript-item rendering still unevidenced), dev-server rendering only,
Electron/Chromium only, static frames, and **no lifecycle claim** — this is observation,
not issuance or approval.
