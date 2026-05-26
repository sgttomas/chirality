# Specification — DEL-077-04 Vendor Engineered Equipment Package

## Scope

This specification governs the **Vendor Engineered Equipment Package** for the Methanol Injection package (PKG-077, WBS 01, Workbook row 72, CoA 26020-01-29-002). It defines the requirements the **Package Vendor** must meet to deliver:

1. Package engineering and design,
2. Fabrication and/or supply of the physical equipment package, and
3. The vendor package design basis and datasheet set.

The deliverable is anchored by, and must be developed from, the EPC Integrator's **Scope of Work (DEL-077-01)** and **Package Datasheet (DEL-077-02)**. Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration — is **out of scope** for the vendor and remains with the EPC Integrator. [Source: `PACKAGE_REGISTER.csv` row 72; `DELIVERABLE_REGISTER.csv` row 399]

**Exclusions:** Facility-level integration, tie-in design, construction execution, and EPC vendor package review/acceptance (the latter is DEL-077-06). TBD: no package-specific exclusions are stated in the source materials beyond the responsibility split [Source: `PACKAGE_REGISTER.csv` row 72 "Exclusions" field = "TBD; no package-specific exclusions stated in source materials."].

## Requirements

### R1. Engineering Authorship
The Package Vendor SHALL author the package engineering deliverables, including the vendor package design basis and datasheet set. [Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 399; `PACKAGE_REGISTER.csv` row 72]

### R2. Design Conformance to EPC Anchors
The vendor design SHALL conform to the requirements expressed in the EPC Scope of Work (DEL-077-01) and the EPC Package Datasheet (DEL-077-02). [Source: `DELIVERABLE_REGISTER.csv` row 399 Notes]

### R3. Coverage of Scope Item
The package SHALL satisfy `SOW-0143`. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 399]

### R4. Physical Equipment Delivery
The vendor SHALL fabricate/supply the physical equipment package. [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row 399]

### R5. Interface Compatibility
The package SHALL be engineered to support, at each defined battery-limit boundary, the interface types declared for PKG-077: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. Detailed interface requirements are carried in the EPC Package Datasheet interface requirements matrix (DEL-077-02 evidence). [Source: `PACKAGE_REGISTER.csv` row 72; `INTERFACE_REGISTER.csv` rows 574-586; `ARTIFACT_REGISTER.csv` rows 4273-4277+]

### R6. Process Service
The package SHALL serve "Methanol Injection" service. Process conditions (flowrates, pressures, temperatures, methanol concentration, operating cases) are TBD until the source slice is locally extracted from the EPC Package Datasheet (DEL-077-02) and the underlying workbook (Workbook Packages row 72). [Source: `PACKAGE_REGISTER.csv` row 72; deeper process slice location TBD]

### R7. Integration Acceptance Readiness
Vendor deliverables SHALL be sufficient to enable EPC Integrator vendor package review and acceptance (DEL-077-06). [Source: `DELIVERABLE_REGISTER.csv` row 401]

### R8. Vendor Documentation Set
The vendor SHALL deliver the **vendor package design basis and datasheet set** as one of the two anticipated artifacts. [Source: `_CONTEXT.md` Anticipated Artifacts]

### R9. Compliance with Gate 6 Scope Disposition
ASSUMPTION: The vendor SHALL coordinate with the Cryogenic Unit package scope per the Gate 6 disposition that "Methanol Injection scope is included with the Cryogenic Unit package scope." Operational meaning at the vendor-package level is TBD. [Source: `PACKAGE_REGISTER.csv` row 72 Notes]

## Standards

| Standard / Code Family | Applicability | Locally Accessible? |
|---|---|---|
| Mechanical discipline standards governing methanol-service packages (e.g., piping, vessel, instrumentation codes typical to methanol injection skids) | ASSUMPTION: likely applicable based on Discipline=Mechanical and Methanol service | TBD — no specific standards enumerated in the deliverable's accessible reference set |
| Project-level design basis manuals (`DBM-Comp_and_Liquids`, `DBM-Deepcut`) | ASSUMPTION: likely applicable as project-level design basis | location TBD (present in `_Sources/` but not extracted as deliverable-local slices) |
| Workbook Package Requirements (`26020-Package_Requirements.docx`) | ASSUMPTION: likely applicable to all PKG-* deliverables | location TBD (present in `_Sources/` but not extracted as deliverable-local slices) |

Specific clause-level requirements cannot be derived without locally accessible source slices.

## Verification

| Requirement | Verification Method | Verification Owner |
|---|---|---|
| R1 | Document review of vendor design basis and datasheet set | EPC Integrator (DEL-077-06) |
| R2 | Traceability check: vendor design ↔ DEL-077-01 + DEL-077-02 | EPC Integrator |
| R3 | Scope coverage check against SOW-0143 | EPC Integrator |
| R4 | Factory acceptance test (FAT) / inspection of physical package (TBD — specific FAT scope) | Package Vendor with EPC Integrator witness (ASSUMPTION) |
| R5 | Interface requirements matrix verification against PKG-077 declared interfaces | EPC Integrator |
| R6 | Process design review against EPC Package Datasheet (TBD pending source extraction) | EPC Integrator |
| R7 | Acceptance package completeness check (DEL-077-06) | EPC Integrator |
| R8 | Vendor document register reconciliation (cross-checked in DEL-077-05) | EPC Integrator |
| R9 | Coordination evidence with Cryogenic Unit package scope (TBD) | EPC Integrator |

## Documentation

Required vendor-produced artifacts (from `_CONTEXT.md` Anticipated Artifacts and `DELIVERABLE_REGISTER.csv` row 399):

- Vendor engineered physical equipment package (the equipment itself, with vendor-issued certifications)
- Vendor package design basis and datasheet set

Companion vendor documentation (vendor document register, submittals, turnover records) is carried in DEL-077-05 (Vendor Document Turnover Package). [Source: `DELIVERABLE_REGISTER.csv` row 400]
