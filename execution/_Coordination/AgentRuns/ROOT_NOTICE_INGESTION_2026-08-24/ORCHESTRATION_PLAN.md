# Orchestration Plan — Root Notice Ingestion — 2026-08-24

- **Plan version:** 1
- **Selection authority:** HUMAN — R11-A and the owner-carried notice-ingestion steer
- **Basis:** `origin/main@8884b143f3d8dbca49756e981e4e20299d55875d`
- **Posture:** `TERMINAL_FAN_OUT_IN` (one bounded node)
- **Objective:** record the routed SCA-APP-008 Gate-5 notice byte-for-byte and return a Root/App contract-drift result without adopting or repairing its content.

## Work graph

| Node | Executor | Depends on | Write ownership | Expected return | Fan-in gate |
|---|---|---|---|---|---|
| N1 notice ingestion | bounded ephemeral Agent 2 | verified basis gate and Root G0–G4 | destination notice plus this node's instance records | exact copy identity; drift-check result; ledger disposition; changed-path inventory | destination SHA equals source; no Root/App divergence; no out-of-scope write |

## Human gates and stops

- Any exact Root/App contract divergence stops the tranche for owner routing.
- Any identity disagreement, unexpected ledger requirement, or write outside the steer stops the tranche.
- Adoption, amendment, declination, blocker lift, lifecycle, implementation, release, publication, reliance, and merge remain owner acts outside this run.

## Validation owner

HELP_HUMAN validates the Agent 2 return, reruns the required checks, appends Receipt 128, and performs Git closeout without merging.
