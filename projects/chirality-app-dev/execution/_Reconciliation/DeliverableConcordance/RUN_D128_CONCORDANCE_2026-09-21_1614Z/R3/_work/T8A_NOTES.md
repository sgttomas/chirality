# T8A notes: blind spot check, S1 sample A (PKG-00..PKG-05)

Input `R3/_work/SPOT_S1_A.csv`: 81 S1 rows, all checked on `Disposition`. No S2 or S3 rows in this sample.
Judged blind: only claim text in the frozen tree, frozen code and records, the rulebook, and the shared evidence pack.
Scripts: `R3/_work/T8A_scripts/dump.py` (claim-text extraction), `write_verdicts.py` (output).

## Counts

| Class | Rows | CONFIRMED | REFUTED | UNDECIDED | UNVERIFIABLE |
|---|---|---|---|---|---|
| S1 | 81 | 73 | 3 | 5 | 0 |

Verdict-field refutation rate: 3/81 = 3.7%. It is 8/81 = 9.9% if every UNDECIDED row counts against the concordance.

## Refuted

- S1-022 DEL-02-04#CLM-005.5: DOCUMENTED_UNIMPLEMENTED -> PARTIALLY_IMPLEMENTED. The live turn-coordinator drops unknown opts and applies fallbacks. Only the warning is missing.
- S1-024 DEL-02-03#CLM-009.3: IMPLEMENTED_DIFFERENTLY -> ALIGNED. Clearing the root nulls projectRoot, and composer, attach and workflow actions are then disabled on the live shell.
- S1-055 DEL-04-05#CLM-009.14: IMPLEMENTED_DIFFERENTLY -> AUTHORITY_CONFLICT (R4-Q5). The claim restates unamended K-ENGINE-4, and amended K-EVENT-1/6 require upstream names and payloads to be preserved. MEDIUM confidence.

## Undecided (both readings are in the CSV)

- S1-031 DEL-02-02#REGISTER-6: REMAINING_STATE_MISMATCH vs STALE_SPECIFICATION ("TBD - no accepted edges extracted yet"). The tie-break rules 2b and 1 overlap here.
- S1-035 DEL-02-05#CLM-025: STALE_SPECIFICATION vs NOT_AUDITABLE (a trade-off guidance row typed CONTEXT_CLAIM).
- S1-052 DEL-04-01#CLM-024: ALIGNED vs IMPLEMENTED_DIFFERENTLY. On the product reading, principles 1 and 4 hold only through legacy code, so HDN would need R4-Q1/Q5.
- S1-070 DEL-05-03#CLM-010.14: DOCUMENTED_UNIMPLEMENTED vs no-feature. The live path has no PEC transport, so IMPLEMENTED_DIFFERENTLY fits neither reading.
- S1-076 DEL-05-04#CLM-027: STALE_SPECIFICATION vs NOT_AUDITABLE. The conflict-table "None" is scoped to P1/P2.

## Systematic observations

1. R4-Q5 versus AUTHORITY_CONFLICT. Rows that restate unamended K-ENGINE-4 and diverge only because of the D-GOV-43 passthrough are dispositioned IMPLEMENTED_DIFFERENTLY or PARTIALLY_IMPLEMENTED, with R4-Q5 in HDN. Examples: S1-055, and the live reading of S1-043 and S1-060. CONVENTIONS 1 makes an unresolved GOVERNING conflict AUTHORITY_CONFLICT. R3 should state one rule for this group.
2. Subject test on SDK-era principle and rationale rows (S1-052, S1-060). The module reading was used although rule 2 prefers the product reading. On the product reading, the HDN token changes from R4-Q1 to R4-Q5.
3. Stale MATCH, snapshot and REF rows (S1-005, 016, 018, 036, 050, 051, 062) were applied consistently under tie-break rule 3 and CONVENTIONS 2.7. All confirmed.
4. SCA-APP-010 retirement (S1-032, 033) and MR-11 staleness via the amended K-EVENT-1 and K-EVENT-4 (S1-049, 064, 077, 078, 079) are consistent with the governing texts. S1-077 also touches unamended SPEC 8.2 (`CHIRALITY_SESSION_ROOT`). It stays STALE only if the DIRECTIVE 0 order ranks CONTRACT above SPEC. That ranking was not checked.
5. NOT_AUDITABLE heading and narrative rows (12 rows) were all confirmed.
6. HumanDecisionNeeded had no clear error in the rows I checked. S1-052 is the exception: HDN is `NO`, and on the product reading it needs R4-Q1 and R4-Q5.
