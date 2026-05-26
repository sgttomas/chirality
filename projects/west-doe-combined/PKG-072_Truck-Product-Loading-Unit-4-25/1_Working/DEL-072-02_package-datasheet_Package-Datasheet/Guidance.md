# Guidance: DEL-072-02 Package Datasheet

## Purpose

The package datasheet exists to turn the accepted Gate 7 decomposition basis for `PKG-072` Truck Product Loading Unit 4-25 into a concise EPC Integrator technical handoff. Its role is to preserve package identity, scope, objectives, and interface facts for downstream Package Vendor engineering and design (`DEL-072-04`) and for EPC construction integration (`DEL-072-03`).

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet`; `ARTIFACT_REGISTER.csv` artifacts `ART-1E30749941`, `ART-6F113CE055`, and `ART-170CD144CD`.

## Principles

- Preserve workbook identity exactly: `PKG-072`, workbook ID 72, workbook row 99, WBS 01, Mechanical, Truck Product Loading Unit 4-25, CoA tracking number `26020-01-23-001`. Source: `PACKAGE_REGISTER.csv` row `PKG-072`.
- Preserve responsibility split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: `PACKAGE_REGISTER.csv` row `PKG-072`; `OBJECTIVE_REGISTER.csv` row `OBJ-004`.
- Carry all eleven interface facts exactly as named in the Gate 7 register; treat them as datasheet evidence and not as standalone deliverables. Source: `INTERFACE_REGISTER.csv` rows for `PKG-072`; `ARTIFACT_REGISTER.csv` interface-fact artifacts.
- Use objective mappings as context, not as mechanical/process design values. Source: `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-072-02_package-datasheet`.
- Surface the conflict between the package title and the source-row basic-scope text rather than silently selecting a single interpretation. Source: `PACKAGE_REGISTER.csv` row `PKG-072`; `SCOPE_LEDGER.csv` rows `SOW-0246`, `SOW-0247`.
- Leave unsupported dimensions, capacities, MAWP, materials, code clauses, and acceptance criteria as `TBD`. Source: `SCOPE_LEDGER.csv` row `SOW-0248`.

## Considerations

The strongest accepted facts for this deliverable are identity, the eleven interface facts, the nine mapped objectives, and the responsibility split. The Gate 7 snapshot reproduces a source-row anomaly: the package title and the workbook designation (Truck Product Loading Unit 4-25; `26020-01-PT-23-001 - Condensate Truck Loading Stations`; Product Loading interface = YES) consistently identify a truck loading station, while the basic-scope text quoted into `SOW-0246`/`SOW-0247`/`SOW-0248` describes a low-pressure fuel gas skid (heater + scrubber, > 8.4 MMSCFD design flow). Both readings cannot be true; this is captured as HRR-072-02-001 in the Conflict Table below.

Notable accessible source signals consistent with a truck loading interpretation include DBM-Deepcut/4-25_Deepcut_DBM.md citing API 2510 for distance between pressurized bullets and truck loading station, and a Deepcut DBM section requiring facility-installed ground studs at truck-out piping connections for grounding before loading.

The package maps to nine objectives:

- `OBJ-001`: 04-25 Deepcut facility scope.
- `OBJ-003`: commercial stream disposition, metering accountability, and facility boundary interfaces (truck loading explicitly named).
- `OBJ-004`: vendor-owned package execution with EPC integration review.
- `OBJ-005`: electrical power, grounding/bonding, lighting, EHT, and electrical interfaces to vendor packages.
- `OBJ-006`: controls, instrumentation, communications, fire/gas, and shutdown interfaces.
- `OBJ-007`: shared utilities and ancillary support systems including drains and building services.
- `OBJ-008`: civil, structural, site, foundations, grading, containment, access, and construction-support scope.
- `OBJ-009`: sour-service safety, drain/containment, fire/gas, environmental, regulatory, codes, and standards visibility.
- `OBJ-010`: operability (per `OBJECTIVE_REGISTER.csv` row `OBJ-010`).

Sources: `OBJECTIVE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-072-02_package-datasheet`.

## Trade-offs

| Topic | Conservative handling | Reason |
|---|---|---|
| Package-name vs source-row-text conflict | Carry both readings, mark numeric values as ASSUMPTION (CONFLICT), and require human ruling. | Choosing either reading silently would either invent truck-loading equipment values or overwrite the workbook package title. |
| Design / operating values from `SOW-0248` | Quote verbatim with explicit source pointer; mark MAWP and final flow as `TBD`. | The source row text itself marks them `TBD`. |
| Interface facts | Carry all eleven names exactly as recorded; do not collapse or rename. | `INTERFACE_REGISTER.csv` is the accepted register basis. |
| Standards / codes | Cite API 2510 from the DBM where directly supported; mark loading-specific codes (metering, static electricity, grounding) as `TBD` at clause level. | Only the DBM-cited spacing/grounding text is directly accessible; broader code clauses are not extracted. |
| Responsibility model | Keep Package Vendor as engineering/design/equipment owner and EPC Integrator as integrator; do not re-assign vendor work to EPC. | `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, and `OBJ-004` jointly fix this split. |

## Examples

TBD - no truck-loading-station datasheet exemplar exists yet in this project workspace; the closest sibling (`PKG-099_Truck-Product-Loading-Unit-3-25` for the 3-25 facility) has not yet been initialized.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-072-02-001 | Package name and CoA tracking identify a truck loading station, but the basic-scope text quoted into the workbook describes a fuel-gas skid. | `PACKAGE_REGISTER.csv` row `PKG-072` (PackageName = "Truck Product Loading Unit 4-25"; CoA `26020-01-23-001`; Product Loading interface = YES); `INTERFACE_REGISTER.csv` `IFC-E3B7B98B0B`; sibling row `PKG-099` for 3-25 Truck Loading | `SCOPE_LEDGER.csv` rows `SOW-0246`, `SOW-0247`, `SOW-0248` quoting "Low Pressure Fuel Gas Package" and a fuel-gas heater/scrubber with > 8.4 MMSCFD design flow; 26020-Package_Requirements.docx package heading 26 (Source Basis references `26020-01-PT-RFQ-23-001_FG_Skid_2.docx`) | Datasheet Attributes (Major included equipment); Datasheet Conditions (Design flow); Specification Requirements REQ-072-02-007; Procedure Steps 7-9 | Treat the package title and `26020-01-PT-23-001 - Condensate Truck Loading Stations` heading as authoritative for package identity; treat the basic-scope text as a likely upstream source-document copy-paste error to be reconciled by the human; do not propagate fuel-gas equipment values as truck-loading values without confirmation. | TBD |
| HRR-072-02-002 | Detailed truck-loading design criteria (number of loading bays, pump count and duty, meter sizing, vapor recovery routing, loading-arm configuration, secondary containment volume, grounding-stud layout) are required for a usable datasheet but are not present in the Gate 7 accepted snapshot. | `DELIVERABLE_REGISTER.csv` row `DEL-072-02_package-datasheet`; `ARTIFACT_REGISTER.csv` artifact `ART-6F113CE055` requires "technical basis, battery limits, design expectations, and source-supported requirements." | `PACKAGE_REGISTER.csv` row `PKG-072`; `SCOPE_LEDGER.csv` row `SOW-0248` (multiple `TBD` markers); 26020-Package_Requirements.docx package heading 26 Interface Coordination Notes = TBD | Datasheet Construction (Major equipment construction criteria, Codes and standards); Specification Standards | Hold detailed truck-loading design criteria as `TBD` pending approved source slice (sibling `PKG-099` source basis `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` may be applicable by analogy) or human ruling. | TBD |
