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

## SR-23 — Workbench returns as the Workflows view; the ladder of plain chat, specification, governed workflow

Owner, 2026-09-04, on what Workbench should be: "That's where the governed workflows are. Then in chat mode there's just options to do things in a working folder, with a particular agent, following any particular delegating policy. And one should be able to use chat mode to create governed workflows (the structure of which is tied to a particular Agent 1 type, must have a working directory selected, and will declare its delegation policy (including 'none'))." The owner agreed with two refinements: keep the centre invariant (Workflows is a right-panel view, not a surface), and offer a rung below a workflow (a specification applied to a plain chat).

**Consequence.**
- **The ladder.** Every chat sits on one of three rungs, derived from how much of the specification tuple is declared (see SR-24 for the tuple as the owner defined it): *Plain chat* (nothing declared); *Specified chat* (an Agent 1 role and the policies chosen deliberately, no roadmap); *Governed workflow* (the specified chat plus a roadmap, saved as a file in the folder). The rung shows as the last item of the context line and offers the promotions. Most work stays on the first rung. *(Superseded wording from 2026-09-04 morning defined the middle rung as a skill applied to a chat; the owner corrected that, Q11.)*
- **A governed workflow** is a file in the folder (`.chirality/workflows/<name>.md`) declaring an Agent 1 role, the folder, a delegation policy (including *None*), where briefs run, and a roadmap of steps with human gates marked. It steers the chat by context injection; it is never the record. The app refuses to create one with any of the three declarations missing.
- **Workflows view** in the right panel lists the folder's workflows with role, policy, roadmap position, and next human gate, plus templates the folder qualifies for. Opening one shows the roadmap; *Follow in this chat* sets the chat's agent and policy and injects the roadmap. The context line then reads *Following <workflow> · step n of m* so the current step is always visible.
- **Created from chat** through the ladder's *Governed workflow…* entry, which opens the New workflow form in the right panel: folder fixed from the chat; role and policy required; roadmap drafted from the conversation or taken from a template.
- SR-06 stands: the retired Workbench code is not revived; the Workflows view is new and small. The owner directed that this work falls into the same redesign tranches rather than a later revision.

## SR-24 — The specification tuple; the ladder is prompted as well as chosen; Q10 and Q11 ruled

**Q11 ruled — what a specification is.** Owner: "'Specification' I meant the working directory, the agent persona, roadmap, and the delegation policy (and if there's anything else at that 'level of specification'). I don't want to get into the nitty gritty. There's other ways to do that kind of thing, and later versions of this app may include a 'builder' variant where you can define new agents and skills and such… For now, this is the minimum set (allowing for anything else you bring forward and I agree to include)."

The tuple is therefore **five items: folder, agent, permission mode, delegation policy, roadmap** (roadmap only for a governed workflow). The permission mode (read only, ask before changes, approve each write, run bounded briefs) was brought forward under the owner's "anything else you bring forward and I agree to include" and **ruled in on 2026-09-04 (Q12)**: in the service model the workflow file must fully determine how the client's people run it. *Where briefs run* (local or hosted) stays an app setting. Skills and agent definitions are not part of the specification; they belong to a later "builder" variant.

**Q10 ruled — where a workflow lives.** Owner: "yes the workflow lives with the working directory (you can do that how you see fit) and a new working directory should also be able to pick from existing workflows and bind it to that directory too." Consequence: `.chirality/workflows/<slug>.md` inside the folder, git-tracked if the folder is; and a **library**: the Workflows view offers workflows from other known folders and the templates derived from Agent 1 protocols, and *Bind to this folder* copies one in with the folder rewritten, the position reset, and the template's prerequisites checked.

**The ladder is prompted.** Owner: "The ladder is still an interesting concept, where those can be applied by 'prompting' the user rather than relying on them to do it, or to do it consistently each time. But yes, it should be possible to initiate such a state from the chat with selecting the tuple and roadmap directly too."

**Consequence.**
- **The proposal card** is the one inline object the transcript carries. When the agent judges the work has earned the next rung it posts a card: who proposed it, which rung to which, the tuple filled in with the changed items in the accent colour, the roadmap when a workflow is proposed, and three actions: **Accept**, **Adjust…**, **Not now**, plus *Why this?* naming the trigger in one sentence. Accepting is the human act; the app performs the write. Nothing is promoted silently.
- **Who proposes which rung.** HELP_HUMAN (Agent 0, the default) proposes rung 1 → 2 when a plain chat's work matches an Agent 1 protocol. The Agent 1 proposes rung 2 → 3 when the request matches a procedure in its own protocol. Neither needs write scope: proposing is an alignment act and the app writes on acceptance.
- **Triggers are few and named** in the instruction packages, not heuristics in code: the human asks for something that matches an Agent 1 protocol; the same kind of request recurs in a chat; the folder gains a decomposition so templates become available; a bound workflow's prerequisites become satisfied.
- **Anti-nag is a rule.** One proposal per chat per trigger. *Not now* collapses the card to a dashed record line, is remembered for the chat, and is recorded so an audit can see the offer was made and declined.
- **Direct selection is the same card.** *Specify…* and *Governed workflow…* from the context line open the same form the proposal would have filled in, empty. *Adjust…* on a proposal opens it filled in. One mechanism, two entry points.
- **Records.** Accepted and declined proposals stay in the transcript as collapsed lines with who and when, and are written to the session record as **additive harness event types** (`proposal.offered/accepted/adjusted/declined`; **ruled 2026-09-04, Q13**), so the offer and the decline are in the record an audit and the follow-up engagement can read; the resulting rung is local chat state (`chatRung`); the workflow file is the only project-side artifact and it steers, never records.
- Mock: walkthrough steps 21 to 25.

## SR-25 — This is the product, and it is part of a service

Owner, 2026-09-04: "This is the product. This last bit of work we did to define the 'governed workflows' and what 'specifications' are and how the 'ladder' works. This is the product. And it's part of a professional consulting service that leaves behind the workflows and agents and skills for the organization to use."

**Consequence for the design.** The app is the runtime for a method; the prompted ladder is what keeps the method applying itself after the consultant has left; the Workflows view is the catalogue of what an engagement left behind and should say where each workflow came from and which protocol version it instantiates. The mock's Product tab is the one-page statement. Three decisions the service model forces are opened as Q14 to Q16 in `04_IMPLEMENTATION_PLAN.md` §6: where client-owned agents and skills live relative to the protected bundled instruction root; how a leave-behind's currency against the method is detected; and how several people in one shared folder follow the same workflow.

## SR-26 — Plain vocabulary on the surface; the doctrine keeps its terms underneath

Owner, 2026-09-04: "You've used some very specific terminology like 'Section 8' and several others that appear to be idiosyncratic terms that you can probably state as a generic term and be understood better… instead of 'Help' (even though I named it HELP_HUMAN) I think we should use 'Assistant'… The concepts are there, but we need to make this a coherent and familiar surface for people to interact with. This is about Knowledge Work as such. That doesn't mean use jargon, it means it's generic as can possibly be without losing specificity." The owner adopted the table below, keeping "Proposal from Assistant" since the events are named `proposal.*`.

| Doctrine / earlier mock | Surface | Note |
|---|---|---|
| HELP_HUMAN, "Help" | **Assistant** | Default agent display name |
| Plain chat | **Chat** | The first rung needs no name |
| Specified chat | (no label) | The chosen agent and permissions show it; menu item **Choose agent and permissions…** |
| Governed workflow | **Workflow** | "Governed" stays in the doctrine; menu item **Start a workflow…** |
| Roadmap | **Plan** | "step n of m" stays |
| Bounded briefs, child sessions, children | **Delegated tasks**, **tasks** | Activity sub-tab "Tasks" |
| Delegation policy | **Delegation** | No delegation · Ask before delegating · Delegate, approve changes · Delegate freely |
| Permission mode | **Permissions** | Read only · Ask before changes · Approve each change · Make changes freely |
| Proposal from Assistant | **Proposal from Assistant** | Kept; events are `proposal.*` |
| Accept and follow / Follow in this chat / Create and follow | **Start workflow** / **Continue in this chat** / **Create and start** | |
| Bind to this folder | **Use in this folder** | |
| human gate / you decide | **your decision** | |
| Agent 1 role | **Role** | Roster shows Assistant, then roles by what they do (Reviewer, Analyst, Writer, Reconciler, …); the doctrine name is the tooltip |
| Agent 0 / 1 / 2 session role | **Supervisor / Manager / Specialist** | The K-ROLE labels stay verbatim in the tooltip |
| Command network | **Network** | The verbatim contract label stays in the tooltip |
| Working root | **folder** | already ruled |
| Section 8, DEL-nn-nn, receipts, PR numbers, rulings | generic knowledge-work example | The mock now shows a design review in a folder called Northgate expansion |

Kept as they are: **Consent** (it does legal work and "permission" is taken) and **Opt-in Preview** (required verbatim by the contract). Example content in the mock is a document review: a report whose findings are checked against their sources, a Reviewer role, and a seven-step plan with one decision that is the human's.

**How proposals are made in the harness (recorded with SR-24, ruled direction).** Not hooks. Agent 0 and the Agent 1 roles get one registered deterministic tool, `propose`, that takes the tuple and, for a workflow, a plan reference from the role's own procedures; the tool validates against the roster, the folder, and the policy values, refuses a trigger already declined in the chat, and emits `proposal.offered`. The card is the UI's rendering of that event, as permission requests already are; Accept, Adjust, and Not now are events back, applied by the app. Triggers stay in instruction text; the tool call is the only mechanical part, and if the model never calls it nothing happens. PreToolUse may double-check the once-per-chat rule; the tool handler is the primary enforcement.

## Decisions explicitly deferred to the owner

Listed in `04_IMPLEMENTATION_PLAN.md` §6. None of them blocks the first two tranches.
