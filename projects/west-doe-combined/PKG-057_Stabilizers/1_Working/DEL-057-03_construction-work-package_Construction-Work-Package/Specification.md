# Specification — DEL-057-03 Construction Work Package (PKG-057 Stabilizers)

## Scope

This deliverable is the EPC Integrator's normative Construction Work Package (CWP) for the three (3) Inlet Stabilizer Packages in PKG-057. It defines how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. It governs only the EPC-integration construction scope; vendor package engineering, design, fabrication, and vendor documentation are covered by `DEL-057-04` and `DEL-057-05`.

**In scope (EPC-integration construction):**
- Site receipt, set, and erection of three vendor-supplied stabilizer skids.
- Foundations and structural supports for the skids and associated EPC-scope equipment.
- Skid-edge interconnect piping (process, utility, relief/flare/vent, drain/containment).
- Plant MCC electrical power supply to the package; EHT, grounding/bonding, area lighting, and I&C/control cabling tie-ins.
- DCS integration of vendor package controls into the facility control system.
- Construction interface management and turnover record assembly across the applicable interface families.

**Out of scope (Package Vendor or other deliverables):**
- Package engineering, package design, vendor documentation, and physical equipment supply — see `DEL-057-04`, `DEL-057-05`.
- Operational/process control of the stabilizers post-handover — defined by facility operations procedures (not produced here).

## Requirements

| ID | Requirement | Source / Authority |
|---|---|---|
| REQ-CWP-01 | Construction work package SHALL cover installation, tie-in, inspection, turnover, and facility integration of the package, per the decomposition deliverable description. | `DELIVERABLE_REGISTER.csv` row `DEL-057-03` |
| REQ-CWP-02 | Three (3) Inlet Stabilizer Packages SHALL be installed in a 3 x 40% configuration. | `SOW-0179` |
| REQ-CWP-03 | The EPC Integrator SHALL provide installation/erection, foundations, skid-edge interconnect piping, electrical power supply from the plant MCC, and DCS integration ("By Others" to the Package Vendor). | `SOW-0180`; `PACKAGE_REGISTER.csv` row 82 responsibility split |
| REQ-CWP-04 | The construction work package SHALL plan and document tie-ins for every applicable interface family identified for PKG-057: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. | `PACKAGE_REGISTER.csv` row 82 (Applicable interface types) |
| REQ-CWP-05 | The package SHALL produce an installation and tie-in workface plan as an anticipated artifact. | `_CONTEXT.md` Anticipated Artifacts |
| REQ-CWP-06 | The package SHALL produce a construction interface and turnover checklist as an anticipated artifact, sized to the interface families in REQ-CWP-04. | `_CONTEXT.md` Anticipated Artifacts |
| REQ-CWP-07 | Tie-ins to the stabilizer column SHALL respect the source-stated minimum operating pressure of 793 kPag and the design pressures of upstream/downstream equipment (1724 kPag flash feed separator design inlet). | `SOW-0180` |
| REQ-CWP-08 | The construction scope SHALL preserve maintenance access for stabilizer column trays (20 floating valve trays), feed pumps, product cooler fan, LIT, TIT, and the feed/bottoms exchanger. | `SOW-0179`; OBJ-010 maintenance-access intent |
| REQ-CWP-09 | Sour-service safety, relief, flare, drain/containment, fire/gas, and shutdown integration SHALL be carried into tie-in design and turnover evidence. ASSUMPTION: stabilizer service is sour-service per the 04-25 Deepcut DBM scope (OBJ-001, OBJ-009); confirm from DBM SEC-09/SEC-14 source slice. | OBJ-009; OBJ-001 (ASSUMPTION — DBM slice TBD) |
| REQ-CWP-10 | Vendor/EPC responsibility separation SHALL be preserved throughout construction execution: package engineering/design/equipment/documentation remain Package Vendor; integration, interfaces, constructability, and facility-level integration remain EPC Integrator. | OBJ-004; `PACKAGE_REGISTER.csv` row 82 |
| REQ-CWP-11 | Electrical integration (MCC supply, EHT, grounding/bonding, lighting, cathodic protection at package boundary) SHALL be planned and inspected as part of the CWP. | OBJ-005; `PACKAGE_REGISTER.csv` row 82 interface list |
| REQ-CWP-12 | Controls and instrumentation integration (I&C cabling, communications, fire & gas, shutdown interfaces, package control input to DCS) SHALL be planned, terminated, loop-checked, and recorded. | OBJ-006; `PACKAGE_REGISTER.csv` row 82 interface list |
| REQ-CWP-13 | Shared utility tie-ins (fuel gas, instrument air, drains, flare/blowdown/vent, heat medium, HVAC/building services as applicable) SHALL be identified and executed. | OBJ-007; `PACKAGE_REGISTER.csv` row 82 interface list |
| REQ-CWP-14 | Civil/structural scope (foundations, grading, containment, access, pipe rack, platform, construction-support) SHALL be coordinated with the package layout and skid edge. | OBJ-008; `PACKAGE_REGISTER.csv` row 82 interface list |
| REQ-CWP-15 | Commissioning, turnover, and controlled open-item closure evidence SHALL be assembled for handoff under `DEL-057-06`. | OBJ-010; `DELIVERABLE_REGISTER.csv` row `DEL-057-06` |
| REQ-CWP-16 | Specific values for civil loadings, structural support, lift weights, lift plans, lay-down, hydrotest, and PWHT SHALL be sourced from the Package Vendor design basis (TBD — vendor input not yet in scope of this deliverable). | TBD; vendor input from `DEL-057-04` |

## Standards

| Item | Status |
|---|---|
| Sour-service, regulatory, codes, and standards basis | location TBD — DBM SEC-15 referenced by OBJ-009 but source slice not extracted locally |
| Electrical codes and grounding/bonding standards | location TBD — DBM SEC-12 referenced by OBJ-005 |
| Controls/I&C/fire & gas standards | location TBD — DBM SEC-13/SEC-14 referenced by OBJ-006 |
| Constructability / construction-support standards | location TBD — DBM SEC-11 referenced by OBJ-008 |

ASSUMPTION: applicable governing standards will be carried into the CWP from the deliverable's source-grounded DBM slices once those slices are extracted to `_REFERENCES.md` for this deliverable.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-CWP-01..06 | Review of CWP narrative and artifacts against the decomposition row; presence of installation/tie-in workface plan and turnover checklist artifacts |
| REQ-CWP-02 | Inspection: three skids installed and tied in; configuration matches 3 x 40% |
| REQ-CWP-03 | Responsibility matrix review; By-Others scope items present in EPC scope, not vendor scope |
| REQ-CWP-04 | Interface checklist coverage review against the PKG-057 applicable interface list |
| REQ-CWP-07 | Pressure tie-in design review; hydro/pneumatic testing per applicable code (code TBD); turnover dossier includes test packages |
| REQ-CWP-08 | Maintenance access walkdown against vendor maintenance-access requirements |
| REQ-CWP-09 | Sour-service tie-in review; relief/flare and shutdown loop tests; closure of safety open items |
| REQ-CWP-10 | Audit of construction RFIs and change records against vendor/EPC split |
| REQ-CWP-11 | Electrical termination tests; grounding/bonding measurements; EHT commissioning records |
| REQ-CWP-12 | I&C loop checks; DCS point-to-point verification; fire & gas cause-and-effect tests |
| REQ-CWP-13 | Utility tie-in flush/clean records and operational checks |
| REQ-CWP-14 | Foundation as-builts and structural inspection records |
| REQ-CWP-15 | Open-item closure log delivered to `DEL-057-06` |
| REQ-CWP-16 | Vendor-supplied design basis received before construction scope is frozen |

## Documentation

Required artifacts produced by this deliverable:

- Construction work package narrative (this deliverable's primary artifact).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Required input documents (consumed):

- `DEL-057-01` Scope of Work.
- `DEL-057-02` Package Datasheet.
- Vendor package design basis from `DEL-057-04` (when available).

Required output documents (produced for downstream):

- Turnover record set consumed by `DEL-057-06` EPC Vendor Package Review and Acceptance.
