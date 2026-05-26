# Guidance: DEL-080-02 — PKG-080 Inlet Compressors Package Datasheet

## Purpose

This deliverable is the mandatory EPC Integrator technical handoff document for **PKG-080 Inlet Compressors**. It exists so that a third-party package vendor (and the EPC discipline engineers integrating around the package) can engineer, design, and procure the two parallel sour inlet gas reciprocating compressor packages on a single, source-grounded basis. It is the Gate 5 EPC anchor deliverable for this package and intentionally carries interface evidence rather than deferring it to standalone interface deliverables (`_CONTEXT.md` Notes).

## Principles

1. **Source authority over convention.** Every non-trivial datasheet value must trace to an accessible source (primary: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05; package row in `PACKAGE_REGISTER.csv`). Generic API-618 conventions, vendor catalog norms, and engineer judgment are not substitutes for cited basis.
2. **Two scopes, one document.** Package Vendor scope and EPC Integrator scope are both visible in the datasheet but never merged. The datasheet records what the vendor will engineer/design/supply and the boundaries the EPC owns (PACKAGE_REGISTER.csv row PKG-080).
3. **Mark unknowns; do not invent.** Values that the DBM marks TBC carry forward as TBC. Items that depend on `26020-Package_Requirements.docx` heading 33 (not locally accessible) are marked `location TBD`. Inferences are labelled `ASSUMPTION`.
4. **Supersession is final.** Where the DBM explicitly supersedes a prior basis (e.g., 800 psig second-stage discharge supersedes 650 to 800 psig), the datasheet uses the superseded value only and notes the supersession.
5. **Interface evidence is first-class.** The interface types in PACKAGE_REGISTER.csv row PKG-080 are carried verbatim; DBM-anchored interface counterparts (MCC-8200 / fuel gas / VRU suction / TEG / drive-gas recycle) are recorded inline.

## Considerations

- **Sour service.** The DBM compressor composition is approximately 0.296 mol% H2S (DBM SEC-05). Material selection, NACE/MR-class compliance, and inspection requirements are referenced by `26020-Package_Requirements.docx` heading 33 — currently `location TBD`. Until that slice is accessible, the datasheet flags sour service but does not invent metallurgy clauses.
- **Starting basis.** SCA-001 VE #34 (DBM SEC-05/SEC-09) governs use of starting VFDs for KM-2150 and KM-2250; soft starts are not the current basis. SCA-001 VE #37 removes capacitor banks on MCC-8200 where VFDs are present. Harmonic and reactive-power mitigation are detailed-design items, not datasheet values.
- **No installed spare.** The 2 x 50 percent philosophy (DBM SEC-05) means a single package outage is a 50 percent loss of compression. This is a design intent of the project basis and must not be re-characterised in the datasheet.
- **Modular delivery.** Each package is shop-assembled, disassembled into three pieces for transport, and field-installed in a self-framing building (DBM SEC-05; SEC-08). Foundation/anchorage design is equipment-specific (DBM SEC-08).
- **Recycle valve failure action.** Recycle valves are expected to fail open; final failure action is TBC (DBM SEC-05). The datasheet records the expectation as TBC, not as a confirmed requirement.
- **Cross-package coupling.** Downstream TEG package (1 x 100 percent) treats compressed sour gas before export to 04-25; packing drains/vents route to VRU suction; sweet-gas start-up purge is supplied from fuel gas. These are interface anchors the datasheet must surface.

## Trade-offs

- **Carry-vs-cite interface data.** Carrying interface anchors inline (DBM-cited counterparts) makes the datasheet usable as a single handoff document at Gate 5 but creates duplication risk if downstream interface deliverables (DEL-080-03 to DEL-080-06) later restate them. Mitigation: keep cited-source pointers in the datasheet so any divergence is traceable to source rather than to drafting drift.
- **TBC values now vs deferred filling.** Filling current TBC items (final dP, second-stage suction temperatures, scrubber K-factor, recycle valve failure action, NACE/MR clauses) requires vendor input or access to `26020-Package_Requirements.docx` heading 33. Closing them now without source would violate K-PROV-1; leaving them as TBC defers risk to vendor review. The chosen trade-off is to keep TBC items explicit and flag them in the conflict table when they would otherwise block downstream design.
- **Strict deliverable-level objective mapping vs package heuristic.** The decomposition's objective-to-deliverable mapping is package-grouped, so this deliverable inherits OBJ-002 through OBJ-010 as an ASSUMPTION. A stricter mapping would either drop or pin specific objectives; absent human ruling, the conservative choice is to carry the full set with the ASSUMPTION label.

## Examples

- **Cited value example.** "Per-package capacity: 40 MMSCFD." Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 Compressor Item table.
- **Supersession example.** "Second-stage discharge pressure (normal/design): 800 psig — fixed under current supersession basis (prior 650 to 800 psig is superseded)." Source: DBM SEC-05 "Compression Design Conditions".
- **Location-TBD example.** "Material specification per NACE/MR-class sour service requirements: location TBD (`26020-Package_Requirements.docx` heading 33 not locally accessible)."
- **Interface-anchor example.** "Electrical Power interface: 4,000 V supply from MCC-8200 in the 4.16 kV inlet/overheads compressor electrical building." Source: DBM SEC-09 "Power and Motor Control".

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-080-02-001 | Material/NACE-MR clauses cited by decomposition row but not locally accessible | PACKAGE_REGISTER.csv row PKG-080 (source basis: `26020-Package_Requirements.docx` heading 33) | DBM SEC-05 (composition only; no material clauses) | Datasheet "Attributes — H2S service material requirements"; Specification R10; Standards table | Extract heading 33 to Markdown and refresh the datasheet material rows; until then carry `location TBD` and ASSUMPTION-applicable for NACE/MR. | TBD |
| C-080-02-002 | Objective mapping is package-grouped (heuristic), not deliverable-strict | `_CONTEXT.md` Supports Objectives (OBJ-002 through OBJ-010) | PROJECT_DECOMP objective-deliverable mapping convention | Datasheet Identification — "Supports Objectives" | Carry full list as ASSUMPTION until objective-deliverable map confirms or narrows the mapping for DEL-080-02 specifically. | TBD |
| C-080-02-003 | Recycle valve failure action stated as "expected fail open" with final action TBC | DBM SEC-05 "Scrubbers, Coolers, Recycle, and Purge" | None — single source | Datasheet "Construction — Recycle control valves"; Specification R7 | Carry as TBC; defer to vendor-confirmed failure mode at vendor engineering kickoff. | TBD |
| C-080-02-004 | Governing reciprocating-compressor standard (e.g., API 618) not stated in accessible source | (none) | DBM SEC-05 (silent) | Specification "Standards" | Mark as ASSUMPTION pending heading 33 access; if heading 33 omits it as well, raise to project standards lead. | TBD |
