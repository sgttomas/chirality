# N2 federation evidence — Dependent Objective V2

The corrected V2 release is
`execution/_Coordination/AgentRuns/ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21/amendments/N2-TASK-MANAGEMENT/V2.md`,
SHA-256
`7faab5380b92244ca4198231a941748366c30433bf0b0dd81cf8861b36867b7e`.

## Mandatory V2 preflight

The deterministic federation helper returned `COMPLETE` before V2 row work:
four canonical registers, 79 typed findings, zero operational errors, zero
unresolved ambiguities, and zero register writes. Root began V2 with 22 live
rows (`OPEN=14`, `DEFERRED=8`) and 105 archived closed rows.

## Final V2 federation

The deterministic federation helper returned `COMPLETE` after closure and
archive: four canonical registers, 79 typed findings, zero operational errors,
zero unresolved ambiguities, and zero register writes. Root ended with 21 live
rows (`OPEN=13`, `DEFERRED=8`) and 106 archived closed rows.

Finding counts were unchanged: 49 `FOREIGN_LINK_TO_LOCAL`, 2
`LOCAL_LINK_TO_FOREIGN`, 2 `REMOTE_CLOSED_LOCAL_OPEN`, 22
`LOCAL_CLOSED_REMOTE_OPEN`, and 4 `MISSING_NOTICE`. None was selected or
dispositioned by V2.

Root live SHA-256 changed from
`db13beefb51bef20321565faffe5f6557e9d26f76144ea871486b3d1498a8830`
to `cd0f1b96c500bcf7bc0886a0d5d20459129b10a86b4f106798a560432adcb5e9`.
Root archive SHA-256 changed from
`7185b82085f60ed8af669f3d6cdccb724b6d52624aa5585a171b6656d924c61b`
to `c05a15d4886ca57dba8460f85be196f239cccf5a1b2394748f1ae90ec91e686c`.
Keyed comparison proves exactly `TM-ROOT-124` moved from live to archive and
every common row remained byte-semantically unchanged.

All App, Piping, and PEC live/archive hashes were identical before and after.
No foreign register write occurred.
