# Guidance — Vendor Engineered Equipment Package (DEL-089-04)

## Purpose

DEL-089-04 carries the **Package Vendor production unit** for PKG-089 Pig Receivers (Inlet) 3-25 — the vendor's engineering, design, fabrication/supply, and the resulting physical equipment package. The deliverable exists to make vendor scope a first-class production unit (per OBJ-004), distinct from EPC Integrator scope (Scope of Work, Package Datasheet, Construction Work Package, Acceptance), so that vendor responsibilities are not silently merged into EPC deliverables (DELIVERABLE_REGISTER.csv DEL-089-04; OBJ-004).

It is downstream-routed from the EPC Scope of Work (DEL-089-01) and EPC Package Datasheet (DEL-089-02), and upstream of EPC Vendor Package Review and Acceptance (DEL-089-06) (per `_CONTEXT.md` scope text and DELIVERABLE_REGISTER.csv).

## Principles

- **Vendor owns engineering and design**, not just supply. The vendor is expected to produce a coherent design basis and datasheet set that the EPC can integrate against, not just hardware (OBJ-004; ART-6017932F95).
- **Source-anchored equipment list**. The 24 in (610 mm) OD twin-receiver configuration, ESDV-upstream arrangement, sweet-gas purge, and HP flare vent are stated in the project source (SOW-0158; SOW-0159). The vendor design must preserve this configuration; deviations require explicit EPC ruling.
- **Pressure and temperature envelope is fixed by the source**. The MAOP/MAWP and ambient design temperatures (SOW-0160) are project facts, not vendor selections.
- **Sour service is non-negotiable**. The receivers handle plant inlet sour gas; sour-service material and component selection is required (SOW-0159; OBJ-009).
- **Clear battery limits**. Interconnecting piping, DCS integration, foundations, and MCC electrical supply are explicitly "by others" (SOW-0160). The vendor design basis must expose the interface points cleanly.
- **Two-track documentation**. The *vendor design basis and datasheet set* lives in this deliverable (ART-6017932F95). The *vendor document turnover register and submittals* live in DEL-089-05. These two should not be confused.

## Considerations

- **Throughput interpretation**: 80 MMSCFD is a package design throughput (SOW-0160); per-receiver normal flow is TBC. The vendor sizing approach (e.g., one duty / one spare, parallel split, or alternating service) is not specified in source and is an open vendor design decision — TBD with EPC concurrence.
- **End-closure type and pig handling features** (quick-opening closure, pig signaller, kicker line, drain) are not enumerated in the accessible source slices. The vendor design must propose these consistent with industry practice and the project sour-service philosophy.
- **Purge philosophy**: Source specifies sweet-gas purge downstream of a manual isolation valve before opening for pig retrieval (SOW-0159). Operator pig-retrieval procedure (in DEL-089-03 Construction Work Package and project operating procedures) must align with this purge arrangement.
- **Vent to HP flare** (SOW-0159) requires the vendor to coordinate vent line sizing, set pressure, and back-pressure assumptions with the EPC flare-system design (cross-package interface, OBJ-007 utilities and OBJ-009 safety/relief/flare).
- **Skid layout**: "non-enclosed skid" (SOW-0158) implies outdoor exposure under the ambient design range (-40 to +35 °C). Winterization, EHT (heat tracing), and weather protection of skid-mounted instrumentation must be considered (OBJ-005 electrical infrastructure / EHT; OBJ-010 winterization).
- **Maintainability**: Pig handling, valve actuation access, and ESD test access must be considered consistent with OBJ-010 (operability/maintainability).

## Trade-offs

- **Vendor standard product vs project-specific design**: Vendor catalog skids may reduce cost and schedule but may not match the exact ESDV-upstream, vent-to-HP-flare, and sweet-gas purge configuration required by SOW-0159. Configuration faithfulness should not be traded against schedule without EPC ruling.
- **Single vs split sour-service material strategy**: Selecting fully NACE-compliant materials throughout vs zoning by partial-pressure analysis. The source defines 0.1 mol% H2S design (SOW-0159) but does not state the partial-pressure or zoning approach (TBD).
- **Quick-opening closure type** (e.g., threaded vs clamp vs hinged): trade-off between operator ergonomics, sealing reliability, and cost. Not specified in source.

## Examples

No worked examples are available from the accessible sources. Worked examples (e.g., from prior project executions or vendor reference installations) are TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none identified) | No cross-source conflicts identified within accessible source slices during Pass 2. Conflicts may surface once DEL-089-01 (Scope of Work) and DEL-089-02 (Package Datasheet) are drafted. | — | — | — | — | TBD |
