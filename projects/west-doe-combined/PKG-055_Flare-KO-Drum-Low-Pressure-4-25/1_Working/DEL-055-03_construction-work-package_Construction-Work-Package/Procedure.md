# Procedure: DEL-055-03 — Construction Work Package (LP Flare KO Drum, 4-25)

**Interpretation:** This Procedure describes the steps required to *produce* the Construction Work Package deliverable (the document set and its supporting artifacts) for PKG-055. It is not the field execution procedure for installing the equipment (that artifact — the workface plan — is one of the *outputs* of this deliverable).

## Prerequisites

1. Accepted upstream snapshot available: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. — `_REFERENCES.md`.
2. Deliverable-local files present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`. — verified in this run.
3. Vendor package documentation for `26020-01-PT-17-003 — Flare KO Drum (LP)` available. — PACKAGE_REGISTER.csv row PKG-055. (Detailed vendor document set is TBD until DEL-055-04 / DEL-055-05 produce content.)
4. West Doe Deepcut DBM (4-25) available. — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
5. `26020-Package_Requirements.docx` package heading 10 content — currently `location TBD` (not locally accessible as markdown).

**Declared dependencies (from `_DEPENDENCIES.md`):** None declared during PREPARATION; `Dependencies.csv` not yet generated. Treat as advisory; this Procedure does not assume blockers.

## Steps

### Step 1 — Confirm package boundary and scope

- Read PACKAGE_REGISTER.csv row PKG-055 to confirm vendor-vs-EPC ownership split.
- Confirm the equipment list (V-3900-1, P-3900-1) and the package tag (26020-01-PT-17-003) match `_CONTEXT.md` and DBM equipment list lines 2580-2581.
- Record any boundary ambiguities as `TBD` or in the Conflict Table.

### Step 2 — Catalog interface scope

- List every applicable interface type from PACKAGE_REGISTER.csv row PKG-055 (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports).
- For each interface type, identify the responsible discipline lead and the target tie-in points based on the DBM (e.g., LP flare relief header — DBM line 2029).

### Step 3 — Establish facility-integration design basis

- Extract the LP flare architecture from DBM Sec. 8 (lines 1834, 2021-2042):
  - LP flare header size (508 mm / 20 in).
  - Piggy-back configuration on the common HP/cryo stack.
  - LP KO drum pump truck-out provision.
- Capture spacing requirements (DBM line 287) and freeze-protection requirements (DBM line 2033) as construction constraints.
- Where the DBM defers to OGAOM, OGPFR, or API 2510 and the underlying text is not locally accessible, retain DBM-stated values as the design basis and flag `location TBD`.

### Step 4 — Draft the installation and tie-in workface plan

- Sequence tie-ins to the LP flare header so that upstream LP relief consumers (amine regen, TEG regen, VRU, recip compressor seal pot, primary seal vent, mole-sieve regen blowdown — DBM lines 1702, 1781, 1801) can be commissioned without re-opening the LP header.
- Constrain VRU suction header to LP flare bypass routing to free-drain without traps, sloping toward the LP KO drum (DBM line 1787).
- Identify scaffolding, laydown, and lifting plans that maintain ≥10 m spacing from vegetation/fire hazards (DBM line 287).
- Steps requiring vendor-specific information not yet available shall be marked `TBD` and resolved when DEL-055-04 produces the vendor engineered package.

### Step 5 — Draft the construction interface and turnover checklist

- Produce one checklist per interface type from Step 2.
- Each checklist row shall include: tie-in tag, partner discipline, mechanical completion criterion, inspection record reference, signoff line.
- Include a turnover (mechanical-completion) section covering: NDE records, pressure-test records, EHT continuity, alignment records, surveyed location, instrument loop checks (for I&C interface).

### Step 6 — Capture mechanical-integrity record requirements

- List record types required for turnover: welder qualifications, NDE reports, pressure-test reports, EHT commissioning report, alignment/torque records, as-built surveys.
- ASSUMPTION: this list reflects standard EPC CWP practice; once `26020-Package_Requirements.docx` heading 10 is accessible, reconcile this list with the project-specific package-requirement clauses.

### Step 7 — Cross-document consistency sweep

- Verify Datasheet ↔ Specification: tags V-3900-1 and P-3900-1, header size 508 mm, spacing 10 m, services list are identical across documents.
- Verify Specification ↔ Procedure: every requirement R-CWP-01..R-CWP-10 has a verification method that is reflected here as a step or a record.
- Verify Specification ↔ Guidance: requirements have rationale in Guidance Principles or Considerations.
- Resolve inconsistencies from drafts where possible; otherwise add to the Conflict Table in `Guidance.md`.

### Step 8 — Status update

- If `_STATUS.md` Current State is `OPEN`, set state to `INITIALIZED` using `tools/scaffolding/write_status.sh` with caller `TASK+four-documents`.
- Otherwise leave `_STATUS.md` unchanged and report the skip.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Four documents exist | File listing in `{DELIVERABLE_PATH}` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present |
| Default schema sections present in each | Review | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose/Prereqs, Steps, Verification, Records) |
| At least one locally accessible source read from `_REFERENCES.md` | Run record | `DBM-Deepcut/4-25_Deepcut_DBM.md` read with section line references |
| Substantive claims source-grounded; missing values marked `TBD`; inferences labeled `ASSUMPTION` | Document review | All non-trivial values cite source path + line/section, or are marked `TBD` / `ASSUMPTION` |
| Cross-document consistency | Review per Step 7 | No contradictions, or contradictions captured in Conflict Table |
| `_STATUS.md` updated safely | File diff | State transitioned `OPEN → INITIALIZED` only when starting state was `OPEN` |

## Records

- This deliverable folder, containing: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, updated `_STATUS.md`.
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md`.
- (Downstream) After equipment installation, the EPC Integrator's executed workface plan, interface checklists, NDE reports, EHT commissioning report, alignment/torque records, pressure-test certificates, and turnover punch list.
