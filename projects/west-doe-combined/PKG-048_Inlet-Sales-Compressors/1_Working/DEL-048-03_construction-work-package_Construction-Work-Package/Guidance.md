# Guidance: DEL-048-03 — Construction Work Package

## Purpose

This Construction Work Package (CWP) is the mandatory Gate 5 EPC anchor deliverable that translates the engineered scope for PKG-048 (Inlet / Sales Compressors) into a physically executable construction plan. It enables the EPC Integrator to install, build, inspect, turn over, and tie in the inlet compression and sour-gas dehydration scope at the 03-25 West Doe Compressor Station (Sources: _CONTEXT.md Scope/Notes; 3-25_Comp_and_Liquids_DBM.md SEC-03, SEC-05).

## Principles

- **Modular execution first.** Compressor packages are modularized for shop assembly and field-installed in three pieces inside self-framing buildings. The CWP shall preserve the module-set sequence and minimize field rework (Source: 3-25_Comp_and_Liquids_DBM.md SEC-05).
- **Sour-service rigor.** All construction practices for sour-service piping, joint integrity, and pressure testing follow the governing sour-service specifications. Material substitution and field repairs require documented engineering approval (Source: 3-25_Comp_and_Liquids_DBM.md SEC-03 sour-gas basis).
- **Geotechnical gating.** Foundations and subgrade work are gated by acceptance of the final geotechnical report. DBM placeholder values shall not be construed as closed construction criteria (Source: 3-25_Comp_and_Liquids_DBM.md SEC-03).
- **Workface planning.** Execution is organized at the workface level so that each module set, hookup, tie-in, and turnover boundary is a planned, resourced, and verifiable unit (ASSUMPTION based on _CONTEXT.md anticipated workface plan).
- **Interface discipline.** Construction interfaces — vendor packages, shared utilities, shared flares/incinerator, and 04-25 boundary — are managed via an explicit construction interface register feeding the turnover checklist (Source: 3-25_Comp_and_Liquids_DBM.md SEC-03 shared utilities; _CONTEXT.md anticipated artifacts).

## Considerations

- **Vendor package boundaries.** Mechanical hookups to vendor-supplied compressor and TEG packages occur at vendor-defined interface points. The CWP should reflect the vendor-engineered equipment package (DEL-048-04) terminals (ASSUMPTION; cross-deliverable reference).
- **Shared utilities from 04-25.** Instrument air, and shared flare/incinerator routing originate at 04-25 under SCA-006. Construction sequencing must respect availability windows for these cross-facility services (Source: 3-25_Comp_and_Liquids_DBM.md SEC-03).
- **Electrical sequencing.** Two 5,200 hp motors and the VFD starting basis (SCA-001 VE #34) impose substantial electrical infrastructure scope; energization and motor solo-run sequencing requires substation/MCC readiness ahead of mechanical run-in (Source: 3-25_Comp_and_Liquids_DBM.md SEC-05).
- **Demolition restraint.** Demolition is restricted to that strictly necessary for project tie-ins; brownfield disturbance beyond scope is avoided (Source: 3-25_Comp_and_Liquids_DBM.md SEC-03).
- **Cold-weather and northern BC climate.** Site is in northern BC near Dawson Creek; cold-weather construction provisions are warranted but specific allowances are TBD against project execution standards (location TBD).
- **Turnover boundaries.** Mechanical-completion subsystems should map cleanly to the commissioning system breakdown to avoid orphan punch items at turnover (ASSUMPTION based on standard EPC practice).

## Trade-offs

- **Module reassembly speed vs. quality holds.** Faster module hookup risks deferring NDE/hydrotest closure; CWP should pre-stage ITPs to keep quality holds short without skipping them.
- **Parallel workface density vs. safety footprint.** Running multiple workfaces in the compressor bays at once increases throughput but constrains hot-work permitting and H2S exclusion zones during commissioning approach.
- **Local fabrication vs. shop-built spools.** Greater shop content reduces field labor risk but constrains field flexibility for IFC revisions; CWP should set a default toward shop-built spools for sour-service piping (ASSUMPTION based on sour-service rigor principle).

## Examples

- Module-set sequence example: receive KM-2150 base, mid, and roof sections; set base on foundation; bolt mid section; weld interconnecting piping; set roof; commission HVAC and lighting; release for mechanical hookup (illustrative; derived from modularization basis in 3-25_Comp_and_Liquids_DBM.md SEC-05; specific lift plan TBD).
- Tie-in window example: plant inlet pipeline tie-in at the first aboveground flange within the lease boundary is sequenced after Doe-field pipeline contractor handover and before inlet ESDV functional test (Source: 3-25_Comp_and_Liquids_DBM.md SEC-04).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CT-01 | 26020-Package_Requirements.docx package heading 3 is cited as the authoritative package-requirements source but is a binary .docx not parsed in this pass; some CWP-content mandates may be missing. | _REFERENCES.md / _CONTEXT.md cite docx | DBM SEC-03/05 (used as proxy) | Specification R-* set; Datasheet Construction row | PROPOSAL: parse .docx into a source slice and re-run Pass 2 | TBD |
| CT-02 | Package-heuristic objective mapping (OBJ-001, OBJ-003..010) is treated as ASSUMPTION; explicit deliverable-level objective mapping not confirmed. | _CONTEXT.md Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv (not deliverable-row resolved) | Datasheet Attributes | PROPOSAL: confirm or supersede with explicit deliverable-level mapping | TBD |
