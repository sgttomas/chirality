# Shell Redesign 2026-09-04 — Handoff Package

**Status:** Owner-adopted design basis. Non-authoritative handoff package.
**Owner:** Ryan Tufts (ryan@chirality.ai). Decisions in `01_DECISIONS.md` are the owner's, recorded verbatim or near-verbatim from the 2026-09-04 design session.
**Prepared by:** Claude Fable 5.1 acting as HELP_HUMAN (Agent 0) in an advisory session. No product source was changed. No lifecycle, release, or Root act.
**Basis commit:** `origin/main` `307addfc2` (merge of PR #694, 2026-09-04). Every code path, line count, and test name in this package was read at that commit.

## What this package is

The Chirality desktop shell is being reshaped around one rule: **the dialogue is the interface with the agent; everything else is a side panel.** There is no header row; the folder a chat works in is chosen in the composer before the first message; sign-in is app-wide while consent and permissions stay per folder. The owner reviewed three rounds of mocks, ruled on each open question, and adopted a single design. This package records those rulings, describes what the code does today, specifies the target, sequences the work, and carries the logo assets the design depends on.

It exists so that another agent, in a new session with no memory of the design conversation, can seat the work in the loop and execute it without re-deriving intent.

## Authority boundary (read first)

- `plans/` is a historical archive under **F-APP-5** (`loop/WORKPLAN_2026-09-03_app_dev_loop.md`, "Standing constraints"). Nothing here is a work queue. Work is selected only from `execution/PKG-*/1_Working/DEL-*/_STATUS.md` `## Remaining`.
- This package therefore does two things only: (1) it is the **design basis** a deliverable's Remaining item may cite, and (2) `04_IMPLEMENTATION_PLAN.md` §7 offers **proposed** Remaining-item text for the owner to seat, amend, or decline. Seating is an owner act.
- The owner directed that this package be created in `plans/` (session instruction, 2026-09-04). That instruction is the reason these files exist here rather than in a deliverable folder.
- All standing fences apply unchanged: F-APP-1 (provider/network), F-APP-2 (release/distribution), F-APP-3 (domain engine), F-APP-4 (no issuance), F-APP-5 (single surface). Nothing in the design expands provider, network, tool, or release posture.

## Contents

| File | Purpose |
|---|---|
| `README.md` | This file. Index, boundary, inventory, reading order. |
| `01_DECISIONS.md` | The owner's design decisions, numbered SR-01 to SR-23, with rationale and consequences. SR-19 to SR-23 (app-wide sign-in, chats across folders, folder chosen per chat, message box with a context line, Workflows view and the ladder) were added after the owner's markup of the round-3 mock. |
| `02_CURRENT_STATE.md` | What the shell does today at the basis commit: routes, components, state, APIs, tests, CSS, brand assets. Includes the places where the code contradicts the adopted design. |
| `03_TARGET_SPEC.md` | The target shell, region by region: header, left panel, centre, right panel views, viewer controls, activity strip, account row, popover, settings, copy, tokens, keyboard, persistence, accessibility. |
| `04_IMPLEMENTATION_PLAN.md` | Seven tranches in dependency order with file-level scope, acceptance checks, tests, evidence, deliverable ownership, fence and trigger analysis, open questions, and proposed Remaining-item text. |
| `05_LOGO_AND_BRAND.md` | The adopted mark and wordmark, the asset inventory with hashes, how the assets were produced, where each is applied, and the cleanup of superseded files. |
| `mock/chirality-shell-mocks.html` | The interactive mock the owner approved. Self-contained HTML. Open it in a browser. Tabs: What changed, Shell, Walkthrough (21 click-through states), Activity/replay/expand, Logo, Notes. |
| `assets/` | Logo files. See `05_LOGO_AND_BRAND.md` for the inventory and hashes. |

The mock is also published as a private Claude artifact at `https://claude.ai/code/artifact/9bf2966f-1f4b-412f-95a3-86dcb58be3ed` (owner's account). The file in `mock/` is the copy of record; the artifact may be updated later and drift.

## Reading order for a new agent

1. `01_DECISIONS.md` end to end. Everything else follows from it.
2. Open `mock/chirality-shell-mocks.html`, Walkthrough tab, and step through all twenty-one states with the arrow keys. Then the Shell tab in both themes.
3. `02_CURRENT_STATE.md` with the listed source files open. Confirm the line numbers still hold; if `origin/main` has moved, re-read the files named in §9 first.
4. `03_TARGET_SPEC.md`.
5. `04_IMPLEMENTATION_PLAN.md`. Stop at §6 (open questions) and §7 (proposed Remaining items); those need the owner.
6. `05_LOGO_AND_BRAND.md` only when a tranche touches brand or icon files.

## Prior art this design builds on

- `plans/artifacts/DIALOGUE_CENTRED_CONCEPTS_2026-07-24_0121Z/` — the three dialogue-centred concepts. Concept 3, Woven Dialogue, is the one the code implements. Its thesis ("Dialogue is the stable centre") is the rule this package enforces; its inline-artifact feed is **not** adopted (see SR-03).
- `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_run_records/R6_WOVEN_REDESIGN_2026-07-24.md` — the tranche that produced the current Woven Dialogue shell, tokens, and persisted workspace state. The schema-version discipline it records still binds any new persisted field.
- `docs/ui/UI_POLISH_EXECUTION_PLAN.md` — the evidence-routing checklist for shell changes. Every tranche in `04_IMPLEMENTATION_PLAN.md` cites it.
- `docs/ISSUE_READINESS_PROFILES.md` §4 (D-APP-36) — the component render-test bar for UI/product deliverables.
- `docs/PRD.md` FR-006 — "calm, professional, dense-but-readable interface."

## Owner acts that remain

None of the following was done and none may be done by an agent on its own authority:

1. Seat the work: adopt, amend, or decline the proposed Remaining items in `04_IMPLEMENTATION_PLAN.md` §7 into the owning deliverables.
2. Rule on the open questions in `04_IMPLEMENTATION_PLAN.md` §6, including Q8 on when the shared-login contract amendment is raised with the Root loop (SR-19).
3. Merge each tranche's PR.
4. (Done 2026-09-04.) The superseded logo files were removed and the corporate `LOGO*` set written; see `05_LOGO_AND_BRAND.md` §3 and §6.

## Asset integrity

SHA-256 of every binary and the mock, recorded at package creation. Recompute with `shasum -a 256` from this folder.

```
7b46f2fc38804b41a35013e09b4cf445e943baa24fca60ac097c230584fc8c6b  assets/chirality-logo-lockup-400-dark.png
14e22c3b6b8bdc45311d04d47562b3e7d5aaa37bf879357223bd64158233279c  assets/chirality-logo-lockup-400-dark.svg
c687946e0bb2665e954fb63429ecbe43f4afdbccf45a07dd3ba51c1c39c17afb  assets/chirality-logo-lockup-400.png
bebdf63bf55c8ab83ba85abcc2d0db090cde2ae498cf1fe4156147b1ace13ef3  assets/chirality-logo-lockup-400.svg
a3495dfa7ad1a8bbba9b7026d3e68964013b5cfb3e4364dee713285fd4a86616  assets/painted-field-1024.png
b0fc9c26afa26ddafdec575b91a4e49fb58e4db73dd85cfaea14e41813114126  assets/painted-field-16.png
f38e405626c150ed88cfe4ef878930659a8d8247f323b51d803eb7130efaffef  assets/painted-field-256.png
dfe92ed3307e3394d402fceb6a6c939e824b630d8398d9ae2246cd3357060c2b  assets/painted-field-32.png
4215f30a9088a9d712df52e3556f72d27ef0bafac6c6764e525f343812f339e3  assets/painted-field-64.png
1f932536afd216d9f3fcd11feac3eb95595101cd69a945dcd9faf0b68f362d8b  assets/painted-field-square-1024.png
adb22d8f286cbaf87a8da79dbbead589463a2c08bc71c26d9212ff863733c56a  assets/painted-field.icns
fdce823b831ab0d2043aa1597abea36b9a6276d36e4ab84d5ac21d26f73486b0  mock/chirality-shell-mocks.html
```
