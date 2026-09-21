# V-DEL-06-02_A: verifier shard notes (DEL-06-02, unit DEL-06-02_A)

I verified this shard against the frozen tree at `00115c719` only, using evidence and the shared grading
key in `R2/PKG-06/BRIEFS/VERIFIER_BRIEF.md` and `CONVENTIONS.md`.

- Unit `DEL-06-02_A` is the ledger of record. I did not read `DEL-06-02_B`.
- I edited no ledger, worker or pack file.
- The unit has no errata file, so the selection holds no class `e` items.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 4 | 2 | 1 | 1 |
| a30 (30% of other non-ALIGNED) | 16 | 11 | 0 | 5 |
| b (ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse) | 6 | 6 | 0 | 0 |
| **Total** | **28** | **21** | **1** | **6** |

## (ii) Systematic patterns

1. **The dated REF-006 note (MR-8 iv) is CONTESTED.** This covers CLM-001 and its SEE row CLM-008.
   - The "D-APP-56 R5 P40 current-state note (2026-07-12)" was true of that snapshot.
   - D-APP-56 P13 (dated-note discipline) and P16 ("REF-006 register-lag class") point to a register-lag reading. REGISTER-1 already carries the hash defect.
   - The undated MATCH assertions are correctly STALE_SPECIFICATION: CLM-004.1 at line 75, CLM-007's References column, and CLM-029 at line 447.
   - This matches the V-DEL-06-01 treatment of DEL-06-01 CLM-001, 007 and 023.
2. **The boundary between AUTHORITY_CONFLICT and IMPLEMENTED_DIFFERENTLY is applied unevenly.**
   - The rows that restate only the unamended clause hold as AUTHORITY_CONFLICT with R4-Q1: CLM-010.6 (K-TOOL-2) and CLM-024 (K-TOOL-2, K-PERM-3, K-MCP-1).
     - D-GOV-43 names none of these clauses (`D-GOV-43.proposed.md:173-195`).
     - The enforcement surfaces are the legacy tool pool and options builder (`CONTRACT.md:92-98`).
   - CLM-003 is CONTESTED.
     - Its Attributes table carries dedicated "Exposure boundary" (K-TOOL-2) and "Restriction boundary" (K-PERM-3) rows.
     - The whole unit is nonetheless IMPLEMENTED_DIFFERENTLY. That effectively resolves the clause the ledger elsewhere escalates.
   - CLM-010.7 (PRD FR-082 read-first) is CONTESTED the other way.
     - D-GOV-43 item 4 sets the recommended default to on-request with workspace-write, undercutting FR-082 without naming it.
     - DIRECTIVE §0 does not rank D-GOV rulings against the PRD.
   - CLM-010.9 (K-PERM-3) could go either way. It is phrased in SDK terms that the CONTRACT's Codex-only preamble (`CONTRACT.md:13-15`) treats as compatibility history, and the live path restricts through the Codex sandbox, which is a mode policy.
3. **CLM-010.9 AssessmentEvidence is REFUTED (field-level).**
   - The gloss copied from the REQ006/REQ007 rows claims that INSP-03's REQ009 PASS cited the removed `tool-descriptor.ts`.
   - It actually cites `sdk-options-builder.ts` lines 87-116 (`Assessment_INSP-03_DEL-06-02.md:31`).
   - That file still exists at lines 147-210 (LEGACY_ONLY). The token OVERTAKEN is still right because the live engine is now Codex.
4. **Where legacy code is the only carrier, the Disposition is contested.**
   - CLM-005 is CONTESTED between STALE_SPECIFICATION (the TBD cells) and IMPLEMENTED_DIFFERENTLY.
     - Its Construction rows are met only on the LEGACY_ONLY tool pool, turn engine and options builder.
     - Deterministic ordering is not implemented: `tool-pool.ts:41-45` keeps request order.
     - CLM-003 and CLM-019 already disposition that content as IMPLEMENTED_DIFFERENTLY.
   - STATE-2 (the worker's LOW self-flag) is CONTESTED between IMPLEMENTED_DIFFERENTLY and PARTIALLY_IMPLEMENTED or DOCUMENTED_UNIMPLEMENTED. The App registers no application-tool catalog; only the Runtime validates.
5. **Evidence mechanics are sound.**
   - Every line anchor I opened shows the cited content. Drift was at most 1 line (`codex-supervisor.ts:653-657`), and no anchor showed different content.
   - REACH tags match `REACHABILITY.csv`.
     - `tool-descriptor.ts` and `mcp/tool-names.ts` are LIVE by module map but LEGACY_ONLY in CAP-RTCONTRACT-042/044 symbol notes.
     - That difference changes no Disposition here, because the ALIGNED CLM-035.2 is a module-level VER-002 inspection.
   - PostReleaseBasis YES on STATE-2 is verified against `TOUCHED_PATHS.csv`: `contracts/src/application-tools.ts` is wholly da95ec194, and `codex-supervisor.ts` lines 626-676 are da95ec194.
   - All 6 reverse responses hold. D-APP-70 item 5 maps `generate-tool-catalog.mjs` to DEL-06-02, which confirms CAP-BUILD-036 → STATE-1.

## (iii) Effort

- **Files opened:** about 20.
  - Rulebook and run basis.
  - Unit ledger and reverse files.
  - Pack files: REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES, DECISION_HITS and the D-APP-127 map.
  - Deliverable files: ScopeOfWork, `_REFERENCES`, `_CONTEXT` and `Assessment_INSP-03`.
  - App CONTRACT, PRD and DIRECTIVE §0.
  - D-GOV-43 proposal §4, and the D-APP-56 and D-APP-70 rulings.
  - About 10 code and test files, read as line ranges.
- **Recomputes:** DIRECTIVE, TYPES and PLAN SHA-256.
- **Not checked:** the D-APP-56 P15 packet ("declared-TBD register class") was not in reach. It may bear on the NONE_FOUND DirectionEvidence of CLM-005 and CLM-006.
- **Git:** no git commands were needed.
- **Context budget:** comfortable.
