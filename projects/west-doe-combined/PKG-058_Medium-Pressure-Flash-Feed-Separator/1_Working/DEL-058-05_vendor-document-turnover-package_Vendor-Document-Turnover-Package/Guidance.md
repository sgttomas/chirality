# Guidance — DEL-058-05 Vendor Document Turnover Package (PKG-058)

## Purpose

This guidance frames how the Vendor Document Turnover Package is to be assembled, interpreted, and reviewed for PKG-058 (Medium Pressure Flash Feed Separator, MPFF). It supports `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (recorded as ASSUMPTION via the package-grouping heuristic) by ensuring the EPC Integrator receives a complete, traceable vendor documentation set sufficient for facility integration, operations, and regulatory readiness for an MPFF pressure-equipment package.

## Principles

1. **Source-driven document list.** The applicable document classes come from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables". This deliverable does not invent new document classes for the PKG-058 turnover.
2. **Discipline filtering, not document invention.** The vendor and EPC reviewer apply the source's discipline tables to mark each line APPLICABLE / N/A with rationale, rather than removing or re-inventing IDs.
3. **EPC Integrator as acceptor, not author.** Per `_CONTEXT.md` and the Gate 7 register, the Package Vendor authors; the EPC Integrator reviews and accepts via `DEL-058-06`. Acceptance is a human decision.
4. **Traceability over volume.** The Vendor Document Index (`PRQ-009`) is the canonical contents list; every document submitted must appear in it with current revision and status.
5. **Codes and standards stay sourced.** Where the accessible source set does not cite a specific clause, the turnover set states the applicable standard and leaves clause-level claims to detailed-design documents.
6. **Process-basis fidelity.** The DBM-cited MPFF basis (overheads to SOC third-stage suction, automated blowdown valve, Mistex internals, no internal coating, self-framing building enclosure, methanol injection on feed) is a baseline against which vendor documentation is read.

## Considerations

- **Mechanical discipline center.** PKG-058 is identified Mechanical (`_CONTEXT.md`). Mechanical, pressure-equipment, piping, and I&C document classes dominate the applicable list; electrical applies as enclosure/instrumentation scope rather than power transmission.
- **Pressure-equipment registration.** Cold-climate Canadian sites typically require jurisdictional pressure-vessel registration (e.g., ABSA in Alberta). The vendor documentation set must include the manufacturer's data report or jurisdictional equivalent and the design calculations supporting it. ASSUMPTION pending detailed-design confirmation.
- **Mist eliminator vendor-named.** The DBM explicitly names Mistex internals (DBM line 672). The vendor documentation set must include the internals datasheet, demister selection rationale, and any sizing/de-entrainment calculations that justify the named selection or any equivalent substitution.
- **Internal coating disposition.** DBM line 672 states no internal coating is specified for the MPFF (contrast with the inlet separator and stabilizer flash/feed which carry Devchem 253). The vendor documentation set should explicitly confirm the no-coating disposition or flag any deviation.
- **Hydrate suppression.** DBM line 674 retains methanol injection upstream of the MPFF inlet level/pressure control valve as a safeguard pending confirmation of upstream HEX outlet temperatures. The vendor I&C documentation must reflect methanol-injection tie-ins.
- **Building enclosure.** DBM line 672 calls for a self-framing building enclosing instrumentation and one end of the vessel. Electrical, lighting, EHT, and grounding documentation should be scoped to that enclosure rather than a full process building.
- **Turnover gate.** Turnover records (`PRQ-016`, `MEC-023`, `QLT-020`, `QLT-021`, mechanical FAT, hydrotest, NDE) are the critical evidence for `DEL-058-06` acceptance. Plan the FAT milestones backwards from the EPC Integrator's acceptance gate.
- **Interface basis with adjacent packages.** Upstream interface is the inlet-separator liquid outlet (heater outlet) feeding through level control; downstream interfaces include SOC third-stage suction (overhead vapour) and the LP flash/feed system (liquid). Skid-edge piping and instrumentation documentation must record these tie points.

## Trade-offs

- **Breadth vs. signal.** A wide vendor document set is more defensible at regulatory and operational reviews but increases review cost and submittal turnaround. Use the discipline applicability call to keep the set tight while preserving traceability.
- **Early submittal vs. as-built quality.** Releasing documents early helps the EPC Integrator coordinate facility-level integration but creates revisioning churn. The Vendor Document Control Procedure (`DOC-008`) should establish a small number of named milestones (preliminary, certified-for-construction, as-built).
- **Standalone vendor IOM vs. integrated turnover book.** A combined `PRQ-016` book is easier for operations to use long-term; per-document standalone files are easier for vendor revisioning. Decide upfront and reflect in `DOC-008`.
- **Combined MPFF train documentation.** DBM line 658 ("All MPFF flow values are per MPFF separator") implies multiple MPFF trains. Vendor documentation may be issued either per-train or as a single set covering identical units; the index must make the choice traceable.

## Examples

- The source's compressor and inlet-separator sections in `26020-Package_Requirements.docx` illustrate how the same Vendor Engineering Deliverables template is instantiated for different physical packages, with the same core vendor documents and discipline applicability table. The MPFF instantiation follows the same shape with mechanical-led applicability filtering.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 264 discusses drive-gas pressure set above the 04-25 stabilizer flash feed separator pressure — confirming MPFF/stabilizer-flash-feed as first-class systems in the facility design basis whose turnover packages are expected.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-058-05-001 | Number of MPFF trains is not unambiguous in accessible sources. DBM line 658 states flows are "per MPFF separator" and lines 672 reference "V-7110-1 and V-7310-1" overheads, suggesting two trains; the inlet-separator-quantity dispute referenced in DBM line 668 may also implicate MPFF count. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 658, 672 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 668 (legacy "4 vessels" reference for upstream chain) | Datasheet Construction; Specification R-4; Procedure scope per train | Issue vendor documentation per-train with a single common index covering all MPFF trains. Confirm train count in `DEL-058-02` package datasheet before vendor PO. | TBD |
| HRR-058-05-002 | Specific pressure-vessel and piping codes (e.g., ASME BPVC Sec. VIII Div. 1, ASME B31.3) and Canadian jurisdictional registration (e.g., ABSA) are not explicitly cited in the accessible source slices. | `_Sources/26020-Package_Requirements.docx` (no explicit code citation in accessible slices for MPFF) | None | Specification R-4, R-13; Standards table | Carry as ASSUMPTION; require the EPC Integrator to confirm governing codes and jurisdictional registration in the package PO or `DEL-058-06` review criteria before vendor mobilization. | TBD |
| HRR-058-05-003 | Submittal cadence and native-file formats are not stated in accessible source slices. | `_Sources/26020-Package_Requirements.docx` (no explicit cadence) | None | Specification R-14 | Carry as TBD; specify in package PO. | TBD |
| HRR-058-05-004 | The objective set `OBJ-001`, `OBJ-004`–`OBJ-010` is associated to this deliverable via the package-grouping heuristic; the explicit objective-to-deliverable map may differ. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (not opened in Pass 1; opens in Pass 2/3) | Datasheet Identification; Guidance Purpose | Treat the listed objectives as directionally relevant context (ASSUMPTION). Confirm during `DEL-058-06` or via a coordination ruling. | TBD |
| HRR-058-05-005 | Vendor Engineering Deliverables per-line ID list for piping, structural, and civil scopes was not enumerated in detail at draft time (sources are binary `.docx` slices). | `_Sources/26020-Package_Requirements.docx` package heading 13 | Drafted IDs (MEC, INS, ELE) carried by parallel siblings | Datasheet Construction; Specification R-7 | Re-read source slice at production time and populate per-line IDs; flag any deviations from the sibling pattern. | TBD |
