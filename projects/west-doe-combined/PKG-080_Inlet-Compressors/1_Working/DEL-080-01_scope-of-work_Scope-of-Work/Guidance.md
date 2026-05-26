# Guidance — DEL-080-01 Scope of Work (PKG-080 Inlet Compressors)

> Directional guidance for authoring, reviewing, and maintaining the EPC
> Integrator Scope of Work for the Inlet Compressors package. This document
> explains rationale, principles, considerations, and trade-offs; it does not
> establish requirements (see Specification.md).

## Purpose

The Scope of Work is the **anchor EPC Integrator deliverable** for PKG-080. It
declares what the EPC Integrator is responsible for delivering at the package
boundary, what the Package Vendor owns inside the skid/building, and what the
facility-level integration looks like. Without a clear Scope of Work, the
downstream EPC deliverables in PKG-080 (`DEL-080-02` Package Datasheet,
`DEL-080-03` Construction Work Package, `DEL-080-06` EPC Vendor Package Review
and Acceptance) have no governed scope statement to anchor against, and the
Package Vendor's production unit (`DEL-080-04`) cannot be reviewed against a
stable EPC-defined intent.

Source: `_CONTEXT.md` Notes (Mandatory Gate 5 EPC anchor deliverable);
`DELIVERABLE_REGISTER.csv` row `DEL-080-01_scope-of-work`.

## Principles

1. **Source-anchored, not narrative-anchored.** Pressure values, capacity
   numbers, motor ratings, and tie-in lists come from DBM SEC-04/SEC-05, not
   from generic compressor-package convention or prior project memory. When the
   DBM and `26020-Package_Requirements.docx` package heading 33 are both
   needed, prefer DBM as the locally accessible governed source and mark
   `location TBD` for the docx slice until it is converted to a readable form.
2. **Responsibility split is the heart of the SoW.** The decomposition
   `PACKAGE_REGISTER.csv` row for PKG-080 carries the canonical responsibility
   narrative ("Package Vendor owns package engineering, package design, vendor
   documentation, and the physical equipment package. EPC Integrator owns
   integration into the functional process facility..."). The SoW must mirror
   this split exactly. Do not blur the boundary in either direction.
3. **Interface enumeration is normative.** The thirteen interface types listed
   in `PACKAGE_REGISTER.csv` are the agreed scope of EPC interface
   responsibility at the package boundary. The SoW enumerates them, even when
   downstream deliverables will manage them in detail.
4. **Mandatory Gate 5 anchor.** The SoW must be complete enough to support
   Gate 5 sign-off; gaps belong in the `TBD` register or the Conflict Table,
   not in soft language.
5. **No silent reconciliation.** Where source and decomposition disagree (see
   Conflict Table below), preserve the disagreement and route it to human
   ruling. Do not pick a "best" answer in the SoW.

## Considerations

- **Workbook row 66 is authoritative for package identity.** `SCOPE_LEDGER.csv`
  notes "Workbook package row is authoritative. Duplicate tracking numbers are
  not merged." The Datasheet identity block reflects this.
- **SCA supersessions are non-trivial.** SCA-001 (VFD starting), SCA-002
  (800 psig fixed discharge), and SCA-006 (instrument-air supply from 04-25;
  no local 03-25 stabilizer/SOC) all change the active basis. The SoW must
  reflect the post-supersession state, not legacy DBM language. The DBM SEC-05
  "Superseded Content Controls" subsection enumerates what is no longer current.
- **Modularization and constructability.** Three-piece modularization for
  transport (DBM SEC-05) constrains lift planning, road permits, and structural
  foundations. EPC owns those facility-level concerns; vendor owns module
  assembly geometry.
- **Starting basis is electrically dominant.** 5,200 hp / 3,878 kW driver with
  starting VFD is a major electrical-system load and a significant interface
  with the facility power distribution. The SoW must list Electrical Power as
  an EPC-owned interface (already in the thirteen-interface enumeration).
- **TEG dehydration is the immediate downstream consumer.** Although TEG is a
  separate downstream system, the compressor discharge tie-in to TEG inlet is
  a package-boundary interface that the EPC integrator coordinates.
- **VRU and seal-pot routing.** Packing drains and vents to a common seal pot
  with vapour to VRU suction is a cross-package interface. The SoW must record
  it even though the VRU is a separate package.

## Trade-offs

| Trade-off | Direction taken | Rationale |
|---|---|---|
| Carry detailed compressor design values in SoW vs. defer to Package Datasheet | Defer; SoW carries identifying basis only | `DEL-080-02` Package Datasheet is the technical handoff deliverable; duplicating values here invites drift |
| Use kPag (decomposition summary) or psig (DBM source) | Carry psig as governing; note kPag in Conflict C-02 | DBM SEC-05 is the locally accessible governed source slice; SCOPE_LEDGER kPag values are directional summaries |
| Reconcile Ariel KBC/6 vs KBZ/6 model designation | Do not reconcile; surface as Conflict C-01 | Both designations are TBC; silent reconciliation would create an unsourced "fact" |
| Enumerate vs reference interface types | Enumerate inline | Interface scope is a primary SoW output; readers should not need to consult `PACKAGE_REGISTER.csv` separately |
| Include vs exclude TEG dehydration in scope narrative | Include as **downstream tie-in**, not as in-package scope | TEG is a separate package; treating it as in-scope would blur the package boundary |

## Examples

Example narrative paragraph (illustrative, for downstream SoW publication
drafting; sourced fragments only):

> "PKG-080 Inlet Compressors comprises two electric-drive separable
> reciprocating compressor packages (KM-2150 and KM-2250) sized at 40 MMSCFD
> per unit (2 x 50%, no spare; 80 MMSCFD total). Each two-stage package is
> driven by a 5,200 hp / 3,878 kW, 4,000 V, 60 Hz electric motor with starting
> VFD per SCA-001 VE #34. Discharge pressure is fixed at 800 psig per SCA-002.
> Compressed sour gas discharges through aftercooling and is routed to the
> 1 x 100% TEG dehydration package, then to the 04-25 sour-gas export tie-in."

Source: DBM SEC-05 (Inlet Compression Overview; Electric Driver and Starting
Basis; Compression Design Conditions; TEG Dehydration Basis).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Compressor preliminary model name: "Ariel KBZ/6" vs "Ariel KBC/6" (both labeled TBC) | `SCOPE_LEDGER.csv` SOW-0121 (decomposition row) — "Ariel KBZ/6 separable reciprocating compressor packages" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 Inlet Compression Overview table — "Ariel KBC/6, TBC" | Datasheet.md Attributes (Preliminary model); Specification.md REQ-080-01-15 | DBM SEC-05 (locally accessible governed source slice) — record as Ariel KBC/6, TBC | TBD |
| C-02 | Process pressure units: SOW-0122 expresses 1275 kPag suction / 6550 kPag discharge; DBM SEC-05 expresses 165 psig 1st-stage suction / 800 psig 2nd-stage discharge | `SCOPE_LEDGER.csv` SOW-0122 | DBM SEC-05 Compression Design Conditions table | Datasheet.md Conditions; Specification.md REQ-080-01-04 / -05 | DBM SEC-05 psig values are governing; SOW-0122 kPag values are directional summaries (note: rough conversion: 165 psig ≈ 1138 kPag; 800 psig ≈ 5516 kPag — the SOW-0122 1275 / 6550 kPag values do not exactly match either suction/MAWP or normal/discharge pairs, so they may reflect a different basis or earlier supersession state) | TBD |
| C-03 | `26020-Package_Requirements.docx` package heading 33 is cited as a primary source by `_REFERENCES.md` and `PACKAGE_REGISTER.csv`, but is not locally accessible as a text slice | `_REFERENCES.md` Source Materials | `_Sources/` directory listing (only `.docx`/`.xlsx`/DBM `.md` present; no extracted text from package_requirements docx) | All four documents (Standards, Requirements, Conditions) | Convert the docx package heading 33 to markdown and re-run Pass 3 (lensing) once available | TBD |
| C-04 | `Bid Docs/Budgetary/brief.md` and `24292-02-PT-ENR-12-201_Compressors_R2.pdf` are cited as the Word Source Basis / budgetary go-by in `PACKAGE_REGISTER.csv`, but neither is present under `_Sources/` | `PACKAGE_REGISTER.csv` PKG-080 source basis | `_Sources/` directory listing | Datasheet.md References; Specification.md Standards | Locate and stage these documents under `_Sources/` before Gate 5 | TBD |
