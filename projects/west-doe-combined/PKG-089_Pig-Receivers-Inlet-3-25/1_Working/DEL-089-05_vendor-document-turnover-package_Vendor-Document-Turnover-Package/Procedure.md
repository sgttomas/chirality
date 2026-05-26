# Procedure — DEL-089-05 Vendor Document Turnover Package (PKG-089)

> Operational. Steps to **produce** and **operate** the vendor document register, submittal flow, and turnover record set. Where source slices do not state a step explicitly, the step is labeled `ASSUMPTION` and listed in `Guidance.md` Conflict Table.

## Purpose

Translate the Specification requirements into an operating procedure the Package Vendor follows to build, submit, and turn over the vendor document set, and the EPC Integrator uses as the interface surface for review.

## Prerequisites

### Inputs (Required)

| Prerequisite | Location | Source |
|---|---|---|
| GATE-07 PROJECT_DECOMP snapshot (registers) | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` | `_REFERENCES.md` |
| DELIVERABLE_REGISTER.csv row 430 | Same snapshot | `_REFERENCES.md` |
| PACKAGE_REGISTER.csv row 77 | Same snapshot | `_REFERENCES.md` |
| ARTIFACT_REGISTER.csv DEL-089-05 rows (109 rows) | Same snapshot | `_REFERENCES.md` |
| SCOPE_LEDGER.csv SOW-0157..0160 | Same snapshot | `_REFERENCES.md` |
| Vendor Engineering Deliverables table | `_Sources/26020-Package_Requirements.docx` heading 42 (binary, not opened directly — content reaches procedure via decomposition extraction) | `_REFERENCES.md`; ARTIFACT_REGISTER.csv |
| Inlet Pipeline Interface and Pigging design basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 226-239 | `_REFERENCES.md` |

### Declared dependencies

- No declared upstream/downstream dependencies at PREPARATION (`_DEPENDENCIES.md`). Natural informational relationships (with DEL-089-02, DEL-089-04, DEL-089-06) are not declared and are not gating; run `TASK + dependency-extract` if formalization is required.

### Permissions and access

- Package Vendor: write access to its document control system and to submittal channels into the EPC Integrator review queue.
- EPC Integrator: read access to vendor submittals; write access to review records and acceptance evidence is in DEL-089-06 scope.

## Steps

### Section A — Build the Register (Production)

1. **Initialize the register from the source basis.**
   - Source: ARTIFACT_REGISTER.csv DEL-089-05 rows (109 rows) and `26020-Package_Requirements.docx` heading 42 (Vendor Engineering Deliverables table).
   - Action: Create one register row per source artifact row. Each register row carries: source artifact ID (e.g., `ART-F156006A5E`), category, document title, planned-revision placeholder, submittal status (initially `planned`).
   - Verification: Row count = 109. (V-001)

2. **Group the register by the 10 source categories.**
   - Categories: Core vendor documents; Core package engineering; Process package design; Process piping interfaces; Relief/Flare/Vent interfaces; Drainage/containment interfaces; Electrical; I&C interfaces; Structural; Pipeline/Pigging interfaces.
   - Source: ARTIFACT_REGISTER.csv DEL-089-05 category rows; PACKAGE_REGISTER.csv row 77 (Applicable interface types).
   - Verification: Every register row carries one of the 10 categories. (V-002)

3. **Anchor each row to authority.**
   - Action: Each register row carries a `SourceBasis` field referencing the source ID (Workbook Packages row 77; or `26020-Package_Requirements.docx` heading 42 entry; or other accepted decomposition source).
   - Verification: Sample-row inspection confirms 100% of rows carry a source citation. (V-003)

4. **Identify and flag identical-twin treatment.**
   - PR-1010-2 and PR-1020-2 are identical receivers (SOW-0159). Mark register rows that apply to either-or-both. Deltas, if any, are itemized.
   - Verification: Identical-twin annotation present where applicable. (V-014)

### Section B — Submit and Track (Operation)

5. **Submit the Vendor Document Control Procedure first.**
   - Source: ARTIFACT_REGISTER.csv DEL-089-05 (ART-F156006A5E). Sequencing as "first" is `ASSUMPTION` (Conflict Table HRR-006).
   - Action: Submit the Vendor Document Control Procedure as Rev A. Do not log other submittals into the live review queue until this is accepted (or provisionally accepted by EPC Integrator).
   - Verification: Vendor Document Control Procedure status = accepted before any other submittal advances past `submitted`. (V-013)

6. **Submit documents per category per the lifecycle.**
   - Lifecycle (`ASSUMPTION`, Conflict Table HRR-001): `planned -> submitted -> under EPC review -> accepted (or returned with comments) -> incorporated into turnover`.
   - Action: Each submission updates the register row with revision, submittal date, and status. Returns-with-comments trigger a new revision (Rev B, Rev C, ...).
   - Verification: Status field present and current for every register row; `planned` count tends to zero as the register matures. (V-004)

7. **Issue the Pressure Equipment Registration Package for the pig receivers.**
   - Source: SCOPE_LEDGER.csv SOW-0160 (MAWP = 635 psig; Design pressure normal high = 200 psig).
   - Action: Assemble the package per the jurisdictional authority's requirements (`ASSUMPTION`: ABSA for Alberta, Conflict Table HRR-002) and submit before shipment release.
   - Verification: Pressure Equipment Registration Package row submitted and accepted. (V-005)

8. **Provide sour-service material evidence.**
   - Source: SCOPE_LEDGER.csv SOW-0159 (0.1 mol% sour).
   - Action: Submit MTRs/certificates and ITP showing material qualification for sour service (`ASSUMPTION`: NACE MR0175 / ISO 15156, Conflict Table HRR-003).
   - Verification: MTR rows and ITP row carry sour-service compliance evidence. (V-006)

9. **Submit ESDV documentation.**
   - Source: SCOPE_LEDGER.csv SOW-0159; DBM `3-25_Comp_and_Liquids_DBM.md` line 239.
   - Action: Submit ESDV data sheets and functional requirements (full-port, piggable, position transmitters) for each inlet ESDV.
   - Verification: ESDV data sheets row submitted; functional requirements traceable to DBM line 239. (V-007)

10. **Document sweet-gas purge and HP flare vent provisions.**
    - Source: SCOPE_LEDGER.csv SOW-0159; DBM lines 230-238.
    - Action: Vendor documentation describes the sweet-gas purge (downstream of manual isolation valve, used prior to opening for pig retrieval) and the vent line to the HP flare system as integrated package provisions.
    - Verification: P&ID submittal and Process Description show both provisions. (V-008)

11. **Run FAT and submit Procedure and Report.**
    - Source: ARTIFACT_REGISTER.csv DEL-089-05 (FAT Procedure row; FAT Report row).
    - Action: Submit FAT Procedure first; on EPC acceptance, execute FAT; submit FAT Report before shipment release (`ASSUMPTION`: pre-shipment sequencing, Conflict Table HRR-005).
    - Verification: Both rows submitted-and-accepted; pre-shipment release evidence exists. (V-009)

12. **Deliver interface-discipline documentation at integration-review level of detail.**
    - Source: PACKAGE_REGISTER.csv row 77 (ApplicableInterfaceTypes); ARTIFACT_REGISTER.csv DEL-089-05 interface rows.
    - Action: Submit interface documents (Process Piping; Relief/Flare/Vent; Drainage; Electrical Power; EHT; I&C; Structural; Pipeline/Pigging) at the level needed for EPC Integrator integration review — not full re-engineering.
    - Verification: Each applicable interface category has at least one document accepted by EPC review. (V-011)

13. **Maintain no-cross-deliverable-bleed.**
    - Source: DELIVERABLE_REGISTER.csv rows 426-431.
    - Action: Do not re-author content owned by sibling deliverables (DEL-089-01..04, DEL-089-06). When a referenced item exists elsewhere, the register row points to that authoritative location.
    - Verification: Cross-deliverable boundary audit shows no duplication. (V-012)

### Section C — Turn Over (Closeout)

14. **Aggregate accepted submittals into the Vendor Data Book / Final Supplier Documentation.**
    - Source: ARTIFACT_REGISTER.csv DEL-089-05 (Vendor Data Book / Final Supplier Documentation row); DELIVERABLE_REGISTER.csv row 431 (DEL-089-06).
    - Action: Compile the final turnover record set: index, all accepted-status submittals at their accepted revision, sour-service traceability chain, pressure equipment registration certificate, FAT report, and SPIR.
    - Verification: Vendor Data Book table-of-contents matches the accepted set of register rows; no `planned` or `submitted-pending` rows remain. (V-010)

15. **Issue final register snapshot to EPC Integrator.**
    - Action: Issue the final register and Vendor Data Book to EPC Integrator as the input to DEL-089-06 (EPC Vendor Package Review and Acceptance).
    - Verification: Issue record exists; EPC Integrator confirms receipt of the final turnover bundle.

## Verification

| Verification ID | Step(s) | Method | Pass Criterion |
|---|---|---|---|
| V-001 | 1 | Register row count vs ARTIFACT_REGISTER.csv | Count = 109; gap report empty |
| V-002 | 2 | Inspection of register structure for all 10 categories | All 10 categories present |
| V-003 | 3 | Sample-row inspection | 100% of rows carry source citation |
| V-004 | 6 | Status field audit | Every row has current status; `planned` count -> 0 over time |
| V-005 | 7 | Pressure Equipment Registration row check | Submitted-and-accepted before shipment |
| V-006 | 8 | Sour-service evidence trace | MTRs + ITP carry sour-service compliance evidence |
| V-007 | 9 | ESDV documentation check | ESDV data sheets row submitted-and-accepted; functional requirements aligned with DBM line 239 |
| V-008 | 10 | Sweet-gas purge / HP flare vent documentation | Provisions documented in P&ID and Process Description |
| V-009 | 11 | FAT records check | FAT Procedure + FAT Report both submitted-and-accepted; pre-shipment release record exists |
| V-010 | 14 | Vendor Data Book audit | Aggregates accepted submittals; no open rows |
| V-011 | 12 | Interface document coverage | Each applicable interface category has at least one accepted document |
| V-012 | 13 | Cross-deliverable boundary audit | No content duplicated from sibling deliverables |
| V-013 | 5 | Document Control Procedure sequencing | Accepted before any other submittal advances |
| V-014 | 4 | Identical-twin treatment audit | Annotations present; deltas itemized |

## Records

The following records result from executing this procedure (each becomes an artifact row tracked in the register):

- **Vendor Document Register** (live, then frozen at turnover) — ART-8BDAE89EA5
- **Vendor Document Index** — ART-D9A4B1F2F5
- **Vendor Document Control Procedure** — ART-F156006A5E
- **Supplier Quality Plan** — ART-83DE002D42
- **All submittals** (one per accepted register row, at accepted revision)
- **FAT Procedure and FAT Report**
- **Pressure Equipment Registration certificate(s)** for PR-1010-2 and PR-1020-2
- **Material Test Reports / Certificates and Inspection Release Certificate(s)**
- **Spare Parts Interchangeability Record (SPIR)**
- **Final Vendor Data Book / Final Supplier Documentation** (the turnover bundle)
- **Issue record to EPC Integrator** (handoff to DEL-089-06)

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `Datasheet.md` (this folder)
- `Specification.md` (this folder)
- `Guidance.md` (this folder) — Conflict Table for HRR items
- GATE-07 PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER.csv row 430; PACKAGE_REGISTER.csv row 77; ARTIFACT_REGISTER.csv DEL-089-05 rows; SCOPE_LEDGER.csv SOW-0157..0160
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 226-239
