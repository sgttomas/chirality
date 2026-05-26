# Guidance — DEL-056-05 Vendor Document Turnover Package (PKG-056 Inlet Separators 4-25)

## Purpose

The Vendor Document Turnover Package exists so that the inlet separator packages (V-1600-1, V-1700-1) can be received, installed, integrated, commissioned, operated, and maintained on the basis of a complete, traceable, certified set of vendor-authored documentation. Without a disciplined vendor document register and turnover record set, the EPC Integrator cannot close out package acceptance (`DEL-056-06`) and the Owner cannot operate the equipment safely or maintain its regulatory standing.

This deliverable is the Package Vendor's accountability surface for documentation. It is paired with the EPC Integrator's review-and-acceptance deliverable (`DEL-056-06`); together they form the documentation half of package handover. (**Source:** `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` rows for DEL-056-05 and DEL-056-06.)

## Principles

1. **The register is the system of record.** The Vendor Document Register (VDR) is the canonical index of all vendor documents. Documents that exist but are not on the VDR do not exist for turnover purposes. (Derived from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.)

2. **Source-required documents govern.** Where `26020-Package_Requirements.docx` heading 11 specifies a document, that requirement governs. Generic completeness ("we usually submit X") does not substitute for a source-required item. (**Location TBD** until heading 11 is extracted.)

3. **Vendor owns vendor documents; integrator owns interfaces.** The Package Vendor owns package engineering and documentation. The EPC Integrator reviews for integration acceptance and owns interface-quality decisions. (**Source:** `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 68.)

4. **Code and jurisdictional records are non-negotiable.** For coded HP separators (V-1600-1, V-1700-1) the ASME-stamp documentation, material test reports, NDE records, hydrotest reports, and CRN/jurisdictional certificates must be in turnover before equipment can be placed in service. (ASSUMPTION — standard regulatory pattern for HP separators in BC service.)

5. **As-built reflects reality.** Final certified drawings must match the as-installed configuration including approved deviations. Redlines without trace to certified-finals are an audit gap.

6. **Turnover is a transfer of accountability, not a courtesy package.** Receipt and acceptance of turnover records by EPC Integrator and Owner is the formal transfer point of operating responsibility for the documented equipment.

## Considerations

- **Heading 11 unknown at drafting time.** The package-specific required-document list lives in `26020-Package_Requirements.docx` heading 11 (DOCX not extracted to markdown). Until extracted, the document set in this deliverable is grounded in the cross-package baseline (DBM §Mechanical packages line 617) and standard convention. When heading 11 is available, the Datasheet and Specification shall be reconciled.

- **Quantity conflict carried.** The inlet separator quantity (two installed + plot space for a third, vs. legacy four-package references) is unresolved at the design-basis level (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 589). The VDR should be organized to accommodate a third package's documentation set if/when authorized, without restructuring.

- **Coating inspection has elevated weight.** Devchem 253 internal coating on the vessels (excluding piping) is specified (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 646). Coating-application QA records (surface prep, DFT, holiday testing) should be treated as gating turnover content, not as routine attachments.

- **Shipped-loose items are documentation hazards.** The DBM list (line 617) explicitly includes shipped-loose item lists as required content. Shipped-loose instrumentation, valves, and tie-in hardware are commonly under-documented; the VDR should track them as discrete documents.

- **Cause-and-effect inputs are an upstream consumer interface.** The vendor's cause-and-effect inputs feed the project-level cause-and-effect matrix. Late or incomplete C&E inputs from a package vendor delay system-level shutdown/ESD logic finalization (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 858 — "cause-and-effect matrix and shutdown philosophy" remains to be defined).

- **Review codes and revisions belong to the EPC, not the vendor.** The Package Vendor records the review code applied; it does not set the code system. The EPC project document control procedure governs.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Comprehensive single-issue turnover vs. rolling submittals | Rolling submittals (IFR → IFA → IFC → As-Built) give the EPC and Owner earlier visibility but require disciplined revision control; single-issue turnover is operationally simpler for the vendor but creates schedule risk at the back end. Recommendation: rolling submittals with a clearly marked final turnover gate. (ASSUMPTION) |
| Vendor-standard document numbering vs. project-aligned numbering | Vendor-standard numbering is faster for the vendor but harder for the EPC to index across the project; project-aligned numbering is more work for the vendor but simplifies multi-package coordination. Heading 11 may settle this. (TBD) |
| Paper turnover book vs. structured electronic turnover | Electronic turnover (indexed PDF/structured data) is easier to maintain over the operating life; paper-only turnover is operationally fragile. Project document control procedure governs. (TBD) |
| Vendor scope vs. integrator scope on field tie-in lists | Vendor field tie-in lists must be complete enough for EPC field-engineering; over-reach into integrator-controlled tie-in design adds rework. The boundary is the package skid edge. (Derived from `PACKAGE_REGISTER.csv` row 68.) |

## Examples

Examples are illustrative; package-specific document lists are governed by `26020-Package_Requirements.docx` heading 11 (location TBD).

- **Example VDR row:** `Doc No: 26020-PKG056-MEC-DS-001 | Title: V-1600-1 Vessel Datasheet | Rev: B | Status: Issued for Approval | EPC Review Code: TBD | Transmittal: TBD | Date: TBD | Turnover-Flag: Y` (ASSUMPTION — illustrative format pending project document-control procedure).
- **Example turnover record:** Hydrotest certificate for V-1700-1 keyed to material test reports for the shell and head courses, NDE map, and ASME U-stamp documentation, bound under one VDR row.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-056-05-01 | Package-specific required-document list is referenced but not locally extracted | `_REFERENCES.md` (cites `26020-Package_Requirements.docx` heading 11) | DBM cross-package baseline (`3-25_Comp_and_Liquids_DBM.md` line 617) | Datasheet "Construction", Specification R2 / R4 / R5 | Treat DBM line 617 list as baseline; supersede with heading 11 list once extracted | TBD |
| CONF-056-05-02 | Inlet separator quantity (2 installed + 1 future plot vs. legacy 4 packages) | `4-25_Deepcut_DBM.md` line 589 (two installed) | Legacy project references (four packages) | VDR structure; turnover record scope | Carry current basis (2 packages, V-1600-1, V-1700-1); flag VDR template to allow a third package without restructure | TBD |
| CONF-056-05-03 | DEL-056-05-specific artifact rows absent from `ARTIFACT_REGISTER.csv` GATE-07 snapshot | `ARTIFACT_REGISTER.csv` (no DEL-056-05 rows) | `_CONTEXT.md` Anticipated Artifacts list | Specification R4.2 | Add artifact rows when heading 11 is extracted and source-required documents are enumerated | TBD |
