# Agent User Manual edits for Piping's binding-form loop and App v4's reading sentence

Prepared by AM, a Type 2 TASK, for HELP_HUMAN (ROOT), run `ROOT-LOOPINIT-AUM-ALIGNMENT-20261005`. This file is analysis and proposal only; no other file was written.

**Revision 2 (ROOT's rulings, 2026-10-05).** The AUM HTML will be re-rendered on a new source basis: main after PRs #1092 and #1093. So the App (v3) statements formerly listed in L4 are now corrected to be true at that basis.
- Changed: E1 (note), E2, E4 and E5. E5 uses a variant of ROOT's proposed form, for the reason given there.
- Added: E16 (line 573) and E17 (line 585, the Node note; it goes beyond L4, so ROOT may drop it).
- Q2 (`[field-book]`) is accepted, and Q3 (no App v4 parity edit) is confirmed.
- The #1093 check, L3, L4 and the new L5 are updated below.

**Basis.**
- `RUN2/OWNER_DECISIONS.md`: updates that make the Agent User Manual consistent with Piping's binding-form LOOP_INIT and with App v4's changed sentence, plus other minimal consistency edits.
- `NUM` at HEAD `8225f8f2a2` (#1092's commit). `AUM` there has 895 lines and sha256 `08ca0e40cd5157574a011bac57d539e77e9007a0d46494785da8b92745391b1a`, the source fingerprint its HTML edition records. At this HEAD, AUM, App's loop and construct match the local `origin/main` ref.
- Piping's new `NUM/projects/chirality-piping/loop/LOOP_INIT.md`, read in full, and its predecessor at `8225f8f2a2~1` for the old §§0–6. App's loop, `NUM/projects/chirality-app-dev/loop/LOOP_INIT.md`, read for E2, E4, E5 and E16.
- `PRUN/CONSISTENCY_EDITS.md` §C1 (cited below as C1) and `PRUN/LOOP_INIT_MAPPING.md` (its rows are cited as "mapping row n").
- App v4's sentence: "If you are unsure whether something matters, ask the human." becomes "If you are unsure whether a section matters, read it."
- #1093 is not in this checkout. Its two sentences are taken from ROOT's message.

**Method.**
- Line numbers are AUM's at the basis. Each AUM paragraph is one line, so each edit stays within one line; E15 adds a line.
- Each Before block occurs exactly once in AUM, counted on the file's bytes, and lies on the stated line. E15's Before is the whole line; its After adds the next line.
- All seventeen edits were applied together in memory, not on disk. The result has 896 lines and sha256 `1ba63acdf4b4ad9efe88ac8a7fe4ac009ce05681a2f6025b62841720915761ce`.
  - Every reference-style link in the result resolves, and no definition loses its last use.
  - No `[Piping loop §…]` citation remains. The 8 remaining `[Piping loop]` citations (lines 62, 104, 347, 524, 601, 603, 605 and 613) cite content the new file holds.
  - No "at this basis" or "none selected" statement remains about the App or Piping loops. The one "at this basis" left, line 607's Piping Cargo note, was checked: `projects/chirality-piping/Cargo.toml` does not exist.
- Every quotation here was checked verbatim against its source, with runs of whitespace collapsed to one space.
- Abbreviations: construct = `NUM/workflows/construct-local-work-graph/WORKFLOW.md`; BR = `NUM/workflows/bounded-reconciliation/WORKFLOW.md`; FB = `NUM/docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Field_Book_v1.md`; P/AGENTS = `NUM/projects/chirality-piping/AGENTS.md`; Piping loop = `NUM/projects/chirality-piping/loop/LOOP_INIT.md`; App = App v3, `NUM/projects/chirality-app-dev`; App loop = its `loop/LOOP_INIT.md`.

**App v4 check.** AUM says nothing about App v4's reading guidance, so the changed sentence needs no AUM edit.
- §14's App v4 entry (line 595) stays true: "Its `LOOP_INIT.md` binds it to this manual, the Field Book and the bundled workflows, and holds its project pointers, conventions and standing constraints."
- §1 (line 46) already agrees with the new sentence: "It should prepare consequential human decisions, rather than multiply prompts for each tool result or harmless implementation detail."
- §5, step 4 (line 239) ends "In doubt, ask." It concerns relationships found during development, not reading, so the changed sentence does not contradict it. See L2.

**#1093 check.** No AUM passage quotes or paraphrases either of #1093's revised sentences: construct's introduction ("`LOOP_INIT.md` supplies, or points to, the evergreen procedure…") and §3's adopter list ("currently App, App v4, Piping and PEC").
- Line 347 ("In the adopted App and Piping loop") and line 381 ("the adopting App/Piping current graph") name App and Piping without claiming they are the only adopters. They stay true.
- Line 518 cites construct's receipt location, not its adopter list.
- The adopter list does bear on AUM's statements that PEC keeps its own continuation rules. See L5.

## 1. AUM edits

Seventeen edits. Apply them in any order; their Before blocks do not overlap. E1, E2, E4 and E5 changed in revision 2; E16 and E17 are new.

### E1. Line 5: front matter, revision note (changed in revision 2)

Reason: Records this revision, so that "Other content and its source basis are unchanged" stays true.

Now carried by: AUM's own practice: each 4 October revision extended this note. If E17 is dropped, drop its clause here too.

Before:
```text
links now point to the book's current edition. Other content and its source basis are unchanged.*
```

After:
```text
links now point to the book's current edition. Revised 5 October 2026: App and Piping loop statements (§§1–2, 9, 14–15) match the current loops, Piping loop citations (§§2, 9, 13, 15, 18, 20) follow Piping's current loop, and §14's Node note matches the App build guide. Other content and its source basis are unchanged.*
```

### E2. Line 74: §1, adoption table, App/Piping row (changed in revision 2)

Reason: Neither loop has a "none selected" header now; both are evergreen and name no undertaking (C1; ROOT ruling Q1).

Now carried by: App loop: "Keep this file evergreen: undertaking selection and graph references come from the init steering and subsequent human directions". Piping loop: "The human's steering selects the undertaking".

Before:
```text
Both checked loop headers currently say “none selected for a successor undertaking”; this selects no new work and proves no prior program complete.
```

After:
```text
Neither loop names an undertaking; the human's steering selects it, and the loop's silence selects no new work and proves no prior program complete.
```

### E3. Line 102: §2, the five recoveries

Reason: The recovery steps left Piping's loop (mapping rows 22–26); FB §5, which Piping's entry reading reads in full, carries them.

Now carried by: FB §5, "Orient and recover": "Read the human's steering and the accepted basis." … "Confirm that previous workers have stopped or transfer ownership before reassigning their files or resources."

Before:
```text
development. [App loop][app-loop] · [Piping loop][piping-loop] · [Runtime loop][runtime-loop] · [PEC loop][pec-loop]
```

After:
```text
development. [App loop][app-loop] · [Runtime loop][runtime-loop] · [PEC loop][pec-loop] · [Field Book §5][field-book]
```

### E4. Line 104: §2, App and Piping recovery (changed in revision 2)

Reason: Neither loop holds a graph pointer or a "none selected" header, and Piping's has no §§0–1 (C1; ROOT ruling Q1).

Now carried by: App loop §0: "The init steering and subsequent human directions establish the purpose, phase, priorities and limits. Recover the graph for that undertaking from the supplied references and relevant project records." Piping loop, entry step 3: "Read the work graph of the undertaking the steering names." Construct §1: "Recover a continuing undertaking through the current graph and compare its position with actual work before planning it again."

Before:
```text
For App and Piping, resolve the actual `loop/LOOP_INIT.md` pointer and the undertaking named by the human. Read its graph, phase cursor, owner directions and handoff where applicable; compare them with the branch, working tree, consequential unmerged work and evidence. Both checked headers say “none selected for a successor undertaking.” That is not a finding that earlier work is complete: recover an ongoing program and its pins before replacing it. A missing or stale expected graph needs recovery. Create a successor only within the human's direction, at the required WorkGraphs location. [App loop §§0–1][app-loop] · [Piping loop §§0–1][piping-loop] · [Construct a local work graph §4][construct-graph]
```

After:
```text
For App and Piping, take the undertaking from the human's steering, since neither `loop/LOOP_INIT.md` names one, and read its graph, phase cursor, owner directions and handoff where applicable; compare them with the branch, working tree, consequential unmerged work and evidence. The loop's silence is not a finding that earlier work is complete: recover an ongoing program and its pins before replacing it. A missing or stale expected graph needs recovery. Create a successor only within the human's direction, at the required WorkGraphs location. [App loop §§0–1][app-loop] · [Piping loop][piping-loop] · [Construct a local work graph §§1, 4][construct-graph]
```

### E5. Line 381: §9, the graph's location (changed in revision 2)

Reason: Neither loop points to a particular graph (ROOT ruling Q1). App's loop names the full path pattern and Piping's only the folder, so "the WorkGraphs location" replaces ROOT's "that location" to stay true for both. SPEC §9.8 is added because the cited v8 §4.2 still says the opposite (L1).

Now carried by: App loop §1: "Create the Git-tracked graph at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`." Piping loop: "**Work graphs.** `execution/_Coordination/WorkGraphs/`." SPEC §9.8: "LOOP_INIT remains evergreen and carries no undertaking-specific pointer or execution state."

Before:
```text
The revised method requires the adopting App/Piping current graph at exactly `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, relative to the project, included early in the PR sequence and kept current. `LOOP_INIT.md` points to that actual path. Historical graphs remain in place; a still-pinned undertaking moves only through its owning explicit adoption. Carry current scope and state into the adopted graph, with detailed AgentRuns evidence linking to it instead of maintaining a second current copy. [Human manual §§4.1–4.2][human-manual]
```

After:
```text
The revised method requires the adopting App/Piping current graph at exactly `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, relative to the project, included early in the PR sequence and kept current. `LOOP_INIT.md` names the WorkGraphs location, not a particular graph; the human's steering selects the graph. Historical graphs remain in place; a still-pinned undertaking moves only through its owning explicit adoption. Carry current scope and state into the adopted graph, with detailed AgentRuns evidence linking to it instead of maintaining a second current copy. [Human manual §§4.1–4.2][human-manual] · [SPEC §9.8][spec]
```

### E6. Line 387: §9, walking the route

Reason: Piping's loop no longer holds the route checks or the no-release statement (mapping rows 38–41 and 92).

Now carried by: Construct §3: "executable dependencies are acyclic, and shared writes have an integration owner." Construct §4: "Graph construction changes no scope, hold, lifecycle or release authority by itself."

Before:
```text
issue a deliverable. [App loop][app-loop] · [Piping loop][piping-loop]
```

After:
```text
issue a deliverable. [App loop][app-loop] · [Construct a local work graph §§3–4][construct-graph]
```

### E7. Line 524: §13, MEMORY shape and PR URL

Reason: Piping's §5 is gone (C1); its loop keeps only the MEMORY convention.

Now carried by: Piping loop: "Add a terse Runs entry to each affected deliverable's `MEMORY.md`, and create the file the first time it is needed." Construct §4: "Do not require a later commit solely to write the final merge result back into its own candidate."

Before:
```text
[App loop §5][app-loop] · [Piping loop §5][piping-loop]
```

After:
```text
[App loop §5][app-loop] · [Piping loop][piping-loop] · [Construct a local work graph §§3–4][construct-graph]
```

### E8. Line 601: §15, opening

Reason: Replaces the stale "none selected" quotation (C1) with what the file now is, in the form of AUM's App v4 entry (line 595).

Now carried by: Piping loop: "This file binds Piping to Root `AGENTS.md`, the active role, project `AGENTS.md`, the bundled workflows and the manuals." and "The human's steering selects the undertaking".

Before:
```text
At this basis, the published Piping loop says “none selected for a successor undertaking.” The revised entry
```

After:
```text
Piping's `loop/LOOP_INIT.md` binds it to project `AGENTS.md`, this manual, the Field Book and the bundled workflows, and holds its entry reading, record pointers, conventions and standing constraints. It names no undertaking; the human's steering selects one. The revised entry
```

### E9. Line 605: §15, recovery

Reason: The live loop selects no graph; the steering names it (C1).

Now carried by: Piping loop, entry step 3 (as E4). Construct §1 (as E4).

Before:
```text
Recover the graph selected by the live loop, then its linked resume procedure, phase events, handoff, and later owner directions. When a summary and its events disagree, establish what actually ran and which candidate was examined before continuing. A selected reconciliation program retains its activation, method pins, evidence restrictions, and separate repair authority. Apply the selected run's actual testing instructions; the general development commands below cannot override a narrower audit brief. [Piping loop][piping-loop] · [Reconciliation contract][reconciliation-contract]
```

After:
```text
Recover the graph of the undertaking the human's steering names, then its linked resume procedure, phase events, handoff, and later owner directions. When a summary and its events disagree, establish what actually ran and which candidate was examined before continuing. A selected reconciliation program retains its activation, method pins, evidence restrictions, and separate repair authority. Apply the selected run's actual testing instructions; the general development commands below cannot override a narrower audit brief. [Piping loop][piping-loop] · [Construct a local work graph §1][construct-graph] · [Reconciliation contract][reconciliation-contract]
```

### E10. Line 613: §15, closeout

Reason: Piping's §§3–6 are gone (C1); its loop adopts construct's closeout and BR.

Now carried by: Piping loop: "Piping adopts its graph, closeout, receipt and MEMORY conventions" and "`bounded-reconciliation`, for the closeout comparisons". BR: "normally the penultimate merge".

Before:
```text
[Piping loop §§3–6][piping-loop]
```

After:
```text
[Piping loop][piping-loop] · [Construct a local work graph §3][construct-graph] · [Bounded reconciliation][bounded-reconciliation]
```

### E11. Line 673: §18, recovering from the actual state

Reason: Piping's §0 is gone (C1); the paragraph's checks are FB §5's (mapping rows 22 and 25).

Now carried by: FB §5, "Orient and recover" (as E3).

Before:
```text
[Piping loop §0][piping-loop]
```

After:
```text
[Field Book §5][field-book]
```

### E12. Line 682: §18, cursor validation

Reason: Piping's loop holds no validation rule, only the closed ledger's status (C1).

Now carried by: P/AGENTS, "Software checks": "Historical receipt validation protects existing records and does not require new entries." Piping loop, for the ledger only: "is a closed historical ledger that ends at Receipt 162."

Before:
```text
validator claim. [App loop][app-loop] · [Piping loop][piping-loop]
```

After:
```text
validator claim. [App loop][app-loop] · [Piping software checks][piping-agents]
```

### E13. Line 690: §18, terminal condition

Reason: Piping's §6 is gone (C1); construct §§3–4 is already cited.

Now carried by: Construct §3: "The final PR merge is the terminal condition after the promised work and required review, checks and human decisions." P/AGENTS: "The loop ends when its completed graph's final PR merges after required checks, review and human decisions."

Before:
```text
[Piping loop §6][piping-loop]
```

After:
```text
[Piping instructions][piping-agents]
```

### E14. Line 769: §20, a stale continuation summary

Reason: Piping's loop holds no recovery procedure (C1).

Now carried by: Construct §1 (as E4). Construct §4: "One maintainer integrates changes against the latest graph revision."

Before:
```text
discrepancy. [Piping loop][piping-loop] · [Bounded reconciliation][bounded-reconciliation]
```

After:
```text
discrepancy. [Construct a local work graph §§1, 4][construct-graph] · [Bounded reconciliation][bounded-reconciliation]
```

### E15. Line 803: §21, new link definition

Reason: E3 and E11 cite the Field Book, which AUM does not yet define; the new line follows `[human-manual]` (accepted, ROOT ruling Q2).

Now carried by: The target is the Field Book edition that `NUM/docs/alignment-manual/README.md` lists as current; the path resolves from AUM's folder.

Before:
```text
[human-manual]: Project_Management_for_Human_Agent_Teams_Consolidated_v8.md
```

After:
```text
[human-manual]: Project_Management_for_Human_Agent_Teams_Consolidated_v8.md
[field-book]: Project_Management_for_Human_Agent_Teams_Field_Book_v1.md
```

### E16. Line 573: §14, App's loop (added in revision 2)

Reason: App's loop has no "none selected" header; it is evergreen (former L4; ROOT ruling Q1). The next sentence, "Its revised procedure matches the shared graph, closeout and memory methods.", stays true.

Now carried by: App loop: "Keep this file evergreen: undertaking selection and graph references come from the init steering and subsequent human directions".

Before:
```text
At this basis, the published App loop says “none selected for a successor undertaking.” Its revised procedure
```

After:
```text
The App loop is evergreen and names no undertaking; the human's steering selects it. Its revised procedure
```

### E17. Line 585: §14, Node requirement (added in revision 2)

Reason: The App build guide now records Node `>=22.19.0`, so "stale at this basis" would be false at the new render basis. This goes beyond L4; it is offered under ROOT's rule that every "at this basis" statement must be true there. If ROOT drops it, drop E1's Node clause too.

Now carried by: App build guide §3: "The current package manifest declares:" followed by "Node engine: `>=22.19.0`;". Both manifests declare `"node": ">=22.19.0"`.

Before:
```text
; the older App build guide's `>=20` statement is stale at this basis.
```

After:
```text
, as the App build guide also records.
```

## 2. Edits outside AUM

**None are needed for App v4's sentence change.** I searched for "something matters", "section matters", "unsure whether" and "ask the human", and for the paragraph's other sentences ("When to read further", "Read the section, not the chapter", "Record what you read"):
- `NUM/projects/chirality-app-v4` outside `execution/`: only `loop/LOOP_INIT.md` line 33, the sentence itself. `README.md` and `init/dev-loop-init-prompt.md` point to the loop without describing its reading guidance. `conceptual/EXEMPLARS_AND_LESSONS.md` line 217, "A design aim for where to ask the human and what to show.", is a product design aim and is unaffected.
- `NUM/init/`: no App v4 text.
- `NUM/docs/`, excluding AUM, archives and historical manifests: only FB line 94, "In doubt, ask." (L2). FB's HTML line 336 is its rendering.
- `NUM/workflows/`: "Ask the human" appears only for named decisions (reconciliation, project-setup, review, dbm-publisher). None concerns reading.

**Pinned product resources: listed, not proposed.** Each records the current sha256 of App v4's LOOP_INIT, `45c23cf477e23aff1d0152189caf7e8ebfb53eca42e3a1fae87a06af8c197f28`, and will be one revision behind after the sentence change:
- `NUM/projects/chirality-app-v4/app/src-tauri/resources/instructions/SOURCE_MAP.json`, line 103 (entry `"id": "loop"`);
- `NUM/projects/chirality-app-v4/app/src-tauri/resources/policy_standing/basis.json`, line 20;
- `NUM/projects/chirality-app-v4/app/src-tauri/resources/policy_standing/a16/basis.json`, line 14.

Searching `app/` for `basis.json` and `SOURCE_MAP` found no source or test that compares these hashes with the file. This agrees with ROOT's staged notice.

**The sentence itself, for reference.** This is ROOT's edit and is not counted above. In `NUM/projects/chirality-app-v4/loop/LOOP_INIT.md`, lines 32–33, the Before occurs exactly once.

Before:
```text
govern; the manuals explain. Record what you read in the run evidence. If you
are unsure whether something matters, ask the human.
```
After:
```text
govern; the manuals explain. Record what you read in the run evidence. If you
are unsure whether a section matters, read it.
```

**Publication follow-on.** This is a consequence, not a drafted edit. The HTML edition records the Markdown's sha256 (`08ca0e40…`). After the AUM edits, regenerate `NUM/docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.html` with `render_manual.py` on the new basis, and update the render-basis lines in `NUM/docs/alignment-manual/README.md`, as commit `f3c49c341e` did after the 4 October revisions. No CI check runs the renderer (searched for `render_manual`). AUM's line 3, "repository source basis `b3e2ce4…`", is the guide's original documentation basis; earlier re-renders left it unchanged.

## 3. Listed only

**L1. Consolidated v8 says LOOP_INIT points to the graph.** These three statements have been stale since the 2026-09-23 evergreen rule. They contradict construct §4 ("Keep undertaking-specific paths and state out of reusable loop instructions."), SPEC §9.8 and both loops:
- line 1678 (§4.2): "keep it current, and point LOOP_INIT to its actual location." (C2);
- line 1782: "and LOOP_INIT must point there." (C2);
- line 1786: "Keep LOOP_INIT's pointer aligned with the actual selected graph at the required WorkGraphs path." This one is not in C2.

**L2. "In doubt, ask."** This appears in FB line 94 and in AUM line 239 (§5, step 4). Both lines concern relationships found during development and name the cases to raise; App v4's rulings GC-7 and GC-8 are the source. The changed sentence concerns reading, so it does not contradict them. They do share the old sentence's tension with Root `AGENTS.md`, "uncertainty alone does not require an extra prompt.". No edit is proposed.

**L3. Construct's introduction.** `NUM/workflows/construct-local-work-graph/WORKFLOW.md`, lines 11–12, currently says: "The human's steering selects the undertaking; `LOOP_INIT.md` supplies the evergreen procedure for recovering, constructing and following its graph." According to ROOT, #1093 revises it to "supplies, or points to". That is not verifiable in this checkout.

**L4. App (v3) statements: now resolved** by E2, E4, E5 and E16 under ROOT's ruling Q1. App's loop contains no "none selected" (0 occurrences) and is evergreen.

**L5. PEC statements stale for other reasons (new).** PEC's loop adopted the shared development loop on 2026-09-25 (commit `11be801130`, "docs(pec): adopt the shared development loop"). It is evergreen, uses `construct-local-work-graph`, and writes one receipt at `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`. Construct §3 lists PEC as an adopter. AUM still treats PEC as outside the revised arrangement:
- line 62: "Runtime and PEC retain different continuation rules.";
- line 74, table row "Runtime or PEC": "Retain the project's accepted selection, recording and closeout arrangements.";
- line 106: "Neither project inherits App/Piping's removal of routine receipts.";
- line 667 (§17): "PEC retains one branch per run, one commit and receipt per iteration, a validated receipt chain";
- lines 684 and 690 (§18): Runtime and PEC "retain their own closeout contracts" and "their own accepted completion contracts".

I did not audit §17 beyond these lines, or Runtime's statements.

## 4. Questions for ROOT

- **Q4. PEC (L5).** On the new render basis, AUM's PEC statements look untrue. Should a further minimal pass correct them in this tranche, or should they wait for a PEC-scoped revision? A pass would cover §1 (line 62 and the table), §2 (line 106), §17 and §18.
- **Q5. E17 (the Node note).** It goes beyond L4. Keep it under the "true at the new basis" rule, or drop it, together with E1's Node clause?
