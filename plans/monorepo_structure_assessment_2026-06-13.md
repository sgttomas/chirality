# Chirality Monorepo Structure Assessment

Date: 2026-06-13

Repository root: `/Users/ryan/ai-env/projects/chirality`

Report status: planning assessment. This report is descriptive and advisory. It does not supersede governed authority documents such as `docs/PLAN.md`, project decomposition records, accepted snapshots, or handoff states.

## Executive Summary

This repository is a private canonical monorepo for Chirality, a filesystem-native agent operating system for deliverable-heavy professional work. Its central architecture is not a service mesh or application backend. It is a state-and-authority system: project truth is stored in versioned files, agent behavior is governed by instruction contracts, deterministic tools perform repeatable operations, and humans retain binding decision authority.

The repo has four major structural layers:

1. Shared Chirality operating-system surface: `AGENTS.md`, `agents/`, `docs/`, `skills/`, `tools/`, `frontend/`, `examples/`, and `init/`.
2. Public export surface: `exports/chirality-app/`, an allowlist-based profile that stages a sanitized public `chirality-app` package.
3. Private product/project workspaces: `projects/chirality-app-dev/` for future Chirality App development and `projects/chirality-piping/` for OpenPipeStress.
4. Private domain/source workspace: `domains/piping-design/`, a large domain pack containing source extraction, audit, asset, and decomposition material for piping-design knowledge.

The tracked repository currently contains 40,650 files. The tracked footprint is dominated by domain extraction artifacts (`domains/`, 29,514 tracked files), private project workspaces (`projects/`, 5,477), and public examples (`examples/`, 5,055). The raw local filesystem is much larger because private workspaces include dependency folders, build products, caches, and generated export staging trees; tracked-file counts are the better structural baseline.

The most salient strength is architectural consistency: the same concepts recur across the repo - stable IDs, flat package/deliverable decomposition, explicit write scopes, provenance, immutable snapshots, handoff states, and human gates. The main structural risk is registry drift across narrative documents, live agent files, skills, and tool registry entries. The repo already acknowledges that live registries should govern when narrative lists disagree, but several concrete inconsistencies are visible and should be retired or reconciled.

## Scope And Method

Assessment scope covered the whole repository at `/Users/ryan/ai-env/projects/chirality`, with emphasis on monorepo structure, authority surfaces, subprojects, domain workspaces, export boundaries, validation surfaces, and known structural risks.

Local commands run:

- `git ls-files` inventory by top-level path and extension.
- `python3 tools/validation/validate_skill_metadata.py skills`.
- `python3 tools/validation/discover_test_surfaces.py . --text`.
- Read-only inspections of root governance docs, live agent/skill/tool registries, project docs, project manifests, domain pack metadata, frontend manifests, export tooling, and example workspace layouts.

Subagents were used for read-only fan-out:

- Governance explorer: `agents/`, root `docs/`, `skills/`, `tools/`.
- Product/project explorer: `projects/chirality-app-dev/`, `projects/chirality-piping/`.
- Domain/export/frontend explorer: `domains/`, `examples/`, `exports/`, `frontend/`, `init/`, root metadata.

No project files outside this report were intentionally modified. The working tree already had unrelated local changes under `projects/chirality-app-dev/init/` and `projects/chirality-piping/init/`; those were left untouched.

## Inventory Baseline

Tracked files by top-level path:

| Path | Tracked files | Structural role |
|---|---:|---|
| `domains/` | 29,514 | Private domain pack and source extraction workspace |
| `projects/` | 5,477 | Private product and project workspaces |
| `examples/` | 5,055 | Public-exported example execution workspaces |
| `tools/` | 232 | Deterministic helper and validation layer |
| `skills/` | 153 | Repo-native TASK method packs |
| `frontend/` | 83 | Public-exported Next/Electron harness snapshot |
| `plans/` | 52 | Non-governing planning workspace |
| `agents/` | 37 | Live agent instruction files |
| `docs/` | 31 | Root governance, specification, roadmap, and design-basis docs |
| `exports/` | 5 | Public export profile and reports; generated staging is ignored |
| `.github/` | 2 | Release and harness validation workflow templates |
| `init/` | 1 | Bootstrap/next-session surface |
| Root docs/config | 9 | `README.md`, `INIT.md`, `AGENTS.md`, framework/professional docs, license, gitignore, Claude guidance |

Tracked files by major extension:

| Extension | Tracked files | Interpretation |
|---|---:|---|
| `.md` | 21,968 | Governed prose, source extraction pages, deliverables, reports, docs |
| `.json` | 14,755 | Schemas, manifests, source assets, fixtures, tool outputs |
| `.csv` | 1,561 | Ledgers, registers, decomposition, dependency and audit data |
| `.xlsx` | 1,269 | Materialized table assets and spreadsheet artifacts |
| `.py` | 350 | Deterministic tools and Python project code |
| `.ts` | 158 | Frontend/runtime TypeScript |
| `.tsx` | 91 | React UI surfaces |
| `.rs` | 42 | Rust mechanics, solver, serialization, reporting, and Tauri support |

Live registry counts:

| Surface | Count | Notes |
|---|---:|---|
| `agents/AGENT_*.md` | 37 | Indexed by `AGENTS.md` |
| `skills/*/SKILL.md` | 37 | All passed `validate_skill_metadata.py` |
| `tools/` files | 256 local files | 232 tracked files; includes tests and helper modules |
| Deterministic test surfaces | 5 | 195 test files, 1,840 discovered test symbols |

## Architectural Layers

### 1. Root Governance And Framing

Root files define the repo's identity and authority model:

- `README.md` describes this as the private canonical source tree for Chirality and distinguishes public export, private projects, domains, plans, and archives.
- `INIT.md` gives the maintainer/operator orientation order and names the authoritative governance documents.
- `AGENTS.md` indexes the agent suite, agent matrix, task-skill dispatch relationships, and governance integration rules.
- `CHIRALITY_FRAMEWORK.md` supplies the theory of professional accountability: claims, warrants, accountable humans, and the four pillars.
- `PROFESSIONAL_ENGINEERING.md` supplies the professional practice and responsibility frame.
- `CLAUDE.md` gives Claude Code specific orientation and validation commands.

The governing doctrine is stable and repeated across root docs:

- Filesystem state is project truth.
- Git is the audit/event substrate.
- Agents propose, extract, draft, reconcile, and audit.
- Humans approve, adjudicate, authenticate, and accept residual risk.
- Unknowns become `TBD`.
- Claims require provenance.
- Conflicts are surfaced rather than silently resolved.
- Phase-boundary or closure work terminates in immutable snapshots and explicit handoff state where applicable.

### 2. Governance Documents

Root `docs/` is the authoritative Chirality-wide governance layer:

- `docs/DIRECTIVE.md`: founding intent, four-pillar philosophy, human authority, evidence over plausibility, instruction/execution separation.
- `docs/SPEC.md`: physical filesystem structures, package and deliverable layouts, required files, tool roots, lifecycle state, file formats, schemas, and agent instruction structure.
- `docs/TYPES.md`: canonical vocabulary, stable identifiers, enums, agent roles, lifecycle states, coordination representations, and epistemic ontology terms.
- `docs/CONTRACT.md`: 21 stable K-* invariants across hierarchy, identity, authority, sealing, dependencies, status, staleness, gates, merge/publication, provenance, write scope, and snapshots.
- `docs/PLAN.md`: active roadmap. It states the current architecture direction: `TASK` as canonical Type 2 shell, method logic in skills, deterministic steps in tools, and Type 1 personas for human-facing orchestration.
- `docs/DBM_Agent_Instruction_Architecture.md`, `docs/SE_Design_Analysis.md`, and `docs/thesis/`: deeper design basis and systems-engineering rationale.

The docs layer is unusually central. It is not incidental documentation for code; it is the normative substrate that tells agents, tools, and human operators what counts as valid state and valid authority.

### 3. Agent Instruction Layer

`agents/` contains 37 live `AGENT_*.md` instruction files. `AGENTS.md` indexes them into three types:

- Type 0 canonical standards: `HELPS_HUMANS`, `DECOMP_BASE`.
- Type 1 interactive personas: orchestration, decomposition, change, reconciliation, publishing, review, domain, scheduling, tool/skill governance, and similar manager roles.
- Type 2 bounded task agents: `TASK`, `PREPARATION`, `AGGREGATION`, audits, evaluation tasks, domain hypergraph generation, and compatibility shells.

The most important architectural shift is that `TASK` is now the canonical Type 2 shell. It normalizes an `INIT-TASK` brief, resolves scope, loads an optional `TaskSkill`, applies a hard write boundary, creates run records, and refuses implicit write authority from convenience fields such as `ScopePath`, `DeliverablePath`, or deprecated `TaskProfile` labels.

The agent matrix in `AGENTS.md` is both a routing view and a governance grammar:

- Normative row: defines rules and standards.
- Operative row: performs bounded task execution.
- Evaluative row: audits, reconciles, judges, and publishes.

This matches the broader Chirality pattern: rule-setting, execution, and judgment are separated but linked through explicit handoff and closure rules.

### 4. Skill Layer

`skills/` contains 37 live repo-native method packs. Each skill folder is expected to contain:

- `SKILL.md`
- `BRIEF_SCHEMA.md`
- `TOOL_POLICY.md`
- `QA_CHECKS.md`

The live folder rule is explicit: every immediate `skills/*/SKILL.md` folder is a skill; static narrative lists are not authoritative if they drift. The skill validator confirmed `37 valid, 0 invalid, 37 checked`.

Skills do not grant authority. They supply method, outputs, QA, runtime options, and preferred tools to `TASK`. The dispatch model is:

```text
narrative/persona intent -> Type 1 dispatcher -> TASK brief -> TASK shell -> TaskSkill -> allowed deterministic tools -> bounded output/run record
```

Skill families currently include:

- Project deliverable production and consistency: `four-documents`, `dependency-extract`, `semantic-matrix-build`, `semantic-lensing`, `lens-register`, `deliverable-consistency`, `content-digest`, `proposal-format`.
- PDF, equation, drawing, and P&ID extraction: `pdf2md*`, `equation-*`, `drawing-*`, `pandid-*`.
- Domain decomposition and publication: `domain-source-atomize`, `domain-documents`, `domain-prose-validate`, `dbm-*`, `decomposition-package-review`, `kty-*`.
- Estimating and equipment extraction: `estimate-prep`, `estimate-snapshot`, `equipment-extract`, `equipment-costing-extract`.
- Scope/change support: `scope-change-packet`, `scc-resolution-case`.

### 5. Deterministic Tool Layer

`tools/` is the LLM-independent execution layer. `tools/REGISTRY.md` is the curated tool contract surface, and the directory tree groups helpers by purpose:

- `scaffolding/`: package, deliverable, tool-root, snapshot, pointer, and status file creation.
- `validation/`: enum, ID, dependency schema, deliverable consistency, skill metadata, test discovery, semantic validators, domain integrity, KTY remediation, and related checks.
- `coordination/`: dependency closure, DAG audits, supersession maps, local dependency materialization.
- `pdf2md/`: rasterization, per-page brief rendering, asset materialization, folio extraction, markdown assembly, asset validation, XLSX rendering.
- `equation_audit/`: equation audit migration, schema validation, brief rendering, backcheck processing, crops, snapshot pruning.
- `drawing_extract/`: target-aware drawing stubs, titleblock/equipment/valve workflows, validation, crop preparation, reconciliation.
- `decomp/`: source skeletons, atomization briefs, vocabulary seed merge, source HTML review surfaces.
- `publication/`: section map, context packets, dispatch briefs, publication assembly, source supersession and concordance checks.
- `source_audit/`, `source_catalog/`, `retrieval/`: source review surfaces, source database snapshots, and retrieval indexes.
- `reporting/`, `evaluation/`, `review/`, `query/`, `release/`, `pipe_specs/`, `diagnostics/`: project reporting, evaluation, release readiness, extraction, and query helpers.

The tool layer follows the correct separation: deterministic scripts implement repeatable transformations and validators; any LLM judgment is expected to live in skills or agent instructions, not inside tools.

### 6. Frontend Harness Snapshot

The root `frontend/` is a public-exported Next/Electron harness snapshot, not the long-term private app-development source. It uses:

- Next 16.1.6
- React 19.2.3
- Electron 33.3.1
- TypeScript
- Claude agent SDK dependency

Important structure:

- `frontend/app/`: Next app entrypoint.
- `frontend/components/`: workbench, pipeline, toolkit, file tree, settings, and layout components.
- `frontend/lib/harness/`: agent SDK manager, session manager, persona manager, attachment resolver, instruction-root handling, logging, defaults, and types.
- `frontend/electron/`: desktop shell, preload, signing/notarization config, icons, entitlements.
- `frontend/scripts/`: harness validation wrappers.
- `frontend/docs/harness/`: harness decisions, validation, CI integration, artifact mirroring, and implementation notes.

Electron packaging explicitly bundles root `agents/`, `skills/`, `tools/`, `docs/`, `init/`, and selected root files into `instruction-root/`. This physically implements the instruction-root/working-root split: release-managed instructions are packaged with the app, while user project roots remain selected writable workspaces.

### 7. Public Export Profile

`exports/chirality-app/` is the profile that builds a sanitized public `chirality-app` tree. The tracked source surface is small:

- `README.md`
- `export_public.py`
- `export-manifest.csv`
- `export-report.md`
- `staging/.gitignore`

The generated `exports/chirality-app/staging/` tree exists locally but is ignored and should not be treated as source truth. The export script:

- copies allowlisted root files and directories;
- excludes private roots such as `.archive/`, `projects/`, `domains/`, `plans/`, and `exports/`;
- skips dependency/build/cache folders, source corpora, local indexes, environment files, and private runtime state;
- sanitizes private absolute paths in text files;
- writes a manifest and report;
- fails boundary checks for forbidden paths, forbidden files, or private absolute path leaks.

This is an important boundary-control mechanism because private workspaces and domain corpora contain many pathful, generated, or sensitive-local artifacts.

### 8. Public Examples

`examples/` is a public-exported corpus of governed execution workspaces. It is not sample code. It demonstrates the Chirality filesystem model at scale:

- `examples/AB-2026-01424-WDMLRL-2026-Claude/`: 21-package execution example.
- `examples/execution-6a/`: 6-package execution example.
- `examples/execution-6b/`: 10-package execution example.
- `examples/execution-6c/`: 9-package execution example.
- `examples/_PriceSources/`: shared estimating price sources.

Common structures include:

- `PKG-*` package folders.
- `1_Working/DEL-*` deliverable folders.
- Four-document kits and metadata files.
- `_Aggregation/`, `_Decomposition/`, `_Estimates/`, `_Reconciliation/`, `_ScopeChange/`, `_Sources/`, `_Evaluation/`, and `_PriceSources/` tool roots.

These examples are valuable because they materialize the abstract governance model as realistic package/deliverable state, estimates, reconciliation outputs, audits, and source references.

### 9. Private Project Workspaces

`projects/` contains private non-exported workspaces. The two live project workspaces are structurally different but both use the Chirality filesystem governance model.

#### `projects/chirality-app-dev/`

This is the private development workspace for the future Chirality App path. It is larger and more active than root `frontend/`.

Key features:

- Project-local docs define product requirements, runtime contract, instruction-root/working-root separation, permission boundary, audit model, and fallback path.
- Execution tree contains product packages plus a `PKG-00_DAG_Closure_and_Project_Control` meta/control package.
- Active decomposition reportedly describes 10 product packages, 51 deliverables, and 78 scope items.
- Coordination is tranche-based and app-integration oriented.
- Executable product source lives mainly under `projects/chirality-app-dev/frontend/`.
- The app-dev frontend contains source, harness runtime abstractions, validation docs, tests, build artifacts, and dependency folders.

Structural status:

- App-dev inherits root `AGENTS.md`; it does not have its own project-local `AGENTS.md`.
- Latest dependency-closure state is documented as cyclic, so project-wide blocked/unblocked claims should remain qualified.
- There is path drift in at least one plan reference to a harness runtime doc location.
- A required companion invariant coverage register is referenced by decomposition notes but was not found during read-only inspection.

#### `projects/chirality-piping/`

This is the OpenPipeStress project workspace. It is both a governed execution project and an actual software product tree.

Project stance: "Open the mechanics; protect the standards; empower the engineer."

Key features:

- Project-local `AGENTS.md` overlays the Chirality agent framework for OpenPipeStress.
- Project docs define product intent, PRD, professional boundary, IP/data policy, technical spec, release quality gates, build/release, security, architecture, validation strategy, user/developer/contributor guides.
- `execution/` contains 18 packages and reportedly 101 deliverables, with package-level roots for aggregation, change, coordination, DAG, decomposition, evaluation, reconciliation, and scope change.
- `schemas/` is a major contract surface for models, units, materials, components, rule packs, reports, persistence, handoff, analysis, comparison, external prover metadata, exports, and adapters.
- `core/` contains Python services plus many Rust crates for units, physics, loads, solver, rules, reporting, serialization, runners, model operations, and GUI support.
- `apps/desktop/` is a Vite/React/Tauri desktop application with Vitest and Playwright coverage.
- `fixtures/` contains invented or cleared contract fixtures.
- `validation/` contains benchmarks, hand calculations, witness/evidence assets, and validation evidence.
- `tests/` contains Python project tests.

Structural status:

- The authoritative decomposition reportedly has 18 packages, 101 deliverables, 76 scope items, and 17 open issues.
- DAG authority points to a `_LATEST.md` pointer under `execution/_DAG/`.
- Execution state was reported as 100 deliverables in `CHECKING` and 1 in `ISSUED`.
- OpenPipeStress docs warn that downstream surfaces may be stale relative to rev 0.7 until refreshed by owning workflows.
- Release-impacting `TBD`s remain around tolerances, solver choices, rule grammar, approval workflow, migration, comparison tolerances, handoff coverage, and CAEPIPE clarifications.

### 10. Private Domain Pack

`domains/piping-design/` is a private/manual domain pack. Its `domain-pack.yaml` declares:

- shared canonical roots: root `agents`, `skills`, `tools`;
- local roots: `_Sources`, `_Decomposition`, `_Coordination`, `vocabularies`.

The domain pack is dominated by `_Sources/`, with multiple extracted piping-design sources, per-page Markdown, page folios, asset manifests, tables, image/figure/table assets, equation audit outputs, source review HTML surfaces, and proof-case decomposition artifacts.

Key source families visible during inspection include:

- `MWK_1956`
- `Pipe-Stress-Engineering`
- `Piping_Manual`
- `Process-Piping-Design-Rip-Weaver-Volume-1`
- `Process-Piping-Design-Rip-Weaver-Volume-2`
- `industry-practices`

The domain structure is tightly coupled to the PDF2MD, equation-audit, source-audit, domain-decomposition, source-catalog, retrieval, and DBM publication tools. It represents domain knowledge work in progress rather than public app surface.

### 11. Plans And Archives

`plans/` is explicitly non-governing unless a plan declares active scope, owner, status, and transition path. It contains active planning seeds and historical imported plans. It should be used for working assessments like this report, not as a replacement for `docs/PLAN.md` or accepted project snapshots.

`.archive/` and project-local `.archive/` folders contain historical migration, retired plan, and prior execution material. They are useful context but not live registry or current topology.

### 12. CI And Validation

Root `.github/workflows/` contains:

- `desktop-release-template.yml`: macOS and Windows desktop build/release template for root `frontend/`.
- `harness-premerge.yml`: pre-merge harness validation workflow that starts the frontend server and runs harness validation.

The deterministic test discovery tool reported:

| Surface | Runner | Files | Test symbols | Suggested command |
|---|---|---:|---:|---|
| Root deterministic tools | pytest | 44 | 437 | `python3 -m pytest -q tools` |
| Chirality app-dev frontend | vitest | 40 | 295 | `cd projects/chirality-app-dev/frontend && npm test` |
| OpenPipeStress Python | pytest | 59 | 359 | `cd projects/chirality-piping && python3 -m pytest -q tests` |
| OpenPipeStress desktop | vitest | 15 | 145 | `cd projects/chirality-piping && npm test --workspace apps/desktop` |
| OpenPipeStress Rust | cargo | 37 | 604 | `cargo test --manifest-path <crate>/Cargo.toml` per crate |

Only discovery and skill metadata validation were run for this report. Full suites were not run.

## Structural Strengths

1. Clear authority model: root docs consistently separate human authority from agent execution.
2. Filesystem-native state: governed truth, working state, snapshots, ledgers, registers, and reports are inspectable plain files.
3. Strong decomposition grammar: packages and deliverables are stable and flat, with stable IDs and deliverable-local state files.
4. Good separation of concern: agents define roles and authority; skills define reusable methods; tools perform deterministic work; projects/domains hold applied state.
5. Explicit public/private boundary: export is allowlist-based, private roots are excluded, and private absolute paths are sanitized.
6. Practical validation tooling: skill metadata, dependency schemas, domain integrity, source catalogs, asset validation, test discovery, and many specialized validators exist.
7. Realistic examples: public examples show full execution workspaces, not toy snippets.
8. Product workspaces are substantial: OpenPipeStress and app-dev have governance docs, decomposition, implementation code, tests, schemas, fixtures, and validation assets.

## Structural Risks And Inconsistencies

| Risk | Severity | Observation | Suggested action |
|---|---|---|---|
| Registry drift: pipeline categories | Medium | `AGENTS.md` names `PDF2MD*` and `DRAWING_EXTRACT*`; `docs/TYPES.md` still appears narrower. | Update `docs/TYPES.md` or add an explicit transitional note. |
| Registry drift: PDF2MD dispatch | Medium | Some surfaces reference `pdf2md-page` and `pdf2md-page-assets`; `AGENT_PDF2MD.md` indicates `pdf2md-page-full` as newer canonical dispatch. | Decide canonical dispatch model and update `AGENTS.md`, `skills/README.md`, and PDF2MD docs together. |
| Deprecated wrapper residue | Medium | Older design-basis prose still references retired standalone task agents now replaced by `TASK + TaskSkill`. | Add historical-status labels or a deprecation appendix to older narrative docs. |
| `DELIVERABLE_TASK` status ambiguity | Low to medium | Indexed as Type 2 but file is a deprecated compatibility pointer. | Keep index but mark explicitly as compatibility pointer in the matrix/table, or move to legacy section. |
| `WRITE_SCOPE` enum drift | Medium | Live agent headers use values beyond the narrow enum in root type/spec docs. | Normalize the enum or explicitly permit structured/custom scopes under a grammar. |
| Publication legacy note conflict | Medium | Tool registry and skills README disagree on whether `dbm-concordance-seed` is legacy or still new-run path. | Reconcile `tools/REGISTRY.md`, `skills/README.md`, and DBM publisher instructions. |
| Domain `_LocalIndexes` ignore policy | Low | README says exceptions are trackable, but `.gitignore` re-ignores `_LocalIndexes`. | Fix `.gitignore` exception order if README is still intended. |
| Private absolute paths in source workspaces | Low to medium | Many source/domain/example files contain private absolute paths; export sanitizes them but source remains pathful. | Keep export checks strict; consider reducing pathful generated artifacts in public examples over time. |
| Generated staging tree visible locally | Low | `exports/chirality-app/staging/` exists and is large but ignored. | Treat profile script, manifest, and report as source truth; optionally document cleanup/rebuild procedure. |
| App-dev dependency closure | High for app-dev project planning | Latest app-dev closure report says all-active graph is cyclic and project-wide status should not be overclaimed. | Resolve or explicitly isolate cycles before closure/readiness claims. |
| App-dev path drift | Low to medium | At least one plan references `docs/harness/...` while live file is under `frontend/docs/harness/...`. | Clean stale plan references or mark old paths as historical. |
| App-dev missing companion register | Medium | Decomposition references an invariant coverage register not found during read-only inspection. | Locate, regenerate, or update the decomposition note. |
| OpenPipeStress stale downstream surfaces | Medium to high for release work | Decomposition warns downstream surfaces may lag rev 0.7. | Use owning workflows to refresh derivative packages and record handoff state. |
| OpenPipeStress release TBDs | High for release readiness | Open issues remain in tolerances, solver choices, rule grammar, approval workflow, migration, comparisons, handoff, CAEPIPE clarifications. | Treat these as release-blocking until dispositioned by project owners. |
| Local noise and generated artifacts | Low | `.DS_Store`, dependency folders, build outputs, caches, and staging outputs distort raw filesystem counts. | Use tracked-file inventory for structural assessments; keep ignore rules current. |

## Recommended Maintenance Priorities

1. Reconcile live registry drift.

   Start with `AGENTS.md`, `docs/TYPES.md`, `docs/SPEC.md`, `skills/README.md`, `tools/REGISTRY.md`, and the affected agent files. The largest practical benefit is reducing ambiguity for future agents about what is canonical versus historical.

2. Clarify legacy surfaces.

   Mark `DELIVERABLE_TASK`, old standalone task-agent names, legacy publication/concordance helpers, and PDF2MD split-skill paths with consistent "legacy", "compatibility", or "current" status.

3. Keep generated and canonical surfaces visibly separate.

   `exports/chirality-app/staging/`, dependency folders, caches, and build outputs should remain operational artifacts. Reports and docs should cite profile scripts and tracked manifests, not generated staging contents.

4. Normalize project-local closure states.

   App-dev and OpenPipeStress both have real governed execution state. Their reports should continue to distinguish authoritative decomposition truth, derivative packages, snapshots, open issues, and closure status.

5. Preserve the public/private boundary.

   The export profile is doing important work. Any change to exported roots should run `python3 exports/chirality-app/export_public.py` and review boundary findings before promotion.

6. Use test discovery as the source of validation inventory.

   Avoid stale test-count prose. Let `tools/validation/discover_test_surfaces.py` produce current surfaces, and cite its suggested commands in plans or readiness reports.

## Bottom Line

This monorepo is best understood as a canonical governance-and-execution repository with embedded product workspaces, not as a conventional app repo. The most important assets are the authoritative instruction contracts, filesystem state conventions, deterministic tools, public export profile, and governed project/domain workspaces. Its structure is coherent and unusually explicit, but its scale and fast evolution have produced predictable drift in narrative registries and legacy references. The next structural quality gains should come from registry reconciliation, legacy-status cleanup, and continued separation between authoritative snapshots and generated derivative packages.
