# VERIFIER_VERDICT_01 — D-PEC-98 act (PR #958, head `d6feee9eb`)

**Overall verdict: PASS WITH NOTES**

Nothing blocks. All eight checks and the reliance preflight pass. The notes below are non-blocking. Note 1 should be disclosed to the owner, because fixing it needs bytes the ruling did not allow the act to move.

## Identity

- Fresh, read-only pec-reviewer TASK (Type 2). I authored nothing in this package and did not delegate.
- The host reports the model as Opus 5.5 (`claude-opus-5-5`). The `high` reasoning effort comes from the brief's steer; the host does not confirm it.
- Worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d98-first-sows-act`, branch `claude/pec-d98-first-sows-act`, HEAD `d6feee9ebd3b31be18bc0e82a03672df32d66a0e`.
- After `git fetch`, `origin/main` is `6b48b6f26ed3e9ef60fde1c7d2289843bd1aea25`, which is also the merge base.
- Interpreter: CPython 3.13.7. Commands ran from the repository root with `PYTHONDONTWRITEBYTECODE=1` (one exception, see note 7).
- Scratch outputs are under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d98v/`.
- `git status --short` is empty after my run. I changed no tracked byte.

## Instruction and source files relied on (SHA-256, recomputed)

| File | SHA-256 |
|---|---|
| `AGENTS.md` (root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `_DECISIONS/D-PEC-98_RULING_2026-09-26.md` (same on `origin/main` and at `189f205ff`) | `039dc7e2d11db5e7e4ad46be18d2261302b37070f18737d8e794e22c08cd8361` |
| `_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md` (revision 2; same on `origin/main`) | `92b6f1a223f5cb6fffc399f16e5e4e63cf5d8aa8f391981d3afcb9f4027a3e40` |
| `_DECISIONS/_REGISTER.md` (worktree = `origin/main`) | `4306bd1094204552e3f5af448f1afb5928d57d58dc52775bdfee250972b70cf4` |
| Brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3A_D98_SOW_ACT.md` | `d9a013489faac17c9a9f2ef90c0f5039e061ab098d8bde0e43defc7b65486291` |
| `workflows/scope-of-work/WORKFLOW.md`: current (PR #955) / bound edition at `189f205ff` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` / `d616865a5cbfa84b47fd509d2910826106db57473543a86d067ddc3edf6fbd8b` |
| `resources/checks.md`: current / at `189f205ff` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` / `fbb2c8ebdee578ad9ce9b36f17fadd1013f10d470142921ce18855ee174576b8` |
| `resources/tools.md`: current / at `189f205ff` | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` / `2bbb55ccc68e2ab8bedfe9d2b766770b449a5119dc2cb1313cd5b5f5e3010f3f` |
| `resources/brief.md`: current / at `189f205ff` | `1696cd9a0c13aeda4151ebdd666fff7d0450450c88ea1aa00f7435fdcbf492bc` / `a082f1afac4eac22c0225f79191006358c6cb4508bd94f7dc2111594e8045145` |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (same at `189f205ff`) | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` |
| `tools/scope_of_work/validate_scope_of_work.py` / `derive_review_checklist.py` / `check_boundary_owner_resolution.py` / `common.py` | `f0f10590…fecfe` / `bfb64dc9…0109` / `22ef57e0…ae16a` / `61a34722…0389` (the proposal's values; unchanged by PR #955) |
| `tools/validation/validate_decomposition_registers.py` / `tools/practitioner_harness/harness.py` / `tools/validation/validate_pec_loop_receipts.py` | `869df1d5…57ee` / `01a9b954…61f3` / `8eb62995…bad9` |
| SCA-006 group-3 `ACCEPTED_MANIFEST.csv` | `d2f24792b80d5de9189416d74389c50c568baabba81a56c43b19237f3c3bfe12` |
| `_Decomposition/_LATEST.md` at `189f205ff` | `768ae4c4286b50737d323f6c5a1c6cdcb8247f67fb65822679443bbb76eea771` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |

I also read in full: SCA-006 group-3 `DECISION.md`, `REPIN.md`, `REPIN_WORDDIFF.txt`, `repin_candidates.py`, `verify_d98_quotes.py`, `verify_d98_state_claims.py` (both editions), the head of `test_apply_d98.py`, the head of `apply_d98.py`, and the recorded evidence files listed under the checks.

## Checks

### 1. Basis — PASS

**Ruling and register on `origin/main`.**
- The ruling on fetched `origin/main` hashes `039dc7e2…8361`.
- Register row `D-PEC-98` on `origin/main` reads `RULED A + S + M / EFFECTIVE ON MERGE` and quotes the owner's words, "D-PEC-98: A; S; M; re-pin yes; CON-005 open; defaults".
- Both are present at `189f205ff` too.

**The pin commit.**
- `189f205ff02df4111b33c20be441ce06e65ada7a` is "Merge pull request #954 from sgttomas/claude/pec-rulings-20260926b".
- It is an ancestor of `origin/main` (`merge-base --is-ancestor` exit 0).

**Run-root scripts match REPIN.md.** Recomputed:

| File | SHA-256 |
|---|---|
| `apply_d98.py` | `0a28d05d7d285596497a98306f4327909fd3817ac8403f66a1b64f7c86d29343` |
| `verify_d98_state_claims.py` | `65059ce21309dea7ba945db562353c7d45884e6f3bf77aad3b51b244309e835f` |
| `repin_candidates.py` | `479eb8f1d6148876aa092d0a0868092229aaaa67f2422fc18b5fbb8b8be4265b` |
| `REPIN_WORDDIFF.txt` | `d67bc0991ddaec149d9c7b41dc61e43a7f4f15e76ea52ea556e57d06cc66ed61` |
| `verify_d98_quotes.py` (as prepared) | `9cadc2c4…b745` |
| `test_apply_d98.py` (as prepared) | `ad7dce86…9a7a` |
| `run_d98_checks.sh` (as prepared) | `abc20da2…b8d` |

The three aids are byte-identical to the PREP copies (`diff`).

**Preparation evidence.**
- PREP `apply_d98.py` = `19c2ecb6…419e`.
- PREP candidates = `03cce13f…dc0a` and `aafb54fd…188b`.
- `shasum -c SHA256SUMS` in the PREP folder gives OK for 29 of 30 entries. The one failure is outside this PR (note 8).

**The pins, recomputed with `git show`.**

| File | Value | At |
|---|---|---|
| `SOFTWARE_DECOMP.md` | `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` | `189f205ff`, `6b48b6f26`, HEAD, working tree |
| `Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` | same |
| `ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` | same |
| `docs/PRD.md` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` | same |
| Both `_STATUS.md` | `d80800a4…0eef` and `3e14313c…d768` | `53145aaeb`, `189f205ff`, `6b48b6f26`, HEAD, working tree |
| Both `Dependencies.csv` | `c23cd711…701e` and `41afd6dc…8e4b` | same |

- The four register and PRD values equal the group-3 `ACCEPTED_MANIFEST.csv` rows.
- At `c9e5cd87d` and `53145aaeb` the four files still hold the prepared values (`dc2b8479…`, `b8628fc4…`, `83152a94…`, `fff27a66…`).

### 2. Byte identity — PASS

| Contract | Written file | Run-root candidate | `TARGETS` in run-root `apply_d98.py` |
|---|---|---|---|
| DEL-02-08 | `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26` | `2319661b…dd26` | `2319661b…dd26` |
| DEL-02-09 | `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e` | `eab18e17…6f5e` | `eab18e17…6f5e` |

Independent reproduction, all in scratch:
- I ran the run-root `apply_d98.py` against a fresh `git archive 6b48b6f26 projects/pec` export.
- `--check-only` gave `CHECK write set = grant (2 creates, 0 modifies, 0 removes); nothing written`.
- The real run gave `CHECK targets 2/2 byte-exact; write set = grant (2 created, 0 modified, 0 removed under projects/pec); pinned 8/8 unchanged`, exit 0.
- Both outputs are byte-identical to the written files (`cmp`).
- A second run exited 1.
- `test_apply_d98.py` against a `189f205ff` export gave `RESULT PASS 5/5`.

### 3. `MODE=VERIFY` (resources/checks.md) — PASS

**Tool runs.**

| Tool (run per contract) | Exit | Result |
|---|---|---|
| `validate_scope_of_work.py` | 0 | `PASS format=SOW_V1` for each; `--json` gives `"issues": []`, `"valid": true` |
| `derive_review_checklist.py --output <scratch>` (twice each) | 0 | Reruns byte-identical; equal to run-root `checklist_DEL-02-08.json` (`dd05939d…048c`) and `checklist_DEL-02-09.json` (`0ca3f3ad…8c2a`) |
| `check_boundary_owner_resolution.py --json <scratch> --show-not-checkable` | 0 | "boundary requirements checked: 1 … per-act exclusions for skill QA: 3 … contracts failing: 0"; NOT_CHECKABLE are 08 REQ-009/010/011 and 09 REQ-007/008/009; my JSON equals the run-root `boundary_*.json` |

**Per item.**

| Item | Result | Evidence |
|---|---|---|
| 1. Exact pilot variance | PASS, on the reading below | The contracts carry no pilot-variance marker, and none is needed |
| 2, 5–7, 10–12, 14, 17 | NOT_APPLICABLE | CONVERT-only |
| 15 | NOT_APPLICABLE | `RENDER_HTML=false` |
| 22 | NOT_APPLICABLE | REVISE-only |
| 3 | PASS | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` is empty; both `_STATUS.md` blobs equal the tabled preimages |
| 4 | PASS | Validator PASS for both, no issues |
| 8 | PASS | OUT-001..003 (08) and OUT-001..002 (09) each appear in matrix rows carrying `SOW-095`/`SOW-096` and `OBJ-001 OBJ-002` |
| 9 | PASS | Every checklist item has a non-empty verification. Only 08 AC-018 and 09 AC-017 use `HUMAN_REVIEW`; all others map to a VER |
| 13 | PASS | 21 and 17 items, in source order (AC-001..AC-021 and AC-001..AC-017), exact text, qualified IDs, each item's `source_identity.sha256` equal to the postimage hash, matrix-linked VER or human review |
| 16 | PASS | This verdict separates schema, project-content and execution-substrate findings (see the notes) |
| 18 | PASS | Reruns are byte-identical. Negative control in scratch: I deleted the 08 matrix row for AC-013. The validator returned `FAIL format=INVALID`, and `derive_review_checklist.py --output` refused ("format state is INVALID …") with exit 1 and no output file |
| 19 | PASS | Scan with blockquotes removed: 106 (08) and 90 (09) local definitions, every bare local-ID reference defined, no undefined bare ID. Upstream IDs are qualified (e.g. `DEL-01-03/CON-001`) or sit inside a carve-out blockquote (08 CLM-015, 09 CLM-014) |
| 20 | PASS | Every matrix row carries exactly one AC |
| 21 | PASS | Tool reports no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`. Hand resolution below |

**QA 21 hand resolution** (read in the contract text):
- DEL-02-08 REQ-009 → `DEL-04-05`, REQ-010 → `DEL-01-03`, REQ-011 → `DEL-04-03`. Each requirement cites CLM-011, and CLM-011 names that owner ("rendering a limitation into a response is `DEL-04-05`"; "the ingest-boundary guard is `DEL-01-03`"; "stamping freshness and attaching per-claim citations is `DEL-04-03`").
- DEL-02-09 REQ-007/008/009 → the same three owners via CLM-010, which names each.
- This agrees with the run-root `evidence/post/qa21_hand_resolution.out`.

**How I read item 1 for a new SOW_V1 INIT.**
- "Pilot variance" is a mechanism from before ratification and from conversion work. The tools use it only as a `pilot-variance` control marker in CONVERT evidence candidates (`finalize_scope_of_work.py`).
- D-GOV-16 was ruled 2026-07-12, "items 1–10 APPROVED exactly as proposed" (`docs/governance_harness/_DECISIONS/_REGISTER.md`). It ratified the standard, whose §7 says "New deliverables use `SOW_V1`".
- For an INIT of a new deliverable, the "exact variance" is therefore the ratified standard plus an exact path-scoped owner grant. D-PEC-98's exact product grant names both `ScopeOfWork.md` paths, so the item is met.

**Effect of Root PR #955 (`MODE=REVISE`, merged at `6b48b6f26`): none on any INIT or VERIFY check applied here.**
- `git diff 189f205ff 6b48b6f26` changes only four files: `WORKFLOW.md`, `checks.md`, `tools.md` and `brief.md`.
- In `checks.md`, only the preamble changed: it adds `REVISE` to the NOT_APPLICABLE sentence and declares item 22 REVISE-only. The text of items 1–21 is unchanged.
- The `WORKFLOW.md`, `tools.md` and `brief.md` changes add REVISE-only text and constraints.
- `execution.json`, `representation-migration.md`, `tools/scope_of_work/**` and the standard are unchanged.
- Under `projects/pec`, PR #955 adds only `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md`.
- The re-pin was not a REVISE: it moved candidate bytes before any production contract existed, under the owner's question-4 ruling.

### 4. Semantics — PASS (see notes 1 and 2)

**State claims.**
- `verify_d98_state_claims.py .` exits 0 with `RESULT PASS 56/56`.
- The prepared edition still gives `RESULT PASS 44/44`.

**Checks I added by hand** (at `53145aaeb` unless stated):

| Claim | Result |
|---|---|
| 08 CLM-007 and 09 CLM-006: `Dependencies.csv` statements and Notes; `DEP-03-01-015`/`016` statements in the DEL-03-01 register; `[E-P81]`/`[E-P82]` in `_DEPENDENCIES.md` | True |
| 08 CLM-009 and 09 CLM-008: DEL-01-06 contract strict version-1; SCA-005 §B4 "STALE_REBUILD_REQUIRED" and "gated on B6" | True |
| 08 CLM-010 and 09 CLM-009: PhaseHints (every listed ID `P1`; DEL-05-01 `P2`; DEL-06-02, DEL-06-06, DEL-10-06 `P3`) | True |
| 08 CLM-013: `ea5009d05` lies between `c9e5cd87d` and `53145aaeb` and revised both files; notice `NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md` names tranche `ROOT-WORKFLOW-WAVE2A-EXECUTION-20260926`, lists PEC among adopting loops and "one designated current graph ref"; template has "Current graph ref" and "Open deferrals" | True |
| 08 CLM-017 at `7a00a88df`: identity spellings 4 plain and 1 bold (PEC); tokens `T0R`/`B3A`/`D72`/`M01`; PR citation forms `#868`, `PR #919` and pull URLs | True |
| 08 CLM-017: SCA-005 risks R-01, R-02, R-08 and R-09 ("53 `WORK_GRAPH.md`, 3 canonical") | True |
| 09 CLM-016 at `7a00a88df`: 156 files (App 54, Piping 101, PEC 1); four `## Runs`, all bullet (App 1, Piping 3); 145 dated-heading files (46/98/1); 7 App with neither | Exactly true |
| 09 CLM-013: the same four `## Runs` files at `d61981ee2` (App DEL-05-04; Piping DEL-08-01, DEL-08-05, DEL-10-04) | True |
| 09 CLM-004: `ContextEnvelopeNotes` empty; `S`; `ResponsibleParty` `TBD` | True |

**Quotations.**
- `verify_d98_quotes.py` passes 69/69 against the tree and against a `189f205ff` export (check 6d).
- Quotes the tool does not cover, which I checked by hand at both `53145aaeb` and `189f205ff`: DL-4 "one per feed kind"; the charter lead "Read-side grammars over governed files:"; both `AnticipatedArtifacts` values; the 08 ContextBudgetQA `RecommendedAction`. All verbatim.
- The rows `SOW-015`/`SOW-095`/`SOW-096`, `DEL-01-01`/`DEL-02-05`/`DEL-02-08`/`DEL-02-09` and ContextBudgetQA `DEL-02-08`/`DEL-02-09` hash-identical between `53145aaeb` and `189f205ff`.

**Scope and open items.**
- I read all 20/16 REQs, 21/17 ACs and 20/16 VERs.
- Each traces to the `SOW-095`/`SOW-096` field lists, the register rows (Description, AnticipatedArtifacts, envelope notes), PRD v2.3 (PEC-RCN-002, §7.1, PEC-K-10, PEC-ORI-004/006, PEC-SVC-001/002), the PKG-02 charter, or SCA-005 §B4/§B7 and IA §9.3.
- I found no added scope.
- Every open item is TBD-00n or CON-00n (08: 7 TBD and 5 CON; 09: 7 TBD and 4 CON). CON-005 (08, line 198) stays open as "a scope question for the scope-change process or an owner ruling".

**Other semantic points.**
- The `OBJ-002` qualification (08 lines 51–56; 09 lines 50–56) says "indirect, through the record tier" (09: "thinner"). That is no stronger than the §3 note, "underlie OBJ-001/OBJ-002 through the record tier (SOW-001)".
- D-PEC-96 identifiers appear only as observations in 08 CLM-009 and 09 CLM-008. TBD-004 (08) and TBD-003 (09) disclaim reliance, and the REQs use generic surface wording.
- No `## Remaining` section is read (08 REQ-001/015, CLM-018; 09 REQ-001/013, CLM-017).

### 5. Containment and lifecycle — PASS

- `git diff --name-status origin/main...HEAD` lists exactly 59 added paths: the two `ScopeOfWork.md`, the brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S3A_D98_SOW_ACT.md`, and 56 files under `_Coordination/SOW_INIT_D98_2026-09-26/`. Nothing else.
- No `_STATUS.md` changed.
- `git diff --check origin/main...HEAD` exits 0 with no output.
- The run-root `.gitattributes` (`evidence/** -whitespace`) hides nothing: the added lines contain no trailing whitespace at all (`grep -c '^+.*[[:blank:]]$'` gives 0).

### 6. Re-pin checks

**a. Word diff — PASS.**
- I ran `diff` from each PREP candidate to its new candidate. Each contract has exactly three hunks:
  - frontmatter line 5, `@c9e5cd87d` → `@189f205ff02df4111b33c20be441ce06e65ada7a`;
  - the Purpose paragraph beginning "The accepted basis is …" (08 lines 19–27; 09 lines 20–28);
  - the "**Observation commit.**" clause (08 lines 33–43; 09 lines 34–42).
- The result matches `REPIN_WORDDIFF.txt`. `repin_candidates.py` replaces exactly three exact-match strings per file and asserts each occurs once.

The new wording is true:
- `_LATEST.md` at `189f205ff` reads "revision 1.6 (`current_basis` — accepted 2026-09-26 as the SCA-006 successor under the owner's checkpoint-group-3 audited-poststate acceptance)" and lists all four hashes.
- `DECISION.md` records the owner's verbatim "SCA-006 CP3: accept; Q1 a; Q2 a.".
- The PRD at the pin is v2.4 (`| **Version** | 2.4 |`).
- The four short hashes in each contract match.
- At `53145aaeb` the four files differ from the pin.
- Every locus the clause names is quoted in that contract, and I checked where:
  - DEL-02-08: CLM-001, CON-005, CLM-005, CLM-006, CLM-008, CLM-011, CLM-003, the warrant, CLM-012, CLM-004, CLM-002, CLM-018, REQ-010.
  - DEL-02-09: CLM-001, CLM-005, CLM-007, CLM-003, the warrant, CLM-011, CLM-004, CLM-002, CLM-017.
- Each named locus is verbatim at the pin (the quote checker passes against the `189f205ff` export).
- The clause's list leaves out two quoted loci; see note 2.

**b. `TARGETS`/`PINNED` — PASS.**
- `diff` of PREP `apply_d98.py` (`19c2ecb6…419e`) against the run-root copy shows changes only at line 29 and line 31 (the two `TARGETS`) and lines 35–38 (the four register and PRD `PINNED` values).
- All six equal the hashes I recomputed.
- The four deliverable-file pins are unchanged. The stale comment above `PINNED` is note 3.

**c. `verify_d98_state_claims.py` — PASS.**
- The only change from PREP (`7bb9e6bb…b673`) is lines 86–102, the `PIN2 = "189f205ff…"` block inserted before the result lines. Every original `c9e5cd87d`/`53145aaeb` check is intact.
- Run: exit 0, `RESULT PASS 56/56`. The 12 new lines all PASS: three register hashes and the PRD hash; PRD v2.4; revision 1.6 `current_basis` accepted through SCA-006 group 3; `_LATEST.md` records it; the pin is an ancestor of `origin/main`; the four files differ at `53145aaeb`.

**d. `verify_d98_quotes.py` — PASS.**
- `python3 …/verify_d98_quotes.py . <08 folder> <09 folder>` exits 0 with `RESULT PASS 69/69`.
- Its body is identical to `evidence/post/quotes.out` apart from header and trailer lines.
- Against a `189f205ff` export it also exits 0 with `RESULT PASS 69/69`.

### 7. Strict registers and every-PR checks — PASS

| Command | Exit | Output | Compared with recorded evidence |
|---|---|---|---|
| `validate_decomposition_registers.py --strict projects/pec/execution` | 1 | "ERROR findings: 0", "WARNING findings: 28" (26 `XRG-013` plus 2 `DRB-008`) | Identical to `evidence/strict_pre.out` and `evidence/post/strict_post.out` after removing their two header lines and `exit=1` trailer; identical to `evidence/at_189f205ff/strict_pre.out` (no header) |
| `harness.py self-check` | 0 | — | Body identical to `harness_pre.out`, `post/harness_post.out` and `at_189f205ff/harness_pre.out` |
| `validate_pec_loop_receipts.py --repo-root .` | 0 | "VALID … frozen through Receipt-166; versioned receipt contract satisfied" | Identical to the pre and post files |

### 8. Checklists — PASS

- 21 and 17 items, bound to `2319661b…dd26` and `eab18e17…6f5e`.
- PREP checklists hash `54c84487…e2db` and `2f495a54…86f3`.
- I compared the JSON trees field by field. Every difference is either the contract sha256 (old → new) or a `line`/`source_line` value: +10 for every AC and VER in 08 (63 diffs) and +8 in 09 (51 diffs). There are no other differences.
- The offsets match the added lines in the word diff:
  - 08: +1 in the Purpose paragraph and +9 in the observation clause.
  - 09: +1 and +7.
- This confirms `evidence/post/checklist_repin_equivalence.out` independently.

### Reliance-hold preflight — PASS

- Run from `projects/pec`: `pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <each ScopeOfWork.md> --operation candidate-validation`.
- Result for each: `{"operation": "candidate-validation", "status": "ALLOW"}`, exit 0.
- The register has a header and no rows.
- The recorded `dispatch-for-production` and `rely-for-production` outputs show ALLOW.

## Defects (blocking)

None.

## Notes (non-blocking)

1. **Project content: DEL-02-08 CLM-013 now calls the old pin "the decomposition pin".**
   - Location: `…/DEL-02-08_Work_graph_parser/ScopeOfWork.md` line 111, "at the decomposition pin `c9e5cd87d` they were `4411d0c25b1d…2261` and `24268f3545ea…4525`".
   - After the re-pin, the decomposition pin is `189f205ff…` (frontmatter line 5 and the Purpose paragraph). The hashes at `c9e5cd87d` are correct; the label is stale and contradicts the frontmatter.
   - Related: lines 29–31 of both contracts ("The pin binds the accepted decomposition bytes only. This deliverable's folder … did not exist at `c9e5cd87d`") now justify the observation commit by pointing at the former pin without saying it is the former pin. Those lines are still true.
   - Question 4's "What stays" did not anticipate this. The ruling allowed only the three moves, so the act correctly left the text alone.
   - Recommend disclosing it to the owner in the act return and VALIDATION, and carrying a one-word correction ("former"/"prepared") into a later owner-authorized revision.

2. **Project content: the observation clause's list of re-verified loci is incomplete.** Locations: 08 lines 36–43, 09 lines 37–42. Two quoted loci are missing from the list:
   - each contract's `Deliverables.csv` `AnticipatedArtifacts` quote (08 lines 84–87; 09 lines 77–78);
   - DL-4 "one per feed kind" from `SOFTWARE_DECOMP.md` (08 CLM-011; 09 CLM-010).

   `verify_d98_quotes.py` does not check these either. I checked both by hand: they are verbatim at `189f205ff` (and at `53145aaeb`), and the relevant register rows are byte-identical across the two pins. No false byte claim results. The list simply is not exhaustive, although it reads as if it were.

3. **Execution substrate: stale comment in `apply_d98.py`.**
   - Location: run-root `apply_d98.py` line 33 still reads `# Read-only files the act re-verifies (values at origin/main 53145aaeb).`
   - It is now true only for the four deliverable-file entries.
   - `REPIN.md` discloses this and explains it: the ruling allows changing only the values.

4. **Execution substrate: run-root records still pending.**
   - `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` and the manager's return are not in the branch yet.
   - `REPIN.md` refers to "the post-write validation in `VALIDATION.md`", and the run-root `.gitattributes` comment says "(hash-listed in MANIFEST.md)".
   - The proposal's administrative grant and brief step 7 require these files. They should record the SHA-256 of the scope-of-work method files actually loaded; the act ran on the post-#955 edition.
   - The manager's return at `…/returns/S3A_D98_SOW_ACT.md` is also not yet present.

5. **Execution substrate: re-check if D-PEC-99 merges first.**
   - The parallel D-PEC-99 act (brief RR3) changes `projects/pec/AGENTS.md`.
   - DEL-02-09 CLM-012 quotes two `AGENTS.md` phrases ("indexes what each run did in this deliverable", "memory carries no future assignments").
   - If D-PEC-99 merges first, rerun `verify_d98_quotes.py` and `verify_d98_state_claims.py` on the new base, as the brief requires. At `origin/main` `6b48b6f26` both pass.

6. **Schema: the prepared-checklist equality row cannot hold after a re-pin.**
   - The proposal's finite-verification checklist row asks for byte identity with the prepared checklists.
   - After a re-pin that cannot hold. The ruling and brief anticipate this, and check 8 establishes the equivalence instead.

7. **Execution substrate (my own run): a gitignored cache file was created.**
   - One `--help` probe of the scope-of-work tools ran without `PYTHONDONTWRITEBYTECODE`. It created the ignored, untracked `tools/scope_of_work/__pycache__/common.cpython-313.pyc` (12:15 local).
   - `.gitignore:26` `**/__pycache__/` covers it, and `git status` is clean. No tracked byte changed.
   - I did not delete it, because deleting is outside my brief. The manager may remove it.

8. **Execution substrate, outside this PR: stale PREP checksum entry.**
   - PREP `SHA256SUMS` lists `./D-PEC-98_DRAFT.md`, which is absent: `shasum -c` reports "FAILED open or read" for 1 of 30 entries.
   - This is state already on `origin/main`, not in this diff. All other entries are OK, including every prepared hash this act relies on.

Add-on S (status act) and add-on M (MEMORY files) have not run. That is correct at this stage: S may run only after this verdict, and M waits for closeout.
