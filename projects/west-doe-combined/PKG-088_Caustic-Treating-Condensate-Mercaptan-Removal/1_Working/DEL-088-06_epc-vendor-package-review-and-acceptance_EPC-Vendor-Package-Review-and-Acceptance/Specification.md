# Specification — DEL-088-06 EPC Vendor Package Review and Acceptance

## Scope

This deliverable specifies the EPC Integrator's review, integration acceptance, and handoff-readiness verification activities applied to the PKG-088 Caustic Treating (Condensate Mercaptan Removal) package supplied under DEL-088-04 (Vendor Engineered Equipment Package) and DEL-088-05 (Vendor Document Turnover).

**In scope:**
- Review of vendor engineering, fabrication, FAT, and turnover documentation against:
  - EPC Scope of Work (DEL-088-01)
  - EPC Package Datasheet (DEL-088-02)
  - Construction Work Package (DEL-088-03)
- Documented integration acceptance and handoff-readiness decision for the vendor package.

**Out of scope:**
- Vendor design, fabrication, or FAT execution (DEL-088-04 / DEL-088-05).
- Final operating/commissioning procedures executed downstream of acceptance.
- Standalone interface deliverables (interface facts remain in DEL-088-02).

## Requirements

### R1 — Acceptance Basis Documents

The EPC Integrator shall perform the package review and acceptance against the accepted versions of DEL-088-01 (SOW), DEL-088-02 (Package Datasheet), and DEL-088-03 (Construction Work Package). [Source: _CONTEXT.md Scope]

### R2 — Non-Regenerative Caustic Mercaptan Treating Conformance

The vendor package shall implement non-regenerative caustic mercaptan treating (Merichem or equivalent) with 20,000 bbl/d C5+ treating capacity, with no caustic regeneration included. Acceptance shall confirm vendor documentation evidences these basis values. [Source: 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating]

### R3 — DSO Entrainment Verification

Acceptance shall verify vendor evidence supports DSO entrainment at expected 30 ppmw S with design value 50 ppmw S (TBC by vendor). [Source: same]

### R4 — Caustic Solution Basis

Acceptance shall verify vendor data confirms the caustic solution basis of 50 wt% NaOH/H2O with SG 1.75 (TBC). [Source: same]

### R5 — Package Component Completeness

Acceptance shall confirm the vendor package includes a caustic C5+ contactor, pre-heater, caustic outlet filter, water wash, DSO/spent/fresh-caustic/fresh-water tanks, and incinerator overhead/dilution/enrichment-gas interfaces. [Source: same]

### R6 — Material and Storage Restrictions

Acceptance shall verify:
- Aluminum is not used in the caustic building.
- Fresh and spent caustic tanks are atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation.
- Spent caustic tank vents through a flame arrestor to the incinerator header.
- Fresh caustic is not connected to the VRU.
[Source: same]

### R7 — Caustic Drain Interface

Acceptance shall verify caustic drain design conforms to minimum 300# ANSI rating, with maximum temperature 121 deg C / 250 deg F (TBC) and heat-tracing provisions consistent with the facility basis. [Source: 3-25_Comp_and_Liquids_DBM.md §Drains]

### R8 — Extractable Compounds Coverage

Acceptance shall verify vendor process guarantees address H2S, CO2, and methyl/ethyl/propyl/butyl mercaptans as the extractable compound set. [Source: 3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating]

### R9 — Vendor Document Turnover Conformance

Acceptance shall verify DEL-088-05 turnover artifacts (vendor document register, submittals, source-required vendor documentation, turnover records) are present, complete, and consistent with DEL-088-02. [Source: DELIVERABLE_REGISTER.csv row DEL-088-05]

### R10 — Construction and Tie-in Conformance

Acceptance shall verify vendor scope is consistent with the installation, tie-in, inspection, and turnover requirements stated in DEL-088-03. [Source: DELIVERABLE_REGISTER.csv row DEL-088-03]

### R11 — Acceptance Decision Record

The EPC Integrator shall produce a documented acceptance decision identifying: status (accept / accept-with-conditions / reject), open non-conformances, conditional-acceptance conditions, and handoff-readiness call. [ASSUMPTION: standard EPC acceptance practice; explicit format `location TBD` in 26020-Package_Requirements.docx package heading 41]

## Standards

| Standard / Source | Coverage | Location |
|---|---|---|
| 26020-Package_Requirements.docx package heading 41 | Package requirements basis | location TBD (binary source not extracted) |
| 26020-Packages_Interfaces_4_export.xlsx | Package interface basis | location TBD |
| 3-25_Comp_and_Liquids_DBM.md | Design Basis Memorandum for 03-25 facility (governing for caustic treating attributes) | _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md |
| ANSI B16.5 (300# rating) | Caustic drain flange rating | ASSUMPTION; explicit clause TBD |
| HAZOP discipline review | Required for caustic drain pressure segregation | 3-25_Comp_and_Liquids_DBM.md §Drains |

## Verification

| Req | Verification Approach |
|---|---|
| R1 | Document trace matrix mapping vendor docs to accepted versions of DEL-088-01/02/03 |
| R2 | Review of vendor PFD, process datasheet, and technology selection statement |
| R3 | Review of vendor process guarantees and FAT evidence |
| R4 | Review of vendor utilities/consumables datasheet |
| R5 | Bill of equipment and P&ID review against listed component set |
| R6 | Material certification review; constructability review against caustic-building exclusions |
| R7 | Piping class review; drain interface drawing review |
| R8 | Process guarantee review; sulphur speciation in vendor performance test |
| R9 | Vendor document register reconciliation against DEL-088-05 |
| R10 | Constructability and tie-in review against DEL-088-03; punch-list closure |
| R11 | Issued acceptance decision record signed by EPC Integrator |

## Documentation

The deliverable produces the following anticipated artifacts (from _CONTEXT.md):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence (FAT, integration witness)
- Turnover evidence
