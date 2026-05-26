# Specification — DEL-080-06 EPC Vendor Package Review and Acceptance

## Scope

This deliverable specifies the EPC Integrator's review and acceptance of the vendor-engineered Inlet Compressors package (PKG-080) and the evidence required for integration acceptance and handoff readiness. It covers SOW items SOW-0119 through SOW-0122 (`SCOPE_LEDGER.csv`).

**In scope:**
- Review of the vendor's package engineering, design, and documentation against the EPC Scope of Work (DEL-080-01), Package Datasheet (DEL-080-02), and Construction Work Package (DEL-080-03).
- Acceptance of the vendor-engineered equipment package (DEL-080-04) and the vendor document turnover package (DEL-080-05).
- Verification of interface conformance for the interface envelope declared for PKG-080 (`PACKAGE_REGISTER.csv`).
- Capture of test/inspection evidence and turnover evidence supporting facility handoff readiness.

**Out of scope (per OBJ-004 vendor/EPC split, `OBJECTIVE_REGISTER.csv`):**
- Package engineering, package design, vendor documentation authorship, and the physical equipment package itself — these are Package Vendor responsibilities and are reviewed (not authored) here.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| SPEC-080-06-R1 | The EPC Integrator shall review the vendor's package engineering and design against the EPC Scope of Work (DEL-080-01) and the Package Datasheet (DEL-080-02) and record dispositions for every reviewed item. | `_CONTEXT.md` Scope; OBJ-004 |
| SPEC-080-06-R2 | The EPC Integrator shall accept or reject the vendor-engineered equipment package (DEL-080-04) and the vendor document turnover package (DEL-080-05) based on documented review evidence. | `_CONTEXT.md` Anticipated Artifacts |
| SPEC-080-06-R3 | The EPC Integrator shall verify interface conformance for each interface type declared for PKG-080: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` PKG-080 |
| SPEC-080-06-R4 | The package acceptance checklist shall reflect the supplied scope: two (2) Ariel KBZ/6 separable reciprocating compressor packages with two-stage compression, intercooling and aftercooling, modular self-framing buildings, piping, instrumentation, electrical, HVAC, and package auxiliaries. | `SCOPE_LEDGER.csv` SOW-0121 |
| SPEC-080-06-R5 | Acceptance evidence shall confirm 2 x 50% configuration with no dedicated spare, sour-service (NACE-compliant) materials and seals, approximate suction ~1275 kPag, approximate discharge ~6550 kPag, and combined throughput approximately 80 MMSCFD (40 MMSCFD per unit). | `SCOPE_LEDGER.csv` SOW-0122 |
| SPEC-080-06-R6 | The EPC Integrator shall record test and inspection evidence (witness/hold points, ITR/ITP completion, NCR records and closeouts, FAT and SAT outcomes where applicable). | `_CONTEXT.md` Anticipated Artifacts; OBJ-010 |
| SPEC-080-06-R7 | The EPC Integrator shall record turnover evidence sufficient for facility handoff readiness, including controlled open-item closure (OBJ-010). | OBJ-010; `_CONTEXT.md` Anticipated Artifacts |
| SPEC-080-06-R8 | Commercial/stream-boundary expectations (sales/sour gas stream disposition, metering accountability, tie-in limits) per OBJ-003 shall be confirmed during acceptance review. ASSUMPTION: applies via OBJ-003 association in `OBJECTIVE_DELIVERABLE_MAP.csv`. | OBJ-003 |
| SPEC-080-06-R9 | Safety/regulatory expectations (sour-service, fire and gas, relief/flare/vent, drain/containment, emissions, codes/standards) per OBJ-009 shall be confirmed during acceptance review. | OBJ-009 |
| SPEC-080-06-R10 | Electrical, controls/instrumentation, utilities, and civil/structural integration expectations (OBJ-005, OBJ-006, OBJ-007, OBJ-008) shall be confirmed via the corresponding interface verifications under SPEC-080-06-R3. | OBJ-005, OBJ-006, OBJ-007, OBJ-008 |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| NACE materials and seal requirements for sour service | Acceptance must confirm sour-service compliance for the inlet compressor package | Cited at SOW-0122; specific NACE document/clauses TBD (no local source slice copied) |
| Project Design Basis Memoranda: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Governs facility/package design basis for the 03-25 (compressors/liquids) facility | Cited via `PACKAGE_REGISTER.csv` PKG-080; local slice not copied — location TBD |
| `26020-Package_Requirements.docx` package heading 33 (Inlet Compressors) | Vendor-document and package requirements basis | location TBD (not copied locally) |
| Other applicable codes and standards per OBJ-009 | Sour-service, environmental, regulatory, safety codes | Specific clauses TBD (no local source slice copied) |

## Verification

| Requirement | Verification Approach |
|---|---|
| SPEC-080-06-R1 | Inspection — completed vendor document review log with disposition per reviewed item against DEL-080-01 and DEL-080-02 |
| SPEC-080-06-R2 | Inspection — signed package acceptance checklist referencing DEL-080-04 and DEL-080-05 |
| SPEC-080-06-R3 | Inspection — interface verification matrix covering all declared interface types from `PACKAGE_REGISTER.csv` |
| SPEC-080-06-R4 | Inspection — checklist line items mapped to the equipment list in SOW-0121 |
| SPEC-080-06-R5 | Inspection of design/operating data; review of process datasheets, vendor mechanical data, and materials/seal selection records (location TBD) |
| SPEC-080-06-R6 | Inspection — ITR/ITP records, NCR register and closures, FAT and SAT records (as applicable) |
| SPEC-080-06-R7 | Inspection — mechanical-completion records, turnover packages, and open-item closure evidence |
| SPEC-080-06-R8 | Review — confirmation against OBJ-003 commercial/stream-boundary basis (DBM reference; local slice TBD) |
| SPEC-080-06-R9 | Review — confirmation against safety/regulatory basis (DBM/codes; local slice TBD) |
| SPEC-080-06-R10 | Review — confirmation that interface verifications under R3 close out OBJ-005..008 expectations |

## Documentation

Anticipated production artifacts for this deliverable (per `_CONTEXT.md`):
- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence (witness records, ITRs/ITPs, NCRs, FAT/SAT records)
- Turnover evidence (mechanical completion, open-item closure)

Upstream deliverables consulted (peer deliverables within PKG-080):
- DEL-080-01 Scope of Work
- DEL-080-02 Package Datasheet
- DEL-080-03 Construction Work Package
- DEL-080-04 Vendor Engineered Equipment Package
- DEL-080-05 Vendor Document Turnover Package
