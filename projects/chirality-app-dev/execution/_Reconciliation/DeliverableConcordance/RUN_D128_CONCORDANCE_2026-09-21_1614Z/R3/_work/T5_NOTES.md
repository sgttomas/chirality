# T5 notes: Addendum 5 tie-break on sealed rows

Input `R3/_work/CAND_TIEBREAK.csv` (82 rows; the owner-deferred `DEL-06-02#CLM-005` and `#CLM-032` are
not in it). Output `R3/_work/T5_TIEBREAK_VERDICTS.csv`; script `R3/_work/T5_scripts/t5_tiebreak.py`.

## Counts
- KEEP 50, MOVE 30, UNDECIDED 2, OUT_OF_SCOPE 0. ALSO notes (rule 4): 5, all ALSO:REMAINING_STATE_MISMATCH.
- MOVE RSM -> STALE_SPECIFICATION: 21. MOVE STALE_SPECIFICATION -> RSM: 9.
- By package (KEEP/MOVE/UNDECIDED): PKG-01 5/0/0; PKG-02 5/0/0; PKG-03 3/0/0; PKG-04 3/17/1;
  PKG-05 5/1/0; PKG-06 3/3/1; PKG-07 6/2/0; PKG-08 3/3/0; PKG-09 10/3/0; PKG-10 6/1/0; EXT 1/0/0.

## Patterns behind the moves
1. **_REFERENCES.md MATCH rows (5 to SS).** DEL-04-01#REGISTER-1, DEL-04-02#REGISTER-1, DEL-08-04#REGISTER-1..3.
   The frozen tables record ActualSHA256 = Expected, Status MATCH, with no snapshot date. Rule 1 names
   "a hash recorded as MATCH". DEL-09-07#REGISTER-1 stays RSM: pins only, no MATCH verdict.
2. **P40 "current-state note" restating MATCH (14 to SS).** DEL-04-01, DEL-04-02, DEL-04-04 SoW rows say
   REF-006 "is MATCH" and call the note current. The date names the note, not a MATCH snapshot.
   Rule 3: each carries `SEE:` to its deliverable's REGISTER-1 row.
3. **Register-internal lag (9 to RSM).** DEL-05-03, DEL-06-03, DEL-06-04, DEL-07-01, DEL-07-02, DEL-09-02,
   DEL-09-03, DEL-09-06, DEL-10-05. Scaffold "TBD - no accepted dependency edges extracted yet", lagging
   counts, un-flipped "preview"/"current mirror" labels, lagging PENDING fields. Reading applied: rule 2b
   admits text false about the register itself (as a stale `Last Updated` is) and bars text false about the
   product or its references. Workers had split on this same text.
4. **Other moves to SS (2).** DEL-04-05#REGISTER-5 (a closed RQ-011 gap said to "remain", rule 1).
   DEL-06-02#REGISTER-2 (absent EvidenceFile targets and SATISFIED on a non-reproducing MATCH; rule 4,
   ALSO:RSM). DEL-06-05#REGISTER-3 has the same shape and stays SS with ALSO:RSM.

## Patterns kept
- Remaining items with a correct open status but a stale gate or write locus stay SS (2a fails).
- Empty `## Remaining` contradicted by open work stays RSM (2a).
- Remaining prose stating false present facts and closing items (DEL-02-01#REM-1, DEL-02-02#REMTXT-1,
  DEL-08-02#REMTXT-1) stays SS with ALSO:RSM (rule 4: the repair is a rewrite).
- SoW TBD/open-items entries behind known values stay RSM (2b TBD placeholder).

## UNDECIDED
- DEL-04-01#CLM-004.2: says `_REFERENCES.md` "records MATCH" (literally true) and asks for snapshot
  confirmation. A: SS, "reconciled under D-APP-38" presents MATCH as current. B: not false; neither fits.
- DEL-06-06#STATE-2: empty `## Remaining` (2a, RSM) plus MEMORY.md naming a LEGACY_ONLY module as the
  canonical surface (1, SS). The row carries both claims and the rules do not rank them.
