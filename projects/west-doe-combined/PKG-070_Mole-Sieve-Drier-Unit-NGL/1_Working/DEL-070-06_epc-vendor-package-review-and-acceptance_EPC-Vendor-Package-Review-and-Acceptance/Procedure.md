# Procedure — DEL-070-06 EPC Vendor Package Review and Acceptance

> Operational procedure to **produce** the EPC Integrator acceptance package for the PKG-070 Mole Sieve Drier Unit (NGL) vendor package. The acceptance package is the deliverable; this procedure walks the EPC Integrator from upstream-input availability through signed disposition.

## Purpose

Establish a repeatable, auditable workflow for reviewing the PKG-070 vendor package, producing acceptance evidence, and dispositioning open items so that an authorized EPC Integrator signatory can issue binding acceptance.

## Prerequisites

| # | Prerequisite | Source / Reference |
|---|---|---|
| P1 | DEL-070-01 Scope of Work issued (covers SOW-0145..SOW-0148) | Sibling deliverable in PKG-070 1_Working |
| P2 | DEL-070-02 Package Datasheet issued | Sibling deliverable in PKG-070 1_Working |
| P3 | DEL-070-03 Construction Work Package issued | Sibling deliverable in PKG-070 1_Working |
| P4 | DEL-070-04 Vendor Engineered Equipment Package received | Sibling deliverable in PKG-070 1_Working |
| P5 | DEL-070-05 Vendor Document Turnover Package received and indexed | Sibling deliverable in PKG-070 1_Working |
| P6 | DBM-Deepcut accessible to reviewers | `_REFERENCES.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| P7 | `26020-Package_Requirements.docx` heading 24 accessible (extracted to text) — **TBD** | `_REFERENCES.md`; **location TBD** |
| P8 | Authorized EPC Integrator signatory identified | ASSUMPTION (K-AUTH-1) |
| P9 | Reviewer assignments by discipline confirmed | ASSUMPTION (standard EPC integration practice) |

If P1–P6 are not satisfied, do not begin formal acceptance; record the gap and return to upstream owners. P7 should be closed before issuing final acceptance to avoid REQ-070-06-12 being TBD.

## Steps

### Step 1 — Initialize acceptance package workspace

1.1 Create a working folder for the acceptance package under PKG-070/2_Checking or per project file convention. (Out of this deliverable's write scope; do not perform here.)
1.2 Capture inputs received: list each upstream deliverable (DEL-070-01..-05) with revision and receipt date.
1.3 Open the Vendor Document Review Log, the Package Acceptance Checklist, the Open-Items Disposition Table, and the Deviation/NCR Log as empty registers seeded from the Specification requirement IDs (REQ-070-06-01..-13).

### Step 2 — Document-by-document vendor review (REQ-070-06-01, REQ-070-06-10)

2.1 For each document in the DEL-070-05 turnover index, assign a reviewer by discipline.
2.2 Reviewer records: doc ID, revision, reviewer, review date, comments, disposition (Accept / Accept w/ Comments / Revise & Resubmit / Reject), and close-out reference.
2.3 Where a document spans multiple disciplines, record concurrent dispositions and reconcile to the most restrictive.
2.4 Reconcile log entries 1:1 against the turnover index; flag missing documents as turnover gaps for DEL-070-05 owner action.

### Step 3 — SOW conformance checklist (REQ-070-06-02)

3.1 For each scope item SOW-0145, SOW-0146, SOW-0147, SOW-0148, populate the checklist with the SOW clause text (from DEL-070-01). If SOW clause text is not yet drafted, mark **TBD** and surface as a prerequisite gap.
3.2 Map each scope item to the vendor evidence demonstrating conformance (drawing, FAT report, test record, datasheet line).
3.3 Record ruling: Pass / Conditional / Fail. Conditional rulings require a closure plan with owner and date.

### Step 4 — Design-basis conformance verification (REQ-070-06-03..-08)

4.1 Outlet water content / dewpoint (REQ-070-06-03): cross-check vendor FAT dewpoint analyzer record against DBM-Deepcut line 1254–1255 acceptance targets. Confirm cryogenic protection limit dewpoint <-75 degC at maximum operating pressure is satisfied or carried with operations note.
4.2 Adsorbent supply (REQ-070-06-04): inspect vendor material certificate; confirm 3A; reject 4A/5A per DBM line 1269.
4.3 BAHX bring-online trip (REQ-070-06-05): inspect commissioning interlock test record or vendor logic check confirming 66 degC trip; capture I&C tag references.
4.4 Equipment FAT coverage (REQ-070-06-06): confirm FAT certificate or equivalent for each item listed in DBM lines 1274–1287 that falls within the vendor scope; record certificate ID for each.
4.5 Pressure-class compliance (REQ-070-06-07): inspect flange records; confirm 900# where required by DBM line 628.
4.6 MRU media compliance (REQ-070-06-08): inspect MRU media certificate (sulphur-impregnated activated carbon); confirm life ≥6 years, inlet ≤100 µgHg/Nm3, outlet ≤0.01 µgHg/Nm3, end-of-life ΔP <6 psi per DBM line 1286.

If any check fails, raise an NCR in the Deviation/NCR Log (Step 6) before assigning a disposition.

### Step 5 — Open-items disposition (REQ-070-06-09)

5.1 For each DBM-flagged open item relevant to PKG-070 (DBM line 1291: inlet pressure, inlet temperature, cycle times, adsorbent life, regen compressor capacity/differential, regen heater temperature basis, scrubber drain sizing, dry-out header pressure and MAWP), record vendor-supplied value or status.
5.2 Disposition each: Resolved (with reference) / Conditional Acceptance (with closure plan) / Carried Forward to Operations.
5.3 Reflect Conflict Table items C-01..C-04 from `Guidance.md` in the disposition table where they affect PKG-070 acceptance.

### Step 6 — Deviation and NCR handling (REQ-070-06-13)

6.1 For each departure from DEL-070-02 Package Datasheet or DEL-070-01 SOW, classify:
- Approved deviation: reference the concession record.
- Non-conformance: open NCR with corrective action, owner, due date.
6.2 No deviation may be silently normalized into the acceptance package.

### Step 7 — Cross-reference and provenance check (REQ-070-06-12)

7.1 Confirm the acceptance package cites: DBM-Deepcut Molecular-Sieve sections; `26020-Package_Requirements.docx` heading 24 (mark location TBD until extraction is available); applicable sibling deliverables.
7.2 Where a citation is TBD, flag in the package summary so the signatory sees it before disposition.

### Step 8 — Internal QA review

8.1 EPC Integrator QA reviewer (independent from primary reviewers) walks the acceptance package against REQ-070-06-01..-13.
8.2 QA review produces a brief memo: pass / hold-points / fail. Hold-points must be resolved before Step 9.

### Step 9 — Authorized signatory disposition (REQ-070-06-11)

9.1 Authorized human EPC Integrator signatory reviews the assembled package, the QA memo, and the Open-Items Disposition Table.
9.2 Signatory issues one of: Full Acceptance / Conditional Acceptance (with named conditions and closure schedule) / Non-Acceptance (with required actions).
9.3 Signature, name, role, date, and disposition recorded on the Acceptance Disposition Record.
9.4 Agents MUST NOT issue this signature (K-AUTH-1).

### Step 10 — Issue and archive

10.1 Move the acceptance package to PKG-070/3_Issued per project file convention (out of this deliverable's write scope).
10.2 Notify downstream consumers (commissioning, operations, project controls).
10.3 Update `_STATUS.md` per project governance (separate task; not part of drafting).

## Verification

| Step | Verification check |
|---|---|
| 2 | All DEL-070-05 documents present in review log (reconciliation count) |
| 3 | Each of SOW-0145..-0148 has a row with evidence reference and ruling |
| 4 | Each REQ-070-06-03..-08 has a recorded evidence reference and pass/conditional ruling |
| 5 | Each DBM-line-1291 open item has a disposition row |
| 6 | Deviation/NCR log is present and non-blank entries are referenced from affected checklist rows |
| 7 | Citations list includes DBM and Package Requirements heading 24 (or explicit TBD) |
| 8 | QA memo is present and signed by independent reviewer |
| 9 | Acceptance Disposition Record carries authorized human signature |

## Records

The procedure produces (or maintains) the following records as components of the acceptance package:

- Vendor Document Review Log
- Package Acceptance Checklist (SOW-0145..-0148 + REQ-070-06-* mapping)
- Test/Inspection Evidence Index with attached FAT/SAT, NDE, hydrostatic, calibration records
- Turnover Evidence Summary (DEL-070-05 receipt and completeness)
- Open-Items Disposition Table
- Deviation/NCR Log
- QA Review Memo
- Acceptance Disposition Record (signed)
- Citation/Provenance Index

All records are retained as project quality records per the EPC Integrator's document control plan (**TBD** — plan not enumerated in accessible references).
