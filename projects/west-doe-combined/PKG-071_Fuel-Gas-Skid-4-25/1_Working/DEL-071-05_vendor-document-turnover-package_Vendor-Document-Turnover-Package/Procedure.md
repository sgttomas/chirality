# Procedure — DEL-071-05 Vendor Document Turnover Package (PKG-071 Fuel Gas Skid 4-25)

This procedure covers steps to **produce** and **maintain** the vendor document turnover package across the PKG-071 Fuel Gas Skid 4-25 life cycle. Steps to **use** the turnover package (e.g., O&M operations of the skid itself) belong to operating procedures owned by Operations, not by this deliverable.

## Prerequisites

- `_CONTEXT.md` accepted, with PKG-071 scope confirmed.
- Vendor selection complete for the fuel gas skid (vendor identity TBD as of this draft).
- Project document-control plan available (numbering scheme, revision classes, transmittal templates) — TBD.
- EPC interface documents (P&IDs, line list, instrument index, area classification drawing, plot plan) available at each relevant revision class.
- Locally accessible reference: DBM-Deepcut Fuel Gas Basis (L1839-L1905) for technical-content cross-checks.
- Declared upstream dependencies: none in `_DEPENDENCIES.md`; implicit upstream is PKG-071 procurement.

## Steps

1. **Initialize Vendor Document Register.** Create the register skeleton using the project-defined column set (column set TBD; ASSUMPTION columns: vendor doc number, EPC doc number, title, class, revision, status, planned-submit date, actual-submit date, review code, As-Built revision).
2. **Populate expected entries.** Seed the register with one row per required vendor document class for the fuel gas skid scope (class list per Specification R-2; final list TBD).
3. **Map decomposition vendor-document rows to register entries.** For any vendor-document table rows in the GATE-07 PROJECT_DECOMP snapshot that name PKG-071, create or link the corresponding register entry (per Specification R-9 and `_CONTEXT.md` Notes).
4. **Issue submittals per project schedule.** The vendor issues each document at the planned revision class; each transmittal updates the register status. Format per Specification R-6 (TBD).
5. **EPC Integrator review.** EPC reviews each submittal for interface consistency with current P&IDs, line list, instrument index, and area classification drawing. Review codes are assigned per project review code set (TBD).
6. **Resolve review comments.** Vendor responds to review comments and re-issues at the next required revision class.
7. **Cross-check against Fuel Gas Basis.** EPC integration review verifies vendor data against DBM-Deepcut L1843-L1903 design values (V-3210-1 sizing; heater type and controls; regulator sparing; emergency-generator supply pressure ceiling; buyback gas independence). Discrepancies trigger MoC or vendor correction.
8. **Capture turnover records.** As fabrication, FAT, shipment, site receipt, SAT, preservation, and commissioning events occur, the vendor (and EPC where applicable) collects turnover records (pressure-test, NDE, calibration, FAT/SAT, preservation, lifting). Each record is logged as a register entry (per Specification R-7).
9. **Issue terminal-revision (As-Built) set.** Before Hand-Over, vendor issues As-Built (or project-terminal class) for every register entry not already at that class.
10. **Hand-Over.** EPC confirms register completeness and revision-class compliance; package is transmitted to Owner with final register and full artifact set.

## Verification

- Register completeness check: every required document class has at least one entry, and every entry has a final revision class.
- Interface-consistency check: vendor data values match the Fuel Gas Basis design values cited in Specification R-3.
- Code-compliance check: U-Stamp letter, CRN, electrical certifications, NDE reports present for applicable equipment (per Specification R-4).
- Turnover-records inventory: required records present per Specification R-7 (full required-records list TBD).
- Sour-service review: materials and purge documentation explicitly address sour exposure per Guidance Considerations.

## Records

The records produced by following this procedure ARE the deliverable artifacts:

- The maintained Vendor Document Register (live document; final version archived at Hand-Over).
- All vendor document submittals (one per register entry).
- All turnover records (FAT, SAT, pressure-test certificates, NDE reports, calibration certificates, preservation logs, lifting records, etc., as applicable; full list TBD).
- The EPC Integrator review correspondence and review-code disposition log (file location TBD).
- The Hand-Over transmittal package and acceptance acknowledgement (format TBD).
