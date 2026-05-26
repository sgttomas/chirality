# Datasheet — DEL-056-04 Vendor Engineered Equipment Package

**Pass:** P1 (Datasheet) | **DECOMP_VARIANT:** PROJECT | **Skill:** four-documents

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-056-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-056` |
| PackageName | Inlet Separators 4-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers Scope Items | SOW-0127; SOW-0128; SOW-0129; SOW-0130 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic per `_CONTEXT.md`) |

## Attributes

The Vendor Engineered Equipment Package comprises engineered, designed, and supplied physical equipment for the Inlet Separators 4-25 package, anchored to the EPC Scope of Work (DEL-056-01) and Package Datasheet (DEL-056-02).

| Attribute | Value | Source |
|---|---|---|
| Package function | Inlet receipt and separation: pig receiver/isolation plus horizontal three-phase inlet separators | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Inlet receipt and separation row) |
| Separator configuration (current authority) | Two identical horizontal three-phase inlet separator packages, each ~50% of facility capacity | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Conflicting legacy count | Legacy "four inlet separator packages" / "4 x 50%" tabulation preserved as unresolved | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Representative tags | V-1600-2 / V-1700-2 (Comp_and_Liquids basis); V-1600-1 / V-1700-1 (Deepcut basis) | both DBM files; CONFLICT — see Conflict Table in `Guidance.md` |
| Separator size (Deepcut basis) | 9 ft ID x 40 ft S/S, horizontal three-phase | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Internal coating | Devchem 253 internal coating on separator vessel; associated piping not internally coated | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Mist eliminator | Vertical high-performance mesh/vane type, operations-review subject | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Weir | Manually adjustable weir per separator | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Inlet pressure control valves | At least two parallel balanced-globe PCVs per package, hardened trim, design dP <= 5 psid at design inlet pressure | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Produced-water level-control valves | At least two parallel per package | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Liquid outlet heater | One per separator package; warms cold liquid (~-26 deg C) to a temperature sustaining MPFF LCV feed above hydrate/freeze thresholds | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Heater outlet temperature, duty, medium | TBD pending process simulation; candidate media warm glycol or process-stream cross-exchange | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Building | Self-framing package building enclosing instrumentation and one end of vessel (configuration shared with MPFF arrangement narrative) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour natural gas, sour raw condensate, sour produced water (three-phase) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Maximum inlet operating pressure | 1300 psig (based on 90% of assumed upstream gathering pipeline MAOP of 1440 psig); must be validated in detailed engineering | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Plant gate design pressure upstream of inlet PCV downstream manual isolation | MAWP equal to upstream inlet pipeline | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Design pressure downstream of inlet PCV to J-T valve/expander outlet isolation | 1360 psig (600# flanges at 200 deg F equivalent) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Inlet separator shut ESDV pressure shutdown | 1360 psig (Deepcut basis); 635 psig at inlet separator ESDV per Comp_and_Liquids basis — CONFLICT | both DBM files; see Conflict Table |
| Total design inlet vapour flow | 300 MMSCFD (sum of metered overhead vapour) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Per-separator slug capacity | Unresolved between 31.8 m3 and 33.9 m3 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Peak produced water, water retention time, condensate retention time | TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Methanol service | Methanol injection upstream of PCV and upstream of HCL/water dump valves; design capacities TBC | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Drive gas | Sales gas upstream of sales gas splitter (alternate: inlet compressor discharge); separately metered to each inlet separator package | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| HIPPS requirement | TBC during detailed engineering if inlet pipeline MAOP exceeds facility inlet design pressure | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

## Construction

| Item | Value | Source |
|---|---|---|
| Pressure vessel design | Per applicable pressure class, sour-service requirements, corrosion allowance, coating, manway access, internals removal, drainage, venting, inspection | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Specific bases for separator vessels | Per SEC-04 of the design basis memorandum, including Devchem 253 internal coating | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Package isolation philosophy | Multiple parallel packages isolated on a unit basis so an entire unit can be isolated and removed from service while remaining units operate | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Inlet ESDV (facility) | Full-port piggable with position transmitters on the pig receiver inlet skid | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Outlet manual isolation | Permits PCV maintenance without blowing down the full separator | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Skid-edge inlet isolation | Isolates inlet PCVs for maintenance | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Shop/field assignment | Shop-built (Deepcut tag table: 160-1 Inlet Separator, 170-1 Inlet Separator listed as Shop) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Vendor design basis and datasheet set | Anticipated artifact produced by vendor engineering | `_CONTEXT.md`; DELIVERABLE_REGISTER row 375 |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Inlet Separator Design Parameters and related sections)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Inlet separation system; pressure vessel design)
- `_Sources/26020-Package_Requirements.docx` — package heading 11 (location: docx; clause-level slice TBD until extracted)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 68 (location TBD until extracted)
- Decomposition: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 375
- Upstream anchor deliverables (this folder consumes): DEL-056-01 (Scope of Work), DEL-056-02 (Package Datasheet)
