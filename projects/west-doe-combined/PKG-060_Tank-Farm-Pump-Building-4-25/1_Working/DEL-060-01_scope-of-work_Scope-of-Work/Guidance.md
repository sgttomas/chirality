# Guidance — DEL-060-01 Scope of Work (PKG-060 Tank Farm Pump Building 4-25)

> Directional guidance for authors and reviewers of the EPC Integrator Scope of Work for PKG-060. Guidance is rationale-only and not normative; see `Specification.md` for normative requirements.

## Purpose

This deliverable exists because PKG-060 (Tank Farm Pump Building 4-25) is a Mandatory Gate 5 EPC anchor deliverable defined by user instruction (`_CONTEXT.md` Notes). The Scope of Work is the EPC Integrator's package-level scope statement — it routes the workbook row 85 package and the 26020-Package_Requirements.docx heading 15 source material into a coherent statement that:

- declares package identity and the EPC/Package-Vendor responsibility split (OBJ-004),
- enumerates the tagged in-package equipment and the package's process function inside the 04-25 facility (OBJ-001, OBJ-003),
- exposes the applicable interfaces so downstream packages (electrical, controls, civil/structural, utilities) can plan integration (OBJ-005..008),
- preserves sour-service safety and operability requirements at package level (OBJ-009, OBJ-010), and
- anchors the four sibling deliverables in PKG-060 (Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance).

## Principles

1. **Vendor scope is vendor scope.** The Scope of Work shall not author vendor package engineering or design content. OBJ-004 and PACKAGE_REGISTER ResponsibilityModel are explicit: Package Vendor owns engineering/design/equipment, EPC Integrator owns integration/interfaces. Where the source basis says "vendor to design" (process water pumps, fresh caustic pumps), the Scope of Work shall preserve that language and not pre-specify vendor design choices.

2. **The four sibling deliverables consume this document.** The Scope of Work is the upstream of DEL-060-02..06. Keep the Scope of Work disciplined about scope-only content — push datasheet detail into DEL-060-02, construction sequence into DEL-060-03, vendor engineering into DEL-060-04, document turnover into DEL-060-05, and EPC review into DEL-060-06.

3. **Source authority hierarchy.** When the workbook row, the package requirements heading, and the 4-25 DBM are all available, the package requirements heading governs package scope, the workbook row governs package identity, and the DBM governs facility-context narrative. The bid doc (`26020-01-PT-RFQ-18-002`) is the most detailed but is not locally accessible — content sourced solely from it must be marked `TBD` until the bid doc is brought into scope.

4. **Whole-facility integration is the EPC differentiator.** The package vendor produces the pumps and the building; the EPC Integrator places them in the 04-25 facility and ties them to the 03-25 Liquids Hub. Condensate transfer to 3-25, produced water transfer to 3-25, and shared electrical/MCC infrastructure are the integration story; the Scope of Work must say so explicitly.

## Considerations

### Sour-service and -40 deg C cold-start

The pumps are in sour condensate / sour produced-water service at a facility designed for -40 deg C cold-start (DBM SEC-01; SOW-0192). The Scope of Work should flag, at scope level:

- Motor sizing at -40 deg C startup for inlet stabilizer composition density (SOW-0192; DBM line 1679).
- Sour-service materials (e.g., no aluminium for caustic service per SOW-0191; sour-service implications for condensate transfer pump materials are TBC in the source basis).
- EHT and freeze-protection of pump auxiliaries (interface row "EHT" is in scope for PKG-060).

### NPSH and tank elevation

DBM-Deepcut (line 1677) states: design NPSHR at design flow shall be no greater than 0.75 m because condensate tanks are not elevated; if exceeded, a condensate booster pump plus a downstream transfer pump may be required. The Scope of Work should flag this as a vendor-design constraint and an EPC tank-farm layout interface to PKG (tanks).

### Interface coverage

PKG-060 carries 14 interface types (INTERFACE_REGISTER). Notably:

- Building HVAC / Services is an interface — the self-framing building requires HVAC scope coordination (likely an EPC scope item, not a package-vendor scope item).
- Fire & Gas / Safety Systems is an interface — the building is a hydrocarbon-handling enclosure and falls inside the facility F&G envelope.
- Grading / Site Drainage / Spill Containment is **not** listed for PKG-060 in INTERFACE_REGISTER, although it is listed for sibling PKG-091 (3-25 sister package). Authors should flag this asymmetry as a TBD for human ruling rather than silently importing the interface.

### Naming discrepancy (DBM vs workbook)

The decomposition uses "Tank Farm Pump Building 4-25" (workbook row 85). The 4-25 DBM Process Units table (line 2555) refers to the same physical building as "Tank Farm Pump Building 2". The Scope of Work should adopt the decomposition name as primary and note the DBM name as an alias.

## Trade-offs

- **Scope-only vs detail.** Tempting to include datasheet-style pump performance details, but those belong in DEL-060-02 Package Datasheet. Keep the Scope of Work to identity, function, capacity headlines, interfaces, and boundaries.
- **Bid-doc fidelity vs `TBD`.** Where source detail exists only in the inaccessible bid doc, use `TBD (source: 26020-01-PT-RFQ-18-002, not locally accessible)` rather than inventing or paraphrasing.
- **"By others" clarity.** Foundations, DCS integration, and MCC electrical supply are explicit "by others" per SOW-0192. Keep these visible to prevent EPC/vendor scope creep in either direction.

## Examples

- Example responsibility statement (drawn from PACKAGE_REGISTER ResponsibilityModel): "Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration."
- Example integration narrative seed (drawn from DBM-Deepcut SEC-05 line 452 and SEC-06 line 504): "Stabilized C5+ condensate is pumped to the 3-25 Liquids Hub via the condensate transfer pumps housed in this building. Produced water is pumped via a new water pipeline to the 3-25 Liquids Hub; trucking is reserved for emergency cases."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none at draft time) | No source-to-source conflicts detected between accessible sources during Pass 1 / Pass 2. | — | — | — | — | TBD |

NOTE: One asymmetry was noted but is not a source conflict — the omission of "Grading / Site Drainage / Spill Containment" from PKG-060 INTERFACE_REGISTER while it is present for sibling PKG-091. This is flagged in `Specification.md` REQ-SOW-060-01-009 NOTE and in this Guidance as a `TBD` rather than as a Conflict Table entry.
