# Specification: DEL-089-03 — Construction Work Package

> **Document role:** Normative — defines what the Construction Work Package (CWP) for `PKG-089 Pig Receivers (Inlet) 3-25` must contain, the standards it must satisfy, how its content is verified, and what documentation it must produce.

## 1. Scope

### 1.1 In scope
- Defines the EPC Integrator's Construction Work Package for PKG-089, covering field installation, building, inspection, turnover, and tie-in of the pig receiver skid(s) into the operating facility.
- Addresses all interface types listed for PKG-089: Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging. [Source: `PACKAGE_REGISTER.csv` row PKG-089]
- Covers `SOW-0157`, `SOW-0158`, `SOW-0159`, `SOW-0160`. [Source: `DELIVERABLE_REGISTER.csv` row DEL-089-03]

### 1.2 Out of scope
- Package engineering, package design, vendor documentation, and physical equipment fabrication, which are owned by the Package Vendor and produced under `DEL-089-04` and `DEL-089-05`. [Source: `PACKAGE_REGISTER.csv` row PKG-089 (Scope/Boundary)]
- Operations-phase pigging procedures beyond what is required to commission and turn over the package; ongoing operator pigging and flowback management is referenced as a downstream operations concern. [Source: DBM line 270]
- Offsite pipeline design and the pipeline contractor's scope upstream of the plant inlet boundary (first aboveground flange within lease boundary). [Source: DBM line 228]

## 2. Requirements

| ID | Requirement | Authority | Basis |
|---|---|---|---|
| R-089-03-01 | The CWP shall describe construction means and methods for installing the PKG-089 skid(s) on dedicated structural-steel non-enclosed skid foundations within the lease boundary. | NORMATIVE | DBM lines 230, 237; PACKAGE_REGISTER.csv row PKG-089 |
| R-089-03-02 | The CWP shall define tie-in scope for each interface type applicable to PKG-089 (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging). | NORMATIVE | PACKAGE_REGISTER.csv row PKG-089 (Interface types) |
| R-089-03-03 | The CWP shall include an installation and tie-in workface plan that sequences skid setting, pipeline tie-in at the first aboveground flange within the lease boundary, and tie-in to the two inlet separators (V-1600-2 / V-1700-2). | NORMATIVE | DBM lines 228, 244; DELIVERABLE_REGISTER.csv row DEL-089-03 |
| R-089-03-04 | The CWP shall include a construction interface and turnover checklist covering each applicable interface type and the EPC-Integrator-to-operations handoff. | NORMATIVE | DELIVERABLE_REGISTER.csv row DEL-089-03 (Anticipated Artifacts) |
| R-089-03-05 | The CWP shall preserve the inlet ESDV functional requirements (full-port, piggable, position transmitters) through installation, alignment, and testing. | NORMATIVE | DBM lines 230, 239 |
| R-089-03-06 | The CWP shall include provisions for sweet-gas purge and HP flare vent connections at the pig receiver, including pressure testing, purge, and inerting prior to introducing hydrocarbon service. | NORMATIVE | DBM line 238 |
| R-089-03-07 | The CWP shall reconcile the pig receiver count and size with the upstream Package Datasheet (`DEL-089-02`) and Scope of Work (`DEL-089-01`) before mobilization; the construction basis shall match the package datasheet at time of issue for construction (IFC). | NORMATIVE (interface) | PACKAGE_REGISTER.csv row PKG-089 vs. DBM line 230 — see Guidance §Conflict Table |
| R-089-03-08 | The CWP shall identify all hold points, witness points, and code-required inspections, including pressure testing of pig receiver pressure boundaries and tie-in welds, and shall require sour-service compliant materials and weld procedures where applicable. | NORMATIVE | Sour service per DBM §SEC-04 line 244; specific code clauses — **location TBD** (heading 42 of `26020-Package_Requirements.docx`) |
| R-089-03-09 | The CWP shall describe drain/containment provisions for hydrocarbon and produced-water releases during pig launching/receiving operations, consistent with the facility grading/site drainage/spill containment interface basis. | NORMATIVE | PACKAGE_REGISTER.csv row PKG-089 (Interface types) |
| R-089-03-10 | The CWP shall traverse construction completion through mechanical completion to operations turnover, with documented punchlist closeout. | NORMATIVE | DELIVERABLE_REGISTER.csv row DEL-089-03 (Description) |

> **ASSUMPTION:** Requirements R-089-03-08 cites code/clause obligations only at the level of "code-required inspections" because the specific code text in `26020-Package_Requirements.docx` heading 42 is not locally readable in this run.

## 3. Standards

| Standard / Reference | Role | Location / Status |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 42 | Source for package-level construction, inspection, and turnover requirements applicable to PKG-089 | location TBD (binary source) |
| `Bid Docs/26020-02-PT-RFQ-35-001-Pig_Recv_1.docx` | Pig Receiver RFQ — vendor scope basis that the CWP must align to for vendor-supplied skid receipt and installation | location TBD (binary source) |
| `3-25_Comp_and_Liquids_DBM.md` §SEC-04 | DBM basis for inlet pipeline interface and pigging | Locally accessible; lines 226–240 |
| Facility welding, NDE, and pressure testing standards | ASSUMPTION: project standards govern; specific standards list — location TBD | location TBD |
| Sour-service material standards (e.g., NACE MR0175 / ISO 15156) | ASSUMPTION: applicable based on sour gas service per DBM line 244 | location TBD |

## 4. Verification

| Requirement | Verification approach |
|---|---|
| R-089-03-01 | Document review of CWP construction-methods section; cross-check skid foundation drawings against the structural/foundations interface scope. |
| R-089-03-02 | Document review against the PACKAGE_REGISTER.csv interface-type list; checklist coverage audit. |
| R-089-03-03 | Workface plan review; verification that pipeline tie-in at the lease-boundary flange and the two inlet separators are sequenced and resource-loaded. |
| R-089-03-04 | Inspection of the interface and turnover checklist artifact for completeness against the interface-type list. |
| R-089-03-05 | Construction QC records: ESDV alignment, stroke test, and position-transmitter calibration; piggable-bore verification. |
| R-089-03-06 | Pressure-test packages, purge/inert records, and tie-in test reports for sweet-gas purge and HP flare vent lines. |
| R-089-03-07 | Cross-document audit between Datasheet (DEL-089-02), Scope of Work (DEL-089-01), and the CWP at IFC; resolution of the receiver-count/size conflict (see Guidance §Conflict Table). |
| R-089-03-08 | Hold/witness point records; pressure-test certificates; weld procedure qualification records (PQR/WPS); material test reports for sour-service compliance. |
| R-089-03-09 | Drainage and containment as-built; verification against grading/drainage interface drawings. |
| R-089-03-10 | Mechanical completion certificate; punchlist register; turnover certificate signed by EPC Integrator and Operations. |

## 5. Documentation

The Construction Work Package shall deliver:

- The **Construction Work Package** document — bound construction means/methods package with hold points, inspection plan, and acceptance criteria. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03]
- **Installation and tie-in workface plan** — workface-level execution plan addressing each applicable interface type. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03]
- **Construction interface and turnover checklist** — interface-by-interface acceptance and turnover artifact. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03]
- **Construction QC and turnover evidence** referenced by the verification matrix above (pressure-test records, weld records, ESDV stroke/position records, mechanical-completion and turnover certificates). [ASSUMPTION: standard EPC deliverable set; exact list — location TBD]
