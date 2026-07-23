# SCA-APP-003 Handoff State

**Package role:** immutable governance-propagation snapshot / implementation handoff
**Status:** `IMPLEMENTATION_VALIDATED_PR_MERGE_PENDING`
**Accepted snapshot:** `execution/_ScopeChange/SCA-APP-003_2026-07-22_Shared_Runtime_Local_Agent_Pilot/`
**Closure verdict:** `BOUNDED_PILOT_COMPLETE_MERGE_PENDING`

The closure verdict covers the bounded shared-runtime implementation, automated
validation, packaging proofs, public-export boundary, and opt-in local-model
pilot. It does not authorize release, publication, professional reliance, PEC
production use, or lifecycle advancement. Pull-request review and merge remain
open.

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
| `DerivativePackageState` | COMPLETE_FOR_BOUNDED_PILOT | Runtime, Desktop, CLI, PEC, packaging, pilot, and export derivatives are present and validated; release derivatives are outside this ruling. |
| `ContentRemediationState` | NOT_REQUIRED | This is a SOFTWARE scope change; no KTY remediation applies. |
| `DownstreamRerunState` | PASS | Runtime, packaging, pilot, security, regression, authority, and export checks passed on the implementation branch. |
| `MetadataAlignmentState` | NOT_REQUIRED | No DOMAIN KTY metadata transition is involved; implementation evidence is tracked as downstream work rather than KTY metadata alignment. |
| `AuditState` | ACCEPTED | G0A accepted governance reconciliation and G4 independently accepted the final runtime reliability controls. |
| `ReadyForNextPhase` | PR_REVIEW | The bounded pilot may proceed to PR review; this does not authorize publication, release, production PEC use, or lifecycle advancement. |

## Derivative-package currency

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| App authority corpus and 51 deliverable `_REFERENCES.md` files | D-APP-38 reconciliation workflow | CURRENT at v14 | `AUTHORITY_CORPUS.json`; status/audit reports | Reconcile again if a registered authority source changes during implementation. |
| SCA-APP-003 coverage, supersession, impact, and action records | G0 integration owner | CURRENT for Gate 4 | This accepted snapshot; 11-row cumulative map with zero findings | Preserve as the immutable governance input to G1-G5. |
| Affected app deliverable `_STATUS.md` records | Existing package managers | CURRENT for governance | `Execution_Deliverable_Impact.csv`; dated Remaining entries | Add only dated, validated implementation evidence; do not advance lifecycle state. |
| Root/app/domain/PEC narrative and decision surfaces | Root integration owner and project managers | CURRENT for accepted governance scope | Registered rulings and `Amendment_Actions.csv` | Re-audit after implementation fan-in for accidental authority drift. |
| Runtime, Desktop, CLI, PEC pilot, package, security, and regression evidence | G1-G5 owners | CURRENT_FOR_BOUNDED_PILOT | Coordination returns, runtime AgentRuns, automated suites, packaged proofs, and redacted live proof | Re-run if implementation changes during PR review. |
| Public exporter allowlist, generated manifest, and export report | G3/G5 integration owner | CURRENT | Generic runtime is exported; private PEC/Piping adapters, credentials, machine state, and project evidence remain excluded. | Re-run if the public boundary changes. |

## Active implementation surfaces

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| App authority corpus and governed `_REFERENCES.md` | RECOMPUTE | CURRENT at v14 | Corpus status/audit pass with all eight sources matched. |
| App decomposition and affected `_STATUS.md` records | DIRECT_EDIT | CURRENT_FOR_GOVERNANCE | DEC-019, OI-007, and the impact register preserve topology/lifecycle state. |
| Root/app/domain/PEC decision and narrative surfaces | DIRECT_EDIT | CURRENT_FOR_GOVERNANCE | D-GOV-20, D-APP-73, D-T0-23, D-PEC-56, and registered propagation edits. |
| `runtime/` and Desktop/PEC implementation | DIRECT_EDIT | IMPLEMENTED_AND_VALIDATED | Root runtime, daemon clients, Desktop settings/proxies, and PEC adapter/client seam. |
| Public exporter allowlist and generated outputs | RECOMPUTE | CURRENT | Exporter includes generic `runtime/`; boundary scan excludes private projects and runtime state. |

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

- Pull-request review and merge remain open; source changes during review
  require proportional reruns.
- D-PEC-49 remains awaiting ruling; PEC production data and mutation are out of
  scope.
- T0 product-authority rebaseline remains open.
- Piping, automatic scheduling, local Agent 1, forced or automatic switching,
  and multiple primary local models remain future milestones.

## Next owning workflows

- G0/G0A governance reconciliation is complete.
- G1 runtime, G2 PEC migration, and G3 integration fan-in are complete.
- G4 independent security/regression review accepted the final remediation.
- G5 validation and scoped implementation closeout are complete; branch push,
  pull-request review, and merge remain.
