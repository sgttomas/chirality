# Specification — DEL-048-06 EPC Vendor Package Review and Acceptance

## Scope

### In Scope
EPC Integrator-led activities to review, accept, and document handoff readiness of the Package Vendor's Inlet/Sales Compressor package against:
- The EPC Scope of Work (`DEL-048-01`),
- The Package Datasheet (`DEL-048-02`),
- The Construction Work Package (`DEL-048-03`),
- The Vendor Engineered Equipment Package (`DEL-048-04`),
- The Vendor Document Turnover Package (`DEL-048-05`).

Source: `_CONTEXT.md` Scope; GATE-07 SCOPE_LEDGER SOW-0115 (PKG-048 split between Package Vendor engineering/design/equipment and EPC Integrator facility integration).

### Out of Scope
- Detailed design of the compressor package itself (Package Vendor scope per SOW-0115).
- Shipping, pile installation, tie-in piping, electrical connections, and mounting platform/stairs are explicitly "By others" within SOW-0118 — these are EPC Integrator execution scope but are not the subject of this review-and-acceptance deliverable. ASSUMPTION: such activities are reviewed under their own deliverables (location TBD).

## Requirements

REQ-1. **Vendor document review coverage** — The EPC Integrator SHALL produce a review log covering all vendor documents within the Vendor Document Turnover Package (`DEL-048-05`). Source: ARTIFACT_REGISTER ART-F8E220700B; SOW-0115.

REQ-2. **Acceptance checklist completion** — The EPC Integrator SHALL execute and record completion of a package acceptance/turnover checklist. Source: ARTIFACT_REGISTER ART-7862D9EB63.

REQ-3. **Test and inspection evidence** — The EPC Integrator SHALL collect and verify factory/shop test and inspection evidence from the Package Vendor. Source: ARTIFACT_REGISTER ART-00AE5AE3CA. Detailed test scope: TBD (source-specific where available; not extracted in GATE-07).

REQ-4. **Specification conformance — Equipment count and model** — Reviewer SHALL verify the delivered package comprises five (5) Ariel KBC/6 three-stage reciprocating compressors. Source: SOW-0116.

REQ-5. **Sizing margin** — Reviewer SHALL verify each compressor is sized for 120% of design. Source: SOW-0116.

REQ-6. **Service split** — Reviewer SHALL verify single-stage inlet and double-stage sales gas configuration. Source: SOW-0116.

REQ-7. **Driver conformance** — Reviewer SHALL verify each unit is driven by a DOL 8-pole induction motor with soft-start, rated 6600 V / 3PH / 60 Hz, 891 RPM, TEFC or WPII enclosure with non-sparking bidirectional cooling fan, in accordance with NEMA MG 1. ASSUMPTION (location TBD): preferred motor frame KBZ and preferred make WEG are stated preferences, not mandatory acceptance criteria. Source: SOW-0117, SOW-0118.

REQ-8. **Driver rated power** — Reviewer SHALL verify rated motor power. CONFLICT: SOW-0117 states 5,000 kW (6,700 HP) per unit (Major Included Equipment); SOW-0118 states 5,220 kW (7,000 HP) per unit (Scope Notes). Both cite ~10% excess over design. See Guidance Conflict Table CFLT-1. Acceptance value: TBD pending human ruling.

REQ-9. **Total connected load** — Reviewer SHALL verify aggregate 5-unit connected load of 26,100 kW (35,000 HP). Source: SOW-0118. NOTE: not arithmetically consistent with REQ-8 candidate values (5 × 5,000 = 25,000 kW; 5 × 5,220 = 26,100 kW). Supports SOW-0118 (7,000 HP / 5,220 kW) interpretation. See CFLT-1.

REQ-10. **Suction scrubber configuration** — Reviewer SHALL verify two-phase suction scrubbers upstream of each stage, vertical flow vane-style demisters (horizontal or vertical acceptable), K factor ≤ 0.5 Imperial plus pressure de-ration, liquid density basis 0.61 SG. Source: SOW-0117.

REQ-11. **Air cooler configuration** — Reviewer SHALL verify one common air cooler frame per package for both services, with automated pneumatic louver temperature control per process bundle. Source: SOW-0117.

REQ-12. **Operating/design conditions** — Reviewer SHALL verify operating and design conditions match SOW-0118 (inlet: 4,309 / 7,791 kPag; sales: 3,034 / 10,343 kPag; capacities 1,766 / 1,630 e3m3/d; no turndown).

REQ-13. **Scope-split confirmation** — Reviewer SHALL confirm "by-others" items in SOW-0118 (shipping, pile install, tie-in piping, electrical connections, mounting platform/stairs) are addressed under EPC Integrator scope and are excluded from vendor acceptance criteria.

REQ-14. **Turnover readiness** — Reviewer SHALL produce turnover evidence demonstrating handoff readiness to operations/commissioning. Detailed content of turnover evidence: TBD (artifact list in `_CONTEXT.md` but not itemized in GATE-07 register).

REQ-15. **Traceability to objectives** — Acceptance records SHALL trace to the supported objectives (OBJ-001, OBJ-003 through OBJ-010) per OBJECTIVE_DELIVERABLE_MAP. ASSUMPTION (PACKAGE_HEURISTIC): objective association is package-level; specific objective texts not extracted into this deliverable's local references — location TBD.

## Standards

- NEMA MG 1 — Motors and Generators (driver enclosure/rating reference). Source: SOW-0118. Clause-level location: TBD.
- API standards for reciprocating compressors (e.g., API 618), pulsation studies, and packagers: TBD — not cited in extracted source slices for this package.
- ASME B31.3 / equivalent piping code: TBD — not cited in extracted source slices.

## Verification

| Requirement | Verification Method | Evidence Artifact |
|---|---|---|
| REQ-1 | Document review log walkthrough | ART-F8E220700B |
| REQ-2 | Checklist completion review | ART-7862D9EB63 |
| REQ-3 | Witness/review of factory & shop test records | ART-00AE5AE3CA |
| REQ-4..REQ-7, REQ-10..REQ-12 | Vendor data sheet vs. specification comparison | ART-F8E220700B |
| REQ-8 (after ruling) | Nameplate review against ruled value | ART-F8E220700B |
| REQ-9 | Electrical load summary cross-check | ART-F8E220700B |
| REQ-13 | Scope-split confirmation memo | ART-7862D9EB63 |
| REQ-14 | Turnover package walkdown | Turnover evidence (TBD) |
| REQ-15 | Traceability matrix to OBJECTIVE_DELIVERABLE_MAP | ART-7862D9EB63 |

## Documentation

Deliverable shall produce:
- Vendor document review log (ART-F8E220700B)
- Package acceptance checklist (ART-7862D9EB63)
- Test/inspection evidence (ART-00AE5AE3CA)
- Turnover evidence (TBD artifact ID)

Source: `_CONTEXT.md` Anticipated Artifacts; GATE-07 ARTIFACT_REGISTER rows 3496-3498.
