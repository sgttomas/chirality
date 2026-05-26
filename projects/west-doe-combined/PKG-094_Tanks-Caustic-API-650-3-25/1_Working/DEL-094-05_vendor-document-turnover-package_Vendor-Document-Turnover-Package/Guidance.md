# Guidance: DEL-094-05 — Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists because the PKG-094 caustic tanks package is supplied by an external Package Vendor while the EPC Integrator owns facility integration. The set of vendor documents — registered, submitted, reviewed, and turned over — is the controlled evidence layer that lets the EPC Integrator (a) accept the vendor package against the EPC Scope of Work and Package Datasheet, (b) integrate the package into the facility, and (c) close out the package at handoff. [Source: `_CONTEXT.md`; PACKAGE_REGISTER row PKG-094; DELIVERABLE_REGISTER rows DEL-094-04..06]

## Principles

1. **Register-as-truth.** The vendor document register is the single point of truth for what documents are required, what was submitted, what was reviewed, and what was turned over. Everything else (submittals, review logs, turnover records) hangs off register rows. [Source: `_CONTEXT.md` Anticipated Artifacts]

2. **Source rows as artifacts, not deliverables.** Each row of the source vendor document table (`_Sources/26020-Package_Requirements.docx` package heading 46, `location TBD`) is preserved as an artifact/evidence row in this deliverable rather than promoted to a separate deliverable. [Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER row DEL-094-05 Notes]

3. **Vendor authors, EPC reviews.** The Package Vendor authors and submits; the EPC Integrator performs interface/integration review and ultimately accepts under DEL-094-06. Vendor and EPC roles do not blur. [Source: `_CONTEXT.md` ResponsibleParty; OBJ-004]

4. **Code-anchored.** API 650 (modified) governs the equipment; vendor documentation must reflect that code basis. [Source: SOW-0195]

5. **Hold-item visibility.** DBM-level TBC/TBD/hold items affecting the caustic tank package (material selection, coatings, drain temperature limits, heater design, etc.) must be visible in the document set — either as resolved submittals or as explicit hold/closure records. [Source: DBM 3-25 caustic / drain sections]

## Considerations

- The 26020 Package Requirements document is the authoritative source for the document-table rows required for this package, but the binary source could not be slice-extracted in this run; clause-level rows are therefore `location TBD`. The first downstream task that can extract that table should populate the register row template against the source rows. [Source: `_REFERENCES.md` Missing/Deferred References]
- The vendor document register is part of standard mechanical-package deliverables called out by DBM 3-25 line 617, so the omission of any standard category (datasheets, cause-and-effect, utility loads, relief/load data, tie-in lists, envelopes, sparing, materials/coating, maintenance access, shipped-loose, registers) should be deliberate and recorded — not silent. [Source: DBM 3-25 line 617]
- Caustic service is corrosive and presents material/coating selection challenges. Vendor documentation that fixes material and coating choices is therefore safety- and integrity-relevant, not just commercial. Aluminum is prohibited in the caustic building. [Source: DBM 3-25 caustic basis]
- Spent-caustic venting through a flame arrestor to the incinerator header, and the LP fuel-gas blanket on the atmospheric caustic tanks, are interface-sensitive and should be visible in the vendor document set so the EPC Integrator can verify against facility interfaces. [Source: DBM 3-25]
- Minimum drain-header rating (300# ANSI flange minimum, terminating at the spent-caustic tank) and caustic drain max temperature 121 deg C / 250 deg F TBC are interface-critical for vendor documentation that touches the drain system. [Source: DBM 3-25 line 493]
- Foundations, on-site mounting, electrical / instrumentation, platforms, and staircases are "by others" per SOW-0196 — vendor documentation should clearly identify the interface line so the EPC Integrator inherits the right scope. [Source: SOW-0196]

## Trade-offs

- **Completeness vs. cycle time.** Holding for every detail (e.g., coating finalization, drain temperature limit closure) before issuing the document set delays turnover. Issuing with explicit hold items lets work progress while preserving traceability. The HRR table below captures items expected to drive this trade-off.
- **Vendor format vs. EPC interface format.** Vendor's native deliverable formats may not match facility/discipline registers. Where they conflict, surface the conflict rather than silently reformat (the register row carries vendor source identity).
- **API 650 modifications.** "Modified API 650" per SOW-0195 leaves edition/appendix selection open; pinning a specific edition / appendix combination has cost and schedule implications. [Source: SOW-0195]

## Examples

Examples of register rows (illustrative — actual rows must come from the source table at `_Sources/26020-Package_Requirements.docx` package heading 46, `location TBD`):

- Equipment datasheet — TK-6930-2 Spent Caustic Tank — Rev — Submittal date — EPC review status — Turnover status.
- General Arrangement drawing — Fresh / Spent caustic tanks — Rev … etc.
- Hydrotest record — TK-6930-2 — Date — Acceptance status — Turnover status.

## Conflict Table (for human ruling) — HRR Items

This table records items that are **Held for Review/Resolution (HRR)** between source materials, decomposition narrative, and standing practice. They are surfaced rather than silently resolved.

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-001 | Clause-level rows of the source vendor document table are not locally accessible as text (binary `.docx`). | `_Sources/26020-Package_Requirements.docx` package heading 46 | `_CONTEXT.md` Notes — source rows preserved as artifacts | Datasheet/Construction; Spec/R1, R3; Procedure step 2 | PROPOSAL: extract the table into a markdown side-file under `_Sources/` before next pass, then re-populate the register row template. | TBD |
| HRR-002 | Caustic tank material of construction not finalized; aluminum prohibited but specific MOC TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic basis; aluminum prohibition) | DEL-094-04 Datasheet (Material TBD) | Spec/R6.2; Datasheet Construction row | PROPOSAL: carry as HOLD against vendor MOC submittal; closure via vendor datasheet + EPC review. | TBD |
| HRR-003 | Internal coating for caustic tanks TBC; DBM specifies Devchem 253 for produced-water tanks but caustic coating remains open. | DBM 3-25 (coating basis) | DEL-094-04 Datasheet | Spec/R6.2; Datasheet Construction | PROPOSAL: carry as HOLD against vendor coating submittal. | TBD |
| HRR-004 | Caustic drain maximum temperature 121 deg C / 250 deg F is marked TBC; minimum drain tank temperature stated as 80 deg F. | DBM 3-25 line 493 | DEL-094-04 Datasheet (drain interface) | Spec/R6.2; Datasheet Conditions | PROPOSAL: carry as HOLD against vendor thermal datasheet. | TBD |
| HRR-005 | Heater design for spent-caustic tank is vendor-responsibility ("Vendor to design the heater") but utility loads and control interface are EPC-side. | SOW-0195 | DBM 3-25 line 617 (utility load summaries as mechanical-package deliverable) | Spec/R3.2; Datasheet Construction | PROPOSAL: register row "Heater datasheet + utility load summary" required; EPC review under DEL-094-06. | TBD |
| HRR-006 | Capacity / design throughput is marked "TBC" and flow rate is TBD in SOW-0196. | SOW-0196 | DEL-094-04 Datasheet (capacity basis 400 bbl) | Spec/R3.2; Datasheet Conditions | PROPOSAL: register row capturing capacity/throughput confirmation; HOLD until closed. | TBD |
| HRR-007 | API 650 "modified" — specific edition / appendices not declared in source. | SOW-0195 | API 650 base standard | Spec/R6.1; Standards section | PROPOSAL: confirm edition/appendix selection via vendor code datasheet; record in register as a code-stamp item. | TBD |
| HRR-008 | Objective association to this deliverable is by package-grouping heuristic; not row-level confirmed. | `_CONTEXT.md` Supports Objectives; OBJECTIVE_DELIVERABLE_MAP at decomposition snapshot | brief `RuntimeOverrides.OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC` | Datasheet Identification; Guidance/Purpose | PROPOSAL: treat OBJ-002..OBJ-010 as directional context (ASSUMPTION), confirm per row at next pass with human ruling. | TBD |
