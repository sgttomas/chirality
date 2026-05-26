# Guidance: DEL-066-06 — EPC Vendor Package Review and Acceptance (PKG-066)

> Directional guidance for executing the EPC Integrator review-and-acceptance activity for the Condensate Storage Tanks (4-25) vendor package. Rationale is grounded in `_REFERENCES.md` sources where available; inferential guidance is labeled `ASSUMPTION`. Unresolved tensions are surfaced in the Conflict Table.

## Purpose

This deliverable closes the loop between the EPC Integrator's anchor deliverables (SoW, Package Datasheet, CWP) and the Package Vendor's production-unit outputs (engineered equipment package, document turnover). Its purpose is to produce an auditable acceptance record demonstrating that the as-delivered vendor package is fit to integrate into the 4-25 Deepcut facility tank farm — or to surface what is missing so the gap can be closed before turnover.

Source basis: `_CONTEXT.md` scope statement; `DELIVERABLE_REGISTER.csv` row 503.

## Principles

1. **EPC acceptance is the integration gate, not a design substitute.** The vendor designs the package; the EPC Integrator verifies the package integrates against project-level scope, datasheet, and CWP. The acceptance activity does not re-engineer the package. (Source: deliverable description in `DELIVERABLE_REGISTER.csv` row 503.)

2. **Source-grounded acceptance.** Each acceptance disposition should cite the specific vendor document and the specific EPC anchor document (or DBM clause) that supports it. Acceptance based on prose-level summary is not acceptance.

3. **Coverage over depth, then depth where it matters.** Every enumerated vendor deliverable for `26020-01-PT-19-004 - Tanks, Condensate` should be reviewed and dispositioned. Depth of review concentrates on items that carry safety, integration, or warranty risk: API 650 design conformance, API 2000 blanket-gas sizing, EPRV sizing, blanket/VRU header tie-ins, grounding/cathodic protection, foundation/anchorage. (Source: `26020-Package_Requirements.docx` lines 5012, 5060-5119; `4-25_Deepcut_DBM.md` line 1663 open-items list.)

4. **Defer rather than guess.** Where the DBM or source explicitly defers an item (`TBC`, `TBD`, "remain detailed-engineering review items"), the acceptance package records the deferral with owner and target date rather than fabricating a disposition.

5. **No agent self-acceptance.** Acceptance signature authority rests with the EPC Integrator's responsible discipline lead. (Project K-AUTH-1; signatory roster `TBD`.)

## Considerations

### Tank-package specifics
- The PKG-066 tank set per the Deepcut DBM register comprises 5 tanks (TK-9110-1, -9120-1, -9130-1, -9140-1, -9150-1) at 4-25 (Deepcut) — `4-25_Deepcut_DBM.md` line 2625. Section 16.x of the DBM (lines 1633-1665) describes the operational philosophy: two of the tanks are designated inlet tanks receiving stabilizer bottoms, and condensate cascades by gravity through an internal pipe stand into outlet tanks; sediment and water collect in inlet tanks while cleaner product collects in outlets. Inlet and outlet tanks share a common truck-out connection. The vendor general arrangement and piping/instrumentation must reflect this inlet/outlet philosophy — verify in MEC-016 / MEC-017.
- VRU header connection is mandatory (`4-25_Deepcut_DBM.md` line 1663). Acceptance must confirm vendor-supplied vapour connection points, sizing basis, and tie-in elevation.
- Blanket-gas (API 2000) sizing for the worst-case winter vacuum scenario must be evidenced in the vendor's relief / venting calculations (PRO-014/015/016). Off-spec condensate overhead vent sizing, EPRV sizing, and tank isolation philosophy with possible sour vapours remain detailed-engineering review items (`4-25_Deepcut_DBM.md` line 1663) — do not accept these silently.
- Product tanks are non-insulated; the vendor's documentation should describe any recycle / temperature-maintenance accommodations (`4-25_Deepcut_DBM.md` line 1645). If the vendor introduces insulation, that is a deviation requiring explicit acceptance.

### Source-basis status
- The package requirements text for `26020-01-PT-19-004 - Tanks, Condensate` (4-25) explicitly notes (line 5008): *"Analog basis from 26020-03-PT-19-006_Tanks_Cond ... no direct package-folder brief.md, DOCX, or PDF scope source found for 4-25."* This means the 4-25 scope is derived analogically from the 3-25 condensate-tank package. Acceptance reviewers must be alert to the risk that vendor assumptions reflect the 3-25 analog rather than 4-25-specific facts (tank count, tags, sources, recycle paths).
- The package requirements text further lists open items (line 5013): "confirm the tank count, tags, capacity, inlet/outlet sources, whether mercaptan treating bypass/recycle paths apply, VRU/blanket-gas tie-ins." These open items should be carried explicitly in the DBM-open-items disposition annex.

### Sibling-deliverable dependencies
- The acceptance activity is downstream of: DEL-066-01 (SoW), DEL-066-02 (Package Datasheet), DEL-066-03 (CWP) on the EPC side; and DEL-066-04 (Vendor Engineered Equipment Package), DEL-066-05 (Vendor Document Turnover Package) on the vendor side. None of these are formally declared as upstream in `_DEPENDENCIES.md` (Coordination Mode: DECLARED; none declared during PREPARATION). The acceptance reviewer should treat sibling maturity as an informal precondition and surface any maturity gap as a hold rather than proceeding silently.

## Trade-offs

| Trade-off | Choice direction |
|---|---|
| Accept early to maintain schedule vs. defer to gather missing evidence | Default to defer for items affecting safety (relief, venting, blanket gas, grounding, foundations); accept-with-conditions only for items with low integration risk and a credible close-out plan. |
| Detailed re-derivation of vendor calculations vs. spot-check | Spot-check by default; full re-derivation only when vendor calculations conflict with the DBM or Package Datasheet. |
| Per-tank acceptance vs. per-package acceptance | Per-package acceptance is the default boundary (the package is the vendor production unit); per-tank deviations are recorded as conditions on the package acceptance. (ASSUMPTION; project precedent `TBD`.) |
| Acceptance based on FAT alone vs. FAT + site verification | Where FAT covers the verification scope (e.g., dimensional, hydrostatic), FAT suffices; site verification is required for items that depend on installation (foundations, grounding network connection, tie-in alignment). |

## Examples

No worked examples are present in the locally accessible sources. (`TBD` — examples to be developed in `MEMORY.md` as the acceptance activity executes and produces real disposition records.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-066-06-01 | Workbook row identifier for PKG-066: `_CONTEXT.md` and `_REFERENCES.md` state "row 89"; the Deepcut DBM register lists `Tanks, Condendate (API 650) 2` at numeric row "90" (with row 89 = `FRESH CAUSTIC STORAGE TANK (4-25)`). | `_CONTEXT.md` line 49; `_REFERENCES.md` line 14 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2624-2625 | Datasheet (Identification); decomposition row trace | PROPOSAL: treat the row number as a label inherited from the source workbook; defer reconciliation to the next decomposition refresh, since the package-name match is unambiguous. | TBD |
| CONF-066-06-02 | Tank count: the Deepcut DBM operational section (line 1639) states "Local 04-25 condensate storage = 4 x 3,800 bbl tanks"; the package register (line 2625) lists 5 tags (TK-9110-1 through TK-9150-1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1639 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2625 | Datasheet (Attributes — Storage capacity); Specification (REQ-066-06-05) | PROPOSAL: the 5th tag is likely the slop tank (`Condensate slop tank`, fully insulated, `4-25_Deepcut_DBM.md` line 1644) or an inlet tank distinction; acceptance reviewer should confirm tag-to-service mapping against MEC-002 (Mechanical Equipment List) before accepting. | TBD |
| CONF-066-06-03 | Acceptance disposition vocabulary and document-control coding scheme are referenced indirectly (via DOC-008) but no project-defined vocabulary is present in the locally accessible sources. | `26020-Package_Requirements.docx` line 5064 | (no counter-source) | Specification (REQ-066-06-02, REQ-066-06-10); Procedure (Steps) | PROPOSAL: adopt a placeholder vocabulary (ACCEPT / ACCEPT-WITH-CONDITIONS / REJECT / DEFER) until the project document control procedure (DOC-008) is read; reconcile and reissue if the project standard differs. | TBD |
| CONF-066-06-04 | Slop-tank scope inclusion: the DBM (line 1665) describes the condensate slop tank as receiving from multiple sources; PKG-066 is named "Tanks, Condensate (API 650) 4-25" and the package-register row (2625) tags only the 5 storage tanks. Whether the slop tank is in PKG-066 or in a separate package is not explicitly stated in the locally accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1644, 1661-1665 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2625; `_CONTEXT.md` | Specification (REQ-066-06-05 scope note); Datasheet (Attributes — insulation) | PROPOSAL: treat PKG-066 scope as on-spec condensate product storage only (TK-9110-1…-9150-1); confirm against EPC SoW (DEL-066-01) before issuing acceptance. | TBD |
