# Guidance — DEL-070-01 Scope of Work (PKG-070 Mole Sieve Drier Unit (NGL))

> Directional guidance for drafting and using the EPC Integrator Scope of Work
> for the NGL Mole Sieve Drier Unit. This document explains *why* the Scope of
> Work is shaped as it is, what trade-offs the decomposition embeds, and where
> to be careful when the accessible source slices are sparse.

## Purpose

The Scope of Work (SoW) for PKG-070 exists to define the EPC Integrator's
binding statement of what the NGL Mole Sieve Drier Unit package is, what it
must do at the facility level, where its boundaries sit, and how
responsibilities are split between the Package Vendor and the EPC Integrator.
It is the upstream anchor for the Package Datasheet (DEL-070-02), the
Construction Work Package (DEL-070-03), the Vendor Engineered Equipment
Package (DEL-070-04), the Vendor Document Turnover Package (DEL-070-05), and
the EPC Vendor Package Review and Acceptance (DEL-070-06). (Source:
`DELIVERABLE_REGISTER.csv` rows for PKG-070; `_CONTEXT.md` Notes — "Mandatory
Gate 5 EPC anchor deliverable".)

## Principles

1. **Decomposition routes; source determines.** The SoW MUST stay grounded in
   the GATE-07 PROJECT_DECOMP snapshot for identity, scope, interfaces, and
   objective mapping, and in the underlying source documents
   (`26020-Package_Requirements.docx` heading 24 and
   `26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx`) for technical content.
   When the underlying source is not locally accessible, do not invent
   technical content — mark it **TBD** or **location TBD**.
2. **Respect the vendor/EPC split.** PKG-070 is a vendor-engineered package
   (OBJ-004). The SoW must scope vendor engineering and supply at the package
   level and integrator scope at the facility/interface level. Do not write
   detailed vendor design requirements into the SoW — those belong in the
   Package Datasheet (DEL-070-02).
3. **Liquid-phase service is distinct from gas-phase sieve service.** The DBM
   SEC-06 describes the *process-gas* molecular-sieve dehydration system,
   which uses two-on-line / one-in-regeneration on a 332.6 MMSCFD gas duty.
   PKG-070 is the *NGL* (liquid-phase) molecular-sieve package, three-tower
   one-on-line / one-regeneration / one-standby at 2,385 m³/d (15,000 bbl/d)
   of C3+ liquid (SCOPE_LEDGER SOW-0146). Do not transcribe gas-system
   design values into the NGL SoW.
4. **Exclusions are part of the scope.** The "by others" list in SCOPE_LEDGER
   SOW-0148 is binding negative scope and SHALL appear in the SoW.
5. **Interface coverage is comprehensive.** All twelve PKG-070 interface
   types in INTERFACE_REGISTER must be acknowledged, even when the package
   has no active scope on a particular interface — the SoW should state
   responsibility for the tie-in, not avoid the interface.

## Considerations

- **Source accessibility.** The NGL-specific RFQ
  (`26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx`) is referenced by
  PACKAGE_REGISTER but not present in `_Sources/`. The DBM (Deepcut) is
  available and is the closest analogous source, but it is gas-service.
  Treat DBM SEC-06 as ASSUMPTION for any NGL-package detail and confirm
  during downstream deliverables.
- **Cycle-time openness.** Adsorption cycle is preliminarily 24 hours; the
  remaining cycle phases (draining, heating ramp, regeneration pre-heat/hold,
  heating, cooling, filling, standby, total regeneration) are explicitly
  TBC by vendor (SCOPE_LEDGER SOW-0148). The SoW should preserve this as an
  open item rather than pre-empt the vendor.
- **Regeneration-side conditions.** The accessible source slice truncates at
  "Regeneration side. Design conditions:" without enumerated values. The SoW
  should mark this as TBD and route the resolution to the Package Datasheet
  workstream.
- **Heated enclosure scope.** Whether the heated enclosure is required and
  what it must house depends on final heater/scrubber location and area
  classification (SCOPE_LEDGER SOW-0147). The SoW should not over-constrain
  enclosure scope in advance of the area-classification deliverable.
- **Outlet specification firmness.** The < 7 ppmw NGL outlet water spec is
  stated firmly in SCOPE_LEDGER SOW-0146 and is the single most consequential
  performance number in the SoW.

## Trade-offs

- **Detail vs. vendor latitude.** Pushing too much equipment detail into the
  SoW (e.g., specific vessel sizes, valve models) compresses vendor design
  latitude and risks conflicting with the Package Datasheet. Pushing too
  little risks an under-bounded RFQ. Default position: include items
  enumerated in SCOPE_LEDGER SOW-0147 (function-level) and stop there;
  defer dimensional/material specifics to DEL-070-02.
- **Carrying TBDs vs. resolving them upstream.** TBDs that depend on the
  inaccessible RFQ source slice should be carried explicitly in the SoW and
  surfaced for procurement, rather than guessed.
- **Interface-by-interface scope vs. integration-narrative scope.** Twelve
  interfaces is a lot to enumerate clause-by-clause. Prefer a single
  integration narrative that covers the twelve types as a matrix appendix.

## Examples

- **Capacity statement.** "The package shall be one (1) NGL molecular sieve
  dehydration package, three-tower configuration (one tower in adsorption,
  one in regeneration, one on standby), rated 2,385 m³/d (15,000 bbl/d),
  processing water-saturated C3+ NGL to an outlet water content less than
  7 ppmw." (Source: SCOPE_LEDGER SOW-0146.)
- **Exclusion statement.** "By others: upstream NGL mercaptan treating
  process package and caustic process-provider design; downstream NGL
  storage bullets, NGL loading, LACT, and product export systems; sales gas
  compressors and stabilizer overheads compressor package; produced-water
  tank, produced-water drain header, and facility drain infrastructure
  beyond package nozzles/tie-ins; flare header." (Source: SCOPE_LEDGER
  SOW-0148.)
- **Cycle-basis statement.** "Adsorption cycle: 24 hours (preliminary).
  Draining, heating ramp, regeneration pre-heat/hold, heating, cooling,
  filling, standby, and total regeneration cycle: TBC by vendor." (Source:
  SCOPE_LEDGER SOW-0148.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Regeneration-side design conditions are referenced ("Regeneration side. Design conditions:") but no values follow in the accessible source slice. | `SCOPE_LEDGER.csv` SOW-0148 (truncated) | `26020-Package_Requirements.docx` heading 24 — not locally accessible | Specification R-4.4; Datasheet "Regeneration-side conditions" | Carry as TBD in SoW; resolve in DEL-070-02 Package Datasheet using NGL RFQ when accessible. | TBD |
| C-02 | Package-specific exclusions field in PACKAGE_REGISTER reads "TBD; no package-specific exclusions stated in source materials", while SCOPE_LEDGER SOW-0148 enumerates substantial "by others" exclusions. | `PACKAGE_REGISTER.csv` row PKG-070 (Exclusions) | `SCOPE_LEDGER.csv` SOW-0148 | Datasheet "Excluded by others"; Specification §Scope/Out of scope; Specification R-6 | Treat SCOPE_LEDGER SOW-0148 as authoritative (richer, source-grounded); reconcile PACKAGE_REGISTER text downstream. | TBD |
| C-03 | DBM SEC-06 prohibits 4A/5A molecular sieve and requires 3A for *process-gas* service. SCOPE_LEDGER SOW-0147 specifies 3A for the NGL package without restating the prohibition. | DBM SEC-06 (process-gas) | SCOPE_LEDGER SOW-0147 (NGL) | Specification §Standards; Datasheet "Adsorbent type" | Carry 3A as a requirement; carry the 4A/5A prohibition as ASSUMPTION until confirmed by NGL RFQ. | TBD |
| C-04 | Source basis cites both `26020-01-PT-RFQ-22-003_NGL-Mole-Sieve-Dehy.docx` and `DBM-Deepcut/4-25_Deepcut_DBM.md` for PKG-070; the latter describes gas-phase service. | `PACKAGE_REGISTER.csv` SourceRefs | DBM SEC-06 content vs SCOPE_LEDGER NGL content | All four documents | Treat the NGL RFQ as authoritative when accessible; treat DBM as analogous/ASSUMPTION only. | TBD |
