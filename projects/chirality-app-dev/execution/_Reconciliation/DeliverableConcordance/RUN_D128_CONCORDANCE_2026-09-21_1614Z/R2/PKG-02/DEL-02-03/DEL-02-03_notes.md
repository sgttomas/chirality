# DEL-02-03 — forward-pass notes (RUN_D128, R2 PKG-02)

Ledger: `DEL-02-03_claims.csv`. It is sealed at SHA-256
`2c3c1a16d50204a7eae75f817368abdd0b5e726540f9d575595eca980442dcc8` (validator: `RULES errors none | warnings none`, `RESULT PASS`).
Basis: frozen tree at `00115c719`. Disposition is evidence, not a ruling.

## 1. Census

- 56 rows: 34 indexed units (CLM-001..CLM-032, REM-1, REM-2), plus 5 run-local `REGISTER-n` rows and no `STATE-n` rows.
- Split rate: 4 of 34 units (11.8%).
  - CLM-004 splits into .1–.3 (a table of conditions that are dispositioned independently).
  - CLM-009 splits into .1–.14 (DEL-02-03-REQ-001..014; the index's SubItems cell is empty, so this split is optional and follows the REQ numbering).
  - CLM-015 splits into .1 (the text) and .2 (AC-001, its SubItem).
  - CLM-023 splits into .1 (the text) and .2 (VER-001, its SubItem).
- SEE rows, counted separately: 8.
  - CLM-001 → REGISTER-3.
  - CLM-004.3, CLM-016, CLM-024, CLM-030, CLM-031, CLM-032 → CLM-001.
  - CLM-023.1 → CLM-014.

| ClaimType \ Disposition | ALIGNED | STALE_SPEC | PARTIAL | DOC_UNIMPL | IMPL_DIFF | NOT_AUD | UNKNOWN | REM_STATE_MISMATCH | Total |
|---|---|---|---|---|---|---|---|---|---|
| REQUIREMENT | 9 | – | 6 | 6 | 2 | – | – | – | 23 |
| ACCEPTANCE | 1 | – | 3 | – | – | – | 1 | – | 5 |
| STATE_ASSERTION | 3 | 7 | – | – | – | – | – | – | 10 |
| CONTEXT_CLAIM | – | 5 | – | – | – | 6 | – | – | 11 |
| REGISTER_DEFECT | – | 4 | – | – | – | – | – | 1 | 5 |
| REMAINING_WORK | 1 | – | 1 | – | – | – | – | – | 2 |
| **Total** | 14 | 16 | 10 | 6 | 2 | 6 | 1 | 1 | 56 |

- HumanDecisionNeeded: `NO` 42, `R4-Q4` 14. No row cites R4-Q1: no relied-on code is tagged `LEGACY_ONLY`. No row cites R4-Q2, R4-Q3 or R4-Q5.
- No errata file exists (forward pass only).

## 2. Least-confident rows

- **CLM-009.13 (REQ-013, stable IDs), LOW.** I judged it as product behaviour under the Addendum 6 subject test. On the live shell no summary widgets or route targets carry deliverable identity, so the verdict is `DOCUMENTED_UNIMPLEMENTED`.
  - Alternative reading: at module level, `splitStableId` and the `pkg::id` keys meet the contract, which would make the row `ALIGNED`.
- **CLM-023.2 (VER-001), LOW, `UNKNOWN`.** I found no record of the ScopeOfWork migration verification in the deliverable folder, in `_run_records`, or in the three commits that touch `ScopeOfWork.md`.
  - Alternative reading: the verification is recorded in a coordination run I did not search, which would make the row `ALIGNED`.
- **CLM-009.1 and CLM-009.3 (REQ-001 and REQ-003), MEDIUM, `IMPLEMENTED_DIFFERENTLY`.** The live shell selects a folder per chat and locks it after the first message. It has no Clear control.
  - Alternative reading: `PARTIALLY_IMPLEMENTED`, because path entry, picker and apply do exist live.
  - I did not use `AUTHORITY_CONFLICT`. Under DIRECTIVE §0, PRD FR-002 and §7.1 (unamended) rank above the SCA-APP-010 decomposition text, so the authority order resolves the disagreement.
- **Pipeline/Workbench-dependent rows (MEDIUM): CLM-004.2, CLM-009.7–.10, CLM-009.13, CLM-003, CLM-005, CLM-008, CLM-012, CLM-019, CLM-020, CLM-029 and CLM-011.**
  - Why they fail on the live shell: the pack tags `pipeline-surface.tsx` and `workbench-surface.tsx` `LIVE` by import. However, the only thing that constructs them is LoopShell/LoopTertiaryShell, and every page passes those as the discarded `legacy` prop (`woven-dialogue-route.tsx:18`, `void legacy`, introduced by 9b005c23a). The rows are therefore judged `DOCUMENTED_UNIMPLEMENTED` or `PARTIALLY_IMPLEMENTED` on the live path, with `SYMBOL-UNREACHED` recorded in Notes.
  - Alternative reading: `AUTHORITY_CONFLICT` + R4-Q4. D-APP-108 Q3 and SCA-APP-010 SOW-001 retire the Pipeline/Workbench mounts, while PRD FR-010/011/012 and SPEC §17.3 item 6 ("re-hosted Workbench, Pipeline") stand unamended. I kept the Disposition as the behavioural verdict because DIRECTIVE §0 ranks SPEC and PRD above scope-change records. I cited R4-Q4 because the surface retirement is the question those rows turn on.

## 3. Register-defect summary

- **REGISTER-1..3 (`STALE_SPECIFICATION`, HIGH):** `_REFERENCES.md` records CONTRACT, SPEC and PRD as `MATCH`. All three fail recompute at `00115c719` (pack `REFERENCE_HASHES.csv`: Match=NO).
  - I also recomputed DIRECTIVE, TYPES, PLAN and the three `workflows/software-decomp` references. They still match.
  - `_REFERENCES.md` was not revised under D-APP-127, so the rows carry `CARRIER_PROPAGATION` with `CAUSE2:DOC_HYGIENE`.
- **REGISTER-4 (`REMAINING_STATE_MISMATCH`):** the SoW `decomposition_basis` is pinned at `7b0be4d8`, where SOW-002 reads "global working-root selection". The applied SOW-002 (SCA-APP-010) now reads per-chat folders fixed after the first message.
  - DEL-02-03 was seated outside the thirteen re-pinned carriers (D-APP-108), and MEMORY.md acknowledges the pin.
  - The pin is snapshot-tied (MR-8 iv), so this is a REGISTER row.
- **REGISTER-5 (`STALE_SPECIFICATION`):** the `Dependencies.csv` TargetLocation line anchors (#L285, #L333, #L335–337, #L346, #L378, #L379) now point to the wrong rows. Those rows are at L309, L357, L359–361, L370, L405 and L406.

The SoW restates the PRD `MATCH` as current in eight places (CLM-001, 004.3, 016, 024, 030, 031, 032, and CLM-021 as part of its records list). Each carries `STALE_SPECIFICATION` and points by `SEE:` to CLM-001, which points to REGISTER-3.

## 4. Direction and cause

**Main CauseTags:**

- `SHELL_REDESIGN` (16). SCA-APP-010 / D-APP-108 moved the shell to a per-chat folder and unmounted Workbench/Pipeline; the v3 adoption commit 9b005c23a dropped the legacy-route rendering.
- `CARRIER_PROPAGATION` (12). These are stale PRD-MATCH notes and prerequisite/consideration text that UPD-068/UPD-108 left partial, plus unrevised `_REFERENCES.md`.
- `DOC_HYGIENE` (5): stale section citations:
  - PRD §7.2 is now "Collaborate Through Woven Dialogue"; the Pipeline journey is §7.5.
  - PRD §13 is now "Runtime Development Sequence"; the workspace APIs are in §9.2.
  - PRD §6.2 is now "Current Release Target".
  - TYPES §8.2 is "Permission Decision"; TaskScopeMode is in §4.4.
  - The retired four-document kit files are still listed in Records.
- `PRE_V3_DRIFT` (2):
  - REQ-011: the UI keeps only `error.message` and drops the type, status and details. `git blame` places this at 7bee9ae41, 2026-05-18.
  - CLM-011: missing fixture tests.
- `LIFECYCLE_GATE_PENDING` (1): REM-1, where the D-APP-121 PDF effect is HELD and `inlinePdfPreview` is `false`.

**CAUSE2 secondaries:** `DOC_HYGIENE`, `CARRIER_PROPAGATION`, `SHELL_REDESIGN`, `PRE_V3_DRIFT`.

**Direction records used:**

- GOVERNING:
  - D-APP-108 (SCA-APP-010 seating; Q3 retired routes; SOW-002 per-chat folder).
  - D-APP-121 (flagged: PDF effect held).
  - D-APP-38 (reference-integrity model).
  - D-APP-56 (UPD-068/UPD-108).
- CONTEXT: `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/` (v3 adoption; it records no Pipeline-specific direction beyond the commit itself).

**Searches behind each `NONE_FOUND`** (CLM-006, CLM-009.11, CLM-010, CLM-011, CLM-021, CLM-023.2, REGISTER-5):

- I grepped `_DECISIONS/_REGISTER.md` for "four-document", "ScopeOfWork", typed-error and reference-refresh wording. The only hits were D-APP-75 and D-APP-78 (repin holds), which do not explain these rows.
- I checked the CONTEXT AgentRuns listing (CHIRALITY_V3_APP_ADOPTION_20260909: UI_SOURCE_FREEZE_v7, MANAGER_RETURN).
- Neither source explains these divergences.

**Other decisions checked:**

- D-APP-70/71: DEL-02-03 keeps `selectDirectory` semantics, and the preload `selectDirectory` is live.
- D-APP-110: the DEL-02-03 → DEL-02-04 edge DEP-02-04-019 lives in DEL-02-04's register.

**PostReleaseBasis:** no file cited by this ledger appears in `TOUCHED_PATHS.csv`, so every row is `NO`.

## 5. Method friction

- **MR-4 direction for SEE.** The Conditions (CLM-004) and Construction (CLM-005) tables restate the same requirements that CLM-009 numbers, but they come earlier. MR-4 would put the full disposition on the earlier, non-numbered table, with the REQ rows as SEE rows. I did the reverse: the numbered REQ rows carry the full disposition, and the earlier rows name them in prose, not with `SEE:`.
  - Proposed revision: allow the numbered REQ unit to be the SEE target when an earlier summary table paraphrases it.
- **Pack reach vs symbol reach.** `REACHABILITY.csv` tags `pipeline-surface.tsx`, `workbench-surface.tsx`, `portal-loop-shell.tsx`, `loop-shell.tsx` and `shell-frame.tsx` (the non-workspace branch) `LIVE`. The import chain passes through a JSX element that is constructed but never rendered.
  - Proposed revision: have the pack builder treat `woven-dialogue-route.tsx`'s `legacy` prop as a non-rendering edge.
- **REM-1 gate marker.** The written gate (DEL-02-02-V3-03 landed) is satisfied, but the marker was not updated. The row is still correctly open, so no tie-break verdict fits. I recorded this in Notes only.

### Coverage gaps (for R3)

- **Document viewer and file endpoint not in the SoW.** The in-app document viewer (`document-view.tsx`), the bounded file-read endpoint (`/api/working-root/file`), the right-panel view switcher and the Quick Look handoff are live and belong to DEL-02-03 through `_STATUS.md` REM-1 and decomposition row L309. However, the unrealigned SoW has no indexed unit for them; only REM-1 covers them.
- **ChatMarkdown/ANSI consumer ownership not in the SoW.** D-APP-70 names DEL-02-03 the production consumer of ChatMarkdown/ANSI (`document-view.tsx` imports `chat-markdown.tsx`), but no SoW unit covers it.
- **`selectDirectory` retention not in the SoW.** D-APP-71 retains DEL-02-03 `selectDirectory` semantics on `preload.ts`, but no SoW unit states it.
- **Scope route has no rendered consumer.** `/api/working-root/scope` is a live route with no rendered consumer. Scope-scan backend ownership is DEL-07-03's. The UI gap is recorded under CLM-009.7.

## 6. Effort

- Files read: about 45 (deliverable folder 8, run and convention files 6, evidence pack 5, App frontend sources 15, tests (names only) 8, decisions and governing docs 6). I also ran read-only `git log`, `show` and `blame` about 12 times against the frozen tree.
- Context budget: moderate, not tight.
