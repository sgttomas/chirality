# C1155 ordinary-path required-file producer/copy trace

Status: `COMPLETE — 21/21 REQUIRED FILES WIRED`

| C1155 required file | Producer | Ordinary-path return/copy | Screen / manifest consumer | Result |
|---|---|---|---|---|
| `lldb-transcript.txt` | C1144 Terminal LLDB export | C1144 writes directly to returned | C1157 / C1154 | PASS |
| `control-transcript.txt` | C1151 Terminal CONTROL export | C1151 writes directly to returned | C1157 / C1154 | PASS |
| `completed-evidence-return.md` | C1150 writable derivative + C1152 completion | C1153 exact copy to returned | C1157 / C1154 | PASS |
| `CONTROL_RANGE_INDEX.txt` | C1156 exact awk/dd/shasum | C1156 writes directly to returned | C1157 / C1154 / C1155 recompute | PASS |
| `SOURCE_SCREEN_RESULTS.txt` | C1148 exact result function | C1130 fifteenth source copied to returned | C1157 / C1154 / C1155 exact rows | PASS |
| `FINAL_SCREEN_RESULTS.txt` | C1157 exact result function | C1157 writes directly to returned | C1154 / C1155 exact rows | PASS |
| `helper.stdout.txt` | C1114 redirect | C1130 source 1 | C1148 / C1157 / C1154 | PASS |
| `helper.stderr.txt` | C1114 redirect | C1130 source 2 | C1148 / C1157 / C1154 | PASS |
| `helper.pid` | C1114 exact PID record | C1130 source 3 | C1148 / C1157 / C1154 | PASS |
| `gui.stdout.txt` | C1117 redirect | C1130 source 4 | C1148 / C1157 / C1154 | PASS |
| `gui.stderr.txt` | C1117 redirect | C1130 source 5 | C1148 / C1157 / C1154 | PASS |
| `gui.pid` | C1117 exact PID record | C1130 source 6 | C1148 / C1157 / C1154 | PASS |
| `c1105.output.txt` | C1105 tee | C1130 source 7 | C1148 / C1157 / C1154 | PASS |
| `c1105.exit.txt` | C1105 pipestatus record | C1130 source 8 | C1148 / C1157 / C1154 | PASS |
| `c1106.output.txt` | C1106 tee | C1130 source 9 | C1148 / C1157 / C1154 | PASS |
| `c1106.exit.txt` | C1106 pipestatus record | C1130 source 10 | C1148 / C1157 / C1154 | PASS |
| `c1107.output.txt` | C1107 tee | C1130 source 11 | C1148 / C1157 / C1154 | PASS |
| `c1107.exit.txt` | C1107 pipestatus record | C1130 source 12 | C1148 / C1157 / C1154 | PASS |
| `c1108.output.txt` | C1108 tee | C1130 source 13 | C1148 / C1157 / C1154 | PASS |
| `c1108.exit.txt` | C1108 pipestatus record | C1130 source 14 | C1148 / C1157 / C1154 | PASS |
| `RETAINED_EVIDENCE_MANIFEST.txt` | C1154 exact inline manifest | C1154 writes directly to returned | C1155 identity check; intake hash | PASS |

`COMPLETENESS_RESULT.txt` is the output of C1155 itself and therefore is not a
pre-existing member of C1155's required array. C1155 writes it directly to
returned and intake independently hashes it. Optional
`control-transcript-precleanup.txt` is manifest/screen checked when present but
is not required for ordinary-path `PASS_COMPLETE` because the complete final
CONTROL transcript is required.

Trace verdict: `PASS_ORDINARY_PATH_REQUIRED_FILES_21_OF_21`.
