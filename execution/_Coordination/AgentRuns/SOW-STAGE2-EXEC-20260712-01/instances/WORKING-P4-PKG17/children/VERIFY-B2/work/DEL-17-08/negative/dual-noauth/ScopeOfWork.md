---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-17-08
package_id: PKG-17
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@e8f59a63372f38d9e788ac39b39995558f5aba73
project_scope_refs: [SOW-030, SOW-074]
package_objective_refs: [OBJ-009, OBJ-017]
---

# Scope of Work — DEL-17-08

## Purpose and Objective Traceability

This migration candidate defines `DEL-17-08` in service of project scope [SOW-030, SOW-074] and package objectives [OBJ-009, OBJ-017].

- **OUT-001** — A deterministic GLB/glTF review-geometry export contract that preserves model identity and visual-review boundaries without implying solver fidelity is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-17-08 GLB/glTF review geometry export

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-001"} -->
#### Datasheet: DEL-17-08 GLB/glTF review geometry export

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-08-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":12,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-003"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":39,"line_start":26,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Target family | GLB/glTF review geometry | `_CONTEXT.md`; SOFTWARE_DECOMP DEL-17-08; PLAN-EXPORT-INTEROP Geometry Exchange |
| Primary output intent | Lightweight 3D visual inspection and review context | PLAN-EXPORT-INTEROP Geometry Exchange |
| Non-authority boundary | Geometry-only review aid; not solver geometry, analysis proof, formal validation, code compliance, release readiness, or professional acceptance | DEL-17-01 F-17-01-005; DEL-17-02 Boundary Requirements; CONTRACT OPS-K-AUTH-1 |
| Format basis | Khronos glTF 2.0 public specification | GLTF-2.0, sections 2.4, 3.4, 4.2-4.4, and 5.24-5.25 |
| Binary container | Binary `.glb` remains outside the selected bounded profile. | `DEC-074` O11/E7 |
| Selected JSON profile | `model.gltf` with embedded buffer data, line-mode centerline segments, direct identity `extras`, and authoritative `id_map.json`. | Current implementation; `DEC-074` O11/E7 |
| Coordinate and unit basis | glTF is right-handed, +Y-up, and uses meters for linear distances | GLTF-2.0 section 3.4 |
| Stable identity basis | Canonical OpenPipeStress IDs must be preserved directly through target metadata where supported or through a manifest-referenced sidecar | DEL-17-02 stable ID map requirements |
| Loss reporting | Required even for successful review-geometry exports | DEL-17-02 loss report requirements |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":54,"line_start":40,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-005"} -->
##### Conditions

| Condition | Phase A disposition |
|---|---|
| Input source model | Canonical model surface from `schemas/model.schema.yaml`; exact export service boundary remains `TBD`. |
| Export profile | `gltf_json_embedded_buffer`, `LINES`, and `centerline_segments_only` are selected; GLB and broader profiles remain unselected. |
| Geometry coverage | Centerline segments are emitted; broader components, supports, equipment, annotations, overlays, and surface/tube geometry remain outside the selected profile. |
| Visual fidelity | Review geometry may be simplified. It shall not be described as solver-fidelity, analysis-fidelity, or CAD/manufacturing fidelity. |
| Identity metadata | Selected centerline entities carry canonical refs in node and primitive `extras`; no extension or viewer behavior is claimed. |
| Sidecar identity map | Always authoritative in the selected profile; one-to-one correlation with emitted node/primitive identity is blocking-validated and round-trip tested. |
| Timestamp/generator behavior | Current output has a fixed versioned generator and omits timestamps. PDU-031 exact normative policy remains owner-unselected. |
| Coordinate conversion | Source-to-glTF axis/origin/scale conversion rules remain `TBD` until the profile declares the source coordinate policy and target transform. |
| Units | Linear geometry emitted to glTF must resolve to meters or carry explicit conversion diagnostics. |
| Private/protected data | Exported metadata and sidecars must not contain private project data, protected standards content, proprietary catalog values, owner criteria, or copied commercial examples unless separately rights-cleared. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":67,"line_start":55,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-006"} -->
##### Construction

The DEL-17-08 export package concept should include, at contract level:

| Package member | Role | Phase A status |
|---|---|---|
| `model.gltf` | Selected JSON glTF visual review geometry artifact | Implemented; binary `model.glb` remains unselected |
| Embedded export profile | Declares JSON glTF 2.0, line-mode centerlines, coordinate/unit policy, identity policy, and boundary notes | Implemented in the package record |
| `id_map.json` | Maps canonical centerline IDs to glTF node indices and remains authoritative | Implemented and round-trip validated |
| `manifest.json` | Lists package members, source model reference/hash basis, profile, diagnostics, and boundary notes | Implemented |
| `loss_report.json` and/or `loss_report.md` | Records exported, omitted, approximated, delegated, unsupported, and `TBD` review-geometry behavior | Required by DEL-17-02; exact rendering `TBD` |
| Geometry fixtures | Invented or public-permissive fixtures for deterministic checks | `TBD`; no fixtures created in Phase A |

<!-- sow-source-end -->

### CLM-007 — Future Data Slots

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":77,"line_start":68,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-007"} -->
###### Future Data Slots

These slots remain descriptive records, not implementation authority. They are kept as `TBD` until a later profile, schema, or fixture task supplies source-grounded values.

| Slot ID | Future record | Source reread evidence | Phase A disposition |
|---|---|---|---|
| B-001 | Exact package filenames, schema or storage locations, and field sets for `review_geometry_profile.json`, `id_map.json`, manifest, and loss report. | DEL-17-02 Datasheet `## Contract Objects`, `## Required Export-Profile Fields`; DEL-17-02 Specification `## Export Package Requirements`, `## Stable ID Map Requirements`, `## Manifest Requirements`, `## Loss Report Requirements`. | Converted to `TBD`; Construction remains the descriptive inventory. |
| F-002 | Future fixture inventory, fixture rights basis, and fixture-to-check coverage. | IP-DATA `## Public Repository Boundary`; DEL-17-01 Datasheet `## Boundary Facts`; DEL-17-02 Guidance `## Boundary Guidance`. | Converted to `TBD`; no fixtures are created in Phase A. |
| X-002 | Canonical ID families and schema source for emitted and intentionally omitted review entities. | DEL-17-02 Datasheet `## Stable ID Families`; PLAN-EXPORT-INTEROP `## Stable ID Strategy`; `schemas/model.schema.yaml` top-level description. | Converted to `TBD`; canonical family list is not enumerated locally until the source schema/profile boundary is selected. |

<!-- sow-source-end -->

### CLM-008 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":91,"line_start":78,"source_sha256":"5b7ff61903ebc73e80c75a56962aa74f0912689cbd1114d9066abc73d6d96dea","target_id":"CLM-008"} -->
##### References

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

PDU-036 evidence state: emitted-entity mapping completeness is checked only for current JSON line geometry; impossible-bend, GLB, viewer, and broader geometry diagnostics remain outside O11 scope and unvalidated.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-009 — Specification: DEL-17-08 GLB/glTF review geometry export

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-009"} -->
#### Specification: DEL-17-08 GLB/glTF review geometry export

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-010 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-010"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-08-ACC-005`, `DEL-17-08-DECL-001`, `DEL-17-08-EXC-001`, `DEL-17-08-EXC-002`.

<!-- sow-source-end -->

### CLM-011 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":17,"line_start":12,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-011"} -->
##### Scope

DEL-17-08 defines and implements a bounded JSON `.gltf` review-geometry profile for lightweight visual inspection, review context, and stable identity correlation back to canonical model entities. Under `DEC-074` O11/E7, the selected profile remains JSON glTF with embedded buffer data, line-mode centerline segments, direct `extras`, and an authoritative sidecar ID map.

This bounded profile does not select or imply binary GLB, broad geometry coverage, viewer compatibility, engineering validation, an API endpoint, release path, external-tool certification, solver geometry, stress analysis handoff, code-compliance process, or professional acceptance workflow.

<!-- sow-source-end -->

### CLM-012 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":19,"line_start":18,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-012"} -->
##### Requirements

<!-- sow-source-end -->

### CLM-013 — Source and Boundary Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":29,"line_start":20,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-013"} -->
###### Source and Boundary Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-001 | The review-geometry export shall consume DEL-17-01 as the source-basis authority for GLB/glTF boundary claims. |
| DEL-17-08-REQ-002 | The review-geometry export shall consume DEL-17-02 for export package, profile, stable-ID map, manifest, and loss-report behavior. |
| DEL-17-08-REQ-003 | Target behavior not confirmed by GLTF-2.0, DEL-17-01, DEL-17-02, or project governance sources shall remain `TBD`. |
| DEL-17-08-REQ-004 | The export shall be described only as visual review geometry and shall not be represented as solver-fidelity geometry, analysis-fidelity geometry, formal validation evidence, code-compliance evidence, release readiness, target compatibility, or professional acceptance. |
| DEL-17-08-REQ-005 | The export shall not include protected standards text, protected tables, private project data, proprietary target examples, owner criteria, copied commercial files, or undocumented proprietary behavior. |

<!-- sow-source-end -->

### CLM-014 — glTF/GLB Format Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":40,"line_start":30,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-014"} -->
###### glTF/GLB Format Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-010 | A GLB/glTF review-geometry profile shall declare the glTF version basis and whether the emitted target is `.glb`, `.gltf`, or both. |
| DEL-17-08-REQ-011 | A glTF asset shall include the required `asset.version` field required by GLTF-2.0. |
| DEL-17-08-REQ-012 | Linear geometry emitted into glTF shall use meters or shall produce a blocking diagnostic before target writing. |
| DEL-17-08-REQ-013 | The profile shall declare the source coordinate basis, target glTF basis, and transform policy, including the glTF +Y-up/right-handed convention. |
| DEL-17-08-REQ-014 | Mesh primitive topology choices shall be profile-declared. Candidate modes include line-style centerline review geometry and triangle-style surface preview geometry; the selected subset remains `TBD`. |
| DEL-17-08-REQ-015 | Use of glTF extensions, if any, shall follow the GLTF-2.0 extension declaration mechanism and shall remain optional unless a later profile explicitly records the viewer impact. |

<!-- sow-source-end -->

### CLM-015 — Identity and Metadata Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":50,"line_start":41,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-015"} -->
###### Identity and Metadata Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-020 | Within the selected centerline JSON glTF profile, every emitted entity shall round trip one-to-one between canonical identity in node/primitive `extras` and the authoritative sidecar ID map; intentionally omitted entities remain represented through the loss report. |
| DEL-17-08-REQ-021 | Direct glTF metadata may use `name`, `extras`, or a declared extension only when the profile records the target location and stripping/consumer-risk policy. |
| DEL-17-08-REQ-022 | A sidecar ID map shall be emitted when direct glTF metadata is unavailable, insufficient, not profile-approved, or not reliable for a receiving workflow. |
| DEL-17-08-REQ-023 | The ID map shall distinguish canonical OpenPipeStress IDs from glTF node indices, mesh indices, primitive indices, generated display names, and sidecar row IDs. |
| DEL-17-08-REQ-024 | Omitted canonical entities shall appear in the ID map or loss report with omission reason, affected canonical ID, severity, and downstream implication. |

<!-- sow-source-end -->

### CLM-016 — Export Package Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":61,"line_start":51,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-016"} -->
###### Export Package Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-030 | A review-geometry export package shall include or reference a manifest, ID map, loss report, diagnostics, and the emitted GLB/glTF artifact. |
| DEL-17-08-REQ-031 | The manifest shall record source model identity, export profile identity, package member inventory, source-basis references, and boundary notes. |
| DEL-17-08-REQ-032 | The loss report shall classify each material review-geometry limitation as exported, omitted, approximated, delegated, unsupported, or `TBD`. |
| DEL-17-08-REQ-033 | Binary GLB or non-JSON package members shall record a hash or explain why a hash is unavailable. |
| DEL-17-08-REQ-034 | The current bounded implementation uses a fixed versioned generator string and emits no timestamp. The exact normative timestamp/generator policy remains owner-unselected under PDU-031 and shall not be invented by implementation evidence. |
| DEL-17-08-REQ-035 | The review-geometry profile shall carry DEL-17-01, DEL-17-02, and GLTF-2.0 source-basis references; missing references shall block package acceptance. |

<!-- sow-source-end -->

### CLM-017 — Review Geometry Coverage Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":70,"line_start":62,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-017"} -->
###### Review Geometry Coverage Requirements

| Req ID | Requirement |
|---|---|
| DEL-17-08-REQ-040 | The profile shall declare which canonical entity families are visually emitted, omitted, approximated, unsupported, or `TBD`. |
| DEL-17-08-REQ-041 | Centerline segments, bends, branches, reducers, components, supports/restraints, equipment interfaces, line labels, material/section labels, load-case indicators, and diagnostics overlays remain `TBD` until the profile selects first coverage. |
| DEL-17-08-REQ-042 | Simplified review shapes shall be recorded as approximations when they replace richer canonical model geometry. |
| DEL-17-08-REQ-043 | Missing units, ambiguous coordinate systems, duplicate stable IDs, zero-length geometry, impossible bend display geometry, and unmapped emitted entities shall produce blocking diagnostics before package acceptance. |

<!-- sow-source-end -->

### CLM-018 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":78,"line_start":71,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-018"} -->
##### Standards

| Standard or source | Use | Boundary |
|---|---|---|
| Khronos glTF 2.0 specification | Public target-format reference for asset structure, coordinate/unit convention, GLB container behavior, nodes, meshes, primitive modes, extensions, and `extras` metadata slots | Not a piping stress, solver, code-compliance, or professional-review standard |
| OpenPipeStress CONTRACT | Binding project invariants for IP/data boundary, no hidden defaults, no professional authority claims, and sealed TASK execution | Governance source, not legal or professional advice |
| DEL-17-02 common export contract | Required package/profile/stable-ID/loss-report basis for PKG-17 target exporters | Contract-level only in this Phase A task |

<!-- sow-source-end -->

### CLM-019 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":94,"line_start":79,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-019"} -->
##### Verification

Current bounded verification covers the selected JSON glTF profile only:

| Check | Expected result |
|---|---|
| Four-document kit exists | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present. |
| Default section check | Each document retains its required default schema sections. |
| Source grounding | Claims cite GLTF-2.0, DEL-17-01, DEL-17-02, PLAN-EXPORT-INTEROP, or governance/schema sources. |
| Stable-ID round trip | Written `model.gltf` node/primitive identity metadata and `id_map.json` round trip to the same canonical centerline IDs; mismatches block package acceptance. |
| Deterministic metadata observation | Repeated packages are byte-deterministic, `asset.generator` is a fixed versioned string, and timestamp keys are absent; no normative policy is inferred. |
| TBD preservation | Binary GLB, broader geometry, viewer compatibility, engineering validation, and exact timestamp/generator policy remain unselected. |
| Boundary check | No proprietary examples, protected standards data, compatibility claims, release claims, formal validation claims, code-compliance claims, or professional claims. |

Existing implementation verification covers JSON glTF structure, deterministic package-member hashing, geometry counts, stable-ID round-trip correlation, and invented fixtures. GLB container checks and rendered visual/viewer validation remain outside the selected profile and shall not be inferred.

<!-- sow-source-end -->

### CLM-020 — Future Requirement-to-Check Map

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":107,"line_start":95,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-020"} -->
###### Future Requirement-to-Check Map

This map records future acceptance slots only. It does not close the underlying `TBD` profile, implementation, fixture, or viewer-behavior decisions.

| Item ID | Requirement area | Future check slot | Source reread evidence | Phase A disposition |
|---|---|---|---|---|
| A-001 | DEL-17-08 `shall` requirements across profile, identity, package, and coverage requirements. | Build an explicit req-to-check matrix before implementation acceptance. | Current `Specification.md` `## Requirements` and `## Verification`; DEL-17-02 Specification `## Export Package Requirements` through `## Loss Report Requirements`. | Incorporated as future acceptance mapping; pass criteria remain `TBD`. |
| C-001 | Direct identity metadata versus sidecar identity policy. | Decide when glTF `name`, `extras`, or extensions are sufficient and when manifest-referenced sidecar ID mapping is mandatory. | GLTF-2.0 sections 3.3, 3.12, 5.16, 5.23-5.25; DEL-17-02 Datasheet `## Stable ID Families`; DEL-17-02 Guidance `### Stable ID map`. | Converted to `TBD`; profile must define consumer-risk threshold before direct metadata is accepted. |
| C-002 | Export service boundary and trigger/interface. | Identify the application-service/API boundary that consumes the canonical model and invokes the writer. | `_CONTEXT.md` Architecture Basis Injection; SOFTWARE_DECOMP SOW-030 and SOW-062; current `Specification.md` `## Scope`. | Already excluded from Phase A; retained as `TBD` for a later interface contract. |
| F-001 | Source-evidence gate for target profile facts. | Verify each GLB/glTF target fact traces to GLTF-2.0, DEL-17-01, DEL-17-02, or governance evidence. | DEL-17-01 Specification `## Source Authority Requirements`; DEL-17-02 Specification `## Source Authority Requirements`; GLTF-2.0 sections 2.4, 3.4, 4, 5.9, 5.16, 5.23-5.25. | Incorporated as future source-evidence check. |
| X-001 | First review-geometry coverage declaration by canonical entity family. | Check each family is classified as emitted, omitted, approximated, delegated, unsupported, or `TBD`. | DEL-17-02 Datasheet `## Required Export-Profile Fields`, `## Loss Categories`; DEL-17-02 Specification `## Export Profile Requirements`; current `Specification.md` `### Review Geometry Coverage Requirements`. | Already required by REQ-040/REQ-041; disposition recorded here with `TBD` coverage. |
| X-003 | Implementation verification for generated artifacts. | Verify the selected JSON glTF structure, deterministic hashing, geometry counts, and stable-ID correlation; add GLB or rendered visual checks only after separately selected scope. | GLTF-2.0 sections 3.2, 3.4, 5.9, 5.23-5.25; DEL-17-02 Specification `## Export Package Requirements`; `DEC-074` O11/E7. | JSON glTF checks are implemented; GLB, viewer, broader geometry, and engineering validation remain outside the selected scope. |

<!-- sow-source-end -->

### CLM-021 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":122,"line_start":108,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-021"} -->
##### Documentation

Current bounded implementation records include:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` safe lifecycle update when permitted
- `_run_records/TASK_RUN_2026-05-18_1156.md`
- `core/handoff/review_geometry/`, `schemas/review_geometry_export.schema.json`, invented fixtures, and focused tests;
- `_run_records/WORKING_ITEMS_RUN_2026-07-12_D41-R5-T2B-PDU029-PDU031.md`.

No binary GLB, broad geometry, viewer-compatibility, engineering-validation, public-API, GUI, or release work is authorized by this repair.

<!-- sow-source-end -->

### CLM-022 — D-41 R5 T4 PDU-036 O11 boundary

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":125,"line_start":123,"source_sha256":"9f72cc620f5bf9d1943e568a57502222a7569c2fcf91d6ff2640a801b4ea3f68","target_id":"CLM-022"} -->
##### D-41 R5 T4 PDU-036 O11 boundary

REQ-043 evidence is bounded to the selected JSON glTF line/centerline profile. Current emitted line entities require authoritative ID-map correlation. Impossible-bend display geometry is not present in this profile, so its specific diagnostic remains an explicit out-of-scope gap rather than an invented bend representation or validation claim.
<!-- sow-source-end -->

- **AC-001** — The contract preserves review-only geometry scope, canonical identity through metadata or sidecars, units and coordinate transforms, deterministic mesh/material/scene behavior, manifest and loss reporting, diagnostics, source/profile gates, invented or rights-cleared fixtures, and explicit TBDs without presenting geometry as an analysis model, fabrication model, or professional acceptance artifact.

## Production and Verification Method — Praxeology

### CLM-023 — Procedure: DEL-17-08 GLB/glTF review geometry export

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-023"} -->
#### Procedure: DEL-17-08 GLB/glTF review geometry export

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-024 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-024"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-08-DECL-004`.

<!-- sow-source-end -->

### CLM-025 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-025"} -->
##### Purpose

This procedure defines how to maintain and review the bounded JSON glTF centerline export without crossing into binary GLB, broader geometry, viewer compatibility, engineering validation, solver-fidelity, release, code-compliance, or professional-acceptance claims.

<!-- sow-source-end -->

### CLM-026 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":28,"line_start":16,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-026"} -->
##### Prerequisites

Before implementation or later enrichment of DEL-17-08, confirm:

1. DEL-17-01 remains the admitted PKG-17 source-basis authority for GLB/glTF review-geometry boundaries.
2. DEL-17-02 remains the common export package/profile/stable-ID/loss-report contract.
3. The GLB/glTF profile has a cited GLTF-2.0 version basis.
4. The source model identity, unit policy, coordinate policy, and canonical ID families are available from project-owned schema/contracts.
5. The write scope authorizes the target files being changed.
6. Public fixtures, if any, are invented or rights-cleared and contain no private project data, protected standards content, proprietary catalog values, owner criteria, or commercial examples.

Declared upstream dependencies for this deliverable are `DEL-17-02`, `DEL-02-01`, `DEL-07-01`, `DEL-13-04`, and `DEL-15-01`; those dependencies do not authorize implementation or claims by themselves.

<!-- sow-source-end -->

### CLM-027 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":30,"line_start":29,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-027"} -->
##### Steps

<!-- sow-source-end -->

### CLM-028 — Phase A document population

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":43,"line_start":31,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-028"} -->
###### Phase A document population

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

<!-- sow-source-end -->

### CLM-029 — Future profile-development procedure

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":56,"line_start":44,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-029"} -->
###### Future profile-development procedure

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

<!-- sow-source-end -->

### CLM-030 — Future export-package review procedure

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":66,"line_start":57,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-030"} -->
###### Future export-package review procedure

1. Confirm every emitted centerline entity has the same canonical ID in node `extras`, primitive `extras`, and exactly one authoritative sidecar row after deterministic write/read round trip; block mismatches.
2. Confirm every target artifact is listed in the manifest.
3. Confirm geometry limitations appear in the loss report.
4. Confirm GLB/glTF target facts are limited to GLTF-2.0 source evidence and selected profile behavior.
5. Confirm current output retains its fixed versioned generator and omits timestamps. Do not declare a normative timestamp/generator policy until the owner selects the exact PDU-031 policy.
6. For E-003, confirm binary GLB and other non-JSON package members have hashes or an explicit, manifest-recorded reason why a hash is unavailable.
7. Confirm no statement implies solver readiness, analysis fidelity, target compatibility, formal validation, code compliance, release readiness, or professional acceptance.

<!-- sow-source-end -->

### CLM-031 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":84,"line_start":67,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-031"} -->
##### Verification

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

<!-- sow-source-end -->

### CLM-032 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":98,"line_start":85,"source_sha256":"66cc1c1d0b25489394a5c2ef4186262b710fd3fc957fc7aefe41f4c5c3a2220d","target_id":"CLM-032"} -->
##### Records

Phase A records are:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-18_1156.md`

Future records remain `TBD` and may include a profile artifact, manifest, ID map, loss report, diagnostics, generated GLB/glTF artifact, and invented fixtures only when a later task explicitly authorizes those writes.

PDU-036 check: verify every emitted line primitive has current authoritative ID-map correlation. Record impossible-bend diagnostic coverage as absent/outside the selected profile; do not add GLB, viewer, or broader bend geometry.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, review-only geometry boundaries, identity and coordinate/unit handling, deterministic scene and mesh output, manifest/loss/diagnostic obligations, retained geometry and target-version TBDs, fixture provenance, and absence of solver-fidelity, fabrication, compatibility, release, compliance, or professional-authority claims.

## Governing Values and Decisions — Axiology

### CLM-033 — Guidance: DEL-17-08 GLB/glTF review geometry export

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-033"} -->
#### Guidance: DEL-17-08 GLB/glTF review geometry export

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-034 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-034"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-08-DECL-003`.

<!-- sow-source-end -->

### CLM-035 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":12,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-035"} -->
##### Purpose

Use DEL-17-08 as a narrow JSON glTF visual-review export surface. The selected profile lets a user inspect centerline shape and correlate emitted objects back to OpenPipeStress canonical IDs through direct `extras` plus an authoritative sidecar. It is not binary GLB, a solver model, an analysis result, a compatibility claim, engineering validation, or professional acceptance evidence.

<!-- sow-source-end -->

### CLM-036 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":16,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-036"} -->
##### Principles

<!-- sow-source-end -->

### CLM-037 — Keep visual review separate from solver meaning

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":18,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-037"} -->
###### Keep visual review separate from solver meaning

GLB/glTF is useful because it is lightweight and broadly viewable. That is also why the boundary needs to be explicit: a visible pipe-like shape does not prove that wall properties, support behavior, branch flexibility, load cases, stress recovery, rule-pack inputs, or target-solver interpretation are complete.

When the exporter emits simplified geometry, describe it as review geometry. If the visual representation drops support/restraint details, component semantics, private metadata, or user rule context, record the loss rather than implying the target file carries those meanings.

<!-- sow-source-end -->

### CLM-038 — Preserve identity before appearance polish

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":31,"line_start":24,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-038"} -->
###### Preserve identity before appearance polish

The review artifact is only useful to OpenPipeStress workflows if visible objects can be traced back to the canonical model. Prefer stable canonical IDs over display-order assumptions. Use direct metadata only where the profile says it is reliable enough; otherwise pair the geometry artifact with a sidecar ID map and reference it from the manifest.

For the selected centerline profile, direct node/primitive `extras` are paired with an always-authoritative sidecar; package acceptance blocks when those representations do not correlate one-to-one after deterministic write/read round trip. This establishes package identity integrity only, not receiving-viewer retention or compatibility.

Do not rely on glTF indices or generated names as the only identity layer unless the loss report records the limitation and the profile accepts it for the selected use.

<!-- sow-source-end -->

### CLM-039 — Make target behavior explicit

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":37,"line_start":32,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-039"} -->
###### Make target behavior explicit

The profile should say what is emitted and what is not. This is especially important for supports, restraints, components, equipment interfaces, and annotations, where a visual marker may communicate less than the source model knows.

Unresolved behavior remains `TBD`; it should not be softened into phrases such as "supported by default" or "compatible with viewers" unless a later source-grounded profile and test set support that wording.

<!-- sow-source-end -->

### CLM-040 — Keep data boundaries visible

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":41,"line_start":38,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-040"} -->
###### Keep data boundaries visible

GLB/glTF metadata and sidecars can accidentally expose private project names, owner criteria, component tags, rule-pack notes, or proprietary catalog data. The review-geometry profile should distinguish user-private metadata from public fixture metadata and should default public examples to invented or rights-cleared data only.

<!-- sow-source-end -->

### CLM-041 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":56,"line_start":42,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-041"} -->
##### Considerations

| Topic | Guidance |
|---|---|
| Coordinate policy | glTF uses a right-handed +Y-up coordinate basis and meters for linear distances. Source model axes, project vertical axis, origin, scale, and transform recording remain profile decisions. |
| Geometry level of detail | First coverage may be centerline-only, simplified tube/symbol geometry, or another declared subset. The choice remains `TBD` and should be loss-report driven. |
| Metadata placement | glTF `extras` and object `name` fields are candidate places for direct review metadata. A sidecar remains necessary when metadata needs stronger auditability or may be stripped by consuming tools. |
| Extensions | Avoid required custom extensions unless the profile records viewer impact and fallback behavior. Extensions used by an asset must be declared according to GLTF-2.0. |
| Hashing | GLB is binary. The manifest should hash the emitted binary when deterministic or record why a hash cannot be stable. |
| Fixtures | Public fixtures must be invented or rights-cleared and should avoid real project/client/tag data. |
| Viewer behavior | Viewer-specific rendering, selection, metadata display, and stripping behavior remain `TBD`; do not claim viewer compatibility in Phase A. |
| Timestamp/generator | Current JSON output uses a fixed versioned generator and omits timestamp fields. Treat this as tested implementation behavior, not the normative policy PDU-031 leaves owner-unselected. |

For E-001, viewer-specific behavior should be treated as evidence-dependent wording. A later profile may name viewer behavior only after source-grounded or test-recorded evidence exists; until then, guidance stays limited to review intent and metadata-risk caution.

<!-- sow-source-end -->

### CLM-042 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":66,"line_start":57,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-042"} -->
##### Trade-offs

| Option | Benefit | Cost or risk | Phase A position |
|---|---|---|---|
| Centerline-only line primitives | Simple, compact, easy to correlate with line/element IDs | May be mistaken for incomplete physical geometry or omit component volume | Selected bounded JSON glTF profile with explicit loss reporting |
| Simplified tube/surface primitives | More inspectable visually | Requires more geometry generation and may imply false dimensional fidelity | `TBD`; must be labeled review geometry |
| Direct `extras` metadata | Keeps identity near the visible object | Some tools may ignore or strip metadata; schema remains target-specific | Selected only with authoritative sidecar; no viewer-retention claim |
| Sidecar ID map | Stronger audit trail and stable identity contract | Requires consumers to keep files together | Required and blocking-correlated for emitted centerlines |
| Required custom extension | Can structure metadata explicitly | Reduces viewer portability and requires extension governance | Defer unless later profile justifies it |

<!-- sow-source-end -->

### CLM-043 — Geometry Detail Rationale

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":70,"line_start":67,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-043"} -->
###### Geometry Detail Rationale

For D-002, a later profile should choose the first review-geometry level of detail by asking whether the representation supports visual orientation, canonical-ID correlation, and limitation disclosure without implying solver, CAD, fabrication, or analysis fidelity. Centerline, simplified tube/surface, symbol, annotation, and overlay choices should be justified by coverage, identity, viewer-risk, package size, deterministic generation, and loss-report clarity; unchosen or unresolved families remain `TBD`.

<!-- sow-source-end -->

### CLM-044 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":81,"line_start":71,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-044"} -->
##### Examples

No example model, GLB file, glTF JSON snippet, proprietary fixture, commercial target file, or standards-derived engineering example is included in Phase A.

Acceptable future examples shall be invented or rights-cleared and shall demonstrate only:

- a visible review entity correlated to a canonical ID;
- an omitted entity recorded in the ID map or loss report;
- a coordinate/unit diagnostic;
- a manifest entry for a GLB/glTF artifact.

<!-- sow-source-end -->

### CLM-045 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":88,"line_start":82,"source_sha256":"5c24ceed376179ef713edf5d321d68c1856dafbdf763d4730dc7d7029c1f5bb8","target_id":"CLM-045"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified in Phase A. Remaining open items are `TBD`, not conflicts. | N/A | N/A | N/A | N/A | N/A |

For PDU-036, do not manufacture impossible-bend geometry merely to satisfy a diagnostic species. Preserve the O11 profile and record the absent bend-specific evidence honestly.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-030 SOW-074 OBJ-009 OBJ-017 | CLM-009 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
