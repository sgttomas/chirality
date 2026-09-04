# 04 — Implementation Plan

Seven tranches in dependency order. Each is one PR, one independent review, one owner merge. Each is usable on its own; the app is never left in a half state between tranches. Nothing here is selectable until the owner seats it (§7).

## 1. Ground rules for every tranche

- **Loop protocol.** Follow `loop/WORKPLAN_2026-09-03_app_dev_loop.md` "The loop protocol" exactly: Step 0 discovery with the A1 re-stage declaration (every tranche touches `frontend/`, which invalidates the staged R20 procedure for any later proof claim), sealed brief, frozen diff, independent `TASK + software-code-review` PASS over 100% of the diff before push, receipt, run record.
- **Evidence bar.** `docs/ISSUE_READINESS_PROFILES.md` §4 (D-APP-36): component render tests for every user-facing control and state; browser or screenshot review for layout, resize, overlay, and interaction changes, recorded with route, viewport, states, and outcome per `docs/ui/UI_POLISH_EXECUTION_PLAN.md` "Required evidence".
- **Registered checks.** `npm run typecheck`, `npm test` (full Vitest), focused Vitest for the tranche, `npm run build`, `git diff --check`, repo-wide harness self-check and pytest, APP-HOLD dispatch preflight, corpus status, receipts validator, change-scope validation. `harness:validate:premerge` and `validate:release-quality` may FAIL locally in the recorded absent-daemon-bindings class; defer to PR CI and never infer a pass.
- **Section 8 preservation (DEL-09-01-V3-01).** Its revision trigger is a merged product change touching `frontend/src/app/api/harness/**`, `frontend/src/lib/harness/**`, `frontend/src/lib/runtime-client/**`, `frontend/electron/**`, `runtime/**`, or the evaluator surfaces in `EVALUATOR_BYTES_revision2.tsv`. Tranches T1, T2, T4, T5, T6 are component and CSS work and do **not** trigger it. **T3 (new read endpoint under `app/api/working-root/`) does not match the list literally; confirm against the evaluator bytes file before claiming no trigger.** T7 (Electron second window, `frontend/electron/**`) and any change to `lib/harness/**` for the quote attachment **do** trigger a revision.
- **Fences.** No provider, network, tool, or release change in any tranche (F-APP-1, F-APP-2). No `_DomainEngines` (F-APP-3). No issuance (F-APP-4). No new status surface (F-APP-5): tranche state lives only in the owning deliverable's `_STATUS.md`.
- **Schema discipline.** New persisted fields are additive under `chirality.woven-workspace/v1` with sanitize-and-fallback readers and focused tests for missing, wrong-type, and out-of-range values (DEL-02-04 Remaining).
- **Retirement is a mount change.** Workbench and Pipeline code, routes, and tests stay. Do not delete them; do not "clean up" their CSS.

## 2. Tranche table

| # | Name | Depends on | Owning deliverable | Touches `electron/` or `lib/harness/` | Section 8 trigger |
|---|---|---|---|---|---|
| T1 | Centre invariance and retirement | — | DEL-02-02 (retirement), DEL-02-04 (state) | no | no |
| T2 | Header, Stone tokens, copy pass | T1 | DEL-02-01 (shell), DEL-01-03 (copy) | no | no |
| T3 | Right panel switcher, Files, Document viewer, Workflows view | T1 | DEL-02-03 (tree/viewer), DEL-02-02 (Who is working, Workflows), DEL-05-04 (Session view), DEL-07-03 (workflow file contract) | no (new `app/api/working-root/file` and `workflows` routes) | verify |
| T4 | Weaving: reference chips, Ask and Attach | T3 | DEL-02-03, DEL-02-01 | possibly `lib/harness/ui-attachments.ts` | yes if `lib/harness/**` changes |
| T5 | Activity strip and Activity view | T3 | DEL-02-04 | no | no |
| T6 | Left panel organisation, account row, popover, Settings view | T2, T3 | DEL-02-01 (left panel), DEL-02-05 (account, keys, runtime), DEL-02-04 (state) | no | no |
| T7 | Pop-out window, app icon, icns | T3, T6 | DEL-02-01 (icon), DEL-09-04 (icns, packaging integrity) | yes | yes |

Deliverable folders: `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-0n_*/`, `execution/PKG-05_.../DEL-05-04_Runtime_Replay_and_Transcript_View/`, `execution/PKG-09_.../DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/`, `execution/PKG-01_.../DEL-01-03_Product_Identity_and_Professional_Boundary_Copy/`.

## 3. Tranche detail

### T1 — Centre invariance and retirement (SR-01, SR-06, SR-08 placement only)

**Scope.**
- `dialogue-viewport.tsx`: remove `focusedSurface`; the primary is never `hidden`. Replay renders through a new `replaySlot` prop that the shell mounts in the right panel (T3 replaces the interim placement with the Session view; for T1 mount the existing lens in the coordination panel area under a "Session" tab so nothing is lost).
- `woven-dialogue-shell.tsx`: drop `WorkbenchSurface` / `PipelineSurface` imports and the `focusedSurface` memo; `activeSurface` collapses to `'dialogue'` only; `returnToPrimaryDialogue` keeps focusing the composer.
- `navigator.tsx`: `SURFACES` reduced to `dialogue`; remove the mode-group chevrons; keep the session list flat, sorted by `updatedAt` (T6 adds grouping).
- `woven-workspace-state.ts`: `WovenWorkspaceSurface` keeps its three literals for reader compatibility; writers only ever record `'dialogue'`.
- `app/page.tsx`, `app/chat/page.tsx`: unchanged. `/workbench` and `/pipeline` route files unchanged.

**Tests.** Update `woven-dialogue-viewport.test.tsx` (primary never hidden; no focused-surface return action), `woven-dialogue-navigator.test.tsx` (no Workbench/Pipeline groups), `woven-dialogue-shell.test.tsx`. Add: replay visible **and** primary visible at once; selecting replay leaves `[data-chat-input="primary"]` mounted and focusable.

**Acceptance.** With a recorded session selected, the composer is visible and accepts focus. No element with `data-focused-surface` exists in the woven route. `/workbench` still renders.

### T2 — Header removal, Stone tokens, copy pass (SR-10 to SR-15, SR-18, SR-21)

**Scope.**
- `shell-frame.tsx`: for `variant="workspace"` render no header at all. The wordmark moves into the Navigator's head. The runtime reconnect action moves to the activity strip's dot (T5; until T5 lands, keep the existing chip inside the activity shelf header so the action is never lost). The settings disclosure's contents move in T6; until then mount `RuntimeSettings` and `ApiKeySettings` behind a temporary "Settings" entry in the navigator footer. `ShellFrame` props `section`, `title`, `subtitle` become optional and unused by the woven route; the legacy shells keep their header.
- Context line (SR-21, SR-22, SR-23): a `ChatContextLine` under the composer box holding `FolderSelect`, `PersonaPicker`, the mode select, and the rung control; the folder is live only while the active session has no messages and a read-only label afterwards. In T2 the rung is derived from the tuple and offers *Specify…* (the specification form: agent from the Type 1 roster, permission, delegation policy); *Governed workflow…* is wired in T3. Delegation policy needs a per-session field carried by the session record and honoured by the delegation bridge (DEL-08-04), defaulting to none; until that lands the control is present and `No delegation` is the only enabled value. It writes through the existing `applyProjectRoot` for now (T6 makes the root per chat); "No folder" calls `clearProjectRoot`.
- `globals.css`: new token values (`03_TARGET_SPEC.md` §11) in the existing block; `.shell-wordmark` single colour, no `em` rule; hairline rules replace panel borders in the woven region; message box and context line rules per `03_TARGET_SPEC.md` §4 (SR-22); remove `.woven-eyebrow` usages from markup (rule may stay).
- `chat-panel.tsx:52-57`: mode labels; `persona-picker.tsx`: display names with identifier tooltips.
- All copy in `03_TARGET_SPEC.md` §10.

**Tests.** `shell-frame.test.tsx` (workspace variant renders no `header`; no `img[src="/chirality-app-icon.svg"]`; legacy variant unchanged), navigator test for the wordmark text "Chirality" with no `em`, `chat-panel-*` (labels; folder select live before first message and a label after; "No folder" state), a snapshot-free render test for the composer's structure (box: quote row when present, then field, attach, send; context line beneath: "Start in" or "Working in", folder, agent, mode). Browser review: 960px and 1440px, both themes, the context line wrapping rather than hiding at 480px centre width.

**Acceptance.** `grep -rn "Chira<em>" src` returns nothing. No `header` element in the woven route DOM. No `.woven-eyebrow` in the woven route DOM. The reconnect action is reachable and keeps its `aria-label`. Contrast checks in the token block still hold (record the measured ratios in the evidence).

### T3 — Right panel switcher, Files, Document viewer, Who is working, Session view (SR-02, SR-04, SR-05 drag and expand, SR-08)

**Scope.**
- New `components/woven-dialogue/right-panel.tsx`: header row with tabs or breadcrumb and the four controls; view registry `files | agents | activity | settings | document | session` (activity content lands in T5, settings in T6; T3 mounts placeholders that say nothing).
- `file-tree-panel.tsx`: file rows become buttons; `onOpen(path)`; keyboard per spec.
- New `components/woven-dialogue/document-view-panel.tsx` reusing `ChatMarkdown` and the type table in `03_TARGET_SPEC.md` §5.4; hand-off card; size guard.
- **New API** `app/api/working-root/file/route.ts`: `GET ?projectRoot=&path=` returning `{ path, size, mtime, mimeType, content | null, reason? }` for files under the validated working root only, using the same root validation and containment as `working-root/tree` and `readDeliverableContent`; 2MB default cap with `?force=1`; never follows symlinks outside the root; never reads dotfiles under `.git`. Add to the security-check inventory if `validate-harness-*` enumerates API routes (check `frontend/scripts/`).
- `coordination-panel.tsx` → "Who is working" view using `AgentsProjection`; Work projection unmounted (component and test stay).
- `selected-session-replay-lens.tsx` mounted as the Session view with the read-only banner and key-value block.
- Proposal card (SR-24, mechanism per SR-26): a registered deterministic `propose` tool exposed to Agent 0 and Agent 1 personas (owner DEL-06-03, permission overlay DEL-06-01) validates the tuple and plan reference, enforces once-per-chat-per-trigger against `chatRung.declined`, and emits `proposal.offered`; `proposal-card.tsx` renders from the `proposal.*` events through the existing harness event stream (additive event types, Q13 ruled; schema owner DEL-05-02); Accept / Adjust / Not now emit the answering events and the app applies them; Accept/Adjust/Not now call the same handlers as the context-line forms; collapsed states; `chatRung.declined` suppression. The agent-side clauses (HELP_HUMAN proposes rung 2, each Agent 1 proposes rung 3, triggers, once-per-chat) are `agents/` changes owned by DEL-08-01 and ship with the routed change notice.
- Workflows view (SR-23): `workflows-view.tsx`, `workflow-roadmap.tsx`, `new-workflow-form.tsx`, plus the *From other folders* library and *Bind to this folder* (Q10); a bounded `GET/POST /api/working-root/workflows` route reading and writing `.chirality/workflows/*.md` under the same containment as the file route, with the front-matter contract owned by DEL-07-03; *Follow* sets persona and mode through the existing session boot path and injects the roadmap through the persona composer's existing instruction-assembly seam (DEL-04-04) as a clearly delimited block. Templates come from `skills/` entries that declare `workflow: true` and their prerequisites.
- Resize: right handle bounds become `280..expandWidth`; expand toggle; per-view widths persisted (additive fields per `03_TARGET_SPEC.md` §12).

**Tests.** Render tests for: each view's header row and controls; breadcrumb back; file row open; hand-off card for an unsupported type; size guard; expand/return restoring widths; Session view banner. API tests for the new route: containment (path outside root → 403), symlink escape, cap, dotfile, mime detection. Browser review: drag range, expand at 1180px and 1440px, dark theme.

**Acceptance.** Every file in the tree either renders or shows the hand-off card; nothing shows an empty panel. The centre never drops below 420px. A workflow cannot be created with role or policy unset; following one changes the context line to *Following* and the next turn's system prompt carries the roadmap block; the workflow file never contains status, approval, or evidence fields.

### T4 — Weaving (SR-09)

**Scope.**
- `lib/shell/reference-resolution.ts` (new, pure): tokenises assistant text for working-root paths, `DEL-nn-nn`, `Receipt nnn`, `D-APP-nnn`; resolves against the loaded tree and deliverable roster; returns spans.
- `chat-markdown.tsx`: a `text` renderer that wraps resolved spans in `ReferenceChip`; chip click calls the right panel's `open`.
- `tool-stream-view.tsx`: `pathFields` values become chips.
- Document viewer: selection bar; Ask inserts the quote row (`{ path, startLine, endLine, text }`) into the composer; Attach adds a `UiAttachment`.
- Composer: quote row UI; on send, the quote is passed to the turn as an attachment. **Decision needed** on the wire shape (§6 Q2): either a new attachment `clientType: 'quote'` with the range in `displayName`, which needs no harness change, or a first-class field, which changes `lib/harness/ui-attachments.ts` and triggers Section 8 revision.

**Tests.** Resolver unit tests (positive, negative, ambiguous ids, paths with spaces). Render tests: chip hover text, chip click opens panel, selection bar actions, quote row remove. Fixture-based test that a quoted send produces the expected attachment payload.

**Acceptance.** In a transcript containing `DEL-09-01` and a working-root path, both are chips; clicking each opens the right target. A quoted send round-trips the range.

### T5 — Activity strip and Activity view (SR-07)

**Scope.** `activity-shelf.tsx` becomes `activity-strip.tsx` (32px, no resize, `role="status"`); the three stream views mount under the right panel's Activity view with sub-tabs; "Details" opens it. Remove the activity resize handle and the `activityHeight` writer (reader stays). Row sentences reuse T2's tool-call sentence function.

**Tests.** Strip idle/running/reconnecting states; Details opens the view and expands a collapsed panel; sub-tab switching; reduced-motion disables the pulse.

**Acceptance.** Centre height is identical before and during a turn.

### T6 — Left panel organisation, account row, popover, Settings view (SR-03, SR-17, SR-19, SR-20, SR-21)

**Scope.**
- Navigator: search, New chat, Pinned / groups / date buckets, titles from first message, folder line under each title, context menu, drag to group, archive, delete (local). State fields per `03_TARGET_SPEC.md` §12.
- Root per chat (SR-20, SR-21): `WorkspaceProvider` gains `knownRoots` and derives `projectRoot` from the active session's recorded root; the session list is assembled by calling `listHarnessSessions` once per known root and merging (bounded to the 50-root cap; errors per root are shown inline, not fatal). Switching chats switches the provider root, so Files, consent, and permissions follow the chat. New chat with a folder not yet known adds it to `knownRoots` after validation.
- Account split (SR-19): `AccountConsentSettings` is split into an app-wide account group and a per-folder group without changing the port calls. The fake port's per-root login remains underneath; the UI shows the account once. The consent fixtures' copy is updated only where it says sign-in is per root; every consent string keeps its root binding. **A Root-loop coordination notice is owed** stating that the App now presents sign-in as app-wide and asking Root DEL-02-09 to carry the shared-login amendment; file it with the tranche's run record. DEL-02-05-V3-03 stays gated on that contract.
- `account-row.tsx` and `account-popover.tsx` (new, `components/shell/`): status derived from the consent port snapshot (fake port until DEL-02-05-V3-03) and the runtime daemon status already polled by `RuntimeSettings`.
- Settings view: `AccountConsentSettings`, `RuntimeSettings`, `ApiKeySettings`, `ThemeControl` restyled into the four groups; **behaviour unchanged**; verbatim strings kept (`02_CURRENT_STATE.md` §7). Remove the temporary gear popover from T2.
- Popover's local-model switch calls the existing start/stop handlers; disabled with a tooltip when the bridge is unavailable (web build).

**Tests.** Grouping and title derivation as pure functions; context menu actions update state; account row states (signed in, signed out, stale consent, daemon stopped, daemon not installed, bridge unavailable) via the existing consent fixtures in `lib/consent/consent-ux-fixtures.ts`; popover switch calls start/stop; Settings groups render the same controls the current panels' tests assert (extend, do not weaken, `account-consent-settings-states.test.ts`, `runtime-settings.test.ts`, `api-key-settings-storage-states.test.ts`).

**Acceptance.** Every string listed as verbatim in `03_TARGET_SPEC.md` §10 appears unchanged. No email or key material is ever rendered (assert with the fixtures). No account line says "for this root"; every consent and permission line names the folder. Chats from at least two folders list together with the folder shown, and selecting each switches the Files view to that folder.

### T7 — Pop-out window, app icon, icns (SR-05 pop-out, SR-16)

**Scope.**
- `electron/main.ts`: `openPanelWindow(view, target)` creating a second `BrowserWindow` with identical `webPreferences`; register its `webContents` with `ipc-sender-policy.ts`; renderer route reads `?panel=`. IPC for "insert quote / attach into main window".
- `src/app/icon.svg` → `src/app/icon.png` (chalk mark, 512px); delete `icon.svg`; DEL-02-01 record-only note about `metadata.icons` stays true (file convention).
- `build/icon.icns` ← `assets/painted-field.icns`; `build/icon-macos.svg` retired (see `05_LOGO_AND_BRAND.md` §4 for the reproducibility record `scripts/generate-macos-icon.mjs` requires); `public/chirality-app-icon.svg` removed once no reference remains.
- DEL-09-04 packaging integrity: any manifest or hash list that pins `build/icon.icns` must be regenerated in the same PR.

**Tests.** Electron main: second window shares origin and preload, sender policy accepts it, closing it does not touch the main window's state. Renderer: `?panel=document&target=` renders only the viewer. Packaging: existing DEL-09-04 workflow tests updated for the new icns hash.

**Acceptance.** Section 8 preservation revision recorded per DEL-09-01-V3-01 (this tranche touches `frontend/electron/**`). Dock shows the chalk mark in a packaged build (owner-executed proof; agent may not claim it).

## 4. What to reuse, file by file

| Reuse | From | For |
|---|---|---|
| `buildNavigatorSessionGroups`, `formatSessionWhen` | `navigator.tsx` | date buckets, deterministic times |
| `buildRecordedAgentHierarchy` | `lib/woven-dialogue/recorded-agent-hierarchy.ts` | Who is working |
| `createSelectedSessionReplayLoader`, `guardRecordedSessionSelection` | `lib/woven-dialogue/` | Session view |
| `resolveDocumentViewState`, `DocumentView` roster logic | `lib/shell/document-view-state.ts`, `document-view.tsx` | Document view for deliverable files |
| `harness-event-views.ts` rows | `lib/shell/` | Activity view and strip |
| Resize handle markup and keyboard handling | `woven-dialogue-shell.tsx:330-440` | both panels |
| Theme stamping | `theme-control.tsx` | Appearance |
| Consent fixtures | `lib/consent/consent-ux-fixtures.ts` | account row and Settings tests |

## 5. Evidence package per tranche

1. Focused Vitest stdout and JSON for the tranche's tests; full Vitest summary.
2. Browser review record: route, viewport(s), theme(s), states exercised, screenshots, outcome. Required for T2, T3, T5, T6, T7.
3. Contrast measurements for any token change (T2).
4. For T3: API containment test output listed separately.
5. For T7: Section 8 revision folder per DEL-09-01-V3-01's `Return` contract.
6. Run record under `execution/_Coordination/AgentRuns/APPDEV_SHELL_Tn_<date>/` and a `_run_records/` entry in each owning deliverable.

## 6. Open questions for the owner

| # | Question | Default if unanswered | Blocks |
|---|---|---|---|
| Q1 | Delete-chat semantics: local hide only (default) or also delete the runtime session record? | local hide only; record untouched | T6 |
| Q2 | Quote wire shape: attachment with `clientType: 'quote'` (no harness change) or a first-class turn field (changes `lib/harness/**`, triggers Section 8 revision)? | attachment | T4 |
| Q3 | Should `/workbench` and `/pipeline` routes stay reachable by URL, or 404 while the code stays? | reachable, unlisted | T1 |
| Q4 | Is a 2MB in-app file cap acceptable, and should PDFs open in-app or hand off? | 2MB; PDFs in-app | T3 |
| Q5 | Pop-out in the first release, or defer T7's window work and ship only the icon change? | defer window; ship icon | T7 |
| Q6 | Chat titles from the first message: acceptable to derive from message text that may contain a path or a secret-shaped string? Proposed: derive, then apply the existing redaction helper. | derive with redaction | T6 |
| Q7 | Does the account row show the OpenAI dot at all before DEL-02-05-V3-03 lands, or only the local model dot? Proposed: show it, driven by the fake port, labelled `Opt-in Preview` in the tooltip. | show | T6 |
| Q8 | Root-loop routing for SR-19: does the owner want the shared-login amendment raised as a Root packet now (so DEL-02-05-V3-03 can consume it), or after T6 lands with the split UI on the fake port? | after T6 | DEL-02-05-V3-03 |
| Q9 | Folder menu contents for a new chat: known folders only, or also a "Recent in Finder" list? Proposed: known folders plus "Choose folder…" only. | known + choose | T2 |
| Q10 | **Ruled 2026-09-04:** in the folder under `.chirality/workflows/`, plus a library and *Bind to this folder* for reuse in other folders (SR-24). | — | — |
| Q11 | **Ruled 2026-09-04:** a specification is the tuple folder, agent, delegation policy, roadmap; not skills (SR-24). | — | — |
| Q12 | **Ruled 2026-09-04:** the permission mode is the fifth item of the specification tuple (SR-24). | — | — |
| Q13 | **Ruled 2026-09-04:** proposals are additive harness event types in the session record (SR-24, spec §4.3). | — | — |
| Q14 | Where do client-owned agents and skills live? The bundled instruction root is protected and separate from the working root (K-ROOT-1, DEL-07-01). Proposed: a layered instruction root, bundled base plus an organisation layer the consultant ships and the client owns, hash-pinned, same protections. Decide before any tranche touches instruction assembly. | organisation layer | T3, DEL-08-01 |
| Q15 | Leave-behind currency: should the app report when a workflow file's `roadmapSource` hash is behind the current protocol or template (as the repo's corpus-drift check does)? Proposed yes, as a line in the Workflows view. | report | T3 |
| Q16 | Several people sharing one folder: workflow position and proposal records are per folder while sessions are per person. Proposed for v1: position advances only at gates, which are human acts, and the file records who advanced it; concurrent editing is documented as unsupported until the thesis's §9.4.6 work. | gate-only advance | T3 |

## 7. Proposed Remaining items (for the owner to seat; PROPOSAL, not selectable)

Format follows the v3 items already in the PKG-02 statuses. Gates, loci, checks, and returns are proposals.

**DEL-02-02-V3-03** (`SELECTABLE`) — Retire Workbench and Pipeline from the woven route and make the primary dialogue invariant (T1). Depends: none. Write locus: `frontend/src/components/woven-dialogue/**`, `frontend/src/__tests__/components/woven-dialogue-*.test.tsx`. Checks: registered frontend gates, D-APP-36 render tests, review PASS. Return: woven route with no focused surface; replay visible beside a visible primary; retired routes intact. Removed when: merged and browser evidence recorded. Basis: `plans/shell-redesign_2026-09-04/` SR-01, SR-06, SR-08.

**DEL-02-01-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed`) — Header removal, Stone tokens, composer folder control, and plain-language copy pass (T2). Write locus: `shell-frame.tsx`, `navigator.tsx`, `globals.css`, `chat-panel.tsx`, `persona-picker.tsx`, a new `folder-select.tsx`, tests. Return: no header in the woven route; wordmark in the left panel; folder select live before the first message and a label after; token block updated with measured contrast. Basis: SR-10 to SR-15, SR-18, SR-21.

**DEL-02-03-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed`) — Right panel view switcher, clickable file tree, in-app document viewer with drag and expand, bounded file read endpoint (T3). Write locus: `components/woven-dialogue/**`, `components/shell/file-tree-panel.tsx`, `app/api/working-root/file/**`, `lib/woven-dialogue/woven-workspace-state.ts` (additive), tests. Return: every tree file opens or hands off; API containment tests. Basis: SR-02, SR-04, SR-05.

**DEL-02-02-V3-04** (`NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed; Q14 to Q16 ruled`) — Workflows view, roadmap, New workflow form, library and Bind, the derived rung with its two forms, the proposal card, and the workflow file read/write route (T3 part). Depends on DEL-07-03's front-matter contract for the workflow file. Basis: SR-23, SR-24.

**DEL-06-03-V3-0n** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`) — The `propose` tool: schema, validation against roster and policy values, plan-reference resolution from Agent 1 procedures, once-per-chat enforcement, `proposal.offered` emission. Basis: SR-24, SR-26.

**DEL-08-01-V3-0n** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`) — Instruction-package clauses: HELP_HUMAN direct assistance and rung-2 proposal with named triggers and once-per-chat; each Agent 1's rung-3 proposal clause referencing its own protocol as the roadmap source; routed change notice per the agent-index rule. Basis: SR-19 discussion, SR-24.

**DEL-08-04-V3-0n** (`NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected`) — Per-session delegation policy field honoured by the delegation bridge (none / ask per brief / approve brief writes / bounded briefs), defaulting to none. Basis: SR-24.

**DEL-07-03-V3-0n** (`NOT_SELECTABLE_UNTIL: Q10 ruled`) — Governed workflow file contract: front matter, roadmap grammar with gate markers, the rule that it steers and never records. Basis: SR-23; `03_TARGET_SPEC.md` §5.10.

**DEL-05-04-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed`) — Session view: replay lens mounted in the right panel with read-only banner and parent link (T3 part). Basis: SR-08.

**DEL-02-03-V3-02** (`NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed and Q2 ruled`) — Reference chips in replies and activity rows; Ask and Attach from the viewer; quote row in the composer (T4). Basis: SR-09.

**DEL-02-04-V3-01** (`NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed`) — Activity strip and Activity view; retire the resizable shelf (T5). Basis: SR-07.

**DEL-02-01-V3-02** (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 and DEL-02-03-V3-01 landed; Q1, Q6 ruled`) — Left panel chat organisation: search, titles, pins, groups, archive, context menu (T6 part). Basis: SR-03.

**DEL-02-05-V3-05** (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 and DEL-02-03-V3-01 landed; Q7 ruled`) — Account row, account popover, Settings view hosting the account-consent (split app-wide / per-folder), runtime, key, and appearance panels unchanged in port behaviour (T6 part). Fake consent port until V3-03. Ships the Root-loop coordination notice for the shared-login amendment. Basis: SR-17, SR-19.

**DEL-02-01-V3-02a** (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed`) — Root per chat: `knownRoots`, multi-root session listing, folder line in the chat list, provider root derived from the active session (T6 part). Basis: SR-20, SR-21.

**DEL-02-01-V3-03** (`NOT_SELECTABLE_UNTIL: DEL-02-05-V3-05 landed; Q5 ruled`) — App icon replacement (`src/app/icon.png`, `public/` cleanup) and, if Q5 allows, the pop-out panel window (T7 renderer and electron part). Basis: SR-05, SR-16.

**DEL-09-04-V3-0n** (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-03 selected`) — `build/icon.icns` replacement with packaging-integrity regeneration and the reproducibility record for the raster icon (T7 packaging part). Basis: SR-16; `05_LOGO_AND_BRAND.md` §4.

**DEL-01-03 note** — the copy table in `03_TARGET_SPEC.md` §10 is offered to the product-identity deliverable as a candidate amendment to its boundary copy; no item proposed here.

## 8. Sequencing summary

```
T1 ──► T2 ──┐
  └──► T3 ──┼──► T4
         ├──► T5
         └──► T6 ──► T7
```

T1 alone fixes the contradiction with SR-01 and is the smallest safe first PR. T2 and T3 can run in parallel worktrees after T1. T6 needs both. T7 last.
