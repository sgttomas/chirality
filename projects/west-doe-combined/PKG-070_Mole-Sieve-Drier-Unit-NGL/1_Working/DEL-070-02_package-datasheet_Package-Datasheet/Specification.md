# Specification — DEL-070-02 Package Datasheet (Mole Sieve Drier Unit, NGL)

## Scope

This specification establishes the requirements that the PKG-070 Mole Sieve Drier Unit (NGL) Package Datasheet must satisfy as an EPC Integrator technical handoff to a third-party Package Vendor or discipline package engineering team. The Package Datasheet is the source-supported design-basis instrument that, together with DEL-070-01 (Scope of Work), defines what the NGL molecular-sieve dehydration package must do.

**Covered (per `_CONTEXT.md` Covers Scope Items):** SOW-0145, SOW-0146, SOW-0147, SOW-0148.

**Excluded:** physical installation, construction tie-in, and turnover planning (DEL-070-03); vendor execution and equipment supply (DEL-070-04); vendor document submittal and turnover (DEL-070-05); EPC vendor review and acceptance (DEL-070-06).

## Requirements

### R-1 — Process service identity

The Package Datasheet shall identify the package as the current-scope NGL molecular-sieve dehydration unit serving the 04-25 Deepcut Gas Plant NGL train upstream of NGL storage.
- Source: DBM-Deepcut §Current-Scope NGL Molecular-Sieve Dehydration (line 1574); §Sales-Gas and NGL Treating Overview (lines 1401-1407).

### R-2 — Design throughput

The Package Datasheet shall record the design rate of 2,385 m3/d (15,000 bbl/d).
- Source: DBM-Deepcut line 1585.

### R-3 — Inlet/outlet pressure and temperature envelope

The Package Datasheet shall record the inlet/outlet pressure and inlet temperature envelopes as defined in the DBM:
- Inlet design pressure 1,978 kPag (low/high TBC).
- Outlet design pressure 1,943 kPag (low/high TBC).
- Inlet temperature low 29.7 deg C, design 46.3 deg C, high 51.8 deg C.
- Source: DBM-Deepcut lines 1586-1588.

### R-4 — Water content performance

The Package Datasheet shall require:
- inlet water saturated at design inlet conditions and flow;
- expected outlet water content less than 1 ppmv H2O;
- maximum outlet water content 7 ppmv H2O;
- governing outlet NGL water content target less than 7 ppmw (TBC).
- Source: DBM-Deepcut lines 1589-1592.

### R-5 — Bed pressure drop limits

The Package Datasheet shall require bed pressure drop less than 4 psid (27.6 kPad) at start of life and less than 10 psid at end of life in adsorption, including vessel nozzles.
- Source: DBM-Deepcut lines 1593-1594.

### R-6 — Adsorbent selection

The Package Datasheet shall specify 3A molecular sieve as the adsorbent, with a silica gel guard layer for liquid carryover protection. Adsorbent lifecycle shall be recorded as 3 years (vendor-defined, TBC).
- Source: DBM-Deepcut lines 1595-1596.
- **ASSUMPTION:** The DBM does not state pore-size exclusion rationale explicitly for the NGL system; selection of 3A for the NGL service is taken from the DBM design parameter row as authoritative.

### R-7 — Vessel configuration and sparing

The Package Datasheet shall record a 3-tower configuration. The Package Datasheet shall note that the current basis has no installed spare (one bed in adsorption, one in regeneration) and that sparing shall be reviewed during detailed engineering; a spare installed bed shall be considered if a five-year adsorbent lifecycle is required.
- Source: DBM-Deepcut lines 1584, 1598.

### R-8 — Inlet pretreatment

The Package Datasheet shall require a 2 x 100% liquid/liquid inlet coalescer that removes entrained free water and routes coalesced water by level control to the produced water tank.
- Source: DBM-Deepcut line 1602.

### R-9 — Regeneration gas service

The Package Datasheet shall record sales gas as the regeneration gas service, with the following parameters carried as design basis pending confirmation (TBC):
- regeneration gas flow 3.5 to 5 MMSCFD;
- BEU heat-medium / process-gas shell-and-tube regeneration heater inside the NGL mole-sieve building;
- bed inlet regeneration temperature 460 deg F.
The Package Datasheet shall flag the existence and final source tie-in of the regeneration gas service as TBC and shall not treat the source tie-in as a closed design claim.
- Source: DBM-Deepcut line 1617.

### R-10 — Regeneration cooling and scrubbing

The Package Datasheet shall require:
- aerial regeneration gas cooler with design outlet 110 deg F, maintaining at least 15 deg F above hydrocarbon dewpoint and/or hydrate point at operating conditions;
- automated warm-air recirculation louvers; plenum heating bundle to be considered for winter recirculated-air freeze protection;
- three-phase regeneration-gas scrubber with mist pad; separated water routed by gap level control to produced water drain; separated hydrocarbon routed by level control to the stabilizer flash feed separator at approximately 50 psig;
- TBC items: scrubber drain capacity, hot-bed filling rate, transient recycle to stabilizer overheads compressor and stabilizer.
- Source: DBM-Deepcut lines 1619, 1621.

### R-11 — Outlet filtration

The Package Datasheet shall require a 2 x 100% P2 bag-filter outlet filter, nominal 5 micron, located downstream of the molecular-sieve dehydrator and upstream of downstream heat exchange. Filter type and drain/filling requirements shall be flagged for review.
- Source: DBM-Deepcut line 1623.

### R-12 — Contamination handling

The Package Datasheet shall require provision to blow down regeneration gas to flare if sulphur contamination occurs due to recycled co-adsorbed compounds. A dedicated NGL mole-sieve regeneration gas compressor cylinder at the stabilizer overheads compressor shall be identified as an alternate isolation path for detailed-engineering review.
- Source: DBM-Deepcut line 1578.

### R-13 — Interface declaration

The Package Datasheet shall declare the package interfaces shown in `Datasheet.md` §Interfaces as required handoff facts to the Package Vendor, including: NGL inlet from NGL water wash/mercaptan treating; dry NGL outlet to outlet filter and downstream heat exchange/storage; regeneration gas inlet from sales gas; regeneration return paths; produced water drain; flare; heat medium / process gas; and the alternate vendor regeneration-compressor cylinder option.
- Source: DBM-Deepcut lines 1513, 1558, 1602, 1617, 1621, 1623, 1578.

### R-14 — Open items disclosure

The Package Datasheet shall reproduce all TBC and TBR markers from the DBM source slice so that the Package Vendor sees them as open items rather than closed values. Items currently TBC include: low/high pressure envelopes (R-3), governing outlet ppmw target (R-4), adsorbent lifecycle (R-6), sparing strategy (R-7), regeneration cycle step times other than 24 h adsorption (R-9 context), regeneration gas tie-in (R-9), scrubber drain capacity and transient recycle (R-10), outlet filter type and drain/filling (R-11).

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx, package heading 24 | Package requirements basis cited by decomposition row | location TBD (binary .docx not extracted; clause-level content not accessible in current source set) |
| 26020-Packages_Interfaces_4_export.xlsx, Packages row 74 | Workbook package definition row | location TBD (binary .xlsx not extracted) |
| Industry/jurisdictional codes for pressure vessels, piping, electrical area classification, and aerial cooler design applicable to the NGL service | Required by EPC Integrator practice | TBD — not enumerated in the available source slice |

The Package Datasheet shall cite governing standards and codes as they are confirmed; uncited entries above remain `location TBD`.

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 service identity | Cross-reference with DEL-070-01 Scope of Work and DBM-Deepcut §1574. |
| R-2 throughput, R-3 P/T envelope, R-4 water content, R-5 dP | Tabular comparison of Package Datasheet values to DBM design-parameter table (lines 1582-1598); discrepancies recorded for human ruling. |
| R-6 adsorbent | Confirm 3A + silica gel guard layer is stated; vendor lifecycle proposal received and recorded TBC. |
| R-7 configuration / sparing | Confirm 3-tower configuration and that sparing review is flagged. |
| R-8, R-10, R-11 ancillaries | Confirm presence of each unit (coalescer, cooler, scrubber, outlet filter) with stated sizing and sparing. |
| R-9 regeneration gas | Confirm flow range, heater type/location, and bed-inlet temperature are recorded; confirm TBC flagging on source tie-in. |
| R-12 contamination | Confirm flare blowdown provision and alternate compressor-cylinder isolation path are recorded. |
| R-13 interfaces | Cross-check Package Datasheet §Interfaces against DBM source slices and against PKG-070 INTERFACE_REGISTER entries (location TBD until consulted). |
| R-14 open items disclosure | TBC/TBR marker preservation audit. |

Verification of compliance to 26020-Package_Requirements.docx and the workbook source row remains pending text extraction of those binary sources.

## Documentation

The deliverable shall produce, at minimum:
- this Package Datasheet (`Datasheet.md`) as the primary technical handoff;
- this Specification (`Specification.md`) capturing requirements and verification;
- `Guidance.md` capturing rationale, considerations, and trade-offs;
- `Procedure.md` covering production of the Package Datasheet (and selected operational notes drawn from the source slice).

The deliverable shall reference (without owning) the package interface requirements matrix and the equipment/design criteria evidence, per `_CONTEXT.md` Anticipated Artifacts. The interface matrix and equipment-criteria evidence are intentionally carried within the Package Datasheet rather than as separate deliverables (per `_CONTEXT.md` Notes).
