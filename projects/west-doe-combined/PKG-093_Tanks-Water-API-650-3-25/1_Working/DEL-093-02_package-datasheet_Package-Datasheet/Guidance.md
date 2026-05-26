# Guidance — DEL-093-02 Package Datasheet (Tanks, Water (API 650) 3-25)

## Purpose

The Package Datasheet is the EPC Integrator's technical handoff record for `PKG-093`. It carries source-supported equipment identity, design conditions, materials, and interfaces in a form a third-party tank vendor or discipline package engineer can engineer against. It is the bridge between the EPC Scope of Work (`DEL-093-01`) and the vendor-engineered package (`DEL-093-04`).

The authoritative package boundary is **two sweet produced-water storage tanks (TK-9060-2, TK-9070-2)** per `PACKAGE_REGISTER.csv` row PKG-093. The DBM describes the broader 7-tank produced-water family (5 sour + 2 sweet); only the sweet pair is within this package.

## Principles

- **Companion register is authoritative for identity and boundary.** `PACKAGE_REGISTER.csv` row PKG-093 names the specific equipment tags (TK-9060-2, TK-9070-2) and the applicable interface types. The DBM provides the wider design basis but does not redefine the package boundary.
- **Source fidelity over convention.** Quantities, design SGs, code references, and interfaces come from the accepted DBM and the governing 26020-Package_Requirements basis — not from generic tank-package convention.
- **Mandatory Gate 5 anchor.** Per `_CONTEXT.md`, interface facts are intentionally carried *here as evidence*, rather than promoted to standalone deliverables. The interface matrix in `Datasheet.md` is part of the datasheet's authority.
- **Explicit TBD.** Where source language is qualified ("TBC", "assumed", "discrepancy shall be closed"), the datasheet preserves those qualifications rather than reconciling them silently.
- **API 650 Modified means modified.** The DBM is explicit that these tanks are *API-650 Modified*. The "Modified" clauses live in `26020-Package_Requirements.docx` heading 45, which is the controlling source even though its clause text is not locally accessible at PREPARATION time.

## Considerations

- **Sweet service label is a process-allocation label, not a wet-chemistry guarantee.** PKG-093 carries the "Sweet Produced Water" label per the package register. Produced water still warrants H2S contingency review until the owner clauses confirm the sweetness boundary; coating choice (Devchem 253) and ambient design (-40 deg C) are common with the sour pair regardless.
- **SG basis discrepancy is a real design risk.** Tank design SG 1.25 vs. pump basis 1.18 is an open item flagged by the DBM. Vendor datasheets should adopt the more conservative value pending resolution.
- **VRU and H2O2 interfaces are tightly coupled.** Tank vapour management is not a peripheral interface — under SCA-002 it routes through the 03-25 VRU to 04-25 SOC. Tank pressure/relief design is co-dependent with VRU sizing.
- **Cold-climate service is not optional.** -40 deg C ambient drives external insulation, external heating, foundation winterization, and material toughness. Reusing temperate-climate API 650 vendor packages without modification is a likely non-compliance.
- **Interface set is enumerated.** The `PACKAGE_REGISTER.csv` interface list (Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports) is the basis of the package interface matrix.

## Trade-offs

- **Internal coating choice.** Devchem 253 is named for the entire produced-water tank family in the DBM; "or accepted equivalent" is typical EPC practice but not stated in source. Treating Devchem 253 as exclusive minimizes interpretation risk but may close off acceptable equivalents — TBD how strict to be.
- **Truck-out as fallback vs. designed disposition.** The DBM frames pipeline as primary and truck as fallback; designing the truck-out interface to peak capacity costs more but de-risks pipeline-outage scenarios.
- **Treating the .docx heading 45 as authority without locally-rendered text.** This datasheet cites `26020-Package_Requirements.docx` heading 45 with `location TBD` rather than paraphrasing it. The alternative — synthesizing requirements from convention — would violate the skill's source-grounding rule.
- **Process-water duty.** PACKAGE_REGISTER process function names "Sweet Produced Water and Process Water". Whether "process water" implies cleanliness criteria beyond produced-water duty is TBD.

## Examples

- Source-grounded example: "Tanks shall be API 650 Modified, externally insulated and heated, internally coated Devchem 253" — directly traceable to `3-25_Comp_and_Liquids_DBM.md` line 421.
- Conservative example: Reporting the 2.75 m3/min vacuum-truck connection as an ASSUMPTION rather than a firm requirement, because the DBM itself labels it "assumed."
- Boundary example: Citing `PACKAGE_REGISTER.csv` for "Item No. 1: Two (2) 3800 bbl Sweet Produced Water Storage Tank (TK-9060-2, TK-9070-2)" rather than paraphrasing the DBM 7-tank narrative as the package scope.

## Conflict Table (for human ruling)

The columns below follow the four-documents skill template. HRR = Human Ruling Required.

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (HRR) |
|---|---|---|---|---|---|---|
| CONF-093-02-01 | Service classification — package register names "Sweet Produced Water" but DBM groups all 7 tanks (5 sour + 2 sweet) under common construction (API 650 Modified, Devchem 253, insulated/heated). Question: does "sweet" relax sour-service materials/welding rules for TK-9060-2 / TK-9070-2? | `PACKAGE_REGISTER.csv` row PKG-093 (Process Function "Sweet Produced Water") | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 419-421); §SEC-04 produced-water contaminants (line 194) | Datasheet Process/Materials; REQ-093-02-010 | Treat as produced water with potential H2S contingency; apply sour-service materials and welding rules unless owner clause expressly relaxes them. | TBD |
| CONF-093-02-02 | Design SG 1.25 (tank) vs. 1.18 (pump basis) | `3-25_Comp_and_Liquids_DBM.md` §SEC-04 (line 176) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | Datasheet conditions; REQ-093-02-005 | Use 1.25 for tank structural; 1.18 for pump hydraulics; reconcile in detailed design. | TBD |
| CONF-093-02-03 | API 650 "Modified" clauses authority — `26020-Package_Requirements.docx` heading 45 not locally accessible | `_CONTEXT.md` / `_REFERENCES.md` cite the .docx as authoritative | Local-only DBM (DBM-Comp_and_Liquids) | All requirements citing "API 650 Modified" detail; REQ-093-02-002, REQ-093-02-010 | Carry clause-level location as TBD; render .docx to markdown in a later run and re-cite. | TBD |
| CONF-093-02-04 | Coating equivalence — "or accepted equivalent" convention vs. exclusive "Devchem 253" wording in source | EPC practice (convention) | `3-25_Comp_and_Liquids_DBM.md` §SEC-06 (line 421) | REQ-093-02-004 | Cite Devchem 253 as the named system; equivalence acceptance is a vendor-submittal item, not a datasheet relaxation. | TBD |
| CONF-093-02-05 | Process-water duty — package function names "Process Water" alongside "Sweet Produced Water". Does process-water service impose cleanliness or material criteria beyond produced-water duty? | `PACKAGE_REGISTER.csv` row PKG-093 (Process Function) | DBM is silent on process-water-specific cleanliness criteria for these tanks | Datasheet Service fluid; REQ-093-02-004; REQ-093-02-010 | Treat process-water as a secondary allocation served by the same materials/coating envelope unless owner clause states otherwise. | TBD |
