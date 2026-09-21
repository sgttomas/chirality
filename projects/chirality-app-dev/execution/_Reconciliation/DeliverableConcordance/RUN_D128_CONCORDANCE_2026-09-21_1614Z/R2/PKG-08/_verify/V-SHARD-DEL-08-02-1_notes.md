# V-SHARD-DEL-08-02-1: verifier notes (RUN_D128, R2 PKG-08, unit DEL-08-02)

This is fresh TASK verification against the frozen tree at `00115c719`. The only git used
was read-only `log`, `show` and `blame -L` against that tree. I edited no ledger, notes,
reverse or errata file. DEL-08-02 has no errata file, so there are no class-e items.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (REMAINING_WORK) | 1 | 1 | 0 | 0 |
| a30 (30% of other non-ALIGNED) | 18 | 13 | 2 | 3 |
| b (unselected ALIGNED) | 2 | 2 | 0 | 0 |
| c (reverse PARTIAL) | 6 | 6 | 0 | 0 |
| **Total** | **27** | **22** | **2** | **3** |

- **Disposition-level REFUTED:** none.
- **Disposition-level CONTESTED:** `DEL-08-02#CLM-003.2` and `DEL-08-02#CLM-004.3`.
- **Field-level REFUTED:**
  - `#CLM-003.6` AuthorityTier: it should be GOVERNANCE_INVARIANT, not PRD.
  - `#CLM-005.3` Notes: the count of tests is wrong.
- **Field-level CONTESTED:** `#CLM-021` AuthorityTier.

## (ii) Systematic patterns

1. **Live by static import, but never rendered.** Examples: `#CLM-004.3`, `#CLM-003.4`,
   `#CLM-003.3`.
   - `REACHABILITY.csv` tags `pipeline-surface.tsx` and `agent-matrix.tsx` as LIVE.
   - Both modules exist only inside the `legacy` prop, which `woven-dialogue-route.tsx:18`
     voids. `WovenDialogueShell` also ignores its props (`:77`).
   - Every row states the REACH tag that matches the pack and then gives the code-verified
     reason. This handling is correct.
   - Only `#CLM-004.3` changes Disposition on this nuance, so the key makes it CONTESTED.
     The worker's reading (unrendered, so DOCUMENTED_UNIMPLEMENTED) is the better-supported
     one.
   - A `LIVE_IMPORT_ONLY` class in the pack would settle this.
2. **AuthorityTier drift to PRD where SPEC is restated.** This repeats R0 VERIFICATION §4.6.
   - `#CLM-003.6` cites SPEC §13.2 in its own NormativeSource but is tagged PRD. The
     class-c item on `#CLM-009.12` shows the same defect: its SoW source cell names SPEC
     §13.2.
   - `#CLM-021` mixes principles that restate TYPES and SPEC §13.1 with deliverable
     guidance.
   - These are metadata errors only. Every Disposition holds.
3. **Partial alias tables and the choice between IMPLEMENTED_DIFFERENTLY and
   PARTIALLY_IMPLEMENTED.** Example: `#CLM-003.2`.
   - The live resolver keeps the same mechanism, with 2 of the 4 TYPES §3.4 entries.
   - The reachability rule's "live path covers part ⇒ PARTIALLY_IMPLEMENTED" supports the
     alternative reading.
   - Compare `#CLM-003.5`: there the live behaviour affirmatively contradicts the clause
     (resume-on-selection), so IMPLEMENTED_DIFFERENTLY is clearly right.

**Checks that held across the shard:**

- PostReleaseBasis `NO` on every row. None of the cited files is in `TOUCHED_PATHS.csv`.
- REACH tags match the pack.
- The CTX citation (`MANAGER_RETURN.md:6-13`) and the GOV citations (D-APP-108 Q3 and
  D-APP-127 §D-APP-88) are verified.
- The `9b005c23a` (2026-09-09) and `3b6852548` (2026-07-22) dates, and the SoW blame
  (`f2fd30604`, 2026-07-14), support the V3_RELEASE_SCOPE and PRE_V3_DRIFT tags.
- My spot-check of `_REGISTER.md` for ORCHESTRATOR, four-role, direct-entry and resume found
  no governing direction. The NONE_FOUND values stand.
- The four class-c PARTIAL responses on HARNESS capabilities all point at LEGACY_ONLY
  modules, and the links hold. For example, `persona-manager.ts:209` reads AGENT files
  through `readAgentInstruction`, and `assertDirectChatPersona` raises INVALID_REQUEST.

**Rule ambiguities noted:**

- MR-8(iv) versus a SoW row restating a REGISTER snapshot row (`#CLM-004.1`).
- AuthorityTier on REMAINING_WORK rows (`#REM-1`).
- CONTEXT_CLAIM rows whose premise is now false, for which STALE_SPECIFICATION is allowed
  but not required (`#CLM-020`).

## (iii) Effort

- **Files read:** about 30 files or line ranges.
  - The shard's ledger rows and the unit notes.
  - The reverse rows and the SURFACES capability rows.
  - The pack's REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES, DECISION_HITS and D-APP-127
    map rows.
  - App TYPES §3.4/§4 and SPEC §13.1/§13.2/§17.1/§17.6/§17.9; PRD FR-008/011/023/025/026.
  - The SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `_DEPENDENCIES` and `Dependencies.csv`.
  - About 14 frontend and Runtime source and test files.
  - The D-APP-108 and D-APP-127 rulings and the register.
- **Git:** 3 `log` calls and 3 `blame -L` calls, all against the frozen tree.
- **Context budget:** adequate.
