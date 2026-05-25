# Guidance: DEL-029-01 Scope of Work

## Purpose

PKG-029 (`Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V`) is a vendor-owned Electrical package in WBS 01 of the 04-25 Deepcut facility scope. The EPC Scope of Work deliverable exists to fix the package identity, articulate the package function within the facility electrical distribution architecture, list the source-supported interfaces, and define the responsibility split before downstream production deliverables (Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, and EPC Vendor Package Review and Acceptance) are produced.

The Scope of Work is the EPC anchor for Gate 5 readiness; it does not duplicate vendor package engineering and does not invent technical values that are not present in accessible source materials.

## Principles

- **Package identity is workbook-anchored.** Identity fields (name, WBS, tracking number, discipline, interfaces) come from workbook Packages row 31 and the Gate 7 `PACKAGE_REGISTER.csv` row for PKG-029. They are not paraphrased.
- **Function is DBM-anchored.** The transformer's facility function is described using `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System and System Voltages slices: the facility 13.8 kV switchgear distributes power radially through step-down transformers, of which TXP-8600-1 is one, to a 600 V (and 347 V line-to-neutral) low-voltage service.
- **Responsibility split is non-negotiable.** Package Vendor owns engineering, design, documentation, and physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. The Scope of Work does not migrate vendor scope to the EPC.
- **Source authority.** When workbook identity values and DBM narrative disagree, workbook row 31 controls package identity; DBM controls facility-level electrical basis.
- **Conservative inference.** Quantities, ratings, locations, and configurations that are not in accessible source slices remain `TBD`. ASSUMPTION labels are used only where the inference is unavoidable and is bounded.

## Considerations

- **Facility role inference (ASSUMPTION).** TXP-8600-1 is a 13.8 kV / 600 V class transformer. The DBM identifies several 600 V distribution targets, including a "4.16 kV/600 V General Area/Tank Farm/Process Electrical Building" and 600 V Acid Gas / Sales / Overheads Compressor Electrical Buildings. The Scope of Work does NOT assign TXP-8600-1 to a specific downstream target on the basis of these candidates; assignment requires source-supported confirmation.
- **600/347 V notation.** "600/347 V" in the package title corresponds to a wye secondary with 600 V line-line and 347 V line-neutral. This is consistent with the DBM facility 600 V, 3-phase, 3-wire service basis at line 2937 but extends it to include a line-neutral access point; downstream design must confirm whether 347 V loads are served from this transformer.
- **Insulating medium.** The DBM speaks generally of "large oil-filled transformers" being spaced per CEC and installed on structural-steel transformer bases, but for a 2.5 MVA distribution transformer the selection between oil-filled and dry-type is a vendor/EPC decision driven by secondary containment, indoor vs. outdoor location, fire load, and CEC spacing. The Scope of Work shall surface this as a vendor selection question, not pre-decide it.
- **Grounding rule.** The DBM rule that "Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor" is taken as binding for the secondary of TXP-8600-1 unless a documented exception is approved.
- **Primary grounding.** The 13.8 kV system grounding is a facility-level decision (low-resistance grounded per the System Voltages table); the transformer primary is a participant in the facility primary grounding scheme rather than the originator of it.
- **Secondary containment.** The DBM directs that secondary-containment requirements shall be reviewed and that transformer selection should avoid or limit containment requirements where practical. The Scope of Work passes this through to detailed engineering.
- **Interface set is the workbook set.** The seven workbook-flagged interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are all carried; none are deleted on the basis of "obvious" or "not applicable" without a source-supported rationale.
- **Objective association.** The seven objectives associated with PKG-029 (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`) are taken from the package-grouped objective rows via `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`. They are treated as directional context (ASSUMPTION) rather than as hard requirements until a human confirms the mapping at deliverable-ID granularity.

## Trade-offs

- **Specificity vs. source fidelity.** A reader of a Scope of Work for a transformer naturally wants kVA rating basis (ONAN/ONAF), BIL, impedance, vector group, dimensions, weight, and noise levels. None of these are confirmed by accessible source slices for TXP-8600-1; the Scope of Work prefers to mark them `TBD` rather than invent them.
- **Oil-filled vs. dry-type.** Oil-filled offers efficiency and overload capacity at the cost of fire/containment risk and CEC spacing; dry-type reduces fire/containment risk and CEC spacing constraints at higher first cost and (depending on enclosure) larger footprint. The Scope of Work surfaces this trade-off as a vendor decision.
- **Indoor (electrical building) vs. outdoor (yard) installation.** Indoor installation simplifies maintenance access and weather exposure but imposes room/clearance design on the electrical building. Outdoor installation simplifies the electrical building but imposes weatherproof enclosure and security/containment design. Source slices do not assign TXP-8600-1 to either; the Scope of Work surfaces the choice without selecting it.

## Examples

- The DBM describes the facility's main 25 kV / 13.8 kV / 50 MVA utility transformer and the radial 13.8 kV switchgear distribution architecture (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2919). PKG-029's TXP-8600-1 is one of the radial step-down transformers in that architecture, not a utility transformer.
- The 03-25 Compressors & Liquids DBM (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 744-745) describes a "13.8 kV to 600V, 3 MVA transformer" feeding a 600V MCC for LV loads at 03-25. This is an analog for PKG-029's function pattern but is a different facility (WBS 02 / 03-25, not WBS 01 / 04-25); the Scope of Work cites it only as a pattern reference.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-029-01-001 | The package title states `2.5MVA 13.8kV/600/347V` but no package-specific source slice confirms whether this is the ONAN base rating or includes a forced-cooled higher rating, nor whether the transformer is oil-filled or dry-type. | Workbook Packages row 31 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Transformers paragraph (line 2949) | Datasheet.Attributes (insulating medium, rating); Specification.SOW-029-08, SOW-029-10 | Carry 2.5 MVA as the title-derived nameplate basis; leave cooling class and insulating medium `TBD` until vendor data or detailed electrical source is accepted. | TBD |
| HRR-029-01-002 | The DBM Power System lists multiple 600 V distribution candidates (general-area/tank-farm/process electrical building; compressor electrical buildings), but TXP-8600-1's downstream electrical building or load assignment is not confirmed by an accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (lines 2919-2925) | `_CONTEXT.md` (no installation location stated) | Datasheet.Construction (installation location); Specification.SOW-029-05 | Treat the downstream allocation as `TBD`; do not assign TXP-8600-1 to a specific electrical building until source-supported confirmation. | TBD |
| HRR-029-01-003 | The package interface set includes "Area / Exterior Lighting" and "Communications / Network", but no accessible source slice provides the package-specific tie-in basis for these interfaces. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` rows `IFC-DFC1A10C2D`, `IFC-81CFD2A32C` | DBM-Deepcut (no transformer-specific lighting or network text) | Datasheet.Conditions (Area / Exterior Lighting, Communications / Network) | Carry both interfaces as workbook-flagged; describe tie-in scope as `TBD` pending detailed-engineering allocation. | TBD |
