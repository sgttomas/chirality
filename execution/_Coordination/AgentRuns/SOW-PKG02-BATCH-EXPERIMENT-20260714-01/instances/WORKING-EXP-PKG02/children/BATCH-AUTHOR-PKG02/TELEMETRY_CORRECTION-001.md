# Telemetry Integrity Correction 001

Status: `RETAINED — REMEDIATED EXECUTION-SUBSTRATE FINDING`

The first durable `DEL-02-01` precheck row originally recorded in
`PROGRESS.tsv` was:

```text
1	DEL-02-01	precheck	2026-07-14T18:02:00Z	2026-07-14T18:07:00Z	PASS	0	PASS	NONE	NONE	YES	members/DEL-02-01/PRECHECK.md
```

Those timestamps were a manual transcription error: they were twelve hours
ahead of the actual UTC interval. Before batch execution, that row was
improperly replaced rather than preserved append-only with this corrected row:

```text
1	DEL-02-01	precheck	2026-07-14T06:30:00Z	2026-07-14T06:35:00Z	PASS	0	PASS	NONE	NONE	YES	members/DEL-02-01/PRECHECK.md
```

This correction artifact preserves both versions and classifies the rewrite
as a telemetry-integrity/process defect. It did not alter the frozen row,
source/control bytes, candidate bytes, deterministic-tool outputs, validation,
mapping, parity, checklist, rendering, finalization binding, or quality
verdict. A correction row was appended to `PROGRESS.tsv`; the existing row was
not rewritten again.

No other durable evidence artifact was rewritten. The authored helper
`run_author.sh` was amended once before execution after `bash -n` caught a
quoting error; the original syntax error is retained in
`harness-syntax-attempt-1.stderr` and `.exit`. The candidate and member evidence
families were then created once by the syntax-valid harness. The earlier BSD
`find` probe created no artifact and is retained in `DEL-02-01/PRECHECK.md`.
