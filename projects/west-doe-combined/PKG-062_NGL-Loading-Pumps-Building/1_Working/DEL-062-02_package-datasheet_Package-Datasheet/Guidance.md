# Guidance — DEL-062-02 Package Datasheet (NGL Loading Pumps Building, PKG-062)

> Pass 1 + Pass 2 draft. Directional rationale for engineers using the Datasheet, plus the Conflict Table for human ruling.

## Purpose

The Package Datasheet exists to be the EPC Integrator's single technical handoff to the Package Vendor for `PKG-062`. It carries enough source-grounded fact (equipment, capacity, driver, building, interfaces, by-others) for the vendor to begin package engineering, and enough interface evidence for EPC discipline engineering to plan tie-ins. Per `_CONTEXT.md` Notes, interface facts are intentionally consolidated here as evidence rather than spawning standalone deliverables.

Source: `_CONTEXT.md` Scope, Notes; `DELIVERABLE_REGISTER.csv` row `DEL-062-02_package-datasheet`.

## Principles

1. **Source fidelity over convenience.** Pump make/model, capacity, driver class, motor sizing temperature, and by-others list come verbatim from `26020-Package_Requirements.docx` (`26020-01-PT-18-003`). If the source carries `TBC`, the Datasheet carries `TBC` — it does not invent a value to "complete" the sheet.

2. **Battery limits are an EPC contract surface.** "By others: DCS integration, foundations, electrical supply to MCC" is not narrative; it is the boundary the vendor priced against. Any change to this list is a scope change.

3. **Interface applicability is binary and authoritative.** The `Yes / No` matrix in the source row determines which interface deliverables apply. Engineers shall not silently re-classify an interface; conflicts go to the Conflict Table.

4. **Motor sizing condition is unusual and load-bearing.** Sizing for **inlet stabilizer composition density at −40 °C start-up** is explicit in the source. Substituting a "normal LPG density" basis will under-size the motors and is forbidden.

5. **Vendor deliverables list is contractually transmitted.** The Vendor Engineering Deliverables list in `Datasheet.md` is the basis for the Vendor Document Index (`PRQ-009`). Truncating or "trimming" the list silently is forbidden.

## Considerations

- **Naming.** Decomposition uses "NGL Loading Pumps Building"; the source row label is "LPG Loading Pumps" with process function "move LPG product from storage to LPG Truck Loading." This is recorded as CONFLICT-1 below. The Datasheet uses the decomposition name as the package identity but flags the discrepancy.

- **TBC values.** `TBC` markers are not gaps to fill — they are open items requiring vendor confirmation through `MEC-007 Pump Data Sheets`, `PRO-013 Pump Hydraulic / NPSH Calculations`, and `ELE-011 Motor Starting Study`. Engineers consuming the Datasheet should treat TBC values as inputs to vendor follow-up, not as targets for assumed values.

- **Interface workbook reference.** The source row points to `26020-Packages_Interfaces.3.xlsx`; the file present in `_Sources` is `26020-Packages_Interfaces_4_export.xlsx`. CONFLICT-2 records the version mismatch; the column M / row 76 reference for Area / Exterior Lighting may or may not align in the newer export — verify before relying on it.

- **Vendor bid doc not locally available.** `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` is cited as the source basis but is not present under `_Sources`. Capacity, driver, and motor-sizing values are corroborated by the package-requirements document itself, so the Datasheet does not depend on the bid doc for these values; however, finer detail (NPSH, casing pressure rating, materials of construction) is `TBD` until the bid doc or vendor data sheet is available.

- **Structural / foundations / supports vendor-deliverable group.** The source slice extracted for Pass 1 ends mid-section ("Structural, fou…"). The remaining IDs in that group are `TBD`; re-extract from the source at closeout or at next pass.

- **DBM source applicability.** `DBM-Deepcut/4-25_Deepcut_DBM.md` is the basis-of-design reference cited in `PACKAGE_REGISTER.csv` (and matches the "4-25 West Doe Deepcut" status note in the source row). It is available locally but no specific clauses have been cross-referenced in this pass; reread during Pass 3 if `_SEMANTIC_LENSING.md` flags items dependent on DBM conditions.

## Trade-offs

- **Carrying TBC vs. inserting design assumptions.** The skill mandates `TBC`/`TBD` over invention. The trade-off is that a Vendor receiving the Datasheet must engage in confirm-back exchanges before it can complete `MEC-007`. This is the intended outcome.

- **Single-vendor model assumption (Blackmer LGL4B).** The source names a specific model. The vendor may propose an equivalent during bid clarification, but the Datasheet shall not preemptively generalize the model away from the source spec; doing so loses the corroboration between source and Datasheet.

- **Interface evidence carriage vs. standalone interface deliverables.** Per `_CONTEXT.md` Notes, interface facts are carried in the Datasheet rather than as separate deliverables. The trade-off is increased Datasheet density vs. proliferation of small deliverables; the project has chosen density.

## Examples

- **Reading capacity.** "68 m³/hr at 345 kPad (300 USGPM at 50 psid)" is per pump. Total package capacity at full duty is 4 × 68 = 272 m³/hr, but the source does not state total package capacity directly — `ASSUMPTION: sum of parallel pump capacities`. Do not publish the sum as a source value.

- **Reading motor sizing.** "Sized for inlet stabilizer composition density at −40 °C start-up condition" implies sizing for the densest expected fluid + cold motor torque, not for normal LPG density.

- **Reading the by-others list.** "DCS integration ... by others" means the Vendor delivers an interface specification (`CTL-026 Package Vendor Interface Specification`) and signals, not a DCS configuration.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-1 | Package name and process fluid: decomposition says "NGL Loading Pumps Building"; source row says "LPG Loading Pumps" with process function "move LPG product from storage to LPG Truck Loading." | `PACKAGE_REGISTER.csv` row `PKG-062` (Name = "NGL Loading Pumps Building") and `_CONTEXT.md` (PackageName) | `26020-Package_Requirements.docx` (`26020-01-PT-18-003 - LPG Loading Pumps`, "Basic Scope") | `Datasheet.md` Identification, Conditions; `Specification.md` R-DEL-062-02-002, -004; `Guidance.md` Considerations | PROPOSAL: keep decomposition's package identity for project-control traceability, but record process-fluid statement verbatim from source (LPG product). Treat "NGL Loading Pumps Building" as the building identity and "LPG Loading Pumps" as the equipment identity within that building. | TBD |
| CONFLICT-2 | Interface workbook version: source row references `26020-Packages_Interfaces.3.xlsx` (column M / row 76); local file in `_Sources` is `26020-Packages_Interfaces_4_export.xlsx`. | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Physical Interface Summary") | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (present) | `Datasheet.md` Physical Interface Applicability; `Specification.md` R-DEL-062-02-010 | PROPOSAL: rely on the source-row Yes/No matrix (which is internally complete) and treat the interface workbook as a corroborating artifact pending verification that "_4_export" still maps row 76 to PKG-062. | TBD |
| CONFLICT-3 | Bid doc cited but not locally accessible: `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx`. | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Source Basis") | `_Sources/` directory listing (file absent) | `Datasheet.md` Identification ("Source Basis" row); `Specification.md` Standards section | PROPOSAL: keep the citation but mark "location TBD" until the bid doc is added to `_Sources` or formally deferred. | TBD |
