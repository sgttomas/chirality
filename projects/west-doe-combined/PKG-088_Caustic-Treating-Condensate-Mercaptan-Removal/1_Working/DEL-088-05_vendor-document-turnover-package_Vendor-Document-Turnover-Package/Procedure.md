# Procedure — DEL-088-05 Vendor Document Turnover Package

## Purpose

This procedure describes the steps to **produce** the Vendor Document Turnover Package: assemble the vendor document register, collect submittals, gather source-required vendor documentation, and close out turnover records with the EPC Integrator. It is operated jointly by the Package Vendor (lead) and the EPC Integrator (interface/integration review).

## Prerequisites

- Package scope is established (DEL-088-01 Scope of Work issued or at least at INITIALIZED).
- Package datasheet (DEL-088-02) is available so the vendor knows the equipment design envelope.
- Vendor Engineered Equipment Package (DEL-088-04) is producing the engineering content that will flow into this turnover.
- Access to 26020-Package_Requirements.docx package heading 41 to enumerate the required documents. (TBD — currently locally inaccessible to drafting.)
- Project document-control standard (numbering, revision codes, transmittal format). TBD.
- Reference: DBM-Comp_and_Liquids §"Mechanical Package Structure" (line 617) for the requirement that vendor document registers are a package deliverable.

## Steps

| # | Actor | Step | Notes |
|---|---|---|---|
| 1 | Package Vendor | Establish the Vendor Document Register file using project document-control conventions. | Schema TBD pending project standard. |
| 2 | Package Vendor | Enumerate every document the vendor expects to produce for the package (datasheets, drawings, P&IDs, ITPs, MTRs, manuals, certificates, FAT records). Populate one register row per controlled document number. | ASSUMPTION on granularity (see Guidance Trade-offs). |
| 3 | Package Vendor | Cross-check the enumeration against 26020-Package_Requirements.docx heading 41 list of source-required documents; flag any gaps. | TBD until source accessible. |
| 4 | Package Vendor | As each document reaches issue revision, transmit it to the EPC Integrator with a controlled transmittal reference; update the register row (revision, status, transmittal). | |
| 5 | EPC Integrator | Log receipt; perform interface/integration review against package interfaces, plant-wide design basis, and the DBM. Record review status (accepted / accepted with comments / rejected) per register row. | |
| 6 | Package Vendor | Resolve review comments; resubmit revised documents with new revision codes; update the register and transmittal log. Retain superseded revisions in the register history. | REQ-088-05-07. |
| 7 | Package Vendor + EPC Integrator | When the register is complete (all source-required documents present, all rows at an acceptable status), prepare the turnover transmittal: register, submittal set, source-required documentation, and a turnover record summarizing the package. | |
| 8 | EPC Integrator | Sign the turnover record acknowledging receipt and the integration review state. Note any open items as known issues, not as omissions. | |
| 9 | Package Vendor | Archive the complete package (register, submittals, transmittals, turnover record) per project retention requirements. | Retention requirements TBD. |

## Verification

| # | Check |
|---|---|
| V1 | Register exists and lists each submitted document with current revision, status, and transmittal reference. |
| V2 | Every source-required document from 26020-Package_Requirements.docx heading 41 appears in the register (once enumeration is available). |
| V3 | Every register row at "submitted" status has a matching transmittal record. |
| V4 | EPC Integrator review status is populated for every submitted row. |
| V5 | Turnover record is signed by both Package Vendor and EPC Integrator and dated. |
| V6 | Superseded revisions remain traceable in register history. |
| V7 | No vendor documents exist outside the register (zero-orphan check). |

## Records

The following records result from this procedure and constitute the deliverable:

- **Vendor Document Register** — controlled file with one row per vendor document, including revision history.
- **Vendor Document Submittals** — the actual submitted documents at their issue revisions.
- **Source-Required Vendor Documentation** — the subset of submittals that satisfy 26020-Package_Requirements.docx heading 41.
- **Transmittal Log** — the chronological record of vendor-to-EPC transmittals (may be the register itself if the schema supports it).
- **Turnover Record** — signed acknowledgement of package turnover from Package Vendor to EPC Integrator, with date and any known open items.

Retention period and storage location: TBD pending project document-control standard.
