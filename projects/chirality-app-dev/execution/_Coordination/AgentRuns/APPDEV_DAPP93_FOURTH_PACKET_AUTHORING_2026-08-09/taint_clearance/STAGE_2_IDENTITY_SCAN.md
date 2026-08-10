# Stage 2 — Historical identity scan

Verdict: `BLOCK_N1_PREVALIDATED_COMMAND_FORM_NOT_EXECUTABLE`

The frozen, prevalidated scan command was invoked with the four mandatory
case-sensitive patterns and all six salvage files as explicit path arguments.
It did not start: this runtime has no `/usr/bin/rg` executable.

- Exit: `127`
- Stdout: `0 bytes`
- Stderr: `zsh:1: no such file or directory: /usr/bin/rg`
- Pattern result: **not established**; no scan occurred
- File content read by the failed scan: none (the executable lookup failed
  before any file argument could be opened)

Exact actual command:

```text
/usr/bin/rg -n --no-heading -e 'C[0-9]{3,}' -e 'A3-OP-[0-9]{3}' -e 'R[0-9]+-C[0-9]{3,}' -e 'ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+' -- projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_1_SOURCE_INVENTORY.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_2_AUTHORITY_SEMANTICS.md projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_3_COMMAND_EXTRACTION_CORE.csv projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_4_COMMAND_EXTRACTION_SAFETY.csv projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_6_LEDGER_ALIGNMENT_CHECK.md
```

The sealed brief requires an immediate BLOCK for any result that cannot be
proved from the allowed files and forbids silent substitution or repair. No
alternate `rg` path, shell alias, Python regex scan, or other unvalidated
command form was attempted. Stages 3 through 5 were not started.
