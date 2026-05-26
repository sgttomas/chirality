# Specification — DEL-089-01 EPC Scope of Work, Pig Receivers (Inlet) 3-25

## Scope

### In scope

This Scope of Work defines the EPC Integrator's scope for procuring, integrating, and accepting the Pig Receivers (Inlet) package PKG-089 (tag 26020-02-PT-35-001) at the 03-25 West Doe Compressor Station and Liquids Hub. It establishes:

- Package identity, tag, and facility integration boundaries (see Datasheet).
- The EPC / Package Vendor responsibility split for engineering, design, vendor documentation, equipment supply, and facility integration. SOURCE: PACKAGE_REGISTER.csv (PKG-089 responsibility model); OBJ-004 (vendor/EPC split).
- Interfaces the package must satisfy across the facility, listed in Section "Applicable Interfaces" below.
- The scope items SOW-0157, SOW-0158, SOW-0159, SOW-0160 attached to this deliverable. SOURCE: _CONTEXT.md; DELIVERABLE_REGISTER.csv.

### Out of scope

- Vendor package engineering, package design, vendor documentation, and physical equipment supply — owned by the Package Vendor, not the EPC Integrator. SOURCE: PACKAGE_REGISTER.csv PKG-089; OBJ-004.
- Offsite Doe field inlet pipeline design and installation. The plant inlet boundary is the first aboveground flange within the lease boundary. SOURCE: DBM 3-25 SEC-04.
- LACT custody-transfer equipment and downstream NRM NEBC connector scope. SOURCE: DBM 3-25 Facility Overview, Commercial and Facility Interfaces.
- Package-specific exclusions beyond those above: TBD (PACKAGE_REGISTER.csv PKG-089 exclusions field marked TBD).

## Requirements

### R-1 Package identity and tag
The deliverable shall reference the package as PKG-089, tag 26020-02-PT-35-001 (Workbook row 77, WBS 02, Mechanical). SOURCE: PACKAGE_REGISTER.csv PKG-089.

### R-2 Function
The EPC Scope of Work shall state the package process function: plant inlet pipeline gas enters the facility through the pig receivers installed and proceeds to the inlet separators. SOURCE: PACKAGE_REGISTER.csv PKG-089 scope.

### R-3 Equipment configuration
The EPC Scope of Work shall record the equipment configuration of the package, including count, nominal size, skid type, ESDV configuration, and purge/vent provisions. The current authoritative entries are:
- Count and size per PACKAGE_REGISTER.csv PKG-089: "2 identical 610 mm (24") OD pig receivers on dedicated structural steel non-enclosed skids".
- Configuration per DBM 3-25 SEC-04: "single combined three-phase pig receiver" on a structural steel non-enclosed skid; receiver size TBD.
- Inlet ESDV: full-port, piggable, with position transmitters (DBM SEC-04).
- Purge/vent: sweet-gas purge and HP flare vent (DBM SEC-04).
This requirement is satisfied by reproducing both source statements and flagging the count/size discrepancy as Conflict C-001 for human ruling (see Guidance.md). SOURCE: PACKAGE_REGISTER.csv PKG-089; DBM 3-25 SEC-04.

### R-4 Facility integration boundary
The EPC Scope of Work shall identify the plant inlet boundary as the first aboveground flange within the lease boundary, where the Doe field pipeline contractor transfers scope to the facility fabricator or construction contractor. Final inlet pipeline configuration is confirmed during detailed design. SOURCE: DBM 3-25 SEC-04.

### R-5 Downstream interface
The EPC Scope of Work shall identify the immediate downstream destination as the two identical horizontal three-phase inlet separator packages V-1600-2 and V-1700-2. SOURCE: DBM 3-25 SEC-04 Inlet Separation.

### R-6 Shutdown pressures
The EPC Scope of Work shall carry the inlet separator ESDV shutdown pressure of 635 psig and shall flag the delivery-point ESDV shutdown pressure as TBC. SOURCE: DBM 3-25 SEC-04.

### R-7 Responsibility split
The EPC Scope of Work shall state explicitly that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package, and that the EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and integration review/acceptance. SOURCE: PACKAGE_REGISTER.csv PKG-089 responsibility model; OBJ-004.

### R-8 Applicable interface types
The EPC Scope of Work shall enumerate the applicable interface types this package presents to the facility: Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging. SOURCE: PACKAGE_REGISTER.csv PKG-089 applicable interface types.

### R-9 Sour service and codes
The EPC Scope of Work shall acknowledge sour service and the applicability of CSA Z662 for the pipeline / pig receiver / inlet ESDV tie-in scope. Detailed code applicability list: ASSUMPTION; full standards table TBD until Word source basis is accessible. SOURCE: DBM 3-25 SEC-04 (sour service); DBM 3-25 SEC-15 (Regulatory, Codes and Standards basis, ASSUMPTION).

### R-10 Scope items coverage
The EPC Scope of Work shall demonstrate coverage of scope items SOW-0157, SOW-0158, SOW-0159, SOW-0160. Mapping of each SOW item to specific subsections is TBD pending readable source for the workbook scope ledger row content. SOURCE: _CONTEXT.md; DELIVERABLE_REGISTER.csv.

### R-11 Objectives supported
The EPC Scope of Work shall make explicit how it supports the package-grouped objectives OBJ-002 through OBJ-010 to the extent applicable to this package. Linkage is ASSUMPTION (PACKAGE_HEURISTIC). SOURCE: DELIVERABLE_REGISTER.csv; OBJECTIVE_REGISTER.csv.

### R-12 Conflicts and TBDs
The EPC Scope of Work shall not silently reconcile contradictions between source materials. Any unresolved value shall remain TBD and any source contradiction shall appear in the Conflict Table in Guidance.md. SOURCE: skill four-documents Step 5; K-PROV-1.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| CSA Z662 | Pipeline / pig receiver / inlet ESDV tie-in design | DBM 3-25 SEC-04; DBM 3-25 SEC-15 (ASSUMPTION on detailed citation; location TBD until Word source basis readable) |
| 26020 Package Requirements (package heading 42) | Package vendor documentation, package basis | _REFERENCES.md; PACKAGE_REGISTER.csv source-basis column; location TBD (binary source) |
| 26020-02-PT-RFQ-35-001-Pig_Recv_1.docx | Procurement basis | PACKAGE_REGISTER.csv PKG-089 word source basis; location TBD (binary source) |

Additional standards (ANSI/ASME piping, pressure vessel code, sour-service materials standards): TBD pending accessible Word source basis. ASSUMPTION: standard mechanical/process piping codes apply because the package is mechanical sour-service equipment, but specific clauses are not derived here.

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 Identity/tag | EPC review confirms PACKAGE_REGISTER row matches deliverable artifact identity. |
| R-2 Function | Cross-check function statement against PACKAGE_REGISTER scope statement and DBM SEC-04. |
| R-3 Equipment configuration | Review against Datasheet rows; resolve Conflict C-001 (count/size) before procurement issue. |
| R-4 Boundary | Verify plant inlet boundary description matches DBM SEC-04. |
| R-5 Downstream interface | Verify against DBM SEC-04 Inlet Separation. |
| R-6 Shutdown pressures | Verify against DBM SEC-04; confirm delivery-point ESDV pressure resolves at detailed design. |
| R-7 Responsibility split | Cross-check OBJ-004 wording and PACKAGE_REGISTER responsibility column. |
| R-8 Interface types | Verify against PACKAGE_REGISTER applicable interface types column. |
| R-9 Sour service / codes | Detailed standards table verification: TBD. |
| R-10 SOW item coverage | Map each SOW item identifier explicitly; verification of mapping: TBD. |
| R-11 Objective support | EPC review of OBJ-002..OBJ-010 linkage; package heuristic only. |
| R-12 Conflicts/TBDs | Audit the document set for any non-cited claim. |

## Documentation

Anticipated artifacts (from _CONTEXT.md):

- Package scope of work narrative
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Companion EPC deliverables for this package (from DELIVERABLE_REGISTER.csv): DEL-089-02 Package Datasheet; DEL-089-03 Construction Work Package; DEL-089-06 EPC Vendor Package Review and Acceptance. Vendor companion deliverables: DEL-089-04 Vendor Engineered Equipment Package; DEL-089-05 Vendor Document Turnover Package. SOURCE: DELIVERABLE_REGISTER.csv rows DEL-089-02 through DEL-089-06.
