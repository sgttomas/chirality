# Specification — DEL-101-03 Construction Work Package (PKG-101 Precast Concrete Foundations)

## Scope

This specification governs the EPC Integrator's Construction Work Package (CWP) for PKG-101 (Precast concrete foundations). The CWP shall describe how the precast-concrete foundation scope of PKG-101 is physically installed, built, inspected, turned over, and tied into the larger facility systems (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER row DEL-101-03).

**Included** (anticipated artifacts per `ARTIFACT_REGISTER.csv`):

1. Construction work package (ART-384DBDF766) — installation/construction/tie-in narrative.
2. Installation and tie-in workface plan (ART-674B3EBE60) — workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable.
3. Construction interface and turnover checklist (ART-37A6123862) — construction-facing interface, tie-in, inspection, and turnover evidence for the approved package.

**Excluded**:

- Vendor-package engineering and design handoff content (carried by DEL-101-02 Package Datasheet).
- Package scope/identity/integration narrative (carried by DEL-101-01 Scope of Work).
- Detailed discipline production package content (carried by DEL-101-04).
- Final geotechnical design parameters (external dependency; see Standards/External Dependencies below).

## Requirements

| Req ID | Requirement | Source / Provenance | Label |
|---|---|---|---|
| R-101-03-01 | The CWP shall be authored by the EPC Integrator for PKG-101 | `_CONTEXT.md` ResponsibleParty; DELIVERABLE_REGISTER row DEL-101-03 | FACT |
| R-101-03-02 | The CWP shall cover physical installation, construction, inspection, turnover, and tie-in to larger facility systems | `_CONTEXT.md` Scope; ARTIFACT_REGISTER ART-384DBDF766 description | FACT |
| R-101-03-03 | The CWP shall include an installation and tie-in workface plan covering adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable | ARTIFACT_REGISTER ART-674B3EBE60 description | FACT |
| R-101-03-04 | The CWP shall include a construction interface and turnover checklist for the approved package | ARTIFACT_REGISTER ART-37A6123862 description | FACT |
| R-101-03-05 | Tie-in workface planning shall address the workbook-declared PKG-101 interfaces: Grading / Site Drainage / Spill Containment (IFC-26343B703C) and Structural / Foundations / Supports (IFC-BED3DE4194) | `INTERFACE_REGISTER.csv` lines 905-906 | FACT |
| R-101-03-06 | Foundation installation shall use the default support basis of driven steel piles unless a more specific foundation basis is declared (e.g., precast concrete bearing foundations for transformers; precast concrete blocks on driven steel piles for compressors) or detailed engineering confirms a different requirement | DBM-Deepcut SEC-11 §Piles and Foundations | FACT |
| R-101-03-07 | Where compressors are supported on precast concrete blocks on driven steel piles, installation shall not be released for service prior to acceptance of the compressor dynamic analysis | DBM-Deepcut SEC-11 §Piles and Foundations; §Assumptions/TBDs ("Compressor foundation dynamic analysis results are TBD") | ASSUMPTION (best-effort: installation gating inferred from dynamic-analysis prerequisite) |
| R-101-03-08 | Compressor skid/foundation construction shall implement containment and management provisions for on-skid oil leaks per the issued detailed arrangement | DBM-Deepcut SEC-11 §Piles and Foundations table | FACT (requirement); detailed arrangement TBD |
| R-101-03-09 | Final pile design parameters and foundation closure shall not be set as construction criteria until the final geotechnical report is accepted | DBM-Comp_and_Liquids §Civil/Structural line 141; DBM-Deepcut SEC-11 §External Dependencies | FACT |
| R-101-03-10 | Construction shall comply with the -40 deg C minimum-ambient site basis for exposed work, materials handling, concrete placement temperature controls, and equipment exposure | DBM-Comp_and_Liquids §Site basis line 145 | FACT (basis); concrete cold-weather method statement TBD |
| R-101-03-11 | Structural and foundation engineering applied during construction shall align with the latest applicable editions of the codes listed in DBM-Deepcut SEC-11 §Governing Codes (including the Canadian Foundation Engineering Manual and the National Building Code of Canada) | DBM-Deepcut SEC-11 §Governing Codes table; §Buildings | FACT |

Per-tag installation sequences, lift plans, anchor schedules, embed details, concrete mix designs, grout specifications, survey tolerances, and inspection acceptance criteria are **TBD** pending issue-for-construction discipline engineering and the accepted geotechnical report. The CWP shall not invent these values; it shall reference the upstream issued drawings and specifications when they become available.

## Standards

| Standard / Reference | Applies To | Location |
|---|---|---|
| National Building Code of Canada (current edition) | Building snow/rain/wind/seismic loading; egress | DBM-Deepcut SEC-11 §Buildings |
| Canadian Foundation Engineering Manual | Foundation engineering basis | DBM-Deepcut SEC-11 §Governing Codes table |
| Project geotechnical assessment report | Bearing capacity, lateral pile design, LPILE curves, dynamic design criteria | DBM-Deepcut SEC-11 §External Dependencies — TBD pending report completion |
| 26020-Package_Requirements.docx | Package requirements basis | `_Sources/`; clause-level location TBD (binary; not extracted in this pass) |
| 26020-Packages_Interfaces_4_export.xlsx, row 102 | Package row of record | `_Sources/`; row content location TBD (binary; not extracted in this pass) |

## Verification

| Verifies | Method | Evidence |
|---|---|---|
| R-101-03-02, R-101-03-03, R-101-03-04 | Document review of CWP, workface plan, and turnover checklist against artifact descriptions | CWP package as issued |
| R-101-03-05 | Cross-check of workface plan tie-in scope against PKG-101 interface register rows | INTERFACE_REGISTER.csv lines 905-906; turnover checklist sign-off |
| R-101-03-06, R-101-03-08 | Field inspection against issued foundation drawings and specifications | Inspection and Test Plan records — TBD until ITP issued |
| R-101-03-07 | Hold-point release tied to acceptance of compressor dynamic analysis | Engineering acceptance record — TBD |
| R-101-03-09 | Hold-point release tied to acceptance of geotechnical report | Geotechnical acceptance record — TBD |
| R-101-03-10 | Cold-weather concrete placement method statement and temperature records | Method statement / placement records — TBD |
| R-101-03-11 | Code-compliance review against current-edition references | Engineering certification records — TBD |

## Documentation

The deliverable shall produce, at minimum, the three anticipated artifacts (CWP, workface plan, turnover checklist) per `ARTIFACT_REGISTER.csv` rows for DEL-101-03. Supporting registers, ITPs, method statements, and inspection records are anticipated but are not enumerated in the locally accessible sources and are carried as TBD.
