# Guidance — DEL-078-04 Vendor Engineered Equipment Package

> Directional rationale for the Pig Receivers (Inlet) 4-25 vendor-engineered equipment package. Rationale is drawn from accessible sources; speculative content is omitted or marked `TBD`.

## Purpose

This deliverable exists to ensure the Package Vendor delivers a complete, source-anchored engineered equipment package for the plant inlet pig receivers of the 4-25 Deepcut facility, suitable for integration by the EPC Integrator into the larger process facility.
Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` line 435.

## Principles

1. **Source-anchored design.** Vendor engineering shall be grounded in the EPC Scope of Work (`DEL-078-01`), Package Datasheet (`DEL-078-02`), the project DBM (`DBM-Deepcut/4-25_Deepcut_DBM.md`), and the RFQ source basis. Decomposition prose is routing context only, not a design source.
2. **Three identical units.** The three pig receivers are identical to simplify spares, operations, and maintenance. Source: `PACKAGE_REGISTER.csv` row 78.
3. **Pigging-friendly inlet.** Upstream isolation valves and ESDVs must be full port; barred tees protect facility piping from pig migration. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
4. **Safe opening practice.** Sweet-gas purge from low-pressure fuel gas prepares the receiver for opening; vents route to HP flare. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
5. **HIPPS protects inlet separators.** The HIPPS package on the receiver skid protects the inlet separators if inlet pipeline MAOP can exceed facility inlet design pressure. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.
6. **Clear scope split.** Package Vendor owns the package; EPC Integrator owns facility-level integration. Source: `PACKAGE_REGISTER.csv` row 78.

## Considerations

- **Inlet pipeline MAOP vs. facility inlet design pressure.** If MAOP exceeds facility inlet design pressure, HIPPS is required; HIPPS architecture and setpoints are to be confirmed during detailed engineering. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809 and §Assumptions/TBDs.
- **Shutdown setpoints and gas inventory.** Setpoints must account for the high-pressure gas volume between plant inlet ESDVs and inlet separator inlet PCVs. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.
- **Sour wet service.** Materials of construction must accommodate Alberta sour-service requirements; specific material grades are **TBD** (not stated in accessible source slices).
- **Pipeline final configuration unresolved.** Inlet pipeline final configuration, detailed tie-ins, and any second inlet pipeline pig receiver/isolation requirements are **TBD** (Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §Assumptions/TBDs). Vendor package must be flexible enough to accommodate facility-level changes during detailed engineering.
- **Interface coverage.** Ten interface types are declared on PKG-078; vendor engineering must surface and resolve each with EPC Integrator. Source: `PACKAGE_REGISTER.csv` row 78.

## Trade-offs

- **Skid count vs. layout.** Three independent skids increase footprint but improve maintainability and isolation between receivers. The DBM-stated configuration is non-enclosed structural-steel skids. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585.
- **HIPPS vs. larger receiver design pressure.** HIPPS allows downstream equipment (inlet separators) to be rated lower than the upstream pipeline MAOP. Whether HIPPS is needed depends on the MAOP-vs-design-pressure margin (TBC). Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.
- **Vendor-standard vessel vs. custom design.** A vendor-standard 24" pig receiver may be acceptable if it meets project sour-service material and HIPPS-integration requirements; otherwise a custom design is required. **TBD** in accessible sources.

## Examples / Precedent

- The sister facility 3-25 Compressor Station Pig Receivers (PKG-089) carries the same six-deliverable Gate 5 pattern with the same EPC/Vendor split. Source: `DELIVERABLE_REGISTER.csv` lines 429-431 (PKG-089 family).
- The 4-25 Deepcut DBM line 2550 lists "Pig Receivers (Inlet) 2" with quantity 3, consistent with this package's three-receiver basis.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| C-01 | Pig receiver quantity: PACKAGE_REGISTER and DBM line-item row 61 specify three (3) receivers; DBM narrative §Inlet Pipeline (line 585) states "one 610 mm OD (24 in.) pig receiver" | `PACKAGE_REGISTER.csv` row 78 + `DBM-Deepcut/4-25_Deepcut_DBM.md` line 2611 (qty 3) | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 585 (qty 1) | Datasheet §Identification, §Package Attributes; Specification REQ-01, REQ-02 | PROPOSAL: take PACKAGE_REGISTER + DBM Line-Item Requirements (qty 3) as authoritative; DBM narrative likely describes a single-receiver phase or train within the broader three-receiver package; carry as evidence rather than ruling. | TBD |
| C-02 | HIPPS package presence: PACKAGE_REGISTER row 78 declares HIPPS bundled with receiver skids; DBM line ~809 frames HIPPS as conditional ("may be required" if MAOP > facility design pressure) | `PACKAGE_REGISTER.csv` row 78 | `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809 | Datasheet §Package Attributes; Specification REQ-06, REQ-08 | PROPOSAL: PACKAGE_REGISTER row 78 is project authority — HIPPS is included by scope; DBM "may be required" reflects the open architectural detail (HIPPS basis, setpoints) rather than HIPPS presence. | TBD |
| C-03 | RFQ Word source basis (`26020-01-PT-RFQ-35-001-Pig_Recv_2.docx`) and project Package Requirements .docx (heading 31) are referenced but not locally rendered; many quantitative parameters (design pressure, temperature, materials) remain `TBD`. | `PACKAGE_REGISTER.csv` row 78; `_REFERENCES.md` | (Sources not locally accessible) | Datasheet §Service Conditions, §Construction; Specification REQ-14 | PROPOSAL: convert RFQ and .docx to locally accessible markdown before next pass to resolve `TBD` quantitative values. | TBD |
