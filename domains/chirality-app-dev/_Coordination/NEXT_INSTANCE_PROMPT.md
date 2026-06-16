# NEXT INSTANCE PROMPT — chirality-app-dev DOMAIN_DECOMP

## Status: Gate 6 ACCEPTED — DOMAIN_DECOMP COMPLETE

**DOMAIN_DECOMP for `chirality-app-dev` is COMPLETE.** All six gates closed and
accepted. **Gate 6 ACCEPTED** (token `GATE6_ACCEPT_20260616`; snapshot
`gate_snapshots/GATE6_PUBLISH_20260616T170027Z/`; `_LATEST_GATE6.md`). Operator
statement: *"This domain decomposition is the accepted basis for downstream work."*

Accepted basis: 11,809 atoms (IN 11,140 / OUT 107 / TBD 562); 16 Categories /
59 KTYs / 279 Subjects; 844 vocabulary terms; 987 cov-empty sections attested
scaffold-for-fill. Final integrity validator **PASS** (0 CRITICAL / 0 MAJOR / 0 MINOR).
Published control surface `Chirality_App_Dev_Domain_Decomposition.md`; authoritative
ledger `Domain_Ledger_Gate4_KTY_Draft.csv` (annex `annex_domain_ledger.csv`);
`Companion_Inventory.csv` (1,707 rows). Objectives omitted by design (Deviation A;
`annex_objectives.csv` header-only). Gate-6 builder: `_adapter/gate6_build_companion_inventory.py`.

**No gate remains open.** Documented deferred caveats carried in the accepted basis
(future scope-change amendments, NOT closure blockers): **OI-011** (corpus drift;
re-atomization deferred), **OI-013** (562 TBD-scope atoms), **OI-012** (catalog-rebuild
chunk_id collision; authorized shared-tool fix). Any amendment to the basis or any
downstream/derivative work requires an explicit scope-change cycle and explicit
authorization. See `gate_snapshots/GATE6_PUBLISH_20260616T170027Z/HANDOFF_STATE.md`.

---
### (prior status retained below)
## Status: Gate 4 ACCEPTED — Gate 5 (Coverage) next

**Gate 4 ACCEPTED** (token `GATE4_ACCEPT_20260616`; snapshot
`gate_snapshots/GATE4_KTY_20260616T161222Z/`). Knowledge-kind KTY axis +
per-deliverable subjects: **59 Knowledge Types, 279 Subjects**
(`Knowledge_Type_Register.csv`, `Knowledge_Subject_Register.csv`). 11,140 IN atoms
each carry one primary KTY + Subject (`Domain_Ledger_Gate4_KTY_Draft.csv`, status
`ACCEPTED_GATE4`, `CoversUnits` populated). Deterministic source-routing
(`_adapter/gate4_assign.py`): CAT-001..011 → 4 doc-kind KTYs each (Datasheet→
Reference/Specification/Guidance/Procedure); CAT-012..016 → content-kind KTYs.
Binding KTY ratification (`_adapter/gate4_ratify.py`, within-category nearest
centroid): **59/59 CLUSTER_COHERENT, 0 blocking**; 49 candidates
RESOLVED_SOURCE_ROUTING (0 open). `IntendedUsers`/`WhenUsed` left `TBD` (persona
allowance). Integrity validator: only `objectives` + `coverage` annexes
outstanding (Gate 5).

**Next: Gate 5 (Coverage)** — section-coverage attestation: verify every IN atom has
exactly one Category (✓) + ≥1 KTY (✓ 100%); build coverage & section-coverage
telemetry (coverage-review HTML; scaffold-for-fill); produce the `coverage` and
`objectives` annexes the integrity validator still wants. Model: self-domain
`domains/chirality/_Decomposition/` Gate-5 artifacts + any `tools/decomp`/`tools/validation`
coverage tooling — verify reusable vs self-domain-specific (author pack-local adapter
if specific, as for Gates 3–4).

---
### (prior status retained below)
## Status: Gate 3 ACCEPTED — Gate 4 (Knowledge Types) next

**Gate 3 ACCEPTED** (token `GATE3_ACCEPT_20260616`; snapshot
`gate_snapshots/GATE3_CATEGORIES_20260616T153015Z/`). 16 flat faithful-to-author
categories `CAT-001..016` (PKG-00..10 preserved 1:1 as CAT-001..011 + 5
cross-cutting: CAT-012 product reqs/arch, CAT-013 dev-process/build/release,
CAT-014 coordination/scope-change gov, CAT-015 decomposition/reconciliation/closure,
CAT-016 frontend source+harness docs). 11,140 IN atoms assigned one Category each
(`Domain_Ledger_Gate3_Category_Draft.csv`, status `ACCEPTED_GATE3`); 562 TBD +
107 OUT uncategorized (TBD deferred, OI-013). Binding dense ratification
(`SRCIDX_20260616T043733Z`, BAAI/bge-base-en-v1.5): **16/16 CLUSTER_COHERENT, 0
blocking**, own-centroid cosine 0.71–0.77; 330 semantic-adjacency misassignment
candidates RESOLVED_SOURCE_ROUTING (0 open). Pack-local adapters
`_adapter/gate3_assign.py` + `_adapter/gate3_ratify.py` (data-driven; re-run in
seconds). Registers: `Category_Register.csv`, `Category_Scope_Ratification.csv`,
`Category_Assignment_Findings.csv`, `Category_Boundary_Decisions.csv`.

> Catalog rebuild note still applies (OI-012): exclude `gate_snapshots/` when
> rebuilding the source DB. Dense embeddings now built into the snapshot.

**Next: Gate 4 (Knowledge Types)** — define `KTY-CC-TT_*` types (within each of the
16 categories) + `SUB-CC-TT-SS_*` subjects; binding retrieval-driven KTY scope
ratification; assign KnowledgeTypeIDs/SubjectIDs onto the ledger (currently
`TBD_GATE4`). Model: self-domain `tools/decomp/propose_gate4_kty.py` (verify if it
is reusable/data-driven or, like refine_gate3_categories.py, self-domain-specific —
if specific, author a pack-local adapter).

---
### (prior status retained below)
## Status: Phase 2.5 COMPLETE — Gate 3 (Categories) next

**Phase 2.5 done** (deterministic): catalog `SRCIDX_20260616T043733Z` (validate
**PASS**; 20,398 chunks; 660 artifacts / 547 source docs), BM25 built
(`--no-embeddings`), TOC priors `_Decomposition/cross_source_toc_matrix.{md,csv}`
(96 sources, 76,933 alignment pairs). Manifest re-stamped to live HEAD — SHA-256
`e9000e97e04b2e913a3ea70d421765350456ffcde4e8fd20e12d1cf963d6e491` (467 rows; 319
`IncludeInIndex=YES`, all markdown). New issues: **OI-010** (frontend/src code +
docs/MANIFEST.json → index-metadata-only; code covered via grouped-unit atoms),
**OI-011** (corpus drift to merge `bcb74dc09`; 22 files re-stamped, re-atomization
+ new-file admission DEFERRED to a scope-change pass before Gate 6), **OI-012**
(latent catalog-rebuild collision — exclude `gate_snapshots/` when rebuilding the
catalog). Snapshot `gate_snapshots/PHASE2_5_20260616T044500Z/` (+ `_LATEST_PHASE2_5.md`).
**Next: Gate 3 (Categories)** — flat categories reconciled from the TOC matrix +
retrieval; binding scope ratification + per-atom misassignment check.

> NOTE for any catalog rebuild: gate snapshots embed ledger/section-node CSVs that
> collide on `chunk_id`. Move `_Decomposition/gate_snapshots/` aside during
> `build_source_database.py`, then restore (see OI-012).

---
### (prior status retained below)
## Status: Gate 2 ACCEPTED — Phase 2.5 (source catalog + retrieval) next

Gate 1 RE-ACCEPTED + Gate 1.5-S CLOSED + **Phase 2 COMPLETE**: 96 source units
atomized via individual-agent fan-out (≤20 parallel, staged by group) →
`_Decomposition/Atomic_Domain_Ledger.csv` (11,809 atoms; IN 11,140 / TBD 562 /
OUT 107; 0 hash mismatches, 0 dup IDs, 0 unresolved Corrects) +
`Vocabulary_Map.csv` (844 terms). 96 atom-review HTMLs under
`_Decomposition/atom_review_html/<batch>/`. Snapshot
`gate_snapshots/PHASE2_20260616T033617Z/`. **Gate 2 ACCEPTED**
(token `GATE2_ACCEPT_20260616`). **Next: Phase 2.5** (deterministic, no gate):
`tools/source_catalog/build_source_database.py --repo-root projects/chirality-app-dev`
→ then BM25 via `tools/retrieval/build_source_index.py` (`--no-embeddings`) →
`tools/decomp/build_toc_priors.py` → `cross_source_toc_matrix.{md,csv}`; then Gate 3 (Categories).

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
