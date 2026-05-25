# Guidance — DEL-026-03 Construction Work Package

Directional guidance for authoring and using the Construction Work Package (CWP) for PKG-026 Transformer TXP-8300-2.

## Purpose

The CWP exists so the EPC Integrator can carry the PKG-026 step-down distribution transformer from a vendor-delivered package into a physically installed, terminated, grounded, inspected, and turned-over facility asset (DELIVERABLE_REGISTER row DEL-026-03). It is the construction-side counterpart to the EPC Scope of Work (DEL-026-01) and Package Datasheet (DEL-026-02), and it produces the turnover evidence that DEL-026-06 (EPC Vendor Package Review and Acceptance) will consume.

## Principles

1. The CWP is EPC Integrator-owned. Vendor-owned engineering, design, vendor documentation, and the equipment package itself belong in DEL-026-04 and DEL-026-05 (PACKAGE_REGISTER row PKG-026). Do not duplicate vendor-owned content; reference it.
2. Construction responsibility for the facility is assigned to Tourmaline Oil Corporation per DBM-Deepcut §Construction Responsibility. The CWP should align workface plans with that responsibility split rather than re-define it.
3. Tie-in interfaces are first-class objects. PKG-026 declares seven interface types (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports). Each should have an explicit checklist entry, not be folded into a generic "installation" step.
4. Source authority is the DBM and registers. Where the DBM is silent on transformer-specific parameters, the CWP should leave the value `TBD` or label `ASSUMPTION`, not invent vendor-style detail.
5. CEC governs spacing and grounding-conductor sizing for large oil-filled transformers (DBM-Deepcut §Transformers; §Power System grounding paragraph). Constructability decisions should respect CEC clearances even before vendor drawings are final.

## Considerations

- **Dual rating (20/26 MVA).** Interpretation depends on cooling-class designation (ONAN/ONAF assumed). The CWP should flag the cooling configuration as an installation-affecting parameter (radiator clearance, fan power supply, controls tie-in) and defer specifics to vendor turnover.
- **Three voltages in the title (13.8 / 6.9 / 0.4 kV).** This could be one three-winding unit or one two-winding unit paired with a step-down to 0.4 kV elsewhere. The construction approach to terminations, cable trays, and grounding differs between these cases. Capture the ambiguity in the Conflict Table until vendor data or DEL-026-02 resolves it.
- **Grounding configuration.** The DBM specifies a 100 A, 10 s NGR on each 6.9 kV transformer secondary and a 5 A continuous HRG resistor on each 600 V transformer. A 0.4 kV winding sits below the 600 V tier the DBM addresses; do not assume the 5 A HRG applies without confirmation.
- **Containment and spacing.** Transformer secondary containment is to be reviewed (DBM §Transformers). The CWP should call out containment as a planning input, not as already-resolved.
- **Construction interfaces with shared facilities.** Power distribution is shared between 04-25 and 03-25 facilities (DBM §Power System); construction sequencing should account for any energization windows that touch the shared backbone.
- **Tie-in responsibility marker.** ISBL/OSBL tie-ins carry an external-interface responsibility marker per DBM; the CWP should treat each such tie-in as needing a named counterparty before execution.

## Trade-offs

- **Workface plan granularity vs. vendor-data availability.** Until the vendor package (DEL-026-04) and vendor turnover (DEL-026-05) are sufficiently mature, a highly granular workface plan risks rework. Favor a structured-but-coarse plan with clearly marked `TBD` rows over speculative detail.
- **Turnover checklist breadth vs. signing burden.** Comprehensive interface-by-interface checklists serve DEL-026-06 acceptance well but increase field documentation burden. Bias toward the seven declared interface types as the minimum checklist axes.
- **Field-decision authority.** Pre-authorizing field decisions speeds execution but can drift from EPC Integrator intent. The CWP should explicitly route conflicts to the EPC Integrator (REQ-CWP-026-09).

## Examples (illustrative, not normative)

- A grounding-section worksheet entry might cite "DBM-Deepcut §Power System grounding paragraph" as basis for a 100 A, 10 s NGR commissioning check on the 6.9 kV secondary.
- An interface-checklist row for "I&C / Control Cabling" might list: home-run cable installed; terminations completed; loop checked; signal-list reconciled against DEL-026-02.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-026-03-01 | Package title implies three voltage levels (13.8 / 6.9 / 0.4 kV) on one transformer, but DBM-Deepcut describes 13.8 kV → 6.9 kV step-down at the Inlet/Sales Compressor Electrical Building and separate 600 V→208/120 V or 600 V→480 V transformers, not a 0.4 kV winding on a 13.8/6.9 kV unit. | `_CONTEXT.md` Package name (Workbook Packages row 28) | DBM-Deepcut/4-25_Deepcut_DBM.md §Power System; §System Voltages; §Transformers | Datasheet "Subject Equipment"; Specification REQ-CWP-026-07; Guidance "Three voltages in the title" | PROPOSAL: treat 0.4 kV as a separately fed companion transformer until vendor data resolves; install grounding per the actual winding configuration vendor delivers | TBD |
| CFL-026-03-02 | Rating "20/26 MVA" is given in the title but DBM does not state the cooling-class basis for this unit. | `_CONTEXT.md` Package name | DBM-Deepcut §Transformers (silent on this tag) | Datasheet "Subject Equipment"; Guidance "Dual rating" | PROPOSAL: record as ASSUMPTION ONAN/ONAF pending vendor datasheet via DEL-026-04 / DEL-026-05 | TBD |
| CFL-026-03-03 | Construction responsibility text (DBM-Deepcut §Construction Responsibility) is facility-wide; PKG-026 PACKAGE_REGISTER row assigns vendor/EPC split for the package. The CWP must reconcile these for the transformer specifically (e.g., who performs oil fill, energization). | DBM-Deepcut §Construction Responsibility | PACKAGE_REGISTER row PKG-026 | Specification REQ-CWP-026-02, REQ-CWP-026-09; Procedure Steps section | PROPOSAL: vendor commissioning agent leads energization and oil quality testing; Tourmaline field forces perform setting, terminations, and grounding installation | TBD |

## Notes

- This Guidance is directional. Where it conflicts with the Specification, the Specification (and its cited sources) prevails.
