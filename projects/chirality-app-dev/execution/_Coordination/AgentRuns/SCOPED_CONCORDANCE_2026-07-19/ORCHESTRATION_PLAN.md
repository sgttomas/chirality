# Orchestration Plan — Scoped Concordance Pass (D-APP-65 disposition 7)

- **RunID:** SCOPED_CONCORDANCE_2026-07-19
- **Plan version:** 1 (frozen before dispatch)
- **Authority:** D-APP-65 disposition 7 (owner-accepted recommendation 7: scoped
  concordance pass, post-merge, after items 2 and 5 landed — both merged at
  PR #283, HEAD `ff2f68c82dc2cf10269c0a2d149718cf9ca897c9`). Method basis:
  D-APP-55 run ratified method revisions (R0 report §4 MR-1..MR-11) plus
  `R2_METHOD_ADDENDUM.md`, applied scoped-not-whole-corpus.
- **Selection authority:** AGENT_0 (HELP_HUMAN posture) under the owner's
  scheduled direction; posture `TERMINAL_FAN_OUT_IN`.
- **Baseline (drift window):** R6 closure basis `c313325b74d37da1aacc4d988046cfbd26c88bf4`
  → HEAD `ff2f68c82`. Accepted upstream snapshots:
  `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (claim ledger) and
  `R6_D55_BACKCHECK_2026-07-12_1903Z` (closure verdict). This run is a
  derivative package citing both; it is not decomposition truth.

## Scope rule (what a discovery agent re-adjudicates)

A prior claim row is IN SCOPE iff any of:
(a) a file cited by the claim (NormativeSource / ImplementationEvidence /
    VerificationEvidence / AssessmentEvidence) or under its deliverable folder
    changed in the drift window (see per-package manifest);
(b) the claim's substance rests on a shared surface listed in
    `MANIFESTS/SHARED_changed_files.txt` (authority docs, frontend runtime,
    loop/governance) that changed in a way bearing on the claim;
(c) a post-R6 governed record (new Evidence_*, `_run_records/**`, register rows
    D-APP-57..D-APP-67) materially bears on the claim.
Everything else is out of scope and its R3/R6 disposition stands unexamined
(the 833-ALIGNED bulk has no reason to have moved — accepted basis).

Additionally each agent scans its package's changed files for NEW drift
(assertions that contradict live implementation or ruled state), minting new
rows `DEL-XX-YY-SCOPED-Snn`.

## Work graph — six discovery children, then one adversarial verifier

| Instance | Packages | Write target (disjoint) |
|---|---|---|
| G1 | PKG-00, PKG-01 | `PKG_LEDGERS/PKG-00_*`, `PKG_LEDGERS/PKG-01_*` |
| G2 | PKG-02, PKG-03 | `PKG_LEDGERS/PKG-02_*`, `PKG_LEDGERS/PKG-03_*` |
| G3 | PKG-04 | `PKG_LEDGERS/PKG-04_*` |
| G4 | PKG-05, PKG-06 | `PKG_LEDGERS/PKG-05_*`, `PKG_LEDGERS/PKG-06_*` |
| G5 | PKG-07, PKG-08 | `PKG_LEDGERS/PKG-07_*`, `PKG_LEDGERS/PKG-08_*` |
| G6 | PKG-09, PKG-10 | `PKG_LEDGERS/PKG-09_*`, `PKG_LEDGERS/PKG-10_*` |
| V1 | all (read-only recheck) | `instances/V1/RETURN.md` copy only |

All children: bounded file tools only (Read/Grep/Glob/Write; no Bash), read
scope repo-wide, write scope exactly the listed run-folder targets. F-APP-3:
no `_DomainEngines/**` or piping writes. Fan-in gate: all six ledgers present,
schema-valid, every in-scope claim dispositioned; V1 recheck ≥25 rows sampled
across all six returns with contradictions resolved or escalated before
assembly. Failures isolate to their instance.

## Outputs

Run folder `execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/`:
MANIFESTS (frozen inputs), PKG_LEDGERS (per-package scoped ledgers + notes),
`SCOPED_SUMMARY.md`, `HANDOFF.md`. Control-plane records under this AgentRuns
folder. No `_STATUS.md`, kit, register, or lifecycle edits in this pass —
repairs, if any emerge, are slated for owner decision, not executed here
(proposal-only, mirroring the R3→R4 contract).
