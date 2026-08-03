# G4 diff-mode CI handoff — TM-ROOT-110

Status: **PREPARED ROUTED HANDOFF — NO CI OR GOVERNANCE FILE CHANGED**
Prepared by: Root TASK_MANAGEMENT
Addressee: Root governance-harness owning workflow, with CHANGE used for the
human-gated Git closeout
Owning register row: `TM-ROOT-110`

## Ruled change

Wire the existing G4 diff-mode manifest check into CI. Preserve the current
manifest discipline and make a missing required G4 manifest fail the governed
CI path for an applicable instruction-surface diff.

## Basis

- `execution/_Coordination/LOOP_RECEIPTS.md`, Receipt 77, source SHA-256
  `abd0f89081cc7bb426a7a8d6c687128cc6d94a42d46ffc72cb1a2b42d059510d`.
- `execution/_Coordination/_TaskManagement/RULING_2026-08-02_ROOT_HARVEST_SLATE.md`,
  SHA-256 `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.

## Nine-domain completeness scan

| Domain | Handoff result |
|---|---|
| Action Item | `TM-ROOT-110`; existing diff-mode validation is not wired into CI. |
| Assignment | Human A remains unset; governance-harness owner supplies R/S/C/I. |
| Prioritization | `TBD`; no priority was supplied in the promotion ruling. |
| Deliverables | Existing G4 validator plus the applicable Root CI workflow. |
| Work | Identify the canonical diff base/range, invoke diff-mode validation, and add positive/negative CI evidence. |
| Planning | Preserve current schema validation; add the diff-mode gate without weakening other checks. |
| Approval | Human-gated change/PR under Root policy. |
| Checking | Local positive case, missing-manifest negative case, CI run, and exact changed-file evidence. |
| Decisions | The change choice is already ruled; record implementation evidence, not a replacement policy. |

## Acceptance and return contract

Return exact changed paths and SHAs, local commands/results, negative-case
proof, CI check URL/ref, and accepted PR/change evidence. `TM-ROOT-110` remains
OPEN until the owner accepts that change evidence.
