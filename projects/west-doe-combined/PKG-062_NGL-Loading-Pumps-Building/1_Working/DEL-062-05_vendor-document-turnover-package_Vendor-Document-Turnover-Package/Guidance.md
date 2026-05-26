# Guidance — DEL-062-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package is the single Package-Vendor deliverable that consolidates the vendor document register, all required vendor submittals, and the turnover records for `PKG-062 NGL Loading Pumps Building` (source equipment package `26020-01-PT-18-003 — LPG Loading Pumps`; the LPG vs NGL fluid-name discrepancy is flagged as Conflict C-01). It exists so that the EPC Integrator can review and accept the vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and so the Owner ultimately receives a complete, controlled record of the equipment package as built and tested.

Source authority: `26020-Package_Requirements.docx` heading 16 → Vendor Engineering Deliverables (the document set this turnover package controls); `_CONTEXT.md` (responsibility and scope); `DELIVERABLE_REGISTER.csv` (deliverable identity and downstream consumer).

## Principles

1. **The source vendor deliverables table is the document-scope authority.**
   The vendor deliverables table at heading 16 is what the vendor must produce. The turnover package does not add documents the source does not require, and does not omit documents the source requires. Additions or omissions must be reconciled against the EPC Scope of Work and Package Datasheet, and recorded as scope changes.

2. **The Vendor Document Index (PRQ-009) is the operational backbone.**
   Every other document in the package is enumerated, revisioned, transmitted, and reviewed through the index. The index is updated continuously, not just at turnover.

3. **The Vendor Document Control Procedure (DOC-008) is the rule book.**
   Numbering, revision states, transmittal mechanics, hold/code/review codes, and acceptance flow all live in DOC-008. When DOC-008 contradicts informal practice, DOC-008 wins. (DOC-008 is not yet locally accessible — see Conflict Table.)

4. **Turnover is staged, not a single event.**
   The vendor data books (PRQ-016 / MEC-023) are the final, consolidated artifact, but FAT/SAT, material certs, as-builts, and regulatory packages are issued at their natural points in the schedule. The turnover package is the running compilation, not only the final book.

5. **Source-required documents stay first-class; they are artifacts of this deliverable, not standalone deliverables.**
   Per `_CONTEXT.md` Notes, individual source document rows are evidence under this deliverable, not separate decomposition deliverables. The decomposition deliberately keeps them aggregated here.

6. **Interface to acceptance lives in DEL-062-06.**
   Vendor turnover (this deliverable) provides the controlled record. The acceptance ruling lives in `DEL-062-06_epc-vendor-package-review-and-acceptance`. Do not co-mingle.

7. **Loading-service operability is first-class evidence.**
   The pumps exist to move LPG product from storage to truck loading (heading 16 → Basic Scope). The Operating Guidelines / Startup-Shutdown Narrative (PRO-025) and the metering package specification (INS-015) are not "support" documents — they are central to demonstrating that the delivered package performs its declared function.

## Considerations

- **LPG vs. NGL service-fluid naming.** The decomposition names the package `NGL Loading Pumps Building` (`_CONTEXT.md`, `PACKAGE_REGISTER.csv`), while source heading 16 names the equipment package `LPG Loading Pumps` and describes the service as "LPG product from storage to LPG Truck Loading." The two names may refer to the same site facility under different fluid characterizations (the broader cryogenic deep-cut plant produces both NGL and LPG fractions), or they may be a mismatch. The turnover package should not silently overwrite either name. See Conflict Table C-01.

- **Four-unit configuration.** With 4 × identical Blackmer LGL4B pumps (P9510/20/30/40-1) in parallel (heading 16), expect four sets of unit-specific documents (e.g., pump data sheets per tag, FAT reports per tag) plus shared design-basis and package-level documents. The index should disambiguate per tag.

- **Cold-start motor sizing is the controlling electrical case.** Heading 16 explicitly calls out "motors to be sized for inlet stabilizer composition density at -40 °C start-up condition." This is non-trivial and must be evidenced in ELE-011 and PRO-013; reviewers should expect the worst-case density basis to drive motor power.

- **Capacity / TDH is marked TBC in source.** Heading 16 lists per-pump capacity as "68 m³/hr @ 345 kPad (300 USGPM @ 50 psid) TBC TDH." The TDH value is explicitly to-be-confirmed in source; the turnover package must carry the final confirmed TDH on MEC-007 and reconcile it against the FAT performance curve on MEC-022.

- **"By others" scope items are not in this turnover.** Heading 16 → Scope Notes / Open Items explicitly excludes DCS integration, foundations, and electrical supply to MCC from the vendor scope. The turnover package documents the vendor side of the interface (e.g., CTL-026 Package Vendor Interface Specification, ELE-028 Interconnection Diagrams) but does not include the by-others work product.

- **Pressure-equipment registration NOT enumerated.** Unlike the compressor-package vendor turnover (PKG-080 DEL-080-05), heading 16 does NOT enumerate `REG-022 Pressure Equipment Registration Package` for the LPG Loading Pumps. Rotary vane pumps may not trigger provincial pressure-equipment registration at the same threshold as a reciprocating compressor cylinder; do not add REG-022 to the turnover without a scope-change record. See Conflict Table C-06.

- **Source-basis budgetary go-by is not contract.** Heading 16 → Source Basis cites `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` as a budgetary RFQ basis only. It is not the document control basis for turnover; do not propagate its numbering, terms, or quantities into the vendor index without verification.

- **Interfaces file naming discrepancy.** Source heading 16 → Physical Interface Summary cites `26020-Packages_Interfaces.3.xlsx`; the locally accessible file is `26020-Packages_Interfaces_4_export.xlsx`. Treat as a revision/export-naming discrepancy and follow the more recent file unless a human ruling says otherwise (see Conflict Table C-04).

- **Interface Coordination Notes are explicitly TBD in source.** Heading 16 → Interface Coordination Notes contains only "TBD." The turnover package cannot pre-empt this; reviewers should expect coordination notes to be issued separately and woven into the index when they appear.

## Trade-offs

- **Comprehensive index vs. transmittal burden.** A finer-grained index (one row per source ID) increases administrative load but makes acceptance verification straightforward. A coarser index (one row per vendor PDF) shifts burden to verification time. Preferred posture: fine-grained index, coarse transmittals — index resolves the mapping.

- **Stage-by-stage submittal vs. final-book-only.** Issuing only the final vendor data books reduces EPC review cycles but produces a one-shot review surge at turnover. Stage-by-stage submittal smooths review load and surfaces defects early; preferred where DOC-008 permits.

- **Native vendor numbering vs. project numbering.** Native numbering preserves vendor configuration management; project numbering eases EPC consumption. PRQ-009 should carry both columns to avoid the trade-off entirely.

- **Per-tag pump documentation vs. one-set-fits-all.** Since the four pumps are identical, a single set of pump data sheets covers them all electrically and hydraulically; per-tag records may only be needed for FAT and material certs. Optimizing here trades vendor effort against per-unit traceability.

## Examples

- The source vendor deliverables table for PKG-062 (heading 16) enumerates roughly 100+ document IDs across functional groups (core vendor docs, core package engineering, rotating equipment / pumps, loading/metering, relief/flare, process piping, utility piping, drainage/containment, electrical, instrumentation/controls, building/HVAC, fire/gas, structural). The Vendor Document Index (PRQ-009) must therefore have at least one row per enumerated source ID. See `Datasheet.md` for the full enumeration.

- A Pump Data Sheet (MEC-007) for pump tag P9510-1 carries the per-tag serial number, motor nameplate, mechanical seal arrangement, and the finalized TDH that resolves the source TBC.

- The Equipment FAT Performance Test Report (MEC-022) is issued as soon as FAT is complete for each pump tag; the executed copies are then bound into the Mechanical Final Documentation (MEC-023) at turnover.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Package fluid-service naming: NGL vs LPG | Decomposition (`_CONTEXT.md`, `PACKAGE_REGISTER.csv`): "NGL Loading Pumps Building" | Source heading 16: "LPG Loading Pumps"; service description "LPG product from storage to LPG Truck Loading" | Datasheet Identification + Attributes; Specification Scope; Guidance Purpose | PROPOSAL: confirm whether the package serves LPG (per source) or NGL (per decomposition) or both; reconcile the package name accordingly | TBD |
| C-02 | Submittal revision stages not stated in source | heading 16 (no stages defined) | Industry convention (Bid/IFR/IFA/IFC/As-Built) | Specification REQ-15; Datasheet Conditions | PROPOSAL: adopt Bid/IFR/IFA/IFC/As-Built pending DOC-008 issuance | TBD |
| C-03 | Transmittal medium / review turnaround not stated | heading 16 (silent) | Project document-control standard (not locally accessible) | Specification REQ-16, REQ-17; Datasheet Conditions | PROPOSAL: confirm against issued DOC-008 and project doc-control matrix | TBD |
| C-04 | Interfaces filename mismatch | heading 16 cites `26020-Packages_Interfaces.3.xlsx` | Local file is `26020-Packages_Interfaces_4_export.xlsx` | Datasheet References / Physical Interface table; Guidance Considerations | PROPOSAL: use the `_4_export` file as the latest revision unless overruled | TBD |
| C-05 | Capacity TDH is marked TBC in source | heading 16: "68 m³/hr @ 345 kPad (300 USGPM @ 50 psid) TBC TDH"; Operating / Design Conditions: "TBC. Please see capacity/site conditions." | Final pump data sheets (MEC-007) and FAT report (MEC-022), not yet issued | Datasheet Attributes; Specification REQ-14 | PROPOSAL: turnover package must carry the final TDH confirmed by MEC-007 and FAT MEC-022 | TBD |
| C-06 | Pressure-equipment registration not enumerated | heading 16 vendor deliverables (no REG-022) | Sibling deliverable DEL-080-05 (compressor package) does enumerate REG-022 | Specification REQ-10 (no REG-022); Datasheet document list | PROPOSAL: do not add REG-022 to the turnover without a confirmed scope change; rotary vane pumps may be below the registration threshold | TBD |
| C-07 | Fire / building code not cited | heading 16 lists REG-021 without code reference | Provincial fire / building code (TBD) | Specification Standards table; REQ-10 | PROPOSAL: confirm code from project location (4-25 West Doe Deepcut) | TBD |
| C-08 | Objective-to-deliverable mapping is package-grouped | OBJECTIVE-related mapping in decomposition shows OBJ-001, OBJ-003..OBJ-010 against PKG-062 | No deliverable-level explicit objective mapping | _CONTEXT.md Supports Objectives | ASSUMPTION (package-heuristic) per skill default | TBD (confirm) |
| C-09 | Interface Coordination Notes explicitly TBD in source | heading 16 → Interface Coordination Notes: "TBD." | None | Datasheet Conditions; Procedure prerequisites | PROPOSAL: track separately; reissue when notes are published | TBD |
| C-10 | Electrical area classification standard not cited | heading 16 (silent on hazardous-area standard) | NFPA / CEC (ASSUMPTION) | Specification Standards table | PROPOSAL: confirm with project electrical design basis | TBD |
