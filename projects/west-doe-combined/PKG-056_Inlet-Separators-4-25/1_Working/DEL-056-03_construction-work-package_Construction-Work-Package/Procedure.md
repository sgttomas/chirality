# Procedure — DEL-056-03 Construction Work Package (PKG-056)

## Purpose

Procedural steps to assemble, install, mechanically complete, tie in, and turn over the PKG-056 Inlet Separators 4-25 vendor-supplied package at the West Doe 04-25 facility. This procedure describes how the construction work package artifacts are produced and how the physical installation is executed under EPC Integrator coordination and Tourmaline field construction scope.

## Prerequisites

- Accepted upstream PROJECT_DECOMP snapshot (GATE-07_Final_Published_2026-05-24) and current PACKAGE_REGISTER.csv row PKG-056.
- Vendor general arrangement, lift, and outline drawings for the inlet separator packages (TBD; not present in deliverable folder).
- Approved foundation and grading design and signed-off foundations on site (DBM SEC-01).
- Site permit-to-work standard and project-standard piping code reference (location TBD).
- DBM SEC-01 Construction Responsibility table and DBM SEC-04 Inlet Separation basis available to the field team.
- `_DEPENDENCIES.md` declared dependencies: none declared during PREPARATION (no blocker).
- Hazardous-area classification drawings (TBD).
- Heat medium selection and routing decision (currently unresolved per Conflict C-056-03-4).

## Steps

### S-1 Develop the Construction Work Package documents

1.1 Confirm scope against PACKAGE_REGISTER.csv PKG-056 and DELIVERABLE_REGISTER.csv DEL-056-03.
1.2 Produce the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist (anticipated artifacts per `_CONTEXT.md`).
1.3 Identify each tie-in by interface type from PACKAGE_REGISTER.csv PKG-056 (Process Piping, Utility Piping, Relief/Flare/Vent, Drain/Containment, EHT, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Fire & Gas/Safety Systems, Maintenance Access, Structural/Foundations/Supports) and assign each a tie-in number, governing P&ID, work pack, and responsible crew.
1.4 Establish hold points, ITP entries, and turnover criteria for each work pack.

### S-2 Pre-mobilization readiness

2.1 Confirm foundations, piling, grading, and miscellaneous structural supports are in place and accepted (Tourmaline scope per DBM SEC-01).
2.2 Confirm vendor package delivery schedule and offloading plan; perform lift studies.
2.3 Confirm long-lead shipped-loose items list against vendor packing list.
2.4 Verify scaffolding, access platforms, and maintenance access provisions per the package register interface list.

### S-3 Receive and set the package

3.1 Off-load modules and equipment from transport (Tourmaline scope, DBM SEC-01).
3.2 Inspect receipt condition, including external damage, weather seals, and internal coating where accessible (Devchem 253 per DBM SEC-04).
3.3 Set modules, pipe racks, and equipment on foundations per vendor drawings and alignment tolerances (alignment criteria TBD).
3.4 Grout and align as required.

### S-4 Mechanical hookup

4.1 Install interconnecting piping from rack to inlet separator packages, preserving symmetrical distribution to each separator (DBM SEC-04).
4.2 Install or align the at-minimum two parallel balanced-globe inlet PCVs per separator, including skid-edge inlet isolation supporting PCV maintenance without full separator blowdown (DBM SEC-04).
4.3 Install methanol injection points upstream of each inlet separator inlet PCV (DBM SEC-04).
4.4 Install or hook up the per-separator liquid outlet heater to the selected heat medium (Conflict C-056-03-4; selection TBD).
4.5 Install shipped-loose instruments, valves, and components (Tourmaline scope per DBM SEC-01).
4.6 Install miscellaneous structural supports (Tourmaline scope per DBM SEC-01).

### S-5 Tie-ins to facility systems

For each tie-in identified in S-1.3:

5.1 Confirm system state (live, depressurized, isolated) and obtain the appropriate permit-to-work (site standard TBD).
5.2 Execute weld or bolt-up per the governing piping code/class (TBD; ASSUMPTION ASME B31.3 pending confirmation).
5.3 NDE per code class; record results in the tie-in pack.
5.4 Update interface and turnover checklist entry.

### S-6 Electrical, I&C, and safety systems

6.1 Install home-run cables and terminate (Tourmaline scope per DBM SEC-01).
6.2 Connect F&G and safety system devices at the package boundary; perform functional loop tests with the plant safety system.
6.3 Install and verify grounding/bonding for vessels, piping, and skids (site standard TBD).
6.4 Confirm area/exterior lighting hookup (Tourmaline scope).

### S-7 Pressure testing, cleanliness, and dry-out

7.1 Build pressure-test packages by system; identify code class (TBD; pending governing piping code).
7.2 Execute hydrostatic or pneumatic test per package; reconcile any concerns with the Devchem 253 vessel internal coating.
7.3 Flush, clean, and dry out as defined in the work pack prior to hydrocarbon introduction.

### S-8 Mechanical completion and punch-listing

8.1 Walk down each system with operations.
8.2 Capture Category A and B punch items and disposition.
8.3 Complete check sheets per ITP.

### S-9 Turnover

9.1 Compile the turnover package: test certificates, NDE records, calibration records, red-line as-builts, punch-list status, and operator-required documentation.
9.2 Operations sign-off of the construction interface and turnover checklist.
9.3 Hand off custody of the system to commissioning/operations.

## Verification

| Step | Verification approach |
|---|---|
| S-1 | Documents reviewed against `_CONTEXT.md` Anticipated Artifacts list; tie-in register cross-checks PACKAGE_REGISTER.csv PKG-056 interface set. |
| S-2 | Pre-mobilization checklist signed; foundation acceptance sheets on file. |
| S-3 | Receipt inspection report; alignment survey (criteria TBD); coating inspection check sheet. |
| S-4 | Hookup check sheets; PCV stroke test; heater hookup and (where possible) leak/loop test. |
| S-5 | Tie-in NDE records; interface and turnover checklist line items closed. |
| S-6 | Cable continuity/megger records; F&G loop test; ground-continuity records. |
| S-7 | Pressure test certificates; flushing/dry-out sign-offs. |
| S-8 | Walkdown punch lists; ITP check sheets signed. |
| S-9 | Operator-signed turnover certificate. |

## Records

- Construction work package (this kit), installation and tie-in workface plan, construction interface and turnover checklist.
- Receipt inspection records.
- Foundation acceptance and alignment surveys.
- Mechanical hookup check sheets and ITP records.
- Tie-in weld and NDE records.
- Cable continuity, megger, F&G, and grounding test records.
- Pressure-test certificates; flushing and dry-out records.
- Red-line as-built drawings.
- Punch-list and turnover acceptance records.
