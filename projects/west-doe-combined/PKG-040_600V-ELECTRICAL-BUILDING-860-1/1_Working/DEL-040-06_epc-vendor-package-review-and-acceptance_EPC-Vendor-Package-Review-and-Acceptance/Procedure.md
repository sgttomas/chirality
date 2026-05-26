# Procedure: DEL-040-06_epc-vendor-package-review-and-acceptance

This procedure describes how the EPC Integrator **produces and operates** the vendor package review-and-acceptance evidence set for `PKG-040` (building 860-1, 600 V General Area / Tank Farm Electrical Building). The artifact outputs are listed in `_CONTEXT.md` and `ARTIFACT_REGISTER.csv` rows for `DEL-040-06`.

## Purpose

Execute and record EPC review of the Package Vendor's engineered electrical building package, decide acceptance against the EPC Scope of Work / Package Datasheet / Construction Work Package, and preserve the evidence required for handoff and downstream construction / commissioning.

## Prerequisites

Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at PREPARATION.

Working prerequisites (read-only inputs to this procedure):

- `DEL-040-01_scope-of-work` — accepted EPC Scope of Work for `PKG-040`.
- `DEL-040-02_package-datasheet` — accepted EPC Package Datasheet (technical handoff basis and interface requirements).
- `DEL-040-03_construction-work-package` — accepted construction interface and turnover plan.
- `DEL-040-04_vendor-engineered-equipment-package` — vendor's engineered package and supporting submittals.
- `DEL-040-05_vendor-document-turnover-package` — vendor document register and submittals.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility electrical design basis (read-only authority).
- `INTERFACE_REGISTER.csv` rows for `PKG-040` — twelve applicable interface types.
- `PACKAGE_REGISTER.csv` row `PKG-040` — responsibility model.

## Steps

1. **Establish the review baseline.** Open `DEL-040-02` Package Datasheet and confirm the latest accepted revision. Snapshot the twelve `PKG-040` interface entries from `INTERFACE_REGISTER.csv` into the working checklist template. Confirm the facility electrical design basis source slices (DBM lines 298, 2210, 2816, 2911, 2919-2925, 2937, 2943, 2959, 2969, 2971-2979, 2985) are the authority set used in review.

2. **Open the vendor document review and comment log** (`ART-127E61EEAE`). For each vendor submittal in the `DEL-040-05` register, create a log entry with: submittal ID, vendor document title, Package Datasheet requirement(s) being verified, reviewer, review date, disposition (accept / comment / reject), open-item ID(s) if any, and closure date when resolved.

3. **Review electrical-power interface evidence (REQ-040-06-04).** Confirm 600 V, 3-phase, 3-wire, 60 Hz HRG service architecture; bottom-entry incoming and outgoing power cables; 600 V MCC as the main building distribution. Cross-check vendor single-line, panel schedules, and cable schedule against DBM lines 2937, 2959, 2977.

4. **Review grounding/bonding evidence (REQ-040-06-05).** Confirm 5 A continuous HRG for the 600 V transformer feeding the building, 600 V MCC ground/resistor fault detection, alarm-only ground-fault protection on 600 V, and connection of major equipment to the ground grid at two points (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2985).

5. **Review building construction evidence (REQ-040-06-07).** Confirm prefabricated modular construction, pile elevation with cable-tray space beneath the building, bottom-entry cable design, TECK/ACIC cabling, EMT for adjacent runs, outdoor GFI receptacle, and equipment doors / transom sections sized for largest equipment removal (DBM lines 2977-2979).

6. **Review HVAC evidence (REQ-040-06-06).** Confirm n+1 HVAC sizing (DBM line 2975). Reject single-unit HVAC arrangements unless an approved Package Datasheet change exists.

7. **Review area classification and spacing (REQ-040-06-08).** Confirm building sited in a general purpose (unclassified) area and minimum 25 m from fired heaters (DBM lines 298, 2911).

8. **Review equipment-housed list (REQ-040-06-09).** Confirm the vendor's housed-equipment list aligns with the 600 V building scope set in DBM lines 2969 and 2973. Flag any medium-voltage equipment as a finding for ruling (likely outside building 860-1 scope per the DBM building list, line 2816).

9. **Review standby-power interface evidence (REQ-040-06-10).** Determine whether 860-1 MCC participates in the TOU standby-generator transfer-switch arrangement (DBM line 2943). If unstated on the Package Datasheet, open as a `TBD` item rather than asserting either way.

10. **Review F&G interface evidence (REQ-040-06-11).** Confirm vendor F&G device schedule and shutdown matrix align with the Package Datasheet requirement for `IFC-AB1228ED22`. Device list specifics remain `TBD` if Package Datasheet has not finalized them.

11. **Review structural/foundation evidence (REQ-040-06-12).** Confirm pile-supported elevated structure, load data, and anchor patterns align with the EPC structural/foundation interface (`IFC-327D21980E`) and DBM line 2977.

12. **Receive and review test/inspection evidence (REQ-040-06-03).** Receive FAT reports, routine test records, and shop inspection evidence from the Package Vendor and file them in the evidence packet (`ART-993D18AF3B`). Confirm coverage against vendor ITP and Package Datasheet.

13. **Populate the vendor package acceptance and turnover checklist** (`ART-F627B8462B`, REQ-040-06-02). For each of the twelve `PKG-040` interface types and for the vendor document register, mark `pass`, `conditional`, or `fail`. For `conditional`, list the open-item ID(s), owner, and closure date.

14. **Closure gate (REQ-040-06-13).** Acceptance shall be issued only when: (a) every entry in the vendor document review log has a final disposition, and (b) no `fail` markings remain on the checklist. Conditional items shall list owners and closure dates. Sign the acceptance.

15. **Compose the turnover evidence packet.** Combine the acceptance checklist, the vendor document review log, the test/inspection evidence, and the turnover records received from `DEL-040-05`. Place the final packet in the deliverable folder.

16. **Update `_STATUS.md` and `MEMORY.md` per the deliverable-local write policy and current run authority.**

## Verification

- Each numbered Specification requirement has at least one log/checklist entry (REQ-040-06-01 through REQ-040-06-13).
- The acceptance checklist enumerates all twelve `PKG-040` interface types (`INTERFACE_REGISTER.csv`).
- No `fail` markings remain at acceptance; all `conditional` items have owners and dates.
- All vendor document register items have a final disposition in the log.
- Source slices cited in this Procedure resolve to the listed lines in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

## Records

The following records are preserved in the deliverable folder as the acceptance evidence set:

- Vendor document review and comment log (`ART-127E61EEAE`).
- Vendor package acceptance and turnover checklist (`ART-F627B8462B`).
- Factory/shop test and inspection evidence packet (`ART-993D18AF3B`).
- Turnover evidence packet (composed from `DEL-040-05` outputs and the acceptance checklist).
- Signed EPC acceptance decision (acceptance / conditional acceptance) with open-item list.

Source: `_CONTEXT.md` anticipated artifacts; `ARTIFACT_REGISTER.csv` rows for `DEL-040-06`.
