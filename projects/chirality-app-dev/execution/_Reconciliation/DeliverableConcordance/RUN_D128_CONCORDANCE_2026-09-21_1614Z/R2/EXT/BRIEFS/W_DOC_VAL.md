# EXT worker brief — item 4b, validation and reliance documents (`DOC-VALSTRAT`, `DOC-RELIANCE`)

First read `<RUN>/R2/EXT/BRIEFS/_COMMON_RULES.md` and follow it; it binds this brief.

- **Folder (only write target):** `<RUN>/R2/EXT/DOC_VAL/`.
- **Outputs:** `DOC-VALSTRAT_claims.csv` + `DOC-VALSTRAT_notes.md` (9 units, source
  `projects/chirality-app-dev/docs/VALIDATION_STRATEGY.md`); `DOC-RELIANCE_claims.csv` +
  `DOC-RELIANCE_notes.md` (13 units, `docs/harness/reliance_boundary_register.md`); then
  `RETURN.md`.
- **Units:** the `Item = 4` rows of `<RUN>/R1_INVENTORY/EXTENSION_INDEX.csv` with those
  DOCIDs. `<n>` is the 1-based `##`/`###` heading ordinal (ignoring fenced code); `#0` is the
  preamble. ClaimKey = unit key (e.g. `DOC:VALSTRAT#3`); ClaimID = `VALSTRAT#3`; split rows
  `DOC:VALSTRAT#3.1`; run-local `DOC:VALSTRAT#STATE-n`. PackageID `EXT`; DeliverableID =
  the owning deliverable when evident, else `NONE`.
- **Audit question:** does the section match what shipped?
  - **"What shipped"** is judged from App code and tests under
    `<FROZEN_TREE>/projects/chirality-app-dev/frontend/**`, runtime
    `packages/**`/`tests/**`, `<RUN>/R2/SURFACES/*_capabilities.csv` (BUILD, ELECTRON,
    HARNESS, RTCORE, RTCONTRACT and others as relevant) and `<RUN>/GATE_TRANSCRIPTS/`.
  - **Evidence only:** `<FROZEN_TREE>/.github/workflows/harness-premerge.yml` and
    `desktop-release-template.yml`, and release AgentRuns records under
    `<FROZEN_TREE>/projects/chirality-app-dev/execution/_Coordination/AgentRuns/`. Do not
    read other `.github` files.
  - The reliance register's rows about harness guarantees (path containment, hooks,
    approval, redaction …) are product-behaviour claims under the Addendum 6 subject test:
    judge them on the live Codex path and apply R4-Q1 rule 3 by REACH evidence.
  - Where a section names a deliverable, you may read that deliverable's SoW/`_STATUS.md`
    in the frozen tree.
- **Column guidance:** tier by the source the section restates; process sections that
  restate nothing normative are `STATE_ASSERTION` with `AuthorityTier = NOT_APPLICABLE`.
  Split `.n` only when a section holds separately numbered items or a table of
  independently dispositionable rows (a register table usually is one) — then give each its
  own row.
- **For the manager's summary**, put `RELEASE_PROCESS_NOT_RUN:<what>` in Notes on every row
  whose section describes a validation or release process that did not run at or before the
  frozen basis (release-quality gates, signing, notarization, manual QA passes …), stating
  the evidence.
