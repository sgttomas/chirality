# Guidance — DEL-084-01 Scope of Work (PKG-084 Fuel Gas Skid 3-25)

Directional guidance for drafting and reviewing the EPC Integrator Scope of Work for the LP Fuel Gas Skid (`26020-02-PT-23-001`). Pass directive: P1_P2.

## Purpose

This deliverable exists because the PKG-084 Fuel Gas Skid is one of the mandatory Gate-5 EPC anchor packages for the West Doe 3-25 Compressor Station, and a clear EPC-Integrator-authored Scope of Work is required to (a) bound the Package Vendor's work, (b) carry the source-supported design basis forward into the Package Datasheet and Construction Work Package, and (c) hand off a clean responsibility split between the EPC Integrator, the Package Vendor, and By Others. (Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row 324; `3-25_Comp_and_Liquids_DBM.md` §Utilities, §"## Fuel Gas".)

## Principles

1. **Source-authority over convention.** Where the package source heading (26020-Package_Requirements.docx heading 37) and the facility DBM (`3-25_Comp_and_Liquids_DBM.md`) provide a value, that value is binding. Generic fuel-gas-skid convention shall not substitute for the actual source values. (Source: skill `four-documents` Authority Hierarchy.)
2. **Tight scope at the skid boundary.** The package source explicitly lists shipping, installation, tie-in piping, and electrical tie-in as "By others" — the SOW shall keep these out of the package and place them with the responsible By-Others party. (Source: 26020-Package_Requirements.docx Scope Notes / Open Items.)
3. **Facility-side vs. package-side fuel-gas equipment.** The facility-side LP fuel-gas scrubber referenced in the DBM (`V-3210-2`) is downstream of the heater and routes liquids to `TK-9130-2`; the SOW shall not conflate this facility-side equipment with the in-package scrubber on the skid. (Source: `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas".)
4. **Open items remain open.** Heater capacity, final flow, MAWP, and the emergency-buyback question are all genuinely unresolved in the source — the SOW shall carry them as TBD/CONFLICT rather than back-fill values that the source does not support. (Source: 26020-Package_Requirements.docx Scope Notes / Open Items; `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas".)

## Considerations

- **Shared cross-facility utilities.** The fuel-gas system is shared with 04-25; the SOW narrative shall acknowledge that the LP fuel-gas users include TEG stripping, caustic treating overhead dilution, maintenance purge, drive gas, and blanket gas — even though most of those consumers live outside the PKG-084 skid. This matters for sizing margin discussions and for the facility integration narrative. (Source: `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas", §Utilities.)
- **Sweet-gas purge dependency.** The DBM notes that start-up sweet-gas purge is supplied from the fuel-gas system, and that methyl mercaptan toxicity/odour hazards are relevant to purge, analyzer, and operations planning. This may drive analyzer, isolation, and maintenance requirements that surface in the Construction Work Package and in vendor PHA inputs. (Source: `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas", §"## Fuel-Gas Sulphur and Purge Hazard Basis".)
- **Heater electrical interface.** The SCR control panel is vendor-supplied at 600 V and located in the electrical building; the SOW shall therefore frame "Electrical Power: No" in the interface table as "no field power tie-in within package scope" rather than "no electrical content" — the panel itself is package scope. (Source: 26020-Package_Requirements.docx Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary.)

## Trade-offs

- **K-factor scrubber sizing margin.** The K = 0.35 maximum is a ceiling; vendor may choose a lower K to add carry-over margin at the cost of vessel size. The SOW should leave the sizing decision with the vendor but require disclosure of the K used in `MEC-014`. (Source: 26020-Package_Requirements.docx Major Included Equipment.)
- **Buyback fuel-gas inclusion.** Including buyback adds scope and tie-in burden but resolves a single source of fuel-gas reliability risk during loss of Enbridge supply; excluding it follows W242510. The SOW shall not pre-decide this — it is a human ruling. (Source: `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas".)

## Examples

Examples beyond what the source provides are not introduced (per source-grounding rule). Use the source's "Basic Scope" and "Major Included Equipment" narrative as the model for SOW prose; use the source "Vendor Engineering Deliverables" list as the model for the vendor document checklist appendix. (Source: 26020-Package_Requirements.docx heading 37.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CFL-084-01 | Emergency buyback fuel gas inclusion in 04-25 utility package | W242510 — "not required" (cited in `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas") | Process_DBM_fixed — includes buyback (cited in same section) | `Specification.md` §R-SOW-084-7, R-SOW-084-11; `Datasheet.md` §Conditions ("Emergency buyback fuel gas") | PROPOSAL: hold buyback out of PKG-084 SOW and route the question to the 04-25 utility package owner | TBD |
| CFL-084-02 | Source heading uses descriptor "West Doe Deep Cut Facility" while package is sited at the 3-25 Compressor Station and Liquids Hub | 26020-Package_Requirements.docx Basic Scope ("West Doe Deep Cut Facility") | `3-25_Comp_and_Liquids_DBM.md` §Utilities (LP fuel-gas users / shared utility framing) | `Specification.md` §R-SOW-084-2, R-SOW-084-7; `Guidance.md` §Principles | PROPOSAL: treat as harmless naming variation — the skid serves the 3-25 facility's LP fuel-gas system within the shared cross-facility utility scheme. Confirm in SOW narrative. | TBD |
| CFL-084-03 | Interface source filename in source heading (`26020-Packages_Interfaces.3.xlsx`) differs from local source filename (`26020-Packages_Interfaces_4_export.xlsx`) | 26020-Package_Requirements.docx Physical Interface Summary | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (locally available) | `Datasheet.md` §Physical Interface Summary; `Specification.md` §R-SOW-084-8 | PROPOSAL: treat `_4_export` as the controlled successor to `.3.xlsx` for this PKG-084 row 60. Confirm. | TBD |
