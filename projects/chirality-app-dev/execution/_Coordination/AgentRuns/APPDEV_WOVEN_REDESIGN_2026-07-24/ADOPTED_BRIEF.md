# Implementation Tranche Brief — Woven Dialogue Visual Redesign & IA Consolidation

**Brief ID:** `TRB-APPDEV-WOVEN-REDESIGN-2026-07-24`
**Status:** `CANDIDATE — awaiting owner adoption (K-AUTH-1; D-GOV-04)`
**Author:** Claude Fable 5, HELP_HUMAN (Agent 0) loop operator, 2026-07-24
**Working root:** `projects/chirality-app-dev/`
**Epistemic status:** agent-authored candidate; every load-bearing code/test claim below was re-verified against the live tree on 2026-07-24 by two read-only Opus verifier subagents plus three earlier Explore surveys this session. Sources govern on any disagreement.

---

## 1. Authority basis

| Instrument | Bearing |
|---|---|
| **D-APP-74 / SCA-APP-004** (RULED 2026-07-23) | Woven Dialogue + Work/Agents Coordination Panel is the ruled target IA; fixed presentation clauses of D-APP-28/30/31/32 and D-APP-56 R4-P07 prospectively superseded. This tranche implements *presentation* inside that ruling's invariants. |
| **D-APP-36** (RULED 2026-06-21) | Render-evidence bar: component/render tests required for user-facing controls/state; browser-level evidence where layout/overlap/interaction risk is high (this tranche qualifies). |
| **Owner in-session directions, 2026-07-24** (this chat; to be transcribed verbatim into the tranche run record and receipt at closeout as chat-evidence) | (a) calm-editorial direction ratified — "This is the default setting now"; (b) light mode is the primary target; (c) Artifacts ceases to be a navigator surface, folds into Workbench; (d) navigator becomes mode-scoped session history; (e) app logo = quincunx tile mark derived from owner-supplied artwork; (f) this brief + Opus subagents at Agent 1/2. |
| **Approved mockup** | https://claude.ai/code/artifact/8a8fb85d-221c-4b12-b74d-276fc0227e50 (visual reference of record for this tranche). |
| **Hard fences** | F-APP-1..5 all honored: no provider/network change, no release/signing/notarization claims, no `_DomainEngines`/piping writes, no issuance, no new standing surfaces. K-ENGINE-6: this is UI/governance-presentation work over the existing harness — on-strategy. |

**What this brief does NOT authorize:** old-UI retirement (separate owner acceptance per D-APP-74), route/query/API/SSE changes, runtime or dispatch semantics changes, packaging/DMG re-icon (deferred, §8-D3), lifecycle transitions.

## 2. Scope

**In:** `projects/chirality-app-dev/frontend/**` (source, styles, tests, one SVG asset, font asset files), plus closeout records: affected `DEL-*/_STATUS.md` `## Remaining` + `_run_records/**`, `plans/PLAN_COMPLETION_LOG.md`, `loop/LOOP_RECEIPTS.md`, AgentRuns control-plane records.
**Out:** everything else. Legacy loop-first UI (`?legacy=1` and its shells/sidebar) is a frozen compatibility surface — it inherits only what flows through shared chrome (`ShellFrame`) and must remain functional and test-green; no legacy-specific restyling.

**Owning deliverables:** DEL-02-01 (shell composition & compatibility navigation), DEL-02-02 (Workbench/Pipeline presentation), DEL-02-04 (versioned workspace state — theme + navigator state), DEL-08-02 (guarded session routing — navigator history selection), with DEL-05-04 semantics consumed read-only (replay lens).

## 3. Design specification (from the approved mockup)

### 3.1 Tokens (target values; single source in `globals.css` `:root` block)

| Token | Light (default) | Dark |
|---|---|---|
| `--ground` | `#F8F5EE` | `#171511` |
| `--surface` | `#FCFAF4` | `#1C1A15` |
| `--ink` / `--ink-soft` / `--ink-faint` | `#29231A` / `#5F584A` / `#948B79` | `#EAE4D6` / `#A89F8C` / `#79715F` |
| `--rule` / `--rule-strong` | `#E6E0D1` / `#D0C8B5` | `#2C2921` / `#3D392D` |
| `--accent` (dusty sienna — strokes only, never fills) | `#9C5730` | `#C67C50` |
| `--accent-soft` | `#F1E5D6` | `#322316` |
| `--cta` / `--cta-ink` (primary actions) | `#33291D` / `#F6F0E2` | `#E8DCC1` / `#292216` |
| `--sage` / `--sage-soft` (human-approved; healthy status) | `#5E7960` / `#E6ECDE` | `#97B394` / `#232B1F` |
| `--rose` / `--rose-soft` (agent proposal / awaiting human) | `#9C6479` / `#F2E4EA` | `#C795AC` / `#302128` |
| `--slate` / `--slate-soft` (runtime) | `#5B6B85` / `#E6EAF0` | `#8CA0BE` / `#232A35` |
| `--card` / `--composer` | `#FFFDF8` | `#211E18` |
| `--danger` | `#A32E2E` | `#D3705F` |

Composition rules (normative for every styling decision in this tranche):
1. **One voice at a time.** CTA (cream/espresso) is the only filled emphasis; accent appears only as strokes/markers; semantic chips stay tinted-whisper; everything else is ink on ground.
2. **Boxes encode provenance.** Only provenance-bearing objects (artifact cards, permission requests) get borders+cards; panes separate by hairline rules and whitespace.
3. **Light is primary.** Light theme is default for all users; dark is an explicit in-app choice (light/dark/system selector, default **light**, persisted in DEL-02-04 versioned workspace state). No silent `prefers-color-scheme` switching.
4. Semantic state colors are never the interaction accent. Green reads healthy/approved — never orange for status dots.

### 3.2 Typography
- Display face: serif for wordmark/panel headings (`--font-display`). Body: humanist sans. Mono: provenance/source strings.
- **Fonts must actually ship** — bundled files via `next/font/local` (committed to the repo; no runtime network, F-APP-1 untouched). Recommended pair (owner decision §8-D1): **IBM Plex Serif + IBM Plex Sans + IBM Plex Mono** (OFL; matches existing declared identity).
- Scale per mockup: 15px/1.62 dialogue text, 13–14px UI, 10.5–11px uppercase tracked labels.

### 3.3 App logo
Quincunx tile mark (from owner-supplied artwork): rounded cream tile `#F0E9D8` with hairline `#D8CFBA` border; five rounded squares with slight rotations (−3.5°…+4°): four umber (`#4A3423`, `#543C28`, `#503927`, `#46311F`) corners, terracotta `#BC5A28` center. Fixed colors across themes. Replaces the current mark wherever the shared chrome consumes it (blast radius in §5, Stage B3).

### 3.4 IA & interaction
- **Top bar:** single 48px bar — logo + wordmark, surface name, working-root chip (truncating, opens the full working-root/runtime controls as a disclosure), runtime status dot (sage when connected), theme control. The current stacked brand header + Working Root card collapses into this.
- **Navigator = mode-scoped session history:** modes Dialogue / Workbench / Pipeline as expandable groups; active mode expands showing its recent recorded sessions (cap ~4 + "All sessions (N)"); inactive modes collapse. Selecting a past session routes through **guarded recorded-session selection into the read-only replay lens** (DEL-08-02/DEL-05-04 semantics) — never resumes/merges the live dialogue. Live session marked distinctly.
- **Artifacts surface removed; Workbench absorbs it:** the `'document'` navigator entry ("Artifacts") is removed; `DocumentView` mounts as a "Documents" block inside `WorkbenchSurface` ("Documents, evidence & contracts"). `DocumentView` itself and the legacy sidebar Document/Files tabs are untouched (compatibility). Workspace-state `focusedArtifact`/`dialogueAnchorId` fields are **retained** (they serve the ruled inline-artifact mechanism, not the removed page).
- **Ruled invariants preserved verbatim:** mounted primary transcript+composer across in-shell presentation changes; Work/Agents panel toggle; projection non-authority; replay isolation; all routes (`/`, `/chat`, `/workbench`, `/pipeline`), `?agent=`, `?legacy=1`, unknown-param tolerance; every `data-*` hook and ARIA contract listed in §6.

## 4. Verified constraints the work must hold (from live-tree verification)

*(§4 facts were verified 2026-07-24; verifier returns are archived in the tranche AgentRuns record at execution time.)*

- `[data-chat-input="primary"]` focus hook: queried in `agent-matrix.tsx` and `woven-dialogue-shell.tsx`; input in `chat-panel.tsx`. Must survive unchanged.
- ARIA scaffolding: resize `role="separator"` + value attrs, `aria-pressed` tabs, permission `role="alertdialog"`/`aria-modal`, `aria-live` regions, landmark roles.
- Test-coupled markers that survive or get updated in the same stage: `data-woven-surface`, `data-focused-surface`, `data-work-class`, `data-replay-*`, `data-legacy`, `loop-grid`/`loop-main`/`loop-sidebar`, `harness-status-badge--*`.
- Streaming path (UIEvent/HarnessEvent engines → React context) is DOM-independent; restyle must not touch `src/lib/harness/**`.
- **Sessions (verified):** one enumeration path — shell → `listHarnessSessions` → `GET /api/harness/session/list` → daemon `listSessions`. `SessionRecord` carries `sessionId, projectRoot, persona, mode, createdAt, updatedAt` + parentage/agentType optionals; **no title/label field and no UI-surface field**. The `mode` field is *permission posture* (`readOnly|ask|workspaceWrite|bypass|governed|direct`) — not dialogue/workbench/pipeline. `activeSurface` is unpersisted React state, never sent at session create. **Retroactive surface derivation is impossible**; canonical tag-forward would require `SessionCreateRequest` → `SessionStore.create` plumbing in root `runtime/packages/{contracts,core}` — **outside this loop's write fence** (D-APP-73 surface). See §8-D2 for the in-fence path.
- **Workspace state (verified):** `chirality.wovenWorkspace.v1` in `localStorage`, schema string `chirality.woven-workspace/v1`, sanitize-with-fallback reader + non-destructive legacy migration. New navigator/theme fields are **additive under the existing v1 schema string** (optional-with-default); do **not** bump the schema constant without adding a v1 branch, or all stored state is silently discarded (`woven-workspace-state.ts:158` hard-rejects other schemas). One test breaks on any added field (`woven-workspace-state.test.ts:39` `toEqual` on defaults) — update in-stage.
- **Logo (verified):** exactly one source consumer (`shell-frame.tsx:85` `<img src="/chirality-app-icon.svg">`) + two CSS rules (`globals.css:80-88`, `:2160-2163`); no test asserts it. **Packaging gap:** no favicon, no `metadata.icons`, no `BrowserWindow.icon`, no electron-builder `icon` key anywhere — the packaged app ships Electron's default icon today (§8-D3).
- **Fonts (verified):** greenfield — no `next/font`, no `@font-face`, zero font binaries in the repo; the declared "IBM Plex" names resolve only if host-installed. Next 14.2.35 supports `next/font/local`. `--font-mono` is already referenced-but-undefined at four `globals.css` sites (ready-made variable hook). Hardcoded literals to replace: `globals.css:30, 701, 996, 1205, 1306, 1681`. No test asserts font-family strings.
- **Test surface (verified):** no snapshot tests; **no test asserts any color, token value, or font-family string**, and the vitest suite never parses CSS (no vitest config; `renderToStaticMarkup`/`react-test-renderer` in node env). Pure token-value changes cannot break tests — only markup/class/type restructuring can — and **`npm run build` is therefore the only automated proof the CSS/font rewrite compiles**. Guaranteed breaks to fix in-stage: `shell-frame.test.tsx:37-38` (exact full-string `className` + exact `['PORTAL']` children on the `/` anchor) [Stage A]; `woven-dialogue-viewport.test.tsx:52-62` (`id:'document'` fixture + `data-focused-surface="document"`; removing `'document'` from the `FocusedDialogueSurface`/`WovenSurface` unions fails **typecheck**, not vitest) [B1]; `workbench-surface.test.ts` (unmocked `DocumentView` import graph → must `vi.mock`; exact `disabled=""` count 4; exact `<button type="submit" disabled="">Apply Transition</button>` strings — no className may be added to those elements) [B1]; `chat-panel-failed-send.test.ts:121` (`findByProps({className:'chat-input-row'})` exact; attachment chip `title` exactly once; Send label a bare text child) [C]; `woven-workspace-state.test.ts:39-58` (exhaustive `toEqual` on defaults — breaks on ANY added field) [A/B2]; `layout-state.test.ts:111-120` (exact grid-template string — **never rename `--pane-handle-width`/`--pane-chat-width`/`--pane-file-tree-width`**) [A].
- **Trap families (bind into every stage brief):** exact-string HTML matches on `<option>`/submit buttons in workbench + pipeline tests; exact `disabled=""` counts (`workbench 4`, `permission-cards 0/2`, `agent-matrix 0`); bare-text button labels (`>Open<`, `>Loop<`, `>Pipeline<`, `Send`) — no icon/span wrapping; replay lens: exactly 1 `<button>` and forbidden verb labels (`Send/Continue/Interrupt/Allow/Deny/Resume/Boot/Delete`); Work projection: zero `<button>` and `not.toContain('approved'/'assigned')` over the whole markup; **ARIA polarity split** — `role="tab"` REQUIRED in `WorkspaceSidebar`, FORBIDDEN in `CoordinationPanel`/`ActivityShelf` → session lists use `aria-expanded`/`aria-pressed` only; node test env has no `window`/`matchMedia`/`localStorage` → guard all access and extend per-test mock lists (navigator test: any new provider; workbench test: `document-view`; shell-frame test: the theme module).
- **Coverage gaps D-APP-36 obliges this tranche to fill:** `woven-dialogue-shell.tsx` has no direct render test (its only referencing test mocks it entirely), and none of the Working Root controls (`Apply Path`, `Choose Folder`, `Clear`, error/current states) is asserted anywhere — the recomposed top bar, theme control, Workbench Documents block, navigator session lists, and the empty-state fix all require new render tests, not just non-breakage.

## 5. Work breakdown and orchestration

**Runtime hierarchy (per owner direction this run):** HELP_HUMAN (Agent 0, this loop operator) supervises; **one WORKING_ITEMS-posture Agent 1 instance on `opus-5`** manages the package; **all Agent 2 instances on `opus-5`**. Platform-native subagent facility carries the delegation (AGENTS.md allows the loop's native hierarchical facility when briefs/scopes/parentage/returns are frozen — they are frozen in this document + per-stage sealed briefs derived from it). Every stage brief declares read scope, write targets, dependencies, expected returns, and its fan-in gate; sibling write scopes are disjoint or serialized through the named integration owner.

**`globals.css` is the one shared write surface** → its edits are serialized: Stage A owns it exclusively; later stages append only within stage-labeled sections coordinated through the Agent 1 integration owner.

| Stage | Content | Write scope (disjoint unless noted) | Depends on |
|---|---|---|---|
| **0. Setup** (Agent 1 inline) | Branch `feat/woven-redesign` off `main`; commit font asset files under `frontend/src/fonts/` (or confirmed location); baseline: full vitest + typecheck green pre-change | branch, font files | — |
| **A. Tokens & chrome** (Agent 2 ×1 — sole `globals.css` owner this stage) | Rewrite token block + component styles to §3.1/3.2; `next/font/local` wiring in `layout.tsx`; ShellFrame → compact top bar (§3.4); theme selector (light default) with DEL-02-04 versioned-state persistence + migration; update ShellFrame-coupled tests | `globals.css`, `shell-frame.tsx`, `layout.tsx`, theme/state lib, their tests | 0 |
| **B1. Artifacts→Workbench fold** (Agent 2 ×1) | Remove `'document'` from navigator/shell/viewport unions & entries; mount `DocumentView` block in `workbench-surface.tsx`; update `woven-dialogue-viewport` + `workbench-surface` tests | `navigator.tsx`, `woven-dialogue-shell.tsx`, `dialogue-viewport.tsx`, `workbench-surface.tsx`, their tests | 0 (parallel with A; no shared files — navigator styling hooks coordinated via A's published class contract) |
| **B2. Navigator session history** (Agent 2 ×1) | Mode groups + per-mode recent-session lists per §3.4 over the verified `listHarnessSessions` source; `sessionId → surface` attribution map + navigator-group state as additive v1 fields in DEL-02-04 workspace state (no schema-string bump; update `woven-workspace-state.test.ts`); selection → `guardRecordedSessionSelection` → read-only replay lens; unattributed sessions under "All sessions" | `navigator.tsx` (serialized B1→B2), `woven-workspace-state.ts`, shell wiring, tests | B1, A (state schema) |
| **B3. Logo** (Agent 2 ×1, small) | New SVG mark per §3.3 replacing `public/chirality-app-icon.svg` (sole source consumer `shell-frame.tsx:85` + 2 CSS rules); add favicon + Next `metadata.icons` from the same mark; `.icns`/electron-builder icon recorded as DEL-09-04 residual (§8-D3) | icon asset, `layout.tsx` metadata, favicon files | 0 (parallel) |
| **C. Defect & polish** (Agent 2 ×1) | Fix chat-panel empty-state/attachments overlap (browser-verified); density/responsive breakpoints; reduced-motion audit; dark-theme parity pass | `chat-panel.tsx`, stage-C `globals.css` section (serialized after A/B2), tests | A, B1, B2 |
| **V. Independent verification** (Agent 2 ×2, adversarial, read-only + browser) | V1: invariant sweep — every §4 hook/contract, routes/params, legacy UI functional, projection non-authority wording; V2: D-APP-36 browser evidence — screenshots light+dark of all surfaces at 3 widths, overlap defect proven fixed; both attempt to REFUTE stage returns | none (read + screenshots) | each stage's fan-in; final after C |
| **Close** (Agent 1 + Agent 0) | Full gate run (§6); DEL `_STATUS.md` Remaining updates + `_run_records/**` per owner ruling §8-D4; `PLAN_COMPLETION_LOG.md`; owner-direction transcription; receipt + validator; PR — **owner merges** | record surfaces | V green |

Failure isolation: a failed stage blocks only its dependants (B2 blocks on B1; C blocks on A/B1/B2; B3 independent). Partial returns are not accepted at fan-in; the Agent 1 validates each return against its sealed brief before integration.

## 6. Acceptance gates & evidence (all required)

- **Commands (verbatim from `frontend/package.json`):** `npm run test` (full vitest) · `npm run typecheck` (mandatory — B1's union removals are type-level changes) · `npm run build` (mandatory for Stage A — sole automated proof the token/font rewrite compiles; stop any dev server first) · `npm run validate:release-quality` as the closeout evidence wrapper. `npm run harness:validate:premerge` is conditional — this tranche does not touch session boot/SSE/turn behavior, so if skipped, **record the skip and reason explicitly** (RQG §3 evidence-skip rule, not a waiver). Packaging gate (`instruction-root:integrity`, `desktop:pack`) triggers **only if** `package.json` `build.files`/`extraResources` change — placing fonts under `src/` and swapping `public/chirality-app-icon.svg` does not trigger it.
- **Generated evidence artifacts to cite:** `frontend/artifacts/harness/release-quality/latest/summary.json` (+ section9; + section8 only if premerge runs).
- D-APP-36: component/render tests updated in the same stage as any markup/class change, **plus new render tests** for every new user-facing control and its states (theme control incl. light-default; recomposed top bar + Working Root controls; Workbench Documents block present/loading/empty/error; navigator session lists expanded/collapsed/empty/loading/guarded-while-turn-running; chat empty-state arrangement); browser screenshots (light+dark, ≥3 viewport widths) for top bar, navigator, dialogue+composer, workbench (with Documents block), pipeline, coordination panel, replay lens — with route, viewport, states exercised, and outcome recorded per `docs/ui/UI_POLISH_EXECUTION_PLAN.md`.
- Route/param compatibility proof: `/`, `/chat`, `/workbench`, `/pipeline`, `?agent=`, `?legacy=1`, unknown params.
- Legacy surface: loads and passes its existing tests unmodified (shared-chrome changes excepted and explicitly evidenced).
- Accessibility: existing ARIA contracts intact; focus-visible states on new controls; `prefers-reduced-motion` respected; AA contrast for all token pairs (checked light AND dark).
- Containment: diff confined to §2 scope; `git diff --check`; repo `self-check` exit 0; receipt validator pass before/after.
- No wording anywhere implying release-readiness/certification (F-APP-2).

## 7. Records & closeout

Chat-only owner directions (§1 row 3) transcribed verbatim into the tranche run record as evidence-not-ruling; rationale artifacts for any D-APP-60/64 latitude exercises land in the owning deliverable's `_run_records/**`; one versioned receipt appended to `LOOP_RECEIPTS.md` citing this brief's ID, gate outcomes, and pass/fail-only check summary; receipt validator re-run. Owner merge of the PR is the terminal integration act.

## 8. Open decisions for the owner (answer at adoption; defaults applied if adopted as-is)

- **D1 — Font pair.** Default: bundled IBM Plex Serif / Sans / Mono (OFL, matches existing identity). Alternative: name any pair you prefer (licensing permitting).
- **D2 — Session mode-attribution.** Verified: no surface field exists on session records; retroactive derivation impossible; canonical (daemon-side) tag-forward requires root `runtime/packages/{contracts,core}` changes — outside this loop's fence and this brief. Default: **client-side tag-forward via DEL-02-04 workspace state** — the shell records `sessionId → surface` in the versioned local workspace state at session creation; navigator history lists derive from that map; unattributed (pre-existing, or other-machine) sessions appear under "All sessions" only. This is honest as a *projection convenience* (local annotation creates no project truth, per D-APP-74) and keeps the tranche fully in-fence. Alternative: additionally route a coordination notice to the root runtime loop proposing canonical surface metadata on `SessionCreateRequest` for a future runtime tranche (recommended as a notice either way; the client-side map then becomes a fallback).
- **D3 — Packaged app icon (.icns/DMG) and favicon.** Verified gap: the app today has **no favicon, no Next `metadata.icons`, no Electron window icon, and no electron-builder `icon` key** — packaged Desktop ships Electron's default icon. Default: this tranche adds the in-app SVG swap **plus** the cheap web-side wins (favicon + `metadata.icons` from the same mark — still `frontend/**`, no packaging gate); the `.icns`/electron-builder icon is recorded as a named residual for DEL-09-04. Alternative: include the full `.icns` derivation here (adds packaging-gate evidence burden to this tranche).
- **D4 — PR #323 ledger reconciliation.** Default: **fold into this tranche's closeout** — the same DEL record updates that close this tranche also record the PR #323 implementation against the seven affected deliverables (they share files and owners; one reconciliation pass, no separate tranche). Alternative: separate reconciliation tranche first.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Exact-markup test assertions make ShellFrame recomposition churn-heavy | Verifier-B's impact map front-loads every brittle assertion into Stage A's brief; tests updated in-stage, never deferred |
| Mode-attribution for session history under-specified | D2 tag-forward default keeps B2 bounded; anything wider returns to the owner |
| `globals.css` merge conflicts across stages | Single-owner-per-stage serialization (§5); Agent 1 is integration owner |
| Dark theme regressions while light-first | V2 evidences both themes every surface; token-only discipline (no hex outside the token block) |
| Scope creep into runtime/dispatch | Stage briefs name `src/lib/harness/**` read-only; V1 refutation sweep includes a diff-path audit |
