# Guidance: DEL-034-01 — Scope of Work (PKG-034 600V Electrical Building (820-2))

## Purpose

This Guidance accompanies the PKG-034 Scope of Work. It explains why the SOW exists, the principles the EPC Integrator should apply when authoring or maintaining it, the considerations and trade-offs particular to a 600V electrical building package within the 03-25 facility, and source-supported examples. It is directional, not normative; normative content lives in `Specification.md`.

## Principles

- **EPC Integrator authorship.** The SOW is integrator-owned. The Package Vendor authors package engineering, package design, and vendor documentation downstream; the SOW frames what the vendor must integrate into the facility, not how the vendor designs the package internals. (Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 Responsibility column.)
- **Source-anchored identity.** Package identity (name, CoA tracking, WBS, discipline, workbook row) flows directly from the workbook Packages register, not from prose summaries. (Workbook Packages row 36; Gate 7 `PACKAGE_REGISTER.csv`.)
- **Integration over internals.** The SOW should describe what the package does for the 03-25 facility — feeding 600V loads, hosting LV distribution and HVAC — rather than restating vendor design content that belongs in DEL-034-04 / DEL-034-05.
- **Interface fidelity.** The 12 interface types in the workbook are the package's facility-side boundary; the SOW preserves the list and points to DEL-034-02 for interface fact detail.
- **Conservative inference.** Where the accessible source does not specify a value (e.g., generator count, transfer-switch type), the SOW records `TBD`. Do not invent values from convention.

## Considerations

- **Two 600V electrical buildings.** The Gate 7 register lists distinct 600V electrical buildings in different WBS contexts: PKG-034 "820-2" (WBS 02, 03-25), PKG-038 "820-1" (WBS 01, 04-25), PKG-039 "850-1" (WBS 01, 04-25), and PKG-040 "860-1" (WBS 01, 04-25). The SOW must keep PKG-034's identity distinct from these sibling packages by carrying the explicit suffix "(820-2)" and WBS 02 in every identity reference.
- **Source split between 03-25 and 04-25.** PKG-034 sits in WBS 02 (03-25) but is electrically sub-fed from 04-25's 13.8 kV Main Switchgear Electrical Building. The SOW should make this cross-WBS dependency explicit so downstream integration (DEL-034-03 construction; DEL-034-06 vendor review) does not lose it.
- **Modular building basis.** The DBM mandates pre-fabricated modular construction for electrical buildings (DBM §12.5.2 via Trace_Appendix). This is a constraint on the vendor and a constructability driver for the integrator; surface it in the SOW even though detailed module-design content belongs to DEL-034-04.
- **Standby power scope.** The current basis replaces the prior 13.8 kV / 3 MW emergency generator concept with LV standby natural-gas generators at the 600V MCC level. Many parameters remain `TBD` in the source. The SOW should reflect the scope shift but not freeze numbers that the DBM leaves open.
- **Exclusions from electrical scope.** LACT units (third-party) and local 03-25 instrument-air compressors (per SCA-006) are explicitly excluded from related electrical scope. The SOW preserves these exclusions so the vendor does not assume scope.
- **Objective association is heuristic.** `OBJ-002, OBJ-004–OBJ-010` are associated to this deliverable under the package-grouping heuristic. Treat as directional context, not as binding objectives, until human-confirmed.

## Trade-offs

- **Detail vs. scope clarity.** Adding equipment-level detail risks duplicating DEL-034-02 / DEL-034-04 content. Prefer identity + function + boundary in the SOW; defer tagged-equipment and interface-fact detail to those deliverables.
- **Restating DBM vs. citing it.** Long quotations from the 3-25 DBM increase SOW length without adding integration value. Prefer pointed references (section + clause) with brief paraphrase.
- **Inclusion of `TBD` items.** Marking `TBD` for unknown parameters (e.g., generator count) is preferable to selecting plausible-looking values; the latter creates downstream rework if the vendor design diverges.

## Examples (source-supported)

- **Identity line example:** "PKG-034 — 600V ELECTRICAL BUILDING (820-2); CoA 26020-02-30-025; WBS 02; Discipline Electrical; Source Workbook Packages row 36." (Gate 7 `PACKAGE_REGISTER.csv`.)
- **Function paragraph example:** "PKG-034 is a pre-fabricated modular electrical building that houses 600V MCC, distribution equipment, and associated HVAC/ventilation for the 03-25 Compressor Station and Liquids Hub. The building is sited per the project area-classification basis and supports LV power distribution downstream of the 13.8 kV / 600V, 3 MVA transformer sub-fed from the 04-25 Main Switchgear Electrical Building." (Source: DBM 3-25 SEC-12 "Electrical Buildings, ..."; SEC-12 "Incoming Power and Transformers"; Trace_Appendix SUB-12-05-02.)
- **Responsibility paragraph example:** Use the Gate 7 register wording verbatim to avoid drift between deliverables.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-034-01-001 | Workbook row 36 is referenced as the package's primary source but is not copied as a local source slice in `_REFERENCES.md` ("Missing / Deferred References"). | `_REFERENCES.md` (Missing / Deferred References) | Gate 7 `PACKAGE_REGISTER.csv` Source column ("Workbook Packages row 36") | Datasheet `References`; Specification `REQ-034-01-008`; Procedure prerequisites | PROPOSAL: treat Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 as the operative carrier of the row-36 facts; mark direct workbook citations as "location TBD" until the row-36 slice is copied locally. | TBD |
| CFT-034-01-002 | Objective association uses the package-grouping heuristic; no objective-to-deliverable map row explicitly names `DEL-034-01_scope-of-work`. | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-034-01 (objective list) | `OBJECTIVE_DELIVERABLE_MAP.csv` (no row explicitly naming this deliverable in accessible slice) | Datasheet `Identification`; Specification `REQ-034-01-009` | PROPOSAL: keep objectives as ASSUMPTION (best-effort mapping) until the objective-deliverable map is human-confirmed. | TBD |
| CFT-034-01-003 | Discipline is "Electrical" but the workbook responsibility text mentions "Electrical/mechanical package vendor"; the slice is ambiguous on whether mechanical scope is present in PKG-034. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 (Discipline=Electrical) | Gate 7 `PACKAGE_REGISTER.csv` row PKG-034 (Responsibility narrative) | Specification `REQ-034-01-003`; Datasheet `Identification` Discipline | PROPOSAL: treat "Electrical" (the Discipline column) as authoritative; treat "Electrical/mechanical" wording as boilerplate carried by the responsibility narrative. | TBD |
