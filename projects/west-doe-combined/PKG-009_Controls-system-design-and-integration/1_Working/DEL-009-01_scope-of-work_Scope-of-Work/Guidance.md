# Guidance: DEL-009-01_scope-of-work - Scope of Work

## Purpose

This guidance explains how to draft and review the PKG-009 EPC Scope of Work using the accepted Gate 7 decomposition snapshot as upstream truth. The deliverable exists to anchor the Controls system design and integration package under WBS 02 before downstream datasheet, construction work package, and discipline production package work proceeds.

## Principles

- Preserve the package identity exactly as stated in the accepted snapshot: PKG-009, Controls system design and integration, WBS 02, workbook row 10, CoA tracking number 26020-01-32-001.
- Treat the scope-of-work deliverable as an EPC Integrator artifact, not as a vendor package specification, unless a later source slice changes the responsibility basis.
- Carry the package interfaces as scope context, while leaving detailed interface requirements to the package datasheet unless the Scope of Work needs high-level boundary language.
- Use the supported objectives as directional context, not as a basis to invent design values or code-level obligations.
- Keep unsupported details as TBD. The current deliverable references state that no deliverable-specific source slices were copied during PREPARATION.

## Considerations

The package register identifies eight applicable interface types: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. For this Scope of Work, these should be presented as boundary and integration context rather than detailed interface matrices.

The package register also records that controls power-panel interfaces remain interface facts or artifacts under the package datasheet and do not create a separate package or deliverable. The Scope of Work may mention this disposition if it is useful for boundary clarity.

The responsibility model is source-limited. Avoid stating a final EPC-versus-subcontractor split beyond the accepted wording: "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources."

## Trade-offs

| Topic | Guidance |
|---|---|
| Scope completeness vs. source fidelity | Prefer a complete structure with TBD fields over unsupported detail. |
| Interface visibility vs. duplication | List interface types and boundary intent in the Scope of Work; reserve detailed interface requirements for the package datasheet. |
| Objective traceability vs. requirements inflation | Include mapped objectives for traceability, but do not convert objective statements into requirements unless the source basis supports that conversion. |
| Responsibility clarity vs. over-assignment | Record EPC Integrator ownership for this deliverable and preserve source-dependent responsibility wording for execution details. |

## Examples

Example identity statement:

> DEL-009-01_scope-of-work is the EPC Scope of Work for PKG-009, Controls system design and integration, WBS 02, sourced to Workbook Packages row 10 and accepted in the Gate 7 final published PROJECT_DECOMP snapshot.

Example TBD usage:

> Package-specific exclusions: TBD; no package-specific exclusions stated in source materials.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | No source conflict identified during P1/P2 drafting. | N/A | N/A | N/A | N/A | N/A |
