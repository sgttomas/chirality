# Guidance — PKG-068 TEG Dehydration Unit (Package Datasheet)

## Purpose

The Package Datasheet exists to give a third-party Package Vendor the EPC-Integrator-authored technical handoff data required to engineer, design, document, and physically supply the TEG Dehydration Unit. It is the mandatory Gate 5 EPC anchor deliverable for `PKG-068` and the single place where workbook interface facts are carried as evidence rather than being decomposed into standalone deliverables (`_CONTEXT.md` Notes).

It supports objectives `OBJ-001` (04-25 facility scope through gas dehydration), `OBJ-003` (commercial/boundary preservation), `OBJ-004` (vendor/EPC responsibility split), `OBJ-005` through `OBJ-009` (electrical, controls, utilities, civil/structural, safety/regulatory interfaces), and `OBJ-010` (handoff readiness and open-item closure). PACKAGE_HEURISTIC association — ASSUMPTION (best-effort mapping per `_CONTEXT.md`).

## Principles

1. **Source-first.** Process and equipment design values come from the 04-25 DBM (SEC-06 Process-Gas TEG Dehydration Basis). Workbook scope and interface columns set EPC integration responsibilities. Decomposition narrative is structure; sources are authority.
2. **EPC integration vs vendor package engineering.** The EPC Integrator authors this datasheet to define *what* the vendor must deliver and *how it interfaces with the facility*. The vendor is responsible for *how the package is engineered and built*. This split is preserved per `OBJ-004` and the `PACKAGE_REGISTER.csv` Responsibility Model.
3. **Open items remain visible.** TBC / TBD items from the DBM are surfaced in the Conflict Table below rather than silently resolved. A vendor cannot freeze design against an unresolved facility-level basis (e.g., 1100 vs 1085 psig operating pressure).
4. **Interface evidence carried, not duplicated.** All 13 PKG-068 interface facts from `INTERFACE_REGISTER.csv` are listed in the Datasheet rather than spawning per-interface deliverables. Per-interface evidence artifacts (ART-F80D7E8B07 …) are by-design captured here.
5. **Conservative inference.** Where the workbook scope list and the DBM appear to differ (e.g., "Burner Control Panel" vs heat-medium-fired reboiler), record the discrepancy and ask the vendor to confirm rather than silently selecting one.

## Considerations

- **Reboiler firing configuration.** The workbook package scope lists a "Burner Control Panel," which is typical for direct-fired TEG reboilers. The 04-25 DBM SEC-06 explicitly specifies a 425 degF heat-medium-fired reboiler (BKU type) drawn from the facility single-loop heat-medium system (SEC-09). Both cannot be true. The reasonable EPC interpretation is heat-medium fired (DBM is authoritative); the burner-control-panel line item likely reflects either a legacy generic workbook scope description or a small auxiliary fired-equipment item (e.g., make-up tank heater). This must be confirmed.
- **Contactor sparing.** The DBM leaves contactor sparing TBD (1 x 100% vs 2 x 50%). This is a vendor-impacting decision because it changes vessel sizing, plot space, and pipe-rack tie-ins. EPC should close this before vendor RFQ to avoid scope-change risk.
- **Sour-service material discipline.** Although the gas is post-amine "sweet," residual H2S/COS/mercaptans and the carbon-filter slipstream create methyl mercaptan exposure that is flagged in the DBM TEG Open Items. Material selection and TEG carbon-filter location should follow facility sour-service philosophy; specific clauses to be cited from SEC-15.
- **VRU vs blanket-gas convention.** The TEG make-up tank is intentionally *not* connected to VRU and uses a fuel-gas blanket. Vendor must not propose VRU tie-in for this tank.
- **Stripping-gas economy.** Three flow cases are provided (56.8 / 111.8 / 136.4 SCFM at 22.5 / 44.3 / 45.0 USGPM). The vendor should size LP fuel-gas piping and metering for the design case (136.4 SCFM) with turndown to the lowest case.
- **Heat integration coupling.** Dehydrated gas leaves the package and goes to the inlet/TEG dehydration cross-exchanger (outside this package), which is itself open on warm-side stream identity (see DBM SEC-04). This may iterate the package outlet thermal/pressure conditions.

## Trade-offs

- **1 x 100% vs 2 x 50% contactor.** Single contactor is cheaper, simpler, smaller plot but creates a single-train availability constraint; two-vessel basis improves availability and turndown flexibility but increases vessel/piping cost and plot space. Trade-off resolution depends on facility availability targets — not stated in DBM TEG section; TBD.
- **Bloc-welded plate vs shell-and-tube lean/rich exchanger.** Plate is more compact and gives closer approach (better TEG regeneration economy) but is harder to clean if fouling occurs and excludes polymer gaskets. The DBM preference is bloc-welded plate, with sparing and type marked TBC. Vendor may propose alternatives with justification.
- **Direct-fired vs heat-medium reboiler.** Direct-fired is independent of facility heat-medium loop (resilience) but creates a fired-equipment permitting and emissions burden; heat-medium fired centralizes emissions and integrates with facility energy management. DBM choice is heat-medium fired.

## Examples

- **Outlet water spec interpretation.** The contactor design outlet water spec is `<=4 lb H2O/MMSCF`. This is the contractual performance number. The downstream mol-sieve unit can tolerate up to 10 lb H2O/MMSCF; the 4 lb basis preserves mol-sieve bed life and cycle margin.
- **Flash-gas routing.** TEG flash drum operates at 60 psig specifically so flash gas can self-flow to the stabilizer overheads compressor first-stage suction at ~50 psig without dedicated boost compression. Vendor should not lower flash-drum pressure below this floor.
- **Outlet temperature interlock on lean TEG cooler.** Lean TEG outlet is "110 degF or 15 degF above contactor inlet gas temperature, whichever is lower." This avoids hydrocarbon condensation in lean TEG when ambient is warm, while preventing absorption-temperature mismatch in winter.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-068-02-01 | Operating pressure basis: 1100 psig / 7584 kPag vs unresolved 1085 psig / 7481 kPag unit-level basis. | `4-25_Deepcut_DBM.md` SEC-06 TEG Design Values (1100 psig "basis, to be confirmed") | `4-25_Deepcut_DBM.md` SEC-06 TEG Design Values (1085 psig unit-level alternate, unresolved) | Datasheet Conditions; Specification REQ-068-02-005 / -090; vessel design pressures | PROPOSAL: hold at 1100 psig basis until facility-level reconciliation memo issued. | TBD |
| CFT-068-02-02 | Reboiler firing: workbook scope lists "Burner Control Panel" (implying direct-fired) vs DBM specifies 425 degF heat-medium-fired BKU reboiler. | `PACKAGE_REGISTER.csv` PKG-068 scope column | `4-25_Deepcut_DBM.md` SEC-06 TEG Equipment table; SEC-09 single-loop heat-medium basis | Datasheet equipment scope; Specification REQ-068-02-015 / -093 | PROPOSAL: adopt heat-medium fired reboiler per DBM authority; treat the burner-control-panel scope-list line as auxiliary fired-equipment control (e.g., make-up tank heater) pending vendor clarification. | TBD |
| CFT-068-02-03 | Contactor sparing: 1 x 100% unit-level vs 2 x 50% contactor-vessel basis. | `4-25_Deepcut_DBM.md` SEC-06 TEG Equipment ("vessel sizing basis 102 in ID x 60 ft S/S. Final contactor sparing/configuration is TBD.") | `4-25_Deepcut_DBM.md` SEC-06 TEG Open Items (explicit TBD) | Datasheet sparing table; Specification REQ-068-02-012 / -091 | PROPOSAL: defer to EPC availability-target decision; recommend 1 x 100% if facility availability budget tolerates planned outage. | TBD |
| CFT-068-02-04 | Lean/rich exchanger type and sparing. | `4-25_Deepcut_DBM.md` SEC-06 TEG Equipment (bloc-welded plate, 1 x 100%, "type and sparing to be confirmed") | TEG Open Items (lean/rich exchanger type and sparing TBC) | Datasheet construction; Specification REQ-068-02-014 / -092 | PROPOSAL: hold at bloc-welded plate 1 x 100% in RFQ; allow vendor alternates with justification. | TBD |
| CFT-068-02-05 | Workbook Package Requirements .docx clauses not text-readable in this run. | `_REFERENCES.md` cites `26020-Package_Requirements.docx` package heading 23 | binary file; no text extraction performed | Specification Standards table; vendor-document standards rows | PROPOSAL: extract .docx to markdown in a later pass and cite specific clauses; current entries marked `location TBD`. | TBD |
| CFT-068-02-06 | Material selection / sour-service grade selection; methyl mercaptan exposure on TEG carbon filter location. | `4-25_Deepcut_DBM.md` SEC-06 TEG Open Items | SEC-15 Regulatory, Codes, and Standards Basis (referenced via OBJ-009; specific clauses not consulted this pass) | Datasheet construction (Materials row); Specification REQ-068-02-094 / -097 | PROPOSAL: follow facility sour-service philosophy; relocate / qualify TEG carbon filter per detailed engineering review. | TBD |
| CFT-068-02-07 | Ambient design conditions specific to TEG package. | `4-25_Deepcut_DBM.md` (DBM defines facility-wide ambient elsewhere; section not cited in this pass) | none secondary | Datasheet Conditions (Ambient row); Specification REQ-068-02-095 | PROPOSAL: cite facility ambient basis section in a later pass. | TBD |
