# DEL-01-01 — forward-pass notes (RUN_D128 R0 calibration, unit F-01)

Deliverable: `DEL-01-01` Governance Alignment, Human Authority, and Project Truth (PKG-01, `DOC_UPDATE`, `IN_PROGRESS`).
Basis: frozen tree at `00115c719`. Ledger: `DEL-01-01_claims.csv` (54 rows). Agent findings only. No ruling, acceptance or lifecycle effect.

## 1. Census

**Rows by ClaimType × Disposition**

| ClaimType | ALIGNED | STALE_SPECIFICATION | STALE_VERIFICATION | PARTIALLY_IMPLEMENTED | DOCUMENTED_UNIMPLEMENTED | NOT_AUDITABLE | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| REQUIREMENT | 22 | 4 | 0 | 1 | 0 | 0 | 27 |
| ACCEPTANCE | 3 | 0 | 2 | 0 | 1 | 0 | 6 |
| STATE_ASSERTION | 5 | 6 | 0 | 0 | 0 | 0 | 11 |
| CONTEXT_CLAIM | 0 | 2 | 0 | 0 | 0 | 6 | 8 |
| REGISTER_DEFECT | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| **Total** | 30 | 14 | 2 | 1 | 1 | 6 | 54 |

- **Coverage:** all 26 indexed units are covered. The SoW has no REM or REMTXT units, and the `_STATUS.md` Remaining section is empty.
- **Split rate:** 9 of 26 units were split (35%), producing 33 sub-rows:
  - CLM-003 ×2, CLM-004 ×6, CLM-005 ×2, CLM-009 ×11, CLM-010 ×3, CLM-011 ×2, CLM-016 ×2, CLM-017 ×3, CLM-022 ×2.
  - CLM-009.1–.10 map to REQ-001..010.
  - CLM-009.11 isolates the stale audit-path clause in REQ-005's Verification column.
- **Run-local keys:** STATE-1 and STATE-2 (`_CONTEXT.md`, `_STATUS.md`/`MEMORY.md`), plus REGISTER-1 and REGISTER-2.
- **Confidence:** 27 HIGH, 24 MEDIUM, 3 LOW.

## 2. Least-confident rows

- **CLM-009.7 (REQ-007, ALIGNED, LOW).**
  - Alternative reading: STALE_SPECIFICATION with CODEX_SOLE_ENGINE under D-APP-127.
  - CONTRACT K-EVENT-1 now keeps upstream Codex method names and payloads in the browser stream, and the fixed `UIEvent` set is superseded. That arguably lets vendor shape define UI-visible semantics.
  - ALIGNED was kept because K-ENGINE-3/4 still keep `HarnessEvent`, session storage and governance records Chirality-owned.
- **CLM-017.2 (reference-integrity pass condition, STALE_VERIFICATION, LOW).**
  - Alternative reading: ALIGNED. The pass condition only requires `_REFERENCES.md` to say MATCH, and it does.
  - STALE_VERIFICATION was chosen because that cell no longer reflects the tree.
- **CLM-023 (trade-offs, STALE_SPECIFICATION, LOW).**
  - Alternative reading: ALIGNED. The "Chirality-owned contracts, mappers, events, permission overlay, hooks" wording can be read generically.
  - STALE was chosen because D-GOV-43/D-APP-127 direction departs from the Claude-SDK overlay/hook model the row describes: stock Codex App Server, no pinning of approval or sandbox policy, the full published protocol.

## 3. Register-defect summary

- **REGISTER-1.** `Dependencies.csv` row DEP-01-01-011 targets REF-007 `AGENT_SOFTWARE_DECOMP.md` through a machine-specific absolute path.
  - That role file is absent from Root `agents/` at the basis.
  - Corpus v21 replaced it with the `software-decomp` workflow closure. `_REFERENCES.md` was updated, but the SoW (CLM-006, CLM-010.3) and the dependency register were not.
  - `_DEPENDENCIES.md` Run Notes also carry absolute paths.
- **REGISTER-2.** In `_REFERENCES.md`, REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record MATCH against corpus v23 pins, but the live bytes at `00115c719` differ:
  - CONTRACT: `57411f8d…`, pinned `fa8fc9dc…`.
  - SPEC: `8b0d805b…`, pinned `01e1c75c…`.
  - PRD: `17ca3f3c…`, pinned `8649ccba…`.
  - REF-008 is missing from the numbering.
- **Related non-register inconsistency (CLM-025).** CLM-025 shows C002's human ruling as TBD, while CLM-026 R002 records it resolved by D-APP-56 R4-P48.

## 4. Direction and cause

| CauseTag | Rows | CONTEXT record used |
|---|---|---|
| A2_TOPOLOGY | CLM-005.2, CLM-008, CLM-009.11, CLM-011.2, CLM-016.2 | `plans/steers/chirality_app_v3_app_ruling_record_a4_2026-08-23.md` A4-A (owner-selected canonical path `{userData}/runtime/projects/<projectId>/sessions/<sessionId>/events.jsonl`) |
| DOC_HYGIENE | CLM-003.2, CLM-010.2, CLM-015, CLM-017.2, CLM-022.1, CLM-025, REGISTER-2 | NONE_FOUND in the §5 CONTEXT classes (see §5 below) |
| CARRIER_PROPAGATION | CLM-006, CLM-010.3, REGISTER-1 | `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md` |
| CODEX_SOLE_ENGINE | CLM-023, STATE-1 | `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md` |
| OTHER:PENDING_HUMAN_GATE | CLM-017.3 | none needed; this is the normal open human approval gate for an IN_PROGRESS deliverable |

**Main finding (A2 topology).** The deliverable still names project-local `.chirality/sessions/<sessionId>/events.jsonl` as the canonical audit mirror.

- **What governs.** CONTRACT K-EVENT-4 (D-GOV-43/D-APP-127) names the Runtime-owned store as canonical and demotes the project-local path to a read-and-migrate legacy source.
- **Code.**
  - It matches K-EVENT-4: `projects/chirality-runtime/packages/core/src/session-store.ts:1113,1125`, with legacy copy at `:969-974`.
  - The test is `projects/chirality-runtime/tests/session-and-residency.test.ts`.
  - The frontend legacy harness (`frontend/src/lib/harness/session-events.ts`) still writes project-local.
- **Governing set disagrees internally.** App SPEC §8.2, PRD FR-121/§1046 and TYPES line 54 ("normally") still show the project-local path. That inconsistency falls inside DEL-01-01's own alignment scope, so CLM-008 is PARTIALLY_IMPLEMENTED. DIRECTIVE §2.3 tolerates both paths ("or an explicitly configured Chirality-controlled session path").

**Secondary finding (reference drift).** Authority-corpus drift in CONTRACT, SPEC and PRD after corpus v23 makes every "MATCH" assertion stale. The drift is acknowledged in `execution/_Coordination/NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md` and in RUN_BASIS §5 known basis defects, and is carried to owner-directed reconciliation. Those rows carry `HumanDecisionNeeded = R4`.

## 5. Method friction

1. **DirectionEvidence for acknowledged, unreconciled defects.**
   - The 2026-09-19 App loop workgraph notice and its `HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH` run are not in the §5 CONTEXT classes, so rows explained only by them get `DirectionEvidence = NONE_FOUND`.
   - The tempting CauseTag, UNRECORDED_JUDGMENT, is wrong for these rows: the drift is recorded, and it is not a judgment divergence.
   - **Proposal:** either admit `_Coordination/NOTICE_*` and `HELP-HUMAN-APP-*` runs as CONTEXT, or allow `DirectionEvidence = ACKNOWLEDGED:<path>` for defects recorded but not explained.
2. **The governing corpus disagrees internally (CONTRACT K-EVENT-4 vs SPEC §8.2/PRD).**
   - I did not use AUTHORITY_CONFLICT, because DIRECTIVE §0's authority order (CONTRACT over SPEC/PRD) and DIRECTIVE §2.3's allowance settle it.
   - **Proposal:** state explicitly that when the DIRECTIVE authority order resolves a governing-set disagreement, the worker applies it (no AUTHORITY_CONFLICT) but must note the lower-tier stale text.
3. **No CauseTag for the normal pending human gate.** An open human approval gate on an IN_PROGRESS deliverable (CLM-017.3) is not a divergence cause, so I coined `OTHER:PENDING_HUMAN_GATE`.
   - **Proposal:** add `LIFECYCLE_GATE_PENDING`, or allow `NONE` on DOCUMENTED_UNIMPLEMENTED rows whose only gap is a human gate.
4. **PostReleaseBasis cannot be checked.** Without git, a worker cannot tell whether a cited file was touched by the post-v3.0.1 commits. All rows are marked `NO`, meaning not knowingly relied on.
   - **Proposal:** supply per-commit touched-path lists in `RUN_BASIS`.
5. **ClaimType for DOC_UPDATE deliverables.** In a DOC_UPDATE deliverable, most "implementation" is documentary. The MR-10 `documentary claim` form fitted, and `RUN-INSPECTION@00115c719` was the dominant verification token. Guidance on when a hash recompute counts as RUN-INSPECTION would help.

## 6. Effort

- **Files read:** about 35, a mix of full files and line ranges.
  - Run inputs: conventions, run basis, gate transcripts, index rows and the validator.
  - Deliverable files: 9, plus one checklist.
  - Governing docs, by grep and ranges: DIRECTIVE, CONTRACT, SPEC and PRD.
  - Authority corpus JSON; about 8 code and test files; 4 CONTEXT or notice records; the decision register.
- **Context budget:** not tight. This deliverable is a medium-size DOC_UPDATE, with a 391-line SoW and 26 units.
- **Not read:** `_SEMANTIC*.md`, the Evidence_AT-053 files and `_run_records` bodies.
