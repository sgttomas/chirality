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
