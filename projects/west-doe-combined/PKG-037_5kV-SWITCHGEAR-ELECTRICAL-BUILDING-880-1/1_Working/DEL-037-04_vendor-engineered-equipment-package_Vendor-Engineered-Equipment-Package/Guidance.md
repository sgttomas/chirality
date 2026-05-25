# Guidance: DEL-037-04_vendor-engineered-equipment-package

## Purpose

This guidance supports development and review of the **Vendor Engineered Equipment Package** for `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`.

The deliverable exists so the Package Vendor can convert the EPC Scope of Work (`DEL-037-01`) and Package Datasheet (`DEL-037-02`) into the engineered, fabricated / supplied electrical building package and its supporting vendor design basis and datasheet set. Gate 7 decomposition assigns package engineering, package design, vendor documentation, and the physical package to the Package Vendor, with EPC Integrator review for facility interfaces and integration.

Primary evidence sources:

- `_CONTEXT.md`, deliverable identity and scope.
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `ARTIFACT_REGISTER.csv`, rows `ART-7491C7E69C` and `ART-8870C8E2DE`.
- `INTERFACE_REGISTER.csv`, rows `IFC-524BC4670F` through `IFC-8012069CE2` for `PKG-037`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis sections for electrical buildings, medium-voltage services, UPS services, grounding and bonding, cable tray, conduit, and medium-voltage cables.

## Principles

1. Treat the Gate 7 PROJECT_DECOMP snapshot as the accepted package / deliverable basis. Do not replace it with a regenerated or derivative package.
2. Keep ownership explicit: the Package Vendor owns package engineering, package design, vendor documentation, and physical equipment supply; the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration (`PACKAGE_REGISTER.csv` row `PKG-037`).
3. Use source-supported electrical-building requirements first. The DBM states that electrical buildings shall be prefabricated, modular buildings located in general-purpose areas and shall house the equipment subset required by detailed design (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph).
4. Preserve the workbook title "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)" as the package identity. Treat any mapping from "5kV" to a specific facility service voltage as an **ASSUMPTION** unless a later source or human ruling confirms it.
5. Carry all twelve `PKG-037` interface facts into vendor design review because the workbook marks them applicable to the package (`INTERFACE_REGISTER.csv` rows for `PKG-037`).
6. Prefer `TBD` over invented values for bus rating, breaker count, relay scheme, building location, foundation basis, HVAC loads, fire and gas details, and package-specific vendor requirements not present in accessible source slices.

## Considerations

### Voltage and Equipment Basis

The DBM electrical voltage and service table defines medium-voltage services at 13.8 kV, 6.9 kV, and 4.160 kV, all 3-phase, 3-wire, 60 Hz, low-resistance grounded. The package title uses "5kV"; this is consistent with a possible 5 kV insulation class, but the accessible sources do not explicitly assign building 880-1 to 4.160 kV service. Reviewers should keep this as a human ruling item until the EPC Package Datasheet or vendor design basis confirms the service voltage.

### Electrical Building Scope

The DBM electrical buildings paragraph lists possible contents of electrical buildings, including 13.8 kV main switchgear, medium-voltage motor control centers, reduced-voltage soft starters, medium-voltage VFDs, 600 V MCCs, UPS systems, transformers, panelboards, contactor panels, plant PLC control panels, and network racks. For `PKG-037`, the vendor package should include only the building-specific subset required by detailed design. Do not assume that every listed DBM equipment type is present in 880-1.

### Interfaces

The vendor package should be reviewed against the twelve `PKG-037` interface types:

- Utility Piping
- Drain / Containment
- Electrical Power
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Communications / Network
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Grading / Site Drainage / Spill Containment
- Structural / Foundations / Supports

These are interface facts, not standalone deliverables. They should be expressed in the package interface requirements matrix and reviewed by the EPC Integrator during vendor package acceptance.

### Installation and Maintenance Constraints

The DBM states that cable tray routing shall not interfere with maintenance access and that conduit shall not interfere with maintenance access (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs). It also states that electrical buildings shall use bottom entry of incoming and outgoing power cables, be elevated and installed on piles to provide space beneath the building, and include equipment doors sized or arranged to remove the largest equipment. These points should influence vendor general arrangement and interface reviews.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Early vendor definition vs. detailed design maturity | The vendor needs enough information to engineer the building, but bus ratings, equipment lineup, relay schemes, and foundation data remain `TBD` in accessible sources. | Use the EPC Package Datasheet and SOW as the handoff basis; keep missing values explicit as `TBD` until detailed design or vendor documents close them. |
| Package Vendor ownership vs. EPC Integrator integration | The vendor owns the package; the EPC Integrator owns integration into the facility. | Keep package-contained requirements in this deliverable and route facility tie-ins / acceptance to `DEL-037-06`. |
| Workbook interface facts vs. source detail | The workbook marks interface types, but does not provide full technical criteria for each one. | Carry interface facts as required review topics, then cite DBM only where it provides technical support such as grounding, cabling, maintenance access, and electrical-building arrangement. |
| 5kV package label vs. DBM voltage table | The package title uses "5kV"; DBM service table lists 4.160 kV for certain process AC inverter-drive motors. | Do not hard-code the mapping without a human ruling or later source; mark as **ASSUMPTION**. |

## Examples

The accessible source set does not provide a package-specific example vendor design basis for building 880-1. The following are evidence-backed examples of review checks, not source-declared package values:

- Confirm the vendor general arrangement reflects a prefabricated, modular electrical building in a general-purpose area (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph).
- Confirm medium-voltage cable selections use the DBM cable basis where applicable: 6.9 kV cables as three-conductor copper TECK rated 8 kV with 100 percent insulation and shielded, and 4.160 kV cables as three-conductor copper TECK rated 5 kV with 100 percent insulation (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable table).
- Confirm major electrical equipment grounding and building ground wells are addressed (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-037-04-01 | Package title says "5kV", but accessible DBM voltage table does not explicitly assign building 880-1 to a specific service voltage. | Workbook Packages row 39 / `PACKAGE_REGISTER.csv` row `PKG-037` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table | Datasheet Attributes; Specification R-037-04-04; Procedure verification | Treat "5kV" as package title / likely insulation class and require EPC or vendor confirmation before using it as a facility service voltage. | TBD |
