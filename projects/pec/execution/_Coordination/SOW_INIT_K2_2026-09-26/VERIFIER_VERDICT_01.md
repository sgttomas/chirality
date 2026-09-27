# VERIFIER_VERDICT_01: D-PEC-103 act, independent `MODE=VERIFY` (fresh read-only TASK)

**Verdict: PASS WITH NOTES.** Nothing blocks. There are 0 BLOCKING and 0 NON-BLOCKING findings, and 6 NOTEs. None of the notes needs a change to a written byte before add-on S.

- **Verifier:** fresh read-only TASK (Type 2) acting as `pec-reviewer`. The host reports the model as Opus 5.5 (`claude-opus-5-5`); the reasoning effort (high) was set by the dispatcher.
- **Method:** workflow `chirality-root:bundled:workflow:scope-of-work`, `MODE=VERIFY`.
- **Authorship:** I authored nothing in this act or in its preparation.
- **Changes made:** none. I edited, created, staged or deleted no file in the worktree, and ran no git checkout, switch, commit, stash, reset, fetch, pull or push. Every Python run used `PYTHONDONTWRITEBYTECODE=1`.
- **Not claimed:** this verdict makes no acceptance, readiness, release or reliance claim, and raises nothing about `CHECKING`.

## Basis checked

| Item | Value (recomputed with `shasum -a 256`) |
|---|---|
| Brief `VERIFIER_BRIEF_01.md` (untracked, in the run root) | `e49c1daac88348aea1ca27737485f12610bdfc69a9b0542023af50c6f6fbc490` (matches) |
| Worktree / branch / head | `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act`, `claude/pec-d103-first-sows-act`, `4d2c19c1de99deae49577c295bf16701ce906a91` |
| `origin/main` (local ref and `git ls-remote origin main`) | `d385b6a19fd630b680d29d0e9e5988391b1d0cad` (PR #989 merge). It has not moved. |
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| Ruling `D-PEC-103_RULING_2026-09-26.md` | `67ff8f1e2c66a34032f1cf49ac2d87e6a4d622bc55c9473a3254619be888dfa2` (same at base and head) |
| Proposal | `cfc2e65d5ae91f0d62d4ef993bc22a91d2bb4716969d083ae98f0fc948eb5417` (matches the tabled value; same at base and head) |
| `_DECISIONS/_REGISTER.md` | `fe2cc825dac72b17b1b2988195acb626dbe50d6b6092adc98d3d25ebd6ac45ea` (same at base and head; one `D-PEC-103` row, `RULED A + S + M + C8 / EFFECTIVE ON MERGE`) |
| K2A brief copy | `bb0d6e3105cd9a221f9adc1572e446c096bb2af04a472a8df267356c6ba48d6b` (matches) |
| `WORKFLOW.md` / `checks.md` / standard | `84dadde4…2b` / `44ab41ac…f188` / `26c8254a…433c` (as tabled) |
| SOW tools `validate` / `derive` / `boundary` / `common` | `f0f10590…fecfe` / `bfb64dc9…0109` / `22ef57e0…ae16a` / `61a34722…0389` (as tabled) |
| `workflows/index.json` | `2bfa2c5f…dafb3` (as tabled) |
| Interpreter | Python 3.13.7 |

**Reliance-hold preflight.** Run first, from `projects/pec`, with `--operation candidate-validation` on each of the three written paths. The result was `{"status": "ALLOW"}` with exit 0, three times.

## 1. Basis: PASS

- **Ruling on main.** `git merge-base --is-ancestor d385b6a19 HEAD` exits 0. `git cat-file -e d385b6a19:<ruling>` succeeds. The ruling, proposal and register row on `d385b6a19` are byte-identical to the worktree.
- **Prep evidence intact.** In the prep folder, `shasum -a 256 -c SHA256SUMS` passes every entry (exit 0).
- **Run-root copies match prep.** I checked every non-evidence, non-verdict entry of the prep `SHA256SUMS` against the run root (`shasum -c -`, exit 0), 17 files in all:
  - `apply_k2.py` `b10461fa…257a` and `apply_k2_c8.py` `093130c8…84e9`;
  - both candidates, `aecc5131…0826` and `c7743ee2…6633`;
  - `addons/C8` (`609aa807…5693`) and both `addons/S` postimages;
  - `quotes/` ×2 and `claims/` ×2;
  - `check_cited_ids.py`, `scan_old_s2_text.py`, `test_apply_k2.py`, `verify_k2_quotes.py`, `verify_k2_state_claims.py` and `run_k2_checks.sh`.
  All equal the proposal's "Generation method" and aids table.
- **Pins of `apply_k2.py`.** I extracted `PINNED` from the script and hashed it at the worktree, at `d385b6a19` and at `125cfacc1`.
  - At base and at `125cfacc1`: 17/17 as tabled.
  - In the worktree: 16/17. The 17th, DEL-10-13 `_DEPENDENCIES.md`, now holds the C8 postimage `609aa807…5693` instead of the preimage `5087e581…eb63`. The grant intends exactly this (see Note 1).
- **Pins of `apply_k2_c8.py`.** 3/3 match in the worktree (the DEL-10-13 contract, its `Dependencies.csv`, and `Deliverables.csv`). The C8 target equals `POST` at head and `PRE` at base.

## 2. Byte identity: PASS

| Path (under `projects/pec/execution/`) | At head | Required |
|---|---|---|
| `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md` | `aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826`; absent at base | same |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/ScopeOfWork.md` | `c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633`; absent at base | same |
| `…/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` | `609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693` (base `5087e581…eb63`) | same |

- **Line comparison.** Comparing base and head line by line (54 → 55 lines, 3341 → 3537 bytes), there is exactly one inserted line, at line 7. It follows the `- **Notes:** …` line of `## Dependency Tracking Mode`. Removing it gives the preimage exactly.
- **Text match.** `grep -cxF` finds the inserted line exactly once in the proposal, so it equals the tabled line byte for byte.
- **Diff.** `git diff d385b6a19 HEAD` shows one `@@ -4,6 +4,7 @@` hunk with one `+` line.

## 3. `MODE=VERIFY` (`resources/checks.md`): PASS for both contracts

Format resolution: each folder holds one `ScopeOfWork.md` and no legacy four-document kit, so the format is `SOW_V1`. The mode is `INIT` (VERIFY of an INIT contract).

| Item | DEL-08-06 | DEL-10-13 | Evidence |
|---|---|---|---|
| 1 Pilot variance | PASS | PASS | No variance needed. Standard §7 says "New deliverables use `SOW_V1`", and neither deliverable had a contract at base. |
| 2, 5, 6, 7, 10, 11, 12, 14, 17 | NOT_APPLICABLE | NOT_APPLICABLE | `CONVERT` only |
| 3 `_STATUS.md` unchanged | PASS | PASS | `73e21846…2511` / `c7a5705d…543b`, both `**Current State:** OPEN` with one history line. No `_STATUS.md` appears in the branch diff. |
| 4 Frontmatter, headings, IDs, matrix | PASS | PASS | `validate_scope_of_work.py` printed `PASS format=SOW_V1` with exit 0, twice for each. My own parse found no duplicate definitions and contiguous numbering. Counts: DEL-08-06 OUT 3, CLM 16, REQ 16, AC 17, VER 16, AX 13, TBD 8, CON 4; DEL-10-13 OUT 2, CLM 16, REQ 18, AC 19, VER 18, AX 12, TBD 7, CON 4. Both equal the proposal table. |
| 8 OUT → scope/objective refs | PASS | PASS | Every matrix row carries `SOW-099 OBJ-001` or `SOW-100 OBJ-001`, and every defined OUT appears in the matrix. |
| 9 AC → VER or human review | PASS | PASS | AC-001..016 → VER-001..016, and AC-017 → `HUMAN_REVIEW` (DEL-08-06). AC-001..018 → VER-001..018, and AC-019 → `HUMAN_REVIEW` (DEL-10-13). |
| 13 Checklist JSON | PASS | PASS | Derived in my temp dir, twice each: `2227dbeb…9641` and `8e07ff3e…ba30`, both byte-identical to the tabled values and to the run-root `checklist_*.json`. Each AC appears exactly once, in source order, with exact text and a `qualified_id`. `source.sha256` equals the contract hash. The matrix-linked VER, or the human-review method, is carried. |
| 15 HTML | NOT_APPLICABLE | NOT_APPLICABLE | `RENDER_HTML=false` |
| 16 Return classes | PASS | PASS | The findings below are labelled schema, project content or execution substrate. |
| 18 Repeatable, fails closed | PASS | PASS | Reruns are byte-identical. Negative test in my temp dir: a copy missing a heading printed `ERROR: format state is INVALID…`, and a copy with a legacy kit added printed `…AMBIGUOUS…`. Both exited 1 and wrote no output file. |
| 19 Qualified upstream IDs | PASS | PASS | No bare local-ID token outside blockquotes is undefined, and there are no qualified `DEL-NN-NN/PFX-NNN` citations. `check_cited_ids.py` reported `RESULT PASS 0/0` (rerun). |
| 20 No mixed-method AC grouping | PASS | PASS | Every matrix row has exactly one AC: 17 and 19 rows. |
| 21 Boundary owners | PASS | PASS | See below. |
| 22 | NOT_APPLICABLE | NOT_APPLICABLE | `REVISE` only |

**Item 21 detail.**
- **Tool result.** `check_boundary_owner_resolution.py --show-not-checkable` was run twice per contract, exit 0 each time. Output: "boundary requirements checked: 1 | per-act exclusions for skill QA: 0 | … | contracts failing: 0". It reported no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`. The JSON hashes are `b2e8ee78…` and `d0197ec9…`, equal to the run root and to prep.
- **Hand resolution, DEL-08-06.**
  - REQ-014 names 23 deliverable owners, and all appear in CLM-011.
  - REQ-015 names five acts, each resolved in CLM-012 or CLM-013: the token mechanism (the §16.6 ruling), the tier-0 entry (the tier-0 owner), enabling (the consumer), advertising (the separate owner act after §12), and schema fields (the §B8 source packet).
- **Hand resolution, DEL-10-13.**
  - REQ-015's deliverable owners all appear in CLM-009, including DEL-02-01 through DEL-02-09 individually.
  - REQ-013's release acts resolve to the human owner in CLM-010, labelled as an interpretation.
  - REQ-016 is resolved with a small wording gap (Note 2).

## 4. Semantics: PASS

- **Deterministic verifiers.** Both reran on the worktree and inside the export rerun: `RESULT PASS 137/137` (quotes, tree quotations read at `125cfacc1`, "DEP rows citing this contract: 0" for both) and `RESULT PASS 482/482` (state claims).
- **Independent quote sample.** I checked these outside the verifiers, whitespace-normalized, at `125cfacc1`. All are verbatim:
  - ledger rows `SOW-099` and `SOW-100` (exact whole rows);
  - the `Deliverables.csv` and `ContextBudgetQA.csv` rows of both deliverables;
  - decomposition §3 (instruments `SOW-100`), §5 table rows, the §8 envelope sentences, `DL-6`, the `DL-21` phrases ("all mapped to OBJ-001", "SOW-099 (agent tool-call query surface, PEC-API-007 → new DEL-08-06, P3)", "the §12 P1 row is not edited (GATE-a)") and the §10 OI-006 credentials clause;
  - PRD §16.6, PEC-API-006, PEC-ORI-007, PEC-K-02/-03/-11, the §12 P3/P4 non-authorization sentence, the §8 agents clause and the §15 D-PEC-90 concordance;
  - SCA-006 `Propagation_Plan.md` §B4, §B6 (sequence, ownership and "One declared tool entry…") and §B8;
  - `Impact_Assessment.md` (DQ-a rationale, the SOW-100 instrument sentence, "like DEL-10-02", "not the metric", "Only the reliance gate…" and "Nothing is relied on now…");
  - the `SCA006-CP1-GATE` options (a) and (b) in `Decision_Log.md`;
  - the `D-PEC-101` proposal findings (E-P100 amend, DEL-04-03 not added, E-A18 precedent, "this ruling is that acceptance");
  - the `D-PEC-62` exhibit row in `PLAN_2026-07-25_project_setup_dag_gate.md`, which `D-PEC-62` names as its exhibit, and the "flags-as-flags" ruling text;
  - the DEL-08-01 "exactly owner, harness, and admin" sentence (with no `agent access class`), the DEL-10-02 release-process and C-08 "force" sentences, and the DEL-02-07 gate-record phrases;
  - the `pec.yaml` policy, status and integration fields and both gate texts;
  - Root and PEC `AGENTS.md` quotations (Root is `c8ce87ef…` at `125cfacc1`).
- **Independent state-claim sample** at `125cfacc1`:
  - Folder contents: DEL-08-06 held 6 files and no `ScopeOfWork.md`; DEL-10-13 held 6 files.
  - DEL-08-06 `Dependencies.csv`: 6 rows (2 ANCHOR; EXECUTION to 08-01, 08-02, 08-03 and 04-01), with statements as quoted. DEL-10-13 has 14 rows.
  - All 12 DEL-10-13 predecessors, plus DEL-08-01, DEL-08-03, DEL-04-01 and DEL-02-07, are `INITIALIZED`, and their contract hash prefixes equal the cited values (`e007f5307fce`, `6ec7432bf8cf`, `933c012cf16b`, `99730e4e85ce`, `8ac1dc050efb`, `013c615a0c91`, `6f4e8c66a571`, `3d1220872c55`).
  - None of DEL-03-04, 04-03, 04-05 or 10-02 contains "reliance-advertisement", `189f205ff`, `SOW-097`, `DEL-10-13` or `SOW-100`.
  - `v2/contracts/api/v1/schema.json` hash prefix is `0a4e42737e62`, and the file contains no "agent".
- **Scope.** The requirements trace to the ledger rows, the `Deliverables.csv` rows (Description, AnticipatedArtifacts, EnvelopeNotes) and PRD v2.4 (PEC-API-001/-003/-006/-007, §8, §12, PEC-ORI-006/-007, PEC-K-01/-02/-03/-10/-11, PEC-SVC-001/-002). Nothing reaches beyond the artifact lists: tool definitions + binding + tests; gate harness + gate record. Three items are method guardrails, not new scope: DEL-10-13's REQ-010 harness-identity field, REQ-013's not-evaluated record, and REQ-018's synthetic label.
- **Open items stay open.**
  - OI-006 is DEL-08-06 TBD-002 (with REQ-008 embedding no mechanism).
  - The K3 act is TBD-007 and CON-002.
  - The C-08 classification is DEL-10-13 CON-001, written to hold under either answer.
  - The DEL-02-07 edge is DEL-10-13 CON-002, with REQ-005 following whatever the register records.
  - None is decided in the contract text.
- **Objective attribution.** DEL-08-06 states "packaging, not derivation", which is weaker than §3's mapped-item listing. DEL-10-13 states "instrument", exactly as §3 does.
- **`## Remaining`.** Neither contract, nor any quote or claim file, contains "Remaining" (case-insensitive grep).

## 5. C8: PASS

- **What the line records.** "STANDING node … excluded from one-shot COMPLETE/UNBLOCKED arithmetic (owner-classified under `D-PEC-103`)". This is the owner's classification selected by the ruling ("C8", question 4). The one `D-PEC-103` token is correct, because the ruling makes the number final.
- **Placement.** It sits inside the human-owned `## Dependency Tracking Mode` section, as a bullet, and adds no heading.
- **The contract stays true.** CLM-012, CON-001 and AX-007 anchor "not made at `125cfacc1`" and "carries no such section at `125cfacc1`". Both remain true, and no requirement depends on the answer. REQ-016 binds the *harness*, not the owner's instrument.
- **Run Notes.** The `D-PEC-101` Run Notes bullet stays, and stays true.
- **No effect on checks.** Strict registers, harness, receipts and closure are identical before and after C8 in my export rerun.

## 6. Containment and lifecycle: PASS

- **Branch diff.** `git diff --name-status d385b6a19...HEAD` lists:
  - `A` for the two contracts;
  - `M` for DEL-10-13 `_DEPENDENCIES.md`;
  - `A` for `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K2A_D103_SOW_ACT.md`;
  - `A` for files under `SOW_INIT_K2_2026-09-26/` only.
- **Nothing else changed.** Filtering out those paths leaves only the three product paths. A grep for `_STATUS.md|MEMORY.md|_REGISTER|Dependencies.csv|_CONTEXT|_REFERENCES|_Decomposition|PRD|/v2/|_DomainEngines|^docs/` over the diff returns nothing.
- **Lifecycle.** Both `_STATUS.md` files are `OPEN` with their pinned hashes, so add-on S has not run.
- **Whitespace.** `git diff --check d385b6a19...HEAD` exits 0 with no output.
- **Commit order.** A (`96537e934`) comes before C8 (`ece62f792`), as the ruling orders. Each commit carries a `Co-Authored-By: Claude Opus 5.5` trailer.

## 7. Rerun method: PASS

- **Command:** `TMPDIR=<tmp> zsh <run root>/run_k2_checks.sh <worktree> d385b6a19 <run root> <tmp>/rerun`
- **Result:** exit 0, 8 min 15 s. `basis commit: d385b6a19fd630b680d29d0e9e5988391b1d0cad`, Python 3.13.7. Every line passed:
  - `PASS reliance preflight: ALLOW x7`;
  - harness/receipts exit 0 and closure clean, for pre, postA and postC8;
  - `PASS act A: check-only 0, apply 0, rerun refuses 1`;
  - `PASS containment: 2 new files, both ScopeOfWork.md`;
  - validate, checklist and boundary PASS for both contracts, with 0 NOT_CHECKABLE, 17 items = 17 AC and 19 items = 19 AC, and checklist hashes `2227dbeb…9641` and `8e07ff3e…ba30`;
  - quotes `137/137`, state claims `482/482`, cited IDs `0/0`, old S2 text `stale=0 current=43`;
  - strict, harness, receipts and closure_summary identical for pre/postA and pre/postC8;
  - `PASS add-on C8: check-only 0, apply 0, rerun refuses 1`;
  - `PASS containment after C8: 2 new contracts + 1 modified _DEPENDENCIES.md`;
  - `PASS whitespace`;
  - `PASS fault injection: RESULT PASS 19/19`;
  - `OVERALL PASS`.
- **Register output.** Strict registers exit 1, with 0 errors and 26 `XRG-013` warnings (the pre-existing, owner-deferred set), identical before and after.
- **Worktree reruns:**
  - `validate_scope_of_work.py` ×2 per contract: `PASS format=SOW_V1`, exit 0.
  - `derive_review_checklist.py` into my temp dir: byte-identical to `2227dbeb…9641` and `8e07ff3e…ba30`.
  - `check_boundary_owner_resolution.py`: exit 0, as above.
  - `verify_k2_quotes.py --tree <wt> --gitdir <wt> --prep <run root> --observation 125cfacc1`: exit 0, `RESULT PASS 137/137`.
  - `verify_k2_state_claims.py --gitdir <wt> --prep <run root>`: exit 0, `RESULT PASS 482/482`.
- **Manager's evidence vs my rerun.** Checked on `strict_postC8.out` and `harness_postC8.out`: they differ only in the command-echo line and export paths.

## Findings

1. **NOTE (execution substrate): the 17th pin is expected to differ at head.** In `apply_k2.py`'s pin table, `…/DEL-10-13_Reliance_advertisement_gate/_DEPENDENCIES.md` is pinned at the preimage `5087e581…eb63`. At head it holds `609aa807…5693`, because C8 ran after A as ordered. It matches at base and at `125cfacc1`. **Repair:** none. Record in `VALIDATION.md` that "17 pins" means 17/17 at base and 16/17 plus the C8 postimage at head.
2. **NOTE (project content): REQ-016's owner wording (QA 21 hand table).**
   - In DEL-10-13 `ScopeOfWork.md` line 152, the lifecycle owner is cited as CLM-016, which states `OPEN` but does not name `_STATUS.md` as the authority. AX-012 and CLM-004 carry that.
   - The owner of register amends ("an owner-ruled packet") is stated in CON-002 and in REQ-016 itself. The cited CLM-013 says only "is an amend".
   - Similarly, the proposal's DEL-08-06 REQ-015 row lists CLM-002, which REQ-015 does not cite directly; it resolves through CLM-012.
   - This does not fail item 21. The deterministic tool does not classify REQ-016 as a boundary-exclusion requirement, and every act resolves to an owner in text the requirement cites.
   - **Repair:** none for this act, since the bytes are ruled. At any later revision, bind the lifecycle owner and the owner-ruled-packet owner in a claim that REQ-016 cites.
3. **NOTE (project content): CON-001 is now answered outside the contract.** After C8, DEL-10-13's CLM-012 and CON-001 ("not made at `125cfacc1`") remain true as anchored observations. However, the question they leave open has been answered by `D-PEC-103` C8, as the proposal's Limits anticipate. **Repair:** state this in `HANDOFF_STATE.md` and the central receipt, so that no reader of the contract at head treats C-08 as still unmade.
4. **NOTE (project content): DEL-08-06 does not exercise "unreachable" separately.** REQ-005 (line 149) names "PEC absent or unreachable". AC-005 and VER-005 (lines 166, 200) exercise "absent, stopped, refused" and do not name "unreachable" as its own case. It is reasonably covered by "absent". **Repair:** none now. Production tests may add an explicit unreachable case, or a later revision can align the wording.
5. **NOTE (execution substrate): run-root records still to come.** `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` are not yet in the run root at `4d2c19c1d`. The K2A brief schedules them at step 8, after S. The ruling's check-1 `rely-for-production` preflight before fan-in is also still pending. `VERIFIER_BRIEF_01.md` is untracked in the run root. **Repair:** commit the brief with this verdict. Then run S (both validators already print `PASS format=SOW_V1`), the fan-in preflight, and write the three records.
6. **NOTE (schema): no schema-class defect found.** The validator, checklist derivation and boundary tool agree on both contracts, and the negative tests fail closed.

No BLOCKING or NON-BLOCKING finding. As far as this verification goes, the act is ready for add-on S.

## Temp dir

`/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k2verify.pMy3jX/`

It is left in place and holds:
- `rerun/`: the 41 outputs of `run_k2_checks.sh`, including `SUMMARY.out`. The script removed its own `k2chk.*` exports.
- `rerun_hashes.txt`
- `wt/`: the worktree checklist and boundary JSONs (×2 each), `verify_quotes.out` and `verify_state_claims.out`.
- `neg/`: the item-18 negative-test copies (`inv/`, `amb/`), with no output JSON, as the test expects.

Nothing outside this directory was created or deleted.

---

## Manager dispositions (WORKING_ITEMS; added below the verbatim verdict)

The text above this rule is the verifier's report, saved verbatim (verifier agent `a0414fd09eeccb8de`, `pec-reviewer`, opus). The verifier reviewed and did not repair.

| Note | Disposition |
|---|---|
| 1 | Recorded in `VALIDATION.md`: the 17 pins of `apply_k2.py` hash 17/17 at base and at A time; after C8, 16/17 plus the C8 postimage, as the grant intends. No change. |
| 2 | Recorded for a later revision in `HANDOFF_STATE.md`. The contract bytes are ruled; no change in this act. |
| 3 | Recorded in `HANDOFF_STATE.md` (and for HELP_HUMAN's central receipt): the C-08 question DEL-10-13 CON-001 leaves open at `125cfacc1` is answered by the owner under `D-PEC-103` C8. No contract change. |
| 4 | Recorded in `HANDOFF_STATE.md` as a production-test note. No change. |
| 5 | `VERIFIER_BRIEF_01.md` committed with this verdict; S, the `rely-for-production` fan-in preflight and the three run-root records follow. |
| 6 | No action. |
