# Datasheet — DEL-060-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-060-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-060` (Workbook row 85) |
| PackageName | Tank Farm Pump Building 4-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| FacilityIdentifier | 04-25 — West Doe Deepcut expansion (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SectionRef: SEC-01 Facility Identity) |
| ScopeItemsCovered | SOW-0189; SOW-0190; SOW-0191; SOW-0192 (SourcePath: GATE-07 `SCOPE_LEDGER.csv`) |
| ObjectivesSupported | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic via `OBJECTIVE_PACKAGE_MAP.csv`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Construction execution authority | Tourmaline Oil Corporation field construction scope; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination | DBM-Deepcut SEC-01 Construction Responsibility; `PACKAGE_REGISTER.csv` PKG-060 |
| Package contents to be installed | (2x) Water Transfer Pump P-9290-1 / P-9293-1 (radial centrifugal, single mechanical seal); (2x) Condensate Transfer Pump P-9210-1 / P-9220-1 (axial flow multistage horizontal centrifugal, API-682 14/52 seal plan); (1x) Condensate Recycle Pump P-9200-1 (Hydrocell diaphragm positive displacement, sealless, with discharge pulsation dampener and inlet strainer); (2x) process water transfer radial centrifugal pumps (vendor-designed); (2x) fresh caustic transfer radial centrifugal pumps (vendor-designed, corrosive service, no aluminium); self-framing building erected at site | `SCOPE_LEDGER.csv` SOW-0191 |
| Construction-relevant utility / driver basis | 575 V / 3 ph / 60 Hz motors; DOL or VFD starting; local control (H-O-A or On-Off); fed from 600 V MCC; motors sized for inlet stabilizer composition density at -40 °C start-up | `SCOPE_LEDGER.csv` SOW-0192 |
| By-others scope at construction interface | DCS integration, foundations, electrical supply to MCC (vendor "by others") | `SCOPE_LEDGER.csv` SOW-0192 |
| Anticipated produced artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` (ART-F8F13A9988, ART-538DFF5CDE, ART-4CE1B9B840) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site location | LSD 04-25-80-15 W6M, approximately 22.2 km north of Dawson Creek, BC | DBM-Deepcut SEC-01 / SEC-02.2 |
| Plant elevation | 673 m AMSL | DBM-Deepcut SEC-02.2 |
| Design ambient temperature | -40 °C minimum; +35 °C maximum | DBM-Deepcut SEC-02.2 |
| Extreme ambient temperature | -49.2 °C minimum; +38.9 °C maximum | DBM-Deepcut SEC-02.2 |
| Prevailing wind | SW in winter; W in summer; 14 km/h mean; 138 km/h maximum (TBC) | DBM-Deepcut SEC-02.2 |
| Building type | Self-framing erected on site | SOW-0191 |
| Construction phasing | Single phase, single train | DBM-Deepcut SEC-01 |

## Construction (Installation and Tie-In Basis)

| Item | Construction-responsibility basis | Source |
|---|---|---|
| Grading, piling, foundations | Tourmaline field construction scope (foundations are flagged "by others" relative to the package vendor) | DBM-Deepcut SEC-01 Construction Responsibility; SOW-0192 |
| Module / equipment shipping and off-loading | Tourmaline field construction scope | DBM-Deepcut SEC-01 |
| Setting modules, pipe racks, equipment on foundations | Tourmaline field construction scope | DBM-Deepcut SEC-01 |
| Mechanical hookup of modules, equipment, and interconnecting piping | Tourmaline field construction scope | DBM-Deepcut SEC-01 |
| Installation of shipped-loose instruments, valves, components | Tourmaline field construction scope | DBM-Deepcut SEC-01 |
| Interconnecting piping to ISBL/OSBL tie-ins | External interface responsibility marker; responsibility to be confirmed per tie-in (TBD per DBM) | DBM-Deepcut SEC-01 |
| Field installation of home-run cables; electrical terminations | Tourmaline field construction scope | DBM-Deepcut SEC-01 |
| Area lighting at the pump building | Tourmaline field construction scope (consistent with PKG-060 lighting interface) | DBM-Deepcut SEC-01; `INTERFACE_REGISTER.csv` IFC-30393FE7EE |
| DCS integration at MCC and pump local control | By others at vendor boundary; integrated by EPC Integrator (TBD: exact demarcation) | SOW-0192 |
| Tie-in timing and joint planning | Joint planning required; tie-in timing established as project progresses | DBM-Deepcut SEC-01 |

### Interfaces Asserted at PKG-060 Level

The following interface types apply to PKG-060 per the decomposition and govern construction tie-ins and turnover checks (SourcePath: `INTERFACE_REGISTER.csv`):

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-01 Facility Identity, Construction Responsibility; SEC-02.2 Site Data)
- GATE-07 PROJECT_DECOMP snapshot: `PACKAGE_REGISTER.csv` (PKG-060), `SCOPE_LEDGER.csv` (SOW-0189..SOW-0192), `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_PACKAGE_MAP.csv`
- `_Sources/26020-Package_Requirements.docx` package heading 15 — referenced by decomposition; not locally accessible as text (location TBD)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 85 — referenced by decomposition; not locally accessible as text (location TBD)
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
