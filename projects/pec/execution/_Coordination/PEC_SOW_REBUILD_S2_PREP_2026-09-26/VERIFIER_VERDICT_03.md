# VERIFIER_VERDICT_03: S2 Scope of Work rebuild packet (provisional D-PEC-100), PR #964 head 3be700545

Transcribed verbatim by WORKING_ITEMS from the final report of a fresh read-only `pec-reviewer` TASK (Opus 5.5, `claude-opus-5-5`, high reasoning; host-reported model; role instruction-asserted), 2026-09-26. This reviewer took no part in rounds 1 or 2. Dispositions follow the transcription and are the manager's.

---

**Verdict: PASS WITH NOTES.** Nothing blocks.

- **Round-2 blocker is repaired.** On a `git archive` of the head, `shasum -a 256 -c SHA256SUMS` passes, and the manifest lists exactly the tracked files.
- **No candidate, claim or quote byte changed** since `c7719559b`.
- **The act script's pins match.** TARGETS and PINNED equal recomputed hashes at `origin/main` (`2b5389a97`), at `aca930622` and at the head.
- **My runner rerun passes:** `OVERALL PASS`, fault injection 8/8.
- **Findings:** two NON-BLOCKING (the owner-facing changed-ID disclosure, and the location-keyed inventory exclusion) and two INFO.

**Reviewer.** Fresh read-only TASK (pec-reviewer). The host reports the model as Opus 5.5 (`claude-opus-5-5`); the role is instruction-asserted. I authored nothing here and took no part in rounds 1 or 2.
- The worktree is untouched: `git status --short --ignored` on PREP is empty, there is no `__pycache__`, and HEAD is still `3be70054569ea8a22cdfd3072b2143c5243194d6`.
- The remote branch head equals the local head, and remote `main` is `2b5389a97`.
- All Python ran with `PYTHONDONTWRITEBYTECODE=1`. Every write went under the session scratchpad `.../scratchpad/r3/`, and the large copies there are deleted.

**Instructions read:**
- Root `AGENTS.md` `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `agents/AGENT_TASK.md` `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`

**Relayed amendment (REVISE): complied with.**
- Draft L16 records the amendment as evidence.
- L27 is the one-line disclosure.
- L153 appears only under Limits ("grants none of … adoption of `MODE=REVISE`").
- None of the owner questions (L160–163) concerns REVISE.

## Findings

### 1. NON-BLOCKING: the "complete list" of kept IDs whose rule changed is still incomplete, and the AX-partiality note understates

**Where:** `PREP/DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md` L28–35, plus L62.

L28 presents the list as "the complete list, from a comparison of every kept ID with the prior contracts at `aca930622`". I compared every kept ID's defining text at `aca930622` with the postimage (similarity ratio first, then manual reading). The list covers exactly the gaps that verdict 02 named, but these remain.

**Companion criteria that the contracts' own AX entries name, but the list omits:**
- DEL-02-06 `AX-014` names `AC-004`/`VER-004`, `AC-005`/`VER-005` and `AC-012`/`VER-012` with their REQs. The list gives only the REQs.
- DEL-02-07 `AX-014` names `AC-001`, `AC-006`, `VER-001` and `VER-006` as narrowed. The list gives only `OUT-001`, `REQ-004` and `REQ-006`.
- DEL-01-01 `AX-011` names "REQ-001, REQ-002, REQ-012 and their criteria". The list omits the criteria.

For DEL-02-03, by contrast, the list does include `AC-003`/`VER-003`. The convention is therefore inconsistent across candidates.

**Substantive changes named nowhere:**
- **DEL-01-01 `AC-005`.**
  - Old: "No presence-tier entity … and a fixture carrying runtime-daemon user-data state is not representable".
  - New: adds "a RunRecord is representable from each source REQ-006 names … including a `MEMORY.md` run-index entry".
- **DEL-02-03 `AC-011`.**
  - Old: a split "along the recorded adversarial-grammar line" is permitted.
  - New: "no split is taken under this contract".
  - This follows the listed `REQ-011` reversal.
- **DEL-02-03 `CON-002`.**
  - Old: the loop set is "not fixed at the level of accepted truth".
  - New: it is fixed by the loop registry, and the open item narrows to the dependency edge.
  - `TBD-003` changes likewise.
- **DEL-02-06 `VER-009`.** It now also asserts a normalized entrypoint and a full-length procedure SHA, and inspects for guard-evasion encoding.
- **DEL-02-06 `TBD-003`.** The Workplan/Step/Gate field sets become Loop facts plus historical Workplan/Step facts.

**The parenthetical at L28 understates which AX entries are partial.** It reads "(DEL-02-03's `AX-015` names none, and DEL-02-06's `AX-014` names only part)". Two more entries also name none of their listed changes:
- DEL-01-06 `AX-012` does not name `REQ-001` or `REQ-005`;
- DEL-02-04 `AX-012` does not name `REQ-001` (it lists categories only).

**L62 contradicts L28.** L62 says "the full account is in each contract's rebuild-provenance `AX-*` entry and in the drafter returns".
- L28 itself concedes that the AX entries are partial.
- No drafter return is tracked anywhere in the repository. Only `S2P_DRAFTER_BRIEF.md` and `S2P_SOW_REBUILD_PROPOSAL.md` exist under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`.
- L97 ("Confirmed by the drafters") and L235 ("drafter returns; the verifier re-checks") rest on the same unrecoverable returns. `projects/pec/AGENTS.md` asks that required execution provenance stay recoverable.

Each of these changes is grounded, and none reuses a retired ID. The retired sets equal draft L54–60. Candidate validity is unaffected; the issue is only the accuracy of an owner-facing disclosure.

**Repair (draft only, no candidate bytes):**
- Either restate L28 as "the principal changes; each listed REQ's AC/VER changes with it" and add the missing items, or complete the list.
- Correct the parenthetical.
- Point L62 at the L28 list rather than at the AX entries and the returns, or save the drafter returns in the prep folder.

### 2. NON-BLOCKING (robustness): the new inventory exclusion follows the script's location, not a declared run root

**Where:** `PREP/apply_s2p.py` L113 (`SELF_DIR = Path(__file__).resolve().parent`), L120–121 and the closing line at L195.

**Tests.** I copied the bound script into a path-limited scratch export of `projects/pec` at `2b5389a97` and ran seven layouts. Each wrote files during the first `os.replace`. Results:

| Case | Layout | Exit | Targets | Reason |
|---|---|---|---|---|
| T1 | Script outside the tree; evidence written into `_Coordination/SOW_REBUILD_S2_T/` | 1 | pristine | `added=[…act.log]` |
| T2 | Script run from PREP (in the tree); evidence written to a separate run root | 1 | pristine | fail-closed (round-2 finding 5 behaviour returns) |
| T3 | Script in `projects/pec/execution` (ancestor of the targets) | 1 | pristine | `missing=[targets]` |
| T4 | Script in `_Coordination/` (ancestor of the pinned exhibit), plus a stray write | 1 | pristine | `pinned file changed: …EXHIBIT_MOVED_ITEMS.md` |
| T5 | Script in the run root; writes both in the run root and at `docs/stray.md` | 1 | pristine | `added=['projects/pec/docs/stray.md']` |
| T6 | Script in the run root; writes only inside it | 0 | applied | by design |
| T7 | Script in `projects/pec/tools/x` (frozen corpus); creates a file there | 0 | applied | see below |

In T7 the closing line reads "write set = grant (0 created, 7 modified, 0 removed under projects/pec)". So the exclusion hides a write only inside the directory that holds the script, and only when that directory holds no target or pinned file. Any directory that is an ancestor of a target or pin fails closed (T3, T4).

**Answers to the brief's questions:**
- **Could the exclusion hide a real write outside the run root?** Only if the script is run from somewhere other than the bound location (T7).
  - Draft L181 binds the invocation to `…/_Coordination/SOW_REBUILD_S2_{D}/apply_s2p.py`, which is inside the default-writable `_Coordination/**`.
  - Check 11 (`git diff --name-status origin/main...HEAD`) would catch any out-of-grant path.
- **What if the script runs from a directory that is not the run root?** Run-root evidence then trips the check, and the act rolls back fail-closed (T1, T2).

**Wording.** Even in the intended case (T6 and case 8), "0 created … under projects/pec" is literally untrue when evidence files are created in the run root.

**Test 8.** It is correct and discriminating. It loads a copy of the script from `rr`, so `SELF_DIR` is `rr`; it writes on each rename, before the post-write inventory; and it passes. T1 is its negative counterpart and fails as expected.

**Suggestion (optional; requires rebinding the script):**
- Assert that the script's path relative to `repo` matches `projects/pec/execution/_Coordination/SOW_REBUILD_S2_*`, or take the run root explicitly.
- Reword the closing line to say "outside the run root".

### 3. INFO: control 2b tests source presence, not source-content alteration

**Where:** draft L207 and `evidence/negative_controls.out`.
- The draft describes it accurately.
- I reproduced it: Q38 and Q40 re-anchored to `cb85f85d1` (which is `22502e059^1`; the exhibit is absent there) gave `RESULT FAIL 58/60`, exit 1, with byte-identical FAIL lines. The unmodified run gave `RESULT PASS 60/60`.
- Content sensitivity on the source side follows from the substring construction of `verify_s2p_quotes.py`. No action needed.

### 4. INFO: carry-forward for the manager

When `VERIFIER_VERDICT_03.md` is added:
- regenerate `SHA256SUMS` from `git ls-files` of PREP minus itself;
- rerun `shasum -c` on a `git archive` of that new head.

## Disposition backcheck (against the files)

**Round-2 dispositions:**

1. **Repaired.**
   - `git archive 3be700545 <PREP>` followed by `shasum -a 256 -c SHA256SUMS`: exit 0, 85/85 OK.
   - `diff <(git ls-files . | grep -v '^SHA256SUMS$' | sort) <(awk '{print $2}' SHA256SUMS | sort)`: identical (86 tracked files, including `SHA256SUMS`).
   - No `__pycache__` is tracked or present.
2. **Partly repaired.**
   - Every ID that verdict 02 named was added.
   - The draft no longer claims that each AX entry names the changes.
   - The "complete list" claim and the partiality note are still inaccurate (Finding 1).
3. **Repaired.**
   - Control 2b is appended.
   - `cb85f85d1` equals `22502e059^1`, and `git cat-file -e` confirms the exhibit is absent there.
   - Reproduced (Finding 3). Draft L207 names 2b as the replacement.
4. **Repaired.**
   - Verdict 01 disposition 8 now reads S192–S197, with a correction note.
   - `claims/DEL-01-06.json` holds 191 claims at `c0919e261` (last is S191) and 197 at `97cc398b7` and at HEAD.
   - S192–S197 are `contains "RegisteredLoop"`, one per file; S187 and S191 are unchanged.
5. **Repaired.**
   - `SELF_DIR` exclusion, docstring (L26–28), draft L188 and L204.
   - Case 8 passes, and the script is rebound (`f820e581…74e4e5` at draft L178).
   - Robustness note in Finding 2.
6. **Repaired.**
   - The first-parent merges `aca930622..2b5389a97` are exactly #961 `c76434101`, #960 `dfb089b8a`, #963 `5aa4285c2`, #965 `f89eb0f65`, #962 `0883c2108` and #967 `2b5389a97`.
   - Of the 1,213 changed files, the only ones intersecting claim, quote or count-glob sources are:
     - the undertaking `WORK_GRAPH.md`;
     - App `loop/LOOP_RECEIPTS.md`;
     - App `AgentRuns/APP-LIFECYCLE-DEPS-2026-09-26/RECEIPT.md`, via the `*/AgentRuns/*/RECEIPT.md` glob.

     This is exactly what draft L19 says. Every claim is commit-anchored.
   - **D-PEC-101 bullet (L99) verified:**
     - K1 changes 32 files. They include the `_DEPENDENCIES.md` of DEL-02-01..06, 02-08 and 02-09, and the `Dependencies.csv` of DEL-04-03, 08-03, 08-06, 09-06, 10-03 and 10-13. None of these is a TARGET or PIN.
     - Among S2 folders, K4 changes only `_CONTEXT.md` and `_REFERENCES.md`.
     - No D-PEC-101 `*.py` references `ScopeOfWork`.
     - The D-PEC-101 draft (L109, L357) expects 0 `DRB-008` after K1.
     - The candidates' "revision 1.5" statements are observations at `aca930622`.

**Round-1 disposition 8 (corrected):** verified, as item 4 above.

## Item-by-item on the brief

- **No candidate byte changed.** `git diff --stat c7719559b HEAD -- PREP/candidates PREP/claims PREP/quotes` is empty.
  - The PREP diff since `c7719559b` touches only:
    - the draft;
    - `SHA256SUMS`;
    - verdict 01 (one line);
    - verdict 02 (new);
    - `apply_s2p.py` (docstring, pin comment, `SELF_DIR`);
    - `test_apply_s2p.py` (c8);
    - evidence (`negative_controls.out`, plus `run_main/{SUMMARY,containment,receipts_pre,receipts_post,test_apply_s2p}.out`).
  - The PR's diff against `origin/main` touches only PREP and the two S2P briefs.
- **TARGETS/PINNED:** 7 targets and 23 pins recomputed at `origin/main` `2b5389a97`, at `aca930622` and at HEAD, with 0 mismatches. Postimages equal the candidate files.
- **Draft claims re-read in full.** Also verified:
  - no D-PEC-100 row at `2b5389a97` (register `e845e1bb…48e2`);
  - all seven `_STATUS.md` read `INITIALIZED` at `aca930622` and at `2b5389a97`;
  - every basis hash at L223–230 and L21 recomputed at `2b5389a97`;
  - the negative-control text matches the evidence and my reproduction.

**Fresh `MODE=VERIFY` spot-checks, all true at `aca930622`:**

- **DEL-01-06:**
  - CLM-001: the `SOW-094` statement, its SourceRef and its DecisionRef.
  - CLM-004: PRD L256 Loop row; decomposition §9 L640.
  - CLM-006: `DEP-02-07-003`, `DEP-03-01-007` and `DEP-09-02-006`, each with its exact Statement; all ACTIVE, EXECUTION, PREREQUISITE, PENDING, INITIALIZED and PROPOSAL, with EdgeIDs E-N16, E-P18 and E-P62. These are the only rows outside DEL-01-06's own register that target it.
  - CLM-008: PRD §16.3 item 3, L601–614, verbatim.
  - CLM-012: all 15 PhaseHints.
  - CLM-014: `D-PEC-78_…/PACKET.md` (`426dba04…5d17`) §4.2, L129–132, verbatim across line wraps.
  - CLM-020: the second sentence of the `SOW-094` Notes cell; §9 L652.
  - Placement: three ANCHOR rows, and `_DEPENDENCIES.md` "no upstream predecessors (root node)".
- **DEL-02-04:**
  - CLM-004: register row, QA row (`S,LOW,None`) and §5 table row.
  - CLM-005: DL-4 Decision and Rationale cells (L683).
  - CLM-006: PKG-02 charter (L392).
  - CLM-007: all three rows' fields. The `DEP-02-04-003` EvidenceQuote is a raw substring of the DEL-01-01 postimage (count 1).
  - CLM-009: `DEP-03-01-011` fields; DEL-03-01 is the only external register referencing DEL-02-04.
  - CLM-010: PhaseHints, including DEL-01-02 P3.
  - CLM-012: PEC-K-05 (L232), the §16 item 2 premise and the RunRecord phrase.
  - CLM-015: schema description strings, `loops.json` content, register "RULED A / EFFECTIVE ON MERGE", and the ruling and proposal quotes.

## Commands (read-only; scratch under the session scratchpad)

1. **Archive and manifest check.**
   - `git archive 3be700545 <PREP> | tar -x`, then `shasum -a 256 -c SHA256SUMS`: exit 0, 85 OK.
   - The `ls-files` comparison: identical.
2. **Pin recomputation.** `pins.py` (AST extraction of TARGETS/PINNED plus `git show`) at `origin/main`, `aca930622` and HEAD: `mismatches 0` ×3.
3. **Runner.** `TMPDIR=…/r3/tmp zsh prep/run_s2p_checks.sh <worktree> 2b5389a970847850ea05762ca9ca35ac9fbaacb4 …/r3/prep …/r3/out`, with `prep` copied from the `git archive` of HEAD (tracked files only): **exit 0, `OVERALL PASS`**.
   - act: check-only 0, apply 0, rerun refuses 1
   - containment: 7 differing files, all `ScopeOfWork.md`
   - validate, checklist and boundary: PASS ×7
   - quotes: `RESULT PASS 460/460`
   - state claims: `RESULT PASS 1280/1280`
   - sibling IDs: `RESULT PASS 92/92`
   - consequence scan: `SUMMARY stale=31 kept=32`
   - strict, harness and receipts identical before and after (exit 1, 0 and 0)
   - whitespace: PASS
   - fault injection: `RESULT PASS 8/8`
   - All 52 outputs are byte-identical to `evidence/run_main/*`, except `containment.out` and `receipts_{pre,post}.out`, which differ in export path only. `SUMMARY.out` is identical. The runner removed its exports; I removed `tmp/`.
4. **Edge cases.** `edge.py` T1–T7 on a path-limited export (Finding 2). The export is deleted.
5. **Control 2b reproduction.** `verify_s2p_quotes.py --only DEL-02-07` with Q38 and Q40 anchored at `cb85f85d1`: `RESULT FAIL 58/60`, exit 1. Unmodified: `RESULT PASS 60/60`.
6. **Reliance preflight.** `pec_reliance_hold.py` (`b1712e4b…`, register `f877d931…`) with `candidate-validation` and `historical-read-only-inspection` on all 7 targets: `ALLOW`, exit 0 ×14.
7. **Git checks.**
   - `git diff --check origin/main...HEAD`: exit 0.
   - `git diff --check c7719559b HEAD -- PREP`: exit 0.
   - `origin/main` is an ancestor of HEAD.
   - `git ls-remote`: branch at `3be700545`, main at `2b5389a97`.
8. **ID-meaning comparison.** `idcmp.py`, `idcmp2.py` and `show.py` (difflib ratios, then manual reading) over all kept IDs at `aca930622`.

## Hashes relied on

**Draft and scripts:**
- Draft `f8c621a8fea4436ec0c031efb36581a2cec6f67197bbf056ed7d6b692d48864c`
- `apply_s2p.py` `f820e5818b94a95fafe72829a3fc22e4f318a0e3c8c4a87290df5ec61074e4e5`
- `test_apply_s2p.py` `ee460348e5841f8867b7513b7b150d8ce4ac0366c005de0a58ee24a360ca5dfb`
- `run_s2p_checks.sh` `6b2845d91b53de8089c1986b3e72cffbac064ff418c908fb4d24939289a5b8e7`
- `verify_s2p_quotes.py` `be74a06c74457256e12f0573837f8d35e41ee276d76b2e0dc660c376598854af`
- `verify_s2p_state_claims.py` `eb85c15f24ed79b9234a2ab3dd746bbaaa499ea7566bd99efa2e061d87dd8545`
- `check_sibling_ids.py` `e8c0f2bddbc443cd3a5e7f0c2c96c270e626c1d8e4612a061e0cf37f8e099a91`
- `scan_external_quotes.py` `e11fa9ada53490a23e66da4374d8a38b29a90f8ee0904d77ea5355c9584e94b8`

**Postimages (equal to TARGETS and SHA256SUMS; unchanged since round 2):**

| Deliverable | SHA-256 |
|---|---|
| DEL-01-01 | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| DEL-01-06 | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| DEL-02-03 | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| DEL-02-04 | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| DEL-02-05 | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| DEL-02-06 | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| DEL-02-07 | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |

**Basis at `2b5389a97` (full hashes recomputed):**
- Exhibit `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`
- Register `e845e1bbbc8e4f97edd7082197c37061d5c2c4170eeafaa966f74c29fd3a48e2`
- Undertaking `WORK_GRAPH.md` `5cee83f9ea1c98c8c8790784688cb2da68431104aa63b29c9b356b725d8a6788`
- D-PEC-94 `b6814e902c23…1e5a6b`
- D-PEC-96 ruling `852057f0ff69…fb399e`
- D-PEC-98 ruling `039dc7e2d11d…cd8361`
- `Propagation_Plan.md` `50cd0b1d91ea…bf91350`
- SCA-006 IA `93253b7d016d…ecb691`
- `Amendment_Actions_CP2.csv` `7bb3bada88ed…2a09987`
- PEC notice `8829ac840f74…eff64af`
- Guard `740a4a741221…e3e19ee9`
- `validate_decomposition_registers.py` `869df1d54846…cb9157ee`
- `write_status.sh` `1857ad5933ed…2d97bc`
- `MEMORY_TEMPLATE.md` `5a9564f4663b…1c6a5a`
- DEL-01-06 `MEMORY.md` `035ecb8686d7…cf30a3f`
- `workflows/index.json` `2bfa2c5faae1…ccdafb3`
- `scope-of-work/WORKFLOW.md` `84dadde4c573…cebc2b`
- Standard `26c8254aaf2e…741433c`
- `AGENT_WORKING_ITEMS.md` `9ae4bea25bd9…601799665`
- Holds `f877d9316c7d…ad741cbc`
- Preflight `b1712e4b6e9f…b548cd0e`
- D-PEC-78 `PACKET.md` at `aca930622`: `426dba045d63…33e5d17`

---

## Manager dispositions (WORKING_ITEMS, 2026-09-26)

No candidate, claim or quote byte changes in this round.

1. **Repaired.** The Method list now says what it is (every kept ID compared at `aca930622`, verdicts 02 and 03; a listed requirement's matrix-linked `AC-*`/`VER-*` change with it unless noted), adds DEL-01-01 `AC-005`, DEL-02-03 `AC-011`, `CON-002` and `TBD-003`, DEL-02-06 `TBD-003` and `VER-009`, and DEL-02-07's named `AC`/`VER` companions, and corrects the partiality note (DEL-02-03 `AX-015`, DEL-01-06 `AX-012` and DEL-02-04 `AX-012` name none; DEL-01-01 `AX-011` and DEL-02-06 `AX-014` name some). The "What each rebuild changes" lead-in now points to that list and to the contracts, not to untracked drafter returns. The consequence bullet now lists the fifteen contracts the scan flags, from `evidence/run_main/scan_external_quotes.out`, instead of "confirmed by the drafters", and names DEL-02-01's own `REQ-002` separately. The QA 21 note now cites verdicts 01–03, which checked the hand resolutions against the requirement text. The drafter returns are summarized in the manager return; they are not tracked.
2. **Repaired.** `apply_s2p.py` now refuses at preflight if its own directory lies inside `projects/pec` anywhere other than a run root (`projects/pec/execution/_Coordination/SOW_REBUILD_S2_*`), so the inventory exclusion can cover only a run root; run from outside the repository it excludes nothing. The closing line now says "under projects/pec outside the run root". New fault-injection case 9 places the bound copy in `projects/pec/tools/x` and requires preflight exit 1 with nothing written. Script rebound.
3. No action (INFO).
4. Done: `SHA256SUMS` regenerated from `git ls-files` of the prep folder after this verdict was added, and `shasum -a 256 -c` rerun on a `git archive` of the new head (recorded in the return).
