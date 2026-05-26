# Specification — DEL-070-06 EPC Vendor Package Review and Acceptance

> Normative requirements that the EPC Integrator's acceptance instrument for the PKG-070 Mole Sieve Drier Unit (NGL) vendor package must satisfy. Acceptance of the underlying vendor equipment (DEL-070-04) requires that the criteria below be evidenced; this specification does not restate equipment-level design requirements (those live in DEL-070-02 Package Datasheet and DEL-070-04 Vendor Engineered Equipment Package).

## Scope

**In scope**
- Requirements that the EPC Integrator review-and-acceptance package for PKG-070 must satisfy in order to be issued as binding acceptance evidence.
- Required composition of the acceptance package (review log, checklist, test/inspection evidence summary, turnover evidence summary, disposition record).
- Required cross-references to upstream PKG-070 deliverables (DEL-070-01 SOW, DEL-070-02 Package Datasheet, DEL-070-03 CWP, DEL-070-04 Vendor Engineered Equipment Package, DEL-070-05 Vendor Document Turnover Package).
- Verification approach demonstrating each scope item (SOW-0145–SOW-0148) is addressed.

**Out of scope**
- Equipment-level design requirements for the molecular sieve drier (see DEL-070-02 / DEL-070-04).
- Vendor turnover document production (see DEL-070-05).
- Operations or maintenance procedures post-handover.

## Requirements

| ID | Requirement | Source | Notes |
|---|---|---|---|
| REQ-070-06-01 | The acceptance package SHALL evidence completion of vendor document review for every document listed in the DEL-070-05 turnover package, with disposition (Accept / Accept w/ Comments / Revise & Resubmit / Reject) recorded per document. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on disposition enum | Disposition enum is conventional EPC practice |
| REQ-070-06-02 | The acceptance package SHALL include a checklist line item for each SOW scope item SOW-0145, SOW-0146, SOW-0147, SOW-0148 with evidence reference and pass/fail/conditional ruling. | `_CONTEXT.md` Covers Scope Items | Scope-item text **TBD** until DEL-070-01 SOW is drafted |
| REQ-070-06-03 | The acceptance package SHALL demonstrate that the vendor equipment satisfies the molecular-sieve outlet performance basis: outlet water content <0.1 ppmv H2O expected; cryogenic-protection limit dewpoint <-75 degC at the highest operating pressure. | DBM-Deepcut lines 1254–1255 | Outlet dewpoint <-90 degC is "expected"; <-75 degC is the cryogenic protection limit |
| REQ-070-06-04 | The acceptance package SHALL verify that the supplied adsorbent is 3A molecular sieve; supply of 4A or 5A SHALL result in non-acceptance. | DBM-Deepcut line 1269 | Rationale: 4A/5A can adsorb H2S and cause sulphur spikes in regen loop |
| REQ-070-06-05 | The acceptance package SHALL evidence the BAHX downstream temperature protection interlock: gas temperature on bed bring-online SHALL not exceed 66 degC; exceedance causes facility shutdown. | DBM-Deepcut line 1257 | Interlock testing required during commissioning |
| REQ-070-06-06 | The acceptance package SHALL include FAT records or certified test reports for: inlet filter/coalescers, three adsorber vessels, regeneration gas compressor (2 x 100%), regeneration gas heater, regeneration gas cooler, regeneration gas scrubber, molecular-sieve dust filter, mercury recovery unit, and MRU dust filter. | DBM-Deepcut §Molecular-Sieve Equipment, Controls, and Protection (lines 1274–1287) | Scope reflects equipment list in DBM table |
| REQ-070-06-07 | The acceptance package SHALL evidence pressure-class compliance: molecular sieve system 900# flanges where required. | DBM-Deepcut line 628 | Plant-gate basis MAWP framing |
| REQ-070-06-08 | The acceptance package SHALL evidence MRU media compliance: sulphur-impregnated activated carbon; guaranteed media life ≥6 years; allowable inlet ≤100 µgHg/Nm3; required outlet ≤0.01 µgHg/Nm3; end-of-life pressure drop <6 psi. | DBM-Deepcut line 1286 | Acceptance limits on MRU |
| REQ-070-06-09 | The acceptance package SHALL list and disposition all DBM-flagged open items relevant to PKG-070 (mole-sieve inlet pressure, inlet temperature final estimates, cycle times, adsorbent life, final regen compressor capacity and design differential, regen heater temperature basis, scrubber drain sizing, dry-out header pressure, dry-out header MAWP) as either Resolved (with reference), Conditional Acceptance (with closure plan), or Carried Forward to operations. | DBM-Deepcut line 1291 | Open-items closeout |
| REQ-070-06-10 | The acceptance package SHALL include a turnover evidence summary confirming receipt and completeness of the DEL-070-05 Vendor Document Turnover Package. | `_CONTEXT.md`; sibling DEL-070-05 | Turnover dependency |
| REQ-070-06-11 | The acceptance package SHALL carry a final disposition record signed by an authorized human EPC Integrator representative; agents SHALL NOT issue or certify acceptance. | K-AUTH-1 (CONTRACT.md); ASSUMPTION on signatory level | Binding-approval invariant |
| REQ-070-06-12 | The acceptance package SHALL cross-reference applicable design-basis sections of the DBM-Deepcut and the project-level Package Requirements (`26020-Package_Requirements.docx` heading 24). | `_REFERENCES.md`; `_CONTEXT.md` Source Reference | Heading-24 text location **TBD** |
| REQ-070-06-13 | The acceptance package SHALL document any departures from DEL-070-02 Package Datasheet or DEL-070-01 SOW as either approved deviations (with concession reference) or non-conformances with corrective action. | ASSUMPTION (standard EPC integration practice) | Deviation/NCR handling |

## Standards

| Standard / Document | Use | Source / Location |
|---|---|---|
| West Doe Deepcut DBM (4-25_Deepcut_DBM.md) | Governing facility design basis | `_REFERENCES.md`; `_Sources/DBM-Deepcut/` (locally accessible) |
| `26020-Package_Requirements.docx` heading 24 | Project-level package requirements for PKG-070 | `_REFERENCES.md`; **location TBD** (binary not extracted) |
| BC Energy Regulator Section 12.4 site-alteration permit | Permitting envelope | DBM-Deepcut line 131 (referenced; clause text not in scope of this deliverable) |
| Project-level QA/QC, FAT/SAT, NDE, and turnover procedures | Acceptance evidence framework | **TBD** (project-level QA procedures not enumerated in accessible references) |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-070-06-01 | Inspection: 1:1 reconciliation between DEL-070-05 turnover document index and review-log entries |
| REQ-070-06-02 | Inspection: cross-reference matrix of SOW-0145–SOW-0148 against checklist line items |
| REQ-070-06-03 | Test review: FAT and commissioning dewpoint measurement records; analyzer calibration |
| REQ-070-06-04 | Inspection: vendor material certificates for adsorbent supply |
| REQ-070-06-05 | Test review: commissioning interlock test record for BAHX temperature trip |
| REQ-070-06-06 | Inspection: presence and conformance of FAT certificates for each listed equipment item |
| REQ-070-06-07 | Inspection: pressure-class records on flanges in molecular-sieve scope |
| REQ-070-06-08 | Inspection: MRU media certificate and warranty document; sampling/analysis plan |
| REQ-070-06-09 | Review: open-items disposition table inside the acceptance package |
| REQ-070-06-10 | Inspection: receipt evidence for DEL-070-05 turnover package |
| REQ-070-06-11 | Inspection: signed disposition record by authorized human signatory |
| REQ-070-06-12 | Inspection: explicit cross-reference list within the acceptance package |
| REQ-070-06-13 | Inspection: deviation/NCR log included or referenced |

## Documentation

Acceptance package SHALL include:

- Vendor document review log (per REQ-070-06-01)
- Package acceptance checklist (per REQ-070-06-02)
- Test/inspection evidence summary with attached FAT/SAT, NDE, hydrostatic, and calibration records (per REQ-070-06-06)
- Turnover evidence summary referencing DEL-070-05 (per REQ-070-06-10)
- Open-items disposition table (per REQ-070-06-09)
- Deviation/NCR log (per REQ-070-06-13)
- Signed acceptance disposition record (per REQ-070-06-11)
- Cross-reference list to DBM and Package Requirements heading 24 (per REQ-070-06-12)
