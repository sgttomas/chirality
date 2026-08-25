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

Every vendor run used `network-deny.sb`, SHA-256
`17a579161aa13d50b1f5f735c48408ce2ae45000a6fd1a26a4a0d58a045676ab`.
It allows the host defaults needed to load the Mach-O, denies all network and
file writes, re-allows writes only under the disposable root, denies reads of
the real user home, and denies lookup of `com.apple.securityd`. Before each
vendor invocation, a sandboxed TCP connect to `1.1.1.1:443` failed with
`Operation not permitted`. `EXECUTION_GATE_INVENTORY.json` records all ten
gates.

The vendor environment was cleared with `/usr/bin/env -i` and contained only
the disposable `HOME`, `CODEX_HOME`, `TMPDIR`, a system-only `PATH`, `C`
locale, dumb terminal, and—for JSONL runs—structured logging settings. No
credential, token, account, proxy, or approval input was inherited. Standard
input was fixed local JSONL. No login, device-code, account, or approval method
was invoked.

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

There were zero completed connections, zero credential prompts, zero login or
device flows, zero `auth.json` files, zero approval grants, and zero writes
outside disposable state. R14 admits the three denied attempts as inventory;
no other containment exception was used.
