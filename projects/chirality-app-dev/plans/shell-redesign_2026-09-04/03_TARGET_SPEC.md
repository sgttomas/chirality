# 03 — Target Shell Specification

The mock in `mock/chirality-shell-mocks.html` is the visual reference; this document is the written contract. Where they differ, the numbers here win and the mock should be corrected. Walkthrough step numbers refer to the mock's Walkthrough tab.

## 1. Layout

```
┌────────────┬──────────────────────────────────────────┬──────────────────┐
│ Chirality  │ CENTRE                                   │ RIGHT            │
│ search     │ primary                                  │ tertiary         │
│ + New chat │ dialogue transcript                      │ one view at a    │
│ chats      │                                          │ time             │
│ (all       │ ┌──────────────────────────────────────┐ │                  │
│  folders)  │ │ message                        ⊕ (↑) │ │                  │
│            │ └──────────────────────────────────────┘ │                  │
│ ─────────  │  Working in [folder] · [agent] · [mode] · [rung] │              │
│ account    │                                          │                  │
├────────────┴──────────────────────────────────────────┴──────────────────┤
│ ● Idle · Last turn: 5 actions · 12 s                          Details ▸ │  strip
└────────────────────────────────────────────────────────────────────────────┘
```

There is no header row (SR-12). The three panels start at the top of the window; the Electron window keeps the system title bar, so the traffic lights are unaffected.

| Region | Default | Min | Max | Collapsed | Persisted |
|---|---|---|---|---|---|
| Left panel | 240px | 220 | 360 | 56px icon strip | width, collapsed |
| Right panel | 300px | 280 | expand width | 56px label strip | width **per view class** (files, document, activity, session, settings), collapsed |
| Centre | remainder | 420 | — | never | — |
| Expand width | 60% of window, rounded to 8px | | | | — |
| Activity strip | 32px | fixed | fixed | never | — |

Expand (SR-05): right panel width becomes the expand width, left panel collapses to its strip, centre gets the remainder. The same control restores the previous right width and the previous left state. Starting to type in the composer while expanded restores the previous right width (walkthrough step 6). Existing resize handles (`role="separator"`, keyboard Arrow / Home / End, shift for 40px steps) are kept for both panels; the activity handle is removed.

Below 960px window width the layout stacks as today (`globals.css` responsive rules near `:3129` and `:3153`), with the right panel below the centre and the account row still last in the left panel.

## 2. Removed header; where its parts went

| Header element today | Target |
|---|---|
| Icon + split wordmark | Wordmark "Chirality" at the top of the left panel (§3), Plex Serif 500, 19px, `--brand-ink`, not a link. In the collapsed strip a single serif "C". |
| Kicker, title, subtitle | Removed. |
| Working-root chip | Folder selector in the composer (§4.1). |
| Runtime status chip | Removed. The activity strip's dot carries the state (§6); clicking the dot performs the existing reconnect check with the existing `aria-label`. |
| Gear / settings disclosure / theme control | Account popover and Settings view (§7, §8). No gear anywhere. |

## 3. Left panel — chats

Order, top to bottom: wordmark; search field; "New chat" with an umber plus; groups; account row (§7) pinned to the bottom. Chats from **every known folder** are listed (SR-20).

### 3.1 Groups

1. **Pinned** — chats the user pinned, most recently pinned first.
2. **Owner-made groups** — one section per group, alphabetical, with a count. Collapsible; collapse state persisted.
3. **Today / Yesterday / Earlier this week / Earlier** — by `updatedAt` from the session record.

A chat appears in exactly one of: Pinned, its group, or its date bucket, in that precedence.

### 3.2 Chat rows

Title, then time on the right (`HH:MM` today, weekday within seven days, `Mon D` otherwise; formatted from the record's ISO string, never from a clock, so render output is deterministic). Beneath, in the faint colour with a folder glyph, the chat's folder basename, or "No folder". The current chat is highlighted. The live chat has a dot before its title while a turn is running. Tooltip carries the session id.

**Title source.** The first operator message, trimmed to 60 characters at a word boundary, else the persona name, else the session id. Renamed titles override. Titles are local annotation stored with the workspace state (§12), not project truth.

### 3.3 Context menu (walkthrough step 10)

Right-click or the row's overflow button: Rename, Pin / Unpin, Move to › (list of groups + "New group…"), Archive, separator, Delete… (confirm dialog; deletes the local annotation and hides the chat; the runtime record is not deleted). Drag a row onto a group header to move it.

### 3.4 Search

Filters titles as you type; a second line of results searches message text through the existing session replay loader, debounced, limited to the twenty most recent sessions. Escape clears.

### 3.5 Collapsed strip

56px: serif "C", menu glyph (expand), search glyph, "new chat" glyph, avatar at the bottom.

## 4. Centre — dialogue

Unchanged behaviour from `ChatPanel`; layout and copy change.

- Transcript measure 620px, left-aligned in the column; padding 26px 40px. Below 560px centre width, padding 22px 26px and the mode select hides behind the persona select.
- Speaker labels: "You" and the persona display name (`Working Items`, `Help`, `Research`, `Change`, …; identifier in the tooltip).
- Tool calls render as a pill with a dot and a sentence: "Read DEL-09-01 status", "Searched the working root", "Wrote the review record". The function name and raw arguments are in the pill's tooltip and in the Activity view.
- **Reference chips** (SR-09): any token in assistant text that resolves to a path under the working root, a deliverable id (`DEL-nn-nn`), a receipt (`Receipt nnn`), or a ruling id renders as a chip with a document glyph. Hover shows "Open in side panel". Click opens the target in the right panel (document view for files and deliverable status files; the receipts ledger for receipts). Resolution is a pure function over the working-root tree and deliverable roster already loaded by the shell; no network call at render time.
- **Composer** (SR-22): one box holding only the message field, the attach control, and the filled round Send arrow at its right (the only filled control; the word "Send" is its `aria-label`). The field is one line at rest and grows to a maximum of six lines. Above it, inside the same box, an optional **quote row**: left-rule quote of the selected text (single line, ellipsised), source `file · lines a–b`, and a remove control. Attachments render as chips in the quote row. Box height at rest is about 48px; padding 8px, radius 12px, strong hairline border.
- **Context line** (SR-22, SR-23): directly under the box, left-aligned with it, 12.5px in the faint colour: the word "Working in" ("Start in" for a fresh chat; "Following" when a workflow steers the chat), then the **folder** selector, the agent (persona) selector, the mode selector, and the **rung** (§4.2), separated by middle dots. Selectors are small pills with a chevron; a fixed folder is a plain label with a folder glyph; a followed workflow is an umber label with a diamond glyph and the step count. The line wraps rather than hides at narrow widths (the centre column is `minmax(0, 1fr)` so the line can never widen the grid). It is part of the composer region for keyboard order and is announced as one group, "Chat context".

### 4.2 The specification tuple and the rung (SR-23, SR-24)

The context line shows the specification tuple in order: **folder**, **agent**, **permission** (the existing operator mode; ruled in, Q12), **delegation policy** (*No delegation*, *Ask before each brief*, *Approve each brief's writes*, *Bounded briefs*), and the **rung**. The rung is derived, never set on its own:

| Rung | Condition | Label |
|---|---|---|
| Plain chat | default agent, no deliberate policy | *Plain chat* |
| Specified chat | an Agent 1 role chosen and both policies set deliberately, by proposal or by hand | *Specified* (bold) |
| Governed workflow | a specified chat following a workflow file | *Following <workflow> · step n of m* (accent, diamond glyph) |

The rung item is a select on the first two rungs whose menu offers *Specify…* (opens the specification form with the tuple editable) and *Governed workflow…* (opens the New workflow form, §5.10). On the third rung it is a label; leaving the workflow is *Pause* in the Workflows view. A workflow cannot be swapped for another in the same chat. Delegation policy is a per-chat setting carried in the session record beside the operator mode; *No delegation* is the default on a plain chat.

### 4.3 Proposal card (SR-24)

The only inline object in the transcript besides messages and tool pills. Rendered as a bordered card at the transcript measure, immediately after the proposing agent's message.

- **Header:** "Proposal from <agent>" with the agent name in the accent colour; right, the transition ("plain chat → specified chat" or "specified chat → governed workflow").
- **Title:** one question, e.g. "Continue this as a Working Items chat?" or "Run this as the Section 8 preservation workflow?".
- **Tuple:** folder, agent, permission, delegation, and for a workflow the roadmap source; items that would change are in the accent colour.
- **Roadmap** (workflow proposals only): numbered steps in two columns, human gates marked "you decide"; the full protocol is one click away in the Workflows view.
- **Actions:** *Accept* (or *Accept and follow*; filled), *Adjust…*, *Not now*, and *Why this?* on the right, whose tooltip is the trigger sentence.
- **Accepted:** the card collapses to a single line with a green check, the resulting tuple, "you · <time>". **Declined:** a dashed line with a grey dash, "Not now. <agent> will not propose this again in this chat.", "you · <time>". Both stay in the transcript.
- **Behaviour:** Accept applies the tuple (and writes the workflow file under the write gate) and updates the context line; Adjust opens the corresponding form filled in; Not now records the decline and suppresses that trigger for the chat. One open card at a time; a new proposal replaces an unanswered one only if the trigger differs.
- **Events:** `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, `proposal.declined` as additive harness event types (ruled, Q13) in the session record with agent, trigger, and tuple; never in project files.
- **Accessibility:** `role="group"` labelled by the title; actions are buttons; the collapsed line is `role="status"`.

### 4.1 Folder selector (SR-21)

- **New chat, nothing sent.** The folder control, first in the context line, is a select showing the basename of the most recently used folder, or "Choose folder" when none is known. Its menu lists known folders (most recent first), "Choose folder…" (native directory picker, validated through `/api/working-root/validate`), and "No folder". The agent select sits beside it. Both are live. The empty transcript reads "Ask <agent> something about <folder>." with a second line "Pick a different folder or agent below before you start."
- **After the first message.** The context line's first word becomes "Working in" and the folder becomes a read-only label with a folder glyph and a tooltip "This chat works in <path>". Changing folder is not offered; "New chat" is. The agent select stays live (it already is today).
- **No folder.** Label reads "No folder"; Files view shows "Choose a folder to see its files"; Settings → This folder is absent; consent and permission lines do not render.
- The chat's folder is what the runtime session already records as its root; the label is derived from the session record, not from app state, so it survives restarts and reads correctly for chats started elsewhere.
- Permission requests stay inline above the composer as today.

## 5. Right panel — one view at a time

### 5.1 Header row

Left: either the **view tabs** (Files · Who is working · Activity) or, when a document or session is open, a **breadcrumb** (`‹ Files › DEL-09-01 › _STATUS.md`) whose first segment returns to the underlying view. Right: the four controls, always in the same order:

| Control | Glyph | Behaviour |
|---|---|---|
| Menu | ⋮ | View-specific list (§5.5). |
| Pop out | ↗ | Opens the current view in its own window (§5.7). Panel returns to Files. |
| Expand / Return | ⤢ | Toggle per §1. Pressed state shown. |
| Close | × | Document / Session: return to the underlying view. Files / Activity / Who is working / Settings: collapse the panel to its strip. |

### 5.2 Files (default)

The working-root tree. Directory rows toggle. File rows are buttons: click opens in-app when compatible (§5.4); otherwise shows the hand-off card in place of a viewer. The selected file is highlighted while open. Footer: "Choose folder" and the root basename. Keyboard: arrows move, Enter opens, Space toggles a directory.

### 5.3 Document

Rendered file under the breadcrumb. Markdown: headings, lists, tables, code, links (external links open outside; working-root links open in this panel). Title from the first `h1` or the file name; a meta line with the file name and modified time. Footer: **Ask about this** (filled) and **Attach to message**. Text selection shows a floating bar: Ask about this · Attach · Copy. Ask inserts the quote row into the composer with `path` and the 1-based line range covering the selection and focuses the input; Attach adds a `UiAttachment` for the file.

Expanded: measure 640px, 13.5px/1.6, larger headings.

### 5.4 What opens in-app

| Type | Rendering |
|---|---|
| `.md`, `.markdown` | Markdown as above |
| `.txt`, `.log`, `.csv` (as a table, first 500 rows), `.json` (folded tree), `.yaml`, `.toml` | Monospace, wrapped, line numbers on hover |
| `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp` | Image, fit to width, natural size on click |
| `.pdf` | Native `<iframe>` / Electron PDF viewer |
| `.docx`, `.xlsx`, `.pptx`, everything else | Hand-off card: name, size, modified; "Open in default app", "Reveal in Finder" |

Files above 2MB show the hand-off card with a "Load anyway" action for text types.

### 5.5 Menu contents

- Files: Refresh, Reveal root in Finder, Copy root path.
- Document: Reveal in Finder, Copy path, Open in default app, Attach to message, Reload; headings list as a table of contents.
- Activity: Clear view, Copy log.
- Who is working: Refresh.
- Session: Open parent chat, Copy summary, Copy session id.
- Settings: none.

### 5.6 Activity view (walkthrough step 8)

Sub-tabs Actions · Events · Children wrapping the existing `ToolStreamView`, `TranscriptStreamView`, `SubagentStreamView`. Each row: status dot, sentence (same text as the transcript pill), path or detail beneath in the faint colour, time on the right. A path opens the document; a child row opens its Session view. Footer: counts and elapsed time for the current or last turn.

### 5.7 Who is working (walkthrough step 9)

The recorded hierarchy for this working root: the live chat's persona first with its mode, then its children indented with status (`running`, `done`, `failed`, `not started`) and a one-line purpose; then earlier sessions today. Selecting a child opens the Session view. Selecting the live chat does nothing (it is the centre). Footer note as tooltip: "Recorded by the runtime. Status is what each session reported."

### 5.8 Session view (replay, SR-08)

Breadcrumb `‹ Who is working › <persona>`. A read-only banner: "Read-only. Started by <parent persona> in this chat at <time>. Finished in <duration>." Key-value block: Purpose, Allowed, Result. Then the transcript rendered by the existing replay lens components, including the provenance block. Footer: Open parent, Copy summary. Uses the existing loader, selection guard, and reconnect recovery unchanged; only the mount point moves. Selection is still disabled while a live turn runs (guard `liveTurnActive`).

### 5.10 Workflows view (SR-23)

Fourth tab in the right panel header, between Files and Who is working. Lists the folder's governed workflows from `.chirality/workflows/*.md`: title, Agent 1 role, delegation policy, roadmap position as *step n of m* with a thin umber progress bar, and the next human gate if any. Beneath, *Available to start*: templates the folder qualifies for (a template declares what it needs, such as an accepted decomposition or PDF sources). Footer: *New workflow…* and a count. No folder: "Choose a folder to see its workflows."

**Workflow open** (breadcrumb `‹ Workflows › <name>`): a key-value block (Agent, Folder, Policy with where briefs run, Roadmap source and acceptance date), then the roadmap as a numbered list with done, current, and pending states and *human gate* marked on the steps that have one. Footer: *Follow in this chat* (filled) and *Pause*. Following sets the chat's agent and policy from the file, injects the roadmap and current step into the system prompt, and switches the context line to *Following*. The agent is instructed to work the current step, stop at a gate, and say so; advancing past a gate is a human act recorded by the app against the content it accepted.

**Library and Bind** (Q10): beneath *Available to start*, a *From other folders* group lists workflows found in other known folders' `.chirality/workflows/`, and the bundled templates derived from Agent 1 protocols. *Bind to this folder* copies the file in with `folder` rewritten and `current` reset, after checking the template's prerequisites; the copy is an ordinary write under the gate.

**New workflow** (breadcrumb `‹ Workflows › New workflow`): Folder (fixed from the chat); Agent 1 role (required; the Type 1 roster); Delegation policy (required; *None*, *Ask before changes*, *Approve each write*, *Run bounded briefs*); Briefs run on (*Local model* when available, else the hosted account); Roadmap (*Draft from this chat*, or a template). The roadmap is editable before creation. *Create and follow* is disabled until role and policy are set. The file is written to `.chirality/workflows/<slug>.md` under the same write gate as any other write, and the chat follows it.

**The workflow file.** Front matter: `agent`, `folder` (the canonical root), `permission`, `policy`, `briefsRunOn`, `roadmapSource` (protocol or template identity **and hash**, so currency can be checked; Q15), `acceptedAt`; body: the roadmap as an ordered list with `[gate]` markers and an optional `current: n` line the app maintains. It is a derivative package in the project's own vocabulary: it steers the agent and cites accepted truth; it never holds status, approvals, or evidence, which stay in the deliverable records.

### 5.9 Pop-out window

Electron: a second `BrowserWindow` with the same `webPreferences`, preload, and origin, loading the same route with `?panel=<view>&target=<encoded path or session id>`. The renderer, when `panel` is present, renders only the right-panel view full-window with no header, left panel, centre, or strip. Ask and Attach in a popped-out document send their payload to the main window through the existing IPC sender policy (`electron/ipc-sender-policy.ts`), which must accept the second window's `webContents` as the same origin. Closing the window has no effect on the chat.

## 6. Activity strip (SR-07)

One 32px line, stone background, hairline above. The dot is a button carrying the existing runtime reconnect action and its `aria-label`; its colour follows the connection (ok, warn for reconnecting, faint for offline) and its tooltip carries the daemon detail the header chip showed. Idle: `● Idle · Last turn: 5 actions · 12 s`. Running: umber pulsing dot, the running action sentence in bold, counts (`n actions · n children · n s`), and "Details ▸" on the right. Details opens the Activity view in the right panel (and expands the panel if collapsed). The strip never resizes and never hosts content.

## 7. Account row and popover (SR-17)

### 7.1 Row

Pinned to the bottom of the left panel, 56px, hairline above. Avatar (30px circle, umber, initials), name, and beneath it two dots with labels: `OpenAI` and `Local model` (with the model's short name when running). Dot colours: `--ok` on, faint grey off, `--warn` needs attention (stale consent for the active chat's folder, daemon installed but stopped, key missing). Chevron at the right. Signed out: dashed grey avatar with `?`, the row reads "Sign in", both dots grey. Tooltip on the OpenAI dot: "Signed in · consent granted for <folder>" or "Signed in · no consent for <folder>" or "Not signed in". The account is app-wide (SR-19); only the consent clause names a folder.

### 7.2 Popover (walkthrough steps 13 and 15)

Opens upward, within the left panel width. Groups separated by hairlines:

1. **OpenAI** — signed in: name, "Signed in · consent granted|stale|revoked|not granted for <folder>", buttons Sign out, This folder… (opens Settings → This folder). Signed out: "Not signed in", "One account for the app. Consent and permissions are per folder.", button Sign in….
2. **Local model** — running: `oMLX · <model>`, "Running · n active turn(s)", switch on. Installed and stopped: switch off, "Stopped". Not installed: "Not set up", "Runs on this Mac, no account needed.", button Set up… (opens Settings → Local model).
3. Settings… (⌘,), Appearance › (Light / Dark / System radio submenu), Legacy window, About Chirality (shows `Opt-in Preview` and the version).

The switch calls the existing runtime `start` / `stop` actions. It never installs and never activates a model; both remain explicit acts in Settings.

## 8. Settings view (walkthrough step 14)

Opens in the right panel under breadcrumb `‹ Files › Settings`, default width 380. Five groups, in this order.

### 8.1 OpenAI account (app-wide, SR-19)
Status line ("signed in" / "not signed in"). Identity as the digest suffix or epoch the consent port provides, never an email. Sentence when signed out: "One account for the whole app. Each folder asks for its own consent." Buttons: Sign in… or Sign out.

### 8.1a This folder (per folder, SR-19)
Heading carries the active chat's folder basename; absent when the chat has no folder. Lines: Consent (granted · generation n / stale / revoked / not granted / needs sign-in, with the existing explanatory sentences shown beneath when stale or revoked); Command network as a three-way control whose short labels are Off / Ask / On and whose full labels (`No command network (default)`, `Ask per destination`, `Command network on (network_access = true)`) appear as the control's tooltip and in the line beneath the selected item; Role as Agent 0 / Agent 1 / Agent 2 with the verbatim `role not mechanically enforced` label where the port says so. Button: Revoke consent. Groups 8.1 and 8.1a are `AccountConsentSettings` split along the account-versus-root line; behaviour stays on the fake port until DEL-02-05-V3-03, and the port's per-root login semantics are not changed by the UI.

### 8.2 Local model
Status ("running" / "installed, stopped" / "not installed" / "runtime controls available only in Chirality Desktop"). Server switch; model select (exact oMLX ids, "(loaded)" suffix kept); residency line; buttons Install or Start / Stop, Activate (explicit, disabled when the selection is already managed), Refresh, Uninstall. Sentence kept verbatim from the current panel: "Activation never occurs automatically. A switch drains active local turns before unloading the managed model." This group is `RuntimeSettings` restyled.

### 8.3 Keys
Anthropic and oMLX rows with the stored / not stored state and the existing storage warnings; Change… opens the existing entry form inline. This group is `ApiKeySettings` restyled.

### 8.4 Appearance
Theme: Light / Dark / System, wired to `ThemeControl`'s setter.

Footer line: "Opt-in Preview · account is app-wide; consent and permissions are per folder."

## 9. What is removed from the active shell

Workbench and Pipeline surfaces and navigator groups; the Work projection tab; the resizable activity region; the entire header row (icon, wordmark position, kicker, title, subtitle, root chip, status chip, gear, settings disclosure); the navigator's "Compatibility" footer (moved to the popover as "Legacy window"); all `woven-eyebrow` elements; the Coordination panel's evidence-only disclaimer paragraph (becomes the Who is working tooltip).

## 10. Copy table

| Where | Now | Target |
|---|---|---|
| Header title | Woven Dialogue + subtitle | (none) |
| Dialogue toolbar | "Primary conversation" / "Dialogue" | (none) |
| Navigator header | "Workspace" / "Navigator" | (none; search field is the top) |
| Navigator groups | Dialogue / Workbench / Pipeline with notes | Pinned / groups / Today / Yesterday / Earlier |
| Right panel header | "Recorded coordination" / "Coordination" | Files · Who is working · Activity |
| Agents tab | Agents | Who is working |
| Work tab | Work | (removed) |
| Activity header | "Live runtime projection" / "Activity" | strip text per §6 |
| Focused surface | "Focused workspace surface", "Return to primary dialogue" | (removed) |
| Replay | "replay lens" | Session (breadcrumb), "Read-only." banner |
| Modes | Read-only / Plan (ask) / Gated-write / Autonomous | Read only / Ask before changes / Approve each write / Run on its own |
| Persona | WORKING_ITEMS etc. | Working Items etc.; identifier in tooltip |
| Runtime chip | daemon-oriented wording in the header | (chip removed) strip dot states Idle / Working / Reconnecting / Offline; existing detail in the dot's tooltip |
| Account | "Signed in for this root", "Sign-in and consent are per working root" | "Signed in"; "One account for the app. Consent and permissions are per folder." |
| Consent lines | "Consent granted for this root (root generation n)" | under "This folder": "granted · generation n" |
| Folder control | root chip in header | composer select "chirality-app-dev" → label after first message; "Choose folder"; "No folder" |
| Empty transcript | current empty-state copy | "Ask <persona> something about <root>." |
| No root | current | "Choose folder" in the composer select; "No folder" label |
| Rung | (none) | "Plain chat" · "With a specification…" · "Governed workflow…" · "Following <workflow> · step n of m" |
| Delegation policy | operator modes | "None" · "Ask before changes" · "Approve each write" · "Run bounded briefs" |
| Session notice | "Session selection is paused while the primary dialogue is running." | "Paused while a turn is running." |

Identifiers that must stay verbatim: `Opt-in Preview`; the three command-network labels; `role not mechanically enforced`; `instruction-asserted`; oMLX model ids. "For this root" is retired from account lines and survives only in consent and permission copy as "for <folder>" / "This folder".

## 11. Tokens (Stone)

Light: centre and header `#ffffff`; side `#f2f1ed`; side ink `#232220`; side soft `#5c5a55`; side faint `#8a8883`; side active `#e6e4de`; ink `#222120`; hairline `#e2e0da`; strong hairline `#cfccc4`; active `#efede8`; brand ink `#4a3423`; brand accent `#99552f`; call-to-action `#222120` on `#ffffff`; ok `#4f7f5c`; warn `#b5772e`; highlight `rgba(153,85,47,.16)`.

Dark: centre and header `#1e1e1c`; side `#161615`; side ink `#e6e5e0`; side soft `#a5a49d`; side faint `#77766f`; side active `#252523`; ink `#e8e7e2`; hairline `#2b2b29`; strong hairline `#3a3a37`; active `#2a2a27`; brand ink `#e8e7e2`; brand accent `#d08a5c`; call-to-action `#e8e7e2` on `#1a1a19`; ok `#8fbf9f`; warn `#d1a24a`; highlight `rgba(208,138,92,.22)`.

These map onto the existing `globals.css` token block (`:21` onward; dark at `:100` and `:140`): `--ground`, `--surface`, `--ink`, `--accent`, `--accent-soft`, `--cta`. Keep the existing contrast notes in that block; the Stone values were chosen to meet the same ratios (side faint on side ≥ 3.1:1 for small labels; ink on centre ≥ 12:1). Fonts unchanged: Plex Sans 13.5/1.5 body, Plex Serif for the wordmark and document titles only, Plex Mono only inside code and ids.

## 12. Persistence (additive v1 fields, no schema bump)

Add to `WovenWorkspaceState` with sanitize-and-fallback readers:

- `rightPanelView: 'files' | 'agents' | 'activity' | 'settings'` (default `files`)
- `rightPanelWidths: Partial<Record<'files'|'document'|'activity'|'session'|'settings', number>>`
- `rightPanelExpanded: boolean` and `preExpandState: { rightWidth: number; leftCollapsed: boolean } | null`
- `openDocumentPath: string | null` (project-scoped; cleared on root change like `focusedArtifact`)
- `chatTitles: Record<sessionId, string>` (cap 500, oldest evicted)
- `chatPins: sessionId[]`, `chatGroups: { id, name, sessionIds[] }[]`, `chatArchived: sessionId[]` (all project-scoped)
- `groupsCollapsed: string[]`
- `knownRoots: { path: string; lastUsedAt: string }[]` (cap 50, app-scoped, not project-scoped): the folders whose chats the left panel lists and the composer offers. `chirality.projectRoot` is read once as the seed and then left in place for the legacy shells.
- `activeChatRoot` is **not** persisted: it is derived from the active session record.
- `chatRung: Record<sessionId, { kind: 'plain' | 'spec' | 'workflow'; ref?: string; declined?: string[] }>` (cap 500): which rung each chat is on, which workflow file it references, and which proposal triggers have been declined in that chat. The workflow's own state lives in its file, not here.

Remove nothing; `sessionSurfaces` and `navigatorExpandedSurfaces` stay readable and become unused. `coordinationView` is read as before and mapped to `rightPanelView` on load when the new field is absent.

## 13. Keyboard

`⌘N` new chat · `⌘⇧O` open the folder menu in a new chat · `⌘K` focus search · `⌘,` Settings view · `⌘\` toggle left panel · `⌘⇧\` toggle right panel · `⌘E` expand / return · `Esc` closes popover, then floating selection bar, then returns the panel from Document/Session · existing separator keys unchanged.

## 14. Accessibility

Every control from the current shell keeps its role and label. New: view tabs are `role="tablist"`; breadcrumb first segment is a button; the four controls have `aria-label`s "Menu", "Pop out", "Expand" / "Return", "Close"; the account row is a `button` with `aria-haspopup="menu"`; the popover is `role="menu"`; the switch is `role="switch"` with `aria-checked`; status dots carry text alternatives; the strip is `role="status"` with `aria-live="polite"` for the running sentence only. Reduced motion: no pulsing dot, no width animation.

## 15. Non-goals

No inline artifact feed in the transcript (Concept 3's original feed). No multi-window chat. No editing files in the viewer. No provider, tool, or network change. No change to harness events, permission plane, or in-flight-turn survival.
