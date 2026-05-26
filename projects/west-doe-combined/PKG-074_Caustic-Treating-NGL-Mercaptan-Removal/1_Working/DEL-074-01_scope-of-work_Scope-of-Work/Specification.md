# Specification — DEL-074-01 Scope of Work (PKG-074 Caustic Treating, NGL Mercaptan Removal)

> Normative scope-of-work specification for the EPC Integrator deliverable. Requirements are anchored to PKG-074 SCOPE_LEDGER entries and the 04-25 Deepcut DBM. Where the source itself defers a value, this specification carries `TBD` or `TBC` rather than inventing a requirement. Inferences are labeled `ASSUMPTION`.

## Scope

### In scope

- Define the full EPC Integrator package scope for PKG-074 Caustic Treating (NGL Mercaptan Removal), including the package function, package boundaries, tagged equipment list, source basis, and whole-facility integration narrative for the 04-25 Deepcut Gas Plant. (`_CONTEXT.md`; DELIVERABLE_REGISTER.csv DEL-074-01)
- Carry the workbook-defined vendor-responsible Mechanical package as a distinct flat project package for WBS 01, with the Package Vendor owning engineering, design, and equipment, and the EPC Integrator owning facility integration. (SOW-0059)
- Specify a complete caustic treating system for NGL/C3+ mercaptan removal immediately downstream of the de-ethanizer. (SOW-0060)
- Enumerate major included equipment: caustic contactor/mixer equipment, caustic outlet filtration, water wash and coalescing equipment, caustic regeneration equipment (see Conflict Table), heaters/exchangers, circulation and transfer pumps, pressurized caustic drain drum, DSO handling, caustic storage interfaces, incinerator interface, instrumentation, controls, and building-contained caustic equipment. (SOW-0061)
- Define responsibility assignment between Package Vendor and EPC Integrator across engineering, design, supply, fabrication, integration review, and turnover. (DELIVERABLE_REGISTER.csv anticipated artifact: "responsibility assignment record")
- Document the open governing-process-basis conflict (regenerative DBM vs. non-regenerative SCA-001/VE-8) and the resolution path. (SOW-0062)

### Out of scope

- Vendor engineering and detailed design of the package (assigned to Package Vendor under DEL-074-04). (OBJ-004; DELIVERABLE_REGISTER.csv DEL-074-04)
- Construction work-package detail (carried in DEL-074-03). (DELIVERABLE_REGISTER.csv)
- Vendor document turnover register and submittals (carried in DEL-074-05). (DELIVERABLE_REGISTER.csv)
- EPC vendor-package review and acceptance evidence (carried in DEL-074-06). (DELIVERABLE_REGISTER.csv)
- Package technical datasheet values and interface requirements matrix (carried in DEL-074-02 Package Datasheet). (DELIVERABLE_REGISTER.csv)
- Cross-package facility-wide deliverables (electrical, controls, civil/structural, utilities) except as required to state PKG-074 interface boundaries. (`_CONTEXT.md` scope statement)

## Requirements

> Numbered REQ items are scope-of-work requirements imposed by this deliverable. Each cites a source. `ASSUMPTION` labels mark inferences not directly stated in source.

### Package identity and basis

- **REQ-074-01-001** The Scope of Work shall identify the package as PKG-074 Caustic Treating (NGL Mercaptan Removal), Mechanical discipline, EPC Scope of Work type, with the Package Vendor responsible for engineering/design/equipment and the EPC Integrator responsible for facility integration. (SOW-0059; DELIVERABLE_REGISTER.csv)
- **REQ-074-01-002** The Scope of Work shall declare the source basis as Workbook Packages row 51 and `26020-Package_Requirements.docx` package heading 28. (DELIVERABLE_REGISTER.csv; `_REFERENCES.md`)
- **REQ-074-01-003** The Scope of Work shall declare the accepted upstream decomposition snapshot as `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` and cite it as authority for package identity, deliverable set, and scope items. (`_CONTEXT.md`; `_REFERENCES.md`)

### Package function

- **REQ-074-01-010** The package shall provide non-regenerative caustic mercaptan removal from cooled C3+ NGL immediately downstream of the de-ethanizer, sized for 2,385 m3/d (15,000 bbl/d). (4-25_Deepcut_DBM.md "Current-Scope NGL Mercaptan Treating")
- **REQ-074-01-011** Treated NGL shall flow downstream to NGL filtration, water wash, molecular-sieve dehydration, and NGL storage. (4-25_Deepcut_DBM.md SEC-07)
- **REQ-074-01-012** Rich caustic shall flow to caustic heating and spent-caustic storage/handling; the current basis includes no active on-site caustic regeneration column. (4-25_Deepcut_DBM.md SEC-07; see Guidance.md Conflict Table)
- **REQ-074-01-013** Disulphide oil shall be routed to the on-site 400 bbl DSO storage tank for truck-out; alternate mixing of recovered DSO into C5+ product is permitted only after detailed engineering review. (4-25_Deepcut_DBM.md "Disulphide Oil, Spent Caustic, and Waste Amine")
- **REQ-074-01-014** Spent caustic shall be routed to the on-site 400 bbl spent caustic storage tank for truck-out and off-site disposal. (4-25_Deepcut_DBM.md SEC-04)

### Equipment scope (major included items)

- **REQ-074-01-020** The package shall include the major equipment categories enumerated in SOW-0061: caustic contactor/mixer, caustic outlet filtration (2 x 100%), water wash and coalescing equipment, caustic regeneration equipment (subject to Conflict Table), heaters/exchangers, circulation and transfer pumps (water wash recycle 2 x 100% vertical inline centrifugal with single mechanical seals), pressurized caustic drain drum, DSO handling, caustic storage interfaces, incinerator interface, instrumentation, controls, and building-contained caustic equipment. (SOW-0061; 4-25_Deepcut_DBM.md SEC-07)
- **REQ-074-01-021** The Scope of Work shall carry the thirteen tagged items listed in 26020-Package_Requirements.docx package heading 28 as the package's tagged equipment list, and shall reconcile the one duplicated tag identified in SOW-0062 before issue to the Package Vendor. (SOW-0062; tag list `TBD` — heading 28 slice not locally extracted)
- **REQ-074-01-022** The package shall include a pressurized caustic drain drum (V-6940-1) with heating, insulation, demister, sizing K < 0.2; drum vapours route to the stabilizer overheads compressor (SOC) first-stage suction; drum liquids are level controlled to the spent caustic storage tank. (4-25_Deepcut_DBM.md SEC-07)
- **REQ-074-01-023** Fresh, spent, and DSO storage tanks shall each be 1 x 400 bbl atmospheric, heated, insulated, with LP fuel-gas blanket. Fresh caustic tank shall be truck-in capable and shall NOT be connected to the VRU header. Spent caustic and DSO tanks shall be truck-out capable, vent to the incinerator header, and be protected against backflash with a flame arrestor. (4-25_Deepcut_DBM.md "NGL Mercaptan Treating Equipment and Utilities")

### Building, materials, and safety

- **REQ-074-01-030** All caustic-containing equipment shall be installed indoors in the Mercaptan Treating Unit building or immediately adjacent area, with provisions for caustic freezing and crystallization risk. (4-25_Deepcut_DBM.md SEC-07)
- **REQ-074-01-031** No aluminum materials shall be installed in the caustic building. Insulation cladding and straps in caustic exposure areas shall be stainless steel. Caustic storage tank materials/coatings shall be polymer or other caustic-compatible materials; final selection is detailed-engineering `TBD`. (4-25_Deepcut_DBM.md SEC-07)
- **REQ-074-01-032** The building shall include water safety showers; quantity and location are `TBD` pending detailed engineering. Shower activation shall provide a discrete control-room alert. (4-25_Deepcut_DBM.md SEC-07)

### Interfaces

- **REQ-074-01-040** The package shall interface with the de-ethanizer outlet (inlet stream), downstream NGL filtration/water wash/molecular-sieve dehydration, the stabilizer overheads compressor first-stage suction (caustic drain drum vapour route), the LP fuel-gas blanket header, the incinerator header at the 3-25 facility (spent caustic and DSO vapours), the produced water system (water wash drain), the electrical building (motor loads), the BPCS and package control system, and the building HVAC system. (4-25_Deepcut_DBM.md SEC-07, "Incinerator Interface"; OBJ-003, OBJ-005, OBJ-006, OBJ-007)
- **REQ-074-01-041** The Scope of Work shall preserve commercial stream disposition, metering accountability, and facility boundary interfaces consistent with OBJ-003, including treated NGL C3+ product disposition through the NGL storage, dehydration, and downstream LACT path. (OBJ-003; 4-25_Deepcut_DBM.md "NGL C3+ Product")

### Responsibility split (EPC Integrator vs. Package Vendor)

- **REQ-074-01-050** The Scope of Work shall record the responsibility assignment consistent with OBJ-004: Package Vendor owns package engineering, package design, vendor documentation, physical equipment supply, and fabrication; EPC Integrator owns facility integration, interface coordination, integration review, and turnover acceptance. (OBJ-004; DELIVERABLE_REGISTER.csv DEL-074-04 / DEL-074-05 / DEL-074-06)
- **REQ-074-01-051** The Scope of Work shall identify the third-party proprietary process provider as the source of the detailed engineering package for the caustic treating unit. (4-25_Deepcut_DBM.md SEC-07)

### Safety, regulatory, operability (cross-cutting objectives)

- **REQ-074-01-060** The Scope of Work shall flow down sour-service, fire/gas, methyl mercaptan detection, shutdown, relief, drain/containment, environmental, and code/standards requirements consistent with OBJ-009 to the Package Vendor. Specific code lists are `TBD` (24-25 DBM SEC-15 slice not extracted into this deliverable). (OBJ-009; ASSUMPTION: codes apply based on facility-wide regulatory basis)
- **REQ-074-01-061** The Scope of Work shall flow down operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and controlled open-item closure requirements consistent with OBJ-010 to the Package Vendor. (OBJ-010)

### Open items

- **REQ-074-01-070** The Scope of Work shall surface and require vendor/process-provider confirmation of the governing process basis (regenerative DBM vs. non-regenerative SCA-001/VE-8). The non-regenerative basis is carried as the current default per the 04-25 DBM. (SOW-0062; 4-25_Deepcut_DBM.md SEC-07; see Conflict Table CFT-001)
- **REQ-074-01-071** The Scope of Work shall list and require closure of the open items inherited from the source basis, including: pressure low/high cases (`TBC`), circulating caustic concentration confirmation, fresh caustic tank SG (1.75 `TBC`), DSO tank SG (1.75 `TBC`), winter vapour pressure values, high-ethane case review, process provider selection, contactor stage count, water make-up routing, DSO blending into C5+ disposition, building floor material, caustic tank material selection, safety shower quantity/location, and incinerator supplemental fuel-gas rate and operational responsibility. (4-25_Deepcut_DBM.md SEC-07 and "Incinerator Interface")

## Standards

- `26020-Package_Requirements.docx` package heading 28 — governing source for package scope; clause-level extract `location TBD`.
- 04-25 Deepcut DBM (`DBM-Deepcut/4-25_Deepcut_DBM.md`), SEC-07 — governing process basis for current-scope non-regenerative caustic treating.
- Facility-wide codes and standards basis (4-25 DBM SEC-15) — applicable but slice not extracted into this deliverable (`location TBD`).
- API, ASME, CSA, and provincial regulatory standards — `ASSUMPTION: likely applicable` for caustic service, atmospheric storage tanks, indoor process buildings, and sour-service piping; clause-level identification deferred to Package Datasheet (DEL-074-02) and to the Package Vendor under DEL-074-04.

## Verification

| Requirement set | Verification approach | Verifying deliverable |
|---|---|---|
| REQ-074-01-001 through -003 (identity and basis) | Document review against `_CONTEXT.md`, DELIVERABLE_REGISTER.csv, and `_REFERENCES.md` | This Scope of Work; EPC Vendor Package Review (DEL-074-06) |
| REQ-074-01-010 through -014 (package function) | Process design review against 04-25 DBM SEC-07; vendor process flow review | DEL-074-02 Package Datasheet; vendor process package (DEL-074-04) |
| REQ-074-01-020 through -023 (equipment scope) | Equipment list reconciliation against heading 28 tagged items; vendor equipment list review | DEL-074-02 Package Datasheet; DEL-074-04 vendor package |
| REQ-074-01-030 through -032 (building/materials/safety) | Materials certificate review; safety shower commissioning test; building inspection | DEL-074-03 Construction Work Package; DEL-074-06 review and acceptance |
| REQ-074-01-040 through -041 (interfaces) | Interface matrix verification against interface register | DEL-074-02 Package Datasheet; INTERFACE_REGISTER.csv |
| REQ-074-01-050 through -051 (responsibility split) | Responsibility matrix review; process provider identification confirmation | This Scope of Work; DEL-074-06 |
| REQ-074-01-060 through -061 (cross-cutting safety/operability) | Code and standards compliance review; sparing/isolation/winterization review | DEL-074-04 vendor package; DEL-074-06 review and acceptance |
| REQ-074-01-070 through -071 (open items) | Open-item register closure with documented rulings | DEL-074-06 review and acceptance; vendor documentation (DEL-074-05) |

## Documentation

Required artifacts produced by or referenced from this deliverable (per DELIVERABLE_REGISTER.csv "Anticipated Artifacts"):

- Package scope of work narrative (this document and accompanying narrative content in `Guidance.md`)
- Tagged equipment and package identity list (REQ-074-01-021; tag list closure pending heading 28 slice)
- Package function and integration narrative (`Guidance.md`)
- Responsibility assignment record (REQ-074-01-050)

Companion deliverables in PKG-074:

- DEL-074-02 Package Datasheet — technical datasheet and interface requirements matrix
- DEL-074-03 Construction Work Package — installation, tie-in, turnover
- DEL-074-04 Vendor Engineered Equipment Package — vendor engineering, design, fabrication, equipment supply
- DEL-074-05 Vendor Document Turnover Package — vendor document register and submittals
- DEL-074-06 EPC Vendor Package Review and Acceptance — review log, acceptance checklist, turnover evidence
