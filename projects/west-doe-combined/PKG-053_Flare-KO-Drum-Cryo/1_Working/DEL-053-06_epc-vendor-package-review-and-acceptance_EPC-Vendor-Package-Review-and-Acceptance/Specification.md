# Specification — DEL-053-06: EPC Vendor Package Review and Acceptance (Flare KO Drum (Cryo))

## Scope

### In Scope

This specification governs the EPC Integrator's review, integration acceptance, and handoff readiness determination for the Package Vendor's engineered Flare KO Drum (Cryo) package (PKG-053), evaluated against:

- the EPC Scope of Work for the package (DEL-053-01),
- the EPC Package Datasheet (DEL-053-02),
- the EPC Construction Work Package (DEL-053-03),
- the Vendor Engineered Equipment Package (DEL-053-04),
- the Vendor Document Turnover Package (DEL-053-05),

and against facility-level integration interfaces enumerated by PKG-053 (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports). Source: `PACKAGE_REGISTER.csv` PKG-053.

### Out of Scope

- Authoring or modifying vendor design, calculations, or fabrication records (Package Vendor scope, DEL-053-04).
- Issuing vendor turnover documentation (Package Vendor scope, DEL-053-05).
- Authoring the Package Datasheet, Scope of Work, or Construction Work Package (separate PKG-053 deliverables).
- Granting Mechanical Completion or Ready-for-Start-Up certifications (out of agent/EPC-review scope; commissioning authority).

## Requirements

Each requirement has a verification hook in `Procedure.md` Steps section. Source-grounded requirements cite the source slice; inferred requirements are labeled `ASSUMPTION`.

### REQ-053-06-01 — Vendor Document Review Log

The acceptance evidence set SHALL include a complete Vendor Document Review Log covering every submittal listed in the Vendor Document Turnover Package register. Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-053-05.

### REQ-053-06-02 — Package Acceptance Checklist

The acceptance evidence set SHALL include a Package Acceptance Checklist that maps each acceptance line item to (a) the Scope of Work clause it satisfies, (b) the Package Datasheet attribute it confirms, and (c) the Construction Work Package step that depends on it. Source: `_CONTEXT.md` Anticipated Artifacts.

### REQ-053-06-03 — Source-of-Truth Alignment

Acceptance SHALL be evaluated against DEL-053-01 (SoW), DEL-053-02 (Datasheet), and DEL-053-03 (CWP) as the controlling EPC documents. Where vendor documents disagree with EPC source-of-truth deliverables, the EPC documents govern unless a formal change is processed. Source: `DELIVERABLE_REGISTER.csv` DEL-053-06 description.

### REQ-053-06-04 — Cryogenic Service Verification

The acceptance review SHALL verify that the vendor design accommodates relief from molecular-sieve-dehydrated systems and cryogenic-unit reliefs occurring below -45.5 degC, non-sour service. Source: `SCOPE_LEDGER.csv` SOW-0070; `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.

### REQ-053-06-05 — Equipment Identity

The package SHALL be identified to contain cryogenic flare KO drum V-4110-1 and immersion heater H-4112-1. Tag continuity with the EPC tag list SHALL be verified. Source: `SCOPE_LEDGER.csv` SOW-0069; `4-25_Deepcut_DBM.md` §Equipment Schedule row 11.

### REQ-053-06-06 — Relief Header Interface

The acceptance review SHALL verify the 610 mm (24 in) cryogenic relief header inlet connection and the downstream tie-in where cryogenic and HP flare headers combine before the common HP/cryo stack. Source: `4-25_Deepcut_DBM.md` §Flare Equipment and Routing.

### REQ-053-06-07 — Built-up Backpressure Envelope

The acceptance review SHALL confirm that vendor-provided design backpressure values are consistent with the project HP/cryo design basis (preliminary 695 kPag built-up; PSV maximum total backpressure target < 1172 kPag under 150# rating) or that any deviation is documented and accepted. ASSUMPTION: project values remain the design envelope unless detailed-engineering deliverables (DEL-053-02) supersede them. Source: `4-25_Deepcut_DBM.md` §Flare Radiation Criteria preface.

### REQ-053-06-08 — Facility Interface Acceptance

The acceptance review SHALL produce sign-off evidence for each facility-level interface type listed by PKG-053. Source: `PACKAGE_REGISTER.csv` PKG-053.

### REQ-053-06-09 — Test and Inspection Evidence

The acceptance evidence set SHALL include vendor test and inspection records covering hydrostatic/pressure test, NDE, dimensional/PMI as applicable, and any cold-service-specific testing called by the Package Datasheet. Detailed test set: TBD pending DEL-053-02 inspection/test plan. Source: `_CONTEXT.md` Anticipated Artifacts; specific tests TBD.

### REQ-053-06-10 — Turnover Evidence

The acceptance evidence set SHALL include turnover records sufficient for handoff into commissioning per the Construction Work Package turnover checklist. Source: `DELIVERABLE_REGISTER.csv` DEL-053-03; `_CONTEXT.md` Anticipated Artifacts.

### REQ-053-06-11 — Discrepancy / Punchlist Handling

The acceptance review SHALL classify discrepancies as (a) accept, (b) accept with conditions, (c) punchlist for resolution before handoff, or (d) reject for vendor rework, and SHALL document each disposition with reference to the governing source-of-truth clause. ASSUMPTION: standard EPC review practice; not explicitly stated in accessible sources.

### REQ-053-06-12 — Responsibility Boundary Preservation

Package Vendor remains responsible for package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator's acceptance does not transfer vendor warranty/responsibility for vendor scope. Source: `PACKAGE_REGISTER.csv` PKG-053; `_CONTEXT.md` Identity.

## Standards

| Standard / Document | Role | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 8 | Governing package-requirements text for PKG-053 | location TBD (binary source; text not accessible to this draft) |
| Workbook Packages row 53 (`26020-Packages_Interfaces_4_export.xlsx`) | Workbook authority for PKG-053 identity, vendor responsibility, and interfaces | location TBD (binary source) |
| `4-25_Deepcut_DBM.md` | Design Basis Memorandum providing flare system design context including cryogenic flare equipment and routing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| `Bid Docs/Budgetary/brief.md` | Word Source Basis cited by PKG-053 | location TBD (not located in accessible source tree) |
| `24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` | Budgetary pricing/delivery go-by only (NOT a design authority) | `_Sources/...` (location TBD; PDF; go-by reference only) |
| ASME BPVC Section VIII Div. 1/2 (pressure vessel code) | ASSUMPTION: governs design of V-4110-1 as a pressure vessel | not enumerated in accessible sources; verify via DEL-053-02 |
| API 521, API 520, API 526 (flare/relief sizing and PSV) | ASSUMPTION: governing relief-system standards | not enumerated in accessible sources; verify via DEL-053-02 |

Note: Cryogenic service introduces low-temperature material toughness considerations (e.g., impact testing requirements). Specific governing clauses are `TBD` until the package vendor's design code and the EPC Datasheet are read directly.

## Verification

| Requirement | Verification Method | Verification Artifact |
|---|---|---|
| REQ-053-06-01 | Document review against vendor document register | Vendor Document Review Log |
| REQ-053-06-02 | Checklist completion with SoW/Datasheet/CWP traceability columns | Package Acceptance Checklist |
| REQ-053-06-03 | Traceability matrix from vendor docs to DEL-053-01/02/03 | Traceability matrix appendix |
| REQ-053-06-04 | Review of vendor design temperature, MDMT, material, and service classification against -45.5 degC, non-sour basis | Acceptance checklist line; vendor design report excerpt |
| REQ-053-06-05 | Tag-list cross-check against EPC equipment list | Acceptance checklist line; tag list excerpt |
| REQ-053-06-06 | Inspection of vendor P&ID/GA against EPC flare-header tie-in drawing | Acceptance checklist line; redlines if any |
| REQ-053-06-07 | Compare vendor backpressure inputs to project HP/cryo backpressure basis | Acceptance checklist line; calc reference |
| REQ-053-06-08 | Per-interface sign-off sheet | Interface acceptance log |
| REQ-053-06-09 | Review of vendor ITP records, NDE reports, hydrotest charts, MTRs | Test/inspection evidence package |
| REQ-053-06-10 | Construction Work Package turnover-checklist completion | Turnover evidence package |
| REQ-053-06-11 | Disposition column populated for every line in the acceptance checklist | Acceptance checklist; punchlist log |
| REQ-053-06-12 | Statement-of-responsibility appendix; vendor warranty intact | Acceptance Report cover memo |

## Documentation

The deliverable SHALL produce, at minimum, the artifacts listed in `_CONTEXT.md` Anticipated Artifacts:

- Vendor Document Review Log
- Package Acceptance Checklist (with traceability columns)
- Test/Inspection Evidence Package
- Turnover Evidence Package
- Acceptance Report (cover memo summarizing dispositions and any conditions)
- Interface Acceptance Log (per PKG-053 interface types)
- Punchlist Log (if discrepancies are recorded)
