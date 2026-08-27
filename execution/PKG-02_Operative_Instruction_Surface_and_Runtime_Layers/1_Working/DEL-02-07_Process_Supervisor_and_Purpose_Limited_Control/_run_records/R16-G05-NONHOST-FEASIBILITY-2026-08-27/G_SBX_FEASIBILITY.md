# R16 N3.1 — G-SBX bounded feasibility evidence

- Date: 2026-08-27
- Node: `N3.1`
- Primary carrier: `DEL-02-07`
- Calibrated state: `SUPPORTED_FOR_DESIGN`
- Gate status: feasibility evidence only; `G-SBX` has not passed
- Exact App Server payload SHA-256:
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`

## Basis and execution boundary

The exact accepted OpenAI App Server 0.149.0 arm64 payload was executed only
after N0 commit `9164d95456bd67576a1b1164fd08e52516edb368` and its pushed
proof commit `0246e92b4bfede52c226d58122e8ac4bb980e666`. Its fresh release
asset and payload identities were verified before execution. Every invocation
used a fresh `mktemp` root, `/usr/bin/env -i`, a non-login shell, a disposable
`HOME`, `CODEX_HOME`, and `TMPDIR`, a system-only `PATH`, and a macOS Seatbelt
outer profile that:

1. denied all network operations;
2. denied all writes except beneath the fresh disposable root;
3. denied reads beneath `/Users/ryan`; and
4. denied lookup of `com.apple.securityd`.

No credential, token, account, Keychain operation, device-code flow, network
approval, host mutation, product configuration, or production implementation
was used. The vendor process had no authority to complete an external
connection.

## Exact observations

The final successful fresh probe root was
`/private/tmp/chirality-r16-g-sbx.46AYwj`; it was mode `0700` and is disposable,
not evidence.

| Probe | Exact result |
|---|---|
| fail-closed egress preflight | `nc -z -v -G 1 1.1.1.1 443` exited `1`; stderr was `nc: connectx to 1.1.1.1 port 443 (tcp) failed: Operation not permitted`; no connection completed |
| allowed disposable-root write | `touch <probe-root>/work/inside-write` exited `0` |
| denied outside-root write | `touch /private/tmp/chirality-r16-g-sbx-outside-65707` exited `1` with `Operation not permitted`; target remained absent |
| denied real-home read | `head -c 1 /Users/ryan/.codex/worktrees/0b6e/chirality/AGENTS.md` exited `1` with `Operation not permitted`; stdout length was zero |
| exact App Server startup | exited `0`; stdout length `23009`; stderr length `0` |
| exact pin readback | initialization reported `0.149.0`; `config/read` reported `sandbox_mode=workspace-write`, `network_access=false`, `exclude_tmpdir_env_var=true`, `exclude_slash_tmp=true`, `allow_login_shell=false`, and session `features.plugins=false` |

Durable observation identities captured before cleanup:

| Transient observation | SHA-256 |
|---|---|
| App Server JSONL stdout | `895bb761353a1be479c28ce909bd2d0022e83aaecfa9e3a77a7af2b3d9511fd5` |
| App Server stderr (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| denied-egress stderr | `b66318a4e27ea144257f9cf29ff0ab556f6b196cbe531a5a1ebed9c305b47f49` |
| denied-outside-write stderr | `bbb6b1007080d5ec4f0b369b20c219a19fcec915ab79f764e0f6019450ca0ad3` |
| denied-home-read stderr | `ec32b79221d29303f1708d407a0af16c6fd7ab3c9a915d51853de43287ef5268` |
| sorted final disposable inventory | `f4ee4a0dfb896cecff0021281f037200af2dbddedc33cc549a5b662503755634` |

## Calibration by required property

| Required property | Result in this tranche |
|---|---|
| hard outer root-only write boundary | directly supported for design by the allowed in-root and denied outside-root probes |
| hard outer real-home read exclusion | directly supported for design by the denied read probe |
| hard outer command-network denial | directly supported for design by the fail-closed egress preflight and successful exact-binary startup inside the same profile |
| configuration for `/tmp` and `$TMPDIR` exclusion | configuration-asserted by exact-pin `config/read`; actual model/tool enforcement remains unavailable |
| `includePlatformDefaults: false` on production `turn/start` policy | `UNAVAILABLE_UNDER_BOUNDS`; no authenticated turn was permitted, and `command/exec` is not an acceptable substitute |
| exact immutable runtime-read inventory | `UNAVAILABLE_UNDER_BOUNDS`; this probe establishes absence of real-home dependence, not an exhaustive packaged runtime-read allowlist |
| client process/shell surface denial | `UNAVAILABLE_UNDER_BOUNDS`; the raw App Server contains client process/shell methods, while the product IPC denylist and renderer boundary are unimplemented/withheld |
| packaged Electron fuse/entitlement and signed-bundle posture | `UNAVAILABLE_UNDER_BOUNDS` as R16 expressly directs |

## Verdict and implementation implication

`SUPPORTED_FOR_DESIGN` is limited to the non-packaged hard-outer containment
limb. The exact binary can initialize and return effective configuration while
network, real-home reads, securityd lookup, and outside-root writes are denied.
This is useful feasibility evidence for a wrapper/supervisor design, but it is
not proof of the production per-turn sandbox.

A later authorized implementation must bind the final release-plan
`workspaceWrite.readOnlyAccess` or restricted `readOnly.access` object to every
actual `turn/start`, set `includePlatformDefaults: false`, freeze an exhaustive
immutable runtime-read allowlist, deny `/tmp` and the effective `$TMPDIR` for
model/tool actions, and make process/shell methods unreachable at the product
client boundary. Packaged primary and descendant canaries plus fuse,
entitlement, and signature checks remain mandatory before `G-SBX` can pass.

## Repair cycle

The first local attempt was blocked by the calling tool's own outer sandbox:
nested `sandbox-exec` returned `sandbox_apply: Operation not permitted`; no
vendor execution occurred. The first authorized outer invocation then failed
closed at config loading because its inherited cwd was under the deliberately
denied real home. A fresh repair changed cwd to the disposable `work/` root and
placed `config.toml` directly in the disposable `CODEX_HOME`; that invocation
exited `0`. The final evidence run repeated the repaired construction in a new
fresh root and passed all preconditions and observations above.
