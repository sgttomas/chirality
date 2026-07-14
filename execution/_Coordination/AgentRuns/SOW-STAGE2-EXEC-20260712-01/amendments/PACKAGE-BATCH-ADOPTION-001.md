# Amendment — Package-Batch Adoption

AmendmentID: `PACKAGE-BATCH-ADOPTION-001`
Recorded: 2026-07-14
Authority: explicit human ruling
AppliesTo: remaining ordinary Stage-2 representation migration
Status: `ACCEPTED`

## Ruling and evidence

The human accepted the PKG-01 and PKG-02 package-batch experiments as valid
for adoption. PKG-01 established sufficient faithful-representation quality
for three members and 727 source lines; PKG-02 repeated the result for five
members and 2,053 source lines with no observable task or context drift. The
human also accepted the experiments' documented immutable-evidence whitespace
warnings. Neither experiment exposed native token/context occupancy, so no
larger or unbounded-capacity claim is made.

Accepted evidence:

- `execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01/HANDOFF_STATE.md`
- `execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/HANDOFF_STATE.md`
- `execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/HUMAN_RULING_CHANGE_AMENDMENT.md`

## Adopted operating rule

For related four-document to `SOW_V1` migration, one WORKING_ITEMS manager owns
the package and dispatches one package-wide author followed by one fresh
package-wide evidence-only verifier for a batch of no more than five members
and no more than 2,053 frozen legacy source lines. If either limit would be
exceeded, the manager partitions ascending numeric `DeliverableID` order into
the minimum number of consecutive sub-batches that each satisfy both limits.

The session reduction does not reduce evidence. Both returns preserve complete
per-member mappings, source-line coverage, source/evidence/production hashes,
finalization reports, replacement and inverse rows, simulations, checks,
telemetry, findings, and rerun conditions. The verifier reviews every member,
is fresh from the author, and does not repair author output.

RECONCILIATION retains 100% aggregate, manifest, containment, and
apply/rollback coverage; freshly reproduces every exception and at least the
numerically final clean member per package; and expands to the affected full
package, across all sub-batches, upon any exception or aggregate/sample
failure.

## Unchanged authority and fences

This amendment changes only ordinary representation-migration session
topology. It does not authorize semantic scope changes, project lifecycle
changes, ISSUED `DEL-01-01` integration before H1, legacy retirement before
H2, Piping PKG-00 conversion, evidence-rich candidate integration, verifier
repair, or bypass of deterministic clean finalization and CHANGE closeout.
Clean production remains the only integration input.
