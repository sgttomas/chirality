# Guidance: DEL-035-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable exists so the EPC Integrator can demonstrate, with auditable evidence, that the vendor-engineered 13.8 kV switchgear electrical building package (Building 810-1) has been reviewed, tested, accepted, and is ready for facility integration and turnover. It is the EPC's evidence pack that the vendor's package satisfies the EPC Scope of Work (DEL-035-01), the EPC Package Datasheet (DEL-035-02), and the Construction Work Package (DEL-035-03) for `PKG-035`, and that the package's twelve declared interfaces have been closed against the EPC interface evidence. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `SCOPE_LEDGER.csv` `SOW-0036`.

## Principles

- **Vendor/EPC responsibility split is preserved (OBJ-004).** The Package Vendor authored and tested the package; the EPC reviews, accepts, and integrates. This deliverable shall not author vendor design content or substitute EPC judgment for vendor specifications. Source: `PACKAGE_REGISTER.csv` row `PKG-035`; `OBJECTIVE_REGISTER.csv` OBJ-004.
- **Acceptance is evidence-based, not narrative.** Every acceptance statement shall be traceable to a vendor document, a test/inspection record, an interface evidence row in DEL-035-02, or a signed checklist line. Source: `ARTIFACT_REGISTER.csv`.
- **The 13.8 kV switchgear is the plant main power distribution centre.** Acceptance treats this package as facility-critical infrastructure feeding downstream electrical buildings; defects or unclosed interfaces here propagate facility-wide. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis.
- **Open items are tracked, not hidden (OBJ-010).** Items not closed at acceptance shall be recorded with owner, closure plan, and target date rather than waived silently. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.

## Considerations

- **Shop-built building.** Building 810-1 is identified in the DBM Building Strategy table as shop-fabricated. Plan factory acceptance and shop inspection accordingly; field-only acceptance is insufficient. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table.
- **Interface count.** Twelve interface facts are declared for `PKG-035` in the interface register. A checklist that does not address each one is incomplete by construction. Source: `INTERFACE_REGISTER.csv` rows for `PKG-035`.
- **HVAC n+1.** The DBM mandates n+1 HVAC sizing for electrical buildings. Confirm vendor sizing matches; this is a recurring source of vendor under-design when ambient or load assumptions drift. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings.
- **Bottom-entry cabling and elevated installation.** Acceptance shall confirm the building is configured for bottom entry and is designed for elevated installation on piles; retrofitting bottom-entry later is costly. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings.
- **Grounding two-point + ground wells.** Acceptance shall confirm both the two-point ground grid connection for major equipment and the ground wells with bolted test points at the building. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding.
- **Equipment door / transom.** Verify the largest piece of switchgear can be removed through the doors or removable transom. This is a maintainability gate, not a paperwork item. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings.
- **Vendor documentation set.** The vendor document review log should be structured around the vendor-document tables in `_Sources/26020-Package_Requirements.docx`. The specific table content was not slice-extracted in this pass (binary source); confirm the table list during execution. Source: `OBJECTIVE_REGISTER.csv` OBJ-004 narrative.

## Trade-offs

- **Depth of FAT witnessing vs. schedule.** Witnessing all hold points adds schedule; relying solely on vendor self-inspection reduces EPC evidence. The acceptance package shall record which hold points were witnessed by the EPC and which were accepted on vendor evidence. ASSUMPTION: the witness/hold-point list is governed by the vendor specification; `_Sources/26020-Package_Requirements.docx` slice — `location TBD` — would normally control.
- **Acceptance with open items vs. delayed acceptance.** Accepting with logged open items unblocks facility integration but transfers risk; delaying acceptance preserves leverage but holds schedule. The open-items log (OBJ-010) is the mechanism that allows the first path without losing traceability. Source: `OBJECTIVE_REGISTER.csv` OBJ-010.
- **EPC interface closure timing.** Some interfaces (e.g., grounding, structural, drainage) can only be fully closed after the building is set in place; others (e.g., HVAC sizing, door/transom) are factory-closeable. Sequence the checklist so factory items close at FAT and field items close at turnover.

## Examples

- **Vendor documentation review log row (illustrative).** A row identifies the vendor document number, revision, EPC reviewer, comment count, comment disposition (incorporated / clarified / rejected), and the revision that closed the comments. The structure is consistent with the Vendor Document Turnover Package deliverable (DEL-035-05). Source: `ARTIFACT_REGISTER.csv` `ART-AA841F7CA1`; `DELIVERABLE_REGISTER.csv` row `DEL-035-05_vendor-document-turnover-package`.
- **Interface closure row (illustrative).** For `IFC-A5EF521315` (Electrical Power), the row points to the DEL-035-02 EPC Interface Requirements Evidence entry, the vendor design document that satisfies it, the FAT test that proved it, and the EPC sign-off. Source: `INTERFACE_REGISTER.csv` `IFC-A5EF521315`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-035-06-001 | Detailed vendor documentation tables and factory witness/hold-point requirements are referenced by OBJ-004 / OBJ-010 narrative as governed by `_Sources/26020-Package_Requirements.docx`, but the source is binary and was not slice-extracted in this pass. | `OBJECTIVE_REGISTER.csv` OBJ-004 / OBJ-010 narrative | `_Sources/26020-Package_Requirements.docx` (binary; location TBD) | Specification REQ-035-06-003; Specification Standards table; Guidance Considerations | PROPOSAL: extract the vendor-document and witness/hold-point tables in a follow-on pass (text/markdown conversion) and re-anchor REQ-035-06-003 to specific table rows. Treat current entries as `location TBD` until extracted. | TBD |
| CFL-035-06-002 | The DBM identifies Building 810-1 as Shop-built but does not state the full vendor design specification (witness/hold-point depth, FAT scope) for the 13.8 kV switchgear inside it. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table | `_Sources/26020-Package_Requirements.docx` (binary; location TBD) | Specification REQ-035-06-003; Datasheet Construction (Factory/shop test row) | PROPOSAL: keep REQ-035-06-003 framed as "consistent with the vendor specification" with explicit `location TBD` until the vendor specification slice is available. | TBD |
