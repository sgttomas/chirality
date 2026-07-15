# Root Governance Workplan — PKG-00 Post-Consolidation State

Status: `CLOSED — CURRENT-STATE POINTER`
Date: 2026-07-15
Supervising role: `HELP_HUMAN`

## Goal

Preserve a deterministic root entry point after the owner's PKG-00 reversal
and Piping decision D-43. This workplan records current state; it does not
authorize another implementation tranche.

## Step 0 — Current-state preflight

1. Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
2. Require synchronized `main` containing merge commit
   `291301291bdaa8ec6b64dbbf3cff98ecfeadeca7` and this successor handoff.
3. Read `execution/_Coordination/HANDOFF_STATE.md`, Piping decision D-43, and
   `projects/chirality-piping/execution/PKG-00_Software Architecture Runway/CONSOLIDATION_MANIFEST.md`.
4. Run
   `python3 projects/chirality-piping/tools/validation/validate_architecture_basis.py`.
5. Treat a census, lifecycle, reading-contract, compatibility, or authority
   delta as a new decision request; do not absorb it silently.

## Current closure

- The 146-member Scope-of-Work conversion remains closed and unchanged.
- The eight Piping PKG-00 members are reference-only
  `ArchitectureBasis.md` members under D-43, not production contracts and not
  live four-document kits.
- Root four-document compatibility machinery remains retained because the
  owner reversed the PKG-00 file disposition only; no root-tool retirement
  was directed.
- Historical H2-R receipts and frozen evidence remain accurate for their
  recorded basis and are not current-state pointers.

## Parked lanes

- Root compatibility-tool retirement requires a new explicit human ruling
  plus fresh caller and rollback evidence.
- A DAG successor must be produced by the Piping DAG-owning workflow; DAG-007
  remains an immutable accepted snapshot.
- PDU-007 and TP-SEAM-WASM-001 remain routed to REVIEW through their existing
  project authority paths.

## Stop state

No lane is released by this pointer. If the preflight passes and no new owner
direction is present, return the closed state and stop.
