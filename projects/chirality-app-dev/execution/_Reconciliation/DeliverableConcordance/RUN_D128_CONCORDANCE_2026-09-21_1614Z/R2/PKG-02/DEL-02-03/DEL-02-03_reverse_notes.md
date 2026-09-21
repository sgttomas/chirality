# DEL-02-03 — reverse-pass notes (RUN_D128, R2 PKG-02)

## Input and result

- Input: `REVERSE_INPUT_capabilities.csv`, 307 rows from seven areas: BUILD, ELECTRON, HARNESS, ROUTES, SHELL, WORKSPACE, WOVEN.
- Output: `DEL-02-03_reverse.csv`, which the validator passes (`RULES errors none | warnings none`).
- Responses:
  - `CLAIMED_BY`: 13.
  - `PARTIAL`: 21.
  - `NOT_MINE`: 273.
- The sealed ledger is unchanged (SHA-256 `2c3c1a16d50204a7eae75f817368abdd0b5e726540f9d575595eca980442dcc8`).
- No errata file. None of the capability rows contradicts a sealed forward row. Two of them confirm forward findings:
  - CAP-WOVEN-001: every page renders the Woven shell, and the `legacy` element is not used.
  - CAP-ELECTRON-017: desktop inline PDF preview is unavailable.

## How I assigned responses

- **`CLAIMED_BY`:** the capability is the UI slice of this deliverable. That covers the folder selector and picker, the file tree and its refresh, the Files view, and the tree endpoint.
- **`PARTIAL`:** the capability is shared with another owner. The other owners are:
  - DEL-07-01: validation and containment.
  - DEL-07-03: scope and deliverable scans.
  - DEL-02-02 and DEL-08-03: Pipeline and Workbench selection.
  - DEL-02-04: per-view width state.
  - DEL-02-05: preload physical lead (D-APP-71).
  - DEL-09-06: security proof and PDF.
- **Unrendered consumers:** some PARTIAL rows point to Pipeline or Workbench consumers that are not rendered (CAP-WORKSPACE-029, 032, 033, 034; CAP-SHELL-044). They are claimed only to the forward rows that already record the gap (R4-Q4).
- **T3 capabilities:** the right-panel switcher, document viewer, file-read route, handoff and Quick Look are claimed by REM-1 (`DEL-02-03-V3-01`). No SoW unit covers them; see gap 1 below.

## Coverage gaps (missing forward rows, for R3)

1. **T3 viewer surfaces have no SoW unit.** These capabilities are live, and only the REM-1 row covers them:
   - CAP-SHELL-043 (document viewer);
   - CAP-ROUTES-034 and CAP-ROUTES-035 (file read and handoff policy);
   - CAP-ELECTRON-024 (Quick Look and handoff);
   - CAP-WOVEN-026 and CAP-WOVEN-027 (view switcher and Files view).

   The SoW has not been realigned to SCA-APP-010, so it has no requirement unit for them.
2. **CAP-SHELL-033 (ChatMarkdown/ANSI) is answered `NOT_MINE`.** D-APP-70 names DEL-02-03 as the current production consumer of ChatMarkdown and ANSI (`document-view.tsx` imports `chat-markdown.tsx`). However, no forward row covers that ownership. R3 should decide whether this becomes a DEL-02-03 unit.
3. **`selectDirectory` retention is not stated in the SoW.** D-APP-71 keeps `selectDirectory` semantics with DEL-02-03 (CAP-ELECTRON-021, CAP-ELECTRON-022), but no SoW unit states it. I mapped both to CLM-009.1 (REQ-001).
4. **Per-chat folder capabilities fall outside the pinned SoW.** CAP-ELECTRON-023 (Open Recent and Finder intents) and CAP-WOVEN-006 (folder lock and folder mismatch) implement SOW-002 as SCA-APP-010 amended it. The SoW is still pinned to the global-selection text (see REGISTER-4), so these are mapped PARTIAL to CLM-009.1.
5. **Known folders and cross-folder chats (CAP-WOVEN-015, CAP-WOVEN-016) are answered `NOT_MINE`.** They belong to DEL-02-04 (additive known-folder fields) and to the Navigator (DEL-02-01). R3 may want to confirm the split, since SOW-002 now names an app-scoped set of known folders.
