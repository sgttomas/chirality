# VERIFIER_VERDICT_01: D-PEC-102 act (S4 Scope of Work currency), independent MODE=VERIFY

**Verdict: PASS WITH NOTES.** Nothing is blocking. There is one non-blocking record finding and there are six notes. This verdict makes no CHECKING, ISSUED, acceptance, REVIEW-gate, readiness, release or reliance claim.

- **Candidate:** branch `claude/pec-d102-s4-sow-act`, commit `a26ca1613378ded4d9a2f97afa6bbb81249b00c8`, read in place in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d102-act`. Base is `4c2a7768ff43ef2d3590a37a28e53c519de744d9` (PR #994 merge). Commits in the act: `70a3cebf9`, `5d13cfdb8`, `a26ca1613`.
- **Verifier identity:** TASK (Type 2), read-only. Mechanism: a delegated-harness-native subagent (Claude Code / Agent SDK) dispatched by the WORKING_ITEMS manager of undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, node S4. Workflow: `chirality-root:bundled:workflow:scope-of-work`, `MODE=VERIFY`. Host-reported model: Opus 5.5 (`claude-opus-5-5`). The "high" reasoning effort is instruction-asserted only. I authored nothing under review.
- **Date:** 2026-09-26 (session date). Python 3.13.7.

## Sources relied on (SHA-256, identical in the worktree and at `a26ca1613`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` |
| `workflows/scope-of-work/resources/tools.md` (hashed only, not loaded) | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (hashed only, not loaded) | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` |
| `_DECISIONS/D-PEC-102_RULING_2026-09-26.md` | `782ee02fc5fc6375bc001568061796562ee2b82a603b601bee7f6e02a1bdd288` |
| `_DECISIONS/D-PEC-102_s4_sow_currency_proposal_2026-09-26.md` | `baf178125e37ea8d82735f0bd4c0913531188ca9daffd95309339eb82fffcfdd` |
| `_DECISIONS/_REGISTER.md` | `e167f532a1749b11e2c5850b9b636e533569bbe50a99b0b68d95c26339efe4bf` |
| `D-PEC-99` `EXHIBIT_MOVED_ITEMS.md` | `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e` |
| Prep `SHA256SUMS` | `bf127a693eb27019ba76792159e7342db43c1bab2f6b22a6868a96952617f611` |
| Brief copy `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S4A_D102_SOW_ACT.md` | `98f744886651e3d4ce9e54ef22dbbbbfaca486de421b45b9e80e46ceada6932e` |
| Run-root `apply_s4p.py` | `2b6792fee7b69266ad28f517734f89f9c01b60c6e6d4489118fd14375f364869` |

The run-root check aids hash as the proposal's aid table gives them:
- `test_apply_s4p.py` `644ee64a…`
- `verify_s4p_quotes.py` `57bf8dfd…`
- `verify_s4p_state_claims.py` `6feb6114…`
- `check_sibling_ids.py` `1e74c88a…`
- `check_quote_currency.py` `f398b4b0…`
- `scan_s2_quotes.py` `940bc2f7…`
- `scan_external_quotes.py` `bb2402e7…`
- `run_s4p_checks.sh` `228ede0c…`
- `negative_controls.sh` `6f7d2c75…`
- `build_apply_s4p.py` `df714b6d…`
- `apply_s4p.template.py` `04e8507a…`

The `quotes/` and `claims/` inputs are byte-identical to the prep folder.

## 1. Basis — PASS

**Fetch and drift.** `git fetch origin` moved `origin/main` from `4c2a7768f` to `78e74f590d6010a52565d250288290b3305a2942` (PR #995).
- `git diff --name-only 4c2a7768f origin/main` shows 106 paths under `projects/chirality-app-dev/**`, 2 under `exports/chirality-app/**`, 1 under `projects/chirality-runtime/**` and `docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927.yaml`.
- Nothing under `projects/pec/**`, `tools/`, `workflows/` or `agents/` changed.
- So no target, pin or quoted locus moved (see Note N1).

**Ruling and register row.** Both are on `origin/main`. The ruling, proposal, exhibit and `_REGISTER.md` hash the same at `4c2a7768f`, `origin/main` and `a26ca1613`.
- Register row `D-PEC-102` reads "RULED A / PART B AND 3a, 3b CONFIRMED / M / EFFECTIVE ON MERGE".
- The ruling commit `ea4b6e73a` is an ancestor of `4c2a7768f`.
- The owner's words in the ruling are verbatim: "D-PEC-102: A; confirm Part B; confirm 3a 3b; M; defaults".

**Script.** The run-root `apply_s4p.py` equals `2b6792fe…4869` in the worktree, at `a26ca1613` and in the prep folder.

**TARGETS and PINNED.** I imported the script and parsed the proposal's grant tables:
- TARGETS equals the 8-row grant table, including order and the pre/post hashes.
- PINNED equals the 19 listed pins.

**Pins.** All 19 pins match at `4c2a7768f`, `a26ca1613` and `origin/main`, with 0 mismatches.

**Prep SHA256SUMS.** `shasum -a 256 -c` gives exit 0 with no non-OK line (recorded as 107/107).

## 2. Byte identity — PASS

For each of the eight targets:
- the base (`4c2a7768f`) blob equals the tabled preimage;
- the candidate (`a26ca1613`) blob equals the tabled postimage;
- the worktree file, the run-root `candidates/…` copy and the prep `candidates/…` copy all equal the postimage;
- `origin/main` still holds the preimage.

Result: 8/8 true on every comparison.

## 3. MODE=VERIFY, mode-applicable checks.md subset — PASS

Run on a `git archive a26ca1613` export:

- **Item 1 (pilot variance covers the path).** The eight paths are exactly the owner-ruled grant. `SOW_V1` is the production format; all eight validate.
- **Item 3 (`_STATUS.md` byte-identical, lifecycle unchanged).** `git diff --quiet 4c2a7768f a26ca1613 -- <each _STATUS.md>` exits 0 ×8. All eight read `**Current State:** INITIALIZED`. The eight `_STATUS.md` are among the 19 pins, all matching. No `MEMORY.md` exists.
- **Item 4 (contract validates).** `validate_scope_of_work.py <DEL folder>` gives exit 0 and `PASS format=SOW_V1` ×8.
- **Item 8 (every `OUT-*` maps to scope/objective).** Every matrix `OUT` row's objective refs are within the frontmatter. `project_scope_refs` equals `Deliverables.csv` `CoversScopeItems` for all eight: DEL-08-03 is `[SOW-043, SOW-098]` and DEL-04-03 is `[SOW-006, SOW-007, SOW-097]`, the only two that changed. `package_objective_refs` equals `SupportsObjectives`.
- **Item 9 (every `AC-*` has a `VER-*` or human review).** Every defined AC appears exactly once in the matrix (19/16/9/21/16/23/19/12) with a `VER-*` or `HUMAN_REVIEW`.
- **Item 13 (checklist derivation).** `derive_review_checklist.py` exits 0 ×8. The hashes equal the prepared hashes: DEL-04-01 `1d8cccbc…`, DEL-04-02 `4b039956…`, DEL-08-01 `2b5beadb…`, DEL-08-03 `b91cf9f4…`, DEL-08-04 `afe85efd…`, DEL-04-03 `85f0d3bc…`, DEL-03-04 `1a86fa42…`, DEL-10-03 `24272d5d…`. Each also equals the run-root `checklist_<DEL>.json`.
- **Item 16.** This return keeps schema findings (none), project-content findings (below) and execution-substrate observations (Notes) apart.
- **Item 18 (repeat derivation byte-identical).** A second derivation is byte-identical ×8. Negative control 6 (a removed matrix row fails validation) trips on rerun.
- **Item 19 (upstream IDs cited correctly).** I scanned own-voice prose, outside blockquotes, for bare upstream-shaped IDs near a deliverable name. Every hit is a local reference, for example "`DEL-01-01` contract quoted in CLM-011". `check_sibling_ids.py` gives `RESULT PASS 57/57`.
- **Item 20 (grouped matrix rows).** Only one row groups ACs: DEL-08-01 `AC-001, AC-005` → `VER-001`. Both criteria are verified only by `VER-001`, so the grouping is permitted. It is carried from the preimage.
- **Item 21 (boundary owners).** `check_boundary_owner_resolution.py --show-not-checkable` exits 0 ×8 with 0 `UNRESOLVED_OWNER` and 0 `UNDEFINED_CLAIM`. `NOT_CHECKABLE` counts are 5/4/0/7/1/3/2/1 (DEL-04-01/02, 08-01/03/04, 04-03, 03-04, 10-03). The JSON is identical to the run-root `boundary_<DEL>.json`.
  - **Hand resolution.** I parsed each flagged requirement and the claims the proposal's table names:
    - Every named owner is actually named in the claim the table gives.
    - Where the table says a claim is not cited (DEL-04-01 REQ-003 → CLM-015; DEL-04-02 REQ-008 → CLM-015, CLM-006; DEL-08-03 REQ-004 and REQ-020 → CLM-009), that is accurate, and the owner is still named in the contract.
    - Where the table gives no claims (DEL-04-02 REQ-006, REQ-007; DEL-08-03 REQ-008, REQ-009, REQ-017, REQ-018), the owner is named in a claim the requirement does cite (CLM-015, CLM-007, CLM-009 or CLM-013).
  - One row is imprecise: see F1.

## 4. Semantics — PASS

**Quotes and claims (scripts).**
- `verify_s4p_quotes.py --tree <a26ca1613 export> --gitdir <worktree> --prep <run root> --observation 125cfacc1` gives exit 0 and `RESULT PASS 740/740`.
- `verify_s4p_state_claims.py` gives exit 0 and `RESULT PASS 1144/1144`.
- `scan_s2_quotes.py --prior-commit ce934ac33` gives `SUMMARY stale=0 kept=2`.

**Quotes and claims (my own spot-checks at `125cfacc1`).** All present verbatim, allowing for source line-wrap normalization:
- the `SOW-004` ledger row, including `,SCA-005,FALSE,`;
- PEC-ORI-001, both PEC-K-03 passages, the §8 Agents bullet, the §12 parity clause, the PEC-API-006 phrases "by dropping citations, stamps or stated limitations" and "Numeric budgets are confirmed at Phase 1", and the PEC-ORI-007 line "No consumer may treat silence as a claim";
- the `projects/pec/AGENTS.md` reliance-distinction sentence;
- the `loops.schema.json` "Surfaces: …" and "historical: …" strings;
- the two exhibit framing phrases DEL-04-01 CLM-020 quotes;
- D-PEC-90 grant item 1;
- in SCA-006 `Propagation_Plan.md`, both pass rules and "`D-PEC-90` grant item 1 bars rebuilding it around verify-before-rely";
- the SCA-006 IA §13.2 sentence ("…separately testable declaration, distinct from stamping.") and "**Not offered:** stating numeric budgets now…";
- the SCA-005 `Amendment_Preview.md` A-02 and A-22 phrases;
- D-PEC-62's "RULED as drafted" and "including the C-08 standing-node exclusion from one-shot blocker arithmetic" (L214–215);
- the `DEP-08-06-006` row values;
- DEL-08-02 `**Current State:** CHECKING`;
- `v2/contracts/api/v1/schema.json` `0a4e4273…`;
- `git grep -E 'OrientationSnapshot|WorkNode|reconcil|orientation' 125cfacc1 -- projects/pec/v2/src/` returns no hits (exit 1), which matches DEL-04-01 CLM-009.

**Scope.** Every requirement I read stays within its deliverable's ledger rows, `Deliverables.csv` row and PRD v2.4. I word-diffed every changed or new `OUT`/`REQ`/`AC`/`CON`/`TBD` record against its preimage for all eight. The new obligations track SCA-006 and SCA-005 scope:
- `agent` class: SOW-003;
- SOW-097 envelope: DEL-04-03;
- SOW-098 budgets: DEL-08-03;
- terminal completion: SOW-004;
- tool-call and gate exclusions: stated as owner-cited exclusions.

**Open items.** New and changed `CON` items route resolution to owners, K2, a scope change or the production packet, and none is decided. Examples: DEL-08-01 CON-003, DEL-08-03 CON-005 to CON-007, DEL-04-02 CON-006 to CON-008, DEL-08-04 CON-007 and CON-008, DEL-03-04 CON-007, DEL-10-03 CON-004, DEL-04-01 CON-005 to CON-008.

**IDs.** Compared with each preimage at `4c2a7768f`:
- no ID is retired, duplicated or reused;
- every new ID is numbered above the prior maximum of its prefix;
- the defined-ID counts equal the proposal's candidate table exactly (for example DEL-04-01: OUT 2, CLM 23, REQ 18, AC 19, VER 18, AX 15, TBD 5, CON 8);
- DEL-04-01's AX-014 changed-ID list is a superset of the changed records I detected.

**Verify-before-rely.** "verify-before-rely" occurs only in quotations of prior text or D-PEC-90/SCA-006 records, or in statements that the contract is not built around it.

**Part B, verbatim with gates binding** (checked byte-for-byte against the exhibit):
- DEL-04-01-REM-001 and REM-002 clause lines appear once each as raw-byte blockquote lines (L281, L289).
- The identical Gate line appears exactly twice (L283, L291).
- CLM-020 L277 states the gates "still bind", with the separate exact owner-ruled DEL-04-01 production packet on `origin/main`, WORKING_ITEMS activation and a current reliance preflight, and upstream sequencing unchanged. AX-015 and the Praxeology ("Production waits for the gates of CLM-020") repeat this.
- The three added verification sentences sit in the Praxeology opening (L421–425), verbatim after whitespace normalization (Note N2).
- The trace table L297–344 maps all 46 prior REQ/AC/VER IDs to kept successors.
- DEL-04-02-REM-002:
  - (1) opening, raw-exact at L19;
  - (2) and (3) at CLM-008, L172 and L174;
  - (4) at AX-010, L381;
  - (5) at AC-016 L307 and matrix L446, both phrases.
  - Each new text occurs once, and each replaced old text is present in the preimage and absent from the postimage.
  - The E-P33 quotation and the `[E-P26]` sentence are unchanged: word-diff shows only the (3) replacement on that line, and CLM-011 L237 equals preimage L217.
  - The Gate line is quoted at L389.
- DEL-04-03-REM-002:
  - (1) opening, raw-exact at L20;
  - (2) both CLM-010 replacements at L213, with the "Two cells…" passage removed;
  - (3) AX-010 at L383.
  - The E-P34 block at post L215–223 is byte-identical to pre L170–178.
  - The Gate line is present.

**Reading 3a.**
- DEL-04-01 REQ-001 (L360) requires all seven components, terminal completion included, and "no eighth component shall be added".
- It is grounded in CLM-001 (the revision-1.6 SOW-004 row, verified) and CLM-002 (PRD v2.4 PEC-ORI-001, verified).

**Reading 3b.**
- DEL-04-03 REQ-001, REQ-005 and REQ-008 are byte-identical to the preimage.
- REQ-001 keeps "no fourth stamp field added".
- REQ-016 reads "The envelope is declared beside the three-field stamp of REQ-001 and is not a stamp field".
- CLM-019 grounds it in SOW-097 Notes "distinct from SOW-006 stamping" and IA §13.2.

**Seven-component consistency.** Every current count of DEL-04-01's components across the eight postimages says seven:
- DEL-04-01 CLM-002, OUT-001, CLM-006, REQ-001, REQ-004, AC-001, AC-004, CON-001, CON-004 ("seven stated absences"), VER-001, VER-002 and the matrix;
- DEL-04-02 CLM-015 L245, REQ-011 L286, AC-011 L302, AX-008 L379;
- DEL-04-03 CLM-011 L225, which cites `DEL-04-01/REQ-001` with "terminal completion … included";
- DEL-08-04, which cites `DEL-04-01/REQ-001` without a count;
- DEL-08-03 CON-004, which dropped its prior "six named components" and cites `DEL-04-03/CON-004`.

"Six" appears only historically: DEL-04-01 CLM-002 ("The revision-1.4 statement enumerated six") and AX-014 ("in place of six").

**No `## Remaining` work surface.** DEL-04-01 CLM-021 excludes Remaining sections as a source. The other postimages mention them only as retired history under D-PEC-99.

## 5. Containment and lifecycle — PASS

**Diff.** `git diff --name-status origin/main...a26ca1613` (merge base still `4c2a7768f`) gives:
- 8 × `M` for the eight `ScopeOfWork.md`;
- 1 × `A` for the brief copy (hash `98f74488…932e`, matching);
- 185 × `A` under `SOW_CURRENCY_S4_2026-09-26/`.

**Nothing else.** A grep for `_STATUS.md|_REVIEW.md|Review_Findings|MEMORY.md|_REGISTER|Dependencies.csv|_DEPENDENCIES|_CONTEXT|_REFERENCES|_SEMANTIC|_Decomposition|/v2/|PRD|docs/` finds nothing (exit 1). There are no `__pycache__`, `.pyc` or `.s4ptmp` files. `git diff --check origin/main...a26ca1613` exits 0.

**Recorded evidence against my reruns** (fresh `git archive` exports of `4c2a7768f` as pre and `a26ca1613` as post):
- strict registers: exit 1, `ERROR findings: 0`, `WARNING findings: 26` (XRG-013). Pre and post are identical, and each equals the recorded `strict_pre.out` and `post/strict_post.out` after path normalization.
- `harness.py self-check`: exit 0, pre and post identical, each equal to the recorded files.
- `validate_pec_loop_receipts.py`: exit 0, pre and post identical, each equal to the recorded files.
- `check_quote_currency.py`: `SUMMARY active_execution_quotes_verbatim 127/127`, pre and post identical, each equal to the recorded files.
- My quote, claim and sibling result lines equal the recorded `post/quotes.out`, `post/state_claims.out` and `post/sibling_ids.out`.
- My validate and boundary outputs equal the recorded `post/validate_*.out` and `post/boundary_*.out`.

**Full runner.** `run_s4p_checks.sh <worktree> 4c2a7768f <a26ca1613-export run root> <out>` gives exit 0 and OVERALL PASS. It covers the act (0/0/1), containment of 8 SOW files, per-contract validate/checklist/boundary ×8, 740/740, 1144/1144, 57/57, S2 stale=0, strict/harness/receipts/quote-currency identical, whitespace, and fault injection 9/9. My `SUMMARY.out` is byte-identical to the recorded `rerun_4c2a7768f/SUMMARY.out`. The other outputs differ only in export paths.

**Negative controls.** `negative_controls.sh` rerun gives exit 0, and all six lines are identical to the recorded `negative_controls.out`.

**Preflight ordering.** The recorded timestamps put `dispatch-for-production` before the act and `rely-for-production` after it:

| Step | Time (UTC) | Detail |
|---|---|---|
| Preconditions | 04:51:29Z | `origin/main` = `4c2a7768f` |
| `dispatch-for-production` ×8 | 04:51:45Z | ALLOW, exit 0, HEAD `4c2a7768f` |
| Act | 04:53:46Z | HEAD `70a3cebf9`, exit 0, "write set = grant … pinned 19/19 unchanged" |
| `rely-for-production` ×8 | 04:54:03Z–04:54:04Z | ALLOW, exit 0 |
| Act commit `5d13cfdb8` | 04:54:05Z | |

The register hash `f877d931…` and script hash `b1712e4b…` match the proposal.

## Manager decision: running the run-root copy with output redirected into the run root

This is consistent with the script and the proposal.
- The script sets `SELF_DIR = Path(__file__).resolve().parent`, and `inventory()` prunes that directory, resolved, from `os.walk`. So the whole run-root subtree is excluded, including `evidence/apply_run.out`, which the shell creates before the script starts.
- The placement guard accepts the path, because `rel_self` starts with `projects/pec/execution/_Coordination/SOW_CURRENCY_S4_`.
- The docstring (L26–31) states this purpose explicitly.
- The proposal says so under "Write set" (L359) and "Finite verification" (L379): "Record each command, exit code and output in the run root; the act script leaves its own directory out of its write-set inventory."
- The copy run was the committed bound bytes: HEAD `70a3cebf9` holds the run root, and the hash is `2b6792fe…`.

The residual effect is that writes inside the run root are not policed by the inventory. Git containment shows only additions there, within the default-writable `_Coordination/**` fence.

## Findings

### BLOCKING
None.

### NON-BLOCKING
**F1 — QA 21 hand-resolution row for DEL-10-03 is imprecise.**
- Locus: proposal `D-PEC-102_s4_sow_currency_proposal_2026-09-26.md` L409 (and the preamble L398), against DEL-10-03 `ScopeOfWork.md` L381 (REQ-013).
- The row gives the owner `DEL-08-01` as named in "(CLM-008, CLM-016)". But REQ-013 cites only CLM-011, and CON-003 is not a claim. Neither CLM-008 nor CLM-016 is cited by REQ-013.
- The table's own convention ("where the requirement itself does not cite that claim, the row says so") calls for a "not cited" annotation, which is missing.
- The preamble says such gaps "are carried from the prior contracts", but REQ-013 is new in this pass: it does not occur in the preimage.
- Substantively the owner is resolved. REQ-013 names `DEL-08-01` in its own text, and the tool-checked whole-requirement exclusion REQ-015 excludes "token path or access-class decision (`DEL-08-01`)" citing CLM-016, which names it.
- The proposal is fixed bytes, so there is nothing to repair in the act. Record it in `VALIDATION.md`. A later DEL-10-03 revision could cite CLM-016 in REQ-013 so the tool can reach it.

### NOTES
**N1 — The base is behind `origin/main` by PR #995** (`78e74f590`: App, exports, one Runtime path and one Root tranche manifest; no `projects/pec` path). No target, pin or quoted locus is affected: pins and preimages verified at `origin/main`.
- The brief asks, if main moves, to merge without rebase and "rerun `--check-only`". After the act, `--check-only` refuses by design ("target does not hold its preimage"; `post/rerun_refuses.out`).
- The meaningful rerun is `run_s4p_checks.sh` on the new base export plus the quote and state-claim verifiers.

**N2 — The three REM-002 verification sentences match only after whitespace normalization.** Locus: DEL-04-01 L421–425.
- The exhibit clause is one line. The postimage re-wraps the sentences across Markdown soft line breaks, so they are verbatim after whitespace normalization, which is how the quote verifier checks them, but not as a raw byte run.
- The clause paragraphs and both Gate lines are raw-byte verbatim.
- The proposal's "verbatim" is accurate in the Markdown sense. No action.

**N3 — A carried sentence sits beside a carried claim about `_CONTEXT.md`.** Locus: DEL-04-02 L19 and L146.
- The owner-accepted exhibit sentence at L19 says "this contract asserts nothing about their present text" (`_REFERENCES.md`, `_CONTEXT.md`).
- L146, byte-identical from the preimage, still says "`_CONTEXT.md` records "(none)"". That is true at `125cfacc1` (`_CONTEXT.md` L25).
- This is a mild tension between two accepted texts, not a falsehood. No action.

**N4 — Dated "provisional / not yet ruled" wording remains in all eight postimages** (for example DEL-04-01 L469, DEL-04-02 L20 and L385). It was disclosed at proposal L243. It is true under each contract's `125cfacc1` observation clause.

**N5 — `evidence/apply_check_only.out` has no timestamp line.** Its order is still evident from commit `70a3cebf9` (04:53:34Z) and the `apply_run.out` header. Negative control 6 prints an empty detail `()`, which is cosmetic.

**N6 — DEL-08-04 CLM-005 and CON-006 now read D-PEC-62 more precisely.** They say the owner's "RULED as drafted" confirmed the C-08 standing-node exclusion. I verified this at D-PEC-62 L214–215. It is consistent with DEL-04-01 and DEL-04-02 AX-010, which call the set a recorded-but-unresolved annotation. No action.

## Footprint

- **Created:** one scratch directory, `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4a-verify.kafX2b`. It held:
  - `git archive` exports of `4c2a7768f` and `a26ca1613`, each with an empty `.git` whose `objects/info/alternates` borrowed the worktree's object store (read-only), as `run_s4p_checks.sh` does;
  - the runner, negative-control and direct-check outputs;
  - my small check scripts (`cmp.py`, `partb.py`, `partb2.py`, `ids.py`, `rdiff.py`, `qa21.py`).
- **Environment:** `TMPDIR` was exported to that directory and `PYTHONDONTWRITEBYTECODE=1` was set for every Python run.
- **Deleted:** only that directory (`rm -rf` of its exact path; confirmed absent afterwards).
- **Repository operations:** `git fetch origin` (it updated remote-tracking refs only), plus `git show`, `git diff`, `git log`, `git ls-tree`, `git archive` and `git grep`. No edit, stage, commit, push, checkout, reset, stash, branch or worktree operation.
- **Checkouts:** `git status --short` in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d102-act` (HEAD still `a26ca1613`) and in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5` is empty in both after the run.
