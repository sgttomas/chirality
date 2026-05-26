# Procedure — DEL-047-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational steps the EPC Integrator follows to review the Package Vendor's PKG-047 (Vapour Recovery Unit 4-25) submittals, accept package integration into the facility, and assemble the turnover evidence required by this deliverable.

## Prerequisites

- DEL-047-01 (EPC Scope of Work) at or above maturity `INITIALIZED`. (Default maturity threshold from `_DEPENDENCIES.md`.)
- DEL-047-02 (Package Datasheet) at or above maturity `INITIALIZED`.
- DEL-047-03 (Construction Work Package) available for tie-in and turnover sequencing context.
- DEL-047-04 (Vendor Engineered Equipment Package) submittals delivered by the Package Vendor.
- DEL-047-05 (Vendor Document Turnover Package) register populated by the Package Vendor.
- Access to: `26020-Package_Requirements.docx` package heading 2; PACKAGE_REGISTER.csv row PKG-047; DELIVERABLE_REGISTER.csv row DEL-047-06.
- Reviewer authority assigned (acceptance decision is human; ASSUMPTION per K-AUTH-1).

Note: `_DEPENDENCIES.md` does not declare formal Upstream/Downstream edges for DEL-047-06. The prerequisites above are derived from the package responsibility split (PACKAGE_REGISTER.csv row PKG-047) and the deliverable inputs (DELIVERABLE_REGISTER.csv). Formal dependency declaration may be required if Coordination Mode is upgraded.

## Steps

1. **Assemble inputs.** Place a working index that points at DEL-047-01, DEL-047-02, DEL-047-03 (EPC inputs) and DEL-047-04, DEL-047-05 (vendor inputs). Identify any input not yet at the required maturity and record the gap.
2. **Build the vendor document review log.** Enumerate every submittal in DEL-047-05. For each, record: document ID, revision, date received, scope reference (which of DEL-047-01/-02/-03 it satisfies), reviewer, disposition (Accept / Accept with comment / Reject), and comment reference. (Satisfies R-01.)
3. **Build the package acceptance checklist.** Create one section per SOW item in scope (SOW-0253, SOW-0254, SOW-0255, SOW-0256) and one row per applicable interface type for PKG-047 (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). Each row cites the vendor document(s) and disposition. (Satisfies R-02, R-03.)
4. **Compile test/inspection evidence.** For each train and for the shared building, list received test/inspection records (FAT, SAT, NDE, hydrotest, performance, and any package-specific tests). Where the required test set is not yet sliced from `26020-Package_Requirements.docx` heading 2, mark rows `TBD` and surface in the Conflict Table (Guidance C-01). (Satisfies R-04.)
5. **Confirm sour-service qualification.** Record the vendor's sour-service material/process qualification document reference(s) for compressor wetted parts, pressure boundary components, and instrumentation as applicable. Where the standard set is uncertain, mark `TBD` and surface in the Conflict Table (Guidance C-02). (Satisfies R-05.)
6. **Compile turnover evidence.** For each train and the shared building, record mechanical completion certificate, punch-list status, and turnover certification reference. (Satisfies R-06.)
7. **Human acceptance.** Route the assembled review log, acceptance checklist, test/inspection index, and turnover evidence index to the designated human acceptor. The acceptor signs the acceptance checklist. Agents do not sign. (Satisfies R-07.)
8. **Status update and handoff.** Update `_STATUS.md` per the deliverable lifecycle to reflect review/acceptance maturity. Notify downstream consumers (commissioning, operations turnover) per the Construction Work Package (DEL-047-03) handoff plan.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| V-01 | Vendor document review log row count vs. DEL-047-05 register | 1:1 coverage; gaps enumerated, not silent. |
| V-02 | Acceptance checklist covers SOW-0253..SOW-0256 | Each SOW ID appears in at least one checklist row. |
| V-03 | Acceptance checklist covers all thirteen applicable interface types for PKG-047 | All listed interface types present. |
| V-04 | Test/inspection records present per train and for shared building | Per-train records or `TBD` with Conflict Table reference. |
| V-05 | Sour-service qualification recorded | Document reference present or `TBD` with Conflict Table reference. |
| V-06 | Turnover evidence present per train and shared building | Mechanical completion + punch-list + turnover certificate references present per train. |
| V-07 | Acceptance signed by human | Signature block populated by an authorized human. |

## Records

- Vendor document review log (per R-01 / V-01)
- Package acceptance checklist (per R-02, R-03, R-07 / V-02, V-03, V-07)
- Test/inspection evidence index and copies (per R-04, R-05 / V-04, V-05)
- Turnover evidence index and certificates (per R-06 / V-06)
- This procedure's run record(s) in `_run_records/`
- `_STATUS.md` history entry on lifecycle transition
