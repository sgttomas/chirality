# Procedure: DEL-075-06 — EPC Vendor Package Review and Acceptance (Cryogenic Unit / PKG-075)

## Purpose

Procedure to produce the EPC Integrator's review-and-acceptance deliverable for the PKG-075 UltraTEF cryogenic unit vendor package, ending in handoff readiness with documented evidence. This is a **production procedure** for the deliverable artifacts (review log, acceptance checklist, evidence files, turnover evidence), not an operating procedure for the cryogenic unit itself.

## Prerequisites

**Inputs**

- EPC Scope of Work for PKG-075 — TBD (not present in deliverable-local references).
- Package Datasheet for PKG-075 — TBD (related to 26020-Package_Requirements.docx heading 29; not locally readable).
- Construction Work Package for PKG-075 — TBD (not present in deliverable-local references).
- Vendor submittal package for PKG-075 (vendor document register, vendor data sheets, fabrication records, FAT/SAT records, certifications).
- Authoritative process basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 UltraTEF Cryogenic Recovery Basis (L1098-L1396).
- Sibling deliverable outputs (when available): `DEL-075-04_vendor-engineered-equipment-package` and `DEL-075-05_vendor-document-turnover-package` (ASSUMPTION based on the sibling-row pattern at `DELIVERABLE_REGISTER.csv` L45-L101; declared upstream dependencies are "None declared" in `_DEPENDENCIES.md`).

**Declared dependencies**

- Upstream: none declared during PREPARATION (`_DEPENDENCIES.md`).
- Downstream: none declared during PREPARATION (`_DEPENDENCIES.md`).

**Required references**

- DBM SEC-06 (above).
- Specification.md (this deliverable, requirements R-01 through R-14).
- Guidance.md (this deliverable, especially the safety/protective functions list).

## Steps

### Step 1 — Establish review baseline

1.1 Open `Specification.md` and confirm the requirement set (R-01 through R-14).
1.2 Open the vendor submittal package and build the **vendor document register** (one row per document).
1.3 For each document, assign a target requirement (R-01 through R-14) and a reviewer.
1.4 Verification: register row count matches submitted document count; every R-* item has at least one assigned reviewing document, or is recorded as "no vendor document submitted — gap" — TBD/ASSUMPTION if 26020 heading 29 mapping is required (R-14).

### Step 2 — Review vendor documents

For each document in the register:
2.1 Confirm the document type, revision, and approval status from the vendor.
2.2 Review against the assigned requirement(s).
2.3 Record disposition: `accept`, `accept-with-comments`, `reject`, or `defer-pending-source`.
2.4 Record review comments and any open items.
2.5 Verification: every register row carries a disposition and a reviewer signature record.

### Step 3 — Performance basis review (R-02, R-08)

3.1 Compare vendor process simulation / performance certification to DBM SEC-06 design point (inlet 7,129 kPag; design winter 14.2 °C / summer 40.5 °C; expander-mode propane recovery 99+ %; sales flow at BAHX C-pass outlet per DBM L1312).
3.2 Confirm winter-condition performance check is included (DBM L1299) — not only the single summer design point.
3.3 Confirm J-T-mode performance evidence (minimum C3 recovery ≥ 27 % for sales-gas total sulphur compliance, per DBM L1346 and L442).
3.4 Confirm deethanizer reboiler thermal sizing (TEMA BKU; 350 °F heat medium; ≥ 25 °F approach in expander mode).
3.5 Verification: each item produces a recorded comparison line in the acceptance checklist.

### Step 4 — Safety / protective-function review (R-05, R-09, R-10)

4.1 Confirm J-T valve mechanical stop / stroke limit is set such that control-failure mass flow does not exceed the cryogenic flare design flow (DBM L1321).
4.2 Confirm turbo-expander anti-surge recycle, seal-gas / lube-oil permissives, and ESD-rundown lube-oil accumulator sizing ≥ 1 minute (DBM L1322-L1323).
4.3 Confirm BAHX A-pass bypass temperature control and E-pass bypass MDMT protection (DBM L1326; L1333).
4.4 Confirm methanol injection coverage at the points listed in `Specification.md` R-06 (closure of DBM L1392 TBC list still required at project level — record as open item if unresolved).
4.5 Confirm BAHX over-temperature interlock at 66 °C with upstream molecular-sieve bed bring-online (DBM L1257).
4.6 Confirm cryogenic dry-out procedure is reviewed and accepted before start-up (DBM L1347; L1390 dry-out header assumption status to be recorded).
4.7 Verification: each protective function has a documented vendor implementation reference and an EPC acceptance signoff line.

### Step 5 — Code/standard compliance review (R-03, R-04, R-07)

5.1 Confirm BAHX ALPEMA 3rd Edition + manufacturer practice compliance with documented vendor exceptions (DBM L1324).
5.2 Confirm BAHX ASME U Stamp data report and BC CRN registration.
5.3 Confirm pump compliance: API-610 vertical inline single-stage; API-682 mechanical seal Plan 14/52 (Plan 13/52 / modified 13/52 acceptable for deethanizer reflux pumps per DBM L1335); space/anti-condensation heaters.
5.4 Confirm turbo-expander auxiliary subsystem compliance (duplex seal-gas filters; lead/lag lube-oil pumps; aerial cooler; duplex lube-oil filters; x/y vibration monitoring).
5.5 Verification: code/standard checklist row for each item, with a vendor reference (data sheet, certificate, or test record).

### Step 6 — Interface and installability review (R-12)

6.1 Confirm BAHX/expander/absorber/deethanizer module installation arrangement against the outdoor multilevel cryogenic-module basis (DBM L1134-L1135).
6.2 Confirm interface points to: upstream MS-dehy + MRU + MS-dust filter feed (DBM L1243); downstream sales-gas compression and NGL treating; dry-out header; fuel gas; heat medium (350 °F); VRU; produced-water / cryogenic drain headers; HP flare / cryogenic flare (DBM L1365-L1378).
6.3 Verification: interface matrix entry for each line in (6.2) with vendor drawing reference.

### Step 7 — Open items and conflict capture

7.1 Record each DBM-flagged TBC/TBD item that touches the vendor package (DBM L1349-L1351; L1391-L1395) in an Open Items log; do not silently close.
7.2 Add the unresolved 26020-Package_Requirements heading-29 mapping as an open item (Conflict Table C-01 in `Guidance.md`).
7.3 Verification: Open Items log non-empty (expected — many DBM TBCs remain at this stage); each item has owner and target closure phase.

### Step 8 — Test / inspection evidence collation

8.1 Collect vendor FAT records for the BAHX (helium leak test, pressure test, design-report sign-off), turbo-expander/compressor (mechanical run test, lube-oil and seal-gas commissioning), pumps (API-610 performance test records), and reboiler/exchangers (TEMA shop test records).
8.2 Collect ASME U Stamp data reports and BC CRN evidence for the BAHX and applicable pressure vessels.
8.3 Verification: each Specification R-* item maps to at least one piece of test/inspection evidence or to a justified gap.

### Step 9 — Turnover evidence assembly

9.1 Assemble: vendor document register (final disposition), package acceptance checklist (closeout state), test/inspection evidence file, open items log, conflict table.
9.2 Confirm the assembled package matches `_CONTEXT.md` "Anticipated Artifacts" (vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence).
9.3 Verification: final acceptance signoff record (EPC Integrator with Package Vendor input) is present.

## Verification (summary)

| Check | Pass criterion |
|---|---|
| All vendor documents reviewed | Vendor document register 100 % dispositioned |
| Performance basis aligned to DBM SEC-06 | Comparison record present for each design-point item; both expander and J-T modes covered |
| All safety/protective functions verified | Each protective function in `Guidance.md` has a vendor implementation reference and EPC signoff |
| All required standards demonstrated | ALPEMA/ASME/CRN/API-610/API-682/TEMA evidence recorded per asset |
| All interface lines reviewed | Interface matrix complete against DBM L1365-L1378 |
| Open items captured | DBM TBC list (L1391-L1395) reflected in Open Items log |
| Turnover evidence present | Anticipated artifact set complete |

## Records

| Record | Format | Owner |
|---|---|---|
| Vendor document review log | Tabular (CSV/MD) | EPC Integrator |
| Package acceptance checklist | Tabular (CSV/MD) | EPC Integrator |
| Test/inspection evidence file | Document set | EPC Integrator (collated from Package Vendor) |
| Open items log | Tabular (CSV/MD) | EPC Integrator |
| Turnover evidence file | Document set | EPC Integrator |
| Final acceptance signoff | Signed record | EPC Integrator (human) |
