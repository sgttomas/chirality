# DEL-06-06 forward ledger notes (rerun, pass 1)

Deliverable: DEL-06-06 Hook Lifecycle and Compaction Mirror (PKG-06), frozen basis `00115c719`.
This is an independent rerun. The original DEL-06-06 folder and `R2/PKG-06/_verify` were not read.

## 1. Census

- Rows: 67. That is 63 unit rows covering all 33 indexed units, plus 4 run-local rows (REGISTER-1, REGISTER-2, STATE-1, STATE-2).
- **By Disposition:**

  | Disposition | Rows |
  |---|---:|
  | STALE_SPECIFICATION | 27 |
  | ALIGNED | 10 |
  | AUTHORITY_CONFLICT | 8 |
  | IMPLEMENTED_DIFFERENTLY | 8 |
  | DOCUMENTED_UNIMPLEMENTED | 4 |
  | NOT_AUDITABLE | 4 |
  | PARTIALLY_IMPLEMENTED | 3 |
  | STALE_VERIFICATION | 2 |
  | REMAINING_STATE_MISMATCH | 1 |

- **By ClaimType:** REQUIREMENT 26, STATE_ASSERTION 23, CONTEXT_CLAIM 12, ACCEPTANCE 4, REGISTER_DEFECT 2.
- **ClaimType × Disposition (main cells):**
  - STATE_ASSERTION: STALE_SPECIFICATION 15.
  - CONTEXT_CLAIM: STALE_SPECIFICATION 8, NOT_AUDITABLE 4.
  - REQUIREMENT: ALIGNED 8, AUTHORITY_CONFLICT 6, IMPLEMENTED_DIFFERENTLY 5, DOCUMENTED_UNIMPLEMENTED 4, STALE_SPECIFICATION 2, PARTIALLY_IMPLEMENTED 1.
  - ACCEPTANCE: STALE_VERIFICATION 2, PARTIALLY_IMPLEMENTED 2.
  - REGISTER_DEFECT: STALE_SPECIFICATION 2.
- **SEE rows, counted separately (16).** These rows carry the Disposition of the row they point to:
  - CLM-008, 016, 023 and 028 point to CLM-001.
  - CLM-010.1, 010.12 and 025.1 point to CLM-004.2.
  - CLM-010.5 and 025.3 point to CLM-003.2.
  - CLM-010.11 points to CLM-004.4.
  - CLM-013 and 021 point to CLM-010.15.
  - CLM-024 points to CLM-009.
  - CLM-025.2 points to CLM-003.1.
  - CLM-025.4 points to CLM-010.9.
  - CLM-025.5 points to CLM-004.5.
- **Census without SEE rows (51 rows):** STALE_SPECIFICATION 20, ALIGNED 8, AUTHORITY_CONFLICT 5, IMPLEMENTED_DIFFERENTLY 5, DOCUMENTED_UNIMPLEMENTED 3, NOT_AUDITABLE 4, PARTIALLY_IMPLEMENTED 3, STALE_VERIFICATION 2, REMAINING_STATE_MISMATCH 1.
- **Split rate: 6 of 33 units (18%).**

  | Unit | Sub-rows | What was split |
  |---|---:|---|
  | CLM-003 | 5 | Attributes table rows |
  | CLM-004 | 7 | Conditions table rows |
  | CLM-010 | 15 | REQ-001..REQ-015 |
  | CLM-015 | 2 | AC-001 and the traceability table |
  | CLM-022 | 2 | VER-001 and the Pass 3 table |
  | CLM-025 | 5 | Numbered principles 1–5 |

  - Every split sub-row names its item in Notes.
  - Index SubItems are AC-001 (CLM-015) and VER-001 (CLM-022). Each got its own `.1` row.
- **Errata:** none. This is pass 1.

## 2. Least-confident rows (with the alternative reading)

No row is marked LOW. The MEDIUM rows most open to a different reading are:

- **CLM-004.2, and SEE rows CLM-010.1, 010.12 and 025.1: IMPLEMENTED_DIFFERENTLY.**
  - *Live path:* persisted types stay inside the Chirality registry. Codex notifications that are not recognised are wrapped as `codex.notification`, and their raw `method` and `params` sit in `data`.
  - *Alternative reading:* this wrapping is the adapter-metadata placement that SPEC 10.3 allows, which would make the rows ALIGNED.
  - *Third reading:* amended K-EVENT-6 ("upstream notifications … preserved") conflicts with SPEC 10.3 "MUST translate", which was not amended, and that would make the rows AUTHORITY_CONFLICT. I did not take this reading, because amended K-EVENT-6 speaks to persistence explicitly.
- **CLM-010.7: IMPLEMENTED_DIFFERENTLY.** Any Codex compaction notification is persisted only as a generic `codex.notification`. The frozen tree contains no Codex protocol schema, so I could not confirm the upstream compaction method name.
  - *Alternative reading:* DOCUMENTED_UNIMPLEMENTED, if Codex emits no compaction notification to this client.
- **CLM-010.4: DOCUMENTED_UNIMPLEMENTED.** The requirement applies "where hook execution evidence is available".
  - *Alternative reading:* if stock Codex exposes no hook evidence, the row is vacuous (ALIGNED or NOT_AUDITABLE).
- **CLM-003.2 / 003.3 / 009 / 010.6 and their SEE rows: AUTHORITY_CONFLICT.**
  - *Alternative reading:* D-GOV-43 item 4 (user-chosen approval and sandbox policy) implicitly retires in-process hooks. Under that reading these rows would be RETIRED/STALE rather than a conflict. I did not choose between the two readings, per §1.
- **CLM-010.10 and CLM-004.5: ALIGNED, relying on D-APP-43 2B.**
  - *Alternative reading:* IMPLEMENTED_DIFFERENTLY, because the SoW text still says "Stop/finalization mapping" and D-APP-43 predates the Codex path.
- **CLM-027 and CLM-030: IMPLEMENTED_DIFFERENTLY (hook.failed).**
  - *Alternative reading:* ALIGNED. On this reading the SoW guidance is about the SPEC 9.4 list, which is still true, and the code registry extension is out of the SoW's scope.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md` hashes do not reproduce.**
  - REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD record `ActualSHA256` equal to the expected hash and a status of MATCH.
  - None of the three reproduces at `00115c719` (`HASH-RECOMPUTE@00115c719`, REFERENCE_HASHES.csv).
  - Disposition: STALE_SPECIFICATION.
  - These rows restate it: CLM-001 (and its SEE rows 008, 016, 023, 028), CLM-003.5, CLM-004.1, CLM-007, CLM-010.14, CLM-011, CLM-018, CLM-032 and CLM-033.
- **REGISTER-2: stale dependency register.**
  - `Dependencies.csv` DEP-06-06-008 is SATISFIED on the strength of the REF-006 MATCH, which no longer reproduces.
  - `_DEPENDENCIES.md:71` still says the paths are TBD, although the SoW now names them.
  - The EvidenceFile columns cite `Specification.md`, `Guidance.md`, `Procedure.md` and `Datasheet.md`. None of these files is in the folder any more.
- **Stale conflict table:** CLM-032 says there is no source conflict, and PRD MATCH. Both assertions are now false.
- **Stale status and carriers:**
  - STATE-2: `_STATUS.md` has an empty Remaining section and was last updated 2026-07-12.
  - `MEMORY.md:7` names the retained SDK mapper as the canonical surface.
  - No D-GOV-43 or D-APP-127 notice reached any DEL-06-06 carrier; all 5 carriers are NO in the pack's application map.
  - STATE-1: `_CONTEXT.md` still describes the daemon and the "Claude Agent SDK first/current path".

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE is the most common: the hook and compaction mirror exists only in the retained Claude SDK harness.
  - DOC_HYGIENE covers the hash drift.
  - PRE_V3_DRIFT covers the Pass 3 TBDs, the SCA-APP-005 re-scope and hook.failed.
  - A2_TOPOLOGY covers the canonical store path and the daemon wording.
  - RUNTIME_EXTRACTION covers redaction lost at the Runtime store.
  - CARRIER_PROPAGATION covers STATE-2.
- **CAUSE2 secondaries:**
  - PRE_V3_DRIFT on the hash rows.
  - RUNTIME_EXTRACTION on CLM-005, 010.15, 012, 015.1 and 020.
  - A2_TOPOLOGY on CLM-004.4, 004.6 and 009.
  - DOC_HYGIENE on the Pass 3 rows and CLM-032.
  - CARRIER_PROPAGATION on CLM-019.
  - CODEX_SOLE_ENGINE on CLM-018 and STATE-1/2.
  - UNRECORDED_JUDGMENT on CLM-027 and 030.
- **Governing records used (GOV:):**
  - D-GOV-43 item 1 (stock App Server), item 2 (faithful transport; the log is never filtered), items 3 and 4 (no configuration veto; user-chosen approval and sandbox), item 5 (compaction and continuity come from the App Server) and item 7 (daemon retirement).
  - CONTRACT K-EVENT-1, K-EVENT-4 and K-EVENT-6 as amended under D-GOV-43.
  - D-APP-43 item 2B: adapter lifecycle mapping is the PreCompact/Stop closure surface. This is applied as MR-11, because the ruling names PreCompact and Stop explicitly.
  - D-APP-38 Option D (versioned corpus).
  - SCA-APP-005 App client boundary (2026-07-27, commit `16f7ed612`).
- **CONTEXT record used:** `R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` DONE-10. It infers that D-GOV-43 item 9 replaced the plan's redaction model. The item 9 text itself says nothing about redaction, and amended K-EVENT-6 keeps redaction before persistence. So the CONTEXT record explains the divergence on CLM-004.4 but does not change its Disposition.
- **Consistency rule applied to one unamended clause.**
  - K-HOOK-1, the SPEC 15.2 fail-closed sentence and the TYPES 8.5 PreToolUse/PostToolUse/Subagent terms are undercut by D-GOV-43 and are not named by it. Every row that restates them is AUTHORITY_CONFLICT with R4-Q1: CLM-003.2, 003.3, 009, 010.5, 010.6, 024 and 025.3.
  - The PreCompact and Stop rows of the same SPEC 15.2 table and TYPES 8.5 are named by D-APP-43. They are therefore judged on the live path under MR-11 in every row that restates them: CLM-004.5, 010.7, 010.8, 010.10, 025.5 and 029.
- **Live-path judgement of REQ-011 / K-EVENT-6.**
  - Redaction exists at the legacy writer (`session-events.ts:17`) and in `tool-result-artifacts.ts`. Neither is on the live path.
  - The live store point (`session-store.ts` appendEvent/persistEvent → `fs.ts` appendJsonLine) has no redaction and no size cap.
  - Upstream of it, the delegated adapter forwards raw Codex `params`. It only truncates `tool.progress` delta to 65,536 characters.
  - There is no `redact` call anywhere in `chirality-runtime/packages/*/src`.
  - Result: DOCUMENTED_UNIMPLEMENTED.
- **Searches behind each NONE_FOUND:**
  - `_DECISIONS/_REGISTER.md` was grepped for compact, hook., K-HOOK, redact and hook.failed. Hits: D-APP-43, D-APP-56 (P04), D-APP-67 and D-APP-99. None explains the relevant divergence.
  - D-GOV-43 (ruling plus proposal items 1–11) and D-APP-127 were grepped for hook, compaction and redaction.
  - The APP_V3_CODEX_HOST_REPLATFORM_20260912 AgentRun was grepped for redaction and compaction. It records redaction only for diagnostics and the desktop log.
  - The done-declaration candidate was grepped for compact, redact and hook.
- **PostReleaseBasis:** NO on every row.
  - `codex-supervisor.ts` lines 545–546, 584–600 and 729–735 blame to `95364569a`, `9eaddb596` and `8b3643e6c`.
  - `session-store.ts` lines 654–669, 813–823 and 1116–1126 blame to `9b005c23a`, `8b3643e6c` and `5c43b3a20`.
  - None of the relied-on lines blames to `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a`.
  - No other cited file is on TOUCHED_PATHS.csv.

## 5. Method friction

- **SEE rows versus earliest-unit placement.** MR-4 puts the full disposition on the earliest unit. For this SoW that is the Datasheet Conditions table (CLM-004) rather than the numbered REQ table (CLM-010), so the REQ rows became SEE rows.
  - Proposed revision: allow the canonical row to be the numbered REQ when an earlier table only paraphrases it.
- **Numbered lists.** The CLM-025 principles list was split as a "table of independently dispositionable rows" so that each principle could show its consistent SEE target.
  - Proposed revision: name numbered lists explicitly in the splitting rule.
- **REACH for validation tooling.** `frontend/scripts/validate-harness-section9.mjs` and its manifest are not product modules. I tagged them REACH=TEST_ONLY.
  - Proposed revision: add an explicit rule for dev and validation scripts.
- **The gate transcripts give suite totals only.** Named test cases were checked for existence in the frozen tree. Their individual pass status is inferred from the whole-suite pass.
- **Unverifiable upstream protocol.** No Codex App Server schema is present in the frozen tree, so claims about which compaction or hook notifications Codex emits cannot be verified statically.

## 6. Effort

- **Deliverable files read:**
  - ScopeOfWork, _STATUS, _CONTEXT, MEMORY, _REFERENCES, _DEPENDENCIES, Dependencies.csv (by script) and Assessment_INSP-03.
  - The `_SEMANTIC*` files, `_run_records` and Evidence_ADQ-11 were not opened. The MEMORY and Assessment summaries of ADQ-11 were sufficient.
- **Code read in line ranges (~10 files):**
  - Runtime: codex-supervisor, delegated-engine-adapter, turn-coordinator, session-store, fs, event-schema and engine-conformance.
  - Legacy frontend: sdk-message-mapper, chirality-hooks, session-events and tool-result-artifacts.
  - Test names were read from 6 test files.
- **Governing and decision texts:** SPEC §8.4–§9.4, §10.3, §15, §19.3; CONTRACT K-rows; TYPES §7.3 and §8.5; the D-APP-43 ruling; D-GOV-43 (ruling and proposal items 1–9); and the register rows.
- **Context budget:** moderate, not tight.
