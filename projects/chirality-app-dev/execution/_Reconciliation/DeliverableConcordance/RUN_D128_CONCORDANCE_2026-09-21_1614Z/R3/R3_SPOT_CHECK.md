# R3 independent spot check — RUN_D128_CONCORDANCE_2026-09-21_1614Z

Three fresh TASK workers (T8A, T8B, T8C; Opus), blind to REMAP_LOG, the run-wide write-ups, the R3 task files and the Notes column, rechecked a deterministic stratified sample of the final concordance against the frozen tree (`_scripts/r3_spot_sample.py`; verdicts in `_work/T8A_VERDICTS.csv`, `T8B_VERDICTS.csv`, `T8C_VERDICTS.csv`; notes in `_work/T8*_NOTES.md`). Verdicts: CONFIRMED, REFUTED, UNVERIFIABLE; the workers also used UNDECIDED where both readings stay defensible (recorded as such, not forced).

<!-- SUMMARY -->
- Items checked: 338 over 271 row-samples — S1 178 rows (5.0% of 3,568, stratified by package × Disposition); S2 65 of 194 AUTHORITY_CONFLICT/UNKNOWN rows (all 40 mandatory + 25 in order; at least 20 required); S3 28 REMAP_LOG entries.
- Totals: CONFIRMED 315, REFUTED 12, UNDECIDED 11, UNVERIFIABLE 0.
- S3 re-mappings: CONFIRMED 29, REFUTED 0, UNDECIDED 1. Refuted items whose checked value came from an R3 re-mapping: 0 → second REMAP_LOG pass reverts 0.
- 12 refutations hit sealed (or errata/corrected) values that R3 did not re-map; they are not changed by R3 and are carried to R4 as contested items (table below).
<!-- /SUMMARY -->

## Counts by sample class

| Class | Rows | CONFIRMED | REFUTED | UNDECIDED | UNVERIFIABLE |
|---|---:|---:|---:|---:|---:|
| S1 stratified ~5% sample (Disposition) | 178 | 168 | 4 | 6 | 0 |
| S2 AUTHORITY_CONFLICT + UNKNOWN rows (Disposition and HDN) | 65 | 118 | 8 | 4 | 0 |
| S3 R3 re-mappings | 28 | 29 | 0 | 1 | 0 |

S1 Disposition refutation rate: 4/178 (2.2%).

## REFUTED items

| Sample | ClaimKey | Field | Checked | Proposed | R3 re-mapped this field? | Handling | Evidence |
|---|---|---|---|---|---|---|---|
| S1-022 | `DEL-02-04#CLM-005.5` | Disposition | DOCUMENTED_UNIMPLEMENTED | PARTIALLY_IMPLEMENTED | NO | CONTESTED → R4 (sealed value kept) | Live projects/chirality-runtime/packages/core/turn-coordinator.ts:179-188 rebuilds opts from known keys with fallbacks (maxTurns ?? 50, persona ?? session.persona, mode chain), so unknown keys do not mutate behaviour and fallback is deterministic; only the war |
| S1-024 | `DEL-02-03#CLM-009.3` | Disposition | IMPLEMENTED_DIFFERENTLY | ALIGNED | NO | CONTESTED → R4 (sealed value kept) | Clearing the root sets projectRoot null (projects/chirality-app-dev/frontend/src/components/workspace/workspace-provider.tsx:115-119, Clear button projects/chirality-app-dev/frontend/src/components/shell/shell-frame.tsx:288); with no projectRoot the composer,  |
| S1-055 | `DEL-04-05#CLM-009.14` | Disposition | IMPLEMENTED_DIFFERENTLY | AUTHORITY_CONFLICT | NO | CONTESTED → R4 (sealed value kept) | RQ-014 restates unamended CONTRACT K-ENGINE-4 (projects/chirality-app-dev/docs/CONTRACT.md:64: HarnessEvent/UIEvent must not become provider-shaped). Amended K-EVENT-1/K-EVENT-6 (:78,:83) under D-GOV-43 require upstream method names and payloads to cross prese |
| S1-112 | `DEL-06-04#CLM-027` | Disposition | STALE_SPECIFICATION | IMPLEMENTED_DIFFERENTLY | NO | CONTESTED → R4 (sealed value kept) | DEL-06-04 ScopeOfWork.md:413 states what the SPEC inventory names, and projects/chirality-app-dev/docs/SPEC.md:814-823 still names status_transition/deps_write as write-gated and scaffold as gated, so no stated fact is false (STALE_SPECIFICATION needs a now-fa |
| S2-009 | `DEL-04-05#CLM-024` | HumanDecisionNeeded | R4-Q1 | R4-Q1; R4-Q6 | NO | CONTESTED → R4 (sealed value kept) | The row turns on App DIRECTIVE s.2.8 versus D-GOV-43, the first clause R4-Q6 names (CONVENTIONS 2.4; RUN_BASIS Addendum 9 lists PKG-04 DEL-04-05). R4-Q1 is right: Claude SDK code is LEGACY_ONLY |
| S2-013 | `DEL-07-01#CLM-011.4` | HumanDecisionNeeded | R4-Q1 | R4-Q1; R4-Q6 | NO | CONTESTED → R4 (sealed value kept) | In workspaceWrite the live sandbox (writableRoots=[cwd]) and project-registry.ts:100-121 keep the instruction root unwritten; the row diverges only through the composer "Full access" option (danger-full-access, projects/chirality-app-dev/frontend/src/component |
| S2-028 | `DEL-06-05#CLM-024` | HumanDecisionNeeded | R4-Q1 | R4-Q1; R4-Q6 | NO | CONTESTED → R4 (sealed value kept) | The row cites K-PERM-6 and its divergence is the live Full access mapping; R4-Q6 names both (CONVENTIONS 2.4). Same deliverable row DEL-06-05#CLM-004.2 carries R4-Q1; R4-Q6 (S3-028) |
| S2-038 | `DEL-02-05#CLM-011.3` | Disposition | AUTHORITY_CONFLICT | ALIGNED | NO | CONTESTED → R4 (sealed value kept) | projects/chirality-app-dev/docs/SPEC.md:693-712 s.11 and projects/chirality-app-dev/docs/TYPES.md s.7.4 are both "Revised under D-GOV-43 (A2)" and keep the eight UIEvent names "as compatibility history", so no unamended text conflicts and the authority is not  |
| S2-038 | `DEL-02-05#CLM-011.3` | HumanDecisionNeeded | R4-Q5 | NO | NO | CONTESTED → R4 (sealed value kept) | R4-Q5 concerns stored payloads under unamended K-ENGINE-4 / SPEC s.10.3, which this row does not cite; no owner question remains |
| S2-043 | `DEL-07-01#CLM-011.6` | HumanDecisionNeeded | R4-Q1 | R4-Q1; R4-Q6 | NO | CONTESTED → R4 (sealed value kept) | "Blocked even when a permissive mode would allow" turns directly on the live Full access option (danger-full-access, projects/chirality-runtime/packages/contracts/src/delegated.ts:318-326; projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx |
| S2-052 | `DEL-02-05#CLM-003.2` | Disposition | AUTHORITY_CONFLICT | ALIGNED | NO | CONTESTED → R4 (sealed value kept) | projects/chirality-app-dev/docs/SPEC.md:693-712 s.11 and projects/chirality-app-dev/docs/TYPES.md s.7.4 are both "Revised under D-GOV-43 (A2)" and keep the eight UIEvent names "as compatibility history". turn:error and process:exit are still produced and consu |
| S2-052 | `DEL-02-05#CLM-003.2` | HumanDecisionNeeded | R4-Q5 | NO | NO | CONTESTED → R4 (sealed value kept) | Row cites only SPEC s.11 and TYPES s.7.4, both amended; R4-Q5 turns on unamended K-ENGINE-4 / SPEC s.10.3 |

## UNDECIDED items (both readings kept; carried to R4)

| Sample | ClaimKey | Field | Checked | Readings / note |
|---|---|---|---|---|
| S1-031 | `DEL-02-02#REGISTER-6` | Disposition | REMAINING_STATE_MISMATCH | REMAINING_STATE_MISMATCH/STALE_SPECIFICATION — projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_DEPENDENCIES.md:14-18 'TBD - no accepted dependency edges have been  |
| S1-035 | `DEL-02-05#CLM-025` | Disposition | STALE_SPECIFICATION | STALE_SPECIFICATION/NOT_AUDITABLE — CONTEXT_CLAIM trade-off (ScopeOfWork.md:460) 'Preserve browser-facing SSE names while runtime internals move behind TurnEngine'. Reading A: implies internals sit behind TurnEngine, now false (turn-engine.ts LEGACY_ONLY; live |
| S1-052 | `DEL-04-01#CLM-024` | Disposition | ALIGNED | ALIGNED/IMPLEMENTED_DIFFERENTLY — Principles of the SDK probe (ScopeOfWork.md:419-440). Reading A (principle level): AgentEnginePort LIVE, probe evidence exists -> ALIGNED. Reading B (product behaviour, rule 2): on the live Codex path upstream method/params ar |
| S1-070 | `DEL-05-03#CLM-010.14` | Disposition | IMPLEMENTED_DIFFERENTLY | IMPLEMENTED_DIFFERENTLY/DOCUMENTED_UNIMPLEMENTED — PEC credential isolation is met only by LEGACY_ONLY modules (projects/chirality-app-dev/frontend/src/lib/harness/mcp/pec-bridge-client.ts). The live Codex path has no PEC transport at all, so no other mechanis |
| S1-076 | `DEL-05-04#CLM-027` | Disposition | STALE_SPECIFICATION | STALE_SPECIFICATION/NOT_AUDITABLE — Conflict table 'None ... during P1/P2' (ScopeOfWork.md:429). Reading A: the table presents open conflicts for ruling, and SPEC 8.2 project-local layout vs amended K-EVENT-4 (projects/chirality-app-dev/docs/CONTRACT.md:81) is |
| S1-172 | `DEL-10-03#CLM-025.2` | Disposition | PARTIALLY_IMPLEMENTED |  — The row's evidence is only that DEL-10-03 ScopeOfWork.md:369 omits 'ready-for-construction' from the projects/chirality-app-dev/docs/CONTRACT.md:152 K-DOMAIN-4 list. Reading 1: a narrower restatement of a governing clause counts as partial coverage (PARTIAL |
| S2-031 | `DEL-09-04#CLM-022` | Disposition | AUTHORITY_CONFLICT | STALE_SPECIFICATION — Reading A: projects/chirality-app-dev/docs/CONTRACT.md:17 (preamble, D-GOV-43) names K-RELEASE-1 ("read with D-GOV-43 items 1 and 4") and states "bundle signing and notarization" apply, so the governing text resolves the point and the SoW |
| S2-031 | `DEL-09-04#CLM-022` | HumanDecisionNeeded | R4 | NO — Follows the Disposition: NO (or D-GOV-43) under reading A; R4 under reading B |
| S2-047 | `DEL-10-04#CLM-016.1` | Disposition | AUTHORITY_CONFLICT |  — Not settled in budget. Reading A: D-APP-56 R4-P27 assigns pec.yaml ownership to DEL-10-04 while PEC-loop commits b1074e7a4/ca49b846d author it under D-APP-70 mapping, a governing disagreement (AUTHORITY_CONFLICT). Reading B: ownership text is a deliverable- |
| S2-059 | `DEL-10-02#CLM-024` | Disposition | AUTHORITY_CONFLICT |  — Reading A: K-DOMAIN-2 hook enforcement exists only in legacy while D-GOV-43 removed Chirality hooks, AUTHORITY_CONFLICT. Reading B: the text is a trade-off for a future implementation; the live path exposes no domain operations, so nothing diverges today (A |
| S3-002 | `DEL-10-01#REM-1` | HumanDecisionNeeded | R4; R4-Q6 | R4 — Row turns on projects/chirality-app-dev/docs/DIRECTIVE.md:320-330 (s.8 per-user daemon, D-GOV-20) versus D-GOV-43 A2. Reading A: s.8 is not among the clauses R4-Q6 names (s.2.8, 2.10, 4.1, 4.2, K-PERM-1/6), so plain R4. Reading B: RUN_BASIS Addendum 9 bro |

## Systematic observations from the checkers

- K-ENGINE-4 restatements that diverge only through D-GOV-43 upstream-event pass-through are dispositioned IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED with R4-Q5 on some rows and AUTHORITY_CONFLICT on others (T8A; bears on CL-05).
- R4-Q6 is applied unevenly to "Full access" and DIRECTIVE §2.8 rows that also cite R4-Q1 (T8C: 4 rows lack R4-Q6; bears on CL-04; T4B listed ~70 adjacent K-ROOT/K-PATH rows it did not move).
- Rule 3 (R4-Q1) is read part-by-part on rows with both LIVE and LEGACY_ONLY evidence; the rulebook does not say whether a claim is judged whole or by part (T8B; 12 sample rows; bears on CL-09).
- The R3 reach re-tags follow the capability files' symbol-level reading and now differ from the evidence pack's module-level REACHABILITY.csv (T8C; recorded in RUNWIDE_CALLS (a)).
- Event-name rows citing only revised SPEC §11 / TYPES §7.4 (DEL-02-05#CLM-011.3, #CLM-003.2) read as ALIGNED to the checker, against sealed AUTHORITY_CONFLICT + R4-Q5.

