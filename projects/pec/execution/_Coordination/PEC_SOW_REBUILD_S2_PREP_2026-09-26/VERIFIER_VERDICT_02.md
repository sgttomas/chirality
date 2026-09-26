# VERIFIER_VERDICT_02: S2 Scope of Work rebuild packet (provisional D-PEC-100), PR #964 head c7719559b

Transcribed verbatim by WORKING_ITEMS from the final report of a fresh read-only `pec-reviewer` TASK (Opus 5.5, `claude-opus-5-5`, high reasoning; host-reported model; role instruction-asserted), 2026-09-26. This reviewer took no part in round 1. Dispositions follow the transcription and are the manager's.

---

**Verdict: FAIL, with one mechanical blocker.**

- The blocker is Finding 1. `SHA256SUMS` lists an untracked, gitignored bytecode file, so `shasum -c` fails on the PR's actual committed bytes.
- Nothing else blocks. The seven candidates pass `MODE=VERIFY`. The grant binding, the Part B fidelity, the lifecycle answer and the owner questions are all sound.
- The repair is one line and changes no candidate or grant byte.
- Findings 2–6 are NON-BLOCKING.

**Reviewer.** Fresh read-only TASK (pec-reviewer), Opus 5.5 (`claude-opus-5-5`). I authored nothing here and took no part in round 1. No tracked file changed: `git status --short` is empty and HEAD is still `c7719559befbd012a9eca2250066fd6687f41c97`.

**One local cache file changed during this review.** My `importlib` loads of `PREP/apply_s2p.py` from the worktree ran without `PYTHONDONTWRITEBYTECODE`. They rewrote the untracked, gitignored `PREP/__pycache__/apply_s2p.cpython-313.pyc` at 14:52. That file is the subject of Finding 1, and it now fails `shasum -c` locally as well. I did not try to restore it.

**Instructions read:**
- Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `agents/AGENT_TASK.md` `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`

**Method loaded:**
- `workflows/scope-of-work/WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`
- `resources/checks.md` `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188`
- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254a…433c`

**Briefs:**
- `S2P_SOW_REBUILD_PROPOSAL.md` `31313b8fafc7fd25ea351eb2826a9e3c64cd5c5f9541f169a5f451a2cb6692d3`
- `S2P_DRAFTER_BRIEF.md` `ab7fdc29e6c76b36b0c3abc1e0f480293cc1af5cac515fe08127290173d543fd`

**Relayed amendment (REVISE): complied with.**
- Draft L16 records the amendment as evidence.
- L27 is the one-line disclosure.
- L263 only excludes REVISE from what the grant gives.
- No owner question concerns REVISE or CHECKING.

## Findings

**1. BLOCKING (mechanical): `SHA256SUMS` lists a file that is not in the PR.**
- **Where:** `PREP/SHA256SUMS`, entry `74b15aaea7652f3f22b9285cf15c62556568b30c1af6d2a4be1563c94f8ea666  __pycache__/apply_s2p.cpython-313.pyc`.
- **Why it fails:** that file is gitignored and untracked (`git status --ignored` shows `!! …/PREP/__pycache__/`).
- **Evidence:** I ran `git archive c7719559b <PREP>` and then `shasum -a 256 -c SHA256SUMS`.
  - Result: `__pycache__/apply_s2p.cpython-313.pyc: FAILED open or read`, exit 1.
  - Every other entry is OK.
  - `comm` of `git ls-files` against the manifest shows this is the only mismatch.
- **Origin:** the entry was added in `97cc398b7`; it is absent at `c0919e261`.
- **Why the check passes in the worktree:** only because the stale local cache happens to be present.
  - A `.pyc` embeds the source mtime and is rewritten on import, so the entry cannot be reproduced on any clean checkout.
  - My own import during this review rewrote it, and it now fails in the worktree too.
- **Repair:** drop the entry (for example, regenerate from `git ls-files`), then rerun `shasum -c` on a `git archive` of the new head.

**2. NON-BLOCKING: disposition 4 is only partly repaired; the list of kept IDs whose rule changed is incomplete.**

Draft L28 says "each contract's rebuild-provenance `AX-*` entry names the kept IDs whose rule changed in substance", and then lists them. I compared every kept ID against the prior contracts at `aca930622`. The list has these gaps:

- **DEL-02-03 (AX-015 names no changed IDs, and L28 omits DEL-02-03):**
  - REQ-011 split rule reversed.
    - Old: split permitted "along the recorded line — a loop whose grammar proves adversarial … requires no register amendment".
    - New: "The only recorded split line is the central-receipt grammar … a register change … No other split line shall be used."
  - REQ-003, AC-003 and VER-003 change from `D-APP-57` adoption to the `receipt-contract-v2` marker: marker-governed entries only, and prose values yield presence only.
  - OUT-001 adds central receipts.
  - OUT-003 moves to FC-1..3 golden-by-reference fixtures.
- **DEL-02-06:** AX-014 says "Five changed in reach, not in subject" but omits three larger changes. L28 does list these three.
  - OUT-001, and REQ-001 (from reading workplans and `LOOP_INIT.md` to emit Workplan/Step/Gate with gate state, down to reading `LOOP_INIT.md` for identity, entrypoint and SHA only).
  - REQ-003 (re-typed to Loop plus the historical entity).
- **DEL-02-05:** CON-004 changed substantially (similarity ratio 0.06). Its own AX-013 names it; L28 omits it.
- **DEL-01-01:** L28 lists only REQ-006. The contract's own AX-011 also names:
  - REQ-008 and AC-007 (now per-grammar, against the marker);
  - REQ-009 (no longer "valid under either candidate isolation style");
  - REQ-001, REQ-002 and REQ-012;
  - CON-001.

Every one of these changes is grounded; I checked the `Deliverables.csv` DEL-02-03 split line, SOW-013 and SOW-016 at `189f205ff`/`aca930622`. No retired ID is reused. The problem is only the completeness of the owner-facing disclosure that round-1 finding 4 asked for.

**Repair:** complete the L28 list, or restate its claim. Optionally, correct DEL-02-06 AX-014 and DEL-02-03 AX-015; that changes candidate bytes, so the act script must be rebound.

**3. NON-BLOCKING: negative control 2 no longer holds with the current verifier inputs.**
- Disposition 5 pinned the exhibit quotes to `"commit": "aca930622"`, so `verify_s2p_quotes.py` now reads them with `git show`, not from the tree.
- **Reproduction:** path-limited export of `projects/pec` at `c7719559b` with the candidates applied, and the exhibit's REM-003 carry-forward altered in the tree ("verify" changed to "VERIFY").
  - Result: `RESULT PASS 60/60`, exit 0.
- Draft L317 still says "an altered exhibit fails the source side", and `evidence/negative_controls.out` control 2 predates the pinning.
- Safety is not affected. The act preflight pins the exhibit hash (`69b646f8…f45e`), and fidelity is still checked against `aca930622`.
- **Repair:** rerun control 2 as a commit-side or quote-text alteration, or restate it.

**4. NON-BLOCKING: disposition 8 names the wrong claim IDs.**
- `VERIFIER_VERDICT_01.md` dispositions item 8 says `claims/DEL-01-06.json` "gains S187–S192".
- The added IDs are actually S192–S197 (six `contains` claims, one per `RegisteredLoop` file). S187–S191 already existed at `c0919e261` and are unchanged.

**5. NON-BLOCKING (robustness): the act's write-set inventory includes the run root.**
- `apply_s2p.py` `inventory()` walks all of `projects/pec`, and that includes the run root `execution/_Coordination/SOW_REBUILD_S2_{D}/`.
- Draft L194 says to "Record each command, exit code and output in the run root".
- If the act's output goes to a file in the run root unbuffered (`python -u` or `PYTHONUNBUFFERED`), or anything else writes there during the run, the post-write inventory sees an extra change and rolls back.
- The failure is fail-closed. Today it works only because stdout to a file is block-buffered and flushed after the inventory. The runner never exercises this setup, because its outputs go outside the exports.
- **Suggestion:** capture act output outside `projects/pec` and copy it in afterwards, or exclude the run root from the inventory.

**6. INFO: `origin/main` has moved on.**
- `git ls-remote` shows `origin/main` at `f89eb0f65`, two commits past `5aa4285c2`.
- The GitHub compare API lists one changed file: a Piping `WORK_GRAPH.md`. No pinned, quoted or claimed file is affected. The PR branch is 2 commits behind main.
- Separately, PR #960 (after `aca930622`) added an App `AgentRuns/…/RECEIPT.md`. It falls inside the `*/AgentRuns/*/RECEIPT.md` count glob. Those claims are anchored at `aca930622`, so they are unaffected; draft L19's "two files … changed" does not mention it.

## Backcheck of round-1 dispositions (against the files themselves)

1. **Repaired.** Draft L19 is correct:
   - `c76434101` is PR #961, `dfb089b8a` is PR #960 and `5aa4285c2` is PR #963.
   - My diff of `aca930622..5aa4285c2` against all 178 quote and claim sources hits only the undertaking `WORK_GRAPH.md` and App `LOOP_RECEIPTS.md`, and no pinned file.
   - The `apply_s2p.py` pin comment names `5aa4285c2`.
2. **Repaired.** L277 names `evidence/run_main/SUMMARY.out`, and L30 names "VERIFIER_VERDICT_01.md onward".
3. **Repaired.** L206 gives 28 warnings (26 XRG-013 and 2 DRB-008 for DEL-08-06 and DEL-10-13, which have no folders at `5aa4285c2`). This matches `strict_pre.out` and graph node K1.
4. **Partly repaired.** See Finding 2.
5. **Repaired.** 439 quote entries in total: 412 carry `"commit": "aca930622"`. The remaining 27 are sibling S2 production contract paths, correctly read from the post-act tree. No quote body changed except Q46. The side effect is Finding 3.
6. **Repaired.** The `--check-only` line now prints the preflight-only wording (`apply_s2p.py` L158), and row 1 at L198 describes it.
7. **Repaired.** L104 says the ruling authorizes the replacements and the workflow supplies the INIT discipline and `MODE=VERIFY`.
8. **Repaired in substance:**
   - six per-file claims were added;
   - Q46 now quotes "each verification method this contract declares", which is at exhibit L823;
   - the DEL-02-07 candidate's only byte change is the lower-case `"this contract"` at L169, and the postimage `3d1220872c55…18fb` is rebound in TARGETS;
   - the negative-controls label note was appended.
   The disposition text misnames the claim IDs (Finding 4).

## MODE=VERIFY on all seven candidates (checks.md items 1, 3, 4, 8, 9, 13, 16, 18–21)

**All seven pass: DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06, DEL-02-07.**

- **Item 1: PASS.** No pilot variance, `MIGRATION_DUAL` or source markers.
- **Item 3: PASS.**
  - All 7 `_STATUS.md` files read `INITIALIZED` at `aca930622` and at `5aa4285c2`, and all are pinned in PINNED.
  - Containment: exactly 7 differing files, all `ScopeOfWork.md`.
  - No `## Remaining` heading exists in any of the 66 PEC `_STATUS.md` files. The byte string occurs in 57 of them, but only in History text.
- **Item 4: PASS.** `PASS format=SOW_V1` ×7; frontmatter pins are `@189f205ff02d…`.
- **Items 8 and 9: PASS.** Every OUT and every AC appears in the matrix, and each AC has a VER or HUMAN_REVIEW method.
- **Item 13: PASS.** Checklists are byte-identical to `evidence/run_main`. Draft L319 hashes match, including DEL-02-07 `6c181371…`.
- **Item 16:** findings are classified in this report. Schema: none. Project content: Finding 2. Execution substrate and evidence: Findings 1, 3, 4, 5 and 6.
- **Item 18: PASS.** Checklist reruns are byte-identical.
- **Item 19: PASS.**
  - No possessive or adjacent bare upstream IDs outside blockquotes.
  - `check_sibling_ids` 92/92.
  - The only qualified citation of an S2 ID from outside S2 is DEL-02-09 → `DEL-01-01/REQ-006`, and that ID is kept.
- **Item 20: PASS.** One AC per matrix row. DEL-01-06 AC-005 appears on two rows, both with VER-005 only.
- **Item 21: PASS.**
  - The tool reports no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`.
  - `NOT_CHECKABLE` clauses: DEL-01-01 REQ-003/004/005/007/015/016, DEL-02-06 REQ-004/006/009/010 and DEL-02-07 REQ-004/006.
  - I checked each against the owner named in the cited claim (DEL-01-01 CLM-012; DEL-02-06 CLM-011 and CLM-012; DEL-02-07 CLM-014). All resolve, and match draft L217–223.

**ID counts and retirement.** Counts per prefix, line counts (245/243/291/242/243/240/292), quote counts (65/44/77/60/65/70/58) and claim counts (207/197/174/191/179/170/162 = 1280) all equal draft L45–51. The retired set equals the draft. No retired ID is reused, and new IDs continue each prefix.

**Claim grounding: at least 5 substantive claims per candidate, recomputed at the commit each names or at `aca930622`. All true.**

- **DEL-01-01**
  - CLM-009: DEL-00-01 is `CHECKING`; ADR `f63ecc27…5db5`; contract `43346150…1740`; register row contains "O-B ruled 2026-08-01", and O-B is the hexagonal option in D-PEC-72.
  - CLM-010: 12 ACTIVE PREREQUISITE consumers (E-P03..08, P10..13, P79, P80) plus DEP-07-05-005 `RETIRED`.
  - CLM-013: 11 files under `v2/src/pec_v2`; no class or name for any of the 16 types.
  - CLM-016/017: 66 `_STATUS.md` files, 4 `RETIRED`; guard `740a4a74…19ee9` has states OPEN..ISSUED and 40/64-hex SHAs; DEL-01-03 `IN_PROGRESS`, contract `986ef155…6341`.
  - CON-001: the OI-012 text.
  - CON-006: D-PEC-98 ruling "**Left open**".
- **DEL-01-06**
  - CLM-015: `loops.json` row; ruling quote at L9; rev-4 `4506597b…180e`; act `c55362095`.
  - CLM-016: `FEED_PROFILE_SURFACES` and the schema option texts.
  - CLM-017: port types.
  - CLM-018: `_REVIEW.md` Gate 5 HOLD at `INITIALIZED`; RF-001/002 RESOLVED; VALIDATION "Ran 19, OK"; `ccd9a2178` merges the DEL-01-06 slice.
  - TBD-003: `_repository_path` accepts `./`, `//`, a trailing `/`, a leading space and `C:x`.
  - AX-007: exactly the six `RegisteredLoop` files.
  - CLM-009: `MEMORY.md` has no row.
- **DEL-02-03**
  - CLM-017: six ledgers; the marker in exactly App, Piping and PEC; the PEC marker comment at L1865; one central RECEIPT.md, `eef5434b…dfa8`, at both `aca930622` and `d61981ee2`.
  - CLM-019: Receipt 197 heading.
  - CLM-011: DAG rows E-N03, E-P21 and E-P05 verbatim.
  - CLM-007: split line per `Deliverables.csv`.
- **DEL-02-04**
  - CLM-014: 16 STATUS.json (all Piping); 8 RUNTIME_SUMMARY.json (Root 2, Piping 3, Runtime 3); 12 with no schema and 4 distinct values; all RUNTIME_SUMMARY files `chirality-runtime-summary/v1`; 954/104 at `8007c5927`.
  - CLM-016: `ARCHIVE_INDEX.json` tag and full SHA; 13 PEC STATUS.json at the tag; commits `34134e093` and `d9385479e`.
- **DEL-02-05**
  - CLM-016, every count: 253 `Dependencies.csv` (66 PEC); 34 `WORK_GRAPH.json`; 18 with extension columns; 65/66 CRLF; 6 with RETIRED rows; 57 with EdgeID; nodes 31 / edges 17; PEC's one file and its keys; at the tag 979 (728 root AgentRuns), 198 against 33 beneath `execution`, PEC 2.
- **DEL-02-06**
  - CLM-015: 13 `LOOP_INIT.md` (6 live, 3 AgentRuns, 2 Piping archive, 2 proposals); headings; "Enter through" in PEC, App and Piping only; Root `CURRENT_WORKPLAN.md`; Piping `loop/` has 6 workplans.
  - CLM-016: `LOOP_INIT.md` `c97d49ff…821b`; `loop/` holds exactly 2 files; 5 workplans; `_DomainEngines/pec` absent.
- **DEL-02-07**
  - CLM-011: 4 working manifests with their schemas and `status_glob` values; 5 `*_harness/adapter.yaml`.
  - CLM-010: no `v2/src` mention.
  - CLM-018: `adapter_project.py` `652b1741…c9bc` applies `exclude_globs`; README quote.
  - Part B verbatim (below).

**Scope.** No requirement goes beyond the ledger rows, the `Deliverables.csv` rows, PRD v2.4, and the ruled D-PEC-96 or accepted SCA-005 §B7 records that the brief makes part of "current".

**CON items.** None is resolved by assumption. Where a candidate chooses, it follows accepted PRD v2.4 per-profile text over stale register wording, and says so: DEL-02-03 CON-004/REQ-015, DEL-02-04 CON-004/REQ-014, and the DEL-02-04 REQ-001 interim no-archive reading.

## Packet review

- **Part B fidelity: PASS.**
  - Candidate L141/149/157/165 each equal one whole exhibit line: L787, L799, L811 and L823.
  - The gates at L143/159/167 equal exhibit L783/807/819; the gate at L151 equals L795.
  - Exhibit hash `69b646f8…f45e` at `aca930622`, `5aa4285c2` and HEAD.
  - The landing table (L71–78) matches the candidate lines and IDs.
  - CLM-016 and AX-011 state that the gates still bind.
- **Lifecycle answer: PASS.** No transition is proposed and the act refuses to run if a `_STATUS.md` differs. The WORKFLOW L105 quote, checks item 3 and standard §8 (L198) are accurate.
- **Grant and binding: PASS.**
  - `apply_s2p.py` `5efb6f5399cdb9805f7a58f7b70ffe6d312730d64623129b658a4d9943350b6d`: 7 TARGETS and 23 PINNED, recomputed at `aca930622`, `5aa4285c2` and `c7719559b`, with 0 mismatches.
  - Postimages equal the candidate files, and every hash appears in the draft.
  - The failure semantics as coded match draft L174–179.
- **Seven dependency EvidenceQuotes:** all raw substrings of the postimages. They are the only PEC rows whose `EvidenceFile` is an S2 contract.
- **Add-on M: correct.**
  - DEL-01-06 `MEMORY.md` `035ecb86…0a3f` exists with no row; the other six are absent at both commits.
  - Template `5a9564f4…6a5a` has the single `{{DEL-ID}}` slot.
  - D-PEC-96 ruling item 5 agrees.
- **Provenance hashes verified at `5aa4285c2`:**
  - D-PEC-94 `b6814e90…5a6b`, with the quote
  - `Propagation_Plan` `50cd0b1d…1350`
  - SCA-006 IA `93253b7d…b691`
  - register `e845e1bb…48e2`, with no D-PEC-100 row
  - D-PEC-96 ruling `852057f0…399e`
  - D-PEC-98 ruling `039dc7e2…8361`
  - notice `8829ac84…64af`, whose L18 carries the quoted phrase
  - D-GOV-48 notice `15ea36ee…e8e6`
  - `AGENT_WORKING_ITEMS` `9ae4bea2…9665`
  - `validate_decomposition_registers.py` `869df1d5…57ee`
  - holds `f877d931…c741` (header only)
  - preflight `b1712e4b…cd0e`
  - `workflows/index.json` `2bfa2c5f…dafb3`
  - `execution.json` `4ad8b7eb…a26d`
  - tools `f0f10590…fecfe`, `bfb64dc9…0109`, `22ef57e0…ae16a` and `61a34722…0389`
- **Commit relations:** `22502e059` is PR #957, `73ed349ed` is PR #950, and `c55362095` and `189f205ff` are ancestors of `aca930622`. The S2 graph row is byte-identical at `aca930622` and `5aa4285c2`. The S4 set excludes all seven deliverables.
- **Owner questions: appropriate.** There is no CHECKING prompt, no REVISE adoption question, and nothing is pre-decided.

## Commands run (read-only; scratch area under the session scratchpad)

1. **Runner.** `rsync` of PREP (excluding `__pycache__`) to `scratchpad/v2/prep`, then `TMPDIR=scratchpad/v2/tmp zsh prep/run_s2p_checks.sh <worktree> c7719559b …/v2/prep …/v2/out`: **exit 0, `OVERALL PASS`**.
   - act: check-only 0, apply 0, rerun refuses 1
   - containment: 7 files, all `ScopeOfWork.md`
   - validate, checklist and boundary: PASS ×7
   - quotes: `RESULT PASS 460/460`
   - state claims: `RESULT PASS 1280/1280`
   - sibling IDs: `RESULT PASS 92/92`
   - consequence scan: `SUMMARY stale=31 kept=32`
   - strict, harness and receipts identical before and after (exit 1, 0 and 0)
   - whitespace: PASS
   - fault injection: `RESULT PASS 7/7`
   - Every output is byte-identical to `evidence/run_main/*`, except `SUMMARY.out` (basis line), `containment.out` and `receipts_{pre,post}.out` (export paths only).
   - The runner deleted both exports; `tmp/` is empty.
2. **`shasum -a 256 -c SHA256SUMS`.**
   - In the worktree at the start of the review: all OK (exit 0).
   - On `git archive c7719559b` of PREP: exit 1, pyc missing (Finding 1). The archive was deleted.
3. **Reliance preflight.** `pec_reliance_hold.py` (path-limited export; script and register hashes above) with `candidate-validation` and `historical-read-only-inspection` on all 7 `ScopeOfWork.md` targets: `ALLOW`, exit 0 ×14. `evidence/reliance_hold_preflight.out` shows 21 `ALLOW`.
4. **Negative-control reproduction (Finding 3):** `verify_s2p_quotes.py --only DEL-02-07` on an altered-exhibit export gave `RESULT PASS 60/60`, exit 0. The export was deleted.
5. **Git and ad hoc checks:**
   - `git ls-remote origin` and a GitHub compare of `5aa4285c2...f89eb0f65`
   - `git diff c0919e261 HEAD` on the draft, script, candidates, evidence, claims and quotes
   - TARGETS/PINNED recomputation at 3 commits
   - ID and meaning comparison against the prior contracts at `aca930622` (similarity ratios, then manual reading)
   - matrix, QA 20 and QA 19 scans
   - the Part B whole-line match
   - all the corpus censuses listed above

## Hashes relied on

**Draft:** `a2c324d39972387677b24da4d07c34e4847bb4e368168c872693b51f087b7927`

**Postimages (equal to TARGETS and SHA256SUMS):**

| Deliverable | SHA-256 |
|---|---|
| DEL-01-01 | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| DEL-01-06 | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| DEL-02-03 | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| DEL-02-04 | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| DEL-02-05 | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| DEL-02-06 | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| DEL-02-07 | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |

**Preimages:** as in draft L108–114, verified at `aca930622`, `5aa4285c2` and `c7719559b`.

**Scripts:**
- `apply_s2p.py` `5efb6f53…d6d350b6d`
- `verify_s2p_quotes.py` `be74a06c…d6af`
- `verify_s2p_state_claims.py` `eb85c15f…8545`
- `check_sibling_ids.py` `e8c0f2bd…a091`
- `test_apply_s2p.py` `9a680ba9…3908`
- `run_s2p_checks.sh` `6b2845d9…e8b7`
- `scan_external_quotes.py` `e11fa9ad…94b8`

**Basis, identical at `189f205ff`, `aca930622` and `5aa4285c2`:**
- `SOFTWARE_DECOMP.md` `9374c21f…8eb1`
- `Deliverables.csv` `94ee5d18…9805`
- `ScopeLedger.csv` `1d24a4b8…916e`
- `ContextBudgetQA.csv` `93b0bb07…4c7c`
- `PRD.md` `ae49b806…3fbe`
- `loops.json` `fd342b4f…53d7`
- `loops.schema.json` `104ed648…b143`

**Other sources:** exhibit `69b646f8…f45e`; guard `740a4a74…19ee9`; undertaking `WORK_GRAPH.md` `5cee83f9…6788` at `5aa4285c2`.

---

## Manager dispositions (WORKING_ITEMS, 2026-09-26)

No candidate contract byte changes in this round.

1. **Repaired.** The local `__pycache__/` is removed and `SHA256SUMS` is regenerated from `git ls-files` of the prep folder (tracked files only). `shasum -a 256 -c` is rerun on a `git archive` of the new head; the result is recorded in the return.
2. **Repaired.** Draft Method now gives the complete list of kept IDs whose rule changed, per this verdict's comparison, and no longer says each rebuild-provenance entry names them. The candidates' own `AX-*` entries are not edited, to avoid re-binding seven reviewed postimages for wording; the draft discloses which entries are partial.
3. **Repaired.** New control 2b (appended to `evidence/negative_controls.out`): reading exhibit quotes Q38 and Q40 at the first parent of the `D-PEC-99` act merge (`cb85f85d1`), where the exhibit does not exist, fails both on the source side (`RESULT FAIL 58/60`). The draft names 2b as the replacement for the tree-side control 2.
4. **Repaired.** Verdict 01 disposition 8 now names S192–S197, with a correction note.
5. **Repaired.** `apply_s2p.py`'s inventory leaves out its own directory (the run root); a new fault-injection case (8) writes evidence into a run root inside the tree during the act and requires the apply to succeed. The draft's generation-method and verification text say so. Script rebound.
6. **Repaired.** Draft source state names every PR since `aca930622` through `2b5389a97` (PR #967), including #962 (the `D-PEC-101` preparation) and the App central `RECEIPT.md` added by #960; a new consequence bullet explains why the `D-PEC-101` draft shares no path with this act and how either ordering is absorbed.
