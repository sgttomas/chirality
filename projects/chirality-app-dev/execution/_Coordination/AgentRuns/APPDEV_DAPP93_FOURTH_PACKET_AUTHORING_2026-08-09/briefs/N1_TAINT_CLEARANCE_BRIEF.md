# Sealed brief — N1 fresh taint clearance

- RequestedBy: `WI-PKG09-DAPP93-FOURTH-01`
- RunID: `APPDEV_DAPP93_FOURTH_PACKET_AUTHORING_2026-08-09`
- ChildInstanceID: `A2-DAPP93-FOURTH-N1-01`
- Objective: independently clear or block the six exact third-lineage staged
  files for hash-bound salvage, without reading any other blocked-root byte.
- Dependencies: frozen graph v1 and manager command preflight PASS.
- Allowed tools: read-only `sed`, `shasum`, `wc`, `rg`, bounded Python/CSV
  parsing, `git rev-parse` for the four exact blocked-root tree identities,
  and writes only through `apply_patch` to the output scope below.
- Exact declared reads: every non-comment path in
  `allowlists/N1_READ_ALLOWLIST.txt`, and only those files; the brief,
  graph, allowlist, command forms, preflight, and four-root baseline inside
  this new run root are also readable.
- AllowedWriteTargets:
  `taint_clearance/STAGE_1_SALVAGE_HASHES.md`,
  `taint_clearance/STAGE_2_IDENTITY_SCAN.md`,
  `taint_clearance/STAGE_3_LIVE_SOURCE_PROVENANCE.csv`,
  `taint_clearance/STAGE_4_LEDGER_STRUCTURE.md`,
  `taint_clearance/STAGE_5_TAINT_SNAPSHOT.md`, and
  `returns/N1_TAINT_CLEARANCE_RETURN.md` only.
- Forbidden: the three historical blocked roots in full; every byte of the
  third blocked root except the six exact staged files; broad directory
  search; unresolved globs; exclusion-pattern fences; repository/project/
  AgentRuns-root search; all operational actions enumerated in ACTIVATION.

## Required stages and shared clock

| Stage | Durable completion output | Expected duration | Acceptance |
|---:|---|---:|---|
| 1 | `STAGE_1_SALVAGE_HASHES.md` | 4 minutes | all six exact sizes and hashes match recorded identities; ledger hash is exactly `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809` |
| 2 | `STAGE_2_IDENTITY_SCAN.md` | 4 minutes | full frozen four-pattern scan on all six files, zero matches, exact command/exit/stdout recorded |
| 3 | `STAGE_3_LIVE_SOURCE_PROVENANCE.csv` | 8 minutes | each of 80 rows mapped to at least one exact live source; every source exists, hashes as current, lies in the allowlist, and is outside all four blocked roots; no third-lineage prose used as provenance |
| 4 | `STAGE_4_LEDGER_STRUCTURE.md` | 4 minutes | 80 rows, 13 fields, contiguous/unique IDs, no empty required fields; Stage3+Stage4 byte-field-equal Stage5; zero blocked provenance |
| 5 | `STAGE_5_TAINT_SNAPSHOT.md` and terminal return | 4 minutes | immutable identity table, actual commands/read paths, limitations, PASS/BLOCK, and no-authority statement |

Total expected duration: 24 minutes. First supervisory checkpoint is at minute
4, never earlier. Thereafter checkpoint every 8 minutes. Progress is exact
on-disk file-count/byte growth under `taint_clearance/**` and `returns/**`.
Quietness is irrelevant. Interrupt only after a complete 8-minute interval
with zero durable growth, recording exact observed state. Native context
occupancy must be reported unavailable when the runtime does not expose it.

## Full historical identity pattern set

Case-sensitive regular expressions, all mandatory:

1. `C[0-9]{3,}`
2. `A3-OP-[0-9]{3}`
3. `R[0-9]+-C[0-9]{3,}`
4. `ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+`

## Acceptance and escalation

Any hash mismatch, pattern hit, missing/ambiguous source, unresolved row,
blocked-root source, undeclared read/search, or structural defect is an
immediate lineage BLOCK. Do not repair or re-author any row or staged file.
Return exact actual commands and read paths so the manager can reproduce
allowlist conformance at fan-in. A PASS is derivative taint-clearance evidence
only and cannot release N2 without independent manager acceptance.
