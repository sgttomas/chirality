# Procedure — Vendor Engineered Equipment Package (DEL-089-04)

This procedure describes how to **produce** the vendor engineered equipment package deliverable (vendor design basis/datasheet set and supply of the physical equipment) for PKG-089 Pig Receivers (Inlet) 3-25. It is scoped to the Package Vendor with EPC Integrator integration review (DELIVERABLE_REGISTER.csv DEL-089-04; OBJ-004).

## Purpose

Produce the vendor-owned engineering deliverable for PKG-089 such that:
- Two 24 in OD pig receiver skids are supplied per source-defined configuration (SOW-0158; SOW-0159).
- Vendor design basis and datasheet set is sufficient for EPC integration review (ART-6017932F95; OBJ-004).
- All Specification.md requirements R1–R13 are met or explicitly flagged for EPC ruling.

## Prerequisites

- **Upstream deliverables available**: EPC Scope of Work (DEL-089-01) and EPC Package Datasheet (DEL-089-02). Source: DELIVERABLE_REGISTER.csv DEL-089-04 description ("...developed from the EPC package Scope of Work and Package Datasheet"). Status: TBD — sibling deliverables not yet drafted.
- **Source references read**: SCOPE_LEDGER.csv rows SOW-0157, SOW-0158, SOW-0159, SOW-0160; OBJECTIVE_REGISTER.csv OBJ-002..OBJ-010; ARTIFACT_REGISTER.csv for DEL-089-04.
- **Local references resolved**: `_REFERENCES.md` Authoritative Decomposition Basis paths (Gate 7 snapshot).
- **Project sour-service philosophy** confirmed (OBJ-009). Detail: TBD — code/standard slices not locally accessible.
- **Battery limits** acknowledged: interconnecting piping, DCS integration, foundations, electrical supply to MCC are by others (SOW-0160).

## Steps

1. **Confirm scope intake.** Read the EPC Scope of Work (DEL-089-01) and Package Datasheet (DEL-089-02) when available. Reconcile any deviations against `Datasheet.md` and `Specification.md` of this deliverable. Raise differences to the EPC Integrator before vendor design starts.

2. **Lock the configuration baseline.** Confirm: two identical 24 in OD pig receivers on dedicated non-enclosed skids; ESDV upstream of each receiver; skid-mounted isolation; sweet-gas purge downstream of manual isolation; vent to HP flare (Specification R1, R2, R8, R9, R10).

3. **Establish process design conditions.** Apply pressure envelope (125–200 psig normal; 572 psig MAOP; 125 psig low / 200 psig normal-high design; 635 psig MAWP) and temperature envelope (-40 / +35 °C design; -19 / +22.2 °C historical) from SOW-0160 (Specification R4, R5).

4. **Size for throughput.** Use 80 MMSCFD package design throughput (SOW-0160). Resolve per-receiver normal flow (TBC) with EPC Integrator before completing vendor capacity calculations (Specification R6).

5. **Select sour-service materials.** Apply project sour-service philosophy at 0.1 mol% H2S design (SOW-0159). Document MoC selection rationale and compliance basis (ASSUMPTION: NACE MR0175 / ISO 15156). Output: vendor MoC report (Specification R7).

6. **Develop vendor design basis.** Produce vendor design basis covering: receiver mechanical design (ASME Sec VIII Div 1, ASSUMPTION), skid piping (ASME B31.3, ASSUMPTION), pipeline-appurtenance considerations (CSA Z662, ASSUMPTION), pig-handling features, end-closure type, drain/kicker arrangement, purge gas tie-in, and HP-flare vent line. Output artifact: ART-6017932F95.

7. **Develop vendor datasheet set.** For each pig receiver, ESDV, isolation valve, purge tie-in, vent line, and skid structural assembly, produce a vendor datasheet (Specification R12).

8. **Produce vendor P&ID and GA drawings.** Show the ESDV-upstream, purge-downstream-of-manual-isolation, and vent-to-HP-flare arrangement (SOW-0159) consistent with Specification R8, R9, R10.

9. **Expose interface requirements.** Document each interface to the EPC scope (interconnecting piping, DCS, foundations, electrical from MCC, HP flare header) with size, location, set conditions, and signals. Required by Specification R11 and OBJ-004.

10. **Address operability/maintainability and winterization.** Document pig-handling access, ESD test access, EHT (if applicable), and winterization assumptions (OBJ-010; OBJ-005). Items not stated in source remain TBD.

11. **Fabricate and supply.** Fabricate, factory-test, and supply the two physical receiver skids consistent with the locked design (ART-AFDDE0BE60).

12. **Submit for EPC integration review.** Issue vendor design basis, datasheets, P&ID, GA drawings, and MoC report to the EPC Integrator (handoff into DEL-089-06). Track vendor document submittals via DEL-089-05.

13. **Resolve EPC review comments.** Address EPC Integrator integration comments and reissue. Vendor design closure feeds EPC Vendor Package Review and Acceptance (DEL-089-06).

## Verification

| Check | Method |
|---|---|
| Receiver count, size, mounting | Compare GA drawings against SOW-0158; SOW-0159. |
| ESDV-upstream configuration | Review vendor P&ID against SOW-0159. |
| Sweet-gas purge and HP-flare vent | Review vendor P&ID against SOW-0159. |
| Pressure rating | Code calculation review (ASSUMPTION: ASME Sec VIII / B31.3) against SOW-0160 envelope. |
| Temperature rating | Material toughness / impact requirements against -40 °C minimum (SOW-0160). |
| Sour-service compliance | MoC report and NACE compliance statement (ASSUMPTION: MR0175 / ISO 15156). |
| Throughput sizing | Sizing calculation against 80 MMSCFD; per-receiver normal flow recorded (TBD until resolved). |
| Battery-limit clarity | Interface schedule shows all "by others" items per SOW-0160. |
| Documentation completeness | Vendor design basis + datasheets present; vendor document register entries registered with DEL-089-05. |

## Records

- Vendor design basis document (artifact ART-6017932F95).
- Vendor datasheet set (receiver, ESDV, isolation valves, purge tie-in, vent line, skid structural) (ART-6017932F95).
- Vendor P&ID and GA drawings (referenced from design basis; specific document numbers TBD).
- Vendor MoC report / NACE compliance statement.
- Vendor capacity / sizing calculation.
- Interface schedule (battery-limit list with sizes, set conditions, signals).
- Factory acceptance test records and Manufacturer Data Reports (MDRs).
- Physical equipment delivery records (ART-AFDDE0BE60).
- EPC integration review correspondence log (input to DEL-089-06).

Vendor document register, submittal log, and turnover records are tracked under DEL-089-05 (not duplicated here).
