# Guidance — DEL-061-01 Scope of Work (PKG-061 NGL Booster and Transfer Pumps Building)

## Purpose

This Scope of Work establishes, on the EPC Integrator's authority, the package identity, function, boundaries, and responsibility assignment for PKG-061 (NGL Booster and Transfer Pumps Building) at the West Doe 4-25 Deepcut facility. It is the Gate 5 anchor deliverable defining what the Package Vendor must engineer, design, fabricate, and supply, and what the EPC Integrator must integrate into the larger facility (foundations, MCC supply, DCS, tie-ins). [Source: DELIVERABLE_REGISTER.csv DEL-061-01; SOW-0149]

## Principles

1. **Package Vendor owns the pumps; EPC Integrator owns the facility.** This split derives directly from SOW-0149 and is reflected in the SOW-0152 exclusion list (DCS, foundations, MCC supply by others). All ambiguity at the boundary should be resolved in favour of explicit, documented assignment.

2. **Heading 17 of 26020-Package_Requirements.docx is the authoritative source basis.** The Basic scope, Major included equipment, and Scope notes are the source slice. Tagged equipment names, hydraulic sizing values, regulatory references, and exclusions originate there and are not to be invented elsewhere.

3. **The package function is transfer to LACT.** The pumps boost product from NGL/LPG storage to the LACT unit where booster pressure may be required. Because LACT scope/ownership is TBD at the facility level (DBM-Deepcut lines 62, 82), the package design must remain compatible with both LACT-included and LACT-excluded resolutions until the project rules on it.

4. **API 610 / API 682 governs the pumps.** Vertical multistage can-type construction with seal plan 13/52 is mandated by SOW-0151 and reinforced by the DBM-Deepcut equipment table. Departures from API 610/682 should be treated as deviations.

5. **Source-grounded language.** Where heading 17 does not state a value (e.g., TDH, suction conditions, NPSHA), the Scope of Work records TBD rather than inventing a value.

## Considerations

- **Conflict between "LPG" and "NGL" terminology.** Heading 17 uses "LPG booster pumps" while the package name and facility process basis use "NGL". Per DBM-Deepcut line 139, current-scope terminology is NGL; legacy LPG framing is a documentation artefact. This package should be referred to as the NGL Booster and Transfer Pumps Building in EPC communications, with LPG retained only when quoting the source.
- **2 x 100% vs 150% capacity.** The DBM-Deepcut equipment table shows two pumps. SOW-0152 specifies sizing at "145 m3/h at 150% capacity". The reading consistent with both sources is two parallel pumps each rated at 145 m3/h, each sized to 150% of facility design transfer flow — analogous to the condensate transfer pump basis (DBM-Deepcut line 1675: "sized for at least 150% of facility design flow ... so tanks can be pumped down quickly"). This is captured as ASSUMPTION until the vendor curve and facility hydraulic study confirm.
- **Driver voltage.** 575 V is a non-standard rotating-equipment voltage for many North American sites and may indicate vendor-package electrical isolation transformers. The MCC supply is by others (SOW-0152), so the EPC Integrator must coordinate voltage and starter type with the facility electrical basis.
- **CRN/TSBC.** CRN registration is mandatory for pressure-containing components in Canadian jurisdictions. TSBC is the BC Technical Safety BC framework; jurisdiction-applicable equivalents (e.g., ABSA in Alberta) are an ASSUMPTION pending facility-location confirmation.
- **NPSH risk.** DBM-Deepcut line 1677 notes that the condensate analogue has very tight NPSH constraints. NGL pumps drawing from storage bullets have additional vapour-pressure considerations; NPSHA shall be confirmed by the EPC Integrator at the suction flange before vendor selection is locked.

## Trade-offs

- **Single can-style multistage pumps vs horizontal multistage.** API 610 BB5/VS6 multistage cans give superior NPSH performance and a small footprint suited to a packaged building, at the cost of higher capital and longer lead time. Heading 17 selects can-type, accepting the cost/lead penalty for the NPSH advantage at NGL service.
- **Plan 13/52 seal arrangement.** Plan 13 (recirculation from seal chamber back to suction) plus Plan 52 (unpressurized external buffer fluid) is a common API 682 Category 1/2 arrangement for low-vapour-pressure light-end services. It is less protective than a Plan 53A/53B pressurized barrier system; selection trades emissions/leak protection against complexity and is presumed source-justified by NGL service severity. Detailed engineering should confirm against the latest emission and HSE requirements.
- **LACT inclusion timing.** Deferring the LACT decision allows pump procurement to begin against the conservative discharge envelope, but risks rework if the LACT pressure profile materially differs from the assumed booster design differential of 25 psid.

## Examples

- **Analogous facility unit — condensate transfer pumps P-9210-1/P-9220-1.** DBM-Deepcut line 1673 describes a 2 x 150% sized configuration delivering 350 kPad / 50 psid to the liquids hub. The NGL booster pumps follow the same pattern (parallel, oversized for pump-down) at lower differential (172 kPad / 25 psid) for the shorter NGL-to-LACT route.
- **Analogous standby logic.** The condensate transfer system permits both pumps to operate simultaneously for high pump-down. Whether NGL booster operation is normal-one-running or normal-both-running is TBD and should be set by the EPC Integrator in coordination with the LACT operating envelope.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-061-01-01 | LPG vs NGL nomenclature for the same package | 26020-Package_Requirements.docx heading 17 ("LPG booster pumps") via SOW-0150/0151 | DBM-Deepcut line 139 (current-scope NGL terminology supersedes legacy LPG) | Datasheet attributes; Specification R-1, R-2; Guidance Principle 3 | Use NGL in EPC-facing language; retain LPG only when quoting heading 17 source | TBD |
| CT-061-01-02 | LACT inclusion vs exclusion at facility level | DBM-Deepcut line 62 (LACT TBD; current scope contains both LACT inclusion and exclusion) | DBM-Deepcut line 82 (LACT units excluded from DBM scope) and DBM-Deepcut line 57 (NGL via LACT) | Specification R-12; Datasheet conditions (downstream connection) | Hold pump discharge envelope at 25 psid booster differential per SOW-0152; revisit when project rules on LACT | TBD |
| CT-061-01-03 | Per-pump flow basis "145 m3/h at 150% capacity" wording | SOW-0152 | DBM-Deepcut equipment table line 2609 (2 pumps, no flow value) | Specification R-4; Datasheet conditions | Read as each pump = 145 m3/h, each at 150% of facility design transfer flow (analogue to condensate transfer pump basis DBM-Deepcut line 1675) | TBD |
| CT-061-01-04 | Motor voltage 575 V vs facility MV/LV standards | SOW-0151 (575 V, 3-phase, 60 Hz) | DBM-Deepcut electrical basis (LV/MV at 4,000 V for large motors; line 505) | Specification R-5; Datasheet electrical conditions | Confirm with facility electrical SLD; 575 V suggests vendor LV package with isolation transformer | TBD |
