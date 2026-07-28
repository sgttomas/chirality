---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-03-06
mode: VERIFY
production_format: SOW_V1
source_state: INITIALIZED
status: complete
---

# DEL-03-06 read-only discovery notes

## Source identities

- Contract:
  `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md`
- Contract SHA-256:
  `d8763664b28333df8a802c476c8796647eb4adc278196a0166a7ef4c456e41f7`
- `_STATUS.md` SHA-256:
  `a024c5ed98513acfde552d651ea0e7fd5c0f99c35eea7f300034d6aee1cf48a4`
- Lifecycle state of record: `INITIALIZED`.
- Frozen source commit:
  `404e47c16a88e7ffdc6d1fc5fac61ebb6864211e`.
- PRD v2.2 SHA-256:
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
- SOFTWARE_DECOMP revision 1.3 SHA-256:
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.

The contract and `_STATUS.md` remained byte-identical during this worker run.
No production or control surface was edited.

## Deterministic checks

| Check | Result |
|---|---|
| `validate_scope_of_work.py --json` | `SOW_V1`, valid, zero issues |
| `derive_review_checklist.py` | 16 acceptance items; source hash matches the contract |
| `check_boundary_owner_resolution.py` | `OK`; one whole-requirement boundary checked; zero unresolved owners, undefined claims, not-checkable clauses, or uncited whole-requirement exclusions |
| `scan_deliverable_consistency.py` | zero missing artifacts, identity mismatches, or candidate unsourced numerics; 21 marker hits, all attributable to explicit contract records/references rather than an unrecorded placeholder |

Semantic boundary backcheck also passes. `REQ-008` enumerates adjacent acts
and cites `CLM-016`/`CLM-017`, where each act has a named deliverable owner.
The narrower exclusions in `REQ-001`, `REQ-002`, `REQ-006`, `REQ-007`,
`REQ-011`, and `REQ-012` either resolve to their cited upstream/adjacent
owners or explicitly preserve an unassigned obligation without inventing one.

## Claim census

- Bold local definitions extracted: **88**.
- `CLM`: 20; `OUT`: 2; `TBD`: 5; `REQ`: 14; `AC`: 16;
  `CON`: 6; `VER`: 13; `AX`: 12.
- `ALIGNED`: 85.
- `DOCUMENTED_DIFFERENTLY`: 3.
- `ACCEPTED_DIVERGENCE`: 0.
- `AUTHORITY_CONFLICT`: 0.
- `UNKNOWN`: 0.
- `STALE_INPUT`: 0.

Explicit `TBD-*` and `CON-*` definitions remain aligned records of known
unknowns or conflicts. They are not silently resolved and are not classified
`UNKNOWN` merely because their own epistemic content preserves uncertainty.

## Exact repair candidates

1. `CLM-016`, line 374:
   - Replace the stale PRD P1 scope quotation
     `"API for one loop (piping or root)"` with the accepted v2.2 P1
     first-ingestion wording for PEC's own build graph.
   - Replace the stale §11 metric label `"harness poll adoption"` with
     `"consumer uptake"`.
   - Preserve the claim's valid conclusion that §11 contains no rebuild
     performance metric and that DEL-03-06 owns no §11 reporting cadence.
2. `CLM-020`, line 381: replace lifecycle state `OPEN` with `INITIALIZED`;
   leave `_STATUS.md` untouched.
3. `AX-012`, line 480: replace lifecycle state `OPEN` with `INITIALIZED`;
   leave `_STATUS.md` untouched.

Whole-contract replacement should also refresh the non-claim provenance at
frontmatter line 5 and the Purpose section's revision-1.2 basis paragraph to
revision 1.3 / SCA-003. The existing explanation that `_REFERENCES.md`
contains deferred provenance must be updated without editing that excluded
file. After changing `CLM-016`, update the quotation record so it truthfully
describes the current quoted PRD v2.2 row.

## Consumer-interface terminology adjudication

- The only stale polling wording is `"harness poll adoption"` inside
  `CLM-016`. It is a superseded metric label, not a valid duty.
- No local definition forces session-start contact, a mode-transition poll,
  injection, an external cadence, receiving-loop conformance, or P2 use as a
  gate.
- `CLM-015` and `AX-010` use “consumer” only for a dependency-graph
  downstream relation. That terminology is neutral and creates no PEC
  consumption duty.
- “practitioner-harness” denotes the parity peer, and “measurement harness”
  denotes this test suite's machinery. Neither is a PEC-enabled interface
  consumer or a contact rule.
- `CLM-019` affirmatively states that the contract creates no reporting
  cadence; that statement is aligned with PRD v2.2.

## Return

The exact changed-claim candidate set is:
`{CLM-016, CLM-020, AX-012}`.
There is no authority conflict and no unresolved semantic ruling needed for
these corrections. W1 performed discovery only; repair and revalidation
belong to the later authorized wave.
