# Return — K2P: K2 Scope of Work packet (provisional D-PEC-103)

**From:** WORKING_ITEMS (Type 1), under HELP_HUMAN. Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node K2.

**Brief:** `briefs/K2P_FIRST_SOWS_PROPOSAL.md`, SHA-256 `5fcc3ef847d95743db804263410e360c070d87c0e7d5ff9ed49432c42d8ee133` (hash verified). HELP_HUMAN's later relayed directions of 2026-09-26 are quoted in the draft's Provenance.

**Status:** the packet is prepared and published as a PR. Nothing is applied: no production file is written, and there is no ruling, register row or lifecycle change.

**Worktree and branch:** own worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep`, branch `claude/pec-k2-first-sows-proposal`, cut from `origin/main` `125cfacc1` and merged forward to `e548d4cfa`. The caller's checkout was not modified.

## Deliverables

- **Draft proposal:** `projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/DRAFT_D-PEC-103_first_sows_del_08_06_10_13_proposal.md`, SHA-256 `3acc37acf2062f02c1e41d80de200441e08bfdd5a7333ac438be9bfc8176e268`. It is in the D-PEC-100 format: provenance; findings; options with A recommended; exact grant with pre/postimage hashes; bound act scripts; finite verification; independent verifier; administrative grant; rollback; limits; owner questions.
- **Candidates** (postimages; both new files):
  - DEL-08-06 `…/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md`: `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826`, 249 lines. IDs: OUT 3, CLM 16, REQ 16, AC 17, VER 16, AX 13, TBD 8, CON 4.
  - DEL-10-13 `…/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md`: `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633`, 253 lines. IDs: OUT 2, CLM 16, REQ 18, AC 19, VER 18, AX 12, TBD 7, CON 4.
- **Bound scripts:**
  - `apply_k2.py` (option A, 2 creates, 17 pins): `b10461fa3928b3dd9439ee318c85e7181cc4a4fc2bfd016acf437c7fdbcc257a`.
  - `apply_k2_c8.py` (add-on C8, 1 modify): `093130c8f009e3c4178ba5d86ac6ea6f47bf3e178ac366b64968124f901c84e9`.
- **Add-on postimages:** S (`addons/S/`): DEL-08-06 `_STATUS.md` `75366b6b…a127`, DEL-10-13 `_STATUS.md` `3771d526…e567` (`{D}` = 2026-09-26). C8 (`addons/C8/`): DEL-10-13 `_DEPENDENCIES.md` `609aa807…3693`.
- **Everything else in the prep folder:** the drafter brief, quotes/claims, verifiers, tests, the check runner, `evidence/`, `VERIFIER_VERDICT_01..05.md` and `SHA256SUMS` (tracked prep files).

## Recommended option

**A**: write the two exact contracts in one act, with no lifecycle change. Add-ons:
- **S** (`OPEN → INITIALIZED`) is offered, not assumed, and recommended.
- **M** (`MEMORY.md` at closeout) is recommended.
- **C8** (the owner's C-08 standing-node classification of DEL-10-13) is recommended. It writes one line in the **human-owned** Tracking Mode section of DEL-10-13's `_DEPENDENCIES.md`, so it applies only on the owner's explicit selection. Both contracts are true under either answer.

## Lifecycle answer

- Both deliverables are `OPEN` at `125cfacc1`, `947075c9a` and `e548d4cfa`. Neither is CHECKING or ISSUED.
- The method never touches `_STATUS.md`. A first contract makes a deliverable eligible for `INITIALIZED`, and recording that is a separate act: add-on S, on the `D-PEC-63` §3.2 / `D-PEC-98` pattern.
- Without an answer, no status act is performed. Nothing prompts about CHECKING.

## Part B landing table

None. The brief names no Part B items for K2, and the `D-PEC-99` exhibit assigns none to DEL-08-06 or DEL-10-13.

## Downstream and anchor accounts

- **External anchors:** none of the 285 `Dependencies.csv` rows at `125cfacc1` has either target contract as its `EvidenceFile`. No dependency row goes stale, and no `Dependencies.csv` is written.
- **Old S2 text:** `scan_old_s2_text.py` compares against the prior contracts at `ce934ac33` and the current ones at `125cfacc1`, and finds stale=0. Two reviewers also ran independent whole-text n-gram scans and found 0 hits.
- **Qualified IDs cited from S4/S1 targets** (DEL-08-01, 08-03, 04-01, 04-03, 03-04, 04-05, 10-02): **none**. `check_cited_ids.py` reports `RESULT PASS 0/0`, neither candidate cites the other's local IDs, and the parallel packets have no K2 ID to keep.
- The candidates do read those contracts as observations at `125cfacc1`, anchored by hash, and these stay true after S4/S1 rewrites them:
  - DEL-08-06: the DEL-08-01 access-class sentence (Q34) and the absence of the `agent` class; the SHA prefixes of DEL-08-01, DEL-08-03 and DEL-04-01.
  - DEL-10-13: the SHA prefixes of DEL-03-04, DEL-04-03, DEL-04-05 and DEL-10-02, with absence claims ("reliance-advertisement", "DEL-10-13", "SOW-100", "SOW-097", the pin); DEL-10-02's "No accepted source establishes a release process …" (Q37) and its C-08 "force is unconfirmed" sentence (Q71); two current DEL-02-07 phrases.
  - The draft's table lists these.

## Check results

Final run: `evidence/run_main/SUMMARY.out`, from `run_k2_checks.sh` on the branch head `f096c465c`, which merges `e548d4cfa`. It ran on `git archive` exports with Python 3.13.7. Result: **OVERALL PASS**.
- Reliance preflight: ALLOW ×7.
- Act A: check-only 0, apply 0, rerun refuses 1. Containment: exactly 2 new `ScopeOfWork.md`.
- `validate_scope_of_work.py`: `PASS format=SOW_V1` ×2.
- Checklists: 17 = 17 AC and 19 = 19 AC, reruns byte-identical (`2227dbeb…9641`, `8e07ff3e…ba30`).
- Boundary owners: 0 unresolved, 0 NOT_CHECKABLE. REQ-015 (08-06) and REQ-013/016/017 (10-13) instrument owners are resolved by hand in the draft.
- Quotes 137/137 (two-sided, pinned to `125cfacc1`); state claims 482/482; cited IDs 0/0; old-S2 stale 0.
- Strict registers: exit 1, 0 errors, 26 pre-existing `XRG-013`, identical before A, after A and after C8.
- Harness, receipts and closure: exit 0, non-empty, identical before and after.
- Add-on C8: 0/0/1, containment 3 files, state identical.
- Whitespace clean. Fault injection 19/19 (12 A, 7 C8, including both exit-2 paths).
- **Pins:** all 17 hold at `125cfacc1`, `947075c9a` and `e548d4cfa` (`origin/main` at return).
- **Containment of the PR:** the prep folder, the brief copy and this return. Nothing else.

## Verdicts (all fresh read-only `pec-reviewer` TASKs, Opus 5.5 high)

| Verdict | Scope | Result |
|---|---|---|
| 01 | MODE=VERIFY DEL-08-06 | FAILED: 1 blocking (B-1: the failure behaviour contradicted pass-through). Repaired by the author |
| 02 | MODE=VERIFY DEL-10-13 | PASS WITH NOTES. Repaired by the author |
| 03 | packet review | PASS WITH NOTES. Repaired or recorded |
| 04 | backcheck of all repairs | PASS WITH NOTES, nothing blocks. Wording repairs made by WORKING_ITEMS itself, disclosed in the draft |
| 05 | backcheck of the post-04 edits | PASS WITH NOTES, nothing blocks. Record items repaired; no candidate byte changed after it |

Each file holds the verbatim report and the dispositions.

## Owner questions (in the draft)

1. A, amend or defer (A recommended).
2. Add-on S (recommended; without an answer, no status act).
3. Add-on M (recommended).
4. Add-on C8. It is human-owned and applies only on explicit selection. Recommended, because the register row calls DEL-10-13 a "Standing gate … re-proved at each such release", "(as DEL-10-02)".
5. Model steer.

## What the caller must resolve or know

- **Number.** D-PEC-103 is provisional; the register has no D-PEC-102..104 row at `e548d4cfa`. The verdict-03 reviewer reported that the parallel packets use 102 (S4) and 104 (S1). HELP_HUMAN publishes the packet and adds the register row. If the final number differs, the C8 line changes one token and the C8 postimage and `apply_k2_c8.py` must be rebuilt. The contracts carry "provisional `D-PEC-103`" nowhere.
- **Findings for the owner (draft "Findings beyond the brief").**
  - DEL-08-06 CON-002: whether authoring and testing tool definitions inside PEC before the K3 tier-0 act counts as "declaring or invoking" a tool.
  - Ordering against S4: DEL-08-01's contract lacks the `agent` class, and DEL-04-03's lacks SOW-097.
  - Possible dependency amends: DEL-08-06 → DEL-04-03, and DEL-10-13 → DEL-02-07.
  - No accepted release process, or definition of "advertising", for PEC v2 (DEL-10-13 CON-004).
  - The DEL-10-02 contract reads C-08's force as "unconfirmed", against `D-PEC-62` and its own `_DEPENDENCIES.md`. This belongs to S1.
- **Open, not decided:**
  - OI-006 (the token mechanism);
  - the K3 profile act content;
  - the C-08 classification, unless C8 is selected;
  - the DEL-02-07 edge;
  - who seeds feeds for the coverage condition (DEL-10-13 TBD-006; assigning it to DEL-10-13 needs a contract revision).
- **Process facts.**
  - The host blocked the Write tool on a worktree other than the session's. I therefore used `EnterWorktree` (path mode) into my own worktree; the caller's checkout was not touched.
  - The session had to hand back twice before completion; this return supersedes those interim handbacks.
  - A drafter's report says it was "also sent to agent `aecdf522c84eec431`". I did not dispatch that agent and have no information about it.
  - Two reviewers disclosed slips that did no harm: one throwaway file written to `/tmp` and deleted at once.
  - No shared-scratchpad file outside a `mktemp -d` directory was deleted by me or reported deleted by any child.
- **PR:** see the PR description. It was not merged. Any "Update the PR base" CI failure is reported, not repaired.
