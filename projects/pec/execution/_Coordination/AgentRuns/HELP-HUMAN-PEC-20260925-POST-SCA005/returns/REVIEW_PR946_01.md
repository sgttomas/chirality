# Review 01 of PR #946 (D-PEC-96 ruling record), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. Its final report is transcribed verbatim from the host subagent transcript.
- **Reviewed head:** `3ba5fde9b92982d559ad995421b023de5f31cb46`.
- **SHA-256 of the report text below (UTF-8):** `1c21baa61fb3d8e9b6b574ceac6608851660c566ba98b2bd27db7e882877506e`.

## Report (verbatim)

## Review of PR #946 (D-PEC-96 ruling record) at head `3ba5fde9b92982d559ad995421b023de5f31cb46`

**Verdict: CHANGES REQUESTED.** There is one blocking finding. It is a one-line fix in the register row. The ruling record is faithful, its hashes are correct and its grant is not enlarged. The non-blocking notes below are wording or citation issues.

I confirmed the head with `gh pr view 946` (headRefOid `3ba5fde9b…`). The base is `origin/main` `6281273fa`, which is the PR #941 merge. The PR is one commit touching two files: the new ruling record (+82 lines) and one register line (+1/−1). I read only through `git show` and `git archive` into my own scratchpad exports. I did not modify the checkout or switch its branch; it is still on `claude/pec-d96-ruling` and clean. The ruling file's SHA-256 at head is `eac4a1395a27047d3caf40dcb611c9822d4db1757d8944431b5d8d1216efdb17`.

### Blocking finding

**B1. The register row says the proposal is ruled and, in the same row, that it is not.**
- **Where:** `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md:113`, column 6 (Notes).
- **Evidence:** column 4 now reads `RULED A / EFFECTIVE ON MERGE`, but column 6 still says "Revision 4 is published; the proposal is not yet ruled." The ruling text is appended directly after that sentence.
- **Precedent:** when D-PEC-95 was ruled (commit `df8acf4f5`), its row carried no leftover "not yet ruled" text.
- **Fix:** replace that sentence with something like "Revision 4 was published as PR #941 (`6281273fa`) after reviews 01 and 02." Change nothing else in the row.

### Non-blocking findings

1. **COV-083 points to a file that is not on main** (ruling `:80–82`).
   - "SCA-006 audit COV-083" exists only in open PR #943, at `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/Decomp_Coverage_IssueLog.csv:84`.
   - On main, COV-083 finds an unrelated SCA-002 row about DEL-07-03 (`COV_SCA002_PRECHANGE_2026-07-25_1040`).
   - **Fix:** give the audit folder and note that it is in unmerged PR #943, or drop the citation.
2. **The ruling misdescribes where the stale sentences go** (`:80–82`).
   - The ruling says they "wait for the next PEC scope change (work-graph S2 note…)".
   - The graph's S2 row (`WORK_GRAPH.md:62`) says they are corrected under the DEL-01-06 rebuild and its governing packet.
   - The proposal (`:96`, `:596`) says "go to S2 and to a later scope change".
   - **Fix:** follow the proposal: S2 for the rebuild, and a later scope change for the decomposition text. The proposal says "a later", not "the next".
3. **The models answer reaches one role further than the proposal** (ruling `:55`).
   - The ruling gives the defaults to "manager, runner and verifier".
   - The proposal (`:575`) gives Opus 5.5 `high` only to "the manager and the verifier". The optional runner TASK (`:560`) has no model stated.
   - The effect is harmless and sits under the "HELP_HUMAN interpretation" heading. Still, "defaults" does not literally cover the runner. Say "manager and verifier (and any runner TASK)", or drop "runner".
4. **The limits list is a subset** (`:75–78`).
   - "All D-PEC-96 limits apply unchanged" makes the list complete by reference.
   - But the bullets after the colon leave out several of the proposal's limits (`:590–604`): no instruction or `projects/pec/AGENTS.md` change, no `_CONTEXT.md`, `_REFERENCES.md` or dependency file, no other registry row, no consumer, parser or fixture suite, no change to `software-workflow.json`, CI, Root or tier-0, no duty on another loop, no readiness or reliance claim, and reliance holds survive.
   - "No … register change" is also ambiguous, since this PR writes `_REGISTER.md`. D-PEC-95 said "decomposition-register-content".
   - **Fix:** write "including:" and say "decomposition-register".
5. **A section from the D-PEC-95 format is missing.**
   - `D-PEC-95_RULING_2026-09-25.md:108–114` has "## Publication and receipt". It authorizes the decision record and the register-row update, calls the graph and receipt ordinary loop records, and routes STATUS/README through D-PEC-88.
   - D-PEC-96 has no such section, and nowhere in the record is the deferred graph update stated.
   - Everything else follows the D-PEC-95 format: heading, owner and recorder line, verbatim block, status line, selected instrument, the three-column resolution table, grant and limits.
6. **Small omissions and imprecisions.**
   - `:34` names `mutate_d96.py` without its prep-folder path.
   - `:68` leaves out the template's pinned hash `5a9564f4…6a5a`. I checked it on main and it matches.
   - Question 3 (`:52`) leaves out "each profile at most once per row" and "kept as a guard". Both are carried by reference.
7. **The supersession statement** (`:51`) is correct and bounded, but "supersedes" is a strong word.
   - The proposal itself asked the owner to rule the departure from §B6 and SCA005-CP1-Q8 (a) as this question (`:613–620`), and "migrated" answers it.
   - The statement is limited to "PEC's registry row". It does not extend to R-05 or FX-PEC-0 (carried to X1) or to the decomposition text.
   - Main's `Decision_Log.md:27` (Q8 (a)) stays unannotated, which fits the limits.
   - Optional: "departs from, as the foreseen own ruling" is closer to the proposal's wording, since the proposal never uses "supersede".

### Question 3: leaving out the graph update

This is acceptable. It does not make anything authoritative false, and the register and ruling are what govern. There are two conditions.
- **Already stale on main.** Since #941 merged, the graph's G1 row (`WORK_GRAPH.md:65`, "ACTIVE … under review … before the owner's ruling") is out of date. So are Order (`:81`), Next work (`:130`) and "Local or unmerged work: … ninth PR" (`:135`). `docs/STATUS.md:232–235` ("proposed as `D-PEC-96` … The ruling follows it") is also out of date. These are execution-state and status lines, not authority, and the grant's preconditions depend only on the ruling and the register row.
- **Real risk: PR #944 (head `47bf0c1c7`).** It writes "BLOCKED — awaiting the owner's ruling on `D-PEC-96` revision 4" and "Blocked on the owner: G1" into the graph, and "awaits the owner's ruling" into `docs/STATUS.md`. #946 does not touch those files, so Git will not report a conflict. If #944 merges after #946 as written, it puts newly false text on main.
  - **Condition 1:** the follow-up must correct the graph and `docs/STATUS.md`. The PR body mentions only the graph.
  - **Condition 2:** either #944 is refreshed before it merges, or the follow-up lands right after it.
- **PR #943 also needs a refresh.** Its COV-083 row says "No accepted decision has yet changed the basis … still needs its ruling". That becomes stale once this PR merges.

### What I verified

- **Quote:** "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults" appears byte-exact in the ruling (`:9`) and in the register row, once each. The mention of "approve hunk" (`:11`) is recorded as `Decision_Log.md` row SCA006-G2-A1 in open PR #943.
- **Hashes (`shasum -a 256`, main equals head):**
  - proposal `4506597b…5180e`
  - `apply_d96.py` `80725b4f…bbf3`
  - `mutate_d96.py` `57c2f031…26f0`
  - `MEMORY_TEMPLATE.md` `5a9564f4…6a5a`
- **Resolutions:** each of the six follows the proposal's questions (`:612–636`) in order.
  - Question 2 matches the proposal's migrated row and its bases.
  - The prepared `loops.json` postimage (`fd342b4f…`) carries exactly those three profiles, states and bases.
- **Grant:** it matches the proposal and is not enlarged.
  - One run of the script, copied into the same run root as the proposal's `:562`.
  - The proposal's finite verification, a fresh verifier, and `MEMORY.md` from the template (`:570`).
  - Binding `mutate_d96.py` by hash tightens the grant rather than enlarging it.
  - The claim that the script re-checks preimages and must-remain files matches the proposal's `:501–508`.
- **Other statements in the record:**
  - PR #941 merged as `6281273fa`. Review 01 was CHANGES REQUESTED on records only, with both findings repaired. Review 02 passed at `5fae6a084`.
  - The N1 and N2 descriptions match `REVIEW_PR941_01.md:31–37`.
  - `D-PEC-96_AMEND_DIRECTION_2026-09-26.md` holds the owner's full sentence.
- **Register:** only line 113 differs out of 115. It has 6 columns before and after, and the hashes in it are correct.
- **Hygiene:**
  - `git diff --check origin/main...HEAD` is clean.
  - In a Git-backed export of the head:
    - The receipts validator reports VALID, exit 0.
    - `harness.py self-check` exits 0.
    - The strict decomposition validator reports 0 errors and 26 XRG-013 warnings, exit 1. The warnings are the same at base; they come from D-GOV-48 in PR #942, not from this PR.
  - PR CI: every check that ran passed.
  - Nothing in the record prompts about CHECKING, and `:80` says so explicitly.

Key paths:
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md

## HELP_HUMAN disposition

The verdict was CHANGES REQUESTED, on B1. It is repaired in the next commit: the register row's leftover "not yet ruled" sentence is replaced.

The non-blocking findings are also repaired:
- The COV-083 citation now names the folder in open PR #943.
- The route follows the proposal: S2 and a later scope change.
- The models answer now covers the manager and the verifier, and any runner TASK.
- The limits now say "including" and "decomposition-register", with the omitted limits added.
- A "Publication and receipt" section now states the deferred graph and STATUS update.
- The paths and template hash are added.
- "Supersedes" is replaced by "departs from … only".

Question 3 is conditions 1 and 2: HELP_HUMAN refreshes PR #944's graph and STATUS lines before it merges, so that they record the ruling.
