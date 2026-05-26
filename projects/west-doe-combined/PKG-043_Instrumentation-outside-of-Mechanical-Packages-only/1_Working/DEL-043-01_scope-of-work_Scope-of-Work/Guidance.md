# Guidance — DEL-043-01 Scope of Work

## Purpose

DEL-043-01 is the mandatory Gate 5 EPC anchor deliverable for PKG-043. It defines what the EPC Integrator is accountable for in delivering the instrumentation scope that lies *outside* of Mechanical vendor packages. It exists to (a) close the boundary between vendor-owned instrumentation and EPC-owned instrumentation, (b) make tagged equipment and integration responsibilities explicit, and (c) anchor downstream EPC deliverables (Package Datasheet, Construction Work Package, Discipline Production Package) to a single source-of-truth scope statement.

## Principles

1. **Boundary clarity over completeness.** The package name itself ("outside of Mechanical Packages only") is an exclusion-by-construction. The SOW must make that boundary operational by referencing the Mechanical package equipment lists, even when the full PKG-043 tagged list is not yet available.
2. **Decomposition routes; sources determine.** PROJECT_DECOMP and the PACKAGE_REGISTER define what PKG-043 *is*; the DBM and project E&I specifications determine what PKG-043 must *do*. Do not promote decomposition prose to requirement text where source text exists.
3. **Conservative on responsibility.** PACKAGE_REGISTER row PKG-043 records "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources." The SOW should preserve that conservatism rather than over-assigning to a single party.
4. **Whole-facility integration is mandatory.** The DELIVERABLE_REGISTER text explicitly calls for a "whole-facility integration narrative"; instrumentation cross-cuts almost every other package, so this narrative is the principal value of the SOW.

## Considerations

- **Shared instrument air.** The DBM treats instrument air as a consolidated 04-25 package serving both 04-25 and 03-25 (DBM L1822, L1906-1925). PKG-043 is *Instrumentation*, not *Instrument Air*; the SOW should explicitly delineate.
- **Shared analyzers.** Process analyzers and special instrumentation are also addressed as a utility basis in DBM SEC-08 (L2093 ff.); the SOW should clarify whether analyzer instrumentation falls inside PKG-043 or under the utility/analyzer scope.
- **Interface coverage.** The interface set recorded for PKG-043 includes Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, and Communications / Network. The SOW should explicitly state which of those are *active* interfaces for the package and which are not yet confirmed (per the InterfaceReviewNotes caveat that "Field supports, power, and comms not marked unless confirmed by package scope").
- **Field installation responsibility.** DBM L115 allocates installation of shipped-loose instruments, valves, and components to Tourmaline field construction. Whether that applies inside PKG-043 (vs. EPC field installation) is an ASSUMPTION until confirmed.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Enumerate now vs. carry as TBD | Tagged-equipment list at row-45 scope is not extractable from current accessible sources. Carrying as TBD with explicit Workbook reference is safer than inferring a list. |
| Single SOW vs. split by sub-discipline | PKG-043 covers all non-mechanical-package instrumentation, which spans field instruments, analyzers, fire-and-gas, ESD push buttons, and control cabling. Splitting risks fragmenting the boundary statement; keeping a single SOW preserves boundary clarity at the cost of internal detail. Recommend single SOW with sub-discipline sections. |
| Include analyzers vs. defer to utility scope | Including analyzers keeps the instrumentation discipline whole; deferring respects the DBM utility partitioning. Recommend including by reference and flagging the overlap. |

## Examples

- **Boundary statement (example wording):** "PKG-043 covers all instrumentation under WBS 01 not owned by a Mechanical vendor package, including field instruments, transmitters, control valves not integral to packaged equipment, analyzers and special instrumentation, fire-and-gas detection, ESD push buttons, and associated I&C / control cabling and network connections. Instrumentation that ships inside a Mechanical vendor package (including its skid-mounted transmitters, gauges, and packaged-control elements) is excluded."

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-043-01-001 | PKG-043 boundary vs. consolidated 04-25 Instrument Air package. Instrument air is treated as a separate consolidated utility package in DBM SEC-08 (L1822, L1906-1925), but PKG-043 is labeled simply "Instrumentation (outside of Mechanical Packages only)". Whether instrument-air instrumentation belongs to PKG-043 or to the utility package is ambiguous. | DBM-Deepcut/4-25_Deepcut_DBM.md §SEC-08 (L1822, L1906-1925) | PACKAGE_REGISTER.csv row PKG-043 (Name; ResponsibilityModel) | Datasheet §Conditions; Specification REQ-043-01-05, REQ-043-01-09 | PROPOSAL: PKG-043 owns field instruments and analyzers outside Mechanical packages; instrument-air *system* package is separate; instrument-air *consumers* (pneumatic valves, switches) downstream of utility supply remain in PKG-043 when not in a Mechanical package. | TBD |
| CONF-043-01-002 | Installation responsibility for shipped-loose instruments. DBM L115 assigns this to Tourmaline field construction; PKG-043 SOW must state whether EPC Integrator or owner is responsible. | DBM-Deepcut/4-25_Deepcut_DBM.md L115 | _CONTEXT.md ResponsibleParty (EPC Integrator) | Specification REQ-043-01-10; Procedure Prerequisites/Steps | PROPOSAL: EPC Integrator owns engineering, procurement, and management; field installation allocation follows project execution contract (likely Tourmaline construction). | TBD |
| CONF-043-01-003 | Tagged equipment list at PKG-043 scope is not available in extracted sources. Workbook docx is binary and not extracted; the related Instrument Air Building tag list (DBM L2601) belongs to the 04-25 IA package, not PKG-043. | _Sources/26020-Package_Requirements.docx (binary) | DBM-Deepcut/4-25_Deepcut_DBM.md L2601 | Datasheet §Construction; Specification REQ-043-01-02 | PROPOSAL: Extract row 45 tagged list from workbook docx during detailed engineering; do not infer from DBM utility tags. | TBD |
