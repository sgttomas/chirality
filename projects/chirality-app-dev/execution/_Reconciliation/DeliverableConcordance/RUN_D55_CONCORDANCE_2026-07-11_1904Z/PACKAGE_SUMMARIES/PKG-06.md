# PKG-06 package summary — Permissioned Tools, MCP, and Hooks

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; derived by the orchestrator
  at W2 fan-in from the claim ledgers (plan §7).
- **Ledgers:** `R2_WAVES/PKG-06/DEL-06-0{1..6}_claims.csv` (131 rows, bound at
  `fac46e33f`). Verification: `R2_WAVES/PKG-06/_VERIFICATION.md` (34 rows
  rechecked + directed ALIGNED sample; 4 refutations accepted; 1 standing
  contested row).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## Census (6 deliverables, 131 claim rows)

| Disposition | 06-01 | 06-02 | 06-03 | 06-04 | 06-05 | 06-06 | Total |
|---|---|---|---|---|---|---|---|
| ALIGNED | 19 | 19 | 20 | 21 | 15 | 19 | 113 |
| STALE_SPECIFICATION | 1 | 1 | 1 | 1 | 3 | 2 | 9 |
| IMPLEMENTED_UNDOCUMENTED | 1 | 0 | 0 | 0 | 1 | 1 | 3 |
| REMAINING_STATE_MISMATCH | 1 | 1 | 1 | 0 | 1 | 0 | 4 |
| ACCEPTED_DIVERGENCE | 0 | 1 | 1 | 0 | 0 | 0 | 2 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Package-level picture

1. **The permission spine is the corpus's strongest package** (113/131
   ALIGNED): overlay mode-mapping, read-tool surface + validation, MCP read
   tools, write/path hooks with mutating-tool SDK-parity gating, bash
   governance, and hook lifecycle/compaction mirror are all implemented,
   tested, and INSP-03-current at the source state. The fan-in's directed
   sample verified 40+ D-APP-48 re-anchored citations — the relocation to
   `@chirality/harness-contract` is behaviorally neutral evidence-pointer
   drift.
2. **The dominant defect is one root cause:** ~80 stale REF-006
   HASH_MISMATCH assertions across all six kits (D-APP-38/ADQ-11 resolution
   never transcribed) plus D-APP-42/43-overtaken TBD wording (06-05 REQ-009/
   REQ-016; 06-06 REQ-015's five TBD path placeholders) — a single
   package-wide R5 doc-repair tranche.
3. **Genuine unmapped behaviors (3):** the `subagent` permission class /
   conditional Agent exposure under the D-APP-10 bridge (06-01 UNMAPPED-1;
   PKG-08 W3 adjacency); the unsourced Bash timeout numerics (06-05
   UNMAPPED-1 — Guidance conflict DEL-06-05-TIMEOUT-001 explicitly awaits a
   human ruling; NEW-PACKET); the untested, kit-unnamed `hook.progress`
   event (06-06 UNMAPPED-1).
4. **Fan-in tightened the register-defect set from 7 to 4:** the Declared-TBD
   class rows (06-02, 06-06) were refuted on SPEC §5.2 and dropped —
   originating the cross-package class conflict R3 must harmonize
   (`_VERIFICATION.md` §3.1) — and the "corpus v2" provenance labels were
   ruled non-defects (06-01 row dropped; 06-05 row narrowed to the one
   present-tense false cell).
5. **Standing contested row:** DEL-06-02 REGISTER-2 (single-row satisfaction
   advance vs equally-MATCH TBD siblings) — explicitly contested,
   NEW-PACKET, deciding fact named. R3/R4 input.
6. Ruled bounded postures: domain read tools + roster on the read surface
   under D-APP-50/51/52 (06-02 UNMAPPED-1, 06-03 EXC-005 — both
   ACCEPTED_DIVERGENCE with gate-acknowledging kit text).

## Unknowns / conflicts

One explicitly contested register row; zero AUTHORITY_CONFLICT / UNKNOWN /
DEFERRED_AGENT_WORKFLOW rows.
