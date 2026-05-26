# Guidance — DEL-098-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so the EPC Integrator can demonstrate, with traceable evidence, that the PKG-098 Tanks, Sour Water (API 650) — 3-25 vendor package is fit for integration into the broader project: that the vendor delivered what was specified, that interfaces match what other packages will tie into, and that the package is ready for construction handoff and operations turnover. The decomposition notes this is a "Gate 5 deliverable framed as EPC-integrator review and acceptance evidence" [`_CONTEXT.md` Notes].

## Principles

1. **Evidence over assertion.** Acceptance statements must be backed by a specific vendor document with rev and date, not by recollection or a verbal commitment. The vendor deliverable list in heading 50 of `_Sources/26020-Package_Requirements.docx` is the canonical checklist; nothing is "accepted" without a corresponding deliverable in hand.
2. **EPC scope is the boundary; vendor scope is the subject.** This deliverable does not re-author the vendor's engineering. It evaluates the vendor's engineering against the EPC Scope of Work (DEL-098-01) and Package Datasheet (DEL-098-02).
3. **By-others items are out of scope to the vendor, not to acceptance.** Foundations, on-site mounting, electrical/instrumentation installation, platforms, and staircases are explicitly by-others per heading 50. Acceptance verifies the vendor did *not* supply them, and that EPC has a clear plan for them; it does not accept those works under this deliverable.
4. **Interface conformance is binary at the line level.** Each interface row from Package Interfaces row 93 is "Yes" or "No". "No" rows must not appear in vendor scope. "Yes" rows must have a verifiable tie-point or interface document.
5. **Open items are surfaced, not silently resolved.** TBDs in the source (operating conditions beyond atmospheric / 10 °C, capacity in Appendix A, driver) must be resolved by the vendor data book before final acceptance, or carried explicitly as conditional acceptances with a closure plan.
6. **No agent or reviewer signs acceptance.** Per project governance, only authorized humans issue binding acceptance. Drafted documents propose dispositions; humans rule. (See `docs/CONTRACT.md` K-AUTH-1 in the controlling framework.)

## Considerations

- **Seven tanks, three service classes.** The package covers three sour produced water tanks (TK-9030-2/9040-2/9050-2), two sour inlet produced water tanks (TK-9010-2/9020-2), and two produced water tanks (TK-9010-1/9020-1). Acceptance should preserve the per-class distinction; do not aggregate MTRs or FAT records across service classes without explicit traceability.
- **Analog versus authoritative source.** The 4-25 Deepcut analog (heading 51 in the same source) lists additional construction details (internal coating, external insulation, electric heating, PVRV/EPRV, LP fuel gas blanket, API 650 modified atmospheric). Heading 50 itself does not restate these. Treat analog content as orienting context only; confirm against the package-50 RFQ `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (referenced in heading 50 as Source Basis) before relying on it for acceptance.
- **Relief / flare / vent coupling.** The package's PSV sizing, relief valve data, flare loads, and blowdown study (PRO-015..PRO-018) feed back into the EPC's Relief and Flare Design Basis (PRO-014). Acceptance should not close until that round-trip is consistent.
- **Cathodic protection and grounding/bonding are "Yes" interfaces.** Vendor scope includes coupons / connections; EPC installation completes them. Acceptance should confirm the vendor-side delivery is sufficient for the EPC-side install.

## Trade-offs

- **Speed of acceptance vs. completeness of evidence.** A conditional acceptance with a small punch list may enable downstream construction sequencing earlier; an unconditional acceptance protects against late surprises but may delay site work. Document the chosen posture explicitly in the acceptance checklist.
- **Granularity of MTR traceability.** Traceability per shell course per tank is the highest-fidelity option; traceability per tank is the practical minimum. Anything coarser than per-tank is below the bar for sour-water service.
- **Reliance on FAT vs. site test.** A successful FAT (MEC-022) is necessary but not sufficient for atmospheric storage tanks erected on site. The acceptance must note any tests deferred to site (hydrotest, settlement survey, coating inspection) and where the responsibility lies.

## Examples

The heading-50 source does not include worked examples. Examples should be drawn from prior project acceptance packages once available; until then, the structural template is the vendor deliverable list itself (heading 50) as a one-row-per-deliverable checklist.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-098-06-01 | API 650 is named in `PKG-098` package name and in the 4-25 analog (heading 51), but heading 50 itself does not restate the design code. | `_CONTEXT.md` PackageName "Tanks, Sour Water (API 650) 3-25"; `_Sources/26020-Package_Requirements.docx` heading 51 paragraph "API 650 modified atmospheric" | `_Sources/26020-Package_Requirements.docx` heading 50 (does not restate) | Datasheet "Design code basis"; Specification REQ-098-06-04, Standards table | Adopt API 650 as the governing code (consistent with package naming and analog), pending confirmation in `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx`. | TBD |
| CONF-098-06-02 | Capacity / design throughput in heading 50 says "See attached in Appendix A", but the Appendix A is not in the locally read slice. | `_Sources/26020-Package_Requirements.docx` heading 50, "Scope Notes / Open Items" | — | Datasheet "Capacity / design throughput"; Specification REQ-098-06-05 | Carry as TBD; resolve by locating Appendix A in the source set or in the vendor data book. | TBD |
| CONF-098-06-03 | Operating temperature is stated as "10 °C" but is followed by "Temperature: TBD" in the same scope-notes block, suggesting two values (operating vs. design) where only one is supplied. | `_Sources/26020-Package_Requirements.docx` heading 50, "Scope Notes / Open Items" | — | Datasheet "Conditions"; Specification REQ-098-06-05 | Treat 10 °C as operating temperature; flag design temperature(s) as TBD pending vendor data book / RFQ. | TBD |
| CONF-098-06-04 | Construction details (coating, insulation, heating, PVRV/EPRV, fuel-gas blanket) appear in the 4-25 analog only, not in heading 50. | `_Sources/26020-Package_Requirements.docx` heading 51 paragraph 5240 | `_Sources/26020-Package_Requirements.docx` heading 50 | Datasheet "Construction" row "Coating / heating / insulation" | Mark as ASSUMPTION based on analog; do not promote to requirement without confirmation in the package-50 RFQ. | TBD |
| CONF-098-06-05 | `_CONTEXT.md` declares the deliverable Supports OBJ-002..OBJ-010, but the mapping is by package-heuristic, not by explicit deliverable-ID rows. | `_CONTEXT.md` "Supports Objectives" | `_Decomposition/.../OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped) | Datasheet Identification table | Treat as ASSUMPTION (best-effort mapping) per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`. | TBD |
