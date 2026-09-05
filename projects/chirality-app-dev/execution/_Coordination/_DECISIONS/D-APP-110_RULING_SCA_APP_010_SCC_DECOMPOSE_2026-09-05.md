# D-APP-110 — Decompose the SCCs recorded under D-APP-109

Status: RULED (owner direction in chat 2026-09-05)

Owner: Ryan Tufts

Date: 2026-09-05

## Conversation provenance

After the D-APP-109 emission (PR #714, second commit `7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985`),
HELP_HUMAN reported that the live dependency graph carries one twenty-node
SCC and one two-node SCC (DEL-06-03 / DEL-08-01), recorded and unresolved,
and that the likely resolution move is decompose because the new edges are
already acyclic at item level through the seated `Depends` lines. The owner
directed, verbatim:

> Decompose the SCC, record it as part of PR #714.

These quotations are from the current conversation supplied to this run.

## Ruling as applied (HELP_HUMAN's reading; the owner may amend by reply)

1. **Move:** `decompose`, the agent-proposable move under
   `docs/CYCLE_DRIVEN_RESOLUTION.md` §2.3, applied to both SCCs in the form
   this loop established in `SCC-SAFE-MOVES-001`
   (`execution/_Reconciliation/DepClosure/CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z/`):
   a coarse deliverable-to-deliverable edge that records consumption of a
   documented contract is re-targeted to that contract as a `DOCUMENT` node
   (`TargetType=DOCUMENT`, `TargetRefID` naming the contract,
   `TargetLocation` at the owning carrier's Scope of Work anchor), the row
   stays `ACTIVE` with its evidence and its deliverable relation preserved in
   `Notes`, and the strict deliverable graph becomes acyclic. No row is
   retired, cut, merged, inverted, or marked out-of-objective; no
   decomposition topology changes.
2. **Selection rule and result:** only rows of type `INTERFACE`, `HANDOVER`,
   `CONSTRAINT`, or `ENABLES` are eligible; every `PREREQUISITE` row (the
   seated items' gates and the pre-existing hard prerequisites) stays a strict
   deliverable edge. Among eligible edges the minimum set that leaves the
   strict graph acyclic was computed exhaustively (no set of one to four
   eligible edges suffices; two sets of five do, differing only in which
   side of the two-node SCC is opened; the DEL-06-03 side was chosen
   because DEL-08-01's Scope of Work carries the documented clause contract,
   acceptance obligation 2, while no DEL-06-03 anchor for the propose-tool
   contract is cited) and checked for semantic fit. The five edges (seven
   rows: six of the nineteen rows emitted under D-APP-109 plus the
   pre-existing `DEP-04-05-010`) and their contract targets:
   - `DEL-04-05 -> DEL-02-05` (`DEP-04-05-010`): consumption of DEL-02-05's
     documented stored-key-status and safe key-source contract.
   - `DEL-02-01 -> DEL-02-04` (`DEP-02-01-010`, `DEP-02-04-017`),
     `DEL-02-03 -> DEL-02-04` (`DEP-02-04-019`), and
     `DEL-02-02 -> DEL-02-04` (`DEP-02-02-022`, `DEP-02-04-018`): consumption
     of DEL-02-04's documented additive v1 workspace-state field contract
     (SOW-008 as revised; applied row L310).
   - `DEL-06-03 -> DEL-08-01` (`DEP-06-03-014`): consumption of DEL-08-01's
     documented proposal-trigger clauses (SOW-082; applied row L368).
   The per-row workbook is `SCC_DECOMPOSE_RULINGS.csv` in the run folder;
   the resulting acyclic graph is recorded by a fresh `AUDIT_DEP_CLOSURE`
   snapshot whose report carries the move basis.
3. **Consequence for the other cycle-participating rows:** the thirteen
   remaining rows emitted under D-APP-109 stay strict deliverable edges in
   the acyclic graph; their `Notes` are updated from "non-gating until
   resolved" to "resolved by decompose under D-APP-110", and they gate per
   their `SatisfactionStatus` exactly like every other strict edge. The
   pre-existing rows of the former nine-node SCC that are not re-targeted
   are likewise strict edges of the acyclic graph and are not edited.
4. The record lands on PR #714 as a third commit; merge confers register
   currency only.

## What this ruling does not do

It authorizes no implementation tranche, lifecycle transition, Checking
Approval SHA change, dependency acceptance, product byte, signing, release,
pointer move, or Root act. Acceptance of the resulting closure snapshot as
the loop's DepClosure pointer remains a separate owner act. Selection of any
seated item remains a later act under `loop/LOOP_INIT.md`.

## Attribution

Transcribed and applied by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) in
an untyped Claude Code session acting as HELP_HUMAN (Agent 0); the edge
selection is the agent's recorded rationale under the owner's directed move;
the register rows are written by bounded TASK + dependency-extract Agent 2
instances under sealed briefs and independently reviewed. Role not
mechanically enforced.
