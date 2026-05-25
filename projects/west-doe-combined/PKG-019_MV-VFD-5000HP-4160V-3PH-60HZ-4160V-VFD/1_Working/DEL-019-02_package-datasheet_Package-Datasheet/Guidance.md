# Guidance: DEL-019-02_package-datasheet

## Purpose

`DEL-019-02_package-datasheet` is the EPC Integrator's mandatory technical handoff datasheet for `PKG-019` (MV VFD — nominal 5000 HP, 4160 V, three-phase, 60 Hz, 4160V VFD). It exists so a third-party vendor or discipline package engineering function can begin vendor-engineering work from a source-grounded basis defined by the EPC Integrator. It also carries the package's six interface facts as evidence (rather than spawning six separate deliverables).

## Principles

- Source authority before convention. The DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) is the only accessible authoritative slice for the driven-motor electrical basis, MV source bus, and VFD policy (SCA-001 VE #34, VE #37). Where the DBM is silent, the datasheet uses `TBD`.
- Workbook identity preserved verbatim. The package is referred to by its workbook name and CoA number even when the name is ambiguous (see Conflict Table below).
- Detailed VFD engineering deferred. Per DBM line 326, "VFD sizing is an electrical detailed-design item." The datasheet must not pre-empt that.
- Interface-fact carriage. The six `INTERFACE_REGISTER.csv` PKG-019 rows are evidence in the datasheet matrix; they are not separate deliverables.

## Considerations

- Two workbook rows (PKG-018 row 20, PKG-019 row 21) carry identical names and CoA tracking numbers. Until human ruling allocates motor tags (DBM identifies KM-2150 and KM-2250 as the two inlet compressors needing starting VFDs at DBM line 326), the datasheet cannot identify a unique driven tag.
- The DBM cites the driven motor as 4,000 V / 5,200 hp; the workbook package name is "5000HP, 4160V". This nameplate-vs-design mismatch is recorded as a conflict.
- Harmonic and reactive-power mitigation depends on the synchronous-bus context per SCA-001 VE #37 and on detailed electrical studies not present in accessible sources.
- The `_Sources/26020-Package_Requirements.docx` file is listed in shared sources but no PKG-019-specific slice was located in this run; this is recorded as a source gap, not as an absence of requirement.

## Trade-offs

- Recording `TBD` rather than inferring values protects vendor handoff fidelity at the cost of an incomplete datasheet. Given the deliverable's intended use (vendor handoff basis), TBD is preferable to invented values.
- Treating workbook row 21 as a distinct package (despite the row 20 duplication) preserves the decomposition's accepted identity at the cost of carrying an unresolved allocation question. Re-merging the rows must be a human decision against source-of-truth (workbook).

## Examples

- Driven-motor electrical envelope (Attributes row): cited verbatim from DBM lines 324-326 / 533 rather than reinterpreted into vendor-style specification language.
- Capacitor-bank constraint (Attributes row): captured exactly as DBM line 756 expresses SCA-001 VE #37, without extending the rule beyond MCC-8200.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-019-02-A | PKG-018 (row 20) and PKG-019 (row 21) share identical package name "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" and identical CoA `26020-02-30-009`. Allocation between the two inlet-compressor motor tags (KM-2150, KM-2250) is undefined. | `PACKAGE_REGISTER.csv` rows 20-21 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 (two starting VFDs identified) | `Datasheet.md` Identification / Attributes; `Specification.md` REQ-019-02-08 | PROPOSAL: treat PKG-019 as one of the two MV starting-VFD packages and defer specific motor-tag assignment to a human ruling that aligns workbook rows 20/21 with KM-2150/KM-2250. | TBD |
| CONF-019-02-B | Workbook package name states 5000 HP, 4160 V; accessible DBM source states the driven inlet-compressor motors are 4,000 V / 5,200 hp. | Workbook Packages row 21 (`PACKAGE_REGISTER.csv` row 21) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 | `Datasheet.md` Attributes (nameplate row); `Specification.md` REQ-019-02-09 | PROPOSAL: keep the workbook name as the package identity (decomposition authority) but cite the DBM motor electrical basis for engineering values, and request human ruling on whether the workbook name should be normalized to the DBM figures (4000 V, 5200 hp). | TBD |
| CONF-019-02-C | `26020-Package_Requirements.docx` is referenced in `_REFERENCES.md` but no PKG-019-specific section was located during this run. | `_REFERENCES.md` (shared source root); `_Sources/26020-Package_Requirements.docx` | (no matching slice located) | `Specification.md` Standards (package-requirements row); `Procedure.md` prerequisites | PROPOSAL: defer the `26020-Package_Requirements.docx` mapping to a follow-on extraction run and keep the entry as `TBD` in the datasheet. | TBD |
