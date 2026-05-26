# Procedure — DEL-097-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator to review the Package Vendor's deliverables for the Tanks, Condensate (API 650) 3-25 package and to produce the acceptance evidence set. This procedure describes how to produce the acceptance artifacts; it does not redefine vendor engineering activities.

## Prerequisites

Declared upstream dependencies are not currently listed in `_DEPENDENCIES.md`; the following are the **effective** upstream inputs derived from the decomposition register and `_CONTEXT.md`:

- `DEL-097-01 Scope of Work` — accepted EPC SOW for the package.
- `DEL-097-02 Package Datasheet` — accepted EPC technical Datasheet (governing for conformance checks).
- `DEL-097-03 Construction Work Package` — accepted CWP (governing for installation/turnover context).
- `DEL-097-04 Vendor Engineered Equipment Package` — vendor's engineered/designed/supplied package.
- `DEL-097-05 Vendor Document Turnover Package` — vendor document register and submittals.

Reference materials required:

- `_Sources/26020-Package_Requirements.docx` heading 49 (`26020-03-PT-19-006 - Tanks, Condensate`) — Basic Scope, Major Included Equipment, Scope Notes, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes.
- DBM `3-25_Comp_and_Liquids_DBM.md` — Facility Overview; Condensate and Produced-Water Receipts; Condensate Storage and Product Handling (line 406-417); VRU and Vapour Handling (line 436-442); Site Basis.
- API 650 (Modified; applicable edition `TBD`) — clause-level text not in local source set.
- API 2000 (applicable edition `TBD`) — clause-level text not in local source set.

Resource prerequisites (ASSUMPTION — convention not in accessible sources):

- Discipline review leads identified (mechanical, electrical, controls/I&C, civil/structural).
- Project document control system access for upload and status tracking.
- Inspection/witness coverage arranged for hold points.

## Steps

### Step 1 — Initiate Acceptance Cycle

1.1 Confirm `_STATUS.md` of upstream deliverables `DEL-097-01`, `-02`, `-03`, `-04`, `-05` is at or beyond `INITIALIZED` (advisory: ASSUMPTION on threshold).
1.2 Open the acceptance log and record vendor package identifier, vendor name, and revision basis.
1.3 Register the acceptance cycle in the project document control system. (ASSUMPTION on system name.)

### Step 2 — Vendor Document Review

2.1 Retrieve the vendor document register from `DEL-097-05`.
2.2 Cross-check the register against the "Vendor Engineering Deliverables" list at `26020-Package_Requirements.docx` heading 49 (Core vendor documents; Core package engineering; Storage tanks; Relief/flare/vent design; Process piping interfaces; Drainage/containment interfaces; Electrical/lighting/EHT/grounding; Cathodic protection interfaces; Instrumentation and controls interfaces; Structural/foundations/supports/access; Civil grading/spill containment interfaces).
2.3 For each vendor document, assign a reviewer based on document discipline.
2.4 Reviewer evaluates against the EPC Package Datasheet (`DEL-097-02`), DBM source basis, and the heading-49 source slice.
2.5 Record review status (Approved / Approved with Comments / Revise and Resubmit / Rejected — ASSUMPTION on status set) and comments per document.
2.6 Route comments back to vendor for any non-Approved items; track resubmittals until closure.

### Step 3 — Conformance Verification (Equipment)

3.1 Compare the vendor As-Designed package against the EPC Package Datasheet attribute-by-attribute. Record matches and deviations.
3.2 Verify against heading 49 Basic Scope and Major Included Equipment:
- Four (4) × 3,800 bbl C5+ Condensate Product Storage Tanks;
- Modified API 650 non-insulated atmospheric tanks;
- Internal coating Devchem 253 on floors, walls, and roof;
- Blanket gas system per API 2000;
- Per-tank PVRV (vacuum / modulating pressure relief), EPRV (single worst-case relief), VRU header connection, blanket gas connection;
- Tank nozzles sized so plant design capacity can fill a single tank;
- 90 % fill maximum shutdown;
- Winter recycle provision (required vs not required, with rationale).
3.3 Verify operating and design envelope against heading 49 Scope Notes: atmospheric operating pressure; 0-40 °C operating temperature; 32 oz design test pressure; -40 °C to 60 °C design temperature; preliminary capacity 94,940 kg/h / 3,187 Am3/d.
3.4 For each deviation, require a vendor change record (RFI/DCN equivalent) and disposition. Do not informally accept deviations.

### Step 4 — Test and Inspection Evidence Review

4.1 Retrieve hydrotest, NDE, coating (Devchem 253), PVRV/EPRV function-test, and blanket-gas function-test records from the vendor (QLT-003 ITP results; QLT-013 MTRs; QLT-020 Inspection Release; QLT-021 Manufacturing Record Book).
4.2 Verify pass/fail status and traceability to tank tags. Confirm signatures and inspection authority.
4.3 Verify cold-service applicability against -40 °C minimum design (heading 49 Scope Notes) and -40 °C minimum ambient (DBM Site Basis).
4.4 Material/MTR verification against project material specs. (Clause-level details `location TBD`.)
4.5 Capture witness sign-offs at hold points where applicable. (Hold-point list `TBD` — not extracted from accessible source slice.)

### Step 5 — Interface Acceptance Walkdown

5.1 Conduct a multi-discipline walkdown covering only the interfaces marked **Yes** in heading 49 Physical Interface Summary:

- Process Piping;
- Relief / Flare / Vent (PVRV/EPRV discharge routing; VRU header tie-in);
- Drain / Containment;
- Area / Exterior Lighting;
- Grounding / Bonding;
- Cathodic Protection;
- I&C / Control Cabling;
- Grading / Site Drainage / Spill Containment;
- Structural / Foundations / Supports.

5.2 Explicitly confirm and record that interfaces marked **No** in source (Utility Piping; Electrical Power; EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging) are not applicable to this package.

5.3 Each discipline lead signs off their interface scope. Unresolved interface items are recorded as open items with closure dates.

5.4 Resolve the source-level "Interface Coordination Notes: TBD" item: either populate the coordination notes content or record an explicit human-approved carry-over.

### Step 6 — Open-Item Register and Disposition

6.1 Consolidate all unresolved items from Steps 2 through 5 into an open-item register.
6.2 Each item carries: ID, description, source step, owner, target closure date, current status.
6.3 Items required to be closed before acceptance are flagged; items eligible for carry-over require explicit human approval (per OBJ-010 and Guidance principle 5).

### Step 7 — Acceptance Decision

7.1 EPC Integrator acceptance lead reviews the assembled evidence pack:

- Vendor document review log (complete or with documented exceptions);
- Conformance matrix;
- Test and inspection evidence pack;
- Interface acceptance record (including non-applicable confirmations and coordination-note resolution);
- Open-item register with dispositions.

7.2 Issue one of:

- **Accept** — all R-1 through R-6 satisfied with no material open items.
- **Conditional Accept** — material conformance achieved; specific open items tracked with explicit human-approved carry-over.
- **Reject** — material non-conformance; vendor required to remediate and resubmit.

7.3 Record the decision with rationale referencing specific requirements.

### Step 8 — Turnover

8.1 Upon Accept or Conditional Accept, assemble the turnover evidence pack: mechanical completion certificates, punch list, commissioning records, custody handoff documents (per OBJ-010).
8.2 Transfer custody to facility operations per the project turnover convention. (Convention `TBD` — not in accessible local sources.)
8.3 Update `_STATUS.md` of `DEL-097-06` per project lifecycle rules (outside the four-documents skill scope; performed by the appropriate later task).

## Verification

| Step | Verification |
|---|---|
| Step 2 | All vendor register items have a recorded review status and disposition; heading 49 Vendor Engineering Deliverables coverage confirmed |
| Step 3 | Conformance matrix complete; every deviation has a change record; preliminary-vs-final design conditions reconciled |
| Step 4 | Test/inspection records traceable to tank tags; pass/fail recorded; cold-service confirmation present; PVRV/EPRV and blanket-gas function tests recorded |
| Step 5 | Multi-discipline interface sign-off complete for **Yes** interfaces; **No** interfaces explicitly confirmed non-applicable; coordination-note item closed or carried over |
| Step 6 | Open-item register present, current, and explicitly dispositioned |
| Step 7 | Acceptance decision recorded with cited requirement basis |
| Step 8 | Turnover pack assembled; custody handoff record present |

## Records

Records produced by this procedure (the acceptance evidence set):

- Vendor document review log
- Package acceptance checklist / conformance matrix
- Test and inspection evidence pack (hydrotest, NDE, coating, PVRV/EPRV function, blanket-gas function)
- Interface acceptance record (including non-applicable confirmations and coordination-note resolution)
- Open-item register and dispositions
- Acceptance decision record (Accept / Conditional Accept / Reject + rationale)
- Turnover evidence pack and custody handoff record

Record formats and document numbering are `TBD` pending the EPC document control convention for this project; this is consistent with the open items in `Guidance.md` Conflict Table CONF-03.
