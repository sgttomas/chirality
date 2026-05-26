# Datasheet — DEL-063-01 Scope of Work (PKG-063 Tanks, DSO (API 650))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-063-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-063` — Tanks, DSO (API 650) | `PACKAGE_REGISTER.csv` row 90 |
| Workbook Row | 90 | `PACKAGE_REGISTER.csv` (WorkbookRow=90) |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-19-001 (also reported as 26020-01-PT-19-001) | `PACKAGE_REGISTER.csv`; `Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` (file-name evidence) |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply one (1) atmospheric disulphide oil (DSO) storage tank. Tank receives separated DSO from the DSO separator (level-controlled) within the caustic regeneration system. | `SCOPE_LEDGER.csv` SOW-0210; `26020-Package_Requirements.docx` package heading 18 (Basic scope) |
| Major Equipment | DSO Storage Tank — Design and fabrication to modified API 650; 400 bbl nominal capacity; atmospheric pressure tank; design pressure 32 oz, 1.0 oz vacuum; complete with heater (vendor to design) sized to 32.2 °C (90 °F) minimum; internally coated (floor, walls, roof); insulated to maintain DSO above pour point for truck-out and handling (minimum temperature TBD). | `SCOPE_LEDGER.csv` SOW-0211; `26020-Package_Requirements.docx` package heading 18 (Major included equipment); corroborated by `DBM-Deepcut/4-25_Deepcut_DBM.md` Disposition / Tank disposition table (400 bbl DSO storage tank for truck-out and disposal) |
| Process Integration | DSO is a by-product of the NGL non-regenerative caustic treating process; the tank stores recovered DSO for truck-out and disposal. Alternate mixing of recovered DSO into C5+ product is identified as a possible disposal path, to be reviewed during detailed engineering. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (Disulphide oil disposition paragraph; open-issues table "DSO disposal: review alternate DSO mixing into C5+ product") |
| Scope Notes / By-Others | By others: foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. Capacity/design throughput: TBC. Operating conditions: not stated in source slice. Design conditions: atmospheric; minimum ambient temperature TBD; design pressure 32 oz, 1.0 oz vacuum; flow rate TBD; 400 bbl. | `SCOPE_LEDGER.csv` SOW-0212; `26020-Package_Requirements.docx` package heading 18 (Scope notes and open items) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). | `PACKAGE_REGISTER.csv` PKG-063 ResponsibilityModel; ART-42CDF63E00 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Atmospheric disulphide oil (DSO) storage; receives level-controlled DSO from the DSO separator in the caustic regeneration system. Sour-service classification at the package level: ASSUMPTION (DSO is a mercaptan-derived by-product associated with sour-service NGL caustic treating per the 04-25 DBM). | `SCOPE_LEDGER.csv` SOW-0210; `DBM-Deepcut/4-25_Deepcut_DBM.md` (Disulphide oil paragraph); `OBJ-009` |
| Design pressure | 32 oz (positive); 1.0 oz vacuum | `SCOPE_LEDGER.csv` SOW-0211, SOW-0212; `26020-Package_Requirements.docx` package heading 18 |
| Design / heating temperature | Heater sized for 32.2 °C (90 °F) minimum (vendor to design heater); insulated to maintain DSO above pour point — minimum temperature TBD | `SCOPE_LEDGER.csv` SOW-0211 |
| Nominal capacity | 400 bbl | `SCOPE_LEDGER.csv` SOW-0211, SOW-0212; `DBM-Deepcut/4-25_Deepcut_DBM.md` (400 bbl DSO storage tank) |
| Operating regime | Continuous storage of recovered DSO with periodic truck-out; design throughput TBC; operating flow rate TBD | `SCOPE_LEDGER.csv` SOW-0212 |
| Materials of construction | Tank internals coated (floor, walls, roof); coating system specification — location TBD (the 04-25 DBM cites "Devchem 253" for produced-water tanks; DSO tank coating product is not stated in the source slice). | `SCOPE_LEDGER.csv` SOW-0211; coating product TBD — location TBD in `26020-Package_Requirements.docx` package heading 18 |
| Maximum fill / overfill protection | TBD — location TBD (the 04-25 DBM states 90% maximum fill with thermal-expansion review for produced-water tanks; not stated for DSO tank). | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. By-others list (per SOW-0212) explicitly carves out: foundations, on-site mounting, electrical/instrumentation, platforms, and staircase. | `PACKAGE_REGISTER.csv` ResponsibilityModel; `SCOPE_LEDGER.csv` SOW-0212 |
| Applicable interface types (package boundary integration) | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-063 rows (IFC-B8225E1CAC, IFC-55319DFCC3, IFC-976437DD6E, IFC-F0E7550CA2, IFC-BDDC5F17F1, IFC-89C542835E, IFC-289323FEB4, IFC-391B72231B, IFC-DFD52CFB01); `PACKAGE_REGISTER.csv` InterfaceTypes |
| Internal coating | Floor, walls, and roof internally coated. | `SCOPE_LEDGER.csv` SOW-0211 |
| Insulation / heat tracing | External insulation required to maintain DSO above its pour point for truck-out and handling; vendor-designed heater (32.2 °C / 90 °F minimum). Whether heating is internal coil, external EHT, or both — TBD; location TBD. | `SCOPE_LEDGER.csv` SOW-0211 |
| Tank standard | Modified API 650 atmospheric tank. | `SCOPE_LEDGER.csv` SOW-0211 |
| Truck-out / disposal | Tank designed for truck-out; alternate disposal path (mixing recovered DSO into C5+ product) flagged as open item for detailed engineering. | `SCOPE_LEDGER.csv` SOW-0211; `DBM-Deepcut/4-25_Deepcut_DBM.md` (DSO disposal open issue) |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0209` | Carry the workbook-defined vendor-responsible Mechanical package "Tanks, DSO (API 650)" as a distinct flat project package for WBS 01; Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration. |
| `SOW-0210` | Basic scope: Supply one (1) atmospheric DSO storage tank; tank receives separated DSO from the DSO separator (level-controlled) within the caustic regeneration system. |
| `SOW-0211` | Major included equipment: DSO Storage Tank; modified API 650; 400 bbl nominal; atmospheric; design pressure 32 oz, 1.0 oz vacuum; c/w heater at 32.2 °C (90 °F) minimum (vendor-designed); internally coated (floor/walls/roof); insulated for pour-point maintenance (minimum temperature TBD). |
| `SOW-0212` | Scope notes / open items: by-others (foundations, site mounting, E&I, platforms, staircase); capacity/throughput TBC; operating conditions not stated; design conditions atmospheric with minimum ambient TBD; flow rate TBD; 400 bbl. |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Statement (short) | Source |
|---|---|---|
| `OBJ-001` | Provide the 04-25 Deepcut facility scope (sour gas processing through inlet separation, stabilization, compression, amine, dehydration, cryogenic recovery, product handling, acid-gas, and supporting systems). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-003` | Preserve commercial stream disposition, metering accountability, and facility boundary interfaces (truck-out, cross-facility exchanges). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-004` | Execute electrical/mechanical packages as vendor-owned with EPC integration review preserved as separate responsibilities. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-005` | Provide and integrate facility electrical power basis and interfaces to vendor packages (grounding, lighting, cathodic protection relevant to tankage). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-006` | Provide and integrate controls, instrumentation, and package control interfaces (level control from DSO separator). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-007` | Provide and integrate shared utilities and ancillary support systems (heat medium, drains, vents). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-008` | Provide civil, structural, site, foundations, grading, containment, and access scope (by-others for this package). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-009` | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, regulatory, codes, and standards requirements. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-010` | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure evidence. | `OBJECTIVE_REGISTER.csv` |

Objective association mode: PACKAGE_HEURISTIC (configured); however `OBJECTIVE_DELIVERABLE_MAP.csv` maps every listed objective explicitly to `DEL-063-01_scope-of-work`, so the association here is an explicit mapping rather than a heuristic-only association.

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv` (ART-8D38072F13, ART-469823FD54, ART-B502E838FB, ART-42CDF63E00, ART-A0E63EAD7C), `INTERFACE_REGISTER.csv` (nine PKG-063 rows), `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 90; `26020-Package_Requirements.docx` package heading 18; `Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` (budgetary RFQ go-by, informational only); `DBM-Deepcut/4-25_Deepcut_DBM.md` (accessible at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — provides DSO disposition context, 400 bbl tank confirmation, and DSO-disposal open issue).
- Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION (per `_REFERENCES.md`); clause-level extraction beyond `SCOPE_LEDGER.csv` rows SOW-0209..SOW-0212 and the DBM disulphide-oil paragraph is marked `location TBD` above.
