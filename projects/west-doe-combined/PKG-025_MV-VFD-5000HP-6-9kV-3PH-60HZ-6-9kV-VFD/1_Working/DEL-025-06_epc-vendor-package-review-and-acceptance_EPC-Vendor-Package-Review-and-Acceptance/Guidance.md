# Guidance — EPC Vendor Package Review and Acceptance (DEL-025-06)

## Purpose

This guidance directs the EPC Integrator's review and acceptance of the PKG-025 MV VFD vendor package. Acceptance closes the loop between the EPC anchor deliverables (SOW, Datasheet, CWP) and the vendor-provided equipment and documentation packages, and provides the binding evidence that the facility may integrate the MV VFD into the 6.9 kV inverter-drive motor service. Source: `_CONTEXT.md` Scope; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Medium-voltage services.

## Principles

1. **Acceptance is anchored, not improvised.** Use only the accepted revisions of `DEL-025-01` (SOW), `DEL-025-02` (Datasheet), and `DEL-025-03` (CWP) as the acceptance basis. (Source: `DELIVERABLE_REGISTER.csv`.)
2. **Trace, do not retell.** Every acceptance line shall reference a specific SOW / Datasheet / CWP origin and a specific vendor-evidence origin.
3. **Bind decisions to humans.** Per Chirality governance (K-AUTH-1), acceptance is a binding decision; agent output is at most a proposal. (ASSUMPTION on citation; no project-source restatement.)
4. **Treat deviations as routed events.** A vendor design that does not match the EPC basis is not silently accepted; it is recorded, routed, and resolved.

## Considerations

- The DBM specifies 6.9 kV service for inverter-drive motors **5,500 hp and above** (`4-25_Deepcut_DBM.md` line 2935). The package title carries "5000HP". Confirm whether this is the package-level rating, a motor frame rating, or a legacy value (see Conflict Table CFT-1).
- The DBM places MV VFDs inside prefabricated MV electrical buildings shared with MV switchgear, MCCs, RVSS, UPS, transformers, and PLC panels (`4-25_Deepcut_DBM.md` line 2973). Building integration is therefore a real interface review item, not a bookkeeping line.
- PKG-025 declares six interface types (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). Each warrants explicit acceptance evidence; absence of evidence on any interface is an acceptance gap, not a clean pass.
- No deliverable-specific source slices were copied during PREPARATION (`_REFERENCES.md` Missing / Deferred References). Source-grounding is therefore limited to the DBM and the Gate 7 registers; vendor-specific clause-level requirements (e.g., IEEE 519 harmonic limits, NEMA ICS 7 inverter ratings) are `TBD` until accepted source slices are added.

## Trade-offs

- **Acceptance depth vs schedule.** Deeper FAT review is slower; in absence of a stated FAT scope in accessible sources, scope is `TBD` and should be confirmed at the package kickoff between EPC and Vendor.
- **Vendor-standard vs project-specific documentation.** Accepting vendor-standard document classes simplifies turnover but may understate project-specific items (e.g., the BC Hydro utility interface). Prefer project-specific where the DBM cites the topic.
- **Conditional acceptance vs reject-and-resubmit.** Conditional acceptance compresses schedule but creates open items; ensure each open item is tracked to closure before any handoff to operations.

## Examples

(Examples from accessible sources only.)

- The DBM identifies "Starting VFDs … for the KM-2150/2250 Inlet/Sales Gas Compressor motors" (line 2955). If the PKG-025 MV VFD is the starting VFD for these compressor motors, acceptance must confirm synchronous transfer compatibility with `MCC-8200`. **ASSUMPTION** — the link between PKG-025 and KM-2150/2250 is not asserted in accessible sources; treat as directional context only.
- The DBM forbids power-factor-correction capacitor banks on the MCC-8200 synchronous-transfer bus (line 2955). If the vendor VFD package proposes PF capacitors at that interface, acceptance must reject or route the deviation.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CFT-1 | Package title and `_CONTEXT.md` state "5000HP" for the MV VFD package; DBM states 6.9 kV service is for inverter-drive motors **5,500 hp and above**. | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` (PKG-025) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2935 | Datasheet Attributes (Subject package); Specification REQ-025-06-03; Procedure Step 3 (rating verification) | PROPOSAL: keep "5000 HP" as title/identity only; treat HP rating as `TBD` pending vendor confirmation or EPC ruling on 5,500 hp DBM threshold. | TBD |
| CFT-2 | Acceptance depth (witness/hold points, FAT scope, document classes) is not specified in accessible project sources. | `_CONTEXT.md` Anticipated Artifacts (high-level only) | `_Sources/` — `26020-Package_Requirements.docx` (binary, not opened) | Specification §Standards; Specification REQ-025-06-06; Procedure Steps 6-7 | PROPOSAL: open `26020-Package_Requirements.docx` for PKG-025 / 26020-class requirements and re-run drafting (Pass 3 or new run). | TBD |
| CFT-3 | Whether PKG-025 supplies the starting VFD for KM-2150/2250 compressor motors is not stated in accessible sources but is suggested by DBM line 2955. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2955 | `_CONTEXT.md` / `PACKAGE_REGISTER.csv` (no compressor-link) | Datasheet Attributes (Subject package); Guidance Examples | PROPOSAL: keep the linkage as ASSUMPTION and do not condition acceptance on it until the EPC confirms motor allocation. | TBD |
