# DEL-07-03 — reverse-pass notes (R2, PKG-07)

## Input and output

- **Capability files,** in the order the manager gave: BUILD, ELECTRON, ROUTES, SETTINGS, SHELL,
  WORKSPACE, WOVEN. Together they hold 289 capabilities.
- **Output:** `DEL-07-03_reverse.csv`, 289 rows plus `#END`.
- **Responses:**
  - 6 CLAIMED_BY: ROUTES-028, WORKSPACE-011, -013, -016, -017, -038.
  - 5 PARTIAL: ROUTES-036, WORKSPACE-009, -012, -014, -015.
  - 278 NOT_MINE.
- **Validator:** PASS, 0 errors and 0 warnings, for each of the seven capability files.
- **Errata:** none. No sealed forward row was found wrong. The seal holds; the claims SHA-256 is
  unchanged.

## Coverage gaps (missing forward rows; not errata)

- **CAP-WORKSPACE-014 and -015** (ScopeOfWork.md production-format resolver, and the migration-dual
  workspace). Both are live code inside this deliverable's scanner, but no SoW unit describes them.
  - I answered PARTIAL against CLM-009.4, the four-doc-kit detection they extend.
  - An owning claim is missing. The pass-1 notes record this under Coverage gaps as an
    IMPLEMENTED_UNDOCUMENTED candidate. The side effect recorded there also stands: a valid SOW_V1
    folder still receives four `missing_document_kit_file` warnings.

## REACH/STATE disagreements with my ledger or the evidence pack

- **CAP-WORKSPACE-012** Notes say the "live UI consumer document-view uses deliverables and
  deliverableContracts". CAP-WORKSPACE-021 Notes say "document-view is mounted by the woven right
  panel".
  - Both are imprecise for the scan output. `right-panel.tsx:191` always passes a `target`, so it
    renders `FileDocumentView`.
  - The fetch of `/api/project/deliverables` and the read of `deliverableContracts` are in
    `LegacyDocumentView` (`document-view.tsx:48-100`). That component renders only when `target` is
    undefined, which in practice means the 404 AppShell sidebar.
  - CAP-SHELL-044 and my ledger (CLM-009.10 Notes) agree with this narrower reading.
- **CAP-WORKSPACE-008** says the provider's scan result is never read, because its sole consumer
  `PipelineSurface` is retired and unmounted. This is consistent with my ledger:
  - the scanner executes on the live path, so `REACH=LIVE` holds, because the root-layout provider
    fetches the route;
  - the findings have no live UI reader, which is out of scope for this deliverable (CLM-008).
  - My CLM-009.10 wording "deliverables-provider.tsx (roster only)" undersells this. The roster is
    fetched but unused. The disposition is unaffected, so I filed no erratum.
- **CAP-WORKSPACE-038** (`governed-workflow.ts`) is `REACH=TEST_ONLY; STATE=DISABLED`. This agrees
  with my SEC-1, SEC-2 and STATE-1 rows and with the pack's REACHABILITY entry.
- **CAP-WOVEN-042** (WorkflowsView TEST_ONLY) and **CAP-ROUTES-036** (the workflow route LIVE with no
  live UI caller) agree with my SEC-1 notes.
- **CAP-WOVEN-030** confirms that the live Workflows tab is the Runtime method-catalog library. This
  supports the SEC-1 and SEC-2 PARTIALLY_IMPLEMENTED reading.
- **CAP-WORKSPACE-019** shows realpath-based containment on the *other* deliverable contract routes
  (`deliverable-contracts.ts`). It does not cover `/api/project/deliverables`, which uses only
  `normalizeProjectRoot` (CAP-WORKSPACE-009).
  - This strengthens my CLM-009.8 finding that the scanner route lacks the containment its sibling
    routes have. No change is needed.

## Cross-deliverable

- **Workflow capabilities belong to DEL-02-02.** CAP-ROUTES-036, CAP-WOVEN-030/032/042 and
  CAP-SHELL-028 are DEL-02-02's surfaces. The question whether SOW-081 governed files are still
  wanted, now that the live Workflows view uses v3 method packages, should be put to the DEL-02-02
  worker and to R3.
- **Unmounted pipeline surfaces.** CAP-WORKSPACE-020/022/023/024 and the pipeline and workbench
  capabilities belong to DEL-07-04 and DEL-07-05. Their UI surfaces are not mounted.

## Census

With no errata, the sealed and errata-applied census figures are identical (see
`DEL-07-03_notes.md` §1).
