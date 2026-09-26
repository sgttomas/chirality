# Review 02 of PR #919 (work graph), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It cannot write, so HELP_HUMAN transcribed its final report verbatim from the host subagent transcript.
- **Reviewed head:** `ae4ddc447f4014681a5eaf910443c707a350fc24`. This file is the only addition after that head.
- **SHA-256 of the report text below (UTF-8):** `b9d576c0a1ae7854e551e90d176e068baea014e6e967ec27a1ea1012545e2042`.

## Report (verbatim)

**Verdict: PASS.** Nothing blocks. B1 and NB1–NB7 are repaired, and the review transcription is byte-faithful. I found seven non-blocking issues, listed below; the HELP_HUMAN graph maintainer can fix them in graph maintenance.

**Head reviewed:** `ae4ddc447f4014681a5eaf910443c707a350fc24`. It matches `gh pr view 919 --json headRefOid`, and the base is `13df8b795e47ab2284018eeefc9d5473d00c232d`. The repair diff `5570fd095..ae4ddc447` touches exactly the three files named in the brief. I read the head with `git archive`, ran the validators in a scratch `--shared` clone at the head, and modified nothing.

**Work graph SHA-256 at head:** `f669ebe53d483419799e5c947ea903996187570e608f3ee2b849030c0ec00f78`

## Blocking
None.

## Non-blocking (ranked)

**1. The S4 "citing PRD §8" candidates are partly wrong.**
- **Where:** `WORK_GRAPH.md` L64. The same list is in HELP_HUMAN's SendMessage addendum to the SCA-006 manager (2026-09-26T01:12:47Z).
- **Wrong entries:** three SOWs match "§8" only because they cite `SOFTWARE_DECOMP.md` §8 (the Context Budget QA section), not PRD §8:
  - DEL-01-01 `ScopeOfWork.md` L90 (CLM-007)
  - DEL-02-03 L104 (CLM-007)
  - DEL-04-03 L146 (CLM-006)
- **Missing entry:** the list omits DEL-08-03 L229 (CLM-009, "`SOW-003`, `§8`"). This is harmless because DEL-08-03 is already a candidate through K-03.
- **Why it matters:** DEL-01-01 and DEL-02-03 are S2 rebuilds, and DEL-02-03 is on the X1 parser path. If either is misclassified as affected, it waits for R3 for no reason. The addendum asks the manager to classify each SOW as AFFECTED or NOT_AFFECTED, so this should correct itself there.
- **Fix:** relabel the three as SOFTWARE_DECOMP §8 hits and mark them expected NOT_AFFECTED.
- **My grep of all 32 SOWs:**
  - K-03: DEL-04-01, 04-02, 08-01, 08-03.
  - Verify-before-rely: DEL-04-01, 04-02, 08-01.
  - Genuine PRD §8 references: DEL-01-05 L66, DEL-04-02 L363, DEL-08-01, DEL-08-03 L229, DEL-08-04 L274.
  - Every true hit is inside the candidate set, so no SOW that quotes K-03 or PRD §8 escapes the gate.

**2. The membership rules for S1/S2 and S4 do not line up.**
- **Where:** L61–L62, L64 and L76.
- **The mismatch:** S1 and S2 exclude "the R1 affected-SOW list", which is fixed at checkpoint 1. S4 is "the set that checkpoint 2 fixes". So:
  - A SOW that R2 adds after S1/S2 have processed it gets reworked before R3, and escapes the gate.
  - A SOW that R2 drops from the R1 list belongs to neither batch.
- **DEL-04-01 has no guaranteed home.** It is a rebuild-class SOW (SCA-005 §B4: A-02, A-22), but it appears only in S4's conditional candidate list and is missing from S2's closed list. If SCA-006 did not name it, its SCA-005 rebuild would have no node. The practical risk is low: the D-PEC-90 proposal, which the ruling selects, names DEL-04-01 CLM-016/AX-007 as a locus at L64.
- **Fix:**
  - State that S1/S2 membership follows the latest accepted SCA-006 set (R1, then R2), and that a SOW dropped at R2 returns to S1/S2.
  - Name DEL-04-01 as a fixed S4 member, citing the D-PEC-90 proposal L64.

**3. R1 writes a fenced path but names no packet.**
- **Where:** L57.
- **Evidence:**
  - R1's scope is `_ScopeChange/SCA-006_<date>/`. `projects/pec/AGENTS.md` §Write Scopes And Fences (about L116–137) makes only `execution/_Coordination/**` writable by default.
  - The graph's own N1 row (L53) treats `_ScopeChange/**` as fenced.
  - L30 says fenced nodes list their owner ruling.
  - R1's Needs column cites only "`D-PEC-90` R-A".
- **Likely basis:** D-PEC-90 grant item 3 ("prepare the exact PRD and `projects/pec/AGENTS.md` amendment as the next PEC scope change once SCA-005 checkpoint 2 is accepted"). This parallels D-PEC-86 authorizing SCA-005's checkpoint-1 package preparation, and the precondition is met by D-PEC-92.
- **Fix:** cite grant item 3 explicitly as the path basis, labelled as HELP_HUMAN's interpretation. This PR itself writes nothing under `_ScopeChange/`.

**4. T1 states its owner basis more firmly than the disposition table does.**
- **Where:** T1 at L68.
- **Evidence:** the row says "Owner basis: checkpoint-2 acceptance of … §B8", while the disposition table in `REVIEW_PR919_01.md` L78 calls it the "candidate owner basis". The UNCERTAIN state and the D-PEC-95 check keep this honest. The quoted B8 text matches `Propagation_Plan.md` L891 exactly.
- **Fix:** say "Candidate owner basis", and cite D-PEC-92 (register L109) as the acceptance.

**5. `D-PEC-95` is used before it is registered.**
- **Where:** L53–56, L68, L75, L88 and L92.
- **Evidence:** the ID is not in `_DECISIONS/_REGISTER.md`. `git log --all -S "D-PEC-95"` finds it only in `ae4ddc447`, so there is no collision.
- **Fix:** reserve the number, since SCA-006 may need its own D-PEC.

**6. S3 and X1 dependencies are slightly out of step with the Order list.**
- S3's Needs (L63: U1; packet; S2 context) omit R1, but Order (L76) places S3 after U1 and R1.
- X1 (L67) needs only S2 and S3. If DEL-02-03 ever moved to S4, X1 would implicitly depend on R3.

**7. Cosmetic: one STATUS line breaks the wrap.** `docs/STATUS.md` L139, the new heading line, runs past the paragraph's hard wrap.

## What I verified

**B1 (SOW sequencing)**
- D-PEC-90 grant item 1 is respected: DEL-04-01 has left S2 and waits for R3 in S4.
- DEL-01-06 sits in S2 "after G1". Its SOW contains no K-03, verify-before-rely or §8 text. Propagation_Plan §B4 records its class as `STALE_REBUILD_REQUIRED … gated on B6`.
- The rebuild class adds up to 8: the six named in S2, plus DEL-01-06 in S2 and DEL-04-01 in S4.
- S1 is defined as the §B4 review class minus the affected set, and S2 moves affected members to S4.
- DEL-04-02 is `current` in §B4 and is now in the deliverable-scope table (L40) and in S4.
- §9 and §12 are cited widely across the SOWs. The D-PEC-90 proposal (L62) says those changes are additive. The structural gate on the R1 affected set covers them.
- The HELP_HUMAN claim that "the SCA-006 manager was told to enumerate" is true: SendMessage to `ac99bcedfa2b85474` at 01:12:47Z.

**NB1–NB7**
- NB1: T1 cites §B8, is UNCERTAIN, and the completion check names an owner disposition. `task-management/WORKFLOW.md` L47 was checked. The D-PEC-95 brief (`scratchpad/closeout/H9_D95_CURRENCY_PROPOSAL.md`, SHA-256 `02fb7370…`) does task T1 with this check (L31).
- NB2: S4, D1 and X1 now name their packet basis. §B7 L884 does say "authored under a v2 packet".
- NB3: the L8 quote is a byte-exact substring of `D-PEC-94` L7, double spaces included. It also matches the owner's chat message in the host transcript.
- NB4: the Route, Active operations, per-node owners and completed-work table are present, per the template fields at L16, L50 and L53–55.
- NB5: R4 now covers Root and App, with Runtime only if checkpoint 2 names it.
- NB6: no node is called P1. Every "P1" is a parser phase, U1 is used consistently, and a naming note is added at L29.
- NB7: the STATUS heading is true. SCA-005 was closed for scope change only on 2026-09-25 (RUN_SUMMARY L340; Handoff_State L291).

**Transcription**
- Lines 9–71 of `REVIEW_PR919_01.md`, taken as UTF-8 without the final newline, hash to `c3633eb7…f725`. That equals the recorded value.
- The text is byte-identical (`cmp`) to the original reviewer's SubagentHandback in subagent transcript `agent-ad738112242331f23.jsonl`.
- The disposition rows are accurate, apart from the "candidate" wording in finding 4.

**New defects checked**
- The dependencies are acyclic.
- No CHECKING prompt: the only mentions are L20, L41 and L95, which says "nothing here prompts".
- No new grants: D-PEC-90's limits and the "a work graph opens no path" rule in AGENTS.md are respected, apart from the interpretive gap in finding 3.
- The D-PEC-88 trace (L104–106) lists both STATUS hunks in the `base..head` diff, and README is unchanged.
- The active-operations claims hold:
  - The D-PEC-95 TASK was launched read-only, writing only a scratch `h9/` folder.
  - The SCA-006 manager is WORKING_ITEMS in its own worktree `agent-ac99bcedfa2b85474`, on local branch `claude/pec-sca006-cp1-package` (not yet on origin). Its brief (`B4_SCA006_CHECKPOINT1.md`, SHA-256 `87612aca…`) sends returns to the stated `returns/` path.

**Hygiene**
- `git diff --check` is clean for both `base..head` and `5570fd095..head`.
- `validate_pec_loop_receipts.py --repo-root .` reports VALID, exit 0.
- `validate_decomposition_registers.py --strict projects/pec/execution` reports 0 errors and 0 warnings, exit 0.
- PR #919 checks pass (harness, pec, Harness pre-merge, Desktop E2E source mode, the three Select coverage jobs); the rest were skipped.

## Files
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR919_01.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/docs/STATUS.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md
- /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md
- The SOWs cited above, under /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md

## HELP_HUMAN disposition

The verdict is PASS, with no blocking findings, so the PR merges at the reviewed content with this transcription added. The non-blocking findings are routed as follows:
- **NB1 and NB2 (the S4 §8 candidates and DEL-04-01 as a fixed member):** sent to the SCA-006 checkpoint-1 manager at once as a brief correction. The graph text will be corrected in the next graph update.
- **NB2 membership rule, NB3 (R1 path basis, D-PEC-90 grant item 3), NB4 ("candidate" basis, D-PEC-92), NB6 (S3/X1 needs) and NB7 (STATUS wrap):** corrected in the next graph update. That update is reviewed with its PR.
- **NB5:** `D-PEC-95` is reserved in `_DECISIONS/_REGISTER.md` when its draft is published.
