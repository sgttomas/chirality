# Procedure — DEL-067-01 Scope of Work

> Operational procedure for producing the EPC Scope of Work for PKG-067 "Tanks, Sour Water (API 650) 4-25". This procedure describes the steps required to **produce** the SOW artifact (deliverable type: EPC Scope of Work, `DELIVERABLE_REGISTER.csv` row 528). Where judgment is required and source does not constrain, the step is marked `TBD`.

## Purpose

Define a repeatable, source-grounded procedure for authoring and verifying the EPC Scope of Work for PKG-067 such that it satisfies every requirement in `Specification.md` (R-067-01-01 through R-067-01-09) and reproduces the source-anchored language captured in `Datasheet.md`.

## Prerequisites

- Read the deliverable-local truth set:
  - `_CONTEXT.md`
  - `_STATUS.md`
  - `_REFERENCES.md`
  - `_DEPENDENCIES.md`
  - `_SEMANTIC.md` (placeholder during Pass 1/Pass 2)
- Confirm access to authoritative sources:
  - `_Sources/26020-Package_Requirements.docx` (heading `26020-01-PT-19-005 - Tanks, Sour Water`, paragraphs 276–288)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Produced Water section, lines 502–525; facility tables lines 268, 493, 1646, 1714, 2013, 2555–2559, 2627)
  - GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row 528; `PACKAGE_REGISTER.csv` row 94
  - Analog: `26020-03-PT-19-007 - Tanks, Sour Water` (3-25)
- Declared upstream dependencies: none in `_DEPENDENCIES.md`. (No blocker; downstream consumers documented in DELIVERABLE_REGISTER rows 529–533.)

## Steps

### Step 1 — Establish identity and source basis

1. Read `_CONTEXT.md` Identity table; record the canonical deliverable ID, package ID, package name, discipline, and responsible party.
2. Open `26020-Package_Requirements.docx` at heading `26020-01-PT-19-005 - Tanks, Sour Water`. Capture the "Basic Scope" and "Major Included Equipment" paragraphs verbatim into the SOW source notebook.
3. Open `PACKAGE_REGISTER.csv` row 94. Capture: package short name, governance note (responsibility split), interface type list, exclusions field (`TBD; no package-specific exclusions stated in source materials`), and Word Source Basis note (3-25 analog reference).
4. Open `DELIVERABLE_REGISTER.csv` row 528. Capture: anticipated artifacts list, covered scope items (`SOW-0225`–`SOW-0228`), supported objectives.

### Step 2 — Draft the package identity section

1. Use Datasheet `Identification` row content to seed the SOW identity heading.
2. List the two expected tags `TK-9010-1` and `TK-9020-1` exactly as in `26020-Package_Requirements.docx` paragraph 281.
3. Cite the source heading number explicitly (`26020-01-PT-19-005`).

### Step 3 — Draft the package function and integration narrative

1. Compose the integration narrative using the example in `Guidance.md` (R-067-01-04 example). Required upstream/downstream pointers:
   - Upstream sources of produced water: inlet separator system (DBM line 589), NGL water-wash recycle (DBM line 1558), mole-sieve inlet coalescer (DBM line 1602), regeneration-gas scrubber (DBM line 1621), compressor stage-1 scrubber (DBM line 1025), 300# ANSI produced-water drain header (DBM line 2013).
   - Storage at `TK-9010-1` / `TK-9020-1`.
   - Downstream transfer: 2 x 100% produced-water transfer pumps in Tank Farm Pump Building 2 / PKG-060 (DBM lines 521, 2555) → new produced-water pipeline → 03-25 Liquids Hub (DBM lines 493, 502–510).
   - Vapour management: LP fuel gas blanket; VRU header where applicable (DBM line 1683; `26020-Package_Requirements.docx` paragraph 281).
2. Use the verbatim phrase "produced water" from DBM line 508 to describe the service composition. Do not invent a closed contaminant list; reproduce the "non-exhaustive; TBC" qualifier.

### Step 4 — Draft the boundary and interface section

1. Enumerate each interface type from `PACKAGE_REGISTER.csv` row 94, once, in the listed order.
2. For each, write a one-line bound: what the package provides at the interface, and what the EPC Integrator picks up. Mark interface line/tag specifics as `TBD — to be carried by DEL-067-02 Package Datasheet`.
3. Add the explicit exclusion bullets:
   - produced water pipeline beyond facility riser is by others (DBM line 506);
   - sour-produced-water with sand/solids from the 03-25 Compressor Station stream is NOT in 04-25 produced water (DBM line 504);
   - detailed sizing reserved for detailed engineering (EPRV sizing, tank isolation philosophy, dimensions, capacity at maximum operating level) — DBM line 524; line 1714.

### Step 5 — Draft the responsibility assignment record

1. Reproduce the governance note from `PACKAGE_REGISTER.csv` row 94 as the basis paragraph. Cite the register row inline.
2. Add a small table mapping deliverable IDs in the package to responsible parties (DEL-067-01 EPC Integrator; DEL-067-02 EPC Integrator; DEL-067-03 EPC Integrator; DEL-067-04 Package Vendor with EPC integration review; DEL-067-05 Package Vendor with EPC review; DEL-067-06 EPC Integrator lead with Package Vendor input). Sources: `DELIVERABLE_REGISTER.csv` rows 528–533.

### Step 6 — Draft the source basis citation block

1. Cite the GATE-07 snapshot folder, deliverable register row, package register row, package requirements docx heading, and DBM section line ranges.
2. Identify the 3-25 analog (`26020-03-PT-19-007 - Tanks, Sour Water`) explicitly as analog and not as 4-25 source authority.

### Step 7 — Internal cross-document consistency check (Pass 2)

1. Confirm tag names appear identically in `Datasheet.md`, `Specification.md`, `Guidance.md`, and the draft SOW narrative (`TK-9010-1`, `TK-9020-1`).
2. Confirm units, capacities, and rates match across all four documents (2 x 2,000 bbl; 60 m3/d continuous; ~240 m3/d batch; design SG 1.25 (TBC)).
3. Confirm interface type list is identical in `Datasheet.md`, `Specification.md` R-067-01-06, and the draft SOW boundary section.
4. Confirm "modified API 650" qualifier handling matches Conflict Table entry CT-067-01-A.
5. Reconcile any drift back to source; record unresolved drift as a new Conflict Table row in `Guidance.md`.

### Step 8 — TBD and ASSUMPTION sweep

1. List every `TBD` and `ASSUMPTION` marker in the SOW draft and the four documents.
2. For each, confirm it traces to either a source `TBC`/`TBD` (e.g., DBM line 524) or an explicit skill-side ASSUMPTION (e.g., objective association via PACKAGE_HEURISTIC).
3. Convert nothing silently; only convert when the human ruling (Conflict Table) authorizes.

### Step 9 — Status update

1. Confirm `_STATUS.md` Current State is `OPEN` (or `INITIALIZED` per ALLOW_OVERWRITE_STATES).
2. Update `_STATUS.md` to `INITIALIZED` with provenance `TASK+four-documents` and append a History line. Do not regress state.

## Verification

| Check | Pass Criterion |
|---|---|
| Tagged equipment listed | Both `TK-9010-1` and `TK-9020-1` present in SOW identity section. |
| API 650 (modified) cited | Standard cited with explicit "modified" qualifier per `26020-Package_Requirements.docx` paragraph 281; clause location `TBD`. |
| Service description matches source | Composition language reproduces DBM line 508 (non-exhaustive; SG 1.25 (TBC)). |
| Integration narrative completeness | All upstream sources (inlet separator, NGL water wash, mole-sieve, regen scrubber, compressor stage-1 scrubber, drain header) and downstream targets (PKG-060 pumps, produced-water pipeline, 03-25 Liquids Hub) named with source citations. |
| Interface types present | All nine interface types from `PACKAGE_REGISTER.csv` row 94 enumerated. |
| Responsibility section | Governance note from `PACKAGE_REGISTER.csv` row 94 reproduced; in-package responsibility table consistent with `DELIVERABLE_REGISTER.csv` rows 528–533. |
| Exclusions captured | All three explicit exclusions present (pipeline-by-others; 03-25 sand/solids exclusion; detailed-engineering reservations). |
| Source citations resolve | Every citation path resolves to an existing file under `_Sources/` or under the GATE-07 snapshot. |
| Status updated | `_STATUS.md` set to `INITIALIZED` only if previous state was `OPEN`. |

## Records

| Record | Location |
|---|---|
| SOW narrative artifact | Package SOW document (produced under this deliverable; canonical filename per project convention — `TBD`). |
| Source-anchored notebook | Working notes captured during Steps 1–6 (working artifact; not persisted in deliverable folder). |
| Conflict Table updates | `Guidance.md` (this deliverable). |
| Run record | `_run_records/TASK_RUN_*.md` (this deliverable). |
| Status history | `_STATUS.md` History section. |
