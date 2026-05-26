# Specification — DEL-066-04 Vendor Engineered Equipment Package

> Normative requirements for the vendor-engineered condensate storage tank package (PKG-066, 4-25 Deepcut), to be satisfied by the Package Vendor and accepted by the EPC Integrator.

## Scope

### In Scope

- Vendor engineering, design, fabrication/supply, and the physical equipment package for the PKG-066 condensate storage tanks (TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1) at the West Doe Deepcut 04-25 expansion.
- Mechanical, structural, civil-interface, instrumentation, electrical termination, coating, and accessory scope normally part of an API 650 tank package vendor's scope of supply.
- Vendor package design basis and datasheet set (per `_CONTEXT.md` anticipated artifacts).
- Coordination with the EPC Integrator on inputs published in the EPC Scope of Work (DEL-066-01) and EPC Package Datasheet (DEL-066-02), and on installation interfaces with the Construction Work Package (DEL-066-03).

### Out of Scope (Excluded From This Vendor Package)

- Plot plan engineering and as-built site coordinates — governed by drawing CIV-235633-5002 (DBM-identified as TBD; not in accessible source set).
- VRU equipment (separate package; condensate tanks tie to VRU suction header at Module 930 boundary per DBM § VRU).
- Condensate transfer pumps P-9210-1 / P-9220-1 (separate package; condensate tank discharge is interfaced).
- Stabilizer / upstream processing.
- LACT, downstream 03-25 Liquids Hub storage (6 x 3,800 bbl tanks — DBM § Condensate Product Storage).
- Construction installation work — covered by DEL-066-03 Construction Work Package.
- Document turnover and turnover records — covered by DEL-066-05.
- EPC integration acceptance — covered by DEL-066-06.

## Requirements

Requirements are tagged R-#. Mandatory verbs ("shall") indicate normative requirements.

### Mechanical / Tank Design

- R-01 Tanks shall be designed and constructed to a Modified API 650 atmospheric standard. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage]
- R-02 Tank design test pressure shall be 16 oz/in2 (atmospheric tank). [Source: same]
- R-03 Maximum fill shutdown shall be set at 90% of tank volume. [Source: same]
- R-04 Each tank shall provide 3,800 bbl nominal working volume. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage; per CONFLICT C-01 the count of tanks (4 vs 5) and the total facility storage volume require human ruling before fabrication.]
- R-05 Tank design specific gravity shall be 1.0 for condensate product service. [Source: same]
- R-06 Tanks shall be non-insulated for product condensate service (recycle may be required for winter temperature maintenance — accommodate recycle nozzle interface). [Source: same]
- R-07 Tanks shall accommodate stored fluid density across operating ambient range (combined/stabilizer-only C5+: 709.8 kg/m3 at -40 deg C to 612.6 kg/m3 at 60 deg C; stabilizer-only C5+: 732.2 at -40 deg C to 638.6 at 60 deg C). [Source: same — density table]
- R-08 Each tank shall be fitted with at least one PVRV. [Source: extrapolated from `4-25_Deepcut_DBM.md` § Produced water tanks reference "Each tank has at least one PVRV" combined with general tank-farm vapour management; ASSUMPTION for condensate tanks pending vendor datasheet confirmation; location TBD in 26020-Package_Requirements.docx package heading 21.]
- R-09 EPRV sizing shall be determined during detailed engineering with vendor input. [Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage — explicit TBD]
- R-10 Off-spec condensate overhead vent sizing shall be determined during detailed engineering with vendor input. [Source: same]
- R-11 Thermal expansion of the tank shell and contents shall be reviewed over the ambient range. [Source: same]
- R-12 Tanks shall be designed for blanket gas service per API 2000 rates to prevent winter vacuum. [Source: same; § Condensate Product Storage]

### Configuration and Internals

- R-13 Two of the tanks shall be assigned as "inlet tanks" receiving stabilizer bottoms. [Source: same]
- R-14 An internal pipe stand shall allow condensate to cascade by elevation from inlet tanks into downstream tanks. [Source: same]
- R-15 Inlet and outlet condensate tanks shall share a common truck-out connection. [Source: same]
- R-16 Tank arrangement shall allow sediment and water collection in inlet tanks while keeping cleaner product in final outlet tanks. [Source: same]

### Nozzles and Interfaces

- R-17 Each tank shall provide nozzles for: blanket gas inlet, VRU suction takeoff to Module 930 header, level instrumentation, temperature instrumentation, fill (stabilizer bottoms for inlet tanks; cascade for downstream tanks), discharge to condensate transfer pumps (P-9210-1 / P-9220-1), product recycle return, truck-out, drain, manway access, EPRV, PVRV, and roof vent. (Specific nozzle list: TBD pending the EPC Package Datasheet DEL-066-02.)
- R-18 Tank discharge nozzles shall be sized and located such that the downstream condensate transfer pumps achieve NPSHR no greater than 0.75 m at design flow (tanks are not elevated). [Source: `4-25_Deepcut_DBM.md` § Product Pumps]
- R-19 The vendor shall confirm interface elevations, flange ratings, and nozzle orientations against the EPC Package Datasheet (DEL-066-02) before fabrication release.

### Civil / Structural

- R-20 Tank-to-tank centerline spacing shall comply with NFPA 30 Table 22.4.2.1 minimums (2.35 m / 7.72 ft). [Source: `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing]
- R-21 Foundations, ringwall, anchorage, seismic, wind, and snow loads — TBD (site-specific civil/structural basis not present in accessible sources; vendor shall coordinate with the EPC civil discipline).
- R-22 Coatings, internal lining, and corrosion allowance for condensate service — TBD (not specified in accessible sources for product condensate tanks; vendor shall propose values referenced to applicable standards and seek EPC acceptance).

### Materials

- R-23 Materials of construction shall be suitable for stabilized C5+ condensate at the stated density basis and ambient temperature range (-40 deg C to 60 deg C). Specific material grades: TBD pending vendor proposal aligned to API 650 and project material class (location TBD in 26020-Package_Requirements.docx).

### Documentation Delivered With Equipment

- R-24 The vendor shall deliver a Package Vendor Design Basis aligned to the EPC Package Datasheet (DEL-066-02) covering: tank dimensions, materials, coatings, internals, nozzle schedule, accessories, instrumentation lists, electrical loads, code datasheets, calculations (shell, roof, anchorage, seismic, wind, hydrotest), and inspection/test plan.
- R-25 Vendor data shall be delivered into DEL-066-05 (Vendor Document Turnover Package) — this specification governs the technical scope of the equipment package; document register management is out of scope here.

## Standards

| Standard | Application | Location in Source |
|---|---|---|
| API 650 (Modified) | Tank code of construction | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| API 2000 | Blanket gas / venting rate basis | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| NFPA 30 (Table 22.4.2.1, 22.4.1.5) | Tank-to-tank and property-line spacing | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| OGAOM § 9.6.15 | Public-road, flare, fired-heater spacing | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| DPR 48 | Public-road spacing (referenced jointly with OGAOM) | same |
| 26020-Package_Requirements package heading 21 | Authoritative project-level package requirements for PKG-066 | `_REFERENCES.md` and `_CONTEXT.md`; location TBD (.docx not accessible in this run) |

## Verification

| Requirement | Verification Method | Acceptance Evidence |
|---|---|---|
| R-01 to R-07, R-12 | Design calculations and certified vendor datasheets | API 650 datasheet, shell/roof calculations, density-range design check |
| R-08 to R-11 | Detailed-engineering review with EPC Integrator | Sizing calculations for EPRV / PVRV / vent / thermal expansion |
| R-13 to R-16 | Drawing review (GA, P&ID alignment) | Tank arrangement drawings showing inlet tank assignment, internal pipe stand, truck-out manifold |
| R-17 to R-19 | Drawing review against EPC Package Datasheet (DEL-066-02) | Nozzle schedule and tank GA accepted by EPC Integrator |
| R-18 | NPSHR calculation against P-9210-1 / P-9220-1 datasheet | Hydraulic check signed by vendor and reviewed by EPC |
| R-20 | Plot-plan check against drawing CIV-235633-5002 (TBD — drawing currently outside accessible source set) | Plot plan compliance memo |
| R-21 | Civil/structural calculations to project basis | Foundation and anchorage calculations |
| R-22 | Coating spec submittal | Approved coating system datasheet |
| R-23 | Material test reports and MTRs | MTRs aligned to API 650 and project material class |
| R-24, R-25 | Document register cross-check (with DEL-066-05) | Vendor document register entries for each item |

## Documentation

Anticipated artifacts (per `_CONTEXT.md`):

- Vendor engineered physical equipment package (the equipment itself, with nameplate, MTRs, hydrotest records).
- Vendor package design basis and datasheet set.

Required vendor documentation (technical, delivered with the equipment package; turnover management is DEL-066-05):

- API 650 datasheet per tank
- Tank general arrangement drawings
- Nozzle orientation drawings
- Shell, roof, anchorage, seismic, wind, hydrotest calculations
- Material test reports (MTRs)
- Coating specifications and inspection records
- Inspection and test plan, including hydrotest report
- PVRV/EPRV/vent sizing report
- Thermal expansion review
- Blanket gas rate calculation (API 2000)
- Accessory bills of material (gauges, switches, manways, ladders/platforms)

(Detailed vendor document list will be reconciled against 26020-Package_Requirements.docx package heading 21 — location TBD in this run.)
