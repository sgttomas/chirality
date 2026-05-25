# Specification — DEL-017-06 EPC Vendor Package Review and Acceptance

## Scope

### Includes

- EPC Integrator review of the Package Vendor's engineering, design, fabrication/supply, and equipment package for `PKG-017` (MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD).
- EPC Integrator review of the Vendor Document Turnover Package (DEL-017-05), including the vendor document register and submittals.
- Integration-acceptance evaluation of the vendor package against the EPC Scope of Work (DEL-017-01), Package Datasheet (DEL-017-02), and Construction Work Package (DEL-017-03).
- Handoff-readiness determination across the declared interface surface for PKG-017: Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports.
- Capture of test/inspection and turnover evidence sufficient to support EPC Integrator acceptance.

Source: `_CONTEXT.md` Scope; Gate 7 `DELIVERABLE_REGISTER.csv` DEL-017-06; Gate 7 `PACKAGE_REGISTER.csv` PKG-017.

### Excludes

- Re-performance of Package Vendor engineering, design, or detailed electrical studies (e.g., harmonic/reactive-power studies referenced in 3-25 DBM SCA-001 VE #37) — these remain Package Vendor or detailed-design scope. (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.)
- Authoring of binding approval or certification of fitness for reliance. EPC Integrator acceptance records vendor-package conformance; binding sign-off is a human approval action outside this deliverable's scope.
- Whole-facility integration deliverables beyond the PKG-017 boundary.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-017-06-01 | The acceptance record SHALL be assembled by the EPC Integrator (lead) with Package Vendor input. | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-017-06 ResponsibleParty |
| R-017-06-02 | The acceptance record SHALL evaluate the vendor package against accepted versions of DEL-017-01, DEL-017-02, and DEL-017-03. | `_CONTEXT.md` Scope |
| R-017-06-03 | The vendor document review log SHALL list each vendor document considered, its revision, the EPC reviewer, review code, comments, and disposition. | ASSUMPTION (industry convention); detailed format `TBD` until DEL-017-05 vendor document register is accepted |
| R-017-06-04 | The package acceptance checklist SHALL provide traceability from each accepted SOW/Datasheet/CWP clause to the corresponding vendor evidence. | ASSUMPTION (industry convention) |
| R-017-06-05 | Test/inspection evidence SHALL cover the vendor package's FAT and any specified site acceptance and hold-point inspections. | ASSUMPTION; specific test set `TBD` until DEL-017-02 Verification section is accepted |
| R-017-06-06 | Turnover evidence SHALL document mechanical completion, energization readiness, and the care-custody-control transfer for PKG-017. | ASSUMPTION (industry convention); specific turnover scope `TBD` until DEL-017-03 turnover checklist is accepted |
| R-017-06-07 | The acceptance record SHALL address each interface listed for PKG-017 (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-017 (InterfaceTypes) |
| R-017-06-08 | Open items, NCRs, and outstanding vendor commitments SHALL be tracked to closure or carried as explicit holds at handoff. | ASSUMPTION (industry convention) |
| R-017-06-09 | The acceptance record SHALL preserve traceability to Workbook Packages row 19 / `26020-02-30-008` package identity. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-017 |
| R-017-06-10 | Acceptance content SHALL support the objectives associated with `SOW-0018` / `PKG-017` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010). | `_CONTEXT.md`; Gate 7 `OBJECTIVE_SCOPE_MAP.csv` |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project Decomposition Contract (Gate 7 snapshot) | Authoritative basis for PKG-017 identity, scope, interfaces, and objectives | `_REFERENCES.md` (Gate 7 path) |
| 3-25 DBM (Comp & Liquids) | Discipline-of-record context for the 03-25 facility electrical scope referenced by PKG-017 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Equipment / IEEE / NEMA standards governing MV VFDs | Likely applicable to the equipment under review | ASSUMPTION; location `TBD` (no clause text locally accessible) |
| SCA-001 VEs (e.g., #34 starting VFDs, #37 capacitor banks on MCC-8200) | May govern the technical basis vendor evidence must address | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |

## Verification

| Req | Verification Method | Evidence |
|---|---|---|
| R-017-06-01 | Review of acceptance record authorship and EPC Integrator sign-off block | Acceptance checklist header |
| R-017-06-02 | Cross-check between acceptance checklist clauses and DEL-017-01/02/03 accepted snapshots | Acceptance checklist; snapshot pointers |
| R-017-06-03 | Inspection of vendor document review log | Vendor document review log |
| R-017-06-04 | Trace audit of checklist-to-evidence links | Acceptance checklist |
| R-017-06-05 | Inspection of FAT reports and any site test records | Test/inspection evidence pack |
| R-017-06-06 | Inspection of turnover packet (MC, energization, CCC transfer) | Turnover evidence pack |
| R-017-06-07 | Interface-by-interface coverage check against PKG-017 InterfaceTypes | Acceptance checklist interface section |
| R-017-06-08 | Open-item / NCR register review | Open-item log |
| R-017-06-09 | Header/identity check against Gate 7 PACKAGE_REGISTER | Acceptance record header |
| R-017-06-10 | Objective traceability check using Gate 7 OBJECTIVE_SCOPE_MAP | Acceptance checklist objective trace section |

## Documentation

Required output artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence pack
- Turnover evidence pack

Records SHALL cite the accepted upstream snapshot identifier (Gate 7 Final Published 2026-05-24) and the accepted revisions of DEL-017-01, DEL-017-02, DEL-017-03, DEL-017-04, and DEL-017-05.
