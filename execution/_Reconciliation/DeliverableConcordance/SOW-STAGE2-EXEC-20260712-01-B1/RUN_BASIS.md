# RECON-B1 Run Basis

Status: `PASS — INDEPENDENT B1 VERIFICATION COMPLETE`
Observed: `2026-07-13` (America/Edmonton)
Subject basis: `main@9349594530dc19e55baf9c2ef0b7eb4716f48a17`

## Accepted authority and derivative inputs

- D-GOV-16 ruling: `7584718aa32b112e415331736d1a8e68c12ac176`.
- Accepted Stage-2 B1/G3 contract and sealed `RECON-B1` brief v1.
- Accepted `P0_BASIS` handoff SHA-256
  `6f9c62f9f8f2912c7f0287b1bdcac3ca1344ea4de8ddb79b458dea3dead5c3ca`.
- Accepted `P2_CONSUMERS` postmerge handoff SHA-256
  `fa9870c5cdd84c8e4eaf7d789ab2e4fd269575366df2fc1c97bb6a4b009add87`.
- `P3_MANIFEST` candidate and ORCHESTRATOR-B1 terminal PASS were verified as
  derivative evidence, not accepted as authority by assumption.

Local `main`, `origin/main`, and remote `refs/heads/main` independently
resolved to the exact subject basis with divergence `0/0`. The ruling commit
is an ancestor. H1 and H2 remain `UNAPPROVED` in the current work graph.

## Fences and method

The verification used commit-bound `git grep`, tracked-path enumeration,
SHA-256 recomputation, TSV/JSON parsing, status-field extraction, and
changed-path comparison. It did not delegate and did not write the P3
candidate, either project, any deliverable, caller, source, lifecycle surface,
Git state, release state, receipt, conversion output, or retirement state.
The pre-existing `.claude-worktrees/` container was excluded and not read.

This package is read-only reconciliation evidence. It recommends the B1 fan-in
result but cannot itself accept P3 or release conversion.
