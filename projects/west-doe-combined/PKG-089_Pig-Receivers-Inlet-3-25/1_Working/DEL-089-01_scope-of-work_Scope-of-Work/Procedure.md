# Procedure — DEL-089-01 EPC Scope of Work, Pig Receivers (Inlet) 3-25

Interpretation note: this Procedure describes how the EPC Integrator produces and maintains the Scope of Work artifact for PKG-089. It is not an operating procedure for the physical pig receiver. SOURCE: skill four-documents Procedure interpretation rule; _CONTEXT.md (deliverable type: EPC Scope of Work).

## Prerequisites

- Read deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`. SOURCE: AGENT_TASK deliverable-local mode.
- Accepted upstream decomposition snapshot is `GATE-07_Final_Published_2026-05-24`. The deliverable register row (DEL-089-01) and the package register row (PKG-089) are the primary registers consumed. SOURCE: _REFERENCES.md.
- Locally accessible authoritative source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04, SEC-05, SEC-15).
- Binary sources `26020-Package_Requirements.docx` (package heading 42) and `26020-02-PT-RFQ-35-001-Pig_Recv_1.docx` referenced by PACKAGE_REGISTER PKG-089 are not directly readable; treat all unreadable detail as TBD or convert before final issue. SOURCE: _REFERENCES.md; Guidance Conflict C-003.
- No declared upstream/downstream dependencies in `_DEPENDENCIES.md` (DECLARED mode). SOURCE: _DEPENDENCIES.md.

## Steps

1. **Establish identity and tag** — Reproduce DeliverableID, ParentPackageID, package tag, discipline, type, and responsible party from PACKAGE_REGISTER.csv PKG-089 and DELIVERABLE_REGISTER.csv DEL-089-01. SOURCE: PACKAGE_REGISTER.csv; DELIVERABLE_REGISTER.csv.
2. **State package function** — Use the PACKAGE_REGISTER PKG-089 scope statement verbatim or a faithful paraphrase. Cite the source. SOURCE: PACKAGE_REGISTER.csv PKG-089.
3. **State equipment configuration** — Carry both source statements for receiver count/size (Datasheet Attributes) and route the disagreement through Guidance Conflict Table C-001. SOURCE: PACKAGE_REGISTER.csv; DBM 3-25 SEC-04.
4. **State facility boundaries** — Reproduce plant inlet boundary and downstream separator interface from DBM SEC-04. SOURCE: DBM 3-25 SEC-04.
5. **Enumerate applicable interfaces** — List the ten interface types from PACKAGE_REGISTER PKG-089 applicable-interface-types column. SOURCE: PACKAGE_REGISTER.csv PKG-089.
6. **Document responsibility split** — Capture the vendor / EPC Integrator responsibility model verbatim from PACKAGE_REGISTER and OBJ-004. SOURCE: PACKAGE_REGISTER.csv PKG-089; OBJECTIVE_REGISTER.csv OBJ-004.
7. **Map scope items** — Identify SOW-0157, SOW-0158, SOW-0159, SOW-0160. Detailed per-item mapping: TBD pending readable workbook scope-ledger row content. SOURCE: _CONTEXT.md; DELIVERABLE_REGISTER.csv.
8. **Map supported objectives** — Record OBJ-002..OBJ-010 as supported (PACKAGE_HEURISTIC, ASSUMPTION). SOURCE: OBJECTIVE_REGISTER.csv; skill four-documents Step 1.
9. **Standards and codes table** — Cite CSA Z662 (DBM SEC-04, SEC-15). Detailed standards list: TBD until Word source basis (heading 42, RFQ-35-001) is readable. SOURCE: DBM 3-25 SEC-04, SEC-15; Guidance Conflict C-003.
10. **Cross-document consistency sweep** — Verify terminology, equipment tags, ESDV shutdown pressures, boundary statements, and interface-type list are consistent across Datasheet, Specification, Guidance, and Procedure. Update if drift is found. SOURCE: skill four-documents Step 5.
11. **TBD/conflict ledger** — Confirm every non-cited claim is either resolved or marked TBD and that contradictions appear in the Guidance Conflict Table. SOURCE: skill four-documents Step 5; K-PROV-1.
12. **Status update** — Update `_STATUS.md` from `OPEN` to `INITIALIZED` only when Pass 1/Pass 2 has run successfully and the current state is `OPEN`. No state regression. SOURCE: skill four-documents Step 7.

## Verification

| Check | What to verify | Source |
|---|---|---|
| Identity matches register | DeliverableID, PackageID, tag, discipline, type, responsible party agree with DELIVERABLE_REGISTER and PACKAGE_REGISTER. | DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| Function statement source-grounded | Function text traces to PACKAGE_REGISTER PKG-089 scope. | PACKAGE_REGISTER.csv |
| Boundary statement source-grounded | Boundary text traces to DBM SEC-04. | DBM 3-25 SEC-04 |
| Interface list complete | All ten applicable interface types listed. | PACKAGE_REGISTER.csv PKG-089 |
| Responsibility split explicit | Vendor/EPC split text traces to PACKAGE_REGISTER and OBJ-004. | PACKAGE_REGISTER.csv; OBJECTIVE_REGISTER.csv OBJ-004 |
| C-001 surfaced | Receiver count/size conflict appears in Guidance Conflict Table. | Guidance.md C-001 |
| Cross-document consistency | Same terms, same values, same tags across the four documents. | Specification Verification table; skill four-documents Step 5 |
| TBDs and ASSUMPTIONs labeled | No unsupported assertion is presented as fact. | K-PROV-1; skill four-documents constraint |

## Records

- This deliverable folder's four documents (Datasheet.md, Specification.md, Guidance.md, Procedure.md).
- `_STATUS.md` updated to INITIALIZED when Pass 1/2 ran from OPEN.
- Run record under `_run_records/TASK_RUN_<timestamp>.md` for this invocation.
- Updates to companion deliverables in PKG-089 (DEL-089-02 Package Datasheet; DEL-089-03 Construction Work Package; DEL-089-06 EPC Vendor Package Review and Acceptance) are out of scope for this deliverable and not modified here. SOURCE: DELIVERABLE_REGISTER.csv.
