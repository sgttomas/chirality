# Guidance — DEL-017-05 Vendor Document Turnover Package (PKG-017)

## Purpose

The Vendor Document Turnover Package exists so that the Package Vendor's documentation for the PKG-017 MV VFD (600 HP, 4160 V, 3-phase, 60 Hz) reaches the EPC Integrator in a controlled, complete, and review-ready form. It is the documentation backbone of the vendor scope: without it, EPC integration, construction, commissioning, and operations lose traceability to vendor design intent and as-built reality. (Source: Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-017-05`; DBM `3-25_Comp_and_Liquids_DBM.md` line 617.)

## Principles

- **Single controlled index.** One Vendor Document Register is the authority for what exists, what revision, and what status — not email threads or ad-hoc transmittals.
- **Artifacts, not deliverables.** Individual source-required document rows live inside this package as artifacts; they do not get promoted into separate decomposition deliverables (Gate 7 `DELIVERABLE_REGISTER.csv` Notes).
- **Interface-aware.** Each documented item should be traceable to the PKG-017 interfaces it informs (Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports — Gate 7 `INTERFACE_REGISTER.csv`).
- **Vendor authors, EPC reviews.** Authority for content sits with the Package Vendor; authority for interface/integration acceptance sits with the EPC Integrator (Gate 7 `DELIVERABLE_REGISTER.csv` Responsible Party).
- **Turnover-grade closure.** The package is not finished until the MDR/VDB is compiled, the acceptance log is closed, and handover is signed.

## Considerations

- The accessible source set does not contain a PKG-017–specific vendor deliverable list within `26020-Package_Requirements.docx`. The list of required documents must therefore be reconciled at execution against the active project requirements source. Until then, the document classes named here are ASSUMPTION-grade (location TBD).
- The site basis (-40 °C minimum ambient, DBM line 145) makes documentation of cold-service ratings, heaters, and enclosure suitability non-optional for the VFD.
- Declared upstream/downstream dependencies in `_DEPENDENCIES.md` are empty; the working assumption (ASSUMPTION) is that this deliverable consumes the engineered equipment package (`DEL-017-04`) and feeds review and acceptance (`DEL-017-06`).
- The objective-to-deliverable association (`OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`) is carried under the package-heuristic mode; it is directional context, not a hard requirement, until human-confirmed.

## Trade-offs

- **Document granularity vs. register noise.** A finer register catches more, but inflates review burden. Group source document table rows under parent documents where it preserves traceability.
- **Early vs. late MDR compilation.** Building the MDR incrementally lowers turnover risk but adds revision churn; deferring it concentrates effort but raises late-stage discovery risk.
- **Vendor-native document control vs. project document control conventions.** When vendor numbering and project DCC conventions diverge, prefer dual identifiers in the register (vendor ID + project DCC ID) rather than forcing a re-stamp that strips vendor traceability.

## Examples

No PKG-017-specific worked example exists in accessible sources (location TBD). The 26020 package requirements document (table of contents inspected) provides generic vendor-deliverable list patterns for other packages (e.g., `26020-01-PT-12-001` Acid Gas Compressor lists Core vendor documents, Core package engineering, Rotating equipment / compressors, etc.); the same shape is a reasonable structural model for the PKG-017 register but the specific entries must be confirmed against the active source for this package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-017-05-001 | The PKG-017-specific vendor deliverable list is not located in `26020-Package_Requirements.docx`; document classes here are ASSUMPTION. | `_Sources/26020-Package_Requirements.docx` (no PKG-017 / `26020-02-30-008` section found) | Gate 7 `DELIVERABLE_REGISTER.csv` (anticipated artifacts only at register-level) | Datasheet `Construction`; Specification `REQ-VDT-02`, `Documentation`; Guidance `Considerations` | Carry the document classes as ASSUMPTION; require the EPC project DCC and the Package Vendor to publish the authoritative VDRL/VDDR for PKG-017 at execution. | TBD |
| HRR-017-05-002 | Declared upstream/downstream dependencies are empty in `_DEPENDENCIES.md`, but Gate 7 narrative implies `DEL-017-04 → DEL-017-05 → DEL-017-06`. | `_DEPENDENCIES.md` (empty declared lists) | Gate 7 `DELIVERABLE_REGISTER.csv` (DEL-017-04, DEL-017-05, DEL-017-06 narrative roles) | Specification `REQ-VDT-09`; Procedure `Prerequisites` | Adopt the narrative-implied edges as declared upstream/downstream via a dependency-extract run; do not treat as binding until declared. | TBD |
| HRR-017-05-003 | Document numbering / DCC convention not established in accessible sources. | `_Sources` (no project document-control standard located) | Vendor document control procedures (vendor-supplied at execution) | Specification `Standards`; Guidance `Trade-offs` | Use dual identifiers (vendor ID + project DCC ID) in the register until the EPC DCC standard is fixed. | TBD |
