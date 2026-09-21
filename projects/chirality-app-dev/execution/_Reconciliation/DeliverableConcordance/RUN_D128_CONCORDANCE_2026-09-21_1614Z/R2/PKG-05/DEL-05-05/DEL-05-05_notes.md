# DEL-05-05 ToolResultStore and Session Artifacts: forward-pass notes (R2, PKG-05)

Basis: frozen tree `00115c719`. Ledger: `DEL-05-05_claims.csv`, 60 rows, validator PASS (0 errors, 0 warnings).
RUN_BASIS Addendum 7 (R4-Q5) arrived **before sealing** and is applied.

## 1. Census

Indexed units: 33 (CLM-001..CLM-032, REM-1). Run-local rows: REGISTER-1..3, STATE-1.

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 14 | 7 (CLM-013, 020.1 → CLM-005; CLM-006, 007, 017, 025, 032 → REGISTER-1) |
| STALE_VERIFICATION | 12 | 1 (CLM-012.9 → CLM-010.14) |
| PARTIALLY_IMPLEMENTED | 9 | 0 |
| DOCUMENTED_UNIMPLEMENTED | 8 | 3 (CLM-018, 027 → CLM-010.2; CLM-028 → CLM-010.7) |
| ALIGNED | 7 | 1 (CLM-029 → CLM-010.9) |
| NOT_AUDITABLE | 7 | 0 |
| IMPLEMENTED_DIFFERENTLY | 2 | 0 |
| REMAINING_STATE_MISMATCH | 1 | 0 |
| **Total** | **60** | **12** |

By ClaimType: REQUIREMENT 36, CONTEXT_CLAIM 10, STATE_ASSERTION 8, REGISTER_DEFECT 3, ACCEPTANCE 2,
REMAINING_WORK 1.

Split rate: 4 of 33 indexed units were split (12%), giving 27 sub-rows. CLM-010 has 14 rows, one per REQ-001..014
(the table of independently dispositionable requirements). CLM-012 has 9 rows, one per the SubItems it lists.
CLM-014 has 2 rows (partition note, AC-001). CLM-020 has 2 rows (Records, VER-001).

HumanDecisionNeeded: R4-Q1 on 33 rows (5 of them also R4-Q5, 2 also D-APP-116); D-APP-116 alone on REM-1; NO on 26.
No errata file (pass 1).

## 2. Least-confident rows

No LOW rows. The MEDIUM rows most open to another reading:

- **CLM-010.8 / CLM-010.9 (ALIGNED).** The live Runtime replay tolerates malformed lines, and events are appended in
  order under a per-session lock. No Runtime test covers either behaviour; the cited App tests exercise the legacy store.
  Alternative: `STALE_VERIFICATION`. I kept the implementation verdict ALIGNED and put the verification gap on CLM-012.5 and CLM-012.6.
- **CLM-010.4, CLM-022 (IMPLEMENTED_DIFFERENTLY).** The live path bounds persisted fields by fixed truncation (512-char
  summaries, 64 KiB `tool.progress` deltas) instead of using descriptor budget classes. Alternative: `DOCUMENTED_UNIMPLEMENTED`,
  on the reading that truncation is not a budget policy at all. Both rows also turn on R4-Q5 (payload stored as received or translated).
- **CLM-010.6 (PARTIALLY_IMPLEMENTED).** Only diagnostic e-mail redaction exists on the live path (the Codex stderr path and
  `electron/desktop-log.ts`). Alternative: `DOCUMENTED_UNIMPLEMENTED`, on the reading that e-mail scrubbing of diagnostics is not
  the secret redaction REQ-006 means. Amended CONTRACT K-EVENT-6 still requires structural redaction before persistence, so this is not an AUTHORITY_CONFLICT.
- **CLM-010.11 (ALIGNED, R4-Q1).** Judged at module level because the claim names `ToolResultStore` and describes only its
  interface. Alternative: a product-behaviour reading, which would make it DOCUMENTED_UNIMPLEMENTED on the live path.
- **STATE-1 (PARTIALLY_IMPLEMENTED).** The live App preview consumer exists; the Runtime producer that the governing scope
  presumes does not. Alternative: `STALE_SPECIFICATION`, if "daemon-managed" is read as a now-false fact rather than as scope.

## 3. Register-defect summary

- **REGISTER-1.** In `_REFERENCES.md`, the MATCH hashes for REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD do not
  reproduce (`HASH-RECOMPUTE@00115c719`). DIRECTIVE, TYPES, PLAN and the three software-decomp workflow files do reproduce.
  CLM-006, 007, 017, 025 and 032 restate MATCH as current and cite REGISTER-1 with SEE.
- **REGISTER-2.** In `Dependencies.csv` / `_DEPENDENCIES.md`, rows DEP-006/007/008 are SATISFIED on MATCH verdicts that no
  longer reproduce. DEP-009 is SATISFIED on an implementation path that is legacy-only. The EvidenceFile `Procedure.md` no
  longer exists. The SOW-053/059 statements predate their SCA-APP-005 wording.
- **REGISTER-3.** The SoW `decomposition_basis` pin (`7b0be4d87`) is older than the SCA-APP-005 change to decomposition
  row 340 (`16f7ed612`). This is bookkeeping lag. SCA-APP-005 explicitly left the pins unchanged.
- Other stale metadata, recorded inside rows rather than as separate register rows:
  - CLM-006 C-001 cites `Specification.md` and `Procedure.md`, which do not exist.
  - The SoW REF-007 (`AGENT_SOFTWARE_DECOMP.md`) differs from `_REFERENCES.md` REF-007.
  - CLM-026 cites a threshold path that is now a two-line `@deprecated` re-export facade.
- D-APP-127 application map: every DEL-05-05 carrier is `NO`. D-APP-127 does not name DEL-05-05, so this is not itself a
  defect; it is noted on STATE-1.

## 4. Direction and cause

- **Main finding.** The artifact store the SoW describes is App-owned and implemented in
  `frontend/src/lib/harness/tool-result-artifacts.ts` + `tool-evidence.ts` + `session-events.ts`. All three modules are
  `REACH=LEGACY_ONLY`, and every caller is Claude SDK/Pi-path code. On the live Codex path
  (`delegated-engine-adapter.ts` → `turn-coordinator.ts` → `SessionStore.persistEvent`), no tool result is budgeted,
  previewed as an artifact, checksummed or redacted before persistence. Command output is persisted inline as
  `tool.progress` deltas of up to 64 KiB each. The live App consumer (`transcript-replay.ts` → `transcript-stream-view.tsx`)
  can display `artifactMetadata`, but nothing on the live path produces it.
- **Scope drift.** Accepted SCA-APP-005 (2026-07-27) re-bounded DEL-05-05 to App consumption and preview of Runtime-owned
  outputs (decomposition :340, SOW-053/059, `_CONTEXT.md`). It left the SoW (finalized 2026-07-14) unchanged. MR-11 applied on CLM-009.
- **Amended CONTRACT.** K-EVENT-4 now names `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl`
  as canonical and `.chirality/sessions` as a legacy source. The live code matches, so CLM-010.1 is `STALE_SPECIFICATION`.
  K-EVENT-6 (amended) still requires structural redaction before every sink; the live path does not do this (CLM-010.6/7, CLM-028).
- **CauseTags.**
  - Primary: CODEX_SOLE_ENGINE 34, DOC_HYGIENE 8, RUNTIME_EXTRACTION 2, A2_TOPOLOGY 1, FACADE_DEPRECATION 1.
  - Secondaries: CAUSE2:RUNTIME_EXTRACTION (most CODEX rows), A2_TOPOLOGY, CREDENTIAL_CUSTODY, FACADE_DEPRECATION and PRE_V3_DRIFT (SCA-APP-005-era drift).
- **Records used.**
  - `GOV:D-GOV-43`.
  - `GOV:SCA-APP-005` (Amendment_Preview.md:28-31, Propagation_Plan.md:19-21). SCA-APP-005 has no D-ID, so LatestDecision is NONE_FOUND there.
  - RULING-RECORD D-APP-68 (CLM-014.1) and D-APP-102 (REM-1).
  - The done-declaration candidate DONE-10 was considered and not relied on: amended K-EVENT-6 keeps redaction.
- **NONE_FOUND searches.** These rows are CLM-006, 007, 017, 025, 032 and REGISTER-1. I searched
  `execution/_Coordination/_DECISIONS/_REGISTER.md` (D-APP-38, 42, 48, 56, 68, 102, 116, 127). I also searched the CONTEXT
  sources: the done-declaration candidate, `plans/steers`, the v3 execution plan, and the AgentRuns `APP_V3_CODEX_HOST_REPLATFORM_20260912`.
  No record explains the reference-hash drift or the missing Specification/Procedure files. RUN_BASIS §5 lists the corpus
  drift as a known basis defect.
- **PostReleaseBasis.** The only cited file on TOUCHED_PATHS is `projects/chirality-runtime/packages/core/src/session-store.ts`.
  Its touched ranges are 6-8 and 128-158. `git blame -L` on the relied-on lines (654-668, 810-824, 848-895) attributes them to
  `8b3643e6c` / `9b005c23a`, so every row is `NO`.
- **R4-Q5 rows.** CLM-010.2, 010.4, 022, 023 and 027. Each turns on whether Codex payloads are stored as received (large
  output in the event log) or translated and budgeted.

### Coverage gaps (no forward row owned)

- **Live producer.** No live Runtime tool-result artifact producer exists, although K-EVENT-7 (`ToolResultStore`) and SPEC 9.2
  still require one. `_STATUS.md` Remaining records only the D-APP-116 full-policy packet, not this base residual. Ownership
  after SCA-APP-005 is Runtime (Root). DEL-05-05 would own only the App consumption and conformance side.
- **Unredacted tool output.** `codex.notification` events persist full upstream `params` for non-tool items, and
  `tool.progress` persists raw output. This is a K-EVENT-6 sink-redaction gap shared with DEL-05-02 (event persistence) and DEL-05-03 (redaction).

## 5. Method friction

- **Tier for a D-APP-only restatement.** AuthorityTier has no class for a restatement of a D-APP ruling only (not D-GOV).
  I used LOCAL_DESIGN. Proposal: say explicitly that D-APP rulings tier as LOCAL_DESIGN unless they restate CONTRACT/SPEC.
- **SCA LatestDecision.** An accepted SCA is GOVERNING but has no D-ID, so `LatestDecision` must be NONE_FOUND even when
  MR-11 applies. Proposal: allow `SCA-APP-nnn` in LatestDecision.
- **Verification-plan rows.** CLM-012 splits by SubItems (the first REQ of each verification row), but each row verifies a
  group of REQs. Naming "(with REQ-002, REQ-003)" in Notes worked, but the index would be clearer if it listed the grouped IDs.
- **Mid-pass Addendum 7.** It arrived before sealing. It meant re-reading the amended CONTRACT, which changed CLM-010.1
  (IMPLEMENTED_DIFFERENTLY to STALE_SPECIFICATION) and removed an AUTHORITY_CONFLICT alternative on CLM-010.6.
  Suggestion: evidence packs should flag clauses amended since the deliverable's references were pinned.

## 6. Effort

About 35 files or ranges read: the deliverable folder (8 files); three rulings and register rows; SCA-APP-005 (3 files);
the decomposition rows; SPEC/PRD/CONTRACT excerpts; 6 legacy App modules; 6 Runtime modules; 6 test files; the gate
transcripts; and the evidence pack. Context budget was moderate, not tight.
