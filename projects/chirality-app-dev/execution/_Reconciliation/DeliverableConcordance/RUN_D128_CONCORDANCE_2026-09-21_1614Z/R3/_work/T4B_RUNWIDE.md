# T4B — Run-wide disposition consistency: calls (c), (d), (f)

TASK T4B, R3, RUN_D128. Evidence, not rulings. Remaps: `R3/_work/T4B_REMAPS.csv` (239 records; built by `R3/_work/T4B_scripts/build_remaps.py` against the current R3 concordance cells). Arrows read sealed/current → new. Every row keeps its sealed value in `SealedDisposition`; Notes+ records carry the other reading as `ALSO:`.

## (c) SoW-conversion parity items (AC-001 / VER-001; D-APP-68, D-GOV-16)

**Evidence.**
- Population: a script search of both concordances for AC-001/VER-001/parity/D-APP-68/D-GOV-16 gave 126 hits. Most are functional AC-001/VER-001 rows. 42 rows state the SoW conversion itself: legacy content kept (AC-001) or conversion checks run (VER-001).
- D-GOV-16 (Root `docs/governance_harness/_DECISIONS/`, cited by D-APP-68 disposition 2 as "the conversion authority"), items 7–8. The conversion gate needs validator, map, parity, checklist and render results, plus per-deliverable receipts and verifier returns. These live in the Stage-2 wave run. That run is Root `execution/`, outside the evidence roots.
- App `AgentRuns/SOW-STAGE2-EXEC-20260712-01-C2A*` hold only the frontend runtime activation, not per-deliverable parity.
- D-APP-68 dispositions 1–2 (`D-APP-68_PACKET_CONCORDANCE_RULINGS_2026-07-19.md:58-71`) repair live CLM rows and citations. They do not rule that any parity check was met.
- T4B recomputed line parity from frozen git (`T4B_scripts/parity.py`: non-empty legacy lines, heading and blockquote markers stripped):
  - DEL-00-02: 209/209 lines kept at fae8e5117 and 670a71ed0. 11 lines changed later: 1 by 7fd0466f9 (D-APP-65) and 10 by 03f4e10d8 (D-APP-68, disposition 1 names the PKG-00/01 rows).
  - DEL-05-03: 248/248 lines kept at e9b9e302c and 571e729d1. One line (R14) changed by 03f4e10d8 (D-APP-68 disposition 7 names DEL-05-03).
- Sealed dispositions on the same fact pattern (no conversion record in the App tree): DOCUMENTED_UNIMPLEMENTED ×3; UNKNOWN ×6; PARTIALLY_IMPLEMENTED ×5; ALIGNED ×2.

**Call (one shape, three sub-classes).**
- **C1: AC-001 legacy content.** This is a present-state documentary fact, checkable from git. The row is ALIGNED when traceability holds and parity is kept, allowing changes made under a ruling that names the rows (MR-11). Two sealed UNKNOWN rows had not recomputed parity. T4B did, so they move to ALIGNED.
- **C2: VER-001 conversion checks with no conversion record in the evidence roots.** This is an off-code event, and the only evidence is an absent record, so the row is UNKNOWN + OWNER_CHECK (Addendum 10). The CauseTag is DOC_HYGIENE. Positive partial records stay in Notes: a validator PASS, or parity markers in git history. The human-review half is an open lifecycle gate on IN_PROGRESS deliverables. This is kept as `ALSO:PARTIALLY_IMPLEMENTED`.
- **C2-R: parity reproduced by an R2 worker.** Unchanged: DEL-04-03#CLM-019.2 ALIGNED, DEL-10-03#CLM-022 ALIGNED, DEL-10-02#CLM-019.2 STALE_VERIFICATION (a note is added only).
- One OWNER_CHECK wording is used on every C2 row, so the rows group in `OWNER_CHECK.md`.

**Affected rows.**
- C1:
  - DEL-00-02#CLM-014.2: UNKNOWN → ALIGNED.
  - DEL-05-03#CLM-014.1: UNKNOWN → ALIGNED, CauseTag DOC_HYGIENE → NONE. Its RemainingWork should be NONE_OBSERVED; that field is outside the T4B remap fields, so the manager sets it.
- C2, Disposition changes to UNKNOWN (CauseTag change in brackets):
  - DEL-00-01#CLM-018.2 DOCUMENTED_UNIMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-00-02#CLM-021.2 PARTIALLY_IMPLEMENTED.
  - DEL-01-01#CLM-018 ALIGNED (NONE → DOC_HYGIENE). The Records half holds.
  - DEL-01-02#CLM-038.4 PARTIALLY_IMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-01-03#CLM-022 and DEL-01-04#CLM-020.2 PARTIALLY_IMPLEMENTED (LIFECYCLE_GATE_PENDING → DOC_HYGIENE).
  - DEL-02-01#CLM-023.2 DOCUMENTED_UNIMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
  - DEL-02-05#CLM-020.1 DOCUMENTED_UNIMPLEMENTED (LIFECYCLE_GATE_PENDING → DOC_HYGIENE).
  - DEL-10-01#CLM-022.2 ALIGNED (NONE → DOC_HYGIENE). The sealed ALIGNED rested on a Root record outside the roots.
  - DEL-10-05#CLM-020.1 PARTIALLY_IMPLEMENTED (PRE_V3_DRIFT → DOC_HYGIENE).
- C2, already UNKNOWN:
  - CauseTag only: DEL-02-02#CLM-021.2 (PRE_V3_DRIFT → DOC_HYGIENE).
  - OWNER_CHECK note only: DEL-02-03#CLM-023.2, DEL-02-04#CLM-021.2, DEL-05-03#CLM-020.1, DEL-05-04#CLM-019.2, DEL-10-04#CLM-023.2.
- Notes only, Disposition kept (it stands on other evidence):
  - DEL-03-02#CLM-018 STALE_SPECIFICATION.
  - DEL-05-05#CLM-020.2 STALE_VERIFICATION.
  - DEL-10-02#CLM-019.2 STALE_VERIFICATION.
- Unchanged, outside the class shape:
  - Distinct positive defects: DEL-02-02#CLM-014.2 STALE_SPECIFICATION (SOW-007 trace) and DEL-05-02#CLM-019 STALE_SPECIFICATION (retired kit files in the records list).
  - Mixed functional rows: DEL-06-03#CLM-016 and #CLM-024, DEL-03-03#CLM-013, DEL-01-01#CLM-012.

**Limits.**
- ALIGNED AC-001 rows whose worker checked traceability but not parity were not recomputed:
  - DEL-00-01#CLM-012.2, DEL-01-02#CLM-023.2, DEL-01-03#CLM-013, DEL-01-04#CLM-013.2;
  - DEL-02-01, -03, -04 #CLM-015.2; DEL-02-05#CLM-013.6;
  - DEL-10-04#CLM-016.2, DEL-10-05#CLM-012.1. The same script can confirm them.
- The 0410a15df `decomposition_basis` pin edit touches many converted SoWs. Only DEL-10-02 treats it as invalidating verification (RUN_BASIS §5 known defect). Two readings remain.
- Overlap with T3 (CAND_ADD10): DEL-00-01#CLM-018.2, DEL-01-03#CLM-022, DEL-02-01#CLM-023.2, DEL-02-05#CLM-020.1 and DEL-05-05#CLM-020.2. T4B's class verdict is REMAP_UNKNOWN, except DEL-05-05, which is NOTE_ONLY.

## (d) D-GOV-43 policy rows under R4-Q6

**Evidence.**
- Script search: rows citing K-PERM-1/6, DIRECTIVE §2.8/§2.10/§4.1/§4.2, Full access, `~/.codex`, approval policy, shared config, pass-through or R4-Q6, together with D-GOV-43. This gave 183 rows. Each AUTHORITY_CONFLICT and IMPLEMENTED_DIFFERENTLY row was read for the clause it turns on.
- The App DIRECTIVE clauses are unamended at 00115c719: §2.8 (`DIRECTIVE.md:115-136`: Chirality owns permission semantics and hard-deny precedence; Claude is the key-aware default); §2.10 (:144-148); §4.1 (:227-248: Anthropic access, API key); §4.2 (:250-270: no ambient settings, no shipped `bypassPermissions`, no remote MCP/plugins or bash before governance).
- CONTRACT K-PERM-1 and K-PERM-6 (`CONTRACT.md:90,95`) are unamended.
- D-GOV-43 item 3 shares the user's Codex configuration and resources. Item 4 leaves approval and sandbox policy to the user, including Full access. Neither item names these clauses. The ruling sits outside the §0 order, so the order does not resolve the conflict. Under CONVENTIONS §1 this is AUTHORITY_CONFLICT with R4-Q6.
- The owner's answer (Addendum 9) is context only. It is not applied.

**Call.**
- Every row whose claim restates one of the six R4-Q6 texts, where live code follows D-GOV-43 item 3 or 4, is AUTHORITY_CONFLICT with `R4-Q6` in HumanDecisionNeeded.
- R4-Q1 stays where rule 3 applies, because only LEGACY_ONLY code meets the claim.
- R4-Q5 stays where the row also turns on K-ENGINE-4 against K-EVENT.
- Plain `R4` stays only for the K-PERM-4/K-PERM-5 half, which R4-Q6 does not name.
- ID→AC rows keep `ALSO:IMPLEMENTED_DIFFERENTLY`.

**Affected rows** (sub-cluster: key sealed → new).
- **SC, shared config and resources:**
  - DEL-01-02#CLM-006.7 and #CLM-018.8: AUTHORITY_CONFLICT, HDN `R4-Q1; R4` → `R4-Q1; R4-Q6`.
  - DOC:RELIANCE#3.8 and #4.8, SOW:SOW-045.2: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`.
  - HDN `R4` → `R4-Q6`: SOW:SOW-076; SOW:SOW-075.2 (DIRECTIVE §2.6 via the `~/.codex` memories link); DEL-01-04#CLM-003.1, #CLM-003.4, #CLM-006.1, #CLM-010.2, #CLM-023; DEL-01-04#CLM-004.5 (PARTIALLY_IMPLEMENTED, kept).
- **AP, approval policy and permission ownership:**
  - IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-02#CLM-006.3, #CLM-007.4,
    #CLM-018.10; DEL-06-01#CLM-003, #CLM-009.3, #CLM-024, #CLM-025.
  - DOC:RELIANCE#3.4 and #4.4: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT, HDN `R4` → `R4-Q1; R4-Q6`.
  - DEL-09-03#CLM-005.8 and #CLM-009.9: IMPLEMENTED_DIFFERENTLY → AUTHORITY_CONFLICT (HDN already R4-Q6).
  - AUTHORITY_CONFLICT, HDN `R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-02#CLM-044; DEL-01-03#CLM-024; DEL-06-04#CLM-003,
    #CLM-009.7, #CLM-018, #CLM-022; DEL-06-05#CLM-022, #CLM-004.2; DEL-06-03#CLM-004; DEL-09-02#CLM-010.6; SOW:SOW-050.2.
- **FA, Full access:**
  - AUTHORITY_CONFLICT, HDN `R4; R4-Q1` → `R4-Q1; R4-Q6`: DEL-01-04#CLM-003.5, #CLM-006.2, #CLM-010.4, #CLM-024,
    #CLM-025.
  - DEL-06-01#CLM-009.9: `R4` → `R4-Q1; R4-Q6`.
  - DEL-06-01#CLM-004, #CLM-027, #CLM-031: `R4; R4-Q1` → `R4; R4-Q1; R4-Q6`.
  - DEL-01-04#REGISTER-3 (STALE_SPECIFICATION kept): `R4; R4-Q1` → `R4-Q1; R4-Q6`.
  - DEL-06-01#CLM-032 (STALE_SPECIFICATION kept): `R4` → `R4-Q6`.
- **EV, event pass-through:**
  - These rows cite DIRECTIVE §2.10 as well as K-ENGINE-4, so they turn on R4-Q5 and R4-Q6.
  - DEL-01-01#CLM-009.7, #CLM-021.5, #CLM-023: `R4-Q5; R4-Q1` → `R4-Q1; R4-Q5; R4-Q6`.
  - DEL-03-01#CLM-004.1, #CLM-004.6, #CLM-009.2, #CLM-009.7 and DEL-04-05#CLM-026: `R4` → `R4-Q5; R4-Q6`.
  - Belongs to R4-Q5 only, unchanged: DEL-01-02#CLM-018.5. It turns on K-ENGINE-4 against K-EVENT-1 and cites no DIRECTIVE or K-PERM text. DEL-09-03#CLM-023 already carries both.
- **ED, Claude/Anthropic default and API-key UI (UNDECIDED):**
  - The same statement ("Claude Agent SDK / Anthropic remains the first concrete/current path", "key-aware default") is AUTHORITY_CONFLICT on 11 rows and STALE_SPECIFICATION on 23.
  - Reading A: unamended §2.8, not named by D-GOV-43, gives AUTHORITY_CONFLICT.
  - Reading B: §2.8's own clause "Every other provider or harness path requires a fresh governed tranche", with D-GOV-43 and amended K-ENGINE-3 as that tranche. The §0 order then resolves it, as DEL-04-02#CLM-004 reads.
  - Both readings are defensible. Dispositions are kept, and both readings are recorded in Notes on all 34 rows.
  - HDN on the 11 AUTHORITY_CONFLICT rows:
    - DEL-01-01#STATE-1 and DEL-01-02#STATE-1: `R4-Q1; R4` → `R4-Q1; R4-Q6`.
    - DEL-01-02#CLM-040, DEL-01-04#STATE-2, #STATE-4: `R4; R4-Q1` → `R4-Q1; R4-Q6`.
    - DEL-01-03#STATE-1, #STATE-3 and DEL-04-01#CLM-003: `R4-Q1` → `R4-Q1; R4-Q6`.
    - DEL-02-05#CLM-003.1, #CLM-004.2, #CLM-005.2: `R4` → `R4-Q6`.
  - The 23 STALE_SPECIFICATION rows get Notes only: DEL-03-01#CLM-021; DEL-04-01#STATE-2; DEL-04-02#CLM-004,
    #CLM-023, #STATE-1; DEL-04-04#STATE-1; DEL-04-05#STATE-2; DEL-06-01#STATE-1; DEL-06-02#REGISTER-4; DEL-06-03#STATE-1; DEL-06-04#STATE-1; DEL-06-05#REGISTER-5; DEL-09-01..03#STATE-1; DEL-09-04#REGISTER-52; DEL-09-05#REGISTER-55; DEL-09-06#STATE-1; DEL-10-01..05 STATE/REGISTER rows.
- **Adjacent, not R4-Q6** (no change; they turn on clauses R4-Q6 does not name, mostly R4-Q1 or an unframed K-PERM-3/4/5 or K-BASH-1 question):
  - DEL-06-01#CLM-009.1, .2, .4, .5, .6, .7, .12, .15, #CLM-005, #CLM-019, #CLM-028;
  - DEL-06-02#CLM-010.11;
  - DEL-06-04#CLM-004.2, .004.3, .008, .009.1–.009.4, .009.6, .009.8, .009.9, .009.13, .013, .025, .029, .030;
  - DEL-06-05#CLM-003, .005, .008, .009.1–.009.5, .009.12, .009.13, .013, .018, .024, .026, .029;
  - DEL-07-01#CLM-011.4–.011.7 (K-ROOT/K-PATH; .011.6 is Full access through K-ROOT-2), .011.9, .024;
  - DEL-01-02#CLM-006.4, .006.6, .006.10, .013; DEL-01-03#CLM-009.7 (K-RELIANCE-2/§2.9); DOC:RELIANCE#3.5, #4.5,
    #3.11, #4.11; DOC:ADDING_A_TOOL#3; SOW:SOW-027.2, SOW-060.2;
  - DEL-04-02#CLM-009 (a Claude builder scope statement).
- DEL-01-04#CLM-010.3 stays ALIGNED. It names only `~/.claude` files, which live code does not load. Its sibling CLM-023 carries the conflict.

**Limits.**
- 43 of these keys are also in CAND_R4PLAIN (T1). The manager should reconcile T1's R4→R4-Qn mapping with the values above.
- The ID→AC change on 14 rows follows the brief's normalisation. The sealed readings ("authority route: none; the tension is R4-Q1") stay as `ALSO:`.
- The ED split is not resolved. The R4-Q6 packet should include both populations.

## (f) DEL-09-04 / DEL-09-05 release-signing cluster (framed, not resolved)

**Evidence.**
- Reading 1, STALE_SPECIFICATION (MR-11 through §0):
  - The amended CONTRACT preamble (`CONTRACT.md:17`, 23b3879b3) names K-RELEASE-1 and reads it with D-GOV-43 items 1 and 4. It lists bundle signing and notarization as ordinary integrity.
  - SPEC §19.4 and PRD §7.12/§12.8/NFR-030 name a signed, notarized candidate.
  - K-RELEASE-1 itself says "unless amended" (:138).
  - PRD §6.2 (:339-346) is below CONTRACT and SPEC in the §0 order.
  - V-DEL-09-04 REFUTED the AUTHORITY_CONFLICT reading on CLM-022 and CLM-023.3.
- Reading 2, AUTHORITY_CONFLICT:
  - The K-RELEASE-1 row text and PRD §6.2 are unamended.
  - D-APP-97 (`D-APP-97_RULING_RELEASE_PREPARATION_2026-08-17.md:20`) keeps the F-APP-2 fence on signing, notarization and distribution, and no ruling names F-APP-2 as lifted.
  - The decomposition v3_2 DEL-09-05 row keeps the G6a exact-candidate gate, and D-APP-127 does not name G6a.
  - V-DEL-09-05 graded CLM-026 CONTESTED.
- Done-declaration Q-02 is context only.
- **Question for the owner:** does the amended CONTRACT preamble (with SPEC §19.4 and PRD §12.8) supersede the unsigned/unnotarized target, the F-APP-2 signing fence and the G6a gate for DEL-09-04 and DEL-09-05?

**Call.**
- The rows below form one cluster, marked by Notes+ `R3_CLUSTER:RELEASE_SIGNING`. Dispositions are unchanged.
- MR-11 consistency: DEL-09-04#CLM-022 and #CLM-023.3 are AUTHORITY_CONFLICT but carry `NO`. PKG-09 CORRECTIONS applied only the HumanDecisionNeeded half of V-DEL-09-04's REFUTED verdict.
- The consistent value while the Disposition stands is `R4`. No named question fits: this is not R4-Q6, because K-RELEASE-1 is not a DIRECTIVE or K-PERM text.
- If the manager instead applies the Disposition half of that verdict (STALE_SPECIFICATION), `NO` becomes consistent. That is outside T4B's brief.
- DEL-09-05#REM-2 is REMAINING_STATE_MISMATCH with `NO`, which is consistent. It gets the marker only.

**Affected rows** (all Notes+ `R3_CLUSTER:RELEASE_SIGNING`).
- DEL-09-04:
  - CLM-003.1, 004.3, 008, 009.1, 011.6, 012.2: STALE_SPECIFICATION/NO.
  - CLM-016: IMPLEMENTED_DIFFERENTLY/R4. CLM-017: PARTIALLY_IMPLEMENTED/R4.
  - CLM-022 and CLM-023.3: AUTHORITY_CONFLICT, HDN **NO → R4**.
- DEL-09-05:
  - STATE-1, CLM-003, 009, 010.6, 010.7, 012, 013: STALE_SPECIFICATION/NO.
  - CLM-016.3: AUTHORITY_CONFLICT/R4 (G6a). CLM-016.6: PARTIALLY_IMPLEMENTED/R4.
  - CLM-020 and 023.2: STALE_SPECIFICATION/R4. CLM-026: AUTHORITY_CONFLICT/R4.
  - REM-2: REMAINING_STATE_MISMATCH/NO. REGISTER-52: STALE_SPECIFICATION/NO (G6a, `MOOT:D-APP-127`). STATE-52: STALE_SPECIFICATION/NO.
- EXT: SOW:SOW-072 ALIGNED/NO. It reads the unsigned target as unamended, which is a third disposition of the same text. DOC:BUILDREL#4.14 and #11: STALE_SPECIFICATION/NO.

**Limits.**
- DOC:BUILDREL#10.8 (ALIGNED: "current ordinary output is unsigned") and DEL-09-05#CLM-016.2 are not marked. They describe build output or the phase boundary and do not turn on the question.
- Several cluster rows are also T3 Addendum 10 candidates (signing and notarization events), for example DEL-09-05#CLM-026 and #CLM-016.3.
- The owner's statement that v3.0.1 was notarized is not applied.
- Outside the three calls: DEL-06-04#STATE-2 is also AUTHORITY_CONFLICT with `NO` (from CORRECTION). This breaks the same MR-11 rule, and the manager should check it.
