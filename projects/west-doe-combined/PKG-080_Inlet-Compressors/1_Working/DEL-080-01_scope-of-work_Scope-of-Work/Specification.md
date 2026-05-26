# Specification — DEL-080-01 Scope of Work (PKG-080 Inlet Compressors)

> Normative specification of the EPC Integrator Scope of Work deliverable for
> the Inlet Compressors package. Requirements are derived from accessible
> sources; inferences are labeled `ASSUMPTION`; unknown locations are marked
> `TBD`.

## Scope

### In scope (this deliverable)

This Scope of Work defines the EPC Integrator's package-level scope statement
for PKG-080 Inlet Compressors. It documents:

1. The tagged equipment and package identity comprising PKG-080.
2. The package function and its place in the 03-25 facility process flow.
3. The source basis governing the package.
4. The boundaries (battery limits, interface types) between the Package Vendor
   scope and the EPC Integrator scope.
5. The whole-facility integration narrative.

Source: `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` description for
`DEL-080-01_scope-of-work`.

### Out of scope (this deliverable)

- Vendor package internal engineering, design, fabrication, vendor documentation
  (covered by `DEL-080-04` Vendor Engineered Equipment Package and `DEL-080-05`
  Vendor Document Turnover Package).
- Package technical datasheet for vendor handoff (covered by `DEL-080-02`
  Package Datasheet).
- Construction/installation/turnover workface plan (covered by `DEL-080-03`
  Construction Work Package).
- Vendor package review and acceptance (covered by `DEL-080-06` EPC Vendor
  Package Review and Acceptance).

Source: `DELIVERABLE_REGISTER.csv` rows `DEL-080-02` through `DEL-080-06`.

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-080-01-01 | The Scope of Work shall identify the package as PKG-080 Inlet Compressors, workbook package row 66, tracking no. 26020-02-PT-12-001, WBS 02, Mechanical discipline. | `PACKAGE_REGISTER.csv` PKG-080 |
| REQ-080-01-02 | The Scope of Work shall name and tag the production units as two electric-drive separable reciprocating compressor packages KM-2150 and KM-2250. | DBM SEC-05 Electric Driver and Starting Basis |
| REQ-080-01-03 | The Scope of Work shall describe the package function as compressing Doe field sour inlet gas in two stages and delivering compressed sour gas to downstream TEG dehydration and 04-25 sour-gas export. | DBM SEC-04 Sour-Gas Export; SEC-05 Inlet Compression Overview |
| REQ-080-01-04 | The Scope of Work shall state the capacity basis: 2 x 50% configuration with no installed spare; 40 MMSCFD per unit; 80 MMSCFD total facility. | DBM SEC-05; SCOPE_LEDGER SOW-0122 |
| REQ-080-01-05 | The Scope of Work shall declare the discharge pressure basis as fixed at 800 psig under SCA-002 supersession; prior 650–800 psig language shall not be carried as current basis. | DBM SEC-05 Compression Design Conditions |
| REQ-080-01-06 | The Scope of Work shall require NACE-compliant materials and seals for sour service. | SCOPE_LEDGER SOW-0122 |
| REQ-080-01-07 | The Scope of Work shall assign package engineering, package design, vendor documentation, and physical equipment supply to the Package Vendor. | `PACKAGE_REGISTER.csv` PKG-080 |
| REQ-080-01-08 | The Scope of Work shall assign facility-level integration, interface management, tie-ins, constructability, procurement/construction coordination, and facility-level integration to the EPC Integrator. | `PACKAGE_REGISTER.csv` PKG-080 |
| REQ-080-01-09 | The Scope of Work shall enumerate the applicable EPC interface types at the package boundary: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. | `PACKAGE_REGISTER.csv` PKG-080 |
| REQ-080-01-10 | The Scope of Work shall declare the starting basis as starting VFDs for KM-2150 and KM-2250 per SCA-001 VE #34; soft starts are not the current basis. | DBM SEC-05 Electric Driver and Starting Basis |
| REQ-080-01-11 | The Scope of Work shall require the package to be modularized for shop assembly, disassembled into three transport pieces, and installed inside self-framing buildings. | DBM SEC-05 Inlet Compression Overview; SCOPE_LEDGER SOW-0121 |
| REQ-080-01-12 | The Scope of Work shall identify utility tie-ins: sweet-gas startup purge from the fuel-gas system; packing drains/vents to a common seal pot with vapour routed to VRU suction and a vacuum-pump interface. | DBM SEC-05 Scrubbers, Coolers, Recycle, Purge |
| REQ-080-01-13 | The Scope of Work shall list the downstream process tie-in: compressor discharge to a 1 x 100% TEG dehydration package and onward sour-gas export to the 04-25 inlet gathering system. | DBM SEC-05 TEG Dehydration Basis; SEC-04 Sour-Gas Export |
| REQ-080-01-14 | The Scope of Work shall record the major included equipment per package: suction scrubbers, intercooler and aftercooler, recycle valve, package piping, instrumentation, electrical, HVAC, and package auxiliaries. | DBM SEC-05; SCOPE_LEDGER SOW-0121 |
| REQ-080-01-15 | The Scope of Work shall record the preliminary compressor model as Ariel KBC/6 (TBC) per DBM SEC-05; the conflict with the decomposition row's "Ariel KBZ/6" shall be surfaced for human ruling, not silently reconciled. | DBM SEC-05; SCOPE_LEDGER SOW-0121; Guidance Conflict Table C-01 |
| REQ-080-01-16 | The Scope of Work shall not redefine internal Package Vendor scope (cylinder selection, internal piping geometry, vendor datasheet values); those belong to `DEL-080-02` Package Datasheet (handoff) and `DEL-080-04` Vendor Engineered Equipment Package. | `DELIVERABLE_REGISTER.csv` `DEL-080-02`, `DEL-080-04` |

ASSUMPTION rows (best-effort; label retained until confirmed):
- ASSUMPTION-A: The objective associations (OBJ-002 through OBJ-010) carried in
  `_CONTEXT.md` are derived from PACKAGE_HEURISTIC mapping at the package level
  and are best-effort context, not hard requirements. Source:
  `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC).
- ASSUMPTION-B: The kPag pressure values carried in SCOPE_LEDGER SOW-0122
  (1275 kPag suction, 6550 kPag discharge) are directional summaries; the
  governing pressure values are the psig values in DBM SEC-05. Conflict C-02 in
  Guidance.

## Standards

| Standard / Code | Applicability | Source / Location |
|---|---|---|
| NACE (sour service materials and seals) | Materials for all wetted parts in sour service | SCOPE_LEDGER SOW-0122 (NACE-compliant materials and seals required); specific NACE document reference **location TBD** in accessible sources |
| NEMA MG1 | Electric motor design compliance for compressor drivers | DBM SEC-05 Electric Driver and Starting Basis |
| CSA Z662 | Pipeline design and overpressure protection for sour-gas export (downstream of package, but referenced for tie-in design) | DBM SEC-04 Sour-Gas Export |
| SCA-001 VE #34 | Governs starting basis (starting VFDs for KM-2150 / KM-2250) | DBM SEC-05 |
| SCA-002 | Governs discharge pressure fixation at 800 psig | DBM SEC-05 |
| SCA-006 | Governs facility-wide supersession of local 03-25 stabilizer / SOC / instrument-air content | DBM SEC-03/SEC-05 Superseded Content Controls |
| 26020-Package_Requirements.docx package heading 33 | Project-internal package requirements document | Referenced by `_REFERENCES.md`; **location TBD** (binary docx; section text not locally accessible as markdown slice) |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-080-01-01 / -02 / -03 | Document review: confirm the SoW narrative names the package, tags KM-2150/2250, and describes the compress-and-export function. |
| REQ-080-01-04 / -05 | Document review against DBM SEC-05 capacity and discharge-pressure tables; check no 650 psig discharge language is carried. |
| REQ-080-01-06 | Document review for explicit NACE compliance statement; verify NACE document reference resolved before Gate 5 (currently TBD). |
| REQ-080-01-07 / -08 / -09 | Responsibility matrix review against PKG-080 PACKAGE_REGISTER row (responsibility narrative + applicable interface types list). |
| REQ-080-01-10 | Cross-check against SCA-001 VE #34 reference; verify SoW does not specify soft starts as the basis. |
| REQ-080-01-11 | Document review against DBM SEC-05 modularization statement. |
| REQ-080-01-12 / -13 / -14 | Cross-check tie-in narrative against DBM SEC-05 utility/tie-in subsections and SEC-04 sour-gas export. |
| REQ-080-01-15 | Confirm Conflict Table C-01 is present in Guidance and is open for human ruling; do not silently pick a model name. |
| REQ-080-01-16 | Boundary check: confirm SoW does not encroach on `DEL-080-02` datasheet, `DEL-080-03` CWP, `DEL-080-04` Vendor EEP, `DEL-080-05` Vendor Doc Turnover, or `DEL-080-06` EPC Review/Acceptance scopes. |

Gate-level verification target: Mandatory Gate 5 EPC anchor deliverable
(`_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row notes).

## Documentation

Documentation required from this deliverable (artifact set):

1. **Package scope of work narrative** — this Specification.md plus
   Datasheet.md, Guidance.md, Procedure.md inside the deliverable folder.
2. **Tagged equipment and package identity list** — Datasheet.md
   "Identification" and "Attributes" sections.
3. **Package function and integration narrative** — Specification.md "Scope"
   section and Guidance.md "Purpose" / "Principles" sections.
4. **Responsibility assignment record** — Datasheet.md "Construction" table and
   Specification.md REQ-080-01-07 through REQ-080-01-09.

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv`
artifact list for `DEL-080-01_scope-of-work`.
