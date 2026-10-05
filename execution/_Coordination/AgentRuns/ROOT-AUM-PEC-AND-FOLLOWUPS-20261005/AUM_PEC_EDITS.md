# Agent User Manual edits for PEC's current state

Prepared by PM, a Type 2 TASK, for HELP_HUMAN (ROOT), run `ROOT-AUM-PEC-AND-FOLLOWUPS-20261005`. This file is analysis and proposal only; no other file was written.

**Basis.**
- `RUN3/OWNER_DECISIONS.md`: correct the Agent User Manual's PEC statements "based on the current state of PEC".
- `NUM` at HEAD `9f8ebac002`, whose tree equals main `7ba1181d43` (both trees are `53ef3dbf3e…`). `AUM` there has 896 lines and sha256 `1ba63acdf4b4ad9efe88ac8a7fe4ac009ce05681a2f6025b62841720915761ce`, the result #1094's edits produced.
- The working tree also holds another worker's uncommitted edits to the three Consolidated v8 files. I read v8 from `HEAD` with `git show`. `AUM` and every `PEC` file I read are unmodified from `HEAD`.
- PEC's records, read as the brief lists: `PEC/AGENTS.md` and `PEC/loop/LOOP_INIT.md` in full; `PEC/init/`; commit `11be801130` and the four `PEC-*` tranche manifests; the notices it routed; `PEC/loop/LOOP_RECEIPTS.md`; PEC's work graphs, central receipts, `MEMORY.md` files and Task Management registers; `NUM/init/dev-loop-init-prompt.md` §4; and `NUM/workflows/construct-local-work-graph/WORKFLOW.md` §3.
- The prior TASK's list: `NUM/execution/_Coordination/AgentRuns/ROOT-LOOPINIT-AUM-ALIGNMENT-20261005/AUM_EDITS.md` §3 L5. Its lines 62, 74, 106, 667, 684 and 690 are now AUM lines 62, 76, 106, 667, 684 and 690. Line 74 is now the App/Piping row, and the "Runtime or PEC" row moved to 76.

**Method.**
- Line numbers are AUM's at the basis. Each AUM paragraph is one line. Where one line needs changes in two or three places, the edit has hunks (a), (b) and (c), each with its own Before.
- Every Before occurs exactly once in AUM, counted on the file's bytes, and lies on the stated line.
- All edits were applied together in memory, not on disk. Section 3 gives the result.
- Every quotation from a source was checked verbatim against that source, with runs of whitespace collapsed to one space.
- Abbreviations: P/AGENTS = `PEC/AGENTS.md`; P/LOOP = `PEC/loop/LOOP_INIT.md`; construct = `NUM/workflows/construct-local-work-graph/WORKFLOW.md`.

## 1. PEC's current state at main `7ba1181d43`

**Adoption.** PEC adopted the shared development loop on 2026-09-25 under its own decision `D-PEC-94`. Commit `11be801130` made the change, PR #917 carried it, and merge `13df8b795e` landed it the same day. Its manifest is `NUM/docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`.
- P/AGENTS: "Under `D-PEC-94` (owner direction of 2026-09-25, recorded by HELP_HUMAN), PEC adopts the shared development-loop method that App and Piping run."
- PEC routed non-binding notices to Root, App, Piping and Runtime. The Root notice, `NUM/execution/_Coordination/NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md`, flags that Root texts still name only App and Piping, and that the manual "still describes PEC's loop as `Remaining`-based".
- PEC sent itself no notice. The September 22 notices in `PEC/execution/_Coordination/` predate the adoption, and the Root notice of 5 October concerns construct's wording.

**Entry.** `PEC/init/dev-loop-init-prompt.md` starts HELP_HUMAN, which reads `P/LOOP` and follows it.
- `NUM/init/dev-loop-init-prompt.md` §4 is PEC's launcher in the Root catalog: "Paste-ready as written; this block byte-matches the PEC project launcher." I confirmed the byte match.
- The App and Piping launchers end "follow it within the owner's steering and live authority." PEC's launcher ends "follow it."
- P/LOOP: "Enter through `init/dev-loop-init-prompt.md` with the selected role and the human's steering. This file owns the recurring development-loop procedure; project `AGENTS.md` supplies standing responsibilities, boundaries and checks."

**Loop form.** The loop is evergreen and mirrors App's and Piping's Steps 0–6.
- P/LOOP: "Keep this file evergreen: undertaking selection and graph references come from the init steering and subsequent human directions; execution state lives in the selected work graph."
- The old Step 0 discovery, Remaining-based selection and per-iteration commit and receipt are retired. P/AGENTS: "former §§1–2 and 4–7 (bootstrap, pointers, Remaining selection, Steps 0–5, first return, posture) are replaced by the current `loop/LOOP_INIT.md`".
- The old fences moved to P/AGENTS "Write Scopes And Fences". The old checks, preflight and evidence contract moved to "Development checks and evidence" and "Active Reliance Holds".

**Graph method.** P/LOOP: "Use `chirality-root:bundled:workflow:construct-local-work-graph` when no graph exists or its route needs substantial revision."
- The graph lives at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`.
- Construct §3 names PEC: "For a loop that adopts this method (currently App, App v4, Piping and PEC)".
- Three undertakings have run under this loop, each with a graph and a central receipt: `HELP-HUMAN-PEC-20260925-POST-SCA005`, `-20260926-REMAINING-RETIREMENT` and `-20260927-RV1-INTAKE`. Their final PRs, #1014, #982 and #1028, merged on 26–27 September. No other graph is present under `PEC/execution/_Coordination/WorkGraphs/`.

**Selection.** Steering selects the undertaking.
- `D-PEC-99` retired the deliverable `## Remaining` sections. No `_STATUS.md` under `PEC/execution/PKG-*` has one; there are 68 such files. The 109 headings that remain are all historical concordance copies under `_Reconciliation/DeliverableConcordance`.
- P/AGENTS: "Add no `## Remaining` section or entry."
- Dependency rule, P/AGENTS: "A dependency-register row blocks work only when it is `ACTIVE`, of type `PREREQUISITE`, its `SatisfactionStatus` is `TBD`, `PENDING` or `IN_PROGRESS`, and the work needs its target."

**Closeout.** Substantive PRs carry their own consequences. One bounded documentation/governance closeout follows, using `bounded-reconciliation`, normally at the penultimate merge and before the final PR (P/LOOP §3).
- P/LOOP: "The loop ends when the completed work graph's final PR merges under standing Git authority."

**Receipts and MEMORY.** One central receipt per undertaking, and terse MEMORY rows (P/LOOP §5).
- The receipt is at `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`.
- The MEMORY rows go in the deliverables' `MEMORY.md` `## Runs` tables. There are 33 `MEMORY.md` files and no `_MEMORY.md`.
- P/AGENTS: "`loop/LOOP_RECEIPTS.md` is a historical ledger, closed by Receipt 197 at this adoption. Append nothing further".
- The validator still runs on every PR. P/AGENTS: "(protects the closed ledger; requires no new entry)".

**Task Management.** Intake is conditional, under P/LOOP §4, through WORKING_ITEMS selecting `chirality-root:bundled:workflow:task-management`.
- `PEC/init/taskmgmt-init-prompt.md` is now a pointer: "This former session script is retired."
- The registers are `REGISTER.csv` and `REGISTER_CLOSED.csv`, under `PEC/execution/_Coordination/_TaskManagement/`.

**What PEC keeps that App and Piping do not.**
- **MEMORY rows need a grant.** Outside `execution/_Coordination/**`, a MEMORY row needs the path grant of the governing `D-PEC` packet. Without that grant the graph cannot complete until the grant is given and the row written, or until the owner decides to complete without the row.
- P/AGENTS: "a MEMORY row needs the path grant of the undertaking's governing `D-PEC` packet like any other write there." The RV1-INTAKE graph shows this in use: "`D-PEC-107` granted no `MEMORY.md` path; the owner then granted the rows".
- **The `D-PEC` packet rule.** Every other write needs an owner-ruled packet, under fences F-PEC-1..4. P/AGENTS: "The development loop, a work graph, a Task Management outcome or a central receipt opens no path either."
- **Frozen corpus and data.** The frozen reference corpus, and content-minimal data (PEC-K-10).
- **Reliance holds.** The reliance-hold preflight (`pec_reliance_hold.py`) runs before dispatch, review, fan-in, reliance, consumption or promotion. Operational reliance on PEC data waits on the PRD §12 gate (`D-PEC-90`).
- **A closed ledger.** PEC's ledger closed with a closing receipt; App and Piping stopped theirs without one. The validator still protects it on every PR.
- **Status and README trace.** While `D-PEC-88` applies, each `docs/STATUS.md` and `README.md` change is named in the graph and central receipt.
- **Model convention.** PEC keeps its own session model convention.
- **Its reading of `D-PEC-80`.** A `WORKPLAN_*.md` in `loop/` is a defect.
- **Records on `origin/main`.** Owner acts, rulings, notices and hold releases are relied on only once observable on `origin/main` after `git fetch`.

## 2. AUM edits

There are 16 edits, on 16 lines. Their Before blocks do not overlap, so they apply in any order.

### E1. Line 5: front matter, revision note

Reason: Extends #1094's 5 October entry, so that "Other content and its source basis are unchanged" stays true.

Before:
```text
, and §14's Node note matches the App build guide.
```

After:
```text
, §14's Node note matches the App build guide, and PEC statements (§§1–2, 8, 17–18) match PEC's current loop, instructions and profile.
```

### E2. Line 62: §1, the common route

Reason: PEC now uses the local work graph; only Runtime keeps different continuation rules.

Now carried by: P/AGENTS "PEC adopts the shared development-loop method that App and Piping run."

Before:
```text
the revised App and Piping route uses a local work graph; Runtime and PEC retain different continuation rules.
```

After:
```text
the revised App, Piping and PEC route uses a local work graph; Runtime retains different continuation rules.
```

### E3. Line 74: §1, adoption table, the adopting row

Reason: PEC is now an adopting loop, and its loop also names no undertaking. This row and E4 together move PEC out of the Runtime row.

Now carried by: construct §3 "(currently App, App v4, Piping and PEC)". P/LOOP "Keep this file evergreen: undertaking selection and graph references come from the init steering and subsequent human directions".

Before (a):
```text
| App/Piping undertaking adopting the revision |
```

After (a):
```text
| App, Piping or PEC undertaking adopting the revision |
```

Before (b):
```text
Neither loop names an undertaking;
```

After (b):
```text
None of these loops names an undertaking;
```

### E4. Line 76: §1, adoption table, the Runtime or PEC row

Reason: PEC no longer keeps its earlier selection, recording and closeout. The row now covers Runtime alone, whose notice is singular.

Now carried by: the Runtime September 22 notice: "This is an M6 source notice, not Runtime adoption".

Before:
```text
| Runtime or PEC | Retain the project's accepted selection, recording and closeout arrangements. The source notices neither adopt the revision there nor authorize product work. |
```

After:
```text
| Runtime | Retain the project's accepted selection, recording and closeout arrangements. The source notice neither adopts the revision there nor authorizes product work. |
```

### E5. Line 104: §2, recovery for the adopting loops

Reason: PEC recovers the way App and Piping do. Its own recovery passage on line 106 is removed by E6.

Now carried by: P/LOOP §0 "Recover the graph for that undertaking from the supplied references and relevant project records."

Before (a):
```text
For App and Piping, take the undertaking from the human's steering, since neither `loop/LOOP_INIT.md` names one,
```

After (a):
```text
For App, Piping and PEC, take the undertaking from the human's steering, since none of their `loop/LOOP_INIT.md` files names one,
```

Before (b):
```text
[App loop §§0–1][app-loop] · [Piping loop][piping-loop] · [Construct a local work graph §§1, 4][construct-graph]
```

After (b):
```text
[App loop §§0–1][app-loop] · [Piping loop][piping-loop] · [PEC loop §§0–1][pec-loop] · [Construct a local work graph §§1, 4][construct-graph]
```

### E6. Line 106: §2, recovery for Runtime and PEC

Reason: Several things on this line are untrue for PEC now.
- PEC's prescribed discovery is retired.
- Its Remaining sections are gone.
- It writes one central receipt, not routine receipts.

The Runtime sentence is unchanged.

Now carried by: P/AGENTS "former §§1–2 and 4–7 (bootstrap, pointers, Remaining selection, Steps 0–5, first return, posture) are replaced by the current `loop/LOOP_INIT.md`".

Before:
```text
For PEC, perform its prescribed discovery and re-derive selectable work from deliverable Remaining sections, gates, and exact ruled packets. Neither project inherits App/Piping's removal of routine receipts. [Runtime loop][runtime-loop] · [PEC loop][pec-loop]
```

After:
```text
Runtime does not inherit the removal of routine receipts that App, Piping and PEC adopted. [Runtime loop][runtime-loop]
```

### E7. Line 331: §8, readiness

Reason: PEC's blocking rule no longer uses a Remaining item's `Depends` line. The cited "PEC loop §5" is now the receipt step; the rule is in P/AGENTS "Selection and decisions".

Now carried by: P/AGENTS "A dependency-register row blocks work only when it is `ACTIVE`, of type `PREREQUISITE`, its `SatisfactionStatus` is `TBD`, `PENDING` or `IN_PROGRESS`, and the work needs its target."

Before (a):
```text
PEC retains its earlier conjunction involving an active `PREREQUISITE`, an unsatisfied status and the selected item's `Depends` line.
```

After (a):
```text
PEC blocks work only on an active `PREREQUISITE` row whose status is unsatisfied and whose target the work needs.
```

Before (b):
```text
[App selection rules][app-agents] · [PEC loop §5][pec-loop]
```

After (b):
```text
[App selection rules][app-agents] · [PEC selection rules][pec-agents]
```

### E8. Line 644: §17, the live entry

Reason: Step 0 no longer validates receipts, checks for workplans or discovers Remaining surfaces. It has no command block. The first and last sentences of this line stay true.

Now carried by:
- P/LOOP §0 "Recover the graph for that undertaking from the supplied references and relevant project records."
- P/AGENTS "citations of former `loop/LOOP_INIT.md` §3 (fences) resolve to "Write Scopes And Fences" above; former §8 (checks, preflight) and §9 (evidence contract) resolve to this section and "Active Reliance Holds"".

Before (a):
```text
The loop's full Step 0 refreshes remote references, validates receipts, checks retired-workplan absence, reads decision/profile/decomposition/hold sources, and discovers actual Remaining surfaces. Do not substitute a general quick-start command block for this adopted procedure during execution.
```

After (a):
```text
Since 25 September 2026, under its own decision `D-PEC-94`, PEC runs the shared development loop: the loop is evergreen, and its Step 0 recovers the selected undertaking's graph and actual state. Project `AGENTS.md` now holds the fences, checks, reliance-hold preflight and evidence contract the earlier loop carried.
```

Before (b):
```text
they are not a second live loop. [PEC loop][pec-loop]
```

After (b):
```text
they are not a second live loop. [PEC loop][pec-loop] · [PEC instructions][pec-agents]
```

### E9. Line 646: §17, selection

Reason: Selection from `_STATUS.md ## Remaining`, and its exception for owner requests, are retired. The `origin/main` rule survives in P/AGENTS.

Now carried by:
- P/AGENTS "Add no `## Remaining` section or entry."
- P/AGENTS "Steering selects the undertaking; record new open scope in its work graph and governing records."
- P/AGENTS "A moved item's gate markers still bind it at its destination."
- P/AGENTS "Rely on an owner act, ruling, routed notice or reliance-hold release only once its record is observable on `origin/main` after `git fetch`, never on an unmerged branch's claim of it."

Before:
```text
Select work from deliverable `_STATUS.md ## Remaining` and the exact scope of its grant. A missing Remaining section means no recorded selectable scope, not completion and not permission to invent an assignment. The loop permits an explicitly scoped owner request for preparation or correction without a Remaining item, but that exception does not authorize production or bypass a merged owner prerequisite. Owner acts and hold releases required by the loop are observed on fetched `origin/main`; predecessor work on the run branch is a different condition. [PEC loop §5][pec-loop]
```

After:
```text
The human's steering selects the undertaking; record new open scope in its graph at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` and in its governing records. Deliverable `## Remaining` sections were retired under `D-PEC-99`: `_STATUS.md` carries lifecycle and history only, so add no Remaining section and select nothing from one. An item moved into that decision's exhibit keeps its gate markers there. Owner acts and hold releases are relied on only once their records are observable on fetched `origin/main`; an unmerged branch's claim is a different condition. [PEC deliverable records][pec-agents] · [PEC loop §§0–1][pec-loop]
```

### E10. Line 648: §17, write fences

Reason: The fences now live only in P/AGENTS, so the "PEC loop §3" citation is stale. The adopted loop adds the explicit rule that loop records open no path.

Now carried by: P/AGENTS "The development loop, a work graph, a Task Management outcome or a central receipt opens no path either."

Before (a):
```text
Existing code or a valid PRD grants no broader implementation permission.
```

After (a):
```text
Existing code or a valid PRD grants no broader implementation permission; nor do the loop, a work graph, a Task Management outcome or a central receipt.
```

Before (b):
```text
[PEC write fences][pec-agents] · [PEC loop §3][pec-loop]
```

After (b):
```text
[PEC write fences][pec-agents]
```

### E11. Line 661: §17, hold-tool citation

Reason: The preflight moved from "PEC loop §8" to P/AGENTS "Active Reliance Holds". The paragraph's text stays true.

Now carried by: P/AGENTS "The deterministic preflight is `execution/_Scripts/pec_reliance_hold.py`."

Before:
```text
[PEC loop §8][pec-loop] · [PEC hold tool][pec-hold]
```

After:
```text
[PEC reliance holds][pec-agents] · [PEC hold tool][pec-hold]
```

### E12. Line 665: §17, profile and conventions

Reasons:
- `PEC/software-workflow.json` now registers six checks. `v2-parsers` arrived on 2026-09-27 with commit `26b27b2b06`, under `D-PEC-106`.
- The "compatibility treatment" the line calls for has been given. P/AGENTS maps the former agent names to Root roles and keeps the model convention as "the convention's home".
- The "PEC loop §8" citation is stale.

Now carried by: `PEC/software-workflow.json` `checks`: `v2-api-contract`, `v2-loop-registry`, `v2-store-guard`, `v2-parsers`, `v2-core-posture`, `harness-self-check`. P/AGENTS "The former agent names map to these role and method pairs".

Before (a):
```text
`v2-store-guard`, `v2-core-posture`, and `harness-self-check`
```

After (a):
```text
`v2-store-guard`, `v2-parsers`, `v2-core-posture`, and `harness-self-check`
```

Before (b):
```text
Existing role/model conventions and stale launcher references need owning-loop compatibility treatment; a newer Root notice alone does not silently migrate PEC's accepted method. [PEC profile][pec-profile] · [PEC loop §8][pec-loop] · [PEC operational review][pec-report]
```

After (b):
```text
PEC's instructions now map its former agent names to Root roles and keep its model convention. [PEC profile][pec-profile] · [PEC checks][pec-agents] · [PEC operational review][pec-report]
```

### E13. Line 667: §17, closeout and continuity

Reason: Every claim on this line is now untrue for PEC.
- The branch per run, the commit and receipt per iteration, the validated receipt chain and the PR at terminus are gone. They are replaced by the graph's PR sequence and one central receipt.
- PEC no longer "keeps those outputs" apart from the adopting undertakings.

The after text keeps the line's last sentence. It adds PEC's MEMORY grant, the closed ledger and conditional Task Management.

Now carried by:
- P/AGENTS "Item C's per-iteration commit and receipt with one PR at terminus is replaced by the graph's PR sequence and one central receipt."
- P/AGENTS "The graph completes only after that grant is given and the row written, or after the owner decides to complete without the row".
- P/LOOP §4 "Only a material, evidenced concern without a current or identified successor home qualifies for bounded Task Management intake."
- `PEC/init/taskmgmt-init-prompt.md` "This former session script is retired."

Before:
```text
PEC retains one branch per run, one commit and receipt per iteration, a validated receipt chain, and a PR at terminus or when a merged prerequisite is needed. The September 22 development-loop notice leaves its accepted basis unchanged. Retiring obsolete Task Management launchers does not migrate PEC selection or create a new intake. Keep those outputs while adopting App/Piping undertakings use graph-based continuity. Close out only exact granted scope and preserve human-gated lifecycle, artifact acceptance, release, and professional reliance as separate acts. [PEC loop §§5–7][pec-loop] · [PEC development-loop notice][pec-development-notice]
```

After:
```text
Closeout follows the shared arrangement: one bounded documentation/governance closeout before the final PR, one central receipt at `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`, and terse `MEMORY.md` Runs rows. PEC's fences still apply. A `MEMORY.md` row needs the path grant of the undertaking's governing D-PEC packet; without it, record the run in the graph and receipt and bring the missing grant to the owner, and the graph completes only once the row is written or the owner decides to complete without it. The receipt ledger `loop/LOOP_RECEIPTS.md` closed at Receipt 197 and takes no new entries. Task Management intake is conditional under the loop's Step 4; the former Task Management launcher is now a pointer to the bundled workflow. Close out only exact granted scope and preserve human-gated lifecycle, artifact acceptance, release, and professional reliance as separate acts. [PEC loop §§3–6][pec-loop] · [PEC deliverable records][pec-agents]
```

### E14. Line 682: §18, cursor validation

Reason: PEC's validator protects a closed ledger; it no longer validates a live continuation cursor. The Runtime clause is unchanged.

Now carried by: P/AGENTS every-PR check "`python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` (protects the closed ledger; requires no new entry)".

Before (a):
```text
PEC has its own live receipt-validation obligation; Runtime explicitly has no corresponding validator claim.
```

After (a):
```text
PEC still runs its receipt validator on every PR, but only to protect its closed ledger, which is no longer a continuation cursor; Runtime explicitly has no corresponding validator claim.
```

Before (b):
```text
[Piping software checks][piping-agents] · [PEC loop][pec-loop]
```

After (b):
```text
[Piping software checks][piping-agents] · [PEC checks][pec-agents]
```

### E15. Line 684: §18, continuation home

Reason: PEC's graph is now its continuation home, and it has no separate session receipt. Only Runtime keeps its own closeout contract.

Now carried by:
- P/LOOP §5 "A graph node or Task Management invocation does not create another loop receipt."
- P/LOOP §6 "On interruption, retain the candidate, open checks, active operations and next safe action in the graph."

Before (a):
```text
For App/Piping development, the current graph
```

After (a):
```text
For App, Piping and PEC development, the current graph
```

Before (b):
```text
Runtime and PEC retain their own closeout contracts.
```

After (b):
```text
Runtime retains its own closeout contract.
```

### E16. Line 690: §18, terminal condition

Reason: PEC's loop ends when its final PR merges. Only Runtime, and any in-flight program, keep their own completion contracts.

Now carried by: P/LOOP §6 "The loop ends when the completed work graph's final PR merges under standing Git authority. A review hold, unfinished required node or unmerged final PR means it remains open." P/AGENTS "In-flight method bases retain their own authority until explicitly transitioned."

Before (a):
```text
The revised App/Piping loops make final PR merge their terminal condition;
```

After (a):
```text
The revised App, Piping and PEC loops make final PR merge their terminal condition;
```

Before (b):
```text
In-flight programs and Runtime/PEC retain their own accepted completion contracts.
```

After (b):
```text
In-flight programs and Runtime retain their own accepted completion contracts.
```

Before (c):
```text
[App loop §6][app-loop] · [Piping instructions][piping-agents]
```

After (c):
```text
[App loop §6][app-loop] · [Piping instructions][piping-agents] · [PEC loop §6][pec-loop]
```

## 3. The result, checked

- All 16 edits (26 hunks) were applied together in memory. The result has 896 lines and sha256 `16fb79f5e8397dbcfc982726f444feb08d07d8c006b0e99924f06d0ce1eebef1`.
- **Links.** Every reference-style link in the result resolves to an existing definition. No definition loses its last use; `[pec-development-notice]` is still cited on line 78. No new link definition is needed.
- **Residual phrases.** The result contains none of these: "Runtime and PEC", "Runtime or PEC", "Runtime/PEC", "PEC loop §3", "PEC loop §5", "PEC loop §8", "PEC loop §§5–7", "Remaining surfaces".
- **Remaining.** In §17 the word "Remaining" survives only in E9's statement that the sections are retired.
- **Sections.** E1's section list (§§1–2, 8, 17–18) matches the edited lines: 62, 74, 76, 104, 106, 331, 644–667, 682, 684 and 690.

**Publication follow-on.** This is a consequence, not a drafted edit. The HTML edition `NUM/docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.html` records the Markdown's sha256. After these edits, regenerate it with `render_manual.py` and update the render-basis lines in `NUM/docs/alignment-manual/README.md`, as was done after #1094.

## 4. Checked and left unchanged

- **Line 78.** The citation of the PEC September 22 notice still supports the source comparison. That notice did leave PEC's basis unchanged; the later adoption was PEC's own.
- **Line 102.** The citation of the PEC loop supports the general advice to recover the project's cursor.
- **Line 146.** "PEC retains a distinct historical model convention that must be read in its own instructions" is still true. P/AGENTS "Session model convention" keeps it: "this section is the convention's home".
- **Lines 347, 381, 524 and 675.** These name App and Piping as using the revised method without saying that others do not. They remain true; see Q1.
- **Line 623 (§16).** This is Runtime's statement about PEC compatibility as a verification opportunity. It concerns product compatibility, not the loop.
- **Lines 642, 650, 652–659 and 663 (§17).** These agree with P/AGENTS:
  - the posture, graceful absence and no dispatch;
  - the frozen corpus, content-minimal data and no second execution loop;
  - the preflight's acts and command;
  - the `v2/src/pec_v2` tree, whose tests import `unittest`.
- **Line 661's text.** It matches P/AGENTS "A missing, malformed, or unreadable register fails closed." Only its citation changes, in E11.

## 5. Listed only

**L1. Runtime.** No Runtime statement in AUM looks stale.
- `projects/chirality-runtime/loop/LOOP_INIT.md` was last changed on 2026-09-12. It still names `HANDOFF_STATE.md`, the newest receipt and the Remaining discovery. It still says "no Runtime receipt validator or automatic receipt-format enforcement is claimed."
- Its profile registers `typecheck` and `unit` as always-checks, and its manifest declares Node `>=22.19.0`. Both agree with line 625.
- `packages/` also holds `engine-claude` and `engine-pi-omlx`. Line 625 says "principally", and line 623 already covers retained compatibility providers.
- One observation, not an AUM issue: Runtime received three PEC notices (adoption, Remaining retirement, SCA-006). By the Remaining-retirement manifest's rationale, Runtime DEL-02-06 pins `projects/pec/AGENTS.md`. That repin is Runtime's own matter.

**L2. Field Book and Consolidated v8.**
- Neither the Field Book nor v8 at `HEAD` mentions PEC; a whole-word search finds no "PEC".
- v8 lines 1678 and 1782 at `HEAD` call the arrangement "the adopted App/Piping arrangement" and "the App/Piping local development arrangement". PEC has since adopted that arrangement, but neither line says other loops cannot, so nothing conflicts.
- v8 lines 1678, 1782 and 1786 are the three LOOP_INIT-pointer lines under separate repair in this run. The working tree shows uncommitted edits to them.

**L3. Root texts PEC's notice flagged.** These are not AUM edits. PEC's adoption notice names four Root texts that list only App and Piping: SPEC §9.8, PRD_ROOT E-1, the 2026-09-22 amendment record, and construct with its template. Construct §3 now names PEC. The other three were not checked in this run.

## 6. Questions for ROOT

- **Q1. Lines 347 and 381 (§9).** These say "the adopted App and Piping loop" and "the adopting App/Piping current graph". They are true, but they now omit PEC. They also omit App v4, which construct §3 lists too.
  - The minimal extension would be "App, Piping and PEC" on each line, and §9 in E1.
  - I left them unchanged, because adding PEC but not App v4 would make a different partial list.
  - Should they be extended, and if so with App v4 too?
- **Q2. E12(a), `v2-parsers`.** This is a PEC statement that is untrue at main, but the cause is a 27 September product slice, not the loop adoption. Keep it under the brief's "every AUM statement about PEC that is untrue" rule, or drop it, together with "and profile" in E1?
- **Q3. `D-PEC-88` trace clause.** For minimality, E13 omits PEC's rule that each `docs/STATUS.md` and `README.md` change is named in the graph and receipt. Section 1 records the rule, and E13 cites P/AGENTS, where it lives. Should E13 state it explicitly?
