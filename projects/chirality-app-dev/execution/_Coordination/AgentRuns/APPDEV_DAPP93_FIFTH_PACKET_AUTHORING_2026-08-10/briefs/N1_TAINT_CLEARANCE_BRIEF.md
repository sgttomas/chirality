# Sealed brief — N1 fifth-lineage taint clearance

- RequestedBy: `WORKING_ITEMS-DAPP93-L5-20260810`
- RunID: `APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10`
- ParentInstanceID: `WORKING_ITEMS-DAPP93-L5-20260810`
- ChildInstanceID: `A2-DAPP93-L5-N1-TAINT-01`
- PackageID: `D-APP-93 exact packet preparation`
- Objective: independently determine whether the six owner-authorized salvage
  files, especially the 80-row ledger, are byte-correct, free of historical
  command identities, structurally valid, and provenance-resolved entirely to
  live repository sources at base
  `226e92a69125fe746d3e55e44414ec5afe15010d`.
- Dependencies: manager executable-tool preflight PASS only.
- DeclaredReads: exactly `allowlists/N1_READ_ALLOWLIST.txt`.
- AllowedTools: `apply_patch` for the exact writes below and only shell forms
  F01-F11 in `allowlists/FROZEN_COMMAND_FORMS.md`.
- AllowedWriteTargets: exactly `taint_clearance/STAGE_1_SALVAGE_HASHES.md`,
  `STAGE_2_HISTORICAL_ID_SCAN.md`, `STAGE_3_LIVE_SOURCE_PROVENANCE.md`,
  `STAGE_4_LEDGER_ROW_PROVENANCE.csv`, `STAGE_5_STRUCTURAL_VALIDATION.md`,
  `STAGE_6_TAINT_CLEARANCE_VERDICT.md`, and
  `returns/N1_TAINT_CLEARANCE_RETURN.md`.
- EXCLUSIONS: every path in `ABSOLUTE_READ_WRITE_EXCLUSIONS.txt`, with only
  direct reads of the six exact paths in `SALVAGE_FILES.txt` excepted. Never
  list, glob, search, or walk a historical root. Never copy a salvage file.

## Ordered durable stages and shared clock

1. `STAGE_1_SALVAGE_HASHES.md` (4 minutes): hash all six exact files; Stage 5
   must equal the owner-recorded digest.
2. `STAGE_2_HISTORICAL_ID_SCAN.md` (5 minutes): run exact F02 against the six
   explicit file paths. Required result: zero matches, exit 1, stdout 0 bytes.
3. `STAGE_3_LIVE_SOURCE_PROVENANCE.md` (8 minutes): resolve every source path
   and digest declared by Stage 1 to a live allowed repository source; no
   historical root or third-lineage prose may stand in for provenance.
4. `STAGE_4_LEDGER_ROW_PROVENANCE.csv` (8 minutes): one row for each ledger
   row with its row identity, source_basis, resolved live source family/path,
   and PASS/BLOCK. All 80 must resolve.
5. `STAGE_5_STRUCTURAL_VALIDATION.md` (5 minutes): validate exact 13-column
   schema, 80 rows, unique contiguous `L3-CMD-001`..`L3-CMD-080`, nonempty
   required fields, allowed actors/classes, exact approval fence, and Stage
   3+4 byte-field equality to Stage 5.
6. `STAGE_6_TAINT_CLEARANCE_VERDICT.md` plus terminal return (4 minutes): PASS
   only if every prior check passes; otherwise BLOCK with no repair.

Total expectation: 34 minutes. First checkpoint is not before minute 4;
subsequent checkpoint interval is 8 minutes. Durable progress is file-count
and byte growth. Quietness is not failure. Native token/context occupancy is
not exposed and must be recorded as unavailable in updates/return.

## Acceptance and escalation

PASS requires: all six hashes confirmed; full four-pattern scan zero-hit;
every one of 80 rows mapped to live repository provenance; structural ledger
PASS; no forbidden path read/search/write; exact target containment; and a
terminal return listing every shell invocation and output SHA. A mismatch,
taint hit, unresolved row, structural defect, or fence breach is an immediate
BLOCK. Do not repair, substitute a command, consult prior prose, or dispatch.
