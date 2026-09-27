# Review 01 of PR #987, transcribed

- **Reviewer:** a fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high) dispatched by HELP_HUMAN. It authored nothing in the PR. Its final report is transcribed from the host subagent transcript (verbatim apart from any disclosed whitespace normalization).
- **Reviewed head:** `4261a8d3d26502cbcaf8eeb2dbfe2a23c5abd89e`. The repairs listed under Disposition, this file and the `SHA256SUMS` update follow that head.
- **SHA-256 of the report text below (UTF-8; the report text between the blank line after "## Report (verbatim)" and the blank line before the final "## Disposition", with no trailing newline):** `445e8388cc9719bcbafb3729115a23a45d48c55f831f3c26aeab9e1bb1af1938`.

## Report (verbatim)

**Verdict: PASS WITH NOTES.** I found no blocking and no non-blocking findings, only four notes. Nothing was modified. I made one `mktemp -d` directory (`rev987.lYGBBa`) inside the session scratchpad and deleted only that. The worktree is clean. I ran no checkout or switch and no git writes.

**What was reviewed:** PR #987 at head `4261a8d3d26502cbcaf8eeb2dbfe2a23c5abd89e`. It is open, mergeable and its CI checks pass. Its merge base is `e548d4cfa`. Current `origin/main` is `1c281c8ba` (PR #985, Root tool fixes only; no `projects/pec`, PRD or `_DomainEngines` file changed since `e548d4cfa`).

## 1. The check run, reproduced at current main
I ran `run_k2_checks.sh` from the PR head's prep folder against `origin/main` `1c281c8ba`, with `TMPDIR` set to my own directory. Result: **OVERALL PASS, exit 0**. Every line passes:
- reliance preflight: `ALLOW` ×7;
- act A: check-only 0, apply 0, rerun refuses with 1; containment is exactly 2 new `ScopeOfWork.md`;
- validator: `PASS format=SOW_V1` ×2;
- checklists: 17 = 17 AC and 19 = 19 AC, byte-identical on rerun (`2227dbeb…9641`, `8e07ff3e…ba30`);
- boundary owners: 0 unresolved, 0 NOT_CHECKABLE;
- quotes 137/137, state claims 482/482, cited IDs 0/0, old S2 text stale=0 (43 current);
- strict registers: exit 1, 0 errors, 26 `XRG-013`, identical before A, after A and after C8; harness, receipts and closure identical at the same three points;
- add-on C8: 0/0/1, containment 3 files;
- whitespace clean; fault injection 19/19.

Every file I produced matches the committed `evidence/run_main/*` byte for byte, apart from temp paths and the basis-commit line.

**Pins, recomputed with `git show | shasum -a 256`:** all 17 pins in `apply_k2.py` hold at `1c281c8ba`, `e548d4cfa` and `125cfacc1`. At `189f205ff` the first five and `pec.yaml` match; the deliverable folders did not exist yet, as the draft says. Both targets are absent at current main. The register's last row is still `D-PEC-101`.

**Hashes:** `shasum -a 256 -c SHA256SUMS` passes for all 66 entries. The draft `3acc37ac…e268`, the candidates `aecc5131…0826` and `c7743ee2…6633`, `apply_k2.py` `b10461fa…257a`, `apply_k2_c8.py` `093130c8…84e9` and the brief `5fcc3ef8…e133` all match. The method and tool hashes (`WORKFLOW.md`, standard, `index.json`, the four scope-of-work tools, holds file, preflight script, `MEMORY_TEMPLATE.md`, `write_status.sh`) also match at current main.

## 2. Substance of both candidates (MODE=VERIFY)
- **Grounding.** I checked each against the live revision 1.6 registers:
  - The `SOW-099` and `SOW-100` ledger rows, the `DEL-08-06` and `DEL-10-13` Deliverables rows and their ContextBudgetQA rows are quoted exactly.
  - The phase of every deliverable named is right: all P1 except DEL-08-06 at P3.
  - The objective warrants are no stronger than the sources: `SOFTWARE_DECOMP.md` §3 line 347 ("instruments: … SOW-100"), DL-21 and the §8 text.
  - The PRD v2.4 loci are verbatim: PEC-API-007 (line 385), the §8 Agents bullet and `agent` class (lines 298–315), the §12 gate paragraph (lines 451–461) and §16.6 (line 624).
- **Upstream contracts.** The SHA prefixes of DEL-08-01, 08-03, 04-01, 03-04, 04-03, 04-05 and 10-02 match. None contains `agent`, `SOW-097` or "reliance-advertisement". The `Propagation_Plan.md` §B4 classes for these are as stated.
- **Other state claims.** DEL-08-06 folder: six files, six register rows, `schema.json` `0a4e4273…` with no `agent` term, `pec.yaml` declaring two tools. The twelve DEL-10-13 predecessors are `INITIALIZED` at `125cfacc1`.
- **Open items stay open.** OI-006 is TBD-002; the K3 profile content is TBD-007 in DEL-08-06; the C-08 question is CON-001 in DEL-10-13; the DEL-02-07 edge is CON-002 in DEL-10-13; the release process is CON-004 in DEL-10-13. None is decided.
- **No reliance claim.** The only "reliance is available" text in either candidate is the quoted PEC-K-03 gating sentence (DEL-08-06:127, DEL-10-13:120). DEL-08-06 REQ-009 and DEL-10-13 REQ-012 forbid asserting reliance.
- **CHECKING.** Neither candidate mentions it. The draft names it only at line 72 (an observation) and line 422 (a limit). DEL-08-02, an upstream of DEL-08-06, is at `CHECKING`; correctly, nothing prompts about it (draft:160).

## 3. The draft
- **Options:** A is recommended (draft:188); the add-ons are independently selectable.
- **Exact grant** (draft:205–227): the pre- and postimages match the files.
- **Add-on S** is offered, not assumed (draft:19, 435–438). I regenerated both postimages with `write_status.sh` (`0bf835f5…`) on a current-main export dated 2026-09-26, exit 0 ×2. The results are byte-identical: `75366b6b…a127` and `3771d526…e567`.
- **Add-on M** (draft:249–257) uses the template hash as stated.
- **Add-on C8** (draft:21, 259–285, 440–443):
  - It says plainly that it writes one line in the human-owned Tracking Mode section, citing SPEC.md:448 and :460 verbatim, and that it applies only on the owner's explicit selection. It says the contracts stay true either way.
  - The preimage at current main is `5087e581…`. The postimage diff is exactly the one tabled line after the Notes bullet.
  - No tool reads C-08 annotations, and the C8 checks show no output change.
- **Also complete:** ordering rules, verification table, rollback, limits, owner questions and the provisional-number note (draft:3, 285).

## 4. Findings for the owner
All five are accurately stated:
- **DEL-08-06 CON-002** (draft:176): stated as the source-and-tests question for K3.
- **Ordering against S4** (draft:177–180): DEL-08-01 lacks the `agent` class and DEL-04-03 lacks SOW-097 at current main.
- **Possible dependency amends** (draft:181): these match D-PEC-101 findings 2 and 3 verbatim.
- **DEL-10-13 CON-004** (draft:182): accurate.
- **DEL-10-02 C-08 wording** (draft:183): the contract says "unconfirmed" at line 295, while its `_DEPENDENCIES.md` line 22 says "owner-confirmed at D-PEC-62 ruling".

## 5. Verdict dispositions and containment
- I checked every disposition in verdicts 01–05 against the final bytes, and each is true. Examples:
  - B-1: REQ-005 is limited to cases with no API response.
  - The quote-file change is Q48.
  - NB-A: "admits a tool definition".
  - `SHA256SUMS` now exists.
  - Recorded, not changed, as stated: verdict 01 N-4/N-6/N-7, verdict 04 note 7, verdict 05 note 2.
- **Containment:** `git diff --name-status origin/main...HEAD` shows 69 added files. They are the 67 prep-folder files (66 plus `SHA256SUMS`), `briefs/K2P_FIRST_SOWS_PROPOSAL.md` and `returns/K2P_FIRST_SOWS_PROPOSAL.md`. Nothing else.
- `git diff --check origin/main...HEAD` is clean (exit 0).

## Notes
1. **Wording tension between Limits and C8** (draft:424 against draft:259–263, 440–443). Limits says a ruling selecting "A with any of S, M or C8 … grants none of … a resolution of any `CON` item". But selecting C8 is the owner answering exactly what DEL-10-13 CON-001 leaves open. The contract stays true, because CON-001 is anchored at `125cfacc1`. Suggest "other than the owner's own C-08 classification if C8 is selected" when HELP_HUMAN publishes.
2. **Source-state rechecks stop at `e548d4cfa`** (draft:43; return:63). Main is now `1c281c8ba`. I confirmed that nothing pinned changed there and that every check reproduces, so the recheck line can be updated when the packet is published.
3. **DEL-10-13 REQ-010** (candidate:146) says "no field … can hold … prose copied from the evidence". Given the free-text reason field, that is absolute. Verdict 04 note 7 recorded it without change; it is carried, not new.
4. **DEL-10-13 REQ-005 composes only the suites that its own `Dependencies.csv` names** at the candidate's commit (candidate:141, CON-002). So the owner's DEL-02-07 amend decides whether that suite joins the gate. The draft's Finding 4 frames it as a register amend, which is accurate, but the owner may want to know it changes what the gate checks.

## Relevant paths
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/DRAFT_D-PEC-103_first_sows_del_08_06_10_13_proposal.md` (read at the PR head)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/apply_k2.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/apply_k2_c8.py`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/run_k2_checks.sh`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/K2P_FIRST_SOWS_PROPOSAL.md`

These worktree paths are where the PR adds the files. The files are not checked out in this worktree; I read them from the PR head through `git archive`.

## Disposition (HELP_HUMAN)

Verdict PASS WITH NOTES; no blocking or non-blocking findings. Dispositions of the four notes:

- **Note 1 (Limits against C8): repaired.** The Limits bullet in the draft now says that add-on C8 is the one exception: if the owner selects it, the owner's own C-08 classification of DEL-10-13 answers the question DEL-10-13 CON-001 leaves open, and the candidate text stays as written because CON-001 is anchored at `125cfacc1`.
- **Note 2 (recheck stops at `e548d4cfa`): repaired.** The draft's source-state bullet list now adds a recheck at `1c281c8ba` (PR #985). It names the Root tool files changed since `e548d4cfa`, states that none is pinned and no `projects/pec`, PRD or `_DomainEngines` file changed, and cites this review's OVERALL PASS rerun.
- **Note 3 (DEL-10-13 REQ-010 absolute wording): carried, not changed.** Verdict 04 note 7 already recorded it. The candidate is not edited in this PR.
- **Note 4 (REQ-005 composes only the suites in its own `Dependencies.csv`): carried to the owner.** HELP_HUMAN will state it with the D-PEC-103 questions: a DEL-10-13 → DEL-02-07 amend would change what the gate checks, not only the register.

After both repairs the draft is `d761be8644416f6cc047fd05df51931a1ee5d7cd9620b7f9b03676e338eed87e` (was `3acc37ac…e268`), and `SHA256SUMS` is updated to match; all its entries pass `shasum -c`. No candidate, act script, check script or evidence file changed. The manager's return keeps the preparation-time draft hash as a historical record. The repair head needs a fresh review before merge.
