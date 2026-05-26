# Procedure: DEL-086-06 — EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator produces the acceptance evidence artifacts for the Flare Stack (Low Pressure) vendor package.

## Prerequisites

- DEL-086-01 (EPC Scope of Work) issued at acceptance-usable maturity.
- DEL-086-02 (Package Datasheet) issued at acceptance-usable maturity.
- DEL-086-03 (Construction Work Package) issued at acceptance-usable maturity.
- DEL-086-04 (Vendor Engineered Equipment Package) submitted by Package Vendor.
- DEL-086-05 (Vendor Document Turnover Package) submitted by Package Vendor.
- Access to project NCR register and QA/QC procedures (TBD — site-level).
- Access to `26020-Package_Requirements.docx` heading 39 source slice (currently not locally extracted — TBD).

## Steps

1. **Establish review basis.**
   1. Compile the basis-item list from DEL-086-01, DEL-086-02, and DEL-086-03.
   2. Tag each basis item with its acceptance criterion and verification method.
   3. Confirm coverage of scope items SOW-0091, SOW-0092, SOW-0093, SOW-0094.

2. **Build the vendor document review log.**
   1. Enumerate submittals from DEL-086-05.
   2. For each submittal, assign reviewer(s), basis-document reference(s), and target disposition date.
   3. Record disposition: `Accept`, `Accept with comment`, `Revise and resubmit`, or `Reject`.
   4. Track resubmittals through to terminal disposition.

3. **Build the package acceptance checklist.**
   1. For each basis item from Step 1, create one or more checklist rows with acceptance criteria.
   2. For each row, identify the evidence source (vendor submittal, test record, inspection record, EPC observation).
   3. Mark rows `Open`, `Met`, `Met with deviation` (link to NCR), or `Not met`.

4. **Collect test and inspection evidence.**
   1. Identify acceptance-critical items from DEL-086-02 (TBD until DEL-086-02 finalized).
   2. Obtain vendor test reports and EPC/third-party inspection records.
   3. Index records into an evidence register tied to checklist rows.

5. **Process non-conformances.**
   1. Open an NCR for each `Not met` or `Met with deviation` checklist row.
   2. Track NCRs to closure (corrective action, accepted concession, or scope change).
   3. Block acceptance until all blocking NCRs are closed.

6. **Assemble turnover evidence.**
   1. Compile turnover evidence per DEL-086-03 handoff expectations.
   2. Confirm tagging, marking, and document hand-off match construction requirements.

7. **Issue acceptance.**
   1. EPC Integrator reviews complete checklist, review log, evidence index, and NCR closures.
   2. Issue acceptance disposition (full / conditional / declined) with documented basis.
   3. ASSUMPTION: human signoff is performed outside this agent's scope (per K-AUTH-1).

## Verification

- Review log: every DEL-086-05 submittal appears with a terminal disposition.
- Checklist: every basis item from DEL-086-01/02/03 maps to at least one checklist row.
- Evidence register: every `Met` row cites at least one evidence record.
- NCR register: no `Open` or `In progress` NCRs remain for blocking items at acceptance.
- Scope coverage: SOW-0091..0094 all mapped to checklist rows.

## Records

- Vendor document review log (final).
- Package acceptance checklist (final, with dispositions).
- Test/inspection evidence index (with record references).
- NCR register entries opened against this package (with closure evidence).
- Turnover evidence package.
- Acceptance disposition record (human-signed; outside agent scope).
