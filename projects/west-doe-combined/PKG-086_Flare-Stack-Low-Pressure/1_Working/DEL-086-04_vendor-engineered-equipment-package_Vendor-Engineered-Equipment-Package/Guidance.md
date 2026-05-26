# Guidance — DEL-086-04 Vendor Engineered Equipment Package

## Purpose

DEL-086-04 exists so that a single Package Vendor production unit converts the EPC-side anchor deliverables (`DEL-086-01` Scope of Work and `DEL-086-02` Package Datasheet) into the engineered, fabricated, and supplied physical Flare Stack (Low Pressure) package. It is the "vendor-side" anchor for PKG-086, intentionally separated from EPC integration (handled by `DEL-086-06`) and from vendor turnover documentation (handled by `DEL-086-05`). (`_CONTEXT.md` Notes; `PACKAGE_REGISTER.csv` row 59 — FACT)

## Principles

- **Vendor scope vs. EPC integration scope is a hard line.** The vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (`PACKAGE_REGISTER.csv` row 59 PrimaryResponsibilities — FACT)
- **The LP flare is one element of a shared dual-stack system.** PKG-086 is the LP element of an HP/Cryo + LP dual flare stack shared between 03-25 and 04-25 with an unresolved service-split allocation. Treat the 03-25/04-25 service split as an open interface item until source language resolves it. (DBM lines 56, 497 — FACT)
- **Anchor on the EPC datasheet, not on the budgetary go-by.** The self-supported dual flare stack budgetary pdf is explicitly tagged as "budgetary pricing/delivery go-by only" in PACKAGE_REGISTER row 59 and must not be treated as design authority. (FACT)
- **Staggered blowdown limits the package, not just the relief network.** Vendor sizing of stack and tip must remain consistent with the facility's staggered blowdown intent and the eventual W242510-PRC-REP-000003-001 outcome. (DBM line 501 — FACT)

## Considerations

- The LP relief header is carried at 508 mm / 20 in in the current source basis; the LP stack OD is explicitly TBD. Vendor sizing iterations should clearly carry these provenance pointers so that downstream piping, structural, and emissions reviews can update consistently. (DBM line 499 — FACT)
- The LP flare receives TEG regeneration, VRU, and compressor seal-pot services — meaning the vendor cannot assume a single clean service. Materials, drainage, and tip selection must accommodate this service mix. (DBM line 499 — FACT)
- Sour-service exposure is real (TEG regen offgas, seal-pot routing); isolation philosophy and materials should be evaluated against NACE MR0175 / ISO 15156 (ASSUMPTION: standards likely applicable; not enumerated in accessible source) and against the DBM isolation requirements at lines 605–611 (FACT).
- Foundation/structural design must use the project geotechnical and civil basis; flare stacks are explicitly called out as requiring equipment-specific foundation and anchorage checks. (DBM line 700 — FACT)
- The associated LP flare stack blower is in package scope per PACKAGE_REGISTER row 59. Vendor must treat the blower as inside its engineering boundary, not as a separate utility tie-in. (FACT)
- Coordination must be active with PKG-086's EPC anchor deliverables (`DEL-086-01`, `DEL-086-02`) and the review deliverable (`DEL-086-06`).

## Trade-offs

- **Tip selection vs. service mix.** A single tip simplifies vendor scope but may force conservatism for the mixed LP service (TEG regen + VRU + seal pots). A combined / staged tip improves turndown but adds vendor complexity. Decision basis is TBD until vendor proposes.
- **Self-supported vs. guyed/derrick stack.** Budgetary go-by indicates a self-supported dual stack (24292-02-PT-ENR-25-201, location TBD); final selection depends on plot space, wind/seismic loads, and dual-stack integration. ASSUMPTION pending vendor study.
- **Vendor-supplied vs. facility-supplied KO drum.** Current DBM line 499 assigns LP KO drum V-3900-2 and pump P-3900-2 to the facility/upstream side. Moving these into vendor scope would simplify integration but expand vendor scope. (FACT — current allocation; alternatives PROPOSAL only.)

## Examples

The DBM equipment summary explicitly lists LP flare KO drum transfer pump count as "1 × 100%" (line 584 — FACT). Vendor design and sparing philosophy should remain consistent with this facility-side sparing decision even though those items are not vendor-owned.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-01 | OBJ-002, OBJ-004…OBJ-010 association uses PACKAGE_HEURISTIC; objective mapping at deliverable-ID granularity not confirmed | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07) | Datasheet Identification; Specification Scope | Treat as ASSUMPTION until human confirms | TBD |
| CFL-02 | 03-25 / 04-25 service split for HP/Cryo + LP dual flare stack is open per DBM line 56 | DBM §3-25 Comp/Liquids line 56 | EPC-side `DEL-086-01` SOW (not yet drafted) | Specification R-06; Guidance Principles | Carry as open interface; vendor scope must accept either allocation | TBD |
| CFL-03 | LP stack OD is TBD in source; sizing required by vendor | DBM line 499 ("LP stack OD remains TBD") | Budgetary self-supported dual flare stack pdf (location TBD) | Datasheet Attributes; Specification R-07 | Vendor sizing study; do not adopt budgetary go-by as authority | TBD |
| CFL-04 | `26020-Package_Requirements.docx` package heading 39 is named as governing but not locally text-extracted | `_CONTEXT.md`; `_REFERENCES.md` | (no local extraction) | All four documents | Resolve via PREPARATION source-slice extraction before downstream gates | TBD |
