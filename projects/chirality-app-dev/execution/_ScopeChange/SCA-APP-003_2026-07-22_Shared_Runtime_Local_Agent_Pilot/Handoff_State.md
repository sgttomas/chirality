# SCA-APP-003 Handoff State

**Package role:** immutable governance-propagation snapshot / implementation handoff
**Status:** `GOVERNANCE_PROPAGATION_CLOSED_IMPLEMENTATION_OPEN`
**Accepted snapshot:** `execution/_ScopeChange/SCA-APP-003_2026-07-22_Shared_Runtime_Local_Agent_Pilot/`
**Closure verdict:** `OPEN_PENDING_DERIVATIVE_CLOSURE`

The closure verdict applies only to Gate 4 governance propagation. Gate 5
implementation, validation, packaging, pilots, and export remain open and
cannot be inferred from this handoff.

## Accepted upstream snapshots

| Upstream truth | Accepted snapshot | Status |
|---|---|---|
| Owner authority | Owner instruction dated 2026-07-22 to implement the shared-runtime and local-agent pilot | ACCEPTED |
| Root governance | D-GOV-20 and its registered root downstream amendments | ACCEPTED |
| App governance | D-APP-73, DEC-019, OI-007, and authority corpus v14 | ACCEPTED |
| Tier-0 domain governance | D-T0-23 and its registered profile/bridge amendments | ACCEPTED |
| PEC governance | D-PEC-56, with D-PEC-49 still open and production claims prohibited | ACCEPTED_WITH_OPEN_GATE |

## Fixed state fields

| Field | Value | Evidence |
|---|---|---|
| `DecompositionTruthState` | COMPLETE | DEC-019 and OI-007 carry the amendment without topology change. |
| `DerivativePackageState` | INCOMPLETE | Governance-local derivatives are in parity, but the accepted amendment explicitly requires later runtime, pilot, packaging, and export derivatives before SCOPE_CHANGE closure. |
| `ContentRemediationState` | NOT_REQUIRED | This is a SOFTWARE scope change; no KTY remediation applies. |
| `DownstreamRerunState` | FROZEN | Runtime, packaging, pilot, security, regression, and export checks have not run for this amendment. |
| `MetadataAlignmentState` | NOT_REQUIRED | No DOMAIN KTY metadata transition is involved; implementation evidence is tracked as downstream work rather than KTY metadata alignment. |
| `AuditState` | NON_BLOCKING_PASS | The independent G0A re-audit accepted the remediated packet; corpus v14 and the cumulative supersession map pass deterministically. |
| `ReadyForNextPhase` | REGEN_ONLY | G1-G3 implementation and derivative generation may proceed; this does not authorize Phase 7, publication, release, or lifecycle advancement. |

## Derivative-package currency

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| App authority corpus and 51 deliverable `_REFERENCES.md` files | D-APP-38 reconciliation workflow | CURRENT at v14 | `AUTHORITY_CORPUS.json`; status/audit reports | Reconcile again if a registered authority source changes during implementation. |
| SCA-APP-003 coverage, supersession, impact, and action records | G0 integration owner | CURRENT for Gate 4 | This accepted snapshot; 11-row cumulative map with zero findings | Preserve as the immutable governance input to G1-G5. |
| Affected app deliverable `_STATUS.md` records | Existing package managers | CURRENT for governance | `Execution_Deliverable_Impact.csv`; dated Remaining entries | Add only dated, validated implementation evidence; do not advance lifecycle state. |
| Root/app/domain/PEC narrative and decision surfaces | Root integration owner and project managers | CURRENT for accepted governance scope | Registered rulings and `Amendment_Actions.csv` | Re-audit after implementation fan-in for accidental authority drift. |
| Runtime, Desktop, CLI, PEC pilot, package, security, and regression evidence | G1-G5 owners | DEFERRED | Gate 5 remains `PENDING` | Generate and validate in G1-G5. |
| Public exporter allowlist, generated manifest, and export report | G3/G5 integration owner | DEFERRED | D-GOV-20 and exporter README boundary | Change only after the generic runtime exists and both pilots pass. |

## Active implementation surfaces

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| App authority corpus and governed `_REFERENCES.md` | RECOMPUTE | CURRENT at v14 | Corpus status/audit pass with all eight sources matched. |
| App decomposition and affected `_STATUS.md` records | DIRECT_EDIT | CURRENT_FOR_GOVERNANCE | DEC-019, OI-007, and the impact register preserve topology/lifecycle state. |
| Root/app/domain/PEC decision and narrative surfaces | DIRECT_EDIT | CURRENT_FOR_GOVERNANCE | D-GOV-20, D-APP-73, D-T0-23, D-PEC-56, and registered propagation edits. |
| `runtime/` and Desktop/PEC implementation | NO_CHANGE | DEFERRED_TO_G1_G3 | G0 made no code or dependency changes; `RUN_SUMMARY.md` records the boundary. |
| Public exporter allowlist and generated outputs | NO_CHANGE | DEFERRED_TO_G3_G5 | G0 left the exporter unchanged so it remains operational before `runtime/` exists. |

## KTY remediation and metadata alignment

KTY content remediation is `NOT_REQUIRED`: this is a SOFTWARE amendment and no
KTY-local content, factual-use gate, or remediation manifest is involved.
KTY metadata alignment is likewise `NOT_REQUIRED`.

## Active snapshot state

| Snapshot | Artifact completeness | `_LATEST.md` parity |
|---|---|---|
| `SCA-APP-003_2026-07-22_Shared_Runtime_Local_Agent_Pilot/` | COMPLETE for the SOFTWARE Gate 4 governance handoff | MATCH |

## Rerun requirements

- Run the full D-APP-72 baseline after each behavior-preserving extraction
  stage and before Desktop cutover.
- Run daemon/client/CLI conformance, socket/auth/project isolation, session
  migration, residency, Agent 1 delegation, PEC scratch/demo/RBAC, export
  boundary, build, packaging, secret, and network-policy checks during G1-G5.
- Re-run authority-corpus status/audit, supersession accumulation, and an
  independent final authority/regression review before closeout.
- Perform live oMLX switching only as the opt-in, non-destructive proof defined
  by D-APP-73; never infer a production or performance claim from it.

## Remaining blockers and exclusions

- G1-G5 implementation and all behavioral validation remain open.
- D-PEC-49 remains awaiting ruling; PEC production data and mutation are out of
  scope.
- T0 product-authority rebaseline remains open.
- Piping, automatic scheduling, local Agent 1, forced or automatic switching,
  and multiple primary local models remain future milestones.
- Exporter allowlist and generated export artifacts remain unchanged until the
  generic runtime exists and the prescribed pilots pass.

## Next owning workflows

- G0A accepted this remediated governance packet without writes.
- G1 owns bounded `runtime/` implementation and G2 owns bounded PEC adapter
  migration; the integration owner serializes shared contracts, lockfiles,
  Desktop cutover, and fan-in.
- G4 performs independent security/regression review; G5 owns final validation,
  scoped closeout, branch push, and pull request.
