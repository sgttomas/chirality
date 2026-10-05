# LR-LOOPINIT: independent review of PR #1092 (piping LOOP_INIT binding form; T3 handoff as init steer)

**Reviewer:** LR, a Chirality Type 2 TASK dispatched by HELP_HUMAN (ROOT) for run `PIPING-LOOP-INIT-20261005`, under `RUN/BRIEF_LR.md`. Model: Claude Opus 5.5 (`claude-opus-5-5`), as a Claude Code subagent. I wrote none of the reviewed text. I made no Git writes, used no network beyond `gh` reads, and wrote only this file, `SHA256SUMS` beside it, and logs under `WT/scratch/lr_loopinit_01/`.

**Placeholders.** `WT` = the T3 worktree root; `NUM` = `WT/numerics`; `RUN` = `NUM/projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING-LOOP-INIT-20261005`; `V4RUN` = App v4's `APP-V4-GRAPH-CLOSURE-20261004` run; `P` = `projects/chirality-piping`; `T3` = `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3`; `RR` = `T3/ROOT_RULINGS_V1.md`; `WG` = `P/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`; `COORD` = `P/execution/_Coordination/_COORDINATION.md`; AUM, FB = the Agent User Manual v3 and the Field Book v1.

**Candidate.** PR https://github.com/sgttomas/chirality/pull/1092, head `605adf726d569b3f0f7166fcfe7558f09982b7a0` (draft, open, MERGEABLE), one commit on main `6479bf110a3b1f6dd9afecab83bc847237e42240`. NUM head `8225f8f2a2`.

| File at the head | sha256 (prefix) |
|---|---|
| `P/loop/LOOP_INIT.md` | `5c20a16fef96…` (matches RULINGS) |
| `RUN/LOOP_INIT_MAPPING.md` | `12c34aa82533…` |
| `RUN/LOOP_INIT_PROPOSED.md` | `072f6d36f367…` |
| `RUN/CONSISTENCY_EDITS.md` | `3021790802cc…` |
| `RUN/RULINGS.md` | `6cd178e87078…` |
| `RUN/OWNER_DECISIONS.md` | `d1f24dadeec8…` |

## Verdict

**REPAIR.** One MAJOR finding: the new LOOP_INIT's only standing constraint points stage-gate assessment at the wrong criteria. Its fix is a one-sentence edit to a path the manifest already covers. The mapping is sound, no load-bearing rule is lost, every path and workflow name checks, the validators and GEN-8 pass, and the T3 records are accurate apart from the items below.

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| MAJOR | 1 |
| MINOR | 3 |
| NOTE | 9 |

## Findings

### MAJOR-1: The stage-gate constraint sends an assessor to PRD §24's milestone criteria, but Piping's gate criteria are the ones ruled in COORD

**Evidence.**
- LOOP_INIT lines 84–87: "Piping's stage gates are the exit criteria of the release milestones in `docs/PRD.md` §24. `execution/_Coordination/_COORDINATION.md`, under "Current Target Stage", records the target stage; only the owner's approved update advances it."
- COORD "Current Target Stage (ruled record)" records the target as "PRD R5 exit criterion" and states its exit criteria itself, "expressed in amended-PRD tokens per `DEC-080`": the actor-neutral clean-checkout reproduction criterion of "amended PRD (v0.3) §24 R6", and "the public repository contains no known protected standards data (v0.3 §20.1 / D-20 lineage)". The label follows the historical v0.1 PRD ("### 22.6 Release R5: Engineering Beta" in `P/docs/_history/PRD_v0.1.md`, exit criteria "External engineers can reproduce validation examples" and "Public repository contains no known protected standards data"), through the D-21 Annex A crosswalk.
- `P/docs/PRD.md` §24's "### R5: Piping Components and Nonlinear Supports" has different exit criteria: "component data appears in reports with provenance" and "nonlinear cases converge or report actionable diagnostics".
- `P/docs/PLAN.md` names COORD ("Working Desktop Application Standard") as "**authoritative for the stage gate**". AUM §5: "Stage gates remain human-managed milestones under the project's own records."

**Consequence.** An agent that follows LOOP_INIT reads the recorded target "R5" against §24's R5 and prepares or assesses stage evidence against the wrong criteria. Advancement still needs the owner, so nothing advances wrongly, but the one standing constraint misdirects the work it exists to steer. Mapping row N13 and RULINGS ("HELP_HUMAN checked … the stage-gate source") carry the same reading.

**Fix.** Replace the bullet with a pointer to the ruled record, for example: "Piping's stage gate is the target stage and the exit criteria recorded in `execution/_Coordination/_COORDINATION.md` under "Current Target Stage". Assess against those criteria, not against a `docs/PRD.md` §24 milestone read by its label; only the owner's approved update advances the target." Note the correction in a RULINGS addendum (N13).

### MINOR-1: "It records each adopted amendment" is not true of SCA-010

**Evidence.** LOOP_INIT lines 54–57 say the decomposition "records each adopted amendment, and `execution/_ScopeChange/_LATEST.md` selects the accepted scope change." The decomposition's revision notes record SCA-001 to SCA-009 and SCA-011 (v0.4–v0.13) and D-77 (v0.14). SCA-010 (accepted by the owner on 2026-09-18, PRD-only, "accepted, not yet executed") is not recorded there; its `Impact_Assessment.md` says "revision 0.12 stands". `_ScopeChange/_LATEST.md` selects "only the accepted SCA-011 amendment" and leaves earlier snapshots as historical authority.

**Fix.** "Its revision notes record each amendment that changed it; `execution/_ScopeChange/` holds every amendment, and its `_LATEST.md` selects the latest accepted one."

### MINOR-2: The manifest's M6 record names the changed instruction files as notice routes, and its rationale omits the workflow sentence RULINGS says it records

**Evidence.**
- `m6_notice.disposition: routed` with `routed_to` = `P/loop/LOOP_INIT.md` and `init/dev-loop-init-prompt.md`. The validator's schema documents `routed_to` as "notice paths", and of the 153 manifests this is the only one whose routes are not `NOTICE_*.md` files. Piping-only precedents route a notice to Piping's own `_Coordination` (PIPING-LOOP-WORKGRAPH-20260919, PIPING-REMAINING-RETIREMENT-20260923); an own-loop change with no other affected loop has also used `none-required` (APP-V4-LOOP-ENTRY-20260928). No notice was written, so "routed" is not truthful as recorded.
- RULINGS ruling 5: "Section C, the manual citations and construct's introduction sentence, is outside this tranche. The manifest's notice rationale records it." The rationale records only the AUM citations. `workflows/construct-local-work-graph/WORKFLOW.md` line 11 ("`LOOP_INIT.md` supplies the evergreen procedure for recovering, constructing and following its graph") becomes untrue for Piping with this change, as it already is for App v4 (CONSISTENCY_EDITS C3).
- G4 passes in every mode; this is a truthfulness finding, not a validator failure.

**Fix.** Either set `disposition: none-required` with `routed_to: []`, or write a Piping notice and route it. In either case add one rationale sentence that C3 needs a `create-workflow` revision of construct's introduction.

### MINOR-3: The product-PR gate set and Git rules no longer have a live consolidated statement, although the new ruling says they live in the rulings

**Evidence.**
- The old handoff's "Rules that continue", on main, held "Gates before a main merge" (complete-diff review with same-reviewer confirmation; hosted CI and the full-SHA dispatch; the 40-manifest suite before the freeze; an exact-final-head Mac DEC-025 compared per test against a fresh main baseline; GEN-8; Pass B with confirmation and T9/both-entry for D1 call-graph changes) and the Git rules (TASKs make no Git writes; never rebase or force-push; product PRs `--merge --match-head-commit`; no auto-merge; check main is unmoved). The PR rewrites the handoff without them.
- RR "Owner direction: proportionate CI…" says "**The full gate set stays** for PRs that change source, tests, CI, tools or the portability policy". The set it refers to is enumerated only in that old handoff text. RR's other gate statements are unit-specific (U9/#1082; "I61's U8 plan ruled…", item 7, for U8 only).
- The new steer spells out the records-only PR gates but not the product-PR gates, although S-I1's PR and the T6 slice's PR come first. `BRIEFS/I73_S_I1.md` gives no PR gates. The old handoff's "S-I1 … needs no D1 gates, but does need DEC-025 and hosted CI" is now only in Git history. Project `AGENTS.md` keeps review, the DEC-025 sweep and required CI; the T3-specific parts (full-SHA dispatch, per-test comparison with a fresh main baseline, GEN-8 on product PRs, carry-over by ruling, merge method) have no live consolidated home.
- RR "Owner direction: piping LOOP_INIT in the binding form…" says the handoff "no longer restates the loop, the gates or the rules, which live in the workflows, project `AGENTS.md`, LOOP_INIT and these rulings."

**Fix.** Append a short RR ruling that restates the product-PR gate set and the Git/merge rules, with their bases (RR is append-only, so append). List it under the WG section's "T3 rulings in force", and add one steer bullet pointing to it.

### NOTEs

- **NOTE-1: The PR tree is not NUM's tree; it is NUM's plus five App v4 files from main.** `git diff 8225f8f2a2 605adf726d` shows only the five files of #1090 (`decision_view.rs`, `record_relations.rs` ×2, two APP-V4-GROUP-A records). NUM last absorbed main at `928145450a` (09:03 −06:00); #1090 merged at 09:23. The PR's delta from main is exactly the six instruction paths plus `P/execution/`, and the PR equals NUM on every path of that delta. The construction is right, but the dispatch's and brief's premise that the trees are equal is not. The WG "Position" ("Its maintained source equals main's") and steer item 1 have been stale since #1090. Steer step 4 ("whether main moved … absorb it into NUM first") catches this; "equalled main's at its last absorb" would stay true.
- **NOTE-2: Main has moved again,** to `01809013ae` (#1091). `gh api …/compare` lists 35 files, all under `projects/chirality-app-v4/`, disjoint from the PR, and the PR remains MERGEABLE. This meets the premise of T3's carry-over rule ("RV100 passes #1088 at H…": another project's directory only; nothing in `P/`, `tools/`, `.github/`, the policy or root build files). The rule also needs GEN-8 on the local combination, which I did not run, because building the combination needs a fetch.
- **NOTE-3: Ruling 3 is sound.** "If you are unsure whether a section matters, read it." keeps the reading decision with the agent, as the owner directed ("the agent decides when to visit it"). It removes the tension with Root `AGENTS.md` ("uncertainty alone does not require an extra prompt"), and "Read the section, not the chapter" bounds it. App v4's LOOP_INIT still says "ask the human", so the shared paragraph now differs between the two loops. Align App v4 at its next instruction change, or take mapping O1 (an AUM home) at the next manual revision.
- **NOTE-4: The LOOP_RECEIPTS statement is accurate.** The last entry is Receipt-162, and the 2026-09-23 notice says the ledger "remains historical and … is not appended by this method". Two residues remain. The ledger's own header still says "Append-only", and Receipt-162 says "Receipt-161 remains reserved to the unrelated unmerged continuation" (branch `codex/swbpipe-continuation-20260919`, paused 2026-09-21). If that continuation resumes, it may not append; its receipt goes to its own run.
- **NOTE-5: Some three-part-test residue remains,** in the same shape as App v4's accepted file.
  - The opening says the file "states only what is specific to Piping and stated in none of them", which is stronger than App v4's wording, but several clauses restate other layers:
    - "Record what you read … as Root `AGENTS.md` requires";
    - the MEMORY clause's first half (AUM §13);
    - "`bounded-reconciliation`, for the closeout comparisons" (construct §3);
    - "through WORKING_ITEMS" (AUM §13);
    - "Instructions … govern; the manuals explain" (the alignment-manual README).
  - The `WORKING_ROOT` sentence repeats project `AGENTS.md`.
  - "When to read further" is general by design (ruling 6).
  - Dropping "and stated in none of them" would make the self-description true. Alternatively, trim the restatements.
- **NOTE-6: Some stale statements are left out correctly, but nothing routes them for correction.**
  - Section B is correctly left out. B1–B3 were stale before this change (since 2026-09-19/23).
  - I found one more of the same kind: `P/docs/contributor_guide/index.md` row 8, "`loop/LOOP_INIT.md`, its selected current work graph" (written 2026-09-22, stale since the evergreen change).
  - Section C is correctly out of scope: manual authorship stays with the owner, and workflow revisions need `create-workflow`.
  - B is recorded only in this run's records. A Task Management intake or the next Piping instruction tranche would keep it from being lost.
- **NOTE-7: Some host details in the handoff need a check before the next session.**
  - "with no swap": T3's own `OPERATING_NOTES_2026-09-30.md` §4 says "no swap partition; macOS showed about 1 GiB of dynamic swap". `sysctl vm.swapusage` now shows 1024 MB total, about 91 MB used.
  - "Worktrees: Only those two", and the steer's check "the worktrees are `numerics` and `sweep-skewpin`": `WT/loop-init-pr` is a third registered worktree. ROOT should remove it after the merge.
  - **Host note from this review:** the permitted `test_ci_e2e_plan.py` run built two small crates. It left gitignored `target/` folders, about 79 MB, under `WT/loop-init-pr/P/core/serialization/canonical_json/` and `WT/loop-init-pr/P/core/units/`. My removal was refused by the host's permission check, so they go when the worktree is removed.
  - A few host-table imperatives duplicate the steer ("It must run during any build", "Never pruned without the owner"). They are tolerable as machine-local notes.
- **NOTE-8: Small gaps in the WG section and the steer.**
  - **Owner decisions.** The WG's "Owner decisions in force" omits the 2026-10-05 direction that all T3 scratch lives in `WT/scratch`. `T3/IMPLEMENTATION/HANDOFF_2026-10-05/CLEANUP.md` step 0 and `BRIEFS/U8_COMMON.md` carry it, so it is not lost.
  - **Bases of the steer's practices.** The steer says the practices' "basis is in the T3 rulings the graph lists". For "Product PRs are cut compactly from main, with maintained-source equality", the basis is in rulings the graph does not list ("U9 planned and ruled: the D1 milestone PR", decision 2, and RR:6921). For "verify every return yourself", the basis is practice recorded throughout RR. "In T3's rulings" would be exact.
  - **T3 row.** The row's historical 2026-10-03 tail still says the handoff and ROOT_CURRENT "own details and owner decisions". This is acceptable as history, now that ROOT_CURRENT is a retirement pointer.
- **NOTE-9: A4 is acceptable shorthand.** It says "the project `AGENTS.md` holds its fences". Project `AGENTS.md` binds F-PIP-1 to F-PIP-4, and their definitions are in `loop/WORKPLAN_2026-07-18b_piping_loop.md`.

## 1. The new `P/loop/LOOP_INIT.md`

**The three-part test.** I read each sentence against the owner's test in `V4RUN/OWNER_DECISIONS.md` and `RUN/OWNER_DECISIONS.md`.
- **The sentences pass:** entry steps 1–3, the Methods bindings and permissions, the record pointers, the MEMORY creation grant and the LOOP_RECEIPTS convention.
- **Residue:** NOTE-5, which is App v4's accepted pattern.
- **The stage-gate bullet** is specific and instructs, but is inaccurate (MAJOR-1).
- **Owner constraints:** no routers, no edition pin (editions come from the README), and no new record type.
- **Entry step 2** ("Read project `AGENTS.md` in full before you write anything") is justified. Piping's init prompt does not read project `AGENTS.md`, the entry map gives only the AUM headings, and the write fences apply before the first write.

**No load-bearing rule is lost.**
- **Class (a) quotes.** I re-ran the mapping's destination quotes with a script, `WT/scratch/lr_loopinit_01/quotecheck.py`, which collapses whitespace and attributes each quote to the source label before it, against the files at the head.
  - **Result:** 123 class-(a) quotes, from 71 rows, were found verbatim in their attributed sources: construct 29, AUM 28, BR 20, FB 17, project `AGENTS.md` 14 (at the head, after A1–A3), Root `AGENTS.md` 7, TM 5, SPEC 2 and the init prompt 1.
  - **Unmatched by the script:** 24 strings. All are parser artifacts: draft section names, owner quotes without a label, and pairs mis-split by nested quotes in rows 8, 9 and 29. I checked the five record-pointer quotes in those rows by hand with `grep -F`, and all were found.
- **Substance.** The rows I read in substance, not just words, carry their rules: 22, 26, 47, 53, 56, 59, 62–67, 80, 83, 89 and 92.
- **Class (b), every row** (1, 2, 7–11, 13–15, 17) lands in the draft.
- **Class (d), every row** is correctly retired:
  - row 4, by the owner's reading;
  - row 29, because `_DAG/_LATEST.md` names "approved_active_graph_authority";
  - row 36, which goes with the removed steps;
  - row 71, which is editorial.
- **The MEMORY creation grant** (ruling 1) is safe today: the five deliverables without `MEMORY.md` (DEL-04-07, DEL-07-09, DEL-07-11, DEL-07-12, DEL-16-06) are all OPEN.

**Paths and names.**
- **Paths.** Every path exists at the head:
  - `docs/PRD.md`;
  - `_Decomposition/SOFTWARE_DECOMP.md` and its `_LATEST.md` (revision 0.14);
  - `_ScopeChange/_LATEST.md`;
  - `_DAG/_LATEST.md`;
  - 106 deliverable folders: 97 `ScopeOfWork.md`, 8 PKG-00 `ArchitectureBasis.md`, DEL-07-09 bespoke; 106 `_DEPENDENCIES.md`, 98 `Dependencies.csv`, 106 `_STATUS.md`, 101 `MEMORY.md`;
  - `_DECISIONS/_REGISTER.md`, whose header says how rulings are recorded;
  - 74 `NOTICE_*.md`;
  - `software-workflow.json`, and project `AGENTS.md`'s "## Software checks";
  - `_TaskManagement/REGISTER.csv`;
  - `WorkGraphs/`;
  - `loop/LOOP_RECEIPTS.md`;
  - COORD;
  - `{REPO_ROOT}/docs/alignment-manual/README.md`.
- **Workflows.** All eight workflow names are in `workflows/index.json` `methods` as `kind: workflow`, `source: bundled`, `sourceRootId: chirality-root`.
- **Machine-local content and current state.** None. "Receipt 162" names where a closed ledger ends, and "PKG-00" names a structure.

**Item by item.**
- **The stage-gate constraint** is not accurate (MAJOR-1).
- **The LOOP_RECEIPTS statement** is accurate (NOTE-4).
- **Ruling 3** is sound (NOTE-3).
- **The record pointers** are accurate apart from MINOR-1.

## 2. Consistency edits A1–A7

**Each edit is minimal and true.**
- **The diff matches the plan.** The PR's diff against main changes exactly the "before" text of each edit into its "after" text. Nothing else changes in those files.
- **A1–A3** (project `AGENTS.md`) describe LOOP_INIT as binding, not owning. The unchanged lines 65–67 and 87–88 stay true.
- **A4** (the Root launcher §5 prose) is true (NOTE-9). The tagged block is unchanged, and `validate_instruction_entrypoints.py` passes, so it still byte-matches `P/init/dev-loop-init-prompt.md`.
- **A5** (COORD header), **A6** (the DEL-11-05 banner) and **A7** (the newest WORKPLAN's navigation) are true. A7 also removes the clause "with LOOP_INIT pointing to the selected graph", stale since 2026-09-23. The owner-adopted retirement text is unchanged.

**Nothing else in live instructions becomes untrue,** apart from what is recorded already.
- **What I searched:** `LOOP_INIT` in `P/` outside `execution/`, Root `init/`, `docs/SPEC.md`, `workflows/` and `agents/`.
- **Still true:**
  - `P/init/dev-loop-init-prompt.md` and both `taskmgmt-init-prompt.md` files;
  - the Root launcher catalog;
  - SPEC line 998 ("LOOP_INIT remains evergreen…");
  - the work-graph template.
- **Becomes untrue:** construct's introduction sentence (C3; MINOR-2).
- **Already stale:** B1–B3 and the contributor guide's row 8 (NOTE-6). `AGENTIC_DEVELOPMENT_WORKFLOW.md` line 51's table row is old text that its own banner disclaims.
- **The test that reads LOOP_INIT** (`P/tests/test_ci_e2e_plan.py`) uses only the path, and it passes.

**A6: no active concordance run freezes DEL-11-05.**
- DEL-11-05's `_STATUS.md` reads "**Current State:** IN_PROGRESS" (last updated 2026-09-22).
- `RECON_2026-09-21_WHOLE_CORPUS` last changed at `a89b5ddecf` ("Close App and Piping record reconciliation") and `e715b2055c` (the D-74 closeout), both on 2026-09-22. Piping development has continued since then.
- The other concordance runs (`DELIVERABLE_CONCORDANCE_2026-07-11_1305` and three SCOPED/TM runs) are older.
- An earlier instruction tranche (`29decb9fee`) and D-77/D-78 (`b53c0f8c4b`, `b529c22aec`) edited the same file without a MEMORY row. A6 follows that precedent.

**Sections B and C** are correctly left out (NOTE-6). However, ruling 5's claim about the rationale is inexact (MINOR-2).

## 3. The tranche manifest

- **The validator passes,** run in `WT/loop-init-pr` with the Piping venv (logs in `g4_*.log`):
  - **CI mode:** G4 PASS (153 manifests schema-valid).
  - **Diff mode,** `--base 6479bf110a… --head 605adf726d… --tranche PIPING-LOOP-INIT-20261005`: PASS. 47 changed paths, 2 on the instruction surface, covered.
  - **Governed mode,** `--added-manifests-only`: PASS.
  - **INFO only:** the five project paths are over-declaration.
- **Authorization quotes.** "Make appropriate changes to the LOOP_INIT and your own handoff steering instruction ... carry out those actions to get things set up properly." matches `RUN/OWNER_DECISIONS.md`, with the ellipsis eliding the parenthetical and "So don't start the next session, I'll do that, but otherwise". "No routers" and "No don't pin to editions" match `V4RUN/OWNER_DECISIONS.md`.
- **The notice disposition.** The rationale's facts hold. I found no other loop's live instructions or basis records that pin Piping's LOOP_INIT or the Root launcher's §5 paragraph; the other hits are historical records. The recorded disposition and routes are not truthful as recorded (MINOR-2).
- **The review field** names this file.

## 4. T3 records

**The WG section "T3 current route (numerical integrity)" matches T3's records.**
- **Nodes.** U8, SI1, T6S, B0, B1/B6, B2/B3/B4, B7, B8, SI2/F2b/F3 and G10, with their needs, assignments and states, match:
  - the old handoff (main `6479bf110a`);
  - RR "I61's U8 plan ruled…" decisions 1–14;
  - PLAN §§1–3 (`I61/u8_plan_01/PLAN.md`: §2 "The F2a-breadth roadmap", §2.2 "The end of F2a…", §3 "S-I1's readiness", §4 "Main's movement");
  - `BRIEFS/` (U8_COMMON, I68, I69_I70_I71, I72, I73, I74, RV97, RV98 and RV99 all exist).
  - "RR near line 10407" is the D-6 lock residual that RR:11946 cites.
- **Owner-held choices.** All eight match the old handoff.
- **Owner decisions.** The F2a order, the T6 pull-forward, proportionate CI, cleanup, G10 and the earlier T1/D-3/D-6/D-7 match RR and the old handoff (NOTE-8).
- **IDs.** I75 and RV101 are next; RV100 reviewed #1088.
- **Ruling headings.** All seven quoted headings exist verbatim as prefixes of RR headings, at lines 11769, 11898, 12179, 12198, 12111, 12134 and 12096. Each supports the item it is cited for. "Ruled for T3's later freezes: the full 40-manifest suite…" is at RR:11769ff.
- **Routed notes.** They match the old handoff's open items plus RV95 N-6.
- **The anchor** `#t3-current-route-numerical-integrity` resolves.

**The T3 row's status** points to the section.

**The retired `ROOT_CURRENT.md`** is a correct retirement pointer. Every item of the old file (closed, open, next, branches, IDs) is carried by the WG section.

**The ephemeral handoff** is accurate apart from NOTE-7. It no longer restates the loop. MINOR-3 is about what its rewrite removed.

**`HANDOFF_2026-10-05_PROMPT.md`.**
- **The init block is byte-identical** to `P/init/dev-loop-init-prompt.md`, except for the steer. The prefix up to `Steer (this run):` is equal, and the suffix `</init-prompt>\n` is equal; checked byte-wise in Python.
- **The steer is consistent with LOOP_INIT and project `AGENTS.md`.** It names the undertaking and its graph, which completes LOOP_INIT entry step 3. It adds ckw in proportion, as LOOP_INIT's Methods do. It contradicts neither file.
- **Its only stale statement** is "Its maintained source equals main's" (NOTE-1), which its own step 4 corrects.
- **Each listed practice has a basis in RR:**
  - the guard and one cargo job: I61 decisions 1 and 13;
  - TASKs run no DEC-025, native or solver-at-scale jobs: I61 decision 1;
  - `run_dec025.sh` and `ALL-DONE`: "RV100 passes #1088…" N-6;
  - the full suite before a freeze: "DEC-025 on F…";
  - compact product PRs: "U9 planned and ruled…" decision 2, RR:6921;
  - never merging NUM: "A follow-up records-only PR…";
  - records-only PRs: "Owner direction: proportionate CI…", A-1, E-4 and N-1;
  - fresh IDs: I61 "Dispatches prepared…";
  - owner-held choices: I61 decisions 9 and 12;
  - cleanup: "Handoff prepared…" and "Stray scratch gathered…".
  
  Some of these bases are outside the graph's list (NOTE-8). The product-PR gate set is missing (MINOR-3).

**The T3 ruling** "Owner direction: piping LOOP_INIT in the binding form; T3's handoff becomes an init steer; ROOT_CURRENT retired" is accurate apart from its claim that the gates and rules live in the rulings (MINOR-3). Its owner quotes match `RUN/OWNER_DECISIONS.md`.

**RR is append-only.** Main's copy (1,042,052 B) is a byte prefix of the PR's (1,047,134 B). The PR appends "#1088 squash-merged…" and the new ruling.

## 5. Publication and portability

- **GEN-8:** `python -m pytest -q -p no:cacheprovider tools/practitioner_harness/test_live_baseline.py -k gen8`.
  - In `WT/loop-init-pr`, a clean Git checkout at `605adf726d`: 1 passed (`gen8.log`).
  - On a clean `git archive` of the head with `CHIRALITY_REQUIRE_LIVE_TESTS=1`: 1 passed (`gen8_archive.log`). This repeat is clean of the build output described in NOTE-7.
- **Machine paths:** none in the 1,808 added lines. The only home-directory strings are the `<user>` placeholder forms quoted inside RV100's records. Living documents use `WT/…` and `<repo>/…`.
- **Credentials and whole-host data:** none found. I scanned the added lines for credential prefixes and key material, process listings, app paths, session IDs and host names. The hits are RV100's own description of its searches, the `Co-Authored-By` trailer, the owner's name in the manifest, and the guard's PID.
- **The entry validator:** `tools/validation/validate_instruction_entrypoints.py` gives "PASS: root instruction entrypoints are canonical".
- **The test that reads LOOP_INIT:** `P/tests/test_ci_e2e_plan.py` gives 41 passed and 21 subtests (NOTE-7 for its build output).
- **Hosted CI on the head:** every check that ran passed, including `harness`, Harness pre-merge, Desktop E2E (source mode) and the App instruction bundle. The cargo, source and accessibility jobs were skipped by coverage selection, as expected for a change with no product code.

## Repair confirmation

Repairs should be confirmed by this reviewer: MAJOR-1, and preferably MINOR-1 to MINOR-3 in the same pass. On a repaired head I would re-check:
- the LOOP_INIT diff and its sha256;
- G4 in diff mode;
- the entry validator;
- GEN-8 on the exact head;
- RR's prefix property, if a ruling is appended.
