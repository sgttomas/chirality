# Procedure — DEL-046-06 EPC Vendor Package Review and Acceptance

This Procedure describes how the EPC Integrator produces the deliverable artifacts: it is a "produce-the-acceptance-evidence" procedure, not an operate-the-equipment procedure.

## Prerequisites

Per the Specification scope and the package-level dependency context (note: not yet formally declared in `_DEPENDENCIES.md` — see Guidance Conflict CF-046-06-003):

- DEL-046-01 (EPC Scope of Work for PKG-046) — required as binding scope basis (TBD: currently shows minimum-viable fileset only).
- DEL-046-02 (Package Datasheet) — required as binding equipment-attribute basis (TBD: minimum-viable fileset).
- DEL-046-03 (Construction Work Package) — required as installation/interface basis (TBD: minimum-viable fileset).
- DEL-046-04 (Vendor Engineered Equipment Package) — required as the subject of review (TBD: minimum-viable fileset).
- DEL-046-05 (Vendor Document Turnover Package) — required as turnover content basis (TBD: minimum-viable fileset).
- Locally accessible source slice from `26020-Package_Requirements.docx` package heading 1 — TBD (binary `.docx` only).
- DBM source for project-wide design envelope: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (accessible).
- EPC Integrator review team identified (mechanical, controls, materials/metallurgy, QA/QC).
- Acceptance checklist template — TBD (project-level form not yet referenced).

## Steps

1. **Confirm baseline.** Confirm current revisions of DEL-046-01 (SOW), DEL-046-02 (Datasheet), DEL-046-03 (CWP), DEL-046-04 (Vendor Engineered Package), DEL-046-05 (Vendor Turnover Package), and the package-specific source slice from `26020-Package_Requirements.docx` are accessible and current. Record any missing items.

2. **Open the Vendor Document Review Log.** Index every vendor-supplied document under PKG-046 and DEL-046-04/DEL-046-05. Capture: document number, revision, type, applicable spec section, reviewer, review date, status (Accepted / Accepted-with-Comment / Returned for Correction / Rejected).

3. **Document content review (Specification R1, R2).** For each vendor document, verify that the content list satisfies the DBM SEC-09 line-617 package content set: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers.

4. **Scope-boundary review (Specification R3).** Verify package boundary alignment with the EPC SOW (DEL-046-01) tie-in lists and the facility utility interface basis. Flag any vendor scope extending into facility-owned interfaces or any package-internal scope unjustifiably transferred to field. Capture in the review log.

5. **Controls integration review (Specification R4).** Verify Unit Control System (UCS) interface design (data maps, alarms replicated to BPCS, permissive logic, trip interfaces, alarm priorities) per DBM SEC-12 line 810. Capture open items for the vendor integration meeting.

6. **Environmental envelope check (Specification R5).** Verify package and component ratings against the design ambient envelope -40 deg C to +35 deg C (DBM SEC-02). Flag any vendor-stated condition that is more severe than the project envelope as governing; flag any less-severe vendor assumption as a non-conformance.

7. **Sour-service / materials review (Specification R6).** Verify material certifications and sour-service compliance traceability for any wetted, pressure-containing, or process-exposed components. Flag missing NACE MR0175/ISO 15156 traceability. (Clause-level requirement basis is `location TBD` pending the readable package-requirements slice.)

8. **Test and inspection evidence review (Specification R8).** Compile and review FAT records, hydrotest records, NDE reports, performance/run-in records, instrument loop-check records (where vendor-executed), and witness/hold-point sign-offs. Place into the Test/Inspection Evidence Index.

9. **Turnover documentation review (Specification R7).** Index vendor turnover documents against DEL-046-05 turnover content list. Place into the Turnover Evidence Index. Flag missing items.

10. **Punch list assembly (if conditional acceptance is proposed).** Aggregate Returned-for-Correction items, open controls-integration items, missing turnover items, and any non-safety-critical residual issues into a Punch List. Each item carries owner, due date, and acceptance criterion.

11. **Acceptance decision (Specification R9).** Mark the Package Acceptance Checklist as Accepted, Accepted-with-Punch-List, or Returned-to-Vendor. The Integrator's lead reviewer signs the checklist. The Package Vendor representative signs as informed.

12. **Handoff to construction/commissioning.** Issue the Acceptance package (Vendor Document Review Log, Package Acceptance Checklist, Test/Inspection Evidence Index, Turnover Evidence Index, Punch List if any) to the construction and commissioning leads. Record the handoff in the package transmittal log.

13. **Close the deliverable.** Set `_STATUS.md` to the next governed state per the project's status workflow (TBD: specific terminal state name and authorized authority); record provenance in `MEMORY.md` if durable context warrants it.

## Verification

| Step | Verification |
|---|---|
| 1 | Baseline confirmed and any missing inputs recorded; no acceptance proceeds against an unconfirmed baseline. |
| 2 | Review Log row count equals or exceeds the vendor document register count. |
| 3 | Each required SEC-09 content category is checked off (or `TBD` with justification) in the Review Log. |
| 4 | Tie-in list reconciled against EPC SOW; deltas resolved or carried as punch items. |
| 5 | UCS-BPCS data map reviewed; open items captured for vendor integration meeting. |
| 6 | Ambient-envelope check signed by mechanical reviewer. |
| 7 | Materials/metallurgy reviewer has signed the sour-service compliance check (or recorded NCRs). |
| 8 | Each acceptance-critical test/inspection record present and signed by witnesses/holders. |
| 9 | Turnover Evidence Index complete or all gaps captured as punch items. |
| 10 | Punch list items have owner, due date, and acceptance criterion. |
| 11 | Package Acceptance Checklist signed per project authority basis. |
| 12 | Transmittal log entry exists; construction/commissioning leads acknowledge receipt. |
| 13 | `_STATUS.md` state change is authorized and recorded. |

## Records

The following records are produced and retained:

- Vendor Document Review Log (artifact)
- Package Acceptance Checklist (artifact, signed)
- Test/Inspection Evidence Index (artifact)
- Turnover Evidence Index (artifact)
- Punch List (artifact, if applicable)
- Transmittal log entry to construction/commissioning
- Updates to deliverable `_STATUS.md` and (if warranted) `MEMORY.md`

Retention period, signatory authority, and document-control numbering scheme: TBD — `location TBD` (project document-control basis not referenced in deliverable-local context).
