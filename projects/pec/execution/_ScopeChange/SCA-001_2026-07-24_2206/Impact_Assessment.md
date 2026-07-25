---
amendment_id: SCA-001
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-07-24
status: awaiting_gate_2_confirmation
accepted_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md revision 1.0
authority: D-PEC-61
---

# SCA-001 Gate 2 — Impact Assessment

## Assessment summary

SCA-001 is a bounded clarification of PEC's construction and validation
direction. It changes descriptions, mappings, constraint/source-basis text,
and one Context Envelope. It does not add, retire, reclassify, merge, split,
or renumber any product-topology member.

| Impact dimension | Gate 2 conclusion |
|---|---|
| Topology | No change: 94 scope items, 64 deliverables, 11 packages, 6 objectives |
| Stable IDs | No change or reuse |
| Package lineage | No change; `SOW-064 → PKG-10 → DEL-10-10` remains |
| Product functions | No addition or removal |
| Dependency graph | Not written here; complete DAG remains downstream `PROJECT_SETUP` work |
| Filesystem scaffolding | None exists and none is authorized |
| Current estimates/schedules | None exist; no current surface becomes stale |
| Authority | PRD v2.1 and `D-PEC-61` are already-adopted upstream authority; SCA-001 reconciles the decomposition to them |
| Downstream hold | `PROJECT_SETUP` remains held until Gate 5 validation and owner confirmation |

## Impact by action

| Action | Decomposition structure | Companion-register impact | Downstream consequence | Principal risk |
|---|---|---|---|---|
| A001 — C16 | Adds one row to the existing Hard Constraints section and reconciles constraint references, source basis, decision log, and revision history | None directly | `PROJECT_SETUP` must interpret C16 as an ordering and learning constraint when it later materializes `FULL_GRAPH` | Wording could accidentally elevate self-bootstrap into PEC's singular product purpose; Gate 3 must scope it to PEC's own construction |
| A002 — SOW-064 | Expands the existing SSOW statement and adds `OBJ-006` support | `ScopeLedger.csv` row `SOW-064` statement, source, objective, decision/note fields | Later work briefs can cite observed bootstrap progression as validation evidence; no new deliverable is created | A coordination observation must remain evidence for a candidate/human gate, never an automatic scope mutation |
| A003 — DEL-10-10 | Renames and strengthens the existing deliverable control row; envelope changes `S → M`; P1 remains the introduction point | `Deliverables.csv` row `DEL-10-10`; `ContextBudgetQA.csv` matching row; objective support parity with `ScopeLedger.csv` | `PROJECT_SETUP` later scaffolds the same deliverable ID with the strengthened accepted basis | “Standing thereafter” must be expressed without inventing a new phase, deliverable, or lifecycle state |
| A004 — summaries/traceability | Reconciles OBJ-006, source-corpus references, coverage/telemetry summary, decision log, revision history, and accepted handoff pointer | No new register; parity updates only to already-affected registers | All downstream work consumes revision 1.1 after closure | Partial edits could leave PRD version, objective support, envelope telemetry, or revision labels inconsistent |

## Expected telemetry deltas

These are impact predictions, not Gate 3 amendment text:

| Metric | Before | Expected after approved amendment |
|---|---:|---:|
| Scope items | 94 | 94 |
| `IN / OUT / TBD` | 71 / 14 / 9 | 71 / 14 / 9 |
| Packages | 11 | 11 |
| Deliverables | 64 | 64 |
| Objectives | 6 | 6 |
| Context Envelopes `S / M / L / XL` | 29 / 33 / 2 / 0 | 28 / 34 / 2 / 0 |
| OBJ-006 mapped scope items | 8 | 9 |
| OBJ-006 mapped deliverables | 8 | 9 |
| IN items without objective mapping | 32 | 31 |
| Unassigned IN items | 0 | 0 |
| IN items without a deliverable | 0 | 0 |

The exact Coverage & Telemetry revision-label replacement is deferred to the
Gate 3 before/after preview. Gate 2 records only that the current front matter
and `_LATEST.md` say revision 1.0 while the telemetry table retains its Phase
6 label “Revision 0.9.”

## Surface classification

`Classification` describes the eventual approved Gate 5 disposition. No
surface in this table is changed by Gate 2 except the SCA-owned snapshot and
its pointer.

| Surface | Package role | Classification | Gate 2 authority and impact |
|---|---|---|---|
| `projects/pec/docs/PRD.md` | Upstream governing product definition | `NO_CHANGE` | Already advanced to v2.1 by `D-PEC-61`; SCOPE_CHANGE consumes it and does not rewrite it |
| `execution/_Coordination/_DECISIONS/D-PEC-61_directed_full_dag_self_bootstrap.md` | Upstream owner decision / authority record | `NO_CHANGE` | Opens SCA-001 and supplies the exact fence |
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | `working surface` | `DIRECT_EDIT` | Eventual revision 1.1 amendment surface for A001–A004 |
| `execution/_Decomposition/ScopeLedger.csv` | `authoritative companion register` | `DIRECT_EDIT` | Eventual `SOW-064` statement/source/objective traceability update |
| `execution/_Decomposition/Deliverables.csv` | `authoritative companion register` | `DIRECT_EDIT` | Eventual `DEL-10-10` name/description/artifact/objective/envelope update |
| `execution/_Decomposition/ContextBudgetQA.csv` | `authoritative companion register` | `DIRECT_EDIT` | Eventual `DEL-10-10` envelope/risk/action QA parity update |
| `execution/_Decomposition/_LATEST.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Eventual revision 1.1 accepted-basis and handoff-state pointer |
| `execution/_Decomposition/Companion_Inventory.csv` | `authoritative companion register` | `NO_CHANGE` | File membership and package roles do not change; only an exact Gate 3 parity finding may reopen this classification |
| `execution/_ScopeChange/SCA-001_2026-07-24_2206/**` | `snapshot / handoff artifact` | `DIRECT_EDIT` | SCA-owned progressive gate evidence; final artifact set is completed only at Gate 5 |
| `execution/_ScopeChange/_LATEST.md` | `snapshot / handoff artifact` | `DIRECT_EDIT` | Pointer/state advances only as each owner-confirmed gate opens |
| `execution/_Evaluation/DecompCoverage/COV_SCA001_PRECHANGE_2026-07-24_2209/**` | `derived publication artifact` | `NO_CHANGE` | Immutable pre-change audit evidence; expected `FAILED_INPUTS` remains historically correct |
| Future Gate 5 post-change audit snapshot | `derived publication artifact` | `RECOMPUTE` | New audit attempt required after amendment; pre-scaffold limitation is expected to persist |
| Deterministic `Post_Change_Coverage.json` | `snapshot / handoff artifact` | `RECOMPUTE` | Must compare topology, mappings, objective support, envelopes, and hashes against the Gate 1 baseline |
| `execution/Dependencies.csv` | Downstream Project Setup truth; currently absent | `NO_CHANGE` | Creation is prohibited in SCA-001 and remains `PROJECT_SETUP` work |
| `execution/PKG-*/1_Working/DEL-*` | Downstream scaffold; currently absent | `NO_CHANGE` | Creation belongs to `PROJECT_SETUP`/`PREPARATION` after SCA closure |
| Estimates and schedules | Downstream derivative state; currently absent | `NO_CHANGE` | No present artifact is stale; future generation must consume revision 1.1 |
| Implementation and frozen reference corpus | Product/output and cite-only historical surfaces | `NO_CHANGE` | Outside the exact D-PEC-61 fence |
| PEC `AGENTS.md`, README, `docs/STATUS.md`, decision register, and loop receipts | Live project/governance pointers | `NO_CHANGE` | Already updated in the D-PEC-61 owner-governance tranche; SCOPE_CHANGE has no Gate 2 write here |

## Derivative-package and downstream status

| Package or consumer | Owner | State during Gate 2 | Required action |
|---|---|---|---|
| Pre-change decomposition audit | `AUDIT_DECOMP` | `CURRENT_AS_HISTORICAL_EVIDENCE`; `FAILED_INPUTS` by pre-scaffold contract | Preserve immutable result; do not treat it as filesystem coverage |
| Post-change decomposition audit | `AUDIT_DECOMP` | `NOT_RUN` | Dispatch at Gate 5; preserve the same limitation if no folders exist |
| Register-integrity comparison | `SCOPE_CHANGE` | Pre-change baseline complete | Produce deterministic post-change comparison at Gate 5 |
| Project Setup full DAG | `PROJECT_SETUP` | `FROZEN` / held by `D-PEC-61` | Resume only from accepted revision 1.1; materialize full dependency graph and blocker computation |
| Package/deliverable scaffolding | `PROJECT_SETUP` → `PREPARATION` | `NOT_CREATED` | Create only after SCA closure under Project Setup's own gates and packet |
| Dependency register / work graph | `PROJECT_SETUP` and its bounded dependency workflow | `NOT_CREATED` | Materialize from the complete accepted graph; SCOPE_CHANGE must not create it |
| Estimate/schedule snapshots | `PROJECT_SETUP` scheduling workflow | `NOT_CREATED` | Generate from the successor graph if the owner later selects them |
| PEC implementation tranches | `WORKING_ITEMS` | `NOT_STARTED` | Consume only accepted/scaffolded successor state under separate owner packets |
| Git closeout | `CHANGE` | `NOT_OPENED` | Stage only validated SCA-001 tranche after Gate 5 owner confirmation |

No existing downstream derivative package becomes misleadingly “current”:
none has yet been created. The pre-change audit and baseline remain immutable
evidence about revision 1.0 rather than being overwritten or presented as
revision 1.1 evidence.

## Orphan and structural-closure risk

| Check | Expected post-change state | Risk disposition |
|---|---|---|
| Package parentage | 64/64 deliverables retain exactly one package | No topology action; verify deterministically at Gate 5 |
| IN scope assignment | 71/71 retain one package and one deliverable | No assignment change; verify deterministically |
| Target lineage | `SOW-064 → PKG-10 → DEL-10-10` | Preserved |
| Objective support | All six objectives remain supported | OBJ-006 gains one scope item and one deliverable |
| Stable IDs | All IDs preserved; no ID reused | `ALLOW_RENUMBERING=false` |
| Context QA | 64/64 deliverables retain one QA row | `DEL-10-10` must change to `M` on both authoritative surfaces |
| Child closure | Not applicable | No parent or child entity is removed, moved, merged, or split |

Predicted orphan counts remain zero. The principal structural failure mode is
not orphan creation but **partial parity**: changing only one of the document,
ledger, deliverable register, QA register, objective summary, or telemetry
surfaces. Gate 3 must preview them together and Gate 5 must validate them
together.

## Invariant and semantic risks

1. **Plural product intent must remain intact.** C16 and the strengthened
   self-ingest deliverable govern PEC's own construction path. They must not
   imply that `FULL_GRAPH`, self-bootstrap, or concurrent Agent 0 operation
   is the privileged PEC usage mode.
2. **Reflexive but acyclic bootstrap.** A node may consume only a capability
   accepted from a predecessor and cannot depend on the capability it
   produces. Project Setup must encode this in the later full graph; SCA-001
   records the constraint but does not invent edges.
3. **Files remain sufficient.** Progressive use of PEC may never make PEC a
   prerequisite for recovery or governance. C1/C2 and the file-native
   fallback remain binding.
4. **Discovery does not grant authority.** Observed friction may create
   evidence-linked candidates, boundary questions, or SCOPE_CHANGE requests;
   it cannot adopt a function, alter accepted scope, or rule a boundary.
5. **Phase metadata remains metadata.** P1 remains the introduction point for
   `DEL-10-10`; “standing thereafter” must not create a new package, phase,
   deliverable, or lifecycle state.
6. **Source and objective parity.** PRD v2.1 §12 and `D-PEC-61` must appear
   consistently in the successor source basis, and `SOW-064`/`DEL-10-10`
   must appear consistently in OBJ-006 mappings.
7. **Context-budget parity.** The `S → M` change affects both
   `Deliverables.csv` and `ContextBudgetQA.csv`, plus the aggregate envelope
   telemetry.

## Estimate and schedule staleness

There is no current `Dependencies.csv`, work graph, estimate snapshot,
schedule basis, package scaffold, or activated deliverable state. Therefore
SCA-001 creates no present estimate/schedule staleness and requires no
dependency-closure analysis at Gate 2.

The prospective risk is controlled by the existing hold: any Project Setup
graph, blocker computation, estimate, or schedule derived from decomposition
revision 1.0 would be invalid. `PROJECT_SETUP` must begin from the accepted
SCA-001 successor and then run its normal full-graph, maturity-threshold,
dependency-storage, estimate, and schedule gates.

## Audit and validation impact

- The pre-change `AUDIT_DECOMP` result is `FAILED_INPUTS` because no
  deliverable folders exist. It cannot establish filesystem coverage.
- The deterministic Gate 1 baseline establishes register integrity and target
  before-values.
- OI-013 remains open: there is no durable repository-native register
  validator. Gate 5 must run an equivalent deterministic post-change check,
  compare it to `Pre_Change_Coverage.json`, and record this tooling gap.
- Expected Gate 5 assertions include unchanged topology counts, zero dangling
  references, preserved lineage, OBJ-006 support 9/9 at scope/deliverable
  level, envelope counts 28/34/2/0, companion inventory existence, and exact
  successor hashes.
- A post-change `AUDIT_DECOMP` should be dispatched as required, but an
  unchanged pre-scaffold `FAILED_INPUTS` remains a warning rather than
  filesystem-coverage evidence.

## Handoff impact

Until all later SCOPE_CHANGE gates close:

- decomposition revision 1.0 remains the accepted decomposition truth;
- PRD v2.1 is the upstream product authority;
- the resulting controlled drift is explicit;
- `PROJECT_SETUP` remains held;
- `ReadyForNextPhase=NO`.

After an approved Gate 5 amendment and owner confirmation, the intended
handoff is to `PROJECT_SETUP` with revision 1.1, `FULL_GRAPH` already selected,
and dependency materialization still pending. Project Setup retains its normal
Phase 1.3 owner decisions for dependency maturity threshold and register
storage. `CHANGE` owns any subsequent Git staging/commit closeout.

## Gate 2 confirmation question

**Do you accept this impact assessment?**
