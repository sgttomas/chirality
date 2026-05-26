# Specification: DEL-095-04 Vendor Engineered Equipment Package (PKG-095 Tanks, Slop API 650)

## Scope

### In scope
- Engineering, design, fabrication/supply, and physical delivery of the slop tankage vendor package per `PKG-095 - Tanks, Slop (API 650)`, developed from the EPC Scope of Work (DEL-095-01) and the EPC Package Datasheet (DEL-095-02). [Source: `_CONTEXT.md` Scope]
- Vendor package design basis and vendor datasheet set covering tank shell, roof, foundation interface, nozzles, internals, PVRV/EPRV, instrumentation, heat tracing, insulation, coating, and truck-in/out interfaces. [Source: `_CONTEXT.md` Anticipated Artifacts; `3-25_Comp_and_Liquids_DBM.md` lines 421, 1644, 1661]
- Compliance with Modified API 650 atmospheric tank basis (16 oz test pressure equivalent class) and `26020-Package_Requirements.docx` package heading 47 (location TBD at clause level). [Source: `4-25_Deepcut_DBM.md` line 518; `_REFERENCES.md`]

### Out of scope (excluded)
- Pipeline tie-ins and EPC-side piping downstream of the vendor's package battery limit; these are EPC integrator scope per the Scope of Work split. [ASSUMPTION; confirm at DEL-095-02 issue]
- Off-site disposal/trucking operations beyond the tank truck-in/out interface envirobox connection. [Source: `3-25_Comp_and_Liquids_DBM.md` line 1661]
- Facility flare and KO drum equipment (separate packages); slop receives liquids from KO drum pumps but the slop package terminates at its inlet header nozzle. [Source: `3-25_Comp_and_Liquids_DBM.md` line 497]

## Requirements

| Req ID | Requirement | Source | Notes |
|---|---|---|---|
| SPEC-095-04-R1 | Tanks shall be designed and fabricated to Modified API 650 (atmospheric) with 16 oz test pressure equivalent class | `4-25_Deepcut_DBM.md` line 518; `3-25_Comp_and_Liquids_DBM.md` line 1646 | Tank-family basis from DBM |
| SPEC-095-04-R2 | Condensate slop tank (03-25, TK-9130-2) shall be sized at 1 x 3,800 bbl with design SG 1.00 (TBC) and shall be fully insulated | `3-25_Comp_and_Liquids_DBM.md` lines 406, 463, 1643-1644 | TBC flag carried |
| SPEC-095-04-R3 | Slop tank arrangement at 04-25 (Deepcut) shall be 2 x 2,000 bbl with handling/disposal service | `4-25_Deepcut_DBM.md` line 494 | |
| SPEC-095-04-R4 | Tanks shall be externally insulated and heated, with tank heating consistent with the -40 deg C minimum ambient site basis | `3-25_Comp_and_Liquids_DBM.md` line 421 (Modified API-650 tank-family basis); site basis statements | ASSUMPTION extension from produced-water tank family to slop tank family |
| SPEC-095-04-R5 | Each tank shall have at least one PVRV; EPRV sizing shall be reviewed during detailed engineering | `4-25_Deepcut_DBM.md` line 522 | ASSUMPTION for slop service from produced-water tank basis |
| SPEC-095-04-R6 | Tank maximum fill shall be limited to 90% of tank volume; thermal expansion shall be reviewed | `4-25_Deepcut_DBM.md` line 519 | |
| SPEC-095-04-R7 | Tank isolation philosophy shall be reviewed in the context of potential sour vapours | `4-25_Deepcut_DBM.md` line 523 | |
| SPEC-095-04-R8 | Tank foundations shall be designed against the final geotechnical report and equipment-specific anchorage criteria | `3-25_Comp_and_Liquids_DBM.md` (foundations section) | |
| SPEC-095-04-R9 | Internal coating shall be Devchem 253 (floor, walls, roof) unless DEL-095-02 specifies otherwise for slop service | `3-25_Comp_and_Liquids_DBM.md` line 421 | ASSUMPTION carry-over from produced-water tank basis; confirm in DEL-095-02 |
| SPEC-095-04-R10 | Material of construction (MOC) shall be specified per `26020-Package_Requirements.docx` heading 47 and DEL-095-02 | `_REFERENCES.md`; `_CONTEXT.md` | TBD - not in accessible DBM slices |
| SPEC-095-04-R11 | The condensate slop tank (03-25) shall be configured to receive: inlet-tank manual cascade, hydrocarbon drain header, LP condensate pump header, stabilizer outlet header, flare KO drum pump discharges, amine surge skim, caustic unit drain drum (TBD), amine/TEG flash skims | `3-25_Comp_and_Liquids_DBM.md` lines 1665, 497 | |
| SPEC-095-04-R12 | The condensate slop tank shall have a dedicated truck-in/out envirobox connection | `3-25_Comp_and_Liquids_DBM.md` line 1661 | |
| SPEC-095-04-R13 | Tank vapour management shall be compatible with site VRU/blanket-gas/LP flare philosophy; slop tank shall not be connected to VRU unless DEL-095-02 directs otherwise | `3-25_Comp_and_Liquids_DBM.md` lines 438, 463 | ASSUMPTION: similar to fresh-caustic / makeup-tank philosophy |
| SPEC-095-04-R14 | Vendor shall conform vendor document deliverables to the EPC vendor document register format defined in DEL-095-05 | `DELIVERABLE_REGISTER.csv` row DEL-095-05 | |
| SPEC-095-04-R15 | All instrumentation, electrical, and controls interfaces shall conform to the facility electrical area classification and the -40 deg C ambient | `3-25_Comp_and_Liquids_DBM.md` (site/electrical basis) | |

## Standards

| Standard | Use | Locally accessible | Source |
|---|---|---|---|
| API 650 (Modified) | Atmospheric tank design, fabrication, examination | Standard not in repo; cited via DBM | `4-25_Deepcut_DBM.md` line 518; `3-25_Comp_and_Liquids_DBM.md` line 1646 - location TBD at clause level |
| NFPA 30 | Tank spacing, atmospheric tank to property line / building (referenced for facility spacing) | Standard not in repo; cited via DBM | `4-25_Deepcut_DBM.md` lines 283-284 - location TBD at clause level |
| API 2510 | Pressurized storage spacing (limited applicability) | Standard not in repo | `4-25_Deepcut_DBM.md` line 282 |
| OGAOM Sec. 9.6.15 | Spacing - tanks vs flare, public road, etc. (Alberta) | Standard not in repo | `4-25_Deepcut_DBM.md` lines 285-289 |
| `26020-Package_Requirements.docx` package heading 47 | Package-level engineering deliverables and core vendor documents | Source file present in repo; text not extracted | `_REFERENCES.md`; location TBD at clause level |

## Verification

| Req ID | Verification approach | Source |
|---|---|---|
| SPEC-095-04-R1 | Vendor design-basis review against API 650; hydrostatic / 16 oz test record per pressure test plan; MTRs | `4-25_Deepcut_DBM.md` line 518 |
| SPEC-095-04-R2, R3, R6 | Sizing calculation review (capacity, working/fill volume, thermal expansion) by EPC Integrator | `4-25_Deepcut_DBM.md` line 519 |
| SPEC-095-04-R4, R9 | Coating QA records (DFT, holiday test), insulation/heating system FAT or commissioning checks | `3-25_Comp_and_Liquids_DBM.md` line 421 |
| SPEC-095-04-R5, R7 | PVRV/EPRV sizing review during detailed engineering; sour-vapour isolation review in HAZOP | `4-25_Deepcut_DBM.md` lines 522-523 |
| SPEC-095-04-R8 | Geotechnical-driven anchorage review; foundation drawings vs final geotech | `3-25_Comp_and_Liquids_DBM.md` foundations section |
| SPEC-095-04-R10 | MOC confirmation against DEL-095-02 and `26020-Package_Requirements.docx` heading 47 | `_REFERENCES.md` |
| SPEC-095-04-R11, R12 | P&ID review of inlet/outlet nozzle list and envirobox interface; nozzle schedule reconciliation | `3-25_Comp_and_Liquids_DBM.md` lines 1661, 1665 |
| SPEC-095-04-R13 | Vapour management review with VRU/flare/blanket-gas systems; HAZOP node review | `3-25_Comp_and_Liquids_DBM.md` lines 438, 463 |
| SPEC-095-04-R14 | Vendor document register conformance check at turnover (DEL-095-05) | `DELIVERABLE_REGISTER.csv` row DEL-095-05 |
| SPEC-095-04-R15 | Electrical area classification and ambient design review during detailed engineering | site basis |

## Documentation

Vendor shall deliver (specific document IDs per `26020-Package_Requirements.docx` heading 47 - TBD at clause level):

- Vendor package design basis (descriptive)
- Tank datasheets per tank tag (e.g., TK-9130-2 for 03-25 condensate slop)
- Equipment general arrangement (GA) drawings and nozzle schedules
- P&ID extensions for tank inlet/outlet interfaces (incl. envirobox)
- Instrumentation list and control narrative for level/temperature/PVRV monitoring
- Weld map, NDE records, MTRs (per QLT requirements)
- Hydrostatic / pressure test plan and records
- Coating and insulation QA records
- Vendor Data Book / Final Supplier Documentation at turnover (per DEL-095-05)
