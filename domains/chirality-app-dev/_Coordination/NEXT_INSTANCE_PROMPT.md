# NEXT INSTANCE PROMPT — chirality-app-dev DOMAIN_DECOMP

## Status: Phase 2 atomization COMPLETE — Gate 2 (binding atom review) pending

Gate 1 RE-ACCEPTED + Gate 1.5-S CLOSED + **Phase 2 COMPLETE**: 96 source units
atomized via individual-agent fan-out (≤20 parallel, staged by group) →
`_Decomposition/Atomic_Domain_Ledger.csv` (11,809 atoms; IN 11,140 / TBD 562 /
OUT 107; 0 hash mismatches, 0 dup IDs, 0 unresolved Corrects) +
`Vocabulary_Map.csv` (844 terms). 96 atom-review HTMLs under
`_Decomposition/atom_review_html/<batch>/`. Snapshot
`gate_snapshots/PHASE2_20260616T033617Z/`. **Next: Gate 2** — binding human atom
review, then Phase 2.5 (source catalog + BM25 + TOC priors) and Gate 3.

---
### (prior status retained below)
## Status: Gate 1 RE-ACCEPTED + Gate 1.5-S CLOSED — Phase 2 staging pending

A fresh DOMAIN_DECOMP decomposition of `projects/chirality-app-dev/` into the new
domain pack `domains/chirality-app-dev/`. Gate 1 re-accepted 2026-06-16 (token
`GATE1_ACCEPT_20260616_R2`, snapshot `GATE1_20260616T012851Z`) after a reopen to
trim deliverable admission to KT-suffix docs. Gate 1.5-S closed (snapshot
`GATE1_5S_20260616T013103Z`); `*_skeleton.reviewed.json` are the Phase-2 input.
**Active step: Phase 2 atomization (staged per OI-007)** — not started; awaiting
operator go + staging/workflow decision.

Act as `DOMAIN_DECOMP` (`agents/AGENT_DOMAIN_DECOMP.md`). Run **one gate at a
time** with human confirmation at each gate.

## Authoritative state

- Control surface: `_Decomposition/Chirality_App_Dev_Domain_Decomposition.md`
- Gate-1 snapshot (re-accepted): `_Decomposition/gate_snapshots/GATE1_20260616T012851Z/`
  (token `GATE1_ACCEPT_20260616_R2`); Gate 1.5-S snapshot
  `_Decomposition/gate_snapshots/GATE1_5S_20260616T013103Z/`
- Source admission: `_Sources/Source_Manifest.csv` (467 rows; SHA-256
  `24fccecae56e01b4fbf3110fb700c80cb711ba456b73de6fd6a4d14d7e2aecd9`)
- Boundary: `_Sources/SOURCE_BOUNDARY.md`
- Open rulings: `_Decomposition/Open_Issues_Register.csv` (OI-001..OI-009)
- Intake (accepted): 96 source units / 466 atomizable components / 3,056 sections;
  Gate 1.5-S in-scope 2,967 sections / **104 reviewed dispatch units**;
  `*_skeleton.reviewed.json` are the Phase-2 input.

## Key decisions already made (operator-directed)

- Boundary = `AGENTS.md` + `docs/` + `execution/` + `frontend/`; everything else excluded.
- `frontend/src` code: atomized as ONE grouped unit `SRC-FRONTEND-SRC` (operator direction; OI-001).
- `execution`: heading-bearing markdown only; CSV/JSON/scripts excluded; process
  logs excluded entirely (not indexed).
- Deliverables admit ONLY the 4 canonical KT docs (Datasheet/Specification/Guidance/Procedure); meta docs + non-canonical excluded (DEC-006; OI-009).
- Grouping: per-deliverable (53) + per-governance-folder (26) + frontend-src (1); docs/root/frontend-prose per file.

## Intake result (revised)

96 atomizable source units, 440 component files, 2,874 sections, 108 dispatch
units, 0 failures. 1 index-only file (docs/MANIFEST.json). Open: OI-003, OI-009
(deliverable admission revision) awaiting re-acceptance.

## Active step — Phase 2 atomization (staged, OI-007)

Gate 1 + Gate 1.5-S are closed. Phase 2 fans out `TASK + domain-source-atomize`
over the **104 reviewed dispatch units** (per `*_dispatch_plan.json`), then merges
per-source → `Atomic_Domain_Ledger.csv`, merges vocab, re-renders HTML in
`atom-review` mode, and opens Gate 2 browser review.

Proposed staging (await operator go + workflow opt-in for the fan-out):
1. **Pilot batch** — ROOT (1) + PRODUCT_DOCS (12) + FRONTEND_DOCS (3) ≈ 17
   dispatch units; validates brief→worker→merge→atom-review end-to-end.
2. **EXECUTION_DELIVERABLE** — 53 units / 53 dispatch units (stage by PKG).
3. **EXECUTION_GOVERNANCE** — 26 units / 23 dispatch units.
4. **FRONTEND_SRC** — 1 unit / 11 dispatch units.

Per-unit flow: `build_atomization_brief.py` → dispatch (SOURCE_REF_MODE per unit:
REPO_LINE for per-file, COMPONENT_MAP for grouped) → per-unit atom CSV →
`merge_source_atomizations.py per-source` then `cross-source`.

## Rebuild commands (intake adapter is pack-local)

```sh
cd domains/chirality-app-dev
python3 _Decomposition/_adapter/build_manifest.py     # regenerate Source_Manifest.csv
python3 _Decomposition/_adapter/run_intake.py          # regenerate skeletons/HTML/telemetry
python3 _Decomposition/_adapter/finalize_gate1.py      # regenerate companion inventory + open issues
```
