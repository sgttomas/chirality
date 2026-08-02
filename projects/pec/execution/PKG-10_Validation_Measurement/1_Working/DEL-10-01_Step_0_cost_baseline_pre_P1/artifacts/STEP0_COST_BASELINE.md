# PEC Step-0 cost baseline — pre-P1 capture report

**Artifact status:** candidate measurement report; **UNACCEPTABLE AS THE TOKEN
BASELINE because exact token telemetry was unavailable.** C-05 remains open.

**Method:** `STEP0_COST_BASELINE_METHOD.md` v1.0

**Capture corpus:** `19404e7bd2f1b365452114ad75aef042fa02b180`

**Capture time:** 2026-08-01T23:58:23Z

**P1 state:** no P1 node had started; D-PEC-72 opened only the three pre-P1
deliverables and explicitly excluded every P1 source node.

[METHOD] Classification rule: prose, tables, and list items inherit the most
recent `[METHOD]`, `[VALUE]`, or `[LIMIT]` label within their section until a
new label appears.

## 1. PRD token metric capture

[VALUE] Sampling population: PEC loop only. Planned sample count: `n = 1`.
Eligible sample: the D-PEC-72 loop iteration begun from
`90c2c4727373ed126d263dd231a5c46d141e2112` and continued through the committed
activation basis `19404e7bd2f1b365452114ad75aef042fa02b180`.

| Sample | Loop / scope | UTC window | Provider / model / runtime | Input tokens | Cached input | Output tokens | Logical total | Evidence |
|---|---|---|---|---:|---:|---:|---:|---|
| PEC-PRE-P1-001 | PEC / loop-iteration orientation | exact start/end not exposed | Codex desktop task; exact provider/model/runtime identity not exposed to the repository session | NOT_OBSERVED | NOT_OBSERVED | NOT_OBSERVED | NOT_OBSERVED | no exact per-call usage record was available |

[LIMIT] The active task and repository shell exposed neither an exact
per-call token ledger nor exact interval timestamps/provider identifiers for
this orientation. No count can be produced under the method's exactness rule.
The table deliberately contains no estimate, backsolve, word conversion, or
fabricated zero.

[LIMIT] Because the only planned sample is `NOT_OBSERVED`, the report has no
valid token baseline value and no token summary statistic. DEL-10-01 fails
REQ-005/AC-003 for this run and remains unaccepted. The identical method may be
rerun when the runtime exposes exact interval-bound usage telemetry.

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
- Exact token baseline: not observed; acceptance blocked.
- DEL-10-01: candidate/unaccepted.
- C-05: open; no P1 node may start.
- Rerun trigger: a runtime supplies exact per-call input, cached-input, and
  output token usage plus an interval locator for a fresh PEC orientation.
