# REPAIR — cycle 1 — A2-PKG09-R20-IMPLEMENT-01

Verdict: `BLOCKED_REQUIRED_CHECK_FAILED`

Basis: immutable review
`instances/A2-PKG09-R20-REVIEW-01/REVIEW.md`, SHA-256
`0134c2db5a9255236171880b95f66a5d93292cd41f71be458dc853dc5636ef76`,
plus `ORCHESTRATION_PLAN_V2.md`, `WORK_GRAPH_V2.json`, and sealed brief
`briefs/A2-PKG09-R20-REPAIR-01.md`.

The original implementation evidence remains unchanged. The accepted
predecessor hashes were independently confirmed before repair.

## Five-finding closure matrix

| Finding | Repair attempted | Deterministic coverage authored | Cycle-1 disposition |
|---|---|---|---|
| F-01 | Final PASS is assigned before best-effort PASS-only failed-log deletion; deletion failure cannot append a cleanup error or retroactively create FAIL. | Injected deletion failure expects irrevocable PASS and intact copies. | `IMPLEMENTED_NOT_ACCEPTED`; focused run failed on the shared F-02 snapshot mechanism before closure. |
| F-02 | Added ownership/mode validation, non-following opens, pre/open identity comparison, stable descriptor reads, nested-directory checks, and substitution hooks. | `logs`/`auth`/`tokens` ancestor symlinks and final-file substitution/refusal. | `BLOCKED`; `/dev/fd/<directory-fd>/<child>` traversal is not supported on this macOS host and returned ENOENT for the ordinary safe fixture. |
| F-03 | Capture requires both logs; either/both missing returns private-only preservation and blocks runtime removal. Install-attempt cleanup retains the distinct both-absent allowance. | Zero-log observation failure and one-log later-default-protection failure. | `IMPLEMENTED_NOT_ACCEPTED`; assertions were reached with private retention, but expected missing-log classification was masked by the F-02 platform failure. |
| F-04 | Field presence is recognized independently of value; empty and whitespace-only last-exit values throw, while the exact sentinel remains unique. | Malformed table adds empty and whitespace-only cases. | `LOCALLY_PASSING_IN_FAILED_RUN`; no parser test appeared in the failure list. Overall closure withheld because the required focused file failed. |
| F-05 | Added successful bootout with `bootoutRemovesJob=false` and stopped process, asserting job-loaded refusal, no plist/runtime removal, reporting, and log integrity. | Dedicated isolated test. | `IMPLEMENTED_NOT_ACCEPTED`; destructive preservation assertions held, but intact-copy assertion failed because F-02 prevented snapshot creation. |

## Blocking cause

The proposed descriptor-relative traversal opened the runtime root safely but
then attempted `lstat('/dev/fd/<fd>/runtime')`. macOS returned ENOENT for this
ordinary safe fixture. This made every normal preservation attempt fail closed
as private-only, producing 15 focused failures. The behavior is safe but not
functional and cannot be accepted.

Per the sealed escalation rule, no corrective iteration followed the failed
required check. Manager disposition and a new authorized repair continuation
are required.
