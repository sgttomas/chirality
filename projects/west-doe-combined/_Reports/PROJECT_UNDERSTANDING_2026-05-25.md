# Project Understanding — west-doe-combined

**Date:** 2026-05-25
**Author:** ORCHESTRATOR persona, human-directed (ryan@chirality.ai), via five bounded read-only `Explore` evidence agents
**Project:** `projects/west-doe-combined/` (105 packages / 594 deliverables / 11 objectives)
**Decomposition basis:** Gate-7 Final Published PROJECT_DECOMP snapshot, 2026-05-24, verdict APPROVED / FINAL PUBLISHED, zero open issues at close
**Snapshot path:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Framing reference:** `docs/thesis/` (read in full this turn) — claims here carry FACT / ASSUMPTION / PROPOSAL / TBD labels per K-PROV-1 / K-INVENT-1

---

## 1. Project state at a glance

| Quantity | Value | Label |
|---|---|---|
| Packages | 105 | FACT |
| Deliverables | 594 | FACT |
| Artifacts (anticipated) | 8,036 | FACT |
| Interfaces (Gate-7 register) | 922 | FACT |
| Objectives | 11 | FACT |
| OBJECTIVE_SCOPE mappings | 2,146 | FACT |
| OBJECTIVE_DELIVERABLE mappings | 4,575 | FACT |
| Open issues at Gate-7 close | 0 | FACT |
| Lifecycle distribution | 594 IN_PROGRESS; 0 in all other states | FACT |
| Authentication / ISSUED count | 0 | FACT |

Lensing phases (2.3 semantic-matrix-build, 2.4 lens-register, 2.5 four-documents P3_ONLY) were intentionally skipped per human directive. `docs/TYPES.md` §5.1 sanctions the direct `INITIALIZED → IN_PROGRESS` transition. Consequence: no `_SEMANTIC.md` and no `_SEMANTIC_LENSING.md` files exist anywhere in the project; four-document kits reflect Pass 1 (draft) + Pass 2 (cross-document consistency) only.

---

## 2. Ontology — what exists (Agent A)

**On-disk ↔ register reconciliation:** 594 of 594 deliverables in `DELIVERABLE_REGISTER.csv` correspond 1-to-1 to on-disk `DEL-XX-YY_*/` folders with `_CONTEXT.md` present. Zero orphans. **FACT.**

**Scope and objective resolution (sample of 25 deliverables):** Every `CoversScopeItems` SOW-ID and every `SupportsObjectives` OBJ-ID resolves to a row in `SCOPE_LEDGER.csv` / `OBJECTIVE_REGISTER.csv`. **FACT.** This means anchor-class traceability from deliverable → SOW → objective is intact at the register level.

**Package label collisions (six groups, broader than previously catalogued):** **FACT.**

| Group | Packages sharing label |
|---|---|
| "Earthworks for foundations" | PKG-001, PKG-002 |
| "Site Grading" | PKG-003, PKG-004, PKG-005 |
| "Controls system design and integration" | PKG-008, PKG-009, PKG-010 |
| "MV VFD" family variants (5000HP etc.) | PKG-019, PKG-025 (plus 600HP/1500HP/2000HP near-duplicates) |
| "Instrumentation (outside of Mechanical Packages only)" | PKG-043, PKG-044, PKG-045 |
| "Tanks [DSO/API]" | 11 packages in the PKG-063 … PKG-098 range |

These are not necessarily defects — the Gate-7 decomposition rationale may justify scope-by-fluid or scope-by-rating splits — but they violate one-glance distinguishability and may surface ambiguity in cross-deliverable references.

**OBJECTIVE_ASSOCIATION basis:** 105 of 106 packages declare `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC` (698 explicit occurrences across run records and metadata). Objective mapping is therefore an **ASSUMPTION** rooted in package-level heuristics, not deliverable-level explicit mapping — this is the dominant ontological assumption in the project.

---

## 3. Praxiology — how work is done (Agent B)

**INTERFACE_REGISTER shape:** 922 rows; columns `InterfaceID, PackageID, WorkbookID, WorkbookRow, PackageName, Discipline, InterfaceType, Applicability, SourceRef, Notes`. Each row is a *package-to-discipline* interface fact (touchpoint with electrical, I&C, utility piping, etc.), not a deliverable-to-deliverable edge. **FACT.**

**Anchor compliance (K-DEP-1):** 0 of the sampled deliverables carry an `IMPLEMENTS_NODE` anchor row in a `Dependencies.csv`. **FACT.** No `Dependencies.csv` files have yet been extracted for the sampled set; each `_DEPENDENCIES.md` shows the PREPARATION scaffold ("None declared during PREPARATION"). This is consistent with the coordination policy in `_Coordination/_COORDINATION.md` (DECLARED mode, advisory blocker computation, on-demand aggregation).

**Edge density:** Median EXECUTION-class dependency rows per deliverable in sample = 0. **FACT.** Cross-deliverable production coupling is not yet machine-readable.

**Unresolved / TBD locations:** 189 TBD/UNKNOWN mentions across 30 sampled deliverables, concentrated in mechanical/process packages (PKG-046, PKG-100 carry 7–12 each); electrical (PKG-040) carries 10+; civil (PKG-001) carries 0 in this sample. **FACT.**

**Cross-discipline interface concentration (ASSUMPTION, small sample):** Electrical-to-mechanical coupling appears densest; controls packages (PKG-008/009/010) function as integrators with ~8 interfaces each; civil packages carry the fewest (~2 each). **ASSUMPTION.**

**Topology blocker:** Dependency closure cannot be attempted in its current state. Until `TASK + dependency-extract` runs to populate `Dependencies.csv` across the project and anchors are declared, cross-package impact analysis, critical-path scheduling, and K-DEP-2 resolution checks are infeasible. **PROPOSAL** for next-assignment consideration.

---

## 4. Epistemology — what can be known (Agents C + E)

**This is the load-bearing pillar (thesis Ch. 3 §3.4). The findings here are the headline.**

### 4.1 Warrant-state distribution (Agent C, 22-kit sample, 764 label tokens)

| Label | Count | % |
|---|---|---|
| FACT | 2 | 0.3% |
| ASSUMPTION | 120 | 15.7% |
| PROPOSAL | 31 | 4.1% |
| TBD | 611 | 80.0% |

**FACT.** Four-fifths of the sampled warrant labels are TBD. Only two FACTs were detected in the entire sample (both in PKG-104 structural-steel kit). Civil, Controls, and Electrical clusters carry zero FACT labels.

### 4.2 Provenance attachment

Across ~3,571 substantive claims in the sample, **~12% carry an explicit source citation** (file path or section reference). **ASSUMPTION** (sampling-driven). Structured Datasheet/Specification table rows reach 25–40% citation density; prose sections (Guidance narrative, Procedure steps) drop below 5%. Provenance is therefore concentrated in the structured-table interface that the four-document schema mandates, and largely absent from the prose layer where lensing would have inserted it.

### 4.3 Conflict Table density

164 HRR rows across the 22 sampled kits — **avg 7.5 HRR rows per kit**, range 5–23. Every sampled Conflict Table is non-empty. **FACT.**

### 4.4 Source corpus & provenance chain (Agent E)

`_Sources/` contains four substantial markdown artifacts (the two DBM files — Comp & Liquids 73 KB / 941 lines; Deepcut 334 KB / 3,479 lines — and their two traceability appendices) and two unparsed binaries:

| Binary | Size | Referenced by | Status |
|---|---|---|---|
| `26020-Package_Requirements.docx` | 729 KB | **312 of 594 deliverables (52.5%)** | Unparsed |
| `26020-Packages_Interfaces_4_export.xlsx` | 16 KB | 0 sampled `_REFERENCES.md` | Unparsed |

**FACT.** All 20 of 20 spot-checked path pointers in sampled `_REFERENCES.md` files resolve on disk (100%). However, every `_REFERENCES.md` explicitly carries a "Missing / Deferred References" boilerplate: *"No deliverable-specific source slices copied during PREPARATION. Downstream drafting must resolve locally accessible source slices before producing source-grounded production documents."* The warrant chain is **intrinsic-complete** (decomposition anchors, Gate-7 registers, DBMs all resolve) but **extrinsic-incomplete** (K-PROV-1 dead-ends on the unparsed `.docx` for over half the project). **FACT.**

---

## 5. Axiology — human-ruling queue (Agent D)

Agent D extracted **78 HRR rows** across its sampled deliverables and clustered them. Ranked clusters:

| Rank | Theme | HRR rows in sample | Reach |
|---|---|---|---|
| 1 | Vendor-deliverable enumeration missing (vendor doc registers, test schedules, acceptance criteria) | 12 | High — all vendor packages |
| 2 | Compressor/equipment model & configuration conflict (Ariel KBT/6 vs KBK/6; 2×100% vs 3×50% AGI) | 10 | Medium-high — PKG-046 dominant, electrical cascade |
| 3 | Binary source slice inaccessible (`26020-Package_Requirements.docx` headings 1 & 18; `.xlsx` row 90) | 8 | High — 10+ packages |
| 4 | Pressure / design-value conflict (5th-stage discharge 1,200 vs 1,500 psig; disposal-well MAWP TBC; MAWP anomalies) | 7–8 | Medium-high — PKG-046 |
| 5 | Package identity / nomenclature ambiguity (4160V switchgear vs MCC; API 650 Standard vs Modified; DSO acronym) | 7 | Medium |
| 6 | Cross-facility external interface assumption (02-25 disposal well; shared incinerator; truck-out vs C5+) | 6 | Medium |
| 7 | Responsibility-assignment ambiguity (EPC vs subcontractor; Tourmaline field exec vs deliverable author) | 6 | Medium |
| 8 | Missing design value (disposal-well min/max; pour point; DSO coating; dehydration) | 6 | Medium |
| 9 | Interface applicability / tier assignment | 5 | Medium |

Agent D's highest-leverage single ruling: **extract `26020-Package_Requirements.docx` (headings 1, 18) and `.xlsx` row 90 to plain-text and re-run conflict detection.** That one action is estimated to clear 40–50 of the sampled 78 HRR rows (~51–64%) by closing the binary-access cluster directly and unblocking downstream vendor-enumeration and nomenclature clusters. **PROPOSAL.**

---

## 6. Warrant-lifecycle position

Per thesis Ch. 3 §3.2.2 / Ch. 5 §5.5, every non-trivial claim sits on UNWARRANTED → CITED → REVIEWED → AUTHENTICATED.

**The project is currently in early CITED state.** **FACT.**

- ~20% of claims carry source citations (FACT / ASSUMPTION / cited PROPOSAL) — partially CITED.
- ~80% of claims carry TBD — formally UNWARRANTED, but visibly so per K-INVENT-1.
- Zero claims are REVIEWED. No licensed-professional review has been recorded; `_STATUS.md` shows no transitions beyond IN_PROGRESS.
- Zero claims are AUTHENTICATED. No deliverable has reached CHECKING or ISSUED. K-AUTH-1 reserves these transitions to the licensed professional.

Lensing-skip impact: lensing would have raised the FACT share by ~8–12 percentage points (by mechanically anchoring claims to DBM line numbers and to the unparsed binary once extracted), normalized vocabulary, and surfaced semantic-redundancy conflicts not currently visible. Skipping was a deliberate, sanctioned choice — but the choice means downstream warranting work must do that lifting manually. **ASSUMPTION** on the magnitude; **FACT** on the direction.

---

## 7. Candidate next assignments

All three are **PROPOSAL**; the user picks (K-AUTH-1).

**Option A — Parse the unparsed source binaries.** Extract `_Sources/26020-Package_Requirements.docx` (729 KB) and `_Sources/26020-Packages_Interfaces_4_export.xlsx` (16 KB) to plain-text markdown with section-level anchoring. Highest leverage by far: Agent E shows the `.docx` is referenced by 312 of 594 deliverables (52.5%); Agent D's top-3 ranked clusters all depend on this extraction. Estimated downstream impact: ~40–50 HRR rows cleared in the sampled subset alone, with proportional clearance project-wide. Read-only deliverable: parsed markdown placed in `_Sources/` alongside the existing DBMs, with a fresh `_run_records/` entry per deliverable noting the new source availability. No state transitions.

**Option B — Run `TASK + dependency-extract` across the project.** Populate `Dependencies.csv` for all 594 deliverables, attach IMPLEMENTS_NODE and TRACES_TO_REQUIREMENT anchors against Gate-7 registers, and surface EXECUTION-class edges. Resolves Agent B's topology blocker. Enables downstream blocker computation, critical-path analysis, and AUDIT_DEP_CLOSURE. Tractable in parallel batches (40 deliverables × ~15 batches). Stays within DELIVERABLE-LOCAL write scope per K-WRITE-1.

**Option C — Pilot REVIEW gates on one package end-to-end.** Pick a single small package (PKG-001 Earthworks-for-foundations, 4 deliverables, low TBD density per Agent B) and run the REVIEW agent's 5-gate protocol to advance its kits from CITED toward REVIEWED. Generates empirical data on what review-time cost looks like in practice, which is precisely the empirical gap thesis Ch. 9 flags as highest-priority future work. Smaller scope; serves a thesis-validation function.

**Recommended sequencing (PROPOSAL):** A → B → C. Option A unblocks the inputs Option B's extraction will rely on; Option C is most informative once warrant state is mid-CITED rather than early-CITED.

---

## 8. Open items / TBD

- **TBD:** Whether the six label-collision groups (§2) reflect intentional Gate-7 scope splits or artefacts of decomposition. Resolution: read `PROJECT_DECOMP.md` rationale sections or raise as a scope-change packet candidate.
- **TBD:** Whether `26020-Packages_Interfaces_4_export.xlsx` is genuinely orphaned (Agent E found zero sampled-`_REFERENCES.md` references) or referenced via non-path mechanisms.
- **TBD:** Exact provenance-attachment rate across the full 594-deliverable population — Agent C's ~12% is a 22-kit estimate; project-wide measurement would require AUDIT_EPISTEMIC (specified, not yet implemented).
- **TBD:** Whether the discrepancy between "anticipated 8,036 artifacts" and the realized four-document kits per deliverable (~2,376 production docs across 594 deliverables) reflects the artifact-vs-production-document distinction in `docs/TYPES.md` §1.3 or a coverage shortfall. Likely the former — labelled ASSUMPTION pending verification.

---

## 9. Provenance for this report

- Five `Explore` subagents, read-only, each scope-bounded; all sampling and counts traceable to the file paths cited in the body.
- Numbers may vary slightly across agents because each picked its own stratified package sample within the user-directed discipline-cluster strategy. Where agents diverge (e.g., Agent A's 25-deliverable sample vs Agent B's 30-deliverable sample), both reports are preserved verbatim above and are not silently reconciled. Per K-CONFLICT-1, the user adjudicates.
- No state was mutated. No `_STATUS.md`, `_MEMORY.md`, tool-root, or commit changes were made. Only this report file was created.
