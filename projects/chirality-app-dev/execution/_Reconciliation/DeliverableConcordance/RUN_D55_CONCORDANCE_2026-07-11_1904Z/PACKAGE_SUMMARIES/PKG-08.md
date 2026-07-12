# PKG-08 package summary — Agent Suite, Pipeline Dispatch, and Subagent Governance

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; derived by the orchestrator
  at W3 fan-in from the claim ledgers (plan §7). Product-runtime portions
  only — agent-workflow surfaces are FROZEN_PROCESS_INPUT (plan §3 boundary
  8); the fan-in verified no row required DEFERRED_AGENT_WORKFLOW routing.
- **Ledgers:** `R2_WAVES/PKG-08/DEL-08-0{1..5}_claims.csv` (98 rows, bound at
  `fac46e33f`). Verification: `R2_WAVES/PKG-08/_VERIFICATION.md` (28 rows
  rechecked; 1 refutation accepted; 2 contests resolved by owner with
  escalated label questions).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## Census (5 deliverables, 98 claim rows)

| Disposition | 08-01 | 08-02 | 08-03 | 08-04 | 08-05 | Total |
|---|---|---|---|---|---|---|
| ALIGNED | 21 | 17 | 16 | 14 | 14 | 82 |
| STALE_SPECIFICATION | 0 | 5 | 1 | 2 | 1 | 9 |
| IMPLEMENTED_UNDOCUMENTED | 0 | 1 | 1 | 0 | 1 | 3 |
| IMPLEMENTED_DIFFERENTLY | 0 | 1 | 1 | 0 | 0 | 2 |
| REMAINING_STATE_MISMATCH | 0 | 0 | 0 | 1 | 1 | 2 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 | 0 | 0 |

## Package-level picture

1. **The governance spine is fully landed and ruled** (82/98 ALIGNED;
   DEL-08-01 is the run's first perfect 21/21 ledger): instruction-root
   packaging + agent conformance validation, persona-alias/agent-matrix
   routing, pipeline dispatch, the D-APP-10 Option C executable subagent
   bridge (`rulingRef` encoded in source), and child-run records/artifacts
   all carry gate-bound implementation + verification evidence with INSP-03
   current or overtaken-stronger.
2. **The dominant defect family is untranscribed corpus wording, not code:**
   DEL-08-02's NEW-PACKET set (REQ-003/004/008/009/014 + ACC-001 — six
   D-APP-38-family corpus-amendment packets) captures pre-pivot
   AGGREGATE/RECONCILING aliases, WORKBENCH matrix destinations (D-APP-28/24
   rule; TYPES §3.4/§4.1/§4.3 + PRD FR-008/FR-026 never transcribed), the
   incomplete alias table vs the accepted DEPENDENCIES→EVALUATION cell, and
   SPEC §13.1's misdescription of the live hardcoded WORKING_ITEMS default.
   DEL-08-04's two STALE_SPECIFICATION rows are pre-implementation "TBD"
   kit voice over a landed bridge — repair-shaped, no ruling needed.
3. **Fan-in adversarial value:** REQ-004 flipped STALE_SPECIFICATION →
   IMPLEMENTED_DIFFERENTLY on the verifier's fact that AGENT_RECONCILIATION
   was never Type-2 (so the cited rulings don't govern that alias removal);
   REQ-014's defect relocated from kit to the live corpus line; DEL-08-01's
   packaged-SDK unmapped row folded under DEL-09-04's decomposition
   assignment (W4 must verify DEL-09-04 claims it); a false "no
   inside-instruction-root route test" absence claim was corrected with the
   evidence strengthened.
4. **Genuine unmapped behaviors (3):** the `isMatrixLaunchBlockedByStreaming`
   UI guard (08-02 — no decomposition assignment found; R3 ownership);
   pipeline-surface scaffold/contracts/lifecycle panels (08-03 — known
   double-count with merged W1 DEL-02-02 rows; R3 de-duplication, candidate
   owners DEL-07-02/07-04); hardcoded child-output thresholds 16 KiB/512 KiB
   (08-05 — values unmapped, NEW-PACKET; behavior maps to REQ-007; cleanly
   distinct from DEL-05-05's resultBudget, resolving the W2 handle).
5. **Cross-package handles verified consistent:** subagent permission-class
   declaration (DEL-06-01) vs consumption (DEL-08-04) — compatible;
   child-output limits (DEL-08-05) vs tool-result budget (DEL-05-05) —
   separated; governance conformance (DEL-08-01) vs implementation
   (DEL-08-04) — compatible.

## Unknowns / conflicts

Zero contested dispositions standing on recorded rows; two owner-resolved
contests carry escalated R3/R4 label questions (REQ-004
IMPLEMENTED_DIFFERENTLY-vs-AUTHORITY_CONFLICT; REQ-014 corpus-vs-kit repair
locus). Zero AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW rows.
