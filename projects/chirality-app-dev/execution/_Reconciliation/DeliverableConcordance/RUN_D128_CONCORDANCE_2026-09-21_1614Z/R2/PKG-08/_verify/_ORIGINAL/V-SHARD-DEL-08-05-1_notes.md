# V-SHARD-DEL-08-05-1 — verifier notes (RUN_D128, R2 PKG-08, DEL-08-05)

These verdicts are evidence for the manager, not rulings. All evidence was read at the frozen tree
`00115c719`. The only git use was read-only `blame -L` and `log`/`show` against that tree.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (LOW / self-flag / AUTHORITY_CONFLICT / REMAINING_WORK) | 10 | 7 | 3 | 0 |
| a30 (30% sample of other non-ALIGNED rows) | 16 | 15 | 0 | 1 |
| b (15% sample of ALIGNED rows) | 3 | 3 | 0 | 0 |
| e (errata) | 2 | 2 | 0 | 0 |
| c (capability responses) | 2 | 2 | 0 | 0 |
| **Total** | **33** | **29** | **3** | **1** |

- **REFUTED at Disposition level:** DEL-08-05#CLM-018.1. The sealed value is PARTIALLY_IMPLEMENTED;
  the correct value is DOCUMENTED_UNIMPLEMENTED. The worker's own errata already proposes this
  value, and both errata rows are CONFIRMED.
- **REFUTED on a field, with the Disposition holding:**
  - REM-1, on Notes: the APP-HOLD-1 staleness claim is wrong.
  - STATE-1, on AuthorityTier: the row has NOT_APPLICABLE and should have LOCAL_DESIGN.
- **CONTESTED:** CLM-022, on Disposition: DOCUMENTED_UNIMPLEMENTED versus PARTIALLY_IMPLEMENTED.

## (ii) Patterns

1. **The AUTHORITY_CONFLICT rows hold up well.**
   - The ChildRunRecord cluster (CLM-006, CLM-012.1, CLM-012.2, CLM-013.2) conflicts with TYPES
     §10:
     - D-APP-40 explicitly names `ChildRunRecord.childRunId` as canonical.
     - TYPES §10 was later rewritten, in `c9734a6ee` and `ee35409f5` on 2026-07-11, to
       `chirality-agent-runs/v2` with `childInstanceId` and LAUNCHED..BLOCKED.
     - No ruling records that rewrite.
     - DIRECTIVE §0 does not rank rulings, so the conflict is correctly left open.
   - The daemon-linkage rows (CLM-037.2, STATE-1) match the rule for a ruling that undercuts an
     unamended GOVERNING clause without naming it:
     - D-GOV-43 item 7 retires daemon requirements as a class;
     - the decomposition row at line 372 is unamended.
2. **Errors come from the managed-writer reach nuance.**
   - `agent1-run-coordinator.ts` is LIVE by the pack, but it is never composed. `runAgent1` throws
     REQUIRED_DELEGATION_MISSING, and no Agent1RunPort is passed anywhere.
   - Rows that already say "no product instantiation" hold: CLM-003.1 and CLM-004.2.
   - CLM-018.1 let that module support PARTIALLY_IMPLEMENTED. This is the one disposition-level
     refutation, and the errata fixes it.
3. **Some rationale and tag details are sloppy.**
   - REM-1 says APP-HOLD-1 was retired by D-APP-127:
     - D-APP-127 removes only the `APP-HOLD-1-INIT-DEL-09-07` row;
     - the APP-HOLD-1 dispatch-preflight check stays in LOOP_INIT, and this run uses it.
   - STATE-1 uses NOT_APPLICABLE although it names a normative source.
   - MR-9: rows resting on INSP-03 (2026-06-21, before the 2026-07-13 SoW migration) cite no old
     REQ-08-05-nnn ID. Examples: CLM-004.3 (should cite REQ-08-05-009) and CLM-003.3.
   - There are two small line-anchor drifts, noted as ConventionIssue and not refuted:
     - CLM-012.2 cites `agent1-run-coordinator.ts:102`; the status union is at :96.
     - CLM-004.4's replay loop is at `session-store.ts:866-890`.

**Checked and found clean:**

- REACH tags match `REACHABILITY.csv` for every cited module.
- PostReleaseBasis is NO everywhere, and that is correct. The only touched files cited are
  `session-store.ts` and `codex-supervisor.ts`, and every relied-on line falls outside the
  TOUCHED_PATHS ranges.
- Every cited test case exists at the frozen tree.

## (iii) Effort

- **Reading:**
  - about 25 files or ranges, covering the deliverable carriers and key frozen code, plus
    rulings (D-APP-40/56/68/127, D-GOV-43), CONTRACT, TYPES, DIRECTIVE §0, LOOP_INIT and the
    evidence pack;
  - one RUN_D55 row (UPD-138).
- **Budget:** context was not tight.
