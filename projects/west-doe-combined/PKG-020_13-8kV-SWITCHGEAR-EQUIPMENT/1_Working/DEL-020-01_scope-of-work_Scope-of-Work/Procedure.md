# Procedure: DEL-020-01 Scope of Work

## Purpose

Define the working procedure for producing and checking the EPC Integrator Scope of Work for PKG-020, `13.8kV SWITCHGEAR EQUIPMENT`, using accepted Gate 7 truth and accessible source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook Packages row 22 is available in `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Facility-level DBM electrical basis is available in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Power System, System Voltages, Standby Power, Transformers, Motor Control, Electrical Buildings, Grounding and Bonding, Cable Specifications, Trace Appendix).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Package-specific vendor data: TBD; not present in accessible source slices.
- `_Sources/26020-Package_Requirements.docx`: TBD; no accessible PKG-020 match in this run (HR-020-01-03).

## Steps

1. Confirm deliverable identity from `_CONTEXT.md`: `DEL-020-01_scope-of-work`, Scope of Work, PKG-020, Electrical, EPC Integrator.
2. Confirm package identity from workbook Packages row 22 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-020: ID 20, WBS 01, tracking number `26020-01-30-011`, package name `13.8kV SWITCHGEAR EQUIPMENT`, discipline Electrical.
3. Confirm Gate 7 package basis: Package Vendor responsibility for package engineering/design/equipment/vendor documentation; EPC Integrator responsibility for facility integration/interfaces.
4. Confirm Scope of Work deliverable role from Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-020-01_scope-of-work.
5. Confirm source-supported interface categories from workbook row 22, Gate 7 `PACKAGE_REGISTER.csv` PKG-020, and Gate 7 `INTERFACE_REGISTER.csv` PKG-020 rows: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
6. Use the DBM Power System section to state facility-level function: the 13.8 kV switchgear is the plant main power distribution center, fed from the 25 kV / 13.8 kV / 50 MVA utility-supplied transformer downstream of the BC Hydro 25 kV utility supply (25 kV is TBC per source), with the 13.8 kV bus sized for the full facility scope and distributing radially through step-down transformers to: 6.9 kV Inlet/Sales Compressor Electrical Building; 4.16 kV Acid Gas/Overheads Compressor Electrical Building; 600 V Acid Gas Compressor Electrical Building; 600 V Sales/Overheads Compressor Electrical Building; 4.16 kV/600 V General Area/Tank Farm/Process Electrical Building.
7. Capture the 13.8 kV system basis from the DBM System Voltages table (3 phase, 3 wire, 60 Hz, low-resistance grounded) as facility context only; do not propagate to package-specific switchgear ratings.
8. State explicitly that PKG-020 is not the standby-power tie-in: per the DBM Standby Power paragraph, standby power moves to TOU generators at the 600 V MCC level via transfer switches, replacing the prior centralized 13.8 kV emergency-generator concept.
9. Reference 13.8 kV cable basis (three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded) and the DBM Electrical Buildings bottom-entry cable approach as facility-level construction context for interfaces.
10. Reference the DBM grounding basis (BC Hydro utility transformer 200 A / 10 s NGR tripping system; two-point ground-grid connection for major electrical equipment) as facility-level interface context only.
11. Draft the SOW content so that EPC Integrator scope is limited to integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance support.
12. Mark missing package-specific information as `TBD`, including: tagged equipment; bus continuous current; short-circuit interrupting rating; BIL; breaker count and arrangement; lineup configuration; control voltage source (120 VAC / 125 VDC selection); enclosure type; environmental rating; dimensions; weights; relay/protection settings; coordination tables; and arc-flash boundaries.
13. Carry the utility-voltage "25 kV (TBC)" qualifier as Conflict HR-020-01-01 rather than normalizing it.
14. Carry tagged-equipment allocation (DBM "Medium Voltage Switchgear, qty 1" `ELC-QAS-000007-001`; "810-1 13.8kV Switchgear Electrical Building") as Conflict HR-020-01-02 and keep PKG-020 equipment tags `TBD`.
15. Carry the missing PKG-020 match in `26020-Package_Requirements.docx` as Conflict HR-020-01-03.
16. Carry the absence of PKG-020-specific interface-clause text as Conflict HR-020-01-04; cite workbook/Gate 7 interface flags as the SOW interface list and keep tie-in detail `TBD`.
17. Cross-check the SOW against the Package Datasheet, Construction Work Package assumptions, Vendor Engineered Equipment Package handoff, Vendor Document Turnover Package expectations, and EPC Vendor Package Review and Acceptance needs before closure.

## Verification

- Identity fields match `_CONTEXT.md`, workbook row 22, and Gate 7 `PACKAGE_REGISTER.csv` row PKG-020.
- Responsibility statements match Gate 7 package register and do not transfer vendor design work to EPC.
- Interface list matches workbook row 22 and Gate 7 PKG-020 interface columns / `INTERFACE_REGISTER.csv` rows.
- 13.8 kV facility-context language is not overstated as package-specific switchgear design data.
- All unsupported technical values remain `TBD`.
- Standby-power non-tie-in statement is present and consistent with the DBM.
- Tagged equipment is `TBD` and the allocation question (HR-020-01-02) is visible.
- Human ruling items HR-020-01-01 through HR-020-01-04 are visible in `Guidance.md`.
- Cross-document terminology preserves the accepted package name spelling `13.8kV SWITCHGEAR EQUIPMENT`.
- No undeclared dependencies are treated as blockers.

## Records

- Completed package Scope of Work.
- Tagged equipment and package identity list, with unavailable tag fields marked `TBD`.
- Package function and whole-facility integration narrative (13.8 kV main distribution center; radial step-down to named electrical buildings).
- Responsibility assignment record.
- Interface checklist for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- TBD / Human Ruling Required list for unresolved source gaps.
