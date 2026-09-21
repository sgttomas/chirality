# V-DEL-06-01_RERUN — verifier notes

Unit `DEL-06-01_RERUN` (ledger `DEL-06-01`), graded against `CONVENTIONS.md` and the PKG-06 shared grading key at frozen basis `00115c719`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT) | 7 | 6 | 0 | 1 |
| a30 | 14 | 5 | 8 | 1 |
| b (ALIGNED sample) | 2 | 1 | 0 | 1 |
| c (reverse) | 4 | 4 | 0 | 0 |
| **Total** | **27** | **16** | **8** | **3** |

All 8 REFUTED verdicts are on a single field. None refutes a Disposition.

## (ii) Systematic patterns

1. **The REF-hash DirectionEvidence gloss is wrong (6 rows: CLM-001, 006, 007, 023, 033, REGISTER-1).**
   - The rows say CONTRACT, SPEC and PRD were amended under D-GOV-43 and that "no PKG-06 register refresh followed".
   - At the frozen tree, `_REFERENCES.md` REF-002..006 blame to the D-GOV-43 application tranche `23b3879b3`. The recorded hashes (fa8fc9dc, 01e1c75c, 8649ccba) are exactly the three documents at that commit.
   - The drift comes from later commits on 2026-09-12: `9eaddb596` (#778) changed PRD and SPEC, and `95b342519` and `7f1e9f387` changed CONTRACT.
   - The Disposition, CauseTag `DOC_HYGIENE` and hash evidence all hold.
   - REGISTER-1's Disposition is also contestable under grading key 5: STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH (register lag).
2. **PostReleaseBasis misses a touched line (CLM-003, CLM-009.2).**
   - Both rows cite the range `codex-supervisor.ts:694-717`.
   - Line 695 in that range blames to `da95ec194` and is listed in `TOUCHED_PATHS.csv`, so the rule gives YES.
   - The relied-on approval logic is at 696-717 and is pre-release. Narrowing the citation would restore NO.
3. **The AUTHORITY_CONFLICT cluster holds (CLM-004, 009.5, 009.6, 009.8, 009.9, 027, 031).**
   - D-GOV-43 item 4 (proposed.md:187-195) does not name K-PERM-4..6, TYPES 8.1 or SPEC 15.1/15.2. All of these are unamended at the frozen basis.
   - Only CLM-009.9's plain `R4` is contested. Its siblings carry `R4; R4-Q1`, and its Notes turn on the retained SDK env-var gate.
4. **Module-level ALIGNED on LEGACY_ONLY code.**
   - VER-002 (CLM-034.3) is confirmed, because it concerns the overlay constant and branch themselves.
   - VER-001 (CLM-022.2) is contested: it verifies the mode behaviour, and the row itself flags R4-Q1.
   - CLM-009.4 is contested: IMPLEMENTED_DIFFERENTLY vs ALIGNED, because K-PERM-3 accepts "mode policy" and the live path restricts by mode.

I checked every cited code anchor I relied on, and each shows the stated content at the frozen tree with no material drift. REACH tags match `REACHABILITY.csv`. Every cited test case name exists.

## (iii) Effort

- **Read:** about 25 targeted reads/greps. These covered the rulebook, the ledger rows, the D-GOV-43 ruling and proposal item 4, and App CONTRACT/TYPES §8.1, §13. They also covered the SoW, `_REFERENCES.md`, the decomposition rows, 8 code files and 4 test files.
- **Git:** read-only `git log`/`show`/`blame -L` on `codex-supervisor.ts`, `_REFERENCES.md` and the docs history.
- **Context budget:** adequate.
