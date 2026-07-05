# D-PEC-01 Pilot Evidence Manifest - Template

> **Epistemic status:** template only. A completed manifest becomes a
> derivative evidence package after the owner supplies the D-PEC-01 execution
> basis and the branch-first evidence run is performed.

## Identity

| Field | Value |
|---|---|
| Evidence package | `PEC_YYYY-MM-DD_DPEC01-pilot-evidence-XX` |
| Git SHA at run start | TBD |
| Branch | TBD |
| Governing decision | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-01_pilot_rehearsal_real_data_authorization.md` |
| Related gates | D-PEC-04 Gate 2 deferred; D-PEC-05 L3 deferred; `force=true` separate ruling required |
| Operator | TBD |
| Date/time | TBD |

## Owner-Supplied Basis

| Required input | Value |
|---|---|
| MDL spreadsheet/export path | TBD |
| RAIL spreadsheet/export path | TBD |
| Decisions spreadsheet/export path, if in scope | TBD |
| Risks spreadsheet/export path, if in scope | TBD |
| Schedule spreadsheet/export path, if in scope | TBD |
| Actor identity for authenticated capture | TBD |
| Visibility basis | TBD |
| Scratch import `PEC_DB` path | TBD |
| Scratch backup directory | TBD |
| Real backup artifact path, if in scope | TBD |
| Scratch restore `PEC_DB` path | TBD |
| Raw file content viewing permitted? | TBD |
| Unredacted exports/reports committable? | TBD |
| Additional capture limits | TBD |

## Input File Hashes

| Input | Path | SHA-256 | Size, if permitted | Notes |
|---|---|---|---|---|
| MDL | TBD | TBD | TBD | TBD |
| RAIL | TBD | TBD | TBD | TBD |
| Decisions | TBD | TBD | TBD | TBD |
| Risks | TBD | TBD | TBD | TBD |
| Schedule | TBD | TBD | TBD | TBD |
| Backup artifact | TBD | TBD | TBD | TBD |

## Commands

| Step | Command summary | Environment | Exit code | Log/artifact pointer |
|---|---|---|---|---|
| Hash inputs | TBD | n/a | TBD | TBD |
| Import rehearsal | TBD | scratch `PEC_DB` only | TBD | TBD |
| Restore rehearsal | TBD | scratch `PEC_DB`, scratch `PEC_BACKUP_DIR` only | TBD | TBD |
| Optional API/export/report capture | TBD | owner actor/visibility basis | TBD | TBD |

## Import Results

| Contract | Accepted | Updated | Conflicts | Rejected | Intake created | Notes |
|---|---:|---:|---:|---:|---:|---|
| MDL | TBD | TBD | TBD | TBD | TBD | TBD |
| RAIL | TBD | TBD | TBD | TBD | TBD | TBD |
| Decisions | TBD | TBD | TBD | TBD | TBD | TBD |
| Risks | TBD | TBD | TBD | TBD | TBD | TBD |
| Schedule | TBD | TBD | TBD | TBD | TBD | TBD |

## Reject Summary

| Source | Row/ref | Reason summary | Raw content omitted? |
|---|---|---|---|
| TBD | TBD | TBD | yes |

## Restore Results

| Check | Value |
|---|---|
| Restore source backup hash | TBD |
| Scratch restore target | TBD |
| Pre-restore scratch DB preserved aside | TBD |
| Spot checks performed | TBD |
| Real pilot DB mutated | No |

## Captured Derivative Artifacts

| Artifact | Path | SHA-256 | Contains raw real content? | Owner permitted? |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## Limitations

- No `force=true` was used.
- No raw real input file was committed unless listed above with explicit owner
  permission.
- No real database file was committed unless listed above with explicit owner
  permission.
- No Gate 2 adoption was performed.
- No L3 proposal-shaped apply design or execution was performed.
- No pilot-readiness or go-live claim is made.
- No professional approval, check acceptance, decision outcome, revision issue,
  waiver judgment, or other reserved PEC human act is claimed.

## Gate Outcome

TBD: summarize what this evidence proves and what remains parked.
