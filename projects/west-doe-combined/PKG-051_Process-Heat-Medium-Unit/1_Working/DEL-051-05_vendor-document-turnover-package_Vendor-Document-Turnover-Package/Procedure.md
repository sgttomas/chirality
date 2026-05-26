# Procedure: DEL-051-05 — Vendor Document Turnover Package

## Purpose

Describe how the Vendor Document Turnover Package for the Process Heat Medium Unit (`26020-01-PT-15-001`) is produced, transmitted, reviewed, and closed out. Covers both production of the deliverable (the register, submittals, and turnover records) and its use by the EPC Integrator at handover.

## Prerequisites

- EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02) issued and accepted as the basis for vendor scope.
- Vendor Engineered Equipment Package (DEL-051-04) award in place; package vendor identified.
- `26020-Package_Requirements.docx` §6 Vendor Engineering Deliverables list (source basis for the register).
- EPC document-control procedure / Master Document Register (MDR) format (TBD if not yet issued).
- `_REFERENCES.md` and `_CONTEXT.md` for this deliverable read.

## Steps

### Phase A — Register baseline
1. Extract the Vendor Engineering Deliverables list from `26020-Package_Requirements.docx` §6 into PRQ-009 (Vendor Document Index), preserving deliverable IDs and names.
2. Issue DOC-008 (Vendor Document Control Procedure) describing revisioning, hold codes, transmittal format, and numbering aligned to the EPC MDR (mechanics TBD).
3. Baseline PRQ-009 with the EPC Integrator's acknowledgement.

### Phase B — Engineering submittals
4. Vendor produces and transmits core package engineering documents (MEC-001/002/003/006/014/016/017/018; PRO-004/005/007/008/010/011/012/020; STR-001/002/004/005/006; INS-002/003/005/006/008/009/010/011; ELE-002/003/014/015/016/020; TSF-002/003/004/009/011/013) per PRQ-009 schedule.
5. Vendor produces rotating-equipment and heat-transfer specialist documents (MEC-004/007/019, PRO-013, ELE-011; MEC-005/010; REG-022 in preparation).
6. EPC Integrator performs interface/integration review against the Package Datasheet interface matrix; review status recorded against each submittal in PRQ-009.

### Phase C — Manufacturing and quality
7. Vendor issues QLT-006 (Supplier Quality Plan) and QLT-003 (ITP) before fabrication.
8. During fabrication: collect QLT-013 (MTRs/Certs); issue QLT-020 (Inspection Release Certificate) at hold/witness points; assemble QLT-021 (Manufacturing Record Book).

### Phase D — FAT
9. Issue MEC-021 (Equipment FAT Procedure) and ELE-029 (Electrical FAT/SAT Procedure) ahead of FAT.
10. Execute FAT; produce MEC-022 (FAT Report) and ELE-030 (Electrical Test Records / Energization Package).
11. Close FAT punch items; obtain EPC acceptance to ship.

### Phase E — Shipment and code registration
12. Issue PRQ-013 (Logistics / Shipping Plan) and PRQ-015 (SPIR).
13. Complete REG-022 (Pressure Equipment Registration Package) per jurisdictional requirements (specific code TBD).
14. Reconcile MEC-024 (Mechanical Spares / Special Tools) with SPIR.

### Phase F — Installation / SAT support documents
15. Issue MEC-017 (Installation / Setting Drawings), MEC-018 (Lifting / Handling Study), STR-013 (Anchor Bolt / Embedment), STR-014 (Lifting Lug / Transport Analysis), and PIP-008/017/024 in support of EPC construction (DEL-051-03).
16. Provide MEC-025 (IOM Manual) and CTL-003 (Control Narrative) / CTL-005 (Cause and Effect) / CTL-006 (DCS I/O List) / CTL-026 (Package Vendor Interface Specification) for commissioning.

### Phase G — As-builts and turnover close-out
17. Issue as-built PFD/P&ID package (PRO-028) and instrument as-builts (INS-029) after mechanical completion and commissioning.
18. Compile and transmit final Vendor Data Book (PRQ-016) and Mechanical Final Documentation (MEC-023), incorporating all preceding submittals as listed in PRQ-009.
19. EPC Integrator performs final interface/integration review; turnover acceptance recorded against PRQ-009 (acceptance criteria TBD per EPC procedure).

## Verification

- Cross-walk: every Vendor Engineering Deliverable code in `26020-Package_Requirements.docx` §6 appears in PRQ-009 with a current revision and status.
- Every "Yes" interface row in the source's Physical Interface Summary has at least one corresponding discipline document submitted (e.g., Utility Piping → PIP-003/008/017/024; Electrical Power → ELE-002/003/014/015/016/020/027/028; I&C Cabling → INS-009/011 + CTL-006; Fire & Gas → TSF-002/003/004/009/011/013).
- All quality records (QLT-003/006/013/020/021) signed and included in MEC-023 / PRQ-016.
- FAT/SAT records present and accepted.
- REG-022 jurisdictional acceptance evidenced.
- As-builts (PRO-028, INS-029) issued after commissioning.
- EPC interface/integration review sign-offs captured in PRQ-009.

## Records

- PRQ-009 baselined and revised register (the canonical turnover index).
- All submittals listed in the Datasheet "Construction" section, at their accepted revisions.
- DOC-008 procedure issue and revision history.
- QLT-003/006/013/020/021 records.
- MEC-021/022, ELE-029/030 FAT/SAT records.
- PRQ-013, PRQ-015, MEC-024 shipping/spares records.
- REG-022 jurisdictional registration evidence.
- PRO-028, INS-029 as-builts.
- PRQ-016 (Vendor Data Book) and MEC-023 (Mechanical Final Documentation) — turnover artifacts.
- EPC Integrator interface/integration review records (handed to DEL-051-06 vendor package review/acceptance, ASSUMPTION).
