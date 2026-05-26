# Procedure — DEL-070-05 Vendor Document Turnover Package

## Purpose

Describe how the Package Vendor produces, controls, submits, and turns over the vendor documentation set for PKG-070 Mole Sieve Drier Unit (NGL), and how the EPC Integrator interfaces with that flow.

## Prerequisites

- EPC Scope of Work (DEL-070-01) issued. (Declared package context; no upstream dependency rows declared in _DEPENDENCIES.md — treated as project-level prerequisite.)
- Package Datasheet (DEL-070-02) issued (technical handoff basis for vendor engineering).
- Vendor Engineered Equipment Package (DEL-070-04) underway (this document-turnover unit wraps that vendor execution).
- Local accessible references: 26020-Package_Requirements.docx (Mole Sieve §heading 24); 26020-Packages_Interfaces_4_export.xlsx (interface source pointer; slice TBD).
- DOC-008 Vendor Document Control Procedure available.

## Steps

1. Build the Vendor Document Register.
   a. Initialize the register with every row from the Mole Sieve "Vendor Engineering Deliverables" table in 26020-Package_Requirements.docx, preserving discipline grouping.
   b. Add each row's attributes: Deliverable ID, Deliverable Name, discipline group, required revision target, EPC review owner. ASSUMPTION on attribute set (location TBD).
   c. Issue the register as PRQ-009 Vendor Document Index.

2. Establish document control under DOC-008.
   a. Apply numbering, revision, and transmittal conventions per DOC-008.
   b. Tie every submittal back to a register row.

3. Author and issue source-required vendor documentation per discipline group.
   a. Core package engineering: MEC-001/002/003/006/014/016/017/018/021/022/023/024/025.
   b. Static pressure equipment: MEC-005/009; REG-022.
   c. Heat transfer equipment: MEC-010.
   d. Process package design: PRO-004/005/007/008/010/011/012/020/025/026/027/028.
   e. Relief / flare / vent design: PRO-014/015/016/017/018.
   f. Process piping interfaces: PIP-003/004/006/007/008/009/017/018/024/025/028.
   g. Drainage / containment interfaces: PRO-023; CIV-014.
   h. Electrical, lighting, EHT, grounding: ELE-002/003/014/015/016/020/027/028/029/030/017/018/012/019; PIP-020/021.
   i. Instrumentation and controls: INS-002/003/005/006/008/009/010/011/016/017/018/025/029; CTL-003/005/006/026.
   j. Fire and gas / technical safety: TSF-002/003/004/009/011/013/028.
   k. Structural, foundations, supports, access: STR-001/002/004/005/006/011/012/013/014/020.

4. Submit vendor documents to the EPC Integrator.
   a. For each row, transmit issued revision via the DOC-008 transmittal mechanism.
   b. Flag interface-bearing rows (CTL-026, PIP-004, INS-018, ELE-028) for coordinated EPC review.
   c. Capture EPC review disposition (accepted / accepted with comments / rejected / re-issue).

5. Drive quality and inspection evidence.
   a. Issue QLT-006 Supplier Quality Plan.
   b. Issue QLT-003 Inspection and Test Plan.
   c. Collect QLT-013 Material Test Reports / Certificates as fabrication progresses.
   d. Issue QLT-020 Inspection Release Certificate.
   e. Assemble QLT-021 Manufacturing Record Book / Vendor Data Book.

6. Close regulatory submission.
   a. Compile and submit REG-022 Pressure Equipment Registration Package per jurisdiction. ASSUMPTION on jurisdiction; not stated in accessible source.
   b. Capture acceptance evidence in the register.

7. Address logistics and spares documentation.
   a. Issue PRQ-013 Logistics / Shipping Plan.
   b. Issue PRQ-015 Spare Parts Interchangeability Record (SPIR).

8. Phase as-built / late-revision closures.
   a. Track inherently late rows (e.g., PRO-028, PIP-028) on a separate phase of the register.
   b. Revise to as-built before turnover gate.

9. Execute turnover.
   a. Confirm every register row is at an accepted / closed state, or marked "N/A — justified" with engineering justification.
   b. Issue MEC-023 Vendor Data Book / Mechanical Final Documentation.
   c. Issue PRQ-016 Vendor Data Book / Final Supplier Documentation.
   d. Hand the consolidated turnover record to the EPC Integrator (review and acceptance evidence is captured separately in DEL-070-06).

## Verification

- Register-to-source completeness check: every row in the Mole Sieve "Vendor Engineering Deliverables" source table appears in the register (R-1, R-2, R-8).
- Document control audit: sample submittals trace cleanly back to register rows under DOC-008 (R-3).
- Quality evidence check: QLT-003/006/013/020/021 issued and accepted (R-6, R-5).
- Turnover gate check: PRQ-016, MEC-023, QLT-021 are accepted; no register row left in open state without justified N/A (R-5, R-12).
- Interface-row coordination check: CTL-026, PIP-004, INS-018, ELE-028 carry coordinated-review disposition (R-14).
- Regulatory check: REG-022 closure evidence captured (R-13).
- Interface-notes integration check: if interface notes are published after Specification issue, re-verify register and submittal closures incorporate them (R-15).

## Records

- Vendor Document Register (issued as PRQ-009; maintained through turnover).
- Submittal transmittal log per DOC-008.
- EPC review disposition log (one entry per submittal/revision).
- Quality records: QLT-003, QLT-006, QLT-013, QLT-020, QLT-021.
- Regulatory closure record: REG-022 acceptance evidence.
- Logistics / spares records: PRQ-013, PRQ-015.
- Final closures: MEC-023 (mechanical), PRQ-016 (commercial), QLT-021 (manufacturing).
- Turnover handoff record to EPC Integrator (acceptance evidence resides in DEL-070-06).
