# Procedure — DEL-066-04 Vendor Engineered Equipment Package

> Operational procedure for producing the vendor-engineered condensate storage tank package and handing it to the EPC Integrator. This Procedure addresses how the deliverable artifact is produced; physical installation and commissioning steps belong to DEL-066-03 (Construction Work Package) and downstream commissioning deliverables.

## Purpose

Define a repeatable, auditable sequence for the Package Vendor to engineer, design, fabricate/supply, and document the PKG-066 condensate storage tank package such that it meets the requirements in `Specification.md` and the rationale in `Guidance.md`, and is acceptable to the EPC Integrator under DEL-066-06.

## Prerequisites

- Receipt of DEL-066-01 (EPC Scope of Work) from the EPC Integrator.
- Receipt of DEL-066-02 (EPC Package Datasheet) from the EPC Integrator, including resolution of CONFLICT C-01 (tank count), CONFLICT C-02 (sour service basis), and CONFLICT C-03 (26020-Package_Requirements package heading 21 contents).
- Access to the 4-25 Deepcut DBM (`4-25_Deepcut_DBM.md`) for design-basis context.
- Vendor purchase order executed.
- Project-level material class, coating standard, instrumentation standard, and tagging convention received from EPC Integrator.
- Plot plan inputs (CIV-235633-5002) or interim coordinate envelope from EPC Integrator (DBM flags this as TBD).
- `_DEPENDENCIES.md` — no upstream dependencies declared at PREPARATION time; the prerequisites above are derived from `_REFERENCES.md` and the package roster context.

## Steps

### 1. Kick-off and Input Reconciliation

1.1 Vendor reviews DEL-066-01 and DEL-066-02 against `Specification.md`. Discrepancies are logged.
1.2 Vendor confirms the resolved authoritative values for C-01, C-02, C-03 (see `Guidance.md` Conflict Table).
1.3 Vendor records the operative density basis (combined/stabilizer-only C5+ table) and confirms the -40 deg C to 60 deg C ambient envelope.

### 2. Tank Mechanical Design

2.1 Produce Modified API 650 datasheet per tank (R-01, R-02, R-03, R-04, R-05).
2.2 Perform shell, roof, anchorage, seismic, wind, and hydrotest calculations.
2.3 Confirm material class against project basis (R-23). Issue MTR plan.
2.4 Confirm coating system against project basis (R-22). Issue coating spec.
2.5 Size PVRV and EPRV (R-08, R-09). Size off-spec overhead vent (R-10).
2.6 Perform thermal expansion review across -40 deg C to 60 deg C (R-11, R-07).
2.7 Compute blanket gas rate per API 2000 (R-12).

### 3. Tank Configuration and Internals

3.1 Designate two tanks as "inlet tanks" per arrangement requirement (R-13).
3.2 Detail the internal pipe stand cascade (R-14).
3.3 Detail the common truck-out manifold (R-15).
3.4 Confirm sediment/water collection arrangement (R-16).

### 4. Nozzle Schedule and Interface Drawings

4.1 Issue nozzle schedule covering blanket gas in, VRU vapour takeoff (Module 930 header tie point), level / temperature instrumentation, inlet (stabilizer bottoms vs cascade), discharge to P-9210-1 / P-9220-1, product recycle return, truck-out, drain, manway, EPRV, PVRV, roof vent (R-17).
4.2 Verify nozzle elevations and orientations to achieve NPSHR ≤ 0.75 m for the transfer pump scope (R-18).
4.3 Cross-check against DEL-066-02 (EPC Package Datasheet) and obtain written EPC acceptance before fabrication release (R-19).

### 5. Civil / Structural Interface

5.1 Issue foundation and anchorage loads to the EPC civil discipline (R-21).
5.2 Confirm tank-to-tank spacing satisfies NFPA 30 Table 22.4.2.1 in the EPC plot plan (R-20).

### 6. Procurement, Fabrication, Inspection

6.1 Issue material requisitions per MTR plan.
6.2 Fabricate to the issued-for-construction (IFC) drawing set.
6.3 Execute the inspection and test plan, including shop hydrotest where required by API 650.
6.4 Generate coating inspection records.

### 7. Vendor Document Submittal

7.1 Compile vendor documentation per `Specification.md` R-24, including datasheets, GAs, nozzle drawings, calculations, MTRs, coating records, ITP, hydrotest report, PVRV/EPRV/vent sizing, thermal expansion review, blanket gas calc, and accessory BOMs.
7.2 Submit into DEL-066-05 (Vendor Document Turnover Package) per the EPC Integrator's vendor document register (R-25).

### 8. EPC Integration Review

8.1 Support EPC Integrator review of integration (DEL-066-06): vendor responds to EPC comments and updates documents as needed.
8.2 Issue final certified documentation set to support construction (DEL-066-03) and turnover.

## Verification

| Check | Method | Pass Criterion |
|---|---|---|
| Modified API 650 datasheet issued per tank | Document review | One certified datasheet per tank, signed by vendor |
| Calculations complete | Document review | Shell, roof, anchorage, seismic, wind, hydrotest all signed and stamped |
| MTRs against material class | MTR review | Each pressure-retaining plate / weld material has a traceable MTR |
| Coating system meets project spec | Coating spec review and inspection records | Approved coating system, holiday and DFT records compliant |
| Inlet/outlet tank designation and cascade | GA drawing review | Two tanks marked as inlet; internal pipe stand drawn |
| Common truck-out manifold | P&ID/GA review | One truck-out connection on the shared manifold; isolation valving as agreed |
| NPSHR ≤ 0.75 m | Hydraulic calc check | Calculated NPSHR at design flow ≤ 0.75 m using transfer pump datasheet |
| Tank-to-tank spacing | Plot plan check | All centerline spacings ≥ 2.35 m and compliant with NFPA 30 / OGAOM as applicable |
| PVRV / EPRV / vent / thermal / blanket | Sizing report review | Each sizing report signed and consistent with API 2000 and project basis |
| Conflict resolutions incorporated | Cross-reference C-01/C-02/C-03 against EPC Package Datasheet | Each conflict's resolved value reflected in vendor datasheets |
| Document register coverage | DEL-066-05 register cross-check | All required vendor documents listed and submitted |

## Records

- Vendor design basis document
- Vendor datasheets per tank
- General arrangement drawings (IFA, IFC, AS-BUILT)
- Nozzle orientation drawings
- Calculations (mechanical, civil-interface, sizing, hydraulic)
- MTRs
- Coating specs and inspection records
- Inspection and test plan, hydrotest report
- PVRV/EPRV/vent sizing report
- Thermal expansion review
- Blanket gas (API 2000) calculation
- Accessory bills of material
- Vendor comment response sheets from EPC integration review
- Final certified documentation set issued for construction and turnover

(All records are routed through DEL-066-05 for register management; DEL-066-06 records integration acceptance evidence.)
