# Review 01 of PR #919 (work graph), transcribed

- **Reviewer:** fresh read-only `pec-reviewer` (TASK, `claude-opus-5-5`, high), dispatched by HELP_HUMAN. It cannot write, so HELP_HUMAN transcribed its final report verbatim from the host subagent transcript.
- **Reviewed head:** `5570fd0953f69dd8c23e0e7ae43501a31cad8947`.
- **SHA-256 of the report text below (UTF-8):** `c3633eb7a02355df6796f51912bb7fa2be11bd9446f30572bbf6b5eea175f725`.

## Report (verbatim)

**Verdict: FAIL.** There is one blocking finding: the SOW sequencing does not follow D-PEC-90. The rest of the PR is correct.

**Reviewed:** head `5570fd0953f69dd8c23e0e7ae43501a31cad8947` (matches `gh pr view 919`), base `13df8b795e47ab2284018eeefc9d5473d00c232d`. I extracted the head with `git archive`, and made a `--shared` clone of it in scratch for the validators. Host-reported model: Opus 5.5 (`claude-opus-5-5`).

## Blocking

**B1. The SOW batches do not follow the reliance ordering the graph itself states.**
- **Location:** `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` L14 (approach), L52 (S1), L55 (S4), L67–69 (Order).
- **The graph's own rule (L14):** SOW currency waits for the reliance amendment "for the deliverables that quote PEC-K-03 or §8".
- **D-PEC-90 grant item 1** (`_DECISIONS/D-PEC-90_RULING_2026-09-25.md`) says "DEL-04-01 and the §8 refresh are not to be rebuilt around verify-before-rely".
- **DEL-08-01 breaks the rule.** Its `ScopeOfWork.md` L92 (CLM-004) quotes the PRD §8 access classes and "Under `PEC-K-03` … subject to verify-before-rely". R1 amends exactly that text (it adds a direct-query access row). Yet DEL-08-01 is in S1, which is ready after P1 and not gated on R3.
- **DEL-08-03 is in the same position.** Its SOW L256 (REQ-005) also quotes PEC-K-03, and it sits in S1.
- **DEL-04-02 has no node at all.** Its currency class is "current", but its SOW L225 (CLM-016) quotes PEC-K-03 with verify-before-rely, so it will go stale at R3.
- **DEL-01-06 is mislabelled.** It is listed as "K-03-bound" but its SOW quotes neither K-03 nor §8. Its real gate is G1/B6.
- **Fix:** gate S4 on the affected-SOW set that R1/R2 identifies, or at minimum move DEL-08-01 and DEL-08-03 there and add DEL-04-02. Relabel DEL-01-06 as waiting on G1.

## Non-blocking

1. **T1 has no human act (L59, L66).** It is marked "ready now", and its completion check is "Row `RESOLVED_BY_DECISION` via task-management" with no human disposition named.
   - `workflows/task-management/WORKFLOW.md` L47: "Record only the human's actual promotions and dispositions". WORKING_ITEMS owns register writes.
   - `docs/STATUS.md` (~L217) lists "TM-PEC-023 disposition" under current owner gates.
   - Fix: cite the owner basis (for example the D-PEC-92 acceptance of Propagation_Plan §B8) or name the owner disposition in the completion check.
2. **Some fenced nodes name no packet (L23 vs rows).** L23 says the owner rulings "are listed per node", but three nodes that write fenced paths name no D-PEC packet:
   - S4 (L55) writes ScopeOfWork.md and lists no packet.
   - D1 (L57) says "Owning workflows plus exact-byte gates" for the DEL-00-01 ADRs and DEL-00-03 SPEC, which are outside the default write surfaces.
   - X1 (L58) writes fixtures; Propagation_Plan §B7 says these are authored under a v2 packet.
3. **The steering quote is not exactly verbatim (L8).** It is labelled "recorded verbatim" but collapses the owner's double spaces and ends after the second sentence without marking the omission. The verbatim source is D-PEC-94 L7.
4. **Some template and workflow fields are missing.**
   - There is no "Route through the project DAG" field and no "Active operations and ownership" line.
   - Per-node owners are absent except S1 (WORKING_ITEMS); workflow §3 asks for a "write boundary and owner" on each node.
5. **The R4 Runtime notice (L51) has no cited basis.** D-PEC-90 grants notices only to Root and App; the graph should cite the scope-change route that would authorize a Runtime notice.
6. **The ID "P1" is used for two things.** It names the currency-PR node and also PEC's P1 parser phase (L9, L18, L58), so "ready after P1" (L52, L67) reads ambiguously.
7. **A STATUS heading is stale, outside this diff.** `docs/STATUS.md` L139 still reads "**Active scope change — SCA-005:**" although SCA-005 is closed.

## Verified

- **Graph structure:**
  - The run ID is stable across the graph path, receipt path and PRs.
  - Intent, steering and *Interpretation* are kept distinct.
  - Nodes carry scope, needs, checks and states.
  - The dependencies are acyclic.
  - There is one C1/M1/F1 closeout. M1's MEMORY rows depend on packet grants, as `projects/pec/AGENTS.md` requires.
  - `projects/pec/loop/` is unchanged by the diff.
- **Counts match the live tree and the audit:**
  - 42 `_CONTEXT.md` and 64 `_REFERENCES.md` lack revision 1.5 (24 and 2 have it). This matches COV-068/069. The plan's "40" was corrected to 42 by audit D-13.
  - My own recount found 19 non-verbatim ACTIVE EXECUTION evidence quotes in 10 registers. The IDs are identical to COV-072.
  - The 23 SOWs (8 rebuild, 15 review) plus 5 housekeeping-only match Propagation_Plan §B4, and the partition into S1–S4 sums to 28.
- **D-PEC-94 edit:** it only adds lines (6 appended, none deleted). The quote matches the owner's words exactly, the register row changes only by an added parenthetical, and it is truthful.
- **Cited manifest hash:** `PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml` recomputes to `0ccddebe…b783` with `shasum -a 256`, as D-PEC-94 states.
- **Old run record:** the G22 and W1 closing notes are accurate. `13df8b795` is the PR #917 merge, and `returns/F19_REVIEW_LOOP_MIGRATION.md` exists.
- **STATUS pointer:** correct. README needed no change, and the D-PEC-88 trace (graph L86–90) is accurate.
- **Hygiene:**
  - `git diff --check` is clean.
  - `validate_pec_loop_receipts.py --repo-root .` reports VALID with exit 0; the ledger is unchanged.
  - `validate_decomposition_registers.py --strict projects/pec/execution` reports 0 errors and 0 warnings.
  - The harness self-check exits 0.
- **Work graph hash** (SHA-256): `f78484a79a923b09d5acb9ee964ebf07acaa5d8234f9de36e1738593fc60c329`

Files:
- `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-project-assessment-6106d5/projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` (on the branch)
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md`
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md`
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md`

## HELP_HUMAN disposition

| Finding | Disposition |
|---|---|
| B1 SOW sequencing | Repaired. S4 is now the set that SCA-006 checkpoint 2 fixes, with candidates DEL-04-01, DEL-04-02, DEL-08-01 and DEL-08-03 (K-03), and the §8 citers. S1 and S2 exclude the R1 affected list. DEL-01-06 moved to S2 after G1. The SCA-006 manager was told to enumerate the affected SOWs explicitly. |
| NB1 T1 human act | Repaired. T1 cites the checkpoint-2 acceptance of §B8 as its candidate owner basis, and is UNCERTAIN until `D-PEC-95` settles whether a direct owner disposition is needed. |
| NB2 packets not named | Repaired. S4, D1 and X1 name their packet basis, and a table preamble defines "packet". |
| NB3 quote | Repaired. The full direction is quoted with its original spacing, from `D-PEC-94` L7. |
| NB4 template fields | Repaired: added Route through the project DAG, Active operations and ownership, per-node owners and the completed-work table. |
| NB5 R4 Runtime | Repaired. Root and App per `D-PEC-90`; Runtime only if checkpoint 2 names it. |
| NB6 "P1" ambiguity | Repaired. The currency-PR node is renamed U1, and a naming note is added. |
| NB7 STATUS heading | Repaired under `D-PEC-88`; traced in the graph. |
