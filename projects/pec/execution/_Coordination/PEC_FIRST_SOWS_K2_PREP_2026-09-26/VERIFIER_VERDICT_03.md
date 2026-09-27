# Verifier verdict 03 — packet review (K2, provisional D-PEC-103)

- **Reviewer:** a fresh read-only `pec-reviewer` TASK (`claude-opus-5-5`, high), dispatched by WORKING_ITEMS. It authored nothing in the packet.
- **Reviewed:** branch `claude/pec-k2-first-sows-proposal` at `a26af25e4` (draft `93a86d14…aedc`; candidates `31d0aa6e…d036` and `23f6505e…f182`).
- **Transcription:** the report below is the reviewer's hand-back message as delivered, with the harness's indentation removed. The manager's dispositions follow it.

## Report

**Verdict: PASS WITH NOTES.** Packet review of provisional D-PEC-103 (node K2), branch `claude/pec-k2-first-sows-proposal` at `a26af25e4`. I found no blocking findings: 2 non-blocking and 9 notes. Nothing was modified. I made and deleted my own `mktemp -d` directory, `k2pkt.hd9HcM`. Near the end of my run a new untracked file appeared, `PEC_FIRST_SOWS_K2_PREP_2026-09-26/VERIFIER_VERDICT_01.md`. I did not write it; another agent did.

Prep folder: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/`. The draft (`DRAFT_D-PEC-103_…md`, SHA-256 `93a86d14…aedc`) is cited below as "draft:line".

## What I verified

- **Check runner:** I reran it on a fresh export of HEAD `a26af25e4` with my own `TMPDIR`. Result: **OVERALL PASS**, exit 0, every line PASS.
  - Quotes 133/133, state claims 479/479, cited IDs 0/0, old S2 text stale=0 (43 current).
  - Fault injection 15/15.
  - Strict registers, harness, receipts and closure output are identical before and after A, and before and after C8.
  - Every committed file in `evidence/run_main/` matches my rerun byte for byte, after path normalisation. The only exception is the basis-commit line of `SUMMARY.out`.
- **Hashes:** every hash I recomputed with `shasum -a 256` matches what the draft states.
  - Brief `5fcc3ef8…e133`, both candidates (`31d0aa6e…d036`, 249 lines; `23f6505e…f182`, 252 lines), both S postimages, the C8 preimage and postimage.
  - `apply_k2.py` `557b73ee…8589`, `apply_k2_c8.py` `0b162a74…aba`, the six check aids, `K2_DRAFTER_BRIEF.md` `aefa51fa…aa40`, the checklists `d9eae773…4c21` / `b0b56b38…c8be` (17 and 19 items).
  - Every basis-table and method hash at `125cfacc1`: workflow files, the standard, tools, `pec.yaml`, holds file, preflight script, register, the D-PEC-101 and D-PEC-62 records, the SCA-006 plan and assessment, and the work graph (`8296ad0c…b148` at `125cfacc1`, changed at `947075c9a`).
  - The defined-ID counts match the draft (draft:89).
- **Pins and commits:**
  - `TARGETS` and all 17 `PINNED` entries in `apply_k2.py`, and the 3 pins in `apply_k2_c8.py`, equal the draft's tables.
  - All 17 pins hold at `125cfacc1`, `947075c9a`, HEAD and current `origin/main` `ce99bc256`. At `189f205ff` the five decomposition and PRD files, plus `pec.yaml`, are equal.
  - `189f205ff` is an ancestor of `origin/main`. `125cfacc1` is the PR #979 merge, `947075c9a` the PR #981 merge and `ce934ac33` the PR #976 merge.
  - The list of files changed between `125cfacc1` and `947075c9a` is exact (draft:42). Both targets are absent at every commit.
  - The register's last row is still D-PEC-101. The parallel packets use D-PEC-102 (S4) and D-PEC-104 (S1), so 103 does not collide.
- **Add-on C8 diff:** the postimage differs from the preimage by exactly the one tabled line, inserted after the Notes bullet.
- **Add-on S:** I ran `write_status.sh` fresh on an `origin/main` export (date 2026-09-26), exit 0 twice. The resulting files are byte-identical to `addons/S/*` (`75366b6b…a127`, `3771d526…e567`).
- **Containment:** `git diff --name-status origin/main...HEAD` shows only the brief copy under `AgentRuns/.../briefs/` and files under the prep folder. There is no production file.
- **Act scripts:**
  - Preflight runs before any write. Writes go to a temporary file, are hash-checked, then renamed.
  - Rollback removes created targets and temporaries (A), or restores the preimage (C8).
  - The before/after inventory of `projects/pec` excludes only the script's own directory.
  - The run-root guard refuses a copy placed anywhere under `projects/pec` outside `SOW_INIT_K2_*`, which closes the PR #964 review 01 gap. A second run is refused.
  - The four verifier scripts are sound: two-sided quotes, all read at a pinned commit; state claims checked in git and in the candidate; raw dependency-quote check.
- **Qualified IDs:** neither candidate cites any `DEL-NN-NN/PFX-NNN` ID of another contract, or the other K2 candidate's local IDs. I also checked prose forms such as "REQ-nnn of DEL-…" and found none. The current S4 and S1 candidates cite no DEL-08-06 or DEL-10-13 IDs either. The draft's observation table (prefixes `8ac1dc050efb` etc., the Q34 quote, the absence claims) checks out at `125cfacc1`.
- **External anchors and old S2 text:**
  - 285 `Dependencies.csv` rows, none with a target contract as `EvidenceFile`.
  - Because `scan_old_s2_text.py` looks only at quoted spans, I ran my own 10-word scan of both whole candidates against the prior S2 contracts at `ce934ac33`. After excluding text still present in current contracts or accepted sources, it found 0 hits.
- **Brief conformance:** every "Produce" element is present, in the same order and depth as D-PEC-98 and D-PEC-100.
  - No lifecycle transition is assumed: S is offered, and "Without an answer, no status act is performed."
  - Nothing prompts the owner about CHECKING. REVISE appears as a one-line disclosure (draft:53) plus a provenance line and a limits line, the same pattern as D-PEC-100:16/27/273, and adoption is not put to the owner.
  - Part B carry-forwards: none, and the draft says so. M is at closeout. Every qualified ID from the S4/S1 targets is listed (none).
- **C8 against docs/SPEC.md §5.1–5.2 (D-GOV-46):**
  - "Dependency Tracking Mode" is human-owned (SPEC.md:448–449), so the plain statement at draft:21, 260 and 421 is accurate.
  - A fourth bullet under the existing heading adds no heading. The tool that writes these files, `tools/coordination/materialize_local_dependencies.py`, preserves human-owned sections and never writes them.
  - Nothing in either candidate becomes false under either answer. The C-08 state claims in DEL-10-13 (CLM-012, CON-001, REQ-016, AX-007) are all tied to `125cfacc1`. DEL-08-06 does not touch C-08.

## NON-BLOCKING

1. **`SHA256SUMS` is missing, and the verdicts are described as if already saved.** The brief (K2P brief:23) requires `SHA256SUMS` (tracked files only), and draft:465 says "hashes in `SHA256SUMS`", but no such file exists at `a26af25e4`. Draft:57, 354 and 472 describe `VERIFIER_VERDICT_NN.md` as already run and saved, but no verdict is committed. Only an untracked `VERIFIER_VERDICT_01.md` appeared during my run.
   - Repair: before return, commit the verdicts with their dispositions, then generate `SHA256SUMS` over the tracked prep files at the final head. Until then, reword draft:57 so it does not state as fact something that has not happened yet.

2. **The SPEC quote for C8 is broader than its source (draft:260).** The draft says an agent "never fills" a human-owned section. That phrase comes from SPEC.md:460–462, which is about an agent adding a *missing* human-owned section only as a `TBD` placeholder. §5.1 also lets "the coordinating workflow" maintain these sections (SPEC.md:448), and the current Tracking Mode bytes were written by D-PEC-101's bound generator under `project-setup`. The conclusion that C8 applies only on the owner's explicit selection is still right, but it rests on D-PEC-101 finding 4 (the classification is the owner's) together with the section being human-owned.
   - Repair: quote the SPEC sentence exactly, or cite "Agent-owned sections never overwrite human-owned sections" (SPEC.md:460). Give D-PEC-101 finding 4 as the reason for owner-only application.

## NOTES

1. **Placement wording (draft:270–271).**
   - "The legacy standing nodes (DEL-10-02, DEL-03-04)": all five D-PEC-62 C-08 nodes carry the separate section (DEL-01-05, DEL-03-04, DEL-10-02, DEL-10-03, DEL-10-10). Repair: say "the five D-PEC-62 C-08 nodes, e.g. …".
   - "D-GOV-46 gives new files a single heading schema, so no new heading is added": SPEC.md:443–446 binds `preparation`, `dependency-extract` and `project-setup` when they create a file or add a missing section. It does not forbid other headings in an existing file. Repair: present the bullet as the conservative choice rather than as something the schema requires.

2. **Quote counts (draft:92).** "Quotes … 61 / 72" includes the two per-candidate FORBID and OBS checks; the quote files hold 59 and 70 entries. Repair: "59 + 2 / 70 + 2" or a footnote.

3. **The runner asserts less than finite-verification rows 3, 4 and 10 require.** `run_k2_checks.sh:75–79` does not check the 17/19 item counts, the prepared checklist hashes, or "0 `NOT_CHECKABLE`". Lines 43–47 compare output but do not require exit 0 for harness and receipts, nor a non-empty closure summary; if the summary extraction failed, two empty files would still compare equal. D-PEC-98's row says "exit 0 each". I confirmed by hand that all of these hold.
   - Repair: add the assertions, or say at draft:321 that the act verifier checks them by hand.

4. **Fault-injection gaps (`test_apply_k2.py:98–115`).** There is no case for the C8 run-root guard, a C8 pinned-hash mismatch, or either script's exit-2 (incomplete clean-up) path. Optional repair: add them.

5. **`check_cited_ids.py:26–31` labels DEL-04-05 and DEL-10-02 as "other (not in this undertaking)"; they are S1.** This does no harm at 0 citations. Optional repair: add an S1 label.

6. **The REVISE disclosure (draft:53) omits the notice hash that D-PEC-100:27 carries.** The notice is `8829ac84…64af`. Add it for parity.

7. **`origin/main` has moved to `ce99bc256` (PR #982).** Since `947075c9a` only `docs/STATUS.md`, two work graphs, a receipt and two returns changed; none is pinned, and all 17 pins still hold. Repair: record a recheck at the final base when publishing (draft:42–43).

8. **Add-on dependencies and ordering (draft:187; `apply_k2_c8.py:36–40`).**
   - C8 pins DEL-10-13's option-A postimage, so it depends on A writing that contract; an "Amend: write only one contract" ruling without DEL-10-13 excludes C8.
   - Any single-contract amend needs a rebuilt, re-hashed `apply_k2.py`.
   - C8 and S must not run at the same time: C8's inventory check would fail and roll back. That is safe, but worth saying.
   - Repair: one sentence each.

9. **Process status.** No PR exists yet for the branch; the brief requires one. The return under `returns/` is also still to come, which containment allows.

Relevant paths:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/DRAFT_D-PEC-103_first_sows_del_08_06_10_13_proposal.md`
- `…/PEC_FIRST_SOWS_K2_PREP_2026-09-26/apply_k2.py`, `apply_k2_c8.py`, `test_apply_k2.py`, `run_k2_checks.sh`, `check_cited_ids.py`, `scan_old_s2_text.py`
- `…/PEC_FIRST_SOWS_K2_PREP_2026-09-26/addons/C8/projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md`
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/docs/SPEC.md` (lines 443–462)
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2P_FIRST_SOWS_PROPOSAL.md`

## Dispositions (WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| NB-1 | **Repaired at publication.** The verdicts 01–03 are committed with dispositions; `SHA256SUMS` is generated over the tracked prep files at the final head. |
| NB-2 | **Repaired.** The C8 paragraph quotes SPEC §5.1 exactly ("humans or the coordinating workflow, ordinarily `project-setup`, maintain them"; "Agent-owned sections never overwrite human-owned sections") and rests owner-only application on `D-PEC-101` finding 4. |
| N1 | **Repaired.** Placement names the five D-PEC-62 C-08 nodes and presents the bullet as a conservative choice, with the legacy-style section as a possible amend. |
| N2 | **Repaired.** The candidates table gives "61 quotes (+2 file checks)" and "72 quotes (+2 file checks)". |
| N3 | **Repaired.** `run_k2_checks.sh` now asserts harness and receipts exit 0, a non-empty closure summary with no cycle or bidirectional pair, 0 `NOT_CHECKABLE`, and checklist item count = AC count, and records each checklist hash; rows 3, 4 and 10 say so. |
| N4 | **Repaired.** `test_apply_k2.py` adds the C8 run-root guard, a C8 pinned-file change, and the exit-2 paths of both scripts: 19/19. |
| N5 | **Repaired.** `check_cited_ids.py` labels DEL-04-05, DEL-10-02 and the other SCA-005 review-class contracts S1. |
| N6 | **Repaired.** The REVISE disclosure carries the notice hash `8829ac84…64af`. |
| N7 | **Repaired.** Source state records the recheck at `e548d4cfa` (17/17 pins hold); the final run is on the branch head that merges it. |
| N8 | **Repaired.** The C8 section states the ordering: after A, not with an amend that omits DEL-10-13, not concurrently with S; any single-contract amend rebuilds `apply_k2.py`. |
| N9 | The PR is opened after verdict 04 and the return is written; recorded. |
