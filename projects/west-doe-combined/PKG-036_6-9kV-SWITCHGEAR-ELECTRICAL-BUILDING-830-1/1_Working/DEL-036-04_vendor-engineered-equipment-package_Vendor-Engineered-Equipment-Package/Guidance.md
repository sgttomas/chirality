# Guidance: DEL-036-04_vendor-engineered-equipment-package

## Purpose

PKG-036 is the facility's 6.9 kV switchgear electrical building package. The vendor production unit (`DEL-036-04`) exists to convert the EPC-defined scope and datasheet (`DEL-036-01`, `DEL-036-02`) into a buildable, testable, and integrable engineered electrical package: a prefabricated electrical building, the 6.9 kV switchgear (and associated MV equipment as defined by the EPC Package Datasheet), and the vendor design basis and datasheet set that document how the package will be built, controlled, grounded, ventilated, and integrated. The vendor production unit is the bridge between the EPC scope/datasheet and the construction, document-turnover, and acceptance deliverables (`DEL-036-03`, `DEL-036-05`, `DEL-036-06`).

## Principles

- **EPC drives, vendor delivers.** The EPC Scope of Work and EPC Package Datasheet are the authoritative inputs. The vendor production unit may not silently override or expand those inputs; mismatches must be raised through the EPC Vendor Package Review and Acceptance deliverable (`DEL-036-06`).
- **Source fidelity.** Where the DBM gives an explicit electrical-design value (voltage, grounding, cable rating, HVAC redundancy, cable entry), the vendor design must respect it. Where the DBM is silent, values stay TBD until the EPC Package Datasheet supplies them.
- **Responsibility separation is structural.** Anything that is facility integration (tie-ins, constructability, procurement/construction coordination, facility-level integration) belongs to the EPC Integrator, not the vendor, even when the vendor has the better technical view.
- **Interface set is fixed.** All twelve PKG-036 interface types in `INTERFACE_REGISTER.csv` are in scope as package-side counterparts; the vendor cannot drop any of them without an explicit ruling.

## Considerations

- **MV switchgear vs. MCC scope.** The DBM gives explicit construction direction for the 6.9 kV MCC (mechanically latched fused contactors, motor protection relays, Ethernet to plant PLC) but does not give equivalent construction direction for the 6.9 kV switchgear. Treat MCC text as informative analogue (e.g., Ethernet integration) and label as ASSUMPTION for switchgear (REQ-036-04-009) until the EPC Package Datasheet confirms.
- **Building number ambiguity.** The package name carries "(830-1)", but the DBM equipment list assigns 830-1 to 4.16 kV (acid gas/overheads compressor electrical building) and 820-1 to the 6.9 kV (inlet/sales compressor electrical building). This must be reconciled before vendor design freeze; see CT-036-04-001.
- **MV switchgear count.** The DBM equipment list records exactly one "Medium Voltage Switchgear" for the facility, while the package universe contains multiple medium-voltage electrical buildings (13.8 kV, 6.9 kV, 4.16 kV). The single MV switchgear allocation across packages should be confirmed by the EPC Package Datasheet; do not assume the entire MV switchgear count belongs to PKG-036.
- **Modular shop build.** The DBM equipment list rows for the electrical buildings are marked "Shop", which is consistent with a prefabricated, factory-built vendor production unit; the vendor design basis should align fabrication and shipping strategy accordingly.

## Trade-offs

- **More vendor scope vs. cleaner EPC integration.** The vendor can offer pre-integrated MV switchgear, transformers, MCCs, UPS, and panels in the same building, which reduces field integration risk but increases dependency on a single vendor and raises early-stage cost and lead time. The EPC Package Datasheet decides this scope split; the vendor production unit must follow it.
- **Building cable entry strategy.** Bottom entry (DBM-mandated) constrains site civil layout, pile spacing, and cable tray geometry under the building, but simplifies cable terminations inside the building and supports maintenance access.
- **HVAC n + 1 sizing.** Increases footprint and capital cost relative to n + 0, but matches DBM availability expectations for medium-voltage electrical buildings.

## Examples

- The DBM "Electrical Buildings" section (line 2973) enumerates services that an electrical building "shall house, as required by detailed design"; PKG-036 selects a subset (6.9 kV switchgear and supporting equipment) per the EPC Package Datasheet rather than housing every listed service.
- The MV transformer grounding example (100 A, 10 s NGR, tripping) is reused as the upstream grounding condition for the vendor's 6.9 kV switchgear protection coordination.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-036-04-001 | Package name combines "6.9kV SWITCHGEAR ELECTRICAL BUILDING" with building number "830-1", but the DBM equipment list assigns 830-1 to a 4.16 kV building (line 2813) and 820-1 to the 6.9 kV building (line 2812). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 2811-2816 | `PACKAGE_REGISTER.csv` row `PKG-036`; Workbook Packages row 38 | Datasheet Attributes (Building 830-1 designation), Specification REQ-036-04-014, vendor design freeze | PROPOSAL: Treat "6.9 kV" as authoritative for vendor service rating and treat "830-1" as a project tag whose voltage assignment must be reconciled at gate review; do not change vendor MV rating from 6.9 kV. | TBD |
| CT-036-04-002 | DBM gives explicit Ethernet-to-plant-PLC and protection-relay direction for the 6.9 kV MCC (line 2955) but no equivalent direction for the 6.9 kV switchgear. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2955 | (no opposing source) | Specification REQ-036-04-009, Procedure verification | PROPOSAL: Extend MCC convention to switchgear as ASSUMPTION until the EPC Package Datasheet confirms; do not finalize protection/communication architecture without `DEL-036-02`. | TBD |
| CT-036-04-003 | DBM equipment list records one (1) Medium Voltage Switchgear for the entire facility (line 2880), but multiple PKG IDs (e.g., 13.8 kV, 6.9 kV, 4.16 kV buildings) imply MV switchgear in more than one package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2880 | `PACKAGE_REGISTER.csv` rows for 13.8/6.9/4.16 kV building packages | Datasheet Attributes (Switchgear quantity reference), vendor count/rating sizing | PROPOSAL: Do not assume the single facility MV switchgear count belongs entirely to PKG-036; defer count and rating allocation to the EPC Package Datasheet (`DEL-036-02`). | TBD |
