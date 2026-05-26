# Guidance — DEL-071-02 Package Datasheet (Fuel Gas Skid 4-25)

## Purpose

This Guidance explains *why* the EPC Package Datasheet for `PKG-071` exists, what it is for, and the judgment calls the EPC Integrator must make while preparing it. The deliverable is the mandatory Gate 5 EPC anchor for the technical handoff from the EPC Integrator to the Package Vendor for engineering, design, and equipment supply of the Fuel Gas Skid 4-25 (DELIVERABLE_REGISTER.csv row 331; PACKAGE_REGISTER.csv row 61; `_CONTEXT.md` Notes).

It supports objectives `OBJ-001`, `OBJ-004`..`OBJ-010` (`_CONTEXT.md`; PACKAGE_REGISTER.csv row 61). The package-grouping objective association is recorded as ASSUMPTION (best-effort mapping) per `four-documents` skill `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`.

## Principles

1. **Source-of-truth fidelity.** Every datasheet value reflects what the workbook row, the package-requirements heading, or the DBM actually says. Where the source says TBD, the datasheet says TBD. (Source: `SOW-0101`, `SOW-0102` openly carry TBDs.)
2. **Responsibility split is non-negotiable.** Package Vendor owns package engineering/design/vendor documentation/physical equipment. EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. (PACKAGE_REGISTER row 61; `OBJ-004`.)
3. **Interfaces are first-class.** All 12 X-column interface facts for `PKG-071` are carried in this datasheet as evidence rather than being routed to standalone deliverables (`_CONTEXT.md` Notes). The matrix is the integration contract between EPC and Vendor.
4. **No invention.** When source data is missing, mark `TBD`. When a position must be taken to make the datasheet usable, label it `ASSUMPTION:` and surface it for human ruling.
5. **Derivative anchor.** This datasheet aggregates accepted upstream truth (PACKAGE_REGISTER, SCOPE_LEDGER, INTERFACE_REGISTER, ARTIFACT_REGISTER at Gate 7). It cites the snapshot and must not substitute for the decomposition.

## Considerations

- **Heater sizing is open.** Heater capacity is TBD in source (`SOW-0101`); vendor will need a duty derived from feed composition, flow, and outlet temperature (95 F / 35 C). Final flow is TBD (`SOW-0102`). Vendor input or a separate calc will be required to close.
- **SCR control voltage and location matter for electrical integration.** SCR control panels are 600 V in the electrical building (`SOW-0102`); this couples to `OBJ-005` electrical infrastructure and the `Electrical Power` interface row (`IFC-5AB340F539`).
- **Scrubber sizing convention.** k-factor 0.35 imperial maximum with a pressure de-ration is stated; the vendor designs to it (`SOW-0101`). The datasheet carries the sizing basis, not the resulting dimensions.
- **By-others scope is part of the integration risk surface.** Shipping, installation, tie-in piping, and electrical tie-in are explicitly excluded from vendor scope (`SOW-0102`); EPC must absorb these in `DEL-071-03_construction-work-package` and downstream packages.
- **MAWP TBD.** The design pressure is stated (150 psig) but MAWP is TBD (`SOW-0102`); this is a code/standards interaction (CSA B51 / ASME — clause-level standards not slice-read in this run).
- **Sour-service applicability.** `OBJ-009` identifies sour-service safety as a project-wide concern; whether the Fuel Gas Skid feed is sour is not explicitly stated in the package heading and is recorded as `TBD` (do not assume sweet).
- **Twelve applicable interfaces** mean this package has a wide integration footprint; the datasheet's interface matrix is what makes the package vendor-engineerable without re-reading the workbook.

## Trade-offs

- **Carrying interface facts in the datasheet vs. separate interface deliverables.** Chosen: carry as evidence here (`_CONTEXT.md` Notes). This keeps the EPC handoff self-contained but means the datasheet must be re-issued when interface facts change. ASSUMPTION: change frequency is low because workbook row 61 is authoritative and frozen at Gate 7.
- **Preserving TBDs vs. proposing values.** Chosen: preserve TBDs. Trade-off: vendor will quote with placeholders; benefit: no spurious commitments. (Source-grounding rule from `four-documents` skill.)
- **Citing CSA/ASME clauses vs. citing only the DBM.** Chosen: cite DBM section pointers where available; mark clause-level codes as `location TBD`. Trade-off: less prescriptive; benefit: no overclaim against unread source slices.

## Examples

- The Datasheet's "Conditions" block reproduces the SCOPE_LEDGER `SOW-0102` line verbatim where possible, then expands each value into a labeled row with provenance. This is the canonical shape for any package whose source basis lives in a single Word-document heading.
- The Datasheet's "Interfaces" matrix lists each `IFC-*` ID alongside its interface type so an EPC interface engineer can resolve a row to its register entry in one lookup.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | No source-vs-decomposition conflicts identified for this deliverable in this Pass 2 sweep. | — | — | — | — | — |

If clause-level DBM or codes/standards reads later surface conflicts (e.g., design pressure vs. MAWP basis, sour-service applicability), add rows here.
