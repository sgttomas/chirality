# Guidance: DEL-039-05_vendor-document-turnover-package

## Purpose

This guidance supports preparation and review of the Vendor Document Turnover Package for `PKG-039`, the 600 V Electrical Building (850-1). The package is a Package Vendor documentation deliverable covering the vendor document register, vendor document submittals, source-required vendor documentation carried as artifacts where available, and turnover records, with EPC Integrator interface and integration review. Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05_vendor-document-turnover-package`.

The deliverable should be treated as evidence of vendor documentation completeness, not as the EPC review closeout itself. EPC review and acceptance are covered by `DEL-039-06_epc-vendor-package-review-and-acceptance`. Sources: `DELIVERABLE_REGISTER.csv` row `DEL-039-06`; `ARTIFACT_REGISTER.csv` rows `ART-3910447327`, `ART-AA4BFB86C9`, and `ART-0156F0196A`.

## Principles

1. Keep the register as the controlling index for vendor documentation. Each vendor submittal, turnover record, and source-required documentation item should be traceable to a register entry or explicitly marked `TBD` where the governing document-control basis is unavailable. Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05`.
2. Separate vendor-produced documentation from EPC review evidence. Vendor document submittals and turnover records belong in this deliverable; review comments, acceptance checklists, and factory/shop test acceptance evidence belong with `DEL-039-06`. Sources: `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv`.
3. Preserve interface coverage. `PKG-039` has applicable interface facts for Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports. The vendor document register should either identify package-side documentation for each applicable interface or record the gap as `TBD`. Sources: `PACKAGE_REGISTER.csv` row `PKG-039`; `INTERFACE_REGISTER.csv` rows for `PKG-039`.
4. Use DBM electrical-building requirements as content prompts, not as a substitute for package-specific vendor requirements. The DBM identifies building features that vendor documentation should address where applicable: climate-controlled HVAC sized as an n + 1 system, bottom-entry incoming/outgoing cables, building elevation on piles, TECK and ACIC wiring, EMT for adjacent equipment, an outdoor GFI receptacle, and doors or removable transoms sized for removal of the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section.
5. Do not invent project document-control rules. Document numbering, revision states, transmittal format, required native files, and turnover checklist fields are `TBD` until a governing project-wide vendor document control source is available. Source status: `ARTIFACT_REGISTER.csv` row `ART-A64A8A25DC`; local source gap.

## Considerations

The most important practical issue is completeness against interfaces. The electrical building is a vendor-owned package, but its vendor documentation must allow EPC integration into facility systems. The register should therefore make interface-related submittals visible: power distribution and feeder data, grounding/bonding details, communications and control cabling, fire and gas/safety-system interfaces, HVAC/service data, maintenance access provisions, and structural/foundation support information. Sources: `PACKAGE_REGISTER.csv` row `PKG-039`; `INTERFACE_REGISTER.csv` rows for `PKG-039`.

The DBM source basis is stronger for electrical-building technical features than for vendor document control mechanics. Use it to guide technical content coverage, while marking document-control mechanics as `TBD`. Sources: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section; `ARTIFACT_REGISTER.csv` row `ART-A64A8A25DC`.

The general package-deliverables paragraph in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` names vendor document registers as package deliverables, but it is written for mechanical packages. Applying that paragraph to this electrical-building vendor document set is an **ASSUMPTION** and should remain directional unless confirmed by a project-wide package documentation standard.

No upstream or downstream dependencies were declared during PREPARATION. That absence should not be interpreted as technical independence; it only means no dependency edges were declared in `_DEPENDENCIES.md`.

## Trade-offs

| Topic | Trade-off | Recommended posture |
|---|---|---|
| Register detail | A detailed register improves reviewability but may imply document-control rules that are not source-supported. | Include required topics and traceability fields where known; mark numbering, revision, and transmittal fields `TBD`. |
| Interface coverage | Listing all twelve applicable interface types may create placeholders before vendor data exists. | Keep placeholders visible so EPC review can close gaps explicitly. |
| DBM technical requirements | DBM electrical-building requirements provide useful technical coverage prompts but do not enumerate a vendor document table. | Use DBM items as review prompts for submittal coverage, not as invented document numbers or formats. |
| Turnover records | A broad turnover list supports completeness but can overclaim acceptance criteria. | Identify expected record classes and leave checklist fields/acceptance criteria `TBD` pending the governing turnover source. |

## Examples

The following are example register coverage entries, not final project document-control rows:

| Register coverage topic | Why it belongs | Source / status |
|---|---|---|
| Electrical-building HVAC data | DBM requires climate-controlled buildings with HVAC sized as n + 1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Cable-entry and cable-routing information | DBM requires bottom entry for incoming and outgoing power cables and space beneath elevated buildings for cable trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Grounding/bonding drawings or details | `PKG-039` has a grounding/bonding interface and the DBM describes plant grounding/bonding methods. | `INTERFACE_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section |
| Door/removable-transom information | DBM requires equipment doors sized for, or including removable transom sections to allow, removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section |
| Vendor document numbering/revision fields | Required format is not locally available. | `TBD`; source gap |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-039-05-01 | Detailed vendor-document requirements are expected for the turnover package, but no package-specific vendor document table or document-control standard is locally accessible. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-039-05` | `ARTIFACT_REGISTER.csv` row `ART-A64A8A25DC`; `_REFERENCES.md` Missing / Deferred References | `Datasheet.md` Attributes/Construction; `Specification.md` Requirements/Standards; `Procedure.md` Steps/Records | Treat document-control fields and package-specific mandatory document list as `TBD`; use DBM technical scope and interface registers as coverage prompts only. | TBD |
