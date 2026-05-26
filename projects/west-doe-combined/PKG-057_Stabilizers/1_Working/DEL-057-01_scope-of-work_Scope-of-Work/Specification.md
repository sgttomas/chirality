# Specification — DEL-057-01_scope-of-work — Scope of Work (PKG-057 Stabilizers)

This Specification is the normative companion to the Datasheet. It states what the EPC Scope of Work for the PKG-057 Stabilizers package must contain when issued. It is grounded in the Gate 7 PROJECT_DECOMP snapshot and the locally accessible source slices listed in References. Inferred items are labeled **ASSUMPTION**; missing source-supported values are marked **TBD**.

## Scope

### In scope (this deliverable shall cover)

1. The full EPC Scope of Work for PKG-057 Stabilizers, including tagged equipment, package function, source basis, package boundaries, and whole-facility integration narrative. (Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv `_description`.)
2. Identification of the three (3) Inlet Stabilizer Packages (3 x 40% design with future-fourth provision) and their role in the inlet-liquids processing train at 04-25. (Source: SOW-0178; SOW-0179; DBM-Deepcut SEC-04 line 612.)
3. Process function statement: receive raw condensate from MPFF bottoms; stabilizer flash-feed produced-water knockout; basket-strained feed-pump transfer; feed/bottoms exchanger pre-heat; stabilizer column reboiled distillation; stabilized C5+/NGL liquid product to NGL mercaptan treating; stabilizer overhead vapour to SOC second-stage suction. (Source: SOW-0178; DBM-Deepcut SEC-04 lines 575, 678, 710, 712.)
4. Package boundary statement: skid-edge boundaries with explicit "by others" items (interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, installation/erection). (Source: SOW-0180.)
5. Responsibility assignment: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (Source: PACKAGE_REGISTER.csv `_responsibility`; OBJ-004.)
6. Facility integration narrative covering interface types applicable to the package: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. (Source: PACKAGE_REGISTER.csv `_interface_types`.)
7. Source-supported equipment list per package: stabilizer column (20 floating-valve trays), stabilizer flash feed separator, stabilizer feed pumps (2 x 100%), basket strainers, feed/bottoms exchanger, reboiler, product cooler, level/temperature instrumentation (1 LIT, 1 TIT minimum). (Source: SOW-0179; SOW-0180; DBM-Deepcut SEC-04 lines 706–708.)
8. Coverage of scope items SOW-0177, SOW-0178, SOW-0179, SOW-0180 (SCOPE_LEDGER.csv).

### Out of scope (this deliverable shall not redefine)

- Detailed vendor engineering or vendor design work (carried by DEL-057-04 Vendor Engineered Equipment Package). (Source: DELIVERABLE_REGISTER.csv.)
- Construction installation execution detail (carried by DEL-057-03 Construction Work Package). (Source: DELIVERABLE_REGISTER.csv.)
- Vendor document register and turnover (carried by DEL-057-05 Vendor Document Turnover Package). (Source: DELIVERABLE_REGISTER.csv.)
- EPC vendor-package review and acceptance (carried by DEL-057-06). (Source: DELIVERABLE_REGISTER.csv.)
- Datasheet content (carried by DEL-057-02 Package Datasheet). (Source: DELIVERABLE_REGISTER.csv.)
- Local 03-25 stabilization (removed; stabilization consolidated to 04-25). (Source: DBM-Comp_and_Liquids line 65.)

## Requirements

R1. The EPC Scope of Work shall identify the package as PKG-057 Stabilizers, vendor tag 26020-01-PT-17-005, three (3) Inlet Stabilizer Packages. (Source: PACKAGE_REGISTER.csv; SOW-0178.)

R2. The EPC Scope of Work shall state the per-package design rate of 1,272 m3/d (8,000 bbl/d), 3 x 40% installed basis, 3:1 turndown, and future-fourth-package plot provision. (Source: SOW-0179; SOW-0180; DBM-Deepcut SEC-04 line 612.)

R3. The EPC Scope of Work shall state the MPFF-to-stabilizer one-to-one pairing and the operational consequence (loss of stabilizer takes paired MPFF out of service; 80% capacity on single-unit outage). (Source: DBM-Deepcut SEC-04 lines 608–612.)

R4. The EPC Scope of Work shall state the stabilizer flash feed separator operating basis (345 kPag, 30.6 °C, ~15 min retention TBC, ≥10 min LLL–HLL) and design basis (1,724 kPag, 60 °C). (Source: SOW-0180; DBM-Deepcut SEC-04 line 704.)

R5. The EPC Scope of Work shall state the stabilizer column operating basis (top-tray feed at ~71 °C; trayed reboiled column; 20 floating-valve trays; 3:1 turndown; minimum design pressure 793 kPag). (Source: SOW-0179; SOW-0180; DBM-Deepcut SEC-04 line 678.)

R6. The EPC Scope of Work shall require the feed/bottoms exchanger to be sized for a 16.7 °C (30 °F) minimum approach with inlet liquids on the shell side. (Source: SOW-0180; DBM-Deepcut SEC-04 line 706.)

R7. The EPC Scope of Work shall require two 100% multistage horizontal centrifugal feed pumps with upstream basket strainers; strainer mesh and seal type remain TBD pending detailed engineering. (Source: DBM-Deepcut SEC-04 line 706.)

R8. The EPC Scope of Work shall require the reboiler to be a vertical NEN single-pass thermosiphon, process fluid on tube side, tubes seal-welded to tubesheet, hot heat medium supply; heat-medium temperature is to be reviewed during detailed engineering. (Source: DBM-Deepcut SEC-04 line 706.)

R9. The EPC Scope of Work shall require the product cooler to have 130% excess area at the design point, single fan, cooling product to 110 °F (43.3 °C). (Source: SOW-0180; DBM-Deepcut SEC-04 line 708.)

R10. The EPC Scope of Work shall require feed pumps and product cooler fan drivers to be electric motors, VFD compatible. (Source: SOW-0180.)

R11. The EPC Scope of Work shall route stabilized C5+ product to NGL mercaptan treating as primary feed, with a manual single-package divert capability to the condensate slop tank. (Source: DBM-Deepcut SEC-04 line 710.) ASSUMPTION: divert provision is interpreted as a package-level routing requirement at the EPC interface.

R12. The EPC Scope of Work shall require stabilizer overhead vapour to be pressure controlled to SOC second-stage suction and stabilizer flash feed overhead to SOC first-stage suction; relief and blowdown from the flash feed separator and stabilizer tower shall route to HP flare. (Source: DBM-Deepcut SEC-04 lines 678, 704, 813.)

R13. The EPC Scope of Work shall enumerate the package boundary and "by others" items: interconnecting piping at skid edge, DCS integration, foundations, electrical power supply from plant MCC, installation/erection. (Source: SOW-0180.)

R14. The EPC Scope of Work shall require the package to be developed under the Package Vendor / EPC Integrator responsibility model (per OBJ-004), with vendor engineering, design, documentation, and equipment supply held with the vendor and facility integration held with the EPC Integrator. (Source: PACKAGE_REGISTER.csv; OBJ-004.)

R15. The EPC Scope of Work shall reflect all applicable package-level interface types listed in PACKAGE_REGISTER.csv `_interface_types` for whole-facility integration. (Source: PACKAGE_REGISTER.csv.)

R16. The EPC Scope of Work shall preserve sour-service, fire-and-gas, relief, blowdown, drain/containment, environmental, and codes/standards constraints applicable to the package. (Source: OBJ-009; DBM-Deepcut SEC-14, SEC-15.) Detailed clause-level requirements: **location TBD** — relevant DBM SEC-14/SEC-15 slices not opened in this pass.

R17. The EPC Scope of Work shall preserve operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, and turnover requirements from OBJ-010. (Source: OBJ-010.)

## Standards

The following standards are governing for this scope; clause-level citations are **location TBD** until source slices are opened:

- DBM-Deepcut SEC-15 Regulatory, Codes, and Standards Basis (location TBD).
- DBM-Deepcut SEC-09 Energy, Prime Movers, and Emissions Basis (location TBD).
- DBM-Deepcut SEC-14 Instrumented Protection Basis (location TBD).
- 26020-Package_Requirements.docx package heading 12 (governing package-requirements text for PKG-057; SOW-0178/0179/0180 are extracts).
- Vendor RFQ 26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0 (location TBD; not opened as raw source in this pass).

ASSUMPTION: standard package specifications referenced by the vendor RFQ (mechanical/process pressure-vessel codes, etc.) are likely applicable but are not enumerated here in absence of locally opened source slices.

## Verification

| Requirement | Verification approach |
|---|---|
| R1, R2 | Inspection of the Scope of Work text against PACKAGE_REGISTER and SOW-0178/0179. |
| R3 | Inspection against DBM-Deepcut SEC-04 lines 608–612. |
| R4–R10 | Inspection against the Datasheet (DEL-057-02) once issued and against SOW-0180 / DBM-Deepcut SEC-04 lines 678–708. |
| R11–R12 | Cross-check with downstream interface artifacts (SOC, NGL mercaptan treating, HP flare) in INTERFACE_REGISTER.csv. |
| R13 | Inspection of skid-edge battery limit drawing list against SOW-0180 "By others" clause. |
| R14 | Inspection of responsibility-matrix section against PACKAGE_REGISTER `_responsibility` and OBJ-004. |
| R15 | Cross-check against PACKAGE_REGISTER `_interface_types` and INTERFACE_REGISTER rows for PKG-057. |
| R16, R17 | Traceability check against OBJ-009 and OBJ-010 evidence. (Detailed verification clauses TBD.) |

## Documentation

The Scope of Work itself, plus references to the package's anticipated artifacts:
- Package scope of work (this deliverable).
- Tagged equipment and package identity list (this deliverable; see Datasheet).
- Package function and integration narrative (this deliverable).
- Responsibility assignment record (this deliverable).
- Downstream deliverables produced from this Scope of Work: DEL-057-02 (Package Datasheet), DEL-057-03 (Construction Work Package), DEL-057-04 (Vendor Engineered Equipment Package), DEL-057-05 (Vendor Document Turnover Package), DEL-057-06 (EPC Vendor Package Review and Acceptance). (Source: DELIVERABLE_REGISTER.csv.)
