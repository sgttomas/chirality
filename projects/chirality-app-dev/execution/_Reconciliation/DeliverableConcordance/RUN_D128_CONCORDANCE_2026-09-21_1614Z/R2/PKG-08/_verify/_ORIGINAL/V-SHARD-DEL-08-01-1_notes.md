# V-SHARD-DEL-08-01-1 — verifier notes (DEL-08-01)

Evidence only. These verdicts are not rulings. Evidence was read at the frozen basis
`00115c719`; git use was limited to `log -1`. No ledger, notes, reverse or errata file was
edited.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (errata, LOW/self-flag, REMAINING_WORK, AUTHORITY_CONFLICT) | 6 | 3 | 1 | 2 |
| a30 (30% sample of other non-ALIGNED rows) | 12 | 6 | 1 | 5 |
| b (ALIGNED sample) | 1 | 0 | 0 | 1 |
| e (errata rows) | 2 | 2 | 0 | 0 |
| c (capability responses) | 2 | 2 | 0 | 0 |
| **Total** | **23** | **13** | **2** | **8** |

**REFUTED on Disposition:** `DEL-08-01#STATE-1`. The row is AUTHORITY_CONFLICT; the proposed reading is
STALE_SPECIFICATION with A2_TOPOLOGY and HumanDecisionNeeded NO. DIRECTIVE §0 settles the
disagreement: CONTRACT K-RUNTIME-1, re-expressed under D-GOV-43, outranks the decomposition
package-scope row. §1 does not allow AUTHORITY_CONFLICT when the authority order settles it.

**REFUTED on another field:** `DEL-08-01#CLM-004`, AuthorityTier. The unit restates DIRECTIVE
§2.7 and CONTRACT K-ROOT-3, so the tier is GOVERNANCE_INVARIANT, not NOT_APPLICABLE. The
Disposition holds.

**CONTESTED on Disposition:**
- `CLM-009.12`: IMPLEMENTED_DIFFERENTLY or AUTHORITY_CONFLICT (R4-Q1).
- `CLM-009.3`: IMPLEMENTED_DIFFERENTLY or PARTIALLY_IMPLEMENTED (only `docs/PLAN.md` is missing).
- `REM-1`: STALE_SPECIFICATION or DOCUMENTED_UNIMPLEMENTED with LIFECYCLE_GATE_PENDING.

## (ii) Systematic patterns

1. **Build scripts have no fitting reach tag.** This affects CLM-005, 011, 012, 016 and 008, and
   is also noted on CLM-004 and 009.3.
   - The forward rows tag `frontend/scripts/{prepare-packaged,verify}-instruction-root*.mjs` as
     `REACH=TEST_ONLY`.
   - The BUILD capability surface tags the same scripts `REACH=LIVE; BUILD-TIME`. The scripts
     are chained in `desktop:prepare`, `desktop:pack` and `desktop:dist` (`package.json:41-43`).
   - The pack's `REACHABILITY.csv` does not cover `frontend/scripts`, and the tag vocabulary has
     no build-time value. Read literally, the A0 rule would even give `LEGACY_ONLY` + `UNREACHED`.
   - I grade these CONTESTED on the ImplementationEvidence field only. No Disposition turns on
     the tag. The reverse notes already flag the issue without errata.
   - Recommendation for the manager: settle one run-wide convention, for example the BUILD
     area's `BUILD-TIME` note.
2. **LatestDecision and DirectionEvidence classes disagree.** On CLM-009.12, 009.11 and 002,
   LatestDecision marks `D-APP-nnn (context)` while DirectionEvidence cites `GOV:` for the same
   decision. On delegation rows (009.11, 009.12), D-APP-127 contains no delegation text. The
   ruling that explains native delegation is D-GOV-43, carried in SPEC §25 (`SPEC.md:1232-1233`,
   `:1336-1340`).
3. **Authority-order steps are skipped or left half-applied (MR-11 / §1).**
   - STATE-1 uses AUTHORITY_CONFLICT where DIRECTIVE §0 settles the question.
   - CLM-009.12 states in its own RemainingWork that K-SUBAGENT-1 is unamended and routes the row
     to R4-Q1, but still picks a substantive Disposition.
   - CLM-009.7 applies §0 in Notes but keeps plain `R4` beside `R4-Q1`.
4. **LOW-row alternatives are off-vocabulary.** CLM-009.14's LEAST-CONFIDENT alternative is
   NOT_AUDITABLE, which §2.6 reserves for CONTEXT_CLAIM rows. A valid alternative is
   IMPLEMENTED_DIFFERENTLY.
5. **Both errata rows hold.**
   - 009.7: the Runtime `listAgents` function (`runtime-service.ts:587-615`, used at :176 and
     :316) is a LIVE consumer of the SPEC §7.1/§7.2 fields.
   - 009.12: the live child-role path is `materializeProductNativeRoles`
     (`product-native-role-config.ts:8-37`), called from `delegated-engine-adapter.ts:213` with
     `nativeRoleDirectory` from `app-owned-composition.ts:214`. `loadTrustedNativeRoleConfiguration`
     has only a test caller. That makes it a module-LIVE, symbol-TEST_ONLY nuance, and it does not
     change the Disposition.

**Checks that passed on every item:**
- PostReleaseBasis: no cited file appears in TOUCHED_PATHS.
- All cited test case titles exist at the frozen basis.
- SoW line anchors for REQ003, REQ007, REQ009, REQ011, REQ012 and REQ014 are exact.
- Code anchors are within tolerance.
- MechanicallyUnblocked is NO throughout. On REM-1 this is correct: DEL-02-02-V3-04 is not
  selected, and DEL-06-03-V3-01 is still pending.

## (iii) Effort

- **Read:** about 25 targeted reads or greps. Sources:
  - the deliverable SoW, `_STATUS`, `_CONTEXT`, Dependencies, INSP-03 and MEMORY;
  - App SPEC §1.1, §7 and §25, CONTRACT, DIRECTIVE §0, and the decomposition;
  - D-APP-110 and D-APP-127;
  - the CONTEXT source CORPUS_V21 §Basis;
  - 8 code files and the test titles;
  - the evidence pack, and the BUILD and HARNESS surfaces.
- **Context budget:** comfortable.
