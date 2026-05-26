# Specification — DEL-056-03 Construction Work Package (PKG-056)

## Scope

This Construction Work Package (CWP) defines how the PKG-056 Inlet Separators 4-25 vendor-supplied package shall be physically installed, mechanically completed, inspected, tied into the larger 04-25 facility, and turned over to operations. It covers:

- Receipt, offloading, and setting of the vendor-supplied package (two installed inlet separators plus future-plot provisions per the current governed package basis).
- Foundations, structural supports, and grading prepared by Tourmaline field construction scope.
- Mechanical hookup of the package to the facility, including process piping, utility piping, relief/flare/vent, drain/containment, EHT, grounding/bonding, area lighting, I&C and control cabling, and fire & gas/safety systems tie-ins.
- Field installation of shipped-loose instruments, valves, and components.
- Mechanical completion, inspection, testing, and operational turnover activities.

Out of scope (owned by Package Vendor or other deliverables):
- Package engineering, package design, and vendor documentation (Package Vendor — PACKAGE_REGISTER.csv PKG-056).
- Cryogenic, amine, NGL, VRU, fuel-gas, heat-medium, flare, drain, and downstream utility/product systems beyond the documented PKG-056 tie-in interfaces.

## Requirements

### R-1 — Construction responsibility allocation

R-1.1 Field construction shall be executed by Tourmaline Oil Corporation per DBM SEC-01 Construction Responsibility scope, covering construction management; grading, piling, and foundation work; setting modules and equipment on foundations; mechanical hookup; installation of shipped-loose instruments, valves, and components; installation of miscellaneous structural supports; field installation of home-run cables; electrical terminations; and area lighting. (Source: DBM SEC-01.)

R-1.2 Installation of interconnecting piping to ISBL/OSBL tie-in points is an external interface activity; the responsibility for each individual tie-in shall be confirmed in the workface plan prior to execution. (Source: DBM SEC-01.)

### R-2 — Vendor package interface conformance

R-2.1 The installed configuration shall match the governed package register basis: two (2) identical horizontal three-phase HP inlet separators (9 ft ID x 40 ft S/S), with plot provision preserved for a future third separator. Any deviation requires a documented change against PACKAGE_REGISTER.csv PKG-056. (Source: PACKAGE_REGISTER.csv PKG-056; DBM SEC-04.) ASSUMPTION (best-effort mapping): aligned to current body basis pending resolution of legacy 4-package conflict (see Guidance Conflict Table).

R-2.2 The Construction Work Package shall implement all applicable tie-in interface types listed in PACKAGE_REGISTER.csv PKG-056: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports.

### R-3 — Receipt and handling

R-3.1 Offloading of modules and equipment at site shall be Tourmaline field construction scope; offloading methods, lifting plans, and rigging studies are TBD by the CWP and must be issued prior to mobilization. (Source: DBM SEC-01.)

R-3.2 Vessel internal coating (Devchem 253) condition shall be inspected on receipt and protected during all handling, storage, and installation operations. (Source: DBM SEC-04.)

### R-4 — Foundations and supports

R-4.1 Foundations, piling (where required), grading, and miscellaneous structural supports shall be in place and accepted prior to package setting. (Source: DBM SEC-01.)

R-4.2 Foundation alignment tolerances, anchor-bolt setting, and grouting requirements are TBD pending vendor general arrangement and foundation design drawings.

### R-5 — Mechanical hookup

R-5.1 Process piping hookup at separator inlets shall preserve the symmetrical inlet distribution intent of DBM SEC-04 and shall not introduce uneven gas/liquid distribution between separators. (Source: DBM SEC-04 / Inlet Separation.)

R-5.2 At minimum two parallel balanced-globe inlet pressure control valves shall be installed and aligned per separator with hardened trim where recommended. Skid-edge inlet isolation shall enable PCV maintenance without blowing down the full separator. (Source: DBM SEC-04 / Inlet Separator Design Parameters.)

R-5.3 The liquid outlet heater on each inlet separator package shall be installed, hooked up to heat medium per the selected heating medium basis, and verified for the cold-liquid heating duty. Final heat-medium identity is TBC (DBM SEC-04 notes warm glycol or process-stream cross-exchange as candidates).

R-5.4 Methanol injection points upstream of each inlet separator shall be installed where indicated, to support hydrate suppression during two-phase inlet conditions. (Source: DBM SEC-04.)

### R-6 — Tie-ins

R-6.1 Each tie-in shall be executed under an isolation, lockout, hot-work, and confined-space permit set as appropriate to the system state at the time of cut-in. (ASSUMPTION: standard EPC practice; no project-specific permit-to-work standard reviewed in this run — location TBD.)

R-6.2 Tie-in welds shall be inspected per the applicable piping code class for the affected service. The governing piping code/class for each tie-in is TBD in deliverable-local sources.

R-6.3 The CWP shall identify each tie-in by interface ID and include a construction interface and turnover checklist entry per `_CONTEXT.md` Anticipated Artifacts.

### R-7 — Electrical, I&C, and safety systems

R-7.1 Field installation of home-run cables and electrical terminations shall be performed by Tourmaline construction scope; tray/conduit routing, cable schedules, and termination drawings are TBD. (Source: DBM SEC-01.)

R-7.2 Fire & Gas/Safety Systems interface devices identified at the package boundary shall be connected, functionally tested, and integrated into the 04-25 plant safety system before turnover.

R-7.3 Grounding/bonding of vessels, piping, and skids shall be installed and verified per the applicable site standard (location TBD).

### R-8 — Pressure testing and mechanical completion

R-8.1 All site-installed pressure-containing piping shall be pressure tested in accordance with the applicable code (TBD pending governing piping code reference).

R-8.2 Cleanliness, flushing, and dry-out activities shall be defined in the CWP prior to introduction of hydrocarbons.

R-8.3 Mechanical completion shall be documented per system using check sheets aligned to the construction interface and turnover checklist artifact.

### R-9 — Documentation and turnover

R-9.1 The CWP shall produce, at minimum, the anticipated artifacts in `_CONTEXT.md`: a construction work package, an installation and tie-in workface plan, and a construction interface and turnover checklist.

R-9.2 Red-line as-built mark-ups shall be captured for all field changes and forwarded to engineering for incorporation into as-built drawings.

R-9.3 Turnover packages shall provide the operations team with all tests, inspections, calibrations, and punch-list dispositions required to accept the system.

## Standards

The following standards are stated or implied by reference; clause-level requirements are location TBD until source slices are obtained:

- DBM-Deepcut SEC-01, SEC-04 (project Design Basis Memorandum) — local source.
- 26020-Package_Requirements.docx package heading 11 — referenced by `_CONTEXT.md` and DELIVERABLE_REGISTER; binary not directly readable in this run (location TBD).
- Governing piping code (e.g., ASME B31.3 or equivalent) — ASSUMPTION; not explicitly named in local sources reviewed.
- Welding, NDE, hydrostatic testing, electrical, grounding, and hazardous-area standards — TBD; not extracted from local sources in this run.

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Cross-check construction execution against DBM SEC-01 responsibility table; record exceptions in red-line. |
| R-2 | Configuration audit against PACKAGE_REGISTER.csv PKG-056; deviation report against governed basis. |
| R-3 | Receipt inspection report; coating inspection check sheet. |
| R-4 | Foundation acceptance check sheet; alignment survey (criteria TBD). |
| R-5 | Mechanical hookup check sheet; PCV alignment and stroke test; heater leak/loop test. |
| R-6 | Tie-in register signed off per interface; weld NDE records. |
| R-7 | Cable continuity and megger records; F&G loop test; ground continuity test. |
| R-8 | Pressure test packages; flushing and cleanliness sign-offs. |
| R-9 | Turnover package acceptance by operations. |

## Documentation

Required artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Construction work package (this deliverable set).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Supporting artifacts (TBD; produced inside this deliverable folder during execution):

- Receipt and offloading procedures and lift plans.
- Mechanical completion check sheets and ITP.
- Pressure-test packages and certificates.
- As-built red-line set.
- Punch-list and turnover acceptance records.
