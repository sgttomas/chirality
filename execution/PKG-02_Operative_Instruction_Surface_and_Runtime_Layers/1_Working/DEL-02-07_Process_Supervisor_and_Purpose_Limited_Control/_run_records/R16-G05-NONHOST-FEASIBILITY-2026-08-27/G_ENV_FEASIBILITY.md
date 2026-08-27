# R16 N3.3 — G-ENV bounded feasibility evidence

- Date: 2026-08-27
- Node: `N3.3`
- Primary carrier: `DEL-02-07`
- Calibrated state: `SUPPORTED_FOR_DESIGN`
- Gate status: feasibility evidence only; `G-ENV` has not passed
- Exact App Server payload SHA-256:
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`

## Method and containment

After pushed N0, the exact accepted 0.149.0 payload ran in the same
fail-closed macOS outer profile described in `G_SBX_FEASIBILITY.md`: no
network, no `/Users/ryan` read, no write outside the disposable root, and no
securityd lookup. The final fresh root was
`/private/tmp/chirality-r16-g-env.29D2aB` with mode `0700`. Invocation used
`/usr/bin/env -i` and a non-login shell from the disposable `work/` cwd. No
plist, launchd, LaunchAgent, installer, daemon, host config, credential,
account, or production surface was touched.

## Exact effective environment

The exact environment passed to the vendor process contained only:

```text
CODEX_HOME=/private/tmp/chirality-r16-g-env.29D2aB/codex-home
HOME=/private/tmp/chirality-r16-g-env.29D2aB/home
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin:/usr/sbin:/sbin
TERM=dumb
TMPDIR=/private/tmp/chirality-r16-g-env.29D2aB/tmp
```

There was no inherited token, credential, account, proxy, socket, SSH, cloud,
CI, or user-profile variable. Effective-environment SHA-256 was
`de6bc9ab7f18971ee4f3eb3af9733e95426564f8b54eaaa2d7863271c6b3302e`.
The outer profile separately made the real home unreadable and securityd
unreachable.

## Exact observations

| Observation | Result |
|---|---|
| egress preflight | exit `1`, `Operation not permitted`; no completed connection |
| App Server | exit `0`; stdout `23009` bytes; stderr `0` bytes |
| startup identity | `chirality_root_supply_probe/0.149.0`; disposable `codexHome` |
| login shell posture | exact-pin readback `allow_login_shell=false` |
| command network posture | exact-pin readback `sandbox_workspace_write.network_access=false` |
| temporary-root posture | exact-pin readback `exclude_slash_tmp=true` and `exclude_tmpdir_env_var=true` |
| update/web/telemetry posture | `check_for_update_on_startup=false`, `web_search=disabled`, analytics and feedback disabled |
| timeout surface | readback exposed `background_terminal_max_timeout=300000`; no production supervisor/job timeout was inferred |
| root-local state | all App Server databases, skills, logs, and scratch were created only beneath the mode-`0700` disposable root |

Transient observation identities captured before cleanup:

| Observation | SHA-256 |
|---|---|
| App Server stdout | `e68e611fcfc300e217f6184022d873756f0cfdffc8aaac70fa42aa2e107aa65d` |
| App Server stderr (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| denied-egress stderr | `b66318a4e27ea144257f9cf29ff0ab556f6b196cbe531a5a1ebed9c305b47f49` |
| sorted pre-run inventory | `5d4a3d4da2e21c10699ff4c1b12391b1471912c9aad4e3a5fdd6f0424011e071` |
| sorted post-run inventory | `c95f3004c18a64f709bc3ff3fa9db8ce8c12285cbe2b8a011b3e062351df8168` |

## Verdict, limitations, and implication

`SUPPORTED_FOR_DESIGN` applies to the disposable server/worker environment
limb: an exact allowlist environment, non-login invocation, hard outer network
and home exclusion, and root-local private state are compatible with exact
App Server initialization. The readback also carries the required network,
temporary-root, and login-shell posture.

This does not prove effective plist/launchd or supervisor behavior, packaged
bypass resistance, client/model enforcement of temporary-root denial,
production timeout/termination behavior, or actual-turn primary/descendant
inheritance. Those claims remain `UNAVAILABLE_UNDER_BOUNDS` because R16
forbids host mutation, product implementation, live authentication, and the
necessary packaged/actual-turn execution.

A future authorized supervisor must construct an equally closed environment,
create a root-local `0700` scratch container, bind explicit job/turn timeouts,
deny login shells and ambient home/secret inheritance, and clean worker state
on termination. It must then prove launchd/plist and packaged bypass behavior
without relaxing the hard outer boundary.

## Repair cycle

The calling tool's outer sandbox initially blocked nested Seatbelt setup, so
that attempt performed no vendor execution. The first authorized invocation
then returned config-load `Operation not permitted` because cwd still pointed
into the denied real home. A fresh repaired invocation moved cwd and
`CODEX_HOME` wholly beneath the disposable root and exited `0`. A third fresh
run added a three-second JSONL drain so every read request completed; it is the
final evidence run recorded here.
