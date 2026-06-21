# Evidence: ADQ-12 Agent/Subagent Residuals

## Header

| Field | Value |
|---|---|
| Queue item | ADQ-12 |
| Package | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance |
| Date | 2026-06-21 |
| Persona | WORKING_ITEMS |
| Scope | Conformance fixtures, persona spec reconciliation, Pipeline coverage, and child-output artifact alignment |

## Summary

ADQ-12 closes the inspected PKG-08 residuals without changing lifecycle state or provider posture.

- Added machine-checkable agent instruction conformance validation for `AGENT_*.md` naming, doc marker/title, `AGENT_TYPE`, Agent Type table rows, valid class/write-scope vocabulary, required marker pairs, and allowed frontmatter keys.
- Made the long-term persona contract explicit: do not preserve `AGGREGATE -> AGGREGATION` or `RECONCILING -> RECONCILIATION`; keep Type 2 agents out of top-level persona routing; default empty persona input to `WORKING_ITEMS`; defer unknown non-empty personas to instruction-file lookup.
- Added Pipeline render coverage for category controls, disabled variants, valid TASK knowledge-type deep links, and stale knowledge-target reset during initial render.
- Added route regression proving Pipeline TASK selector state is ignored as unknown runtime options and cannot bypass Type 2 governance.
- Persisted over-inline child summaries as child-output artifacts with relative paths, parent turn, task, child-run, tool-use, source-output, byte-count, checksum, truncation, and redaction metadata.
- Added source-completeness checklist rows to the instruction-root integrity summary for SOW-073/OI-004 and KG-001 candidate source assets.
- Updated DEL-08-01 through DEL-08-05 assessments, dependency summaries, memory notes, semantic-lensing notes, and source-state records to remove stale REF-006 warning blockers and residual claims.

## Implementation Evidence

| Area | Evidence |
|---|---|
| Agent conformance | `frontend/src/lib/harness/agent-instruction.ts`; `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts` |
| Source completeness checklist | `frontend/scripts/verify-instruction-root-integrity.mjs`; `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts` |
| Pipeline surface | `frontend/src/components/pipeline/pipeline-surface.tsx`; `frontend/src/__tests__/components/pipeline-surface.test.ts` |
| Pipeline/TASK governance boundary | `frontend/src/__tests__/api/harness/routes.test.ts` |
| Child-output artifacts | `frontend/src/lib/harness/tool-result-artifacts.ts`; `frontend/src/lib/harness/sdk-message-mapper.ts`; `frontend/src/lib/harness/claude-agent-sdk-manager.ts`; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts`; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` |
| Deliverable records | DEL-08-01 through DEL-08-05 assessment, dependency, memory, and semantic-lensing updates under `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/` |

## Validation

| Check | Result |
|---|---|
| Focused ADQ-12 suite | PASS: 14 files / 116 tests |
| `npm run typecheck` | PASS |
| `npm run test -- --testTimeout=30000` | RETRIED: one existing route taxonomy test timed out under whole-suite concurrency at 30s |
| Isolated route rerun | PASS: `src/__tests__/api/harness/routes.test.ts`, 36 tests |
| `npm run test -- --testTimeout=60000` | PASS: 79 files / 551 tests |
| `npm run harness:validate:section9` | PASS: 14 checks |
| `npm run desktop:pack` | PASS: includes `next build`, Electron package directory build with publish disabled, and instruction-root integrity |
| `npm run instruction-root:integrity` after package refresh | PASS: 47 checked files; `sourceCompleteness.status=needs_remediation` surfaces KG-001 candidate remediation state |
| `npm run harness:validate:premerge` | RETRIED: initial no-server run failed reachability; rerun with local Next dev server passed 8 Section 8 checks and 14 report-only Section 9 checks |
| D-APP-38 authority-corpus status | PASS: corpus `v2`, no drift |
| `git diff --check -- projects/chirality-app-dev` | PASS |

## Notes

The initial instruction-root integrity failure was against a stale generated local app bundle (`docs/SPEC.md` and `docs/TYPES.md` mismatched). `npm run desktop:pack` regenerated ignored package artifacts and reran integrity successfully. Generated `frontend/dist/` and `frontend/artifacts/` outputs remain ignored evidence artifacts and are not committed.

The new source-completeness checklist intentionally reports KG-001 candidate remediation state separately from the SPEC-backed source-to-bundle integrity status. It makes candidate gaps visible without changing the current app-dev staging scope.
