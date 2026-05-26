# Datasheet — DEL-049-02 Package Datasheet (Sales Gas Booster Compressor, PKG-049)

> Source-grounded descriptive datasheet. Substantive values are cited to the
> Deepcut DBM source slice. Unknowns are marked `TBD`; inferences are labeled
> `ASSUMPTION`. The accepted upstream decomposition snapshot is GATE-07
> (2026-05-24). The Word and Excel package source files
> (`26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`)
> are referenced by the decomposition row but are not locally accessible as
> readable source slices; content depending solely on those files is `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-049-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-049` Sales Gas Booster Compressor | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Workbook Row | 80 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Tag (vendor) | `26020-01-PT-12-004` Sales Gas Booster Compressor | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (handoff to Package Vendor) | `_CONTEXT.md`; PACKAGE_REGISTER.csv (Scope_Split) |
| Decomposition Snapshot | GATE-07 Final Published 2026-05-24 | `_REFERENCES.md` |

## Attributes — Package Configuration

| Attribute | Value | Source |
|---|---|---|
| Service | Sweet sales gas booster compression | DBM Deepcut §"Sales Gas Booster Compressor Basis" (line 932-934) |
| Configuration | One x 100% sweet sales gas booster compressor; no installed spare package | DBM Deepcut §932-934, §942, §951; Compression Configuration table (line 877) |
| Compressor type | Separable reciprocating, single induction-motor-driven | DBM Deepcut §934 |
| Frame | Ariel KBK/4, all cylinders dedicated to the single booster stage | DBM Deepcut §936 |
| Stages | One | DBM Deepcut §936, §943 |
| Driver | Electric induction motor, 6,700 hp, 4,000 V, 3-phase, 60 Hz | DBM Deepcut §936 |
| Driver standards | NEMA MG 1; Class F insulation; Class B temperature-rise limit; non-sparking bidirectional cooling fans; TEFC or WPII enclosure | DBM Deepcut §936 |
| Starting basis | DOL with soft-start; no driver speed turndown (mapped basis) | DBM Deepcut §936 |
| Cylinder evaluation | Larger high-efficiency cylinder on two-throw design to be evaluated in detailed engineering (low compression ratio) | DBM Deepcut §936 |
| Clearance pockets | Automated continuously variable or fixed-volume clearance pockets to be evaluated against standard manual variable volume clearance pockets — `TBD` until detailed engineering | DBM Deepcut §930, §969 |

## Conditions — Process Design

| Parameter | Value | Source |
|---|---|---|
| Capacity (design) | 3,962 e3m3/d (140 MMSCFD) in both J-T and expander modes; high/excess capacity TBC | DBM Deepcut §934, §947 |
| Suction pressure | 6,137 kPag (890 psig); low suction pressure `TBD` | DBM Deepcut §934, §944 |
| Suction temperature | 43 deg C service basis; 35 deg C winter / 43.3 deg C summer in design table | DBM Deepcut §934, §945 |
| Discharge pressure | 12,866 kPag (1,866 psig); normal discharge pressure TBC | DBM Deepcut §934, §946 |
| Minimum MAWP (suction and discharge) | 13,100 kPag (1,900 psig) | DBM Deepcut §948 |
| Design temperature, suction | 149 deg F (65 deg C); 300 deg F (149 deg C) alternate | DBM Deepcut §949 |
| Design temperature, discharge | 177 deg F (81 deg C); 350 deg F (177 deg C) alternate | DBM Deepcut §949 |
| Water content (inlet) | <0.1 ppmv (upstream molecular sieve dehydration) | DBM Deepcut §950 |
| Sparing | No spare compressor; no spare package equipment/instrumentation | DBM Deepcut §951 |

### Inlet Gas Composition (mol%)

| Compound | Expander mode | J-T mode | Source |
|---|---:|---:|---|
| Methane | 88.31 | 84.84 | DBM Deepcut §957 |
| Ethane | 11.32 | 9.61 | DBM Deepcut §958 |
| Propane | 0.03 | 3.63 | DBM Deepcut §959 |
| Nitrogen | 0.17 | 0.46 | DBM Deepcut §960 |
| Carbon dioxide | 0.15 | 0.42 | DBM Deepcut §961 |

## Construction — Package Sub-Systems

| Sub-system | Description | Source |
|---|---|---|
| Suction scrubber | Two-phase suction scrubber upstream of compression; final need to be evaluated in detailed engineering due to very low inlet-gas dewpoint; assumed inlet liquid density 0.61 SG; horizontal double-hook vane-style demister acceptable; sizing per API-11P or vendor vane-style demister sizing | DBM Deepcut §963 |
| Suction pressure control valve | Full-port automated ball valve with upstream manual isolation; 5 psid differential pressure allowance; fails closed | DBM Deepcut §963 |
| Aftercooler | Horizontal airflow, single-fan, on-module air cooler; winter outlet 35.0 deg C; summer outlet 43.3 deg C; simulated first-stage gas-section dP 69.0 kPad (design dP TBC); automated pneumatic louver control required | DBM Deepcut §965 |
| Blowdown valve | Fails closed; sized for start from equalization pressure; equalization pressure shall not exceed system MAWP | DBM Deepcut §967 |
| Recycle valve | Sized for 100% capacity at minimum pipeline operating pressure and high suction pressure (initial start-up case); fail position fail-closed (TBC in detailed engineering); single full-port manual isolation on recycle valve outlet | DBM Deepcut §969 |
| Bypass option | If an additional automated bypass valve is needed, alternate is to depressure back into the sales compressor discharge header | DBM Deepcut §967 |
| Lube oil | Electric circulating lube oil heater included | DBM Deepcut §967 |
| Packing drains/vents | Collected to common seal pot; seal-pot vapour routed to VRU suction header; liquids trucked out locally; distance-piece sweep purge required to prevent backflow from VRU header | DBM Deepcut §967 |
| Sweet gas purge | Manual sweet gas purge NOT included; remains an external-responsibility item | DBM Deepcut §967 |
| Automated sequences | Isolation, purging, pressurization, depressurization, lubrication, start-up, loading, unloading, cooldown, and shutdown sequences are automated | DBM Deepcut §967 |
| Filter/coalescer (downstream, F-3500-1) | In 350 fuel gas module adjacent to the booster package; receives cooled gas from aftercooler; removes aerosols, lube oil, particulates; 1 x 100% with manual bypass and isolation for filter change-out; clean dP <2 psid | DBM Deepcut §1471, §1474-§1482 |

### Filter/Coalescer F-3500-1 Operating Envelope

| Parameter | Summer | Winter | Notes | Source |
|---|---:|---:|---|---|
| Expected normal inlet flow, MMSCFD | 95 | 95 | low/high TBC | DBM Deepcut §1475 |
| Design inlet flow, MMSCFD | TBD | TBD | Records differ between 100 and 140 MMSCFD; confirmation required (CONFLICT, see Guidance) | DBM Deepcut §1476, §1808 |
| Expected normal temperature, deg C | 43.3 | 35 | low/high/design TBC | DBM Deepcut §1477 |
| Expected normal pressure, kPag | 11,376 TBC | 11,376 TBC | low/design TBC | DBM Deepcut §1478 |

## Interfaces (carried as evidence within this datasheet)

Applicable interface types for the package (PACKAGE_REGISTER.csv, Applicable_Interfaces):

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

Process interface evidence:

- Suction header: HP Sales Header 2 from sales compressors 2400/2500; ~95 MMSCFD nominal to booster suction; ~20 MMSCFD flow-controlled to HP Sales Header 1 (DBM Deepcut §1435).
- Discharge routing: through booster aftercooler to F-3500-1, then through sales gas splitter for TC Energy (TCPL) pipeline delivery; bypass downstream of F-3500-1 can route gas toward TC sales gas splitter meter on booster shutdown (DBM Deepcut §1436, §1471).
- Booster shutdown case: HP Sales Header 1 receives gas from compressors 2100/2200/2300/2400/2500 (~277 MMSCFD) at ~11,376 kPag (DBM Deepcut §1434).
- Sales booster compressor sweep and purge gas flow basis: 340 (units per source table); detailed values `TBC` (DBM Deepcut §1712).

Non-process interface scope details (Electrical Power voltage class beyond motor, EHT, Grounding/Bonding, Area Lighting, I&C cabling, Building HVAC/Services, Fire & Gas, Maintenance Access, Structural/Foundations): `TBD` — not present in accessible source slices. Resolution requires Word source (`26020-Package_Requirements.docx` package heading 4) and Excel interface export.

## References

- DBM Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Sales Gas Booster Compressor Basis" (lines 932-969), §"Sales Gas Booster Filter/Coalescer" (lines 1469-1483), §"Compression Configuration" (lines 870-879), §"HP Sales Header" (lines 1434-1436), §"Sales booster compressor sweep and purge gas" (line 1712).
- Decomposition row: DELIVERABLE_REGISTER.csv `DEL-049-02_package-datasheet` (GATE-07 snapshot).
- Package register row: PACKAGE_REGISTER.csv `PKG-049` (GATE-07 snapshot).
- Word source `26020-Package_Requirements.docx` package heading 4 — referenced by decomposition; not locally accessible as text; `location TBD`.
- Excel source `26020-Packages_Interfaces_4_export.xlsx` — referenced by decomposition; not locally accessible as text; `location TBD`.
- RFQ source `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` (referenced by PACKAGE_REGISTER row Word_Source_Basis); not locally accessible; `location TBD`.
