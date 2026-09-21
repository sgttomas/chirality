# V-DEL-10-01 verifier notes (DEL-10-01, PKG-10, RUN_D128)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 1 (REM-1) | 0 | 2 (CLM-022.2, REM-2) |
| a30 | 11 | 8 | 1 (CLM-004.5, ImplementationEvidence) | 2 (CLM-002, CLM-004.1) |
| b | 3 | 3 | 0 | 0 |
| c | 1 | 1 | 0 | 0 |
| **Total** | **18** | **13** | **1** | **4** |

Verdict-field refutations (Addendum 3): 0. The one REFUTED item is a field-only line-anchor issue.

## (ii) Patterns

1. **"Present fact now false" text kept under non-STALE verdicts (§2.6 tie-break rule 1).** CLM-002 ("not current implementation", NOT_AUDITABLE), CLM-004.1 ("tools live", PARTIALLY_IMPLEMENTED) and REM-2 ("staged, read-only boundary", ALIGNED): the rulebook also allows STALE_SPECIFICATION for each. In two of them (REM-2 and CLM-004.1) the worker's own Notes or RemainingWork already call the text wrong. These are graded CONTESTED, not REFUTED, because §2.3's reachability rule (CLM-004.1), the CONTEXT_CLAIM "may take" wording (CLM-002) and the open-item reading (REM-2) each leave the worker's reading open too.
2. **Evidence-boundary and anchor issues.** CLM-022.2 grounds ALIGNED on a Root top-level `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/...` record, which is outside the RUN_BASIS §3 roots (the worker flagged this itself). Inside the roots, only the matrix half of VER-001 holds (SoW:493). No parity report or source-marker map exists on any App surface. The Disposition is therefore CONTESTED (ALIGNED vs PARTIALLY_IMPLEMENTED), and the out-of-root ImplementationEvidence citation should be dropped. Separately, in CLM-004.5 `domain-proposal-tools.ts:139` points at the pec transport-profile resolver, not at the propose/validate tool set (use :38-39/:438/:589).
   Minor, recorded in CLM-004.1's CorrectReading: DirectionEvidence tags `docs/CONTRACT.md` with `CTX:`, but CONTRACT is GOVERNING (RUN_BASIS §5).

Confirmed as sound: REACH tags match `REACHABILITY.csv` (domain-profile.ts LIVE via runtime daemon standalone-bin; registry, read-tools, proposal-tools and headless runner LEGACY_ONLY). The facade TEST_ONLY tag is not in the map (frontend/packages is not covered), but it holds statically: the only importer is harness-contract-rollback.test.ts. REM-1's plain `R4` is correct: DIRECTIVE §8 is unamended while CONTRACT:7 is amended under D-GOV-43, and none of R4-Q1..Q4 names the shared-daemon or PEC-client premise. UNKNOWN for a Root/PEC gate with no App carrier is correct. `_DomainEngines/profiles/*.yaml` is Root-owned, but the App registry loads it (registry :53-60), so citing it at CLM-003.2 is admissible under RUN_BASIS §3. No cited path appears in TOUCHED_PATHS.csv, so PostReleaseBasis NO holds for every item.

## (iii) Effort

About 25 file and range reads, 10 greps, 4 read-only git log/show calls against the frozen tree. I read nothing from other units, R0 ledgers, runtime execution or the Root top-level execution tree. The context budget was comfortable.
