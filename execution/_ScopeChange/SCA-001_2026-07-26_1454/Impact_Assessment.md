---
amendment_id: SCA-001
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-07-26
status: awaiting_gate_2_confirmation
accepted_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md revision 1.0
upstream_authority: D-GOV-28; Root PRD Revision 6; O-11
---

# SCA-001 Gate 2 — Impact Assessment

## Assessment summary

SCA-001 reconciles the accepted Root decomposition to the adopted O-11
requirement for continuing Root stewardship of the generic runtime. The
smallest coherent topology change is:

1. add one atomic IN scope item, using the next available stable identifier
   `SOW-104`;
2. add one standing runtime-stewardship deliverable under the existing
   `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`, using the next
   available stable identifier `DEL-02-06`; and
3. reconcile the package description, four objective mappings, forward and
   reverse traceability, telemetry, source basis, and change history.

No package or objective is added. No existing ID is renamed, retired,
reclassified, or reused.

The existing
`DEL-02-02_Three_Layer_Authority_Boundary_Conformance` is not an adequate
carrier for O-11. Its accepted purpose is the conformance boundary among the
three operative layers; its context note says “no implementation change
implied,” and its SOW limits outputs to a layer register, separation notes,
and a fourth-substrate guard. Expanding it to own consequential `runtime/`
changes, versioned contracts, client migration/conformance, regression
evidence, and release disposition would combine two artifact kinds and erase
the distinction the architecture review required.

| Impact dimension | Gate 2 conclusion |
|---|---|
| Package topology | Unchanged: 6 packages |
| Deliverable topology | Add one `PKG-02` deliverable: 45 → 46 |
| Scope topology | Add one IN item: 103 → 104; IN 94 → 95 |
| Objectives | Unchanged: 7; new carrier supports OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| Stable IDs | All existing IDs preserved; next IDs `SOW-104` and `DEL-02-06` |
| Existing boundary carrier | `DEL-02-02` remains unchanged and distinct |
| Root write locus | New deliverable anticipates bounded writes to `runtime/**` plus its execution/evidence tree |
| Authority | Root PRD Revision 6 and D-GOV-28 are adopted upstream authority |
| Implementation | Not authorized by decomposition amendment or this assessment |
| Downstream hold | Root package dispatch that could rely on runtime stewardship remains held until SCA closure and guard-state refresh |

## Topology alternatives assessed

| Alternative | Assessment | Disposition |
|---|---|---|
| Modify `DEL-02-02` only | Conflicts with its accepted boundary-conformance purpose and “no implementation change implied” envelope; would mix boundary verification with implementation/release stewardship | Not recommended |
| Add a new package | PKG-02 already expressly owns the operative runtime layer; a seventh package would duplicate that work domain | Rejected as unnecessary topology |
| Add one `PKG-02` deliverable | Preserves the boundary/stewardship distinction, gives O-11 a standing carrier and declared `runtime/` locus, and keeps all existing IDs stable | Recommended |
| Split O-11 across multiple new deliverables | Possible if Gate 3 proves one bounded carrier cannot meet the context budget, but presently creates avoidable coordination and ownership seams | Held as Gate 3 fallback |

The Gate 3 preview must test the recommended single deliverable against the
Context Envelope rules. `M` is the initial recommendation because the
standing carrier governs one proportionate runtime-change tranche at a time;
`L` is the bounded fallback if the exact artifact set cannot be kept coherent
at `M`. `XL` is not acceptable.

## Impact by action

| Action | Decomposition structure | Companion-register impact | Downstream consequence | Principal risk |
|---|---|---|---|---|
| A001 — source basis | Advance the sole scope source from Root PRD Rev 5 to adopted Rev 6 and cite D-GOV-28 as the adopting instrument | No topology row; source and revision references update across the working surface and coverage records | Every successor consumer must cite the accepted SCA basis, not mutable PRD prose alone | Treating D-GOV-20 or D-T0-23 as a second scope source; Gate 3 must preserve the PRD as sole scope source |
| A002 — atomic scope | Add `SOW-104` for O-11 as one IN item under PKG-02 | Scope ledger; objective register; forward/reverse trace; telemetry | New SOW contract cannot be relied upon until PROJECT_SETUP/PREPARATION and SOW authoring complete | Overloading one row with separable requirements; Gate 3 must keep the statement bounded to the standing stewardship carrier |
| A003 — standing carrier | Add `DEL-02-06` under PKG-02 and clarify the package description; keep DEL-02-02 unchanged | Deliverable register; objective register; forward/reverse trace; telemetry | PROJECT_SETUP must create the deliverable scaffold and refresh G2/G3 guard state before dispatch | A broad carrier could become an unbounded “all runtime work” bucket; activation briefs must remain change-bounded |
| A004 — traceability | Add O-11 forward coverage and new reverse unit; update OBJ-1/2/4/7 aggregates, counts, context QA, decisions, revision history, and open issues | All six companion registers are affected | Audits and SOW-basis review must consume the successor snapshot | Partial parity could make the amendment appear covered while one register remains on v1.0 |

## Proposed lineage and boundary

The Gate 2 topology recommendation is:

```text
O-11
  → SOW-104
  → PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
  → DEL-02-06 (exact name approved only at Gate 3)
  → OBJ-001, OBJ-002, OBJ-004, OBJ-007
```

`DEL-02-02` continues to own the three-layer authority-boundary conformance
slice (`SOW-027`, `SOW-035`). The new deliverable owns continuing generic
runtime stewardship: bounded `runtime/` semantic changes, versioned-contract
evidence, affected-client conformance or migration evidence, proportionate
regression evidence, and a human release disposition. Client implementation
does not transfer ownership.

The amendment creates a scope carrier and planning locus. It does not itself
authorize a runtime edit, decide a release, grant authority to transport,
change credential/session ownership, or settle any D-GOV-28 open seam.

## Expected telemetry deltas

These are impact predictions, not Gate 3 amendment text:

| Metric | Before | Expected after approved amendment |
|---|---:|---:|
| Scope items | 103 | 104 |
| `IN / OUT / TBD` | 94 / 9 / 0 | 95 / 9 / 0 |
| Packages | 6 | 6 |
| Deliverables | 45 | 46 |
| Objectives | 7 | 7 |
| Context Envelopes `S / M / L / XL` | 14 / 30 / 1 / 0 | 14 / 31 / 1 / 0 if Gate 3 accepts `M` |
| Forward PRD items | 84 | 85, adding O-11 |
| Reverse-trace units | 51 | 52, adding DEL-02-06 |
| Unassigned IN items | 0 | 0 |
| IN items without a deliverable | 0 | 0 |
| Unmapped objectives | 0 | 0 |

The four-category demonstration is expected to gain one Operative Product
scope item and deliverable. Whether Evidence is also assigned is an exact
Gate 3 classification question; the category classification does not alter
package ownership.

## Authoritative surface classification

`Classification` describes the eventual approved Gate 5 disposition. Gate 2
changes only SCA-owned evidence and pointers.

| Surface | Package role | Classification | Gate 2 authority and impact |
|---|---|---|---|
| `docs/PRD_ROOT.md` | Upstream product definition | `NO_CHANGE` | Exact Rev 6 bytes are already adopted; SCOPE_CHANGE consumes them |
| `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md` | Upstream authority record | `NO_CHANGE` | Adopts O-11 and supplies the applied-state identity |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `working surface` | `DIRECT_EDIT` | Eventual revision 1.1 source, package, deliverable, trace, decision, open-issue, and revision summaries |
| `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` | `authoritative companion register` | `DIRECT_EDIT` | Add SOW-104 |
| `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` | `authoritative companion register` | `DIRECT_EDIT` | Add DEL-02-06 |
| `execution/_Decomposition/chirality_root_objective_register_v1_0.csv` | `authoritative companion register` | `DIRECT_EDIT` | Reconcile OBJ-001/2/4/7 scope and deliverable mappings |
| `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv` | `authoritative companion register` | `DIRECT_EDIT` | Add O-11; reconcile affected objective rows |
| `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv` | `authoritative companion register` | `DIRECT_EDIT` | Add DEL-02-06 and reconcile PKG-02 |
| `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md` | `authoritative companion register` | `RECOMPUTE` | Counts, context QA, category membership, F4, revision, and open-issue telemetry |
| `execution/_ScopeChange/SCA-001_2026-07-26_1454/**` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Progressive gate evidence; incomplete until Gate 5 |
| `execution/_ScopeChange/_LATEST.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Points to this active, incomplete SCA state without changing decomposition truth |
| Gate 1 audit snapshot | `derived publication artifact` | `NO_CHANGE` | Immutable v1.0 pre-change evidence |
| Future Gate 5 audit snapshot | `derived publication artifact` | `RECOMPUTE` | Required after the amendment; expected to surface the not-yet-created DEL-02-06 scaffold |
| `Supersession_Delta.csv` | `snapshot / handoff artifact` | `NO_CHANGE` / not required | O-11 is an adopted supplementary requirement and overrides no admitted authority fact |

## Downstream and guard-state classification

These surfaces are not written by SCOPE_CHANGE. They become downstream work
only after an accepted Gate 5 amendment.

| Surface / package | Owner | State after amendment | Required action |
|---|---|---|---|
| `execution/PKG-02.../DEL-02-06.../` | PROJECT_SETUP → PREPARATION | `STALE_REBUILD_REQUIRED` / absent | Create `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, and the working folder; no implementation |
| New `ScopeOfWork.md` | Governed SOW authoring / WORKING_ITEMS | `NOT_CREATED` | Author and validate from accepted SOW-104/DEL-02-06 only after scaffold |
| Existing 45 Root SOW contracts | Owning Root loop / RECONCILIATION | `CURRENT_FOR_UNCHANGED_ROWS; BASIS_REVIEW_REQUIRED` | Do not mechanically repin; determine which contracts require successor-basis refresh, with PKG-02 reviewed first |
| `execution/_harness/surface_ownership.yaml` (G2) | PROJECT_SETUP | `STALE_REBUILD_REQUIRED` | Record the accepted `runtime/**` ownership locus at package/deliverable granularity and keep instruction-surface classification accurate |
| `execution/_harness/work_graph.yaml` (G3) | PROJECT_SETUP | `STALE_REBUILD_REQUIRED` | Refresh accepted basis and PKG-02 declared targets; preserve package-level graph unless dependency evidence justifies an edge |
| Root G0–G4 validators | HELPS_HUMANS / PROJECT_SETUP as applicable | `CAPABILITY_CURRENT; STATE_REVALIDATION_REQUIRED` | Re-run against refreshed G2/G3 state; change validator code only through separate authority if a real capability gap appears |
| Deliverable-local dependency surfaces | PROJECT_SETUP / dependency workflow / human declarations | `NEW_ROW_REQUIRED_FOR_DEL-02-06` | Inspect sibling patterns, extract candidates, and return any dependency edge for human acceptance; invent no edge in SCOPE_CHANGE |
| Estimate, schedule, budget, usage, cost, forecast services | Optional resource-governance owner | `NO_CURRENT_ARTIFACT_IDENTIFIED` | No rerun unless the owner has activated that optional service; if activated later, consume the successor graph |
| App and PEC decomposition/scope | Their owning loops | `NO_CHANGE` | Root SCA grants no client scope; OD-5 remains a separate App gate |
| App/PEC coordination notices | Root/receiving-loop coordination | `ROUTE_AFTER_ACCEPTANCE` | Notify the accepted Root carrier and basis; notices coordinate and do not amend receiving-loop scope |
| Public export | Export owner | `NO_DECOMPOSITION_CONTENT_CHANGE` | Root `execution/` is not exported; no export-profile change expected |

The current G2 ownership register already assigns
`execution/PKG-02_.../**` to PKG-02, but it does not declare `runtime/**`.
The current G3 graph likewise limits PKG-02 to its execution subtree and is
pinned to the prior initialization basis. Those are the principal downstream
state changes created by this topology decision.

## Dependency, estimate, and schedule impact

No central `Dependencies.csv`, accepted estimate snapshot, schedule, budget,
cost, usage, or forecast surface was identified for the Root execution
instance. Deliverable-local `_DEPENDENCIES.md` files exist, and the accepted
package-level G3 graph currently declares no dependency or serialization
edges.

Gate 2 does not invent an edge. At downstream Project Setup:

- the new deliverable requires a local dependency surface;
- likely relationships to boundary, capability-control, export, evidence, and
  release deliverables are candidates for extraction and human disposition,
  not accepted dependencies;
- the six package nodes remain flat unless accepted evidence requires a graph
  amendment; and
- no optional resource-governance service is made mandatory by this SCA.

## Orphan and structural-closure risk

| Check | Expected post-change state | Risk disposition |
|---|---|---|
| Package parentage | 46/46 deliverables have exactly one package | New DEL-02-06 binds to existing PKG-02 |
| IN scope assignment | 95/95 have one package and at least one deliverable | New SOW-104 binds only to PKG-02/DEL-02-06 |
| Existing lineage | All 103 existing scope rows and 45 existing deliverables retain IDs and parents | No rename, retirement, reclassification, merge, or split |
| Objective support | All seven objectives remain supported | OBJ-001/2/4/7 gain the new carrier |
| Forward trace | 85/85 PRD items covered or recorded deferred | Add O-11 as COVERED |
| Reverse trace | 52/52 package/deliverable units traced | Add DEL-02-06; reconcile PKG-02 |
| Context QA | 46/46 deliverables represented | Gate 3 must choose and justify M or L |
| Child closure | Not applicable | No parent is removed or moved |

The main structural failure mode is partial parity across seven authoritative
decomposition surfaces. Gate 3 must preview them together; Gate 5 must
validate them together.

## Invariant and semantic risks

1. **Carrier is not authority.** A decomposed runtime carrier and `runtime/`
   locus do not authorize a change, grant project authority, or replace the
   human gate.
2. **Root-owner/client boundary.** App, PEC, and future clients consume generic
   runtime contracts; their implementation does not transfer Root ownership.
3. **Boundary conformance remains distinct.** DEL-02-02 must not absorb
   stewardship or lose its existing O-2/O-10 boundary role.
4. **One carrier must remain bounded.** DEL-02-06 may carry one proportionate
   runtime-change tranche at a time; it cannot become an unbounded backlog for
   every runtime concern.
5. **Ruled seams are transcribed, not repartitioned.** Exact changes must cite
   O-11 and D-GOV-20. Uncovered credential, session, adapter, and fallback
   seams remain PROPOSED/open rather than being decided in decomposition prose.
6. **Operational state is not project truth.** Runtime user-data, engines, and
   sessions remain operational; checkout-contained decisions, manifests,
   evidence, and Git remain governed state.
7. **File-native fallback and human release remain load-bearing.** No runtime
   dependency may make governance unrecoverable without the daemon, and release
   disposition remains an accountable-human act.
8. **Guard state must precede dispatch.** The refreshed G2 ownership and G3
   work graph must pass before any Root work is dispatched against `runtime/**`.
9. **No fabricated basis repair.** Existing SOW pins are reviewed and refreshed
   only where successor content is verified; they are not mechanically
   rewritten.

## Audit and validation impact

- The Gate 1 `AUDIT_DECOMP` result is `OK` / `PASS`: 6/6 packages, 45/45
  deliverables, 45/45 contexts, 0 BLOCKER, 0 WARNING.
- All seven decomposition-package hashes remained unchanged through D-GOV-28
  adoption and EffectiveSHA backfill.
- Gate 5 must produce a new post-change audit and deterministic register
  comparison.
- Before downstream scaffold, `AUDIT_DECOMP` is expected to report DEL-02-06
  missing from the execution tree. That is a real derivative-state gap, not a
  decomposition-truth failure; closure must report it honestly and hand it to
  PROJECT_SETUP.
- Required deterministic assertions include 104 scope rows, 46 deliverables,
  6 packages, 7 objectives, zero duplicate IDs, zero unresolved references,
  bidirectional mapping parity, O-11 forward coverage, DEL-02-06 reverse
  trace, and exact OBJ-001/2/4/7 aggregate parity.
- A post-PROJECT_SETUP audit must reach 46/46 filesystem coverage before the
  new deliverable is activated.

## Handoff impact

Until Gates 2–5 close:

- decomposition revision 1.0 remains authoritative truth;
- Root PRD Revision 6 and O-11 are authoritative upstream scope;
- the controlled PRD/decomposition drift is explicit;
- runtime-stewardship work remains undispatchable through the Root package
  graph; and
- `ReadyForNextPhase=NO`.

After an approved Gate 5 amendment, the intended first handoff is to
PROJECT_SETUP for DEL-02-06 preparation and G2/G3 state refresh. Only after
those surfaces pass may WORKING_ITEMS author/activate the new SOW or execute
bounded runtime work. App SCOPE_CHANGE remains a separate owner gate.

## Gate 2 confirmation question

**Do you accept this impact assessment, including the recommendation to add
one new PKG-02 deliverable rather than expanding DEL-02-02?**
