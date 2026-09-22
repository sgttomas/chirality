# DOC-PRODAGENTS notes (RUN_D128 R2 EXT, item 6, audit-only)

Ledger: `DOC-PRODAGENTS_claims.csv`, 9 rows, validator `RESULT PASS errors=0 warnings=0`. This ledger is audit-only (CONVENTIONS §8): nothing is repaired by this run; residuals route to Root (Δ10).

## 1. Census

STATE_ASSERTION 4 (ALIGNED 4); CONTEXT_CLAIM 5 (NOT_AUDITABLE 5). Split rate 0/9. SEE rows 0. No errata.

## 2. Least-confident rows

- `DOC:PRODAGENTS#1` (MEDIUM, ALIGNED). Alternative: PARTIALLY_IMPLEMENTED, reading 'TASK ... does not delegate' and 'Start a fresh child context' as product guarantees; no LIVE depth limit exists (native-role-config max_depth has no product importer) and fork_context=false is advisory. I read both as instructions to the agent, which is how the text is worded.
- `DOC:PRODAGENTS#3` (MEDIUM, ALIGNED). Alternative: none material; PostReleaseBasis YES rests on the shared thread/start line (codex-supervisor.ts:219).
- NOT_AUDITABLE rows #0, #2, #5, #6, #8: an alternative reading would treat conduct norms as ALIGNED because the file is supplied to every agent; they assert nothing product-observable, so NOT_AUDITABLE follows the adopted CONTEXT_CLAIM rule.

## 3. Register-defect summary

None. Item 6 has no register surface.

## 4. Direction and cause

All rows NONE (no divergence). No `ROUTE:ROOT (Δ10)` residual arises because no row is non-ALIGNED; the guidance is accurate about product behaviour at the frozen basis. LatestDecision uses `D-GOV-43 (context)` / `D-GOV-35 (context)` only as touch points.

## 5. Method friction

- Item 6 is conduct-heavy prose; five of nine units have no product mechanism. The CONTEXT_CLAIM/NOT_AUDITABLE path fits, but a census tag for 'conduct-only' would make item-6 figures easier to read.
- AuthorityTier: the file restates Root `AGENTS.md` (execution-protocol class), not DIRECTIVE/CONTRACT/SPEC/TYPES, so the four STATE_ASSERTION rows use NOT_APPLICABLE.

## 6. Effort

About 10 sources: the guidance file, INSTRUCTIONS capabilities and notes, workflows/index.json, workflow-draft UI files by grep, codex-supervisor blame. Context comfortable.
