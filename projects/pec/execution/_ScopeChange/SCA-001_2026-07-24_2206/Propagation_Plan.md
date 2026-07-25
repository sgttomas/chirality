---
amendment_id: SCA-001
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-07-24
status: awaiting_gate_4_approval
accepted_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md revision 1.0
approved_preview: Amendment_Preview.md
authority: D-PEC-61
---

# SCA-001 Gate 4 — Propagation Plan

## Propagation boundary

Gate 5 may apply only the exact Gate 3 diff in `Amendment_Preview.md` and the
SCA-owned closure evidence described here. This plan creates no authority to
change implementation, dependencies, scaffolding, estimates, schedules,
project metadata, or the frozen reference corpus.

All four actions are `MODIFY`. There are no `ADD`, `REMOVE`, `RECLASSIFY`,
`MERGE`, or `SPLIT` actions; therefore there is no child-closure set, folder
creation/relocation, retirement, or lifecycle propagation.

## Direct Gate 5 writes

### Authoritative decomposition package

| Surface | Package role | Action | Exact authorized change |
|---|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | `working surface` | `DIRECT_EDIT` | Apply only the approved front-matter/source-basis, intake, C16, SOW-064, OBJ-006, PKG-10, DEL-10-10, telemetry, DL-16, and revision-history changes |
| `execution/_Decomposition/ScopeLedger.csv` | `authoritative companion register` | `DIRECT_EDIT` | Replace only the complete `SOW-064` row approved at Gate 3 |
| `execution/_Decomposition/Deliverables.csv` | `authoritative companion register` | `DIRECT_EDIT` | Replace only the complete `DEL-10-10` row approved at Gate 3 |
| `execution/_Decomposition/ContextBudgetQA.csv` | `authoritative companion register` | `DIRECT_EDIT` | Replace only the complete `DEL-10-10` QA row approved at Gate 3 |
| `execution/_Decomposition/_LATEST.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Replace with the approved revision 1.1 successor wording after validation supports it |

### SCA-owned state and evidence

| Surface | Package role | Action | Gate 5 disposition |
|---|---|---|---|
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/Post_Change_Coverage.json` | `snapshot / handoff artifact` | `RECOMPUTE` | Deterministically recompute register integrity and compare to `Pre_Change_Coverage.json` |
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv` | `snapshot / handoff artifact` | `RECOMPUTE` | Generate a header-only map with the registered accumulator and `--allow-empty` |
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/Handoff_State.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Record accepted basis, package/derivative state, warnings, closure, blockers, and downstream owners |
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/RUN_SUMMARY.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Record actions, pre/post comparison, state fields, and `CHANGE` handoff |
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/Decision_Log.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Record Gate 4 approval, Gate 5 execution/validation, and final owner confirmation |
| `execution/_ScopeChange/_LATEST.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Advance through Gate 5 execution to the honest final closure state |

`Amendment_Actions.csv`, `Brief.md`, `Pre_Change_Coverage.json`,
`Impact_Assessment.md`, `Amendment_Preview.md`, and this propagation plan
remain the approved historical record; Gate 5 does not rewrite their
substantive content.

## Recomputations and audit evidence

1. **Deterministic post-change baseline — SCOPE_CHANGE-owned**
   - Parse the same four authoritative package surfaces used by the Gate 1
     baseline.
   - Write `Post_Change_Coverage.json`.
   - Compare topology, statuses, mappings, lineage, objective support,
     Context Budget QA parity, package inventory existence, and SHA-256
     identities against `Pre_Change_Coverage.json`.
   - Record the absence of a durable repo-native validator as OI-013, not as
     evidence that the check did not run.

2. **Post-change `AUDIT_DECOMP` attempt — derivative evidence**
   - Dispatch `AUDIT_DECOMP` with `DECOMP_VARIANT=SOFTWARE`, `SCOPE=ALL`,
     accepted source revision 1.1, and expected handoff
     `SCOPE_CHANGE_GATE_5`.
   - Write only a new immutable audit snapshot and the audit tool's pointer
     under `execution/_Evaluation/DecompCoverage/`.
   - If Project Setup has still created zero deliverable folders, preserve the
     contract-required `FAILED_INPUTS` result as an expected warning. It does
     not replace deterministic register-integrity validation.

3. **Supersession state**
   - A001–A004 supplement construction direction and decomposition
     traceability. They do not contradict an admitted source DBM, discipline
     DBM, vendor fact, regulation, or other admitted authority fact.
   - Every action therefore has
     `SupersessionBindingPresent=NO`.
   - No `Supersession_Delta.csv` is required.
   - With no prior accepted map and no current delta, Gate 5 runs:

     ```text
     python3 tools/coordination/accumulate_supersession_map.py \
       --output-map projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/Supersession_Map.csv \
       --allow-empty
     ```

   - The result must be a schema-valid header-only cumulative map.

## Explicit no-change surfaces

| Surface | Classification | Reason |
|---|---|---|
| `projects/pec/docs/PRD.md` | `NO_CHANGE` | PRD v2.1 was already adopted and written under `D-PEC-61`; it is upstream authority for SCA-001 |
| PEC `AGENTS.md`, README, `docs/STATUS.md`, decision register, and loop receipts | `NO_CHANGE` | Already changed in the owner-governance tranche; outside SCOPE_CHANGE propagation |
| `execution/_Decomposition/Companion_Inventory.csv` | `NO_CHANGE` | Gate 3 confirmed no revision-parity field exists; file membership and package roles are unchanged |
| All non-target rows in `ScopeLedger.csv`, `Deliverables.csv`, and `ContextBudgetQA.csv` | `NO_CHANGE` | Exact approved amendment changes one row in each register |
| `execution/Dependencies.csv` / `WORK_GRAPH.json` | `NO_CHANGE` | Not present and not created by SCOPE_CHANGE; complete graph materialization belongs to `PROJECT_SETUP` |
| `execution/PKG-*/1_Working/DEL-*` and deliverable `_CONTEXT.md` / `_STATUS.md` | `NO_CHANGE` | Scaffolding does not exist; there is no metadata file to update and no paired status/memory read is required |
| Estimates and schedules | `NO_CHANGE` | Not present; future artifacts must consume revision 1.1 |
| Implementation and frozen reference corpus | `NO_CHANGE` | Outside D-PEC-61's SCOPE_CHANGE fence |

There is no `PREPARATION` dispatch in SCA-001. Creation of package and
deliverable folders, metadata, dependency truth, estimates, or schedules
would be premature and unauthorized.

## Downstream handoffs and reruns

| Workflow | Gate 5 action | State after SCA closure |
|---|---|---|
| `AUDIT_DECOMP` | Execute one post-change attempt | Derivative evidence; expected warning if still unscaffolded |
| SCOPE_CHANGE deterministic postcheck | Execute and compare pre/post | Required closure evidence |
| `PROJECT_SETUP` | Do not execute | Next owner after closure; consumes revision 1.1 and materializes owner-selected `FULL_GRAPH` |
| `PREPARATION` | Do not dispatch | Remains downstream of Project Setup's approved scaffold plan |
| Dependency extraction | Do not execute | Project Setup-owned; no `Dependencies.csv` is created here |
| Estimate/schedule workflows | Do not execute | Project Setup-owned and gated by its normal choices |
| `WORKING_ITEMS` | Do not execute | Cannot activate work before accepted scaffold/graph state |
| `CHANGE` | Do not execute before final owner confirmation | Receives the validated file list only after Gate 5 confirmation |

Project Setup retains its Phase 1.3 owner gate for dependency maturity
threshold and dependency-register storage. `FULL_GRAPH` itself is already
selected by `D-PEC-61`.

## Gate 5 execution order

1. Confirm Gate 3 amendment approval and Gate 4 propagation approval are
   recorded verbatim.
2. Re-hash all revision 1.0 authoritative inputs and compare them to
   `Pre_Change_Coverage.json`. Stop if any accepted input changed outside the
   approved preview.
3. Apply only the exact Gate 3 changes to the five direct decomposition
   surfaces.
4. Parse all CSVs and validate the exact post-change assertions below.
5. Generate the header-only `Supersession_Map.csv`.
6. Produce deterministic `Post_Change_Coverage.json` and compare it with the
   pre-change baseline.
7. Dispatch the post-change `AUDIT_DECOMP` attempt and preserve its exact
   result.
8. Run `git diff --check`, scoped path-fence inspection, PRD/decomposition
   source-anchor checks, and immutable-snapshot completeness checks.
9. Write `Handoff_State.md` and `RUN_SUMMARY.md`; update the SCA and
   decomposition pointers only to the state actually supported.
10. Present the post-change state for final owner confirmation. Only after
    that confirmation may `CHANGE` receive a scoped closeout handoff.

## Exact Gate 5 validation

### Structural and register checks

- Decomposition front matter says revision 1.1 and cites PRD v2.1 /
  `D-PEC-61`.
- C16 exists exactly once and is explicitly scoped to PEC's own build.
- Counts remain 94 scope items, 64 deliverables, 11 packages, 6 objectives.
- Status counts remain 71 `IN`, 14 `OUT`, 9 `TBD`.
- Every `IN` row has exactly one existing package and one existing
  deliverable.
- Every deliverable belongs to exactly one package; all `DEL-XX-YY` prefixes
  match parent packages.
- Every scope→deliverable and deliverable→scope reference resolves in both
  directions.
- `SOW-064 → PKG-10 → DEL-10-10 → OBJ-006`.
- `SOW-064` and `DEL-10-10` carry PRD v2.1 / D-PEC-61 direction without
  treating `FULL_GRAPH` as an eventual product-mode priority.
- All six objectives retain scope-item and deliverable support.
- OBJ-006 support is 9 scope items and 9 deliverables.
- IN items without objective mapping are 31.
- `DEL-10-10` is `TEST_SUITE`, `P1`, Context Envelope `M`, and has one
  matching `M` QA row.
- Context Envelope counts are S 28 / M 34 / L 2 / XL 0.
- `Companion_Inventory.csv` is byte-for-byte unchanged and every listed path
  exists.
- The telemetry revision is exactly `1.1, 2026-07-24 (SCA-001)`.
- DL-16 and revision-history 1.1 occur exactly once; historical gate/DL/OI
  rows remain unchanged.

### Fence and non-effects

- No `Dependencies.csv`, `WORK_GRAPH.json`, package/deliverable folder,
  `_CONTEXT.md`, `_STATUS.md`, estimate, schedule, implementation, or frozen
  corpus file is created or changed.
- PRD v2.1 and D-PEC-61 project-pointer changes remain outside the SCA write
  diff.
- No new network, database, dependency, runtime, or external-system action
  occurs.

## Rollback

Before applying Gate 5, the accepted revision 1.0 hashes in
`Pre_Change_Coverage.json` are the rollback identity.

- If a pre-apply hash differs, stop without writing decomposition truth and
  return the conflict to the owner.
- If application or validation fails before final owner confirmation, apply
  the exact reverse of the approved Gate 3 diff only to SCA-001's five direct
  decomposition surfaces; verify all six pre-change hashes; leave the SCA
  snapshot as honest `OPEN`/`BLOCKED` evidence and keep Project Setup held.
- Never use a broad Git reset or overwrite unrelated worktree state.
- After final owner confirmation, revision 1.1 is accepted truth. Any rollback
  then requires a successor owner act; the immutable SCA-001 snapshot remains
  historical evidence.

## Expected closure state

After successful Gate 5 validation and owner confirmation:

| Field | Expected value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `COMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `WARNINGS` if the only warning is expected pre-scaffold `FAILED_INPUTS`; otherwise reflect the actual result |
| `ReadyForNextPhase` | `REGEN_ONLY` |
| Closure verdict | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |
| Next owning workflow | `PROJECT_SETUP`, then `CHANGE` for scoped Git closeout after owner confirmation |

`DerivativePackageState=COMPLETE` means the affected decomposition package
and SCA-owned evidence are internally consistent. It does not claim that
Project Setup, scaffolding, dependency materialization, estimates, schedules,
implementation, or heterogeneous-loop validation has run.

## Gate 4 confirmation question

**Do you approve this propagation plan?**
