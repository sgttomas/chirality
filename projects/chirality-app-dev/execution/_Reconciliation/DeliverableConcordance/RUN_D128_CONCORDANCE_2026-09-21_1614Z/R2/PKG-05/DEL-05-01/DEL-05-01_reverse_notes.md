# DEL-05-01 — reverse-pass notes (R2, PKG-05)

- **Capability files.** Eight files were answered, in the order the manager gave: BUILD, ELECTRON, HARNESS,
  ROUTES, RTCONTRACT, RTCORE, SETTINGS and WORKSPACE.
- **Rows.** 364 in total:
  - `CLAIMED_BY`: 1;
  - `PARTIAL`: 10;
  - `NOT_MINE`: 353.
- **Validator.** Each file was checked separately with `validate_ledger.py reverse --capabilities <file>`.
  All eight report PASS with 0 errors and 0 warnings.
- **Sealed ledger.** Unchanged: SHA-256 `b4f524561cd14fd2ac10af0407d9c685ba3260d440015efb4d48cb6297da3cea`.
- **Errata.** None. The capability rows confirm the forward reach judgments:
  - CAP-HARNESS-037 is `FileSessionManager` at LEGACY_ONLY;
  - CAP-RTCORE-015 and CAP-RTCORE-009 are the live Runtime store and the live bootstrap;
  - CAP-HARNESS-026 is `assertProjectRootAccessible` at LIVE.
- **Census.** No errata file exists, so the sealed and errata-applied figures are identical. They are in
  `DEL-05-01_notes.md` §1.

## Ownership reading

- **CLAIMED_BY.** The only capability DEL-05-01 fully owns is the legacy App file-backed store
  (CAP-HARNESS-037). The SoW specifies exactly that module, which is why the forward pass cites R4-Q1.
- **PARTIAL.** On the live path, DEL-05-01's slice is the legacy-migration part of the Runtime session
  store:
  - CAP-RTCORE-015, the store itself;
  - CAP-RTCORE-009, the bootstrap manifest;
  - CAP-RTCONTRACT-008, the `legacySessionRoots` field;
  - CAP-ROUTES-003, the get-by-id migration trigger.
- **Not owned.** Generic session persistence is excluded by the PKG-05 package scope, which leaves it to the
  Runtime or other deliverables.

## Coverage gaps (for the manager; no forward row can own these)

1. **Deletion tombstones (CAP-RTCORE-015).** `SessionStore.delete` writes `.deleted/<id>.json` tombstones.
   These hide retained legacy sources from list and get. This is live, product-visible deletion state, and
   no DEL-05-01 text describes it. CLM-018 step 7 and CLM-032 still describe delete as removing the flat
   duplicate.
2. **Legacy roots in bootstrapped manifests (CAP-RTCORE-009).** Minimal hosted manifests are created without
   `legacySessionRoots`.
   - Consequence: v2 migration is inert for every bootstrapped project.
   - No SoW unit or Remaining item names who declares legacy roots. That includes the packaged App's old
     `cwd/.chirality/sessions` store.
   - REM-1 (V3-02) covers this only implicitly, and its gate names a retired Root dependency.
3. **Operator CLI session commands (CAP-RTCORE-049).** The CLI's session create, list and replay commands use
   the same central store. No App deliverable claims them, which is expected because they are Runtime-owned.
   They are listed here only as a boundary trace.
