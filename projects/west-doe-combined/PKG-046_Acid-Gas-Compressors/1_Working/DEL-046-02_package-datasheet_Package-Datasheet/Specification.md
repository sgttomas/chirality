# Specification — PKG-046 Acid Gas Compressors (Package Datasheet)

> Normative requirements for the PKG-046 acid gas compressor package, derived from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05.
> Items not directly source-supported are labelled ASSUMPTION or TBD.

## Scope

### In scope
- Reciprocating acid gas compressor package(s) compressing water-saturated acid gas from the amine regenerator reflux accumulator and delivering it through an aftercooler to the acid gas injection pipeline / disposal well interface.
- Two 100% packages plus one installed spare (current basis); a possible three x 50% arrangement remains TBD.
- Suction scrubbing (per stage), aftercooling, recycle control (HP and LP), blowdown, sequencing automation, packing/seal-pot vapour recovery to VRU, scrubber liquid handling, disposal metering, and continuous composition monitoring.
- VFD-driven induction-motor driver and on-package controls/protection.

Source: DBM-Deepcut SEC-05 "Acid Gas Injection Compression Basis" and "Acid Gas Disposal Well Interface".

### Out of scope (excluded by source)
- Adjustable volume pockets in compressor cylinders (intentionally excluded to reduce acid-gas leakage points). [DBM-Deepcut SEC-05]
- Manual isolation of recycle valves (intentionally excluded to reduce leakage points). [DBM-Deepcut SEC-05]
- Acid gas injection pipeline detailed design beyond the package boundary (final NPS to be reviewed during detailed engineering). [DBM-Deepcut SEC-05]
- Acid gas disposal well design and reservoir characterization (Tourmaline-provided). [DBM-Deepcut SEC-05]
- Modifications at the existing 02-25 facility (TBD; trigger and extent unresolved). [DBM-Deepcut SEC-01 and SEC-05]
- Acid gas injection pump (current design does not include an injection pump). [DBM-Deepcut SEC-05]

## Requirements

### R-46-01 — Configuration
The package configuration shall be two 100% acid gas compressor packages plus one installed spare. A three x 50% alternative is not authorized unless explicitly approved by the human owner. [DBM-Deepcut SEC-05]

### R-46-02 — Compressor frame
Each package shall use a five-stage separable reciprocating compressor. The current frame basis is Ariel KBT/6; the conflicting KBK/6 reference shall be resolved by the human owner before vendor RFQ (see Guidance Conflict Table). [DBM-Deepcut SEC-05]

### R-46-03 — Design flow & turndown
Each unit shall be sized for design unit flow of 4.5 MMSCFD (preliminary; target 1.10 capacity factor at design) with the package total of 4.209 MMSCFD design and 0.603 MMSCFD start-up; minimum 3:1 speed turndown via VFD shall be supported. [DBM-Deepcut SEC-05]

### R-46-04 — Driver
The driver shall be an 8-pole induction motor rated 969 kW (1,300 hp) including approximately 10% excess power, operated on VFD at 900 rpm full speed with minimum 3:1 speed turndown. [DBM-Deepcut SEC-05]

### R-46-05 — MAWP and design temperature
The package shall meet the minimum MAWP and design temperature per stage per the Datasheet "Acid gas compressor MAWP and design-temperature basis" table. Detailed analysis of system volumes during detailed engineering shall verify MAWP and maximum equalization pressure. [DBM-Deepcut SEC-05]

ASSUMPTION (NEEDS_HUMAN_RULING): the discharge-MAWP values stated for stages 1 and 2 (197 psig) being lower than the corresponding suction MAWPs (205 psig) shall be verified by the source author; pending ruling, the values are quoted as-stated.

### R-46-06 — Stage aftercooling
Each stage discharge shall be cooled by a common forced-draft motor-driven air cooler. Cooler outlet temperatures shall be 110 deg F (43.33 deg C) for stages 1-4 and 150 deg F (65.56 deg C) for stage 5. Each cooler bundle shall include actuated louver temperature control, automatic warm-air recirculation on low discharge temperature, and heat-medium heating for winter freeze protection. [DBM-Deepcut SEC-05]

### R-46-07 — Injection pipeline temperature control
The acid gas aftercooler outlet to the injection pipeline shall be controlled to 8.3 deg C above maximum ambient at all times. [DBM-Deepcut SEC-05]

### R-46-08 — Suction scrubbers
A two-phase suction scrubber shall be provided upstream of each compression stage. Scrubbers shall be sized using a maximum K-factor of 0.55 Imperial with assumed inlet liquid density 1.00 SG. Horizontal double-hook vane demisters are acceptable. Off-design cases (low compression ratio, high package capacity, start-up high-suction / low-discharge) shall be considered. All scrubbers shall include PID liquid-level control; stages 2-5 liquids shall cascade to prior-stage scrubbers; stage 1 liquid shall be pumped to the produced water tank by a 0.75 hp motor-driven Hydra-Cell pump. [DBM-Deepcut SEC-05]

### R-46-09 — Recycle controls
The package shall include high-pressure and low-pressure recycle valves. The HP recycle valve shall route final discharge to the 4th-stage suction upstream of the 4th-stage suction scrubber. The LP recycle valve shall route 4th-stage suction to 1st-stage suction upstream of the 1st-stage suction scrubber. Both recycle valves shall fail open and shall be sized for 100% capacity at minimum driver speed, maximum suction pressure, and minimum injection pipeline pressure. Manual isolation of recycle valves shall not be provided. [DBM-Deepcut SEC-05]

### R-46-10 — Blowdown
The package shall include a single fail-open blowdown valve on the final discharge downstream of the aftercooler. Start-up shall be from equalization pressure with 3:1 VFD turndown and cascading recycle; additional automated bypass is not anticipated. [DBM-Deepcut SEC-05]

### R-46-11 — Volume pockets excluded
Adjustable volume pockets shall be excluded from the cylinders. Capacity control shall be by driver speed control and recycle control. [DBM-Deepcut SEC-05]

### R-46-12 — Sweet gas purge
A manual sweet-gas purge connection shall be included at 1st-stage suction downstream of the inlet shutdown valve, to remove H2S before maintenance. [DBM-Deepcut SEC-05]

### R-46-13 — Packing drains and vents
Packing drains and vents shall be collected to a common seal pot. Seal-pot vapour shall be routed to the VRU suction header. Liquids shall be removed by local truck-out connection. [DBM-Deepcut SEC-05]

### R-46-14 — Disposal metering
Acid gas disposal metering shall be by a high-pressure Coriolis mass meter located downstream of compression. Acid gas routed to the LP flare through the amine reflux accumulator BDV/PCV shall be directly metered. The main LP acid gas line to the compressor shall not be metered. [DBM-Deepcut SEC-05]

### R-46-15 — Composition monitoring
Continuous acid gas composition measurement shall be provided to support sulfur and CO2 balance reporting. [DBM-Deepcut SEC-05]

### R-46-16 — Sequencing automation
Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences shall be automated. [DBM-Deepcut SEC-05]

### R-46-17 — Lubrication oil disposition
Lubrication oil injected into compressor valves and cylinders shall be disposed via the injection well; no separate lube-oil reclamation from the acid gas stream is required. [DBM-Deepcut SEC-05]

### R-46-18 — Dehydration option
Recycle-based partial dehydration to 35-60 lb H2O/MMSCF shall be considered if required by the disposal system; dehydration is not a base requirement unless specified by the disposal-well interface. [DBM-Deepcut SEC-05]

### R-46-19 — Mercaptan / three-phase separation
The vendor shall evaluate three-phase separation needs arising from mercaptan condensation at low temperatures and the resulting impacts on dehydration, recycle, and efficiency. [DBM-Deepcut SEC-05]

### R-46-20 — Interface compliance
The package shall comply with the project interface register entries for PKG-046 in `INTERFACE_REGISTER.csv`. Specific interface IDs: location TBD (register not yet sliced into the deliverable). [DECOMPOSITION_REF]

## Standards

| Standard | Applicability | Source / status |
|---|---|---|
| API 11P | Vane-style demister sizing reference for suction scrubbers | DBM-Deepcut SEC-05 (cited for sales-booster scrubber; applied here by analogy — ASSUMPTION); location TBD |
| Vendor proprietary (Ariel) | Compressor frame design | DBM-Deepcut SEC-05 (Ariel KBT/6 cited) |
| 26020-Package_Requirements.docx | EPC package general requirements (binary; not text-extracted in this pass) | `_REFERENCES.md`; location TBD |
| API 618 (reciprocating compressors), API 619, ASME Section VIII, CSA standards, applicable provincial regulations | Generally applicable to sour-service reciprocating compressor packages in Western Canada | ASSUMPTION (not enumerated in accessible source slices); location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R-46-01 Configuration | Vendor PFD/P&ID and equipment list cross-checked against package count and spare strategy |
| R-46-02 Frame | Vendor data sheet confirming Ariel KBT/6 (or resolved alternative); RFQ acceptance |
| R-46-03 Flow / turndown | Performance datasheet at design, start-up, and turndown cases; FAT capacity test |
| R-46-04 Driver | Motor nameplate and VFD performance test |
| R-46-05 MAWP / design temperature | Code design review and hydrotest per ASME VIII; system-volume study during detailed engineering |
| R-46-06 / R-46-07 Cooling | Aftercooler datasheet and performance test; control loop FAT |
| R-46-08 Scrubbers | Scrubber sizing calc (K=0.55 Imp, SG=1.00); demister vendor datasheet; FAT level-control checkout |
| R-46-09 Recycle | Recycle valve sizing review; fail-position test; recycle operability test |
| R-46-10 Blowdown | BDV stroke and fail-position test |
| R-46-11 Volume pockets | Vendor confirmation of cylinder configuration |
| R-46-12 Sweet gas purge | P&ID review and tie-in test |
| R-46-13 Packing drains/vents | P&ID review; VRU tie-in test |
| R-46-14 Metering | Coriolis meter calibration and witness |
| R-46-15 Composition monitoring | Analyzer factory and site acceptance tests |
| R-46-16 Sequencing | Sequence test, including SAT |
| R-46-17 Lube disposition | P&ID and operating procedure review |
| R-46-18 Dehydration option | Recycle hydraulic study during detailed engineering |
| R-46-19 Mercaptan | Process simulation cases and three-phase separation evaluation |
| R-46-20 Interfaces | Interface register reconciliation at FEED/EPC handover |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):
- Package technical datasheet (this deliverable + `Datasheet.md`)
- Vendor engineering handoff basis (this deliverable + `Guidance.md`, `Procedure.md`)
- Package interface requirements matrix (cross-reference to `INTERFACE_REGISTER.csv` — location TBD)
- Source-supported equipment and design criteria (consolidated in `Datasheet.md` Attributes)

Additional vendor-deliverable documentation expected from the integrator:
- Vendor PFD, P&IDs, GA drawings, control narrative, performance curves, weights, utility list, electrical one-line, hazardous-area classification, datasheets for cylinders/coolers/scrubbers/motors/VFD, FAT/SAT procedures, spare parts list. ASSUMPTION (industry-standard scope; not enumerated in accessible source slices).
