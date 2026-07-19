# Sealed Verifier Brief — T3 Adversarial Governed-Diff Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Posture:** fresh context; no shared authorship; read-only except the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`; default `BLOCK` if uncertain.
- **Write scope:** exactly `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_T3_GOVERNED_DIFF_1.md`.

## Scope under test

The staged diff (`git diff --cached`) against HEAD = commit `770e2a1fc` (T2 commit). This brief file is the declared untracked addition besides your return.

## Claims to refute

1. **Whole-diff claim.** The staged diff touches only: (a) DEL-01-01 dir — seven new artifacts (`Notes_Governance_Consistency_DEL-01-01.md`, `Checklist_Human_Authority_DEL-01-01.md`, `Checklist_Project_Truth_DEL-01-01.md`, `Checklist_Runtime_Audit_DEL-01-01.md`, `Checklist_Document_Diff_DEL-01-01.md`, `Checklist_Acceptance_DEL-01-01.md`, `Table_Conflict_Source_Warnings_DEL-01-01.md`), `ScopeOfWork.md`, `_STATUS.md`, new `_run_records/TASK_RUN_2026-07-18_DAPP65_docs_production.md`; (b) DEL-03-03 dir — `RouteAdapterTestIndex.md`, `SSE_Compatibility_Fixture_README.md`, `_STATUS.md`, new `_run_records/TASK_RUN_2026-07-18_DAPP65_docs_production.md`; (c) run-directory files (two launch briefs, two returns). Nothing else; no `docs/**` or `frontend/**` file changed.
2. **Status-surface rules.** DEL-01-01 `_STATUS.md`: exactly the R4-P48 seven-artifact Remaining item removed + one dated History line; every other Remaining item byte-intact; no Current State/lifecycle/`Last Updated`/`Checking Approval SHA` change. DEL-03-03 `_STATUS.md`: exactly the R4-P48 two-artifact item removed + one History line; the CQ-F1 route-affinity item byte-intact.
3. **ScopeOfWork discipline.** DEL-01-01 `ScopeOfWork.md` diff is confined to the R004 residual-row cell append (prior cell text preserved as prefix); no other line changed.
4. **Artifact honesty (spot-check).** The artifacts record real checks, not templates: (a) pick 5 cited verdicts across different artifacts and confirm each citation resolves (file exists; cited content supports the verdict); (b) confirm `Table_Conflict_Source_Warnings_DEL-01-01.md` carries the REF-006 `docs/PRD.md` matter as OPEN/unresolved for human ruling (any fresh hash evidence may be recorded but no resolution/acceptance rendered); (c) in `RouteAdapterTestIndex.md`, pick 3 indexed test references and confirm the named `it`/`describe` blocks exist in the cited files; (d) confirm the SSE README's claim that no captured fixture files exist is true (search the repo for such fixtures under the frontend tests) and that its event list matches the REQ-003 names in DEL-03-03 `ScopeOfWork.md`.
5. **Authority honesty.** Every artifact header and both run records attribute production to D-APP-65 disposition 4 and state that verdicts/content are agent findings with no acceptance, approval, certification, or issuance rendered; the two D-APP-64 attribution blocks (R004 naming; DEL-03-03 naming) follow the schema with `OwnerCaseSelection: NONE`.
6. **Hygiene.** No staged file contains credential material or unmarked `sk-ant-` continuations; repo-wide `python3 tools/practitioner_harness/harness.py self-check` exits 0 at the pinned baseline (INFO=15, NOT_APPLICABLE=2, REVIEW=33, WARN=6) — pay attention to GEN8 (no new absolute-path findings from these artifacts).

## Return format

`RETURN_T3_GOVERNED_DIFF_1.md`: verdict line first, then per-claim findings with evidence commands and observed values.
