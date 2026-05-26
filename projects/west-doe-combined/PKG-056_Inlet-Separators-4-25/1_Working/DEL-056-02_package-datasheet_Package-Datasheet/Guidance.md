# Package Datasheet — Guidance (DEL-056-02, PKG-056 Inlet Separators 4-25)

> Directional document: purpose, principles, considerations, and trade-offs. Rationale drawn from accessible source slices; gaps are `TBD`.

## Purpose

The Package Datasheet is a mandatory EPC Integrator Gate-5 handoff deliverable. Its purpose is to convey, in a single source-supported package, every technical fact a third-party Package Vendor needs to bid, engineer, design, and supply the inlet separator package without re-asking the EPC team for project basis information. By bundling tagged equipment, operating and design conditions, construction basis, and interface applicability into one document set, the Datasheet anchors the Vendor RFQ and downstream vendor-package production (DEL-056-04) and the Construction Work Package (DEL-056-03). [Source: `_CONTEXT.md`; decomposition row 373.]

## Principles

- **Source over convention.** All numeric values, materials, and applicability calls trace to either `26020-Package_Requirements.docx` heading 11 (the formal package basis) or the 4-25 DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`). Where the two disagree, the Conflict Table below preserves the disagreement rather than silently choosing.
- **Interface facts as evidence.** Interface applicability is carried in the Datasheet rather than as separate deliverables. The deliverable inherits the package-row interface matrix (row 68 of `26020-Packages_Interfaces_4_export.xlsx`) verbatim — additions or modifications require source amendment, not Vendor opinion. [Source: `_CONTEXT.md` Notes.]
- **By-others scope is explicit.** Boundaries excluded from Vendor scope (skid-edge piping, DCS, foundations, MCC supply, install) are stated up front so Vendor scope cannot creep into EPC scope without rebid. [Source: Package Requirements heading 11, Scope Notes / Open Items.]
- **TBD over guess.** Where the source slice does not provide a value (retention times, exact outlet temperature for the liquid heater, heating medium, mol% sour basis above 1.0 mol% threshold cited only for pig receivers, etc.) the Datasheet records `TBD` and Specification records the verification path rather than inventing a value.

## Considerations

### Two-phase inlet conditions
During winter operation and shutdown cooldown, inlet gas can arrive two-phase. Separator sizing, slug-handling, and the inlet PCV trim selection (hardened balanced globe, dP <= 5 psid) all assume two-phase capable throttling. Methanol injection is provided upstream for hydrate suppression. Operability is also affected by upstream pipeline holdup (~67 m3) and the assumed 6-hour processing window via MPFF/SOC/stabilizer trains — operability assumptions are explicit and downstream availability is a hard precondition for inlet-separator operation. [Source: DBM lines 591, 630.]

### Drive-gas service
Each separator can receive sales gas as drive gas upstream of the sales splitter when separator pressure cannot be maintained at normal conditions; inlet-compressor discharge is the alternate. Because drive gas enters upstream of plant inlet gas meters, separate per-package metering is required — a Vendor scope item that must not be missed in the Vendor I&C package. [Source: DBM line 811.]

### HIPPS sensitivity
If detailed-engineering confirms that upstream pipeline MAOP exceeds facility inlet design pressure, a HIPPS may be required to protect the inlet separators. HIPPS configuration and shutdown setpoints are TBD at this stage, but the ESDV shutdown setpoint of 1,360 psig is already specified and the gas volume between plant inlet ESDVs and separator inlet PCVs must be considered in setpoint development. [Source: DBM line 809.]

### Liquid outlet heating
The package includes an outlet HEX per separator to keep MPFF level-control-valve feed above hydrate/freeze thresholds when feed arrives near -26 °C. Heat-medium selection (warm glycol vs cross-exchange) is an open Vendor coordination point with downstream MPFF and stabilizer heat integration. [Source: DBM line 648.]

### Building / instrumentation enclosure
The heated self-framing building covers instrumentation and one vessel end. Building HVAC interface applicability is "No" in the row-68 matrix (instrumentation-area heating is internal to the package), but Building Code / Occupied Building Risk Assessment inputs are still required at vendor scope (TSF-023 in the inherited vendor deliverable list).

## Trade-offs

| Trade-off | Direction | Source |
|---|---|---|
| Two installed separators with future plot vs four packages (legacy) | Current basis: two installed + plot reservation; legacy references retained as unresolved | DBM line 589; see Conflict Table |
| Slug capacity 31.8 m3 vs 33.9 m3 | Datasheet records 33.9 m3 (Package Requirements is source authority); DBM disagrees | Package Requirements heading 11; DBM line 591 |
| Manually adjustable weir vs fixed weir | Manually adjustable weir specified (subject to operations review) | DBM line 646 |
| Single mist eliminator type vs alternatives | Vertical (horizontal-flow) high-performance mesh/vane — subject to operations review | Package Requirements heading 11; DBM line 646 |
| Internal coating (Devchem 253) on vessel but not piping | Cost / corrosion control vs piping maintenance scope | Package Requirements heading 11 |

## Vendor Document Set (R8 expansion)

The Vendor scope shall produce the following deliverables (source: Package Requirements heading 11 "Vendor Engineering Deliverables"). Grouping preserved from source:

- **Core vendor documents:** PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality Plan; QLT-003 ITP; QLT-013 Material Test Reports / Certificates; QLT-020 Inspection Release Certificate; QLT-021 Manufacturing Record Book / Vendor Data Book; PRQ-013 Logistics / Shipping Plan; PRQ-015 SPIR; PRQ-016 Vendor Data Book / Final Supplier Documentation.
- **Core package engineering:** MEC-001 Mechanical Design Basis; MEC-002 Equipment List; MEC-003 Equipment Data Sheets; MEC-006 Package Equipment Specifications; MEC-014 Mechanical Calculation Package; MEC-016 Equipment GA Drawing; MEC-017 Equipment Installation / Setting Drawings; MEC-018 Lifting / Handling Study; MEC-021 FAT / Performance Test Procedure; MEC-022 FAT / Performance Test Report; MEC-023 Vendor Data Book / Mechanical Final Documentation; MEC-024 Mechanical Spares / Special Tools Requirements; MEC-025 Mechanical Equipment IOM Manual.
- **Static pressure equipment:** MEC-005; MEC-009 Pressure Vessel Data Sheets; REG-022 Pressure Equipment Registration Package.
- **Relief / flare / vent design:** PRO-014; PRO-015 PSV Sizing; PRO-016 Relief Valve Data Sheets; PRO-017 Flare Load Summary; PRO-018 Blowdown / Depressurization Study.
- **Process piping interfaces:** PRO-008 P&IDs; PIP-003 Line List; PIP-004 Tie-In List; PIP-006 Equipment Arrangement; PIP-007 Piping Plans/Sections; PIP-008 Isometric Drawings; PIP-009 Fabrication Isometrics with BOM; PIP-017 Piping MTO; PIP-018 Valve Data Sheets; PIP-024 Hydrotest / Pressure Test Packages; PIP-025 Flushing / Cleaning / Drying Procedure; PIP-028 Piping As-Built Drawings.
- **Utility piping interfaces:** PRO-011 Utility Summary / Consumption Report.
- **Drainage / containment interfaces:** PRO-023 Process Sewer / Closed Drain Design Basis; CIV-014 Bund / Dike / Secondary Containment Drawings.
- **Electrical, lighting, EHT, grounding:** ELE-017 Lighting Layout; ELE-018 Electrical Heat Tracing Design Package; PIP-020 Piping Insulation / Heat Tracing Schedule; PIP-021 Piping Heat Tracing Interface Package; ELE-012 Grounding / Earthing Study; ELE-019 Earthing / Bonding Layout.
- **Instrumentation and controls interfaces:** INS-002 Instrument Index; INS-003 Instrument Data Sheets; INS-005 Instrument Location Plans; INS-006 Hook-Up Drawings; INS-008 Loop Diagrams; INS-009 Wiring / Termination Diagrams; INS-010 Junction Box / Marshalling; INS-011 Cable Schedule; INS-016 Control Valve Data Sheets; INS-017 On-Off / Shutdown Valve Data Sheets; INS-018 I/O List; INS-025 Instrument MTO; INS-029 Instrument As-Built; CTL-003 Control Narrative; CTL-005 Cause and Effect Matrix; CTL-006 DCS I/O List; CTL-026 Package Vendor Interface Specification.
- **Building / HVAC / code interfaces:** PRO-024 Ventilation / Process Safety Equipment Inputs; TSF-023 Building Siting / Occupied Building Risk Assessment; REG-021 Fire Code / Building Code Compliance Package; STR-002 Structural GA; STR-012 Module Structural Drawings.
- **Fire & gas / technical safety interfaces:** TSF-002 F&G Philosophy; TSF-003 F&G Mapping Study; TSF-004 F&G Detector Layout; TSF-009 SIL Determination Report; TSF-011 SRS; TSF-013 Supplier SIL Documentation; TSF-028 Emergency Response Plan Inputs.
- **Structural, foundations, supports, access:** STR-001 Structural Design Basis; STR-004 Calculation Package; STR-005 Foundation Design Calculations; STR-006 Foundation Drawings; STR-011 Platform / Access Drawings; STR-013 Anchor Bolt / Embedment Drawings; STR-014 Lifting Lug / Transport Analysis; STR-020 Structural MTO.

## Examples

No fully reduced example datasheet is provided in the accessible source slice for PKG-056. Vendor RFQ document `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` (referenced from Package Requirements heading 11, "Source Basis") would be the natural example template — its text was not directly extracted in this run (binary not yet processed); **location TBD**.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | Installed inlet-separator quantity at 4-25: current basis = two installed + plot reservation for a third; legacy project references describe four packages. | DBM-Deepcut §"Inlet separator system overview" (line 589) | Legacy project references cited in DBM line 589 | Datasheet Identification / Attributes; Specification R1.1; downstream MPFF source table (DBM line 668) | Use two installed + plot-reservation basis (current governed basis stated in DBM). Treat four-package references as legacy until resolved. | TBD |
| CONF-002 | Per-separator slug capacity: 33.9 m3 (Package Requirements heading 11) vs unresolved 31.8 m3 / 33.9 m3 (DBM line 591). | `26020-Package_Requirements.docx` heading 11, "Scope Notes / Open Items" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 591 | Datasheet Conditions-Design (Slug Capacity); Specification R4.10; MEC-014 calc package | Adopt 33.9 m3 (Package Requirements is source authority for the package scope). Record DBM-side 31.8 m3 figure as legacy. | TBD |
| CONF-003 | Maximum inlet operating pressure (1,300 psig) basis: derived from 90% of an *assumed* upstream pipeline MAOP of 1,440 psig. | DBM line 628 | None (assumption-only) | Datasheet Conditions-Operating; Specification R3.6 | Carry as ASSUMPTION; validate during detailed engineering. | TBD |
| CONF-004 | Inlet-separator overhead exchanger warm-side stream identity unresolved (dehydrated overhead gas from TEG contactor vs warm sweet gas from amine sweetening unit). | DBM line 606 | Same DBM section, both statements present | Process Interfaces narrative; potential downstream-spec impact | Flag for process-engineering ruling; do not pre-decide. | TBD |
