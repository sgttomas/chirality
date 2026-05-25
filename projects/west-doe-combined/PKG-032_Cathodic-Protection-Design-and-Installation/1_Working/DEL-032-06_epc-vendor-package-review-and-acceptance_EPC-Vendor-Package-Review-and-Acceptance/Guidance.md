# Guidance: DEL-032-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable exists to evidence EPC Integrator review and acceptance of the vendor-delivered Cathodic Protection package (`PKG-032`) so that vendor-engineered CP equipment and vendor documentation can be integrated into the facility without absorbing CP engineering or supply into facility design scope. It uses the EPC Scope of Work (`DEL-032-01`), Package Datasheet (`DEL-032-02`), and Construction Work Package (`DEL-032-03`) as the acceptance basis.

## Principles

- Preserve the DBM facility-design exclusion of cathodic-protection engineering and supply. EPC acceptance is integration review and turnover evidence, not CP re-engineering.
- Treat the Gate 7 registers (`PACKAGE_REGISTER`, `DELIVERABLE_REGISTER`, `ARTIFACT_REGISTER`, `INTERFACE_REGISTER`) as authoritative for identity, artifact list, and applicable interfaces.
- Keep vendor-owned design accountability with the Package Vendor; carry EPC Integrator responsibility only for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance evidence.
- Use `TBD` for vendor detail values, vendor document register entries, and test/inspection lists that are not supported by accessible source slices; do not invent acceptance criteria.
- Coordinate vendor grounding/bonding submittals with the facility grounding basis to avoid stray-current paths that would defeat cathodic protection of buried/immersed steel.

## Considerations

The DBM (Deepcut) explicitly excludes cathodic-protection engineering and supply from the facility design scope and assigns owner interface coordination. The DBM (Comp and Liquids) includes cathodic protection within the electrical design scope only at the interface-power level — i.e., the facility electrical design supports CP interface power where defined. Acceptance language should reflect both: vendor delivers CP engineering/supply; EPC delivers facility-side interfaces (power, grounding/bonding, I&C cabling, communications) and integration acceptance.

Applicable PKG-032 interfaces are Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network (`INTERFACE_REGISTER.csv`). Each interface should appear in the per-interface acceptance status and the vendor document review log.

The local source set does not include a vendor document register for this package (`ART-A82FC3C3ED` is explicitly a "TBD vendor document register" artifact). Acceptance content that depends on vendor-defined documentation should remain `TBD` until vendor submittals or an owner CP specification are accepted. The package-specific `26020-Package_Requirements.docx` search did not produce a PKG-032 match accessible to this run.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| CP design parameters in acceptance | Do not record CP design values (current density, anode sizing, rectifier rating); accept vendor submittals against owner specification. | DBM excludes CP engineering from facility design; no accessible source defines these values for PKG-032. |
| Grounding coordination | Require vendor and EPC grounding plans to be reviewed together to avoid stray-current paths defeating CP. | DBM mandates facility grounding/bonding basis; CP performance is sensitive to electrical grounding architecture. |
| Vendor document register | Mark register entries TBD until vendor turnover or owner CP spec defines them. | Source artifact register flags the vendor document register as TBD evidence. |
| Test/inspection list | Carry test items as TBD with owner/vendor until vendor test plan is submitted. | No source-supported test list is accessible for PKG-032. |
| Standards | List CEC, project electrical specs, and the owner CP standard as governing bases with locations TBD. | DBM cites electrical bases; owner CP standard is presumed but not accessible locally. |

## Examples

- Acceptable acceptance entry: "Per-interface acceptance: Electrical Power — accepted with reservation pending feeder coordination with EPC electrical lead. Source: `INTERFACE_REGISTER.csv` `IFC-C2719906C1`."
- Acceptable source-gap entry: "Vendor document register: TBD. No source-supported register available; carry as TBD against vendor turnover under `DEL-032-05`."
- Not acceptable without new source: "Rectifier rated 50 A DC at 30 V with magnesium anode bed at grid coordinate X." The accessible source set does not establish CP design values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-032-06-001 | DBM (Deepcut) excludes cathodic-protection engineering and supply from facility design, while DBM (Comp and Liquids) lists cathodic protection within the electrical design scope. The acceptance scope must reconcile these as "facility electrical supports CP interface power; CP engineering and supply are vendor/owner." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraph | Datasheet Attributes/Conditions; Specification Scope/Requirements; Guidance Principles | Treat facility scope as interface-power support only; CP engineering and supply remain vendor/owner. | TBD |
| HRR-032-06-002 | No vendor document register, vendor test plan, or owner CP specification is locally accessible for PKG-032; the acceptance log, checklist, and test/inspection evidence depend on these. | `ARTIFACT_REGISTER.csv` row `ART-A82FC3C3ED` ("TBD vendor document register") | `_REFERENCES.md`; `26020-Package_Requirements.docx` (no PKG-032 match) | Specification Requirements REQ-032-06-003/004/007; Procedure Steps; Datasheet Attributes | Carry vendor register, test plan, and CP spec as TBD with owner; produce acceptance scaffolding without inventing items. | TBD |
