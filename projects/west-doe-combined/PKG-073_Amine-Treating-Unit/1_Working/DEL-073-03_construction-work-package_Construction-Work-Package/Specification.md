# Specification — DEL-073-03 Construction Work Package (PKG-073 Amine Treating Unit)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for PKG-073 Amine Treating Unit at the 04-25 Deepcut Gas Plant. The CWP defines how the vendor-supplied Amine Treating Unit (Module 1 — Amine Gas Sweetening; Module 2 — Amine Regeneration) is physically installed, built, inspected, turned over, and tied into facility systems. The CWP covers SOW-0051 through SOW-0054.

**In scope:**
- Site receipt, set, and installation of the vendor ATU package (skids, columns, exchangers, pumps, tanks, instruments, and electrical/I&C cabling internal to the package).
- Field tie-in scope across the interfaces identified for PKG-073: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. (Source: PROJECT_DECOMP PACKAGE_REGISTER PKG-073, "Applicable interface types".)
- Construction inspection, NDE, pressure testing, leak/tightness testing, system cleaning/flushing, electrical and instrument loop checkout supporting mechanical completion and turnover.
- Construction interface management with adjacent packages (inlet compression, TEG dehydration, acid gas handling, flare, utilities) and turnover handoff to commissioning.

**Out of scope:**
- Package process engineering, package detailed design, and vendor documentation — owned by Package Vendor under DEL-073-04 and DEL-073-05.
- Vendor package acceptance evidence and integration review — owned under DEL-073-06.
- Commissioning, start-up, and operational acceptance after turnover.
- Off-package scope items beyond PKG-073 boundaries.

## Requirements

| ID | Requirement | Source / Basis | Notes |
|---|---|---|---|
| REQ-CWP-01 | The CWP shall identify all tagged equipment items in PKG-073 (absorbers, regenerator, reboiler, flash drum, exchangers, filters, pumps, surge tank, accumulator, coalescers, tanks) and trace each to its installed location and vendor drawing. | DBM-Deepcut Amine Treating Unit equipment list | ASSUMPTION: tag list per Datasheet Construction table; vendor general arrangement to confirm. |
| REQ-CWP-02 | Installation sequencing shall preserve the absorber configuration of 2 × 50% upflow contactors with their inlet coalescer trains (2 × 100%) and demisters, including line-of-sight access for internal demister/distributor inspection prior to closure. | DBM-Deepcut "Amine Equipment and Design Requirements" | |
| REQ-CWP-03 | Lean/rich amine plate-and-frame exchangers (2 × 50%) shall be set with provisions for plate removal and gasket replacement; required maintenance envelopes shall be coordinated with the plot plan. | DBM-Deepcut, Sec. 2.3 maintainability basis | |
| REQ-CWP-04 | Amine regenerator (20 actual trays) shall be installed with manway access at each water-wash stage and with internals protected against debris ingress until system flushing is complete. | DBM-Deepcut "Amine Equipment and Design Requirements" | |
| REQ-CWP-05 | Amine reboiler hot-oil tie-ins shall be installed for 350 °F supply-side service with provision for heat-medium mixing valves limiting amine-side skin temperature to ≤350 °F. | DBM-Deepcut "Amine Equipment and Design Requirements" | |
| REQ-CWP-06 | Surge tank installation shall include LP fuel-gas blanket connection, secondary containment, truck-out connection, insulation and heater provisions, and hydrocarbon skim outlet routing. | DBM-Deepcut "Amine Equipment and Design Requirements" | |
| REQ-CWP-07 | All pressure-containing tie-ins on amine, sour gas, sweet gas, acid gas, and flare service shall be hydrotested or system-tested per the EPC pressure-test plan; test pressures and media are TBD until detailed P&ID/line-list issue. | Inferred from REQ-CWP scope; ASSUMPTION pending plant test specification | |
| REQ-CWP-08 | Field tie-ins shall be installed for each interface type identified for PKG-073 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). | PROJECT_DECOMP PACKAGE_REGISTER PKG-073 | |
| REQ-CWP-09 | The CWP shall include a workface plan covering crew composition, work-pack sequencing, lay-down and crane plans, hot-work boundaries, simultaneous-operations (SIMOPS) management, and constraint sign-off. | `_CONTEXT.md` Anticipated Artifacts ("installation and tie-in workface plan") | Detailed contents TBD against EPC execution standards. |
| REQ-CWP-10 | The CWP shall include a construction interface and turnover checklist covering mechanical completion punch lists, NDE/PWHT records (where applicable), instrument loop-check records, electrical megger/continuity records, and turnover witness sign-off. | `_CONTEXT.md` Anticipated Artifacts ("construction interface and turnover checklist") | |
| REQ-CWP-11 | Site environmental loads (design ambient -40 °C / +35 °C; extreme -49.2 °C / +38.9 °C) shall be respected in installation specifications, including cold-weather welding, hydrotest freeze protection, and EHT installation acceptance. | DBM-Deepcut Sec. 2 site basis | |
| REQ-CWP-12 | Construction work shall not commence on any tie-in until DEL-073-01 (Scope of Work), DEL-073-02 (Package Datasheet), and the vendor general arrangement and P&ID issue under DEL-073-04 are at or above the maturity threshold required by the EPC integrator. | DELIVERABLE_REGISTER rows 258–261; ASSUMPTION on maturity gate | Specific maturity threshold TBD. |
| REQ-CWP-13 | Construction turnover into commissioning shall be supported by the vendor turnover document set produced under DEL-073-05 and accepted under DEL-073-06. | DELIVERABLE_REGISTER rows 262–263 | |

## Standards

| Standard / Reference | Applicability | Locally Accessible? | Notes |
|---|---|---|---|
| ASME B31.3 — Process Piping | Sour gas, sweet gas, amine, hot-oil, utility piping installation, fabrication, examination, and testing. | No (location TBD) | ASSUMPTION: standard jurisdictional default for the discipline; to be confirmed against EPC piping specification. |
| ASME BPVC Section VIII | Pressure vessels (absorbers, flash drum, surge tank, accumulator). | No (location TBD) | ASSUMPTION pending vendor data; specific code stamp jurisdiction to be confirmed. |
| API 610 | Amine charge pumps (multi-stage horizontal centrifugal, axial-split casing). | No (location TBD) | Cited as basis in DBM-Deepcut "Amine Equipment and Design Requirements". |
| Provincial OH&S, Boiler & Pressure Vessel Regulation (BC; jurisdiction TBC) | Construction safety, pressure-equipment registration, welder/procedure qualification. | No (location TBD) | ASSUMPTION: 04-25 Deepcut Plant facility located in BC per DBM context; jurisdiction to be confirmed. |
| 26020-Package_Requirements.docx (Package heading 27) | Owner package requirements for ATU. | Binary; not text-accessible | location TBD — clause-level requirements cannot be extracted from this run. |
| 26020-Packages_Interfaces_4_export.xlsx | Package/interface workbook reference. | Binary; not text-accessible | location TBD. |

## Verification

| REQ | Verification Method | Verification Evidence |
|---|---|---|
| REQ-CWP-01 | Document review of equipment register vs. vendor BOM and tag list. | Equipment register cross-walk; redline of vendor general arrangement. |
| REQ-CWP-02 | Inspection witness at column setting; pre-closure inspection of demisters/distributors. | Inspection records (ITP hold/witness points). |
| REQ-CWP-03 | Field walkdown post-installation; maintenance envelope check vs. plot plan. | Walkdown report; envelope check sign-off. |
| REQ-CWP-04 | Manway access inspection; debris-prevention closeout sign-off prior to flushing. | ITP records; closure log. |
| REQ-CWP-05 | Functional check of heat-medium mixing-valve setpoint; instrument calibration record. | Loop-check record; setpoint verification log. |
| REQ-CWP-06 | Visual and functional inspection of surge-tank ancillaries; secondary containment integrity test. | Containment test record; ancillary checkout list. |
| REQ-CWP-07 | Pressure/leak test execution per EPC pressure-test plan (TBD). | Hydrotest/leak-test records (test packs). |
| REQ-CWP-08 | Tie-in completion checklist per interface type; mechanical completion punch-list closeout. | Interface completion records; punch-list. |
| REQ-CWP-09 | Workface-plan review and approval prior to mobilization. | Approved workface plan document. |
| REQ-CWP-10 | Turnover checklist closeout, including NDE/loop-check/electrical records. | Turnover dossier (MC certificate). |
| REQ-CWP-11 | Verification of cold-weather welding procedures, hydrotest freeze plan, and EHT installation acceptance records. | WPS/PQR records; EHT installation acceptance. |
| REQ-CWP-12 | Document maturity check against upstream DEL-073-01/02/04 status. | Maturity checklist; sign-off prior to tie-in. |
| REQ-CWP-13 | Confirm DEL-073-05 turnover dossier accepted under DEL-073-06 prior to commissioning handoff. | Acceptance evidence (DEL-073-06 sign-off). |

## Documentation

The CWP deliverable comprises the following anticipated artifacts (per `_CONTEXT.md`):

1. **Construction work package** — the primary CWP document, including scope, equipment list, tie-in list, ITPs, safety and environmental plans, and references to vendor and EPC engineering documents.
2. **Installation and tie-in workface plan** — sequenced workface plans, crew/crane/lay-down plans, SIMOPS management, hot-work coordination, and constraint sign-off log.
3. **Construction interface and turnover checklist** — mechanical completion punch list, NDE/PWHT records, instrument loop-check records, electrical records, interface signoffs, and turnover witness sign-off enabling handoff to commissioning.

Supporting record sets (created during execution, not always carried in this deliverable) include ITP records, test packs, and weld registers.
