# B0 — focused dependency currency and deliverable mapping

Status: **bounded source/evidence basis established** for the activated first
wave. No project-readiness, producer maturity or dependency satisfaction is
asserted. Product/audit basis is `3bddc2b05f6106e969c7cf43373b230845c7cc66`;
activation HEAD is `86bb36d6fb88e7699df595bce1d6a31f5fbd6be5`. ROOT retains
remote-main/PR checks, Git, shared records and decisions.

## Currency evidence and fresh comparison

`execution/_DAG/_LATEST.md` names accepted DAG-011. Its actual owner adoption
is recorded in `_DAG/DAG-011/APPROVAL_RECORD.md` and
`_ScopeChange/_PostAcceptanceValidation/SCA-011_20260922T173404Z/OWNER_DECISION.md`.
The acceptance-time source-binding record is that postacceptance directory's
`dependencies/CURRENT_SOURCE_BINDINGS.json`, explained by `dependencies/RETURN.md`.
There is no `execution/_Evaluation/DAGCurrency/` directory here and no tracked
Piping path with “currency” in its name. That absence is only a search result.

A later local-versus-DAG comparison is retained at
`execution/_Coordination/WorkGraphs/PIPING_DEP_MATERIALIZATION_20260927/evidence/comparison.json`.
Its `direct_local_vs_accepted_dag` section reports all 1,571 rows, no only-local
or only-DAG rows, 1,036 identical rows and 535 rows whose DAG Notes extend local
Notes. That earlier comparison is historical evidence, not this response's
fresh verification. Its materializer reruns operated on scratch copies.

This response's `check_b0.py` reads only the four scoped local registers and
DAG-011. `B0_COMPARISON.json` records the complete comparison and hashes:

| Deliverable | Local / DAG rows | Active execution satisfaction retained | Structural differences |
|---|---:|---|---|
| DEL-04-01 | 11 / 11 | 8 SATISFIED | None; 11 DAG Notes extensions |
| DEL-04-05 | 9 / 9 | 5 SATISFIED, 2 TBD | None; 2 DAG Notes extensions |
| DEL-04-07 | 24 / 24 | 16 PENDING | None |
| DEL-09-01 | 14 / 14 | 8 SATISFIED, 3 TBD | None; 10 DAG Notes extensions |

The four `_DEPENDENCIES.md` row summaries were also read in full and agree
with their current CSVs. Their narrative pointers are not all current:
DEL-04-01 `_DEPENDENCIES.md:53` and DEL-04-05 `_DEPENDENCIES.md:51` retain “DAG-007 is current”
handoff wording, and DEL-09-01 `_DEPENDENCIES.md:72` retains an old R23
“DAG-008 remains graph authority” note beneath its newer current-pointer/
D-GOV-49 clause at line 5. The accepted `_LATEST.md` and
adoption record resolve the current version as DAG-011. Preserve these
historical words and carry the stale narrative pointers into bounded C0
reconciliation; this checkpoint does not rewrite their instructions. C0 must
stay bounded to these four mapped deliverables. Any correction outside DELIVERY
records requires ROOT to grant the precise documentary write set first.

No IDs are duplicate/missing, no canonical or satisfaction field differs,
and no nonempty aggregate extension field is absent locally in this scope.
The result is `NO_STRUCTURAL_DEPARTURE_FOUND`, not a whole-project currency
or acceptance verdict. No local register or accepted DAG byte was changed.

### Exact source-binding limits

The acceptance record's whole-source hashes are not all today's hashes.
`B0_SOURCE_DRIFT.json` and the two adjacent `.diff` files compare exact accepted
bytes found at `48f3481eca2b5c0c8dcea31d3f60078b5b1aa5ae` to current bytes:

- DEL-04-07 ScopeOfWork: accepted `2631a2fe…`; current `e3f70134…`.
  The only difference is the added “Delivery commitments and evidence limits”
  section preserving three obligations. All original clauses remain byte for
  byte. Fresh checks find all 24 dependency quotations in their named current
  frontmatter/CLM loci; their full-file hash mismatch stays disclosed.
- SOFTWARE_DECOMP: accepted `c78301c6…`; current `68862517…`.
  Revision 0.14 and later D-74–D-77 records include licensing, nonlinear units
  and single Package homes. D-77 explicitly preserves deliverable mappings
  and dependency edges; SOW-052 now has PKG-05 as its home with DEL-04-07's
  supporting contribution retained. This check does not recertify the entire
  decomposition or every historical source binding.
- DEL-04-07 `_CONTEXT.md` and `_REFERENCES.md` still match their recorded
  accepted whole-file hashes.

These are disclosed source-byte changes, not evidence of a new/removed edge
or cycle in this four-deliverable scope. A later structural departure must
route through the owning currency/decision process; no old snapshot is rewritten.

## Bounded maintained-path mapping

Aliases below are relative to `projects/chirality-piping`.

| Deliverable basis | Concrete response contribution | Binding and limit |
|---|---|---|
| DEL-04-01 OUT-001; CLM-004/006/016 | AUD-T3-01 proof/reachability and any separately selected repair in `core/solver/frame_kernel/src/structural/retained/` | SOW expressly identifies `core/solver/frame_kernel`; this does not close all kernel obligations |
| DEL-04-05 OUT-001; CLM-006/009 | K6c phase estimate, counts, harness regression and observations in `core/solver/performance_harness` | SOW expressly names this carrier; measurements do not set release thresholds |
| DEL-09-01 OUT-001; SOW-026 / OBJ-008 | Numerical-oracle and VR admission/dedup evidence in `validation/benchmarks/numerical_robustness` | **Bounded contribution mapping.** DEL-09-01 SOW/context names `validation/benchmarks/mechanics`, not VR. I17, T3 DESIGN §4.10/§6 (as quoted by I17), maintained VR README and VR Cargo metadata bind VR to the T3 VP-ROBUST lane. That lane supports numerical quality; no explicit DEL-09-01-to-VR maintained-path replacement or full ownership amendment was located in these scoped records. Retain that mapping limit for C0 reconciliation |
| DEL-04-07 CLM-001/004 | D2/F2a consequence analysis and downstream diagnostic/provenance handback | SOW places product composition/result handoff here; no product implementation or source/consumer acceptance in this response checkpoint |

Maintained VR is a concrete T3-owned authorized path under the existing I21
brief. The unresolved deliverable accounting detail does not create permission
to edit the mechanics suite, change the DAG or claim the entire benchmark
deliverable complete. ROOT confirmed this bounded-contribution interpretation
through native collaboration during this first wave.

## Unresolved dependencies and work boundary

- DEL-04-05 → DEL-04-01 (`DAG-002-E0444`) and → DEL-04-06 (`DAG-002-E0445`)
  remain TBD at required/proposed SEMANTIC_READY.
- DEL-09-01 → DEL-04-01 (`DAG-002-E0532`), → DEL-04-02 (`DAG-002-E0533`)
  and → DEL-02-02 (`TP-DAG-004-DEL-09-01-E001`) remain TBD at SEMANTIC_READY.
- DEL-04-07 has 16 PENDING execution dependencies with ProposedMaturity=TBD,
  including → DEL-04-01 (`DEP-04-07-013`).

The audit merge, source availability and structural register agreement satisfy
none of these edges. First-wave reading, independent checking, environment
inventory and checkpoint drafting may proceed under the activated brief. Later
implementation needs its bounded source/consumer witnesses, accepted design
where applicable and ROOT's runtime/slot grants. Whole-deliverable promotion
would require the owning maturity and satisfaction process.

Replay: from repository root run `python3 <Run>/instances/DELIVERY/check_b0.py`.
It prints JSON and writes no source. The committed JSON is the first-wave
snapshot; later HEAD identity may differ after ROOT integrates records.
