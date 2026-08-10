# N1 taint-clearance return

- RunID: `APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09`
- ChildInstanceID: `A2-DAPP93-FOURTH-N1-01`
- Verdict: `BLOCK_N1_PREVALIDATED_COMMAND_FORM_NOT_EXECUTABLE`
- Completed durable stages: Stage 1; Stage 2 block record
- Unstarted stages: Stage 3, Stage 4, Stage 5
- Downstream release: `DENIED`; M1/N2 must remain held

## Result

Stage 1 recorded the exact current identities of the six authorized salvage
files. The ledger is 42,705 bytes and its SHA-256 is exactly
`dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.

Stage 2 could not establish the required zero-match result because the exact
pre-dispatch-approved executable `/usr/bin/rg` is absent. The command exited
127 before opening any search file. Substituting a different executable path
or validator would depart from the frozen command forms, so the child blocked
without repair as required.

During closeout inspection, the prevalidated BSD `sed` form was also found to
be non-portable in this runtime: `/usr/bin/sed -n '1,260p' -- <exact-file>`
treated `--` as a filename, emitted `sed: --: No such file or directory`, and
then displayed the allowlisted Stage 6 file. Thus the command attempted an
undeclared nonexistent relative path named `--`; it opened no undeclared
bytes. This is recorded rather than concealed and independently confirms that
the frozen command forms require manager correction before any replacement
dispatch.

No operational command represented by the ledger was executed. No packet,
freeze, verifier, approval hash, execution authority, Git action, or blocked-
root mutation was produced.

## Exact actual commands

1. Initial authorized control-file reads (six commands in one shell request):
   `sed -n '1,260p' <exact-control-file>`, once each for the sealed brief,
   `WORK_GRAPH.md`, `validation/N1_PRE_DISPATCH_PREFLIGHT.md`,
   `validation/FOUR_ROOT_BASELINE.md`, `allowlists/N1_READ_ALLOWLIST.txt`, and
   `allowlists/N1_COMMAND_FORMS.txt`.
2. `/usr/bin/wc -c -- <the six exact salvage paths as explicit arguments>`.
3. `/usr/bin/shasum -a 256 -- <the six exact salvage paths as explicit arguments>`.
4. `/usr/bin/rg -n --no-heading -e 'C[0-9]{3,}' -e 'A3-OP-[0-9]{3}' -e 'R[0-9]+-C[0-9]{3,}' -e 'ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+' -- <the six exact salvage paths as explicit arguments>`; exit 127, no scan.
5. `/usr/bin/sed -n '1,260p' -- projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_6_LEDGER_ALIGNMENT_CHECK.md`; error on path `--`, followed by read of the exact allowlisted Stage 6 path.

The full literal Stage 2 command is preserved in
`taint_clearance/STAGE_2_IDENTITY_SCAN.md`; the full literal Stage 1 path set
is the six-file sequence in `allowlists/N1_READ_ALLOWLIST.txt` and is also
named in `taint_clearance/STAGE_1_SALVAGE_HASHES.md`.

## Exact read paths

Run-local control files:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/briefs/N1_TAINT_CLEARANCE_BRIEF.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/WORK_GRAPH.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/validation/N1_PRE_DISPATCH_PREFLIGHT.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/validation/FOUR_ROOT_BASELINE.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/allowlists/N1_READ_ALLOWLIST.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09/allowlists/N1_COMMAND_FORMS.txt`

Authorized salvage files opened by `wc`/`shasum`:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_1_SOURCE_INVENTORY.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_2_AUTHORITY_SEMANTICS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_3_COMMAND_EXTRACTION_CORE.csv`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_4_COMMAND_EXTRACTION_SAFETY.csv`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09/source_reconstruction/STAGE_6_LEDGER_ALIGNMENT_CHECK.md`

Only the Stage 6 salvage file's contents were displayed by `sed`. The failed
`rg` opened none of its six path arguments. No live-source allowlist file and
no other historical-root byte was read.

## Telemetry honesty

Native context occupancy telemetry is unavailable in this child runtime.
Durable outputs at return: three files (`STAGE_1_SALVAGE_HASHES.md`,
`STAGE_2_IDENTITY_SCAN.md`, and this return). The supervisor owns checkpoint
file-count and byte-total observations under the frozen pacing contract.
