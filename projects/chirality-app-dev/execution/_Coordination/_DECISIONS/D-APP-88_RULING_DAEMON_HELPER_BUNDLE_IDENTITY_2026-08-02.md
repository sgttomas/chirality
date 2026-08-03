# D-APP-88 — Ruling: Distinct Daemon Helper Bundle Identity

Status: `RULED — OPTION B`

DecisionID: `D-APP-88`

Date: `2026-08-02`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Selected proposal:
`execution/_Coordination/_DECISIONS/D-APP-88_PACKET_DAEMON_HELPER_BUNDLE_IDENTITY_2026-08-02.md`
at SHA-256
`853d9ef60a91d461d6477842dd51fccdde4204fafbe978f7d915b821d6257f95`.

Task Management link: `TM-APP-030` (maintenance remains a separate
`TASK_MANAGEMENT` act).

## Exact owner ruling

The owner returned exactly:

> APPROVE D-APP-88 OPTION B

No omitted identifier, implementation result, release act, or broader effect
is inferred.

## Selected semantics

Option B is selected exactly as proposed. The App loop may execute the bounded
helper-bundle tranche that:

- builds a headless helper `.app` inside the unsigned local Desktop package;
- gives it a distinct `CFBundleIdentifier` and `LSUIElement` posture;
- points the LaunchAgent at the helper executable rather than the GUI bundle;
- preserves one Root runtime daemon, the current socket/auth/session stores,
  project registration, CLI behavior, and graceful/recover-on-start
  semantics; and
- keeps ordinary Chirality GUI identity and launch behavior separate.

The executing tranche must return exact proposed identifiers, paths, plist
changes, rollback bytes, and the complete package/drill evidence required by
the selected packet before closing the decision's implementation residual.

## Scope and stop conditions

If the work discovers that a generic Root runtime semantic must change, it
stops and routes that requirement to Root; this ruling cannot absorb it.
Failure to prove GUI/daemon separation, one-daemon continuity, safeStorage,
resource-root integrity, CLI binding, or recovery behavior leaves the tranche
open and returns exact evidence.

This ruling does not decide the separate SIGKILL residual, satisfy the
release-quality premerge row, deploy a LaunchAgent to the owner's machine,
change instruction-root semantics, exercise login-time `RunAtLoad`, or perform
DMG/release-preparation work.

## Preserved boundaries

- No generic runtime contract, Agent-2 Bash, provider/network expansion,
  lifecycle, Checking Approval SHA, release, signing, notarization,
  publication, distribution, or professional-reliance act is authorized.
- Task Management register maintenance remains outside this ruling tranche.
- The six D-APP-81 historical relations remain
  `HISTORICAL_RELATION_UNKNOWN`.

## No-effect boundary

Recording this ruling creates no helper bundle, identifier, package evidence,
deliverable/state write, Task Management disposition, receipt, commit, push,
or merge effect. It authorizes only the packet's bounded Option B tranche for
later ordinary execution.
