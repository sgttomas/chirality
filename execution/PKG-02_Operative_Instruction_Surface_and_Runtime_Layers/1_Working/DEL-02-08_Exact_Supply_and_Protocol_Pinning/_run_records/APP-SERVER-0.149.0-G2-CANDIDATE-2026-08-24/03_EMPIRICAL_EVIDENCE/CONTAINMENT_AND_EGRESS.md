# Containment and Egress Evidence

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Exact executable fence

| Executable | Invocation purpose | SHA-256 |
| --- | --- | --- |
| `codex-app-server` | version, help, JSONL config/feature probes, negative schema/type command probes | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` |
| `codex-code-mode-host` | ancillary help/entrypoint inventory only | `8f9f6969cd5e69540482d58791f72e4e9b9888e576ae3ad446c422a058b70128` |

The frozen package `rg` and `zsh` members were not executed: neither can emit
App Server protocol schema/types or app-server configuration readback, so
running them would not serve R14-B's bounded purpose.

## Sandbox envelope

The nine complete per-run gate records identify `network-deny.sb`, SHA-256
`17a579161aa13d50b1f5f735c48408ce2ae45000a6fd1a26a4a0d58a045676ab`.
The profile allows the host defaults needed to load the Mach-O, denies all
network and file writes, re-allows writes only under the disposable root,
denies reads of the real user home, and denies lookup of
`com.apple.securityd`. Nine of the ten
vendor invocations have both a committed per-run executable/profile hash
record and a run-specific sandboxed TCP-connect denial record returning
`Operation not permitted`. The `version` run has captured stdout/stderr and
empty preflight files, but no committed per-run gate-hash record and no
attributable denial result. One additional standalone denial record exists,
but it cannot be deterministically attributed to that run.
`EXECUTION_GATE_INVENTORY.json` records the nine complete gates and the one
evidence gap. No new vendor execution is authorized to fill it.

The recorded invocation construction cleared the vendor environment with
`/usr/bin/env -i` and supplied only the disposable `HOME`, `CODEX_HOME`,
`TMPDIR`, a system-only `PATH`, `C` locale, dumb terminal, and—for JSONL
runs—structured logging settings. No committed trace records inherited
credential, token, account, proxy, or approval input. Standard input for the
JSONL runs was fixed local JSONL. No committed trace records a login,
device-code, account, or approval method invocation.

## Sandbox-denied egress inventory

| Exact destination | Triggering operation | Result |
| --- | --- | --- |
| `https://chatgpt.com/backend-api/plugins/featured?platform=codex` | warm featured-plugin IDs cache during normal plugin startup | sandbox denied; request failed; no connection completed |
| `https://api.github.com/repos/openai/plugins` | curated-plugin GitHub HTTP sync after local `git` was unavailable | sandbox denied; request failed; no connection completed |
| `https://chatgpt.com/backend-api/plugins/export/curated` | curated-plugin export-archive fallback | sandbox denied; request failed; no connection completed |

The full structured trace is `raw/stable.stderr.jsonl.gz`; the structured
inventory is `DENIED_EGRESS_INVENTORY.json`. The app-server also logged the
configured remote-control base `https://chatgpt.com/backend-api/`, but it
repeatedly waited for authentication and made no connection attempt. That URL
is therefore recorded separately as configured-not-attempted, not falsely
promoted to the denied-attempt set.

No committed trace records a completed connection, credential prompt, login or
device flow, `auth.json` file, approval grant, or write outside disposable
state. R14 admits the three denied attempts as inventory; no other containment
exception is evidenced.
