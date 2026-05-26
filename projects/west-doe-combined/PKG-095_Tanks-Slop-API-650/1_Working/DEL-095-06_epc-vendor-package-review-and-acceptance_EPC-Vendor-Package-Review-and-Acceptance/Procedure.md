# Procedure — DEL-095-06 EPC Vendor Package Review and Acceptance (PKG-095)

> **Operational procedure** for the EPC Integrator to perform and evidence vendor package review and acceptance for PKG-095 (Tanks, Slop / API 650). This procedure produces the acceptance artifacts; it does not authorize binding approvals — humans sign.

## Purpose

Establish a repeatable sequence for reviewing PKG-095 vendor submittals, recording acceptance against EPC Scope of Work / Package Datasheet / Construction Work Package, capturing test/inspection and turnover evidence, and routing unresolved items to human ruling.

## Prerequisites

- Sibling EPC Integrator deliverables exist and are at least at INITIALIZED state:
  - DEL-095-01 Scope of Work
  - DEL-095-02 Package Datasheet
  - DEL-095-03 Construction Work Package
- Vendor submittals exist for PKG-095 (engineering, design, vendor documentation, physical equipment package per DEL-095-04 and DEL-095-05).
- `_REFERENCES.md` enumerates the authoritative decomposition snapshot and source materials.
- `_DEPENDENCIES.md` records declared upstream/downstream constraints (currently "None declared during PREPARATION").
- Locally accessible source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Open items / Conflict Table from `Guidance.md` are visible to reviewers.

## Steps

### Step 1 — Establish the acceptance baseline

1.1 Confirm the EPC Scope of Work, Package Datasheet, and Construction Work Package versions to be used as acceptance basis. Record version/snapshot identifiers in the acceptance package cover sheet.
1.2 Mirror the Specification requirements table (`R-095-06-01` through `R-095-06-15`) into the package acceptance checklist as the row set.

### Step 2 — Build the vendor document review log

2.1 Enumerate vendor documents received against the PKG-095 vendor document register (DEL-095-05).
2.2 For each vendor document, record: document title, vendor revision, received date, reviewer, review status (Accepted / Accepted-with-comments / Rejected / Hold), and any links to Conflict Table entries.
2.3 Where a source-required vendor document is missing, mark `TBD` and add an HRR entry.

### Step 3 — Walk the package acceptance checklist

3.1 For each requirement R-095-06-NN, record: verification approach actually used, evidence reference (document / inspection report / test record), status (Pass / Fail / Open / N/A), and signoff.
3.2 For interface verification (R-095-06-05), produce one row per declared interface type. (Source: PACKAGE_REGISTER.csv PKG-095.)
3.3 For slop-service routing verification (R-095-06-06), cross-check vendor P&IDs against the 3-25 design-basis routings (TK-9130-2, V-3900-2 / P-3900-2, P-4100-2 / P-4150-2) and resolve against HRR-095-06-05 before signoff.
3.4 For requirements with `TBD` Datasheet values (capacity, SG, coating, design P/T, sour-service), wait for Package Datasheet (DEL-095-02) closure or escalate per HRR list.

### Step 4 — Capture test and inspection evidence

4.1 Collect vendor factory acceptance test (FAT) records, NDE / inspection reports, hydrotest records, coating inspection records, and dimensional/identification verification records.
4.2 File each as an entry in the test/inspection evidence record with: test/inspection identifier, date, witnessing party, result, and link back to the requirement it satisfies.

### Step 5 — Capture turnover evidence

5.1 Compile turnover-ready evidence: vendor data report, mill certificates, weld maps, coating reports, calibration records, spare-parts list, manufacturer's data report (where applicable), and as-built drawings.
5.2 Record turnover handoff to the EPC Integrator construction/commissioning function: receiver, date, completeness check result.

### Step 6 — Resolve open items

6.1 Reconcile the Conflict Table in `Guidance.md` with current evidence. Move resolved items to closed (with ruling reference); leave unresolved items as NEEDS_HUMAN_RULING.
6.2 Update the acceptance checklist for any requirement whose status changed.

### Step 7 — Package and submit

7.1 Assemble the acceptance package: vendor document review log, package acceptance checklist, test/inspection evidence record, turnover evidence record, Conflict / open-items log.
7.2 Submit to the human authority for binding signoff. Record signoff metadata (name, role, date).
7.3 On signoff, propose `_STATUS.md` transition to the next lifecycle state per the project's state model (out of scope for this skill run; humans authorize).

## Verification

| Check | Method | Pass condition |
|---|---|---|
| All Specification requirements have a checklist row | Visual diff Specification ↔ Checklist | 100% coverage |
| Each interface type has an acceptance row | Inspection of checklist | 9 of 9 interface types covered |
| Each scope item SOW-0213..0216 has a result | Inspection of checklist (scope-coverage matrix) | 4 of 4 covered |
| Each test/inspection record references a requirement | Cross-reference scan | No orphans |
| Each Conflict Table entry has a current disposition | Inspection of Guidance.md / open-items log | No stale `TBD` without owner |
| No agent-issued binding approval | Cover-sheet review | Human signoff entries only |
| Cross-document terminology and values consistent | Cross-document scan | Pass |

## Records

The following records shall result from this procedure and live in this deliverable folder:

- Vendor document review log (`anticipated artifact`)
- Package acceptance checklist (`anticipated artifact`)
- Test/inspection evidence record (`anticipated artifact`)
- Turnover evidence record (`anticipated artifact`)
- Conflict / open-items log (seeded by `Guidance.md` Conflict Table)
- Acceptance package cover sheet (with human signoff entries)
- Run record(s) under `_run_records/`
