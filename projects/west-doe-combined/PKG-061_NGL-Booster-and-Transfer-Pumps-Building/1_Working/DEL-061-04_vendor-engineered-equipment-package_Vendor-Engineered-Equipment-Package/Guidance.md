# Guidance: DEL-061-04 Vendor Engineered Equipment Package — NGL Booster and Transfer Pumps Building

## Purpose

This document provides directional guidance for the Package Vendor and EPC Integrator on producing the vendor-engineered equipment package for `PKG-061` (NGL Booster and Transfer Pumps Building). It supports — but does not replace — the Specification (normative requirements) or the EPC Package Datasheet `DEL-061-02` (authoritative design inputs).

Per the decomposition (`DELIVERABLE_REGISTER.csv` row 417), this deliverable exists because the EPC Integrator anchors what must be built (`DEL-061-01`, `DEL-061-02`, `DEL-061-03`) while the Package Vendor is the party that engineers and supplies the physical equipment package.

## Principles

- **Source fidelity over convention.** Design values come from the EPC Package Datasheet (`DEL-061-02`) and the upstream DBM (`4-25_Deepcut_DBM.md`). Where source values are absent or ambiguous, mark them `TBD` rather than supplying convention-based defaults.
- **API 610 first.** The DBM Trace Appendix row 58 fixes the pump configuration as "API 610, multi-stage can." All subsequent decisions (seal, baseplate, instrumentation, FAT) should be consistent with that family.
- **Cold-climate readiness.** The facility operates with sister liquid-pump services designed for cold-climate startup (DBM-Deepcut line 1679 references -40 deg C startup for condensate transfer pumps). Apply the same climate envelope unless `DEL-061-02` explicitly relaxes it.
- **Interface honesty.** The Vendor is the authoritative source for the engineered package; the EPC Integrator is the authoritative source for what the package must interface to. Disagreements are surfaced (Conflict Table) rather than silently reconciled.
- **Traceability to objectives.** All design choices traceable back through `SOW-0149..0152` to `OBJ-001, OBJ-003..OBJ-010` (per `OBJECTIVE_SCOPE_MAP.csv` PKG-061 entries).

## Considerations

- **NPSH margin.** Sister condensate transfer pumps in the same facility were sized for NPSHR ≤ 0.75 m because tanks are not elevated (DBM-Deepcut line 1677). NGL booster service likely faces a similar NPSH constraint downstream of NGL storage bullets; the Vendor should size accordingly and flag exceedances early. (ASSUMPTION — confirm in `DEL-061-02`.)
- **Multi-stage can selection.** "Multi-stage can" implies vertical can (VS) pump topology to gain submerged NPSH. Vendor selection of the inner-bowl assembly should be driven by NPSHa, design flow, and required differential. Specific values `TBD` until `DEL-061-02` content is parsed.
- **Driver sizing for cold startup.** Sister pumps were sized for startup density at -40 deg C (DBM-Deepcut line 1679). Apply the same startup-density check to NGL composition extremes.
- **Minimum-flow protection.** Continuous transfer service typically requires minimum-flow recycle (DBM-Deepcut line 1679 for sister service). Vendor should propose minimum-flow protection consistent with API 610 and the EPC Datasheet.
- **Building / enclosure integration.** "Building" in the package name implies a heated enclosure; package skid arrangement, lifting, and access should be coordinated with the EPC Integrator's building / civil design (`DEL-061-03`).

## Trade-offs

- **Single vs. dual mechanical seal.** Single mechanical seals are typical for many API 610 services (DBM-Deepcut line 1174 shows single mechanical seal on Amine Booster Pumps), but NGL service may warrant dual seals with API Plan 53/54 for emission and reliability reasons. Trade-off to be made against `DEL-061-02` HSE and emissions requirements.
- **Sparing — 2 x 100% vs. 2 x 50%.** DBM-Deepcut row 58 gives count = 2 without explicit sparing percentage; sister condensate transfer service was 2 x 150% to support fast pump-down (DBM-Deepcut line 1673). Vendor should confirm sparing assumption with EPC Integrator before locking driver sizing.
- **Skid extent.** Larger skids reduce field interfaces but raise transportation cost and constrain layout in the building. The EPC Construction Work Package (`DEL-061-03`) should drive the split.

## Examples

- **Sister service precedent — condensate transfer pumps `P-9210-1/P-9220-1`:** 2 x 150%, both pumps capable of simultaneous operation, 350 kPad / 50 psid differential to liquids hub, NPSHR ≤ 0.75 m, minimum-flow control valve, motor sized for -40 deg C startup density (DBM-Deepcut lines 1673–1679). Useful as a design pattern; not a substitute for NGL Booster duty data, which is `TBD` in `DEL-061-02`.
- **Sister service precedent — amine booster pumps:** 2 x 115%, single-stage vertical inline, single mechanical seal (DBM-Deepcut line 1174). Different topology (inline, not multi-stage can) but illustrates the project's preference for vertical configurations and single seals where service permits.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-061-04-01 | Authoritative duty data location | `_REFERENCES.md` cites `26020-Package_Requirements.docx` package heading 17 | The cited `.docx` is not locally text-accessible; DBM-Deepcut Trace Appendix row 58 carries only equipment count, tags, and configuration | Datasheet "Conditions"; Specification R-061-04-04, R-061-04-06, R-061-04-07, R-061-04-11, R-061-04-12 | PROPOSAL: Re-extract `26020-Package_Requirements.docx` package heading 17 to markdown and copy the package-17 slice into `_REFERENCES.md` so the four documents can be source-grounded rather than `TBD`-heavy | TBD |
| C-061-04-02 | Sparing philosophy | DBM-Deepcut row 58 shows count = 2 without explicit sparing % | DBM-Deepcut Sparing table does not include "NGL Booster" row | Datasheet "Conditions" (Sparing philosophy); Specification R-061-04-12 | PROPOSAL: Default to 2 x 100% pending EPC Package Datasheet confirmation; do not select drivers until confirmed | TBD |
| C-061-04-03 | Authority for sister-service design patterns | Sister condensate transfer pump basis (DBM-Deepcut lines 1673–1679) | No explicit NGL Booster basis in DBM-Deepcut | Guidance "Examples", "Considerations" | PROPOSAL: Treat sister-service patterns as illustrative only; do not import values until `DEL-061-02` confirms applicability | TBD |
