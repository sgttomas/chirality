# Specification — DEL-071-05 Vendor Document Turnover Package (PKG-071 Fuel Gas Skid 4-25)

## Scope

This specification governs the assembly, content, quality, and delivery of the vendor document turnover package for PKG-071 Fuel Gas Skid 4-25. The deliverable is a single Package-Vendor-authored documentation set, reviewed by the EPC Integrator for interface/integration consistency, covering: the vendor document register, vendor document submittals, source-required vendor documentation captured as artifact rows where available, and turnover records (Source: `_CONTEXT.md` Scope; Anticipated Artifacts).

Covered Scope Items: SOW-0099, SOW-0100, SOW-0101, SOW-0102 (Source: `_CONTEXT.md`). Excludes the engineering-design deliverables of other PKG-071 deliverables and excludes any vendor documentation for equipment outside the fuel gas skid scope.

## Requirements

### R-1 — Vendor Document Register
The Package Vendor SHALL produce and maintain a Vendor Document Register listing every document submitted for the fuel gas skid, indexed by vendor document number, EPC document number (location TBD), document title, class, revision, status, planned and actual submittal dates, and review code. (ASSUMPTION — standard project document-control practice; specific register columns and numbering scheme not locally specified.)

### R-2 — Submittal Categories
The vendor document set SHALL include, at minimum (where applicable to scope), data sheets, GA/arrangement drawings, P&IDs, BOM, fabrication drawings, MTRs, welding records (WPS/PQR/welder quals, NDE), pressure-test records, surface-prep and coating records, electrical schematics, instrument index and loop diagrams, calibration certificates, FAT and SAT records, preservation records, recommended spare parts, IOM/O&M manuals, and training materials. (ASSUMPTION — derived from typical vendor turnover scope; final list TBD against the vendor master document register which is not locally accessible.)

### R-3 — Fuel-Gas-System Technical Content Coverage
Vendor documentation SHALL be consistent with the LP fuel gas system design basis applicable to PKG-071, including:
- LP fuel gas scrubber V-3210-1 sized for system design flow at design operating pressure using a maximum K factor of 0.35 Imperial with operating-pressure derating; condensed liquids route to TK-9130-1 (Source: DBM-Deepcut L1874).
- Electric resistance LP fuel gas heater with SCR control, skin-temperature thermocouple override, and outlet temperature control; heater duty TBD (Source: DBM-Deepcut L1872).
- All fuel gas regulators with at least one installed spare and 2 x 100 % regulator sparing philosophy; quick-acting internally-sensing start-gas regulators; individual pilot isolation where pilots are external (Source: DBM-Deepcut L1866-L1868).
- Emergency-generator fuel gas supply < 66 psig during normal operation for general-purpose classification compliance; design flow 0.468 MMSCFD; start-gas flow 3.6 MMSCFD for 30 seconds, TBC (Source: DBM-Deepcut L1870).
- Buyback fuel gas regulators independent from plant main regulators; estimated buyback MAOP 9928 kPag, TBC (Source: DBM-Deepcut L1878).

### R-4 — Code Compliance Evidence
Vendor documentation SHALL provide evidence of compliance with applicable design codes (e.g., ASME pressure-vessel U-Stamp and CRN for pressure equipment; ASME B31.3 for piping; CSA / area-classification for electrical; ALPEMA where applicable) (ASSUMPTION — pressure-equipment regulatory regime; vendor scope of applicable codes TBD until vendor selection).

### R-5 — Revision Discipline
Each submittal SHALL be issued at the revision class required by the project document-control plan (e.g., IFR, IFA, IFC, As-Built). Final turnover SHALL contain the As-Built (or equivalent terminal) revision of every register entry. (ASSUMPTION — project document-control plan not locally accessible; revision class names TBD.)

### R-6 — Format
Each submittal SHALL be delivered in native editable format and in a sealed/signed PDF where required by code or project document-control plan. (ASSUMPTION — format requirement not locally specified.)

### R-7 — Turnover Records
Final turnover SHALL include preservation records, FAT/SAT records, pressure-test certificates, electrical insulation-resistance test records (where applicable), calibration certificates for all instruments delivered with the skid, and lifting/handling records as applicable. (ASSUMPTION — final list of required turnover records TBD.)

### R-8 — Interface Consistency
The Package Vendor SHALL ensure vendor documentation is consistent with EPC interface documents (P&IDs, line list, instrument index, area classification drawing, plot plan) at the time of issue. EPC Integrator review SHALL confirm interface consistency (`_CONTEXT.md` ResponsibleParty).

### R-9 — Source Vendor Document Rows as Artifacts
Where the project decomposition lists individual source vendor documents (vendor document table rows), the vendor SHALL deliver those individual documents as artifacts that satisfy register entries, rather than as separate deliverables (Source: `_CONTEXT.md` Notes).

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` heading 25 | Project-level package-requirements section for vendor document turnover | location TBD (binary source not locally readable) |
| `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 61 | Package definition row for PKG-071 | location TBD (binary source not locally readable) |
| ASME Section VIII Div. 1 (Pressure Vessel) | Pressure-containing fuel-gas-skid vessels (e.g., V-3210-1) | ASSUMPTION |
| ASME B31.3 (Process Piping) | Skid piping fabrication | ASSUMPTION |
| Provincial BC CRN | Pressure equipment registration | ASSUMPTION |
| CSA / Canadian Electrical Code; area classification | Electrical equipment on skid | ASSUMPTION |
| Project document-control plan | Revision and numbering scheme | TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Review of Vendor Document Register completeness vs PKG-071 equipment list at MC, Pre-Comm, Comm, and Hand-Over milestones. |
| R-2 | Submittal-by-submittal review against an EPC-issued required-document-list checklist (checklist content TBD). |
| R-3 | Cross-check of vendor data sheets and drawings against the Fuel Gas Basis design values (DBM-Deepcut L1843-L1903) during EPC integration review. |
| R-4 | Verification of code compliance certificates (U-Stamp letter, CRN number, electrical certifications, NDE reports). |
| R-5 | Confirmation that every register entry's final revision is at the project-defined terminal class before Hand-Over. |
| R-6 | Format check of each submittal at receipt. |
| R-7 | Inventory of turnover records against required-records checklist at Hand-Over (checklist TBD). |
| R-8 | EPC Integrator interface review per submittal. |
| R-9 | Mapping of decomposition vendor-document table rows to register entries; gap items flagged. |

## Documentation

The deliverable itself is a documentation set. The artifacts of this deliverable are:

- Vendor Document Register (single live document, version-controlled)
- Vendor document submittals (one per register entry)
- Source vendor document table rows captured as artifact entries in the register (Source: `_CONTEXT.md` Anticipated Artifacts)
- Turnover records (FAT/SAT/pressure test/calibration/preservation/lifting/etc., as applicable)
