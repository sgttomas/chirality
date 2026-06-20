# INSP-01a Rerun After D-APP-33 Ruling

**Date:** 2026-06-20
**Tranche:** `INSP-01a` Normalize preflight
**Prepared by:** WORKING_ITEMS
**Status:** PASSED under D-APP-33 semantic-history acceptance basis
**Ruling:** `execution/_Coordination/_DECISIONS/D-APP-33_RULING_2026-06-20.md`
**Dry-run SHA input:** `dafaa50cacdc05940dc53b76740b68a2fd020346`

The SHA above was used only as a valid formatter input for the in-memory human-gate transition. It
is not the owner-blessed `approvalSha` for `INSP-01`.

## Command Shape

Because this checkout does not have `frontend/node_modules/` installed, the rerun used a read-only
Node stdin script mirroring the parser/writer/transition logic from:

- `frontend/src/lib/lifecycle/status-parser.ts`
- `frontend/src/lib/lifecycle/status-writer.ts`
- `frontend/src/lib/lifecycle/transition.ts`

The script enumerated `execution/PKG-*/1_Working/DEL-*/_STATUS.md`, parsed each file, classified
noncanonical history bullets, then applied an in-memory `CHECKING` transition with actor `HUMAN`,
date `2026-06-20`, and metadata fields:

- `Authorization Basis: D-APP-19 Option D ruling 2026-06-20; D-APP-33 semantic-history normalization accepted 2026-06-20`
- `Directive: owner inspection-phase directive 2026-06-20`
- `Checking Approval SHA: <dry-run SHA input>`

No project `_STATUS.md` files were written by this rerun.

## Results

| Check | Result |
|---|---:|
| Deliverable status files enumerated | 53 |
| Parsed successfully | 53 |
| Current state `IN_PROGRESS` | 53 |
| In-memory transition succeeded | 53 |
| Predicted resulting state `CHECKING` | 53 |
| Transition would add required fields in all files | yes |
| Noncanonical history bullets accepted by D-APP-33 | 52 |
| Unaccepted history bullets that would be dropped | 0 |

The only deliverable with no noncanonical history bullet was `DEL-05-04`.

Affected semantic/provisional-history deliverables accepted by D-APP-33:

`DEL-00-01`, `DEL-00-02`, `DEL-01-01`, `DEL-01-02`, `DEL-01-03`, `DEL-01-04`, `DEL-02-01`,
`DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`,
`DEL-03-04`, `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-04`, `DEL-04-05`, `DEL-05-01`,
`DEL-05-02`, `DEL-05-03`, `DEL-05-05`, `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`,
`DEL-06-05`, `DEL-06-06`, `DEL-07-01`, `DEL-07-02`, `DEL-07-03`, `DEL-07-04`, `DEL-07-05`,
`DEL-07-06`, `DEL-08-01`, `DEL-08-02`, `DEL-08-03`, `DEL-08-04`, `DEL-08-05`, `DEL-09-01`,
`DEL-09-02`, `DEL-09-03`, `DEL-09-04`, `DEL-09-05`, `DEL-09-06`, `DEL-10-01`, `DEL-10-02`,
`DEL-10-03`, `DEL-10-04`, `DEL-10-05`.

## Disposition

`INSP-01a` now passes under the D-APP-33 acceptance basis: the predicted normalization loss is
limited to semantic/provisional history bullets that the owner ruled unnecessary for this project.

`INSP-01` remains blocked until the owner confirms one blessed `approvalSha` for the live
`IN_PROGRESS -> CHECKING` transition. This rerun does not authorize `CHECKING -> ISSUED`, deletion
of semantic artifact files, provider expansion, release posture, or domain-engine work.
