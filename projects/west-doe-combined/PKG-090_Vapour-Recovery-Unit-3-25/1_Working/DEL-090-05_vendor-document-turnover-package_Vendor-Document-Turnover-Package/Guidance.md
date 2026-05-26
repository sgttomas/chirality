# Guidance — Vendor Document Turnover Package (DEL-090-05)

## Purpose

This deliverable exists because PKG-090 (Vapour Recovery Unit 3-25) is a Package Vendor-engineered scope. The EPC Integrator does not author the equipment-internal documentation; the vendor does. To make the package usable by the EPC Integrator and ultimately by the facility operator, the vendor's documentation must be assembled, registered, reviewed, and formally turned over as a coherent set. This deliverable produces that set and the evidence that it is complete.

It is the evidence base consumed by DEL-090-06 (EPC Vendor Package Review and Acceptance). It does not itself certify the package; certification authority lives with the EPC Integrator under DEL-090-06 (and ultimately with the operating company).

## Principles

- **Register first.** The vendor document register is the spine. Every required document should appear there before it is submitted, so completeness is measurable at any time, not only at turnover.
- **Submittals are not the deliverable; the closed set is.** Individual transmittals are artifacts; the deliverable is the assembled, reviewed, accepted set.
- **Source-required vs. vendor-customary.** Documents required by `26020-Package_Requirements.docx` heading 43 are non-negotiable. Vendor-customary documents (additional, beyond the source list) are welcome but do not relieve the source-required list.
- **Evidence over assertion.** "Reviewed" must be backed by a transmittal disposition; "tested" must be backed by an ITP record; "certified" must be backed by a certificate.
- **One deliverable, many artifacts.** Individual source document rows remain artifacts under this deliverable, never separate deliverables (`_CONTEXT.md` Notes).

## Considerations

- The package contains two 200 hp electric-drive VRU compressor packages arranged 2 x 100 percent (DBM line 434, 436). Vendor documentation must cover both packages and their shared/auxiliary scope.
- Discharge is routed to 04-25 SOC suction under SCA-002 (DBM line 436); interface tie-in documentation should be specifically traced because the destination is cross-facility.
- The VRU sees tank vapours and selected process vents; expect rated H2S/mercaptan service. Material certifications and NACE-related metallurgy documentation deserve particular attention. (ASSUMPTION: NACE applicability inferred from sour-service context in DBM SEC-01/SEC-06; explicit code/standard call-out TBD pending `26020-Package_Requirements.docx` heading 43 extraction.)
- Review cycle latency between vendor and EPC drives critical-path risk; cycle-time discipline matters more than perfection on the first round.
- Source-required document list resolution is a precondition for high-confidence completeness — until that list is extracted from `26020-Package_Requirements.docx` heading 43, completeness assertions are PROPOSAL-level only.

## Trade-offs

- **Submittal granularity vs. transmittal overhead.** Bundling submittals reduces transmittal count but slows review; over-fragmenting increases admin burden. Default to vendor-natural document groupings unless the EPC Integrator instructs otherwise.
- **Early register depth vs. stability.** A detailed register early helps planning but invites churn. Recommend: stable column schema and stable required-document rows from day one; revisions and submittal-stage rows accreting as work progresses.
- **Vendor template vs. project template.** Vendor-native templates reduce vendor cost; project-native templates ease EPC review. Default to vendor-native unless the source explicitly requires project format. TBD pending source extraction.

## Examples

Not populated. Vendor-document-turnover examples are project-specific; introducing generic examples here would risk overstating practice. Add concrete examples in MEMORY.md as they emerge under review.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| (none open) | n/a | n/a | n/a | n/a | n/a | n/a |

No conflicts surfaced in Pass 1/Pass 2. Most open items are TBDs awaiting extraction of `26020-Package_Requirements.docx` heading 43, not conflicts between accessible sources.
