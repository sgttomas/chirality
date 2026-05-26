# Guidance: DEL-081-04 — Vendor Engineered Equipment Package (Flare KO Drum, High Pressure, 3-25)

> Directional guidance for the Package Vendor and the EPC Integrator reviewer working on the PKG-081 HP flare KO drum vendor-engineered package. This document captures purpose, principles, considerations, and trade-offs that shape the engineering choices but are not by themselves normative.

## Purpose

The package exists to convert the EPC-issued Scope of Work and Package Datasheet (DEL-081-01, DEL-081-02) into an engineered, fabricated, supplied physical HP flare KO drum package suitable for installation under the Construction Work Package (DEL-081-03), and for downstream review/acceptance (DEL-081-06) and turnover (DEL-081-05). The HP flare KO drum is a safety-critical asset on the 03-25 facility's HP relief path to the HP/Cryo dual flare stack, sized to remove entrained liquids from HP relief flow before flare combustion and to enable orderly liquid disposal via the associated transfer pump. `[SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md; SectionRef: Flare and Blowdown]`

## Principles

1. **Source-anchored design.** Vendor design choices shall be traceable to either the EPC Package Datasheet (when issued) or the governing DBM source slice. Where neither is available, choices are flagged as ASSUMPTION until validated.
2. **Safety-critical asset discipline.** Because the drum sits on a relief path, sizing, materials, instrumentation, and isolation philosophy decisions are conservative and explicitly traced.
3. **Staggered blowdown assumption.** The facility relief basis assumes staggered blowdown to bound maximum relief; the vendor shall not silently rely on a lower relief case than the assigned final flare study allocation. `[SourcePath: DBM; SectionRef: Flare and Blowdown — "Staggered blowdown is required..."]`
4. **Interface clarity.** The vendor scope ends at clearly defined battery-limit nozzles and terminations; the EPC Integrator owns the tie-in.
5. **Sparing fidelity.** One transfer pump per KO drum, 1 x 100 percent, per the project sparing basis. `[SourcePath: DBM; SectionRef: SEC-09 Sparing Philosophy]`

## Considerations

- **Tag identity.** Two HP KO drums are identified in the DBM — `V-4100-2` (compressor area) and `V-4150-2` (tank farm). The PKG-081 vendor production unit serves one of these. The vendor and EPC Integrator must confirm tag identity early; design implications include location-dependent inlet header geometry, liquid disposal routing, and footprint constraints. **NEEDS_HUMAN_RULING.**
- **Sour-service exposure.** The 03-25 facility handles sour streams. Material selection (including weld procedures and HIC/SSC mitigations) should be confirmed against the EPC Package Datasheet and the project materials specification, not assumed by analogy with other HP services. `[SourcePath: DBM; SectionRef: Isolation philosophy (line ~607)]`
- **Final flare-study dependence.** Rated relief load and design margin are downstream of the final flare studies (referenced as W242510-PRC-REP-000003-001, not available locally). Vendor sizing must be revisited if the final studies adjust the allocated relief case. **location TBD.**
- **Pump suction/NPSH.** Liquid hold-up volume and pump suction geometry should be designed for credible relief liquid loadings, including slugging from upstream collection legs.
- **Header rating alignment.** Inlet/outlet nozzle ratings should track the HP relief header (current source basis 508 mm / 20 inch). `[SourcePath: DBM; SectionRef: Flare and Blowdown]`
- **Instrumentation safe states.** Level transmitters and switches should fail in directions that protect the flare stack (avoid sending liquid to the flare) and protect downstream slop systems.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Skid-mounted vs site-erected | Skid mounting reduces field labor and integration risk but limits drum diameter / height; site erection enables larger vessels at the cost of more EPC field activity. The Package Datasheet should set the boundary. (ASSUMPTION; not yet sourced.) |
| Internal mist eliminator vs gravity-only separation | Mist eliminators improve droplet removal at the cost of pressure drop and fouling risk in flare service; gravity-only reduces fouling but requires larger drum volume. (ASSUMPTION; sizing study required.) |
| Single drum vs paired drums per facility area | The DBM basis is two HP KO drums (compressor area + tank farm) — a paired arrangement, each manifolded to the HP flare. The vendor package is one of the two. `[SourcePath: DBM; SectionRef: Flare and Blowdown]` |
| Truck-out vs piped transfer of liquids | DBM allows truck-out or transfer to slop. Site arrangement and operating philosophy drive the choice; vendor scope shall accommodate the Package Datasheet's selection. `[SourcePath: DBM; SectionRef: Flare and Blowdown]` |

## Examples

- HP KO drum `V-4100-2` in the compressor area: collects HP relief from compressor-area headers; pump `P-4100-2` (1 x 100 percent) handles liquid transfer.
- HP KO drum `V-4150-2` in the tank farm: collects HP relief from tank-farm headers; pump `P-4150-2` (1 x 100 percent) handles liquid transfer.

Both manifold to the HP/Cryo flare stack (sonic, 660 mm OD x 60,957 mm tall). `[SourcePath: DBM; SectionRef: Flare and Blowdown]`

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Equipment tag identity of the PKG-081 vendor production unit (V-4100-2 vs V-4150-2) | DBM Flare and Blowdown (lists both drums; does not bind one to PKG-081) | `_CONTEXT.md` / decomposition row (PKG-081 named "Flare KO Drum (High Pressure) 3-25" without tag) | Datasheet Identification/Attributes; Specification R-2; Procedure Steps | PROPOSAL: defer to the EPC Package Datasheet (DEL-081-02) when issued; current default treats the package as "an HP flare KO drum" | TBD |
| CT-02 | Rated relief case and sizing basis | DBM "staggered blowdown required" (qualitative) | Final flare studies W242510-PRC-REP-000003-001 (not available locally) | Specification R-4; Procedure verification | PROPOSAL: hold rated relief as TBD until the final flare study artifact is accessible; design margins per Package Datasheet | TBD |
| CT-03 | Sour-service classification | DBM mentions sour-service isolation considerations | Project materials specification (not directly read in this run) | Datasheet Design Conditions; Specification R-7 | PROPOSAL: treat as likely sour-service (ASSUMPTION) and confirm against EPC Package Datasheet | TBD |
