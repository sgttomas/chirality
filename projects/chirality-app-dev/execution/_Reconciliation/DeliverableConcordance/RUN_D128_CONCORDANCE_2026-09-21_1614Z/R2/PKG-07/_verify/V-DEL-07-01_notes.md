# V-DEL-07-01 — verifier notes (DEL-07-01)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 8 | 7 | 0 | 1 |
| a30 | 12 | 10 | 1 | 1 |
| b | 1 | 1 | 0 | 0 |
| c | 5 | 5 | 0 | 0 |
| **Total** | **26** | **23** | **1** | **2** |

Verdict-field refutations (Addendum 3 threshold): 0. The one REFUTED item is field-only (Notes).
Both CONTESTED items are on Disposition.

## (ii) Patterns

1. **Where the line falls between AUTHORITY_CONFLICT and aggregate or other verdicts on
   K-ROOT/K-PATH/K-HOOK restatements.** CLM-011.4 to CLM-011.8 grade AUTHORITY_CONFLICT with
   R4-Q1. That holds: the clauses are unamended (CONTRACT.md:52, 99-101), D-GOV-43 lets the user
   choose danger-full-access without naming them, and DIRECTIVE §0 does not settle it. Two other
   rows state the same obligations but carry different verdicts. CLM-004's conditions table
   restates K-ROOT-2, K-PATH-2 and K-PATH-3, and was graded PARTIALLY_IMPLEMENTED as an aggregate
   without a split. CLM-011.9 (DIRECTIVE 2.9) was graded IMPLEMENTED_DIFFERENTLY and self-flagged
   LOW. Both are CONTESTED. R4-Q1 is cited correctly throughout.
2. **The REF-006 MATCH restatement token.** The tie-break rule 3 SEE token is applied on CLM-001
   (`SEE:DEL-07-01#REGISTER-1`). CLM-006 (E-002) and CLM-013 use prose "cf. REGISTER-1" instead.
   CLM-006 is REFUTED on Notes because its Disposition matches REGISTER-1, so a SEE row was
   possible. CLM-013's Disposition differs, so no SEE token is possible there. DirectionEvidence
   also varies for the same hash drift: CLM-001 and REGISTER-1 cite GOV:D-GOV-43, while CLM-006
   and CLM-014 cite NONE_FOUND. PRD drift also includes pre-v3 commits (git log shows commits
   from 2026-07-22 to 2026-08-01), so D-GOV-43 explains it only in part.

Other checks passed:
- **Code anchors.** All code anchors show the stated content at the frozen tree
  (codex-supervisor 104-110/719-728, delegated 318-326, project-registry 100-121,
  tool-path-policy 113-126/251-252/298-302, chirality-hooks 589-600, session-manager 161-206,
  validate route 9-18, workspace-provider 36-58, instruction-root 18-54, main.ts 408-425).
- **REACH tags.** They agree with REACHABILITY.csv.
- **PostReleaseBasis.** NO is correct: the cited supervisor lines fall outside the
  TOUCHED_PATHS ranges.
- **Reference hashes.** Recomputed to match REFERENCE_HASHES.csv.
- **Class c.** All five responses are sound.
- **CLM-011.8.** Minor: the ALSO_MODULE gloss says "subagent not shown", but the subagent family
  is in the same fail-closed catch. The module verdict still holds because of the domain family.

## (iii) Effort

About 30 file reads or greps across the frozen deliverable folder, App docs, App/Runtime code,
the evidence pack and the capability files, plus 2 read-only `git log` calls on the frozen tree.
The context budget was comfortable.
