# Guidance — DEL-100-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to give the EPC Integrator a defensible, source-traceable record that the Package Vendor's Hydrogen Peroxide Sweetening Unit (`PKG-100`) has been reviewed and is acceptable for facility integration and handoff. It is the EPC-side counterpart to the vendor-owned engineering/design/equipment/documentation deliverables (`DEL-100-01` through `DEL-100-05`) and supplies the evidence basis needed by `OBJ-004` (vendor/EPC responsibility split) and `OBJ-010` (handoff readiness). (`PACKAGE_REGISTER.csv` PKG-100 responsibility model; `OBJECTIVE_REGISTER.csv` OBJ-004, OBJ-010; `DELIVERABLE_REGISTER.csv` DEL-100-06 Notes)

## Principles

1. **EPC reviews; vendor delivers.** EPC Integrator does not redo vendor engineering, design, or documentation; acceptance evidence is built by review against the vendor outputs. (`PACKAGE_REGISTER.csv` PKG-100; `OBJECTIVE_REGISTER.csv` OBJ-004)
2. **Acceptance is anchored to source.** Each checklist entry cites the underlying source artifact (vendor document ID/section, deliverable ID, or SOW row). Unsourced acceptance is not acceptance. (K-PROV-1; REQ-100-06-12)
3. **Humans certify.** Disposition (accept / conditional / reject) is a human ruling; agents and tools may organize evidence but never issue acceptance. (K-AUTH-1; REQ-100-06-10)
4. **Open items are visible, not hidden.** `SOW-0110` carries explicit TBCs (design conditions, pump capacity); acceptance must surface, not silently close, these. (`SCOPE_LEDGER.csv` SOW-0110)
5. **Interfaces are the integration risk.** The 13 PKG-100 interfaces in `INTERFACE_REGISTER.csv` are the primary integration surface; acceptance is incomplete until each is addressed or explicitly deferred. (`INTERFACE_REGISTER.csv` PKG-100; `OBJ-006`, `OBJ-007`)
6. **Safety and code conformance precede operability.** Sour-service, fire and gas, relief/flare/vent, and electrical-area considerations under `OBJ-009` carry priority in disposition. (`OBJECTIVE_REGISTER.csv` OBJ-009)

## Considerations

- **Coordination with the Package Vendor.** Vendor input is explicitly part of this deliverable (`_CONTEXT.md` Identity: "EPC Integrator (lead) with Package Vendor input"). RFIs and clarifications should be logged, not held informally.
- **"By others" boundary in `SOW-0110`.** Interconnecting piping, DCS integration, foundations, and 600 V MCC supply are EPC-side; acceptance should confirm that EPC-side deliverables exist for these and that the vendor's documentation correctly terminates at the EPC boundary. (`SCOPE_LEDGER.csv` SOW-0110)
- **Electrical driver acceptance.** 575 V / 3 PH / 60 Hz motor basis with starting method DOL or VFD interacts with `OBJ-005` (electrical infrastructure) and the Electrical Power interface (`IFC-62EE7F54FE`). Local control (H-O-A or On-Off) must be consistent with the controls topology under `OBJ-006`.
- **Capacity vs. tank sizing.** Throughput 24,154 BBL/D against 400 BBL H2O2 storage implies dosing-rate and resupply-frequency considerations; this is a vendor-design responsibility but is a fair acceptance question. ASSUMPTION (rationale not stated in source); confirmation pending vendor design.
- **Pump capacity TBC.** Acceptance cannot close on capacity adequacy until the vendor closes the open item; record as a conditional-acceptance item if otherwise complete. (`SCOPE_LEDGER.csv` SOW-0110)
- **Self-framing building (`SOW-0109`).** Site-erected building introduces civil/structural and HVAC interfaces under `OBJ-008` that should not be assumed off-skid.

## Trade-offs

- **Depth of review vs. schedule.** A line-by-line review of every vendor document maximizes assurance but lengthens schedule; risk-based sampling is faster but creates acceptance gaps. The accessible references do not state a project-preferred posture — TBD.
- **Early vs. late acceptance.** Early acceptance lets construction begin sooner; late acceptance reduces rework risk if vendor TBCs change. TBD.
- **Conditional acceptance vs. hold.** Open TBCs in `SOW-0110` can be handled by conditional acceptance with tracked closure (faster) or by holding acceptance until closed (cleaner). Choice depends on EPC integrator procedures — TBD.

## Examples

No worked examples are present in the accessible references. TBD (omit until source examples available; do not invent).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | `_REFERENCES.md` "Missing / Deferred References" states no deliverable-specific source slices were copied during PREPARATION; the skill's Step 1.5 normally requires locally accessible source slices. Decomposition snapshot registers are accessible and authoritative for register-level facts but `26020-Package_Requirements.docx` package heading 52 and the workbook source slices were not opened from `_Sources/`. | `_REFERENCES.md` § Missing / Deferred References | `skills/four-documents/SKILL.md` Step 1.5 | All clause-level claims that would require source slices | PROPOSAL: treat the GATE-07 decomposition snapshot registers as the locally accessible authoritative source set for this run (they encode the workbook row and the Word section content into structured form); flag source-slice deepening as a follow-up enrichment task. | TBD |
| CONF-002 | `_DEPENDENCIES.md` declares no upstream dependencies, yet acceptance logically depends on `DEL-100-01` through `DEL-100-05` being available for review (REQ-100-06-02..04). | `_DEPENDENCIES.md` § Declared Upstream Dependencies | `_CONTEXT.md` § Scope; `DELIVERABLE_REGISTER.csv` DEL-100-06 row | Procedure Prerequisites; Specification Verification | PROPOSAL: declare `DEL-100-01`, `DEL-100-02`, `DEL-100-03`, `DEL-100-04`, `DEL-100-05` as upstream dependencies via `dependency-extract` (out of scope for this skill — `_DEPENDENCIES.md` is metadata and not modified here). | TBD |
| CONF-003 | `SOW-0110` carries explicit TBCs (pump capacity, design conditions); acceptance cannot close on these from the source alone, so REQ-100-06-05 and REQ-100-06-07 inherit TBC. | `SCOPE_LEDGER.csv` SOW-0110 | Specification §§ REQ-100-06-05, REQ-100-06-07 | Specification; Datasheet Conditions; Procedure Verification | PROPOSAL: handle via conditional-acceptance disposition with open-item tracking (Guidance Trade-offs above). | TBD |
