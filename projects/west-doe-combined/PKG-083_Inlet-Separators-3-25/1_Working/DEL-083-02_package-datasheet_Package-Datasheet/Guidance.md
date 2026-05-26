# Guidance — DEL-083-02 Package Datasheet (PKG-083 Inlet Separators 3-25)

Status: INITIALIZED (P1_P2 draft). Directional rationale grounded in DBM-Comp_and_Liquids SEC-03/SEC-04.

## Purpose

The Package Datasheet is the mandatory EPC Integrator technical handoff that carries the package data a third-party vendor or discipline needs to engineer and design PKG-083 (Inlet Separators 3-25). It is also the Gate-5 anchor that carries interface evidence rather than spawning standalone interface deliverables (see `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv DEL-083-02 row).

## Principles

- **Source-anchored.** Every design value originates from an accessible source slice; non-trivial inferences are labeled ASSUMPTION; missing values are TBD. Source: skill "Authority hierarchy" + DBM SEC-04.
- **Two trains, 2x50%.** The facility uses two identical horizontal three-phase separators sized for half capacity each; there is no installed spare. This shapes both turndown expectations and maintenance planning. Source: DBM SEC-04 line 244.
- **Sour service throughout.** All wetted internals, valves, and instrumentation must be selected for H2S service. Source: DBM SEC-03/SEC-04 (raw inlet is sour; SEC-05 cites ~0.296 mol% H2S in adjacent compressor composition).
- **Symmetrical flow distribution.** Inlet piping arrangement is a hydraulic discipline question that materially affects separator performance at split flow. Source: DBM SEC-04 "Flow Distribution and Controls".
- **Slug capture sized for separator only; flowback governs.** The 38 m3 slug volume per separator is for steady upset; frac flowback is the governing transient and is processed downstream by 04-25 stabilization over ~6 hours; operator-side rate management is required. Source: DBM SEC-04 "Slug and Flowback Basis".

## Considerations

- **Inlet temperature reconciliation.** The DBM notes the 8.3 deg C inlet design temperature carries a downstream-excerpt disagreement; detailed design must reconcile before vendor datasheets are issued. Captured in the Conflict Table (CF-01). Source: DBM SEC-04 line 258.
- **Building extent TBD.** Heated self-framing building covers instrumentation and one end of each package, but extent is open; affects heating duty, electrical, and access design. Source: DBM SEC-04 line 260.
- **Drive-gas recycle pressure interlock.** Drive-gas pressure must be held above the 04-25 stabilizer flash-feed separator pressure; this creates a cross-facility control coupling worth surfacing to the controls team early. Source: DBM SEC-04 "Flow Distribution and Controls".
- **Methanol drainage path.** Infrequent methanol presence at the boot is acknowledged; downstream disposition is TBD — coordinate with produced-water/H2O2 treatment design. Source: DBM SEC-03 line 218.
- **Interface count is large (11 types).** The package carries 11 applicable interfaces (INTERFACE_REGISTER.csv); a robust interface matrix in the Datasheet is essential to avoid late-stage tie-in re-work.
- **Binary source documents.** Two key source documents (26020-Package_Requirements.docx heading 36; 26020-02-PT-RFQ-17-003 RFQ) are binary and not text-accessible to this drafting pass; values dependent on them are TBD. Recommend extraction prior to IFC.

## Trade-offs

- **Parallel control valves vs single large valve.** DBM mandates at least two parallel inlet pressure-control valves per package with dP ≤ 5 psid (Source: DBM SEC-04). Trade-off favors rangeability and reliability over equipment count; not adjustable downward without a basis change.
- **Slug volume sizing.** ~38 m3 per separator implies acceptance of frequent flowback management by operations rather than oversizing vessels. The trade-off is capital savings vs operational complexity (Source: DBM SEC-04 "Slug and Flowback Basis").
- **Heated building extent.** Covering more of the package improves cold-weather operability but raises capex and electrical demand. Pending TBD resolution.

## Examples

The DBM source slice does not provide worked examples. None drafted. (TBD.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CF-01 | Inlet design temperature 8.3 deg C vs "some downstream excerpts require confirmation" | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-04 "Inlet Separation" line 258 (states 8.3 deg C as current) | DBM SEC-04 line 258 same paragraph notes downstream excerpts disagree (specific excerpt locations not cited) | Datasheet.md Operating Conditions; Specification.md R-3.3 | PROPOSAL: hold 8.3 deg C as the current basis until detailed design reconciles | TBD |
| CF-02 | Source basis text-accessibility | DBM-Comp_and_Liquids markdown is text-accessible; provides design table and interface narrative | 26020-Package_Requirements.docx heading 36 and 26020-02-PT-RFQ-17-003.docx are binary; clause-level extraction not performed | Specification.md Standards; R-9 (ASME); package code stamps in Datasheet.md Construction | PROPOSAL: extract the .docx slices and re-run four-documents at next pass to firm up Standards and Construction | TBD |
| CF-03 | H2S concentration at separator stream | DBM SEC-05 compressor inlet table cites ~0.296 mol% H2S (post-separation gas) | No explicit H2S mol% given for the raw wellstream into the separators in the DBM slice read | Datasheet.md Service; Specification.md R-9 / NACE applicability | PROPOSAL: treat separator service as sour and require NACE MR0175 / ISO 15156 materials selection regardless of exact mol%; confirm raw mol% in detailed design | TBD |
