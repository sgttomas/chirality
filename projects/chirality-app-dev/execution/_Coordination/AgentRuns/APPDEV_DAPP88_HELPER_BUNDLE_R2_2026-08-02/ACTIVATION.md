# Activation — D-APP-88 standalone Electron helper bundle R2

- RunID: `APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02`
- InstanceID: `WI-PKG09-DAPP88-B-R2`
- Parent: App `HELP_HUMAN`
- Role: `WORKING_ITEMS`
- Package: `PKG-09 Validation, Packaging, Security and Release`
- Selected deliverable: `DEL-09-04 macOS DMG Packaging and Instruction Root Integrity`
- Representation: `SOW_V1`
- Git basis: `97678a841ef58345c73d3470ed8de57c9b1405d2`
- Live integration basis: restored D-APP-89 predecessor plus accepted uncommitted D-APP-86..89 planning/rulings and D-APP-89 migration candidate.
- Authority: D-APP-88 Option B ruling, SHA-256 `858a0d4be9adfca1adf5b990df672fa69000e41a0d840894164d99b382e196c6`.
- Attempt-1 handoff: `APPDEV_DAPP88_HELPER_BUNDLE_2026-08-02/HANDOFF_STATE.md`, SHA-256 `7bd6eb84c47f0ce3ea500d49f312b8b93c8659902d016c3cc09d894dc710cc9a`; immutable diagnostic evidence only.
- Profile: `projects/chirality-app-dev/software-workflow.json`.
- Objective: build a complete standalone Electron runtime-helper `.app` through an explicit electron-builder target/config, then deterministically embed that finished bundle as a whole at the GUI package's `Contents/Library/LoginItems/` location and prove every D-APP-88 preservation criterion on final packaged bits.
- Integration owner: this `WORKING_ITEMS` instance.
- Stop conditions: no copied-main bundle mutation, signal wrapper, Root runtime semantic change, weakened recovery contract, owner-machine deployment, or release action. A builder/platform constraint that survives bounded variants returns as an exact blocker.
- Excluded: decisions/register/TM/receipt/completion log, Root source, PRD/corpus, decomposition, SCOPE_CHANGE, foreign-loop surfaces, Git, release, signing, notarization, publication, distribution, and lifecycle transition.

Frontend dependencies are materialized. A reversible Root dependency projection is authorized only for validation and requires exact pre/post restore evidence.

Attempt 1 remains immutable. R2 may cite its facts but may not edit its run root or reuse its blocked source candidate as an implementation base.
