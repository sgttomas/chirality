# Brief S1P-D — draft one current Scope of Work candidate (TASK, shared part)

Parent: WORKING_ITEMS manager of brief `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `9718ab7307b8575b286369b99ae015f4c42d6edff0f3be546e83518786b79f17`, 2026-09-26), undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S1. Role: TASK (Type 2); no delegation. Model steer: `claude-opus-5-5`, high reasoning. The per-deliverable part of this brief is in your launch prompt; it names exactly one deliverable, `<DEL>`.

This is **preparation only**. Nothing you write is a production file. Your candidate becomes a tabled postimage of an owner-ruled packet (provisional `D-PEC-104`) only if the owner rules it.

## Paths and write boundary

- Worktree (read here; it equals `origin/main` `125cfacc1` plus the prep folder): `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s1-sow-currency` (below: `REPO`).
- Prep folder: `REPO/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/` (below: `PREP`).
- **You may write exactly three files:**
  1. `PREP/candidates/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md` (same relative path as the production file);
  2. `PREP/quotes/<DEL>.json`;
  3. `PREP/claims/<DEL>.json`.
- Plus anything under your own scratch directory: create one with `mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s1pd-<DEL>.XXXX`. Delete only inside directories you created. Never delete or modify any other file in the shared scratchpad.
- Write nothing else in `REPO`. Run no mutating git command (no add, commit, checkout, stash, reset); read-only `git show`, `git log`, `git diff`, `git archive`, `git cat-file` are fine. Never run a tool against `REPO` that writes: run validators and checks on your own `git archive 125cfacc1` export with your candidate copied in.

## Authority and basis (read, and record the hashes you rely on)

- Instructions: root `AGENTS.md` (`c8ce87ef…1dffd`), `projects/pec/AGENTS.md` (`df9196d1…eb925eb8`), `agents/AGENT_TASK.md` (`1a13a5b0…8fb7`).
- Method: `chirality-root:bundled:workflow:scope-of-work`, `workflows/scope-of-work/WORKFLOW.md` (`84dadde4…bc2b`), `resources/brief.md`, `resources/checks.md`, `resources/tools.md`. Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (`26c8254a…433c`). **Authoring discipline is `MODE=INIT`** (source-grounded contract text from the accepted basis), as in the `D-PEC-98`/`D-PEC-100` precedents; the existing contract is replaced as a whole by an owner-ruled exact-bytes act. You do not use `MODE=REVISE` (the owner has deferred adopting it in PEC). `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`.
- **This is a currency revision, not a rebuild.** Start from the prior contract's exact bytes. Change only what is stale, false, or required by the per-deliverable causes below; keep every other byte, every ID and every ID's meaning. Unaffected content stays byte-identical.
- Form models for the current opening and provenance entries: the seven `D-PEC-100` postimages now on main (for example `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md`, its "Purpose and Objective Traceability" opening and its `AX-012`), and `_Coordination/_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`.
- Accepted basis: decomposition **revision 1.6** (`current_basis`, SCA-006 successor, accepted at checkpoint group 3 on 2026-09-26; `_Decomposition/_LATEST.md`). Frontmatter pin: `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a` (the checkpoint-3 acceptance commit, PR #954, an ancestor of `125cfacc1`). At the pin and at `125cfacc1` (verify): `SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`, `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`, `ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`, `docs/PRD.md` v2.4 `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`.
- **Observation commit: `origin/main` `125cfacc1`** (`125cfacc10f664685cb91802a9166b1041f42a25`, PR #979 merge, which applied `D-PEC-100`). Every statement about the state of a file, record, lifecycle or decision is either anchored to a named commit or is an observation at `125cfacc1`, and the contract says so in an "Observation commit" paragraph like the models. Never write "at the basis".
- What "current" means here:
  - revision 1.6 and PRD v2.4 (the ledger rows, `Deliverables.csv` row and `ContextBudgetQA.csv` row for your deliverable; the PRD text you quote). Quote PRD v2.4 text, never superseded PRD text as current;
  - SCA-005 (feed-model rebaseline; `_ScopeChange/SCA-005_2026-09-23_2139/`): its `Propagation_Plan.md` §B4 row for your deliverable (the cause and class in your launch prompt), the `Impact_Assessment.md` §7.1 row and any `Amendment_Preview.md` passage for your deliverable;
  - SCA-006 (`_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md` §7.1) classes every S1 deliverable NOT_AFFECTED; its changed PRD text (PEC-K-03, §8, §9, §12) is not yours to restate beyond what your contract already quotes; where your contract quotes a changed PRD passage, re-quote it as it reads in v2.4;
  - the ruled and applied `D-PEC-96` registry (schema version 2; closed profiles `shared-dev-loop`, `loop-receipts-ledger`, `agentruns-json`; PEC's row: `shared-dev-loop` live, the other two historical; `v2/config/loops.json`, `loops.schema.json`);
  - the `D-PEC-99` retirement: PEC's `_STATUS.md` files carry no `## Remaining` section; no feed profile reads such sections; they are not a work-selection surface (`projects/pec/AGENTS.md` §"Deliverable records and loop ownership"). No contract text may present a Remaining section as a current surface or read one. PEC's `loop/LOOP_RECEIPTS.md` is a closed historical ledger (Receipt 197);
  - the `D-PEC-101` currency: every `_CONTEXT.md` and `_REFERENCES.md` re-pinned to revision 1.6 / PRD v2.4; DEL-08-06 and DEL-10-13 folders exist (`OPEN`); 22 dependency rows added and DEP-09-06-003 / DEP-10-03-003 refreshed (act PR #976, merge `ce934ac33`);
  - the `D-PEC-100` S2 contracts now on main (DEL-01-01, DEL-01-06, DEL-02-03..07). The prior S2 bytes are at `9cf863697` (the parent of the act merge). What changed, per the `D-PEC-100` proposal: DEL-01-01 defines **sixteen** record-tier types (WorkGraph and WorkNode added; Workplan/Step/Gate a declared historical-grammar entity; Receipt covers ledgers and central `RECEIPT.md`), `REQ-006` (RunRecord admission) changed; DEL-01-06 is schema version 2 only (version 1 rejected); DEL-02-03 reads two grammar generations (per-loop `LOOP_RECEIPTS.md`, central `RECEIPT.md`) by declared surface; DEL-02-04 discovers only from `agentruns-json`; DEL-02-05 reads `Dependencies.csv` and `WORK_GRAPH.json` (historical), `WORK_GRAPH.md` is DEL-02-08's; DEL-02-06 reads `LOOP_INIT.md` identity, entrypoint and procedure SHA only; DEL-02-07 is re-purposed to the parity-peer reader (its feed-manifest `REQ-001` retired). **Retired S2 IDs (never cite as live):** DEL-01-01 `AX-006`; DEL-01-06 `CLM-007`, `CON-001`, `TBD-002`; DEL-02-04 `CON-002`, `CON-003`; DEL-02-06 `CON-002`, `CON-003`, `CON-005`, `TBD-004`, `TBD-005`; DEL-02-07 `CON-001`, `REQ-001`.
- **Parser carry-forward (SCA-005 §B4):** the `DEL-01-03` content-minimal guard admits only `OPEN`..`ISSUED` as STATE values; `RETIRED`, graph node states, run tokens and other out-of-class values are `DEL-01-03/CON-001` cases. Never resolve a CON by assumption.

## Currency rules

1. **Common edits (every S1 target except a correction-only target):**
   - C1 frontmatter `decomposition_basis` → the pin above (the old `@3623b958b` pin does not resolve in this repository; `11a494e9a` and `65955cceb` resolve but name superseded bases).
   - C2 the basis paragraph states revision 1.6 as the accepted basis, with the pin and hashes as in the models, and keeps the contract's authoring basis as dated history (for example: "This contract was authored against revision 1.2 (SCA-002 successor; accepted 2026-07-25 at D-PEC-64 closure), kept here as its dated basis." — verify every historical fact you keep). Add one sentence in the Purpose section: it brings the deliverable's earlier contract (SHA-256 `<12 hex>…<4 hex>`) current as a whole, and `AX-<n>` records what changed.
   - C3 an "Observation commit" paragraph (as in the models), naming `125cfacc1`.
   - C4 replace the false "`_REFERENCES.md` still names revision 1.1" claim (where present) with the ruled `D-PEC-99` DEL-04-05 wording: "The deliverable-local `_REFERENCES.md` and `_CONTEXT.md` carry their own revision pins; this contract asserts nothing about their present text."
   - C5 every quotation is re-verified at its source at `125cfacc1` (PRD v2.4, registers, `Dependencies.csv`, `_DEPENDENCIES.md`, decisions, other contracts). A quotation that no longer reads verbatim is either re-quoted from the current source, or kept as dated history with its commit named ("at this contract's authoring the cell read …", quoted from `git show <commit>:<path>` and entered in `quotes/<DEL>.json` with that commit).
   - C6 every quotation of prior S2 contract text is brought current to the S2 postimage on main, or kept only as dated history naming `9cf863697`. The drafting aid `PREP/evidence/audit_prior/<DEL>.out` lists what the heuristic found (S2-STALE, SELF, NOTFOUND spans); it is incomplete (it misses paraphrases such as "the fourteen record-tier types"), so read your whole contract.
   - C7 every stale state claim is corrected as an observation at `125cfacc1` (lifecycle, existence, counts, record states, `## Remaining`, workplans, ledgers, daemon referents, registry schema version, register cells).
   - C8 the per-deliverable cause (launch prompt).
   - C9 one new `AX-<next>` currency-provenance entry in `Governing Values and Decisions — Axiology`: the prior contract SHA-256 (full 64 hex); that this contract is that contract brought current under "the S1 Scope of Work currency packet (provisional `D-PEC-104`)", authored under `MODE=INIT` discipline against revision 1.6 and PRD v2.4; the kinds of change made (pin, basis, observation commit, the false revision-1.1 claim, re-quotations, S2 currency, stale state claims, the per-deliverable cause, any Part B item absorbed); the retired IDs (if any; qualified form, never reused); that every other ID is kept with its meaning; and new IDs. Add the new `AX` to the matrix where the models do (the objective-traceability or provenance row).
2. **ID stability.** Keep each local ID with its meaning. Retire (never reuse) an ID whose meaning you must drop, and say why. New items take the next unused number. Externally cited IDs named in your launch prompt must stay defined with their meaning.
3. **Quotations.** Quote only what the source says verbatim. Every quotation (blockquote, quoted register cell, "…" quotation of a source, quoted text of another contract) gets an entry in `quotes/<DEL>.json`. Quotations of tree files carry `"commit": "125cfacc1"` (or an older commit for dated history). A quotation of another **S1 target's** contract text (the S1 set is DEL-01-03, DEL-01-04, DEL-01-05, DEL-02-01, DEL-02-02, DEL-03-01, DEL-03-02, DEL-03-03, DEL-03-06, DEL-04-05, DEL-10-02, DEL-10-10) carries **no** `commit` and `"s1_sibling": true`: it is read from the act tree, so the manager can reconcile it against that sibling's candidate. List every such sibling quotation in your return.
4. **State claims.** Every hash, lifecycle state, existence or absence, register cell value, count or commit relation you assert or change goes into `claims/<DEL>.json` with a `candidate_text` span that appears in your candidate. Kept historical claims that you re-verified at their stated commit may be entered too; enter at least every claim in text you changed.
5. **No lifecycle, acceptance or readiness claim** beyond observation: no CHECKING, ISSUED, acceptance, release or reliance claim. Do not mention CHECKING as a gate or prompt. Lifecycle stays as observed.
6. **Boundaries (QA 21).** For every boundary-exclusion requirement you touch, enumerate the excluded acts and name one owner per act, citing a claim that names that owner.
7. **Scope.** No requirement beyond the deliverable's ledger rows, its `Deliverables.csv` row and the PRD v2.4 text they cite. Open design choices are `TBD-*` with a responsible party; substantive ambiguity is `CON-*` naming where it resolves. No CON is resolved by assumption.
8. **Part B carry-forwards** (only where your launch prompt names one): apply the exhibit's correction input **verbatim** (`_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`, SHA-256 `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`, Part B, node S1): each replacement string lands byte-exact; where the input gives a direction rather than exact words, author the minimal wording that meets it and report it as authored. Re-verify each quoted evidence value at `125cfacc1` (register cell and PRD row) and enter it in `quotes/<DEL>.json`. Enter each replacement string in `quotes/<DEL>.json` with `"source"` the exhibit path, `"commit": "125cfacc1"`, `"where": "Part B <item> locus <L>"`. The item's gate binds; the owner's ruling on this packet is what accepts the exact wording.

## JSON formats

`PREP/quotes/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "quotes": [
  {"id": "Q01", "text": "exact quoted text", "source": "projects/pec/docs/PRD.md", "commit": "125cfacc1", "where": "CLM-003"},
  {"id": "Q02", "text": "cell text", "source": "projects/pec/execution/_Decomposition/ScopeLedger.csv", "kind": "csv_cell", "key_column": "ScopeItemID", "key": "SOW-013", "column": "Notes", "commit": "125cfacc1", "where": "CLM-001"},
  {"id": "Q03", "text": "text as it was", "source": "path", "commit": "3e5291138", "where": "CLM-007 (dated history)"},
  {"id": "Q04", "text": "sibling text", "source": "projects/pec/execution/PKG-03_…/DEL-03-01_…/ScopeOfWork.md", "s1_sibling": true, "where": "CLM-012"}
]}
```

`strip_emphasis: true` drops `**` on both sides. Minimum 12 characters after whitespace collapse. The checker normalizes blockquote markers and whitespace only.

`PREP/claims/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "claims": [
  {"id": "S01", "commit": "125cfacc1", "kind": "sha256", "path": "projects/pec/docs/PRD.md", "value": "<64 hex>", "candidate_text": "`ae49b8065698…3fbe`"},
  {"id": "S02", "commit": "125cfacc1", "kind": "contains", "path": "…/_STATUS.md", "value": "**Current State:** INITIALIZED", "candidate_text": "`INITIALIZED`"},
  {"id": "S03", "commit": "189f205ff", "kind": "ancestor", "value": "125cfacc1", "candidate_text": "an ancestor of `origin/main` `125cfacc1`"}
]}
```

Kinds: `sha256`, `sha256_prefix` (≥ 12 hex), `contains`, `not_contains`, `exists`, `absent`, `ancestor` (commit is ancestor of value), `csv_cell` (value `{key_column, key, column, equals|contains}`), `count_glob` (value `{pattern, count[, contains]}`). Details in `PREP/verify_s1p_state_claims.py`.

## Self-check before returning (on your scratch export, never on `REPO`)

```text
E=$(mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s1pd-<DEL>.XXXX)
git -C REPO archive 125cfacc1 | tar -x -C $E
cp <candidate> $E/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md
cd $E && PYTHONDONTWRITEBYTECODE=1 python3 tools/scope_of_work/validate_scope_of_work.py projects/pec/execution/<PKG>/1_Working/<DEL folder>
python3 tools/scope_of_work/derive_review_checklist.py --output $E/checklist.json <DEL folder>   (twice; byte-identical)
python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $E/boundary.json --show-not-checkable <DEL folder>/ScopeOfWork.md
python3 PREP/verify_s1p_quotes.py --tree $E --gitdir REPO --prep PREP --observation 125cfacc1 --only <DEL> [--obs-exempt <DEL> for a correction-only target]
python3 PREP/verify_s1p_state_claims.py --gitdir REPO --prep PREP --only <DEL>
python3 PREP/check_qualified_ids.py --prep PREP --gitdir REPO --observation 125cfacc1   (your own lines must pass)
python3 PREP/aids/audit_quotes.py --tree $E --gitdir REPO --s2-prior 9cf863697 $E/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md   (informational: no S2-STALE, and every NOTFOUND/SELF span explained)
diff <prior contract> <candidate>   (every hunk is one of C1–C9 or the Part B item)
```

Other drafters work in parallel on the other S1 targets; their files may appear in `PREP` while you work. Ignore their results in the shared verifiers (use `--only <DEL>`).

Required: `PASS format=SOW_V1`; checklist exit 0 and byte-identical reruns; boundary 0 `UNRESOLVED_OWNER` / `UNDEFINED_CLAIM` (hand-resolve each `NOT_CHECKABLE` in your return); both verifiers `RESULT PASS` for your deliverable; qualified-ID check passes for your citations; a QA 19 scan showing no bare upstream ID in own-voice prose; QA 20 (no grouped ACs with different method sets). Iterate until all pass.

## Return (your final message to the manager)

1. Candidate path, SHA-256, line count; ID counts per prefix; kept, retired and new IDs.
2. A change table: each hunk of the diff (prior line range → candidate line range), its class (C1–C9 or Part B), and the source for the change.
3. Every `CON-*` and `TBD-*` you added or changed, with where each resolves.
4. External anchors: each externally cited ID kept with its meaning (or why not).
5. Every quotation of an S1 sibling's text (for the manager's reconciliation), and every fact you relied on from another contract.
6. Self-check outputs (commands, exit codes, result lines), QA 21 hand resolution.
7. Sources read, with SHA-256 or commit.
8. Anything unresolved, and anything you found false or stale that you did not change (inside your contract, with why; or outside your write boundary: report, do not repair).
