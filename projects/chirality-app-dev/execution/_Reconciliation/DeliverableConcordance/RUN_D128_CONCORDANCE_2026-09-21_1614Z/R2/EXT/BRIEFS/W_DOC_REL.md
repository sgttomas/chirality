# EXT worker brief — item 4a, release documents (`DOC-BUILDREL`, `DOC-RQGATES`, `DOC-RQRUN`)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and follow it; it binds this brief.

- **Folder (only write target):** `<RUN>/R2/EXT/DOC_REL/`.
- **Outputs:** `DOC-BUILDREL_claims.csv` + `DOC-BUILDREL_notes.md` (15 units, source
  `projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md`); `DOC-RQGATES_claims.csv` +
  `DOC-RQGATES_notes.md` (14 units, `docs/RELEASE_QUALITY_GATES.md`); `DOC-RQRUN_claims.csv`
  + `DOC-RQRUN_notes.md` (7 units, `docs/RELEASE_QUALITY_RUNBOOK.md`); then `RETURN.md`.
- **Units:** the `Item = 4` rows of `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv` with those
  DOCIDs. `<n>` is the 1-based `##`/`###` heading ordinal (ignoring fenced code); `#0` is the
  preamble. ClaimKey = unit key (e.g. `DOC:BUILDREL#3`); ClaimID = `BUILDREL#3`; split rows
  `DOC:BUILDREL#3.1`; run-local `DOC:BUILDREL#STATE-n`. PackageID `EXT`; DeliverableID = the
  owning deliverable when the section names or evidently belongs to one, else `NONE`.
- **Audit question:** does the section match what shipped?
  - **"What shipped"** is judged from code, build scripts and packaging config under
    `<FROZEN_TREE>/projects/chirality-app-dev/frontend/**` (e.g. `package.json` scripts,
    electron-builder config, `scripts/`), `<RUN>/R2/SURFACES/BUILD_capabilities.csv` and
    `ELECTRON_capabilities.csv` (+ their `_notes.md`), and `<RUN>/GATE_TRANSCRIPTS/`.
  - **Evidence only** (may show what ran, never what the product must do):
    `<FROZEN_TREE>/.github/workflows/harness-premerge.yml` and
    `desktop-release-template.yml`, and release AgentRuns records under
    `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/AgentRuns/`
    (e.g. `APPDEV_UNSIGNED_RELEASE_WORKFLOW_*`, `APP_V3_*`). Do not read other `.github`
    files.
  - Where a section names a deliverable, you may read that deliverable's SoW/`_STATUS.md` in
    the frozen tree.
- **Column guidance:** tier by the source the section restates; process sections that
  restate nothing normative are `STATE_ASSERTION` with `AuthorityTier = NOT_APPLICABLE`.
  Split `.n` only when a section holds separately numbered items or a table of independently
  dispositionable rows (e.g. a gate table) — then give each its own row.
- **For the manager's summary**, put `RELEASE_PROCESS_NOT_RUN:<what>` in Notes on every row
  whose section describes a release process that did not run at or before the frozen basis
  (notarization, code signing, release-quality gates, published artifacts, update feeds …),
  stating what evidence shows it did not run (or that no evidence shows it ran).
