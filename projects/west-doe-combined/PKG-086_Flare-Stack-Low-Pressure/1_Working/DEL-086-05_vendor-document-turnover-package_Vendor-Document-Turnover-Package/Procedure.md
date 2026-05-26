# Procedure: DEL-086-05_vendor-document-turnover-package — Vendor Document Turnover Package

> Operational procedure for producing and turning over the Package Vendor's document set for PKG-086 (Flare Stack — Low Pressure). The procedure describes steps to **produce** the vendor document register, submittals, source-required vendor documentation, and turnover records, and to support EPC Integrator review through to acceptance handoff (consumed by DEL-086-06). Source-anchored steps cite the relevant register row or DBM slice; inferred steps are labeled `ASSUMPTION` and unresolved details are `TBD`.

## Prerequisites

- Accepted upstream decomposition snapshot available: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` (`_REFERENCES.md`).
- DEL-086-01 EPC Scope of Work (defines vendor responsibility scope) — sibling deliverable.
- DEL-086-02 Package Datasheet (defines vendor technical handoff content) — sibling deliverable.
- Locally accessible reference: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (flare design basis context).
- Source-required vendor document list extracted from `26020-Package_Requirements.docx` package heading 39 — currently `TBD` (source slice not yet copied locally).
- Confirmed sour-service designation for PKG-086 — currently `ASSUMPTION: likely applies` (OBJ-009).
- Package Vendor identification and contract package number — TBD (`location TBD`).
- EPC Integrator review channel and log location (DEL-086-06) — TBD for exact convention.

## Steps

1. **Initialize vendor document register.**
   - Create a single master register that uniquely indexes every vendor-issued document for PKG-086 with at minimum: document number, revision, date, vendor identity, EPC contract/package reference, status, and hold-item flag. (R-086-05-01, R-086-05-12)
   - Register schema details are `ASSUMPTION` pending facility document convention (`location TBD`).

2. **Extract source-required document list.**
   - Open `26020-Package_Requirements.docx` package heading 39 and enumerate every vendor document the source requires for PKG-086. Populate corresponding rows in the register marked `source-required: YES`. (R-086-05-02)
   - This step is currently blocked at the source-slice level — flag as `TBD` until the slice is copied locally.

3. **Add equipment-scope rows.**
   - For each equipment item in SOW-0093 (LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, stack interface details), add the expected vendor documents (datasheet, GA drawing, calculation set, MTRs, ITP/ITR, O&M manual, spare parts list). Mark category origin as `equipment-scope`. (R-086-05-03, R-086-05-04)

4. **Add regulatory/criteria-driven rows.**
   - Add vendor calculation entries for thermal-radiation flux verification against <=9 kW/m2 (inside boundary) and <=5 kW/m2 (outside boundary), citing OGPFR Appendix 1, Schedule 1, Sec. 2 as the governing regulation; note that the DBM identifies this as an external regulation requiring vendor verification. (R-086-05-05; `4-25_Deepcut_DBM.md` lines 285-289)
   - Add vendor reconciliation note tying vendor stack/radiation outputs to the OGAOM Sec. 9.6.15 spacing applied at the facility plot. (R-086-05-06)
   - Add vendor smokeless capacity submittal entry targeting Ringelmann 1 at approximately 5% (TBC) of emergency design case flare loads and supplemental fuel gas LHV >=20 MJ/Sm3. (R-086-05-07; DBM lines 2031-2033)
   - Add LP flare pilot and purge gas datasheet entry to close the DBM `TBC` (line 1892). (R-086-05-08)

5. **Confirm sour-service material documentation.**
   - Request vendor material statements (NACE MR0175 / ISO 15156 conformance, where applicable) for SA-106 LP flare stack and other components. Note current sour-service designation is `ASSUMPTION` pending confirmation (OBJ-009). (R-086-05-04, R-086-05-11)

6. **Issue vendor submittals against the register.**
   - For each register row, the Package Vendor issues the document at the contracted revision state. Update register status (`for review`, `revised`, `approved`, `hold`).
   - Routing to EPC Integrator review uses the channel/log convention referenced by DEL-086-06 — `TBD` for exact convention.

7. **Support EPC Integrator interface/integration review.**
   - Respond to EPC review comments by reissuing affected documents and updating the register revision and status fields. (R-086-05-09)
   - EPC review evidence is captured in DEL-086-06, not in this deliverable.

8. **Compile turnover records.**
   - At handover, generate the turnover transmittal listing every register row, revision-at-handover, outstanding hold items, and EPC acceptance signature. (R-086-05-10)
   - Include the closed register snapshot, vendor submittal set, source-required documentation set, MTRs, calculations, ITRs, and manuals as bundled turnover content.

9. **Hand off to EPC Integrator and end client.**
   - Transmit the turnover bundle to the EPC Integrator and end client per the project document-management convention (`TBD` — `location TBD`).
   - Record transmittal acknowledgments in the turnover record.

## Verification

| Step | Verification |
|---|---|
| 1 | Register exists, indexes every issued document, and supports the metadata fields in R-086-05-12. |
| 2 | Every row in the source-required list from 26020 heading 39 has a register entry with `source-required: YES`. (Verification pending source-slice access.) |
| 3 | Every SOW-0093 equipment item is covered by at least one document of each expected category in the register. |
| 4 | Vendor calculations exist, are reviewed against the DBM-cited regulatory limits, and the OGPFR external-reference note is acknowledged. |
| 5 | Sour-service material statements present where the service is confirmed sour; flagged conditional where designation is still `ASSUMPTION`. |
| 6 | Every register row has a current submittal status and revision; no rows in `for review` past the contracted review cycle. |
| 7 | Every EPC review comment has a vendor response, document re-issue, and updated register status. |
| 8 | Turnover transmittal lists every register row with revision-at-handover and a hold-item disposition; acceptance signatures present. |
| 9 | Transmittal acknowledgment from EPC Integrator and end client present in the turnover record. |

## Records

- Vendor document register (final closed snapshot at turnover)
- Vendor document submittals (full set, at turnover revision)
- Source-required vendor documentation set (per 26020 heading 39 — `location TBD` until source slice copied)
- Material certifications (MTRs) for SA-106 LP flare stack and components
- Vendor calculation set (radiation, dispersion, structural, smokeless capacity)
- Inspection and test plans / records (ITPs/ITRs)
- Operating and maintenance manuals
- Spare parts list
- Turnover transmittal records (with revision-at-handover and outstanding hold items)
- EPC and end-client transmittal acknowledgments
