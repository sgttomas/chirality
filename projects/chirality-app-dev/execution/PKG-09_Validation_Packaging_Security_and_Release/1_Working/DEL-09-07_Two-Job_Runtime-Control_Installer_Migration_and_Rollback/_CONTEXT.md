# Context: DEL-09-07

**Name:** Two-Job Runtime-Control Installer Migration and Rollback
**Package:** PKG-09 Validation, Packaging, Security, and Release
**Discipline:** NOT_PRESENT_IN_ACCEPTED_DECOMPOSITION
**Type:** MIGRATION_SCRIPT
**Responsible:** TBD
**Context Envelope:** M

## Description
Provide the App-side installer transaction for two Root-owned launchd jobs through Root-owned runtime-control IPC, with staging, effective-state inspection, rollback, upgrade/uninstall, and cleanup evidence.

## Anticipated Artifacts
- Two-job installer/migration script
- Transaction journal
- Effective-state inspector
- Rollback, upgrade, uninstall, and cleanup fixtures and evidence

## Traceability
- **Covers Scope Items:** SOW-080
- **Supports Objectives:** OBJ-008

## Authority Boundaries
- This is an App packaging-integration transaction only. Root owns supervisor, runtime-control, and storage semantics through `DEL-02-07` and `DEL-02-11`.
- Consequential generic-runtime implementation changes activate Root `DEL-02-06`; this scaffold grants no such implementation act.
- F-APP-2 and D-APP-97 remain active. No signing, notarization, publication, release-readiness, implementation, or release act is authorized.
- G5/G6 release gates remain downstream and unchanged.

## Decomposition Reference
- **Decomposition:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- **Deliverable ID:** DEL-09-07
- **Candidate Scope Change:** `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/`
