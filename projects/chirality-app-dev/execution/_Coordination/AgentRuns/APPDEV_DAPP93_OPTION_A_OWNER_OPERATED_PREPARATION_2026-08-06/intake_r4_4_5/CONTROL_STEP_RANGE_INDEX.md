# D-APP-93 R4.4.5 CONTROL step/range index

Status: `FROZEN DERIVATIVE — ORDERED UNIQUE THROUGH C1146.30`

Basis: `returned/control-transcript.txt`, 40,008 bytes, SHA-256
`7323f3030d68682b4ce02e7bd21b15c8e3817be05326a3c7570cb02cfc37b768`.
Ranges are zero-based and end-exclusive. Each range ends at the end of the
literal raw exit record for that observed executable step; its start is the
previous observed record end (or byte zero for the first range). This yields
non-overlapping envelopes over all through-step bytes without inventing
ranges for unexecuted steps.

| Step | C1146 record | Range | Exit | Uniqueness/closure |
|---:|---|---:|---:|---|
| 1 | C1146.01 | `[0,264)` | 0 | unique/closed |
| 2 | C1146.02 | `[264,1189)` | 0 | unique/closed |
| 3 | C1146.03 | `[1189,1978)` | 0 | unique/closed |
| 4 | C1146.04 | `[1978,5352)` | 0 | unique/closed |
| 5 | C1146.05 | `[5352,11941)` | 0 | unique/closed |
| 6 | C1146.06 | `[11941,13863)` | 0 | unique/closed |
| 7 | C1146.07 | `[13863,14745)` | 0 | unique/closed |
| 8 | C1146.08 | `[14745,16236)` | 0 | unique/closed |
| 9 | C1146.09 | `[16236,23034)` | 0 | unique/closed |
| 10 | C1146.10 | `[23034,30729)` | 0 | unique/closed |
| 23 | C1146.23 | `[30729,31375)` | 0 | unique/closed |
| 25 | C1146.25 | `[31375,34924)` | 0 | unique/closed |
| 28 | C1146.28 | `[34924,37530)` | 0 | unique/closed |
| 29 | C1146.29 | `[37530,39482)` | 0 | unique/closed |
| 30 | C1146.30 | `[39482,39899)` | 0 | unique/closed; terminal cut |

Exact raw-record spans within those envelopes are respectively
`[225,264)`, `[1150,1189)`, `[1939,1978)`, `[5313,5352)`,
`[11902,11941)`, `[13824,13863)`, `[14706,14745)`,
`[16197,16236)`, `[22995,23034)`, `[30690,30729)`,
`[31336,31375)`, `[34885,34924)`, `[37491,37530)`,
`[39443,39482)`, and `[39860,39899)`.

Steps 11-22, 24, 26, and 27 are absent by selected-route design and are
marked `NOT_RUN`, not missing or unclosed. No record is duplicated or retried.
The finite `[39899,40008)` export/prompt tail has no step range and contains
no later CONTROL input. C1146.30 is the last CONTROL record and input.
