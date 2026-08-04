# Environment and commands

## Revision and source binding

- Repository: `/Users/ryan/.codex/worktrees/1342/chirality`
- `git rev-parse HEAD`: `88e7590d3664d4f1daf91bed2a8899bda0748b92`
- `git rev-parse origin/main`: `88e7590d3664d4f1daf91bed2a8899bda0748b92`
- App notice SHA-256:
  `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`
- Root source SHA-256:
  `runtime/packages/daemon/src/runtime-daemon.ts` =
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`
- Runtime lockfile SHA-256:
  `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f`

The repository was clean at initial binding (`git status --short` empty). The
runtime workspace was copied to `/tmp/chirality-tm112-runtime.iID3BU`; the
copied source and lockfile hashes exactly matched the repository. Dependency
installation and build occurred only in that disposable copy. The built daemon
JavaScript SHA-256 was
`f916c1407584163dd77e736489e16dfce6f74669cc12a0db5fcf79fe923672ab`.

## Environment

```text
Darwin Mac.lan 25.6.0 Darwin Kernel Version 25.6.0: Sat Jul 11 15:27:04 PDT 2026; root:xnu-12377.161.13~4/RELEASE_ARM64_T6050 arm64
ProductName: macOS
ProductVersion: 26.6
BuildVersion: 25G72
Node: v24.18.0
npm: 11.16.0
```

## Exact commands

```sh
git rev-parse --show-toplevel
git rev-parse HEAD
git rev-parse origin/main
shasum -a 256 projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md runtime/packages/daemon/src/runtime-daemon.ts
mktemp -d /tmp/chirality-tm112-runtime.XXXXXX
cp -R /Users/ryan/.codex/worktrees/1342/chirality/runtime/. /tmp/chirality-tm112-runtime.iID3BU/
(cd /tmp/chirality-tm112-runtime.iID3BU && npm ci --ignore-scripts)
(cd /tmp/chirality-tm112-runtime.iID3BU && npm run build)
(cd /tmp/chirality-tm112-runtime.iID3BU && npm test -- --run tests/daemon.test.ts)
node /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/fixtures/runtime-stop-reproducer.mjs /tmp/chirality-tm112-runtime.iID3BU
node /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/fixtures/runtime-stop-reproducer.mjs /tmp/chirality-tm112-runtime.iID3BU
node /Users/ryan/.codex/worktrees/1342/chirality/execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/fixtures/runtime-signal-sse-reproducer.mjs /tmp/chirality-tm112-runtime.iID3BU
```

The socket-bearing test/reproducer commands were run outside the filesystem
sandbox after the first in-sandbox baseline attempt failed with `listen EPERM`.
No network listener was used; all controlled listeners were Unix-domain
sockets in disposable directories.

## Fixture hashes

- `runtime-stop-reproducer.mjs`:
  `4b57168a43f3232ca50f6d5332637a10ef205a4a7921d8262fcc0e2bf7919873`
- `runtime-signal-sse-reproducer.mjs`:
  `0706c826e3a55c9b4c027ab9a2126c236b3ee15ae57193f3153a448891eb444b`

## Non-behavioral fixture failures retained

1. The initial baseline test inside the sandbox produced three `listen EPERM`
   failures and two passes. The same exact suite outside the socket-restricted
   sandbox passed 5/5; the EPERM result is environmental, not a runtime defect.
2. The first custom reproducer attempt used a macOS Unix-socket path exceeding
   the platform length limit and stopped at the third case with `listen EINVAL`.
   The fixture was corrected to use short `/tmp/t112-*` paths; this pathname
   rejection is not a stop-behavior result.

