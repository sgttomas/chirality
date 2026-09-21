# DEL-02-04 reverse notes (RUN_D128, R2 PKG-02)

- **Input:** `REVERSE_INPUT_capabilities.csv`, 313 rows, concatenating the areas BUILD, ELECTRON, HARNESS, RTCORE, SHELL, WORKSPACE and WOVEN.
- **Responses:**
  - CLAIMED_BY: 15;
  - PARTIAL: 12;
  - NOT_MINE: 286 (all of BUILD and ELECTRON are NOT_MINE).
- **Sealed ledger:** unchanged, SHA-256 `13e947b4…ee456b3`.
- **Errata:** none. The capability rows agree with the sealed dispositions:
  - CAP-SHELL-007 and CAP-WORKSPACE-007 confirm the Toolkit UI is reachable only on the 404 AppShell, as recorded in CLM-005.1.
  - CAP-WOVEN-035 (ActivityShelf DISABLED) and CAP-WOVEN-040 (stored fields that no component produces) confirm SEC-4 and SEC-1.
  - CAP-WOVEN-040 also lists `coordinationView`, `activityHeight`/`activityCollapsed` and `expandedObjectIds` as retired. The sealed rows already treat these as legacy v1 fields (SEC-4 Notes), and no verdict changes.
- **PARTIAL rows** mark shared ownership:
  - DEL-02-04 owns the convenience-state field or the obligation.
  - Sibling items own the UI:
    - DEL-02-01 shell frame, Navigator and folder select;
    - DEL-02-03-V3-01 right-panel frame;
    - Runtime turn coordination and the legacy turn engine.

## Coverage gaps (for R3)

- **Workspace-state fields with no DEL-02-04 forward row naming them:**
  - `chatIndex`, `foldersCollapsed`, `chatDocuments`, `lastActiveChat` (CAP-WOVEN-015 and CAP-WOVEN-017);
  - `knownRoots` seeding from `chirality.projectRoot` (CAP-WOVEN-016).
  - These are additive v1 fields added after the SCA-APP-010 row. They are mapped PARTIAL to REM-1 (schema discipline) or SEC-3 (known folders).
  - The SoW's SCA-APP-010 field list does not name the first four.
- **Theme persistence contract (CAP-WOVEN-038, CAP-SHELL-018).** Covered only by the Remaining preamble (REMTXT-1). No SoW unit names `theme`.
- **Toolkit storage warning (CAP-WORKSPACE-005).** A corrupt or unavailable toolkit store warns. FR-043 covers drafts and attachments, not toolkit settings, so no DEL-02-04 requirement states the toolkit warning explicitly.
- **User-data preservation across updates (CAP-SHELL-017).** Snapshots renderer storage, including the woven workspace store. Answered NOT_MINE, because the preservation contract belongs to update and release scope.
