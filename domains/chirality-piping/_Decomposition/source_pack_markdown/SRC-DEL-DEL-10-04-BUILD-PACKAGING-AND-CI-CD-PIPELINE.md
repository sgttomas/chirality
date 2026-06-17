# Source Pack: SRC-DEL-DEL-10-04-BUILD-PACKAGING-AND-CI-CD-PIPELINE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/Datasheet.md

### Datasheet: DEL-10-04 Build, packaging, and CI/CD pipeline

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-10-04 |
| Package ID | PKG-10 |
| Package | Build, Packaging, API, and Interoperability |
| Type | CI_CD_CHANGE |
| Scope item | SOW-032 |
| Objectives | OBJ-008; OBJ-009 |
| Context envelope | L |
| Current setup state | SEMANTIC_READY |

#### Attributes

| Attribute | Value |
|---|---|
| Deliverable purpose | Define the setup basis for reproducible builds, packaging, and CI/CD workflow work. |
| Anticipated implementation artifacts | CI workflows; packaging scripts; release notes template. |
| Runtime/UI baseline | Rust core/application services; Tauri 2 desktop shell; TypeScript/React/Vite GUI where GUI-facing. |
| Test gate baseline | Cargo tests; Vitest; Playwright; validation gates; protected-content/provenance gates. |
| Desktop packaging baseline | Tauri-supported macOS, Windows, and Linux targets. |
| Release-quality boundary | Development/release automation evidence only; no engineering certification or code-compliance claim. |

#### Conditions

| Condition | Status |
|---|---|
| CI provider | TBD - human/project authority decision required. |
| Platform release matrix | TBD - this setup run does not finalize exact OS/architecture coverage. |
| Coverage thresholds | TBD - no final numerical thresholds are set by this setup run. |
| Performance thresholds | TBD - no final timing/size thresholds are set by this setup run. |
| Dependency versions | TBD - exact versions remain implementation-level decisions. |
| Release signing process | TBD - governance/release authority decision required. |

#### Construction

This setup artifact constrains later implementation work without creating implementation files. A future authorized DEL-10-04 implementation pass may draft CI workflows, packaging scripts, and release-note templates only after human authority confirms the CI provider, release matrix, thresholds, and write scope.

The build and packaging pipeline must preserve the OpenPipeStress boundaries:

- public automation must not introduce protected standards text, protected data tables, proprietary vendor data, or private project/rule-pack data;
- test and release gates must keep mechanics verification separate from user rule checks and professional approval;
- release artifacts must disclose validation status, limitations, data-boundary constraints, and professional-responsibility limitations;
- adapters, plugins, and packaging steps must not bypass unit, provenance, diagnostic, or privacy checks.

#### References

- `INIT.md` - bootstrap and data-boundary posture.
- `AGENTS.md` - Type 2 sealed-deliverable dispatch rules.
- `docs/DIRECTIVE.md` - founding intent, stop rules, and no-certification boundary.
- `docs/CONTRACT.md` - invariant catalog, especially OPS-K-IP, OPS-K-DATA, OPS-K-PRIV, OPS-K-AUTH, and OPS-K-AGENT.
- `docs/SPEC.md` - architecture layers, reporting/audit requirements, V&V mechanics, and agentic implementation mechanics.
- `docs/VALIDATION_STRATEGY.md` - benchmark families and release gate expectations.
- `docs/PRD.md` - platform criteria and release milestones, including PRD 19.2, 19.3, and 22.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` - revision 0.7 scope, architecture basis, decisions, and open issues.
- `docs/_Registers/Deliverables.csv` - row DEL-10-04.
- `docs/_Registers/ScopeLedger.csv` - row SOW-032.
- `docs/_Registers/ContextBudgetQA.csv` - row DEL-10-04.

#### TBD and Human-Ruling Slots

- TBD: CI provider.
- TBD: exact supported platform/release matrix.
- TBD: coverage and performance thresholds.
- TBD: release signing/notarization/publishing policy.
- TBD: exact packaging artifact names and distribution channels.


## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/Guidance.md

### Guidance: DEL-10-04 Build, packaging, and CI/CD pipeline

#### Purpose

This guidance explains how to interpret the DEL-10-04 setup artifacts. The deliverable exists to prepare a bounded future implementation path for reproducible builds, packaging, and CI/CD while keeping release engineering, interoperability, data-boundary, and professional-responsibility constraints visible.

#### Principles

- Treat this setup kit as draft/proposal evidence until a human review gate accepts it.
- Keep build automation reproducible and auditable: a future release should be traceable to source revision, build inputs, test results, validation status, and known limitations.
- Preserve SCA-001 architecture baselines: Rust core/application services, Tauri 2 desktop shell where GUI-facing, TypeScript/React/Vite GUI where applicable, schema-first envelopes, and layered software-quality gates.
- Leave unresolved implementation choices as `TBD` unless a cited human ruling resolves them.
- Do not let CI, packaging, adapters, or plugins bypass unit safety, provenance, diagnostics, private-data handling, or protected-content controls.
- Do not present a passing build, passing test suite, packaged desktop app, or release label as engineering certification or code compliance.

#### Considerations

DEL-10-04 is a large context envelope item. Future implementation may need to split into smaller tasks if it expands beyond one bounded change. Natural split points include CI workflow skeleton, desktop packaging skeleton, release-note template, signing/publishing policy, protected-content/provenance gates, and release-checklist automation.

The accepted baseline names Cargo, Vitest, Playwright, validation, and protected-content/provenance gates. It does not finalize the CI host, coverage thresholds, performance thresholds, installer formats, signing identities, release publishing destinations, dependency versions, or exact platform/architecture matrix.

#### Trade-offs

- A minimal CI skeleton can provide early feedback, but final release gating needs human decisions about provider, supported platforms, and thresholds.
- Broad platform coverage improves availability, but it increases signing, notarization, packaging, and validation burden.
- Strict gates reduce release risk, but thresholds must be defensible and should not be invented before solver, GUI, and validation maturity are known.
- Packaging convenience must not weaken local-first privacy or protected-data controls.

#### Examples

TBD. This setup run does not create example workflow files, packaging scripts, release templates, or implementation snippets because the write scope is limited to deliverable-local setup documentation and registers.

#### Human-Ruling Queue

- TBD: CI provider and hosting model.
- TBD: supported OS and architecture release matrix.
- TBD: installer/package formats per supported platform.
- TBD: coverage and performance thresholds.
- TBD: signing, notarization, checksum, and release publishing policy.
- TBD: whether release notes template belongs in this deliverable or a later release-governance deliverable.

#### Conflict Table (for human ruling)

No source conflicts were identified during this setup pass. The unresolved items above are authority gaps, not conflicts.


## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/Procedure.md

### Procedure: DEL-10-04 Build, packaging, and CI/CD pipeline

#### Purpose

Run and verify the deliverable-local setup workflow for DEL-10-04 without creating product CI, packaging, release, manifest, or source-code artifacts.

#### Prerequisites

- Root bootstrap, agent index, contract, decomposition, registers, and project-local skill instructions have been read.
- The working folder is `execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/`.
- Current write scope is limited to this deliverable folder.
- Protected-data, private-data, no-certification, and human-authority boundaries are active.
- CI provider, release matrix, and thresholds remain `TBD` unless human authority resolves them.

#### Steps

1. Execute `four-documents` with `RUN_PASSES=P1_P2` by drafting `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` from the sealed context and accessible governing references.
2. Confirm the four documents preserve the setup-only boundary and do not create CI workflows, packaging scripts, manifests, release files, or source code.
3. Execute `semantic-matrix-build` by replacing `_SEMANTIC.md` with a deliverable-local semantic lens and setting or verifying `_STATUS.md` as `SEMANTIC_READY` only after semantic QA passes.
4. Execute `lens-register` by generating `_SEMANTIC_LENSING.md` from `_SEMANTIC.md` and the four production documents.
5. Execute `four-documents` with `RUN_PASSES=P3_ONLY` by checking the lensing register for warranted enrichment items, applying only source-supported setup-document changes, and recording unresolved items as `TBD`.
6. Execute `dependency-extract` by writing `Dependencies.csv` v3.1 and refreshing `_DEPENDENCIES.md`.
7. Run local validation checks for document presence, dependency schema, semantic/lensing structure, status, and write-scope compliance.

#### Verification

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist.
- `_SEMANTIC.md` contains canonical matrices A and B plus derived matrices C, F, D, K, G, X, T, and E.
- `_SEMANTIC_LENSING.md` contains complete coverage for matrices A, B, C, F, D, X, and E.
- `Dependencies.csv` validates with `python3 tools/validation/validate_dependencies_schema.py`.
- `_DEPENDENCIES.md` summarizes the same ACTIVE dependency rows present in `Dependencies.csv`.
- `_STATUS.md` current state is `SEMANTIC_READY`.
- No files outside the deliverable folder were edited.
- No CI workflow, packaging script, manifest, release file, source code, or repo-level artifact was created or modified.

#### Records

Preserve these setup records:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_*.md`

#### Completion Condition

The setup workflow is complete when the document kit, semantic artifacts, dependency register, run records, and status file exist; local checks pass; and unresolved CI/release decisions remain explicitly marked `TBD` for human authority.

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/Specification.md

### Specification: DEL-10-04 Build, packaging, and CI/CD pipeline

#### Scope

This specification governs the setup basis for `DEL-10-04` only. It describes requirements and verification expectations for a future build, packaging, and CI/CD implementation pass, but this setup session does not modify CI workflows, packaging scripts, manifests, release files, source code, or repository-level artifacts.

In scope for this setup run:

- define build/package/CI requirements at the deliverable-document level;
- surface unresolved authority decisions as `TBD`;
- preserve architecture-basis constraints from SCA-001;
- produce semantic and dependency setup artifacts.

Out of scope for this setup run:

- selecting a final CI provider;
- finalizing a release matrix or final thresholds;
- creating or editing actual workflow files, packaging scripts, manifests, release templates, or source code;
- making certification, endorsement, sealing, or code-compliance claims.

#### Requirements

| ID | Requirement | Source basis | Verification |
|---|---|---|---|
| REQ-10-04-01 | Future implementation must provide reproducible build, packaging, and CI/CD workflows for supported platforms. | SOW-032; Deliverables.csv DEL-10-04 | Human review of future implementation artifacts. |
| REQ-10-04-02 | Build/test gates must align with the accepted Cargo, Vitest, Playwright, validation, protected-content, and provenance gate baseline. | SOFTWARE_DECOMP AB-00-08; DEC-011 | Future CI/job review and test evidence. |
| REQ-10-04-03 | Desktop packaging planning must follow the Tauri-supported macOS, Windows, and Linux baseline without finalizing the detailed platform release matrix in this setup pass. | SOW-032 notes; architecture baseline | Confirm platform matrix remains `TBD` unless human-ruling evidence is cited. |
| REQ-10-04-04 | CI provider, coverage thresholds, performance thresholds, exact dependency versions, signing, publishing, and release matrix details must remain `TBD` unless a human authority record resolves them. | DEC-012; OI-002; user brief | Check all unresolved choices are visible as `TBD`. |
| REQ-10-04-05 | Pipeline and packaging concepts must not bypass unit checks, provenance checks, diagnostics, privacy controls, or adapter/plugin governance boundaries. | AB-00-02; AB-00-06; AB-00-07; OPS-K-UNIT-1; OPS-K-PRIV | Future implementation review and security/privacy checks. |
| REQ-10-04-06 | Public release automation must not include protected standards text, protected examples, proprietary engineering values, private rule packs, private project data, or private library data. | OPS-K-IP-1/2/3; OPS-K-DATA-1/2/3; OPS-K-PRIV | Protected-content/provenance gate and review. |
| REQ-10-04-07 | Release artifacts and pipeline status must not claim certification, sealing, approval, authentication, or engineering code compliance for reliance. | OPS-K-AUTH-1; professional responsibility boundary | Product-claims and release-note review. |
| REQ-10-04-08 | Packaging and CI outputs must support reproducibility evidence such as commit/build identifiers, test results, validation status, and known limitations. | PRD 22; VALIDATION_STRATEGY release gate; SPEC reporting/audit principles | Future release checklist and reproducibility review. |

#### Standards

No external engineering code or standards-body text is incorporated by this deliverable. Governing project standards for this setup pass are internal OpenPipeStress governance artifacts: `INIT.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/IP_AND_DATA_BOUNDARY.md`, `docs/VALIDATION_STRATEGY.md`, and `execution/_Decomposition/SOFTWARE_DECOMP.md`.

The term "Tauri-supported targets" is used only as an architecture-baseline label from the sealed context. Exact Tauri target details, operating-system versions, signing requirements, installer formats, and publishing rules remain `TBD`.

#### Verification

| Check | Method | Expected result |
|---|---|---|
| Document kit presence | File inspection | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist. |
| Semantic setup | File inspection and local QA | `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` exist, with no matrix parse errors. |
| Dependency setup | Schema validation | `Dependencies.csv` validates against v3.1 schema. |
| Scope boundary | Diff/file inspection | No CI workflows, package scripts, manifests, release files, source code, or repo-level artifacts are modified. |
| TBD preservation | Text review | CI provider, release matrix, and thresholds remain visible as `TBD`. |
| Protected-data boundary | Text review | No protected standards content, proprietary values, or private data are introduced. |
| Authority boundary | Text review | No certification, sealing, approval, endorsement, or compliance claim is made. |

#### Documentation

Required setup artifacts for this session:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_run_records/TASK_RUN_*.md`
- `_STATUS.md`

Anticipated implementation artifacts remain future work:

- CI workflows
- packaging scripts
- release notes template
