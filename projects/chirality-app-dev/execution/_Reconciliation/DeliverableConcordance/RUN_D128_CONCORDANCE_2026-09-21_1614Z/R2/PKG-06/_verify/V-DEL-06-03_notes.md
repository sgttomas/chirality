# V-DEL-06-03 verifier notes (DEL-06-03)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT / REMAINING_WORK) | 13 | 11 | 0 | 2 |
| a30 (30% of other non-ALIGNED) | 13 | 9 | 0 | 4 |
| b (ALIGNED sample) | 1 | 1 | 0 | 0 |
| c (reverse) | 3 | 3 | 0 | 0 |
| **Total** | **30** | **24** | **0** | **6** |

Class e: none (the unit has no errata file).

## (ii) Systematic patterns

1. **The AUTHORITY_CONFLICT premise holds.** Examples: SEC-1, CLM-005, CLM-010.5, CLM-010.6 and CLM-010.8.
   - **The unamended clauses.** Each row turns on a clause that is unamended at the frozen tree and names the SDK or in-process mechanism:
     - PRD FR-119, `docs/PRD.md:770`;
     - K-MCP-1, K-TOOL-1 and K-PERM-3, `docs/CONTRACT.md:92-98`;
     - FR-081.
   - **The amended clause.** K-RUNTIME-1 (`CONTRACT.md:224`) was re-expressed under D-GOV-43: the Runtime service owns tools.
   - **Why DIRECTIVE §0 does not resolve it.** Both sides sit at the same CONTRACT tier.
   - **No MR-11.** Neither D-APP-127 nor the D-GOV-43 record names DEL-06-03, FR-119 or the K-MCP/K-PERM/K-TOOL clauses.
   - **Consequence.** AUTHORITY_CONFLICT with R4-Q1 is correct.
   - **Where it is contestable.** It is contestable only where the clause is mechanism-neutral. At CLM-010.9 (K-PERM-4 / FR-091), the §2.3 reach rule gives DOCUMENTED_UNIMPLEMENTED, as the worker itself applied at CLM-010.3, .10 and .14.
2. **Module-level reach versus symbol-level reach decides some Dispositions** (grading key 3). The rows affected are CLM-003, CLM-010.1 and CLM-010.4, all PARTIALLY_IMPLEMENTED.
   - **What the pack says.** It marks `runtime-contracts` `tool-names.ts` and `tool-descriptor.ts` LIVE. The chain runs through the contracts barrel from `daemon/src/standalone-bin.ts`.
   - **What the capability files say.** CAP-RTCONTRACT-042 and CAP-RTCONTRACT-044 record both files as LEGACY_ONLY, because only legacy consumers use them.
   - **Consequence.** Under the symbol-level reading, the three rows become DOCUMENTED_UNIMPLEMENTED. The worker's reverse_notes §1 already flags this.
3. **Minor contests on dated or carrier text.**
   - **STATE-2.** It is a dated D-APP-80 concordance note, carried as `SEE:SEC-1`. A SEE row is meant for a normative statement that recurs; this is a state assertion. STALE_SPECIFICATION is the alternative reading.
   - **STATE-1.** R4-Q1 is arguable, but the text is flatly false under D-GOV-43, so `NO` is also defensible.
4. **Mechanical checks all hold.**
   - **Line anchors.** Every anchor is exact, except `filesystem.ts:309`, which drifts by 1 line (immaterial).
   - **Test names.** Every cited test case name exists.
   - **INSP-03 citations.** Every one checks out; `frontend/src/lib/harness/tool-descriptor.ts` and `mcp/tool-names.ts` are absent at the frozen tree, as the rows say.
   - **PostReleaseBasis.** NO is correct: no cited path appears in TOUCHED_PATHS.csv.
   - **REM-1.** The gate is verbatim, and MechanicallyUnblocked NO is correct, because DEP-06-03-015 is an ACTIVE PREREQUISITE and PENDING.

## (iii) Effort

- **Files read.** About 25 files: the rulebook, the run basis, the ledger rows, the reverse notes, the evidence pack (reach, touched paths, decisions, hashes), and the capability rows. At the frozen tree: SoW, `_STATUS`, `Dependencies.csv`, `_CONTEXT`, INSP-03, CONTRACT, PRD, SPEC §14–15, DIRECTIVE §0, the D-APP-127 and D-GOV-43 records, and the code and test anchors.
- **Git.** No git beyond checking file presence was needed.
- **Budget.** The context budget was comfortable.
