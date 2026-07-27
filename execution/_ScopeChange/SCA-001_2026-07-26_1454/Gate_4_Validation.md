# SCA-001 Gate 4 Validation

Date: 2026-07-26  
Result: `PASS_WITH_RECORDED_DOWNSTREAM_STATE_CHANGES`

## Current-state measurements

| Check | Result |
|---|---|
| Root status files | 45 |
| DEL-02-06 folder | Absent, as expected before approved propagation |
| G1 adapter baseline | `status_files: 45` |
| G2 entries | 6 package entries; PKG-02 owns only its execution subtree |
| G3 nodes | 6 package nodes; PKG-02 owns only its execution subtree |
| Package edges | None |
| Authoritative decomposition changes during Gates 1–4 | None |

## Guard verification

Using the repository's configured `python` interpreter, which supplies
PyYAML:

```text
python tools/validation/validate_root_harness_adapter.py
G1 PASS: schema-valid; status_files=45; pinned baseline matches.

python tools/validation/validate_root_surface_ownership.py
G2 PASS: schema-valid; 6 entries; 6 materialized package children registered.

python tools/validation/validate_root_work_graph_dispatch.py
G3 PASS: schema-valid; 6 nodes; no active node; targets and serialization pass.
```

The system `/usr/bin/python3` lacks PyYAML and returns each YAML guard's
documented operational exit 2. That is an interpreter-capability observation,
not a state failure. Gate 5 and PROJECT_SETUP must record the interpreter used.

## Propagation consequences verified

1. Adding the new `_STATUS.md` makes the observed status-file population 46;
   G1 therefore requires an adapter-baseline refresh in the same PROJECT_SETUP
   tranche.
2. A PKG-02 work-graph node that writes `runtime/**` will fail G3's G2 coverage
   tie-in unless the PKG-02 G2 package entry also owns `runtime/**`.
3. A deliverable-level G2 entry can record the finer DEL-02-06 boundary
   without changing the package-node graph.
4. `runtime/**` is not an instruction-surface target under the current G2/G3
   validator enumeration; `instruction_surface: false` is therefore the
   correct static classification.
5. No dependency edge is required by the accepted decomposition amendment.
6. Validator code, root guard registration, existing deliverables, SOWs,
   clients, and product code require no Gate 5 edit.

## Plan completeness verdict

The propagation plan covers:

- all seven approved authoritative decomposition surfaces;
- the SCA snapshot and pointer;
- the sole new child scaffold;
- G1, G2, and G3 state refresh;
- G0–G4 reruns;
- dependency and SOW boundaries;
- optional resource-governance non-activation;
- coordination routes;
- pre/post validation;
- closure state; and
- rollback before and after Gate 5 confirmation.

Gate 4 validation did not itself authorize any listed write. The owner
subsequently approved `Propagation_Plan.md` in session on 2026-07-26, opening
Gate 5 under its exact boundary.
