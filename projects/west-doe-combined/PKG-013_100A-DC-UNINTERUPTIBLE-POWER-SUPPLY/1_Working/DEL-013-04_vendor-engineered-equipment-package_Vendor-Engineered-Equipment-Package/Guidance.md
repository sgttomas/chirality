# Guidance: DEL-013-04_vendor-engineered-equipment-package

## Purpose

This guidance supports the Package Vendor production unit (engineering, design, fabrication/supply, and physical equipment) for the 100A DC UNINTERUPTIBLE POWER SUPPLY package, `PKG-013`. The deliverable converts the accepted EPC Scope of Work and EPC Package Datasheet into a vendor-engineered package with a defendable design basis and supplied equipment. EPC integration review is performed downstream (`DEL-013-06`).

## Principles

- **Vendor inputs are EPC outputs.** The vendor design starts from `DEL-013-01` (Scope of Work) and `DEL-013-02` (Package Datasheet). The vendor shall not invent package scope outside those inputs.
- **Responsibility split is preserved.** Package engineering, design, vendor documentation, and physical equipment belong to the Package Vendor. Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator.
- **Source-anchored values only.** Where accessible source slices (DBM electrical sections, Gate 7 registers, workbook row 15) define a value or constraint, the vendor design shall reflect it. Where source is silent, values remain `TBD` for vendor data to close — not for invention by drafting.
- **Interfaces drive design, not the reverse.** The four package interfaces (Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports) are inputs to vendor engineering, not items the vendor may redefine.
- **Standby power and integration items remain with the EPC.** The vendor designs for compatibility; transfer-switch configuration, generator sizing, load shedding, sequencing, and TOU standard confirmation are not vendor scope.

## Considerations

- **Service basis.** DBM identifies 120 VAC / 125 VDC UPS services supporting the control system, selected emergency or critical lighting, MV breaker control, and MV protective relays. The "100A DC" in the package name should be treated as package identity/title; specific rating, battery autonomy, and charger/distribution configuration require vendor data.
- **Equipment count.** The DBM equipment list shows two Uninterruptible Power Supply units, but allocation to PKG-013 is not confirmed. The vendor design shall confirm count/rating during package engineering.
- **Vendor package boundary.** The boundary between vendor-supplied internal cable tray/conduit and the EPC site cable tray/conduit shall be defined in the design basis. Maintenance access shall be preserved on both sides.
- **Grounding application.** Major-equipment grounding (two-point ground grid) and CEC-sized separate copper grounding conductors apply where applicable to UPS, distribution transformers, panelboards, and three-phase motors >100 hp. Package-specific applicability is for vendor confirmation.
- **Hazardous-area classification.** Installation location is `TBD`; area classification effects on enclosure ratings, conduit seals, and equipment selection cannot be finalized until EPC confirms the location.

## Trade-offs

- **Standardized vendor packages vs. project-specific engineering.** A standardized 125 VDC UPS unit may simplify supply but require integration adapters (terminations, conduit transitions, grounding tie-ins). Project-specific engineering improves integration fit but extends vendor schedule. The trade-off is a vendor + EPC decision at integration review.
- **Indoor (electrical building) vs. outdoor/skid mounting.** DBM allows electrical buildings to house 120 VAC and 125 VDC UPS systems with battery banks and distribution. Outdoor or skidded options affect environmental ratings, foundations, and grounding approach. Resolution depends on EPC site decisions.
- **Battery technology.** Battery type (e.g., VRLA vs. Ni-Cd vs. Li-ion) affects autonomy, footprint, ventilation, and maintenance. Source is silent; this is a vendor recommendation point.

## Examples

- A vendor 125 VDC UPS production unit including battery bank, charger/rectifier, distribution panel, and a packaged enclosure, supplied with the design basis and datasheet set referenced by Gate 7 artifacts. (ASSUMPTION: representative configuration; actual configuration set by vendor data.)
- A vendor design basis documenting the four interface positions (Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports) and the vendor's response to each at the package boundary.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-013-04-001 | Package title states "100A DC" but accessible sources do not define rating basis, voltage, battery autonomy, or charger/distribution configuration for PKG-013. | Workbook Packages row 15 (package name) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (general 120 VAC / 125 VDC UPS service basis only) | Datasheet attributes; Specification REQ-013-04-004, REQ-013-04-009; Guidance Principles, Considerations | Treat "100A DC" as package identity only and leave detailed UPS parameters `TBD` until vendor data resolves them. | TBD |
| CFL-013-04-002 | DBM equipment list identifies "Uninterruptible Power Supply" quantity 2, but allocation to PKG-013 is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list | Workbook Packages row 15 | Datasheet attributes (UPS count/rating); Specification REQ-013-04-009 | Record UPS count/rating as `TBD` and resolve through vendor data; do not assign quantity to PKG-013 until confirmed. | TBD |
| CFL-013-04-003 | Installation location for the vendor package is unassigned; DBM allows UPS systems in electrical buildings, but no PKG-013-specific assignment exists. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | Gate 7 registers (silent on PKG-013 location) | Datasheet construction; Specification standards (area classification); Guidance Trade-offs | Defer installation location decision to EPC integration; vendor design accommodates both indoor and outdoor options until resolved. | TBD |
