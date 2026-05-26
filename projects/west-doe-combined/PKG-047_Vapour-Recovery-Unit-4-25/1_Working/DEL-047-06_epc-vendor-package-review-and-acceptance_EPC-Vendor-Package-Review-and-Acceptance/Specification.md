# Specification — DEL-047-06 EPC Vendor Package Review and Acceptance

## Scope

### In Scope

- EPC Integrator review of all Package Vendor submittals for `PKG-047 Vapour Recovery Unit 4-25` against the EPC Scope of Work (DEL-047-01), Package Datasheet (DEL-047-02), and Construction Work Package (DEL-047-03).
- Integration acceptance of the vendor-engineered equipment package (DEL-047-04) at the facility-level boundaries: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. (Source: PACKAGE_REGISTER.csv row PKG-047 InterfaceTypes.)
- Handoff readiness review of the Vendor Document Turnover Package (DEL-047-05).
- Production of a vendor document review log, package acceptance checklist, test/inspection evidence index, and turnover evidence index.

### Out of Scope

- Vendor-side package engineering, package design, and vendor documentation production (owned by DEL-047-04 / DEL-047-05). Source: PACKAGE_REGISTER.csv row PKG-047 (Package Vendor vs. EPC Integrator split).
- Authoring the EPC Scope of Work, Package Datasheet, or Construction Work Package (those are DEL-047-01/-02/-03 outputs).
- Operations and maintenance after turnover.
- Package-specific exclusions: `TBD; no package-specific exclusions stated in source materials` (PACKAGE_REGISTER.csv row PKG-047 Exclusions).

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| R-01 | The EPC Integrator SHALL review every Package Vendor submittal listed in the Vendor Document Turnover Package (DEL-047-05) against DEL-047-01, DEL-047-02, and DEL-047-03, and record disposition (Accept / Accept with comment / Reject) in the vendor document review log. | DELIVERABLE_REGISTER.csv row DEL-047-06 (artifacts include "Vendor document review log") | Vendor document review log exists with 1:1 entries to DEL-047-05 register. |
| R-02 | The package acceptance checklist SHALL cover the SOW items in scope: SOW-0253, SOW-0254, SOW-0255, SOW-0256. | `_CONTEXT.md` Covers Scope Items | Checklist traces each SOW ID to one or more checklist rows. |
| R-03 | Integration acceptance SHALL cover all applicable interface types listed for PKG-047. | PACKAGE_REGISTER.csv row PKG-047 InterfaceTypes | Acceptance checklist contains an entry for each interface type. |
| R-04 | Test/inspection evidence (FAT, SAT, NDE, hydrotest as applicable) for both 100% capacity VRU trains (lead-lag) SHALL be received from the Package Vendor and verified before integration acceptance. | PACKAGE_REGISTER.csv row PKG-047 (two trains, lead-lag); ASSUMPTION on specific test set — required test list TBD against `26020-Package_Requirements.docx` heading 2 (source slice not yet local) | Test/inspection evidence index lists per-train records with vendor reference numbers. |
| R-05 | Sour-service qualification of compressor and ancillary metallurgy SHALL be confirmed from vendor documentation. | PACKAGE_REGISTER.csv row PKG-047 ("sour service") | Acceptance checklist row records vendor sour-service certification reference; otherwise `TBD`. |
| R-06 | Turnover evidence SHALL include mechanical completion, punch-list status, and turnover certification covering both trains and the shared building. | `_CONTEXT.md` Anticipated Artifacts; PACKAGE_REGISTER.csv row PKG-047 (both housed in one building) | Turnover evidence index references per-train and building-level certificates. |
| R-07 | Acceptance decisions SHALL be authored by humans; agents may prepare review records but SHALL NOT sign acceptance. | Project governance (K-AUTH-1) — ASSUMPTION applied as governance default; not from package source | Acceptance checklist signatures are human; agent contributions tagged. |

## Standards

| Standard / Reference | Applicability | Status |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 2 | Governing package requirements for PKG-047 | Location TBD — referenced but not sliced into deliverable folder |
| `26020-01-PT-RFQ-12-002_VRU_2_R0.docx` (Bid Docs/_Budgetary) | Word source basis for PKG-047 | Location TBD — referenced by PACKAGE_REGISTER.csv |
| `DBM-Deepcut/4-25_Deepcut_DBM.md` | Design Basis Memorandum for 4-25 Deepcut (parent process context) | Location TBD — referenced by PACKAGE_REGISTER.csv |
| Sour-service material standards (e.g., NACE MR0175 / ISO 15156) | Compressor and wetted-part metallurgy | ASSUMPTION — common practice for sour service; not yet confirmed against accessible source slice |
| EPC contractor QA/QC and acceptance procedure | Acceptance governance | TBD — not enumerated in accessible decomposition sources |

## Verification

Verification approaches are mapped per requirement above. The aggregate verification artifact is the package acceptance checklist (R-01..R-07) supported by:

- the vendor document review log (R-01),
- the test/inspection evidence index (R-04, R-05),
- the turnover evidence index (R-06).

Each checklist row SHALL cite the underlying vendor document or evidence record.

## Documentation

Required artifacts from `_CONTEXT.md` / DELIVERABLE_REGISTER.csv:

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence (index + records)
- Turnover evidence (index + certificates)
