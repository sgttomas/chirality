# Procedure — DEL-083-04 Vendor Engineered Equipment Package (Inlet Separators 3-25)

This procedure covers vendor execution to **produce** the engineered equipment package for V-1600-2 and V-1700-2.

## Prerequisites

- EPC Scope of Work (`DEL-083-01`) issued for vendor use — **ASSUMPTION**: declared upstream (not yet in `_DEPENDENCIES.md`).
- EPC Package Datasheet (`DEL-083-02`) issued for vendor use — **ASSUMPTION**: declared upstream.
- Locally accessible source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Decomposition reference: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- EPC-vendor interface protocol established (engineering query channel for `TBD/TBC` items).
- Material and coating availability confirmed (Devchem 253 supply).
- Vendor QMS, ASME/NACE compliance, and FAT facility accessible.

## Steps

1. **Receive and review EPC inputs.** Confirm receipt of EPC Scope of Work and Package Datasheet. Log all stated requirements and all `TBD/TBC` items.
2. **Establish vendor design basis (PDB).** Reproduce the 03-25 inlet-separation basis (40 MMSCFD per package gas, 556 m3/d condensate, 1,800 m3/d produced water, ANSI 600#, 4,963 kPag, ~38 m3 slug volume). Cite DBM `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Inlet Separation.
3. **Resolve open items via engineering queries.** Submit queries for: pig receiver size (DBM line 230 — interface only), normal high operating pressure (line 258), inlet design temperature reconciliation (line 258), building extent (line 260), methanol downstream disposition (line 218), and the `2 x 50%` vs `2 x 100%` sparing reconciliation (line 570).
4. **Mechanical design.** Size vessels (D 2,743 mm, T/T 12,191 mm), select head type and supports, apply sour-service material selection, set corrosion allowance, locate manways and inspection ports, and confirm internals removal clearances per DBM line 611.
5. **Internals design.** Design manually adjustable weir, vertical/horizontal high-performance mesh/vane mist eliminators, and de-sanding provisions per DBM line 260. Specify Devchem 253 coating per lines 256, 611.
6. **Controls and valves.** Specify ≥ 2 parallel inlet PCVs (balanced globe, hardened trim, ΔP ≤ 5 psid) and ≥ 2 parallel produced-water LCVs per package per DBM line 266. Provide ESDV per 635 psig setpoint at the inlet separator (line 230).
7. **Drains and boots.** Design separator boot to accommodate infrequent methanol drainage per line 218.
8. **Package layout and skid.** Develop skid GA, instrument-air, electrical, and piping interfaces. Provide heated self-framing building enclosing instrumentation and one end of each package; defer final extent until EPC closes the `TBD` per line 260.
9. **Issue vendor datasheets and drawings for EPC review.** Submit equipment datasheets, GAs, P&IDs, internals drawings, coating spec, and control-valve datasheets. Update on EPC review comments (feeds `DEL-083-06`).
10. **Procurement and fabrication.** Procure long-lead items; fabricate vessels and skids; apply Devchem 253 internal coating; perform welding NDE and PWHT per code requirements.
11. **Factory Acceptance Test (FAT).** Execute hydrotest, dimensional verification, internals inspection, coating inspection, control-loop checks, and ESDV setpoint verification. Capture records.
12. **Issue vendor turnover dossier.** Provide MTRs, U1A forms, hydrotest reports, NDE records, coating inspection reports, FAT report, and as-built drawings to feed `DEL-083-05` (Vendor Document Turnover Package).
13. **Ship and field support.** Ship packages and provide vendor field engineering support for installation, tie-in, and commissioning under `DEL-083-03` (Construction Work Package).

## Verification

| Check | Method | Records |
|---|---|---|
| Capacity per package = 40 MMSCFD gas, 556 m3/d condensate, 1,800 m3/d water | Vendor design calculations vs DBM | PDB, vendor datasheet |
| Vessel D 2,743 mm × T/T 12,191 mm, ANSI 600#, MAWP per 4,963 kPag | Mechanical drawings, hydrotest | GA drawing, U1A, hydrotest report |
| Slug volume ~38 m3 | Volumetric calculation from internals layout | PDB |
| Internal coating Devchem 253 applied per spec | Coating inspection | Coating inspection report |
| Internals present (weir, mist eliminators, de-sanding) | Visual inspection at FAT | FAT report |
| ESDV shutdown 635 psig | Setpoint verification | Instrument-loop record |
| Inlet PCVs ≥ 2 parallel, balanced globe, ΔP ≤ 5 psid | Valve datasheet review | Valve datasheets, FAT |
| Produced-water LCVs ≥ 2 parallel | Valve datasheet review | Valve datasheets, FAT |
| Sour-service compliance | MTR review, NACE certificate | MTR, NACE compliance dossier |
| Building heating capacity sufficient for site low ambient | Vendor calculation | Building GA + heating calc |

## Records

- Vendor Package Design Basis (PDB)
- Equipment datasheets for V-1600-2 and V-1700-2
- Mechanical GAs, P&IDs, PFDs, internals drawings
- Control valve datasheets, ESDV datasheet, instrument index
- Coating specification and inspection reports (Devchem 253)
- MTRs, U1A forms, hydrotest reports, NDE records, PWHT records
- FAT plan and FAT report
- Building GA and heating-capacity calculation
- Engineering query log (with EPC responses for `TBD/TBC` items)
- Final as-built vendor document set feeding `DEL-083-05` turnover and `DEL-083-06` acceptance
