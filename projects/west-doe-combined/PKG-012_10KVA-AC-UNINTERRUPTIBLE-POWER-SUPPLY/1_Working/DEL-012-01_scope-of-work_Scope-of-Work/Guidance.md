# Guidance: DEL-012-01_scope-of-work — Scope of Work

## Purpose

This deliverable gives the EPC Integrator a controlled scope-of-work basis for the `PKG-012` 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package. It should identify the package, define the EPC/vendor responsibility boundary, and make the known facility interfaces visible for downstream package datasheet, construction, vendor package, vendor documentation, and acceptance workflows.

## Principles

- Use Workbook Packages row 14 and the Gate 7 registers as the controlling basis for identity, discipline, package ownership, and interface facts.
- Keep the vendor/EPC split explicit: the Package Vendor owns package engineering, design, vendor documentation, and physical equipment; the EPC Integrator owns integration into the functional process facility.
- Treat Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports as required scope-of-work boundary topics because they are marked as workbook interface facts.
- Preserve unsupported UPS technical details as `TBD`. The current source slice does not provide load list, autonomy, battery type, enclosure, input/output ratings, distribution arrangement, environmental conditions, testing criteria, or vendor-document tables for this package.
- Use objective mappings as directional context for why the scope matters, not as a substitute for package-specific technical criteria.

## Considerations

The Scope of Work should be useful as an EPC anchor document. It should therefore separate three layers:

1. Source-grounded facts: package ID, package name, WBS, CoA tracking number, discipline, responsibility model, and interface categories.
2. Integration obligations: what the EPC Integrator must coordinate across facility power, grounding/bonding, access, and supports.
3. Open technical details: UPS-specific requirements that need additional source material or human ruling before they can become firm requirements.

The package is electrical and vendor-owned under the accepted responsibility model. Avoid assigning vendor design work to the EPC Integrator, while still requiring the EPC Integrator to define facility integration expectations and review the vendor package for interface compatibility.

## Trade-offs

| Topic | Guidance |
|---|---|
| Scope completeness vs. source fidelity | Prefer `TBD` for missing UPS design details rather than filling gaps from generic UPS practice. |
| EPC integration vs. vendor design | EPC scope should state facility interfaces and acceptance expectations, while vendor scope should develop the physical UPS package design. |
| Objective context vs. requirements | Objectives `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, and `OBJ-010` explain downstream intent, but only source-supported facts should become document requirements. |
| Interface breadth | Include all four workbook-marked interface categories even if detailed interface parameters are currently unavailable. |

## Examples

| Acceptable wording pattern | Reason |
|---|---|
| "The Scope of Work shall identify Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports as coordination interfaces." | Directly supported by Workbook Packages row 14 and Gate 7 `INTERFACE_REGISTER.csv`. |
| "UPS autonomy, load list, battery type, and environmental criteria are TBD pending source confirmation." | Preserves missing technical detail without invention. |
| "The Package Vendor owns package engineering/design/equipment; the EPC Integrator owns facility integration and interface review." | Matches the accepted Gate 7 responsibility model. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-012-01 | UPS-specific technical criteria are not available in the deliverable-specific source slice, but the scope-of-work document needs enough detail for vendor execution. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 14 gives package identity and interface flags only. | Gate 7 registers require the EPC Scope of Work to include package function and integration narrative. | Datasheet Attributes/Conditions; Specification Requirements/Standards; Procedure Steps | Use workbook and Gate 7 facts now; keep technical criteria as `TBD` until a source or human ruling supplies them. | TBD |
