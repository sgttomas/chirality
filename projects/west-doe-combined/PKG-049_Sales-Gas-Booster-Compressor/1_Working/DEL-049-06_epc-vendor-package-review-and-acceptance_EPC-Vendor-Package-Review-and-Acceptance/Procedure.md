# Procedure — DEL-049-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure for the EPC Integrator to review the Package Vendor's Sales Gas Booster Compressor (PKG-049) submittals, witness/review test and inspection evidence, and accept the package for facility integration handoff.

## Prerequisites

- Authoritative inputs available:
  - EPC Scope of Work for PKG-049 (TBD — specific document location not in accessible sources)
  - Package Datasheet (DEL-049-02) — INITIALIZED or later
  - Construction Work Package (DEL-049-03) — INITIALIZED or later
  - Vendor Engineered Equipment Package submittals (DEL-049-04)
  - Vendor Document Turnover Package (DEL-049-05)
- Project standards references: API 661 (air coolers); NEMA MG 1 (motors); other governing project specs (TBD).
- Review workflow tooling (document management system) in place.
- ASSUMPTION: No upstream dependencies were declared during PREPARATION (`_DEPENDENCIES.md`). DEL-049-02, -03, -04, -05 are inferred prerequisites from package topology.

## Steps

1. **Initialize review log (ART-A1F5908C64).**
   - Establish review log with columns: Submittal ID, Submittal Title, Vendor Rev, Reviewer, Date Issued, Comments, Disposition (Accept / Accept with Comment / Reject), Re-submittal Required, Closed Date.

2. **Receive and register vendor submittals (DEL-049-04, DEL-049-05).**
   - For each submittal: assign Submittal ID, record vendor revision, enter into review log.

3. **Conformance review against SOW item list (REQ-049-06-02 to -05).**
   - Verify equipment list matches SOW-0171 (Ariel KBX/X; 8-pole motor; API 661 air cooler; scrubbers; packing vent/drain pot; seal-pot pump; 0.3 micron / 99.97% / 100 MMSCFD filter coalescer with QOC).
   - Verify design conditions match SOW-0172 (140 MMSCFD; 6137/12866 kPag suction/discharge design pressures; 110 F inlet summer; 0.61 SG liquid density assumption).
   - Verify driver characteristics match SOW-0172 (8-pole, 1000 kW, 4000V/3PH/60Hz, 891 rpm fixed; TEFC/WPII; NEMA MG 1).
   - Record disposition in review log; raise holds for non-conformance.

4. **Interface-boundary verification (REQ-049-06-08).**
   - Walk vendor scope drawings and terminal-point list against EPC by-others list from SOW-0172 (shipping, piles, tie-in piping, electrical connections, mounting platform/stairs).
   - Resolve any scope overlaps or gaps before acceptance.

5. **Standards-compliance review.**
   - Request vendor declarations of compliance for API 661 (air cooler) and NEMA MG 1 (motor).
   - For other project specs: confirm against governing references (TBD — locations not in accessible sources).

6. **Factory/shop test and inspection review (REQ-049-06-06, ART-F7E6330088).**
   - Witness or document-review FAT per the criticality assigned to each test.
   - Verify performance test results against design conditions (Step 3).
   - File records in test evidence package.

7. **Resolve open comments and holds.**
   - Track each hold to closure with documented vendor response and re-submittal.
   - Disposition any unresolved items via the Conflict Table in `Guidance.md` (e.g., C-049-06-01 coalescer rating).

8. **Complete acceptance and turnover checklist (REQ-049-06-07, ART-6439AA1852).**
   - Confirm: all required submittals received and dispositioned; conformance verified; interface boundary verified; FAT accepted; holds closed.
   - Obtain EPC Integrator acceptance sign-off.
   - ASSUMPTION: human authorization is required for final acceptance signature (per K-AUTH-1); agent activity is proposal/evidence only.

9. **Assemble turnover evidence package.**
   - Collate review log, conformance evidence, interface verification, test evidence, and signed acceptance checklist.
   - Transfer to commissioning custody per project handoff procedure (TBD — specific procedure not in accessible sources).

## Verification

- Review log shows every vendor submittal entered and dispositioned to closure.
- All SOW-0171 / SOW-0172 attributes have a matched entry in the conformance section of the acceptance checklist.
- Interface verification confirms no overlap or gap against the EPC by-others list.
- All holds are closed; all unresolved items are captured in the Conflict Table.
- Acceptance checklist is signed by the responsible EPC Integrator authority.
- Turnover evidence package is complete and indexed.

## Records

- Vendor document review and comment log (ART-A1F5908C64)
- Package acceptance and turnover checklist (ART-6439AA1852) — signed
- Factory/shop test and inspection evidence file (ART-F7E6330088)
- Turnover evidence package (assembled in Step 9)
- Conflict Table entries with human rulings (in `Guidance.md`)
