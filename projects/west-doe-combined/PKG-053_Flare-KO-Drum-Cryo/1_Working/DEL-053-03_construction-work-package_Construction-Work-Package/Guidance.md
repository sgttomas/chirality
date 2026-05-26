# Guidance — DEL-053-03 Construction Work Package (Flare KO Drum, Cryo)

## Purpose

This Guidance explains the rationale, principles, and trade-offs behind the Construction Work Package (CWP) for `PKG-053 Flare KO Drum (Cryo)`. The CWP exists to translate vendor-engineered equipment (`DEL-053-04`) and the package datasheet (`DEL-053-02`) into an executable, inspectable, and auditable construction scope that produces a Mechanical-Complete and start-up-ready installation suitable for EPC Vendor Package Review and Acceptance (`DEL-053-06`).

The cryogenic flare KO drum is a safety-critical relief-system asset; construction execution must preserve cleanliness, pressure-boundary integrity, and the cryogenic design intent (no internal water; no heat tracing on cryogenic relief headers) established by the design basis (`DBM-Deepcut §SEC-09 Flare`).

## Principles

1. **Source-grounded scope.** The CWP describes work derived from the IFC vendor package, the package datasheet (`DEL-053-02`), and the project DBM. Construction shall not invent new design content; design ambiguities are surfaced as RFIs back to engineering.
2. **Shop-built where possible.** Module `410-1 HP / Cryo Flare KO Drum Module` is shop-built (DBM-Deepcut §Modularization). The CWP scope at site is set, level, tie-in, and commission — not stick-build of the KO drum island.
3. **Cryogenic discipline.** Cryogenic relief service mandates dryness and prohibits heat-trace on cryogenic headers. Construction cleanliness, drying, and inspection protocols are scaled accordingly.
4. **Interface-first execution.** The package is mechanically and procedurally entangled with `PKG-054 Flare KO Drum (HP)` (co-mounted on module 410-1) and with the common 03-25 HP/cryo flare stack. Interface management is a first-class CWP element, not an afterthought.
5. **Turnover traceability.** Every requirement in the Specification maps to a verification evidence record retained in the turnover dossier (`R# → Records` map in Specification §Verification).

## Considerations

- **Module co-mounting (HP + Cryo).** Module `410-1` carries both HP and Cryo flare KO drum scope per DBM-Deepcut §Modularization. The CWP for `DEL-053-03` (Cryo) and the parallel CWP for HP (PKG-054 / `DEL-054-03`) must align on shared mechanical, structural, and turnover boundaries. ASSUMPTION: a single combined CWP for module 410-1 may be more efficient than two parallel CWPs; this is a method-level decision flagged for human ruling.
- **Cross-facility interface (04-25 ↔ 03-25 stack).** The cryo header ties into the HP/cryo header which routes to the common stack at 03-25. Tie-in ownership, scope split, isolation strategy during commissioning, and joint-test approach require an explicit interface agreement. The DBM notes the 03-25/04-25 allocation remains open in places (DBM-Deepcut §SEC-09 narrative); construction execution is exposed to this uncertainty.
- **No heat trace on cryogenic headers.** Heat-trace exclusion zones must be clearly marked on construction drawings and walked down. Misapplied heat trace would compromise cryogenic design intent.
- **PSV outlet free-drain.** HP flare PSV outlets free-drain into the flare header; the cryo system is dry. Construction slope verification on connected piping is a checkable item even for the cryogenic system (no traps).
- **Spacing compliance.** Spacing rules (OGAOM 9.6.15) constrain where vegetation, roads, and tanks can be relative to the installed flare/KO equipment — typically a plot-plan engineering concern, but a CWP walk-down item.

## Trade-offs

| Trade-off | Option A | Option B | Notes |
|---|---|---|---|
| CWP boundary at module 410-1 | One combined HP+Cryo CWP | Two separate CWPs (DEL-053-03, DEL-054-03) | Combined reduces interface overhead; separate preserves package-level ownership traceability. NEEDS_HUMAN_RULING. |
| Tie-in at 03-25 boundary | EPC scope ends at 04-25 lease boundary | EPC scope extends to common stack base | Affects construction contract scope and joint-testing approach; `location TBD` in DBM-Deepcut §SEC-09 narrative. |
| Lift method for module 410-1 | Single heavy-lift of complete module | Sub-modular lifts | Depends on as-shipped module weight (TBD) and site crane availability. |
| Pre-commissioning dryness verification | Dewpoint by direct measurement | Time-based purge with witness | Dewpoint is more defensible for cryogenic acceptance; ASSUMPTION pending engineering choice. |

## Examples

- **Example tie-in line item:** "TI-053-001: Cryo flare relief header inlet to V-4110-1, 610 mm 304SS, design temperature down to <-45.5 deg C; weld procedure per ASME B31.3 (PROPOSAL, location TBD); 100% RT (TBD); dryness verification per pre-commissioning procedure." — Source basis: DBM-Deepcut §SEC-09 Flare.
- **Example turnover punch closure:** Heat-trace exclusion walk-down on cryo header complete, photographed, and signed off prior to RFC.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-053-03-01 | Module 410-1 carries BOTH HP and Cryo KO drum scope, yet the project decomposition splits them into PKG-053 and PKG-054 with independent Construction Work Packages. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §Modularization (Module 410-1 "HP / Cryo Flare KO Drum Module") | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` rows `DEL-053-03_construction-work-package` and `DEL-054-03_construction-work-package` | Datasheet §Construction; Specification §R6; Guidance §Considerations | Issue ONE combined CWP for module 410-1 owned jointly by DEL-053-03 and DEL-054-03; or formally split the module into two shop deliverables. | TBD |
| C-053-03-02 | Common HP/Cryo flare stack is physically at 03-25 but receives 04-25 cryo header relief. The 03-25/04-25 split for ownership, construction scope, and joint-test responsibility is "open" in the DBM. | `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-09 Flare (HP/cryo stack physically at 03-25, shared with 04-25; allocation open) | `_CONTEXT.md` ScopePath at 04-25 only | Specification §R6; Guidance §Considerations | EPC Integrator to issue an explicit cross-facility construction interface agreement and tie-in ownership matrix prior to CWP IFC. | TBD |
| C-053-03-03 | Governing piping and vessel codes (ASME B31.3, ASME BPVC Sec VIII Div 1) are not enumerated in any accessible source slice for this package; binary sources (`26020-Package_Requirements.docx`) were not read in this run. | DBM-Deepcut §SEC-09 / §SEC-04 (no code clause cited for KO drum CWP) | (none — absent) | Specification §R3 §Standards | Adopt ASME B31.3 (piping) and ASME BPVC Sec VIII Div 1 (vessel) pending verification against `26020-Package_Requirements.docx` heading 8. | TBD |
