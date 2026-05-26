# Specification — EPC Vendor Package Review and Acceptance (DEL-099-06)

> Normative document. Requirements the EPC Integrator review and acceptance evidence shall satisfy for the Truck Product Loading Unit 3-25 vendor package.

## Scope

This specification governs the EPC Integrator review, integration acceptance, and handoff-readiness evidence for the Truck Product Loading vendor package serving Unit 3-25, against:

- the EPC Scope of Work (DEL-099-01),
- the EPC Package Datasheet (DEL-099-02),
- the EPC Construction Work Package (DEL-099-03),
- the Vendor Engineered Equipment Package (DEL-099-04), and
- the Vendor Document Turnover Package (DEL-099-05).

It covers SOW-0241 through SOW-0244 (see DELIVERABLE_REGISTER.csv row 557).

**Excluded:** original vendor design (DEL-099-04 scope); original vendor documentation set (DEL-099-05 scope); third-party NRM LACT equipment (DBM SEC-03 line 22; SEC-06 line 417); construction execution by the construction contractor (DEL-099-03 scope).

## Requirements

| ReqID | Requirement | Source | Verification (see §Verification) |
|---|---|---|---|
| REQ-1 | The acceptance evidence shall confirm that the vendor package provides **three** product truck-loading stations, each with a dedicated condensate loading pump. | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 (lines 414, 654); SEC-08 (line 526) | V-1 |
| REQ-2 | The acceptance evidence shall confirm per-station loading capacity of **103 m3/h at 345 kPad** differential pressure (or document the deviation). | DBM SEC-06 (line 415) | V-1, V-2 |
| REQ-3 | The acceptance evidence shall confirm that the facility/third-party custody boundary is preserved: LACT scope by third-party NRM; facility scope terminates at the tie-in flange. | DBM SEC-03 (line 22); SEC-06 (line 417) | V-3 |
| REQ-4 | The acceptance evidence shall confirm winterization and -40 deg C ambient design provisions for exposed equipment, package buildings, panels, and field devices in the truck loading area. | DBM SEC-04 (line 145) | V-4 |
| REQ-5 | The acceptance evidence shall confirm fire and gas detection coverage (LEL, H2S, methyl mercaptan, fire) appropriate to the truck loading area. | DBM SEC-16 (line 838) | V-4 |
| REQ-6 | The acceptance evidence shall confirm shutdown and control integration of the truck loading package with BPCS, RIO, and ESD per the controls basis. | DBM SEC-17 (line 862) | V-4 |
| REQ-7 | The acceptance evidence shall confirm that civil provisions (truck-loading slab, spill control, access/turning/queuing) are satisfied at the package interface. | DBM SEC-13 (lines 688, 696) | V-4 |
| REQ-8 | A vendor document review log shall exist that records the disposition of each document required by the Vendor Document Turnover Package (DEL-099-05) against the EPC SOW and Package Datasheet. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row 556 | V-5 |
| REQ-9 | A package acceptance checklist shall exist covering: scope conformance to DEL-099-01; technical conformance to DEL-099-02; constructability/turnover conformance to DEL-099-03; integration interface conformance. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv rows 552-554 | V-5 |
| REQ-10 | Test and inspection evidence (FAT, SAT, hydrotest, NDE, electrical loop checks, fire/gas, ESD as applicable) shall be collected, indexed, and traceable to the responsible test plan. | `_CONTEXT.md` Anticipated Artifacts; DBM SEC-09 Mechanical Package Structure (lines 617-619) | V-5, V-6 |
| REQ-11 | Turnover evidence shall record Mechanical Completion, Pre-Commissioning, and Commissioning/Operational Acceptance status. | `_CONTEXT.md` Anticipated Artifacts | V-6 |
| REQ-12 | All acceptance and approval signatures shall be performed by humans; the EPC Integrator and the Owner are the authoritative approvers. Agents may draft, summarize, or check, but shall not certify. | Chirality K-AUTH-1 | V-7 |
| REQ-13 | Items unresolved at the time of acceptance shall be carried as explicit punchlist items with owner and target-resolution date. | ASSUMPTION (industry-standard EPC acceptance practice; not literally quoted in available sources) | V-5 |
| REQ-14 | Permit-status items affecting the truck rack scope (BCER 100120203 amendment) shall be recorded with current status in the acceptance evidence. | DBM SEC-18 (line 872) | V-5 |

## Standards

Standards explicitly cited by source materials available locally:

- **Site/process basis:** DBM `3-25_Comp_and_Liquids_DBM.md` (governing project DBM for Unit 3-25); SEC-04 site basis; SEC-06 liquids hub basis; SEC-09 mechanical package structure.
- **BCER application 100120203** — provincial permitting basis for the liquids hub; truck rack amendment status referenced in DBM SEC-18.

Standards likely applicable but not locally accessible (location TBD):

- 26020-Package_Requirements.docx package heading 51 — package-level EPC requirements (ASSUMPTION: likely applicable; not text-accessible).
- Workbook Packages row 98 — package-level scope/interface attributes (ASSUMPTION: likely applicable; not text-accessible).
- Project standards for piping, electrical, instrumentation, civil, fire/gas, ESD, and HSE — TBD (not enumerated in available sources for this deliverable).

## Verification

| VerID | Method | Applies to | Evidence |
|---|---|---|---|
| V-1 | Document review of vendor datasheets and P&IDs vs DBM SEC-06 quantities | REQ-1, REQ-2 | Vendor document review log entries |
| V-2 | Witness or review of pump/hydraulic test data | REQ-2 | FAT records; pump curves |
| V-3 | Interface drawing and tie-in flange verification | REQ-3 | Interface drawings; tie-in list |
| V-4 | Specification compliance review against DBM SEC-04, SEC-13, SEC-16, SEC-17 | REQ-4, REQ-5, REQ-6, REQ-7 | Compliance matrix entries; design review minutes |
| V-5 | Checklist review and sign-off | REQ-8, REQ-9, REQ-10, REQ-13, REQ-14 | Completed package acceptance checklist; punchlist |
| V-6 | Turnover record review | REQ-10, REQ-11 | MC/Pre-Comm/Comm certificates; vendor turnover records |
| V-7 | Audit of signatory roles on acceptance records | REQ-12 | Signature blocks; role designations |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`) constituting the delivered evidence package:

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence (FAT/SAT/hydrotest/NDE/electrical/fire-and-gas/ESD as applicable)
- Turnover evidence (MC, Pre-Comm, Comm/Operational Acceptance)
- Punchlist (open items with owner and date)
- Acceptance memorandum signed by EPC Integrator (and Owner where applicable)
