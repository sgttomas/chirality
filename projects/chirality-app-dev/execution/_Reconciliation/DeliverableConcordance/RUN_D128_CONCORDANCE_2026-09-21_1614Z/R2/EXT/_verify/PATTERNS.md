**Rerun (1).** `DOC-ADDING_A_TOOL` was rerun by a fresh worker because shard DOC67 refuted 1 of
the 4 checked items on Disposition (25%, above the 10% threshold):
- The refuted item was `#3`, ACCEPTED_DIVERGENCE resting only on the document's own D-GOV-43
  banner. The verifier read it as IMPLEMENTED_DIFFERENTLY.
- The original attempt is kept at `DOC_DEV/DOC-ADDING_A_TOOL_claims.csv`.
- The rerun brief (`BRIEFS/W_DOC_DEV_R1.md`) restated the rules in general terms only.
- The rerun (`DOC_DEV_R1/`) was checked in full by shard DOC67R. That full check is a manager
  addition, class `r`, because deterministic sampling would have checked only 3 of 8 rows. It
  found 0 of 8 Disposition refutations, so the rerun is the ledger of record.
- No other ledger reached the threshold. SOW was 1 of 29 (SOW-045.2); every other ledger was
  0. No errata were filed.

**Patterns across shards** (from the shard notes `_verify/V-*_notes.md`):
1. **Where ACCEPTED_DIVERGENCE ends and a GOVERNING ruling is required.**
   - ADDING_A_TOOL#3 (superseded attempt) rested on a document banner.
   - DEC D-APP-112.2 rests on a 2026-09-19 owner direction that has no register row.
   - DEC D-APP-96 cites a seating ruling that never mentions the ruled presentation.
   - All three were self-flagged or caught. The recurring question is whether an owner
     direction without a register row counts as GOVERNING. R3 should cluster these cases.
2. **One mechanism, different Dispositions.** The D-GOV-43 shared-config, approval-policy and
   event pass-through mechanisms land as AUTHORITY_CONFLICT in some rows and
   IMPLEMENTED_DIFFERENTLY in others.
   - Examples: SOW-076 vs SOW-045.2 (refuted); RQGATES#5 vs RELIANCE#3.1; SOW-050.2 and
     075.2 (contested).
   - Several of these rows now fall under R4-Q6 (Addendum 9), which was adopted after all EXT
     ledgers were sealed. R3 maps them.
3. **Legacy-only guarantee rows split** between STALE_SPECIFICATION (RQGATES#6, RELIANCE#3.2,
   #10) and IMPLEMENTED_DIFFERENTLY (RELIANCE#3.8, #3.11).
4. **AuthorityTier on process/command-table STATE_ASSERTION rows.**
   - VALSTRAT tiers them LOCAL_DESIGN; BUILDREL tiers them NOT_APPLICABLE.
   - Two VALSTRAT rows were corrected (CORRECTIONS.csv); the unsampled `VALSTRAT#4.x` rows
     likely share the defect.
   - ADDING_A_TOOL#7 is contested the same way.
5. **REACH and PostReleaseBasis mechanics.**
   - Build scripts and `package.json` are outside `REACHABILITY.csv`, and workers tagged them
     differently: SOW and DOC_REL used LIVE, DOC_DEV used TEST_ONLY.
   - RELIANCE#3.11 uses a symbol-level LEGACY_ONLY tag for a file the map calls LIVE.
   - RELIANCE#4.7 missed a `da95ec194` blame (corrected); its SEE target `#3.7` likely shares
     the defect.
6. **Root- and Runtime-owned effects.** These cannot be verified inside the evidence roots
   (D-APP-125.1, CONTESTED).
