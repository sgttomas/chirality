# Guidance: EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to let the EPC Integrator accept, qualify, or hold the PKG-011 vendor package for integration into the facility without assuming the Package Vendor's engineering/design ownership. Gate 7 frames DEL-011-06 as review evidence for vendor documentation, integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package.

## Principles

- Preserve the responsibility boundary: vendor engineering, package design, vendor documentation, and physical equipment remain Package Vendor responsibilities; EPC acceptance confirms integration readiness and records exceptions.
- Treat the declared interface types as the review backbone: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Source acceptance claims to available evidence. Where vendor-specific test names, form templates, or acceptance criteria are unavailable, mark them `TBD` or carry them as open items.
- Use the DBM electrical basis to check whether vendor information supports the facility electrical context, including 4,160 V medium-voltage service and 4160V MCC integration.
- Keep unresolved vendor or interface gaps visible through a controlled open-item mechanism rather than treating missing evidence as accepted.

## Considerations

- The workbook row identifies PKG-011 as an Electrical package with specific interface flags, but it does not provide detailed vendor document numbers, inspection points, or turnover form requirements.
- Gate 7 indicates that `26020-Package_Requirements.docx` did not match a package-specific heading for PKG-011. The document is available, but no package-specific source slice was confirmed for this package; avoid importing requirements from other package headings.
- The DBM states that project electrical specifications govern cable tray, conduit, grounding, and bonding, but the relevant project specification slices were not available in this deliverable folder.
- Declared dependencies are empty, so blockers are advisory only and no upstream or downstream deliverable is treated as blocking under the declared dependency mode.

## Trade-offs

| Decision area | Conservative approach | Risk if overextended |
|---|---|---|
| Vendor test evidence | Require evidence or open-item disposition, but leave specific tests as TBD until vendor test procedures are available. | Invented test names or acceptance criteria could conflict with vendor or project inspection requirements. |
| Interface acceptance | Check every declared PKG-011 interface type against vendor and EPC integration records. | Treating undeclared interfaces as mandatory could expand scope beyond Gate 7. |
| Electrical basis | Use DBM SEC-12 for facility-level electrical context, including 4.16 kV service and 4160V MCC integration. | Turning DBM context into detailed vendor acceptance criteria without source slices could overstate authority. |
| Responsibility split | Keep EPC acceptance focused on review, integration, and handoff readiness. | Assigning package engineering/design closure to EPC would conflict with the accepted Gate 7 responsibility model. |

## Examples

- Acceptable evidence entry: "Electrical Power interface reviewed against 4,160 V service basis; vendor data sheet revision X accepted with open item Y for harmonic/reactive-power study result." Exact document numbers are TBD.
- Acceptable open item: "Grounding / bonding vendor termination details not available; carry as open item assigned to Package Vendor with EPC Electrical review required before turnover." Exact form is TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-011-06-001 | Package-specific vendor requirements for PKG-011 are not available from the matched Word package headings, while the acceptance deliverable needs vendor test/inspection and turnover criteria. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011, `DocxPackageMatched=FALSE`; `_REFERENCES.md`, Missing / Deferred References. | Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06, requires review log, acceptance checklist, and test/inspection evidence. | Datasheet Construction; Specification Requirements/Verification; Procedure Steps. | Use Gate 7 artifacts and workbook/DBM context for the initial acceptance framework; keep package-specific test names, hold points, form templates, and acceptance criteria as TBD until source slices are supplied. | TBD |
