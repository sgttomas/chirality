# 01 — Owner Design Decisions

**Source:** Design session with the owner, 2026-09-04, over three rounds of mocks. Quotations are the owner's words from that session. Everything else is the recorded consequence.
**Numbering:** SR-nn (Shell Redesign). These are design decisions, not lifecycle rulings. Where a decision needs a lifecycle or register act, `04_IMPLEMENTATION_PLAN.md` says so.

---

## SR-01 — The dialogue is the interface. Perfect it; do not add interfaces.

> "This is what the 'woven dialogue' concept is, the documents are visible in the right side panel while the center dialogue area always remains. That dialogue panel is the interface with the agent. We need to perfect that interface, not add new ones."

**Consequence.** No new top-level surface, no header surface tabs, no Documents mode. The centre dialogue is never hidden, unmounted, or replaced. Anything that today takes the centre from the dialogue (focused surfaces, replay lens) moves to the right panel. This decision supersedes the "case for Documents" mock from round 2, which the owner rejected.

## SR-02 — Three panels with a rank

> "The right panel is the tertiary screen, with the center dialogue being primary and the left panel navigator as the secondary. Everything else except the activity monitor goes into the right panel, with ways to select what appears."

**Consequence.** Primary: centre dialogue. Secondary: left panel, chat history and navigation. Tertiary: right panel, one view at a time from a switcher. The activity monitor is the one thing outside the three panels, as a strip at the bottom.

## SR-03 — Left panel is the history and navigator for chat

> "Think of the left panel as the history and navigator for chat. This is where you can organize the chats."

**Consequence.** The left panel holds search, New chat, pinned chats, owner-made groups, and date groups. It does **not** hold the file tree (moved to the right, SR-04) or mode groups for retired surfaces (SR-06). Organising means rename, pin, move to group, archive, delete. Titles come from the first message and are editable. All of it is local annotation, not project truth.

## SR-04 — Files live in the right panel and open in-app

> "'Files' should be part of the filetree viewer in the right panel."
> "The File Tree should allow documents to be clicked on and then viewed in-app, where compatible."

**Consequence.** Files is the default right-panel view. Clicking a compatible file opens it in the same panel under a breadcrumb. Incompatible files show a hand-off card ("Open in default app", "Reveal in Finder"), never a broken page. What "compatible" means is fixed in `03_TARGET_SPEC.md` §5.4.

## SR-05 — The document viewer drags and expands

> "The document viewer should be able to drag and expand, in addition to an 'expand' toggle."

The owner supplied an image of the four controls: overflow menu, pop out, expand, close. **Consequence.** The divider between centre and right panel drags between a minimum and an expand width. Expand jumps to a reading width and collapses the left panel to a strip; the centre keeps its composer. Pop out opens the same view in its own window. Close returns the panel to the view the document came from. Exact widths in `03_TARGET_SPEC.md` §5.6.

## SR-06 — Workbench and Pipeline are retired; the code stays

> "Yes, retire 'Workbench' and 'Pipeline' (keep the code, maybe it becomes useful later, but remove it from the active part of this app)."

**Consequence.** Unmount them from the woven route: remove the focused-surface branch in the viewport, the navigator mode groups, and the `WovenSurface` values that name them. Their component trees, routes (`/workbench`, `/pipeline`), and test suites stay in the repository. The reading half of Workbench (deliverable roster and document renderer) is reused inside the right panel, not as a surface.

## SR-07 — The activity monitor stays a strip; no fourth panel

Owner asked: "Does the bottom activity shelf expand, or is it just that strip …? Can clicking on it expand the right panel, or do we want to add a fourth panel?" The recommendation, adopted with the design: **one line at the bottom** that says what is happening now; "Details" switches the right panel to the Activity view. No fourth panel. The strip never takes height from the dialogue.

## SR-08 — Replay: your own chats are not replays; child sessions are

Owner asked: "I don't know what 'Replay' view is? Explain more and why it should reside in the centre panel." The explanation and placement, adopted with the design:

- The runtime records every session, including child sessions an agent starts when it delegates. The current shell can load any recorded session as a read-only transcript ("replay lens") and hides the primary dialogue to show it.
- **Your own past chats** open in the centre as that chat, ready to continue. That is not a replay.
- **Child sessions** (an agent's own run, which you cannot type into) are replays. They open in the right panel, read-only, with the parent link, and can be widened, expanded, or popped out like a document.
- Replay never takes the centre.

## SR-09 — Weave in both directions

> "I like your idea about how to 'Weave the two directions'. Show me what you mean in the mock."

**Consequence.** Dialogue → document: paths and deliverable identifiers in assistant text and in activity rows render as reference chips that open the document in the right panel. Document → dialogue: a text selection in the viewer offers Ask, Attach, Copy; Ask quotes the passage into the composer with file and line range attached; Attach adds the whole file. This is the feature that makes "woven" true rather than a slogan.

## SR-10 — Stone is the treatment; Linen and Umber navigator are dropped

> "Just use the 'Stone' variant and omit the 'Linen' and 'Umber navigator'."

**Consequence.** Neutral stone side panels, white centre (light) or the lightest dark surface (dark), hairlines instead of borders, a single filled call-to-action. Tokens in `03_TARGET_SPEC.md` §11.

## SR-11 — No app icon in the UI; the name alone

> "I think the Chirality app icon needs to go from the UI. It should just have the 'Chirality' name."

**Consequence.** The wordmark "Chirality" is the only brand element in the UI, one face and one colour (SR-15). The icon lives in the Dock, the DMG, and the corporate lockup.

## SR-12 — No header row (supersedes the round-2 compact header)

> "Let's free up the top row by removing the 'Chirality' the current working directory, the status, and the settings wheel."

The owner marked up the round-3 mock: the wordmark moves to the top of the left panel; the working-root chip moves into the composer beside the agent picker; the status chip is deleted because the activity strip already shows it; the gear is deleted because Settings is in the account popover. **Consequence.** The 44px header is removed entirely and the three panels start at the top of the window. The runtime reconnect action that lived in the status chip moves to the activity strip's dot (click to check the connection). See SR-21 for the folder picker.

## SR-13 — White centre, colour on the sides, hairlines not borders

> "the center panel where all the action happens should be white with the color on the side panels. The hairlines instead of borders."

## SR-14 — The message block was too large; single-row composer

> "I don't understand why so much space is allocated to the message block."

**Consequence (as amended by SR-22).** The composer box holds only the message, attach, and send; it is one line until you type more. Quoted context (SR-09) appears as a chip row above the input inside the same box. The folder, agent, and mode selectors are not in the box; they form the context line beneath it.

## SR-15 — The wordmark is one face, one colour

> "'Chirality' should all be one font and color, not split into 'Chira' and 'lity'."

**Consequence.** Plex Serif, one weight, one colour: the dark umber of the mark's squares on light grounds, cream on dark. The current `Chira<em>lity</em>` markup and the italic accent go.

## SR-16 — The logo is the chalk-on-brick drawing, plain and unbordered

> "we will stick with the 'Chalk, plain' and I want to use that in the app itself, not just as the icon. I'm also going to adopt that as the corporate logo (updated from the current `LOGO.jpg`)."

**Consequence.** The composed "field" mark (six chalk squares on a brick ground, no border, no dark variant) is the macOS app icon, the in-app mark wherever a mark is needed outside the header, and the corporate logo. The vector six-tile mark, the bordered variant, the greyscale variant, and the dark-ground variant are all rejected. Details in `05_LOGO_AND_BRAND.md`.

## SR-17 — Account row pinned to the bottom of the left panel

> "We're also going to need a user portal and a way to change user settings and sign in or sign out of the OpenAI OAuth, and to set up / toggle the local model server (when available). This should be located in the left panel pinned to the bottom."

**Consequence.** A persistent row at the bottom of the left panel: avatar, name, and two status dots (OpenAI, Local model). Clicking opens a popover: OpenAI sign in or out and consent for this root; the local model switch; Settings; Appearance; Legacy window; About. Settings opens in the right panel as a view with four groups: OpenAI account, Local model, Keys, Appearance. The signed-out state shows a dashed avatar and "Sign in". All account and consent language keeps the phrase **"for this root"** because sign-in and consent are per working root (`docs/CONTRACT.md` K-CONSENT-1).

## SR-18 — Written for knowledge workers who are not coders

> "This app is targeted at knowledge workers who aren't coders."
> "the amount of 'subtitles' and bits of text that are superfluous and distracting and silly sounding is embarrassing."

**Consequence.** No eyebrows, no route subtitles, no disclaimers in the body copy (they become tooltips), no identifiers with underscores in labels, no monospace outside the ids people already use in their documents. Speaker labels are "You" and the persona's display name. Tool calls read as sentences. Modes read as intentions. The copy table is `03_TARGET_SPEC.md` §10.

## SR-19 — Sign-in is app-wide; consent and permissions are per folder

> "the sign-in should be for the app as a whole, not for the current working directory. However, the specific chat and its permissions should be limited to the current working directory."

**Consequence.** Two layers, and the UI says which is which:

- **Account, app-wide.** One OpenAI identity for the app, shown once in the account row and popover and in Settings → OpenAI account. No "for this root" on it.
- **Consent and permissions, per folder.** Consent, command network posture, role, and the operator mode remain bound to the chat's folder, shown under Settings → This folder and on the popover's OpenAI line as "consent granted for <folder>".

**Contract note.** This keeps `docs/CONTRACT.md` K-CONSENT-1 intact: consent still carries the account digest and the canonical root. What changes is the root-private login home that K-KEY-1 and the current `AccountConsentSettings` copy describe ("Sign-in and consent are per working root"). An app-wide sign-in shares one login across roots. That is Root-owned (DEP-02-05-008/009; Root DEL-02-09) and is the contract DEL-02-05-V3-03 is waiting on. The direction is recorded here as the owner's; the amendment itself is routed through the Root loop and is not an App-loop act. Until it lands, the UI presents the account once while the fake port keeps its per-root semantics underneath, and the consent fixtures' per-root copy is rewritten only on the folder lines. Confirmed by the owner 2026-09-04: "I confirm your sign-in reading. Document it as you've indicated."

## SR-20 — The chat list spans every folder

Owner, adopting the recommendation: "list all folders with the name shown, since the point of moving the picker into the composer is that folders are chosen per conversation, not per session of the app." **Consequence.** The left panel lists chats from every known folder with the folder's basename under each title. No folder filter in the first release; search covers all of them.

## SR-21 — The folder is chosen per chat, in the composer, before the first message

> "The selection of the working directory (if any) should be alongside the agent picker and selectable at the start of a chat before the user has entered anything."

**Consequence.** A new chat shows two selectors in the composer: Folder and Agent. Both are live until the first message is sent. After that the folder is a read-only label on the composer and changing it means starting a new chat. "(if any)": a chat may start with no folder, in which case the label reads "No folder" and file, consent, and permission surfaces show their empty states. The app-level notion of "the working root" becomes "the folder of the active chat".

---

## SR-22 — The message on its own line; folder, agent, and permission level as a context line beneath the box

> "The 'Message' should be a line of it's own, with those other three aspects below it. You can use the empty space below that message bar that currently does nothing to put those things I told you to move. Or propose something better and show me that instead."

Two options were mocked: A, the three selectors as a second row inside the message box; B, the box holding only the message with the three choices under it as a sentence. The owner ruled: "I want Option B." **Consequence.** The message box contains the message field, the attach control, and the filled round Send arrow, on one line that grows as you type. Directly under the box, in the space that was empty, a **context line** reads "Working in <folder> · <agent> · <permission level>", each part a selector; in a fresh chat it reads "Start in …" and the folder and agent are live. After the first message the folder becomes a fixed label in the same line. Option A is removed from the mock and is not to be revived.

## Decisions explicitly deferred to the owner

Listed in `04_IMPLEMENTATION_PLAN.md` §6. None of them blocks the first two tranches.
