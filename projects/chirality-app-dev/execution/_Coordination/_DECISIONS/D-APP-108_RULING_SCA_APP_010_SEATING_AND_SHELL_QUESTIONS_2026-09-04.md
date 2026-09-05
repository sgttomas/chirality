# D-APP-108 — SCA-APP-010 shell-redesign seating and open-question rulings

Status: RULED (owner direction in chat and option selections 2026-09-04)

Owner: Ryan Tufts

Date: 2026-09-04

## Conversation provenance

After PR #711 merged and `_ScopeChange/_LATEST.md` pointed at SCA-APP-010,
HELP_HUMAN explained the seating list for the thirteen SCA-APP-010 carriers
(the proposal built from `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md`
§7 minus the scope the SCA carries in decomposition rows) and the items outside
the thirteen. The owner directed, verbatim:

> adopt the list as presented.  Items outside the thirteen carriers get seated in the same pass.  You may run the WORKING_ITEMS alignment in the same PR.
>
> Present the questions to me here for rulings before you set out. Give me clickable options and your recommendations if any.

HELP_HUMAN then presented the eleven unruled questions of the plan's §6 as
clickable options with labelled recommendations. The owner's selections and
free-text answers are transcribed below exactly as returned. Where an option
was selected, the option's presented description is reproduced because the
owner ruled on the label together with its description.

These quotations are from the current conversation supplied to this run.

## Seating ruling

1. The seating list presented on 2026-09-04 is adopted as presented: every row
   is an owner-adopted `Remaining` item for its named carrier, with the gate
   the list stated. IDs continue each carrier's existing V3 numbering; where a
   presented ID collided with an item already seated on `main`, the next free
   number is used and the collision is recorded in the run `MAPPING.md`.
2. The items outside the thirteen carriers (DEL-02-03-V3-01, DEL-02-03-V3-02,
   the DEL-05-04 Session view, the DEL-09-04 `.icns` item, and the DEL-01-03
   copy-table note) are seated in the same pass.
3. WORKING_ITEMS alignment of the thirteen carriers (SCA-APP-010
   `FUTURE_WRITE_SET.csv` WI-001 to WI-065) runs in the same PR as the seating.
4. Merge of that PR confers selectability only. No implementation, lifecycle,
   dependency-acceptance, product, signing, release, or Root act is inferred.

## Question rulings (plan §6 numbering)

| Q | Question as presented | Owner's answer (verbatim) | Ruling as applied |
|---|---|---|---|
| Q3 | Should the retired `/workbench` and `/pipeline` routes stay reachable by URL, or return 404 while the code stays? | "Reachable, unlisted (Recommended)" — description: "Matches the applied SOW-001 text exactly: routes stay by URL, unmounted from the active shell. No decomposition change; smallest T1." | Retired routes stay reachable by URL and unlisted; no 404; SOW-001 as applied stands. |
| Q9 | What does the folder menu offer when starting a new chat? | "Finder integration will make it fell Mac-native and provide the best user experience." Reading check, selected: "Full Mac-native set (Recommended)" — description: "Native folder picker; known folders registered as macOS recent documents (Dock and Open Recent menus); Reveal in Finder on each chat; drop a folder from Finder onto the composer. All supported Electron APIs." | Full Mac-native set as described; no attempt to read Finder's own Recents list. |
| Q4 | Is a 2 MB in-app file cap acceptable, and do PDFs open in-app or hand off to the OS? Re-asked after the owner's question as Q4a "how do PDF, DOCX, XLSX, and PPTX open from the file tree?" and Q4b "what size cap applies to text, markdown, code, and CSV shown inside the panel? PDF and Quick Look previews are uncapped either way." | "We need PDF, DOCX, XLSX support and native viewer via the renderer.  But what filesize limitation do we have?  These are all local operations, are they not?  No cloud storage needed.  I don't understand this fully perhaps." After HELP_HUMAN's explanation: Q4a selected "PDF in-panel; Office files via Quick Look (Recommended)" — description: "Chromium renders PDF inside the right panel. DOCX, XLSX, PPTX open in a native Quick Look panel with an Open in default app action. Zero new dependencies; Apple's own rendering."; Q4b selected "10 MB in-panel text cap (Recommended)" — description: "Covers any source file, spec, or normal log. Larger files show size and an Open in default app action instead of freezing the panel." | PDF in-panel through the renderer's built-in viewer; DOCX, XLSX, and PPTX through macOS Quick Look with Open in default app; 10 MB cap on the in-panel text path only; PDF and Quick Look previews uncapped. |
| Q2 | How does a quoted reference travel on the wire? | "Attachment with clientType quote (Recommended)" — description: "No harness change and no Section 8 revision. Stays inside DEL-02-03's write locus and raises nothing toward Root DEL-02-10." | Quote is an attachment with `clientType: 'quote'`; `lib/harness/**` untouched. |
| Q1 | What does deleting a chat do? | "Local hide only (Recommended)" — description: "Runtime session record untouched and recoverable. Avoids the fresh-ruling stop in LOOP_INIT §6 on changing the project-truth model for sessions." | Delete hides locally; the runtime session record is untouched and recoverable. |
| Q6 | May chat titles be derived from the first message, which can contain a path or a secret-shaped string? | "Derive with redaction (Recommended)" — description: "First message text passes through the existing redaction helper; the title stays editable. Best navigator with the secret risk covered by code already in the tree." | Titles derived from the first message pass the existing redaction helper and stay editable. |
| Q7 | Does the account row show the OpenAI status dot before DEL-02-05-V3-03 lands, or only the local model dot? | "Local model only, period.  Knowing the local server is running is useful.  Knowing OpenAI is operating is assumed once you log in with OAuth.  And API status is not wanted either.  Just local model server status." | The account row shows only the local model server status; no OpenAI status indicator and no API status indicator, now or after DEL-02-05-V3-03. |
| Q8 | Raise the shared-login amendment toward Root now, or after T6 lands on the fake port? | "Raise now via the SCA-APP-010 Root notice (Recommended)" — description: "The drafted notice already names Root DEL-02-09's login home as an OI-008 dependency. Choosing this also authorizes routing that notice into execution/_Coordination/ in this pass. Root's cadence is the slow path; starting it now is principle (b), discharging a gate early." | The SCA-APP-010 Root notice is routed in this pass (N-001); DEL-02-05-V3-05 ships no separate notice. |
| Q5 | Pop-out panel window in the first release, or defer the window work and ship only the icon change? | "Defer the window, ship the icon (Recommended)" — description: "Keeps T7 to renderer assets and packaging integrity. A pop-out adds a second BrowserWindow, IPC, and panel state sync, better taken after the right-panel views settle." | The pop-out window is deferred and not seated; the icon change is seated (DEL-02-01-V3-04, DEL-09-04-V3-02). |
| Q15 | Should the app report when a workflow file's `roadmapSource` hash is behind the current protocol or template? | "Report it as a line in the Workflows view (Recommended)" — description: "Read-only comparison of the pinned hash against the current template, mirroring the repo's corpus-drift check. Small, and it is what makes a leave-behind trustworthy." | A read-only currency line in the Workflows view. |
| Q16 | Several people share one folder; workflow position and proposal records are per folder while sessions are per person. What is the v1 rule? | "Gate-only advance, attributed (Recommended)" — description: "Position advances only at human gates and the file records who advanced it. Concurrent editing is documented as unsupported until the thesis §9.4.6 work. Matches the applied SOW-081 note." | Position advances only at human gates; the file records who advanced it; concurrent editing documented as unsupported. |

Q10 to Q14 were ruled earlier on 2026-09-04 (SR-24 and the SCA-APP-010
G2-CONFIRM ruling on Q14) and are not re-ruled here.

## Effect

- The twenty items and two record-only history lines listed in the run
  `MAPPING.md` are seated as written in each carrier's `_STATUS.md`; ruled
  questions are cited by item and their gate clauses are dropped.
- The thirteen SCA-APP-010 carriers are aligned to the applied decomposition
  (Scope of Work re-pin and SCA-APP-010 Gate-5 Current Contract section,
  `_CONTEXT.md`, `_REFERENCES.md`, history and memory lines).
- The Root notice is routed to `execution/_Coordination/` (repo root).
- Dependency extraction (DEP-001 to DEP-026), the named closure audit,
  RECONCILIATION, and AUDIT_DECOMP reruns follow owner acceptance of this
  alignment, in the order SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` sets.

## What this ruling does not do

It authorizes no implementation tranche, lifecycle transition, Checking
Approval SHA change, dependency acceptance, product byte, signing,
notarization, distribution, release-readiness claim, or Root register,
contract, decomposition, or pointer write. Selection of any seated item is a
later act under `loop/LOOP_INIT.md`.

## Attribution

Transcribed and applied by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) in
an untyped Claude Code session acting as HELP_HUMAN (Agent 0) and, for the
carrier writes, as WORKING_ITEMS' applicator under the owner's authorization;
role not mechanically enforced. The "Ruling as applied" column is the agent's
reading of the owner's words and selections; the owner may amend by reply.
