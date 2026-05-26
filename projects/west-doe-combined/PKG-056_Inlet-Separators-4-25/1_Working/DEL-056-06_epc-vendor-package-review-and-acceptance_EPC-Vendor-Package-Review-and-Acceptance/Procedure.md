# Procedure: EPC Vendor Package Review and Acceptance

## Purpose

Define the working procedure to produce and check the DEL-056-06 EPC Vendor Package Review and Acceptance evidence set for PKG-056 Inlet Separators 4-25 using accepted Gate 7 truth and accessible Deepcut DBM source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv.
- Mechanical/process source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Inlet Separator narrative and Inlet Separator Design Parameters).
- Advisory upstream evidence from DEL-056-01 (Scope of Work), DEL-056-02 (Package Datasheet), DEL-056-03 (Construction Work Package), DEL-056-04 (Vendor Engineered Equipment Package), and DEL-056-05 (Vendor Document Turnover Package). These are not yet declared as upstream in `_DEPENDENCIES.md` — see HRR-056-06-005.
- Declared dependencies review: no declared upstream or downstream dependencies are currently listed in `_DEPENDENCIES.md`.
- Open external inputs tracked as TBD until accepted: detailed vendor package requirements text from 26020-Package_Requirements.docx heading 11 (location TBD; not locally accessible).

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and DELIVERABLE_REGISTER.csv for DEL-056-06.
2. Confirm package identity against PACKAGE_REGISTER.csv for PKG-056 (Mechanical, WBS 01, CoA 26020-01-17-004).
3. Compile the eleven applicable interface facts from INTERFACE_REGISTER.csv:
   - Process Piping (IFC-C5833B2729), Utility Piping (IFC-2E1ABE7C99), Relief / Flare / Vent (IFC-A1023EBFAC), Drain / Containment (IFC-DE1036D554), EHT (IFC-53DF92868E), Grounding / Bonding (IFC-70423EFFC2), Area / Exterior Lighting (IFC-54942AAFDA), I&C / Control Cabling (IFC-C8EFDB103A), Fire & Gas / Safety Systems (IFC-666C085B26), Maintenance Access (IFC-9626472DCC), Structural / Foundations / Supports (IFC-F7D66A2D0B).
4. Establish the mechanical/process review basis from the Deepcut DBM Inlet Separator section: quantity carry, design pressure, gas design rate range, slug capacity candidates, internal coating, internals, inlet PCV configuration, maintenance isolation, liquid outlet heater treatment, inlet piping distribution, methanol injection, and spacing.
5. Collect vendor submittals via DEL-056-05 (Vendor Document Turnover Package) and prior interface evidence via DEL-056-02 (Package Datasheet) and DEL-056-03 (Construction Work Package).
6. Produce the vendor document review and comment log (ART-C28CAEBE71):
   - one row per vendor submittal,
   - traceback to EPC Scope of Work, Package Datasheet, and Construction Work Package,
   - source-grounded review comments only,
   - flagged items where acceptance criteria would depend on inaccessible source text (mark TBD).
7. Produce the vendor package acceptance and turnover checklist (ART-DBC56EA416):
   - one row per applicable interface (eleven items),
   - one row per Specification requirement REQ-056-06-001..020,
   - accept/reject status per row with evidence pointer,
   - explicit handoff readiness gate per interface.
8. Capture factory/shop test and inspection evidence (ART-95970470BB) covering supplied separators; record deviations and either resolve or carry as open.
9. Maintain an open-conflict log capturing HRR-056-06-001..005 (quantity, capacity, slug capacity, inaccessible docx slice, undeclared upstreams). Do not silently close any.
10. Maintain an open-input log identifying the inaccessible 26020-Package_Requirements.docx heading 11 slice and any other deferred references.
11. Cross-check Datasheet, Specification, Guidance, and Procedure for consistent identifiers, interface labels, source citations, and TBD treatment.
12. Prepare the acceptance evidence set for review by the EPC Integrator; coordinate package vendor inputs where vendor authority is required (engineering, design, documentation).

## Verification

| Check | Method |
|---|---|
| Identity verification | Compare deliverable and package tables to `_CONTEXT.md`, DELIVERABLE_REGISTER.csv, and PACKAGE_REGISTER.csv. |
| Interface verification | Confirm all eleven PKG-056 applicable interface types are included and cited to INTERFACE_REGISTER.csv. |
| Source grounding | Confirm each non-trivial review item cites Gate 7 registers or Deepcut DBM source slices; items depending solely on the inaccessible docx slice are marked TBD. |
| Quantity/capacity conflict carry | Confirm HRR-056-06-001..003 are present in the open-conflict log and not silently closed. |
| Open input verification | Confirm the inaccessible docx slice is listed as a deferred input and any acceptance criteria depending on it are TBD. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use consistent names, interface labels, and source basis. |
| Dependency check | Confirm blockers are not inferred from undeclared relationships; HRR-056-06-005 carries the proposed upstream declaration. |
| Status update | Confirm `_STATUS.md` is updated only per safe-update rule (OPEN -> INITIALIZED). |

## Records

- Vendor document review and comment log (ART-C28CAEBE71).
- Vendor package acceptance and turnover checklist (ART-DBC56EA416).
- Factory/shop test and inspection evidence (ART-95970470BB).
- Interface matrix covering the eleven PKG-056 interface types.
- Open-conflict log for HRR-056-06-001..005.
- Source-input log for the inaccessible 26020-Package_Requirements.docx heading 11 slice.
- Cross-document consistency check record.
- Status update record in `_STATUS.md`.
