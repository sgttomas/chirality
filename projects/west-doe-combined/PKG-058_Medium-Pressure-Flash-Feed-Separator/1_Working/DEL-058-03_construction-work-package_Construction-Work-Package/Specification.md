# Specification — Construction Work Package (DEL-058-03)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for `PKG-058 Medium Pressure Flash Feed Separator`, comprising shop-fabricated Modules `710-1` and `730-1` and their associated vessels (`V-7110-1`, `V-7310-1`) and optional heater bundles (`E-7120-1`), as defined in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Module table, lines 2804, 2806; package register lines 2544, 2603-2604).

The CWP defines how the package is physically off-loaded, set, mechanically hooked up, instrumented, electrically terminated, inspected, and turned over from EPC Integrator construction scope to Tourmaline operations. It covers `SOW-0139` through `SOW-0142` (per `_CONTEXT.md`).

**Excluded** from this CWP:
- Vessel and heater bundle fabrication (covered by `DEL-058-04 Vendor Engineered Equipment Package`).
- Operating procedures (covered by `DEL-058-02 Package Datasheet` operating basis and downstream operations documents).
- Vendor document submittal management (covered by `DEL-058-05 Vendor Document Turnover Package`).
- EPC vendor package acceptance (covered by `DEL-058-06`).

## Requirements

### R1 — Module-level construction sequencing
The CWP shall sequence shop-to-site activities for two parallel modules (`710-1`, `730-1`) such that each can be independently installed, hooked up, tested, and brought into service. Both packages are shop-fabricated per the module list. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2804, 2806.

### R2 — Maintenance-isolation interface preservation
Construction tie-ins shall preserve the unit-basis maintenance-isolation philosophy: each MPFF unit must remain capable of being taken out of service for maintenance while the other continues to operate. Skid-edge isolation valves on interconnect piping between the pipe rack and module shall be installed during hookup. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2408, 2454.

### R3 — Tourmaline construction responsibility integration
The CWP shall identify the Tourmaline field construction interface for each of the following activities and provide work-pack content sufficient for execution by Tourmaline crews:
- off-loading, setting, mechanical hookup, shipped-loose installation, structural supports, home-run cable installation, electrical terminations.
Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 111-119.

### R4 — ISBL/OSBL tie-in responsibility confirmation
For each interconnecting piping tie-in to ISBL/OSBL boundaries, the CWP shall record a per-tie-in responsibility confirmation. Tie-in joint-planning and timing shall be established as the project progresses. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 117, 127.

### R5 — Nozzle and tie-in preservation pending heater bundle disposition
Until the MPFF HCL heater bundle (`E-7120-1`) retention/removal disposition is confirmed by thermal reassessment, the CWP shall require preservation of vessel nozzle provisions and associated heat-medium tie-in stubs. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 674.

### R6 — Methanol injection installation
Methanol injection tie-in upstream of the MPFF inlet level/pressure control valve shall be installed and retained as a hydrate-suppression safeguard. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 674.

### R7 — Self-framing building hookup
The MPFF package self-framing building (enclosing instrumentation and one end of the vessel) shall be set, sealed, and tied into facility area lighting, fire-and-gas, HVAC (if any), and electrical systems during the mechanical-hookup phase. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672. Building HVAC scope — TBD (location TBD in source).

### R8 — Foundation handoff
Foundations and piling for Modules `710-1` and `730-1` are within Tourmaline field construction scope. The CWP shall require a foundation acceptance handoff (level, elevation, anchor-bolt pattern, grout) before module setting. Foundation design inputs depend on the geotechnical report — TBD. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 108, 113, 2834.

### R9 — Cold-weather construction allowance
Construction sequencing shall account for site design ambient of -40 °C minimum and snow loads Ss = 2.5 kPa, Sr = 0.2 kPa. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 198, 206-207.

### R10 — Automated blowdown valve installation
The required automated blowdown valve on the MPFF shall be installed, calibrated, and stroke-tested as part of mechanical completion. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672.

### R11 — Purge-gas tie-in
Low-pressure fuel-gas purge tie-in (from downstream of the fuel-gas scrubber) shall be installed with pressure regulation maintaining MPFF pressure above the downstream stabilizer flash/feed separator and capable of sour-gas sweeping during maintenance. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672.

### R12 — Turnover checklist
The CWP shall deliver a Construction Interface and Turnover Checklist enumerating: punch-list closure status, mechanical completion sign-off, loop-check status, hydrotest/pneumatic-test records, instrument calibration records, vendor turnover documents (referenced from `DEL-058-05`), and operational readiness items. — ASSUMPTION on detailed checklist scope; specific format is `TBD` pending Owner construction procedure.

## Standards

| Standard / Basis | Application | Location |
|---|---|---|
| Project DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Construction responsibility split, module list, MPFF design basis | lines 100-127, 670-674, 2804-2806 |
| BCER equipment spacing guidelines | Site spacing during setting | line 228 |
| National Building Code of Canada 2020 (IDF, Dawson Creek) | Site climate/structural inputs | line 188 |
| `26020-Package_Requirements.docx` package heading 13 | Package-specific requirements | location TBD (source not parsed locally) |
| ASME, CSA, B31.3 piping, B31.8 gas pipe (typical for this scope) | Piping / pressure-vessel construction | ASSUMPTION — not explicitly cited in accessible sources for this CWP |

## Verification

| Requirement | Verification approach |
|---|---|
| R1 module sequencing | Review of CWP schedule against module list; sign-off at module-set milestone |
| R2 maintenance isolation | Walkdown verifying skid-edge isolation valves at each interconnect; isolation P&ID stamp |
| R3 Tourmaline integration | Interface meeting records; signed responsibility matrix per CWP section |
| R4 tie-in responsibility | Per-tie-in responsibility log signed by EPC and Tourmaline |
| R5 nozzle preservation | Nozzle/blanking inspection record; bundle disposition log |
| R6 methanol injection | Installation walkdown + line-check sign-off |
| R7 building hookup | Building close-up checklist; lighting, F&G loop checks |
| R8 foundation handoff | Foundation acceptance certificate prior to setting |
| R9 cold-weather | Construction execution plan review |
| R10 blowdown valve | Stroke-test and calibration certificate |
| R11 purge-gas tie-in | Pressure-regulator setpoint verification; line walkdown |
| R12 turnover checklist | Mechanical completion package signed by EPC and accepted by Tourmaline |

## Documentation

CWP shall produce the following artifacts (anticipated, per `_CONTEXT.md`):

- Construction work package document (this scope).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Additional supporting documents:
- Per-tie-in responsibility log.
- Foundation acceptance certificates (`710-1`, `730-1`).
- Mechanical completion checklists per module.
- Punch-list closure record.
- Loop-check, hydrotest, calibration, and vendor turnover document references (consume `DEL-058-05` outputs).
