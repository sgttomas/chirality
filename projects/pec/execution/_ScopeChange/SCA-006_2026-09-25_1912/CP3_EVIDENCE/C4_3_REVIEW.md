# C4.3 separate review — SCA-006 checkpoint-3 poststate (saved verbatim)

The reviewer was a fresh `pec-reviewer` instance (Claude Code Agent tool, `model: opus`, which the host maps to Opus 5.5), with no write tools, that authored nothing in this candidate. It was dispatched by the WORKING_ITEMS manager (brief B6) under `Propagation_Plan.md` §C4 item 3. The reviewed revision is `c5efad489325dbe1bac61fc4c72867f2b3282872`.

The manager saved the report below as returned; only the harness indentation was removed. The manager's dispositions follow the report.

---

## R3 review of the SCA-006 checkpoint-3 candidate (brief B6, independent review under Propagation_Plan §C4 item 3)

**Verdict: PASS WITH MINOR.** No blocking findings. This is a read-only review. I wrote nothing in the repository; scratch files are under `/private/tmp/claude-501/.../scratchpad/r3review/`. It makes no CHECKING, ISSUED, acceptance or pointer claim.

**Revision reviewed.** Candidate `94e9255b6..c5efad489325dbe1bac61fc4c72867f2b3282872`, branch `claude/pec-sca006-cp3-execution`, worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c`.

The branch moved while I was reviewing:
- At first, the worktree had uncommitted edits: the manifest, `AGENTS_MD_AMENDMENT1_DIFF.md`, `Decision_Log.md`, and a new `RUN_SUMMARY.md`.
- HEAD then advanced to `7f3102ed2` through two commits: `3990f2930`, which records the owner's hunk approval, and `7f3102ed2`, the Handoff_State checkpoint-3 section.

My verdict covers `c5efad489` only. To check the committed bytes, I exported that commit with `git archive` to scratch. The two later commits are out of scope (see finding 5).

**Instruction files read (SHA-256):**
- Root `AGENTS.md`: `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/pec/AGENTS.md`, basis version (read as instructions): `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`
- `projects/pec/AGENTS.md`, candidate version (under review): `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`

**Wider consultation:** none beyond the brief's sources, the SCA-005 package (for the meaning of `remaining-loop`), `D-PEC-96_AMEND_DIRECTION_2026-09-26.md`, and register rows D-PEC-95, D-PEC-96 and D-PEC-97.

## What I verified independently (all hold)

**1. Checkpoints 1 and 2.**
- Every hash in both ACCEPTED_MANIFEST files matches the live bytes, except `Decision_Log.md` and `Handoff_State.md`. The manifests mark those two as "superseded in place", and the candidate does not change them.
- Snapshot folder hashes:
  - group-1: `DECISION.md` `0160dd88…50df`, manifest `b431b514…a797`
  - group-2: `DECISION.md` `30aebd16…f989`, manifest `b9563489…bc52`
  - amendment 1: `DECISION.md` `15720eb1…777e`, which has its §"Verification rule"
- None of these folders is in the diff. The D-PEC-97 register row is present.

**2. Lane A application.**
- The four registers equal their CP2 candidates byte for byte: `1d24a4b8…`, `94ee5d18…`, `93b0bb07…`, `1597ceec…`.
- `docs/PRD.md` is `ae49b806…7fbe`, equal to the candidate. Slots S1–S4 and the `SCA-006_GROUP-2_2026-09-25` token keep the 2026-09-25 act date, and the folder exists.
- `SOFTWARE_DECOMP.md` is `3ef0412a…9b29`. The applied values sit exactly at `date:`, the §7 Revision row and the DL-21 date cell (each once, value 2026-09-26). I put 2026-09-25 back at those three places:
  - the result is `3ad0de686616…8a8b`, the accepted pre-acceptance variant, differing from the candidate only in lines 5 (`status`) and 8 (`accepted`);
  - restoring those two lines as well gives `4eed1247…2d62`, the accepted candidate.
- The three A2 `_CONTEXT.md` files hash to `b28ada46…7b22`, `74b12e73…2d22` and `95fa815a…37b5`. Each matches its planned postimage and mirrors its revision-1.6 `Deliverables.csv` row (description, CoversScopeItems, envelope, notes).

**3. `projects/pec/AGENTS.md`.**
- The accepted candidate `49ce993a…070d`, with L6 filled as 2026-09-26, gives `6f6f2ed1…64e6`.
- The applied file matches that on L1–260 and on candidate L271 onward (applied L273 onward). The only other difference is the amendment-1 hunk, which replaces candidate L261–270 with applied L261–272. The L209 token is unchanged.

**4. Manifest and notices.**
- I extracted the drafts from `AGENTS_MD_CANDIDATE_DIFF.md` §6.1 and §6.3 and confirmed the draft hashes: `852b1d5b…`, `43cfa318…`, `eb927e1f…`, `385e5e2f…`.
- The applied manifest (`f7f48690…0a72`) differs from its draft only in:
  - the filled slots: tranche ID, dates, `basis` 94e9255b6, the notice paths, the verbatim CP2 act, and the CP2 variant (the candidate with I1);
  - one named addition, `group2_amendment_1`.
- `authorization_date` stays at 2026-09-25, the CP2 act date, which is consistent with the group-2 slot interpretation.
- Each notice differs from its draft only in the manifest-path date and one named amendment-1 paragraph. Hashes: Root `b3c60bf4…c601`, App `af4f6342…68ef`, Runtime `e883efac…bb93`.

**5. Invariants.**
- Counts: 100 scope items (74 IN / 18 OUT / 8 TBD); 68 deliverables (64 active / 4 retired); 68 ContextBudgetQA rows.
- No IN item lacks a package, deliverable or objective. The union rule holds on 64/64 active rows.
- Ledger and deliverable rows stay in lockstep (0 mismatches). No deliverable covers a scope item from another package.
- DEL-08-06 is PKG-08/SOW-099/OBJ-001/M/P3. DEL-10-13 is PKG-10/SOW-100/OBJ-001/S/P1.
- New IDs are append-only. The manager's `c3_assert.py` gives 31/31 PASS when I rerun it, and its output is byte-identical to the committed `c3_result.json`.

**6. Write containment.**
- All 37 changed paths are in the Lane A allowlist or are B6 return files.
- The SCA-006 folder only gains files: `Supersession_Map.csv`, `Post_Change_Coverage.json`, `AGENTS_MD_AMENDMENT1_DIFF.md` and `CP3_EVIDENCE/*`.
- No `_STATUS.md`, SOW, SPEC, `Dependencies.csv`, `_REFERENCES.md`, `v2/**`, `pec.yaml`, `_LATEST.md` or `_AUTHORIZED.md` changed. Both pointers hash as required: `e92b3b16…7d24` and `626feaaf…12dd`.
- Re-running the accumulator reproduces `Supersession_Map.csv` exactly: 45 rows, 0 findings, `010ce5c4…aab92`.
- `Post_Change_Coverage.json` equals the audit's `coverage_summary.json` (`b9a068c0…9cf0`). `Pre_Change_Coverage.json` equals the baseline (`b7b432a2…128d`).

**7. Pre/post coverage.**
- **Attribution.** COV-068/069/072 and the pointer part of COV-073 are attributed to D-PEC-95 (N1–N3), not to SCA-006. I checked the baseline rows and the live state:
  - 0 contexts end at revision 1.4: 63 end at 1.5 (61 with the "then by" tail and 2 born at 1.5) and 3 at 1.6;
  - all 66 `_REFERENCES.md` name revision 1.5 and PRD v2.3.
- **Counts.** The per-finding delta adds up: 68 carried + 2 changed + 3 resolved = 73 prior; 68 + 2 + 16 new = 86. Severities: 12 EXPECTED_CONSEQUENCE, 3 WARNING, 71 INFO.
- **Classifications.** Every EXPECTED_CONSEQUENCE cites an accepted source:
  - B1 folders: COV-003/004/073/074 → §B1
  - B3 quotes: COV-075/076 → §B3
  - B7 re-pin: COV-077/078 → §B7
  - A2 postimages: COV-079 → §A2
  - B2 traces: COV-080 → §B2
  - pointers and front matter: COV-084 → §A6 and §A1
  - snapshot mid-completion: COV-085 → §A5
- `closure_summary.json` is byte-identical to the audit's (`bd73806c…187a`).

**8. Lane B and closure claims.** Nothing in the committed candidate says any Lane B item is satisfied. The audit, the hunk record, the notices and the return claim no CHECKING, ISSUED or acceptance, and `ReadyForNextPhase` is NO. The applied `AGENTS.md` does not say revision 1.6 is accepted.

## Findings

**1. MINOR — the amendment-1 hunk contradicts revision-1.6 text in the same poststate, and this is not disclosed where it should be.**
- **The conflict.** Applied `projects/pec/AGENTS.md` L263–264 says: "No PEC feed profile reads them, so the coordination plane does not scan them". The notices repeat it (Runtime notice L25–27; Root and App the same). But the revision-1.6 text in the same PR still says PEC's own `pec` row "declares the `remaining-loop` profile now":
  - `SOFTWARE_DECOMP.md` L259 (SOW-094)
  - `ScopeLedger.csv` L72
  - `Deliverables.csv` L10 (DEL-01-06)
  - §9 L652 (vocabulary example list)
- **Why this matters.** Under SCA-005, `remaining-loop` is the profile that reads PEC's 57 `## Remaining` sections: IA R-05 and FX-PEC-0, and Decision_Log SCA005-CP1-Q8 (a). After checkpoint-3 acceptance, the instruction file and the accepted decomposition would disagree.
- **Why it is not blocking.**
  - The sentence is literally true of the implementation today: `v2/config/loops.json` declares no feed profiles.
  - It follows amendment 1's recorded interpretation word for word.
  - Changing the decomposition needs the pending D-PEC-96 ruling (its record says so).
- **Where disclosure is missing.**
  - `AGENTS_MD_AMENDMENT1_DIFF.md` §2 checks the sentence only against `v2/**` and PRD §7.1, not against the conflicting decomposition text.
  - Audit COV-083 (INFO) records the decomposition vs D-PEC-96 tension but not the `AGENTS.md` hunk in the same PR. Given that contradiction, COV-083 is arguably under-classified: it could mislead amendment work, which is the WARNING test.
- **Repair.**
  - Add the four revision-1.6 loci and COV-083 to the §2 evidence row of `AGENTS_MD_AMENDMENT1_DIFF.md`.
  - In RUN_SUMMARY and Handoff_State, carry forward that SOW-094, DEL-01-06 and the §9 `remaining-loop` text must be reconciled, through the D-PEC-96 ruling plus a later scope change, or the owner knowingly accepts the drift at checkpoint 3.
  - The final verifier should confirm the owner saw this before approving the hunk. The later commit `3990f2930` claims it was presented; I did not verify that.
  - The hunk text itself needs no change. Any qualifier would need owner re-approval.

**2. MINOR — a check result in the B6 return does not match the committed state.**
- **The claim.** `.../returns/B6_SCA006_CHECKPOINT3.md` (`850ad9e0…66ac`, committed at `e07bafedb`, "Checks" section) reports `git diff --check origin/main HEAD` as clean (exit 0).
- **What I found.**
  - `git diff --check 94e9255b6 c5efad489`: exit 2
  - `git diff --check 94e9255b6 e07bafedb`: exit 2
  - `git diff --check 94e9255b6 39a9768c8` (the A4 commit): exit 0
- **Cause.** 46 trailing-whitespace hits, all in `Supersession_Map.csv`, which has CRLF line endings. The SCA-005 map has the same endings (checked with `od -c`).
- **Context.** Cosmetic whitespace is not a merge gate under `projects/pec/AGENTS.md`. The plan says the map is generated, never edited by hand.
- **Repair.** In the final return or RUN_SUMMARY, record exit 2 and its cause (CRLF output of the accumulator, which matches precedent). Do not edit the CSV.

**3. NOTE — decomposition date slots.**
- `Amendment_Preview.md` §"Acceptance-bound tokens" ties `date:`, the §7 Revision row and the DL-21 date to the checkpoint-3 acceptance date. The candidate fills them with the application date, 2026-09-26. Plan §A1 and the group-2 interpretation allow that.
- Plan §A6 restores only the two front-matter lines. If the owner accepts after 2026-09-26, A6 must put the acceptance date at those three places and recompute the hash. The B6 return flags this; make sure the A6 instructions carry it.

**4. NOTE — faithfulness of the hunk.**
- The hunk stays within amendment 1's bounds:
  - it adds nothing new;
  - it keeps the status quo;
  - gate markers still bind;
  - an item is updated only under a packet that opens its `_STATUS.md`;
  - retirement stays a separate undertaking, and the hunk decides nothing about it.
- Dropping "its graph accounts for the Remaining items it touches" is a faithful reading of "no need to scan for them". The duty to record a consequence when an undertaking touches an item is kept.
- One small wording drift: "completes or changes" became "completes or affects" (applied L270), which is slightly broader. The owner may want "changes" back. That is optional and would need re-approval.

**5. NOTE — the branch moved during review; the later commits are unreviewed.**
- `3990f2930` and `7f3102ed2` change:
  - the manifest: `owner_hunk_approval` now claims "approve hunk" from Ryan Tufts on 2026-09-26;
  - `AGENTS_MD_AMENDMENT1_DIFF.md` (status now "owner_hunk_approved");
  - `Decision_Log.md` and `Handoff_State.md`;
  - new files: `RUN_SUMMARY.md`, `c1_containment.py`, `c5_completeness.py`, `verify_manifest.py`.
- I did not verify the approval claim and do not treat it as evidence.
- The final verifier must:
  - rerun G4 in CI and `--added-manifests-only` modes on the final manifest;
  - confirm that the approval names the exact bytes `4400c4e9…`.

**6. NOTE — rerunning the evidence scripts.** Six of the seven `CP3_EVIDENCE` scripts hard-code `/Users/ryan/.../agent-a2942849b8715f72c` (all but `preflight.py`). The evidence contract in `projects/pec/AGENTS.md` asks for a bounded way to rerun checks, and its Path Anchors rule applies. Repair: state in RUN_SUMMARY that `R` should be replaced by the value of `git rev-parse --show-toplevel`, or add a parameter later.

**7. NOTE — items HELP_HUMAN must finish before merge (not Lane A defects).**
- The `docs/STATUS.md` correction under D-PEC-88 that amendment 1 names as a known consequence (STATUS L132–133) is not in the candidate.
- At `c5efad489`, the owner's approval of the hunk was still outstanding, and the manifest said HELP_HUMAN would obtain and record it.

**8. NOTE — the audit reuses finding IDs.**
- The new audit numbers COV-068/069/072/073 again, for different findings from the baseline ones that the plan attributes to D-PEC-95. `PrePost_Comparison.md` maps them correctly.
- However, `Decomp_Coverage_Report.md`'s "What would clear" item 2 mentions COV-068 and COV-073, and a reader could take those as the baseline findings. Suggest writing "this run's COV-068/073".

**9. NOTE — provenance lines that anticipate acceptance.**
- The three A2 contexts say "revision 1.6 (`current_basis`…)" (COV-079), and the notices say "revision 1.6 adds…" without a pending-acceptance qualifier. Both are accepted draft bytes.
- If the owner refuses checkpoint 3, the rollback should name these lines. Plan §"Failure and rollback" does not. Mention this in the checkpoint-3 question.

## Commands run (exit codes)

- `git diff --name-status 94e9255b6 HEAD` (at `c5efad489`) → 0; 37 paths.
- `git archive c5efad489 | tar -x` into scratch `head/` → 0.
- `shasum -a 256` over every written file, both ACCEPTED_MANIFEST files, the snapshots, the pointers and the audit folder. All values are quoted above.
- Slot-substitution proofs (python) → `3ad0de68…` and `4eed1247…` for the decomposition; `6f6f2ed1…` for `AGENTS.md`, with prefix and suffix identical.
- `CP3_EVIDENCE/extract_drafts.py <scratch>` → 0, 4/4 MATCH; then `diff` of each draft against the applied file.
- G4 `validate_instruction_tranche_manifest.py` on the export, with the diff path lists taken from git for `94e9255b6..c5efad489`:
  - CI mode → 0 (PASS, 124 manifests)
  - `--added-manifests-only` → 0 ("37 changed, 1 on the instruction surface, checked against 1 manifest")
  - full diff mode → 0
- `validate_decomposition_registers.py projects/pec/execution --strict` (export) → exit 1 by design: 0 ERROR, exactly 2 WARNING DRB-008 (DEL-08-06, DEL-10-13).
- `analyze_dep_closure.py projects/pec/execution --output-dir <scratch>/closure` → 0: 111 edges, 0 SCCs, 0 bidirectional pairs, 0 orphans, 6 isolated.
- `validate_instruction_entrypoints.py .` (export) → 0 PASS.
- `validate_pec_loop_receipts.py --repo-root .` (worktree) → 0 VALID.
- `pytest -q` on the entrypoints and receipts tests → 33 passed.
- `harness.py self-check` (worktree, at `7f3102ed2`) → 0: no finding names a changed file (INFO 14, REVIEW 4, WARN 124, all elsewhere).
- `accumulate_supersession_map.py` into scratch → 0: 45 rows, 0 findings, identical hash.
- `c3_assert.py` with preimages from `git show 94e9255b6` → 0, 31/31, output identical to `c3_result.json`.
- `pec_reliance_hold.py --operation candidate-validation` for 11 reviewed targets (decomposition, registers, PRD, `AGENTS.md`, the three contexts, the audit summary) → ALLOW for all 11.
- `git diff --check 94e9255b6 <rev>` → exit 2 at `c5efad489` and `e07bafedb`; exit 0 at `39a9768c8`.

---

## Manager dispositions (WORKING_ITEMS B6)

| # | Disposition |
|---|---|
| 1 | Repaired as proposed, with the hunk bytes unchanged. `AGENTS_MD_AMENDMENT1_DIFF.md` §2 now names the four revision-1.6 loci and COV-083. `RUN_SUMMARY.md` (§3.2, Q-CP3-1, §6) and `Handoff_State.md` carry the reconciliation forward. Since the review, `D-PEC-96` has been ruled; the ruling is on `origin/main` through PR #946 and is recorded in `RUN_SUMMARY.md`. The owner saw the COV-083 observation before approving the hunk (per HELP_HUMAN's relay; `Decision_Log.md` SCA006-G2-A1). The audit output is not edited, and COV-083 stays INFO there. The manager records the reviewer's under-classification argument in `RUN_SUMMARY.md` §5 |
| 2 | Recorded in `RUN_SUMMARY.md` §4 and in the final return: `git diff --check` exits 2 because of the accumulator's CRLF output in `Supersession_Map.csv`, as in SCA-005's map; with that file excluded it exits 0. The CSV is not edited. The interim return's claim was true at the time of the A4 check (before the map existed) and is superseded by the final return |
| 3 | Carried in `RUN_SUMMARY.md` §3.1 (A6 note) and `Handoff_State.md` A6 instructions 2–3. Corrected after verifier verdict 01: there are **four** acceptance-date slots (the first token of `accepted:` is the fourth), and the post-A6 hash for acceptance on 2026-09-26 is `9374c21f…08eb1` |
| 4 | Noted. The owner approved the hunk as written, including "affects"; no change |
| 5 | Final verifier scope: it reviews the final head, including the approval record and G4 on the final manifest |
| 6 | Recorded in `RUN_SUMMARY.md` §8 and `AGENTS_MD_AMENDMENT1_DIFF.md` §4 (rerun method: set `R` to `git rev-parse --show-toplevel`) |
| 7 | HELP_HUMAN's pre-merge items; the approval is now recorded |
| 8 | Noted in `RUN_SUMMARY.md` §5; the audit output is not edited |
| 9 | Added to the rollback note in `RUN_SUMMARY.md` §9 and `Handoff_State.md` A6 instruction 5 (only the Runtime notice carries the "revision 1.6 adds" wording) |
