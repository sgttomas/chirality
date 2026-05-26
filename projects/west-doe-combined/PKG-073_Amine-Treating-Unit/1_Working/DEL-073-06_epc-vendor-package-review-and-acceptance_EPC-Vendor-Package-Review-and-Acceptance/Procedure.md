# Procedure — DEL-073-06 EPC Vendor Package Review and Acceptance (PKG-073 Amine Treating Unit)

## Purpose

Describe the operational steps the EPC Integrator follows to review the Package Vendor's PKG-073 Amine Treating Unit deliverables, assemble acceptance evidence, and present a human-authored acceptance decision package. The procedure produces the artifacts listed in `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` rows for this deliverable.

## Prerequisites

Inputs required before review begins:

- **DEL-073-01 Scope of Work** (EPC Scope of Work) — baseline (`DELIVERABLE_REGISTER.csv`).
- **DEL-073-02 Package Datasheet** — baseline (`DELIVERABLE_REGISTER.csv`).
- **DEL-073-03 Construction Work Package** — baseline (`DELIVERABLE_REGISTER.csv`).
- **DEL-073-04 Vendor Engineered Equipment Package** — vendor submission under review.
- **DEL-073-05 Vendor Document Turnover Package** — vendor submission under review.
- **GATE-07 PROJECT_DECOMP snapshot** — package register, deliverable register, scope ledger, interface register, artifact register, objective register (`_REFERENCES.md`).
- **Vendor document register** from DEL-073-05.
- **Reviewer assignments** for each discipline / interface type (ASSUMPTION: defined by EPC project execution plan).
- **Project acceptance and open-item disposition conventions** (status `TBD` — not present in this deliverable's references).

Source-text limitation: clause-level acceptance criteria from `_Sources/26020-Package_Requirements.docx` package heading 27 are not locally accessible as markdown. Where steps below would require clause text, they note `TBD` and refer to Guidance Conflict Table item C-073-06-01.

## Steps

### Step 1 — Initialize Review Pack

1.1 Confirm baselines (DEL-073-01, DEL-073-02, DEL-073-03) are at accepted revisions.
1.2 Confirm vendor submissions (DEL-073-04, DEL-073-05) are at the revision intended for acceptance review.
1.3 Open or seed the vendor document review log (ART-B556C47357) listing every vendor document from DEL-073-05.
1.4 Open or seed the package acceptance checklist (ART-0C77AD875E) with sections: Documentation Completeness, Physical Package Completeness, Interface Coverage, Test/Inspection Coverage, Objective Trace, Open Item Disposition.

### Step 2 — Document Review (REQ-073-06-01, REQ-073-06-02)

2.1 For each vendor document in the register, assign a reviewer per discipline.
2.2 Reviewer compares document content against the corresponding clauses in DEL-073-01 (SOW), DEL-073-02 (Datasheet), DEL-073-03 (CWP).
2.3 Reviewer records: status (e.g., approved / approved-with-comments / re-submit / rejected — ASSUMPTION pending project convention), comments, and references to baseline clauses cited.
2.4 Vendor responds; responses are logged with disposition and closure date.
2.5 Repeat 2.2-2.4 until each document reaches a terminal status.

### Step 3 — Physical Package Verification (REQ-073-06-03)

3.1 Cross-check vendor-supplied bill of materials and tag list against DEL-073-02 Datasheet and DEL-073-04 vendor equipment package.
3.2 Verify physical package completeness (modules, tagged items, skid contents). Specific equipment enumeration is `TBD` — see Guidance C-073-06-01.
3.3 Record findings in the acceptance checklist Physical Package Completeness section.

### Step 4 — Interface Coverage Review (REQ-073-06-05)

4.1 For each interface type listed in `INTERFACE_REGISTER.csv` PKG-073 rows (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports), verify the vendor has supplied the matching interface deliverable (terminal connections, loads, interface documents).
4.2 Where an interface specification exists, compare vendor deliverable to specification. Where it does not, perform a presence check and record the gap.
4.3 Record per-interface acceptance status in the checklist Interface Coverage section.

### Step 5 — Test / Inspection Evidence Review (REQ-073-06-04)

5.1 Receive vendor-supplied factory/shop test and inspection evidence (Factory Acceptance Test, hydrostatic tests, NDE, performance tests, materials certifications — specific required set is `TBD`; see Guidance C-073-06-02).
5.2 Verify each required test has evidence on file; verify witnessing requirements per project quality plan (TBD).
5.3 Record acceptance status in the checklist Test/Inspection Coverage section; file evidence under ART-C9A6D6903F.

### Step 6 — Objective Trace (REQ-073-06-09)

6.1 For each objective associated to this deliverable (OBJ-001, OBJ-003..OBJ-010 — package-level via PACKAGE_HEURISTIC; see Guidance C-073-06-03), trace the evidence that the vendor package satisfies the package-boundary contribution.
6.2 Where no acceptance criteria exist at the deliverable level for a given objective, record as ASSUMPTION (directional support).

### Step 7 — Open Item Disposition (REQ-073-06-08, OBJ-010)

7.1 List all unresolved items from Steps 2-6.
7.2 Disposition each: accepted / accepted-with-condition / deferred-to-commissioning / escalated-to-human-ruling (ASSUMPTION: vocabulary pending confirmation).
7.3 Assign closure owner and target closure date for any non-terminal disposition.
7.4 Record dispositions in the checklist Open Item Disposition section.

### Step 8 — Assemble Acceptance Decision Package

8.1 Compile review log, acceptance checklist, test/inspection evidence, and open-item disposition record.
8.2 Verify completeness against this Specification's Documentation section.
8.3 Present the package to the human authority for acceptance signature (REQ-073-06-10).
8.4 No agent issues acceptance; per K-AUTH-1 only the human acceptance signature closes the gate.

### Step 9 — Turnover

9.1 Upon human acceptance, transfer accepted vendor documentation, evidence, and open-item closure record into the facility turnover record.
9.2 Confirm operability/maintainability/sparing/isolation/winterization/commissioning evidence is included (REQ-073-06-06; OBJ-010).
9.3 Hand off to downstream construction / commissioning / facility integration as defined by the project execution plan.

## Verification

| Step | Verification |
|---|---|
| Step 1 | Review pack initialized with all vendor documents listed; baselines pinned to accepted revisions |
| Step 2 | Every vendor document has a terminal review status with traceable comments and dispositions |
| Step 3 | Acceptance checklist Physical Package Completeness section populated and signed by reviewer |
| Step 4 | Each of the 13 PKG-073 interface types has a recorded acceptance status |
| Step 5 | Each required test/inspection has filed evidence; gaps appear in the open-item list |
| Step 6 | Objective trace populated for OBJ-001, OBJ-003..OBJ-010 at the deliverable boundary (with ASSUMPTION labels where appropriate) |
| Step 7 | Every unresolved item has a disposition, owner, and target closure date |
| Step 8 | Acceptance decision package complete; human signature recorded |
| Step 9 | Turnover record transferred; downstream recipient confirms receipt |

## Records

Records produced by executing this procedure (filed in the deliverable folder or its downstream turnover store):

- Vendor document review and comment log (ART-B556C47357)
- Vendor package acceptance and turnover checklist (ART-0C77AD875E)
- Factory/shop test and inspection evidence (ART-C9A6D6903F)
- Open-item disposition record (PROPOSAL: included in turnover evidence)
- Human-authored acceptance decision record (per K-AUTH-1; specific file convention `TBD`)
- Facility turnover handoff record (downstream consumer; `TBD` per project execution plan)
