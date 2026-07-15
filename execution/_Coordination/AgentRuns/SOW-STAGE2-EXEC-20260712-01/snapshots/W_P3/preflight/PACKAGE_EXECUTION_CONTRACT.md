
# W-P3 Sequential Package Execution Contract

Status: `SEALED CANDIDATE — AWAITING HELP_HUMAN ACCEPTANCE`

This derivative contract freezes the exact 15-member ordinary Piping P3
population on `main@4d153302c3c4cd42578936db160c2bac1270225a`. It does not release a manager or authorize
project mutation.

## Execution topology

Run one fresh WORKING_ITEMS manager per package in strict order PKG-10 through
PKG-12. Within a package, execute every frozen consecutive batch in order.
Each batch has one fresh package-batch author followed only after terminal
author PASS by one fresh evidence-only verifier over 100% of the same members.
The verifier does not repair author output. Both preserve complete per-member
mapping, source-line coverage, source/evidence/production hashes, clean
finalization, exact replacement and inverse rows, simulations, project checks,
telemetry, findings, attempts, repairs, and rerun conditions.

Safe mechanical evidence defects are repaired in owned evidence scope without
stopping: retain the failed attempt, prove the repair is non-semantic, rebuild
every direct/transitive binding, and rerun affected checks. Project, source,
candidate-semantic, lifecycle, authority, or acceptance drift is not mechanical
and must be escalated.

## Content and integration fences

Candidate preparation writes only the exact package candidate/evidence scopes.
Live project paths remain read-only. Every member's future integration delta is
exactly one added clean `ScopeOfWork.md` and four deleted legacy documents;
status and all controls remain byte-identical. Only CHANGE may later integrate
an accepted RECONCILIATION manifest. PKG-00 remains excluded upstream-only
context. H2, retirement, rollback execution, release, and reliance remain
unauthorized.

After all package managers pass, direct RECONCILIATION performs aggregate
fan-in itself without a redundant child layer: 100% manifests, paths,
population/totals, replacement/rollback rows, containment and simulations;
fresh reproduction of every exception and the numerically final clean member
per package; full affected-package expansion on any exception or failure.
