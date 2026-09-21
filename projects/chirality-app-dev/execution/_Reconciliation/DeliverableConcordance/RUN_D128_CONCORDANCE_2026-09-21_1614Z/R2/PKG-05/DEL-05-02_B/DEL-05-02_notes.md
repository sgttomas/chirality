# DEL-05-02 notes (worker B, pass 1)

- Run: `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-05 wave 2. This is an independent double-audit copy.
- Sealed ledger: `DEL-05-02_claims.csv`, 52 rows. Validator: `RESULT PASS errors=0 warnings=0`.
- Claims SHA-256 at seal: `801c5e9cab8575fc130b01ca3139637c9036e6ab2205cfc9292c2f7fd8c8ccd5`.

## 1. Census

- **Coverage.** All 33 indexed units are covered: SEC-1..3, CLM-001..028 and REM-1..2.
- **Run-local rows (5).** REGISTER-1..4 and STATE-1.
- **Split.** One unit was split: CLM-010, the requirements table, became `.1`..`.15`, one row per DEL-05-02-RQ-0nn. That is 1 of 33 units (3.0%) and 15 of 52 rows.
- **Sub-items.** CLM-013 (AC-001) and CLM-019 (VER-001) each list one sub-item, so neither was split. Both name their item in Notes.

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 28 | 10 |
| ALIGNED | 11 | 0 |
| PARTIALLY_IMPLEMENTED | 7 | 1 (CLM-018) |
| DOCUMENTED_UNIMPLEMENTED | 2 | 0 |
| REMAINING_STATE_MISMATCH | 2 | 0 |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 |
| NOT_AUDITABLE | 1 | 0 |
| **Total** | **52** | **10** |

Correction: the SEE count for STALE_SPECIFICATION is 9, not 10. The 10 rows carrying `SEE:` are:

- CLM-001, which points to REGISTER-1 and is also the primary for CLM-008 and CLM-020;
- CLM-008, CLM-015, CLM-018, CLM-020, CLM-021, CLM-025, CLM-027, REGISTER-4 and STATE-1.

CLM-018 is PARTIALLY_IMPLEMENTED, so the STALE_SPECIFICATION SEE rows are 9 and the PARTIALLY_IMPLEMENTED SEE row is 1.

**Rows by ClaimType:** REQUIREMENT 25, CONTEXT_CLAIM 9, STATE_ASSERTION 7, ACCEPTANCE 5, REGISTER_DEFECT 4, REMAINING_WORK 2.

**Cross-tab of ClaimType by Disposition:**

- REQUIREMENT: ALIGNED 11, STALE_SPECIFICATION 8, PARTIALLY_IMPLEMENTED 4, DOCUMENTED_UNIMPLEMENTED 1, IMPLEMENTED_DIFFERENTLY 1.
- CONTEXT_CLAIM: STALE_SPECIFICATION 8, NOT_AUDITABLE 1.
- STATE_ASSERTION: STALE_SPECIFICATION 7.
- ACCEPTANCE: PARTIALLY_IMPLEMENTED 3, STALE_SPECIFICATION 2.
- REGISTER_DEFECT: STALE_SPECIFICATION 3, REMAINING_STATE_MISMATCH 1.
- REMAINING_WORK: REMAINING_STATE_MISMATCH 1, DOCUMENTED_UNIMPLEMENTED 1.

**Confidence:** HIGH 18, MEDIUM 31, LOW 3. There is no errata file; this is the sealed pass only.

## 2. Least-confident rows

- **CLM-007 and CLM-027 (LOW).** These are the P45 reconciliation note: "UPD-124 replaces provider-shaped kit wording …; 11 ACTIVE / 1 RETIRED".
  - Scored as STALE_SPECIFICATION because the SoW still carries `sdk.system.init` and `sdk.mirror.error`. The legacy Datasheet also still had `sdk.system.init` when it was deleted (`0da38db4d^`).
  - Alternative reading: a dated note recording an act on the legacy kit. That would make it NOT_AUDITABLE, or a REGISTER row under MR-8(iv).
- **CLM-010.3 (LOW), RQ-003 "schemaVersion 1".** Scored as ALIGNED against SPEC §9.1 and the code (`event-schema.ts:57`, `session-store.ts:661/711/814`).
  - Alternative reading: CONTRACT K-EVENT-4, as amended and ranking above SPEC under DIRECTIVE §0, names the canonical store's event schema `chirality.event/v1`.
  - Only the UNREACHED `contracts/src/events.ts` `RuntimeEvent` carries that identifier. Read that way, the row is STALE_SPECIFICATION, or an AUTHORITY_CONFLICT if the K-EVENT-4 label is meant as a real schema.
- **REM-1 (MEDIUM).** Scored REMAINING_STATE_MISMATCH with MechanicallyUnblocked YES.
  - The gate's premise is on the production path:
    - `delegated-engine-adapter.ts:255-289` passes `codex.notification` through, with `tool.*` and `turn.started` views;
    - the App consumes it (`harness-event-views.ts:451-458`, `transcript-replay.ts`).
  - Alternative reading: the gate means "D-GOV-43 item 2 accepted as complete", which is a status no App surface records. That gives UNKNOWN, and the item stays DOCUMENTED_UNIMPLEMENTED.
- **CLM-010.12 (MEDIUM, R4).** Scored IMPLEMENTED_DIFFERENTLY: `codex.*` types sit in the canonical HarnessEvent vocabulary, while K-CORE-1 and K-ENGINE-4 are unamended.
  - Alternative reading: AUTHORITY_CONFLICT, if D-GOV-43's upstream-preservation rule (K-EVENT-1/6) is read as requiring provider-named types.
- **CLM-001 (MEDIUM).** The P40 note is dated 2026-07-12 but says "is MATCH". It was treated as current-tense restatement under tie-break 3, with a SEE to REGISTER-1. The alternative is a dated snapshot, which would be REGISTER-only.

## 3. Register-defect summary

- **REGISTER-1.** In `_REFERENCES.md`, the recorded MATCH hashes for CONTRACT, SPEC and PRD do not reproduce. The evidence is `HASH-RECOMPUTE@00115c719`, from REFERENCE_HASHES.csv (3 rows with Match=NO).
  - My own recompute shows the other hashes still match: DIRECTIVE, TYPES, PLAN and the three `workflows/software-decomp` files.
- **REGISTER-2.** `_REFERENCES.md` reuses REF-009 and REF-010 for two different sources each. This is bookkeeping and scored REMAINING_STATE_MISMATCH.
- **REGISTER-3.** Dependencies.csv and _DEPENDENCIES.md keep DEP-05-02-013 (Root closed schema v2) and DEP-05-02-015 (Root DEL-02-10 acceptance, PREREQUISITE, PENDING) ACTIVE.
  - D-APP-127 retired the closed event vocabulary.
  - K-EVENT-3 as amended retires the closed v2 union.
  - `_STATUS` V3-02 says no Root acceptance is awaited.
- **REGISTER-4.** `_CONTEXT.md` Deliverable Scope and Anticipated Artifacts still say "Root-owned daemon" and "once Root accepts them". The D-APP-127 application map has `_CONTEXT` = NO. This row is a SEE to SEC-1.
- **Also observed, not rowed:**
  - The MEMORY.md 2026-09-05 note "`Dependencies.csv` is current with the applied row L337" is dated history. It is now overtaken by D-APP-127.
  - The `_STATUS.md` REM-1 Trace cites decomposition row L323. The SoW and the dependency notes use L337; L323 is the pre-amendment number. This is recorded in REM-1's Notes.

## 4. Direction and cause

- **Main CauseTags:**
  - DOC_HYGIENE 13: reference hashes, PRD notes, conflict table, records list.
  - RUNTIME_EXTRACTION 12: schema, writer and replay moved into `projects/chirality-runtime`, and the App's redacting writer and artifact store were left on the legacy path.
  - CARRIER_PROPAGATION 8: D-APP-127 names DEL-05-02, but only `_STATUS.md` was revised.
  - A2_TOPOLOGY 4: the canonical path moved to the Runtime user-data store per K-EVENT-4.
  - One each: CODEX_SOLE_ENGINE, FACADE_DEPRECATION, LIFECYCLE_GATE_PENDING.
- **Secondary causes:** CAUSE2:A2_TOPOLOGY (SEC-1, SEC-2, CLM-028, REGISTER-4); CAUSE2:CARRIER_PROPAGATION (CLM-003, CLM-009, REM-2); CAUSE2:RUNTIME_EXTRACTION (CLM-010.14, CLM-017); CAUSE2:CREDENTIAL_CUSTODY (CLM-010.9); CAUSE2:CODEX_SOLE_ENGINE (CLM-010.10, CLM-022, REM-1); CAUSE2:PRE_V3_DRIFT (CLM-007).
- **GOVERNING records used:**
  - D-APP-127, which names "PKG-05 DEL-05-02 architecture-bound clauses revised" at line 183;
  - D-APP-108 and D-APP-109;
  - CONTRACT K-EVENT-1, -3, -4 and -6 as amended under D-GOV-43.
- **CONTEXT records used:** `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/SPIKE_DESIGN.md` §6. It records the `codex.notification`/`codex.request` types and raw params carried under `data.codex`. I also read HANDOFF.md ("Event representation (clarified)").
- **Searches behind NONE_FOUND:**
  - I grepped `execution/_Coordination/_DECISIONS/_REGISTER.md` for DEL-05-02, redact, K-EVENT-6, events.jsonl and artifact.
  - I grepped the APP_V3_CODEX_HOST_REPLATFORM_20260912 CONTEXT records (HANDOFF, SPIKE_DESIGN, INDEPENDENT_REVIEW, spike W1–W3 returns) for redact and codex.notification. The only redaction they record is e-mail masking of app-server stderr and the desktop log.
  - Neither search found a record explaining why structural redaction before the Runtime persistence sink is absent (CLM-004, CLM-005, CLM-010.9, CLM-012), or why large payloads are not offloaded to artifacts.
  - For the PRD and reference rows, no ruling re-pins the hashes after D-APP-38.
- **Key live-path facts at 00115c719:**
  - Writer: Runtime `SessionStore.appendEvent` and `persistEvent` (`session-store.ts:655-668`, `813-822`) write through `appendJsonLine` (`fs.ts:24-34`) with no redaction. The events file is `<runtimeDirectory>/projects/<projectId>/sessions/<sessionId>/events.jsonl` (`:1111-1127`).
  - Replay counts and skips any malformed line, not only the tail (`:864-904`), and also accepts schemaVersion 2.
  - Turn lifecycle: `turn.accepted` is persisted before `engine.startTurn` (`turn-coordinator.ts:227-234`), and exactly one terminal is persisted (`:271`, `:393-411`, `:441-449`).
  - The legacy App writer `frontend/src/lib/harness/session-events.ts` (which redacts) is LEGACY_ONLY. The App malformed-tail route test runs through the fake daemon port over that legacy reader.
- **PostReleaseBasis.**
  - `session-store.ts` is in TOUCHED_PATHS (da95ec194, lines 6-8 and 128-158). `git blame -L` on each relied-on range (655-668, 673-750, 813-822, 864-904, 1112-1127) attributes every line to `9b005c23a` or `8b3643e6c`, so PostReleaseBasis is NO.
  - No other cited file is touched.

## 5. Method friction

- **SEC-level supersession clause.** The SoW's SEC preamble says that where older clauses disagree with the applied row, they "remain dated compatibility history".
  - Read literally, this pre-empts STALE_SPECIFICATION for every older clause that conflicts with SEC-1.
  - I scored the older clauses by their content, because they are unmarked and read as current.
  - Proposal: CONVENTIONS should say whether an agent-authored in-document supersession preamble counts as "text acknowledging" the change (MR-8 ii). As I read it, it cannot, because it is not a GOVERNING ruling.
- **Gates phrased as "lands on the production path" (REM-1).** MR-6 lets App code count, but here the gate's subject is a Root/Runtime representation plus App consumers.
  - Proposal: state whether packaged Runtime code at the frozen basis counts as the "production path" for such gates.
- **CONTRACT K-EVENT-4's schema identifier.** It names `chirality.event/v1`, which diverges from SPEC §9.1 and the live writer. This is a governing-document versus code finding that no deliverable unit owns cleanly. It is noted on CLM-010.3; R3/R4 may want it as a named question.
- **SEE on a primary row.** SEE on a row that is itself a SEE target (CLM-001 → REGISTER-1, with CLM-008 and CLM-020 → CLM-001) validates, but it makes the separate census of SEE rows ambiguous. I counted such a row as a SEE row.

## 6. Coverage gaps

- **Output matrix parity report.** The SoW "Output and Evaluation Matrix" (OUT-001 → AC-001, VER-001) expects a "claim map, parity report". No such artifact was found in the folder. This is covered by CLM-013 and CLM-019, not by a separate row.
- **Runtime-only replay tolerance.** The Runtime `replayDetailedUnlocked` malformed-line handling has no Runtime test (grep of `projects/chirality-runtime/tests` for malformed replay). This is noted on CLM-010.8.

## 6a. Addendum 6 notice (R4-Q1 legacy-versus-live subject test)

The notice (`BRIEFS/RULE_NOTICE_ADDENDUM6.md`) arrived **after** the ledger was sealed, so the ledger is unchanged. For R3, these are the rows the rule would have touched:

- **CLM-010.9 (RQ-009 secret exclusion).** This is product behaviour, a redaction guarantee. The only code that meets it is the legacy redacting writer `session-events.ts` (REACH=LEGACY_ONLY).
  - Under the rule, HumanDecisionNeeded would be `R4-Q1`, and the row would add `ALSO_MODULE:ALIGNED` (the legacy module redacts).
- **CLM-010.10 (RQ-010 large payloads as artifacts).** This is product behaviour. The only code that meets it is the legacy `tool-result-artifacts.ts` (REACH=LEGACY_ONLY).
  - Under the rule: `R4-Q1`, plus `ALSO_MODULE:PARTIALLY_IMPLEMENTED`, matching INSP-03's PARTIAL.
- **Partial matches.** CLM-004, CLM-005, CLM-012, CLM-018 and CLM-022 are met partly by LIVE code, and their secret/artifact portion only by legacy code.
  - Whether the row-level R4-Q1 citation applies depends on reading "the only code meeting the claim" per portion. At row level, LIVE code meets part of each claim, so strictly R4-Q1 does not apply.

## 7. Effort

- **Deliverable files read:** ScopeOfWork, _STATUS, _CONTEXT, MEMORY, _REFERENCES, Dependencies.csv (by script), _DEPENDENCIES.md (grep), Assessment INSP-03, and run-record headers.
- **Governing and CONTEXT records read:** D-APP-127, SPEC §8–§10, CONTRACT K-EVENT and K-CORE/K-ENGINE/K-KEY rows, and CONTEXT SPIKE_DESIGN §6 and HANDOFF excerpts.
- **Code, by range:** about 12 Runtime/App files, with about 25 grep passes. Git was limited to `log`, `show` and `blame -L` against the frozen tree.
- **Context budget:** moderate, not tight.
