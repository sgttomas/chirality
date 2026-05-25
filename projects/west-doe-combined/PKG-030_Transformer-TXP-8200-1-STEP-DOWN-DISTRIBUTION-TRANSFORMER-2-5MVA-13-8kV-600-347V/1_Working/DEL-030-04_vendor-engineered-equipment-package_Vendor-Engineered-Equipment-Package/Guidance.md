# Guidance: DEL-030-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package exists to convert the accepted EPC package basis for `PKG-030` (the 2.5 MVA, 13.8 kV / 600 V / 347 V step-down distribution transformer) into a vendor-engineered, fabricated, and supplied physical package. This deliverable should let the Package Vendor execute engineering, design, fabrication/supply, and physical delivery within the EPC-defined battery limits and interfaces, while the EPC Integrator performs integration review.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling.
- Treat the EPC Scope of Work (`DEL-030-01`) and EPC Package Datasheet (`DEL-030-02`) as the upstream basis the vendor package executes against; do not duplicate or restate EPC-authored scope here.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator (integration review).
- Treat workbook interface `X` facts as binding interface obligations the vendor package shall satisfy; carry them via the EPC Package Datasheet matrix, not as separate deliverables.
- Use `TBD` for nameplate impedance, BIL, tap configuration, cooling class, oil type, secondary 4-wire/347 V provisioning, signal lists, area classification, and installation location until vendor data or EPC-issued source resolves them.

## Considerations

The DBM electrical design basis for the 04-25 facility establishes a 13.8 kV medium-voltage backbone fed from a 25 kV / 13.8 kV utility transformer (50 MVA) and a 13.8 kV switchgear that distributes radially through step-down transformers to facility electrical buildings and loads. A 2.5 MVA, 13.8 kV / 600 V transformer fits this radial step-down role; the precise downstream MCC or electrical building served by this unit is not assigned in the accessible source.

The DBM identifies oil-filled transformers in the 04-25 equipment list and states that large oil-filled transformers shall be spaced per CEC and shall be installed on structural-steel transformer bases, with secondary containment minimized where practical. The transformer construction (oil-filled vs. dry-type, K-factor, cooling class) is a vendor engineering decision; the vendor should select consistent with project HSE/containment direction and EPC integration.

Facility grounding basis requires major electrical equipment to be grounded at two points, with a separate CEC-sized copper ground conductor for distribution transformers. The 600 V system is high-resistance grounded with a 5 A continuous resistor; the vendor secondary connection and grounding scheme shall be compatible.

The package name carries "600/347V." 347 V is the phase-to-neutral value of a 600 V wye system. The accessible DBM source describes 600 V as 3-phase, 3-wire (no separately enumerated neutral), so whether this specific transformer secondary is delta or wye-with-neutral-out (4-wire) is not source-confirmed. If a 4-wire 600/347 V secondary is required (e.g., to support 347 V lighting branch circuits), that requirement should come from the EPC Package Datasheet; otherwise the 347 V notation should be treated as nominal voltage-class shorthand and the secondary configuration left to vendor engineering with EPC concurrence.

Maintenance access, cable tray/conduit routing, structural/foundation supports, and area/exterior lighting are explicit `PKG-030` interfaces. The vendor package shall coordinate physical envelope, bushing/tap-changer access, and base support arrangements such that EPC tie-ins and routing remain feasible.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Oil-filled vs. dry-type | Default to oil-filled per facility equipment list, subject to vendor and EPC concurrence on containment/HSE. | DBM 04-25 equipment list explicitly identifies oil-filled transformers; CEC spacing and containment are addressable. |
| 4-wire 600/347 V secondary | Treat 347 V as voltage-class shorthand until EPC Package Datasheet confirms a wye-with-neutral secondary. | DBM describes 600 V as 3-phase, 3-wire; no source slice confirms 4-wire provisioning for this transformer. |
| Standards (clause-level) | List CEC, project electrical specifications, area classification standards, and IEEE/CSA transformer standards as applicable bases with clause/edition locations `TBD`. | Accessible source identifies these bases but does not provide clause-level text. |
| Installation location | Note that the unit serves the radial 13.8 kV → 600 V distribution role; do not assign to a specific electrical building/skid/yard pad. | DBM identifies electrical buildings and distribution but does not assign `PKG-030`. |
| Quantity | Hold quantity as `TBD` for this package. | The 04-25 equipment list reports an aggregate oil-filled transformer count, not a `PKG-030`-specific quantity. |

## Examples

- Acceptable datasheet entry: "Primary system voltage: 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages and services table."
- Acceptable source-gap entry: "Nameplate impedance, BIL, tap configuration, and cooling class: `TBD` pending vendor data."
- Not acceptable without new source: "Transformer impedance is 5.75 % and BIL is 95 kV on the secondary." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-030-04-001 | The package name records "600/347V" but the DBM 04-25 electrical basis describes the 600 V system as 3-phase, 3-wire; whether the transformer secondary is a 4-wire 600/347 V configuration is not source-confirmed. | Workbook Packages row 32; `PACKAGE_REGISTER.csv` row `PKG-030` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltages and services table | Datasheet Attributes (347 V derivation); Specification REQ-030-04-002, REQ-030-04-010; Procedure verification | Treat 347 V as voltage-class shorthand and keep secondary configuration `TBD` until EPC Package Datasheet (`DEL-030-02`) or vendor data resolves it. | TBD |
| HRR-030-04-002 | The 04-25 equipment list identifies an aggregate "Oil-Filled Transformers" quantity of 2 but does not allocate quantity or specific identity to `PKG-030`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list | Workbook Packages row 32; `PACKAGE_REGISTER.csv` row `PKG-030` | Datasheet Attributes; Specification REQ-030-04-001, REQ-030-04-010 | Hold quantity as `TBD` for this package until EPC Package Datasheet or detailed engineering confirms allocation. | TBD |
| HRR-030-04-003 | No `PKG-030`-specific match was confirmed in `_Sources/26020-Package_Requirements.docx` during this run; vendor-facing detailed requirements (e.g., impedance, BIL, taps, cooling, oil type, signal list, area classification) are not source-grounded at the package level. | `_REFERENCES.md`; absence in `_Sources/26020-Package_Requirements.docx` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and electrical paragraphs (facility-level only) | Datasheet Attributes/Construction; Specification REQ-030-04-005 through REQ-030-04-010; Procedure verification | Carry detailed transformer ratings/tests/area-classification as `TBD` and require EPC Package Datasheet (`DEL-030-02`) to supply these to the vendor. | TBD |
