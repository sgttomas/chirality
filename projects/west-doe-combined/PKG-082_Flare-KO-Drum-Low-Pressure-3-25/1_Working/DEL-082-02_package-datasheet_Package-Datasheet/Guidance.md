# Guidance — DEL-082-02 Package Datasheet (Flare KO Drum, Low Pressure, 3-25)

## Purpose

This deliverable is the EPC Integrator's mandatory technical handoff datasheet for the LP flare knock-out drum package (V-3900-2 with transfer pump P-3900-2). It carries the package data required for third-party vendor or discipline-package engineering and design, as identified by the PROJECT_DECOMP Gate 7 snapshot for PKG-082. It is also a Gate 5 EPC anchor deliverable per `_CONTEXT.md` "Notes". Interface facts for this package are deliberately carried here as evidence rather than as standalone deliverables.

## Principles

- **Source fidelity over convention.** Numeric values, equipment counts, tags, and interface sizes are drawn from the 3-25 DBM ("Flare and Blowdown" section and equipment summary). Where the DBM does not state a value, the Datasheet and Specification carry `TBD` rather than a plausible default.
- **Single source of equipment identity.** V-3900-2 and P-3900-2 are the controlling tags for this package; they originate from the DBM equipment summary and Flare-and-Blowdown narrative and shall not be renamed in derivative documents.
- **Shared-interface humility.** The flare stack is a shared 03-25/04-25 asset and its sizing/OD remain partly open in the DBM source. The package datasheet states the interface but does not over-commit to shared-asset design.
- **Staggered blowdown discipline.** Final relief sizing for the LP KO drum depends on staggered blowdown sequencing governed by W242510-PRC-REP-000003-001; downstream readers must treat current sizing as preliminary until that document is brought into the workspace.

## Considerations

- **Sour-service applicability.** The DBM general isolation paragraph (line 607) treats sour hydrocarbon service as a project-wide consideration. Applicability to the LP KO drum specifically is recorded as ASSUMPTION in the Specification (R-10) and must be confirmed by the project materials engineer before vendor materials selection.
- **Inaccessible primary references.** The decomposition source row cites `26020-Package_Requirements.docx` heading 35 and `26020-Packages_Interfaces_4_export.xlsx` Packages row 56 as the package basis. Neither is accessible as parsed text in this workspace. Any content uniquely determined by those documents is `TBD` in this draft.
- **Interface scope.** This deliverable intentionally carries interface facts (LP relief header size, slop transfer destination, utility tie-ins, shared flare stack) rather than deferring them to a separate interface document — per `_CONTEXT.md` Notes.

## Trade-offs

- **Completeness vs. fidelity.** Source slices give us equipment identity, service definition, transfer-pump count, header size, and the shared-flare context. They do not give vessel sizing, design pressure, materials, or instrumentation. The draft preserves fidelity by leaving the missing items `TBD` rather than producing speculative vendor-ready content.
- **1 x 100 percent transfer pump.** The DBM equipment summary records "1 x 100 percent" for the LP KO drum transfer pump. This avoids spared-pump cost but concentrates availability risk; that trade-off is owned by the DBM and inherited here without modification.

## Examples

No source-grounded worked examples (sizing case, relief load tabulation, level-control narrative) are available in the accessible source slices. Examples are intentionally omitted until source content supports them.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-01 | Sour-service applicability to V-3900-2 / P-3900-2 not explicitly stated; DBM only addresses sour-service as a general project consideration. | DBM line 607 (general isolation philosophy) | None explicit at LP KO drum scope | Datasheet "H2S / sour service exposure"; Specification R-10 | Treat as sour-service until materials engineer rules otherwise | TBD |
| CF-02 | LP relief header size carried as 508 mm / 20 inch in DBM basis, but final flare studies are pending and may revise. | DBM line 499 (current basis) | DBM line 555 ("Required Closeout") | Datasheet "Upstream relief header"; Specification R-04 | Hold 508 mm / 20 inch as basis pending final flare study | TBD |
| CF-03 | Document number W242510-PRC-REP-000003-001 is cited in two distinct contexts (shutdown/blowdown and prime-mover/emissions cross-reference); DBM explicitly flags the cross-reference conflict. | DBM line 501 | DBM "Prime Mover Basis" cross-reference note (line ~533) | Specification R-06 (basis for staggered blowdown) | Treat as the shutdown and blowdown philosophy document for R-06 purposes | TBD |
