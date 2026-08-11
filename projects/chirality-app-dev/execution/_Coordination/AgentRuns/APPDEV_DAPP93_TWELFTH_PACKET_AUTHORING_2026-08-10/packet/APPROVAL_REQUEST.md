# Frozen Packet Index and Approval Request

## Authority state

This packet is unexecuted. No execution authority exists until the owner approves the final manager-frozen aggregate packet SHA-256 exactly. Step 0 and every operative step are forbidden before that approval. Approval of a different identity does not authorize this packet.

## Packet index

The other five packet components are indexed below. The manager will replace each placeholder only after fan-in acceptance, as part of the freeze act.

| Component | Packet-relative path | Frozen SHA-256 |
| --- | --- | --- |
| Owner runbook | `OWNER_RUNBOOK.md` | `TO_BE_FROZEN_BY_MANAGER` |
| Environment preflight script | `scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh` | `TO_BE_FROZEN_BY_MANAGER` |
| Evidence capture script | `scripts/CAPTURE_TRACE_EVIDENCE.zsh` | `TO_BE_FROZEN_BY_MANAGER` |
| Evidence capture form | `EVIDENCE_CAPTURE.md` | `TO_BE_FROZEN_BY_MANAGER` |
| Ledger citation | `LEDGER_CITATION.md` | `TO_BE_FROZEN_BY_MANAGER` |

- Final aggregate packet SHA-256: `TO_BE_FROZEN_BY_MANAGER`

The manager will replace placeholders only after acceptance and will then freeze the aggregate identity. No placeholder replacement by the author constitutes acceptance or authority.

## Probe-tier summary

- `AGENT_PROVEN`: `/bin/zsh`, `/usr/bin/lldb` neutral `--version`, `/usr/bin/shasum`, and the `/usr/bin/perl` interpreter chain are pinned and subject to the manager's probe requirements. The operative LLDB attach remains `REVIEWED_NOT_EXECUTED` during preparation.
- `OWNER_PREFLIGHT`: `/bin/ps` is pinned at SHA-256 `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c`; its agent-sandbox probe denial was exit `127`, operation not permitted. Step 0 requires the owner to prove its expected exit `0` and numeric output in the real environment before any operative act.

## Exact approval requested

After manager acceptance, freeze, and verifier PASS, request owner approval only for the exact aggregate SHA-256 written above. Until that exact approval is recorded, keep the packet at the approval gate and do not run Step 0.
