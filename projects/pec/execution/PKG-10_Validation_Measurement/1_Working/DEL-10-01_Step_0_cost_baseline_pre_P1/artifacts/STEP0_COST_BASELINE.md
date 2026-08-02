# PEC Step-0 cost baseline — pre-P1 capture report

**Artifact status:** candidate measurement report; exact token baseline
observed; REVIEW and owner acceptance pending. C-05 remains open.

**Method:** `STEP0_COST_BASELINE_METHOD.md` v1.0

**Token-rerun corpus:** `51866bc87e276ae932f8f06b4caf9a5dc701b3dd`

**Token-rerun window:** 2026-08-02T01:49:10.976Z through
2026-08-02T01:55:18.167Z; qualifying orientation return emitted at
2026-08-02T01:55:10.472Z.

**Latency capture corpus/time:**
`19404e7bd2f1b365452114ad75aef042fa02b180` at 2026-08-01T23:58:23Z.

**P1 state:** no P1 node had started; D-PEC-72 opened only the three pre-P1
deliverables and explicitly excluded every P1 source node.

[METHOD] Classification rule: prose, tables, and list items inherit the most
recent `[METHOD]`, `[VALUE]`, or `[LIMIT]` label within their section until a
new label appears.

## 1. PRD token metric capture

[VALUE] Sampling population: PEC loop only. Exact observed sample count:
`n = 1`. The accepted rerun sample is the D-PEC-72 extension begun on clean
Git state `51866bc87e276ae932f8f06b4caf9a5dc701b3dd` and closed by the explicit
Step-0 orientation return in the window above. The earlier attempt that
returned `NOT_OBSERVED` is retained in the run history as a failed capture,
not counted as a baseline sample.

| Sample | Loop / scope | UTC window | Provider / model / runtime | Input tokens | Cached input | Output tokens | Logical total | Evidence |
|---|---|---|---|---:|---:|---:|---:|---|
| PEC-PRE-P1-002 | PEC / Agent-0 loop-iteration orientation, including four contributing manager/reviewer sessions | `2026-08-02T01:49:10.976Z` through usage boundary `2026-08-02T01:55:18.167Z`; return emitted `01:55:10.472Z` | OpenAI; Codex desktop/CLI `0.146.0-alpha.9.2`; `gpt-5.6-sol` plus one `codex-auto-review` nested review | 5,691,203 | 5,440,768 | 22,436 | 5,713,639 | `_run_records/D-PEC-72_TOKEN_TELEMETRY_RERUN_2026-08-02.md` |

[VALUE] The exact raw classes also report zero cache-write input tokens,
250,435 uncached input tokens, and 8,395 reasoning-output tokens as a subset of
output. The evidence record binds every contributing session, its counted
window, raw class semantics, and exact per-session delta. Cumulative-usage
deltas prevent repeated telemetry snapshots from being double-counted.

[LIMIT] This is one observed orientation, not a population estimate. The
multi-session Agent-0 posture and the disclosed model/runtime mix are part of
the observed session shape. No estimate, context-window backsolve, billing
approximation, word conversion, or fabricated zero is used. AC-003 now has
exact producer-side evidence; DEL-10-01 remains unaccepted pending REVIEW and
the owner's separate AC-008 fitness confirmation.

## 2. Practitioner-harness latency re-test

[METHOD] Five sequential read-only invocations were run from the capture SHA:

```text
/usr/bin/time -p python3 tools/practitioner_harness/harness.py self-check
```

The report output was discarded; governed files were not written.

[VALUE] Environment: Python 3.13.14; Darwin 25.6.0 arm64.

| Run | Wall time (s) |
|---:|---:|
| 1 | 3.34 |
| 2 | 2.81 |
| 3 | 2.78 |
| 4 | 2.70 |
| 5 | 2.64 |

[VALUE] `n = 5`; minimum `2.64 s`; median `2.78 s`; maximum `3.34 s`;
arithmetic mean `2.854 s`.

[VALUE] The historical harness record says query pain was measured unmet on
2026-07-02 when its slowest command, `self-check`, took approximately four
seconds. Every current observation is below that approximate prior value.

[LIMIT] The historical record provides no formal numerical pain threshold.
Accordingly, this re-test supplies no evidence that query pain has increased
from the observation that was judged unmet; it does not itself re-rule the
precondition, direct the harness, or authorize a cache.

## 3. Statement classification and scope boundary

[METHOD] Sections labeled METHOD describe how the observations were taken.
[VALUE] labels report captured evidence. [LIMIT] labels state coverage and
interpretation limits. This report specifies no behavior for DEL-04-01,
DEL-08-04, the practitioner harness, or any other package.

[LIMIT] No post-P1 value exists, no before/after comparison is attempted, and
the PRD §11 falsification clause is not evaluated.

## 4. Candidate disposition

[LIMIT] Candidate dispositions:

- Method document: produced and repeatable, subject to REVIEW.
- Original command-latency observation: produced, distinct from the token
  metric, subject to REVIEW.
- Exact token baseline: observed under the published method; subject to REVIEW.
- DEL-10-01: complete candidate, unaccepted pending REVIEW and owner fitness.
- C-05: open; no P1 node may start.
- Telemetry rerun trigger: satisfied by the bounded evidence record; no further
  rerun is required unless REVIEW finds a defect.
