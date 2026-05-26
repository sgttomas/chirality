# Guidance — DEL-099-01 Scope of Work (PKG-099 Truck Product Loading Unit 3-25)

> Directional view: why this deliverable exists, the principles that govern its drafting, considerations and trade-offs, and a Conflict Table for items requiring Human Resolution (HRR).

## Purpose

This deliverable is the EPC Integrator's authored Scope of Work for the PKG-099 Truck Product Loading Unit (3-25 Liquids Hub). It is the Gate 5 EPC anchor that establishes the package basis (function, tagged equipment identity, source basis, boundaries, and whole-facility integration narrative) from which the Package Datasheet, Construction Work Package, and downstream Vendor production units are derived.
Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-099-01 row; SKILL `four-documents` Purpose.

## Principles

1. **Source authority hierarchy.** Workbook/RFQ/Package Requirements (when accessible) and the DBM are the authoritative source set. Decomposition prose routes and scopes but does not invent design values. Source: SKILL `four-documents` Authority hierarchy.
2. **Carry-forward inaccessible sources as `location TBD`.** Where authoritative documents (e.g., `26020-Package_Requirements.docx`, RFQ docx, workbook xlsx) are not locally machine-accessible, cite the source and mark `location TBD` rather than fabricating clause text. Substantive values not in the DBM or registers become `TBD`.
3. **EPC Scope of Work vs Package Datasheet split.** Function/identity/boundaries/integration narrative live here; vendor-handoff technical data live in `DEL-099-02_package-datasheet`. Source: `DELIVERABLE_REGISTER.csv` DEL-099-01 and DEL-099-02 rows.
4. **Vendor vs Integrator responsibility split.** The Scope of Work must state the responsibility split explicitly; do not implicitly absorb vendor-owned engineering. Source: `PACKAGE_REGISTER.csv` PKG-099 row.
5. **Interface evidence, not interface design.** The Scope of Work enumerates the workbook-flagged interface types and `IFC-*` IDs; detailed interface requirements develop in the Package Datasheet. Source: `INTERFACE_REGISTER.csv` PKG-099 rows.

## Considerations

- **LACT vs truck loading as parallel product dispositions.** Sales condensate exits via either the NRM third-party LACT (custody transfer to pipeline) or via the in-scope truck-loading stations (atmospheric trucks). The Scope of Work narrative should make this parallelism explicit so downstream design does not collapse the two routes. Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 22); SEC-05 (line 207); SEC-06 (line 414–417).
- **Winter and spill considerations are first-class.** The -40 deg C design basis and the spill-control provisions at truck-loading slabs (for condensate, produced water, caustic, H2O2) are basis-of-design items that the Scope of Work should not omit. Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-12 (lines 688, 696).
- **Permit posture.** The truck-rack scope is on the path of a BCER permit amendment beyond the existing liquids-hub permit 100120203; the Scope of Work should flag this so downstream scheduling/permit deliverables can attach. Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-17 (line 872).
- **Detection coverage.** F&G coverage (LEL/H2S/methyl mercaptan/fire) over the truck loading area is required, but device counts and voting logic are not yet resolved; carry as `TBD`. Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-15 (line 838).

## Trade-offs

- **Two-stations-at-2x2 vs three-single-stations.** See CT-01 below. The Workbook/RFQ row records 2 stations each loading 2 trucks (2x2 = 4 simultaneous bays); the DBM records 3 stations with 1 loading pump per station. Trade-offs (throughput at design conditions, peak truck queuing, redundancy on pump trip, civil footprint, fire/spill envelope) cannot be balanced until human ruling fixes the station count basis.
- **Per-station capacity vs total daily throughput.** 103 m3/h per station from the DBM has not been reconciled against an authoritative daily truck-loading demand profile or RFQ requirement; treat as a per-station basis only.
- **Vendor freedom vs integration certainty.** The Scope of Work intentionally limits prescription so the Package Vendor can engineer the equipment; over-prescription here narrows vendor solution space and may force costly Scope changes.

## Examples

- Workbook-derived function statement (R-1) used verbatim in the Scope of Work function section preserves direct source fidelity and is the recommended pattern for `Function` paragraphs.
- The interface enumeration (R-9) is best presented as a table listing the eleven flagged interface types with their `IFC-*` IDs; this mirrors the workbook X-column truth and provides traceability into the Package Datasheet without restating it.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Number of truck-loading stations and arrangement | `PACKAGE_REGISTER.csv` PKG-099 row (Package Scope): "Two truck loading and unloading stations, each capable of loading two trucks simultaneously (2x2)" — derived from Workbook row 98 and RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`; `ARTIFACT_REGISTER.csv` ART-517D0E9F90 (Quantity: 2) | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 line 40, SEC-06 lines 414, 526, 578, 654: "three product truck-loading stations" with "Condensate loading pumps — three pumps, one per truck loading station" | Datasheet (Attributes, Construction), Specification (R-3, R-5), Guidance (Trade-offs), Procedure (Steps) | Workbook/RFQ row is the package-procurement basis and the more current Package Requirements source for PKG-099; DBM may reflect an earlier facility-level basis. **PROPOSAL: adopt 2 stations (2x2) for PKG-099 and re-baseline DBM SEC-06 numbers; raise as an SCC if both are intentional.** | TBD |
| CT-02 | Per-station capacity not corroborated outside DBM | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 415): 103 m3/h per station, 345 kPad differential | `26020-Package_Requirements.docx` heading 51 (not locally accessible); RFQ (not locally accessible) | Datasheet (Attributes), Specification (R-4), Procedure (Verification) | **PROPOSAL: carry DBM value as `ASSUMPTION` until the Package Requirements / RFQ text is extracted to confirm.** | TBD |
| CT-03 | Exclusions statement | `PACKAGE_REGISTER.csv` PKG-099 row (Exclusions): "TBD; no package-specific exclusions stated in source materials." | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 (line 22), SEC-06 (line 216) implies LACT and pipeline-export-by-others are excluded | Specification (R-10) | **PROPOSAL: record LACT third-party scope and downstream pipeline-by-others as facility-level exclusions, and keep "no package-specific exclusions stated" caveat from the workbook.** | TBD |
| CT-04 | F&G detection coverage for truck loading area | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-15 (line 838) requires coverage but defers device counts/voting to detailed design | None — no opposing source available | Datasheet (Conditions), Specification (R-9 / Fire & Gas interface) | **PROPOSAL: carry as `TBD` requiring resolution at Package Datasheet phase.** | TBD |
