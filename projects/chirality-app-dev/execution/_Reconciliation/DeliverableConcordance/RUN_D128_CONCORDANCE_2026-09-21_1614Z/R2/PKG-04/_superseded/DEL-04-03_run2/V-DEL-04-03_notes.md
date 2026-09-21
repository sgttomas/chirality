# V-DEL-04-03 — verifier notes (R2, PKG-04, rerun ledger)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| n (30% of other non-ALIGNED) | 14 | 11 | 2 | 1 |
| b (15% of ALIGNED) | 3 | 2 | 1 | 0 |
| c (PARTIAL reverse responses) | 2 | 2 | 0 | 0 |
| e (errata) | 2 | 2 | 0 | 0 |
| **Total** | **21** | **17** | **3** | **1** |

No Disposition-level refutations. The three refutations are field-level: AuthorityTier on
CLM-004.4 and CLM-023, and ImplementationEvidence reach on CLM-004.2. One Disposition is
CONTESTED (CLM-004.6). Both errata are correct.

## (ii) Systematic patterns

1. **Barrel-inflated reach on contracts symbols (GRADING_KEY 1).** `REACHABILITY.csv` marks
   `engine-conformance.ts` and `agent-engine-port.ts` LIVE through the `contracts/src/index.ts`
   and `harness/index.ts` barrels. At symbol level, `runEngineConformance` and
   `PUBLIC_UI_EVENT_NAMES` have no non-test consumer. `PUBLIC_UI_EVENT_NAMES` is used only by
   `engine-conformance.ts` and by tests. The worker's errata fixed the conformance citations
   (CLM-004.6 and CLM-011.7) but missed the same defect in CLM-004.2
   (`agent-engine-port.ts:97`). None of these changes a Disposition.
2. **AuthorityTier not taken from the sources the row restates (GRADING_KEY 7).**
   - CLM-004.4 cites only SOW-051 and PRD FR-083 but takes GOVERNANCE_INVARIANT; it should be
     PRD.
   - CLM-023 takes LOCAL_DESIGN, but its Considerations table restates SPEC s10-11 and PRD
     FR-075, FR-116 and FR-123; it should be GOVERNANCE_INVARIANT.
3. **Uneven treatment of the superseded "compact UI" direction.** CLM-024 is correctly marked
   STALE_SPECIFICATION under the SPEC s11 and TYPES s7.4 revision (D-GOV-43). CLM-023's
   "UI versus audit detail" consideration (use UI events for compact browser streaming) is
   declared to hold at module level with DirectionEvidence NONE_FOUND. The Disposition is
   unaffected, because CLM-023 is already stale on the promotion slot.
4. **Live versus module reading of the conformance boundary (GRADING_KEY 2).** CLM-004.6 reads
   the SDK-named condition as compatibility history. SPEC s10.3:680 is unamended and applies
   to any provider-backed adapter, and the live Codex default has not been run through
   conformance (R4-Q2), so DOCUMENTED_UNIMPLEMENTED is equally defensible. The row's R4-Q2
   citation already surfaces this.
5. **Minor Notes inaccuracies with no graded effect.**
   - CLM-003.4 attributes all its lines to d1e3d6b68. Lines :871 and :884 blame to e39d07827
     (2026-06-13); both commits predate 2026-08-22, so PRE_V3_DRIFT holds.
   - CLM-003.6 and CLM-023 carry `D-APP-52 (context)`. The register row for D-APP-52 is the pec
     transport ruling; only the 2026-07-18 closure run bears that name.
   - HumanDecisionNeeded differs between CLM-004.4 (NO) and CLM-008/CLM-021 (R4-Q1), although
     all three rest on the same retained-SDK premise. The worker records this alternative.

## (iii) Capability-file accuracy

- CAP-RTCONTRACT-023 (REACH=LIVE, TYPE-ONLY): holds.
- CAP-RTCONTRACT-036 (REACH=LIVE, TYPE-ONLY; PUBLIC_UI_EVENT_NAMES used only by tests): holds.
- CAP-RTCONTRACT-039 (REACH=TEST_ONLY): holds; it contradicts the pack's module-level LIVE
  tag, correctly.

No capability-file inaccuracy found.

PostReleaseBasis: none of the cited code or deliverable files appears in `TOUCHED_PATHS.csv`.
Every checked row's `NO` holds.

## (iv) Effort

- Read the brief, grading key, CONVENTIONS, the 21 selected ledger rows, the errata, the
  reverse rows and 3 capability rows.
- At the frozen tree: ScopeOfWork, Dependencies, _DEPENDENCIES, _REFERENCES and the INSP-03
  assessment; SPEC s10.3, s11 and the preamble; TYPES s7.4; the delegated engine adapter;
  contracts types, event-schema, agent-engine-port and engine-conformance; the SDK mapper and
  its tests; the D-APP-52 register row.
- Blame: 4 commands against the frozen tree.
- The context budget was comfortable.
- Discipline note: one recursive `grep -l` for `engine-conformance` over
  `projects/chirality-runtime` returned file names under `projects/chirality-runtime/execution/**`.
  Their contents were not opened or used, and later greps were limited to `packages` and
  `tests`.
