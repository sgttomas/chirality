# Guidance — DEL-041-01 Scope of Work (PKG-041, 490-1 Standby Generator Building)

## Purpose

DEL-041-01 is the mandatory EPC Integrator Gate 5 anchor deliverable for PKG-041. It captures the full package scope, including tagged equipment, package function, source basis, boundaries, and the whole-facility integration narrative for the standby generator package (workbook title: "13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1)"; design-basis identity: Module 490-1 Emergency Generator Module). It is the upstream anchor for the package datasheet (DEL-041-02), the construction work package (DEL-041-03), and the EPC vendor package review and acceptance deliverable (DEL-041-06). (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv rows 228-233.)

## Principles

1. **Source-of-truth precedence.** When the workbook package title and the design basis disagree, the design basis (DBM-Deepcut/4-25_Deepcut_DBM.md) governs the technical description, and the workbook title is preserved only as the package identifier. The Scope of Work shall not silently reconcile the two — it shall name both and route the discrepancy to the Conflict Table for human ruling. (DBM "Emergency Power Generation Basis"; PACKAGE_REGISTER.csv row 43.)
2. **Ownership split is the spine of the SOW.** Package Vendor owns engineering, design, vendor documentation, and the physical equipment package. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. The SOW must make this split explicit at the interface line-item level. (PACKAGE_REGISTER.csv row 43.)
3. **Open items are first-class content.** Sizing, fuel selection, transfer mode, paralleling, battery/charger sizing, diesel storage sizing, switchgear assignment, and lift provisions are TBD per DBM. The SOW shall surface these as named open items with their conditional owner (MLE, EPC, electrical studies), not as silent assumptions. (DBM "Standby generator integration" item; "Emergency Power Generation Basis" table.)
4. **Interface set is the contract surface.** All twelve interfaces enumerated in PACKAGE_REGISTER.csv row 43 are part of the EPC Integrator scope and must be represented in the SOW interface table; the package datasheet (DEL-041-02) will carry the detailed interface requirements matrix.

## Considerations

- **Module identity:** The vendor module label "490-1 Emergency Generator Module" appears in the DBM Module Assembly table (Shop assembly, part of vendor package). The workbook title uses the same "490-1" suffix. Treat the two labels as referring to the same physical package unless a human ruling separates them. (DBM Module Assembly table; PACKAGE_REGISTER.csv row 43.)
- **Tagged equipment basis:** The DBM Tagged Equipment table (row 69, "Standby Generator", 4 tags) lists AC-4910-1, EGD-4950-1, EG-4950-1, ACM-4910-1. These are the only tags currently attributable to the package from accessible sources. Additional tags shall not be assumed.
- **Load coverage:** Both 04-25 and 03-25 critical loads are served via transfer switch at the 600 V MCC level. The SOW shall not conflate this with a single-unit cross-tie; the DBM language is "transfer switches at the 600 V MCC level" (plural), but DBM also references a single "Standby Generator" row in the tag list. Whether one or multiple physical generator sets are required is TBD. (DBM "Standby Power"; "Standby generator integration" item.)
- **Fuel constraint propagation:** If the natural-gas fuel option is selected, the 66 psig regulation requirement upstream of the enclosure becomes an interface obligation on the utility piping interface (one of the twelve interfaces in PACKAGE_REGISTER.csv row 43). (DBM "Emergency Power Generation Basis" table.)
- **Objectives mapping:** OBJ-001, OBJ-004-010 are recorded in `_CONTEXT.md` and PACKAGE_REGISTER.csv row 43 as supported objectives. Per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`, this association is recorded as ASSUMPTION (best-effort mapping) until the OBJECTIVE_DELIVERABLE_MAP confirms deliverable-ID granularity.

## Trade-offs

- **Natural gas vs diesel fuel:** Natural gas reduces on-site liquid storage and spill/containment risk but imposes a fuel-gas regulation requirement (<66 psig) and exposes standby capability to gas-supply availability. Diesel adds storage and day-tank scope, secondary containment, and operational refueling but is independent of process gas supply. Fuel selection is TBD by MLE. (DBM "Emergency Power Generation Basis" table.)
- **Automatic vs manual transfer:** Automatic transfer minimizes operator action and outage duration; manual transfer simplifies controls and reduces inadvertent-paralleling risk. Transfer mode is TBD pending electrical studies. (DBM "Standby generator integration" item.)
- **Single vs multiple generator sets:** A single shared set simplifies maintenance and shop-assembly. Multiple sets per facility (04-25, 03-25) reduce common-mode failure exposure and may simplify transfer-switch layout. Quantity is TBD. (DBM "Standby Power".)

## Examples

TBD — no narrative examples are present in the accessible source slices. Examples should be added once package datasheet (DEL-041-02) and construction work package (DEL-041-03) drafts exist, or when a vendor reference module is selected.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Package title states 13.8 kV / 3.0 MW; current design basis states LV (480 V or 600 V class) TOU standby generator on LV MCC with transfer switch, and explicitly eliminates the 13.8 kV tie-in. | PACKAGE_REGISTER.csv row 43 (and DELIVERABLE_REGISTER.csv row 228 by inheritance); workbook Packages row 43 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — "Emergency Power Generation Basis" table ("13.8 kV tie-in eliminated"; "Low voltage, 480 V or 600 V class"); "Standby Power" ("replacing the prior centralized 13.8 kV emergency-generator concept") | Datasheet.md (Attributes — voltage, capacity); Specification.md (Scope, R-041-01-03, R-041-01-04, R-041-01-11); Guidance.md (Principles 1); Procedure.md (Verification step) | DBM-Deepcut design basis governs the technical description; workbook title retained as the package identifier only. The "3.0 MW" rating is unsupported by accessible sources and should be marked TBD until either the DBM revision restores it or a sizing study sets it. | TBD |
| CT-002 | Number of generator sets — DBM "Standby Power" uses plural "transfer switches at the 600 V MCC level" implying potentially multiple sets, while DBM Tagged Equipment table lists a single "Standby Generator" row (4 tags). | DBM "Standby Power" | DBM Tagged Equipment table row 69 | Datasheet.md (Attributes — tagged equipment); Specification.md (R-041-01-05); Guidance.md (Considerations) | Treat as a single shop-assembled module 490-1 until electrical study confirms otherwise; surface as TBD open item. | TBD |
