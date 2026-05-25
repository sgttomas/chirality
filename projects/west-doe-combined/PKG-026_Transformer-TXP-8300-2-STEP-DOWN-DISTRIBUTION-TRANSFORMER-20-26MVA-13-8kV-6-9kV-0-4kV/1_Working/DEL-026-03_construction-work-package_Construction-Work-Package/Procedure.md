# Procedure — DEL-026-03 Construction Work Package

Operational procedure for producing the CWP artifact set for PKG-026 Transformer TXP-8300-2 and for using it during field execution.

## Purpose

Define the steps required to (a) produce the Construction Work Package document, installation and tie-in workface plan, and construction interface and turnover checklist for PKG-026; and (b) execute and verify those artifacts in the field so that DEL-026-06 (EPC Vendor Package Review and Acceptance) can be supported with traceable turnover evidence.

## Prerequisites

- Accepted upstream snapshot: Gate 7 PROJECT_DECOMP (`_REFERENCES.md`).
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at this time. Practical inputs needed for full execution:
  - DEL-026-01 EPC Scope of Work (PKG-026)
  - DEL-026-02 EPC Package Datasheet (PKG-026)
  - DEL-026-04 Vendor Engineered Equipment Package (transformer-specific drawings, installation manual, weights, dimensions, terminal layout, oil volume)
  - DEL-026-05 Vendor Document Turnover Package (installation manual, factory test reports, commissioning procedure)
- Source references read for this draft:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
  - GATE-07 DELIVERABLE_REGISTER row DEL-026-03
  - GATE-07 PACKAGE_REGISTER row PKG-026
  - DBM-Deepcut §Power System; §System Voltages; §Transformers; §Construction Responsibility

## Steps — produce the CWP artifacts

1. Confirm package identity and scope.
   - Confirm DEL-026-03 identity, PKG-026 parent, and seven declared interface types from PACKAGE_REGISTER.
   - Capture any deviations in the Conflict Table in `Guidance.md`.
2. Collect upstream EPC inputs.
   - Pull accepted snapshots of DEL-026-01 and DEL-026-02 when available; otherwise record the gap as a CWP prerequisite.
3. Collect vendor inputs.
   - Request vendor installation manual, foundation loads, terminal layout, oil volume, weight, fan/cooler controls, and grounding-stud configuration from DEL-026-04 / DEL-026-05.
   - Until received, mark dependent CWP sections `TBD`.
4. Draft the installation and tie-in workface plan.
   - Sequence: foundation acceptance → setting on base → mechanical hookup → electrical terminations (primary, secondary, tertiary if present) → home-run cabling → grounding/bonding → cooling-system tie-ins → I&C/control cabling → comms/network → lighting/maintenance access provisions → containment readiness check.
   - For each step, cite source (DBM section, vendor manual section, or `TBD`).
5. Draft the construction interface and turnover checklist.
   - One axis per declared interface type from PACKAGE_REGISTER row PKG-026.
   - Each axis must have an explicit completion criterion and a sign-off slot for the responsible party (Tourmaline field construction, vendor commissioning agent, or EPC Integrator).
6. Cross-check against the Specification.
   - Walk each REQ-CWP-026-* entry in `Specification.md` and confirm coverage in the CWP artifact set; mark uncovered requirements as open.
7. Submit CWP draft for EPC Integrator review.
   - Route the draft, the workface plan, and the checklist to EPC Integrator review before issue-for-construction.

## Steps — execute the CWP in the field

1. Verify foundation readiness and CEC spacing layout before setting the transformer (Specification REQ-CWP-026-04, REQ-CWP-026-05).
2. Set TXP-8300-2 on its structural-steel base per vendor manual (TBD section).
3. Perform mechanical hookup (radiators, cooling fans, conservator, etc., per vendor configuration).
4. Install grounding system, including 100 A / 10 s neutral grounding resistor on the 6.9 kV secondary (Specification REQ-CWP-026-06).
5. Perform electrical terminations on primary, secondary, and any tertiary windings using cable types appropriate to the voltage class (DBM-Deepcut §Power System; cable selection deferred to detailed design).
6. Install and terminate I&C/control cabling, comms/network cabling, and area/exterior lighting feeds per interface checklist.
7. Confirm secondary-containment provisions per DBM §Transformers.
8. Support vendor commissioning agent during oil fill (if shipped without oil), insulation resistance testing, transformer ratio testing, and energization. Record results in turnover dossier.
9. Complete the construction interface and turnover checklist for every declared interface type and obtain signatures.
10. Issue turnover transmittal to DEL-026-06.

## Verification

| Check | Linked requirement | Evidence |
|---|---|---|
| Foundation/base set inspection | REQ-CWP-026-05 | Inspection report |
| CEC spacing verified on as-built layout | REQ-CWP-026-04 | Layout walk-down report |
| Grounding system continuity and NGR commissioning | REQ-CWP-026-06 | Test report |
| 0.4 kV grounding configuration confirmed | REQ-CWP-026-07 | Vendor-confirmed configuration; TBD until vendor data accepted |
| Interface/turnover checklist complete | REQ-CWP-026-03 | Signed checklist |
| Tie-in responsibility log complete for ISBL/OSBL tie-ins | REQ-CWP-026-08 | Signed tie-in records |
| Field activity assignments consistent with DBM construction responsibility | REQ-CWP-026-02 | Cross-reference matrix |
| Alignment with DEL-026-01 and DEL-026-02 | REQ-CWP-026-09 | Document-set alignment review |
| Turnover dossier supports DEL-026-06 | REQ-CWP-026-10 | DEL-026-06 acceptance log |

## Records

- Construction work package document (issued-for-construction copy)
- Installation and tie-in workface plan (issued-for-construction copy)
- Construction interface and turnover checklist (signed)
- Field inspection and test reports (grounding, spacing, base, terminations)
- Vendor commissioning records consumed (link to DEL-026-05)
- Punch-list and turnover transmittal to DEL-026-06

## Notes

- Steps that depend on vendor data are marked or implied `TBD` and shall be resolved when DEL-026-04 / DEL-026-05 are accepted.
- This Procedure is normative for producing the deliverable; field execution remains subject to vendor manual and Tourmaline construction procedures.
