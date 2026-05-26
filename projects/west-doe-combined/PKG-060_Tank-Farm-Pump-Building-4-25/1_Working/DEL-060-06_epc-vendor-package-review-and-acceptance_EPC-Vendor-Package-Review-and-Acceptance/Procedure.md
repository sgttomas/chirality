# Procedure — DEL-060-06 EPC Vendor Package Review and Acceptance

This Procedure describes how the EPC Integrator produces the deliverable artifacts: it is a "produce-the-acceptance-evidence" procedure, not an operate-the-equipment procedure.

## Prerequisites

Per the Specification scope and the package-level dependency context (note: not yet formally declared in `_DEPENDENCIES.md` — see Guidance Conflict CF-060-06-003):

- DEL-060-01 (EPC Scope of Work for PKG-060) — required as binding scope basis (TBD: currently shows minimum-viable fileset only).
- DEL-060-02 (Package Datasheet) — required as binding equipment-attribute basis (TBD: minimum-viable fileset).
- DEL-060-03 (Construction Work Package) — required as installation/interface basis (TBD: minimum-viable fileset).
- DEL-060-04 (Vendor Engineered Equipment Package) — required as the subject of review (TBD: minimum-viable fileset).
- DEL-060-05 (Vendor Document Turnover Package) — required as turnover content basis (TBD: minimum-viable fileset).
- Locally accessible source slice from `26020-Package_Requirements.docx` package heading 15 — TBD (binary `.docx` only).
- Locally accessible source slice from `26020-Packages_Interfaces_4_export.xlsx` row 85 — TBD (binary `.xlsx` only).
- DBM source for project-wide design envelope: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (accessible).
- EPC Integrator review team identified (mechanical/rotating equipment, controls, materials/metallurgy, civil/structural, QA/QC).
- Acceptance checklist template — TBD (project-level form not yet referenced).

## Steps

1. **Confirm baseline.** Confirm current revisions of DEL-060-01 (SOW), DEL-060-02 (Datasheet), DEL-060-03 (CWP), DEL-060-04 (Vendor Engineered Package), DEL-060-05 (Vendor Turnover Package), and the package-specific source slice from `26020-Package_Requirements.docx` heading 15 are accessible and current. Record any missing items.

2. **Open the Vendor Document Review Log.** Index every vendor-supplied document under PKG-060 and DEL-060-04 / DEL-060-05. Capture: document number, revision, type, applicable spec section, reviewer, review date, status (Accepted / Accepted-with-Comment / Returned for Correction / Rejected). Maintain separate sub-sections per pump train (condensate transfer, water transfer, sour-water treatment, process water transfer, fresh caustic transfer — DBM lines 2618-2622).

3. **Document content review (Specification R1, R2).** For each vendor document, verify that the content list satisfies the DBM SEC-09 line-617 package content set: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers.

4. **Scope-boundary review (Specification R3).** Verify package boundary alignment with the EPC SOW (DEL-060-01) tie-in lists, the facility utility interface basis (incl. shared 03-25/04-25 fuel gas and instrument air), and tank-farm electrical building (860-1) interfaces. Confirm bullets, tanks, and dike walls are not absorbed into the pump-building vendor scope. Capture in the review log.

5. **Layout / spacing review (Specification R7).** Verify that the package general arrangement and plot plan show pump-suction-from-bullet skids at not less than 3.05 m (10 ft) from pressurized bullets per API 2510 (DBM SEC-02 line 252). Flag deviations.

6. **Controls integration review (Specification R4).** Verify pump-package values and general alarms replicate to BPCS; data maps, permissive logic, trip interfaces, and alarm priorities recorded. Capture open items for the vendor integration meeting. Confirm interface with Tank Farm Electrical Building (DBM line 2816).

7. **Environmental envelope check (Specification R5, R6).** Verify package and component ratings against the design ambient envelope -40 deg C to +35 deg C (DBM SEC-02 lines 197-198) and site wind/elevation inputs (DBM SEC-02 lines 195, 200, 202). Flag any vendor-stated condition that is more severe than the project envelope as governing; flag any less-severe vendor assumption as a non-conformance.

8. **Sour-service / materials review (Specification R8).** Per pump train, verify material certifications and sour-service compliance traceability for wetted, pressure-containing, or process-exposed components in H2S-bearing service (condensate transfer, sour-water treatment). Confirm NACE MR0175 / ISO 15156 traceability where applicable. Document caustic-service compatibility separately for fresh caustic transfer pumps. (Clause-level requirement basis is `location TBD` pending readable package-requirements slice.)

9. **Test and inspection evidence review (Specification R10).** Compile and review FAT records, hydrotest records, NDE reports, mechanical run / performance / vibration records, instrument loop-check records (where vendor-executed), and witness/hold-point sign-offs. Place into the Test/Inspection Evidence Index. Confirm shop-built scope (Tank Farm Pump Module per DBM line 2817) was shop-tested, not deferred to field.

10. **Turnover documentation review (Specification R9).** Index vendor turnover documents against DEL-060-05 turnover content list. Place into the Turnover Evidence Index. Flag missing items.

11. **Punch list assembly (if conditional acceptance is proposed).** Aggregate Returned-for-Correction items, open controls-integration items, missing turnover items, and any non-safety-critical residual issues into a Punch List. Each item carries owner, due date, and acceptance criterion. (Optionally segregated by pump train per Guidance PROPOSAL.)

12. **Acceptance decision (Specification R11).** Mark the Package Acceptance Checklist as Accepted, Accepted-with-Punch-List, or Returned-to-Vendor — at the train level and at the building (package) level. The Integrator's lead reviewer signs the checklist. The Package Vendor representative signs as informed.

13. **Handoff to construction/commissioning.** Issue the Acceptance package (Vendor Document Review Log, Package Acceptance Checklist, Test/Inspection Evidence Index, Turnover Evidence Index, Punch List if any) to the construction and commissioning leads. Record the handoff in the package transmittal log.

14. **Close the deliverable.** Set `_STATUS.md` to the next governed state per the project's status workflow (TBD: specific terminal state name and authorized authority); record provenance in `MEMORY.md` if durable context warrants it.

## Verification

| Step | Verification |
|---|---|
| 1 | Baseline confirmed and any missing inputs recorded; no acceptance proceeds against an unconfirmed baseline. |
| 2 | Review Log row count equals or exceeds the vendor document register count; per-train sub-sections present. |
| 3 | Each required SEC-09 content category is checked off (or `TBD` with justification) in the Review Log. |
| 4 | Tie-in list reconciled against EPC SOW; deltas resolved or carried as punch items. |
| 5 | Plot-plan / GA spacing check signed; deviations from API 2510 captured. |
| 6 | UCS-BPCS data map reviewed; open items captured for vendor integration meeting. |
| 7 | Ambient-envelope and site-loading check signed by mechanical and civil/structural reviewers as applicable. |
| 8 | Materials/metallurgy reviewer has signed the sour-service compliance check per train (or recorded NCRs); caustic-service compatibility recorded. |
| 9 | Each acceptance-critical test/inspection record present and signed by witnesses/holders; shop-built items have shop test evidence. |
| 10 | Turnover Evidence Index complete or all gaps captured as punch items. |
| 11 | Punch list items have owner, due date, and acceptance criterion. |
| 12 | Package Acceptance Checklist signed per project authority basis at train and building levels. |
| 13 | Transmittal log entry exists; construction/commissioning leads acknowledge receipt. |
| 14 | `_STATUS.md` state change is authorized and recorded. |

## Records

The following records are produced and retained:

- Vendor Document Review Log (artifact, per-train sectioned)
- Package Acceptance Checklist (artifact, signed)
- Test/Inspection Evidence Index (artifact)
- Turnover Evidence Index (artifact)
- Punch List (artifact, if applicable)
- Transmittal log entry to construction/commissioning
- Updates to deliverable `_STATUS.md` and (if warranted) `MEMORY.md`

Retention period, signatory authority, and document-control numbering scheme: TBD — `location TBD` (project document-control basis not referenced in deliverable-local context).
