---
amendment_id: SCA-004
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 2
created: 2026-08-02
status: awaiting_gate_2_acceptance
authority: D-PEC-78 O-A and owner-confirmed SCA-004 Gate 1
---

# SCA-004 — PEC-local long-term loop-registry disposition

## Human initiation and Gate 1 confirmation

The upstream product decision is the owner's exact ruling:

> D-PEC-78: O-A

The owner then confirmed the SCOPE_CHANGE intake exactly:

> SCA-004 Gate 1: parsing confirmed as MODIFY-only — SOW-077 → PKG-01 →
> DEL-01-06 → OBJ-004, OI-003 resolved by D-PEC-78 O-A, DEL-01-06 name/path
> preserved. Advance to Gate 2 impact assessment only.

Gate 1 is therefore `CONFIRMED`. Gate 2 remains awaiting owner acceptance.

## Normalized parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-004` |
| `ALLOW_RENUMBERING` | `false` |
| Accepted basis | SOFTWARE_DECOMP revision 1.3 (`current_basis`) |
| Current gate | Gate 2 — impact assessment awaiting owner acceptance |

## Confirmed atomic actions

| Ref | ActionType | EntityType | EntityID | Confirmed field window |
|---|---|---|---|---|
| A001 | `MODIFY` | `OTHER` | `SOW-077` | TBD→IN; assign PKG-01 / DEL-01-06 / OBJ-004; close its OpenIssue flag; carry D-PEC-78 and the selected PEC-local strict-v1 boundary |
| A002 | `MODIFY` | `OTHER` | `SOW-094` | Preserve statement, status, source and lineage; replace only unresolved-long-term DecisionRef/Notes posture |
| A003 | `MODIFY` | `DELIVERABLE` | `DEL-01-06` | Preserve ID/name/path/package/type/envelope/phase/artifacts/objective; add SOW-077 to CoversScopeItems and replace the OI-003-open description |
| A004 | `MODIFY` | `OTHER` | `OI-003` | Retain the row and record it resolved by D-PEC-78 O-A; reconcile open/resolved telemetry |
| A005 | `MODIFY` | `OTHER` | amendment traceability | Reconcile package/objective views, decision/revision history, snapshot evidence and pointers only after later gates |

Exact amendment prose is deliberately absent. It belongs to Gate 3 and is not
authorized by this package.

## Gate boundary

This Gate 2 package changes no decomposition truth, companion register,
accepted pointer, deliverable metadata/content, dependency register, source,
lifecycle, Task Management row, decision, receipt, or foreign-loop surface.

