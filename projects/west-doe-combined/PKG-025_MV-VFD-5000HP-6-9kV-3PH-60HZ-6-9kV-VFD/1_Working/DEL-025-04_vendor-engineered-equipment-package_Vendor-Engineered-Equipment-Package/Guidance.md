# Guidance — DEL-025-04 Vendor Engineered Equipment Package (PKG-025 MV VFD)

## Purpose

This deliverable is the Package Vendor's production unit for the 6.9 kV Medium-Voltage Variable Frequency Drive supporting the Inlet/Sales Gas Compressor service in the West Doe Deepcut 04-25 facility. It exists so that vendor-engineered design, fabrication, and equipment supply are routed through one coherent production unit that takes the EPC Scope of Work (DEL-025-01) and EPC Package Datasheet (DEL-025-02) as inputs and delivers the physical engineered package, plus the vendor design basis and datasheet set, back to the EPC Integrator for facility integration (`_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-025-04; PACKAGE_REGISTER.csv row PKG-025).

## Principles

- **Vendor owns the package; EPC owns the facility.** Vendor scope is package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination (PACKAGE_REGISTER.csv row PKG-025).
- **Source authority before convention.** Where the DBM-Deepcut design basis specifies a value or constraint (voltages, grounding, cabling, motor-start method), that source governs the vendor's design space. Where the DBM is silent, the vendor's documented engineering judgment applies, subject to EPC review.
- **The package serves a Starting VFD function.** Per DBM line 893, the inlet/sales compressor motor start method is a Starting VFD with synchronous transfer to a normal-service bus after reaching full speed. The package is not a continuous-duty VFD on the compressor motors; design must support starting duty cycle and a clean handoff to the normal bus through MCC-8200.
- **Capacitor exclusion on transfer bus.** Power-factor-correction capacitor banks shall NOT be installed on the MCC-8200 synchronous-transfer bus (DBM line 2955); this is a hard exclusion the vendor must respect in any auxiliary equipment proposed.

## Considerations

- **Motor rating uncertainty.** The package title cites 5,000 HP; the DBM cites 6,700 hp current driver basis with an unresolved 7,000 hp legacy conflict. Until a human ruling resolves this, the vendor cannot finalize VFD continuous current, starting current, transformer sizing, or cable sizing. See Conflict Table CT-01 (HRR-025-04-001).
- **Quantity allocation.** DBM Compressor List (line 2196) identifies 5 Inlet/Sales Compressor units. Per-unit VFD allocation (one Starting VFD per motor, or one shared Starting VFD that sequences through multiple motors, or a hybrid) is not stated in the accessible source slice. The EPC Package Datasheet (DEL-025-02) is the expected source for this allocation; see Conflict Table CT-02 (HRR-025-04-002).
- **Area classification.** If any VFD-fed motor (or the VFD itself) is in a Zone 2 area, motor markings and temperature code must be coordinated with the area-classification drawing or fugitive-emissions study (DBM line 2961). The Starting VFD is expected to reside in a general-purpose electrical building (DBM line 2973), but motor location must be confirmed.
- **Cabling between VFD and motor.** VFD-fed low-voltage circuits use copper TECK cable; 6.9 kV cables use three-conductor copper TECK rated 8 kV / 100 percent insulation, shielded (DBM lines 3008, 3013). VFD output cable selection must align.
- **Power quality.** Medium-voltage VFDs introduce harmonic currents into the upstream system. Limits, filtering, and isolation transformer arrangement are TBD (REQ-025-04-15). The vendor's submittal should propose a power-quality basis even where the EPC source is silent, so that EPC review can confirm or constrain it.
- **Two associated binary source files (`26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`) carry vendor-facing clauses and interface schedules but are not locally accessible as readable text in this drafting pass.** Vendor submittals should be re-checked against these files once an extracted slice is available; current drafting cannot ground in their clause-level content.

## Trade-offs

- **Starting VFD vs continuous VFD.** The DBM-prescribed Starting VFD + synchronous transfer architecture optimizes capital cost (smaller VFD, no continuous harmonic injection) at the cost of mechanical/electrical complexity in the transfer scheme. Vendors proposing continuous VFD operation depart from DBM basis and require EPC ruling.
- **Single shared starter vs per-motor starter.** Sharing one Starting VFD across multiple compressor motors reduces equipment count and footprint but couples motor availability through a single asset; per-motor VFDs invert that trade. The accepted allocation is TBD (CT-02).
- **Bypass / maintenance access.** Mechanical or electrical bypass options affect availability during VFD maintenance and the layout of the 6.9 kV electrical building.

## Examples

No worked examples are extractable from the accessible DBM slice. Vendor proposals should provide reference installations with directly comparable service (medium-voltage starting VFD with synchronous transfer for reciprocating compressor service) once available — currently TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 (HRR-025-04-001) | Motor horsepower basis: package title says 5000 HP; DBM-Deepcut says 6,700 hp current basis with 7,000 hp legacy unresolved. | PACKAGE_REGISTER.csv row PKG-025 (package title); workbook row 27 | DBM-Deepcut/4-25_Deepcut_DBM.md lines 893, 1086, 2196 | Datasheet Attributes; Specification REQ-025-04-12; Procedure prerequisites and verification | PROPOSAL: hold VFD continuous-current sizing until EPC Package Datasheet DEL-025-02 publishes the accepted motor rating. Do not adopt 5000 HP, 6,700 hp, or 7,000 hp without a recorded human ruling. | TBD |
| CT-02 (HRR-025-04-002) | Per-unit Starting VFD allocation across 5 Inlet/Sales Compressor units is not stated in the accessible source slice. | DBM line 2196 (5 units identified) | DBM §2955 (Starting VFDs called out for KM-2150/2250 collectively); EPC Package Datasheet DEL-025-02 (expected authority) | Datasheet Attributes (Quantity); Specification scope; Procedure prerequisites | PROPOSAL: defer allocation to EPC Package Datasheet (DEL-025-02). | TBD |
| CT-03 (HRR-025-04-003) | Vendor-facing clauses in `26020-Package_Requirements.docx` and interface rows in `26020-Packages_Interfaces_4_export.xlsx` are referenced authoritative sources but locally inaccessible as readable text. | `_REFERENCES.md` listings | Local filesystem (binary docx/xlsx not text-extractable in this pass) | All four documents | PROPOSAL: re-run drafting against these files once a text-extracted slice is added to `_References/`. Until then, requirements derived solely from those files remain TBD. | TBD |
