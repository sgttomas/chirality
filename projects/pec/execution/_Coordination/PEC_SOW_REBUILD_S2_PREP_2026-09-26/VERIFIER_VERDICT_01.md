# VERIFIER_VERDICT_01: S2 Scope of Work rebuild packet (provisional D-PEC-100), PR #964 head c0919e261

Transcribed verbatim by WORKING_ITEMS from the final report of a fresh read-only `pec-reviewer` TASK (Opus 5.5, `claude-opus-5-5`, high reasoning; host-reported model; role instruction-asserted), 2026-09-26. The reviewer could not write files. Dispositions follow the transcription and are the manager's, not the reviewer's.

---

**Verdict: PASS WITH NOTES.** Nothing blocks. I found 8 non-blocking findings, listed below. Findings 1 and 2 are false or dangling statements in the owner-facing draft. They should be fixed before HELP_HUMAN publishes it. None of them changes the grant, a candidate's bytes, or whether any candidate is true.

Reviewer: fresh read-only TASK (pec-reviewer). I authored nothing here and modified no file. The worktree is still clean at `c0919e261be52d80d1078a4535fbb2761702e5be`.

Instructions read:
- Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `agents/AGENT_TASK.md` `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`

Method loaded: `workflows/scope-of-work/WORKFLOW.md` `84dadde4…bc2b`, `resources/checks.md` `44ab41ac…f188`. I consulted no other role instructions.

Relayed brief amendment: the draft does not put `MODE=REVISE` adoption to the owner. It mentions REVISE once as a disclosure (draft L27) and once under Limits (L262). This complies.

## A. MODE=VERIFY on the seven candidates (checks.md items 1, 3, 4, 8, 9, 13, 16, 18–21)

The results are the same for all seven: DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07.

- **Item 1 (pilot variance): PASS**, on the reading the D-PEC-98 verifier used. No candidate carries a `pilot-variance`, `MIGRATION_DUAL` or source-marker token.
- **Item 3 (`_STATUS.md` untouched): PASS.**
  - All 7 `_STATUS.md` files are pinned in `apply_s2p.py` PINNED and hash as tabled at aca930622, dfb089b8a and c0919e261.
  - My rerun's containment diff shows exactly 7 differing files, all `ScopeOfWork.md`.
  - All seven deliverables are `INITIALIZED` at aca930622 and at dfb089b8a, and none has a `## Remaining` section.
- **Item 4 (validation): PASS.** The validator returns `PASS format=SOW_V1` ×7. All 7 frontmatter pins are `@189f205ff02d…`.
- **Item 8 (outputs trace to scope): PASS.** Every OUT has a matrix row carrying its SOW and OBJ references.
- **Item 9 (acceptance criteria verified): PASS.** Every AC sits in a matrix row with a VER method or a HUMAN_REVIEW method.
- **Item 13 (checklist): PASS.** Item counts are 17, 15, 19, 15, 15, 15 and 16. Each checklist is bound to its postimage hash. The hashes equal draft L318.
- **Item 16 (findings classified by kind): satisfied by this report.**
  - Schema findings: none.
  - Project-content findings: 4 and 7.
  - Execution-substrate and evidence findings: 1–3, 5, 6 and 8.
- **Item 18 (deterministic checklist): PASS.** Reruns are byte-identical. Negative control 5 shows the checklist refusing, with no artifact, after a matrix row is removed.
- **Item 19 (qualified upstream IDs): PASS.**
  - The validator's unresolved-reference check passes.
  - My own scan for possessive bare upstream IDs outside blockquotes found none.
  - `check_sibling_ids` passes 92/92.
  - Every upstream blockquote carries the carve-out sentence.
- **Item 20 (one acceptance criterion per matrix row): PASS.** Every row has one AC. DEL-01-06 AC-005 appears on two rows, both with VER-005 only.
- **Item 21 (boundary owners): PASS.**
  - The tool reports no `UNRESOLVED_OWNER` and no `UNDEFINED_CLAIM`.
  - I checked the hand-resolution table (draft L214–222) against the requirement text:
    - DEL-01-01 REQ-003/004/005/007/015/016 all cite CLM-012, which names DEL-04-03, DEL-03-02, DEL-03-03, DEL-03-01, DEL-01-03, DEL-04-05 and DEL-01-06.
    - DEL-02-06 REQ-004 (CLM-012) and REQ-006/009/010 (CLM-011) resolve correctly.
    - DEL-02-07 REQ-004 → DEL-04-05 and REQ-006 → DEL-01-03 both resolve through CLM-014.
    - DEL-02-03's per-act clauses resolve through CLM-015, which names DEL-04-05, DEL-04-03, DEL-01-03, DEL-03-01 and DEL-01-05.

**Semantics**
- **Retired IDs.** The retired set equals the draft table:
  - DEL-01-01: AX-006
  - DEL-01-06: CLM-007, CON-001, TBD-002
  - DEL-02-04: CON-002, CON-003
  - DEL-02-06: CON-002, CON-003, CON-005, TBD-004, TBD-005
  - DEL-02-07: CON-001, REQ-001
  - None of these is used bare in any candidate, and every new ID is numbered above its prefix's prior maximum.
- **ID gaps.** DEL-02-03 leaves TBD-005 and CON-005 unused. AX-015 explains why.
- **ID counts and line counts** equal draft L44–50.
- **Lifecycle, acceptance, reliance.** No candidate claims CHECKING, ISSUED, acceptance or reliance for its own deliverable. DEL-01-01 CLM-009 observes that DEL-00-01 is `CHECKING`, which is true at aca930622. Every `## Remaining` mention is exclusionary.
- **CON items.** No CON is resolved by assumption. DEL-02-04 REQ-001 adds an interim rule while CON-005 stays open: it does not read archive-tag records. I read that as the narrowest reading of the ledger's "under `execution/**`", not as a resolution, and draft L57 discloses it.
- **Parser guard carry-forward.** Every candidate carries it as a `DEL-01-03/CON-001` case: DEL-01-01 CON-003 and REQ-017; DEL-01-06 CON-002; DEL-02-03/04/05/06 CON-006; DEL-02-07 CON-005.
- **Scope.** Requirements that go beyond the ledger rows, `Deliverables.csv` and the PRD trace to accepted or ruled records:
  - DEL-01-06 REQ-003/008–012 → the D-PEC-96 ruled proposal. The no-echo rule is at proposal L418; the at-least-one-live and disjointness rules are at L108–133.
  - DEL-02-03 REQ-017 → SCA-005 §B7.
  - DEL-02-07 REQ-016 → D-PEC-99 exhibit Part B REM-004.
- **State claims I recomputed independently (all true):**
  - 66 PEC deliverable `_STATUS.md` files, 4 of them `RETIRED`
  - 11 files under `v2/src/pec_v2`, with no record-tier entity classes
  - 6 files in `v2/` name `RegisteredLoop`
  - 16 `STATUS.json` files (all Piping) and 8 `RUNTIME_SUMMARY.json` files (Root 2, Piping 3, Runtime 3); the archive commit `8007c5927` holds 954 and 104, and 13 of them are in PEC-DPEC77-78
  - 13 `LOOP_INIT.md` files; 5 workplans under PEC `plans/workplans/`; 6 in Piping `loop/`
  - 5 `*_harness/adapter.yaml` files, and none under PEC
  - `FEED_PROFILE_SURFACES` matches DEL-01-06 CLM-016
  - SOW-017 is byte-identical at 53145aaeb (revision 1.5) and at 189f205ff

## B. Packet review

- **Part B fidelity: PASS.**
  - Each carry-forward and Gate line in DEL-02-07 (L141/143, 149/151, 157/159, 165/167) matches a whole line of the exhibit exactly: carry-forwards at exhibit L787, 799, 811, 823; Gates at L783 and L795, where the text of L783 is identical for REM-001, -003 and -004.
  - The landing table (draft L70–77) matches the candidate's lines and local IDs.
  - CLM-016 (L137) and AX-011 (L268) state that the gates still bind.
- **Lifecycle answer: PASS.** No transition is proposed, the act refuses to run if any `_STATUS.md` differs, and there is no CHECKING prompt.
- **Grant and binding: PASS.**
  - TARGETS and PINNED in `apply_s2p.py` equal the recomputed preimage hashes at aca930622, dfb089b8a and c0919e261, and the postimage hashes of the candidate files: 7 targets and 23 pins, 0 mismatches.
  - The draft's grant table and pinned list match the script entry for entry.
- **Add-on M: correct.**
  - DEL-01-06 `MEMORY.md` exists (`035ecb86…0a3f`, header with no row); the other six are absent.
  - The template is `5a9564f4…6a5a`.
  - The D-PEC-96 ruling item 5 ("create MEMORY … closeout writes the run row") agrees with draft L157.
- **Owner questions:** appropriate and not pre-decided. None concerns REVISE or CHECKING.
- **Other provenance hashes and quotes: verified**, with the exceptions in findings 1–3. Verified values: brief `31313b8f…92d3`, drafter brief `ab7fdc29…43fd`, `D-PEC-94` `b6814e90…5a6b` with the quote, `Propagation_Plan` `50cd0b1d…1350` with exactly 8 `STALE_REBUILD_REQUIRED` rows (DEL-01-06 "gated on B6"), IA `93253b7d…b691`, `D-PEC-96` ruling `852057f0…399e` routing S2 (L82), register `e845e1bb…48e2` with no D-PEC-100 row, notice `8829ac84…64af` (the quoted "no adoption … expected in this loop now" is at L18), the S4 set, holds (header only), `AGENT_WORKING_ITEMS` `9ae4bea2…9665`, and the tool, workflow and standard hashes.

## Findings (all NON-BLOCKING)

**1. Draft L19 misidentifies the basis commit and makes a false "nothing changed" claim.**
- It says `dfb089b8a` is the "PR #961 merge". In fact `dfb089b8a` is the PR #960 merge; the PR #961 merge is `c76434101`.
- It says only PR #961 landed since aca930622 and that "no file this packet pins, quotes or claims about changed". Both are false:
  - PR #960 (chirality-app-dev and exports) also landed.
  - `git diff --name-only aca930622 dfb089b8a` shows that the undertaking `WORK_GRAPH.md` changed. That file is read from the tree by quotes DEL-01-01 Q44, DEL-02-03 Q53 and DEL-02-05 Q48, and it is a claim target in six claims files.
  - `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, a claim target in DEL-02-03, also changed.
- No candidate is affected: those claims are anchored at aca930622, and the tree quotes pass again at dfb089b8a.
- Also: `apply_s2p.py` L57 says the pins are "values at origin/main c76434101", while draft L117 says dfb089b8a. The bytes are the same at both, but one commit should be named consistently.

**2. Draft L276 cites a file that does not exist.** It names `evidence/RUN_S2P_CHECKS.out`; the actual file is `evidence/run_main/SUMMARY.out` (`01b51468…c925`). Related: L29 ("One fresh read-only pec-reviewer ran MODE=VERIFY") and L326 (`VERIFIER_VERDICT_NN.md`) describe this verdict before it exists. They become true once it is saved.

**3. Draft L205 understates the strict-register baseline.** It says "0 errors, 26 pre-existing XRG-013 warnings". The actual output has 28 warnings: 26 XRG-013 plus 2 DRB-008. The before/after identity check is unaffected.

**4. What "kept IDs keep their meaning" means needs stating in the packet.**
- Draft L28 states the rule literally, and L54/L83 flag only DEL-01-01 REQ-006 as a changed rule.
- Several other kept IDs keep their subject but change their rule in substance:
  - DEL-02-06 REQ-001, REQ-004, REQ-005, REQ-012, CLM-012 and CON-004. Its AX-014 says so ("changed in reach, not in subject").
  - DEL-01-06 REQ-001 and REQ-005: version 1 becomes version 2. Its AX-012 says "text brought to the current basis". DEL-03-01's quotation of REQ-005 is disclosed at L87.
  - DEL-02-07 OUT-001, REQ-004 and REQ-006 are narrowed. Its AX-014 says so.
  - DEL-02-04 REQ-001: discovery now follows the feed profile.
- No retired ID is reused, and every changed ID is disclosed inside its own contract. The only qualified citations from outside S2 are DEL-01-01 REQ-006, REQ-008, AC-007 and CLM-006.
- The Method section should state the reading ("meaning" means subject or role, with the rule brought current) and list these IDs, so the owner rules knowingly.

**5. The act-time quote check can fail for reasons unrelated to the candidates.**
- Finite verification row 5 (L201) runs the verifier on `--tree .`, the act tree. Quotes without a commit read mutable files there: the three `WORK_GRAPH.md` quotes above, which HELP_HUMAN will edit when it records S2, and files in other projects.
- The candidates present those quotes as observations at aca930622. Row 1 routes only a "pin mismatch" to the owner.
- The failure mode is fail-closed, so there is no risk of a false pass.
- Either pin those quotes with `"commit": "aca930622"`, or state how a failure caused only by drift is handled at the act.

**6. The `--check-only` result is a label, not a check.**
- `apply_s2p.py` L157–158 prints `CHECK write set = grant (0 creates, 7 modifies, 0 removes)` as a fixed string. Check-only computes no write set; the real inventory check runs only in apply mode, at L163–168.
- Row 1 (L197) treats that line as a required result. It should be described as passing the preflight.

**7. The grant wording overstates what the workflow authorizes.** L103 says the act runs "under chirality-root:bundled:workflow:scope-of-work". The workflow has no mode that overwrites an existing contract apart from REVISE, which PEC has not adopted. L26 correctly says the ruling authorizes the write and MODE=VERIFY is the independent check. L103 should say the same, to match L26 and the D-PEC-98 practice.

**8. Some verifier entries test less than the candidate asserts.**
- `claims/DEL-01-06.json` S186 is a count check (6 files contain `RegisteredLoop`). The candidate's AX-007 asserts which files they are: port, adapter, package re-exports and tests. I confirmed the six by `git grep`, and they are correct.
- `quotes/DEL-02-07.json` Q46 is "This contract", 13 characters, so it is trivially satisfied.
- By design, `candidate_text` matching is location-free. Short spans such as `` `PENDING` `` occur many times, so a claim's value is not tied to the sentence that asserts it. I sampled DEL-02-07's non-CSV claims fully and DEL-01-06 and DEL-02-05 in part, and each value tests the assertion it supports. For example, the "unchanged between revision 1.5 and 1.6" statement is covered by S157, S158 and S159 together.
- Evidence nit: `negative_controls.out` control 4 is labelled "wrong hash for PRD", but the altered claim is S003, on `SOFTWARE_DECOMP.md`.

## C. Commands run (read-only; scratch area under the session scratchpad)

1. `cp -R PREP → scratchpad/v1/prep`, then:
   `TMPDIR=…/v1/tmp zsh prep/run_s2p_checks.sh <worktree> dfb089b8a …/v1/prep …/v1/out` — **exit 0**, `OVERALL PASS`. Result lines:
   - act: check-only 0, apply 0, rerun refuses 1
   - containment: 7 differing files, all `ScopeOfWork.md`
   - validate, checklist (rerun byte-identical) and boundary (no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM`): PASS ×7
   - quotes: `RESULT PASS 460/460`
   - state claims: `RESULT PASS 1274/1274`
   - sibling IDs: `RESULT PASS 92/92`
   - consequence scan: `SUMMARY stale=31 kept=32`
   - strict registers identical before and after (exit 1)
   - harness identical (exit 0)
   - receipts identical (exit 0)
   - whitespace: PASS
   - fault injection: `RESULT PASS 7/7`

   Every output file is byte-identical to `evidence/run_main/*`, except `receipts_{pre,post}.out` and `containment.out`, which differ only in the export path. The runner deleted both exports.
2. `shasum -a 256 -c SHA256SUMS` in PREP: every entry OK.
3. `pec_reliance_hold.py` with `candidate-validation` and with `historical-read-only-inspection` on all 7 `ScopeOfWork.md` targets, run in a path-limited export: `ALLOW`, exit 0 ×14.
4. `git diff --check dfb089b8a c0919e261`: exit 0, clean.
5. `git merge-base --is-ancestor`: 189f205ff is an ancestor of dfb089b8a, and 73ed349ed of aca930622.
6. `git diff --name-only dfb089b8a c0919e261`: only the prep folder and the two S2P briefs. The PR stays in its write scope.
7. Ad hoc Python and grep scans:
   - TARGETS/PINNED recomputed at 3 commits: 0 mismatches
   - ID set, retirement and numbering comparison against the prior contracts at aca930622
   - matrix and QA 20 check
   - byte comparison of Part B against the exhibit
   - QA 19 possessive scan
   - check of which verifier inputs changed since aca930622 (this found finding 1)

## Hashes relied on

- **Postimages (all equal to SHA256SUMS and TARGETS):**

| Deliverable | SHA-256 |
|---|---|
| DEL-01-01 | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| DEL-01-06 | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| DEL-02-03 | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| DEL-02-04 | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| DEL-02-05 | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| DEL-02-06 | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| DEL-02-07 | `a07d5f17305598731e98d853f71361d0f8a1def3597d5b25c48eb25f03ff9079` |

- **Preimages:** as in draft L107–113, verified at aca930622 and dfb089b8a.
- **Draft:** `b05162eea982d23285ab09a7bfa5b1b454e0285eef2313b93b11d8ccc4f1b14d`
- **Scripts:**
  - `apply_s2p.py` `69ff97c002fd99326fb41f92cfb9b5a1450e9ee86cfb3ed005917d87970d16fe`
  - `verify_s2p_quotes.py` `be74a06c…d6af`
  - `verify_s2p_state_claims.py` `eb85c15f…8545`
  - `check_sibling_ids.py` `e8c0f2bd…a091`
  - `test_apply_s2p.py` `9a680ba9…3908`
  - `run_s2p_checks.sh` `52463303…6531`
- **Basis, identical at 189f205ff, aca930622 and dfb089b8a:**
  - `SOFTWARE_DECOMP.md` `9374c21f…8eb1`
  - `Deliverables.csv` `94ee5d18…9805`
  - `ScopeLedger.csv` `1d24a4b8…916e`
  - `ContextBudgetQA.csv` `93b0bb07…4c7c`
  - `PRD.md` `ae49b806…3fbe`
  - `loops.json` `fd342b4f…53d7`
  - `loops.schema.json` `104ed648…b143`
- **Other sources:**
  - Exhibit `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`
  - Port `a509bfb7…c8a9`
  - Adapter `620a173d…2f07`
  - Guard `740a4a74…19ee9`
  - `WORK_GRAPH.md` at dfb089b8a `5cee83f9…6788` (the S2 row is byte-identical at aca930622)
- **Method and tools:**
  - `workflows/index.json` `2bfa2c5f…dafb3`
  - `execution.json` `4ad8b7eb…a26d`
  - Standard `26c8254a…433c`
  - Validator `f0f10590…fecfe`, checklist deriver `bfb64dc9…0109`, boundary checker `22ef57e0…ae16a`, `common.py` `61a34722…0389`

---

## Manager dispositions (WORKING_ITEMS, 2026-09-26)

All eight findings are repaired in commit `97cc398b7`. One candidate byte range changed, in DEL-02-07 only (item 8).

1. Draft Provenance "Source state" rewritten: `dfb089b8a` is the PR #960 merge; PRs #961, #960 and (since) #963 landed after `aca930622`; the changed files the packet reads are named (the undertaking `WORK_GRAPH.md`, App `LOOP_RECEIPTS.md`), with why no candidate is affected. The final check ran at `5aa4285c2` (PR #963, Piping only), and `apply_s2p.py`'s pin comment names that commit (script rebound).
2. Evidence file name corrected to `evidence/run_main/SUMMARY.out`; the verifier references now name `VERIFIER_VERDICT_01.md` onward.
3. Strict baseline stated as 28 warnings: 26 `XRG-013` and 2 `DRB-008` (DEL-08-06 and DEL-10-13 have register rows and no folders yet; node K1).
4. Method gains the ID-meaning reading and the list of kept IDs whose rule changed.
5. All 412 quote entries whose source is a tree file other than the seven production contract paths now carry `"commit": "aca930622"`; verification row 5 says so. The JSON files were re-serialized with two-space indentation in the same pass.
6. `apply_s2p.py --check-only` now prints `CHECK preflight passed; planned write set 7 modifies, 0 creates, 0 removes (not yet inventoried; the inventory check runs in apply mode); nothing written`; verification row 1 describes it that way.
7. Grant wording aligned with Method: this ruling authorizes the replacements; the workflow supplies the `INIT` authoring discipline and the independent `MODE=VERIFY`.
8. `claims/DEL-01-06.json` gains S187–S192, one `contains` claim per named file. `quotes/DEL-02-07.json` Q46 now quotes "each verification method this contract declares" from the REM-004 carry-forward. Checking Q46 showed the candidate's note quoting that phrase with a capital "This contract", while the exhibit has it lower-case; the manager corrected the DEL-02-07 candidate to `"this contract" in the quotation` (postimage `3d122087…18fb`) and rebound the act script. The negative-controls label is corrected by an appended note.
