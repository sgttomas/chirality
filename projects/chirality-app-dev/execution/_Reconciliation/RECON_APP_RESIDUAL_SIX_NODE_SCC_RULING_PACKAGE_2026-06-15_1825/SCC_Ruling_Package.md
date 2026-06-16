# Residual Six-Node SCC Ruling Package

## Package Status

This is a RECONCILIATION ruling package for human decision support. It records a determination from current dependency evidence and identifies the human rulings needed before executable R5 can proceed.

It does not itself approve:

- SDK `Agent` exposure;
- executable SDK `agents` definitions;
- child turn execution;
- child output artifacts;
- child capability inheritance;
- Pi runtime paths;
- concrete provider implementation;
- provider routing;
- network expansion;
- release-readiness claims;
- lifecycle issuance, professional approval, certification, sealing, authentication, or code-compliance acceptance;
- professional-boundary claim changes.

## Evidence Basis

Primary evidence: `execution/_Reconciliation/DepClosure/CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820`.

The latest dependency-closure audit confirms the residual SCC persisted unchanged from the prior closeout snapshot:

| Evidence item | Current value |
|---|---|
| Strict SCC count | `1` |
| Strict SCC size | `6` |
| Active deliverable execution edges | `101` |
| Bidirectional pair count | `0` |
| Schema-invalid registers | `0` |
| ID normalizations | `0` |

## SCC Membership

| Node | Deliverable surface |
|---|---|
| `DEL-03-01` | AgentEnginePort and Engine Conformance Suite |
| `DEL-03-02` | Thin TurnEngine and Session Locking |
| `DEL-03-03` | Harness API and SSE Compatibility Adapter |
| `DEL-03-04` | Interrupt, Cancel, and Terminal Outcome Handling |
| `DEL-04-03` | SdkMessageMapper and Provider-Neutral Translation |
| `DEL-05-02` | HarnessEvent Schema and Append-Only JSONL |

## Cycle-Participating Edges

The audit found 15 internal active deliverable execution rows in the residual SCC. Full row-level treatment is in `SCC_Edge_Workbook.csv`.

| Dependency ID | Graph edge | Row character |
|---|---|---|
| `DEP-03-01-005` | `DEL-03-01 -> DEL-03-03` | Conformance fixture / interface evidence |
| `DEP-03-02-006` | `DEL-03-02 -> DEL-03-01` | Engine boundary interface |
| `DEP-03-02-007` | `DEL-03-02 -> DEL-05-02` | Runtime event persistence interface |
| `DEP-03-02-008` | `DEL-03-03 -> DEL-03-02` | SSE compatibility / lifecycle handoff |
| `DEP-03-02-009` | `DEL-03-04 -> DEL-03-02` | Lock cleanup / cancellation boundary |
| `DEP-03-03-006` | `DEL-03-03 -> DEL-03-02` | TurnEngine lifecycle delegation |
| `DEP-03-03-007` | `DEL-03-03 -> DEL-03-04` | Interrupt/cancel ownership boundary |
| `DEP-03-04-006` | `DEL-03-04 -> DEL-03-01` | Runtime boundary prerequisite |
| `DEP-03-04-007` | `DEL-03-04 -> DEL-03-02` | Active-turn locking prerequisite |
| `DEP-03-04-009` | `DEL-03-04 -> DEL-05-02` | HarnessEvent writer prerequisite |
| `DEP-04-03-008` | `DEL-04-03 -> DEL-03-01` | Engine contract ownership boundary |
| `DEP-04-03-009` | `DEL-04-03 -> DEL-03-03` | Browser event-name compatibility |
| `DEP-04-03-010` | `DEL-05-02 -> DEL-04-03` | Mapper-to-event-log handoff |
| `DEP-05-02-011` | `DEL-05-02 -> DEL-03-03` | HarnessEvent / UIEvent separation |
| `DEP-05-02-012` | `DEL-05-02 -> DEL-04-03` | SDK-message mapper interface |

## Blocker Implications

### Project-wide closure

The SCC is blocking for project-wide strict dependency-closure claims. The current graph is not acyclic, and the cycle-driven resolution doctrine says cycle-participating edges must remain non-gating until resolved by a recorded move.

### Executable R5 implementation

The SCC is not enough, by itself, to prove that every bounded executable R5 implementation is technically impossible. The cycle is dominated by interface, ownership-boundary, conformance-fixture, handoff, and prerequisite maturity rows spanning runtime lifecycle, compatibility, mapper, and event-log surfaces.

However, executable R5 remains blocked in governance terms until the human accepts a posture ruling. D-APP-06 held executable R5 and denied executable child runtime surfaces. This package cannot convert a dependency interpretation into implementation authority.

### Decomposition or dependency amendment

The SCC is evidence that the current dependency register mixes at least three concerns in one strict graph:

- implementation prerequisites that can block a tranche until a surface is available;
- interface or ownership-boundary references that should often be preserved without being dispatch-gating;
- handoff and conformance evidence that can be validated after both sides exist.

If the project requires strict acyclicity before any executable R5 work, decomposition or dependency amendment is required before R5 can proceed.

## Possible Resolution Moves

| Move | Meaning for this SCC | Human gate |
|---|---|---|
| Decompose | Split interface/reference/handoff rows from hard prerequisite rows, or introduce maturity gates that distinguish contract availability from final closure. | Required before CHANGE edits rows. |
| Invert | Reverse rows where current `Direction` semantics are recording evidence flow rather than execution precedence. | Required before CHANGE edits rows. |
| Cut | Retire rows judged non-gating interface, conformance, or handoff evidence. | Human-gated by doctrine. |
| Merge | Treat a mutually dependent cluster as one merged work unit. | Human-gated by doctrine. |

Recommended non-executed path: classify the SCC as blocking project-wide closure claims now, then ask the human to choose whether bounded executable R5 may proceed with these cycle-participating rows held non-gating or whether dependency/decomposition amendment must land first.

## Required Human Rulings

See `Human_Ruling_Workbook.csv`.

Minimum required ruling: choose whether this SCC blocks executable R5, blocks only project-wide dependency closure claims, or requires decomposition/dependency amendment before R5 can proceed.

## Downstream Handoffs

| Recipient | Handoff |
|---|---|
| Human project authority | Rule the `HR-001` classification choice and any dependency amendment authority. |
| `WORKING_ITEMS` | Continue to hold executable R5 selection unless the human accepts a non-blocking-for-R5 interpretation or closure is achieved. |
| `CHANGE` | Apply no row edits unless a later ruling approves a concrete move set. |
| `AUDIT_DEP_CLOSURE` | Rerun closure after any approved row amendments. |
| `RECONCILIATION` | If amendment is chosen, prepare a row-level resolution package that names exact decompose, invert, cut, or merge moves. |
