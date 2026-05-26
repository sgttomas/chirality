# Guidance: DEL-045-03 Construction Work Package

## Purpose

This guidance explains how to use the initial construction work package for `PKG-045 - Instrumentation (outside of Mechanical Packages only)` without overstating the currently available source basis.

The deliverable exists because Gate 5 makes `Construction Work Package` a mandatory EPC Integrator anchor deliverable for every approved package. For this package, it must describe physical installation, construction, tie-in, inspection, and turnover into larger systems. Source: `DELIVERABLE_REGISTER.csv`, row `DEL-045-03_construction-work-package`; `_CONTEXT.md` Notes.

## Principles

- Treat the accepted Gate 7 snapshot as the authoritative decomposition truth for identity, package membership, objectives, deliverable purpose, artifacts, and interface facts.
- Treat workbook row 47 and the Gate 7 registers as authoritative for package identity and interface flags.
- Treat upstream `DEL-045-01_scope-of-work` and `DEL-045-02_package-datasheet` as the intended carriers of tagged equipment, loop counts, and vendor handoff facts; do not invent that content here.
- Keep instrument quantities, panel counts, cable schedules, loop ITP hold points, hazardous-area classification, and turnover signoffs as `TBD` unless a local source defines them.
- Do not treat the decomposition narrative as a substitute for IFC instrumentation drawings, loop sheets, instrument data sheets, or discipline execution criteria.

## Considerations

| Topic | Guidance |
|---|---|
| Scope boundary (instrumentation outside of mechanical packages) | The package name explicitly carves instrumentation that is not embedded in mechanical packages. The CWP should make this carve-out visible at the interface checklist level and avoid pulling instrumentation already owned by mechanical packages into this scope. |
| Plug-n-play disposition | Gate 6 dispositioned instrumentation field supports, power, and communications as included in each package scope as appropriate under a plug-n-play philosophy (`INTERFACE_REGISTER.csv` rows 307-311 Notes). Apply this when deciding what supports, power, and comms scope belongs in the CWP. |
| Five interface types | All five PKG-045 interfaces (Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network) are flagged YES in the workbook. The CWP should surface tie-ins for each but keep tie-in points, routing, and signoff owners `TBD` unless IFC drawings define them. |
| Upstream handoff dependency | This CWP cannot close instrument lists, loop counts, or vendor-data acceptance until `DEL-045-01` and `DEL-045-02` carry source-supported equipment and interface data. Surface this as a coordination dependency rather than guessing. |
| Responsibility | The package register says responsibility is EPC Integrator or discipline subcontractor source-dependent. Assign coordination to the EPC Integrator and keep subcontractor assignment `TBD` unless separately confirmed. |
| Cited DBM not extracted | `PACKAGE_REGISTER.csv` row 47 cites `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` as supporting basis, but the relevant instrumentation slice was not extracted into `_REFERENCES.md`. Treat any DBM-derived claim as `location TBD` until a slice is captured. |

## Trade-offs

- Early CWP drafting improves package coordination and interface visibility, but premature closure of instrument-list-dependent values would create false precision.
- Carrying all five interface types preserves source fidelity, but the CWP should distinguish which interfaces are physically active in this package's tie-in scope versus carried for completeness.
- Using `TBD` for execution details creates open items, but it preserves source fidelity until IFC-level instrumentation drawings and upstream deliverables are available.

## Examples

- Source-supported: "Address Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network interfaces" because workbook row 47 and `INTERFACE_REGISTER.csv` rows 307-311 identify these interface types.
- Source-supported: "Include instrumentation field supports, power, and communications per the Gate 6 plug-n-play disposition" because the disposition is recorded in `INTERFACE_REGISTER.csv` rows 307-311 Notes.
- Not source-supported yet: specific tagged instruments, loop counts, panel/cabinet quantities, cable schedules, hazardous-area class designation, ITP hold points, or turnover signoff names.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified during P1/P2 drafting. Unsupported detail is marked `TBD` rather than treated as conflict. | N/A | N/A | N/A | N/A | N/A |
