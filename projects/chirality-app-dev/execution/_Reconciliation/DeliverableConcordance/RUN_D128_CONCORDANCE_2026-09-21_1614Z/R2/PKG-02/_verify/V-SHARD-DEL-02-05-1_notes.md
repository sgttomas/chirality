# V-SHARD-DEL-02-05-1: verifier notes (R2 PKG-02, DEL-02-05)

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 21 | 16 | 0 | 5 |
| a30 | 13 | 11 | 1 | 1 |
| b | 2 | 2 | 0 | 0 |
| c | 10 | 10 | 0 | 0 |
| **Total** | **46** | **39** | **1** | **6** |

- **Disposition-level REFUTED:** none.
- **Disposition-level CONTESTED (6):** SEC-2.2, SEC-2.3, CLM-003.2, CLM-005.5, CLM-010.7, CLM-011.3.
- **Field-level REFUTED (1):** CLM-016, on DirectionEvidence.
- **Reverse Response refutations:** none.
- **Errata:** no errata file exists, so there are no class e items.

## (ii) Patterns

1. **The Anthropic API-key UI AUTHORITY_CONFLICT rows stand (10 rows CONFIRMED).**
   - **Rows:** CLM-003.1, CLM-004.2, CLM-005.1, CLM-005.2, CLM-009, CLM-010.1 to CLM-010.4, and CLM-011.2.
   - **Authority reading applied:**
     - DIRECTIVE §0 ranks App DIRECTIVE §2.8 and §4.1 above CONTRACT, SPEC and PRD. Those sections are unamended: the Anthropic key-aware default, and "current Anthropic provider access" in scope.
     - Applied to documents alone, §0 therefore favours the Anthropic text. It does not favour the Codex-only preambles, which rank lower.
     - D-GOV-43 and Root DIRECTIVE §7, as amended under D-GOV-43, are what undercut §2.8 ("Codex is the sole engine"), and neither names it. The sole-engine rule itself dates from the 2026-09-10 owner direction (tranche ROOT-CODEX-MVP-20260910). That direction amended App PRD, CONTRACT and SPEC, but not the App DIRECTIVE.
     - D-APP-127 names DEL-02-05, but only for the Codex custody and architecture clauses. Its boundary expressly leaves the sole-engine rule unchanged. The DEL-02-05 text applied under it keeps the key-UI storage states "where it is still used".
     - So MR-11 does not reach the key UI, and CONVENTIONS §1 bullet 3 applies. STALE_SPECIFICATION would need either a ruling that explicitly retires the Anthropic key UI or a DIRECTIVE amendment. Neither exists at `00115c719`.
   - **Checks on the worker's reasoning:** the worker applied §0 explicitly rather than assuming the preambles win. HumanDecisionNeeded `R4` is correct, because no named question covers this. The SYMBOL-UNREACHED notes are verified: the key panel renders only when the hosted controller is null (settings-view.tsx:35), and the hosted controller is never null on the woven path.
2. **The SSE-name rows citing R4-Q5 are CONTESTED (CLM-003.2, 005.5, 010.7, 011.3).**
   - Graded against Addendum 7. The row's own sources (SPEC §11, TYPES §7.4 and K-EVENT-1, all amended) name `turn:error` and `process:exit` and expressly supersede the eight-name set.
   - The unamended side of R4-Q5 (K-ENGINE-4, SPEC §10.3) requires translation into Chirality-owned contracts but names no event set.
   - **Reading A (worker):** AUTHORITY_CONFLICT. A "translated" answer would reopen the amended clause.
   - **Reading B:** STALE_SPECIFICATION, with R4-Q5 as context.
   - The live code still emits and consumes both names.
   - Two dependent rows are CONFIRMED because the SSE question does not decide them:
     - CLM-009, whose Disposition is held by its key-UI part;
     - CLM-023, whose Disposition is STALE_SPECIFICATION on the REF-006 bullet.
3. **Rows mixing a ruling-superseded clause with a conflict are CONTESTED (SEC-2.2, SEC-2.3).**
   - D-APP-127 names DEL-02-05, its V3-03 gate, the account row and the Settings host. That makes MR-11 ("the clause or the deliverable") a plausible trigger:
     - for Q7's local-model dot, whose truthfulness statements D-APP-127 supersedes by way of D-APP-122;
     - for the per-folder group and fake-port wording.
   - The worker's AUTHORITY_CONFLICT (SEC-2.2) and IMPLEMENTED_DIFFERENTLY (SEC-2.3) are the other readings.
   - CONVENTIONS gives no precedence rule for a row that mixes these parts.
4. **Minor points, not refuted:**
   - **CLM-016:** a GOV: prefix is paired with a LatestDecision marked (context) for the same ID. The refutation is recorded on the DirectionEvidence field.
   - **Line drift ≤ 6:** account-row.tsx:68 → 67; api-key-storage.ts:50/75 → 30/79.
   - **PostReleaseBasis:** app-owned-composition.ts:225 blames to `95364569a`, not a post-release commit, so `NO` holds.
   - **REACH tags:** all tags cited match REACHABILITY.csv.

## (iii) Effort

- **Read:**
  - about 20 files and line ranges: CONVENTIONS, RUN_BASIS, the App and Root DIRECTIVE, the preambles of PRD, CONTRACT, SPEC and TYPES, D-APP-127, D-GOV-43, D-APP-108 Q7 and D-APP-122;
  - the DEL-02-05 SoW, `_REFERENCES.md` and Dependencies.csv;
  - about 10 code files.
- **Git:** one read-only blame and one read-only show.
- **Not read:** runtime execution, R0 ledgers and other units.
- **Context:** the budget was adequate.
