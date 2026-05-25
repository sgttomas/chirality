# Procedure: DEL-024-04_vendor-engineered-equipment-package

## Purpose

Produce, deliver, and integrate the Vendor Engineered Equipment Package for `PKG-024` (MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD), consisting of vendor package engineering, design, fabrication / supply, the physical equipment package, and the vendor package design basis and datasheet set. Procedure addresses **production** of the deliverable; operation / commissioning of the installed VFD is governed by the construction work package (`DEL-024-03`) and vendor turnover (`DEL-024-05`).

## Prerequisites

- `DEL-024-01_scope-of-work` — EPC Scope of Work for `PKG-024` accepted and available to the Package Vendor.
- `DEL-024-02_package-datasheet` — EPC Package Datasheet for `PKG-024` accepted; provides the technical handoff envelope (TBD until issued).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable read.
- Accessible source materials:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Motor Control and Motor Specifications; electrical buildings; grounding; cable table).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
  - `_Sources/26020-Package_Requirements.docx` (search for PKG-024 package-specific slice; record result).
- Declared upstream / downstream dependencies: none declared at `_DEPENDENCIES.md` (`DECLARED` coordination mode).
- Driven motor identification (tag, service, load type) — currently TBD; resolution required before drive sizing finalization (see HRR-024-04-001).

## Steps

1. **Receive EPC handoff.** Confirm `DEL-024-01` and `DEL-024-02` are at acceptable maturity for vendor engineering kickoff; record the snapshot used.
2. **Confirm interface facts.** Cross-check the six declared `PKG-024` interface rows in `INTERFACE_REGISTER.csv` against the EPC Package Datasheet interface requirements matrix; flag any divergence.
3. **Resolve driven-load identification.** Obtain driven motor tag, service, load profile, and starting / running duty from the EPC Package Datasheet; if absent, raise HRR-024-04-001 and pause sizing-dependent activities.
4. **Confirm housing decision.** Obtain the installation location decision (prefabricated electrical building vs. skid / outdoor) from the EPC Package Datasheet; if absent, raise HRR-024-04-003 and pause mechanical / cooling design.
5. **Develop vendor design basis.** Author the vendor package design basis aligned to the EPC handoff envelope; capture drive topology, input / output configuration, harmonic mitigation strategy, output filter decision, bypass arrangement, cooling, enclosure / housing, and protection scheme. Mark vendor-originated proposals explicitly.
6. **Develop vendor datasheet set.** Produce datasheets for the drive itself and for any vendor-supplied auxiliaries (e.g., input transformer, control cabinet); each datasheet shall cite the corresponding EPC Package Datasheet basis row.
7. **Confirm communications interface.** Define the Ethernet interface to the plant PLC central control panel (consistent with the facility 4.16 kV MCC convention) and confirm protocol, addressing, and signal list with the EPC Integrator; reflect in vendor schematic and I/O list.
8. **Confirm grounding and cabling.** Apply the two-point ground connection rule and confirm cable types against the facility cable table; clarify MV output cabling rules with EPC Integrator (HRR-024-04-004).
9. **Engineering review and approval.** Submit vendor design basis and datasheet set for EPC integration review; resolve comments and re-issue.
10. **Fabricate / supply the physical equipment package.** Execute vendor fabrication / procurement against the approved design basis and datasheets.
11. **Factory acceptance test (FAT).** Execute FAT covering rating verification, protection functions, communications interface, and control sequences; record results.
12. **Package release for shipment.** Issue release documentation for shipment to site; downstream construction, installation, and acceptance proceed under `DEL-024-03` and `DEL-024-06`. Vendor document turnover proceeds under `DEL-024-05`.

## Verification

- All six `PKG-024` interface facts addressed in vendor design basis (REQ-1 through REQ-11 referenced as applicable).
- Vendor datasheet rating fields match Workbook Packages row 26 (2,000 HP, 4,160 V, 3-phase, 60 Hz, 4,160 V output).
- Each vendor-asserted requirement either traces to a source citation or is flagged as a vendor-originated proposal subject to EPC Integrator integration review.
- HRR-024-04-001 through HRR-024-04-005 either resolved (with ruling) or carried into the EPC Vendor Package Review and Acceptance (`DEL-024-06`) action list.
- FAT record demonstrates pass of rating, protection, communication, and control checks.

## Records

- Vendor package design basis document.
- Vendor datasheet set (drive and auxiliaries).
- General arrangement and schematic drawing set (vendor convention).
- FAT record and punch list.
- Vendor document register and submittal log (formal turnover under `DEL-024-05`).
- Integration review log between Package Vendor and EPC Integrator.
- Conflict-table dispositions (HRR-024-04-001 .. HRR-024-04-005) carried into `_run_records/` and `MEMORY.md` (if created downstream).
