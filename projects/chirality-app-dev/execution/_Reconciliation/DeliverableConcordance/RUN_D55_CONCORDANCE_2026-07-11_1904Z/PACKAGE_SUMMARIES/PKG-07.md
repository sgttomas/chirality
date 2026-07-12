# PKG-07 package summary — Filesystem, Execution Lifecycle, and Dependencies

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; derived by the orchestrator
  at W3 fan-in from the claim ledgers (plan §7).
- **Ledgers:** `R2_WAVES/PKG-07/DEL-07-0{1..6}_claims.csv` (125 rows, bound at
  `fac46e33f`). Verification: `R2_WAVES/PKG-07/_VERIFICATION.md` (46 rows
  rechecked; 10 refutations accepted; 1 standing contested row + 1 escalated
  classification question).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## Census (6 deliverables, 125 claim rows)

| Disposition | 07-01 | 07-02 | 07-03 | 07-04 | 07-05 | 07-06 | Total |
|---|---|---|---|---|---|---|---|
| ALIGNED | 14 | 16 | 14 | 20 | 18 | 19 | 101 |
| PARTIALLY_IMPLEMENTED | 1 | 3 | 0 | 3 | 2 | 0 | 9 |
| REMAINING_STATE_MISMATCH | 2 | 1 | 1 | 2 | 1 | 1 | 8 |
| STALE_SPECIFICATION | 1 | 1 | 2 | 1 | 0 | 1 | 6 |
| IMPLEMENTED_DIFFERENTLY | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Package-level picture

1. **The filesystem/lifecycle spine is implemented and current** (101/125
   ALIGNED): working-root validation via the shared `assertProjectRootAccessible`
   validator (ORN-05 parity overtook the INSP-03 validate-route PARTIALs),
   scaffolding with ADQ-06 baseline seeding, the ADQ-07 document-kit scanner,
   the status-transition API/MCP pair, the Dependencies.csv v3.1
   reader/writer/linter (post-assessment maturation closed retire-vs-delete
   and symlink-leaf gaps), and the reference-hash/snapshot conventions with
   both `_Scripts` tools live.
2. **The dominant defect is one root cause, mirrored from earlier waves:**
   the D-APP-35-reconciled REF-006 (docs/PRD.md) hash — live MATCH in all six
   `_REFERENCES.md` files — is still presented as an open HASH_MISMATCH by
   every kit (6 STALE_SPECIFICATION rows) and every dependency register
   (6 of the 8 REMAINING_STATE_MISMATCH rows). One bounded package-wide R5
   doc-repair tranche under the existing D-APP-35 authorization.
3. **Genuine implementation residuals (9 PARTIAL rows):** domain-hook-error
   fixture gap (07-01 REQ-008); scaffold-write containment enforcement +
   TBD-preservation/typed-partial-shape fixtures (07-02 REQ-011/012/013);
   content-change SHA revalidation (07-04 REQ-014, D-APP-53-gated, packet
   awaited) + schema fixture pack (REQ-016) + actor-mapping bar (REQ-017,
   contested); target-ID existence resolution (07-05 REQ-010) and
   unknown-option-key warnings (07-05 REQ-017).
4. **Fan-in materially tightened the wave:** the 8-row DEL-07-03
   STALE_ASSESSMENT class flipped to ALIGNED+OVERTAKEN on the
   superseding-note test (assessments carrying ADQ superseding notes no
   longer present stale conclusions as current truth — run-wide boundary for
   R3 ratification); DEL-07-02's scaffold-preview unmapped row folded under
   DEL-06-03's decomposition assignment; DEL-07-04's gated remaining item
   was recognized as concordant (accurately recorded + correctly gated =
   ALIGNED).
5. **Standing contested row:** DEL-07-04 REQ-017 (PARTIALLY_IMPLEMENTED with
   contest) — whether the requirement-internal "exact enum … remains TBD"
   defers enumeration, against the owner's re-verified fact that actor
   authorization is a `startsWith('HUMAN')` prefix wildcard rather than an
   explicit mapping. R3/R4 input.
6. **Escalated classification question:** DEL-07-05 UNMAPPED-001 (adopted
   ALIGNED under docs/TYPES.md §6.2 line 211) — whether TYPES.md
   descriptive-normative vocabulary wording counts as an "accepted mapping"
   under the corpus-wide test. R3 input.

## Unknowns / conflicts

One explicitly contested row (07-04 REQ-017); zero AUTHORITY_CONFLICT /
UNKNOWN / DEFERRED_AGENT_WORKFLOW rows.
