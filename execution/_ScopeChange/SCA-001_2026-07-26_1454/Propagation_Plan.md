---
amendment_id: SCA-001
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-07-26
status: approved_gate_4
accepted_gate_3_candidate: Gate_3_Candidate/ (seven exact surfaces)
requested_by: Ryan Tufts
---

# SCA-001 Gate 4 — Propagation Plan

## 1. Propagation boundary

Gate 3 approved one new scope item and one new PKG-02 deliverable:

```text
O-11
  → SOW-104
  → PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
  → DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
  → OBJ-001, OBJ-002, OBJ-004, OBJ-007
```

This plan does not change those bytes. It identifies where the approved
amendment is applied, what downstream state becomes stale, who owns each
follow-on, how the successor is validated, and how rollback works.

No parent package changes, so there is no child-remap closure set. The only
new child is DEL-02-06 under the existing PKG-02. DEL-02-01..DEL-02-05 and all
other existing deliverables remain unchanged.

## 2. Gate 5 direct-write surfaces

SCOPE_CHANGE may write only the following direct surfaces at Gate 5.

| Surface | Classification | Exact Gate 5 action |
|---|---|---|
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `DIRECT_EDIT` | Replace with the Gate 3 approved candidate bytes |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `DIRECT_EDIT` | Replace with the approved candidate containing SOW-104 |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `DIRECT_EDIT` | Replace with the approved candidate containing DEL-02-06 |
| `execution/_Decomposition/chirality_root_objective_register_v1_0.csv` | `DIRECT_EDIT` | Replace with the approved OBJ-001/2/4/7 mappings |
| `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv` | `DIRECT_EDIT` | Replace with the approved 85-row forward register |
| `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv` | `DIRECT_EDIT` | Replace with the approved 52-row reverse register |
| `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md` | `RECOMPUTE_FROM_APPROVED_CANDIDATE` | Replace with the approved reconciled telemetry bytes |
| `execution/_ScopeChange/SCA-001_2026-07-26_1454/**` | `DIRECT_EDIT` | Record Gate 4/5 decisions, actions, post-change audit, coverage comparison, supersession state, run summary, and handoff |
| `execution/_ScopeChange/_LATEST.md` | `DIRECT_EDIT` | Point to the closed or still-open SCA state and current decomposition basis |

No `execution/_Decomposition/_LATEST.md` exists. This SCA will not invent one:
the root decomposition's stable paths, revision metadata, SCA snapshot, and
scope-change pointer provide the approved identity chain.

### Gate 5 copy discipline

1. Re-run `validate_gate3_candidate.py`.
2. Recompute all seven candidate hashes and require exact equality with
   `Gate_3_Validation.json`.
3. Copy those exact bytes to the seven authoritative paths; do not regenerate
   semantic text during application.
4. Record per-file before and after SHA-256 values.
5. Run the post-change validations in §7.
6. Present the applied state to the owner. The v1.0 predecessor remains
   current until that Gate 5 confirmation; confirmation makes the exact v1.1
   successor current.

## 3. Surfaces unchanged by SCOPE_CHANGE

| Surface | Classification | Reason |
|---|---|---|
| `docs/PRD_ROOT.md` | `NO_CHANGE` | Revision 6 and O-11 are already adopted |
| D-GOV-20 and D-GOV-28 | `NO_CHANGE` | Upstream authority records |
| Existing 45 deliverable folders and `ScopeOfWork.md` files | `NO_CHANGE` | No existing deliverable changed; no mechanical repin |
| `runtime/**` | `NO_CHANGE` | A planning locus is not implementation authorization |
| `execution/_harness/**` | `NO_CHANGE_IN_SCA` | PROJECT_SETUP owns state refresh after accepted amendment |
| App and PEC PRDs, decompositions, SOWs, or implementation | `NO_CHANGE` | Client scope changes require their own instruments |
| Root validator code and CI | `NO_CHANGE` | Existing G0–G4 capability is sufficient; only state changes |
| Estimate, schedule, budget, usage, cost, forecast surfaces | `NO_CHANGE` | No active Root resource-governance artifact was identified; service remains optional |
| Public-export profile | `NO_CHANGE` | Root `execution/` is excluded; no export rule changes |

## 4. Downstream PROJECT_SETUP / PREPARATION handoff

This work begins only after Gate 5 owner confirmation and Git closeout of the
accepted v1.1 decomposition. It is not performed by SCOPE_CHANGE.

### 4.1 DEL-02-06 scaffold

PROJECT_SETUP dispatches PREPARATION using `Preparation_Brief.md`. The sole
new deliverable path is:

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/`

Required outputs:

- `_CONTEXT.md`, transcribed from the accepted v1.1 register;
- `_STATUS.md`, initialized to `OPEN`;
- `_REFERENCES.md`;
- `_DEPENDENCIES.md`, mode `DECLARED`, with no invented edge;
- `_SEMANTIC.md`, placeholder only; and
- `_MEMORY.md`, non-authoritative, when the current PREPARATION policy is
  applied.

`ScopeOfWork.md`, production artifacts, and `runtime/**` changes are
prohibited in this dispatch. `ScopeOfWork.md` is a later governed
WORKING_ITEMS/SOW-authoring action.

### 4.2 G1 adapter baseline

`execution/_harness/adapter.yaml` is a newly identified propagation surface.
Its current `baselines.status_files: 45` is exact for the predecessor tree.
After DEL-02-06 `_STATUS.md` exists, G1 will BLOCK unless PROJECT_SETUP
refreshes the baseline in the same serialized state-refresh tranche:

```diff
-  status_files: 45
+  status_files: 46
```

`status_mismatch` must be observed, not assumed, and written to its measured
value. `pinned_at` must name the accepted SCA-001 v1.1 Git basis used by
PROJECT_SETUP. The expected healthy value is zero mismatches, but observation
governs.

### 4.3 G2 surface ownership

PROJECT_SETUP updates
`execution/_harness/surface_ownership.yaml` after the v1.1 decomposition is
accepted:

1. add `runtime/**` to the PKG-02 package entry; and
2. add a deliverable-level entry:

```yaml
  - id: DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
    kind: deliverable
    decomposition_ref: DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
    write_targets:
      - execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/**
      - runtime/**
    instruction_surface: false
    serialization: null
```

The package/deliverable overlap is an intentional static ownership relation.
G2 may report it as informational; concurrency and serialization remain G3
questions.

### 4.4 G3 work graph

PROJECT_SETUP updates `execution/_harness/work_graph.yaml`:

- `accepted_basis` becomes the accepted v1.1 Git basis;
- the existing PKG-02 node gains `runtime/**`;
- the node remains `pending`;
- no package node is added or removed; and
- no `depends_on` or `serialized_after` edge is invented.

Any later dispatch that touches `runtime/**` requires a bounded brief whose
targets are covered by the PKG-02 node and the G2 register. Whether a
particular runtime change overlaps another active node is decided from that
accepted work graph and brief, not by this SCA.

### 4.5 Guard registration

`execution/_harness/root_guards.yaml` and validator code remain unchanged.
PROJECT_SETUP runs G0, G1, G2, G3, and G4 after the state refresh and records
their actual outputs. Any validator-code gap returns as separate governed
work; it is not silently repaired in the state tranche.

## 5. Dependency and contract follow-ons

### Dependency state

PREPARATION creates DEL-02-06 `_DEPENDENCIES.md` with `Mode: DECLARED` and no
accepted upstream or downstream edge. A later dependency-extraction task may
identify candidates involving boundary, capability-control, evidence,
export, or release deliverables. Candidates do not become graph edges without
human disposition.

The accepted package graph remains six flat nodes with no ordering edges.

### SOW state

- No `ScopeOfWork.md` is created by SCOPE_CHANGE or PREPARATION.
- WORKING_ITEMS may author the DEL-02-06 contract only after the scaffold and
  refreshed guards pass.
- The contract basis must be the accepted v1.1 decomposition Git identity.
- Existing 45 SOWs are not mechanically repinned. Their content remains
  current for unchanged rows; any successor-basis refresh follows a separate
  evidence-based review, beginning with PKG-02.

## 6. Coordination and optional-service follow-ons

| Follow-on | Owner | Gate 4 disposition |
|---|---|---|
| App and PEC notice of accepted Root carrier | Root coordination / receiving loops | Route after Gate 5 acceptance; notice coordinates and grants no client scope |
| App architecture SCOPE_CHANGE | App owner | Separate live gate; not authorized here |
| PEC external-owner annotation or profile work | PEC owner | Separate live gate; not authorized here |
| Piping or other client notices | Owning coordination route | Only where an evidenced consumer relation requires it; no universal broadcast inferred |
| Resource governance | Optional service owner | No activation; if later selected, consume the accepted successor graph for estimates, sequencing, locks/freezes, budgets, usage, cost, and forecasts |

## 7. Validation and closure sequence

### 7.1 Before application

- accepted v1.0 hashes equal the Gate 1 baseline;
- Gate 3 candidate hashes equal `Gate_3_Validation.json`;
- `DEL-02-02` candidate row equals the accepted row;
- authoritative decomposition paths have no unapproved intervening change;
- `git diff --check` passes.

### 7.2 Immediately after decomposition application

- run `validate_gate3_candidate.py` parity against the applied surfaces;
- run the 104/46 deterministic register-integrity suite;
- run `AUDIT_DECOMP` and preserve its real result;
- run relevant governance/path-anchor checks;
- confirm 104 scope items, 95 IN, 9 OUT, 0 TBD;
- confirm 46 deliverables, 6 packages, 7 objectives;
- confirm all IN items have one package and at least one deliverable;
- confirm `SOW-104 → PKG-02 → DEL-02-06 → OBJ-001/2/4/7`;
- confirm O-11 forward coverage and DEL-02-06 reverse trace;
- confirm all seven candidate/applied hashes match;
- confirm no `runtime/**`, existing deliverable, SOW, App, or PEC file changed.

Before scaffold, AUDIT_DECOMP is expected to report one missing filesystem
carrier: DEL-02-06. That is a real downstream derivative gap and must appear
in the handoff. It does not invalidate internally closed decomposition truth.

### 7.3 SCA closure state

If all decomposition checks pass and the only production gap is the absent
downstream scaffold/guard refresh:

- `DecompositionTruthState=COMPLETE`;
- `DerivativePackageState=INCOMPLETE`;
- `ContentRemediationState=NOT_REQUIRED`;
- `DownstreamRerunState=REQUIRED`;
- `MetadataAlignmentState=NOT_REQUIRED`;
- `AuditState=WARNINGS` or the exact AUDIT_DECOMP state;
- `ReadyForNextPhase=PROJECT_SETUP_ONLY`; and
- `ClosureVerdict=CLOSED_FOR_SCOPE_CHANGE_ONLY`.

PROJECT_SETUP later proves:

- 46/46 status files;
- G1 baseline parity;
- G2 ownership of the DEL-02-06 tree and `runtime/**`;
- G3 PKG-02 target coverage at the accepted basis;
- G0–G4 PASS; and
- no dispatch before those conditions.

## 8. Snapshot and supersession

Gate 5 creates:

- `Post_Change_Coverage.json`;
- `RUN_SUMMARY.md`;
- the final `Handoff_State.md`;
- per-file before/after hash evidence; and
- `Supersession_Map.csv`.

SCA-001 introduces no supersession. The map is generated header-only with the
deterministic accumulator's `--allow-empty` mode; rows are not hand-authored.
The Gate 1 AUDIT_DECOMP snapshot remains immutable pre-change evidence.

## 9. Rollback

### Before Gate 5 owner confirmation

If application or validation fails:

1. restore the seven authoritative decomposition surfaces to their recorded
   Gate 1 SHA-256 identities;
2. verify the 103/45 predecessor baseline;
3. record `ROLLED_BACK_BEFORE_GATE_5_CONFIRMATION` in the SCA decision and
   handoff records;
4. keep the approved Gate 3 candidate and failure evidence immutable; and
5. do not release PROJECT_SETUP.

### After Gate 5 owner confirmation

The v1.1 successor is accepted truth. It is not silently rolled back. Any
reversal requires a new human-initiated SCOPE_CHANGE with stable-ID and
downstream-state impact assessed anew.

## 10. Gate 4 question

Do you approve this propagation plan?

## 11. Gate 4 disposition

Approved by Ryan Tufts in session on 2026-07-26:

> I approve this propagation plan

Gate 5 application is limited to the exact direct-write boundary in §2.
