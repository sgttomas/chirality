# Procedure — DEL-066-03 Construction Work Package (PKG-066 Tanks, Condensate (API 650) 4-25)

> Operational document. Describes the procedure for **producing** the Construction Work Package (CWP) deliverable; complementary site-execution procedure outline is included for traceability to the workface plan content the CWP must carry.

## Purpose

Provide a repeatable procedure for the EPC Integrator to assemble, review, and issue the CWP for the 04-25 condensate tank package (PKG-066), and to indicate the on-site construction-execution sequence that the workface plan portion of the CWP must support.

## Prerequisites

### Inputs that must exist before CWP authorship begins

| Prerequisite | Status / Location | Source |
|---|---|---|
| DEL-066-01 Scope of Work (PKG-066) | Sibling deliverable | Decomposition GATE-07 register |
| DEL-066-02 Package Datasheet (PKG-066) | Sibling deliverable | Decomposition GATE-07 register |
| DEL-066-04 Vendor Engineered Equipment Package | Sibling deliverable (vendor-led) | Decomposition GATE-07 register |
| 04-25 Deepcut DBM (governing) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Locally accessible |
| 03-25 Comp & Liquids DBM (cross-facility for condensate transfer tie-in) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Locally accessible |
| Plot plan CIV-235633-5002 | Not available — `location TBD` | DBM-Deepcut line 323 |
| Final geotechnical report | Not available — `TBD` | DBM-Comp_and_Liquids lines 141, 688, 700 |
| Workbook Packages row 89; 26020-Package_Requirements.docx package heading 21 | `_REFERENCES.md` cites; not locally extracted — `location TBD` | `_REFERENCES.md` |
| Declared upstream/downstream dependencies | None declared at PREPARATION | `_DEPENDENCIES.md` |

### Standards required for clause-level CWP content (not locally accessible at the time of this draft)

API 650 (Modified); API 2000; API 2510; NFPA 30; OGAOM Sec. 9.6.15.

## Steps — Producing the CWP deliverable

1. **Confirm package envelope.** Read DEL-066-01 (SOW) and DEL-066-02 (Package Datasheet) and lock the tagged-equipment list, service allocation, and design envelope into the CWP cover page.
2. **Establish authority basis.** Cite the 04-25 Deepcut DBM, the 03-25 DBM (for the cross-facility condensate transfer tie-in), and applicable standards. Flag any standards whose clause text is not locally accessible.
3. **Resolve open conflicts.** Pull the Conflict Table from `Guidance.md` (CFL-01 tank quantity; CFL-02 per-tag service allocation; CFL-03 tie-in responsibility split; CFL-04 standards-clause access) and route to human ruling. Do not issue the CWP for construction with unresolved CFL items.
4. **Assemble the construction work package document.**
   - Section A: Package identity, equipment list, tag assignments, references.
   - Section B: Construction responsibility matrix (per DBM-Deepcut lines 107-125; per-tie-in entries per CFL-03 resolution).
   - Section C: Construction sequence and milestones (foundations → tank erection → mechanical hookup → coating/insulation/heat-trace → instrumentation → blanket-gas / VRU tie-in → hydrotest → loop checks → mechanical completion).
   - Section D: Tie-in register (joint-planned with Tourmaline; references DBM tie-in points: VRU suction header, blanket-gas header, drain headers, condensate transfer to 03-25 Liquids Hub via P-9210-1 / P-9220-1).
   - Section E: Inspection and test plan summary (foundation QC; API 650 erection inspections; hydrotest at 16 oz test pressure; coating/insulation/heat-trace verification; instrument loop checks; blanket-gas leak check). `TBD` clause-level criteria pending standards access.
   - Section F: Punch-list and turnover plan (mechanical completion → care-and-custody → commissioning).
5. **Assemble the installation and tie-in workface plan.**
   - Work-front breakdown by tank and by tie-in.
   - Sequencing dependencies with the adjacent tank-farm pump module (product recycle pump, condensate skim pump, condensate transfer pumps P-9210-1 / P-9220-1) per DBM-Deepcut lines 1669-1675.
   - Tie-in tickets (one per joint-planned tie-in).
   - Permit-to-work / lockout references (per Tourmaline site permitting; details `TBD` to site procedures).
6. **Assemble the construction interface and turnover checklist.**
   - Mechanical completion items mapped to REQ-CWP-02 through REQ-CWP-13 verification rows in `Specification.md`.
   - Loop-check items (PVRVs, blanket-gas, level instruments, transfer-pump interlocks).
   - Coating/insulation/heat-trace verification items (REQ-CWP-06).
   - Care-and-custody handover form references.
7. **Reconcile to registers.** Reconcile the CWP register against the plot plan (when issued), equipment list, and the overall facility construction work-package register per DBM-Comp_and_Liquids line 661.
8. **EPC Integrator review.** Confirm scope alignment with DEL-066-01 and DEL-066-02; confirm conflict-table closure; confirm tie-in responsibility entries are populated; confirm standards citations or `TBD` markers.
9. **Issue for construction (IFC).** Issue the CWP only after: geotechnical report acceptance for foundation portions; plot plan CIV-235633-5002 issuance; conflict-table closure; and tie-in responsibility confirmation.

## Steps — On-site construction execution (workface-plan content the CWP must carry)

This sub-sequence is the field-execution outline the CWP's workface plan must support. It is included in the CWP procedure for traceability; it is not the EPC Integrator's self-perform sequence.

1. Site grading and drainage prep (Tourmaline scope; DBM-Deepcut line 108).
2. Piling and tank foundations (against accepted geotechnical report).
3. Tank erection by tank vendor / sub-contractor (API 650 modified, field-erected). `TBD` site-specific erection sequence pending vendor erection method statement.
4. Coating and internal/external work per service (slop tank fully insulated; product tanks non-insulated).
5. Mechanical hookup: tank nozzles to inlet (stabilizer bottoms), outlet (cascade), drains, blanket-gas, VRU vapour return, PVRVs, level instruments.
6. Installation of shipped-loose instruments and valves (Tourmaline scope; DBM-Deepcut line 115).
7. Tank-farm pump module set and hook-up (sequenced with tank availability; DBM-Deepcut lines 1669-1675).
8. Electrical and instrumentation hookup; home-run cabling and terminations (Tourmaline scope; DBM-Deepcut lines 118-119).
9. Hydrostatic testing per API 650 / 16 oz test pressure basis.
10. Blanket-gas and VRU header tie-in and leak check; PVRV and EPRV verification.
11. Loop checks and interlock proving for level/flow control and transfer pumps.
12. Punch list walkdown and clearance.
13. Mechanical completion; care-and-custody handover to commissioning.

## Verification

| Verification step | Method | References |
|---|---|---|
| CWP scope-against-SOW alignment | Cross-check table CWP vs. DEL-066-01 | Spec REQ-CWP-01 |
| Tank spec compliance | API 650 fabrication and erection inspection records; 16 oz hydrotest record | Spec REQ-CWP-02 |
| Tag and quantity verification | Walkdown vs. equipment register | Spec REQ-CWP-03; Guidance CFL-01 |
| Cascade and slop configuration | P&ID walkdown | Spec REQ-CWP-04 |
| Blanket-gas / VRU hookup | Leak check; PVRV check | Spec REQ-CWP-05 |
| Winterization | Insulation inspection (slop); recycle functional test (product) | Spec REQ-CWP-06 |
| Foundation conformance | Foundation QC records vs. accepted geotechnical report | Spec REQ-CWP-07 |
| Construction responsibility execution | Sign-off per work-front | Spec REQ-CWP-08 |
| Tie-in execution | Joint tie-in tickets + permit records | Spec REQ-CWP-09 |
| Pre-IFC register reconciliation | Reconciliation record | Spec REQ-CWP-10 |
| Coordinate placement | Surveyed walkdown vs. plot plan (when issued) | Spec REQ-CWP-11 |
| Spacing compliance | Surveyed spacing vs. standards | Spec REQ-CWP-12 |
| Pump-module sequenced commissioning | Commissioning checklist | Spec REQ-CWP-13 |

## Records

The following records shall be produced and retained as CWP output evidence:

- Issued Construction Work Package document (Sections A-F).
- Issued installation and tie-in workface plan (per work-front).
- Issued construction interface and turnover checklist.
- Foundation QC records (traceable to accepted geotechnical report).
- API 650 erection inspection records (per vendor scope) and EPC review signoffs.
- Hydrotest records (16 oz test pressure basis).
- Coating, insulation, and heat-trace verification records.
- Instrument loop-check records.
- Blanket-gas / VRU leak-check records.
- Tie-in permit and tie-in ticket records.
- Punch list and mechanical completion records.
- Care-and-custody handover records to commissioning.
- Conflict Table closure records (CFL-01 through CFL-04).
