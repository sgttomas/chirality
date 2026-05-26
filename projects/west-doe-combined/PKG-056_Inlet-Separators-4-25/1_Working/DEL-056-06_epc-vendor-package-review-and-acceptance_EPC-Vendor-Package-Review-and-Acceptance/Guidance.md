# Guidance: EPC Vendor Package Review and Acceptance

## Purpose

This guidance supports the EPC Integrator's review and acceptance of the Inlet Separators 4-25 vendor package against the EPC Scope of Work (DEL-056-01), Package Datasheet (DEL-056-02), and Construction Work Package (DEL-056-03). It exists to turn accepted Gate 7 package/interface/artifact truth and accessible Deepcut DBM source slices into a controlled review-and-acceptance basis without inferring vendor-specific requirements from inaccessible source text.

## Principles

- Treat Gate 7 registers as accepted upstream truth for package identity, deliverable identity, objectives, artifacts, and interface facts.
- Treat the Deepcut DBM Inlet Separator section as the governing accessible source for mechanical/process basis pending availability of the docx package requirements text.
- Preserve the responsibility split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination.
- Carry the existing source-level conflicts (separator quantity, per-separator gas design rate, slug capacity) as unresolved items rather than silently selecting an authority.
- Keep unsupported acceptance criteria as TBD rather than inferring them from decomposition prose when the actual source text is not locally accessible.
- Use declared dependencies only when assessing blockers; this deliverable currently has no declared upstream or downstream dependencies in `_DEPENDENCIES.md`.

## Considerations

- The detailed vendor package requirements live in 26020-Package_Requirements.docx heading 11; that file is referenced by the decomposition but is not locally accessible as text. Review-and-acceptance criteria sourced only from this docx must be marked TBD until a source slice is brought in.
- The deliverable depends on five logically upstream deliverables (DEL-056-01..05) that are not yet declared in `_DEPENDENCIES.md`. Their absence as declared edges means the dependency check is advisory; acceptance still requires their accepted content.
- The Deepcut DBM explicitly preserves unresolved values for separator quantity, per-separator gas rate, slug capacity per separator, and the warm-side stream identity at the inlet/outlet exchanger. Acceptance criteria must not silently close these.
- Outlet heater target outlet temperature, heat duty, and heating medium remain TBD pending process simulation and medium selection. Acceptance content should carry these as open inputs, not assumed values.
- Inlet piping distribution design relies on piping symmetry, with detailed distribution review deferred to detailed engineering; acceptance can confirm the basis but not finalize the distribution design.
- The eleven applicable interface types from the workbook row anchor the interface coverage expectation; an acceptance package missing one of these is incomplete by source-grounded definition.

## Trade-offs

| Topic | Trade-off | Current treatment |
|---|---|---|
| Early acceptance basis vs. final design closure | The EPC Integrator can accept the vendor package against accepted Gate 7 truth and DBM source, but cannot close items that depend on unresolved DBM conflicts or the inaccessible docx slice. | Use a source-limited acceptance closure record with explicit open-input log. |
| Vendor authority vs. EPC integration authority | The vendor owns package engineering/design/documentation; the EPC Integrator owns facility-level integration. Review must not rewrite vendor design content; acceptance must enforce integration boundaries. | Keep review comments scoped to integration, interface, and source-basis conformance. |
| Quantity carry vs. quantity selection | The current package basis is two installed + future plot space; legacy four-package references exist. | Carry both as unresolved; do not select a quantity authority absent a human ruling. |

## Examples

- Supported statement: "Each inlet separator shall be internally coated with Devchem 253." Source: 4-25_Deepcut_DBM.md, Inlet Separator construction.
- Supported statement: "Process Piping applies as an interface to PKG-056." Source: INTERFACE_REGISTER.csv, IFC-C5833B2729.
- Unsupported statement unless later evidence is added: "Vendor shall perform [specific test] per [specific clause of the docx package requirements]." Current treatment: TBD pending source access.
- Unsupported statement unless later evidence is added: "Per-separator gas design rate is [specific value]." Current treatment: TBD; carry the 125 to 150 MMSCFD range and the unresolved facility total.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-056-06-001 | Installed separator quantity is unresolved. | 4-25_Deepcut_DBM.md, Inlet Separator narrative and Inlet Separator Design Parameters: two installed plus future plot provision. | 4-25_Deepcut_DBM.md, Inlet Separator narrative: legacy project references describe four inlet separator packages. | Datasheet Conditions; Specification REQ-056-06-006; Procedure Verification. | Carry two installed plus future plot space as the working basis; preserve the legacy four-package reference as open. | TBD |
| HRR-056-06-002 | Per-separator gas design rate and facility total are unresolved. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters: 125 to 150 MMSCFD per separator. | 4-25_Deepcut_DBM.md, Inlet Separator narrative: facility total unresolved between 300 MMSCFD and approximately 225 MMSCFD. | Datasheet Conditions; Specification REQ-056-06-008. | Carry the 125 to 150 MMSCFD per-separator range and the unresolved facility total until detailed engineering confirms. | TBD |
| HRR-056-06-003 | Slug capacity per separator is unresolved. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters: 31.8 m3. | 4-25_Deepcut_DBM.md, Inlet Separator Design Parameters: 33.9 m3. | Datasheet Conditions; Specification REQ-056-06-009. | Carry both values as candidates pending ruling. | TBD |
| HRR-056-06-004 | Detailed vendor package requirements source (26020-Package_Requirements.docx heading 11) is referenced but not locally accessible as text. | _REFERENCES.md, Source Materials Referenced By Decomposition Row. | _REFERENCES.md, Missing / Deferred References. | Specification REQ-056-06-018; Procedure Steps; Records. | Treat any acceptance criterion that would derive solely from this slice as TBD until the slice is brought into the deliverable's accessible source set. | TBD |
| HRR-056-06-005 | Logically upstream deliverables (DEL-056-01..05) are not declared as upstream dependencies. | _DEPENDENCIES.md, Declared Upstream Dependencies: none declared. | DELIVERABLE_REGISTER.csv, DEL-056-06 description: review against EPC Scope of Work, Package Datasheet, Construction Work Package; and DEL-056-04..05 produce the vendor package and vendor documents. | Procedure Prerequisites; Specification REQ-056-06-020. | Declare DEL-056-01, DEL-056-02, DEL-056-03, DEL-056-04, and DEL-056-05 as upstream during dependency-extract; until then, treat them as advisory upstream evidence. | TBD |
