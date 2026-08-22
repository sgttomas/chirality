# Return — fresh post-Root DEL-08-04 integration review

Verdict: `PASS`

Actionable findings: `0`

The accepted attempt-2 executor evidence and all three frozen DEL-08-04
candidate truth edits satisfy the owner-enumerated Node 1 contract. Attempt 1
is rejected and supplies no acceptance evidence. This review makes no repair,
product, Root, lifecycle, reliance, release, publication, or Git-closeout act.

## Criterion results

| # | Criterion | Independent result |
|---:|---|---|
| 1 | Canonical TASK and explicit-generalist admission | `PASS` — live `AGENT_HELP_HUMAN.md` has canonical `TASK` in `subagents` and `allow_generalist_agent2: true`; Root hierarchy validation admits canonical TASK, while App managed launch directly tests both TASK admission and generalist denial-before/admission-after explicit opt-in. Enumeration remains distinct from launch and does not synthesize TASK eligibility. |
| 2 | Required fail-closed routes | `PASS` — direct Root/App evidence covers unsupported named Agent 2, unresolved instruction/role, missing generalist opt-in, Agent-2-parent delegation, and missing/noncanonical TASK class. |
| 3 | Checks and App source identity | `PASS` — accepted executor recorded Root `34/0/0`, Root tests `19/19`, App files `19/19` and `11/11`, combined `30/30`. Reviewer rerun reproduced Root `34/0/0`, Root `19/19`, and combined App `2 files / 30 tests`, all exit 0. The Receipt-172 four-file diff from `ac2cd801a06a0679bc86830c627218ccca78b658` through `HEAD` is empty. |
| 4 | Attempt/preflight integrity | `PASS` — attempt 1 is `REJECTED_PRECONDITION`, `acceptedForFanIn: false`, and contributes no evidence. Attempt 2 follows the recorded APP-HOLD `ALLOW` for clear/not-held DEL-08-04 and has a complete PASS return/status. |
| 5 | DEL-08-04 state edit | `PASS` — only the satisfied post-Root Remaining bullet is removed; the D-APP-103 packet bullet remains. `IN_PROGRESS`, Authorization Basis, Directive, Last Updated, and Checking Approval SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` reproduce the predecessor bytes. |
| 6 | TM125 acknowledgment | `PASS` — `_STATUS.md`, `MEMORY.md`, and the new deliverable run record consistently disposition the routed notice as `INCORPORATED` under the owner-adopted App iteration, with no Root or duplicate implementation write. |
| 7 | Claim calibration and handoff facts | `PASS` — claims are limited to validation; the run record explicitly identifies derivative evidence, the surviving D-APP-103 residual, no task-local blockers, change-triggered reruns, and all prohibited lifecycle/release/reliance effects. |
| 8 | Containment, hygiene, parse, and hashes | `PASS` — the candidate DEL-08-04 diff contains only `_STATUS.md`, `MEMORY.md`, and the new run record; concurrent TM-APP-032 paths are disjoint. No path is staged, tracked diff hygiene passes, manager JSON/JSONL parses, and every frozen hash reproduces exactly. |

## Frozen identity backcheck

| Artifact | Observed SHA-256 | Result |
|---|---|---|
| Attempt-2 executor `RETURN.md` | `3f51c39e3ddd386da9f34804f6f2379da69f42972821945a781c3248927b070f` | exact |
| DEL-08-04 `_STATUS.md` | `0a60e895113bcfdf530e9c27b260ece9e7364b91a955523d1d2a4eeb6f2ac9bb` | exact |
| DEL-08-04 `MEMORY.md` | `815414626a592c8c1738bef7928004dacc81aae35d37d718cd0963af10eb6407` | exact |
| DEL-08-04 post-Root run record | `e5967b3eeac426807a4d6ecf8ad47a87b23055a9e1ad0707411bf32bd005f0f3` | exact |
| Live `AGENT_HELP_HUMAN.md` | `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` | exact |
| TM125 routed notice | `eb765dc3bebbf9dd84842643fb22aa989539513843647b562098c96468547864` | exact |

Accepted basis also reproduces: branch `codex/app-post-root-login-proof`,
`HEAD == origin/main == 1b375af4f1219ecfc00fc2755854aa7fd4220901`,
with PR #602 merge `adf805e0d9ac55787e8ac815c3018467babb7f50` and App
implementation `ac2cd801a06a0679bc86830c627218ccca78b658` both ancestors.

## Disposition

- Findings: none.
- Blockers: none for this Node 1 validation integration.
- Required reruns: none on unchanged Root/App inputs; rerun the same matrix if
  the Root validator/instructions or either affected App source/test changes.
- Derivative status: this review and the accepted executor package are
  derivative validation evidence and do not replace Root instruction truth,
  App product truth, Receipt 172, or DEL-08-04 lifecycle truth.

