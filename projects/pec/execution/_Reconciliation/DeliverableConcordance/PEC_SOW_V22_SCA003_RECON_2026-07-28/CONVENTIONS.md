---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
doc_kind: deliverable_concordance.conventions
status: owner_approved
created: 2026-07-28
authority: D-PEC-69
---

# PEC contract-reconciliation conventions

## Owner-approved calibration

D-PEC-69 records these RECONCILIATION / Agent 0 recommendations as approved:

1. Preserve the `SOW_V1` schema, heading order, stable local IDs, objective
   mappings, output matrix, and all unaffected contract meaning.
2. Audit claims atomically. A whole contract is changed only when at least one
   claim is incompatible with accepted PRD v2.2 / SCA-003 truth.
3. Repair by whole-file replacement because `ScopeOfWork.md` is one canonical
   contract, but keep the semantic delta minimal and reversible.
4. Treat current PRD/decomposition/decisions as authority; tests and old PEC
   implementation are evidence only.
5. Preserve the following product boundary exactly:
   - PEC serves labeled, non-authoritative orientation on request.
   - An explicitly enabled consumer owns whether and when to consume, its
     mode mapping, contact cadence, and any optional injection.
   - PEC never self-polls, schedules a consumer, injects into an agent, or
     creates a receiving-loop duty or conformance criterion.
   - Pipeline and unscoped-conversation modes support zero contact.
   - P2-B records owner use or non-use as evidence about PEC; manual Step 0
     remains available.
6. DEL-00-01 must retain ADR-002 as live, cite ADR-014 as historical lineage
   only, and carry the accepted v2 runtime/client plus human-only-act boundary
   without re-adopting the retired PEC-project-adapter allocation.
7. New scope, renamed IDs, lifecycle changes, dependency changes, estimates,
   schedules, release semantics and reliance claims are forbidden.

## Claim dispositions

| Disposition | Meaning in this run |
|---|---|
| `ALIGNED` | Claim already matches accepted v2.2/SCA-003 truth |
| `DOCUMENTED_DIFFERENTLY` | Wording is stale or contradictory and requires the approved exact correction |
| `ACCEPTED_DIVERGENCE` | Deliberate retained contract-specific detail that does not conflict with authority |
| `AUTHORITY_CONFLICT` | Live sources disagree; repair stops for that claim |
| `UNKNOWN` | Evidence is insufficient; no repair inferred |
| `STALE_INPUT` | Frozen source changed; affected work reruns |

## Evidence and verification

- Every finding cites contract path, local claim ID/section, accepted source,
  and source commit.
- Every changed claim appears exactly once in the repair manifest and exactly
  once in post-repair re-extraction.
- `validate_scope_of_work.py`, `derive_review_checklist.py`,
  `check_boundary_owner_resolution.py`, and
  `scan_deliverable_consistency.py` govern deterministic contract checks.
- Full-population validation covers every one of the 32 active contracts.
- The final Remaining census represents all 64 deliverables, including
  explicit `NONE` for no recorded residual.

## Repair decision

The approved R4 recommendation is: apply the smallest exact whole-contract
repair to every execution-time-confirmed affected contract, provided semantic
comparison finds no new authority question. No separate per-claim owner pause
is required for ordinary corrections inside this accepted window. Any scope
addition or live-source conflict returns to the owner.
