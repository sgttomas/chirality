# Procedure — DEL-093-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator to review the Package Vendor's deliverables for the Tanks, Water (API 650) 3-25 package and to produce the acceptance evidence set. This procedure describes how to produce the acceptance artifacts; it does not redefine vendor engineering activities.

## Prerequisites

Declared upstream dependencies are not currently listed in `_DEPENDENCIES.md`; the following are the **effective** upstream inputs derived from the decomposition register and `_CONTEXT.md`:

- `DEL-093-01 Scope of Work` — accepted EPC SOW for the package.
- `DEL-093-02 Package Datasheet` — accepted EPC technical Datasheet (governing for conformance checks).
- `DEL-093-03 Construction Work Package` — accepted CWP (governing for installation/turnover context).
- `DEL-093-04 Vendor Engineered Equipment Package` — vendor's engineered/designed/supplied package.
- `DEL-093-05 Vendor Document Turnover Package` — vendor document register and submittals.

Reference materials required:

- DBM `3-25_Comp_and_Liquids_DBM.md` (SEC-04, SEC-06, Site Basis, SEC-15).
- `26020-Package_Requirements.docx` heading 45 (package requirements — must be retrieved; clause-level content currently `location TBD`).
- API 650 (applicable edition `TBD`).

Resource prerequisites (ASSUMPTION — convention not in accessible sources):

- Discipline review leads identified (mechanical, electrical, controls/I&C, civil/structural).
- Project document control system access for upload and status tracking.
- Inspection/witness coverage arranged for hold points.

## Steps

### Step 1 — Initiate Acceptance Cycle

1.1 Confirm `_STATUS.md` of upstream deliverables `DEL-093-01`, `-02`, `-03`, `-04`, `-05` is at or beyond `INITIALIZED` (advisory: ASSUMPTION on threshold).
1.2 Open the acceptance log and record vendor package identifier, vendor name, and revision basis.
1.3 Register the acceptance cycle in the project document control system. (ASSUMPTION on system name.)

### Step 2 — Vendor Document Review

2.1 Retrieve the vendor document register from `DEL-093-05`.
2.2 For each vendor document, assign a reviewer based on document discipline.
2.3 Reviewer evaluates against the EPC Package Datasheet (`DEL-093-02`), DBM source basis, and `26020-Package_Requirements.docx` heading 45 (when retrieved).
2.4 Record review status (Approved / Approved with Comments / Revise and Resubmit / Rejected — ASSUMPTION on status set) and comments per document.
2.5 Route comments back to vendor for any non-Approved items; track resubmittals until closure.

### Step 3 — Conformance Verification (Equipment)

3.1 Compare the vendor As-Designed package against the EPC Package Datasheet attribute-by-attribute. Record matches and deviations.
3.2 Verify tank count, capacity, construction class, materials, coating (Devchem 253), insulation/heating, and SG basis against DBM SEC-06 lines 419-432.
3.3 For each deviation, require a vendor change record (RFI/DCN equivalent) and disposition. Do not informally accept deviations.

### Step 4 — Test and Inspection Evidence Review

4.1 Retrieve hydrotest, NDE, coating, and insulation/EHT functional records from the vendor.
4.2 Verify pass/fail status and traceability to tank tags. Confirm signatures and inspection authority.
4.3 Verify cold-service applicability (-40 °C minimum ambient — DBM Site Basis line 145).
4.4 Sour-service material/MTR verification per DBM SEC-15. (Clause-level details `location TBD`.)
4.5 Capture witness sign-offs at hold points where applicable. (Hold-point list `TBD` — not extracted from accessible source slice.)

### Step 5 — Interface Acceptance Walkdown

5.1 Conduct a multi-discipline walkdown covering the interfaces enumerated in Specification R-4.1:

- Produced-water transfer pumps suction/discharge tie-ins;
- VRU header connection;
- Vacuum truck connection;
- H2O2 storage tank interfaces;
- EHT, power, grounding/bonding;
- Controls, instrumentation, fire/gas, alarm and shutdown signals;
- Foundations, containment, access.

5.2 Each discipline lead signs off their interface scope. Unresolved interface items are recorded as open items with closure dates.

### Step 6 — Open-Item Register and Disposition

6.1 Consolidate all unresolved items from Steps 2 through 5 into an open-item register.
6.2 Each item carries: ID, description, source step, owner, target closure date, current status.
6.3 Items required to be closed before acceptance are flagged; items eligible for carry-over require explicit human approval (per OBJ-010 and Guidance principle 4).

### Step 7 — Acceptance Decision

7.1 EPC Integrator acceptance lead reviews the assembled evidence pack:

- Vendor document review log (complete or with documented exceptions);
- Conformance matrix;
- Test and inspection evidence pack;
- Interface acceptance record;
- Open-item register with dispositions.

7.2 Issue one of:

- **Accept** — all R-1 through R-6 satisfied with no material open items.
- **Conditional Accept** — material conformance achieved; specific open items tracked with explicit human-approved carry-over.
- **Reject** — material non-conformance; vendor required to remediate and resubmit.

7.3 Record the decision with rationale referencing specific requirements.

### Step 8 — Turnover

8.1 Upon Accept or Conditional Accept, assemble the turnover evidence pack: mechanical completion certificates, punch list, commissioning records, custody handoff documents (per OBJ-010).
8.2 Transfer custody to facility operations per the project turnover convention. (Convention `TBD` — not in accessible local sources.)
8.3 Update `_STATUS.md` of `DEL-093-06` per project lifecycle rules (outside the four-documents skill scope; performed by the appropriate later task).

## Verification

| Step | Verification |
|---|---|
| Step 2 | All vendor register items have a recorded review status and disposition |
| Step 3 | Conformance matrix complete; every deviation has a change record |
| Step 4 | Test/inspection records traceable to tank tags; pass/fail recorded; cold-service confirmation present |
| Step 5 | Multi-discipline interface sign-off complete; open interface items have owners |
| Step 6 | Open-item register present, current, and explicitly dispositioned |
| Step 7 | Acceptance decision recorded with cited requirement basis |
| Step 8 | Turnover pack assembled; custody handoff record present |

## Records

Records produced by this procedure (the acceptance evidence set):

- Vendor document review log
- Package acceptance checklist / conformance matrix
- Test and inspection evidence pack
- Interface acceptance record
- Open-item register and dispositions
- Acceptance decision record (Accept / Conditional Accept / Reject + rationale)
- Turnover evidence pack and custody handoff record

Record formats and document numbering are `TBD` pending the EPC document control convention for this project; this is consistent with the open items in `Guidance.md` Conflict Table CONF-03.
