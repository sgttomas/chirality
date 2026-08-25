# OUT-002 Destination Inventory and Policy Handoff

**State:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

This is the exact destination delta observed while generating supply evidence.
It is routed input to DEL-02-08 OUT-002 and the App OUT-002/G-ENV lane, not an
adopted endpoint policy and not command-network authority.

## Sandbox-denied attempted destinations

| Exact destination | Triggering operation | Disposition |
| --- | --- | --- |
| `https://chatgpt.com/backend-api/plugins/featured?platform=codex` | warm featured-plugin IDs cache during normal plugin startup | `SANDBOX_DENIED_NO_COMPLETED_CONNECTION` |
| `https://api.github.com/repos/openai/plugins` | curated-plugin GitHub HTTP sync after local `git` was unavailable | `SANDBOX_DENIED_NO_COMPLETED_CONNECTION` |
| `https://chatgpt.com/backend-api/plugins/export/curated` | curated-plugin export-archive fallback | `SANDBOX_DENIED_NO_COMPLETED_CONNECTION` |

The complete trace for all three is
`03_EMPIRICAL_EVIDENCE/raw/stable.stderr.jsonl.gz`, pinned through
`03_EMPIRICAL_EVIDENCE/ARTIFACT_HASHES.csv` SHA-256
`66453d9bfb62cb61edf10387ac11c76214209ab9d48e8907b0c39f49dd0a43a0`.

## Configured but not attempted

`https://chatgpt.com/backend-api/` was logged as the remote-control base. The
artifact waited for authentication; it made no connection attempt and issued
no credential prompt. It is therefore not part of the denied-attempt count.

## Switch result

`features.plugins` is the exact 0.149.0 whole-plugin feature switch. Baseline
runtime readback is `enabled=true`, `defaultEnabled=true`; the explicit
session override reads back `false` and suppressed all observed plugin startup
attempts. The current official configuration reference documents no dedicated
curated-sync-only switch.

## Policy boundary

- This inventory grants no network access and no destination approval.
- It does not conflate these plugin destinations with command-network consent.
- It does not claim the full accepted OUT-002 account/model/turn endpoint
  enumeration is complete; it supplies the three newly observed plugin
  destinations and one configured-not-attempted base for downstream treatment.
- App adoption, amendment, or rejection remains an App-loop act.
- The Root owner separately accepts or rejects this candidate at G2.
