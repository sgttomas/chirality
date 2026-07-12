# PKG-01 package summary — Product Governance and Reliance Boundaries (R2 Wave 5)

Run: RUN_D55_CONCORDANCE_2026-07-11_1904Z · Source state: frontend/ @ fac46e33f (byte-identical to 242900ae9 = main)
Deliverables: DEL-01-01 (Governance Alignment / Human Authority), DEL-01-02 (Reliance Boundary Register), DEL-01-03 (Product Identity / Professional Boundary Copy), DEL-01-04 (Scope Boundary / Retired Scope Register).
Fan-in record: `R2_WAVES/PKG-01/_VERIFICATION.md` (40 rechecked, 37 confirmed, 2 refuted-and-accepted, 1 owner-resolved contest; standing contests: 0).

## Census

| Disposition | DEL-01-01 | DEL-01-02 | DEL-01-03 | DEL-01-04 | PKG-01 |
|---|---|---|---|---|---|
| ALIGNED | 9 | 15 | 15 | 15 | **54** |
| STALE_SPECIFICATION | 2 | 6 | 3 | 4 | **15** |
| STALE_ASSESSMENT | 2 | 9 | 1 | 0 | **12** |
| PARTIALLY_IMPLEMENTED | 0 | 2 | 1 | 0 | **3** |
| REMAINING_STATE_MISMATCH | 1 | 1 | 1 | 0 | **3** |
| DOCUMENTED_UNIMPLEMENTED | 1 | 0 | 0 | 1 | **2** |
| **Total** | **15** | **33** | **21** | **20** | **89** |

## Package picture

1. **Enforcement truth holds.** This package's special duty — distinguishing "the register says X" from "the product enforces X" — found no case of a register asserting an enforcement the implementation lacks, and no OUT boundary crossed live without a ruling. Identity/boundary copy is live and Chirality-owned (zero "Claude Code" strings; boundary copy in `persona-manager.ts`, `domain-proposal-tools.ts`, human-gate surfaces), the 13-row reliance register's NO/NO discipline is test-guarded, and domain tools remain the ruled propose/validate/read loopback surface with no apply path. The one enforcement-adjacent defect runs the other direction: the register cites four enforcement-surface paths that moved to `frontend/packages/harness-contract/src/` under D-APP-48 (RBR-001, PARTIALLY_IMPLEMENTED), and `reliance-boundary-register.test.ts` asserts schema, not path existence (RBR-025).
2. **The dominant defect family is documentation lag behind ruled reality, not implementation gaps.** 27 of 35 defect rows are STALE_SPECIFICATION/STALE_ASSESSMENT, in three run-wide classes: the corpus v1→v6 label pin (four-way consistent after fan-in; substantive hash MATCH true everywhere by live recompute), the CHECKING-vs-IN_PROGRESS lifecycle wording under D-APP-54 (four-way consistent), and INSP-03 conclusions premised on the then-missing reliance register (10 of DEL-01-02's 12 staleness rows) with no superseding notes. All three are mechanical repair tranches for R5, in the PKG-07 REF-006 pattern.
3. **Fan-in flipped the only ACCEPTED_DIVERGENCE in the package.** DEL-01-04 ACC-002 (BR-005 register wording vs the ruled domain-tool surface) failed the strict affirmative-permission test — D-APP-50/52 permit the tool surface, not the register-wording divergence — and the owner accepted STALE_SPECIFICATION; a minority ALIGNED reading rides to R3. W1–W5 pattern holds: ACCEPTED_DIVERGENCE survives only with an affirmative permitting decision on the exact divergence.
4. **The RBR-014 contest resolved on a live fact, and yields an R3 rule candidate.** The register's "Bash denied by default" is flatly false at HEAD (default resolves to `ask`; workspaceWrite auto-allows after hooks) — owner re-verified and flipped to STALE_SPECIFICATION. Proposed run-wide MR-1 application rule for R3 ratification: assessment-only staleness → STALE_ASSESSMENT; any kit/register surface still carrying the stale wording → STALE_SPECIFICATION.
5. **Genuine unimplemented residue is small and owner-gated:** the seven governance checklist/notes artifacts (DEL-01-01 ACC-002, filenames on open Guidance ruling R004, NEW-PACKET), the SCA-APP-001 Pi/provider-expansion prohibition missing from the BR register (DEL-01-04 ACC-003 — an agent closure review cannot discharge it), the completed human-attributed release copy-review record (DEL-01-03 ACC-05), and the open CT-001 path-label ruling (NEW-PACKET).
6. **Register hygiene:** three REGISTER-class defects, all LOW-grade metadata lag (corpus-v1 pin in DEP-01-01-010; REF-007 machine-absolute path — a wart present in all four deliverables' `_REFERENCES.md`, escalated run-wide; DEP-01-03-011 undated stale clause). Dependencies.csv substance verified consistent in all four deliverables; R1 REQUIREMENT_INDEX parser gap confirmed for DEL-01-02 only (25 claims re-derived from spec).
