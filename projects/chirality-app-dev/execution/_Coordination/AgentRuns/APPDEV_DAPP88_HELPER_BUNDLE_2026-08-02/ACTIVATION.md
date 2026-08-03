# Activation — D-APP-88 distinct daemon helper bundle

- RunID: `APPDEV_DAPP88_HELPER_BUNDLE_2026-08-02`
- InstanceID: `WI-PKG09-DAPP88-B`
- Parent: App `HELP_HUMAN`
- Role: `WORKING_ITEMS`
- Package: `PKG-09 Validation, Packaging, Security and Release`
- Selected deliverable: `DEL-09-04 macOS DMG Packaging and Instruction Root Integrity`
- Representation: `SOW_V1`
- Basis: Git `97678a841ef58345c73d3470ed8de57c9b1405d2`, accepted uncommitted D-APP-86..89 planning/rulings, and accepted D-APP-89 compatibility-facade migration candidate.
- Authority: `D-APP-88_RULING_DAEMON_HELPER_BUNDLE_IDENTITY_2026-08-02.md`, Option B, and its selected packet.
- Profile: `projects/chirality-app-dev/software-workflow.json`
- Objective: build and prove a distinct headless helper `.app` inside the unsigned local Desktop package, point the LaunchAgent at its executable, and preserve the one-daemon/runtime-store/CLI/GUI semantics enumerated in D-APP-88.
- Integration owner: this `WORKING_ITEMS` instance.
- Stop condition: any required generic Root runtime semantic change is routed upward and not absorbed.
- Git, receipt, register, Task Management, PRD/corpus, decomposition, SCOPE_CHANGE, Root runtime, Piping/PEC, release, signing, notarization, publication, distribution, lifecycle, and professional-reliance effects are excluded.

The runtime does not expose reliable token/context occupancy to this managed run. Telemetry records that measurement limitation instead of inferring occupancy.
