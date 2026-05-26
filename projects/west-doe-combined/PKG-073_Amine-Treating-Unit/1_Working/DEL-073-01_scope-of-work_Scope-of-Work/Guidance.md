# Guidance — DEL-073-01 Scope of Work (PKG-073 Amine Treating Unit)

## Purpose

The Scope of Work (SOW) is the EPC Integrator's anchor deliverable for PKG-073 Amine Treating Unit. It defines the package boundary, the vendor/EPC responsibility split, the process function, the tagged equipment, the facility interfaces, and the integration narrative needed to procure and integrate a complete ATU into the 04-25 Deepcut facility. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-073-01; `PACKAGE_REGISTER.csv` PKG-073.)

This deliverable is a Mandatory Gate 5 EPC anchor deliverable as recorded in `_CONTEXT.md` Notes and the deliverable register row.

## Principles

1. **Vendor-owned package, EPC-integrated facility.** Package Vendor owns package engineering, package design, vendor documentation, and physical equipment supply. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The SOW must keep this split explicit and must not silently assign vendor design work to the EPC Integrator. (Source: `PACKAGE_REGISTER.csv` PKG-073; OBJ-004.)

2. **Source-anchored package identity.** Package identity (PKG-073, workbook row 49, tracking 26020-01-27-001, discipline Mechanical, WBS 01) is governed by the workbook + 26020-Package_Requirements.docx heading 27. Identity attributes are not negotiable at the deliverable level. (Source: `PACKAGE_REGISTER.csv` PKG-073.)

3. **Two-module process function.** The ATU is described and procured as two modules: Amine Gas Sweetening (lean MDEA contacts sour inlet gas to produce pipeline-quality sweet gas) and Amine Regeneration (thermal regeneration of rich amine). SOW narrative should preserve this two-module framing. (Source: `SCOPE_LEDGER.csv` SOW-0052.)

4. **All 13 interface types are in scope.** The PKG-073 interface set in `INTERFACE_REGISTER.csv` is the integration surface. The SOW must communicate that the EPC owns the facility-side of every listed interface type, including high-risk safety interfaces (Relief/Flare/Vent, Drain/Containment, Fire & Gas/Safety Systems) given sour service. (Source: `INTERFACE_REGISTER.csv` PKG-073; OBJ-009.)

5. **Sour-service safety, regulatory, and codes context.** Sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, and standards requirements must remain visible in this package's downstream deliverables. (Source: OBJ-009.)

6. **"By Others" boundary is explicit.** Shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs, and the separate process water pumps/tanks scope are explicitly excluded from the package vendor scope. The SOW must list these as out-of-scope and route them to the responsible facility scope. (Source: `SCOPE_LEDGER.csv` SOW-0054.)

## Considerations

- **Appendix A dependency.** Capacity, design throughput, operating conditions, and design conditions are cited "See Appendix A" in the source SOW-0054 text. Appendix A is not locally accessible; downstream deliverables (notably DEL-073-02 Package Datasheet) will need the appendix slice or the bid-doc RFQ file (`26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx`) to populate process conditions. Marked TBD here. (Source: `SCOPE_LEDGER.csv` SOW-0054; `PACKAGE_REGISTER.csv` PKG-073.)
- **Equipment list completeness.** Only the Amine Inlet Filter Coalescer was extracted into `SCOPE_LEDGER.csv` SOW-0053 with full detail. The source Word heading 27 likely enumerates additional equipment (contactor, regenerator, reflux drum, reboiler, lean/rich exchanger, pumps, etc.) — ASSUMPTION based on standard ATU topology; not confirmed from locally accessible source slice. The SOW should flag this gap. (Source: SOW-0053; ASSUMPTION.)
- **Downstream consumers.** Acid gas from this package feeds PKG-046 Acid Gas Compressors (per PKG-046 process-function text referencing "Acid gases (H2S & CO2) coming out of the Amine treating"). Sweet-gas downstream linkage to dehydration is implied by facility narrative. The integration narrative should name these explicitly. (Source: `PACKAGE_REGISTER.csv` PKG-046; ASSUMPTION on dehydration linkage.)
- **Sibling deliverable load-bearing.** The SOW does not stand alone. DEL-073-02 (Package Datasheet), DEL-073-03 (Construction Work Package), DEL-073-04 (Vendor Engineered Equipment Package), DEL-073-05 (Vendor Document Turnover), and DEL-073-06 (EPC Vendor Package Review and Acceptance) consume the SOW's identity, interfaces, and responsibility split. Keep terminology and identifiers stable. (Source: `DELIVERABLE_REGISTER.csv` PKG-073 rows.)

## Trade-offs

- **Breadth vs. precision.** The SOW can either restate the full source Word clauses (high precision, but blocked by binary-format source accessibility) or summarize at the register-row level (broad, but loses clause-level detail). Until the Word heading 27 is extracted to markdown, the SOW must summarize and explicitly mark unresolved clause-level items TBD rather than paraphrase from inference.
- **Vendor latitude vs. EPC prescription.** OBJ-004 frames the package as vendor-owned. The SOW should describe required outcomes (process function, interface boundaries, motor electrical class, exclusions) without over-specifying vendor internal design choices.
- **Two-module narrative vs. integrated unit.** Source SOW-0052 is explicit about the two-module description. Collapsing this into a single "ATU" narrative loses traceability to the source; keep the two-module framing.

## Examples

- **Vendor/EPC responsibility example (from source):** "Package vendor is responsible for the package engineering, design, vendor documentation, and physical equipment package; the EPC Integrator is responsible for integrating this package into the whole process facility." (Source: `PACKAGE_REGISTER.csv` PKG-073 "Basic Scope".)
- **Motor electrical-class example (from source):** "All pumps require electric motors. Motors rated 1 HP to 200 HP shall be 600V / 3-phase / 60 Hz. Motors rated above 200 HP shall be 4160V or 6900V / 3-phase / 60 Hz. All motors 100 HP and above shall be VFD-ready." (Source: `SCOPE_LEDGER.csv` SOW-0054.)
- **Filter coalescer example (from source):** "Amine Inlet Filter Coalescer; Quantity: 2 x 100% (piping configured for on filter is always operational); 0.3 Micron @ 99.97%; Single phase; c/w Bandlock Type QOC; Pressure Drop < 2 psid clean". (Source: `SCOPE_LEDGER.csv` SOW-0053.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| C-073-01-01 | Equipment list completeness — `SCOPE_LEDGER.csv` SOW-0053 lists only Amine Inlet Filter Coalescer, while source Word heading 27 likely enumerates the full equipment set | `SCOPE_LEDGER.csv` SOW-0053 | `_Sources/26020-Package_Requirements.docx` heading 27 (not locally accessible in markdown) | Datasheet "Construction"; Specification R-073-01-03 | Treat Word heading 27 as authority once extracted; current entries are partial | TBD |
| C-073-01-02 | Capacity/design conditions reference "Appendix A" with no accessible content | `SCOPE_LEDGER.csv` SOW-0054 | Bid Doc `26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx` Appendix A (not locally accessible) | Datasheet "Conditions"; Specification R-073-01-07 | Treat Appendix A in the bid-doc RFQ as authority once made accessible | TBD |
