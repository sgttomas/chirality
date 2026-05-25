# Guidance: DEL-027-01_scope-of-work

## Purpose

This guidance document supports drafting of the Gate 5 EPC Scope of Work for `PKG-027`, the Transformer `TXP-8301-1` STEP DOWN DISTRIBUTION TRANSFORMER package. It explains how to keep the Scope of Work source-grounded against the workbook package row, the accepted Gate 7 PROJECT_DECOMP snapshot, and the DBM electrical design basis, while not overstating package-specific facts that are absent from accessible source.

## Principles

- Treat the workbook row 29 package label ("Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV") as the authoritative package-identity source for tag, function, and voltage labelling.
- Treat the Gate 7 PROJECT_DECOMP snapshot (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `ARTIFACT_REGISTER.csv`) as the authoritative decomposition basis for responsibilities, deliverable scope, interface facts, objectives, and artifacts.
- Treat `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` as the authoritative facility electrical design basis for the 13.8 kV switchgear, 6.9 kV motor distribution, transformer foundations and spacing, and grounding philosophy.
- Do not invent transformer ratings, vector groups, impedances, BIL values, cooling classes, or tap configurations that are not present in source. Mark them `TBD`.
- Distinguish facility-wide design rules (DBM) from package-specific vendor data (not yet available). Apply facility rules as applicable design basis, not as confirmed package values.

## Considerations

- The DBM is explicit that the facility 13.8 kV switchgear feeds the 6.9 kV motor distribution through step-down transformers. `TXP-8301-1` (20/26 MVA, 13.8/6.9 kV) is consistent with that role; this is the source-grounded function statement.
- The DBM explicitly grounds each 6.9 kV transformer with a 100 A, 10 s NGR operated as a tripping system. This is a facility design rule and should be reflected in the Scope of Work as the 6.9 kV-side grounding requirement.
- The DBM identifies a 6.9 kV electrical building ("820-1 6.9kV Inlet / Sales Compressor Electrical Building"). It does NOT explicitly assign `TXP-8301-1` to that building, so the installation location remains `TBD`.
- The DBM treats large transformers as oil-filled with CEC spacing and structural-steel/precast bearing foundations; secondary containment is to be reviewed and limited where practical. This guidance applies; the package-specific containment decision is `TBD`.
- The 0.4 kV winding label in the workbook is not aligned with the DBM's defined low-voltage levels (600 V, 480 V, 208/120 V). Either (a) the label is workbook shorthand for a different voltage that the vendor will confirm, or (b) it identifies a vendor-supplied auxiliary winding (e.g., for transformer accessories) outside the DBM facility-distribution voltage set. Mark as `ASSUMPTION` and surface as a human-ruling item rather than inventing a function.

## Trade-offs

- Including transformer technical detail (impedance, vector group, BIL, cooling, tap range) in the Scope of Work would improve vendor handoff completeness but would require values not present in accessible source. Preferred resolution: defer these to the Package Datasheet (DEL-027-02) when source is available, and limit the Scope of Work to the source-grounded function/responsibility/interface story plus explicit `TBD` items.
- Naming the host electrical building improves constructability clarity but is not supported by accessible source; leaving it `TBD` is safer than inferring assignment from building-name keywords.
- Restating the entire DBM electrical chapter inflates the Scope of Work. Preferred resolution: cite the relevant DBM source slices (13.8 kV distribution; 6.9 kV services; transformers; grounding) rather than re-asserting their content verbatim.

## Examples

- Function narrative phrasing grounded in DBM: "The package supplies a step-down from the facility 13.8 kV switchgear to the 6.9 kV process motor distribution; the 6.9 kV side shall be grounded through a 100 A, 10 s neutral grounding resistor operated as a tripping system, per the project DBM."
- Responsibility phrasing grounded in `PACKAGE_REGISTER.csv`: "Package Vendor owns package engineering, design, vendor documentation, and the physical equipment. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination."
- TBD phrasing: "Cooling class (ONAN/ONAF), impedance, BIL, vector group, tap configuration, losses, and noise level are `TBD`; vendor data shall populate these in the Package Datasheet."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-027-01-001 | Workbook package name identifies a "0.4 kV" winding, but the DBM voltage and service table defines facility low voltages as 600 V, 480 V, and 208/120 V — 0.4 kV is not listed. | Workbook Packages row 29 (package name) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table | Datasheet Attributes (Tertiary), Specification REQ-027-01-004 / REQ-027-01-008, Guidance Considerations, Procedure prerequisites | PROPOSAL: carry "0.4 kV" as workbook label only; do not assign a facility-distribution role to it until vendor confirms. | TBD |
| CONF-027-01-002 | Workbook package name implies a single transformer rated 20/26 MVA at 13.8/6.9/0.4 kV, but the DBM does not specifically name `TXP-8301-1`, its host building, or its ratings. | Workbook Packages row 29 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and 13.8 kV switchgear paragraphs | Datasheet Construction, Specification REQ-027-01-008, Procedure Steps | PROPOSAL: rely on workbook identity for tag and rating; mark host building/area as `TBD` pending detailed engineering. | TBD |

## Human Ruling Required (HRR)

- `HRR-027-01-001` — Confirm the technical meaning of the "0.4 kV" winding in the workbook package name (winding voltage role, vendor-auxiliary use, or label correction) before the Package Datasheet finalizes the secondary/tertiary configuration.
- `HRR-027-01-002` — Confirm the cooling class basis (e.g., ONAN/ONAF) implied by the "20/26 MVA" dual rating, since the DBM does not state it.
- `HRR-027-01-003` — Confirm assignment of `TXP-8301-1` to a specific electrical building, pad, or area, since the DBM names possible host buildings but does not assign this transformer.
