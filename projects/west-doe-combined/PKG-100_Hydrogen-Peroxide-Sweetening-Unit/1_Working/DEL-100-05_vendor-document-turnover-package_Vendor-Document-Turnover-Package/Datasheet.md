# Datasheet: DEL-100-05 — Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-100-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-100` |
| Package | Hydrogen Peroxide Sweetening Unit |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (producer) with EPC Integrator (interface/integration review) |
| Authoritative Basis | GATE-07 PROJECT_DECOMP snapshot 2026-05-24 |

Source: `_CONTEXT.md` (FACT).

## Attributes

| Attribute | Value | Source / Status |
|---|---|---|
| Subject equipment package | Sour-water hydrogen peroxide treatment package (Hydrogen Peroxide Pumps, Hydrogen Peroxide Reactors, Static Mixer) | `PACKAGE_REGISTER.csv` row 63 (Specification field); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 line 216 (FACT) |
| Process function (context) | Sour water passes through static mixer then Hydrogen Peroxide Reactors for treatment; H2O2 is pumped in from H2O2 storage tank; treated water is sent to produced-water storage tanks | `PACKAGE_REGISTER.csv` row 63 Specification field (FACT) |
| Package capacity (context) | One H2O2 treatment package, 3,840 m3/d (TBC per DBM) | DBM SEC-06 line 427 (FACT, TBC in source) |
| Companion H2O2 storage | One 400 bbl H2O2 storage tank (out of this deliverable scope; context for documentation set) | DBM SEC-06 lines 216, 428 (FACT) |
| Vendor document register | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts; DBM SEC-09 line 617 ("Package deliverables shall include … vendor document registers") (FACT) |
| Vendor document submittals | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts (FACT) |
| Source vendor document rows (as artifacts) | Required where available; carried as evidence under register rows, not as separate deliverables | `_CONTEXT.md` Notes; `_CONTEXT.md` Anticipated Artifacts (FACT) |
| Turnover records | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts (FACT) |
| Vendor document register contents (line items) | TBD — source `26020-Package_Requirements.docx` package heading 52 not locally parseable | location TBD |
| Submittal list / required vendor document classes | TBD (ASSUMPTION: typical classes include datasheets, GA drawings, P&IDs, electrical schematics, control narrative / cause-and-effect, IOM manuals, QA/QC dossiers, MTRs, FAT/SAT records, spare parts list, training material, warranty) | location TBD; ASSUMPTION |
| Turnover record set | TBD (ASSUMPTION: typical scope includes as-built drawings, completed punch list, signed FAT/SAT reports, calibration certificates, system handover certificate) | location TBD; ASSUMPTION |
| Scope items covered | `SOW-0107`, `SOW-0108`, `SOW-0109`, `SOW-0110` | `_CONTEXT.md` (FACT) |
| Objectives supported (package-grouping heuristic) | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; ASSUMPTION (PACKAGE_HEURISTIC association) |
| Coordination mode | DECLARED; no declared upstream/downstream dependencies at PREPARATION | `_DEPENDENCIES.md` (FACT) |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Site ambient minimum (design envelope context) | -40 deg C governs exposed equipment, package buildings, control panels, and instrumentation unless a more severe process/vendor condition applies | DBM SEC-02 / SEC-09 (line 145) (FACT) |
| Service class | Sour-water treatment service (oxidative sulfide reduction via H2O2 dosing) | DBM SEC-06 lines 214-216 (FACT) |
| Chemical handled | Hydrogen peroxide (H2O2) — oxidizer; safety-critical chemical handling implications for vendor documentation | DBM SEC-06 lines 214-216, 427-428 (FACT) |
| Interface types in scope (package-level) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row 63 Interface_Types_Applicable (FACT) |
| Submission lifecycle | Documents progress from vendor submittal through review/comment cycles to accepted turnover records | ASSUMPTION (industry convention); source location TBD in `26020-Package_Requirements.docx` heading 52 |
| EPC interface | EPC Integrator performs interface/integration review of vendor documents | `_CONTEXT.md` ResponsibleParty (FACT) |

## Construction

This deliverable is a documentation package, not a physical construction item. The "construction" attributes below describe the vendor-supplied equipment whose documentation is collected and the documentation-set structure itself.

| Element | Description | Source / Status |
|---|---|---|
| Equipment class | Mechanical package — H2O2 sweetening (pumps, reactors, static mixer) | `PACKAGE_REGISTER.csv` row 63 Specification; DBM SEC-06 line 216 (FACT) |
| Vendor scope boundary discipline | Clear scope boundaries among process vendors, electrical/controls, field construction, and cross-facility utility interfaces | DBM SEC-09 line 617 (FACT) |
| Vendor Document Register | Tabular index of all required vendor documents for PKG-100: document number, title, type, revision, submittal status, review status, turnover status, applicable SOW item(s) | DBM SEC-09 line 617 (register requirement is FACT); column set is ASSUMPTION (industry convention) until heading-52 accessible |
| Vendor Document Submittals | The vendor-produced document set submitted against the register (datasheets, drawings, calculations, certifications, manuals, test records) | `_CONTEXT.md`; specific list TBD pending `26020-Package_Requirements.docx` heading 52 |
| Source-Required Vendor Documentation | Documents that the source (`26020-Package_Requirements.docx` heading 52) explicitly requires for this package class | location TBD (docx not converted to accessible markdown in workspace) |
| Turnover Records | Final accepted/closed document set, transmittal manifests, and acceptance evidence transferred at package turnover | `_CONTEXT.md` Anticipated Artifacts (FACT) |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally accessible; SEC-01 line 22, SEC-06 lines 214-216, 427-428, SEC-09 line 617 consulted)
- `_Sources/26020-Package_Requirements.docx`, package heading 52 — referenced by `_CONTEXT.md`; NOT locally parseable as markdown; clause-level content **TBD**
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 63 — referenced by `PACKAGE_REGISTER.csv`; NOT locally parseable; interface-level details **TBD**
- GATE-07 PROJECT_DECOMP snapshot 2026-05-24 (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`)
