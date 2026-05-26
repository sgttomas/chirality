# Specification — DEL-096-03 Construction Work Package (PKG-096 Tanks, Sour Condensate API 650)

> Normative document. Requirements are derived from authoritative source slices. Inferences are labeled **ASSUMPTION**; unknowns are `TBD`.

## Scope

### In Scope (EPC Integrator construction surface)

The Construction Work Package defines how PKG-096 (two 3800 bbl sour condensate storage tanks TK-9110-2 and TK-9120-2, design to modified API 650, sour service NACE-compliant) is physically installed, built, inspected, turned over, and tied into the larger facility. (Source: `_CONTEXT.md`; `26020-Package_Requirements.docx` H1 #48.)

Specifically covered:

- Foundation construction and tank mounting at site (source-stated as "By Others" of vendor scope, therefore EPC scope). [`26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items]
- Field electrical and instrumentation installation supporting the tanks. [Source: same slice.]
- Platforms and staircase installation. [Source: same slice.]
- Construction of applicable physical interfaces: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. [`26020-Package_Requirements.docx` H1 #48, Physical Interface Summary.]
- Inspection, testing, and turnover of the installed package to operations.

### Out of Scope

- Tank package engineering, design, vendor documentation, and the physical equipment package itself (owned by Package Vendor). [Source: `PACKAGE_REGISTER.csv` row PKG-096.]
- Interfaces marked "No" in source: Utility Piping; Electrical Power (high-voltage feeder design); EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging. [`26020-Package_Requirements.docx` H1 #48, Physical Interface Summary.]

## Requirements

| Req ID | Requirement | Source / Basis | Label |
|---|---|---|---|
| R-096-03-01 | Construction work package SHALL deliver: (a) construction work package document, (b) installation and tie-in workface plan, (c) construction interface and turnover checklist. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-096-03 | FACT |
| R-096-03-02 | Installed tanks SHALL be configured for sour service (H2S present) and NACE compliance maintained through field work (no carbon contamination, no unapproved repairs, weld map per vendor). | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment | FACT (verbatim service class) |
| R-096-03-03 | Internal coating system Devchem 253 on floors, walls, roofs SHALL be preserved during installation; field touch-up procedures SHALL be approved by vendor. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment | FACT (coating) + ASSUMPTION (touch-up procedure rule) |
| R-096-03-04 | Foundation works SHALL support two 3800 bbl tanks within the design pressure (32 oz test) and design temperature (-40 °C to 60 °C) envelope. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment + Scope Notes | FACT (values) |
| R-096-03-05 | Blanket gas system SHALL be installed per API 2000. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment | FACT |
| R-096-03-06 | Each tank's PVRV, EPRV, and VRU header connection SHALL be tied into the facility relief / flare / vent system. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment + Physical Interface Summary (Relief/Flare/Vent = Yes) | FACT |
| R-096-03-07 | Maximum-fill 90% shutdown instrumentation SHALL be installed, tested, and proven functional before turnover. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment (Fill Limit) | FACT (limit) + ASSUMPTION (test-before-turnover) |
| R-096-03-08 | Process piping tie-ins SHALL accommodate design flows (Item 1: 27,606 kg/h / 919 Am3/d; Item 2: 94,940 kg/h / 3187 Am3/d) such that plant design capacity can fill a single tank. | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment + Scope Notes | FACT |
| R-096-03-09 | Grounding/Bonding and Cathodic Protection installations SHALL be tied to the facility systems consistent with the package's interface applicability. | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary | FACT (applicability) |
| R-096-03-10 | I&C / Control Cabling SHALL be routed and terminated to the facility control system; loop checks SHALL be witnessed prior to turnover. | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary + ASSUMPTION (witnessed loop-check practice) | FACT + ASSUMPTION |
| R-096-03-11 | Grading / Site Drainage / Spill Containment around tanks SHALL be constructed consistent with sour-service containment requirements. | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary | FACT (applicability); details TBD |
| R-096-03-12 | Area / Exterior Lighting around the tank pad SHALL be installed per facility lighting plan (interface applicability per `26020-Packages_Interfaces.3.xlsx` col M row 92). | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary | FACT (applicability); plan TBD |
| R-096-03-13 | A construction interface and turnover checklist SHALL be produced and signed for each of the nine applicable interface types. | `_CONTEXT.md` anticipated artifacts; interface list per source | FACT |
| R-096-03-14 | Installation and tie-in workface plan SHALL declare prerequisites, sequencing, hold points, and required inspection records. | ASSUMPTION (standard workface planning practice; specific contents TBD from project execution standards) | ASSUMPTION |

## Standards

| Standard | Application | Locally accessible? |
|---|---|---|
| API 650 (modified) | Tank design & fabrication; field-erection inspections must respect modifications stated by vendor. | No — **location TBD**. |
| API 2000 | Blanket gas / venting system installation. | No — **location TBD**. |
| NACE sour-service standards (likely MR0175 family) | Sour service compatibility through field work. | ASSUMPTION; **location TBD**. |
| Project execution / construction QA standards | Workface planning, hold points, ITR/turnover protocol. | TBD — not declared in source slice read. |

## Verification

| Req | Verification Approach |
|---|---|
| R-096-03-01 | Document inventory check at deliverable acceptance. |
| R-096-03-02 | Material certs review (NACE); welder qualifications; weld map; NDE per ITP. |
| R-096-03-03 | Coating holiday test, DFT measurement, vendor sign-off on field touch-up. |
| R-096-03-04 | Foundation geotechnical sign-off; survey; load calculations review. |
| R-096-03-05 | Blanket gas system commissioning per API 2000 checklist; leak test. |
| R-096-03-06 | Relief / flare tie-in pressure test; PVRV/EPRV bench-test certs reviewed; VRU header continuity confirmed. |
| R-096-03-07 | High-level shutdown loop check; functional test record. |
| R-096-03-08 | Hydrotest / pressure test packages (vendor deliverable PIP-024) reviewed; flow path validated. |
| R-096-03-09 | Bonding continuity test; CP system commissioning record. |
| R-096-03-10 | I&C loop check records; control-system point-to-point verification. |
| R-096-03-11 | Containment volume calculation; drainage as-built review. |
| R-096-03-12 | Lighting lux survey; energization record. |
| R-096-03-13 | Signed interface turnover checklist (9 interfaces). |
| R-096-03-14 | Workface plan reviewed and approved before construction start. |

## Documentation (artifacts produced under this deliverable)

- `ConstructionWorkPackage.pdf` (or equivalent) — the bound construction work package — **filename TBD**.
- `InstallationAndTieInWorkfacePlan` — **filename TBD**.
- `ConstructionInterfaceAndTurnoverChecklist` — **filename TBD**.
- Supporting inspection and test records (ITRs), hold-point sign-offs, vendor IOM acceptance — **scope TBD pending project execution standard**.
