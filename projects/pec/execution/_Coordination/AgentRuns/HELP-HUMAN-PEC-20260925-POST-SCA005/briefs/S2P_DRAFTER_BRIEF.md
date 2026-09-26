# Brief S2P-D — draft one rebuilt Scope of Work candidate (TASK, shared part)

Parent: WORKING_ITEMS manager of brief `S2P_SOW_REBUILD_PROPOSAL.md` (SHA-256 `31313b8f…6d5c`, 2026-09-26), undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, graph node S2. Role: TASK (Type 2); no delegation. Model steer: `claude-opus-5-5`, high reasoning. The per-deliverable part of this brief is in your launch prompt; it names exactly one deliverable, `<DEL>`.

This is **preparation only**. Nothing you write is a production file. Your candidate becomes the tabled postimage of an owner-ruled packet (provisional `D-PEC-100`) only if the owner rules it.

## Paths and write boundary

- Worktree (read here; it equals `origin/main` `aca930622` plus the prep folder): `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s2-sow-rebuild` (below: `REPO`).
- Prep folder: `REPO/projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/` (below: `PREP`).
- **You may write exactly three files:**
  1. `PREP/candidates/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md` (same relative path as the production file);
  2. `PREP/quotes/<DEL>.json`;
  3. `PREP/claims/<DEL>.json`.
- Plus anything under your own scratch directory (create one with `mktemp -d` under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`).
- Write nothing else in `REPO`. Run no mutating git command (no add, commit, checkout, stash, reset); read-only `git show`, `git log`, `git diff`, `git archive` are fine. Never run a tool against `REPO` that writes: run validators and checks on your own `git archive aca930622` export with your candidate copied in.

## Authority and basis (read, and record hashes you rely on)

- Instructions: root `AGENTS.md` (`c8ce87ef…ffd`), `projects/pec/AGENTS.md` (`df9196d1…eb925eb8` at `aca930622`), `agents/AGENT_TASK.md`.
- Method: `chirality-root:bundled:workflow:scope-of-work`, `workflows/scope-of-work/WORKFLOW.md` (`84dadde4…bc2b`), `resources/brief.md`, `resources/checks.md`, `resources/tools.md`. Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` (`26c8254a…433c`). **Authoring discipline is `MODE=INIT`**: source-grounded authoring of a whole new contract from the accepted basis, as in the `D-PEC-98` precedent. The existing contract is replaced as a whole by an owner-ruled exact-bytes act; you do not use `MODE=REVISE` (the owner has deferred adopting it in PEC). `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`.
- Form models: the merged first contracts `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` and `DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` (both under `REPO/projects/pec/execution/`), and the packet that produced them, `_Coordination/_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md`. Follow their form: frontmatter keys; the six required headings; "Identity of record / Placement in the work graph / Boundaries"; qualified upstream IDs (`DEL-01-03/CON-001`) or blockquote with the carve-out sentence; one `AC-*` per Output and Evaluation Matrix row unless their method sets are identical; a closing human-review criterion for objective traceability; `TBD-*` and `CON-*` for everything open.
- Accepted basis: decomposition **revision 1.6** (`current_basis`, SCA-006 successor, accepted at checkpoint group 3 on 2026-09-26). Frontmatter pin: `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a` (the checkpoint-3 acceptance commit, PR #954). At the pin and at `aca930622`: `SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`, `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`, `ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`, `docs/PRD.md` v2.4 `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` (all byte-identical between the pin and `aca930622`; verify).
- **Observation commit: `origin/main` `aca930622`** (`aca9306224…`, PR #958 merge). Every statement about the state of a file, record, lifecycle or decision is either anchored to a named commit or is an observation at `aca930622`, and the contract says so in an "Observation commit" paragraph like the models. Never write "at the basis".
- What "current" means here (the node S2 row of `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`; read it in full):
  - revision 1.6 and PRD v2.4 (read `_Decomposition/_LATEST.md`; the ledger rows, `Deliverables.csv` row and `ContextBudgetQA.csv` row for your deliverable; the relevant PRD text);
  - the SCA-005 feed model (`_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` §B4 and the `Amendment_Preview.md` section for your deliverable; the feed-model design note `_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`);
  - the ruled and applied `D-PEC-96` registry: `v2/config/loops.json` (`fd342b4f…53d7`) and `loops.schema.json` (`104ed648…b143`) at schema version 2, the closed three-profile vocabulary (`shared-dev-loop`, `loop-receipts-ledger`, `agentruns-json`, each v1), PEC's row migrated (`shared-dev-loop` live; the other two historical); act merged as PR #950 (`73ed349ed`); ruling `_DECISIONS/D-PEC-96_RULING_2026-09-26.md`;
  - the `D-PEC-99` retirement: PEC's `_STATUS.md` files carry no `## Remaining` section; no feed profile reads such sections; they are not a work-selection surface (`projects/pec/AGENTS.md` §"Deliverable records and loop ownership"). No contract text may present a Remaining section as a current surface or read one;
  - SCA-006 (reliance amendment) classes your deliverable NOT_AFFECTED (`_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md` §7.1); PRD v2.4's changed text (PEC-K-03, §8, §9, §12) is not yours to restate beyond what your scope needs. Quote PRD v2.4 text, never v2.3 text as current.
- **Parser carry-forward (graph S2 row; SCA-005 §B4):** the `DEL-01-03` content-minimal guard admits only `OPEN`..`ISSUED` as STATE values; `RETIRED`, graph node states, run tokens and other values outside its produced classes are `DEL-01-03/CON-001` cases. Where your deliverable emits such values, record a `CON-*` routed to `DEL-01-03` (and `DEL-01-01` where typing is involved). Read the guard (`v2/src/pec_v2/core/content_minimal_guard.py`, `740a4a74…19ee9`, produced, not accepted) and the `DEL-01-03` contract (`986ef155…6341`). Never resolve a CON by assumption.

## Rebuild rules

1. **Whole-contract rebuild, grounded.** Read the existing contract (its SHA-256 is in your launch prompt) and every source it cites. Keep what is still true and in scope; rewrite what is stale; add what revision 1.6 now requires. Every claim traces to an accepted source or to an observation at a named commit.
2. **ID stability.** Keep each existing local ID (`OUT-`, `CLM-`, `REQ-`, `AC-`, `VER-`, `AX-`, `TBD-`, `CON-`, etc.) whose meaning survives, with that meaning. Never reuse an ID whose meaning you drop; retire it. New items take the next unused number for their prefix. In `Governing Values and Decisions — Axiology` add one rebuild-provenance entry (a new `AX-*`) stating: the prior contract SHA-256; that this contract is its rebuild under the S2 packet (provisional `D-PEC-100`, not yet ruled — write it as "the S2 Scope of Work rebuild packet (provisional `D-PEC-100`)"); the retired IDs; and that IDs kept keep their meaning.
3. **Externally anchored text.** The launch prompt lists any `Dependencies.csv` `EvidenceQuote` that cites your contract and any other contract's qualified citation of your IDs. Keep each such `EvidenceQuote` as a **raw, byte-exact substring on one line** of your candidate (the checker is `in` on the raw file, as `gen_d95.py` checks it), and keep each externally cited ID. If keeping one would state something false, keep the verbatim span, add a qualifying sentence after it, and report it.
4. **Quotations.** Quote only what the source says verbatim. Where you present text as quoted (blockquote, quoted register cell, "…" quotation of a source), add an entry to `quotes/<DEL>.json`.
5. **State claims.** Every hash, lifecycle state, existence or absence, register cell value, count or commit relation you assert goes into `claims/<DEL>.json` with a `candidate_text` span that appears in your candidate.
6. **No lifecycle, acceptance or readiness claim** beyond observation: no CHECKING, ISSUED, acceptance, release or reliance claim. Do not mention CHECKING as a gate or prompt. Lifecycle stays as observed (all seven S2 deliverables are `INITIALIZED` at `aca930622`).
7. **Boundaries.** For every boundary-exclusion requirement, enumerate the excluded acts and name one owner per act, citing a claim that names that owner (QA 21). Prefer syntactic binding so `check_boundary_owner_resolution.py` can check it.
8. **Scope.** No requirement beyond the deliverable's ledger rows, its `Deliverables.csv` row and the PRD v2.4 text they cite. Open design choices are `TBD-*` with a responsible party; substantive ambiguity is `CON-*` naming where it resolves.

## JSON formats

`PREP/quotes/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "quotes": [
  {"id": "Q01", "text": "exact quoted text", "source": "projects/pec/docs/PRD.md", "where": "CLM-003"},
  {"id": "Q02", "text": "cell text", "source": "projects/pec/execution/_Decomposition/ScopeLedger.csv", "kind": "csv_cell", "key_column": "ScopeItemID", "key": "SOW-013", "column": "Notes", "where": "CLM-001"},
  {"id": "Q03", "text": "text as it was", "source": "path", "commit": "189f205ff", "where": "…"}
]}
```

Without `commit`, the source is read from the tree (`aca930622`). `strip_emphasis: true` drops `**` on both sides. Minimum 12 characters after whitespace collapse.

`PREP/claims/<DEL>.json`:

```json
{"deliverable": "DEL-XX-YY", "claims": [
  {"id": "S01", "commit": "aca930622", "kind": "sha256", "path": "projects/pec/docs/PRD.md", "value": "<64 hex>", "candidate_text": "`ae49b8065698…3fbe`"},
  {"id": "S02", "commit": "aca930622", "kind": "contains", "path": "…/_STATUS.md", "value": "**Current State:** INITIALIZED", "candidate_text": "`INITIALIZED`"},
  {"id": "S03", "commit": "189f205ff", "kind": "ancestor", "value": "aca930622", "candidate_text": "an ancestor of `origin/main`"}
]}
```

Kinds: `sha256`, `sha256_prefix` (≥ 12 hex), `contains`, `not_contains`, `exists`, `absent`, `ancestor` (commit is ancestor of value), `csv_cell` (value `{key_column, key, column, equals|contains}`), `count_glob` (value `{pattern, count[, contains]}`). Details in `PREP/verify_s2p_state_claims.py`.

## Self-check before returning (on your scratch export, never on `REPO`)

```text
E=$(mktemp -d …/scratchpad/s2pd.XXXX); git -C REPO archive aca930622 | tar -x -C $E
cp <candidate> $E/projects/pec/execution/<PKG>/1_Working/<DEL folder>/ScopeOfWork.md
cd $E && PYTHONDONTWRITEBYTECODE=1 python3 tools/scope_of_work/validate_scope_of_work.py projects/pec/execution/<PKG>/1_Working/<DEL folder>
python3 tools/scope_of_work/derive_review_checklist.py --output $E/checklist.json <DEL folder>   (twice; byte-identical)
python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $E/boundary.json --show-not-checkable <DEL folder>/ScopeOfWork.md
python3 PREP/verify_s2p_quotes.py --tree $E --gitdir REPO --prep PREP --observation aca930622 --only <DEL>
python3 PREP/verify_s2p_state_claims.py --gitdir REPO --prep PREP --only <DEL>
```

Required: `PASS format=SOW_V1`; checklist exit 0 and byte-identical reruns; boundary 0 `UNRESOLVED_OWNER` / `UNDEFINED_CLAIM` (hand-resolve each `NOT_CHECKABLE` in your return); both verifiers `RESULT PASS`; a QA 19 scan showing no bare upstream ID in own-voice prose; QA 20 (no grouped ACs with different method sets). Iterate until all pass.

## Return (your final message to the manager)

1. Candidate path, SHA-256, line count; ID counts per prefix; kept, retired and new IDs.
2. What changed and why, per section, with the source for each change (compact).
3. Every `CON-*` and `TBD-*`, with where each resolves.
4. External anchors: each dependency quote and cited ID kept (or qualified, with reason).
5. Cross-deliverable facts you relied on from another S2 deliverable's current contract (the manager reconciles these across the seven candidates).
6. Self-check outputs (commands, exit codes, result lines), QA 21 hand resolution.
7. Sources read, with SHA-256 or commit.
8. Anything unresolved, and anything you found false or stale outside your write boundary (report; do not repair).
