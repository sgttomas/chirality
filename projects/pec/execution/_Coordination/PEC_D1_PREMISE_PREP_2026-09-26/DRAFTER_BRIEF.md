# Brief D1P-D — draft premise-only amendments (TASK, shared part)

Parent: WORKING_ITEMS manager of brief `briefs/D1P_PREMISE_PROPOSAL.md` (SHA-256 `d1cdf4e3104d38a08e8bef8c3641070d942ec9ad2744bddeb9cadfb482cbc1f1`) with `COMMON.md` (`51b70e46f1049696c456be1d4ab7b4b236e3cbfc6fa3a667ed0426035510b311`), undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1 (provisional `D-PEC-105`). Role: TASK (Type 2); no delegation. Model: `claude-opus-5-5`, high reasoning. Your launch prompt names your targets (one deliverable's artifact and Scope of Work) and seeds the premise inventory for them.

This is **preparation only**. Nothing you write is a production file. Your candidates become tabled postimages of an owner-ruled packet only if the owner rules it.

## Paths and write boundary

- Worktree (read only): `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d1-premise-proposal` (below `REPO`), on branch `claude/pec-d1-premise-proposal`, equal to `origin/main` `6c6cc1b00` (`6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`, the PR #992 merge) plus the prep folder `REPO/projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/` (below `PREP`), which holds this brief, `targets.json` and the check aids `render_candidates.py`, `verify_d1p_quotes.py`, `verify_d1p_state_claims.py`.
- Create your own staging directory: `STAGE=$(mktemp -d /private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/d1pd.XXXXXX)` and `export TMPDIR=$STAGE`. **Create and delete files only inside directories you created with `mktemp -d`.** Never delete, move or overwrite anything else in the shared scratchpad, never `rm` a glob of it, never write to `/tmp` directly.
- Copy `PREP/targets.json` into `STAGE/`. You write, under `STAGE`, exactly: `premise/<KEY>.json`, `quotes/<KEY>.json`, `claims/<KEY>.json` for each of your keys, and the rendered `candidates/<target path>` (produced by `render_candidates.py --write`, never hand-edited). Anything else goes in your own `mktemp -d` scratch.
- Write nothing in `REPO` or any other checkout. Read-only git only (`show`, `log`, `diff`, `grep`, `archive`). Never check out a branch anywhere. Run validators on your own `git archive 6c6cc1b00` export with the candidate copied in.

## Authority and basis (read; record the hashes you rely on)

- Instructions: root `AGENTS.md` (`c8ce87ef…1dffd`), `projects/pec/AGENTS.md` (`df9196d1…5eb8`), `agents/AGENT_TASK.md`.
- **The scope-binding sources for D1:**
  - SCA-005 `_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` §B5 (and its rows at L50, L828–829, L873–876); its `Impact_Assessment.md` rows 287–288, 308–309, 358, 513; `Supersession_Map.csv`; and the inventory rows `INV-130..132`, `INV-178..184` in `_Coordination/SCA-005_PREP_2026-09-23/IMPACT_INVENTORY_PEC_BASIS.csv`. SCA-005 amendment 1 deferred cmux out of scope (owner 2026-09-24: "no plans for cmux compatibility").
  - SCA-006 `_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md` §B5 and its rows at L89, L307, L313.
  - The work graph `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (D1 row, and the `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` bullet).
- **Current basis.** Decomposition revision 1.6 (`current_basis`), accepted at SCA-006 checkpoint group 3; pin commit `189f205ff` (`189f205ff02df4111b33c20be441ce06e65ada7a`, PR #954), an ancestor of `6c6cc1b00`. At both commits: `SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`, `Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`, `ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`, `docs/PRD.md` v2.4 `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`. Revision 1.6 facts: 100 scope items (74 IN / 18 OUT / 8 TBD); 11 packages; 68 deliverable rows (64 active; DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05 retired under SCA-005; DEL-02-08, DEL-02-09 added under SCA-005; DEL-08-06, DEL-10-13 added under SCA-006); PRD v2.4 carries 49 `PEC-*-NNN` requirements (PEC-ORI-007, PEC-API-006 and PEC-API-007 are new under SCA-006) and 11 invariants. Verify every fact you use.
- **Ruled records since** (all on `origin/main`): `D-PEC-90` (operational reliance, R-A), `D-PEC-95` and `D-PEC-101` (context and reference re-pins to revisions 1.5 and 1.6), `D-PEC-96` (registry), `D-PEC-99` (Remaining retirement), `D-PEC-100`, `D-PEC-103`. Root: `docs/DIRECTIVE.md` §D-GOV-43 (A2 supplement), `docs/CONTRACT.md` K-RUNTIME-1.
- **Observation commit `6c6cc1b00`.** Every state claim you add is either anchored to a named commit or is an observation at `6c6cc1b00`. Never write "at the basis".

## What D1 is, and the rule you apply

The artifacts are accepted derivative products of `CHECKING` deliverables. D1 is a **premise-only amendment**: the owner-accepted bytes remain history, and no other content is revised.

1. **A premise** is a statement in the target that was true when the bytes were accepted and is false at the current basis because of SCA-005 or SCA-006, including their propagation acts (`D-PEC-93`, `D-PEC-95`, `D-PEC-101`) and the PRD successors they adopted. A present-tense statement that a later scope change contradicts is a premise. A count or completeness claim ("the full catalogue", "all 64 deliverables", "a complete structural index") that a scope change made false is a premise.
2. **Change only premises**, plus the smallest coherent consequence inside the same sentence or table row (for example a count that the corrected list changes). Historical statements stay unchanged: "born from PRD v2.2 and revision 1.3 at `11a494e9a`", "seeded before P1 from revision 1.3", the D-PEC-72 selection, dated rulings. Do not restyle, reorder, re-explain or improve anything else.
3. **Other findings** — stale or imperfect text that is not a premise made false by SCA-005/SCA-006 (for example something already stale since SCA-004, or a wording gap) — are **reported, not changed**.
4. **One premise-amendment note per artifact**, inserted immediately after the artifact's basis paragraph ("**Born from:**" in the SPEC; "**Accepted basis:**" in the ADRs), in exactly this form with the artifact's accepted SHA-256 filled in:

   ```text
   **Premise amendment:** premises that SCA-005 and SCA-006 made false are
   brought current to `projects/pec/docs/PRD.md` v2.4 and decomposition
   revision 1.6 (`current_basis`, accepted at `189f205ff`), under an
   owner-ruled exact-byte packet of work-graph node D1
   (`HELP-HUMAN-PEC-20260925-POST-SCA005`). The owner-accepted bytes this
   amends (SHA-256 `<64 hex>`) remain history; nothing else is revised, and
   no acceptance of these bytes is recorded here.
   ```

   Keep the artifact's own line-wrapping style (about 78 columns). Do not name a D-PEC number anywhere in a candidate (the number is provisional).
5. **Scope of Work targets.** Keep every ID and its meaning; no ID is retired or reused; add no `REQ`/`AC`/`VER` unless a premise cannot be corrected otherwise (then say why). Add exactly one new `AX-*` (next unused number) as premise-amendment provenance: the prior contract SHA-256; that this contract's bytes are the premise-only amendment of work-graph node D1 under an owner-ruled exact-byte packet (name no number); the SCA-005/SCA-006 causes; the kept IDs whose rule changed; that kept IDs keep their meaning; an observation sentence ("Every state claim not anchored to a named commit is an observation at `origin/main` `6c6cc1b00`."); and the pin `189f205ff`. The frontmatter `decomposition_basis` stays the contract's birth basis unless it is itself a premise the method requires changing (report your reasoning). The contract must still validate `PASS format=SOW_V1`; its `AC-*` checklist is re-derived.
6. **Quotations stay verbatim.** A quotation of a register or document that is still verbatim at its source stays, even if the source's own text is old (for example the `Deliverables.csv` envelope note and `SOFTWARE_DECOMP.md` §1.4 intake posture 1 still read "46"); correct the false premise in your own voice next to it. A quotation whose source text changed is re-quoted from the current source.
7. **Operational reliance** (SCA-006, `D-PEC-90` R-A): state it only as the PRD states it — available only from a PEC release that has passed the PRD §12 reliance-advertisement gate, within the pin, coverage and trust tier a response declares, never authority (PEC-K-02), file fallback where PEC is absent, degraded, failing its checks or stating a limitation. Nothing is built around verify-before-rely (`D-PEC-90` grant item 1).
8. **Runtime topology** (SCA-005, `D-GOV-43` A2): no per-user runtime daemon exists; the App starts, owns and stops one Runtime service child, which owns the stock `codex app-server` child together with sessions, delegation, tools, turn admission/locks and interruption for that App instance; credentials are custodied by Codex; local-model residency is retired; `D-GOV-43` supersedes `D-GOV-20` items 2–4 on that path. The hooks CLI is the only remaining bridge; the Runtime SSE bridge and the runtime-client seam are deferred behind trigger T-RT (SOW-035, SOW-087 OUT); the cmux adapter is deferred, re-entry only by a later owner direction (SOW-037 OUT). Quote or cite the PRD v2.4 / revision 1.6 / Root text you rely on.
9. **No lifecycle, acceptance or readiness claim.** Do not mention CHECKING as a gate or prompt; do not claim acceptance, issuance, release or reliance.
10. **External anchors.** Keep verbatim any text another contract quotes from your targets, unless it is itself a false premise (then report the quoting file and line). Keep every ID another contract cites.

## Premise ledger (how the candidate is made)

For each key write `STAGE/premise/<KEY>.json`:

```json
{"key": "DEL-00-03_SPEC",
 "target": "projects/pec/execution/…/artifacts/v2/SPEC.md",
 "preimage_sha256": "<as in targets.json>",
 "hunks": [
  {"id": "P01", "locus": "L23 (§1)", "cause": "SCA-006 Propagation_Plan §B5 (requirement counts L23, L62); PRD v2.4 §9",
   "pre": "exact old text (unique in the running text)", "post": "exact new text",
   "why": "one line: what was true, what made it false, the current source"}
 ]}
```

Then `python3 PREP/render_candidates.py --gitdir REPO --prep STAGE --write --only <KEY>` renders the candidate from the preimage at `6c6cc1b00`; every byte outside the hunks is the accepted preimage. Keep hunks as small as a whole sentence or table row allows. Hunks apply in order; each `pre` must occur exactly once in the running text when it applies.

## Evidence files

- `STAGE/quotes/<KEY>.json`: `{"key": "<KEY>", "quotes": [{"id": "Q01", "text": "…", "source": "<repo-relative path>", "commit": "189f205ff", "where": "P03 / CLM-006"}, …]}`. One entry for **every quotation that appears in any `post` text**, and, for Scope of Work targets, for **every presented quotation anywhere in the candidate** (register cells may use `"kind": "csv_cell", "key_column", "key", "column"`). Every entry names a commit (`189f205ff` for decomposition and PRD; `6c6cc1b00` or an earlier named commit otherwise). Minimum 12 characters after whitespace collapse; blockquote markers are stripped; `"strip_emphasis": true` drops `**`.
- `STAGE/claims/<KEY>.json`: `{"key": "<KEY>", "claims": [{"id": "S01", "commit": "189f205ff", "kind": "sha256", "path": "…", "value": "<64 hex>", "candidate_text": "…"}, …]}`. One entry for **every hash, count, lifecycle state, existence/absence, register cell value or commit relation asserted in any `post` text** (kinds: `sha256`, `sha256_prefix`, `contains`, `not_contains`, `exists`, `absent`, `ancestor`, `csv_cell`, `count_glob`; see `PREP/verify_d1p_state_claims.py`). For register counts use `contains` on the §7 telemetry line of `SOFTWARE_DECOMP.md` or on the ledger rows.

## Self-check (on your own export; never on `REPO`)

```text
X=$(mktemp -d $STAGE/x.XXXXXX); git -C REPO archive 6c6cc1b00 | tar -x -C $X
python3 PREP/render_candidates.py --gitdir REPO --prep $STAGE --write --only <KEY>
python3 PREP/render_candidates.py --gitdir REPO --prep $STAGE --only <KEY>            # PASS
cp $STAGE/candidates/<target> $X/<target>                                             # each of your targets
(cd $X && PYTHONDONTWRITEBYTECODE=1 python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>)       # SOW targets: PASS format=SOW_V1
(cd $X && python3 tools/scope_of_work/derive_review_checklist.py --output $X/cl1.json <DEL folder>)             # twice, byte-identical
(cd $X && python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $X/b.json --show-not-checkable <DEL folder>/ScopeOfWork.md)
python3 PREP/verify_d1p_quotes.py --tree $X --gitdir REPO --prep $STAGE --observation 6c6cc1b00 --only <KEY>...  # RESULT PASS
python3 PREP/verify_d1p_state_claims.py --gitdir REPO --prep $STAGE --only <KEY>...                            # RESULT PASS
grep -nE ' +$|	' <candidates>; tail -c1 <candidate> | xxd                              # no trailing blanks or tabs; final newline
```

Iterate until everything passes. Also diff the preimage checklist with the postimage checklist and report which `AC-*` texts changed.

## Return (your final message)

1. Per key: candidate path, SHA-256, line count, hunk count.
2. **Premise inventory**: one row per hunk — locus, prior text (short), cause (SCA-005/SCA-006 source row), current source (path, commit), new text (short).
3. **Every locus you examined and left unchanged on purpose**, with the reason (historical, still true, quotation still verbatim, not a premise).
4. **Other findings** (not premises; not changed), with evidence.
5. External anchors: any other contract, register or record that quotes or cites text you changed (file, line, what goes stale).
6. For SOW targets: IDs whose rule changed; the new `AX-*`; the checklist diff (which `AC-*` changed); validator, checklist and boundary outputs, and QA 21 hand resolution of any `NOT_CHECKABLE`.
7. Self-check commands with exit codes and result lines.
8. Sources read, with SHA-256 or commit.
9. Anything unresolved, and anything false outside your targets (report; do not repair).
