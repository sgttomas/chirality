# Procedure: DEL-046-04 — Vendor Engineered Equipment Package (Acid Gas Compressors)

This procedure describes the steps to **produce and accept** the Vendor Engineered Equipment Package for PKG-046. Steps to **operate** the package belong to operations procedures derived from the vendor's control narrative (handed over via DEL-046-05).

## Prerequisites

- DEL-046-01 Scope of Work (PKG-046) issued by EPC Integrator. (Conceptual upstream — not declared in _DEPENDENCIES.md; treat as ASSUMPTION until declared.)
- DEL-046-02 Package Datasheet (PKG-046) issued by EPC Integrator. (Conceptual upstream — same caveat.)
- Accepted upstream decomposition snapshot: /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24
- Locally accessible authoritative sources:
  - _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md (SEC-05 Compression and Acid Gas Handling Basis)
  - _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (site ambient envelope, acid gas routing)
- _CONTEXT.md and _REFERENCES.md for this deliverable.
- Resolution of Conflict Table items C-1 through C-3 in Guidance.md is required before vendor design freeze. (TBD)
- Disposal well pressure characteristics (Design/Min/Max) from Tourmaline. (TBC)

## Steps

### Stage A — Inquiry and award
A1. EPC Integrator issues RFQ based on PKG-046 Scope of Work and Package Datasheet to qualified package vendors. (ASSUMPTION on RFQ mechanism; aligns with 26020-01-PT-RFQ-12-001_Acid Gas Compressor.docx reference in PACKAGE_REGISTER.)
A2. Vendors submit proposals including compressor model, performance curves, control narrative, package layout, and price.
A3. Technical evaluation against Specification.md requirements R-...-001 through R-...-021; resolve Conflict Table items C-1, C-2, C-3 via human ruling.
A4. Commercial evaluation and contract award.

### Stage B — Vendor engineering
B1. Vendor produces process basis: heat-and-material balance for Design, Start-up, and High-CO2 cases; confirms compressor model (R-...-002) and 5th-stage discharge basis (R-...-007) per ruling.
B2. Vendor performs API 618 pulsation and mechanical analysis (Design Approach Level: TBD).
B3. Vendor issues package P&IDs, equipment list, instrument index, cause-and-effect / control narrative, and area classification drawings.
B4. Vendor produces datasheets for compressor, driver, scrubbers, air coolers, recycle valves, blowdown valve, seal pot, lube/auxiliary systems, Coriolis meter, and analyzer.
B5. Vendor confirms hydrate-inhibition strategy and methanol injection capacities (R-...-018; Conflict C-5).
B6. EPC Integrator review and IFC release of vendor documents. (ASSUMPTION on review gate; specific gate names TBD.)

### Stage C — Procurement and fabrication
C1. Vendor procures long-lead items (compressor frame, motor, VFD, air coolers).
C2. Material test reports and PMI records collected against R-...-019 (sour service).
C3. Pressure-containing components fabricated and stamped per applicable code; per-stage MAWP/temperature per Datasheet schedule (R-...-008).
C4. Skid/module assembly per vendor layout and shop QC plan.
C5. Winterization, building, HVAC, and lighting per ambient envelope (R-...-020) and PACKAGE_REGISTER interface types.

### Stage D — Factory Acceptance Test (FAT)
D1. Execute FAT per Inspection and Test Plan (ITP) against Verification matrix in Specification.md.
D2. Demonstrate performance at Design and Start-up flow points (R-...-006); record discharge pressures and temperatures.
D3. Demonstrate recycle operation (HP and LP recycle paths) and fail-open action on blowdown (R-...-011, R-...-012).
D4. Demonstrate automated sequencing (R-...-015) start-up from equalization pressure.
D5. Demonstrate cooler louver control and warm-air recirculation logic (R-...-009).
D6. Hydrotest per code; calibrate Coriolis meter and analyzer (R-...-016).
D7. EPC Integrator witnesses FAT and signs FAT report. (ASSUMPTION on witness scope.)

### Stage E — Delivery and field installation interface
E1. Vendor disassembles per shipping plan; preserves equipment per preservation plan.
E2. Ship to site; transfer custody to EPC Integrator.
E3. Vendor field representative supports erection, mechanical completion, and pre-commissioning at the facility interface (EPC Integrator scope). The vendor's package boundary remains the package boundary; facility tie-ins are EPC Integrator scope per PACKAGE_REGISTER.

### Stage F — Closeout to vendor documentation deliverable
F1. Vendor assembles documentation per DEL-046-05 (Vendor Document Turnover Package) requirements. (Closeout into adjacent deliverable; not produced under DEL-046-04.)
F2. EPC Integrator performs vendor package review and acceptance per DEL-046-06.

## Verification

| Stage | Verification check | Records |
|---|---|---|
| A | Technical evaluation completed and conflicts ruled | Tech evaluation memo, ruling records |
| B | All requirements R-...-001..-021 addressed in vendor design package | Compliance matrix |
| B | Pulsation/mechanical study accepted | Study report |
| C | MTR/PMI/coded fabrication records complete | MTRs, PMI, code data reports |
| D | FAT report signed; performance points met | FAT report |
| D | Hydrotest pass; meter/analyzer calibration | Hydrotest cert, calibration certs |
| E | Custody transfer documented; preservation maintained | BoL, preservation log |
| F | Documentation handover complete to DEL-046-05 | Turnover index |

## Records

The following records evidence delivery of this deliverable (kept under EPC Integrator and Package Vendor document control):

- Vendor proposal and technical evaluation memo.
- Award letter / purchase order.
- Vendor design basis and per-component datasheets.
- P&IDs, equipment list, instrument index, control narrative, cause-and-effect.
- API 618 pulsation and mechanical study.
- Material test reports, PMI records, pressure vessel code data reports.
- ITP, FAT procedure, FAT report (with EPC Integrator witness signature).
- Hydrotest certificates, calibration certificates for Coriolis meter and acid gas analyzer.
- Shipping plan, preservation plan, bills of lading.
- Field service report(s) from vendor representative.
- Conflict-resolution records for C-1 through C-5 (Guidance.md).
- Turnover index (handed to DEL-046-05).
