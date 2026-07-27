# Decomposition Coverage Report — SCA001_PRECHANGE

## Audit basis

This immutable snapshot is derivative audit evidence. It evaluates `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` as the accepted root SOFTWARE decomposition, with expected upstream identity `accepted root decomposition revision v1.0 at AcceptedCandidateSHA ec62af0700e530c1640698fa406398cb1cb45d29`, against the filesystem state at Git HEAD `918bb48b8fcee66c031d0d6d4040a46089f96067`. It supports `SCA-001 Gate 1 pre-change baseline` and does not replace decomposition truth.

Authoritative inputs evaluated:

- Working surface: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` (Revision v1.0; AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`).
- Deliverable fields: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- Scope ledger: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- Objective mapping crosscheck: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_objective_register_v1_0.csv`.
- Filesystem product state: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/PKG-*/1_Working/DEL-*`.

## Overall verdict

`OVERALL_STATUS = OK`
`CLOSURE_READINESS = PASS`

There are no BLOCKER or WARNING findings. The accepted topology is fully materialized, contexts are faithful, every production contract validates, ledger and objective references close, and the modular package roles are explicit. The issue log contains 132 INFO entries because anticipated production outputs are not yet present while every deliverable is still `INITIALIZED`; this is lifecycle-appropriate and is not a Gate 1 discrepancy.

## Twelve-check summary

| Check | Name | Verdict | Evidence |
|---|---|---|---|
| 1 | Forward Coverage — Packages | PASS | 6/6 declared packages have matching folders. |
| 2 | Forward Coverage — Deliverables | PASS | 45/45 declared deliverables have matching folders under their declared packages. |
| 3 | Reverse Coverage — Folders | PASS | No reverse-only package or deliverable folder exists. |
| 4 | ID Consistency | PASS | All full SOFTWARE package and deliverable IDs match their folder names. |
| 5 | Context Fidelity | PASS | 45/45 contexts match name, package, type, responsible party, description, and ContextEnvelope. |
| 6 | Artifact Presence | PASS | All 45 clean SOW_V1 contracts validate. Produced anticipated outputs are 0/132; 132 absences are INFO because all deliverables are INITIALIZED. |
| 7 | Objective Mapping | PASS | All 7 ledger-resolved objectives have existing supporting deliverables; companion support counts agree. |
| 8 | Ledger Integrity | PASS | All 94 IN rows reference existing packages and deliverables (or lawful TBD; none observed). |
| 9 | Derivative Package Parity | SKIPPED | Not variant-owned by this SOFTWARE audit. |
| 9b | Package-Shape Conformance | PASS | Companion roles are explicit; heavy truth remains in authoritative registers; no derived authority confusion found. |
| 10 | Active Snapshot and Handoff State | SKIPPED | No execution/_ScopeChange/_LATEST.md exists; this run is the pre-change Gate 1 baseline. |
| 11 | Lifecycle Distribution | PASS | 45 INITIALIZED; no unexpected state values. |

## Per-check evidence

### Checks 1–4 — topology and identifiers

Six declared packages and 45 declared deliverables match the six package folders and 45 immediate `1_Working/DEL-*` folders exactly. There are no missing declarations, reverse-only folders, or ID mismatches. Evidence: decomposition §§8–9 and the filesystem paths enumerated in `Decomp_Coverage_Matrix.csv`.

### Check 5 — context fidelity

All 45 `_CONTEXT.md` files are present and match the authoritative companion register on Name, Package reference, Type, Responsible, Description, and ContextEnvelope. Evidence: `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv` rows 2–46 and each matrix row's deliverable path.

### Check 6 — artifact presence and production format

Every deliverable resolves to a valid clean `SOW_V1` contract. No legacy four-document kit or ambiguous dual format was found. The protocol's folder-local filename scan found 0 of 132 anticipated production artifacts. Because all 45 deliverables are `INITIALIZED`, each absence is logged as INFO, not WARNING. Control surfaces and the production contract itself are not treated as produced outputs.

### Check 7 — objective mapping

The Scope Ledger yields OBJ-001 through OBJ-007. All have supporting deliverables with existing folders. Deliverable-register support counts are OBJ-001=9, OBJ-002=8, OBJ-003=14, OBJ-004=9, OBJ-005=4, OBJ-006=3, OBJ-007=2, and match the objective register exactly. No objective is supported only by RETIRED deliverables.

### Check 8 — ledger integrity

All 94 IN rows among 103 ledger rows reference an existing package and existing deliverable(s); no invalid reference or unrecognized ID occurs. Fifteen IN rows carry no ObjectiveIDs, but Check 8 does not require every scope item to map directly to an objective, and all deliverables themselves have objective mappings.

### Check 9 — derivative-package parity

SKIPPED: this check is DOMAIN-owned. No SOFTWARE derivative-parity verdict is inferred.

### Check 9b — package-shape conformance

PASS. The main document's §3 companion inventory labels the working surface and all six authoritative companion registers. Ledger and full deliverable truth remain in companion CSVs instead of being exhaustively duplicated inline. The document expressly states no derived publication artifact exists and no such artifact is used as an amendment surface.

### Check 10 — active snapshot and handoff state

SKIPPED. `execution/_ScopeChange/_LATEST.md` is absent, which is consistent with a pre-change Gate 1 baseline. No active snapshot or later closure claim was inferred.

### Check 11 — lifecycle distribution

All 45 deliverables are `INITIALIZED`; no unknown or unexpected lifecycle state occurs.

## Top issues

1. INFO — 132 anticipated production artifacts are not present inside their deliverable folders. This is expected at `INITIALIZED`; it becomes actionable only when a deliverable reaches `IN_PROGRESS` or later without its expected outputs.
2. INFO — the artifact-presence metric is 0.0% and must not be misread as structural failure: it measures produced outputs, not the 45/45 valid `SOW_V1` production contracts.
3. INFO — Check 10 has no active SCOPE_CHANGE snapshot to audit because this is the pre-change baseline.

## What to fix for a cleaner rerun

No pre-change structural repair is required. Proceed with SCA-001 Gate 1 using this snapshot as baseline evidence. On later reruns, production agents should materialize anticipated outputs within their authorized deliverable folders and advance lifecycle state only when the selected production contract and evidence support it.
