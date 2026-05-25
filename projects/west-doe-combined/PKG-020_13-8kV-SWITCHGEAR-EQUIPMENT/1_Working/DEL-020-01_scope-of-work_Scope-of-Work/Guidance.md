# Guidance: DEL-020-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-020 (`13.8kV SWITCHGEAR EQUIPMENT`) before downstream Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover Package, and EPC Vendor Package Review and Acceptance work proceeds.

The source basis is intentionally narrow. Workbook row 22 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split; the DBM Deepcut Power System and Electrical Buildings sections describe the 13.8 kV switchgear as the plant main power distribution center, fed by a 25 kV / 13.8 kV / 50 MVA utility-supplied transformer downstream of the BC Hydro 25 kV utility supply, and feeding radially to the named medium- and low-voltage electrical buildings. Package-specific switchgear design details (bus, breaker, BIL, protection, arc-flash, lineup arrangement, dimensions, weights, environmental rating) remain `TBD` unless later source material provides them.

## Principles

- Preserve the accepted package name `13.8kV SWITCHGEAR EQUIPMENT` because it is the Gate 7 / workbook spelling.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering, design, vendor documentation, equipment supply) separate from EPC Integrator responsibilities (integration, interfaces, tie-ins, constructability, procurement/construction coordination, acceptance).
- Include only the six source-supported package interfaces for PKG-020.
- Use the DBM 13.8 kV electrical basis as facility context only; do not infer switchgear bus ratings, breaker interrupting ratings, BIL, protection settings, or arc-flash boundaries from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.
- Reflect the DBM standby-power update: the 13.8 kV switchgear is not the standby-power tie-in; standby power moves to TOU generators at the 600 V MCC level.
- Do not silently allocate DBM-listed equipment tags or electrical-building line items to PKG-020 without source confirmation; carry allocation as a human ruling item.

## Considerations

The DBM Power System section is unambiguous about facility function: the 13.8 kV switchgear "shall be designed, purchased, and installed as the plant main power distribution center" with bus sized for the full facility scope, and shall distribute power radially through step-down transformers to the 6.9 kV, 4.16 kV, and 600 V electrical buildings listed in that section. The Scope of Work can carry that function-level statement directly. It should stop short of asserting bus current, breaker count, BIL, or protection settings, none of which are stated in the accessible source slices.

The DBM also explicitly removes the prior centralized 13.8 kV emergency-generator concept; standby power is now at the 600 V MCC level via transfer switches. This is an important integration boundary: PKG-020 should not be scoped to absorb emergency-generation tie-in work.

The Trace Appendix line "810-1 13.8kV Switchgear Electrical Building" and the electrical equipment list line "Medium Voltage Switchgear, qty 1" (`ELC-QAS-000007-001`) are highly suggestive of PKG-020, but neither line states the package ID explicitly, so allocation should be flagged for human ruling rather than silently asserted.

The workbook and Gate 7 interface basis flags Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. These should drive the SOW boundary narrative and later construction coordination. The Communications/Network interface should align with the DBM EtherNet-to-plant-PLC basis used for MCC/switchgear data acquisition.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Switchgear ratings (bus, breaker, BIL) | Reference the DBM 13.8 kV system basis as facility context; keep ratings `TBD`. | Premature ratings could conflict with vendor design or detailed studies. |
| Tagged equipment allocation | Reference DBM-listed "Medium Voltage Switchgear" qty 1 and the "810-1 13.8kV Switchgear Electrical Building" as facility-context candidates; keep PKG-020 tag allocation `TBD`. | The SOW could silently absorb tags that belong to other packages or get re-assigned during detailed engineering. |
| Standby power | State explicitly that PKG-020 is not the standby-power tie-in. | Scope creep into emergency generation that the DBM has already removed. |
| Studies | Reference relay-coordination/arc-flash and load-flow studies as facility-level deliverables whose PKG-020 inputs/outputs are TBD. | Picking values could pre-empt facility-wide studies. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor switchgear design obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |

## Examples

- Acceptable SOW language: "PKG-020 is the workbook-defined Electrical package `13.8kV SWITCHGEAR EQUIPMENT`, WBS 01, tracking number `26020-01-30-011`; the Package Vendor owns package engineering/design/vendor documentation/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "The 13.8 kV switchgear is the plant main power distribution center, fed from the 25 kV / 13.8 kV / 50 MVA utility-supplied transformer downstream of the BC Hydro 25 kV utility supply, and distributing radially through step-down transformers to the 6.9 kV Inlet/Sales Compressor, 4.16 kV Acid Gas/Overheads Compressor, 600 V Acid Gas Compressor, 600 V Sales/Overheads Compressor, and 4.16 kV/600 V General Area/Tank Farm/Process Electrical Buildings per the DBM Power System section."
- Acceptable SOW language: "Bus continuous current rating, short-circuit interrupting rating, BIL, breaker count, lineup arrangement, control voltage source, dimensions, weights, environmental rating, protection settings, and arc-flash boundaries are TBD pending vendor data and detailed electrical studies."
- Avoid: "The EPC Integrator shall design the 13.8 kV switchgear lineup." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "The 13.8 kV switchgear shall serve as the emergency-generation tie-in." The DBM removes that scope and moves standby power to the 600 V MCC level.
- Avoid: "PKG-020 includes Medium Voltage Switchgear `ELC-QAS-000007-001` and the `810-1 13.8kV Switchgear Electrical Building`." Source does not explicitly bind those tags to PKG-020.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-020-01-01 | The DBM lists the BC Hydro utility incoming voltage as "25 kV (TBC)"; the figure is itself flagged as to-be-confirmed in the source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System utility supply paragraph. | No alternate accessible source. | Datasheet Conditions (utility supply context); Specification SOW-020-05 verification. | Carry "25 kV (TBC)" exactly as the source states; do not normalize. | TBD |
| HR-020-01-02 | Tagged equipment allocation to PKG-020 (the DBM-listed "Medium Voltage Switchgear, qty 1" `ELC-QAS-000007-001` and the "810-1 13.8kV Switchgear Electrical Building" trace-appendix line) is not explicitly stated in workbook row 22 or Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. | Workbook Packages row 22; Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical equipment list and Trace Appendix. | Datasheet Attributes (tagged equipment); Specification SOW-020-11; Procedure Steps and Verification. | Keep PKG-020 tagged equipment `TBD` until allocation is confirmed by a governing source or human ruling. | TBD |
| HR-020-01-03 | `26020-Package_Requirements.docx` was searched for PKG-020-specific 13.8 kV switchgear content but no accessible match was found in this run; package-level requirement clauses (if any) are not available. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. | `_Sources/26020-Package_Requirements.docx` (search returned no PKG-020 match in this run). | Specification Standards; Procedure Prerequisites and Records. | Cite `26020-Package_Requirements.docx` as a target source with location TBD; do not derive clause-level requirements until accessible. | TBD |
| HR-020-01-04 | Workbook row 22 flags Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, and Structural/Foundations/Supports as the package interfaces, but the DBM and `26020-Package_Requirements.docx` do not provide PKG-020-specific interface-clause text mapping each flag to a concrete tie-in basis. | Workbook Packages row 22; Gate 7 `INTERFACE_REGISTER.csv` PKG-020 rows. | DBM facility-level interface paragraphs (cable, grounding, electrical-building bottom-entry, PLC EtherNet) carry general facility basis, not PKG-020-specific clauses. | Datasheet Conditions/Construction (interface treatment); Specification SOW-020-04 verification. | Cite the workbook/Gate 7 interface flags as the SOW interface list; carry tie-in detail as `TBD` pending package-level requirement text or vendor data. | TBD |
