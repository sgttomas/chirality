# Gate 2 (Normalize) — fan-out progress checkpoint

Persona: **DOMAIN_DECOMP**. Decomposing `projects/chirality-piping/` into `domains/chirality-piping/`.
Batch namespace: **`V1`** (all groups). Worker = `domain-source-atomize` via Agent (general-purpose), **max 22 concurrent**.

## Gates
- Gate 1 (Intake): ✅ confirmed. 158 source units, 5,031 sections, 204 dispatch units, 38 index-only (schemas).
- Gate 1.5 (Skeleton review): ✅ confirmed. 4,920 in-scope sections (111 `# Source Pack` boilerplate trimmed). Asset/prose sub-gates N/A (no extracted assets).
- Gate 2 (Normalize): **FAN-OUT COMPLETE — awaiting Gate 2 confirmation.**

## Gate 2 fan-out status (groups) — ALL MERGED, QA CLEAN (qa_problems=0)
| Group | Units | Dispatch | Status | Atoms (IN/OUT/TBD) |
|---|--:|--:|---|---|
| ROOT_DOCS | 3 | 3 | ✅ done, merged, QA clean | 127 (125/0/2) |
| PRODUCT_DOCS | 44 | 44 | ✅ done, merged, QA clean | 3562 (3443/26/93) |
| EXECUTION_GOVERNANCE | 5 | 6 | ✅ done, merged, QA clean | 400 (379/4/17) |
| EXECUTION_DELIVERABLE | 101 | 101 | ✅ done, merged, QA clean | 10810 (10339/85/386) |
| CODE_CORE | 1 | 18 | ✅ done, merged, QA clean | 2801 (2783/17/1) |
| CODE_APPS | 1 | 21 | ✅ done, merged, QA clean | 2592 (2571/15/6) |
| CODE_TESTS | 1 | 5 | ✅ done, merged, QA clean | 883 (883/0/0) |
| CODE_TOOLS | 1 | 1 | ✅ done, merged, QA clean | 81 (81/0/0) |
| CODE_VALIDATION | 1 | 5 | ✅ done, merged, QA clean | 564 (560/0/4) |

**Cross-source merge complete:** `Atomic_Domain_Ledger.csv` = **21,818 atoms** (IN 21,163 / OUT 146 / TBD 509),
158 source units, 204 dispatch units, 0 ID-prefix collisions, 0 unresolved Corrects, all AtomicUnitIDs unique
(`HBA-<PREFIX>-NNNNN`). **Vocabulary consolidation complete:** `Vocabulary_Map.csv` = 1,809 candidate terms
(336 multi-source). Per-source atom-review HTML rendered under `_Decomposition/atom_review_html/V1/`.

Notes: one QA fix applied — `UNIT-CA001-0001` seq1 (a pack `## Component:` boilerplate header atom citing `L-1`,
below the component source range) was dropped and the unit renumbered, matching how other workers omit
unmappable component-header lines; CODE_APPS re-merged clean (2592 atoms).

## REFRESH COMPLETE — V2 re-atomization after dependency/typed-system refresh (2026-06-16)
The operator's dependency refresh landed (commits `28219696d` "deps: refresh dependency registers and
lifecycle status" + `8e8819e94` postmerge validation). Impact was surgically bounded and re-atomized:

- **Detection:** `detect_source_delta.py` flagged 6 source units (7 admitted components changed); a manifest
  rebuild also surfaced **2 newly-admitted files** under `tools/coordination/`
  (`dependency_semantic_refresh_fanin.py`, `dependency_type_rectification.py`) that folded into the existing
  grouped `SRC-CODE-TOOLS` unit. Of 541 changed/added repo files, only 7 were admitted (all the deliverable
  `_DEPENDENCIES.md`/`Dependencies.csv`/`MEMORY.md`/`_STATUS.md`/`_run_records` edits are EXCLUDED → 0 atoms).
- **NOTE for operator:** `docs/TYPES.md` DID change (+`## 5.1 Dependency-register vocabulary`, 4 lines) and
  `docs/SPEC.md` gained `### 3.0 Dependency-register type system` — contrary to the "TYPES.md unchanged"
  expectation. Both look intentional (they document the new typed vocabulary) and were re-atomized accordingly.
- **Re-sync:** `build_manifest.py` → `run_intake.py` → `review_15s.py` regenerated manifest SHAs, base
  skeletons, registers, pack markdown (CODE-TOOLS now 7 components), and reviewed overlays. Invariants held:
  158 units, prefixes 100% stable, 0 skeleton failures, 111 boilerplate sections trimmed (Gate 1.5 parity),
  in-scope sections 4920→4924. `detect_source_delta.py` re-verified clean (846 components, 0 changed).
- **V2 re-atomization** (batch `V2`, `phase2_run/phase2_merge` extended with a `--units` filter): the 6 changed
  units only, 1 dispatch unit each, all SUCCESS, qa_problems=0, missing=[]. New atoms: SRC-AGENTS 57→62,
  SRC-DOCS-PLAN 64→65, SRC-DOCS-README 36→38, SRC-DOCS-SPEC 254→278, SRC-DOCS-TYPES 139→149,
  SRC-CODE-TOOLS 81→133.
- **Rebuilt ledger** (V2 for the 6 changed units, V1 for the other 152): `Atomic_Domain_Ledger.csv` =
  **21,912 atoms** (IN 21,256 / OUT 147 / TBD 509), 158 source units, 204 dispatch units, all AtomicUnitIDs
  unique, 0 unresolved Corrects. Unchanged-unit atom subtotal identical (21,187 → 21,187): no collateral churn.
  DAG-token atoms 160 → 179 (+19, the new typed-dependency references). `Vocabulary_Map.csv` = 1,812 terms.
  V2 per-source ledgers in `per_source_ledgers/V2/`; V2 atom-review HTML in `atom_review_html/V2/`.

**Status: Gate 2 refreshed baseline frozen — awaiting Gate 2 confirmation, then Gate 3.**

## (historical) PARKED before Gate 3 — pending operator dependency/DAG refresh (operator decision 2026-06-16)
Operator is refreshing deliverable dependencies to the canonical typed system in root `docs/TYPES.md`
(TYPES.md itself unchanged), then updating the execution DAG. Decision: **refresh the source repo FIRST,
then re-atomize only the changed source units before starting Gate 3** (so Categories/Knowledge-Types are
built on final text). Gate 2 V1 ledger stands as the baseline. Do NOT start Gate 3 until the refresh lands
and the affected units are re-atomized + re-merged.

Impact scope (measured against `Atomic_Domain_Ledger.csv`): `_DEPENDENCIES.md` and `execution/_DAG/` are
EXCLUDED (0 manifest rows) so editing them alone changes no atoms. But DAG identifiers leaked into admitted
sources by reference: **160 atoms carry a `DAG-NNN` token across 49 source units** (116×DAG-006 version/authority
stamps, ~20 typed `DAG-002-E####` edge rows in deliverable Prerequisite/Verification lines, rest 001/005/007).
TYPES.md is clean (1 incidental atom). Rewriting deliverable prerequisite/interface lines to the typed form
changes those source KT-docs → their atoms change at source.

### Resume procedure after the refresh lands
1. Re-hash detection: `python3 domains/chirality-piping/_Decomposition/_adapter/detect_source_delta.py`
   → prints `affected_source_units` + `affected_groups` (recomputes SHA-256 of all 844 admitted components vs
   `Source_Unit_Component_Map.csv` `ComponentSha256`; CHANGED/MISSING flag the owning SourceUnitID). Verified
   clean (0 changed) on 2026-06-16 against the pre-refresh repo.
2. If new/removed admitted files: re-run `build_manifest.py` then `run_intake.py` + `review_15s.py` for the
   touched units to regenerate skeletons/briefs (pack markdown + component map must reflect the new text).
   For pure in-place edits, regenerate the affected units' briefs only.
3. Re-atomize the affected units in a fresh batch (e.g. `V2`): `phase2_run.py V2 <GROUP>` → dispatch workers for
   ONLY the changed units (same WORKER PROMPT below, ≤22 concurrent) → `phase2_merge.py V2 <GROUP>` (qa_problems=0).
4. Rebuild the consolidated ledger: re-run the cross-source merge over the refreshed per-source ledgers
   (changed units take their V2 ledger, unchanged units keep V1) → regenerate `Atomic_Domain_Ledger.csv` and
   `Vocabulary_Map.csv`. Then present the refreshed Gate 2 ledger and proceed to Gate 3 on operator approval.

## How to run each remaining group (cwd = monorepo root /Users/ryan/ai-env/projects/chirality)
1. Generate briefs: `python3 domains/chirality-piping/_Decomposition/_adapter/phase2_run.py V1 <GROUP>`
   - prints JSON manifest with per-dispatch-unit `unit_id` + `brief_path` (relative to pack root).
2. Dispatch one Agent (subagent_type general-purpose) per dispatch unit, ≤22 concurrent. Worker prompt:
   - Read skill spec: `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/{SKILL.md,BRIEF_SCHEMA.md,QA_CHECKS.md}`.
   - Execute brief at `/Users/ryan/ai-env/projects/chirality/domains/chirality-piping/<brief_path>`.
   - Read ONLY lines LINE_START..LINE_END of MD_PATH. Write the two CSVs (atoms + vocab) to the brief's exact AllowedWriteTargets USING A PYTHON SCRIPT (csv+hashlib).
   - Ledger header EXACTLY: `LocalSeq,UnitStatement,SourceRef,ContentHash,InOutStatus,SectionID,DispatchUnitID,Corrects,Notes`. ContentHash=sha1(UnitStatement)[:12]. LocalSeq from 1. SectionID ∈ TARGET_SECTION_IDS; evidence line ∈ [LINE_START,LINE_END]. SourceRef dual via SOURCE_REF_BASE. InOutStatus∈{IN,OUT,TBD}. No invention (AOP-08).
   - NOTE: grouped CODE/GOVERNANCE/DELIVERABLE units use SOURCE_REF_MODE=COMPONENT_MAP — worker maps generated pack-md line back to @repo component file via ASSET_MANIFEST_PATH source_components.
3. Merge + QA: `python3 domains/chirality-piping/_Decomposition/_adapter/phase2_merge.py V1 <GROUP>` → expect qa_problems=0, missing=[]. Re-dispatch any FAILED/missing unit in isolation.

## After all groups merged — cross-source merge + vocab consolidation, then Gate 2 review
- Cross-source merge: `tools/decomp/merge_source_atomizations.py cross-source --per-source <each per_source_ledgers/V1/*_atomic_units.csv> --output domains/chirality-piping/_Decomposition/Atomic_Domain_Ledger.csv`
- Vocab: `tools/decomp/merge_vocabulary_seeds.py` over per-source vocab seeds → Vocabulary_Map.csv (per-source seeds = concat of dispatch_outputs/V1/<uid>/*_vocab.csv).
- Then present consolidated Domain Ledger for Gate 2 confirmation (drain TBD/flagged via browser atom-review HTML).

## Adapter scripts (pack-local)
`domains/chirality-piping/_Decomposition/_adapter/`: build_manifest.py, run_intake.py, review_15s.py, finalize_gate1.py, phase2_run.py, phase2_merge.py, brief_source_ref_map.csv (alias map), GATE2_PROGRESS.md (this file).
Gate 3-6 adapter scripts can be adapted from `domains/chirality-app-dev/_Decomposition/_adapter/` (gate3_assign.py, gate3_ratify.py, gate4_assign.py, gate4_ratify.py, gate5_classify_coverage.py, gate5_make_source_register.py, gate6_build_companion_inventory.py).
