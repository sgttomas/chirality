# Specification — DEL-079-04 Vendor Engineered Equipment Package

## Scope

This specification governs the Package Vendor's engineering, design, fabrication/supply, and delivery of the consolidated Instrument Air Building vendor package for `PKG-079`, anchored to the EPC Scope of Work (DEL-079-01) and Package Datasheet (DEL-079-02). It covers the 04-25 instrument air compression/treatment skid that serves the 04-25 gas plant, 03-25 liquids hub, and 03-25 compressor station as a shared utility (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: "Instrument Air Basis", L1906-L1908).

Excludes: EPC-side civil/structural building envelope beyond the vendor skid edge, EPC pipe-rack tie-in piping outside skid edge, plant DCS host equipment (interface coordination only), and the question of a separate 03-25 booster compressor (open per source, L1925) — those remain EPC-integrator scope and detailed-engineering decisions.

## Requirements

### R-1 Compressor configuration
Provide 2 x 100 percent capacity instrument air compressors in lead-lag operation. Provide skid spacing and piping provision for a third 100 percent capacity compressor (future). (SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: L1939-L1940.)

### R-2 Capacity rating
Rate compressor capacity at SCM/H at 930 kPag (135 psig). (SourcePath: same; SectionRef: L1934.)

### R-3 Pressure setpoints
- Normal header supply pressure: 827 kPag (120 psig).
- Compressor maximum discharge / shutdown pressure: 1000 kPag (145 psig).
- Facility shutdown pressure: 482 kPag (70 psig).
- Minimum actuator supply pressure: 551 kPag (80 psig) upstream of valve instrument air supply regulators.
(SourcePath: same; SectionRef: L1935-L1938.)

### R-4 Air dryness
Treated instrument air shall meet a maximum water dewpoint of -73.3 deg C at 1000 kPag. (SourcePath: same; SectionRef: L1931.)

### R-5 Reserve volume
Provide receiver/header volume sufficient for 15 minutes usable reserve after instrument air shutdown, computed across the header, dry receiver, and wet receiver from 120 psig down to 80 psig. (SourcePath: same; SectionRef: L1941-L1942.)

### R-6 Demand sizing
The consolidated package shall be sized to the combined 1,113 SCFM (TBC) demand basis comprising 720 SCFM 04-25 demand and 393 SCFM 03-25 cross-facility demand. Per-instrument demand factors: 0.5 SCFM per control valve / air-operated pump / air-cooler louver and 1.0 SCFM per shutdown / switching / blowdown valve, with 20 percent contingency on calculated demand. Final combined sizing, contingency treatment, distribution losses, and the 03-25 booster compressor question are open (TBC) and shall be reconciled in detailed engineering. (SourcePath: same; SectionRef: L1912, L1916-L1925.)

### R-7 Piping classification
Package piping shall be ASME Category D where Category D is permitted by service. (SourcePath: same; SectionRef: L1933.)

### R-8 PSV setting
Package PSV setting shall be 1034 kPag (150 psig) or less. (SourcePath: same; SectionRef: L1932.)

### R-9 Skid-edge isolation
Provide skid-edge block valves for all services at the skid boundary. **Spectacle blinds are NOT required at instrument air skid-edge connections** (explicit exception). Skid-edge isolation shall be located outside buildings in the interconnect piping. (SourcePath: same; SectionRef: "Skid-Edge and Processing-Unit Isolation", L2451-L2454.)

### R-10 Equipment tag set
The package shall deliver, at minimum, the tagged equipment listed for the Instrument Air Building: K-4210-1, K-4220-1, F-4215-1, F-4220-1, F-4225-1, F-4230-1, V-4210-1, V-4240-1. Tag service assignments beyond compressors are TBD pending vendor selection. (SourcePath: same; SectionRef: Building row L2601.)

### R-11 Building area classification
Building area classification is assumed General Purpose / Non-Classified; vendor shall validate during detailed engineering. ASSUMPTION: validated as classification basis pending EPC confirmation. (SourcePath: same; SectionRef: L1943.)

### R-12 Compressor electrical-driver class
Driver type, voltage class, and starting method are TBD; coordinate with EPC electrical basis. (SourcePath dependency: Electrical interface SectionRef "Instrument Air and Electrical Interface" in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L772-L774 establishes that no 03-25 local IA compressor controls shall be added; 04-25 compressor electrical class is location TBD in available sources.)

## Standards

- ASME B31.3 — referenced indirectly via Category D piping classification (location TBD in available source slice).
- ASME Section VIII — pressure vessels (V-tagged receivers); location TBD in available source slice.
- API / ISA instrumentation standards — location TBD; vendor proposal shall list governing standards.
- `26020-Package_Requirements.docx` heading 32 — referenced in decomposition row 381 as governing package source (binary; not text-accessible in this run; location TBD).

## Verification

| Req | Verification Method |
|---|---|
| R-1 | Vendor GA drawing review; factory acceptance test (FAT) of lead-lag changeover |
| R-2 | Compressor performance curves + FAT capacity test at 930 kPag |
| R-3 | Setpoint verification on PSV bench test, header regulator setting, shutdown logic test |
| R-4 | Dryer performance test (dewpoint measurement) at design and turndown |
| R-5 | Reserve-volume calculation review against header + receiver geometry |
| R-6 | Sizing calculation review against EPC-supplied instrument count and per-instrument factors |
| R-7 | Line list and isometric review against Category D scope |
| R-8 | PSV nameplate verification and bench test certificate |
| R-9 | Skid-edge tie-in P&ID review; site walk-down (EPC) |
| R-10 | Tag/equipment list reconciliation against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` building row |
| R-11 | Electrical area classification drawing + EPC confirmation memo |
| R-12 | Driver datasheet review by EPC electrical lead |

## Documentation

The vendor shall deliver, at minimum (vendor package design basis and datasheet set per `_CONTEXT.md` Anticipated Artifacts):
- Vendor package design basis document
- Compressor, dryer, filter, and receiver datasheets
- Skid GA drawing and equipment layout
- P&IDs and line list (Category D scope)
- Electrical one-line and area-classification drawing
- Control narrative and cause-and-effect for lead-lag changeover and shutdown logic
- PSV sizing and certificates
- FAT procedure and report
- Operating and maintenance manual
- Spare parts list

Detailed vendor document register and turnover content are handled by DEL-079-05 (Vendor Document Turnover Package); this specification only sets the minimum content expected at handoff.
