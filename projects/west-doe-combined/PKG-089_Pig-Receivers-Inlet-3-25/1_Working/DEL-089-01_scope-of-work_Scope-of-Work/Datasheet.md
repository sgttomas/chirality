# Datasheet — DEL-089-01 EPC Scope of Work, Pig Receivers (Inlet) 3-25

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-089-01_scope-of-work | _CONTEXT.md |
| Deliverable Name | Scope of Work | _CONTEXT.md |
| Parent Package ID | PKG-089 | _CONTEXT.md |
| Parent Workbook ID | 89 | _CONTEXT.md |
| Package Name | Pig Receivers (Inlet) 3-25 | _CONTEXT.md |
| Package Tag (preliminary) | 26020-02-35-001 / 26020-02-PT-35-001 | PACKAGE_REGISTER.csv (PKG-089) |
| Discipline | Mechanical | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Deliverable Type | EPC Scope of Work | _CONTEXT.md |
| Responsible Party | EPC Integrator | _CONTEXT.md; PACKAGE_REGISTER.csv responsibility model |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04, Facility Overview |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | _REFERENCES.md |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Plant inlet pipeline gas enters the facility through the pig receivers and proceeds to the inlet separators. | PACKAGE_REGISTER.csv PKG-089 scope |
| Service | Sour wellstream — Doe field inlet pipeline; three-phase (sour gas / raw condensate / produced water) | DBM 3-25 SEC-04 Inlet Pipeline Interface and Pigging, Inlet Separation |
| Receiver size (package row) | 610 mm (24") OD | PACKAGE_REGISTER.csv PKG-089 scope statement |
| Receiver count (package row) | 2 identical pig receivers on dedicated structural steel non-enclosed skids | PACKAGE_REGISTER.csv PKG-089 scope statement |
| Receiver count (DBM SEC-04) | A single combined three-phase pig receiver on structural steel non-enclosed skid | DBM 3-25 SEC-04 |
| Receiver size (DBM SEC-04) | TBD | DBM 3-25 SEC-04 |
| Purge / vent provisions | Sweet-gas purge and HP flare vent | DBM 3-25 SEC-04 |
| Inlet ESDV | Full-port, piggable, with position transmitters | DBM 3-25 SEC-04 |
| Inlet separator ESDV shutdown pressure | 635 psig | DBM 3-25 SEC-04 |
| Delivery-point ESDV shutdown pressure | TBC | DBM 3-25 SEC-04 |
| Plant inlet boundary | First aboveground flange within lease boundary | DBM 3-25 SEC-04 |
| Discipline package responsibility split | Package Vendor: package engineering, design, vendor documentation, physical equipment. EPC Integrator: facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | PACKAGE_REGISTER.csv PKG-089 responsibility model; OBJ-004 |
| Covers scope items | SOW-0157; SOW-0158; SOW-0159; SOW-0160 | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Supports objectives (package heuristic, ASSUMPTION) | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md; DELIVERABLE_REGISTER.csv; OBJECTIVE_REGISTER.csv |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Upstream condition | Doe field inlet pipeline gas — single inlet pipeline interface | DBM 3-25 SEC-04 |
| Downstream condition | Routed to two identical horizontal three-phase inlet separators (V-1600-2 and V-1700-2) | DBM 3-25 SEC-04 Inlet Separation |
| Per-separator gas flow basis | 40 MMSCFD | DBM 3-25 SEC-04 |
| Inlet design temperature | 8.3 deg C (downstream excerpts to be reconciled in detailed design) | DBM 3-25 SEC-04 |
| Slug basis | Frac flowback governs over pigging slug; separator slug handling approx 38 m3 | DBM 3-25 SEC-04 Slug and Flowback Basis |
| Sour service | Sour gas with H2S; CSA Z662 applies to pipeline-tie design | DBM 3-25 SEC-04, SEC-05; DBM 3-25 SEC-15 (ASSUMPTION) |

## Construction

| Item | Value | Source |
|---|---|---|
| Skid type | Structural steel, non-enclosed | DBM 3-25 SEC-04; PACKAGE_REGISTER.csv |
| Modularization | Vendor-supplied package on dedicated skid(s) | PACKAGE_REGISTER.csv PKG-089 |
| Applicable interface types | Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging | PACKAGE_REGISTER.csv PKG-089 applicable interface types |
| Inlet ESDV hardware | Full-port piggable valve with position transmitters | DBM 3-25 SEC-04 |
| Building / enclosure | Not enclosed (open structural steel skid) | DBM 3-25 SEC-04; PACKAGE_REGISTER.csv |

## References

- _CONTEXT.md (this deliverable)
- _REFERENCES.md (this deliverable)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv (row DEL-089-01)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv (row PKG-089)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv (OBJ-002..OBJ-010)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (SEC-04 Inlet Pipeline Interface and Pigging; Inlet Separation; SEC-05; SEC-15)
- 26020-Package_Requirements.docx package heading 42 — location TBD (binary source not accessible as text)
- 26020-02-PT-RFQ-35-001-Pig_Recv_1.docx — location TBD (binary source not accessible as text)
