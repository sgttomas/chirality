# Handoff State - RCH_20260618T040502Z_gap_pkg06

Status: DERIVATIVE_RESEARCH_PACKET (immutable run snapshot)
MODE: ORCHESTRATED

## Accepted Upstream Snapshot(s)
- Live execution tree + git HEAD of projects/chirality-app-dev (working root); repo root /Users/ryan/ai-env/projects/chirality (git rev-parse confirmed).
- Deliverable docs: projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-0[1-6]/.

## Retrieval Snapshot(s)
- domains/chirality-app-dev/_LocalIndexes/_LATEST.md -> SRCIDX_20260616T043733Z (build 2026-06-16T04:37:34Z).

## Derivative-Package Status
- Immutable research packet; recommends only, approves nothing. No accepted truth modified.

## Caveats
- Freshness verdict STALE (CONTENT_DRIFT; 49 changed / 660 recorded). Retrieval used for DISCOVERY only; live source/tests are authority. Index NOT rebuilt (per protocol).
- Numeric Bash timeouts (default 120000ms / max 600000ms) are chosen in code (tool-shell-policy.ts); spec leaves them TBD pending accepted policy.

## Conflict Status
- 0 conflicts (Conflicts.csv empty).

## Coverage Gaps
- Section 9 validation runner (section9.chirality_mcp_status_dependencies, section9.context_compaction_boundary) not located in live tree; behavioral coverage exists via vitest instead.
- "Denied Bash never spawns" verified at policy layer (deny precedes SDK execution), not via an instrumented process runner.
- Did not exhaustively read every Datasheet/Guidance/Procedure for all 6 deliverables; Specification + _STATUS + key Dependencies + live source/tests covered.

## Pointer Status
- _Research/_LATEST.md updated to this packet by scaffolder.

## Recommended Downstream Action
- Route AM-01 (per-deliverable Evidence consolidation) and AM-03 (docs/PRD.md REF-006 HASH_MISMATCH reconciliation) to SCOPE_CHANGE/owner.
- Human-gated CHECKING -> ISSUED transitions remain with the human.

## Tests Executed (:RUN)
- vitest run (frontend): permission-overlay (11), tool-descriptor (10), tool-catalog (2), chirality-read-mcp (5), chirality-hooks (5) = 33 passed.
- vitest run (frontend): chirality-mutating-mcp (5), sdk-message-mapper (11), session-events (3), tool-evidence (4), tool-result-artifacts (3) = 26 passed.
- Total 59 PKG-06-relevant tests green.
