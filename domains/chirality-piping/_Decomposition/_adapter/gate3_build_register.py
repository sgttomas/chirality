#!/usr/bin/env python3
"""Gate 3 Category_Register builder for chirality-piping.

Faithful-to-author reconciliation (operator directive, mirrors chirality-app-dev).
The piping corpus is strongly pre-structured by its authors:
  * 18 execution deliverable packages PKG-00..17 (101 deliverables) — preserved 1:1
    as CAT-001..018.
  * 12 cross-cutting categories reconciling the docs/, governance, root, and code
    bodies (CAT-019..030).

This writes Category_Register.csv (the binding category taxonomy). gate3_assign.py
then source-routes every IN atom into exactly one category; gate3_ratify.py runs
the binding retrieval ratification. No atom splits, no UnitStatement/ContentHash
edits (lossless).

Usage:  python3 _adapter/gate3_build_register.py    (cwd = MONOREPO_ROOT)
"""
from __future__ import annotations
import csv
from pathlib import Path

MONO = Path.cwd()
DEC = MONO / "domains/chirality-piping/_Decomposition"

# --- 18 deliverable packages PKG-00..17 -> CAT-001..018 ----------------------
PKG = [
    ("Software Architecture Runway",
     "The PKG-00 architecture runway: ADR baseline, repository/module boundary and application service command-query-job model, persistence and schema-versioning architecture, GUI-state and interaction architecture, the diagnostics/warning/result-envelope contract, the API-boundary and adapter-contract map, and the layered software test and acceptance strategy.",
     "ADR baseline architecture decision record repository module boundary application service command query job persistence schema versioning GUI state interaction diagnostics warning result envelope contract API boundary adapter contract map layered test acceptance strategy"),
    ("Governance, IP Boundary, and Professional Responsibility",
     "The PKG-01 project governance: governance baseline, copyright and protected-data boundary policy, contributor certification workflow, and the professional-responsibility and product-claims policy.",
     "project governance baseline copyright protected data boundary policy contributor certification workflow professional responsibility product claims engineering disclaimer"),
    ("Domain Model, Units, and Core Schemas",
     "The PKG-02 domain core: canonical domain-model schema, unit-system and dimensional-analysis core contract, the code-neutral analysis boundary model, plugin and extension domain contracts, and project persistence and round-trip serialization.",
     "canonical domain model schema unit system dimensional analysis core contract code neutral analysis boundary plugin extension domain contracts project persistence round trip serialization"),
    ("Piping Components, Materials, and Library Data Model",
     "The PKG-03 component and material data model: material library schema with provenance, pipe-section and component library schema, bend/elbow and branch-connection component models, rigid component models (valves, flanges, reducers, specialty), expansion-joint model, public-private library import provenance checker, and the pipe-section property and mass-property calculator.",
     "material library schema provenance pipe section component library bend elbow branch connection rigid valve flange reducer expansion joint import provenance checker mass property calculator"),
    ("Solver Core and Numerical Methods",
     "The PKG-04 solver core: 3D frame stiffness kernel, straight pipe element, linear support and restraint models, nonlinear-support active-set solver, sparse-solver performance harness, and solver diagnostics and singularity detection.",
     "3D frame stiffness kernel straight pipe element linear support restraint nonlinear active set solver sparse performance harness diagnostics singularity detection numerical method"),
    ("Loads, Load Cases, and Stress Recovery",
     "The PKG-05 loads and stress: primitive load-case engine, load-case algebra engine, fundamental stress-recovery module, analysis-status semantics, and concentrated/distributed user load application.",
     "primitive load case engine load case algebra fundamental stress recovery analysis status semantics concentrated distributed user load application combination"),
    ("Rule Packs and User-Supplied Code Check Engine",
     "The PKG-06 rule-check engine: rule-pack schema, sandboxed unit-aware expression evaluator, required-input completeness checker, private rule-pack lifecycle and checksum handling, and the invented non-code example rule pack.",
     "rule pack schema sandboxed unit aware expression evaluator required input completeness checker private rule pack lifecycle checksum code check engine example"),
    ("Graphical User Interface and Engineering Workflow",
     "The PKG-07 GUI and workflow: 3D viewport and centerline editor, model tree and property inspector, material/component/rule-pack editors, missing-data warning and blocking UX, results viewer, accessibility and usability baseline, solve-execution UX (progress/cancellation/diagnostics), and the design-authoring state and comparison workspace.",
     "3D viewport centerline editor model tree property inspector editors missing data warning blocking UX results viewer accessibility usability solve execution progress cancellation comparison workspace"),
    ("Reporting, Audit, and Reproducibility",
     "The PKG-08 reporting and audit: calculation-report generator, audit manifest and model hash, warnings/assumptions/provenance report section, result export format, report protected-content linter, and the state/comparison/handoff report sections.",
     "calculation report generator audit manifest model hash warnings assumptions provenance report section result export protected content linter reproducibility state comparison handoff"),
    ("Verification, Validation, and Quality Oracles",
     "The PKG-09 V&V: mechanics benchmark suite, stress-recovery benchmark suite, nonlinear-support regression suite, validation-manual skeleton, and the release quality-gate checklist.",
     "mechanics benchmark suite stress recovery benchmark nonlinear support regression validation manual skeleton release quality gate checklist oracle verification"),
    ("Build, Packaging, API, and Interoperability",
     "The PKG-10 build and API: public API and plugin boundary, import-export adapter framework, local-FEA handoff data contract, build/packaging/CI-CD pipeline, and the headless CLI and structured-I/O analysis runner.",
     "public API plugin boundary import export adapter framework local FEA handoff data contract build packaging CI CD pipeline headless CLI structured IO analysis runner interoperability"),
    ("Documentation, Examples, and Education",
     "The PKG-11 documentation and education deliverables: user-guide skeleton, developer guide for solver and rule packs, theory notes (classical to modern centerline analysis), invented educational example models, and contributor tutorial and onboarding.",
     "user guide skeleton developer guide solver rule packs theory notes classical modern centerline analysis educational example models contributor tutorial onboarding documentation"),
    ("Security, Privacy, and Private Data Handling",
     "The PKG-12 security deliverables: local-first storage and private-data paths, private-data redaction and export controls, telemetry off-by-default design, secret and private-library handling, and the security threat model.",
     "local first storage private data paths redaction export controls telemetry off by default secret private library handling security threat model privacy"),
    ("Physical Design Knowledge and Constraint Engine",
     "The PKG-13 design-knowledge engine: design-knowledge schema and provenance model, constraint entity and provenance model, constraint-validation engine, and the physical-to-analytical transformation contract.",
     "design knowledge schema provenance constraint entity validation engine physical to analytical transformation contract physical design knowledge"),
    ("Model States, Analysis Runs, and Comparison",
     "The PKG-14 states and runs: immutable model-state records, analysis-run records, model-state comparison engine, analysis-run comparison engine, and comparison mapping/tolerance/export contracts.",
     "immutable model state records analysis run records model state comparison engine analysis run comparison mapping tolerance export contracts"),
    ("Handoff and External Prover Workflow",
     "The PKG-15 handoff: canonical handoff-package schema and manifest, target-mapping and unsupported-behavior contract, downstream modeling export workflow, and external-prover boundary metadata.",
     "canonical handoff package schema manifest target mapping unsupported behavior contract downstream modeling export workflow external prover boundary metadata"),
    ("Model Operation and Agent Proposal Framework",
     "The PKG-16 agent-operation framework: structured model-operation schema, operation validation and diff preview, user acceptance and operation audit trail, and agent rationale and professional-boundary controls.",
     "structured model operation schema operation validation diff preview user acceptance operation audit trail agent rationale professional boundary controls proposal"),
    ("Export Format Interoperability",
     "The PKG-17 export interoperability: CAEPIPE and export-format source basis, export package/profile/stable-ID map contracts, native open-JSON export package, CAEPIPE MBF export profile and deterministic writer, CAEPIPE external-run harness and CSV parser, stress-neutral CSV/JSON package, conservative PCF subset exporter, GLB/glTF review-geometry export, and the export-adapter SDK and additional targets.",
     "CAEPIPE export format source basis package profile stable ID map native open JSON MBF deterministic writer external run harness CSV parser stress neutral PCF subset GLB glTF review geometry export adapter SDK interoperability"),
]

# --- 12 cross-cutting categories CAT-019..030 --------------------------------
CROSS = [
    ("Product Requirements, Specification, and System Architecture",
     "Top-level product-definition and architecture corpus under docs/: PRD, SPEC, TYPES, CONTRACT, DIRECTIVE, INTENT, the product README, the docs/architecture/ body (ADRs, analysis-status semantics, code-neutral analysis boundary, extension/domain contracts, persistence contract, plugin boundary), and docs/theory centerline analysis. The authoritative what/why the PKG deliverables implement.",
     "Atoms from PRODUCT_DOCS units: PRD, SPEC, TYPES, CONTRACT, DIRECTIVE, INTENT, README, docs/architecture ADRs and contracts, docs/theory centerline analysis.",
     "Exclude development-process/build/release/validation docs (CAT-020), IP/security policy (CAT-021), guides/examples (CAT-022), and the per-PKG engineering deliverables (CAT-001..018).",
     "product requirements document PRD system specification type system interface contract directive intent README architecture decision record persistence plugin boundary extension domain contract code neutral analysis centerline theory"),
    ("Development Process, Build, Release, and Validation Strategy",
     "Process-level docs under docs/ describing how the product is planned, built, released, quality-gated, and validated: the implementation PLAN, build-and-release guide, release quality gates, release-notes template, the agentic development workflow, the validation strategy, the validation-manual index, and the report-notice template.",
     "Atoms from PRODUCT_DOCS units: PLAN, BUILD_AND_RELEASE, RELEASE_QUALITY_GATES, RELEASE_NOTES_TEMPLATE, AGENTIC_DEVELOPMENT_WORKFLOW, VALIDATION_STRATEGY, validation_manual/index, report_notice_template.",
     "Exclude product requirement/spec/architecture docs (CAT-019) and the PKG-09 V&V / PKG-10 build deliverables (CAT-010, CAT-011).",
     "implementation plan build and release release quality gates release notes template agentic development workflow validation strategy validation manual report notice process milestones"),
    ("IP, Data Boundary, Security, and Privacy Policy",
     "Cross-cutting IP and security policy under docs/: the IP-and-data boundary, the professional boundary, and the docs/security/ body — local-first storage policy, redaction and export controls, secret and private-library handling, telemetry policy, and the threat model.",
     "Atoms from PRODUCT_DOCS units: IP_AND_DATA_BOUNDARY, PROFESSIONAL_BOUNDARY, docs/security local_first_storage_policy, redaction_export_controls, secret_private_library_handling, telemetry_policy, threat_model.",
     "Exclude the PKG-01 governance deliverables (CAT-002) and PKG-12 security deliverables (CAT-013); this is the cross-cutting policy corpus, not the per-PKG deliverables.",
     "IP data boundary professional boundary local first storage redaction export controls secret private library telemetry policy threat model security privacy protected data"),
    ("User, Developer, and Contributor Guides, Examples, and Local Analysis",
     "End-user/developer/contributor guidance and example corpus under docs/: the user-guide index, developer-guide index, contributor-guide index, the _Examples body (README, rule-pack notice), and the local-analysis local-FEA handoff guidance.",
     "Atoms from PRODUCT_DOCS units: user_guide/index, developer_guide/index, contributor_guide/index, _Examples/README, _Examples/rule_pack_notice, local_analysis/local_fea_handoff_guidance.",
     "Exclude the PKG-11 documentation/education deliverables (CAT-012) and process docs (CAT-020); this is the guide/index and example corpus.",
     "user guide developer guide contributor guide index examples rule pack notice local analysis local FEA handoff guidance onboarding tutorial how to"),
    ("Decomposition and Reconciliation Records",
     "Backward-looking structuring/closure governance under execution/_Decomposition: the OpenPipeStress execution decomposition records, dependency-closure and reconciliation artifacts, and the package/deliverable derivation records.",
     "Atoms from the EXECUTION_GOVERNANCE decomposition unit (execution/_Decomposition/).",
     "Exclude forward scope-change governance (CAT-024) and the repository operating posture (CAT-025).",
     "execution decomposition reconciliation dependency closure package deliverable derivation records DAG structuring closeout governance"),
    ("Scope-Change Governance",
     "Forward-running scope-change governance: the execution/_ScopeChange packets SCA-001..004 and the docs/_ScopeChange corpus (OpenPipeStress PRD v0.2 and its scope-change brief, and the SCA Authority records).",
     "Atoms from EXECUTION_GOVERNANCE scope-change units (SCA-001..004) and PRODUCT_DOCS scope-change units (OpenPipeStress_PRD_v0.2, PRD_v0.2_Scope_Change_Brief, SCA-002/003 Authority).",
     "Exclude the decomposition/reconciliation records (CAT-023) and the current PRD/spec product definition (CAT-019).",
     "scope change application SCA authority packet PRD v0.2 scope change brief amendment ruling governance approval"),
    ("Repository Operating Posture and Contribution Governance",
     "The repository operating posture (root AGENTS.md, CONTRIBUTING.md, README.md) and the governance/ contribution-governance body: maintainers register, contribution review checklist, and the contributor certification template.",
     "Atoms from ROOT_DOCS (AGENTS, CONTRIBUTING, README) and PRODUCT_DOCS governance/ units (MAINTAINERS, CONTRIBUTION_REVIEW_CHECKLIST, CONTRIBUTOR_CERTIFICATION_TEMPLATE).",
     "Exclude the PKG-01 governance deliverables (CAT-002), scope-change governance (CAT-024), and decomposition records (CAT-023).",
     "AGENTS repository operating posture contributing README maintainers contribution review checklist contributor certification template git discipline agent index"),
    ("Core Engine Implementation Source",
     "The core engine implementation source tree (core/): the implementing Python/source modules for the domain model, solver, loads, rules, schemas, and supporting engine internals.",
     "Atoms from CODE_CORE (grouped SRC-CODE-CORE, core/ implementation source).",
     "Exclude the application/GUI source (CAT-027), tests (CAT-028), tooling (CAT-029), validation source (CAT-030), and the PKG specifications that describe the engine behavior (CAT-001..018).",
     "core engine implementation source modules solver domain model loads rules schemas python classes functions internals"),
    ("Application and GUI Implementation Source",
     "The application and GUI implementation source tree (apps/): the front-of-house application, viewport/editor, workflow, and operator-facing implementation modules.",
     "Atoms from CODE_APPS (grouped SRC-CODE-APPS, apps/ implementation source).",
     "Exclude the core engine source (CAT-026), tests (CAT-028), and the PKG-07 GUI specifications (CAT-008).",
     "application GUI source viewport editor workflow operator facing modules desktop app frontend implementation"),
    ("Test Suites",
     "The test source tree (tests/): unit and integration test modules exercising the engine, application, and contracts.",
     "Atoms from CODE_TESTS (grouped SRC-CODE-TESTS, tests/ source).",
     "Exclude the V&V quality-oracle implementation (CAT-030), validation strategy docs (CAT-020), and the PKG-09 V&V deliverables (CAT-010).",
     "tests unit integration test modules fixtures assertions pytest coverage engine application contracts"),
    ("Developer Tooling and Scripts",
     "The developer tooling source tree (tools/): scripts and utilities supporting build, coordination, dependency handling, and repository automation.",
     "Atoms from CODE_TOOLS (grouped SRC-CODE-TOOLS, tools/ source).",
     "Exclude the core/application source (CAT-026/027) and process/build docs (CAT-020).",
     "tools scripts utilities coordination dependency automation build helpers repository maintenance command line"),
    ("Validation and Quality-Oracle Implementation",
     "The validation implementation source tree (validation/): the executable V&V harnesses, benchmark oracles, and quality-gate checks.",
     "Atoms from CODE_VALIDATION (grouped SRC-CODE-VALIDATION, validation/ source).",
     "Exclude the test suites (CAT-028), the validation-strategy/manual docs (CAT-020), and the PKG-09 V&V deliverables (CAT-010).",
     "validation quality oracle implementation benchmark harness verification checks gate executable mechanics stress recovery regression"),
]


def main():
    rows = []
    for i, (name, scope, query) in enumerate(PKG):
        cid = f"CAT-{i+1:03d}"
        pkgnum = i
        rows.append({
            "CategoryID": cid, "Name": name,
            "ScopeDescription": scope,
            "InclusionCriteria": f"Atoms from PKG-{pkgnum:02d} deliverables (group EXECUTION_DELIVERABLE), routed by author package placement.",
            "Exclusions": "Exclude other PKG packages (CAT-001..018), the cross-cutting docs/governance/code categories (CAT-019..030), and TBD/OUT atoms.",
            "SourceAlignment": f"EXECUTION_DELIVERABLE/PKG-{pkgnum:02d} ({name})",
            "Query": query,
        })
    for j, (name, scope, incl, excl, query) in enumerate(CROSS):
        cid = f"CAT-{19+j:03d}"
        rows.append({
            "CategoryID": cid, "Name": name, "ScopeDescription": scope,
            "InclusionCriteria": incl, "Exclusions": excl,
            "SourceAlignment": name, "Query": query,
        })
    cols = ["CategoryID", "Name", "ScopeDescription", "InclusionCriteria",
            "Exclusions", "SourceAlignment", "Query"]
    out = DEC / "Category_Register.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(rows)
    print(f"wrote {out.relative_to(MONO)} with {len(rows)} categories "
          f"({len(PKG)} PKG + {len(CROSS)} cross-cutting)")


if __name__ == "__main__":
    raise SystemExit(main())
