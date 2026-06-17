# Source Pack: SRC-DEL-DEL-17-08-GLB-GLTF-REVIEW-GEOMETRY-EXPORT

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export/Datasheet.md

### Datasheet: DEL-17-08 GLB/glTF review geometry export

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-17-08 |
| Package ID | PKG-17 |
| Package name | Export Format Interoperability |
| Deliverable name | GLB/glTF review geometry export |
| Type | BACKEND_FEATURE_SLICE |
| Scope items | SOW-030, SOW-074 |
| Objectives | OBJ-009, OBJ-017 |
| Source basis | DEL-17-01 source-basis register; DEL-17-02 export package/profile/stable-ID contract |
| Lifecycle role | Target-specific Phase A contract draft for review-geometry export |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Target family | GLB/glTF review geometry | `_CONTEXT.md`; SOFTWARE_DECOMP DEL-17-08; PLAN-EXPORT-INTEROP Geometry Exchange |
| Primary output intent | Lightweight 3D visual inspection and review context | PLAN-EXPORT-INTEROP Geometry Exchange |
| Non-authority boundary | Geometry-only review aid; not solver geometry, analysis proof, formal validation, code compliance, release readiness, or professional acceptance | DEL-17-01 F-17-01-005; DEL-17-02 Boundary Requirements; CONTRACT OPS-K-AUTH-1 |
| Format basis | Khronos glTF 2.0 public specification | GLTF-2.0, sections 2.4, 3.4, 4.2-4.4, and 5.24-5.25 |
| Binary container | `.glb` as Binary glTF when a single review artifact is preferred | GLTF-2.0 section 4 |
| JSON-plus-assets option | `.gltf` with external or embedded resources remains a possible profile option | GLTF-2.0 sections 2.4 and 4.1 |
| Coordinate and unit basis | glTF is right-handed, +Y-up, and uses meters for linear distances | GLTF-2.0 section 3.4 |
| Stable identity basis | Canonical OpenPipeStress IDs must be preserved directly through target metadata where supported or through a manifest-referenced sidecar | DEL-17-02 stable ID map requirements |
| Loss reporting | Required even for successful review-geometry exports | DEL-17-02 loss report requirements |

#### Conditions

| Condition | Phase A disposition |
|---|---|
| Input source model | Canonical model surface from `schemas/model.schema.yaml`; exact export service boundary remains `TBD`. |
| Export profile | A GLB/glTF profile is required before implementation; target profile fields follow DEL-17-02. |
| Geometry coverage | Centerline, pipe segment, component, support marker, equipment interface, annotation, and load-case visual coverage remain `TBD` by entity family. |
| Visual fidelity | Review geometry may be simplified. It shall not be described as solver-fidelity, analysis-fidelity, or CAD/manufacturing fidelity. |
| Identity metadata | glTF `name`, `extras`, or extensions may be candidates for direct identity metadata; final direct-versus-sidecar policy remains `TBD`. |
| Sidecar identity map | Required when direct glTF metadata is insufficient, stripped by consuming tools, or not appropriate for a canonical ID family. |
| Coordinate conversion | Source-to-glTF axis/origin/scale conversion rules remain `TBD` until the profile declares the source coordinate policy and target transform. |
| Units | Linear geometry emitted to glTF must resolve to meters or carry explicit conversion diagnostics. |
| Private/protected data | Exported metadata and sidecars must not contain private project data, protected standards content, proprietary catalog values, owner criteria, or copied commercial examples unless separately rights-cleared. |

#### Construction

The DEL-17-08 export package concept should include, at contract level:

| Package member | Role | Phase A status |
|---|---|---|
| `model.glb` or `model.gltf` | Visual review geometry target artifact | `TBD` exact filename and profile default |
| `review_geometry_profile.json` | Declares target family, glTF version basis, coordinate/unit policy, visual entity coverage, identity policy, and boundary notes | `TBD` schema/location; no schema edit in this phase |
| `id_map.json` | Maps canonical IDs to glTF nodes, meshes, primitives, metadata fields, or omitted entries | Required by DEL-17-02; exact fields `TBD` |
| `export_manifest.json` | Lists package members, source model reference/hash basis, profile, diagnostics, and boundary notes | Required by DEL-17-02; exact fields `TBD` |
| `loss_report.json` and/or `loss_report.md` | Records exported, omitted, approximated, delegated, unsupported, and `TBD` review-geometry behavior | Required by DEL-17-02; exact rendering `TBD` |
| Geometry fixtures | Invented or public-permissive fixtures for deterministic checks | `TBD`; no fixtures created in Phase A |

##### Future Data Slots

These slots remain descriptive records, not implementation authority. They are kept as `TBD` until a later profile, schema, or fixture task supplies source-grounded values.

| Slot ID | Future record | Source reread evidence | Phase A disposition |
|---|---|---|---|
| B-001 | Exact package filenames, schema or storage locations, and field sets for `review_geometry_profile.json`, `id_map.json`, manifest, and loss report. | DEL-17-02 Datasheet `## Contract Objects`, `## Required Export-Profile Fields`; DEL-17-02 Specification `## Export Package Requirements`, `## Stable ID Map Requirements`, `## Manifest Requirements`, `## Loss Report Requirements`. | Converted to `TBD`; Construction remains the descriptive inventory. |
| F-002 | Future fixture inventory, fixture rights basis, and fixture-to-check coverage. | IP-DATA `## Public Repository Boundary`; DEL-17-01 Datasheet `## Boundary Facts`; DEL-17-02 Guidance `## Boundary Guidance`. | Converted to `TBD`; no fixtures are created in Phase A. |
| X-002 | Canonical ID families and schema source for emitted and intentionally omitted review entities. | DEL-17-02 Datasheet `## Stable ID Families`; PLAN-EXPORT-INTEROP `## Stable ID Strategy`; `schemas/model.schema.yaml` top-level description. | Converted to `TBD`; canonical family list is not enumerated locally until the source schema/profile boundary is selected. |

#### References

| Source ID | Source |
|---|---|
| GLTF-2.0 | Khronos glTF 2.0 specification, `https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html` |
| PLAN-EXPORT-INTEROP | `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` |
| DEL-17-01 | `DEL-17-01_CAEPIPE and export-format source basis` four-document kit and `Source_Basis_Register.md` |
| DEL-17-02 | `DEL-17-02_Export package, profile, and stable ID map contracts` four-document kit |
| CONTRACT | `docs/CONTRACT.md` |
| IP-DATA | `docs/IP_AND_DATA_BOUNDARY.md` |
| SPEC / TYPES | `docs/SPEC.md`, `docs/TYPES.md` |
| MODEL-SCHEMA | `schemas/model.schema.yaml` |

## Component: execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export/Guidance.md

### Guidance: DEL-17-08 GLB/glTF review geometry export

#### Purpose

Use DEL-17-08 to define a narrow visual-review export surface. The useful outcome is a GLB/glTF artifact that lets a user inspect model shape and correlate visible objects back to OpenPipeStress canonical IDs. The export is not a solver model, not an analysis result, not a compatibility claim, and not professional acceptance evidence.

#### Principles

##### Keep visual review separate from solver meaning

GLB/glTF is useful because it is lightweight and broadly viewable. That is also why the boundary needs to be explicit: a visible pipe-like shape does not prove that wall properties, support behavior, branch flexibility, load cases, stress recovery, rule-pack inputs, or target-solver interpretation are complete.

When the exporter emits simplified geometry, describe it as review geometry. If the visual representation drops support/restraint details, component semantics, private metadata, or user rule context, record the loss rather than implying the target file carries those meanings.

##### Preserve identity before appearance polish

The review artifact is only useful to OpenPipeStress workflows if visible objects can be traced back to the canonical model. Prefer stable canonical IDs over display-order assumptions. Use direct metadata only where the profile says it is reliable enough; otherwise pair the geometry artifact with a sidecar ID map and reference it from the manifest.

For E-002, "reliable enough" means the future profile has source-grounded consumer-risk criteria for the selected metadata location, including whether the receiving workflow may ignore, alter, or strip the metadata. Until that profile threshold exists, direct metadata remains a candidate and sidecar mapping remains the auditable fallback.

Do not rely on glTF indices or generated names as the only identity layer unless the loss report records the limitation and the profile accepts it for the selected use.

##### Make target behavior explicit

The profile should say what is emitted and what is not. This is especially important for supports, restraints, components, equipment interfaces, and annotations, where a visual marker may communicate less than the source model knows.

Unresolved behavior remains `TBD`; it should not be softened into phrases such as "supported by default" or "compatible with viewers" unless a later source-grounded profile and test set support that wording.

##### Keep data boundaries visible

GLB/glTF metadata and sidecars can accidentally expose private project names, owner criteria, component tags, rule-pack notes, or proprietary catalog data. The review-geometry profile should distinguish user-private metadata from public fixture metadata and should default public examples to invented or rights-cleared data only.

#### Considerations

| Topic | Guidance |
|---|---|
| Coordinate policy | glTF uses a right-handed +Y-up coordinate basis and meters for linear distances. Source model axes, project vertical axis, origin, scale, and transform recording remain profile decisions. |
| Geometry level of detail | First coverage may be centerline-only, simplified tube/symbol geometry, or another declared subset. The choice remains `TBD` and should be loss-report driven. |
| Metadata placement | glTF `extras` and object `name` fields are candidate places for direct review metadata. A sidecar remains necessary when metadata needs stronger auditability or may be stripped by consuming tools. |
| Extensions | Avoid required custom extensions unless the profile records viewer impact and fallback behavior. Extensions used by an asset must be declared according to GLTF-2.0. |
| Hashing | GLB is binary. The manifest should hash the emitted binary when deterministic or record why a hash cannot be stable. |
| Fixtures | Public fixtures must be invented or rights-cleared and should avoid real project/client/tag data. |
| Viewer behavior | Viewer-specific rendering, selection, metadata display, and stripping behavior remain `TBD`; do not claim viewer compatibility in Phase A. |

For E-001, viewer-specific behavior should be treated as evidence-dependent wording. A later profile may name viewer behavior only after source-grounded or test-recorded evidence exists; until then, guidance stays limited to review intent and metadata-risk caution.

#### Trade-offs

| Option | Benefit | Cost or risk | Phase A position |
|---|---|---|---|
| Centerline-only line primitives | Simple, compact, easy to correlate with line/element IDs | May be mistaken for incomplete physical geometry or omit component volume | `TBD`; acceptable candidate only with clear loss report |
| Simplified tube/surface primitives | More inspectable visually | Requires more geometry generation and may imply false dimensional fidelity | `TBD`; must be labeled review geometry |
| Direct `extras` metadata | Keeps identity near the visible object | Some tools may ignore or strip metadata; schema remains target-specific | Candidate, not final policy |
| Sidecar ID map | Stronger audit trail and stable identity contract | Requires consumers to keep files together | Required fallback and likely package member |
| Required custom extension | Can structure metadata explicitly | Reduces viewer portability and requires extension governance | Defer unless later profile justifies it |

##### Geometry Detail Rationale

For D-002, a later profile should choose the first review-geometry level of detail by asking whether the representation supports visual orientation, canonical-ID correlation, and limitation disclosure without implying solver, CAD, fabrication, or analysis fidelity. Centerline, simplified tube/surface, symbol, annotation, and overlay choices should be justified by coverage, identity, viewer-risk, package size, deterministic generation, and loss-report clarity; unchosen or unresolved families remain `TBD`.

#### Examples

No example model, GLB file, glTF JSON snippet, proprietary fixture, commercial target file, or standards-derived engineering example is included in Phase A.

Acceptable future examples shall be invented or rights-cleared and shall demonstrate only:

- a visible review entity correlated to a canonical ID;
- an omitted entity recorded in the ID map or loss report;
- a coordinate/unit diagnostic;
- a manifest entry for a GLB/glTF artifact.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified in Phase A. Remaining open items are `TBD`, not conflicts. | N/A | N/A | N/A | N/A | N/A |

## Component: execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export/Procedure.md

### Procedure: DEL-17-08 GLB/glTF review geometry export

#### Purpose

This procedure defines how to develop and review the GLB/glTF review-geometry export contract without crossing into implementation, solver-fidelity, target-compatibility, release, code-compliance, or professional-acceptance claims.

#### Prerequisites

Before implementation or later enrichment of DEL-17-08, confirm:

1. DEL-17-01 remains the admitted PKG-17 source-basis authority for GLB/glTF review-geometry boundaries.
2. DEL-17-02 remains the common export package/profile/stable-ID/loss-report contract.
3. The GLB/glTF profile has a cited GLTF-2.0 version basis.
4. The source model identity, unit policy, coordinate policy, and canonical ID families are available from project-owned schema/contracts.
5. The write scope authorizes the target files being changed.
6. Public fixtures, if any, are invented or rights-cleared and contain no private project data, protected standards content, proprietary catalog values, owner criteria, or commercial examples.

Declared upstream dependencies for this deliverable are `DEL-17-02`, `DEL-02-01`, `DEL-07-01`, `DEL-13-04`, and `DEL-15-01`; those dependencies do not authorize implementation or claims by themselves.

#### Steps

##### Phase A document population

1. Read the deliverable-local truth set: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `MEMORY.md`.
2. Read AGENTS/TASK/ORCHESTRATOR/four-documents instructions.
3. Read DEL-17-01 and DEL-17-02 four-document kits and DEL-17-01 source-basis records.
4. Read project governance and technical references: `docs/CONTRACT.md`, `docs/IP_AND_DATA_BOUNDARY.md`, `docs/SPEC.md`, `docs/TYPES.md`, `schemas/model.schema.yaml`, and `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md`.
5. Read the Khronos glTF 2.0 source slices for asset structure, coordinate/units convention, GLB container behavior, mesh primitive modes, nodes, extensions, and `extras` metadata.
6. Populate the four documents at contract level only.
7. Preserve `TBD` entries for unresolved geometry coverage, identity metadata placement, sidecar schema, filename/profile defaults, coordinate transform, fixture behavior, and viewer behavior.
8. Do not update `MEMORY.md` in Phase A.
9. Create or update the run record in `_run_records/`.
10. If the four documents exist and `_STATUS.md` is `OPEN`, perform the safe status transition to `INITIALIZED`.

##### Future profile-development procedure

1. Declare the review-geometry export profile ID, version, glTF target version basis, and package member inventory.
2. Declare whether the target artifact is `.glb`, `.gltf`, or both.
3. Declare the source coordinate basis, glTF transform, origin policy, and meter conversion policy.
4. Declare the first review-geometry entity coverage by canonical family.
5. For each family, classify behavior as exported, omitted, approximated, delegated, unsupported, or `TBD`.
6. Select direct identity metadata locations only when the profile documents the glTF target object and consumer-risk policy.
7. Define sidecar ID-map behavior for every canonical ID that cannot be carried directly or reliably in the GLB/glTF artifact.
8. Define manifest and loss-report entries before writing the target artifact.
9. Define diagnostics for missing units, ambiguous coordinate systems, duplicate IDs, invalid geometry, unmapped emitted entities, and private/protected metadata exposure.
10. Use only invented or rights-cleared fixtures for future deterministic checks.

##### Future export-package review procedure

1. Confirm every emitted review entity has a canonical ID or an explicit unmapped/omitted record.
2. Confirm every target artifact is listed in the manifest.
3. Confirm geometry limitations appear in the loss report.
4. Confirm GLB/glTF target facts are limited to GLTF-2.0 source evidence and selected profile behavior.
5. For D-001, confirm timestamp or generator metadata policy is declared as deterministic, normalized, omitted, or intentionally runtime-dependent before package acceptance.
6. For E-003, confirm binary GLB and other non-JSON package members have hashes or an explicit, manifest-recorded reason why a hash is unavailable.
7. Confirm no statement implies solver readiness, analysis fidelity, target compatibility, formal validation, code compliance, release readiness, or professional acceptance.

#### Verification

Run from repository root for this Phase A task:

```bash
tools/validation/check_four_documents.sh "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export"
tools/validation/check_min_viable_fileset.sh "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export"
git diff --check -- "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export"
```

Manual review should confirm:

- all non-trivial claims are source-grounded or marked `TBD`;
- GLB/glTF remains visual review geometry only;
- identity is preserved through metadata or sidecars without relying only on display order;
- unresolved behavior remains `TBD`;
- no proprietary examples, copied protected standards data, implementation code, schema edits, compatibility claims, release claims, formal validation claims, code-compliance claims, or professional claims were added.

#### Records

Phase A records are:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-18_1156.md`

Future records remain `TBD` and may include a profile artifact, manifest, ID map, loss report, diagnostics, generated GLB/glTF artifact, and invented fixtures only when a later task explicitly authorizes those writes.

## Component: execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export/Specification.md

### Specification: DEL-17-08 GLB/glTF review geometry export

#### Scope

DEL-17-08 defines the Phase A contract for exporting GLB/glTF review geometry from OpenPipeStress model data. The export is for lightweight visual inspection, review context, and stable identity correlation back to canonical model entities.

This deliverable does not implement a writer, parser, schema, GUI view, fixture set, API endpoint, release path, compatibility profile, external-tool certification, solver geometry, stress analysis handoff, code-compliance process, or professional acceptance workflow.

#### Requirements

##### Source and Boundary Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-001 | The review-geometry export shall consume DEL-17-01 as the source-basis authority for GLB/glTF boundary claims. |
| DEL-17-08-REQ-002 | The review-geometry export shall consume DEL-17-02 for export package, profile, stable-ID map, manifest, and loss-report behavior. |
| DEL-17-08-REQ-003 | Target behavior not confirmed by GLTF-2.0, DEL-17-01, DEL-17-02, or project governance sources shall remain `TBD`. |
| DEL-17-08-REQ-004 | The export shall be described only as visual review geometry and shall not be represented as solver-fidelity geometry, analysis-fidelity geometry, formal validation evidence, code-compliance evidence, release readiness, target compatibility, or professional acceptance. |
| DEL-17-08-REQ-005 | The export shall not include protected standards text, protected tables, private project data, proprietary target examples, owner criteria, copied commercial files, or undocumented proprietary behavior. |

##### glTF/GLB Format Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-010 | A GLB/glTF review-geometry profile shall declare the glTF version basis and whether the emitted target is `.glb`, `.gltf`, or both. |
| DEL-17-08-REQ-011 | A glTF asset shall include the required `asset.version` field required by GLTF-2.0. |
| DEL-17-08-REQ-012 | Linear geometry emitted into glTF shall use meters or shall produce a blocking diagnostic before target writing. |
| DEL-17-08-REQ-013 | The profile shall declare the source coordinate basis, target glTF basis, and transform policy, including the glTF +Y-up/right-handed convention. |
| DEL-17-08-REQ-014 | Mesh primitive topology choices shall be profile-declared. Candidate modes include line-style centerline review geometry and triangle-style surface preview geometry; the selected subset remains `TBD`. |
| DEL-17-08-REQ-015 | Use of glTF extensions, if any, shall follow the GLTF-2.0 extension declaration mechanism and shall remain optional unless a later profile explicitly records the viewer impact. |

##### Identity and Metadata Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-020 | The exporter shall preserve stable canonical identity for every emitted or intentionally omitted review-geometry entity. |
| DEL-17-08-REQ-021 | Direct glTF metadata may use `name`, `extras`, or a declared extension only when the profile records the target location and stripping/consumer-risk policy. |
| DEL-17-08-REQ-022 | A sidecar ID map shall be emitted when direct glTF metadata is unavailable, insufficient, not profile-approved, or not reliable for a receiving workflow. |
| DEL-17-08-REQ-023 | The ID map shall distinguish canonical OpenPipeStress IDs from glTF node indices, mesh indices, primitive indices, generated display names, and sidecar row IDs. |
| DEL-17-08-REQ-024 | Omitted canonical entities shall appear in the ID map or loss report with omission reason, affected canonical ID, severity, and downstream implication. |

##### Export Package Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-030 | A review-geometry export package shall include or reference a manifest, ID map, loss report, diagnostics, and the emitted GLB/glTF artifact. |
| DEL-17-08-REQ-031 | The manifest shall record source model identity, export profile identity, package member inventory, source-basis references, and boundary notes. |
| DEL-17-08-REQ-032 | The loss report shall classify each material review-geometry limitation as exported, omitted, approximated, delegated, unsupported, or `TBD`. |
| DEL-17-08-REQ-033 | Binary GLB or non-JSON package members shall record a hash or explain why a hash is unavailable. |
| DEL-17-08-REQ-034 | Timestamp or generator metadata shall be declared as deterministic, normalized, omitted, or intentionally runtime-dependent. |
| DEL-17-08-REQ-035 | The review-geometry profile shall carry DEL-17-01, DEL-17-02, and GLTF-2.0 source-basis references; missing references shall block package acceptance. |

##### Review Geometry Coverage Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-040 | The profile shall declare which canonical entity families are visually emitted, omitted, approximated, unsupported, or `TBD`. |
| DEL-17-08-REQ-041 | Centerline segments, bends, branches, reducers, components, supports/restraints, equipment interfaces, line labels, material/section labels, load-case indicators, and diagnostics overlays remain `TBD` until the profile selects first coverage. |
| DEL-17-08-REQ-042 | Simplified review shapes shall be recorded as approximations when they replace richer canonical model geometry. |
| DEL-17-08-REQ-043 | Missing units, ambiguous coordinate systems, duplicate stable IDs, zero-length geometry, impossible bend display geometry, and unmapped emitted entities shall produce blocking diagnostics before package acceptance. |

#### Standards

| Standard or source | Use | Boundary |
|---|---|---|
| Khronos glTF 2.0 specification | Public target-format reference for asset structure, coordinate/unit convention, GLB container behavior, nodes, meshes, primitive modes, extensions, and `extras` metadata slots | Not a piping stress, solver, code-compliance, or professional-review standard |
| OpenPipeStress CONTRACT | Binding project invariants for IP/data boundary, no hidden defaults, no professional authority claims, and sealed TASK execution | Governance source, not legal or professional advice |
| DEL-17-02 common export contract | Required package/profile/stable-ID/loss-report basis for PKG-17 target exporters | Contract-level only in this Phase A task |

#### Verification

Phase A verification is document and boundary verification only:

| Check | Expected result |
|---|---|
| Four-document kit exists | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present. |
| Default section check | Each document retains its required default schema sections. |
| Source grounding | Claims cite GLTF-2.0, DEL-17-01, DEL-17-02, PLAN-EXPORT-INTEROP, or governance/schema sources. |
| TBD preservation | Unresolved identity metadata, geometry coverage, filename/profile/schema, coordinate transform, and fixture behavior remain `TBD`. |
| Boundary check | No proprietary examples, protected standards data, implementation code, schema edits, compatibility claims, release claims, formal validation claims, code-compliance claims, or professional claims. |

Future implementation verification remains `TBD` and shall not be inferred from this Phase A document kit. Candidate future checks include glTF asset-structure validation, GLB container checks, deterministic package-member hashing, geometry count checks, stable-ID round-trip correlation, and visual review fixture comparison using invented or rights-cleared fixtures.

##### Future Requirement-to-Check Map

This map records future acceptance slots only. It does not close the underlying `TBD` profile, implementation, fixture, or viewer-behavior decisions.

| Item ID | Requirement area | Future check slot | Source reread evidence | Phase A disposition |
|---|---|---|---|---|
| A-001 | DEL-17-08 `shall` requirements across profile, identity, package, and coverage requirements. | Build an explicit req-to-check matrix before implementation acceptance. | Current `Specification.md` `## Requirements` and `## Verification`; DEL-17-02 Specification `## Export Package Requirements` through `## Loss Report Requirements`. | Incorporated as future acceptance mapping; pass criteria remain `TBD`. |
| C-001 | Direct identity metadata versus sidecar identity policy. | Decide when glTF `name`, `extras`, or extensions are sufficient and when manifest-referenced sidecar ID mapping is mandatory. | GLTF-2.0 sections 3.3, 3.12, 5.16, 5.23-5.25; DEL-17-02 Datasheet `## Stable ID Families`; DEL-17-02 Guidance `### Stable ID map`. | Converted to `TBD`; profile must define consumer-risk threshold before direct metadata is accepted. |
| C-002 | Export service boundary and trigger/interface. | Identify the application-service/API boundary that consumes the canonical model and invokes the writer. | `_CONTEXT.md` Architecture Basis Injection; SOFTWARE_DECOMP SOW-030 and SOW-062; current `Specification.md` `## Scope`. | Already excluded from Phase A; retained as `TBD` for a later interface contract. |
| F-001 | Source-evidence gate for target profile facts. | Verify each GLB/glTF target fact traces to GLTF-2.0, DEL-17-01, DEL-17-02, or governance evidence. | DEL-17-01 Specification `## Source Authority Requirements`; DEL-17-02 Specification `## Source Authority Requirements`; GLTF-2.0 sections 2.4, 3.4, 4, 5.9, 5.16, 5.23-5.25. | Incorporated as future source-evidence check. |
| X-001 | First review-geometry coverage declaration by canonical entity family. | Check each family is classified as emitted, omitted, approximated, delegated, unsupported, or `TBD`. | DEL-17-02 Datasheet `## Required Export-Profile Fields`, `## Loss Categories`; DEL-17-02 Specification `## Export Profile Requirements`; current `Specification.md` `### Review Geometry Coverage Requirements`. | Already required by REQ-040/REQ-041; disposition recorded here with `TBD` coverage. |
| X-003 | Implementation verification for generated artifacts. | Define future checks for glTF asset structure, GLB container, deterministic hashing, geometry counts, stable-ID correlation, and invented fixture comparison. | GLTF-2.0 sections 3.2, 3.4, 4, 5.9, 5.23-5.25; DEL-17-02 Specification `## Export Package Requirements`; PLAN-EXPORT-INTEROP `Validation and Confidence Building`. | Incorporated as future implementation-verification slot; no pass thresholds are invented. |

#### Documentation

This deliverable produces only:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` safe lifecycle update when permitted
- `_run_records/TASK_RUN_2026-05-18_1156.md`

No code, schema, fixture, export profile file, manifest schema, ID-map schema, public API, GUI artifact, or release documentation is authorized in Phase A.
