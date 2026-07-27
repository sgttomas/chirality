# SCA-APP-005 — Root Runtime / App Client Boundary

**State:** `GATE_1_PENDING_OWNER_CONFIRMATION`
**Date:** 2026-07-26
**Requested by:** Ryan Tufts
**Managing agent:** SCOPE_CHANGE
**Variant:** `SOFTWARE`
**Accepted repository basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
**Allow renumbering:** `false`

> Historical intake record: the state and narrow action envelope below are
> preserved as Gate-1 evidence. The owner later approved the independently
> reconciled Revision 2 envelope in `Gate_2_Exhaustive_Seam_Matrix.md`,
> including Root/Tier-0/PEC coordination notices. The later ruling and exact
> amendment supersede this brief's pending-state and notice-exclusion posture
> without rewriting the original intake evidence.

## Human-initiated change

OD-2 Option A is adopted: Root owns generic runtime semantics and continuing
stewardship; Chirality App and PEC are clients. The accepted App
decomposition still contains a contradictory downstream note saying App
deliverables retain semantic ownership. The App decomposition must be
corrected narrowly so its retained work is client-side integration,
compatibility, packaging, credential-boundary, adapter/fallback, UX, and
acceptance evidence supported by ruled sources.

## Resolved inputs

- `CONTEXT_ROOT`:
  `projects/chirality-app-dev/execution`
- `DECOMPOSITION_PATH`:
  `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `SCOPE_CHANGE_ROOT`:
  `projects/chirality-app-dev/execution/_ScopeChange`
- Accepted App decomposition: v3.2, current SHA-256
  `952d3cbf81b0cea014a1c3f1bd3f62fbc0b23b96bfa1fd1913961731c925b08b`
- Upstream ruled basis:
  - D-GOV-20, especially ruled architecture items 1–10
  - D-GOV-28 and adopted Root PRD O-11
  - accepted Root decomposition revision 1.1 and its
    `SOW-104 → PKG-02 → DEL-02-06` carrier
  - D-APP-73 and SCA-APP-003 as the existing App-side migration basis

## Amendment ID resolution

The generic helper
`tools/query/scan_next_amendment_id.sh` returned `SCA-001` because it scans
the generic `SCA-NNN` grammar and does not understand this App loop's
established `SCA-APP-NNN` namespace. A direct scan of the App scope-change
root found accepted historical identifiers `SCA-APP-001` through
`SCA-APP-004` and no `SCA-APP-005`. The next local identifier is therefore
`SCA-APP-005`.

## Parsed action envelope

| Seq | Action | Entity type | Entity IDs | Requested change |
|---|---|---|---|---|
| A001 | `MODIFY` | `OTHER` | `APP-RUNTIME-BOUNDARY` | Correct unnumbered ownership/boundary statements in Intake Summary, Vocabulary Map, control-coverage notes, and Downstream Execution Notes. Root owns generic runtime semantics; App owns only its supported client duties and acceptance evidence. |
| A002 | `MODIFY` | `OTHER` | `SOW-037` | Replace the current “product-owned engine contract” statement, in both SSOW and Scope Ledger, with an App client-conformance responsibility under Root-owned generic runtime semantics. Preserve its package, deliverable, and objective mappings unless Gate 2 finds a mapping conflict. |
| A003 | `MODIFY` | `PACKAGE` | `PKG-03` | Preserve the package and ID while narrowing its responsibility to App-side runtime-client integration and compatibility. No package addition, removal, split, merge, or reclassification is proposed. |
| A004 | `MODIFY` | `DELIVERABLE` | `DEL-03-01` | Preserve the deliverable and its lineage while replacing generic-runtime semantic ownership with App-side client contract compatibility and conformance. Exact name and text remain a Gate-3 matter. |
| A005 | `MODIFY` | `OBJECTIVE` | `OBJ-002` | Replace the generic product-ownership implication with App client-boundary and conformance language while preserving the objective ID and mappings. |
| A006 | `MODIFY` | `OTHER` | `OI-007` | Reconcile the live shared-runtime open-issue text to adopted D-GOV-28/O-11 and accepted Root decomposition revision 1.1 if Gate 2 confirms the current text is incomplete. |
| A007 | `ADD` | `OTHER` | `DEC-021` | Add the SCA-APP-005 decision row after Gate-3 approval; do not rewrite historical DEC-019. |
| A008 | `ADD` | `OTHER` | `CHANGE-LOG-ENTRY` | Add the dated SCA-APP-005 revision entry after Gate-3 approval, separate from the decision row. |

## Gate-2 impact-classification set

Gate 1 does not silently convert the following rows into amendment actions,
but Gate 2 must trace and disposition each one because it is directly
connected to the corrected boundary:

| Classification | IDs | Gate-2 obligation |
|---|---|---|
| `NECESSARY_CONSEQUENTIAL_ALIGNMENT` | `SOW-009;SOW-010;SOW-011;SOW-012;SOW-015;SOW-038;DEL-03-02;DEL-03-04` | Trace impact and decide between an exact `MODIFY` and ruled-source `NO_CHANGE`; Gate 1 does not preselect the edit. |
| `GATE-2_OBSERVATION_ONLY` | `SOW-040;DEL-03-03` | Verify that the existing UI-event separation and compatibility-adapter language already expresses an App client duty. |
| `MAPPING_IMPACT_ONLY` | `DEL-01-02;DEL-09-02` | Verify that their SOW-037 reliance/conformance mappings remain valid; do not rewrite them merely because they share the mapping. |
| `HISTORICAL_NO_CHANGE` | `DEC-019` | Preserve the accurate historical record; SCA-APP-005 receives a new decision row. |

## Explicit exclusions

This SCA does not:

- add, remove, split, merge, reclassify, or renumber a package, deliverable,
  objective, or scope item;
- amend the App PRD or Root PRD;
- repin any ScopeOfWork contract or other accepted basis;
- perform OD-6 acceptance, invariant-register, APP-HOLD-1, D-APP-48,
  D-APP-49, consumer, version, or population-repin work;
- edit a deliverable-local ScopeOfWork or lifecycle file at Gate 1;
- apply Tier-0, PEC, or Piping notices;
- implement App, daemon, runtime, adapter, credential, UX, or parity code;
- introduce method reform, semantic parity, PEC dependence, or resource
  governance.

## Gate state

- Gate 1: `PENDING_OWNER_CONFIRMATION`
- Gates 2–5: `NOT_OPENED`
- Accepted decomposition and `_ScopeChange/_LATEST.md`: unchanged
