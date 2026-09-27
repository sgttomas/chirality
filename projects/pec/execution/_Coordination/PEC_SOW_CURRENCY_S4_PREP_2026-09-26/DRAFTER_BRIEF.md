# Brief S4P-D — draft one current Scope of Work candidate (TASK, shared part)

Parent: WORKING_ITEMS manager of brief `S4P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `d00a739afc1f4bc03bd5bd9862fb104d880c22ccce6859dbe85c7e588802dc67`, 2026-09-26), undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S4. Role: TASK (Type 2); no delegation. Model steer: `claude-opus-5-5`, high reasoning. The per-deliverable part of this brief is in your launch prompt; it names exactly one deliverable, `<DEL>`.

This is **preparation only**. Nothing you write is a production file. Your candidate becomes the tabled postimage of an owner-ruled packet (provisional `D-PEC-102`) only if the owner rules it.

## Paths and write boundary

- Worktree (read only): `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s4-sow-currency` (below: `REPO`). It equals `origin/main` `125cfacc1` (`125cfacc10f664685cb91802a9166b1041f42a25`, the PR #979 merge) plus the prep folder `REPO/projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/` (below: `PREP`), which holds this brief and the check aids.
- Staging folder (below: `STAGE`): `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4p_mgr/stage/`. The manager copies staged files into `PREP`.
- **You may write exactly three files, all under `STAGE`:**
  1. `STAGE/candidates/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md` (same relative path as the production file);
  2. `STAGE/quotes/<DEL>.json`;
  3. `STAGE/claims/<DEL>.json`.
- Plus anything inside your own scratch directory, created with `mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4pd.XXXXXX`. **Delete only inside directories you created with `mktemp -d`.** Never delete, move or overwrite anything else in the shared scratchpad (other agents' files live there), never run `rm` on a glob of the scratchpad, and never write to `/tmp` directly.
- Write nothing in `REPO` or any other checkout. Run no mutating git command (no add, commit, checkout, stash, reset, worktree); read-only `git show`, `git log`, `git diff`, `git grep`, `git archive` are fine. Never run a tool against `REPO` that writes: run validators and checks on your own `git archive 125cfacc1` export with your candidate copied in.

## Authority and basis (read, and record hashes you rely on)

- Instructions: root `AGENTS.md` (`c8ce87ef…1dffd`), `projects/pec/AGENTS.md` (`df9196d1…5eb8`), `agents/AGENT_TASK.md` (`1a13a5b0…8fb7`).
- Method: `chirality-root:bundled:workflow:scope-of-work`: `workflows/scope-of-work/WORKFLOW.md` (`84dadde4…bc2b`), `resources/brief.md`, `resources/checks.md`, `resources/tools.md`. Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (`26c8254a…433c`). **Authoring discipline is `MODE=INIT`**: source-grounded authoring of a whole contract from the accepted basis, as in the `D-PEC-98` and `D-PEC-100` precedents. The existing contract is replaced as a whole by an owner-ruled exact-bytes act. You do not use `MODE=REVISE` (the owner has deferred adopting it in PEC). `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`.
- Form models (all on `origin/main`): the seven `D-PEC-100` postimages, for example `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` (it carries `D-PEC-99` Part B items verbatim) and `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md`; the packet `_Coordination/_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`. Follow their form: frontmatter keys; the six required headings; "Identity of record / Placement in the work graph / Boundaries"; an "Observation commit" paragraph; qualified upstream IDs (`DEL-01-03/CON-001`) or blockquote with the carve-out sentence; one `AC-*` per Output and Evaluation Matrix row unless their method sets are identical; a closing human-review criterion for objective traceability; `TBD-*` and `CON-*` for everything open; a rebuild-provenance `AX-*`.
- Accepted basis: decomposition **revision 1.6** (`current_basis`, SCA-006 successor, accepted at checkpoint group 3 on 2026-09-26). Frontmatter pin: `decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a` (the checkpoint-3 acceptance commit, PR #954, an ancestor of `origin/main`). At the pin and at `125cfacc1`: `SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`, `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`, `ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`, `docs/PRD.md` v2.4 `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` (verify). `project_scope_refs` follows the deliverable's revision-1.6 `CoversScopeItems` (`Deliverables.csv`).
- **Observation commit: `origin/main` `125cfacc1`.** Every statement about the state of a file, record, lifecycle or decision is either anchored to a named commit or is an observation at `125cfacc1`, and the contract says so in its "Observation commit" paragraph (write the short SHA `125cfacc1` literally; the checker looks for it). Never write "at the basis".

## What "current" means for node S4

Read `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (the S4 row and the "Order" section) in full. Then:

1. **SCA-006 (operational reliance; PRD v2.4).** Read `_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md` §B4 (the S4 membership table and its **pass rules**), `Impact_Assessment.md` §7.1 (the SOW loci for your deliverable), `PRD_V2_4_SUCCESSOR_DIFF.md` and the PRD v2.4 text itself: PEC-K-03 (§6), §8 "Agents" bullet and the access-class sentence (owner, harness, agent, admin; `agent` is read-only query), PEC-ORI-007 (the reliance envelope), PEC-API-006 (response-size budgets; numbers at Phase 1), PEC-API-007 (the agent tool-call query surface; P3; tier-0 profile act before any tool is declared), the §12 standing reliance-advertisement gate, §15 `D-PEC-90` lineage. The pass rules bind you:
   - one pass carries both the SCA-005 and SCA-006 causes; quote PRD v2.4 and revision 1.6, never v2.3 text that SCA-006 changed;
   - **no contract is rebuilt around verify-before-rely** (`D-PEC-90` grant item 1, `_DECISIONS/D-PEC-90_RULING_2026-09-25.md`). Operational reliance is written as available only from a PEC release that has passed the PRD §12 reliance-advertisement gate. It is never authority (PEC-K-02), and it is distinct from the reliance-hold control and from professional reliance (`projects/pec/AGENTS.md`);
   - the new deliverables DEL-08-06 (agent tool-call query surface, SOW-099) and DEL-10-13 (reliance-advertisement gate, SOW-100) exist since `D-PEC-101` (folders, `_STATUS.md` `OPEN`, `Dependencies.csv`), and have no Scope of Work yet. Cite them by deliverable ID and register row only, never by a local ID.
2. **SCA-005 causes** that the S2 packet did not carry for this deliverable: `_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` §B4 (your row, the `@3623b958b` pin and false "revision 1.1" housekeeping where ticked) and the SCA-005 `Amendment_Preview.md` section for your deliverable if one exists.
3. **S2 quotation currency.** `D-PEC-100` replaced the contracts of DEL-01-01, DEL-01-06, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06 and DEL-02-07 (act merged in PR #979, `125cfacc1`; prior bytes readable at `ce934ac33`). Find every place your contract quotes, paraphrases or cites one of those seven contracts (search for each ID) and bring it current against the postimage on `origin/main` (for example DEL-01-01 now defines sixteen record-tier types, not fourteen, and its `REQ-006` rule changed). Qualified citations must resolve to IDs defined in the current S2 contract. `PREP/scan_s2_quotes.py` gives a heuristic start (`--tree <your export> --gitdir REPO --prior-commit ce934ac33`); it is not exhaustive.
4. **`D-PEC-101` currency** (ruled; act merged PR #976 `ce934ac33`): every deliverable's `_CONTEXT.md` and `_REFERENCES.md` now name revision 1.6 and PRD v2.4; `D-PEC-101` K1 added dependency rows (SOW-097..100 anchors; DEL-08-06/DEL-10-13 edges) and refreshed the DEP-10-03-003 quote. Any claim in your contract about those files' present text is re-checked or dropped.
5. **`D-PEC-99`** (ruled; act PR #957): `_STATUS.md` files carry no `## Remaining` section; no feed profile reads such sections; they are not a work-selection surface. No contract text may present a Remaining section as a current surface or read one. Exhibit: `_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` (`69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`).
6. **`D-PEC-96`** (ruled registry, schema version 2, three feed profiles) and the other ruled records named in `projects/pec/AGENTS.md`, where your contract touches them.
7. **Anything else stale.** Re-check every state claim in the prior contract at `125cfacc1` (lifecycles of upstream deliverables — for example DEL-10-01, DEL-08-02 and DEL-00-03 are `CHECKING`, DEL-01-03 and DEL-01-05 `IN_PROGRESS`; source that now exists under `v2/`; register cells; dependency rows; hashes; decision records). Keep true history as dated history; correct present-tense claims that are no longer true.

## Rebuild rules

1. **Whole contract, minimal churn.** Read the existing contract (SHA-256 in your launch prompt) and every source it cites. **Keep every sentence that is still true and in scope byte-for-byte** (other contracts quote these contracts; unchanged bytes keep their quotations valid). Rewrite what is stale; add what revision 1.6 and PRD v2.4 now require. Every claim traces to an accepted source or to an observation at a named commit.
2. **ID stability.** Keep each existing local ID whose meaning survives, with that meaning (its rule may be brought current). Never reuse an ID whose meaning you drop; retire it. New items take the next unused number for their prefix. In `Governing Values and Decisions — Axiology` add one rebuild-provenance entry (a new `AX-*`) stating: the prior contract SHA-256 and its basis pin; that this contract is its currency rebuild under "the S4 Scope of Work currency packet (provisional `D-PEC-102`)" (not yet ruled); the SCA-005 and SCA-006 causes it carries; the retired IDs (qualified, as the prior contract's); the kept IDs whose rule changed; and that kept IDs keep their meaning.
3. **Externally anchored text.** Your launch prompt lists every ACTIVE `Dependencies.csv` `EvidenceQuote` whose `EvidenceFile` is your contract and every other contract's qualified citation or quotation of your IDs. Keep each such `EvidenceQuote` as a **raw, byte-exact substring on one line** of your candidate (the checker is `in` on the raw file). Keep each externally cited ID with its meaning. Where another contract quotes your text, keep that text verbatim unless it is now false or stale; if you must change it, report the change (the packet discloses it; you do not repair the other contract).
4. **Quotations.** Quote only what the source says verbatim. Every presented quotation (blockquote, quoted register cell, "…" quotation of a source) gets an entry in `quotes/<DEL>.json`. **Every entry carries `"commit": "125cfacc1"`** (or an earlier named commit), so the check reads the source there. Do not quote a sibling S4 contract's text (cite its qualified ID instead); siblings change in the same act.
5. **State claims.** Every hash, lifecycle state, existence or absence, register cell value, count or commit relation you assert goes into `claims/<DEL>.json` with a `candidate_text` span that appears in your candidate.
6. **No lifecycle, acceptance or readiness claim** beyond observation: no CHECKING, ISSUED, acceptance, release or reliance claim. Do not mention CHECKING as a gate or prompt (stating another deliverable's observed lifecycle state as a fact is fine). Your deliverable's lifecycle stays as observed.
7. **Boundaries.** For every boundary-exclusion requirement, enumerate the excluded acts and name one owner per act, citing a claim that names that owner (QA 21). Prefer syntactic binding so `check_boundary_owner_resolution.py` can check it. New owners under SCA-006 (for example DEL-08-06 for the tool-call surface, DEL-10-13 for the gate) are named where your deliverable's boundary now touches them.
8. **Scope.** No requirement beyond the deliverable's ledger rows, its `Deliverables.csv` row and the PRD v2.4 text they cite. Open design choices are `TBD-*` with a responsible party; substantive ambiguity is `CON-*` naming where it resolves. **Never resolve a `CON` by assumption.**
9. **`D-PEC-99` Part B carry-forwards** (only where your launch prompt names one). Carry the item exactly as the launch prompt says: a production-obligation item's "Carry-forward input" paragraph and its "Gate" line verbatim in blockquotes with the carve-out sentence (the DEL-02-07 postimage `### Carried production obligations (D-PEC-99 exhibit Part B)` subsection is the model), with a statement in the contract's own voice that the gate still binds here; a documentary-correction item's replacement texts verbatim at the loci it names. Add one quote entry per carried text with `"source"` the exhibit path and `"commit": "125cfacc1"`.

## JSON formats

`STAGE/quotes/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "quotes": [
  {"id": "Q01", "text": "exact quoted text", "source": "projects/pec/docs/PRD.md", "commit": "125cfacc1", "where": "CLM-003"},
  {"id": "Q02", "text": "cell text", "source": "projects/pec/execution/_Decomposition/ScopeLedger.csv", "commit": "125cfacc1", "kind": "csv_cell", "key_column": "ScopeItemID", "key": "SOW-013", "column": "Notes", "where": "CLM-001"}
]}
```

`strip_emphasis: true` drops `**` on both sides. Minimum 12 characters after whitespace collapse. Blockquote markers are stripped and whitespace is collapsed on both sides.

`STAGE/claims/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "claims": [
  {"id": "S01", "commit": "125cfacc1", "kind": "sha256", "path": "projects/pec/docs/PRD.md", "value": "<64 hex>", "candidate_text": "`ae49b8065698…3fbe`"},
  {"id": "S02", "commit": "125cfacc1", "kind": "contains", "path": "…/_STATUS.md", "value": "**Current State:** INITIALIZED", "candidate_text": "`INITIALIZED`"},
  {"id": "S03", "commit": "189f205ff", "kind": "ancestor", "value": "125cfacc1", "candidate_text": "an ancestor of `origin/main`"}
]}
```

Kinds: `sha256`, `sha256_prefix` (≥ 12 hex), `contains`, `not_contains`, `exists`, `absent`, `ancestor` (commit is ancestor of value), `csv_cell` (value `{key_column, key, column, equals|contains}`), `count_glob` (value `{pattern, count[, contains]}`). Details in `PREP/verify_s4p_state_claims.py`.

## Self-check before returning (on your scratch export, never on `REPO`)

```text
X=$(mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/s4pd.XXXXXX)
git -C REPO archive 125cfacc1 | tar -x -C $X
cp <STAGE candidate> $X/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md
cd $X && PYTHONDONTWRITEBYTECODE=1 python3 tools/scope_of_work/validate_scope_of_work.py projects/pec/execution/<PKG>/1_Working/<DEL folder>
python3 tools/scope_of_work/derive_review_checklist.py --output $X/checklist.json <DEL folder>   (twice; byte-identical)
python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $X/boundary.json --show-not-checkable <DEL folder>/ScopeOfWork.md
python3 PREP/verify_s4p_quotes.py --tree $X --gitdir REPO --prep STAGE --observation 125cfacc1 --only <DEL>
python3 PREP/verify_s4p_state_claims.py --gitdir REPO --prep STAGE --only <DEL>
python3 PREP/scan_s2_quotes.py --tree $X --gitdir REPO --prior-commit ce934ac33 --candidates STAGE   (informational; your line must show no STALE)
rm -rf "$X"   (your own mktemp directory only)
```

Required: `PASS format=SOW_V1`; checklist exit 0 and byte-identical reruns; boundary 0 `UNRESOLVED_OWNER` / `UNDEFINED_CLAIM` (hand-resolve each `NOT_CHECKABLE` in your return); both verifiers `RESULT PASS`; a QA 19 scan showing no bare upstream ID in own-voice prose; QA 20 (no grouped ACs with different method sets); no trailing whitespace or tabs; a final newline. Iterate until all pass. (`scan_s2_quotes.py --candidates` needs all eight candidates staged; if siblings are missing, skip it and grep your own candidate instead.)

## Return (your final message to the manager)

1. Candidate path, SHA-256, line count; ID counts per prefix; kept, retired and new IDs; kept IDs whose rule changed.
2. What changed and why, per section, with the source for each change (compact), grouped as SCA-006 causes, SCA-005 causes, S2 quotation currency, Part B, other staleness.
3. Every `CON-*` and `TBD-*`, with where each resolves.
4. External anchors: each dependency quote and each externally cited or quoted ID or text kept (or changed, with reason).
5. Interface facts you rely on from a sibling S4 deliverable (DEL-04-01, DEL-04-02, DEL-04-03, DEL-08-01, DEL-08-03, DEL-08-04, DEL-03-04, DEL-10-03) — the manager reconciles these across the eight candidates.
6. For Part B items: the exact candidate line numbers where each carried text lands, and the local IDs that implement it.
7. Self-check outputs (commands, exit codes, result lines), QA 21 hand resolution.
8. Sources read, with SHA-256 or commit.
9. Anything unresolved, and anything you found false or stale outside your write boundary (report; do not repair).
