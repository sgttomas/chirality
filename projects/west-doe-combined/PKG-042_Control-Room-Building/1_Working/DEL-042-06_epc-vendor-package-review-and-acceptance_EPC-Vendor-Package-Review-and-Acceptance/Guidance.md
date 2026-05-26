# Guidance — DEL-042-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to give the project an auditable record that the Package Vendor's Control Room Building package has been reviewed, integration-accepted, and is ready for handoff into the larger facility. It is the EPC Integrator's evidence layer that the responsibility split (vendor owns engineering/design/equipment/documentation; EPC owns facility integration) was honored and verified.

Source: `PACKAGE_REGISTER.csv` row PKG-042 Responsibility text; OBJ-004; `DELIVERABLE_REGISTER.csv` row DEL-042-06.

## Principles

1. **EPC review, not vendor redesign.** The EPC Integrator's role here is review, integration acceptance, and handoff readiness — not re-engineering the vendor package. (Source: OBJ-004; DELIVERABLE_REGISTER row DEL-042-06.)
2. **Acceptance is anchored to the EPC's own upstream deliverables.** The vendor package is judged against `DEL-042-01` (SoW), `DEL-042-02` (Package Datasheet), and `DEL-042-03` (Construction Work Package). If those anchors are ambiguous, the right move is to fix the anchor, not to invent an acceptance criterion here.
3. **Interface-by-interface evidence.** PKG-042 carries a fixed list of facility interfaces (see Datasheet). Each interface type should be visible in the acceptance record.
4. **Closure conditions over completeness theatre.** OBJ-010 lists explicit closure conditions (operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, open-item closure). Acceptance evidence should map to these — not to a generic checklist.
5. **No agent certification.** Acceptance, sign-off, and approval are human acts. This deliverable records and structures evidence; it does not issue approval.

## Considerations

- The Control Room Building is an Electrical-discipline package, but its interface list pulls in I&C, Communications, HVAC, Fire & Gas, Civil/Structural, and Utility scope. Reviewers should not narrow attention to electrical line items only.
- The decomposition does not separate "engineering review" from "construction review"; both belong inside this single deliverable's checklist for PKG-042. (Source: `DELIVERABLE_REGISTER.csv` row DEL-042-06 anticipated artifacts.)
- Sour-service applicability for PKG-042 is `TBD` in available sources. If sour-service safety boundaries apply, OBJ-009 criteria must be incorporated explicitly.
- 26020-Package_Requirements.docx defines the vendor-document table expected for review (cited by OBJ-004 and OBJ-010). When that slice becomes locally accessible, the acceptance checklist should be reconciled against it. Until then, the vendor-document expectations remain partially `TBD`.

## Trade-offs

| Trade-off | Direction |
|---|---|
| Depth of review vs. schedule | Favor depth on interfaces and OBJ-010 closure conditions; avoid duplicating vendor design verification that the vendor's own QA already covers. |
| Centralized acceptance checklist vs. discipline-specific notes | Use a single acceptance checklist as the index; allow discipline sub-notes as evidence attachments. |
| Open-item tolerance at acceptance | Prefer explicit open-item closure log rather than informal "carry forward" notes; OBJ-010 calls out "controlled open-item closure evidence". |

## Examples

No locally accessible source examples are available for this deliverable in the current reference set. Concrete example checklist structures and vendor-document review templates SHOULD be derived from project-standard templates when those become accessible. `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| none | None observed between accessible sources at Pass 2. | — | — | — | — | TBD |
