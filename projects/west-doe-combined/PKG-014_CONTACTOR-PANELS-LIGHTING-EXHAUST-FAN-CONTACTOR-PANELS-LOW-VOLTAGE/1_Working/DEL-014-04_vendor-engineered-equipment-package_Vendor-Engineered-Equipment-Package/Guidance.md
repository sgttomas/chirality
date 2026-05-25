# Guidance: DEL-014-04_vendor-engineered-equipment-package

## Purpose

This deliverable exists because `PKG-014` is a vendor-owned Electrical package under WBS 02. The EPC Integrator authors the scope of work and the package datasheet, then hands them off to a Package Vendor that engineers, designs, fabricates, and supplies the physical contactor panel equipment for lighting and exhaust fan low-voltage control. The vendor engineered equipment package is the consolidated production output the EPC Integrator integrates into the facility.

## Principles

- **Two-party responsibility split (per `PACKAGE_REGISTER.csv` row `PKG-014`).** Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
- **EPC inputs are normative.** Vendor engineering is bounded by `DEL-014-01` (Scope of Work) and `DEL-014-02` (Package Datasheet). Vendor decisions that exceed or contradict EPC inputs shall be surfaced for integration review, not silently absorbed.
- **DBM is the electrical service basis.** Low-voltage (600 V HRG) and lighting/utility (120/208 V solid grounded) service definitions in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` set the upstream feeder and service voltage context for the package; the vendor shall not invent alternative service classes.
- **Interface compliance is mandatory.** All seven PKG-014 interfaces from the workbook (Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) shall be addressed by the vendor design.

## Considerations

- The accessible DBM does not enumerate contactor panel counts, ratings, lighting branch allocations, or exhaust fan tag lists for PKG-014. The EPC Package Datasheet (`DEL-014-02`) is the primary normative input that will close these load-list gaps; vendor engineering shall flag any datasheet entries that are still `TBD`.
- Where exhaust fans are powered from a 600 V MCC, DBM Section "600V MCC and Standby Power" requires a local control station adjacent to each motor (H-O-A or On-Off) hard-wired to the starter; the contactor panel design shall not duplicate, override, or omit that station without an EPC-sanctioned deviation.
- Area classification is location-dependent. The vendor shall design enclosures appropriate to the installed area class assigned by the EPC documents; the source slices do not pre-classify panel locations.
- Communications/network exposure (status/monitoring/control) is interface-bearing. Network protocol, addressing, and architecture should not be selected by the vendor in isolation from the EPC control system architecture.

## Trade-offs

- **Vendor-standard panel vs. EPC-tailored panel.** A vendor-standard panel reduces engineering cost and lead time but may force compromises on interface alignment. An EPC-tailored panel improves integration fit but increases vendor engineering effort and schedule risk. EPC Package Datasheet (`DEL-014-02`) and Scope of Work (`DEL-014-01`) drive this choice.
- **Centralized vs. distributed contactor panels.** Centralizing contactor panels in an electrical building simplifies maintenance access and area classification but increases lighting/control branch cabling. Distributing panels nearer to loads shortens branch cabling but multiplies enclosure, area class, and maintenance access burdens.
- **Hardwired vs. networked control.** Hardwired control is simpler and reduces communications interface scope; networked control (status, schedules, monitoring) provides operational benefit but expands the Communications/Network interface and EPC review scope.

## Examples

Source material does not provide PKG-014-specific worked examples. The DBM example most directly applicable is the local-control-station pattern for 600 V MCC motor circuits (H-O-A or On-Off station adjacent to each motor, hard-wired to the starter circuit), which the vendor design shall coordinate with where exhaust fan circuits are MCC-fed.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-014-04-001 | Package title says "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE" but no accessible source slice defines panel counts, ratings, control voltage, lighting branch counts, or exhaust fan circuit counts allocated to PKG-014. | Workbook Packages row 16 (title and discipline) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (general electrical scope, no PKG-014-specific contactor panel content) | Datasheet Attributes; Specification REQ-014-04-06 | Treat panel counts/ratings as `TBD` until EPC Package Datasheet (`DEL-014-02`) is finalized; do not invent values. | TBD |
| CFT-014-04-002 | Lighting and exhaust-fan loads served by PKG-014 are not enumerated in accessible sources. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (electrical buildings/lighting paragraphs) | EPC Package Datasheet (`DEL-014-02`) — content not yet final | Datasheet Attributes (lighting load, exhaust fan loads); Specification REQ-014-04-06 | Carry as `TBD`; resolve from `DEL-014-02` load lists during vendor engineering. | TBD |
| CFT-014-04-003 | Standards/codes governing the vendor package (panelboard, contactor, lighting control product standards; hazardous-area enclosure standards) are not enumerated in accessible source slices. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (no PKG-014-specific standards list) | None accessible | Specification Standards; REQ-014-04-10 | List standards as `location TBD`; vendor proposes a standards basis subject to EPC review. | TBD |
