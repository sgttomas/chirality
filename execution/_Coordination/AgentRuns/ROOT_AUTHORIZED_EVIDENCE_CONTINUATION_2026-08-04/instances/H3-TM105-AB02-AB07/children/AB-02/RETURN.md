# AB-02 return — TM105 backend, rights, and topology evidence

Child: `H3-TM105-AB02-AB07/AB-02`

Posture: `EVIDENCE ONLY / PREPARATION ONLY`

Coverage is limited to the 16 SHA-bound inputs and the exact local host
observations authorized by the sealed brief. This is not a complete backend,
platform, deployment, sandbox, packaging, security, or product survey. Every
candidate below is **`NOT_QUALIFIED`**.

## 1. Input verification

`git rev-parse --show-toplevel` resolved the repository root to
`/Users/ryan/.codex/worktrees/1342/chirality`. `shasum -a 256` was run against
every declared input. Every observed digest equals the digest sealed in the
brief; input drift is **`NONE`**.

| Input | Observed and expected SHA-256 |
|---|---|
| `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/instances/H2-TM105-AB01-AB09/children/AB-01/RETURN.md` | `8a3d6d25837cf245bc45f66be95e38c9f05bec002d5fa8133a28a11a5c08f1d6` |
| `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/LOCAL_PROBE_RESULTS.md` | `e25e0d538ac9307b246aa2eb78fb36ec2ea8f213618550d09005f9cf987216dc` |
| `runtime/packages/contracts/src/engine.ts` | `d76fab70ef8ff7a6b5f4b5d669fb6367fa7707b664256433420b8b210c61ebdb` |
| `runtime/packages/contracts/src/harness/tool-descriptor.ts` | `bcb87844dce118a3f7743b3e2e0ecc0c376627d2dbaf1dee483a281c6f2b767b` |
| `runtime/packages/contracts/src/harness/agent-engine-port.ts` | `c51d2b6a173f300acedee468f8e51b29cea2bd946bcdec300eaaa4a3d06a8e5d` |
| `runtime/packages/contracts/src/harness/tool-catalog.ts` | `d63b82288204192b9121826fcd3426f85e94362b0e0d2f7f3be343b7d98498f9` |
| `runtime/packages/core/src/agent1-run-coordinator.ts` | `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` |
| `runtime/packages/core/src/project-registry.ts` | `7b803aa01fc4fae97b3544f66cfafef1d2742270b670dec4011ba352f2fbce71` |
| `runtime/packages/core/src/runtime-service.ts` | `43b2dd4dbf8b1a91a057350558229616e34bfec258b2b9ad8f5e36c058c7c74d` |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` |
| `runtime/tests/agent1-run.test.ts` | `42dbdd15f73e60839fdfd41b980a871a9a49a4ba62d0bb33df23933568167dff` |
| `runtime/tests/daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` |
| `runtime/package.json` | `499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071` |
| `runtime/package-lock.json` | `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-84_PACKET_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_REVISION_2_2026-08-02.md` | `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9` |
| `projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md` | `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7` |

## 2. Exact local observations

These results describe one managed macOS host at one instant only. They do not
establish a supported platform, packaged-product environment, backend API,
deployment topology, entitlement, signing posture, redistribution right, or
security guarantee.

### Environment identity

```text
$ uname -a
exit=0
Darwin Ryans-MacBook-Pro.local 25.6.0 Darwin Kernel Version 25.6.0: Sat Jul 11 15:27:04 PDT 2026; root:xnu-12377.161.13~4/RELEASE_ARM64_T6050 arm64
$ uname -m
exit=0
arm64
$ sw_vers
exit=0
ProductName:		macOS
ProductVersion:		26.6
BuildVersion:		25G72
$ node --version
exit=0
v24.18.0
$ npm --version
exit=0
11.16.0
$ git --version
exit=0
git version 2.55.0
```

### Exact candidate-binary lookup

An empty result below is the raw result of `command -v`; its recorded exit is
the affirmative absence observation for this host environment.

```text
$ command -v /usr/bin/sandbox-exec
exit=0
/usr/bin/sandbox-exec
$ command -v bwrap
exit=1
$ command -v bubblewrap
exit=1
$ command -v nsjail
exit=1
$ command -v firejail
exit=1
$ command -v docker
exit=1
$ command -v podman
exit=1
$ command -v colima
exit=1
$ command -v qemu-system-aarch64
exit=1
$ command -v /usr/bin/codesign
exit=0
/usr/bin/codesign
$ command -v /usr/bin/security
exit=0
/usr/bin/security
$ command -v /usr/sbin/spctl
exit=0
/usr/sbin/spctl
$ command -v /bin/launchctl
exit=0
/bin/launchctl
$ command -v /usr/bin/xcrun
exit=0
/usr/bin/xcrun
$ command -v /usr/bin/clang
exit=0
/usr/bin/clang
```

### Present-binary hashes

```text
$ shasum -a 256 /usr/bin/sandbox-exec
exit=0
e3d7a792c58a5d3783d2f7274c82d70062393830d8cb1ded713ca554a470bd2f  /usr/bin/sandbox-exec
$ shasum -a 256 /usr/bin/codesign
exit=0
6f92f630759f1a7f3faa0bebe1b27b3565a44d5d44c15cc4ddead6b3af373f40  /usr/bin/codesign
$ shasum -a 256 /usr/bin/security
exit=0
2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7  /usr/bin/security
$ shasum -a 256 /usr/sbin/spctl
exit=0
09d41a681499554e72830dc158503f40d7b6c153144f0f5d491b88fbd1a5afad  /usr/sbin/spctl
$ shasum -a 256 /bin/launchctl
exit=0
771d7b881c0c4808f3e1c323f7921773def99de4c6f6296c8744893a4369bc2a  /bin/launchctl
$ shasum -a 256 /usr/bin/xcrun
exit=0
4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6  /usr/bin/xcrun
$ shasum -a 256 /usr/bin/clang
exit=0
44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698  /usr/bin/clang
```

### Only authorized sandbox behavior probe

```text
$ /usr/bin/sandbox-exec -n no-network /usr/bin/true
exit=71
sandbox-exec: sandbox_apply: Operation not permitted
```

The command did not run `/usr/bin/true` under the named profile; profile
application failed. This is negative evidence against treating binary presence
as usable-backend evidence. It does not establish what a separately signed or
entitled context could do.

## 3. Candidate, identity, and disposition inventory

`runtime/package.json` and the lock root identify the sealed runtime workspace
as `@chirality/runtime-workspace@0.1.0`, Node engine `>=22.19.0`, lockfile
version `3`, with exact development packages `@types/node@24.12.4`,
`typescript@5.9.3`, and `vitest@3.2.7`. The local observation found Node
`v24.18.0` and npm `11.16.0`. No string naming `sandbox-exec`, `bwrap`,
`bubblewrap`, `nsjail`, `firejail`, `docker`, `podman`, `colima`, or
`qemu-system-aarch64` occurs in the sealed runtime package manifest or lock.
That absence is not a statement about operating-system packages.

| ID | Candidate visible in sealed evidence | Exact identity evidence | Present control/evidence | Gap and disposition |
|---|---|---|---|---|
| C-01 | macOS `/usr/bin/sandbox-exec` / named `no-network` profile | Host path and SHA-256 `e3d7…1d6`; macOS 26.6/arm64. API/version identity beyond the usage text in the earlier probe is `UNKNOWN`. | Binary present. Exact minimal probe attempted. | Profile application fails `Operation not permitted`, exit 71. No workload, rights, inheritance, packaging, signing, entitlement, or adversarial evidence. **`NOT_QUALIFIED`**. |
| C-02 | `bwrap` | `command -v` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; no sealed implementation or tests. **`NOT_QUALIFIED`**. |
| C-03 | `bubblewrap` | `command -v` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; no sealed implementation or tests. **`NOT_QUALIFIED`**. |
| C-04 | `nsjail` | `command -v` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; no sealed implementation or tests. **`NOT_QUALIFIED`**. |
| C-05 | `firejail` | `command -v` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; no sealed implementation or tests. **`NOT_QUALIFIED`**. |
| C-06 | Docker | `command -v docker` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; container/daemon topology and isolation are unproved. **`NOT_QUALIFIED`**. |
| C-07 | Podman | `command -v podman` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; container/VM topology and isolation are unproved. **`NOT_QUALIFIED`**. |
| C-08 | Colima | `command -v colima` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; VM/container topology and isolation are unproved. **`NOT_QUALIFIED`**. |
| C-09 | `qemu-system-aarch64` | `command -v` exit 1; package/API/version `UNKNOWN`. | None on this host. | Absent; VM boundary, guest image, and broker are unproved. **`NOT_QUALIFIED`**. |
| C-10 | Platform supporting tools: `codesign`, `security`, `spctl`, `launchctl`, `xcrun`, `clang` | Exact paths and SHA-256 values above; individual API/version identities were not authorized probes and remain `UNKNOWN`. | Presence only. | These tools are not shown as sandbox backends. No invocation, signed artifact, entitlement, profile, packaging, or product integration evidence. Each is **`NOT_QUALIFIED`** for any TM105 backend/control claim. |
| C-11 | Governed Agent-1 `read_file` tool bridge | Runtime workspace `0.1.0`; `RuntimeToolDefinition`; child selection fixed to `pi`/`omlx` plus requested model; descriptor grammar registry `harness-tools.v14.headless-preview-live`. | Exactly one relative file is canonicalized with `realpath`, checked contained, checked regular and <=1 MiB, then exposed through one allow/read root; Agent 2 has `allowedWriteTargets: []`; receipt and lifecycle evidence are required (`agent1-run-coordinator.ts:203-330,360-421,660-758`; tests `:225-388`). | One closure is not an OS sandbox. No native-tool negative corpus, stable file descriptor, race defense, process/network/IPC/device/credential containment, or actual adapter no-bypass evidence. **`NOT_QUALIFIED`**. |
| C-12 | Unix-domain HTTP daemon/control-plane broker | Node HTTP `createServer` listening at a configured Unix socket; `/v1` route prefix and tests expecting API `v1`; runtime package `0.1.0`. | Private runtime directory; socket and owner record mode tests at `0700`/`0600`; bearer-scope routing; project scoping; explicit stop/force/degraded states; stale-socket owner checks (`runtime-daemon.ts:1-188,230-488,520-803,879-1001`; `daemon.test.ts:220-330,423-560,559-983`). | This brokers control-plane calls; it is not tool OS containment. Socket/owner TOCTOU, OS peer credential binding, token replay/lifetime, provider topology, arbitrary subprocess cleanup, and packaged behavior are unproved. **`NOT_QUALIFIED`**. |
| C-13 | `domain_headless_preview_run` local-process broker descriptor | Tool registry `harness-tools.v14.headless-preview-live`; descriptor requires `open_pipe_stress`, an absolute executable path and exact lowercase SHA-256 via configuration. | Catalog prose says one foreground spawn, exact stdin bytes, bounded structured JSON stdout, no PATH lookup, shell, network, daemon, telemetry, output-path write, proposal, acceptance, or apply (`tool-catalog.ts:75-108`; `tool-descriptor.ts:811-848`). | The handler, runner binary/package/version, configuration, process launcher, OS sandbox, denials, cleanup, and tests are outside the sealed set. Descriptor prose is candidate evidence only. **`NOT_QUALIFIED`**. |
| C-14 | PEC loopback HTTP proposal/validation wrappers | Tool registry `harness-tools.v14.headless-preview-live`; descriptor names `127.0.0.1` endpoint-allowlisted transport; no package/version identity in scope. | Separate mutate/read descriptors; limited declared methods; acceptance/application unavailable as tools; credentials described as local-environment sourced and omitted from results (`tool-catalog.ts:109-122`; `tool-descriptor.ts:850-980`). | Actual endpoint allowlist, authentication/RBAC, credential custody, loopback bypass, DNS/socket/redirect behavior, handler, and tests are outside the sealed set. **`NOT_QUALIFIED`**. |
| C-15 | Pi-native Read/Write/Edit/Bash inside per-run worker or total broker target | D-APP-84 records a current `0.82.0` App dependency/Root descriptor identity in conflict with D-APP-72's `0.80.10` authority identity; exact package bytes are not in this sealed set. Engine descriptors can carry optional `packageName`/`packageVersion` (`agent-engine-port.ts:14-30`). | Proposal inventories native session primitives and a target plane separation. | D-APP-84 is `AWAITING_RULING`, explicitly says no live OS sandbox exists, and grants no primitive, Bash, version, or topology effect. Version/support/supply-chain/packaging facts remain unresolved. **`NOT_QUALIFIED`**. |
| C-16 | Piping-local foreground structured CLI as a possible bounded tool operation | Consumer response identifies `openpipestress-runner` as foreground JSON I/O with optional explicit output and no declared network/daemon/telemetry/hidden write; no package/version bytes are in this sealed set. | Consumer-local implemented operation evidence. | It is explicitly not an agent harness; Piping reports no operative agent broker, run sandbox, bounded grants, or durable resume. Consumer-local claims do not qualify a generic Root backend. **`NOT_QUALIFIED`**. |

No candidate has packaging, signed-artifact, notarization, entitlement,
redistribution, support, security-update, or packaged-application availability
evidence in this sealed set.

## 4. Rights-grammar expressibility

The sealed code contains two non-identical vocabularies:

1. `ToolPermission` can say `allow|deny` for `read|write|shell|network`, with
   optional string roots (`engine.ts:8-19`).
2. `HarnessToolDescriptor` can annotate `read`, `workspace-write`, `network`,
   `shell`, `subagent`, `coordination`, and `danger`; five coarse path scopes;
   idempotence; concurrency; interrupt behavior; byte budgets; provenance;
   human gates; and model exposure (`tool-descriptor.ts:14-106`).

The vocabularies can describe some intended tool exposure, filesystem scope,
denial, audit, and interruption policy. In the sealed set they cannot express
or establish all of: executable identity, argv/env/cwd, process-tree limits,
UID/GID/capabilities, inherited descriptors, IPC namespaces/endpoints,
devices, DNS versus provider-only transport, credential injection/custody,
mount semantics, hardlinks, stable inode/file-descriptor binding, orphan
reaping, sandbox backend/profile/version identity, signed/entitled context, or
fallback prohibition. There is no sealed mapper proving descriptor policy is
the executing `ToolPermission`, and no OS-sandbox profile field. Human-gate and
`runtime.exposedToModel` metadata are not enforcement proof. This confirms the
AB-01 policy-mismatch and native-tool-bypass gaps; it does not resolve them.

## 5. Expected/actual denial matrix

“Expected” below is only the unruled candidate acceptance target recorded in
D-APP-84 §5 or a declared descriptor intent. It is not an adopted rights
grammar or requirement. “Actual” means only sealed implementation/test/host
evidence.

| Surface | Expected candidate denial/control evidence | Actual sealed evidence | Denial verdict and gap |
|---|---|---|---|
| Process execution/tree | Exact executable identity; child inheritance; bounded tree; no privilege widening/background orphan; timeout/interruption evidence. | `read_file` spawns no process. Headless-preview descriptor claims one SHA-pinned foreground process, but handler is absent. Daemon interrupts engine streams and force-closes sockets after 2 s plus 500 ms settlement, with degraded/failure states and tests. | No arbitrary tool subprocess, nested shell, fork/exec, setsid, daemonization, signal, inherited-FD, kill/reap, or post-parent orphan denial. Daemon transport cleanup is not process-tree containment. **Not established**. |
| Path canonicalization/containment | Exact RO/RW mounts; fail closed on resolution/canonicalization; stable profile identity. | `read_file` rejects absolute paths, resolves root and target through `realpath`, checks containment and a <=1 MiB regular file; project registration canonicalizes declared roots. | Useful bounded control for one file, not a mount. No path-negative tests in sealed Agent-1 tests. Mount/profile identity absent. **Partially expressed; not qualified**. |
| Symlink/hardlink/rename/race | Deny symlink, hardlink, rename and race escape; adversarial evidence. | `read_file` performs `realpath`, then `stat`, later `readFile(canonicalPath)` by pathname. Registry likewise stores canonical strings. Daemon stale recovery uses `lstat`/owner checks then path `unlink`. | No descriptor-pinned `openat`, no `O_NOFOLLOW`, no held descriptor/inode recheck, no hardlink/rename corpus. A check/use race remains plausible from the shown sequence. **Not established**. |
| General network | Default deny for tool DNS/socket/URL; no silent fallback. | Exact `sandbox-exec -n no-network /usr/bin/true` fails before workload execution. Web fetch/search descriptors are reserved/not exposed. | A failed profile application is not a network denial around a workload. Raw sockets, DNS, URLs, redirects, IPv4/IPv6, Unix sockets, and child inheritance untested. **Not established**. |
| Provider/model channel separation | Provider communication only through declared broker; tool network does not inherit it. | Engine selection carries adapter/provider/model; daemon brokers engine calls. PEC descriptor declares a loopback channel. Provider credential port returns a string/status. | Provider endpoint, process placement, channel ACL, DNS/socket ownership, redirects, and separation from tool execution are outside the sealed set. **Not established**. |
| IPC and device | Deny undeclared IPC, sibling-run access, device access, and signals. | Unix-domain daemon socket is mode `0600` and bearer-authenticated in tests; owner record is mode `0600`. | This is one intended control-plane IPC surface, not a sandbox IPC allowlist. No peer-credential binding, sibling IPC, shared memory, Mach service, inherited socket, device, keychain, TTY, signal, or debugger denial evidence. **Not established**. |
| Credentials/environment | Credentials not ambient; brokered and redacted; deny environment/HOME/keychain leakage. | Daemon routes credential status/set/remove under scopes; `ProviderCredentialPort.get` returns a raw string; proposal says credentials should not be ambient but is unruled. AB-01 records plaintext bearer-token files and unknown provider storage. | Credential-store implementation, worker environment, redaction on every channel, memory/log/error/backup handling, token lifetime/audience, keychain and inherited-env denial are absent. **Not established**. |
| Orphan and shutdown cleanup | No background orphan; interruption and cleanup terminal evidence; no stale authority reuse. | Daemon tracks connections/streams, closes admission, requests interruption, force-destroys transport, removes owned socket/owner records, marks degraded/failure, and tests disconnect, stop, restart, late generation events, residual sockets, and foreign owner preservation. Agent-1 interruption updates child/manager records. | Strong candidate control-plane transport evidence, but arbitrary worker/tool process descendants and resources are not enumerated or reaped in scope. Pre-identity cancellation can terminate degraded without semantic interrupt. **Transport covered in fixtures; tool orphans not established**. |
| Native/tool bypass | Unrequested SDK/native tools, alternate implementations, unsandboxed fallback, and `dangerouslyDisableSandbox` denied at the executing boundary. | Descriptor lookup rejects duplicate aliases and enumerates disallowed tool names; network/notebook/multi-edit/subagent descriptors are parked; Agent-1 binds only one closure. D-APP-84 says current lexical shell policy is not containment and records no live sandbox. | Actual adapter wrapper, `request.opts.tools` widening defense, raw SDK alias denials, shell policy, broker handler, and unsandboxed-fallback tests are outside the sealed set. **Not established**. |
| Rights/audit binding | Stable backend/profile/version identity in session/tool/resume/audit and per-operation denial receipt. | Runtime fingerprint has generic policy version strings and optional engine package identity; tool descriptors declare provenance; read bridge emits permission/start/completed events. | No sandbox backend/profile identity exists. No proof descriptor decision equals OS-enforced result. Denial receipts for OS resources absent. **Not established**. |

## 6. Candidate-specific gaps and still-required adversarial acquisition corpus

These are evidence acquisitions, not recommendations or implementation
instructions.

| Candidate group | Candidate-specific controls already visible | Evidence still required before any possible qualification |
|---|---|---|
| C-01 `sandbox-exec` | Present exact binary; failed named-profile probe. | Declared signed/entitled and packaged contexts; backend/profile API and version identity; deterministic profile construction; exact mount/path results; unsupported-context fail-closed behavior; subprocess inheritance; symlink/hardlink/rename races; inherited FDs; env/HOME/keychain; Mach/Unix/TCP/DNS/URL/device/signal access; provider-broker-only channel; daemonized orphan cleanup; evidence capture and restart. |
| C-02–C-09 absent backends/wrappers | Absence is established only on this host. | Reproducible declared platform images; exact packages/binaries/digests/licenses; backend APIs; host/guest or daemon topology; kernel/virtualization prerequisites; rootless/privileged behavior; mounts, devices, IPC, network, credentials, cgroups/job control, cleanup; packaged distribution and update evidence. No install is authorized by this return. |
| C-10 platform tools | Exact present paths/digests. | Their exact role, APIs, versions, signing identities, entitlements, invocation results, packaged availability, and relationship to a chosen backend. Presence alone supplies none. |
| C-11 `read_file` broker | Relative realpath containment, one file, size/type check, read-only closure, empty write targets, receipt, interruption status. | Negative absolute/traversal/symlink/hardlink/rename/swap/race tests; stable descriptor/inode enforcement; unreadable/special/device/FIFO/socket tests; all SDK/MCP/native aliases; writes/shell/network/subagent attempts; concurrent re-registration/root mutation; real adapter execution; durable no-side-effect denial receipts. |
| C-12 Unix daemon broker | Unix socket, file modes, bearer scopes, project visibility, body limit, lifecycle/transport cleanup fixtures. | Socket-directory ownership/ACL and peer credentials; symlink/replacement races; owner-record authenticity/rollback; PID reuse; cross-user/cross-project/replay/concurrency corpus; token expiry/audience/rotation; credential canaries; request smuggling/encoded route corpus; packaged launch/restart/crash/orphan behavior; arbitrary worker process/resource reconciliation. |
| C-13 headless process broker | Descriptor declares absolute SHA pin, foreground process and bounded JSON channel. | Actual handler and exact runner artifact/package/version; pre-exec revalidation without path race; argv/env/cwd/FD specification; stdin/stdout/stderr budgets; timeout/cancel/kill-tree/reap; network/IPC/device/credential denial; malformed/oversize/trailing output; executable replacement; signed/package contexts; durable denial/evidence fixtures. |
| C-14 PEC loopback broker | Descriptor separates mutate/read and names endpoint allowlisting. | Actual handler, exact endpoints/methods, authentication and actor binding, redirect refusal, IPv4/IPv6/DNS/socket rules, cross-project/RBAC negatives, credential custody/redaction, CSRF/confused-deputy/replay behavior, service discovery/start/stop, audit persistence, and packaged topology. |
| C-15 Pi-native target | Proposal states non-bypass/fail-closed targets and version conflict. | Owner ruling if any; exact accepted Pi package/version/digest/license/supply chain; native API inventory at that exact version; wrapper/broker code; unsandboxed/native alias negatives; per-role/run separation; all D-APP-84 §5 escape cases; packaging/signing/entitlement; no-fallback evidence; Root/App independent conformance. |
| C-16 Piping CLI | Consumer reports bounded foreground structured I/O. | Current exact binary/package/version/digest and consumer-owned conformance; broker binding; OS containment; interrupt/recovery/budget/evidence behavior; UI/API equivalence; no fixture-fallback success; product-local authorization. None may be generalized from the coordination response. |

The adversarial corpus remains required across, at minimum: absolute and
relative path escape, symlink, hardlink, rename/swap races, inherited file
descriptors, environment/HOME/keychain, special files/devices, nested shell,
fork/exec/setsid/daemonization, signals/debugging, sibling runs, Unix/Mach IPC,
shared memory, IPv4/IPv6/DNS/URL/redirect, provider-only channel separation,
credential canaries, output/body/event budgets, cancellation at every phase,
backend/profile creation failure, crash/restart, cleanup failure, and all
native/SDK/MCP aliases. No such complete corpus is in the sealed set.

## 7. Conflicts, non-coverage, and `UNKNOWN` facts

1. D-APP-84 records Pi `0.82.0` in current dependency/descriptor surfaces but
   D-APP-72 authority at `0.80.10`; D-APP-84 is an awaiting-ruling proposal and
   explicitly creates no version effect. This return does not resolve the
   conflict.
2. Descriptor prose says read/write/shell tools are exposed behind overlays,
   hooks, timeouts, and policies, while the actual adapter invocation wrapper
   is not sealed. Those statements remain candidate implementation claims.
3. The engine permission grammar and harness descriptor grammar differ. No
   sealed translation or end-to-end OS enforcement joins them.
4. `read_file` canonicalization is stronger than a lexical check, but its
   pathname check/use sequence and the absence of adversarial tests prevent a
   race-safe claim.
5. Daemon lifecycle tests establish the named in-process fixtures, not worker
   process-tree containment or deployed orphan cleanup.
6. Piping explicitly reports no application-owned operative agent harness,
   run sandbox, native-tool broker, durable resume, or completed bounded grants;
   its CLI and proposal panel cannot be promoted into those roles.
7. The current host is not an installed-dependency witness per the earlier
   local probe. No product tests or dependency install were authorized or run.

The following remain **`UNKNOWN`**: accountable backend/runtime/security/
packaging owners; vendor support and commitments; licenses and redistribution
rights; security-update channels; platform support matrix; minimum OS/kernel;
signed/notarized/entitled behavior; packaged app availability; deployment and
provider topology; trusted OS users/services; UID/GID and peer-credential
policy; credential custodian/store/redaction/lifetime; acceptable isolation;
device and IPC policy; network destinations; incident/monitoring/backup
controls; exact Pi accepted version; and whether any candidate can meet a
future governed acceptance contract.

## 8. Separately owned acquisition actions

These are acquisition actions only, not backend, topology, rights-grammar,
control, policy, product, or implementation recommendations.

| Evidence workstream | Accountable owner | Separately owned acquisition action |
|---|---|---|
| OS/platform backend | `UNKNOWN` | Produce exact platform matrix, backend binary/package/API/profile identity, license/support/update evidence, signed/entitled and packaged-context observations, and the complete isolation/escape corpus with raw denials and side-effect checks. |
| Runtime rights grammar | `UNKNOWN` | Produce the mapper from public descriptor and grant to executing `RuntimeToolDefinition` and OS profile, including process, path/inode, network/provider, IPC/device, credential, cleanup, version identity, and denial-receipt fields plus invalid/unexpressible-case tests. |
| Adapter/native enforcement | `UNKNOWN` | Produce actual Pi/SDK preflight, tool-resolution, hooks/broker, shell policy, and real-adapter negative traces for all aliases, widening attempts, unsandboxed fallback, and changed implementation family. |
| Local process broker | `UNKNOWN` | Produce the `domain_headless_preview_run` handler, exact pinned runner artifact, launcher/kill/reap implementation, budgets/redaction, and adversarial path/process/network/credential/cancellation evidence. |
| Daemon/control topology | `UNKNOWN` | Produce deployed and packaged topology, OS peer/auth binding, owner/socket race and PID-reuse corpus, crash/restart reconciliation, token and credential lifecycle, and worker/process resource cleanup evidence. |
| Provider/credential channel | `UNKNOWN` | Produce exact provider endpoint and broker topology, destination/channel allowlist, tool-network separation, credential store/injection/redaction design evidence, and secret-canary tests across errors/events/logs/artifacts. |
| Piping-local affected client | Specific human owner `UNKNOWN`; owning Piping instruments identified in its response | Refresh current broker/grant/API/plugin/guard/fixture/equivalence evidence at the Piping cadence and return consumer-local facts without generic promotion. |
| App affected client | Specific human owner `UNKNOWN`; D-APP-84 remains awaiting ruling | Reconcile authoritative version identity and, only under separately granted authority, acquire exact native API, package/supply-chain, sandbox, packaging, and Root/App conformance evidence. |

## 9. Hold preservation and terminal return

Every candidate disposition is **`NOT_QUALIFIED`**. No backend, topology,
rights grammar, platform pair, vendor, trusted principal, credential custody,
isolation guarantee, control, contract candidate, semantic selection, or
no-TBD successor is chosen or drafted.

All semantic, implementation, client-acceptance, lifecycle, release, reliance,
publication, Git/PR, register, receipt, notice, and byte-gate holds remain
intact. This evidence return authorizes no host change, daemon start, product
test, install, remote-provider access, source change, state transition, or
downstream reliance and has no authority effect beyond returning bounded
evidence to the parent under the sealed brief.
