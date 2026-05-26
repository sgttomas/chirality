# Guidance — DEL-069-06 EPC Vendor Package Review and Acceptance

## Purpose

This guidance supports the EPC Integrator team performing review and acceptance of the PKG-069 Mole Sieve Drier Unit (Gas) vendor package. It explains intent behind the Specification's requirements, key technical considerations specific to molecular-sieve gas dehydration, and trade-offs to weigh when adjudicating vendor deviations and open items. (Source: `_CONTEXT.md` Scope; PROJECT_DECOMP DEL-069-06 narrative.)

## Principles

- **Acceptance is evidence-driven.** Every accepted item should trace from the acceptance checklist (R-5) to a discoverable evidence file (R-6/R-7). Where no evidence exists, the item is open, not accepted. (Aligns with project DBM expectation that vendor packages are accepted on documented basis, SEC-06.)
- **EPC basis is authoritative over vendor preference.** When the EPC SOW, Package Datasheet, or Construction Work Package conflicts with a vendor proposal, the EPC basis governs unless a formal deviation is approved.
- **Source values are conservative anchors.** The DBM-Deepcut SEC-06 values (bed flow, sizing, cycle preliminary times, flange class, adsorbent type) are the baseline. Vendor refinement is expected; vendor regression below those bases requires engineering justification.
- **Open items are decision points, not deferrals.** SEC-06 explicitly enumerates open items; each one is a gated acceptance decision (R-8), not a problem to push past mechanical completion.

## Considerations

### Adsorbent Selection (R-3.2)
3A molecular sieve is mandatory because 4A and 5A pore sizes can adsorb H2S; if H2S adsorbs and desorbs during regeneration, sulphur spikes propagate in the regeneration return loop, contaminating upstream TEG/amine systems and downstream process. (Source: DBM-Deepcut SEC-06 "Molecular-Sieve Bed and Regeneration Basis".) Any vendor proposal to substitute SHALL be rejected.

### Bed Configuration and Cycle Times (R-3.1, R-3.3, R-3.4)
The 2-adsorb / 1-regen configuration with ~54 h adsorption and ~7.6 h total regeneration cycle is preliminary; vendor refinement based on actual inlet conditions is expected. Reviewers should verify the vendor's mass balance preserves the 332.6 MMSCFD adsorption + 25.45 MMSCFD regen totals and that bed sizing accommodates worst-case water loading. (DBM-Deepcut SEC-06.)

### Regeneration Heater Temperature Basis (R-3.9)
The DBM contains an unresolved inconsistency: the system overview cites 450 degF regeneration temperature while the heater detail cites 460 degF. This is recorded in the Conflict Table below. The vendor's heater design and the EPC Package Datasheet must agree before acceptance. Higher temperature improves regeneration but accelerates adsorbent aging; vendor justification should address adsorbent life impact (also a SEC-06 open item).

### Regeneration Gas Compressor Sizing (R-3.6)
A similar inconsistency exists between the assumed 100 psid design differential and the detailed equipment-loop table total of 79.5 psid. The vendor should reconcile final loop hydraulics and propose a coordinated differential basis. Oversizing wastes power and complicates anti-surge control; undersizing risks regeneration shortfall.

### Dust Filtration and MRU Protection (R-3.7)
The mol-sieve dust filter protects the mercury recovery unit (MRU) from carryover fines; the MRU dust filter protects the BAHX from mercury and residual dust. Manual online bypass is required for change-out without unit shutdown; reviewers should verify the bypass design preserves filtration integrity during change (e.g., upstream isolation, depressurization, purging).

### Flange Class and Pressure Boundary (R-3.8)
The 900# flange class is driven by downstream cryogenic-section design pressure (1360 psig). Vendor proposals to use lower-class flanges anywhere on the molecular-sieve system contradict the DBM and SHALL be returned for revision. (DBM-Deepcut SEC-04 §Inlet Pipeline Pressure and Flow.)

### Blowdown Philosophy (R-3.11)
Operator-initiated HMI-only blowdown is deliberate: the mol-sieve system contains hot beds and adsorbent that can be damaged by rapid depressurization. The 50 psi/min rate limit, dual blowdown valves, and regen-compressor bypass are non-negotiable safety design features. Vendor automation that overrides operator control SHALL be rejected.

### Recycle Path Flexibility (R-3.12)
The dual recycle-return path (normal: upstream of TEG inlet coalescer; alternate normally-closed: upstream of mole-sieve coalescers) supports off-design operation and start-up dry-out. Vendors sometimes propose a single return path; reviewers SHOULD insist on the alternate-closed path being installed even if not normally used.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Vendor design refinement vs DBM baseline | Refinement welcomed; deviations require documented engineering basis and EPC acceptance. |
| Acceptance speed vs open-item closure | Avoid conditional acceptance where SEC-06 open items affecting safety or capacity are unresolved (R-8). Conditional acceptance for non-safety open items is acceptable when the disposition is documented. |
| Adsorbent regeneration temperature | Higher temperature → faster/deeper regen but shorter adsorbent life; lower temperature → longer cycles, higher adsorbent loading. Vendor recommendation should be documented against operating-cost / replacement-cost trade. |
| FAT scope vs SAT scope | More FAT reduces SAT risk and field rework, but increases vendor shop time and cost. Recommend high-criticality items (regen compressor, control system integration) be FAT-tested. ASSUMPTION: project ITP not yet available. |

## Examples

- **Example — Adsorbent substitution rejection:** Vendor proposes 4A molecular sieve for cost. Reviewer cites R-3.2 and DBM-Deepcut SEC-06; returns submittal for revision; logs in R-1 as Rejected.
- **Example — Regen temperature reconciliation:** Vendor heater datasheet shows 460 degF outlet. Reviewer flags conflict with system-overview 450 degF; routes to EPC process engineering for ruling; records decision in open-items register (R-8) before accepting heater datasheet.
- **Example — Filter change-out bypass:** Vendor proposes online bypass without isolation valves on filter side. Reviewer cites R-3.7 intent and Considerations §"Dust Filtration"; returns for revision requiring isolation and depressurization provisions.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-01 | Regeneration gas temperature basis: 450 degF vs 460 degF | DBM-Deepcut SEC-06 §"Molecular-Sieve Equipment, Controls, and Protection" (system overview row, 450 degF) | DBM-Deepcut SEC-06 §"Molecular-Sieve Equipment, Controls, and Protection" (heater detail row, 460 degF) | Datasheet Attributes "Regeneration gas heater"; Spec R-3.9; Procedure step on regen-temperature verification | PROPOSAL: defer to the vendor's heat-balance and adsorbent-life calculation; ratify single value in EPC Package Datasheet before acceptance | TBD |
| CFT-02 | Regeneration gas compressor design differential: 100 psid (assumed) vs 79.5 psid (detailed equipment-loop table) | DBM-Deepcut SEC-06 §"Regeneration gas compressor" (assumed 100 psid) | DBM-Deepcut SEC-06 same row (detailed loop totals 79.5 psid) | Datasheet Attributes "Regeneration gas compressor"; Spec R-3.6 | PROPOSAL: vendor reconciles final loop hydraulics and submits coordinated differential basis; EPC ratifies before accepting compressor datasheet | TBD |
| CFT-03 | Objective-to-deliverable mapping for DEL-069-06 (OBJ-001/003-010) is derived via package-grouping heuristic, not an explicit deliverable-level mapping | `_CONTEXT.md` "Supports Objectives" list | Brief `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC` | Datasheet Identification (ParentObjectives) | PROPOSAL: retain as ASSUMPTION until human confirms or an explicit deliverable-level mapping is added to the decomposition snapshot | TBD |
