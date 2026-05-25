# Specification: DEL-037-06 — EPC Vendor Package Review and Acceptance

## Scope

### Covers
- Structured EPC-Integrator-led review of all vendor package outputs for `PKG-037` (5kV SWITCHGEAR ELECTRICAL BUILDING 880-1), specifically the vendor production units `DEL-037-04` (Vendor Engineered Equipment Package) and `DEL-037-05` (Vendor Document Turnover Package).
- Acceptance of vendor package against EPC `DEL-037-01` SOW, `DEL-037-02` Package Datasheet, and `DEL-037-03` Construction Work Package.
- Generation of the four EPC acceptance artifacts: vendor document review log, package acceptance checklist, test/inspection evidence record, and turnover evidence record.
- Verification of facility-level interface readiness for each interface type listed in `PACKAGE_REGISTER.csv` row 39.

### Excludes
- Authorship of vendor engineering or vendor documentation (owned by Package Vendor under `DEL-037-04` / `DEL-037-05`).
- Authorship of the EPC SOW, Package Datasheet, or Construction Work Package (separate EPC deliverables `DEL-037-01`/`02`/`03`).
- Cross-package acceptance for any package other than `PKG-037`.

## Requirements

| ID | Requirement | Basis |
|---|---|---|
| R-1 | The deliverable SHALL produce a vendor document review log itemizing every vendor document submitted under `DEL-037-05`, with disposition (Accepted, Accepted-with-comment, Rejected, Pending) and reviewer identification. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 209 |
| R-2 | The deliverable SHALL produce a package acceptance checklist mapping each requirement from `DEL-037-01` SOW and `DEL-037-02` Package Datasheet to acceptance status against vendor evidence. | `DELIVERABLE_REGISTER.csv` row 209 |
| R-3 | The deliverable SHALL record test/inspection evidence demonstrating that vendor-furnished equipment under `DEL-037-04` meets the EPC Package Datasheet and SOW. | `_CONTEXT.md` Anticipated Artifacts |
| R-4 | The deliverable SHALL record turnover evidence (signed turnover packages, system handover records) covering vendor scope. | `_CONTEXT.md` Anticipated Artifacts |
| R-5 | The acceptance checklist SHALL include an interface-readiness row for each interface type stated for `PKG-037`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `PACKAGE_REGISTER.csv` row 39 |
| R-6 | Acceptance SHALL respect the package ownership split: vendor scope is reviewed for compliance, not re-authored by EPC. | `PACKAGE_REGISTER.csv` row 39 |
| R-7 | Acceptance evidence SHALL support each Supports Objective (`OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010`) via traceable entries (ASSUMPTION: package-grouping heuristic). | `_CONTEXT.md` Supports Objectives |
| R-8 | Where vendor evidence is insufficient or absent, the acceptance checklist row SHALL be marked `TBD` or `Pending`, not silently passed. | Authority hierarchy; epistemic controls |
| R-9 | Building-electrical features assessed during acceptance SHALL be checked for compatibility with applicable DBM provisions (e.g., n+1 HVAC, bottom-entry elevated/piled building, grounding to facility ground grid, TECK/ACWU/ACIC cable conventions) where the EPC SOW/Datasheet has invoked them. | DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings", "Grounding and Bonding", "Cable, Wire, and Raceways" |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Project Design Basis Memorandum (Deepcut) — Electrical Buildings section | Building configuration acceptance basis (HVAC redundancy, cable entry, elevated build). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Project Design Basis Memorandum (Deepcut) — Grounding and Bonding | Grounding acceptance basis for building/equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Project Design Basis Memorandum (Deepcut) — Cable, Wire, and Raceways | Cable type acceptance basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| 5 kV class equipment standards (e.g., IEEE/ANSI C37 series; CSA equivalents) | Vendor 5 kV switchgear acceptance basis. | ASSUMPTION: likely applicable; specific clauses location TBD (not present in accessible sources). |
| Canadian Electrical Code (CEC) requirements referenced by DBM | Grounding conductor sizing and related provisions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Grounding and Bonding" |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 | Inspect the vendor document review log; every `DEL-037-05` submittal has a row with disposition and reviewer. |
| R-2 | Trace each SOW/Datasheet requirement ID to an acceptance checklist row. |
| R-3 | Inspect test/inspection records for required factory acceptance tests, integration tests, and on-site checks. |
| R-4 | Inspect turnover record set for signed handover and any deficiency log. |
| R-5 | Confirm every listed interface type has an acceptance row. |
| R-6 | Review log shows no EPC-authored revisions to vendor documents; comments are tracked as vendor actions. |
| R-7 | Cross-reference acceptance entries against `OBJECTIVE_DELIVERABLE_MAP.csv`. |
| R-8 | Audit the checklist for any silently-cleared `TBD` items. |
| R-9 | Sample-audit the acceptance checklist against the DBM clauses listed in Standards. |

## Documentation

Required produced documents:
- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence record
- Turnover evidence record

Required input documents:
- `DEL-037-01` Scope of Work
- `DEL-037-02` Package Datasheet
- `DEL-037-03` Construction Work Package
- `DEL-037-04` Vendor Engineered Equipment Package outputs
- `DEL-037-05` Vendor Document Turnover Package outputs
