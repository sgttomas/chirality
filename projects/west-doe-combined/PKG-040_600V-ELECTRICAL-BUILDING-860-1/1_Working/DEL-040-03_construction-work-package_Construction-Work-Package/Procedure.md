# Procedure: DEL-040-03_construction-work-package — Construction Work Package

## Purpose

Define a conservative procedure for producing and using the PKG-040 Construction Work Package for the 600V Electrical Building (860-1) from the accepted Gate 7 basis and locally accessible electrical/civil source material.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` have been read.
- Workbook source row is available: `26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 42 (mirrored into PACKAGE_REGISTER.csv PKG-040 and INTERFACE_REGISTER.csv rows for PKG-040).
- DBM electrical and civil source slices are available: `DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility, SEC-02 (Site Data, Plot Plan), SEC-11 (Buildings table; civil/structural basis), SEC-12 (Area Classification, Power System, Electrical Buildings, Grounding/Bonding, Cable/Wire/Raceways, Lighting/Receptacles, Building Heaters, Cathodic Protection).
- Declared upstream dependencies: none declared during PREPARATION.
- Required but unresolved construction inputs: geotechnical assessment report, topographical survey/grade surface file, plot plan CIV-235633-5002, completed electrical studies (HAC, load analysis, short-circuit, relay coordination/arc-flash, load-flow), vendor IFC drawings and equipment list for 860-1, standby generator sizing/transfer-switch ratings, approved inspection/turnover forms.

## Steps

1. Confirm package identity.
   - Verify deliverable ID, package ID (PKG-040), WBS 01, CoA tracking number 26020-01-30-031, Electrical discipline, scope item SOW-0041, and supported objectives against `_CONTEXT.md`, workbook row 42, PACKAGE_REGISTER, and DELIVERABLE_REGISTER.

2. Establish construction scope boundary.
   - Include physical installation, construction, inspection, turnover, and tie-in planning for PKG-040 600V Electrical Building (860-1) as a shop-built modular building.
   - Record exclusions as `TBD` per PACKAGE_REGISTER; document the SEC-12 cathodic-protection exclusion explicitly.

3. Build the interface checklist (all twelve categories).
   - Add the PKG-040 interface categories from workbook row 42 and `INTERFACE_REGISTER.csv`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
   - Add detailed checklist line items only where supported by approved drawings, DBM basis, or project forms; otherwise mark as `TBD`.

4. Build the workface plan.
   - Sequence: receipt of 860-1 building module at site -> off-loading -> setting on piles/foundations -> bottom-entry MCC incoming/outgoing cable installation -> mechanical hookup of utilities/drains -> grounding installation and test (#2/0 main loop, two-point connections, ground wells, 5 A HRG resistor on 600 V) -> HVAC startup and n+1 verification -> 600 V, 3 phase electric building heater installation -> lighting and receptacle installation per area classification (LED, emergency LEDs with battery backup, GFI on outdoor) -> field installation of home-run cables (TECK/ACWU/ACIC per SEC-12) -> electrical terminations -> area/exterior lighting tie-in -> I&C and communications/network tie-in -> fire & gas/safety systems tie-in.
   - Distinguish Package Vendor, EPC Integrator deliverable ownership, and Tourmaline field construction execution responsibility throughout.

5. Carry electrical/civil basis requirements into the package.
   - Include governing electrical codes and standards listed in DBM SEC-12 (CSA C22.1-21; BC provincial codes; Technical Safety BC; WorkSafeBC; BCER; API/IEEE/ISA/NEMA; API RP-505) and civil/structural standards from DBM SEC-11.
   - Reference project electrical specifications ELC-QAS-000001-001 through ELC-QAS-000018-001 by title and revision.
   - Include DBM grounding, cable, lighting, HVAC, building heater, and area-classification basis values only with source citation.
   - Keep geotechnical, topographical, plot-plan, electrical-study, vendor IFC drawing, and standby-power sizing gaps as `TBD` until accepted inputs are available.

6. Prepare inspection and turnover records.
   - Name required record categories: foundation/pile installation records; building setting and anchorage records; bottom-entry cable installation records; grounding installation and test records (continuity, ground-well bolted connections, HRG resistor function test, ground-fault alarm-only verification on 600 V); HVAC commissioning records with n+1 demonstration; lighting and emergency-lighting test records; building heater commissioning records; interface sign-off (all twelve categories); area-classification verification; open item log; turnover checklist.
   - Leave final form numbers and acceptance criteria as `TBD` unless approved project forms are available.

7. Coordinate electrical-study and vendor-document prerequisites.
   - Confirm or list as open: hazardous-area classification, load analysis, short-circuit, relay coordination/arc-flash, and load-flow studies.
   - Confirm or list as open: vendor IFC drawings, equipment lists, vendor data sheets for 860-1 MCC, transformers, UPS, panelboards, SCR heater control panels, and supporting equipment.

8. Run cross-document consistency check.
   - Confirm that Datasheet attributes appear in Specification requirements where applicable (identity, interfaces, voltage class, grounding, cable, lighting, HVAC, building heaters).
   - Confirm that every Specification requirement has a corresponding Procedure step and verification or record hook.
   - Confirm that unsupported values remain `TBD`, `ASSUMPTION`, or conflict-table entries.

9. Route unresolved conflicts for human ruling.
   - Use the Guidance Conflict Table when source roles or requirements conflict (e.g., EPC vs Tourmaline responsibility; SEC-12 vs SEC-11/PACKAGE_REGISTER building naming).
   - Do not resolve responsibility conflicts without an accepted project RACI or human ruling.

## Verification

- Package identity matches workbook row 42, PACKAGE_REGISTER, and Gate 7.
- Interface checklist includes all twelve PKG-040 workbook interface facts.
- Electrical and civil basis values match DBM SEC-11/SEC-12 and are not overstated as final construction criteria where DBM says TBD or pending detailed engineering / studies.
- Construction execution responsibility is not collapsed into deliverable ownership; Package Vendor / EPC Integrator / Tourmaline scopes remain distinct.
- All missing quantities, drawings, form IDs, electrical study results, plot-plan coordinates, and final construction criteria are marked `TBD`.
- Cathodic protection facility-design exclusion is recorded.

## Records

- Construction Work Package.
- Installation and tie-in workface plan (860-1 building module).
- Construction interface and turnover checklist (twelve interface categories).
- Open input / TBD register (geotech, topo, plot plan, electrical studies, standby generator basis, vendor IFC drawings, inspection/turnover forms).
- Electrical study readiness register.
- Responsibility matrix or RACI reference: TBD.
- Foundation/pile, building setting, bottom-entry cable, grounding, HVAC (n+1), lighting/emergency lighting, building heater, and interface sign-off inspection records: TBD final forms.
- Turnover package index: TBD final form/index structure.
