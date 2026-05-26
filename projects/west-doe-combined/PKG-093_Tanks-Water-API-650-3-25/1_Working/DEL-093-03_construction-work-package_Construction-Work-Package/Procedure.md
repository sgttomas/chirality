# Procedure — DEL-093-03 Construction Work Package (PKG-093)

> Operational procedure for producing the Construction Work Package artifact set (Construction Work Package narrative, Installation and Tie-in Workface Plan, Construction Interface and Turnover Checklist) for PKG-093 (two API 650 sweet produced-water tanks TK-9060-2 and TK-9070-2). This procedure describes how to **produce** the deliverable; site-execution procedures are downstream of this artifact set and follow the resulting workface plan.

## Prerequisites

Authoritative inputs:

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- PKG-093 row from `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`.
- DEL-093-03 row from the same snapshot's `DELIVERABLE_REGISTER.csv`.
- 03-25 DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) — Site Basis; Raw Gas and Water Design Conditions; Produced Water sections.
- 26020-Package_Requirements.docx package heading 45 (binary; resolve when text-accessible).
- API 650 (current edition applicable to project — location TBD).

Coordinating inputs (when produced):

- DEL-093-01 Scope of Work (EPC Scope of Work for PKG-093).
- DEL-093-02 Package Datasheet (technical handoff basis and interface requirements matrix).
- DEL-093-04 Vendor Engineered Equipment Package (vendor design basis once issued).

No upstream/downstream dependency edges are declared in `_DEPENDENCIES.md` at this writing; coordinate informally with DEL-093-01 and DEL-093-02 authors. (TBD: formal dependency declaration.)

## Steps

1. **Confirm package identity and interface set.**
   - Re-read the PKG-093 row and confirm: two 3,800 bbl tanks TK-9060-2 and TK-9070-2; sweet produced water & process water service; nine interface types declared.
   - Record any divergence between PACKAGE_REGISTER and DEL-093-01 Scope of Work in the Conflict Table (see Guidance.md).

2. **Establish construction site basis.**
   - Capture site location (LSD 03-25-80-15 W6M), elevation (673 m), and -40 deg C governing minimum ambient from the DBM Site Basis.
   - Record cold-climate constructability drivers (winterization, heat tracing, tank heating, cold-weather concrete) as basis statements.

3. **Resolve tank design basis.**
   - Pull design SG (1.25 TBC) and produced-water density (1.18 SG) from the DBM.
   - Cross-check vendor datasheet (when issued) against DEL-093-02 Package Datasheet. Mark `TBD` if not yet issued.

4. **Draft Construction Work Package narrative.**
   - Sequence: site prep -> foundations -> ring wall / pad -> tank erection (per API 650) -> hydrotest -> coating/finish -> tie-ins -> commissioning support -> mechanical completion -> turnover.
   - For each phase, identify EPC scope, vendor scope, and the EPC/vendor interface boundary; cite PACKAGE_REGISTER row for boundary statement.
   - Add hold points: foundation pre-pour inspection; tank bottom prior to shell; pre-hydrotest readiness; post-hydrotest settlement; pre-coating; pre-tie-in.

5. **Build Installation and Tie-in Workface Plan.**
   - Enumerate workface packages per tank (foundation, ring wall, shell, roof, hydrotest, finish, tie-ins) and assign crew, schedule window, and weather constraints.
   - For each tank, list one row per declared interface type from PKG-093 (nine rows × two tanks = eighteen interface tie-in items minimum); identify drawing reference (TBD where drawings not yet issued) and acceptance criteria reference (API 650 clause or vendor instruction — clause `location TBD`).

6. **Build Construction Interface and Turnover Checklist.**
   - Columns: Interface ID; Interface Type; Tank Tag; Description; Acceptance Criteria Reference; Required Records; EPC Sign-off; Vendor Sign-off; Date Closed.
   - Pre-populate with the eighteen interface tie-in items from Step 5 plus tank-level acceptance items (hydrotest, settlement, NDE, CP commissioning, grounding/bonding test, coating acceptance).
   - Add mechanical-completion and turnover gates referencing DEL-093-06 (EPC Vendor Package Review and Acceptance).

7. **Cross-check requirements traceability.**
   - For each R-093-03-* requirement in `Specification.md`, confirm a corresponding verification step exists in this Procedure and an evidence column exists on the checklist.

8. **Mark unresolved items.**
   - Any clause-level reference still pointing to `location TBD` (e.g., API 650 clauses, package requirements heading 45) is recorded as `TBD` in the deliverable Conflict Table and surfaced for human ruling.
   - Do not invent clause numbers.

9. **Issue for review.**
   - Tag the artifact set for EPC Integrator review; coordinate with DEL-093-01 and DEL-093-02 owners for terminology alignment before downstream consumption by DEL-093-04 / DEL-093-06.

## Verification

- All three artifacts (Construction Work Package narrative, Workface Plan, Turnover Checklist) exist and are internally consistent.
- Every R-093-03-* requirement in `Specification.md` has a corresponding entry on the Turnover Checklist or in the Workface Plan.
- All nine declared PKG-093 interface types appear on the checklist for each tank.
- Cold-climate site basis (-40 deg C) appears explicitly in the narrative.
- All `TBD` items are either resolvable from accessible sources or surfaced in `Guidance.md` Conflict Table.

## Records

The procedure (this document) is satisfied by producing the following records inside the deliverable folder when site execution actually occurs (downstream of this drafting deliverable):

- Construction Work Package narrative document
- Installation and Tie-in Workface Plan document
- Construction Interface and Turnover Checklist document
- Hydrotest records (per tank)
- Settlement survey records
- API 650 NDE/weld inspection records
- Foundation inspection and pour records
- CP and grounding/bonding commissioning records
- Tie-in punch list closure records
- EPC and Vendor sign-off records for each checklist row
- As-built mark-ups

At the time of this draft, the deliverable folder contains the four-document kit only; site-execution records (hydrotest, NDE, etc.) are produced during downstream execution. (TBD: site-execution evidence not yet produced.)
