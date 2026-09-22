# T1 notes — plain `R4` mapped to named questions

Input `R3/_work/CAND_R4PLAIN.csv` (149 rows). Output `R3/_work/T1_R4QN_VERDICTS.csv` (149 rows).
Script `R3/_work/T1_scripts/t1_classify.py` holds one judgment per ClaimKey. These are agent
classifications, not rulings. Only the plain `R4` token was replaced. Other tokens (`R4-Q1`, `R4-Q2`,
`R4-Q4`, `R4-Q5`, `D-APP-117`) are kept. R4-Q1 was never added by judgment, because R4-Q1 is cited
by evidence only (Addendum 6 rule 3).

## Counts (Question column = what the plain R4 became)
- R4-Q6: 45; R4-Q4: 37; R4-Q5: 14; R4-Q1: 1; MULTI: 11; STAYS_R4: 41.
- MULTI breakdown: `R4-Q5; R4-Q6` ×7 (event rows that also cite DIRECTIVE §2.10, plus DEL-04-05#CLM-026);
  `R4-Q6; R4` ×2 (DEL-06-06#STATE-1, DEL-10-01#REM-1); `R4-Q4; R4` ×2 (DEL-08-02#CLM-012.2, REMTXT-1).
  A trailing plain `R4` in a MULTI cell means part of the row stays unframed.
- No row turned on R4-Q2 or R4-Q3 alone. Two rows that already cited R4-Q2 gained R4-Q5.

## STAYS_R4 questions by theme (candidate R4 clusters)
1. **Replay continuation (12 rows; plus the unframed part of 2 MULTI rows).** Does the shipped "Continue this
   chat" continuation (0ed1a1a7f) amend the SCA-APP-004 / SPEC §17.6 / PRD FR-008 read-only replay lens?
   DEL-05-04 (7), DEL-08-02 (5).
2. **Release signing and G6a (8).** Do the signed/notarized candidates and the carrier-only G6a retirement
   amend K-RELEASE-1's unsigned target and D-APP-97 F-APP-2? DEL-09-04 (2), DEL-09-05 (6). Done-declaration
   Q-02 bears on it. Addendum 10's notarization statement was not applied.
3. **D-GOV-43 A2 topology carriers (4; plus the unframed part of 2 MULTI rows).** Do unamended decomposition
   rows naming the retired daemon or Root-owned App Server supply still stand? DEL-04-01#CLM-009,
   DEL-04-01#STATE-1, DEL-05-01#STATE-1, DEL-05-01#REM-1; also DEL-06-06#STATE-1 and DEL-10-01#REM-1 (DEC-019).
4. **Runtime session store contract (3).** SPEC 8.2 subfolders; legacy conversion and bootstrap roots:
   DEL-05-01#CLM-010.2, #CLM-010.3, #CLM-014.2.
5. **SCA-APP-010 presentation versus later direction (4).** Provenance labels removed by the 2026-09-07
   owner direction (DEL-02-02#SEC-3, #REM-1); the v3 workflow library in place of the Workflows contract
   (DEL-02-02#REM-3); both (DEL-02-02#SEC-4).
6. **Ruling-versus-ruling or ruling-versus-TYPES (5).** D-APP-127 account row versus D-APP-108 Q7
   (DEL-02-05#SEC-2.2); ChildRunRecord shape, TYPES §10 versus D-APP-40/D-APP-56 UPD-138 (DEL-08-05 ×3);
   D-APP-112 item B versus the 2026-09-19 session-work-graph direction (DEC:D-APP-112.2).
7. **Event registry drift (3).** hook.failed/hook.progress versus SPEC 9.4 (DEL-06-06#CLM-027, #CLM-030);
   turn.interrupted written for system cancellation versus the D-APP-40 turn.cancelled reservation
   (DEL-03-04#CLM-009.7).
8. **Singletons (2).** App icon: 'no logo' trial direction versus D-APP-108 Q5 (DEL-02-01#REM-7); pec.yaml
   ownership, D-APP-56 R4-P27 versus D-APP-58/SPEC §18 (DEL-10-04#CLM-016.1).

## Hard rows
- **Event rows citing DIRECTIVE §2.10** (DEL-03-01#CLM-004.1, .004.6, .009.2, .009.7; DEL-03-03#CLM-003.6,
  .023.3). Each note frames the conflict as K-ENGINE-4/SPEC §10.3 versus K-EVENT-6/SPEC §11 (R4-Q5). The
  NormativeSource also cites unamended DIRECTIVE §2.10, which R4-Q6 lists. Mapped MULTI. The other reading
  is R4-Q5 alone, if §2.10 is treated as settled by the Q5 answer.
- **R4-Q6 beyond its listed clauses.** Several rows map to R4-Q6 through the "DIRECTIVE-versus-D-GOV-43
  cluster generally" wording, not through a listed clause: DEL-04-05#CLM-009.10 (K-NET-1 remote MCP),
  DEL-06-01 K-PERM-4/K-PERM-5 rows, DOC:RELIANCE#3.4/4.4 (K-PERM-3), SOW:SOW-075.2 (DIRECTIVE
  no-hidden-memory through the unfiltered ~/.codex link), DEL-10-01#REM-1 (DIRECTIVE §8 daemon topology).
  If R4-Q6 is read narrowly (§2.8, §2.10, §4.1, §4.2, K-PERM-1/6 only), these become STAYS_R4.
- **DEL-01-04#CLM-004.5** (PARTIALLY_IMPLEMENTED: conflicts not surfaced). Mapped R4-Q6 because every
  unsurfaced conflict is an R4-Q6 conflict. Other reading: the documentary gap needs no owner answer.
- **DEL-05-01#CLM-010.10** mapped to R4-Q1 (the cell already cited R4-Q1; the A13 posture exists only in
  LEGACY_ONLY code). **DEL-05-01#CLM-010.3** kept plain R4. Its gap is a live-path change (bootstrap
  manifests with no legacy roots, 2f825f180). R4-Q1 alone would not settle it.
- **DEL-02-05#SEC-2.2** kept R4. D-APP-127 versus D-APP-108 Q7 is ruling against ruling. The owner's
  recorded Q6 sequence (Codex first, local models later) bears on it, but Q6 is not framed on App rulings.
- **DEL-09-05 rows** carry R4 only on their signing element. The other elements are STALE_SPECIFICATION.
