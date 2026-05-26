# Specification — DEL-075-03 Construction Work Package (PKG-075 Cryogenic Unit "Deepcut")

## Scope

This Construction Work Package (CWP) defines how the PKG-075 Cryogenic Unit ("Deepcut") — tag `26020-01-PT-28-001` — shall be physically installed, built, inspected, turned over, and tied into the West Doe Deepcut expansion (facility 04-25) by the EPC Integrator, in coordination with the field-construction owner (Tourmaline Oil Corporation) and the Package Vendor.

In scope:
- Receipt, off-loading, and setting of the cryogenic deep-cut propane-plus recovery package modules and shipped-loose items.
- Mechanical hookup of the package to ISBL/OSBL interfaces enumerated in PACKAGE_REGISTER.csv row 52 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports).
- Installation of shipped-loose instruments, valves, and miscellaneous structural supports per Package Vendor drawings.
- Construction interface management and tie-in coordination with adjacent process blocks (front-end inlet/MPFF/stabilizers, amine, NGL mercaptan treating, VRU, fuel gas, heat medium, flare, drains).
- Mechanical completion, inspection, and turnover to the commissioning organization for SOW-0063 through SOW-0066.

Out of scope (the CWP routes these but does not duplicate them):
- Package vendor's engineering, design, vendor documentation, and physical equipment package (DEL-075-04, DEL-075-05).
- Detailed pipeline design beyond defined tie-ins (`DBM` §Scope Exclusions, line 83).
- Acid-gas disposal pipeline and well design responsibility (`DBM` line 84).
- Existing-facility infrastructure outside defined tie-ins, modifications, or interfaces (`DBM` line 85).

## Requirements

R-1. The CWP SHALL identify every PKG-075 interface enumerated in PACKAGE_REGISTER.csv row 52 and assign a construction responsibility for each tie-in. Tie-ins to ISBL/OSBL points are external interfaces and the responsibility per tie-in SHALL be confirmed (DBM line 117, line 174). [SOURCE: PACKAGE_REGISTER.csv row 52; DBM lines 117, 174]

R-2. Field-construction activities listed in `DBM` "Construction Responsibility" (DBM lines 107–125) SHALL be assigned to the Tourmaline field-construction scope unless explicitly reallocated. [SOURCE: DBM lines 101–127]

R-3. Joint planning between the EPC Integrator, Package Vendor, and Tourmaline construction SHALL be performed for all tie-ins to existing or related facilities, with tie-in timing established progressively. [SOURCE: DBM line 127]

R-4. Shared-utility interfaces (power, fuel gas, instrument air) with facility 03-25 SHALL be coordinated under the shared-utility interface basis. [SOURCE: DBM lines 93–95]

R-5. Construction sequencing SHALL respect the layout and spacing basis of DBM §2, including modular installation access routes, maintainability envelopes, hazardous-area separation, and emergency response access. [SOURCE: DBM line 233, §2.6 line 308–319]

R-6. The CWP SHALL include an installation and tie-in workface plan (per the anticipated artifacts list). [SOURCE: _CONTEXT.md "Anticipated Artifacts"; DELIVERABLE_REGISTER.csv row 278 ArtifactsAnticipated column]

R-7. The CWP SHALL include a construction interface and turnover checklist covering mechanical completion, inspection sign-offs, punch-list closure, and handover of records to commissioning. [SOURCE: _CONTEXT.md "Anticipated Artifacts"; DELIVERABLE_REGISTER.csv row 278]

R-8. The CWP SHALL state inspection, NDE, and testing requirements for the package mechanical hookup. [ASSUMPTION — typical EPC CWP content; specific NDE/test acceptance values: location TBD pending access to 26020-Package_Requirements.docx package heading 29]

R-9. The CWP SHALL state the records set required at turnover (weld maps, NDE reports, hydrotest records, instrument loop-check records, electrical termination records, punch lists). [ASSUMPTION — typical EPC CWP content; specific record list: location TBD pending source access]

R-10. All construction activities SHALL be executed under the project's HSE, permit-to-work, and quality program. [ASSUMPTION — project-level governance not localized in DBM; location TBD]

## Standards

| Standard / Basis | Applicability | Source / Location |
|---|---|---|
| West Doe Deepcut DBM (4-25_Deepcut_DBM.md) | Governing design basis for facility 04-25; defines construction responsibility and interface basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| 26020-Package_Requirements.docx, package heading 29 | Authoritative package requirements for PKG-075 | location TBD (docx not locally accessible as text) |
| CSA Z662 / ASME B31.3 / applicable provincial pressure-vessel code | Piping and pressure equipment construction and testing | TBD — not enumerated in accessible sources |
| Owner construction, HSE, and QA/QC procedures | Field execution governance | TBD — not enumerated in accessible sources |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1, R-3 | Review tie-in register against PACKAGE_REGISTER.csv row 52; confirm per-tie-in responsibility entries are signed by EPC and Tourmaline. |
| R-2 | Cross-check construction work breakdown against DBM "Construction Responsibility" table (lines 107–125). |
| R-4 | Review shared-utility interface package signed by 03-25 and 04-25 representatives. |
| R-5 | Review constructability/access study against DBM §2 layout basis. |
| R-6, R-7 | Inspect deliverable folder for the installation/workface plan and turnover checklist artifacts. |
| R-8, R-9 | TBD — verification criteria depend on resolved package source slice. |
| R-10 | Confirm reference to project HSE/PTW/QA procedures; TBD on specific procedure IDs. |

## Documentation

Required artifacts (from `_CONTEXT.md` and DELIVERABLE_REGISTER.csv row 278):

- Construction Work Package (this deliverable's primary artifact).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Supporting artifacts (typical EPC CWP content, ASSUMPTION — confirm against 26020-Package_Requirements.docx heading 29):
- Tie-in register / isolation matrix.
- Inspection and Test Plan (ITP).
- NDE schedule and acceptance criteria.
- Hydrotest / leak-test packs.
- Mechanical completion (MC) walkdown punch list.
- Turnover record set (weld maps, NDE reports, calibration certs, loop checks).
