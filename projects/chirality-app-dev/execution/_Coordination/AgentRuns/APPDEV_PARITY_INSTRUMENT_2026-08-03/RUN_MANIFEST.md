# D-APP-86 Integrated Parity Instrument — Run Manifest

Status: `PASS — EVIDENCE ONLY`

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

Executor: `A2-PARITY-EXECUTOR-01`

Parent: `WI-PKG09-DAPP86-A`

Authority: D-APP-86 Option A, the frozen `ACTIVATION.md`, `WORK_GRAPH.md`,
`instances/A2-PARITY-EXECUTOR-01/LAUNCH_BRIEF.md`, and the two versioned brief
amendments. This run establishes an evidence result only. It does not change
product source, authority, decomposition, lifecycle, release state, Task
Management state, or the D-APP-89 ruling.

## Frozen basis

- Repository HEAD: `97678a841ef58345c73d3470ed8de57c9b1405d2`
- Branch: `codex/appdev-planning-gates-20260802`
- Source manifest: 380 files; manifest SHA-256
  `1672e1d57249dc7d833d05e8e857add1c751728de1d96568d0c83607903955c1`
- Initial App diff digest: SHA-256
  `09d244e3aff0cc73133c1a2cd93b88ee98de13557bf082b744b97a6012e6a7e2`
  (the accepted, concurrent D-APP-89 migration basis; not created by this run)
- Runtime: Node `v24.18.0`; npm `11.16.0`; macOS `26.6` arm64

## Frozen package

Exactly one unsigned/adhoc local package was successfully built and reused.
The first sandboxed packaging invocation stopped before package creation on a
network-resolution error; the authorized network retry produced the sole
package.

- Package: `frontend/dist/mac-arm64/Chirality.app`
- Package manifest: 446 regular files; SHA-256 of manifest
  `90afe8236873558f3d0ad9e83b49e991998565977085eb2bc192f5ef45582e32`
- Symlink census: 14; SHA-256
  `6308b00235ff20598389689fbe50417fbb184ca45d20bd7fe1c1bdc0ac41f73c`
- Main executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- `app.asar` SHA-256:
  `18797e99d5b6330e40e9c31b80ac42479c18a7bd2a721df49275ad0d33c72ce2`
- `Info.plist` SHA-256:
  `a5bfabe95540666235a83da60ad1daabc43c714abcbc21a1877b381a1969d414`
- Architecture: arm64
- Signing posture: linker/adhoc only; no Team ID; no signing, notarization,
  publication, or distribution claim

The package manifest revalidated 446/446 after observation and before
closeout.

## Execution attempts

1. Attempt 01 lawfully started the packaged daemon/App and produced a real
   completed stub session, but native Computer Use could not proceed because
   the Mac was locked. The attempt was stopped cleanly and its exact temporary
   root was removed. It is retained as partial method provenance only.
2. Retry 02 reused the identical package/source bytes. Under authorized Brief
   Amendment 02 it exposed only the packaged renderer's standard loopback CDP
   endpoint, producing DOM, accessibility-tree, and 2560×1580 PNG state for
   all four required observations. The packaged daemon/App and all exact
   Retry-02 temporary state were then stopped and removed.

## Result

All four UI observations, daemon replay binding, the exact validation
contract, source/package preservation, D-APP-89 guards, six-UNKNOWN
preservation, secret scan, projection restoration, owner-state containment,
and cleanup checks pass. See `PACKAGED_UI_SMOKE.md`, `REAL_DAEMON_REPLAY.md`,
`VALIDATION.md`, and `HANDOFF.md`.

The accepted D-APP-88 distinct-helper implementation remains absent/blocked
in this source basis. Any later accepted implementation of that helper is a
non-blocking parity rerun trigger, not a defect in this evidence result.
