# Specification: DEL-052-01 — Scope of Work, PKG-052 Inlet / TEG Dehy Cross Exchanger

This Specification is the normative content of the EPC Integrator Scope of Work for PKG-052. It is grounded in PACKAGE_REGISTER.csv row 62 and the DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" source slice. Items not supported by accessible sources are marked TBD.

## Scope

### In Scope (this deliverable)

1. Define the EPC Integrator Scope of Work for PKG-052 Inlet / TEG Dehy Cross Exchanger, including:
   1.1. Tagged equipment and package identity for the one (1) shell-and-tube heat exchanger E-5718-1 (TEMA 'R' BEM). Source: PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger".
   1.2. Package function: cold sour inlet separator overhead gas / warm process gas heat integration ahead of inlet compression and molecular-sieve filtration. Source: PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger".
   1.3. Source basis: West Doe Deep Cut (04-25) Design Basis Memorandum and the 26020 package requirements. Source: _REFERENCES.md.
   1.4. Boundaries of EPC Integrator scope versus Package Vendor scope at the package skid edges (see Section 2).
   1.5. Whole-facility integration narrative covering interfaces to inlet separation (PKG-056), inlet compression (PKG-048), TEG dehydration (PKG-068) and amine sweetening (warm-side, conflict pending), and molecular-sieve filtration. Source: DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" and "Interfaces".

### Out of Scope (this deliverable)

- Package engineering, package design, vendor documentation, and physical equipment supply (Package Vendor responsibility; covered by DEL-052-04 and DEL-052-05). Source: PACKAGE_REGISTER.csv row 62 (Responsibility); DELIVERABLE_REGISTER.csv rows 339, 340.
- Package datasheet content (covered by DEL-052-02). Source: DELIVERABLE_REGISTER.csv row 337.
- Construction installation/turnover detail (covered by DEL-052-03). Source: DELIVERABLE_REGISTER.csv row 338.
- Vendor package review and acceptance (covered by DEL-052-06). Source: DELIVERABLE_REGISTER.csv row 341.

## Requirements

### R1 — Tagged Equipment and Package Identity

R1.1 The Scope of Work shall identify the package by Workbook ID 52, PKG-052, Equipment Tag 26020-01-PT-16-001, and primary equipment tag E-5718-1. Source: PACKAGE_REGISTER.csv row 62.

R1.2 The package shall comprise one (1) shell-and-tube heat exchanger of TEMA 'R' BEM configuration with associated piping, instrumentation, and skid. Source: PACKAGE_REGISTER.csv row 62 (Scope).

R1.3 The Scope of Work shall record the equipment design duty as 5,514.3 kW (18.82 MMBTU/hr), design pressure 9,756 kPag (1,415 psig), and design temperature 66 deg C. Source: PACKAGE_REGISTER.csv row 62 (Scope) and DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" design table.

### R2 — Package Function

R2.1 The Scope of Work shall describe the package function as heat integration between cold sour inlet separator overhead gas (cold side) and a warm process gas stream (warm side) ahead of inlet compression and downstream molecular-sieve dehydration. Source: PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger".

R2.2 The Scope of Work shall record the warm-side stream identity as **TBD** pending facility heat-integration ruling. The two candidate identities from accessible sources are (a) dehydrated overhead gas from the TEG contactor and (b) warm sweet gas leaving the amine sweetening unit. Source: DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger"; PACKAGE_REGISTER.csv row 62 (Scope). Conflict captured in Guidance.md Conflict Table CT-01.

### R3 — Source Basis

R3.1 The Scope of Work shall cite the DBM-Deepcut source slice "Inlet / TEG Dehy Cross Exchanger" as the design-basis source for process conditions. Source: _REFERENCES.md; DBM-Deepcut.

R3.2 The Scope of Work shall cite 26020-Package_Requirements.docx package heading 7 and Workbook Packages row 62 as the contractual package source basis. Source: PACKAGE_REGISTER.csv row 62 (Source); _REFERENCES.md.

### R4 — Boundaries

R4.1 Package Vendor scope shall include the heat exchanger and its skid-mounted package piping, instrumentation, and skid structure (terminating at skid-edge flanges). Source: PACKAGE_REGISTER.csv row 62 (Responsibility, Scope).

R4.2 EPC Integrator scope shall include all interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration external to the skid. The applicable interface types are: Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. Source: PACKAGE_REGISTER.csv row 62 (Responsibility; Applicable interface types).

R4.3 Package-specific exclusions are not stated in source materials. The Scope of Work shall record this as **TBD** until owner-stated exclusions are obtained. Source: PACKAGE_REGISTER.csv row 62 (Exclusions: "TBD; no package-specific exclusions stated in source materials").

### R5 — Whole-Facility Integration Narrative

R5.1 The narrative shall describe the cold-side flow path: from inlet separator overhead gas (PKG-056 boundary) through E-5718-1 cold side to inlet compressor suction (PKG-048). Source: PACKAGE_REGISTER.csv row 62 (Scope); DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger".

R5.2 The narrative shall describe the warm-side flow path from the (TBD) warm-side source to E-5718-1 warm side and onward to process-gas molecular-sieve inlet filter/coalescers. Source: DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger"; DBM-Deepcut "Interfaces".

R5.3 The narrative shall record that warm-side stream identity must be closed before final P&ID and heat-integration design. Source: DBM-Deepcut "Interfaces".

### R6 — Responsibility Assignment Record

R6.1 The Scope of Work shall include a responsibility assignment record that, at minimum, distinguishes Package Vendor responsibilities (package engineering/design, vendor documentation, equipment supply) from EPC Integrator responsibilities (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). Source: PACKAGE_REGISTER.csv row 62 (Responsibility); _CONTEXT.md (Anticipated Artifacts: "responsibility assignment record").

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| TEMA (Tubular Exchanger Manufacturers Association) — Class R | BEM shell-and-tube heat exchanger configuration is TEMA-classified | location TBD (TEMA standard not in accessible source set; classification stated in PACKAGE_REGISTER.csv row 62 Scope) |
| ASME BPVC Section VIII | ASSUMPTION: applicable to pressure vessel design at 9,756 kPag (1,415 psig). Not explicitly stated in accessible sources; confirm in DEL-052-02 Package Datasheet | location TBD |
| Project documentation register (26020) | Governs package documentation conventions | 26020-Package_Requirements.docx package heading 7 (location TBD; binary) |

## Verification

| Requirement | Verification Method | Verifier |
|---|---|---|
| R1.x — Identity, configuration, design conditions | Document review against PACKAGE_REGISTER.csv row 62 and DBM-Deepcut design table | EPC Integrator (this deliverable); cross-checked in DEL-052-02 Package Datasheet |
| R2.x — Package function and warm-side identity | Document review; warm-side identity ruling logged in MEMORY.md before Datasheet (DEL-052-02) issue | EPC Integrator; Owner ruling required for R2.2 |
| R3.x — Source basis citations | Document review confirming each requirement carries SourcePath + SectionRef or "location TBD" | EPC Integrator |
| R4.x — Boundaries | Cross-check vendor scope split against PACKAGE_REGISTER.csv row 62 and against interface list in DEL-052-02 | EPC Integrator |
| R5.x — Integration narrative | Cross-check against DBM-Deepcut "Inlet / TEG Dehy Cross Exchanger" and "Interfaces" sections | EPC Integrator |
| R6.x — Responsibility assignment record | Presence-check; row coverage for each interface type | EPC Integrator |

## Documentation

The completed Scope of Work shall include, at minimum, the following anticipated artifacts (per _CONTEXT.md):

1. Package scope of work (this document set's normative narrative).
2. Tagged equipment and package identity list (Datasheet.md Identification + Attributes).
3. Package function and integration narrative (Specification R2, R5; Guidance Purpose).
4. Responsibility assignment record (Specification R6; tabulated by interface type).
