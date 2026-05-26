# Guidance: DEL-095-04 Vendor Engineered Equipment Package (PKG-095 Tanks, Slop API 650)

## Purpose

This deliverable exists because PKG-095 is a vendor-supplied package of slop storage tanks built to a Modified API 650 atmospheric tank basis. The EPC Integrator authors the Scope of Work (DEL-095-01) and Package Datasheet (DEL-095-02); the Package Vendor consumes those inputs and produces a complete engineered package - design, datasheets, and the physical tank equipment - that the EPC Integrator can review (DEL-095-06), receive turnover for (DEL-095-05), and install (DEL-095-03). [Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows DEL-095-01 through DEL-095-06]

## Principles

- **Vendor as production unit, not standalone designer.** The vendor's engineering authority is bounded by the EPC Scope of Work and Package Datasheet; battery limits, fluid-system tie-ins, and facility-level basis are EPC scope. [Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`]
- **API 650 Modified is the family standard.** Tank shell, roof, foundation interface, and test class follow Modified API 650; deviations require explicit EPC ruling. [Source: `4-25_Deepcut_DBM.md` line 518; `3-25_Comp_and_Liquids_DBM.md` line 1646]
- **Slop is a sink, not a process tank.** The slop tank receives heterogeneous drain/skim/KO-pump flows. Design for variable composition, sour vapour potential, and infrequent but high-rate truck-out. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 1661-1665]
- **Cold climate governs envelope details.** Insulation, electrical heat trace, and PVRV/EPRV winterization are governed by the -40 deg C ambient and the facility's heat-trace philosophy. [Source: `3-25_Comp_and_Liquids_DBM.md` site basis statements]
- **Conservative on open items.** Where the DBM marks values "TBC" (tank design SG, MOC, coating applicability for slop, EPRV sizing), the vendor carries explicit TBDs rather than assumed values. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 421, 1643; `4-25_Deepcut_DBM.md` lines 519, 522]

## Considerations

- **Sour vapour management.** Slop receives flow from sour drain and skim sources. Isolation philosophy must address potential sour vapour exposure during sampling, truck-out, and maintenance. [Source: `4-25_Deepcut_DBM.md` line 523]
- **Truck-in/out interface.** The 03-25 condensate slop tank has a dedicated envirobox connection; layout the truck spot for grade access without obstructing flare or tank-farm access. [Source: `3-25_Comp_and_Liquids_DBM.md` line 1661]
- **Coating applicability.** Devchem 253 is the produced-water tank coating basis. Whether the same coating system applies to slop service should be confirmed in DEL-095-02; do not propagate as a binding requirement until confirmed. [Source: `3-25_Comp_and_Liquids_DBM.md` line 421]
- **PVRV sizing scenarios.** Slop tank inlets include drain header surges and flare KO drum pump discharges; PVRV/EPRV sizing scenarios should cover simultaneous large-flow inputs and blanket-gas regulator failure modes. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 1665, 463]
- **Functional allocation is provisional.** "Unless superseded by final tank register" applies; vendor should design to nominal sizing while flagging final tank register changes as DEL-095-02 inputs. [Source: `3-25_Comp_and_Liquids_DBM.md` line 406]
- **Amine slop tank scope inclusion.** The amine regeneration module has its own amine slop tank. Whether this is part of PKG-095 vendor scope or a separate amine-package scope is TBD; resolve in DEL-095-02. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 532, 1143]

## Trade-offs

- **Vendor-standard tank design vs. EPC-specific requirements.** Vendors typically have a standard API-650 product. The Modified-API-650 + 16 oz test class + Devchem 253 coating + envirobox interface combination may not map to vendor catalog defaults; price-vs-conformance trade-off should be transparent. [Source: `3-25_Comp_and_Liquids_DBM.md` line 421; `4-25_Deepcut_DBM.md` line 518]
- **Insulation/heating envelope vs. inspection access.** Full insulation and tank heating add maintenance complexity (shell inspection, heat-trace continuity). Vendor design should leave inspection windows / accessible terminations. [Source: `3-25_Comp_and_Liquids_DBM.md` line 1644]
- **Conservative MOC vs. cost.** Without DEL-095-02 MOC confirmation, conservative MOC choices (e.g., upgraded steel for sour service) raise cost; under-spec'd MOC risks rework after HAZOP. Carry MOC as TBD. [Source: `_REFERENCES.md`; `_CONTEXT.md`]

## Examples

- The DBM equipment register lists a single 3,800 bbl slop tank at the 03-25 Liquids Hub with 80 bbl/d throughput and ~40-day holdup. The vendor scope must engineer and supply this tank with the listed interfaces. [Source: `4-25_Deepcut_DBM.md` line 498; `3-25_Comp_and_Liquids_DBM.md` line 406]
- The DBM equipment register lists two 2,000 bbl slop tanks at the 04-25 Deepcut Gas Plant with 200 bbl/d throughput and ~17-day holdup. [Source: `4-25_Deepcut_DBM.md` line 494]
- The condensate slop tank receives stabilizer outlet manual diversions and LP fuel-gas scrubber V-3210-2 liquid drains, illustrating the heterogeneous-source design challenge. [Source: `3-25_Comp_and_Liquids_DBM.md` lines 463, 710]

Worked dimensional examples (nozzle schedule, GA, heat-trace layouts) are TBD pending issue of DEL-095-02.

## Conflict Table (for human ruling)

This table records HRR (Human Ruling Required) items: cross-source conflicts and unresolved-from-sources items affecting clause-level requirements.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-095-04-01 | Tank capacity and count for slop service at 03-25: DBM equipment register shows "1 x 3,800 bbl" while functional allocation prose says "one slop tank" in the 11-tank condensate group "unless superseded by final tank register" | `4-25_Deepcut_DBM.md` line 498 (1 x 3,800 bbl) | `3-25_Comp_and_Liquids_DBM.md` line 406 (one slop tank, subject to final tank register) | Datasheet Attributes, Specification R2 | Treat 1 x 3,800 bbl as the design basis until final tank register issues otherwise | TBD |
| HRR-095-04-02 | Internal coating applicability: Devchem 253 is stated for produced-water tanks; slop tank coating not explicitly named | `3-25_Comp_and_Liquids_DBM.md` line 421 (produced-water tank coating) | (no explicit slop-tank coating slice located) | Datasheet Construction; Specification R9 | Carry Devchem 253 as ASSUMPTION; confirm in DEL-095-02 | TBD |
| HRR-095-04-03 | Material of construction for slop tanks not specified in accessible DBM slices | `_REFERENCES.md`; `26020-Package_Requirements.docx` heading 47 (location TBD) | (no DBM MOC slice for slop tank located) | Datasheet Construction (MOC); Specification R10 | Carry MOC as TBD; resolve via DEL-095-02 and source heading 47 | TBD |
| HRR-095-04-04 | Inclusion of amine slop tank in PKG-095 vendor scope: amine slop tank appears in amine regeneration module description, not in the PKG-095 narrative | `3-25_Comp_and_Liquids_DBM.md` lines 532, 1132, 1143 (amine slop tank in amine module) | `_CONTEXT.md` (PKG-095 Tanks, Slop API 650 - generic slop tankage) | Datasheet Conditions; Specification Scope | Treat amine slop tank as out of PKG-095 vendor scope until DEL-095-02 directs otherwise | TBD |
| HRR-095-04-05 | VRU connection for slop tank: VRU collects vapours from condensate and produced-water tank systems; slop tank connection not explicitly enumerated | `3-25_Comp_and_Liquids_DBM.md` line 438 (VRU vapour collection scope) | (no explicit "slop tank to VRU" slice located) | Datasheet Conditions; Specification R13 | Treat slop tank as NOT connected to VRU unless DEL-095-02 directs otherwise | TBD |
| HRR-095-04-06 | EPRV sizing scenarios for slop tank receiving simultaneous flare KO drum pump discharge and drain header surges | `3-25_Comp_and_Liquids_DBM.md` line 1665 (multiple input sources) | `4-25_Deepcut_DBM.md` line 522 (EPRV sizing to be reviewed) | Specification R5; Verification | EPRV sizing must address simultaneous-input scenario; carry as detailed-engineering review | TBD |
