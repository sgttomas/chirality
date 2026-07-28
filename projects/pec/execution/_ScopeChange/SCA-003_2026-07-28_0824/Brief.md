---
amendment_id: SCA-003
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 1
created: 2026-07-28
status: owner_ruled
authority: owner standing completion approval after D-PEC-68
---

# SCA-003 — Consumer-interface concordance

## Human initiation and standing gate authority

SCOPE_CHANGE is human-initiated. The owner direction of record is:

> "Finish out your plan now (attaining your goal) with self merge of PRs and
> auto approve for owners rulings, which should still be recorded in the usual
> manner with your recommendation standing as what I approved."

Agent 0 directed SCOPE_CHANGE to open SCA-003 after D-PEC-68 became durable on
main at `ec3bec922e2e62e32fb283c5873b28b2bb9c510e`. For each Gate 1–5
decision below, the recorded SCOPE_CHANGE/Agent 0 recommendation therefore
stands as the owner's approved selection.

## Normalized parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-003` |
| `ALLOW_RENUMBERING` | `false` |
| Change class | `MODIFY` only |
| Accepted input | PRD v2.2, SHA-256 `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| Accepted basis | `SOFTWARE_DECOMP.md` revision 1.2 |
| Successor | revision 1.3 |

## Gate 1 recommendation and owner-approved selection

**Recommendation:** validate the request as a narrow semantic concordance,
class every action `MODIFY`, preserve 94 scope items, 11 packages, 64
deliverables, 6 objectives, every stable ID and every dependency edge, and
advance to impact analysis without opening downstream production.

**Owner-approved selection under the standing direction:** approve the
recommendation exactly.

Gate 1 result: **PASS / RULED**.

## Change request

Reconcile decomposition truth to the exact pull-oriented, consumer-owned,
never-forced posture adopted in PRD v2.2 and to the accepted ADR-014
historical-lineage correction. Amend:

- constraints C3 and C15 plus source/basis prose;
- SOW-041, SOW-060, SOW-085 and SOW-088;
- DEL-00-01, DEL-10-05 and DEL-10-12 descriptions;
- the exact three matching `_CONTEXT.md` description/provenance surfaces.

The DEL-10-12 canonical label and path remain
`Poll-adoption measurement` / `DEL-10-12_Poll_adoption_measurement`.

Excluded: `ScopeOfWork.md`, `_REFERENCES.md`, dependency registers, reliance
hold, lifecycle state, estimates, schedules, release, and implementation.

## Entry checks

- `origin/main` descends from the D-PEC-68 durable merge.
- PRD v2.2 hash matches D-PEC-68.
- `pec_reliance_hold.py` returned `ALLOW` for exact-correction preparation
  against DEL-00-01 `CLM-005` / `REQ-004`.
- Pre-change `AUDIT_DECOMP`:
  `COV_SCA003_PRECHANGE_2026-07-28_0817`, status `OK`, 0 blockers,
  0 warnings.
- Strict register validation: 64 registers, 254 dependency rows,
  0 errors, 0 warnings.
