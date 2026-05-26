# Specification: DEL-046-01 — Scope of Work (PKG-046 Acid Gas Compressors)

## Scope

### In Scope (EPC Scope of Work for PKG-046)

The EPC Integrator Scope of Work for the Acid Gas Compressor package (`26020-01-PT-12-001`) covers, at a minimum:

1. Definition of the package identity, tagged equipment count, capacity basis, and process function (compress amine acid gas, H2S+CO2, for injection/disposal). Source: `PACKAGE_REGISTER.csv`; `4-25_Deepcut_DBM.md` §Acid Gas Injection Compression Basis (lines 868, 885, 971-973).
2. Definition of facility-level boundaries and tie-ins for the package (suction-side amine regeneration, discharge-side acid gas injection pipeline interface, utilities, electrical, controls, fire and gas, structural/foundations, drains, HVAC). Source: `PACKAGE_REGISTER.csv` Applicable Interfaces; `4-25_Deepcut_DBM.md` lines 1037-1061.
3. Responsibility assignment between Package Vendor (package engineering, design, vendor documentation, equipment supply) and EPC Integrator (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination). Source: `PACKAGE_REGISTER.csv` Responsibility column.
4. Identification of upstream/downstream package interfaces (amine system, AGI pipeline, disposal well shared interface). Source: `4-25_Deepcut_DBM.md` lines 84, 93, 879, 1037-1061.
5. Identification of source-defined design constraints relevant to scope, schedule, and integration (configuration `2x100% + 1 spare`; alternative `3x50%` TBD; five-stage reciprocating; VFD-driven; common forced-draft air-cooled discharge; recycle-based capacity control with no adjustable volume pockets; sweet gas purge for maintenance). Source: `4-25_Deepcut_DBM.md` lines 878, 994-1035.

### Out of Scope (Excluded from this deliverable, per source)

- Detailed package datasheet content beyond identity-level reference — carried in DEL-046-02 Package Datasheet. Source: PROJECT_DECOMP deliverable framing (`DELIVERABLE_REGISTER.csv` DEL-046-02 description).
- Construction Work Package content — carried in DEL-046-03. Source: same.
- Vendor engineering, design, fabrication, and physical equipment supply — assigned to DEL-046-04 (Package Vendor). Source: `PACKAGE_REGISTER.csv` Responsibility; `DELIVERABLE_REGISTER.csv` DEL-046-04.
- Vendor document submittals and turnover — carried in DEL-046-05. Source: `DELIVERABLE_REGISTER.csv` DEL-046-05.
- Acid gas disposal pipeline and well design — excluded; existing shared interface. Source: `4-25_Deepcut_DBM.md` line 84.
- Disposal well pressure characteristics (MAWP, min, max) — provided by Tourmaline. Source: `4-25_Deepcut_DBM.md` lines 1049-1055.
- Modifications at the existing 02-25 facility for incremental disposal volume — TBD trigger and extent. Source: `4-25_Deepcut_DBM.md` lines 93, 173, 1059.
- Package-specific exclusions stated in source: none declared at the package level. Source: `PACKAGE_REGISTER.csv` Exclusions column (`TBD; no package-specific exclusions stated in source materials`).

## Requirements

Requirements are numbered `SOW-PKG046-REQ-NN`. Each cites a source slice. Where a requirement is inferred from EPC convention rather than source text, it is labeled `ASSUMPTION`.

### Identity and Configuration

- **SOW-PKG046-REQ-01** The Scope of Work shall identify the package as `26020-01-PT-12-001 — Acid Gas Compressor`, owned by Package Vendor with EPC Integrator integration responsibility. Source: `PACKAGE_REGISTER.csv` row PKG-046.
- **SOW-PKG046-REQ-02** The Scope of Work shall declare the operating configuration as two (2x) 100%-capacity acid gas compressor packages plus one spare compressor, and shall note the unresolved `3x50%` alternative as a TBD design decision. Source: `4-25_Deepcut_DBM.md` lines 878, 885, 994.
- **SOW-PKG046-REQ-03** The Scope of Work shall describe the compressor as a separable reciprocating, electric-driven (induction motor, VFD) compressor; specific model (Ariel KBT/6 vs KBK/6) is identified as TBD. Source: `4-25_Deepcut_DBM.md` lines 877-878, 995, 1003-1004.

### Process Function and Capacity

- **SOW-PKG046-REQ-04** The Scope of Work shall state the process function: compress amine-regenerator acid gas (H2S + CO2) for injection/disposal at the shared 02-25/04-25 disposal well. Source: `PACKAGE_REGISTER.csv` Scope; `4-25_Deepcut_DBM.md` lines 50, 868, 971-973, 1037.
- **SOW-PKG046-REQ-05** The Scope of Work shall reference the design total flow of 4.209 MMSCFD and the start-up total flow of 0.603 MMSCFD as the capacity envelope provided by the design basis. Source: `4-25_Deepcut_DBM.md` lines 996, 998.
- **SOW-PKG046-REQ-06** The Scope of Work shall identify five-stage compression with suction/discharge MAWP and design-temperature basis carried into the Package Datasheet (DEL-046-02). Source: `4-25_Deepcut_DBM.md` lines 1006-1020.

### Boundaries and Interfaces

- **SOW-PKG046-REQ-07** The Scope of Work shall enumerate the applicable interface types defined in the package register: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. Source: `PACKAGE_REGISTER.csv` Applicable Interfaces.
- **SOW-PKG046-REQ-08** The Scope of Work shall identify the upstream battery limit at the amine regenerator acid gas outlet (water-saturated). Source: `4-25_Deepcut_DBM.md` lines 988, 1039.
- **SOW-PKG046-REQ-09** The Scope of Work shall identify the downstream battery limit at the acid gas injection pipeline tie-in (3-inch NPS assumed; final sizing TBD; pipeline and well design excluded from this scope). Source: `4-25_Deepcut_DBM.md` lines 84, 1061.
- **SOW-PKG046-REQ-10** The Scope of Work shall identify the shared-interface dependency on the existing 02-25 disposal well/reservoir and shall flag potential 02-25 modification scope as TBD. Source: `4-25_Deepcut_DBM.md` lines 93, 1059.

### Responsibility and Integration

- **SOW-PKG046-REQ-11** The Scope of Work shall include a Responsibility Assignment Record distinguishing Package Vendor scope (engineering, design, vendor documentation, equipment) from EPC Integrator scope (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). Source: `PACKAGE_REGISTER.csv` Responsibility column.
- **SOW-PKG046-REQ-12** The Scope of Work shall reference the EPC handoff chain: this Scope of Work (DEL-046-01) → Package Datasheet (DEL-046-02) → Construction Work Package (DEL-046-03) → Vendor Engineered Equipment Package (DEL-046-04) → Vendor Document Turnover (DEL-046-05) → EPC Vendor Package Review and Acceptance (DEL-046-06). Source: `DELIVERABLE_REGISTER.csv` PKG-046 rows.
- **SOW-PKG046-REQ-13** The Scope of Work shall identify Tourmaline (or Tourmaline-contracted third party) as the provider of disposal well pressure data required to define acid gas compressor lifetime operating conditions. Source: `4-25_Deepcut_DBM.md` lines 1049-1055.

### Scope Items Covered

- **SOW-PKG046-REQ-14** The Scope of Work shall reference scope items `SOW-0047`, `SOW-0048`, `SOW-0049`, `SOW-0050` from the project decomposition. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. Detailed source text for each individual `SOW-####` row: location TBD (Workbook Packages row 48 binary not locally readable).

## Standards

The following standards/specifications are referenced or implied by the source materials. Specific clause-level requirements are not derived in this Scope of Work and are deferred to DEL-046-02 (Package Datasheet) and vendor specifications:

- 26020-Package_Requirements.docx (package heading 1) — Source: `_CONTEXT.md` Source Reference; location TBD (binary not locally readable in this run).
- ASSUMPTION: API 618 (Reciprocating Compressors for Petroleum, Chemical, and Gas Industry Services) is likely applicable to the acid gas compressor package. Source: industry convention for separable reciprocating compressor packages in sour gas service; not cited in available source slices.
- ASSUMPTION: NACE MR0175 / ISO 15156 (sour service materials) is likely applicable given H2S content. Source: industry convention; not cited in available source slices.
- TBD: Tourmaline / Operator standards and specifications referenced by the EPC contract — location TBD.

## Verification

| Requirement | Verification approach |
|---|---|
| SOW-PKG046-REQ-01 to 03 (identity, configuration) | Document review against `PACKAGE_REGISTER.csv` row PKG-046 and DBM §Compression Configuration |
| SOW-PKG046-REQ-04 to 06 (process function, capacity, stages) | Document review against DBM §Acid Gas Injection Compression Basis and §Acid Gas Compressor Design Conditions; trace into DEL-046-02 Package Datasheet |
| SOW-PKG046-REQ-07 to 10 (boundaries/interfaces) | Interface checklist; trace each applicable interface type to the Package Datasheet interface matrix (DEL-046-02) and to construction tie-in plan (DEL-046-03) |
| SOW-PKG046-REQ-11 (RAR) | Responsibility matrix review; cross-check against `PACKAGE_REGISTER.csv` Responsibility column and contract structure |
| SOW-PKG046-REQ-12 (handoff chain) | Deliverable register cross-reference (PKG-046 rows) |
| SOW-PKG046-REQ-13 (disposal well pressure data) | Confirmation of Tourmaline data delivery and incorporation into compressor lifetime operating conditions |
| SOW-PKG046-REQ-14 (scope items SOW-0047..50) | Scope-item traceability matrix to source workbook row 48 — verification deferred until source slices are locally accessible |

## Documentation (Required Artifacts)

From `_CONTEXT.md` Anticipated Artifacts and `DELIVERABLE_REGISTER.csv` Anticipated Artifacts:

- Package scope of work narrative
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record (RAR)

Cross-deliverable artifacts that this Scope of Work points to (produced elsewhere in PKG-046):

- Package Datasheet (DEL-046-02)
- Interface Requirements Matrix (carried in DEL-046-02)
- Construction Work Package (DEL-046-03)
- Vendor Document Register / submittals / turnover records (DEL-046-05)
- EPC vendor package review and acceptance evidence (DEL-046-06)
