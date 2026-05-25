# Procedure — DEL-017-05 Vendor Document Turnover Package (PKG-017)

## Purpose

Operational procedure to **produce, control, and turn over** the Vendor Document Turnover Package for the PKG-017 MV VFD (600 HP, 4160 V, 3-phase, 60 Hz) equipment package. The procedure covers register establishment, submittal management, EPC review handshake, and final turnover.

## Prerequisites

- Access to the Gate 7 snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Accepted upstream content from `DEL-017-04` (Vendor Engineered Equipment Package) sufficient to anchor what must be documented (ASSUMPTION — declared dependency not yet recorded in `_DEPENDENCIES.md`; see Guidance HRR-017-05-002).
- Accepted upstream EPC anchors `DEL-017-01` (Scope of Work) and `DEL-017-02` (Package Datasheet) — used as scope/interface authority for the register.
- Active project Document Control (DCC) numbering and transmittal convention (location TBD — see Guidance HRR-017-05-003).
- Active PKG-017 vendor deliverable list (VDRL/VDDR) — pending publication (HRR-017-05-001).
- References: Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`; DBM `3-25_Comp_and_Liquids_DBM.md` (lines 145, 617).

## Steps

1. **Stand up the Vendor Document Register.**
   - Create a controlled index keyed to PKG-017 identity (`PKG-017`, `26020-02-30-008`, Workbook row 19; Gate 7 `PACKAGE_REGISTER.csv`).
   - Required columns (minimum): vendor document ID, project DCC ID, title, revision, submittal class (e.g., for-information / for-approval / approved-for-construction / as-built / final-MDR), submittal date, EPC review status, EPC reviewer, interface tag(s), notes.

2. **Populate the register from the active vendor deliverable list.**
   - Use the PKG-017 entry of the active package requirements source (location TBD; carry as ASSUMPTION until resolved per HRR-017-05-001).
   - Tag each entry to one or more PKG-017 interface lines from the Gate 7 `INTERFACE_REGISTER.csv` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
   - Mark cold-service documentation requirements driven by the site basis (-40 °C, DBM line 145).

3. **Issue vendor document submittals against the register.**
   - Each issued submittal updates its register row (revision, status, dates).
   - Source-required document table rows are stored as artifacts under the package; they are not promoted to separate deliverables (Gate 7 `DELIVERABLE_REGISTER.csv` Notes).

4. **Run the EPC Integrator review handshake.**
   - EPC Integrator reviews each submittal for interface/integration impact.
   - Comments captured in a review log; vendor responds and re-issues; register status updated until accepted.
   - This handshake is the principal mechanism by which `DEL-017-06` (EPC Vendor Package Review and Acceptance) consumes this deliverable.

5. **Compile turnover records.**
   - Build the Manufacturing Data Record / Vendor Data Book covering all final-revision vendor documents.
   - Close the document acceptance log.
   - Assemble final transmittals and handover sign-off package.

6. **Hand over to `DEL-017-06`.**
   - Issue final-revision Vendor Document Register snapshot, the MDR/VDB, and the closed acceptance log to the EPC Integrator acceptance activity.

## Verification

| Step | Check |
|---|---|
| 1 | Register exists, is controlled (version + owner), and references PKG-017 identity. (V-1) |
| 2 | Every required document class is present; every entry is tagged to at least one PKG-017 interface; cold-service items flagged. (V-2, V-3) |
| 3 | All submittals appear in the register with current revision, status, and dates; source document rows are carried as artifacts only. (V-1) |
| 4 | EPC review log shows comment resolution to closure; no open critical comments at turnover. (V-5) |
| 5 | MDR/VDB is complete; acceptance log closed; sign-off captured. (V-4) |
| 6 | `DEL-017-06` confirms receipt and acceptance of the turnover package. (V-5) |

## Records

Records produced and retained:

- Vendor Document Register (final revision + revision history)
- All vendor document submittals at their final accepted revisions
- Source document table rows as artifact evidence
- EPC review comment log (with vendor responses and closure)
- Manufacturing Data Record / Vendor Data Book
- Final transmittal package and handover sign-off
- Turnover acceptance evidence forwarded to `DEL-017-06`
