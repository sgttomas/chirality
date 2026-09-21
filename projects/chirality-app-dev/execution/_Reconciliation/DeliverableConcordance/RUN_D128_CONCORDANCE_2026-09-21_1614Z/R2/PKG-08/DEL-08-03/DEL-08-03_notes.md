# DEL-08-03 — forward notes (RUN_D128, R2 PKG-08)

Forward ledger: `DEL-08-03_claims.csv`, 63 data rows. Validator: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
Sealed SHA-256: `e652bd88823b28855dfc98c7327d9ef68e4e4296afa71f76b3773038945f4bb7`.
Basis: frozen tree `00115c719`. Everything below is evidence, not a ruling.

## 1. Census

No errata file exists, so only sealed figures are shown.

- **Coverage.** All 40 indexed units are covered (3 SEC, 37 CLM, 0 REM). There are also 6 run-local `REGISTER-n` rows and no `STATE-n` rows.
- **Split rate.** 3 of 40 units were split (7.5%), producing 20 rows:
  - CLM-013 into `.1`–`.16`, one row per REQ-001..016;
  - CLM-019 into `.1` (AC-001) and `.2` (UPD-134, a SEE row);
  - CLM-026 into `.1` (VER-001) and `.2` (the Pass-3 table).
  - The SubItems minimum is met: AC-001 and VER-001 each have their own row.
- **SEE rows (counted separately): 4.**
  - CLM-017 → CLM-007
  - CLM-022 → CLM-007
  - CLM-019.2 → CLM-010
  - CLM-031 → CLM-013.11

| Disposition | Rows |
|---|---:|
| ALIGNED | 16 |
| NOT_AUDITABLE | 12 |
| STALE_SPECIFICATION | 12 |
| PARTIALLY_IMPLEMENTED | 10 |
| ACCEPTED_DIVERGENCE | 8 |
| REMAINING_STATE_MISMATCH | 4 |
| IMPLEMENTED_UNDOCUMENTED | 1 |

| ClaimType × Disposition | Rows |
|---|---:|
| REQUIREMENT: ALIGNED 12, ACCEPTED_DIVERGENCE 8, PARTIALLY_IMPLEMENTED 7, STALE_SPECIFICATION 2, IMPLEMENTED_UNDOCUMENTED 1 | 30 |
| ACCEPTANCE: PARTIALLY_IMPLEMENTED 3, ALIGNED 1, STALE_SPECIFICATION 1 | 5 |
| EXCLUSION: ALIGNED 1 | 1 |
| STATE_ASSERTION: STALE_SPECIFICATION 3, ALIGNED 2, REMAINING_STATE_MISMATCH 1 | 6 |
| CONTEXT_CLAIM: NOT_AUDITABLE 12, STALE_SPECIFICATION 3 | 15 |
| REGISTER_DEFECT: STALE_SPECIFICATION 3, REMAINING_STATE_MISMATCH 3 | 6 |

**HumanDecisionNeeded.**

- NO: 59 rows.
- R4-Q1: 4 rows (CLM-013.11, CLM-031, CLM-015, CLM-019.1).
- No AUTHORITY_CONFLICT or UNKNOWN rows.

**Confidence.** HIGH 31, MEDIUM 29, LOW 3.

**Main finding.** DEL-08-03's semantic modules and tests are present and pass at `00115c719` (App gate transcript):

- `lib/pipeline/pipeline-dispatch-contract.ts` (TEST_ONLY);
- `lib/workspace/task-scope.ts`;
- `lib/workspace/filesystem.ts`;
- `/api/project/deliverables`.

The Pipeline presentation (`pipeline-surface.tsx`) is imported statically, which is why it is LIVE in the static map. It is never rendered, because `WovenDialogueRoute` discards its `legacy` prop (`woven-dialogue-route.tsx:18`). This matches the SCA-APP-010 / D-APP-108 retirement that the SoW's Gate-5 section records. The presentation-exposure requirements are therefore ACCEPTED_DIVERGENCE.

## 2. Least-confident rows

- **CLM-013.11 (REQ-011), LOW.**
  - Disposition: PARTIALLY_IMPLEMENTED with R4-Q1.
  - On the live path, selector state never reaches the Runtime-owned turn route, so it cannot bypass the gates.
  - The recorded pass evidence is weaker. It consists of `pkg08-compatibility-boundaries.test.ts`, which runs on a TEST_ONLY contract, and the `routes.test.ts` case at :812-843, which runs the LEGACY_ONLY SDK runtime.
  - Alternative readings: ALIGNED (no live channel means no bypass), or STALE_VERIFICATION (the claim holds but its proof is stale).
- **CLM-031, LOW.** This is a SEE row of CLM-013.11 and has the same alternatives.
- **CLM-013.13 (REQ-013), LOW.**
  - Disposition: PARTIALLY_IMPLEMENTED.
  - The one retained consumer (PS) keeps a hand-copied taxonomy. Its values are identical to `PIPELINE_CATEGORY_OPTIONS` today, but no parity test checks this, and no consumer imports the neutral contract.
  - Alternative reading: ALIGNED, if the requirement is vacuous once no consumer is mounted.
- **CLM-004, CLM-012 and CLM-013.1–.4, MEDIUM.**
  - Disposition: ACCEPTED_DIVERGENCE.
  - Alternative reading: AUTHORITY_CONFLICT. PRD FR-011 ("Contextual PIPELINE shall expose … category controls") was not amended by SCA-APP-010.
  - I did not raise the conflict for two reasons:
    - the PRD compatibility clauses (FR-001; the compatibility list near PRD :1258) anticipate that surfaces are "separately retired";
    - the SCA-APP-010 ruling explicitly addresses DEL-08-03 (MR-11).
  - A stricter reader could route this to R4.
- **CLM-013.12, CLM-026.1 and CLM-025, MEDIUM.**
  - Disposition: PARTIALLY_IMPLEMENTED because no root-change reset fixture exists.
  - Alternative reading: `task-scope-selection.test.ts::clears stale deliverable keys…` could be read as covering root change.

## 3. Register-defect summary

- **REGISTER-1..3.** The `_REFERENCES.md` MATCH hashes for CONTRACT (REF-002), PRD (REF-006) and SPEC (REF-003) do not reproduce (`HASH-RECOMPUTE@00115c719`). The rows for DIRECTIVE, TYPES and PLAN, and all three software-decomp workflow rows, do reproduce (I recomputed them on the frozen tree). SoW restatements of "REF-006 MATCH" (CLM-007, 017, 022, 030) cite REGISTER-2.
- **REGISTER-4.** `_REFERENCES.md` uses REF-009 and REF-010 twice, with different targets. The corpus-v21 workflow-resource rows (:14-15) collide with the SCA-APP-010 table (:22-23).
- **REGISTER-5.** The `_STATUS.md` Remaining section is empty, yet the 2026-07-24 History line says the SCA-APP-004 item was "retained". The item was removed at `bcd56e5db` (D-APP-85 ApplicationCommit, 2026-08-02) and no History line records the removal.
- **REGISTER-6.** `_STATUS.md` shows `Last Updated: 2026-09-04`, but the latest History line is dated 2026-09-05 (D-APP-109).
- **Related, not a REGISTER row: SEC-3.** It still says DEP-023/DEP-024 "await" the dependency pass. That pass ran under D-APP-109, whose write scope excluded the SoW.
- **D-APP-127 application map.** It shows `Revised=NO` for all five carriers. No SoW text depends on the retired daemon topology. The `_CONTEXT.md` Package Scope ("daemon-client dispatch") copies the decomposition PKG-08 row verbatim, so I did not give it a row.

## 4. Direction and cause

**Main CauseTags.**

| CauseTag | Rows | What it covers |
|---|---:|---|
| SHELL_REDESIGN | 12 | Presentation retirement, parallel taxonomy, absent consumer tests |
| DOC_HYGIENE | 9 | Hashes, _STATUS metadata, REF-006 restatements |
| CARRIER_PROPAGATION | 6 | See below |
| PRE_V3_DRIFT | 6 | See below |
| CODEX_SOLE_ENGINE | 2 | REQ-011 proof on the legacy path |

- **CARRIER_PROPAGATION** covers:
  - D-APP-56 P21 was applied only in part: REQ-010, CLM-004 and CLM-006 now name `/api/project/deliverables`, but CLM-016, CLM-023 step 5, CLM-024 and CLM-026 F-002 still name `/api/working-root/scope`;
  - the v21 migration rewrote `_REFERENCES.md` but not SoW REF-007, which still points to the deleted `agents/AGENT_SOFTWARE_DECOMP.md` via an absolute path;
  - CLM-003 was not aligned under D-APP-109;
  - the REGISTER-4 ID collision.
- **PRE_V3_DRIFT** covers:
  - the "Scope of Work" knowledge bucket, added at c4c5dd2df on 2026-07-12, which is outside TYPES §4.4;
  - the missing root-change fixture;
  - the stale "paths TBD" assumption.

**CAUSE2 secondaries:**

- DOC_HYGIENE: CLM-003, 008, 025, 030, REGISTER-4;
- CODEX_SOLE_ENGINE: CLM-015, CLM-019.1;
- SHELL_REDESIGN: CLM-023.

**Records used as DirectionEvidence:**

- GOV:D-APP-108 (G2-CONFIRM presentation retirement; DEC-025);
- GOV:D-APP-56 (P21 endpoint naming; MR-11 applies because the ruling names DEL-08-03 REQ-010);
- GOV:D-APP-74 (semantic/presentation partition);
- GOV:D-APP-85 (Remaining removal);
- GOV:D-APP-109 (dependency pass, `_CONTEXT`-only alignment);
- GOV:D-APP-127 (Codex-only live path; the D-GOV-43 doc amendments behind the hash drift);
- CTX:`execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md` (REF-007 migration, REF-009/010 additions, v21 MATCH snapshot).

**Searches behind NONE_FOUND.** Rows: CLM-013.9, 013.12, 013.13, 025, 026.1, 030, 036. Each Notes cell names the search:

- in `_DECISIONS/_REGISTER.md`, the rows for D-APP-38/56/74/75/77/78/85/107/108/109/127;
- in CONTEXT, a grep of `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, `plans/steers/chirality_app_v3_*`, `_ScopeChange/SCA-APP-008_*` and AgentRuns `APP_V3_*`, `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909` for `pipeline-surface|pipeline-dispatch-contract|DEL-08-03|scope-of-work`.

No record explains leaving PS on a copied taxonomy, the "Scope of Work" bucket label, or the missing root-change fixture. No row is UNRECORDED_JUDGMENT, because a vocabulary mechanism fits each one.

## 5. Method friction

- **REGISTER disposition.** A duplicate RefID (REGISTER-4) is neither "metadata lag" nor a "now-false fact". I used REMAINING_STATE_MISMATCH. Proposal: allow an `OTHER:`-style note, or add "register integrity" to the REMAINING_STATE_MISMATCH gloss.
- **Snapshot restatements.** MR-8 (iv) and §2.7 say a SoW row that restates a snapshot-only MATCH should cite the REGISTER key, but they do not give that SoW row a disposition. I gave CLM-007 (the earliest) STALE_SPECIFICATION and made CLM-017/022 SEE rows of it. Proposal: state the disposition the restating SoW rows should take.
- **Static reach versus rendering.** The static reachability map marks `pipeline-surface.tsx` LIVE, but the element is created and then discarded, so it never renders. The vocabulary has no tag for this. I kept `REACH=LIVE` and wrote "never rendered" plus the `woven-dialogue-route.tsx:18` citation next to it. Proposal: a `REACH=LIVE` note convention such as `UNRENDERED`.
- **PostReleaseBasis.** No cited path appears in `TOUCHED_PATHS.csv`, so I ran no blame and every row is `NO`.

## 6. Effort

- **Files read:** about 45 (deliverable kit 9, decision/ruling records 6, decomposition/SCA extracts 4, code modules 14, test files 8, pack/inventory/gate 6), mostly as greps and line ranges.
- **Git:** read-only log/show on the frozen tree only.
- **Pre-gather:** used as a locator; every cited path was reopened and confirmed.
- **Context budget:** moderate, not tight.
