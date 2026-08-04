# Deterministic local capability probes

Probe date: `2026-08-03`

Posture: `READ-ONLY OBSERVATION — NOT BACKEND QUALIFICATION`

All commands were executed from the active Root checkout. No dependency was
installed, no sandbox profile was authored, no source was built, and no
product operation was invoked. The results describe one host and one managed
execution environment only.

## Host and toolchain census

```text
$ uname -a
Darwin Ryans-MacBook-Pro.local 25.6.0 Darwin Kernel Version 25.6.0: Sat Jul 11 15:27:04 PDT 2026; root:xnu-12377.161.13~4/RELEASE_ARM64_T6050 arm64
$ uname -m
arm64
$ sw_vers
ProductName:        macOS
ProductVersion:     26.6
BuildVersion:       25G72
$ node --version
v24.18.0
$ npm --version
11.16.0
$ git --version
git version 2.55.0
$ /usr/bin/xcodebuild -version
Xcode 26.6
Build version 17F113
```

Observation: this host can support a macOS/arm64 evidence lane. It establishes
no supported product matrix and says nothing about Linux, Windows, Intel macOS,
older macOS, signing/notarization, packaging, or deployment targets.

## Backend and platform-tool presence

```text
/usr/bin/sandbox-exec
bwrap                    ABSENT
bubblewrap               ABSENT
nsjail                   ABSENT
firejail                 ABSENT
docker                   ABSENT
podman                   ABSENT
colima                   ABSENT
qemu-system-aarch64      ABSENT
/usr/bin/codesign
/usr/bin/security
/usr/sbin/spctl
/bin/launchctl
/usr/bin/xcrun
/usr/bin/clang
```

Hashes of present platform tools:

```text
e3d7a792c58a5d3783d2f7274c82d70062393830d8cb1ded713ca554a470bd2f  /usr/bin/sandbox-exec
6f92f630759f1a7f3faa0bebe1b27b3565a44d5d44c15cc4ddead6b3af373f40  /usr/bin/codesign
09d41a681499554e72830dc158503f40d7b6c153144f0f5d491b88fbd1a5afad  /usr/sbin/spctl
771d7b881c0c4808f3e1c323f7921773def99de4c6f6296c8744893a4369bc2a  /bin/launchctl
4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6  /usr/bin/xcrun
44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698  /usr/bin/clang
```

Presence is not an API/version contract, security guarantee, product backend
selection, redistributability finding, or evidence of availability inside a
packaged application.

## Minimal sandbox-exec probe

```text
$ /usr/bin/sandbox-exec -h
/usr/bin/sandbox-exec: illegal option -- h
Usage: sandbox-exec [options] command [args]
Options:
  -f profile-file     Read profile from file.
  -n profile-name     Use pre-defined profile.
  -p profile-string   Specify a profile on the command line.
  -D key=value        Define a profile parameter.
Exactly one of -f, -n, -p must be specified.

$ /usr/bin/sandbox-exec -n no-network /usr/bin/true
sandbox-exec: sandbox_apply: Operation not permitted
sandbox_no_network_true_exit=71
```

Observation: the binary is installed but a minimal named-profile application
is unusable in this managed environment. This is affirmative negative evidence
against treating binary presence as backend proof. It does not establish
whether a separately entitled/signed product context could use that mechanism.

## Workspace dependency state

`npm ls --depth=0 --json` in `runtime/` exited `ELSPROBLEMS`. It reported all
seven workspace packages plus `@types/node@24.12.4`, `typescript@5.9.3`, and
`vitest@3.2.7` as missing from the current `runtime/node_modules` view. npm also
reported that it could not write its user log directory in this managed
environment.

The checked-in `runtime/package.json` and `runtime/package-lock.json` remain
usable version evidence, but this probe means this environment is not presently
a clean installed-dependency witness for a TM105 conformance or timing run.
No install was attempted.

## Probe consequence

- `TBD-105-02` and `TBD-105-18` remain unresolved.
- No installed backend is qualified.
- No platform pair is admitted.
- No generic timing or budget value can be derived from this host census.
- A later backend/platform evidence run needs a clean, declared, reproducible
  environment and backend-specific adversarial probes.
