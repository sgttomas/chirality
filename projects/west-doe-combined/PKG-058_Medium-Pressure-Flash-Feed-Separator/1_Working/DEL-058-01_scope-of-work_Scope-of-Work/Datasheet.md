# Datasheet — DEL-058-01 Scope of Work (PKG-058 Medium Pressure Flash Feed Separator)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-058-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-058` — Medium Pressure Flash Feed Separator | `PACKAGE_REGISTER.csv` row 71 |
| Workbook Row | 71 | `PACKAGE_REGISTER.csv` (WorkbookRow=71) |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-17-006 (also reported as 26020-01-PT-17-006) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply one (1) Medium Pressure Flash Feed (MPFF) Separator — Two Phase. The MPFF flashes light hydrocarbon vapours from the inlet separator raw condensate to minimize/reduce stabilizer overheads compressor re-compression power. Flashed overhead vapours are pressure controlled to the stabilizer overheads compressor (SOC) 3rd stage suction. Bottoms liquids (condensate) are level controlled. | `SCOPE_LEDGER.csv` SOW-0140; `26020-Package_Requirements.docx` package heading 13 (Basic scope) |
| Major Equipment | One (1) Medium Pressure Flash Feed (MPFF) Separator — Two Phase; fitted with a mistex mist extractor; heated self-framing building module enclosing instrumentation and one vessel end; two (2) PITs; one (1) TIT; one (1) LT for condensate level; one (1) LT for produced water level; one (1) inlet LCV. | `SCOPE_LEDGER.csv` SOW-0141; `ARTIFACT_REGISTER.csv` ART-92F99F284F; `26020-Package_Requirements.docx` package heading 13 (Major included equipment) |
| Tag Identifiers (per facility DBM) | `V-7110-1` and `V-7310-1` (one MPFF vessel per inlet-liquids train; normal operating sparing 2 x 100%). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF and Stabilizer Train Relationship; tag table) — ASSUMPTION: vessel tag binding is from the facility DBM and not the package requirements clause |
| Scope Notes (process integration / by-others / capacities / operating / design conditions) | By others: interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, and installation/erection. Capacity/design throughput — Normal Throughput: 7,883 m³/h; Maximum Throughput: 15,223 m³/h. Operating conditions — Pressure: 1,724 kPag; Inlet Flow rate: 7,883 m³/h; Temperature: −9.55 °C. Design conditions — Design Pressure: TBD; Flange Rating: ASME Class 300; Inlet Flow Rate: 15,223 m³/h; Design Temperature: −40 °C. | `SCOPE_LEDGER.csv` SOW-0142; `26020-Package_Requirements.docx` package heading 13 (Scope notes and open items) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). | `PACKAGE_REGISTER.csv` PKG-058 ResponsibilityModel; `ARTIFACT_REGISTER.csv` ART-2F011685B1 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Two-phase separation of light hydrocarbon vapours from raw condensate; sour service is inferred from facility basis (`OBJ-001`, `OBJ-009`). | `SCOPE_LEDGER.csv` SOW-0140; `PACKAGE_REGISTER.csv` PackageDescription — ASSUMPTION on sour-service classification at the package level |
| Operating Pressure | 1,724 kPag | `SCOPE_LEDGER.csv` SOW-0142 (Operating conditions) |
| Operating Inlet Flow Rate (normal) | 7,883 m³/h | `SCOPE_LEDGER.csv` SOW-0142 |
| Operating Inlet Temperature | −9.55 °C | `SCOPE_LEDGER.csv` SOW-0142 — CONFLICT: facility DBM (`4-25_Deepcut_DBM.md` MPFF section) indicates MPFF inlet temperatures are TBD/TBC pending upstream HEX thermal reassessment and an assumed 40 °C operating temperature pending detailed engineering; see Guidance Conflict Table |
| Maximum / Design Inlet Flow Rate | 15,223 m³/h | `SCOPE_LEDGER.csv` SOW-0142 |
| Design Temperature | −40 °C | `SCOPE_LEDGER.csv` SOW-0142 |
| Design Pressure | TBD | `SCOPE_LEDGER.csv` SOW-0142 (stated as TBD in source) |
| Flange Rating | ASME Class 300 | `SCOPE_LEDGER.csv` SOW-0142 |
| Vessel Internals | Mistex mist extractor; no internal coating specified in accessible sources. | `SCOPE_LEDGER.csv` SOW-0141; `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF internals are Mistex; no internal coating specified) |
| Residence Time | At least 10 minutes of liquid residence time between the weir height and NLL-interface (per facility DBM). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF operating and capacity basis) |
| Materials of Construction | TBD | location TBD — `26020-Package_Requirements.docx` package heading 13 detail text |
| Sizing/Vessel Geometry | TBD | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Package Boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. Skid-edge piping, DCS integration, foundations, electrical power from plant MCC, and installation/erection are explicitly "by others". | `PACKAGE_REGISTER.csv` ResponsibilityModel; `SCOPE_LEDGER.csv` SOW-0142 (By others) |
| Applicable Interface Types (package boundary integration) | Process Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-058 rows (nine rows); `PACKAGE_REGISTER.csv` InterfaceTypes |
| Package Enclosure | Heated self-framing building module enclosing instrumentation and one vessel end. | `SCOPE_LEDGER.csv` SOW-0141; `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF package configured similarly to inlet separator with self-framing building enclosing instrumentation and one end of the vessel) |
| Heat Tracing | EHT interface is declared at the package boundary; specific trace circuits TBD at SOW level. | `INTERFACE_REGISTER.csv` PKG-058 (EHT) |
| Drains/Containment | Drain / Containment interface declared; specific routing to closed hydrocarbon drain and produced-water handling resolved at facility integration. | `INTERFACE_REGISTER.csv` PKG-058 (Drain / Containment); `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF interfaces) |
| Automated Blowdown | An automated blowdown valve is required (per facility DBM). | `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF section) |
| Low-Pressure Fuel Gas Purge | LP fuel gas downstream of fuel-gas scrubber supplies MPFF purge gas; pressure regulated to maintain MPFF pressure above downstream stabilizer flash/feed separator; available for sour-gas sweeping during maintenance. | `DBM-Deepcut/4-25_Deepcut_DBM.md` (MPFF section) — ASSUMPTION: described in facility DBM, not in the package requirements clause |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0139` | Carry workbook-defined vendor-responsible Mechanical package "Medium Pressure Flash Feed Separator" as a distinct flat project package for WBS 01. |
| `SOW-0140` | Basic scope: Supply one (1) MPFF Separator — Two Phase; flashes light hydrocarbon vapours from inlet separator raw condensate; overhead to SOC 3rd-stage suction (pressure controlled); bottoms condensate level controlled. |
| `SOW-0141` | Major included equipment: one (1) MPFF Separator — Two Phase; mistex mist extractor; heated self-framing building module; 2 PITs; 1 TIT; 1 LT (condensate level); 1 LT (produced water level); 1 inlet LCV. |
| `SOW-0142` | Scope notes/open items: by-others scope; capacity/design throughput; operating conditions; design conditions (Design Pressure TBD; ASME Class 300 flange rating; −40 °C design temperature). |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Statement (short) | Source |
|---|---|---|
| `OBJ-001` | Provide the 04-25 Deepcut facility scope (sour gas processing). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-004` | Execute each electrical/mechanical equipment package with vendor and EPC responsibilities preserved. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-005` | Provide and integrate facility electrical power basis and interfaces to vendor packages. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-006` | Provide and integrate controls, instrumentation, and package control interfaces. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-007` | Provide and integrate shared utilities and ancillary support systems (including flare/blowdown/vent, drains). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-008` | Provide civil, structural, site, foundations, access, and construction-support scope. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-009` | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, regulatory, codes, and standards requirements. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-010` | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure. | `OBJECTIVE_REGISTER.csv` |

Objective association mode: PACKAGE_HEURISTIC (the brief specified PACKAGE_HEURISTIC; objectives are also explicitly mapped at the deliverable-ID level in `OBJECTIVE_DELIVERABLE_MAP.csv` for `DEL-058-01_scope-of-work` — this is therefore an explicit mapping, not a heuristic-only association).

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 71; `26020-Package_Requirements.docx` package heading 13; Word Source Basis `Bid Docs/Budgetary/26020-01-PT-RFQ-17-006_MPFF Separator_R0.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible markdown).
- Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION (per `_REFERENCES.md`); clause-level extraction beyond the SCOPE_LEDGER entries and DBM slices is marked `location TBD`.
