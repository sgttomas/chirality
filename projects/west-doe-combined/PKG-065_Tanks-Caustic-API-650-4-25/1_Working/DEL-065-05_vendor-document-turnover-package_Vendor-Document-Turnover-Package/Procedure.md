# Procedure — DEL-065-05 Vendor Document Turnover Package

This procedure describes how to **produce** the Vendor Document Turnover Package deliverable for PKG-065 (the register, submittals, preserved evidence rows, and turnover records) and how it is **used** at handover from Package Vendor to EPC Integrator.

## Prerequisites

- `_CONTEXT.md` confirmed for DEL-065-05.
- Access to the Gate 7 PROJECT_DECOMP snapshot listed in `_REFERENCES.md`.
- Access to the source slice `26020-Package_Requirements.docx` package heading 20 (binary `.docx`). **Not extracted in this drafting run** — extraction is a prerequisite for the Vendor Document Register Rev. 0.
- Access to sibling deliverables' accepted artifacts (DEL-065-01 Scope of Work, DEL-065-02 Package Datasheet, DEL-065-04 Vendor Engineered Equipment Package). Dependencies are not formally declared in `_DEPENDENCIES.md` (`Coordination Mode: DECLARED`, no upstream/downstream declared) and SHALL be treated as informational unless declared.
- Project document control procedure (identity `TBD`).
- EPC Integrator review workflow defined (`TBD`).

## Steps

### S-01 Extract the source-required vendor document list
Open `_Sources/26020-Package_Requirements.docx` (package heading 20). Enumerate every vendor document explicitly listed for the Tanks, Caustic package. Record each as a candidate row for the Vendor Document Register, preserving the source row text verbatim as an evidence artifact. (Source: `_CONTEXT.md` Source Reference; `_CONTEXT.md` Anticipated Artifacts — "source vendor document table rows as artifacts where available".) **This step was not executed in the current drafting run; binary source slice not directly read.**

### S-02 Draft Vendor Document Register Rev. 0
Build the register including, at minimum, columns for: document number, title, document type, revision, planned submittal milestone, current status, review responsibility, and traceability (SOW reference and equipment tag). Populate from S-01 plus the industry-typical turnover record categories listed in Specification R-04. Label any non-source-derived line as ASSUMPTION until EPC Integrator accepts.

### S-03 Agree revision coding and submittal format with EPC Integrator
Confirm revision coding convention (e.g., A/B/C vs. 0/1/2), file formats (native + PDF), transmittal mechanism, and review/return cycle times. Record the agreement in the deliverable's `MEMORY.md` (when present) or in a project document control note. (Source: ASSUMPTION; project-level convention not stated in available sources.)

### S-04 Issue submittals against the register
For each register line, the Package Vendor produces the document and issues it to the EPC Integrator at the planned milestone. Each submittal carries a transmittal record (vendor doc number, revision, status, transmittal number, date).

### S-05 EPC Integrator review and return
EPC Integrator reviews each submittal for interface/integration concerns and returns it with status (e.g., Approved / Approved-with-Comments / Revise-and-Resubmit). Vendor revises and resubmits until accepted. Track status on the register.

### S-06 Assemble turnover records during fabrication
As fabrication progresses, the Vendor collects MTRs, weld maps, NDE reports, hydrotest record(s), inspection releases, nameplate rubbing/photo, as-built drawings, O&M manual (including heater for TK-6780-1 per SOW-0199), and spare parts list. Items beyond explicit source statements are ASSUMPTION; confirm with EPC Integrator before incorporating into the binding turnover set.

### S-07 Issue Turnover Records package
Bind the turnover records into a single package (electronic and/or hardcopy per project agreement). Index the package against the equipment tags (TK-6780-1; Fresh Caustic Tank tag `TBD`).

### S-08 Final register at handover
Issue the Final-Rev. Vendor Document Register reflecting "Accepted" status for every document and pointing into the Turnover Records package. This is the load-bearing index for handover.

### S-09 Handover acceptance
EPC Integrator confirms acceptance of the complete turnover package. This is the closeout event for DEL-065-05.

## Verification

| Step | Verification |
|---|---|
| S-01 | Extracted list matches source slice byte-for-byte (or with declared, traceable interpretation notes). |
| S-02 | Register Rev. 0 review confirms every Anticipated Artifact category from `_CONTEXT.md` is represented. |
| S-03 | Conventions captured in a durable project artifact (not just email). |
| S-04 | Transmittal log entries exist for every submittal; no register row in "planned" status past its milestone without a deviation note. |
| S-05 | Every register row reaches "Accepted" or equivalent before S-08. |
| S-06 | Turnover record checklist (Spec R-04) is complete or has documented EPC Integrator concurrence on omissions. |
| S-07 | Turnover package is internally indexed and the index references valid documents. |
| S-08 | Final register matches submittal history; no missing rows; no superseded revisions. |
| S-09 | EPC Integrator acceptance record exists and is filed against PKG-065. |

## Records

- Vendor Document Register (all revisions, including Rev. 0 and Final-Rev.)
- Transmittal log
- Each individual vendor document submittal (at each revision)
- Preserved source-required vendor document evidence rows (extracted in S-01)
- Turnover Records package (MTRs, NDE, hydrotest, inspection release, as-builts, O&M, spares, nameplate evidence)
- EPC Integrator review/return records for every submittal
- EPC Integrator handover acceptance record (S-09)
