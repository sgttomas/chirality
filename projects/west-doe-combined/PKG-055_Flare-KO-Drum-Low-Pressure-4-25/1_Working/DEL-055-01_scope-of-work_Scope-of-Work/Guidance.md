# Guidance — DEL-055-01 Scope of Work (Flare KO Drum (Low Pressure) 4-25)

> Directional rationale for the EPC Scope of Work for PKG-055: purpose, principles, considerations, and trade-offs.

## Purpose

This deliverable is the mandatory Gate 5 EPC anchor that fixes what PKG-055 is, what it does, who is responsible for which part of it, and how it integrates into the broader 4-25 Deepcut process facility. It is the upstream control for the package datasheet (DEL-055-02), the construction work package (DEL-055-03), and the vendor and acceptance deliverables (DEL-055-04 through DEL-055-06). All downstream package documents inherit their scope boundaries from this Scope of Work.

Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv rows DEL-055-01..06.

## Principles

1. **Source-anchored scope.** Every in-scope and out-of-scope statement traces to the workbook row, the 26020-Package_Requirements.docx heading 10 source slice (via SCOPE_LEDGER SOW-0083..0086), or the 4-25 Deepcut DBM. The Scope of Work does not invent scope items that are not supported by these sources.
2. **Workbook responsibility split is authoritative.** The Package Vendor / EPC Integrator division stated in PACKAGE_REGISTER.csv row 57 governs all responsibility statements in this Scope of Work. Where downstream documents disagree, this Scope of Work prevails (subject to human ruling).
3. **Adjacent flare-system equipment stays outside the package boundary.** The LP flare stack, the common HP/cryo flare stack, and the air-assist blower are connected system equipment, not part of the KO drum package (SOW-0086; DBM-Deepcut lines 2029, 2031). Pulling them into PKG-055 would re-shape package responsibility boundaries the workbook did not authorize.
4. **Integration narrative cites tags, not just topology.** The facility-integration narrative should reference equipment tags (`V-3900-1`, `P-3900-1`, header size, stack arrangement) rather than only abstract topology, so that the Scope of Work can be unambiguously consumed by the construction work package and acceptance deliverable.
5. **Open items remain open.** Where the DBM marks an item TBD (e.g., LP flare stack OD, relief volume basis, shared 03-25/04-25 allocation), the Scope of Work surfaces the TBD rather than substituting an unsupported value.

## Considerations

- **Heading 10 detailed datasheet not yet locally extracted.** The 26020-Package_Requirements.docx is present in `_Sources/` but is not yet rendered to markdown locally. Only the four extracted SOW slices (0083..0086) are currently available as text. Detailed clause-level requirements (pressure, temperature, material, instrumentation, vendor document register) live in this document and are referenced as `location TBD` in the production documents. A pdf2md / docx2md extraction pass should be run before the package datasheet (DEL-055-02) attempts to produce binding design conditions.
- **LP element shares the HP/cryo stack.** Because the LP flare element piggy-backs on the common HP/cryo stack, the Scope of Work's exclusion of the LP stack is also implicitly an exclusion of the common stack. The Scope of Work should make this two-step exclusion explicit, otherwise a downstream consumer could read "LP stack excluded" as "common stack included."
- **Connected LP equipment list defines envelope, not requirements.** The LP flare's connected equipment list (amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot) defines the service envelope but does not supply specific composition, flow, or load data for the KO drum. Those derive from the package datasheet (DEL-055-02).
- **Objective-deliverable mapping is package-grouped.** PROJECT_DECOMP at Gate 7 maps objectives to packages, not to individual deliverables. The eight objectives carried in `_CONTEXT.md` are inherited from PKG-055 and are labeled ASSUMPTION at the deliverable level.

## Trade-offs

- **Comprehensive scope statement vs. interface delegation.** The Scope of Work could attempt to fully specify every interface (process, electrical, I&C, structural) inside this document. Doing so would create duplication with the package datasheet and construction work package. Preferred trade-off: enumerate interface types and assign responsibility (R-5), and delegate clause-level interface requirements to the package datasheet.
- **Tag identification depth.** Listing only `V-3900-1` and `P-3900-1` is faithful to the source slices but excludes ancillary instrumentation, valves, and piping that will appear in the package datasheet. Preferred trade-off: keep the SOW tag list minimal and authoritative, and let DEL-055-02 elaborate.
- **Modularization disclosure.** The DBM identifies the KO drum as a "Shop" module (line 2783). The Scope of Work can either declare shop modularization as a binding requirement or carry it as context. Preferred trade-off: carry as context now; promote to a binding requirement only after the construction work package (DEL-055-03) confirms shop assembly is required.

## Examples

Source-grounded example of an in-scope statement:

> "Supply one LP flare knock-out drum (`V-3900-1`) and one LP flare KO drum transfer pump (`P-3900-1`), including liquid transfer to the condensate slop tank, truck-out provision, and package tie-ins (26020-Package_Requirements.docx heading 10, Major included equipment; SCOPE_LEDGER SOW-0085)."

Source-grounded example of an exclusion statement:

> "The LP flare stack and the air-assist blower are described as connected system equipment in heading 10 scope notes. Stack sizing and flare tip details are explicitly outside this KO drum package's scope (SCOPE_LEDGER SOW-0086)."

## Conflict Table (for human ruling)

No conflicts identified in Pass 1/Pass 2 across drafted documents and accessible sources.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | (none) | — | — | — | — | — |
