
- **2026-07-28 — Receipt 116** (PROJECT_SETUP reference and live-pointer parity after SCA-003).
  - Owner direction and approved PROJECT_SETUP recommendation are recorded
    verbatim in
    `projects/pec/execution/_Coordination/PROJECT_SETUP_REFERENCE_PARITY_2026-07-28/RUN_MANIFEST.md`.
  - Basis: current main `4cd25b348196f7e6dfa925d8c7938184924cb383`;
    PRD v2.2 SHA-256 `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`;
    accepted decomposition revision 1.3 SHA-256
    `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.
  - Applied: all 64 deliverable `_REFERENCES.md` packets now cite PRD
    v2.2 and revision 1.3; current AGENTS, README, STATUS, coordination,
    and standing-workplan pointers are aligned to the accepted SCA-003
    successor.
  - Preserved: every ScopeOfWork contract, active reliance hold,
    lifecycle file, topology/register byte, dependency file, frozen
    implementation file, estimate, and schedule. The 32 affected
    contracts remain `STALE_FROZEN`; `PEC-HOLD-001` remains `ACTIVE`.
  - Checks: 64/64 reference shape and exact-postimage validation; strict
    decomposition-register validation (64 registers, 254 rows, zero
    errors/warnings); dependency closure (119 edges, zero SCCs); path
    containment, preservation hashes, whitespace, and Git diff checks.
  - Gate: pointer parity only. No production reliance, activation,
    lifecycle, topology, dependency, ScopeOfWork, implementation,
    estimate, schedule, release, or hold-release authority is created.
