# Procedure: DEL-081-01 — Scope of Work (PKG-081 Flare KO Drum (High Pressure) 3-25)

> Operational procedure for **producing** the EPC Integrator-authored Scope of Work artifact for PKG-081. (Interpretation rule: this is an EPC document-production deliverable, so Procedure describes how to produce the artifact, not how to operate the equipment.)

## Purpose

Produce the Scope of Work artifact set for PKG-081 ("Flare KO Drum (High Pressure) 3-25") so that downstream PKG-081 deliverables (`DEL-081-02` Package Datasheet, `DEL-081-03` Construction Work Package, `DEL-081-04` Vendor Engineered Equipment Package, `DEL-081-05` Vendor Document Turnover, `DEL-081-06` EPC Vendor Package Review and Acceptance) have an authoritative, source-anchored, integration-and-responsibility document to draw from.

## Prerequisites

### Required deliverable-local files (must be present)
- `_CONTEXT.md` — present.
- `_STATUS.md` — present, current state must be in `ALLOW_OVERWRITE_STATES` (`OPEN, INITIALIZED`).
- `_REFERENCES.md` — present.
- `_DEPENDENCIES.md` — present (no declared upstream / downstream at PREPARATION).
- `_SEMANTIC.md` — present (placeholder only).

### Required accessible source materials
- Gate-7 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` including: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_REGISTER.csv`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (relevant: SEC-01 Exclusions and Shared Interface Notes; SEC-02 Site; SEC-07 HP flare basis; SEC-09 sparing, isolation, vessel design).

### Declared upstream dependencies
- None declared at PREPARATION (`_DEPENDENCIES.md`). No upstream maturity threshold blocks initiation.

### Acknowledged inaccessible references
- `_Sources/26020-Package_Requirements.docx` package heading 34 (binary docx; markdown extraction not in workspace).
- `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy (referenced by DBM SEC-07; not in workspace).
These produce `location TBD` markers, not values.

## Steps

1. **Confirm scope is authorized.** Read `_STATUS.md` and confirm current state is in `ALLOW_OVERWRITE_STATES` (`OPEN` or `INITIALIZED`). If not, stop and report.
2. **Hydrate identity.** Extract identity fields from `_CONTEXT.md` Identity table and corroborate against `DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv` row for PKG-081 / DEL-081-01.
3. **Extract authoritative scope items.** From `SCOPE_LEDGER.csv` pull rows `SOW-0071`, `SOW-0072`, `SOW-0073`, `SOW-0074` exactly as written and treat them as scope-defining statements.
4. **Extract package basis from DBM.** From `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` read the HP flare basis paragraphs in SEC-07 and the HP flare KO drum transfer pump row in SEC-09 sparing table. Capture verbatim phrases for: V-4100-2, V-4150-2, P-4100-2, P-4150-2, HP relief header 508 mm / 20 inch, manifold to HP flare, truck-out provision, sparing 1 x 100 percent per drum.
5. **Enumerate interfaces.** From `INTERFACE_REGISTER.csv` filter rows where `PackageID = PKG-081`; record all 10 interface types (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports).
6. **Capture responsibility split.** Use the `PACKAGE_REGISTER.csv` description column verbatim for the Package Vendor vs. EPC Integrator split, and corroborate against `OBJ-004` register entry and `ART-00ABFE7374` description.
7. **Map artifacts.** From `ARTIFACT_REGISTER.csv` pull all rows with `DeliverableID = DEL-081-01_scope-of-work` and list them as the artifact set this deliverable produces.
8. **Associate objectives.** Use `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-081-01 to record supported objectives. Because the mapping is package-grouped (per skill `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`), label the association `ASSUMPTION (PACKAGE_HEURISTIC)`.
9. **Surface open items.** Translate SOW-0074 into an explicit open-item / conflict entry in `Guidance.md` Conflict Table; record the shared-flare-stack allocation (DBM SEC-01) as a second conflict entry.
10. **Mark inaccessible sources.** Wherever content depends on the binary docx or the external blowdown philosophy report, write `location TBD` and cite the document number; do not reconstruct clause text.
11. **Write the four documents.** Produce `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` with the default schema sections and the cross-document terminology fixed (same equipment tags, same responsibility wording, same interface list).
12. **Cross-check consistency** (Pass 2). Verify identical tag strings, identical interface-type strings, identical responsibility wording, and that no per-vessel design values leaked into the Scope of Work (those belong to `DEL-081-02`).
13. **Update status safely.** If current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` to transition `OPEN -> INITIALIZED`. Do not regress state.
14. **Persist run record.** Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with all required frontmatter and body headings.

## Verification

| Check | How |
|---|---|
| Identity matches registers | Diff `Datasheet.md` Identification table against `DELIVERABLE_REGISTER.csv` row and `PACKAGE_REGISTER.csv` row for PKG-081. |
| Tagged equipment consistent | Search for V-4100-2, V-4150-2, P-4100-2, P-4150-2 in all four documents; counts must match. |
| Interface enumeration complete | Confirm 10 interface types appear and match `INTERFACE_REGISTER.csv` PKG-081 filter. |
| Scope items covered | Confirm SOW-0071..SOW-0074 are each referenced at least once (Datasheet "Covers Scope Items" + Specification REQ-SOW-* + Guidance Conflict Table). |
| No vendor-design values | Confirm no design pressures, dimensions, materials, or pump curves appear in this deliverable. |
| Inaccessible-source claims marked | Confirm `location TBD` is used wherever the docx or `W242510-PRC-REP-000003-001` would be the only basis. |
| Objective association labeled | Confirm objectives are tagged `ASSUMPTION (PACKAGE_HEURISTIC)`. |
| Status transition safe | `_STATUS.md` shows `OPEN -> INITIALIZED` only if it was `OPEN`; no regression. |
| Run record written | `_run_records/TASK_RUN_*.md` exists with `run-status` set to final value. |

## Records

- `Datasheet.md` (this deliverable folder)
- `Specification.md` (this deliverable folder)
- `Guidance.md` (this deliverable folder, including Conflict Table)
- `Procedure.md` (this deliverable folder)
- `_STATUS.md` updated `OPEN -> INITIALIZED` (when applicable)
- `_run_records/TASK_RUN_<timestamp>.md`
- Artifact register entries already declared in `ARTIFACT_REGISTER.csv` (ART-3A59CA7249, ART-531950B8A7, ART-8045E643FB, ART-00ABFE7374, ART-F37B133BFD) are the downstream evidence anchors for the Scope of Work content produced here.
