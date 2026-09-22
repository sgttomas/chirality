# T8C spot check notes (S2 and S3, blind)

Scope: all 30 S3; S2-001..065 (40 MANDATORY, 25 OPTIONAL), two rows each; 160 rows. Blind: no REMAP_LOG,
RUNWIDE_CALLS, T* work files or Notes. Sources: frozen tree, rulebook, R2 evidence pack and capability files.
## Counts

S3 29 CONFIRMED / 1 UNDECIDED. S2 Disposition 60 / 2 REFUTED / 3 UNDECIDED. S2 HDN 58 / 6 REFUTED /
1 UNDECIDED. Total 147 CONFIRMED, 8 REFUTED, 5 UNDECIDED, 0 UNVERIFIABLE.
## Refuted

- S2-009 DEL-04-05#CLM-024 HDN `R4-Q1` → `R4-Q1; R4-Q6` (turns on App DIRECTIVE s.2.8).
- S2-013 DEL-07-01#CLM-011.4 HDN `R4-Q1` → `R4-Q1; R4-Q6` (divergence only via live "Full access").
- S2-028 DEL-06-05#CLM-024 HDN `R4-Q1` → `R4-Q1; R4-Q6` (cites K-PERM-6; sibling CLM-004.2 already has R4-Q6).
- S2-043 DEL-07-01#CLM-011.6 HDN `R4-Q1` → `R4-Q1; R4-Q6` ("even when a permissive mode would allow").
- S2-038 DEL-02-05#CLM-011.3 Disposition `AUTHORITY_CONFLICT` → `ALIGNED`; HDN `R4-Q5` → `NO`.
- S2-052 DEL-02-05#CLM-003.2 Disposition `AUTHORITY_CONFLICT` → `ALIGNED`; HDN `R4-Q5` → `NO`.
  (SPEC s.11 and TYPES s.7.4 are both amended under D-GOV-43 and keep the names; live code handles them.)
## Undecided (both readings in the Evidence column)

- S3-002 DEL-10-01#REM-1: R4-Q6 for DIRECTIVE s.8 (daemon) or plain R4. S2-010 (same cluster) keeps plain R4.
- S2-031 DEL-09-04#CLM-022: CONTRACT preamble line 17 names K-RELEASE-1 and requires signing and
  notarization (STALE_SPECIFICATION), or K-RELEASE-1 is still unamended (AUTHORITY_CONFLICT).
- S2-047 DEL-10-04#CLM-016.1: I did not read the D-APP-70 ruling record within my budget.
- S2-059 DEL-10-02#CLM-024: a trade-off for future domain operations; no domain operations exist on the live path.
## Systematic observations

1. R4-Q6 is applied unevenly: DEL-07-01 and DEL-06-05 rows that turn on danger-full-access ("Full
   access", K-PERM-6) cite only R4-Q1. A sweep for "bypass maps to danger-full-access" would catch them.
2. The run treats event-name rows that cite only SPEC s.11 and TYPES s.7.4 as R4-Q5 conflicts. Those
   two texts are amended. R4-Q5 applies only where unamended K-ENGINE-4 or SPEC s.10.3 is cited.
3. The REACH re-mappings (domain-profile.ts, validate-release-quality-evidence.mjs and
   FileSessionManager) follow the capability files' symbol-level tags. They differ from the pack's
   module-level REACHABILITY.csv (LIVE via barrel or shared module). The re-mappings are correct, but
   the rows now disagree with the pack map, and rows that cite the pack alone will need the same refinement.
4. The SoW-migration VER-001 UNKNOWN rows are sound as process claims. Content preservation can be
   checked with read-only git. For DEL-05-03, 233 of 234 legacy lines survive verbatim
   (`T8C_scripts/parity.py`). ACCEPTANCE rows of the form "every legacy line preserved" (AC-001) can
   therefore get positive evidence rather than NONE_FOUND.
5. On AUTHORITY_CONFLICT rows where a LIVE path meets the claim (Anthropic key UI rows S2-006, 023
   and 063), the conflict rests on R4-Q6 scope alone. This is consistent across the run.
