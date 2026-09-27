# VERIFIER_VERDICT_01 — D-PEC-104 act (MODE=VERIFY)

**Verdict: PASS WITH NOTES.** Nothing is blocking. There are 0 BLOCKING, 0 NON-BLOCKING and 9 NOTE findings.

- **Reviewed commit:** `1cc8ce997900ae6cec4514b475584a62f78d872c` on branch `claude/pec-d104-s1-sow-act`, in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act`.
- **Base:** `origin/main` `16010b4ca9ab6c00247593177e1a8defa97a3ab6`. `git ls-remote` confirms it is the live `refs/heads/main`, and it is the merge-base.
- **Act commits:**
  - `053ca4e22` — run root, preconditions, dispatch preflight, baselines, check-only
  - `1e33df616` — the act and the rely preflight
  - `1cc8ce997` — verification rows 2–13, rerun and negative controls
- **Reviewer:** a fresh read-only TASK (Type 2). I authored nothing in this act or its preparation.
- **Host-reported model:** Opus 5.5 (`claude-opus-5-5`). The reasoning effort is set by instruction and is not visible to me.
- **Date:** 2026-09-27. Interpreter: Python 3.13.7.

This verdict records no ruling. It makes no lifecycle, CHECKING, ISSUED, acceptance, readiness or reliance claim, and it prompts nothing about CHECKING.

## Instruction and authority files loaded (SHA-256, read in the act worktree; each is identical at `origin/main`)

| File | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` |
| `_DECISIONS/D-PEC-104_RULING_2026-09-27.md` | `bb88deb5a9850f2444b99740d5abcf9b127901c2f1e5185d4a75a2f1232ec1bd` (as expected) |
| `_DECISIONS/D-PEC-104_s1_sow_currency_proposal_2026-09-26.md` | `35301840d56f9972b0d7ca3c85dae0ee80ffdf5509c44586f219a47ff6545f51` (as expected) |
| `_DECISIONS/_REGISTER.md` | `bf1366b22aa47b5f0cd56ffb54e3dd73937f6221f001a67e598f93ffaec10054` |
| `D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` | `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e` |
| Brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md` | `b60d21dba14d0a6805b74a611eab057d6318f952e31f8c934247b237d590296a` |

I also consulted these files; their hashes match the abbreviations in the proposal:
- `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`: `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`
- `tools/scope_of_work/validate_scope_of_work.py`: `f0f10590…fecfe`
- `derive_review_checklist.py`: `bfb64dc9…0109`
- `check_boundary_owner_resolution.py`: `22ef57e0…ae16a`
- `common.py`: `61a34722…0389`

I read the prep folder's `VERIFIER_VERDICT_*` files for orientation only. None of their findings is adopted here.

## Item 1 — Basis: **PASS**

- **Ruling and register row on `origin/main`.** `git show origin/main:…/_REGISTER.md` line 121 holds the `D-PEC-104` row with status cell `RULED A / PART B, SCOPE AND Q4 CONFIRMED / M / EFFECTIVE ON MERGE`. The row cites the proposal SHA `35301840…6f51` and act script `26b677a7…625f`. The ruling file hashes `bb88deb5…1bd` at `origin/main`, and its last change is `30bed5c89`, inside PR #1005 (merge `16010b4ca`).
- **Bound script.** `shasum -a 256` gives `26b677a70d5d51041f0d49dd34e9a09685120f136071e906d7ff702719f1625f` for both the run-root `apply_s1p.py` and the prep `apply_s1p.py`.
- **Script structure and the manager's write-set decision.** Verified by reading the script:
  - `TARGETS` has 12 entries. Parsed programmatically, it equals the proposal's grant table (full 64-hex preimage and postimage) exactly.
  - `PINNED` has 35 entries: 9 basis files, the 2 S4 postimages, 12 `_STATUS.md` and 12 `Dependencies.csv`.
  - `inventory()` walks `projects/pec` and prunes `SELF_DIR`, the script's own directory.
  - Preflight refuses when `SELF_DIR` is inside `projects/pec/` but does not start with `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_`.
  - The copy that ran is the run-root copy, so the run root was excluded, and `evidence/apply_run.out`, written beside it, could not trip the write-set check.
- **35 pins.** I recomputed every pin with `git show <c>:<path> | sha256` at both `origin/main` and HEAD: 35/35 match, including:
  - DEL-04-01 `98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0`
  - DEL-04-03 `10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18`

  Both are also byte-equal to the S4 prep candidates at `91a2e8407` and to the landed bytes at `f0a6159c9`.
- **Run-root copies equal the prep files.**
  - `cmp` of 46 files (the script, 9 aids, 12 candidates, 12 quotes, 12 claims) against the prep folder shows 0 differences, and the file sets are identical.
  - The prep `SHA256SUMS` checks 158/158 OK.
  - `evidence/runroot_copy.sha256` equals the prep `SHA256SUMS` entries it names.

## Item 2 — Byte identity: **PASS**

For all twelve contracts, the SHA-256 of `origin/main` equals the tabled preimage, the SHA-256 of HEAD (and of the working tree) equals the tabled postimage, and the preimage also equals the bytes at `125cfacc1`. The result was 12/12, with 0 mismatches against the full 64-hex values in the proposal grant table (proposal L136–149).

## Item 3 — MODE=VERIFY (checks.md items 1, 3, 4, 8, 9, 13, 16, 18–21): **PASS**

Each check below ran on a `git archive` export of `1cc8ce997`, compared against an export of `16010b4ca`.

- **QA 1.** For all 12, `validate_scope_of_work.py` resolves `PASS format=SOW_V1`. `SOW_V1` is the canonical format under the Standard §7, and no pilot-variance marker applies to it (NOTE N7).
- **QA 3.** No `_STATUS.md` changed: `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` is empty. HEAD states are 10 `INITIALIZED`, with DEL-01-03 and DEL-01-05 `IN_PROGRESS`, the same as at `origin/main`.
- **QA 4.** `PASS format=SOW_V1` ×12, exit 0.
- **QA 8.** I checked every contract programmatically:
  - every `OUT-*` matrix scope/objective reference is within the frontmatter `project_scope_refs` and `package_objective_refs`;
  - those refs equal the deliverable's `Deliverables.csv` `CoversScopeItems` and `SupportsObjectives`.
- **QA 9 and QA 13.**
  - `derive_review_checklist.py` exits 0 ×12. A second run is byte-identical, and each output equals the prepared hash in the prep `SHA256SUMS` and the committed run-root `checklist_<DEL>.json` (`e3fe784b`, `ab1efb30`, `4ea83dde`, `691455d0`, `78336479`, `9f683083`, `3a1f8098`, `e7e76f9b`, `e0bcdb5e`, `780b9572`, `9f038cda`, `5e7fde59`).
  - Parsing the JSON, each checklist holds every `AC-*` exactly once, in source order, with exact text, source line and the postimage SHA-256, and each item carries at least one verification method.
- **QA 16.** This report separates findings by kind: schema (validator/checklist), project content (claims, quotes, Part B) and execution substrate (evidence, preflights, footprint).
- **QA 18.** Checklist reruns are byte-identical. I reran `negative_controls.sh` on `16010b4ca`: `RESULT PASS`, 9/9 caught. That includes "DEL-01-04 matrix row removed", where the validator fails and the checklist refuses with no artifact.
- **QA 19.**
  - `check_qualified_ids.py` gives `RESULT PASS 44/44`.
  - I also resolved every qualified citation in the 12 postimages (slash, hyphen and backtick forms, 69 occurrences) against the HEAD tree, which holds the landed S4 contracts and the S1 postimages: 0 unresolved.
  - The backtick-slash style (`` `DEL-04-01`/REQ-001 ``) was already present in the preimages.
- **QA 20.** The only multi-AC matrix row across the 12 contracts is DEL-01-03 `AC-007, AC-008 | VER-007`. It is unchanged from the preimage, and both criteria are verified by exactly `{VER-007}`, so the grouping is permitted.
- **QA 21.**
  - `check_boundary_owner_resolution.py` exits 0 ×12 with 0 `UNRESOLVED_OWNER` and 0 `UNDEFINED_CLAIM`. The JSON outputs are byte-identical to the run-root and prep `boundary_<DEL>.json`.
  - The `NOT_CHECKABLE` set is exactly the one tabled: DEL-01-03 REQ-006; DEL-02-01 REQ-002/003/005/012; DEL-02-02 REQ-005; DEL-03-01 REQ-007/009; DEL-03-03 REQ-015; DEL-04-05 REQ-003/005. The other six report none.
  - I resolved each clause by hand against the claims it cites:

| Contract | Requirement | Owner resolution |
|---|---|---|
| DEL-01-03 | REQ-006 | `DEL-07-01` in CLM-008 |
| DEL-02-01 | REQ-002 | `DEL-01-06` in CLM-011; `DEL-02-07` in CLM-004 and CLM-011 |
| DEL-02-01 | REQ-003 | `DEL-01-01` in CLM-007 and CLM-011 |
| DEL-02-01 | REQ-012 | Every owner listed (DEL-02-02..06, 02-08, 02-09, 02-07, 01-06, 01-01, 03-01..03, 04-03, 04-05, 09-02, 09-07, 01-03, 01-05, 10-02, 10-03, 10-13) is named in CLM-004 or CLM-011 |
| DEL-02-01 | REQ-005 | `DEL-04-03` is named in CLM-011, but REQ-005 cites CLM-007 (pre-existing and unchanged, as the proposal's table says; NOTE N3) |
| DEL-02-02 | REQ-005 | Cites no claim; `DEL-03-01` is in CLM-009 (pre-existing and unchanged; N3) |
| DEL-03-01 | REQ-007 | `DEL-02-06` in CLM-016 (cited); PKG-02 in CLM-007 (cited) |
| DEL-03-01 | REQ-009 | `DEL-04-05` in CLM-019 |
| DEL-03-03 | REQ-015 | `DEL-02-08` and `DEL-04-01` in CLM-015 |
| DEL-04-05 | REQ-003 | `DEL-08-03` in CLM-014 and CLM-016 |
| DEL-04-05 | REQ-005 | `DEL-04-03` in CLM-012 and CLM-016 |

## Item 4 — Semantics: **PASS**

**Aids rerun on the HEAD export (the `--gitdir` is the act worktree, read-only):**
- `verify_s1p_quotes.py --observation 125cfacc1 --obs-exempt DEL-03-06`: `RESULT PASS 884/884`, exit 0
- `verify_s1p_state_claims.py`: `RESULT PASS 905/905`, exit 0
- `check_qualified_ids.py`: `RESULT PASS 44/44`, exit 0

**Hand checks beyond the aids:**

*State claims:*
- **DEL-02-01 CLM-013 census at `125cfacc1`.** I recounted all 68 PEC `_STATUS.md` files: `OPEN` 30, `INITIALIZED` 28, `CHECKING` 4, `RETIRED` 4, `IN_PROGRESS` 2. At `16010b4ca` the counts are 28/30, which the proposal discloses.
- **DEL-01-03 CLM-008.** At `125cfacc1`, DEL-07-02 and DEL-07-04 `_STATUS.md` read `RETIRED`, and both `Deliverables.csv` rows carry the quoted envelope note.
- **DEL-04-05 CLM-014.** Commit `345266081` (`D-PEC-101` K1) adds the line "DEL-10-13 (Reliance-advertisement gate) — TESTS [E-P90]", and `DEP-10-13-005` holds the quoted `Statement`.
- **DEL-04-05 AX-012.** `b7d0450b1` (2026-07-28) removed "revision 1.1, accepted working surface" from DEL-04-05 `_REFERENCES.md` and re-pinned it to revision 1.3.

*Quotations:*
- **DEL-01-03 CON-001.** The three PRD v2.4 quotations and the SCA-005 `Propagation_Plan.md` §B4 quotation each occur verbatim.
- **DEL-03-03 CLM-015.** The A-21 text occurs in SCA-005 `Amendment_Preview.md`, and the R-01 text in `Impact_Assessment.md`. The §7.1 WorkGraph rule is in the PRD. "trailing by method design" is absent from the PRD, as the claim states, and present in the revision-1.6 `Deliverables.csv` DEL-03-03 `Description`.

**No scope added.**
- The new DEL-03-03 REQ-015..017 restate the lag classes in DEL-03-03's revision-1.6 `Deliverables.csv` `Description`.
- The other changed requirements carry the PRD v2.4 / revision-1.6 feed-profile model or add exclusions. They are DEL-02-01 REQ-002/003/007/012, DEL-03-01 REQ-007/008, DEL-03-03 REQ-003, DEL-04-05 REQ-013 and DEL-10-10 REQ-011.
- No requirement exceeds its deliverable's `ScopeLedger.csv` / `Deliverables.csv` row or PRD v2.4.

**Open items; IDs kept and retired.**
- New open questions are carried as `CON`/`TBD`: DEL-02-01 CON-004..006, DEL-02-02 CON-003, DEL-03-03 CON-006/007 and TBD-005, DEL-10-10 CON-006.
- No local ID was removed except DEL-03-01 `TBD-005`. It has no definition in the postimage and appears only in the AX-014 retirement note, so it is not reused.

**Part B landings: byte-exact, with gates binding.** I applied each exhibit replacement string to the preimage line and compared the result with the postimage line.

- **DEL-03-02-REM-016:**
  - L134→L148: EXACT
  - L136→L150: EXACT
  - The rest of CLM-007 and AX-009 (preimage L325, now L339) are unchanged.
- **DEL-03-03-REM-004:**
  - L153→L169, all four replacements: EXACT
  - L317→L347 (AX-009): EXACT
- **DEL-03-06-REM-004.** The word diff shows exactly the four loci:
  - L220: removal and addition exact.
  - L222–225: `EvidenceQuote` column with the two exact PEC-SVC-003 strings.
  - L229: the authored wording as tabled. It adds "The repair records a source for each edge;", uses "supplies no evidence for any of those cells", and removes the "same disposition" comparison.
  - L476: EXACT.
- **DEL-04-05-REM-003:**
  - (1) L20 equals the exhibit text with the bracket resolved to "**revision 1.6** (`current_basis`, SCA-006 successor)".
  - (2) L116: EXACT deletion. The table at L118–122 carries the `EvidenceFile` column (`ScopeLedger.csv` / `docs/PRD.md` / `docs/PRD.md`) and the two replaced `Statement` values.
  - (3) L124: EXACT.
  - (4) L142: EXACT.
  - (5) L298: EXACT.
  - (6) AC-015 at L244: EXACT. Matrix L334: both replacements exact, plus `, AX-012` from currency edit C9 (NOTE N4).
  - Exhibit quotation lines L119–131 are kept verbatim.
- The register cells behind these landings (`DEP-03-02-003`, `DEP-03-03-003`, `DEP-03-06-003/004`, `DEP-04-05-003/004/005`) and the PRD quotations were checked at `origin/main`, and each matches.

**DEL-03-06 is correction-only.** `git diff -U0` shows hunks only at `@@ -220`, `-222,4`, `-229`, `-476`.

**DEL-01-03 and DEL-01-05 verification basis unchanged.** I compared definition blocks (including continuation lines), not just first lines:
- All 29 DEL-01-03 and 32 DEL-01-05 REQ/AC/VER blocks are byte-identical to the preimage.
- DEL-01-05's matrix is unchanged (16 rows).
- DEL-01-03's matrix differs only in the `OUT-003` row, whose claim-reference cell gains `AX-007` (as disclosed). No REQ/AC/VER pairing changes.
- `DEL-01-03/REQ-003` is byte-identical.
- `DEL-01-03/CON-001` keeps its subject, the prose/token admissibility boundary. It now also covers Markdown feeds and values outside the guard's admitted classes (disclosed) and resolves nothing.
- The first sentence of `DEL-02-01/REQ-002` is byte-identical.

**DEL-04-05 matches the landed S4 text.**
- All 11 DEL-04-05 quotation entries sourced from DEL-04-01 or DEL-04-03 (Q53–Q56, Q60–Q62, Q76, Q77, Q80, Q82) occur raw and verbatim in the landed contracts at `origin/main`. They cover DEL-04-01 REQ-001, REQ-006, CON-004 ("seven components … no eighth component") and DEL-04-03 REQ-001, REQ-005, REQ-008, CON-003.
- Across all 12 quote files, 14 quotations of any S4 contract all read verbatim at `origin/main`.
- DEL-04-05's own CLM-013 consequence ("seven components, no eighth added"), REQ-013 ("the seven components … and the 'no eighth component' rule") and CON-003 ("fixes the return at seven components and forbids an eighth") are consistent with each other.

**No Remaining surface, no CHECKING gate.**
- `## Remaining` appears only in DEL-02-01 and DEL-10-10, and each occurrence says the section is retired or not read (DEL-02-01 CLM-012/013/014, REQ-007, AC-007, VER-007, matrix; DEL-10-10 L361).
- `CHECKING` appears only as an observed lifecycle token: the §3.3 ladder and census count in DEL-02-01, and the guard's state set in DEL-02-01 and DEL-02-02. Nothing prompts about CHECKING or presents it as a gate.

## Item 5 — Containment and lifecycle: **PASS**

- **`git diff --name-status origin/main...HEAD`:**
  - 12 `M` for the twelve `ScopeOfWork.md` files;
  - `A` files under `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/` only;
  - `A` for `…/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md`;
  - nothing else. Filtering those three classes out leaves 0 paths.
- **Forbidden paths untouched.** A path-limited diff over `v2`, `projects/pec/docs`, `docs`, `_Decomposition`, `_ScopeChange`, `**/Dependencies.csv`, `**/_DEPENDENCIES.md`, `**/_CONTEXT.md`, `**/_REFERENCES.md`, `**/_SEMANTIC.md`, `**/_REGISTER.md`, `**/MEMORY.md`, `**/_STATUS.md`, `**/_REVIEW.md` and `**/Review_Findings.csv` returns 0 paths. No `MEMORY.md` was created; add-on M is deferred to node M1.
- **Whitespace.** `git diff --check origin/main...HEAD` is clean (exit 0).
- **Exports.** `diff -rq` between the base export and the HEAD export shows 14 entries: the 12 contracts, the run-root directory and the brief.

## Independent reproduction of the finite verification

| Row | Manager recorded | My result |
|---|---|---|
| Validator ×12 | PASS | `PASS format=SOW_V1` ×12 (HEAD export) |
| Checklists | rerun identical = prepared | 12/12 match the prepared, run-root and rerun hashes |
| Boundary owners | exit 0, no UNRESOLVED/UNDEFINED | same; JSON identical to prep and run root |
| Quotes | 884/884 | 884/884 |
| State claims | 905/905 | 905/905 |
| Qualified IDs | 44/44 | 44/44 |
| Dependency-quote currency | 127/127 before and after | 127/127 on the `16010b4ca` export and on the `1cc8ce997` export |
| Strict registers | exit 1, 0 errors, 26 `XRG-013`, identical | identical before and after (paths normalized): exit 1, `ERROR findings: 0`, `WARNING findings: 26`, all `XRG-013` |
| Harness self-check / receipts | identical, exit 0 | identical before and after, exit 0 / exit 0 (exports given a Git identity through alternates) |
| Rerun method | `run_s1p_checks.sh` at `16010b4ca` OVERALL PASS | my own run gives `OVERALL PASS`: S4 overlay no-op ×2; act 0/0/refuses 1; containment 12; fault injection 9/9 |
| Negative controls | 9/9 | 9/9, `RESULT PASS` |

- **Rerun outputs match.** Compared file by file with the manager's `evidence/rerun_16010b4ca/`, every output is byte-identical except four (`audit_quotes_post.out`, `containment.out`, `receipts_pre.out`, `receipts_post.out`), which differ only in the scratch export path.
- **The manager's post outputs say what they claim.** `validate_summary` 12 PASS; `checklist_compare` 12 MATCH; `boundary_summary` 0 unresolved and JSON identical; `pins.out` 35/35 and 12/12; `rerun_refuses.out` 12 FAIL lines and exit 1; `lifecycle.out` empty; `req_ac_ver_identity.out` 29/29 and 32/32; `del_03_06_hunks.out` the four hunks; `before_after_identity.out` IDENTICAL ×4.
- **Reliance preflight, my own run.** I ran `pec_reliance_hold.py --operation candidate-validation` on the 12 targets in the HEAD export: `ALLOW`, exit 0, 12/12. The register (`f877d931…`) holds a header only.

**Reliance-preflight ordering.** The times below are UTC, from `date -u` lines and commit times.

| Time (UTC) | Event |
|---|---|
| 17:14:37 | `origin/main` merge `16010b4ca` |
| 17:17:44 | preconditions |
| 17:18:24–25 | `dispatch-for-production` ×12 ALLOW, exit 0, recorded at HEAD `16010b4ca` |
| 17:18:35–17:19:09 | pre-act baselines |
| 17:19:09 | check-only (exit 0) |
| 17:19:32 | commit `053ca4e22` |
| 17:19:45–47 | the act (exit 0; 12/12 byte-exact; 35/35 pins; write set = grant) |
| 17:19:59 | `rely-for-production` ×12 ALLOW, exit 0, recorded at HEAD `053ca4e22` |
| 17:19:59 | act commit `1e33df616` |
| 17:21:07 | post verification |
| 17:22:10 | rerun |
| 17:24:18 | negative controls |
| 17:28:34 | commit `1cc8ce997` |

So dispatch came before the act, and rely came after the act and before the act commit. `reliance_rely.out` is contained in `1e33df616` itself, which proves it came first even though both carry the same second (N9).

## Findings

**BLOCKING:** none.

**NON-BLOCKING:** none.

**NOTE:**
- **N1 — project content.** Eleven production contracts (all but DEL-03-06) still describe the packet as "(provisional `D-PEC-104`)" in their currency-provenance AX entry, for example DEL-04-05 AX-012 at L301. The number is now final. These bytes are bound, and the ruling says they are not rewritten. This is a later currency item.
- **N2 — project content.** DEL-04-05 AX-012 (L301–315) ends with process text in a production contract: "(manager repair after verdicts 02 and 03)". It is bound bytes, and I flag it only for a later packet.
- **N3 — QA 21 strict reading, pre-existing.** DEL-02-01 REQ-005 cites CLM-007, while its owner `DEL-04-03` is named in CLM-011. DEL-02-02 REQ-005 cites no claim. Both requirements are byte-identical to their preimages and the proposal's hand-resolution table discloses both, so this act introduces neither. A later packet could bind the owners to cited claims. Separately, the table's "PKG-02 (CLM-007, CLM-019)" for DEL-03-01 REQ-007 resolves through CLM-007; CLM-019 names the eight grammar deliverables, not the string "PKG-02".
- **N4 — Part B gate reading.** DEL-04-05 matrix L334 carries both REM-003 replacements exactly and also gains `, AX-012` in its claim references. That comes from currency edit C9, not from the Part B item, which is consistent with the proposal's statement that other changes come from the S1 causes.
- **N5 — execution substrate.** `evidence/apply_check_only.out` records the check-only command without `PYTHONDONTWRITEBYTECODE=1`, although the proposal's generation method includes it. I found no `__pycache__` or ignored file in the act worktree (`git status --porcelain --ignored` is empty), so nothing resulted.
- **N6 — execution substrate.** `evidence/post/containment.out` and `HEADER.out` were captured at `1e33df616`, not at the candidate `1cc8ce997`. The later commit adds only run-root evidence, and my own containment check at `1cc8ce997` confirms the result.
- **N7 — method interpretation.** For QA 1 ("pilot variance covers the path") I treated `SOW_V1` as the canonical format under the Standard §7, resolved by the validator. No variance marker applies to `SOW_V1` production contracts.
- **N8 — disclosed consequences, not defects of this act.** These stand as the ruling (question 3) and the proposal's Consequences section record them:
  - DEL-03-06 L284 and L346 sibling quotations are now non-verbatim;
  - DEL-03-04's quotation of DEL-03-01 CON-005 ("manifest-named feed") is now stale;
  - the premises of DEL-02-07 CON-003 and DEL-10-13 CON-003 are partly overtaken;
  - the `_REVIEW.md` of DEL-03-01 and DEL-01-05 still bind the prior SOW hashes, kept as history under ruling question 4, with no REVIEW acceptance of the new bytes.
- **N9 — evidence timing.** The rely preflight's end line and the act commit share the second 17:19:59Z. The order is established because `reliance_rely.out` is inside commit `1e33df616`.

## Footprint

- **Scratch.** `D=/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s1av.H2v1zs`, with `TMPDIR=$D` and `PYTHONDONTWRITEBYTECODE=1` exported in every command that ran tools. It held:
  - `git archive` exports of `16010b4ca` and `1cc8ce997`;
  - an empty `git init` in each export, with an alternates file pointing at the repository's objects (the method `run_s1p_checks.sh` uses);
  - helper scripts, outputs, and the `mktemp` directories created by `run_s1p_checks.sh` and `negative_controls.sh`.

  `$D` was deleted with `rm -rf` and confirmed gone. No `s1pchk`, `s1pneg` or `s1av` directory remains, and nothing was written to `/tmp` or `/var/folders`.
- **Git.** I ran `git fetch --dry-run` and `git ls-remote`, both network reads with no ref update. Every other Git command was a read: `show`, `diff`, `log`, `ls-tree`, `archive`, `rev-parse`, `merge-base`.
- **Act worktree.** It was not modified: `git status --porcelain` shows 0 lines and HEAD is still `1cc8ce997`. I made no edit, no Git write and no branch switch, and I did not touch `/Users/ryan/ai-env/projects/chirality` or the `pec-project-assessment-6106d5` worktree.
- **Slips:** none known.

## Relevant paths (absolute)

- Act worktree: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act`
- Run root: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/` (`apply_s1p.py`, `evidence/`, `evidence/post/verify_rows_2_13.zsh`, `evidence/rerun_16010b4ca/SUMMARY.out`, `evidence/negative_controls.out`, `evidence/reliance_dispatch.out`, `evidence/reliance_rely.out`)
- Brief copy: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md`
- Ruling: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-104_RULING_2026-09-27.md`
- Proposal: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-104_s1_sow_currency_proposal_2026-09-26.md`
- Exhibit: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`
- Prep folder: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/`
- The twelve contracts: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act/projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md`, as listed in `evidence/targets.txt`
