# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: c4-label-policy.spec.ts >> C4 modes, dedup, Hide/Isolate, hover, camera, resize and nonmutation @explicit-viewport
- Location: e2e/c4-label-policy.scenarios.ts:104:3

# Error details

```
Test timeout of 120000ms exceeded.
```

```
Error: locator.click: Test timeout of 120000ms exceeded.
Call log:
  - waiting for getByTestId('workspace-review')
    - locator resolved to <button type="button" class="shell-tab" aria-pressed="false" title="Review changes" data-testid="workspace-review">Review changes</button>
  - attempting click action
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <header class="workspace-dock-header" data-testid="workspace-dock-header">…</header> from <section data-page="project" data-testid="workspace-dock" aria-label="Workspace sections" class="workspace-dock shell-page">…</section> subtree intercepts pointer events
    - retrying click action
    - waiting 20ms
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <header class="workspace-dock-header" data-testid="workspace-dock-header">…</header> from <section data-page="project" data-testid="workspace-dock" aria-label="Workspace sections" class="workspace-dock shell-page">…</section> subtree intercepts pointer events
    - retrying click action
      - waiting 100ms
    226 × waiting for element to be visible, enabled and stable
        - element is visible, enabled and stable
        - scrolling into view if needed
        - done scrolling
        - <header class="workspace-dock-header" data-testid="workspace-dock-header">…</header> from <section data-page="project" data-testid="workspace-dock" aria-label="Workspace sections" class="workspace-dock shell-page">…</section> subtree intercepts pointer events
      - retrying click action
        - waiting 500ms

```

# Page snapshot

```yaml
- main [ref=e3]:
  - navigation "Application menu" [ref=e4]:
    - button "File" [ref=e6] [cursor=pointer]
    - button "Edit" [ref=e8] [cursor=pointer]
    - button "View" [ref=e10] [cursor=pointer]
    - button "Insert" [ref=e12] [cursor=pointer]
    - button "Analyze" [ref=e14] [cursor=pointer]
  - generic "Toolbar" [ref=e15]:
    - generic [ref=e16]:
      - heading "SWBPIPE" [level=1] [ref=e17]
      - paragraph [ref=e18]: Invented Utility Loop Preview
    - group "Editing tools" [ref=e19]:
      - button "Undo model edit" [disabled] [ref=e20]:
        - img [ref=e21]
      - button "Redo model edit" [disabled] [ref=e24]:
        - img [ref=e25]
      - button "Select" [pressed] [ref=e28] [cursor=pointer]:
        - img [ref=e29]
        - generic [ref=e31]: Select
    - group "View" [ref=e32]:
      - button "Table" [ref=e34] [cursor=pointer]:
        - img [ref=e35]
        - generic [ref=e37]: Table
      - button "Model" [ref=e39] [cursor=pointer]:
        - img [ref=e40]
        - generic [ref=e43]: Model
      - button "Both" [pressed] [ref=e45] [cursor=pointer]:
        - img [ref=e46]
        - generic [ref=e48]: Both
    - generic [ref=e49]:
      - button "Run" [ref=e50] [cursor=pointer]:
        - img [ref=e51]
        - generic [ref=e53]: Run
      - button "Issues, 3" [ref=e54] [cursor=pointer]:
        - img [ref=e55]
        - generic [ref=e57]: Issues
        - generic [ref=e58]: "3"
    - group "Panels" [ref=e59]:
      - button "Inspector" [ref=e61] [cursor=pointer]:
        - img [ref=e62]
        - generic [ref=e64]: Inspector
      - button "Agent" [disabled] [ref=e66]:
        - img [ref=e67]
        - generic [ref=e70]: Agent
    - generic "Display units" [ref=e71]:
      - combobox "Display units" [ref=e72]:
        - option "Entered" [selected]
        - option "SI"
        - option "US"
    - group [ref=e73]:
      - generic "Appearance" [ref=e74] [cursor=pointer]:
        - img [ref=e75]
      - option "System" [selected]
      - option "Light"
      - option "Dark"
      - option "Comfortable" [selected]
      - option "Compact"
    - region "Human toolkit" [ref=e77]:
      - button "Find modeling commands" [ref=e78] [cursor=pointer]:
        - img [ref=e79]
        - generic [ref=e82]: Search or command…
        - generic "Command K" [ref=e83]: ⌘K
  - generic [ref=e84]:
    - navigation "Stages" [ref=e85]:
      - list [ref=e86]:
        - listitem [ref=e87]:
          - button "Model" [ref=e88] [cursor=pointer]:
            - img [ref=e89]
            - generic [ref=e92]: Model
        - listitem [ref=e93]:
          - button "Loads" [ref=e94] [cursor=pointer]:
            - img [ref=e95]
            - generic [ref=e99]: Loads
        - listitem [ref=e100]:
          - button "Results" [disabled] [ref=e101]:
            - img [ref=e102]
            - generic [ref=e105]: Results
        - listitem [ref=e106]:
          - button "Review" [disabled] [ref=e107]:
            - img [ref=e108]
            - generic [ref=e112]: Review
      - separator [ref=e113]
      - list [ref=e114]:
        - listitem [ref=e115]:
          - button "Libraries" [ref=e116] [cursor=pointer]:
            - img [ref=e117]
            - generic [ref=e119]: Libraries
        - listitem [ref=e120]:
          - button "Rules" [ref=e121] [cursor=pointer]:
            - img [ref=e122]
            - generic [ref=e126]: Rules
        - listitem [ref=e127]:
          - button "Issues, 3" [ref=e128] [cursor=pointer]:
            - img [ref=e129]
            - generic [ref=e131]: Issues
            - generic [ref=e132]: "3"
    - generic [ref=e133]:
      - region "Modeling workspace" [ref=e134]:
        - generic [ref=e135]:
          - group "Tables" [ref=e136]:
            - button "Model" [pressed] [ref=e137] [cursor=pointer]
            - button "Review changes" [ref=e138] [cursor=pointer]
            - button "Collapse table drawer" [disabled] [expanded] [ref=e141]:
              - img [ref=e142]
          - generic "Model tree" [ref=e146]:
            - generic [ref=e147]: Model
            - generic [ref=e151]:
              - region "Layout grid mode" [ref=e152]:
                - button "Tree" [pressed] [ref=e153]:
                  - img [ref=e154]
                  - text: Tree
                - button "Grid" [ref=e157]:
                  - img [ref=e158]
                  - text: Grid
              - region "Model tree filtering" [ref=e160]:
                - generic [ref=e161]:
                  - img [ref=e162]
                  - generic [ref=e165]: Filter model
                  - searchbox "Filter model tree" [ref=e166]
                - generic [ref=e167]: 7 of 7 model entities visible
                - button "Clear model tree filter" [disabled] [ref=e168]:
                  - img [ref=e169]
            - tree "Model" [ref=e172]:
              - generic [ref=e173]:
                - treeitem "Invented Utility Loop Preview project:invented-loop-01" [level=1] [selected] [ref=e175] [cursor=pointer]:
                  - img [ref=e176]
                  - generic [ref=e180]:
                    - strong [ref=e181]: Invented Utility Loop Preview
                    - generic [ref=e182]: project:invented-loop-01
                - treeitem "Materials" [expanded] [level=1] [ref=e184] [cursor=pointer]:
                  - generic [ref=e185]: ▾
                  - strong [ref=e186]: Materials
                - treeitem "Invented carbon-steel-like material material:invented-carbon-steel" [level=2] [ref=e188] [cursor=pointer]:
                  - img [ref=e189]
                  - generic [ref=e192]:
                    - strong [ref=e193]: Invented carbon-steel-like material
                    - generic [ref=e194]: material:invented-carbon-steel
                - treeitem "Nodes" [expanded] [level=1] [ref=e196] [cursor=pointer]:
                  - generic [ref=e197]: ▾
                  - strong [ref=e198]: Nodes
                - treeitem "A A" [level=2] [ref=e200] [cursor=pointer]:
                  - img [ref=e201]
                  - generic [ref=e204]:
                    - strong [ref=e205]: A
                    - generic [ref=e206]: A
                - treeitem "B B" [level=2] [ref=e208] [cursor=pointer]:
                  - img [ref=e209]
                  - generic [ref=e212]:
                    - strong [ref=e213]: B
                    - generic [ref=e214]: B
                - treeitem "C C" [level=2] [ref=e216] [cursor=pointer]:
                  - img [ref=e217]
                  - generic [ref=e220]:
                    - strong [ref=e221]: C
                    - generic [ref=e222]: C
                - treeitem "D D" [level=2] [ref=e224] [cursor=pointer]:
                  - img [ref=e225]
                  - generic [ref=e228]:
                    - strong [ref=e229]: D
                    - generic [ref=e230]: D
                - treeitem "Pipes" [expanded] [level=1] [ref=e232] [cursor=pointer]:
                  - generic [ref=e233]: ▾
                  - strong [ref=e234]: Pipes
                - treeitem "P P" [level=2] [ref=e236] [cursor=pointer]:
                  - img [ref=e237]
                  - generic [ref=e241]:
                    - strong [ref=e242]: P
                    - generic [ref=e243]: P
        - separator "Resize table and canvas" [ref=e244]
        - generic [ref=e246]:
          - generic [ref=e247]:
            - group "Viewport controls" [ref=e248]:
              - generic [ref=e249]: 3D Centerline
              - group "Viewport deformation overlay status" [ref=e250]:
                - generic "Deformation · unavailable" [ref=e251] [cursor=pointer]
              - group "Viewport display toggles" [ref=e252]:
                - 'button "Labels: Budget. Cycle Budget, All, Off" [ref=e253]': "Labels: Budget"
                - button "Loads" [pressed] [ref=e254]
                - button "Grid" [pressed] [ref=e255]
              - group "Viewport selection tools" [ref=e256]:
                - button "Box Select" [ref=e257]
                - generic [ref=e258]:
                  - generic [ref=e259]: Selection filter
                  - combobox "Selection filter" [ref=e260]:
                    - option "All" [selected]
                    - option "Pipes"
                    - option "Nodes"
                    - option "Supports"
                    - option "Components"
                - button "Hide" [disabled] [ref=e261]
                - button "Isolate" [disabled] [ref=e262]
                - button "Show All" [disabled] [ref=e263]
                - generic [ref=e264]: Isolate captures the selected geometry. Other shown geometry is dimmed to 20% and remains available to click, hover and box selection; nearer dimmed geometry can be picked before farther undimmed geometry. Selection does not change the snapshot. Hide takes precedence. Show All clears both. I and H apply while focus is in the viewport.
                - button "Fit Model" [ref=e265]
                - button "Fit Visible" [ref=e266]
                - button "Fit Selection" [disabled] [ref=e267]
              - group "Viewport geometry" [ref=e268]:
                - button "Schematic" [pressed] [ref=e269]
                - button "Actual OD" [ref=e270]
                - button "Measure" [ref=e271]
            - generic "Viewport status" [ref=e272]:
              - 'generic "Selected project: project:invented-loop-01" [ref=e273]': "Selected: project:invented-loop-01"
              - group [ref=e274]:
                - generic "0 annotations omitted" [ref=e275]
              - status "Schematic centerline geometry" [ref=e276]
              - status "View command status" [ref=e277]: Fit Model applied to the displayed geometry envelope.
          - generic [ref=e278]:
            - generic "Three.js pipe centerline viewport" [ref=e279]
            - generic "Viewport entity selection":
              - button "Select A in viewport" [ref=e281] [cursor=pointer]:
                - img [ref=e282]
                - generic [ref=e285]: A
              - button "Select B in viewport" [ref=e286] [cursor=pointer]:
                - img [ref=e287]
                - generic [ref=e290]: B
              - button "Select C in viewport" [ref=e291] [cursor=pointer]:
                - img [ref=e292]
                - generic [ref=e295]: C
              - button "Select D in viewport" [ref=e296] [cursor=pointer]:
                - img [ref=e297]
                - generic [ref=e300]: D
              - button "Select P in viewport" [ref=e301] [cursor=pointer]:
                - img [ref=e302]
                - generic [ref=e306]: P
            - img "Orientation gizmo showing X, Y, Z axes"
            - generic "View controls" [ref=e307]:
              - button "Front" [pressed] [ref=e308] [cursor=pointer]
              - button "Top" [ref=e309] [cursor=pointer]
              - button "Isometric" [ref=e310] [cursor=pointer]
            - generic:
              - generic: 1 m
          - region "Command and selection bar" [ref=e311]:
            - generic "Object creation tools" [ref=e312]:
              - button "Node" [ref=e313] [cursor=pointer]:
                - img [ref=e314]
                - text: Node
              - button "Pipe" [ref=e316] [cursor=pointer]:
                - img [ref=e317]
                - text: Pipe
              - button "Support" [ref=e321] [cursor=pointer]:
                - img [ref=e322]
                - text: Support
              - button "Component" [ref=e325] [cursor=pointer]:
                - img [ref=e326]
                - text: Component
              - button "Load" [ref=e329] [cursor=pointer]:
                - img [ref=e330]
                - text: Load
            - generic "Model focus" [ref=e332]: Select
            - group [ref=e333]:
              - generic "Selection & navigation" [ref=e334] [cursor=pointer]
        - text: ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾
      - region "Workspace sections" [ref=e335]:
        - generic [ref=e336]:
          - heading "Project" [level=2] [ref=e337]
          - generic "Local project controls" [ref=e338]:
            - button "Create local" [ref=e339] [cursor=pointer]:
              - img [ref=e340]
              - text: Create local
            - button "New blank" [ref=e344] [cursor=pointer]:
              - img [ref=e345]
              - text: New blank
            - button "Open local" [ref=e348] [cursor=pointer]:
              - img [ref=e349]
              - text: Open local
            - button "List local" [ref=e351] [cursor=pointer]:
              - img [ref=e352]
              - text: List local
            - button "Save local" [ref=e353] [cursor=pointer]:
              - img [ref=e354]
              - text: Save local
          - button "Close" [ref=e358] [cursor=pointer]:
            - img [ref=e359]
            - text: Close
        - group "Project summary" [ref=e363]:
          - generic "Details" [ref=e364] [cursor=pointer]:
            - status [ref=e365]: Opened local browser-preview project snapshot.
            - generic [ref=e366]: Details
        - region "Project section" [ref=e368]:
          - region "Project storage audit" [ref=e369]:
            - generic [ref=e370]:
              - img [ref=e371]
              - text: Project Storage Audit
            - generic [ref=e373]:
              - generic [ref=e374]:
                - generic [ref=e375]:
                  - checkbox "Include known private values in this local export" [ref=e376]
                  - text: Include known private values in this local export
                - generic [ref=e377]: decisions=151; findings=151; blocked=true
                - group [ref=e378]:
                  - generic "Details" [ref=e379] [cursor=pointer]
                - generic [ref=e380]:
                  - img [ref=e381]
                  - text: Local storage JSON
              - generic [ref=e384]: operation=open; pending operations=0; proposals=0; accepted_state_mutated=false
            - generic [ref=e385]:
              - generic [ref=e386]:
                - generic [ref=e387]: Storage capability
                - strong [ref=e388]: Browser memory preview; mode=browser_memory_preview; FTS5=false
              - generic [ref=e389]:
                - generic [ref=e390]: Local-only boundary
                - strong [ref=e391]: network=false; daemon=false; telemetry=false; repository_default_private_write=false
              - generic [ref=e392]:
                - generic [ref=e393]: Project snapshot
                - strong [ref=e394]: project:invented-loop-01; browser_memory_preview; persisted_editor_intents=0; persisted_proposals=0; persisted_review_targets=0; persisted_review_target_ref=not_selected; persisted_mechanics_results=0; persisted_analysis_runs=0; persisted_analysis_run_ref=not_persisted; copied_external_files=false
              - generic [ref=e395]:
                - generic [ref=e396]: Project index
                - strong [ref=e397]: state=not_requested; listed_projects=0; refs=none
              - generic [ref=e398]:
                - generic [ref=e399]: Model hash persistence
                - strong [ref=e400]: persisted_model_hashes=1; persisted_model_hash_ref=sha256:248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea
              - generic [ref=e401]:
                - generic [ref=e402]: Model hash integrity
                - strong [ref=e403]: integrity_status=verified_match; persisted_value=sha256:248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea; recomputed_value=sha256:248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea; verification_basis=recomputed_on_open_from_restored_model; claim_standing=not_recorded; source=open; observed_at=2026-09-24T06:52:07.144Z; persisted snapshot only; later local edits are not verified; review-only integrity signal for human review
              - generic [ref=e404]:
                - generic [ref=e405]: Envelope hash integrity
                - strong [ref=e406]: integrity_status=verified_match; persisted_value=sha256:ef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3; recomputed_value=sha256:ef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3; verification_basis=recomputed_on_open_from_restored_envelope_payload; source=open; observed_at=2026-09-24T06:52:07.150Z; persisted snapshot only; later local edits are not verified
              - generic [ref=e407]:
                - generic [ref=e408]: Unit round-trip
                - strong [ref=e409]: status=unit_metadata_preserved_in_local_project_envelope; checked_refs=11; signature=materials.material:invented-carbon-steel.elastic_modulus=Pa|materials.material:invented-carbon-steel.shear_modulus=Pa|materials.material:invented-carbon-steel.thermal_expansion_coefficient=1/degC|pipe_segments.P.section.outside_diameter=m|pipe_segments.P.section.wall_thickness=m|project.units.angle=rad|project.units.force=N|project.units.length=m|project.units.pressure=Pa|project.units.stress=MPa|project.units.temperature=degC; model=angle=rad,force=N,length=m,pressure=Pa,stress=MPa,temperature=degC; conversion=false
              - generic [ref=e410]:
                - generic [ref=e411]: Payload boundary
                - strong [ref=e412]: private payload=false; protected content=false; release/professional claim=false
            - generic [ref=e413]: Storage audit packets are local evidence only; create/open/save operations do not accept model changes or copy external project files.
          - region "Project validation preflight" [ref=e414]:
            - generic [ref=e415]:
              - img [ref=e416]
              - text: Project Validation Preflight
            - generic [ref=e420]:
              - generic [ref=e421]:
                - generic [ref=e422]:
                  - checkbox "Include known private values in this local export" [checked] [active] [ref=e423]
                  - text: Include known private values in this local export
                - generic [ref=e424]: decisions=284; findings=284; blocked=false
                - group [ref=e425]:
                  - generic "Details" [ref=e426] [cursor=pointer]
                - link "Validation JSON" [ref=e427] [cursor=pointer]:
                  - /url: data:application/json;charset=utf-8,%7B%0A%20%20%22schema_version%22%3A%20%220.1.0%22%2C%0A%20%20%22document_kind%22%3A%20%22openpipestress.technical_preview.project_validation_preflight%22%2C%0A%20%20%22export_scope%22%3A%20%22local_browser_download_preview%22%2C%0A%20%20%22deliverable_refs%22%3A%20%5B%0A%20%20%20%20%22DEL-02-02%22%2C%0A%20%20%20%20%22DEL-02-05%22%2C%0A%20%20%20%20%22DEL-12-01%22%0A%20%20%5D%2C%0A%20%20%22scope_items%22%3A%20%5B%0A%20%20%20%20%22SOW-050%22%2C%0A%20%20%20%20%22SOW-041%22%2C%0A%20%20%20%20%22SOW-029%22%0A%20%20%5D%2C%0A%20%20%22objectives%22%3A%20%5B%0A%20%20%20%20%22OBJ-001%22%2C%0A%20%20%20%20%22OBJ-010%22%2C%0A%20%20%20%20%22OBJ-012%22%0A%20%20%5D%2C%0A%20%20%22project_ref%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%22project_name%22%3A%20%22Invented%20Utility%20Loop%20Preview%22%2C%0A%20%20%22summary%22%3A%20%7B%0A%20%20%20%20%22validation_status%22%3A%20%22preview_current%22%2C%0A%20%20%20%20%22version_check_status%22%3A%20%22stale%22%2C%0A%20%20%20%20%22migration_status%22%3A%20%22browser_memory_snapshot_no_sql_store_migrations_applicable%22%2C%0A%20%20%20%20%22round_trip_status%22%3A%20%22semantic_categories_declared%22%2C%0A%20%20%20%20%22schema_version%22%3A%20%220.1.0%22%2C%0A%20%20%20%20%22document_kind%22%3A%20%22openpipestress.product_preview.model%22%2C%0A%20%20%20%20%22storage_mode%22%3A%20%22browser_memory_preview%22%2C%0A%20%20%20%20%22last_operation%22%3A%20%22open%22%2C%0A%20%20%20%20%22pending_operation_count%22%3A%200%2C%0A%20%20%20%20%22editor_intent_count%22%3A%200%2C%0A%20%20%20%20%22persisted_editor_intent_count%22%3A%200%2C%0A%20%20%20%20%22proposal_operation_count%22%3A%200%2C%0A%20%20%20%20%22persisted_proposal_count%22%3A%200%2C%0A%20%20%20%20%22persisted_selected_review_target_count%22%3A%200%2C%0A%20%20%20%20%22persisted_selected_review_target_ref%22%3A%20%22not_selected%22%2C%0A%20%20%20%20%22persisted_mechanics_result_count%22%3A%200%2C%0A%20%20%20%20%22persisted_analysis_run_count%22%3A%200%2C%0A%20%20%20%20%22persisted_analysis_run_ref%22%3A%20%22not_persisted%22%2C%0A%20%20%20%20%22unit_round_trip_status%22%3A%20%22unit_metadata_preserved_in_local_project_envelope%22%2C%0A%20%20%20%20%22unit_round_trip_checked_ref_count%22%3A%2011%2C%0A%20%20%20%20%22unit_round_trip_signature%22%3A%20%22materials.material%3Ainvented-carbon-steel.elastic_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.shear_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.thermal_expansion_coefficient%3D1%2FdegC%7Cpipe_segments.P.section.outside_diameter%3Dm%7Cpipe_segments.P.section.wall_thickness%3Dm%7Cproject.units.angle%3Drad%7Cproject.units.force%3DN%7Cproject.units.length%3Dm%7Cproject.units.pressure%3DPa%7Cproject.units.stress%3DMPa%7Cproject.units.temperature%3DdegC%22%2C%0A%20%20%20%20%22model_hash_status%22%3A%20%22model_hash_verified_on_open%22%2C%0A%20%20%20%20%22persisted_model_hash_count%22%3A%201%2C%0A%20%20%20%20%22persisted_model_hash_ref%22%3A%20%22sha256%3A248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea%22%2C%0A%20%20%20%20%22model_hash_integrity_status%22%3A%20%22verified_match%22%2C%0A%20%20%20%20%22project_envelope_hash_status%22%3A%20%22project_envelope_hash_verified_on_open%22%2C%0A%20%20%20%20%22persisted_project_envelope_hash_count%22%3A%201%2C%0A%20%20%20%20%22persisted_project_envelope_hash_ref%22%3A%20%22sha256%3Aef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3%22%2C%0A%20%20%20%20%22project_envelope_hash_integrity_status%22%3A%20%22verified_match%22%2C%0A%20%20%20%20%22accepted_model_state_mutated%22%3A%20false%2C%0A%20%20%20%20%22copied_external_files%22%3A%20false%2C%0A%20%20%20%20%22network_required%22%3A%20false%2C%0A%20%20%20%20%22daemon_required%22%3A%20false%2C%0A%20%20%20%20%22telemetry_enabled%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22validation_profile%22%3A%20%7B%0A%20%20%20%20%22profile_id%22%3A%20%22technical_preview_project_persistence_preflight%22%2C%0A%20%20%20%20%22json_schema_baseline%22%3A%20%222020-12%22%2C%0A%20%20%20%20%22canonicalization_basis%22%3A%20%22JCS-compatible%22%2C%0A%20%20%20%20%22hash_service_status%22%3A%20%22canonical_model_hash_service_available_model_payload_scope%22%2C%0A%20%20%20%20%22project_envelope_hash_status%22%3A%20%22project_envelope_hash_verified_on_open%22%2C%0A%20%20%20%20%22project_envelope_hash_scope%22%3A%20%22persisted_envelope_payload_excluding_storage_summary_and_hash_carrier%22%2C%0A%20%20%20%20%22physical_container_status%22%3A%20%22browser_memory_preview%22%2C%0A%20%20%20%20%22store_migration_framework_status%22%3A%20%22browser_memory_preview_no_sqlite_migration_ledger%22%2C%0A%20%20%20%20%22model_document_migration_status%22%3A%20%22migrated%22%0A%20%20%7D%2C%0A%20%20%22round_trip_manifest%22%3A%20%7B%0A%20%20%20%20%22category_count%22%3A%206%2C%0A%20%20%20%20%22categories%22%3A%20%5B%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22model_content%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22ready_for_preview_round_trip%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%205%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22unit_metadata%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22ready_for_preview_round_trip%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%205%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22load_payloads%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22ready_for_preview_round_trip%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%200%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22rule_pack_references%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22not_present_in_invented_fixture%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%200%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22provenance_metadata%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22ready_for_preview_round_trip%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%206%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22category%22%3A%20%22reproducibility_metadata%22%2C%0A%20%20%20%20%20%20%20%20%22semantic_equality_status%22%3A%20%22model_hash_verified_on_open%22%2C%0A%20%20%20%20%20%20%20%20%22checked_ref_count%22%3A%201%2C%0A%20%20%20%20%20%20%20%20%22silent_default_inserted%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22protected_content_expanded%22%3A%20false%2C%0A%20%20%20%20%20%20%20%20%22private_payload_expanded%22%3A%20false%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22parse_validate_normalize_serialize_parse_basis%22%3A%20%22preview_fixture_semantic_category_review%22%2C%0A%20%20%20%20%22volatile_fields%22%3A%20%5B%0A%20%20%20%20%20%20%22storage.database_path%22%2C%0A%20%20%20%20%20%20%22storage.message%22%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22normalization_rules%22%3A%20%5B%0A%20%20%20%20%20%20%22stable%20IDs%20and%20typed%20references%20are%20compared%20semantically%22%2C%0A%20%20%20%20%20%20%22unit-bearing%20values%20must%20retain%20explicit%20unit%20metadata%22%2C%0A%20%20%20%20%20%20%22missing%20optional%20rule-pack%20references%20remain%20explicit%20not-present%20records%22%0A%20%20%20%20%5D%0A%20%20%7D%2C%0A%20%20%22unit_round_trip_evidence%22%3A%20%7B%0A%20%20%20%20%22status%22%3A%20%22unit_metadata_preserved_in_local_project_envelope%22%2C%0A%20%20%20%20%22checked_ref_count%22%3A%2011%2C%0A%20%20%20%20%22signature%22%3A%20%22materials.material%3Ainvented-carbon-steel.elastic_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.shear_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.thermal_expansion_coefficient%3D1%2FdegC%7Cpipe_segments.P.section.outside_diameter%3Dm%7Cpipe_segments.P.section.wall_thickness%3Dm%7Cproject.units.angle%3Drad%7Cproject.units.force%3DN%7Cproject.units.length%3Dm%7Cproject.units.pressure%3DPa%7Cproject.units.stress%3DMPa%7Cproject.units.temperature%3DdegC%22%2C%0A%20%20%20%20%22evidence_source%22%3A%20%22local_project_summary%22%2C%0A%20%20%20%20%22comparison_basis%22%3A%20%22deterministic_unit_metadata_signature_from_restored_local_project_envelope%22%0A%20%20%7D%2C%0A%20%20%22unit_policy_evidence%22%3A%20%7B%0A%20%20%20%20%22evidence_id%22%3A%20%22unit-policy-evidence%3Aproject-validation-preflight%22%2C%0A%20%20%20%20%22unit_system_ref%22%3A%20%7B%0A%20%20%20%20%20%20%22object_type%22%3A%20%22UnitSystem%22%2C%0A%20%20%20%20%20%20%22ref%22%3A%20%22unit-system%3Adec-018-si-dual-display%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22source_model_ref%22%3A%20%7B%0A%20%20%20%20%20%20%22object_type%22%3A%20%22Model%22%2C%0A%20%20%20%20%20%20%22ref%22%3A%20%22project%3Ainvented-loop-01%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22storage_convention%22%3A%20%22entered_units_preserved%22%2C%0A%20%20%20%20%22validation_unit_policy%22%3A%20%22validate_round_trip_preserves_explicit_model_unit_metadata_without_conversion%22%2C%0A%20%20%20%20%22model_units%22%3A%20%7B%0A%20%20%20%20%20%20%22angle%22%3A%20%22rad%22%2C%0A%20%20%20%20%20%20%22force%22%3A%20%22N%22%2C%0A%20%20%20%20%20%20%22length%22%3A%20%22m%22%2C%0A%20%20%20%20%20%20%22pressure%22%3A%20%22Pa%22%2C%0A%20%20%20%20%20%20%22stress%22%3A%20%22MPa%22%2C%0A%20%20%20%20%20%20%22temperature%22%3A%20%22degC%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22unit_bearing_record_count%22%3A%205%2C%0A%20%20%20%20%22unit_round_trip_status%22%3A%20%22unit_metadata_preserved_in_local_project_envelope%22%2C%0A%20%20%20%20%22unit_round_trip_checked_ref_count%22%3A%2011%2C%0A%20%20%20%20%22unit_round_trip_signature%22%3A%20%22materials.material%3Ainvented-carbon-steel.elastic_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.shear_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.thermal_expansion_coefficient%3D1%2FdegC%7Cpipe_segments.P.section.outside_diameter%3Dm%7Cpipe_segments.P.section.wall_thickness%3Dm%7Cproject.units.angle%3Drad%7Cproject.units.force%3DN%7Cproject.units.length%3Dm%7Cproject.units.pressure%3DPa%7Cproject.units.stress%3DMPa%7Cproject.units.temperature%3DdegC%22%2C%0A%20%20%20%20%22conversion_policy%22%3A%20%22project_validation_records_unit_round_trip_metadata_without_conversion%22%2C%0A%20%20%20%20%22conversion_performed%22%3A%20false%2C%0A%20%20%20%20%22decision_basis_refs%22%3A%20%5B%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22object_type%22%3A%20%22Decision%22%2C%0A%20%20%20%20%20%20%20%20%22ref%22%3A%20%22DEC-018%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22object_type%22%3A%20%22Deliverable%22%2C%0A%20%20%20%20%20%20%20%20%22ref%22%3A%20%22DEL-02-02%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22object_type%22%3A%20%22Deliverable%22%2C%0A%20%20%20%20%20%20%20%20%22ref%22%3A%20%22DEL-02-05%22%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22protected_content_included%22%3A%20false%2C%0A%20%20%20%20%22private_payload_included%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22service_operations%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22create%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22available%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22open%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22last_operation_completed%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22save%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22available%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20false%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22validate%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22preflight_generated_preview_current%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22version_check%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22stale%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20true%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22operation%22%3A%20%22migrate%22%2C%0A%20%20%20%20%20%20%22operation_status%22%3A%20%22browser_memory_snapshot_no_sql_store_migrations_applicable%22%2C%0A%20%20%20%20%20%20%22result_available%22%3A%20true%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22store_migration%22%3A%20%7B%0A%20%20%20%20%22migration_framework%22%3A%20%22browser_memory_preview_no_sqlite_migration_ledger%22%2C%0A%20%20%20%20%22migration_status%22%3A%20%22browser_memory_snapshot_no_sql_store_migrations_applicable%22%2C%0A%20%20%20%20%22store_schema_version%22%3A%200%2C%0A%20%20%20%20%22store_schema_target_version%22%3A%200%2C%0A%20%20%20%20%22migrations_applied_on_open%22%3A%20%5B%5D%2C%0A%20%20%20%20%22evidence_source%22%3A%20%22local_project_summary%22%2C%0A%20%20%20%20%22migration_scope%22%3A%20%22local_store_schema_ddl_only_model_document_schema_tracked_separately_per_dec_019%22%2C%0A%20%20%20%20%22destructive_migration_performed%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22model_document_migration%22%3A%20%7B%0A%20%20%20%20%22decision_basis%22%3A%20%22DEC-019_model_document_schema_migration_policy%22%2C%0A%20%20%20%20%22version_authority%22%3A%20%22in_document_schema_version_semver%22%2C%0A%20%20%20%20%22evidence_source%22%3A%20%22persistence_operation_envelope%22%2C%0A%20%20%20%20%22status%22%3A%20%22migrated%22%2C%0A%20%20%20%20%22source_schema_version%22%3A%20%220.1.0%22%2C%0A%20%20%20%20%22target_schema_version%22%3A%20%220.2.0%22%2C%0A%20%20%20%20%22migration_framework%22%3A%20%22application_service_separate_db_and_product_schema%22%2C%0A%20%20%20%20%22persistence_state%22%3A%20%22in_memory_only_not_yet_saved%22%2C%0A%20%20%20%20%22applied_migration_ids%22%3A%20%5B%0A%20%20%20%20%20%20%22model-doc-0.1.0-to-0.2.0-additive-combination-shape-noop%22%0A%20%20%20%20%5D%2C%0A%20%20%20%20%22ledger_record_count%22%3A%200%2C%0A%20%20%20%20%22ledger_records%22%3A%20%5B%5D%2C%0A%20%20%20%20%22destructive_rewrite%22%3A%20false%2C%0A%20%20%20%20%22down_migration_performed%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22storage_capability%22%3A%20%7B%0A%20%20%20%20%22engine%22%3A%20%22Browser%20memory%20preview%22%2C%0A%20%20%20%20%22bundled%22%3A%20true%2C%0A%20%20%20%20%22fts5_available%22%3A%20false%2C%0A%20%20%20%20%22network_required%22%3A%20false%2C%0A%20%20%20%20%22daemon_required%22%3A%20false%2C%0A%20%20%20%20%22telemetry_enabled%22%3A%20false%2C%0A%20%20%20%20%22path_policy%22%3A%20%22browser-session%20memory%20fallback%3B%20no%20repository-default%20writes%22%2C%0A%20%20%20%20%22large_file_policy%22%3A%20%22reference%20external%20files%20by%20path%2Fhash%20metadata%3B%20do%20not%20silently%20copy%20large%20files%22%2C%0A%20%20%20%20%22database_path%22%3A%20%22browser-session%20memory%20fallback%22%2C%0A%20%20%20%20%22compile_options%22%3A%20%5B%5D%2C%0A%20%20%20%20%22migration_framework%22%3A%20%22browser_memory_preview_no_sqlite_migration_ledger%22%2C%0A%20%20%20%20%22migration_status%22%3A%20%22browser_memory_snapshot_no_sql_store_migrations_applicable%22%2C%0A%20%20%20%20%22store_schema_version%22%3A%200%2C%0A%20%20%20%20%22store_schema_target_version%22%3A%200%2C%0A%20%20%20%20%22migrations_applied_on_open%22%3A%20%5B%5D%0A%20%20%7D%2C%0A%20%20%22project_summary%22%3A%20%7B%0A%20%20%20%20%22project_id%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%20%20%22project_name%22%3A%20%22Invented%20Utility%20Loop%20Preview%22%2C%0A%20%20%20%20%22database_path%22%3A%20%22browser-session%20memory%20fallback%22%2C%0A%20%20%20%20%22storage_mode%22%3A%20%22browser_memory_preview%22%2C%0A%20%20%20%20%22migration_status%22%3A%20%22browser_memory_snapshot_no_sql_store_migrations_applicable%22%2C%0A%20%20%20%20%22migration_framework%22%3A%20%22browser_memory_preview_no_sqlite_migration_ledger%22%2C%0A%20%20%20%20%22store_schema_version%22%3A%200%2C%0A%20%20%20%20%22store_schema_target_version%22%3A%200%2C%0A%20%20%20%20%22migrations_applied_on_open%22%3A%20%5B%5D%2C%0A%20%20%20%20%22fts_indexed%22%3A%20false%2C%0A%20%20%20%20%22copied_external_files%22%3A%20false%2C%0A%20%20%20%20%22editor_intent_count%22%3A%200%2C%0A%20%20%20%20%22proposal_count%22%3A%200%2C%0A%20%20%20%20%22selected_review_target_count%22%3A%200%2C%0A%20%20%20%20%22selected_review_target_ref%22%3A%20%22not_selected%22%2C%0A%20%20%20%20%22persisted_mechanics_result_count%22%3A%200%2C%0A%20%20%20%20%22persisted_analysis_run_count%22%3A%200%2C%0A%20%20%20%20%22persisted_analysis_run_ref%22%3A%20%22not_persisted%22%2C%0A%20%20%20%20%22persisted_model_hash_count%22%3A%201%2C%0A%20%20%20%20%22persisted_model_hash_ref%22%3A%20%22sha256%3A248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea%22%2C%0A%20%20%20%20%22persisted_project_envelope_hash_count%22%3A%201%2C%0A%20%20%20%20%22persisted_project_envelope_hash_ref%22%3A%20%22sha256%3Aef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3%22%2C%0A%20%20%20%20%22unit_round_trip_status%22%3A%20%22unit_metadata_preserved_in_local_project_envelope%22%2C%0A%20%20%20%20%22unit_round_trip_checked_ref_count%22%3A%2011%2C%0A%20%20%20%20%22unit_round_trip_signature%22%3A%20%22materials.material%3Ainvented-carbon-steel.elastic_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.shear_modulus%3DPa%7Cmaterials.material%3Ainvented-carbon-steel.thermal_expansion_coefficient%3D1%2FdegC%7Cpipe_segments.P.section.outside_diameter%3Dm%7Cpipe_segments.P.section.wall_thickness%3Dm%7Cproject.units.angle%3Drad%7Cproject.units.force%3DN%7Cproject.units.length%3Dm%7Cproject.units.pressure%3DPa%7Cproject.units.stress%3DMPa%7Cproject.units.temperature%3DdegC%22%2C%0A%20%20%20%20%22message%22%3A%20%22Opened%20local%20browser-preview%20project%20snapshot.%22%0A%20%20%7D%2C%0A%20%20%22model_hash%22%3A%20%7B%0A%20%20%20%20%22algorithm%22%3A%20%22sha256%22%2C%0A%20%20%20%20%22canonicalization%22%3A%20%22rfc8785_jcs%22%2C%0A%20%20%20%20%22payload_scope%22%3A%20%22model_payload%22%2C%0A%20%20%20%20%22payload_ref%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%20%20%22value%22%3A%20%22sha256%3A248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea%22%2C%0A%20%20%20%20%22hash_status%22%3A%20%22computed_local_preview%22%0A%20%20%7D%2C%0A%20%20%22model_hash_integrity%22%3A%20%7B%0A%20%20%20%20%22integrity_status%22%3A%20%22verified_match%22%2C%0A%20%20%20%20%22persisted_value%22%3A%20%22sha256%3A248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea%22%2C%0A%20%20%20%20%22recomputed_value%22%3A%20%22sha256%3A248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea%22%2C%0A%20%20%20%20%22payload_ref%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%20%20%22verification_basis%22%3A%20%22recomputed_on_open_from_restored_model%22%2C%0A%20%20%20%20%22verification_source%22%3A%20%22open%22%2C%0A%20%20%20%20%22observed_at%22%3A%20%222026-09-24T06%3A52%3A07.144Z%22%2C%0A%20%20%20%20%22observation_scope%22%3A%20%22persisted_snapshot_not_current_local_model%22%0A%20%20%7D%2C%0A%20%20%22project_envelope_hash%22%3A%20%7B%0A%20%20%20%20%22algorithm%22%3A%20%22sha256%22%2C%0A%20%20%20%20%22canonicalization%22%3A%20%22rfc8785_jcs%22%2C%0A%20%20%20%20%22payload_scope%22%3A%20%22project_envelope_payload%22%2C%0A%20%20%20%20%22payload_excludes%22%3A%20%22storage_summary_and_envelope_hash_carrier_fields%22%2C%0A%20%20%20%20%22payload_ref%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%20%20%22value%22%3A%20%22sha256%3Aef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3%22%2C%0A%20%20%20%20%22hash_status%22%3A%20%22computed_local_preview%22%0A%20%20%7D%2C%0A%20%20%22project_envelope_hash_integrity%22%3A%20%7B%0A%20%20%20%20%22integrity_status%22%3A%20%22verified_match%22%2C%0A%20%20%20%20%22persisted_value%22%3A%20%22sha256%3Aef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3%22%2C%0A%20%20%20%20%22recomputed_value%22%3A%20%22sha256%3Aef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3%22%2C%0A%20%20%20%20%22payload_ref%22%3A%20%22project%3Ainvented-loop-01%22%2C%0A%20%20%20%20%22verification_basis%22%3A%20%22recomputed_on_open_from_restored_envelope_payload%22%2C%0A%20%20%20%20%22verification_source%22%3A%20%22open%22%2C%0A%20%20%20%20%22observed_at%22%3A%20%222026-09-24T06%3A52%3A07.150Z%22%2C%0A%20%20%20%20%22observation_scope%22%3A%20%22persisted_snapshot_not_current_local_model%22%0A%20%20%7D%2C%0A%20%20%22editor_intent_refs%22%3A%20%5B%5D%2C%0A%20%20%22proposal_refs%22%3A%20%5B%5D%2C%0A%20%20%22editor_operation_statuses%22%3A%20%5B%5D%2C%0A%20%20%22review_operation_statuses%22%3A%20%5B%5D%2C%0A%20%20%22boundary%22%3A%20%7B%0A%20%20%20%20%22local_only_project_store%22%3A%20true%2C%0A%20%20%20%20%22repository_default_private_write%22%3A%20false%2C%0A%20%20%20%20%22external_file_copy_performed%22%3A%20false%2C%0A%20%20%20%20%22network_required%22%3A%20false%2C%0A%20%20%20%20%22daemon_required%22%3A%20false%2C%0A%20%20%20%20%22telemetry_enabled%22%3A%20false%2C%0A%20%20%20%20%22accepted_model_state_mutated%22%3A%20false%2C%0A%20%20%20%20%22private_payload_included%22%3A%20false%2C%0A%20%20%20%20%22protected_content_included%22%3A%20false%2C%0A%20%20%20%20%22release_or_professional_claim%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22diagnostics%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22code%22%3A%20%22PROJECT-VALIDATION-PREFLIGHT-ONLY%22%2C%0A%20%20%20%20%20%20%22class%22%3A%20%22MIGRATION%22%2C%0A%20%20%20%20%20%20%22severity%22%3A%20%22info%22%2C%0A%20%20%20%20%20%20%22source%22%3A%20%22apps%2Fdesktop%2Fsrc%2Ffeatures%2Fproject-validation%2FProjectValidationPanel.tsx%22%2C%0A%20%20%20%20%20%20%22message%22%3A%20%22Validation%20preflight%20is%20local%20evidence.%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22code%22%3A%20%22PROJECT-VALIDATION-MODEL-HASH-REVIEW-ONLY%22%2C%0A%20%20%20%20%20%20%22class%22%3A%20%22REPRODUCIBILITY%22%2C%0A%20%20%20%20%20%20%22severity%22%3A%20%22info%22%2C%0A%20%20%20%20%20%20%22source%22%3A%20%22apps%2Fdesktop%2Fsrc%2Ffeatures%2Fproject-validation%2FProjectValidationPanel.tsx%22%2C%0A%20%20%20%20%20%20%22message%22%3A%20%22Canonical%20model%20hash%20is%20a%20local%20review-reproducibility%20signal%20only%2C%20scoped%20to%20the%20model%20payload.%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22code%22%3A%20%22PROJECT-VALIDATION-ENVELOPE-HASH-REVIEW-ONLY%22%2C%0A%20%20%20%20%20%20%22class%22%3A%20%22REPRODUCIBILITY%22%2C%0A%20%20%20%20%20%20%22severity%22%3A%20%22info%22%2C%0A%20%20%20%20%20%20%22source%22%3A%20%22apps%2Fdesktop%2Fsrc%2Ffeatures%2Fproject-validation%2FProjectValidationPanel.tsx%22%2C%0A%20%20%20%20%20%20%22message%22%3A%20%22Project-envelope%20hash%20is%20a%20local%20review-reproducibility%20signal%20over%20the%20persisted%20envelope%20payload%20(storage%20summary%20and%20hash%20carrier%20excluded).%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22code%22%3A%20%22PROJECT-VALIDATION-STORE-MIGRATION-LEDGER-REVIEW-ONLY%22%2C%0A%20%20%20%20%20%20%22class%22%3A%20%22MIGRATION%22%2C%0A%20%20%20%20%20%20%22severity%22%3A%20%22info%22%2C%0A%20%20%20%20%20%20%22source%22%3A%20%22apps%2Fdesktop%2Fsrc%2Ffeatures%2Fproject-validation%2FProjectValidationPanel.tsx%22%2C%0A%20%20%20%20%20%20%22message%22%3A%20%22Store%20migration%20evidence%20covers%20the%20local%20store%20schema%20ledger%20only%3B%20model%20document%20migrations%20remain%20TBD%20and%20no%20migration%20claim%20exceeds%20the%20local%20store.%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22code%22%3A%20%22PROJECT-VALIDATION-STALE-SCHEMA%22%2C%0A%20%20%20%20%20%20%22class%22%3A%20%22SCHEMA_VALIDATION%22%2C%0A%20%20%20%20%20%20%22severity%22%3A%20%22warning%22%2C%0A%20%20%20%20%20%20%22source%22%3A%20%22apps%2Fdesktop%2Fsrc%2Ffeatures%2Fproject-validation%2FProjectValidationPanel.tsx%22%2C%0A%20%20%20%20%20%20%22message%22%3A%20%22Project%20schema%20version%20is%20stale%20relative%20to%20current%20authoring%20schema_version%200.2.0%3B%20use%20the%20governed%20in-memory%20migration%20path%20before%20treating%20it%20as%20current.%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22data_boundary%22%3A%20%7B%0A%20%20%20%20%22public_examples_policy%22%3A%20%22invented_or_cleared_data_only%22%2C%0A%20%20%20%20%22protected_source_policy%22%3A%20%22no_bundled_protected_owner_or_standards_data%22%2C%0A%20%20%20%20%22private_data_policy%22%3A%20%22no_private_project_data%22%2C%0A%20%20%20%20%22professional_boundary%22%3A%20%22technical_preview_requires_human_engineering_review%22%0A%20%20%7D%2C%0A%20%20%22private_payload_included%22%3A%20false%2C%0A%20%20%22protected_content_included%22%3A%20false%2C%0A%20%20%22release_or_professional_claim%22%3A%20false%2C%0A%20%20%22professional_boundary%22%3A%20%7B%0A%20%20%20%20%22human_review_required%22%3A%20true%2C%0A%20%20%20%20%22software_makes_compliance_claim%22%3A%20false%2C%0A%20%20%20%20%22software_makes_certification_claim%22%3A%20false%2C%0A%20%20%20%20%22software_makes_sealing_claim%22%3A%20false%2C%0A%20%20%20%20%22software_makes_approval_claim%22%3A%20false%2C%0A%20%20%20%20%22software_makes_authentication_claim%22%3A%20false%0A%20%20%7D%0A%7D%0A
                  - img [ref=e428]
                  - text: Validation JSON
              - generic [ref=e431]: validation=preview_current; version=stale; migration=browser_memory_snapshot_no_sql_store_migrations_applicable; round_trip=semantic_categories_declared
            - generic [ref=e432]:
              - generic [ref=e433]:
                - generic [ref=e434]: Schema and version
                - strong [ref=e435]: schema_version=0.1.0; document_kind=openpipestress.product_preview.model; profile=technical_preview_project_persistence_preflight
              - generic [ref=e436]:
                - generic [ref=e437]: Round-trip manifest
                - strong [ref=e438]: 6 categories; unit metadata=ready_for_preview_round_trip; provenance=ready_for_preview_round_trip; reproducibility=model_hash_verified_on_open
              - generic [ref=e439]:
                - generic [ref=e440]: Unit round-trip evidence
                - strong [ref=e441]: status=unit_metadata_preserved_in_local_project_envelope; checked_refs=11; signature=materials.material:invented-carbon-steel.elastic_modulus=Pa|materials.material:invented-carbon-steel.shear_modulus=Pa|materials.material:invented-carbon-steel.thermal_expansion_coefficient=1/degC|pipe_segments.P.section.outside_diameter=m|pipe_segments.P.section.wall_thickness=m|project.units.angle=rad|project.units.force=N|project.units.length=m|project.units.pressure=Pa|project.units.stress=MPa|project.units.temperature=degC
              - generic [ref=e442]:
                - generic [ref=e443]: Unit policy
                - strong [ref=e444]: model=angle=rad,force=N,length=m,pressure=Pa,stress=MPa,temperature=degC; records=5; round_trip=unit_metadata_preserved_in_local_project_envelope; conversion=false
              - generic [ref=e445]:
                - generic [ref=e446]: Model hash evidence
                - strong [ref=e447]: model_hash=model_hash_verified_on_open; persisted_model_hashes=1; persisted_model_hash_ref=sha256:248043c8851784c27f6db1c6266002d2c0d402467f25eeb0cf98b39f89ca23ea; integrity=verified_match; claim_standing=not_recorded; source=open; observed_at=2026-09-24T06:52:07.144Z; persisted snapshot only; later local edits are not verified
              - generic [ref=e448]:
                - generic [ref=e449]: Envelope hash evidence
                - strong [ref=e450]: envelope_hash=project_envelope_hash_verified_on_open; persisted_envelope_hashes=1; persisted_envelope_hash_ref=sha256:ef0aa6fd23739ad4f7137588f4a356724e11f07dfa0abce54a94da43bf5a28d3; integrity=verified_match; source=open; observed_at=2026-09-24T06:52:07.150Z; persisted snapshot only; later local edits are not verified
              - generic [ref=e451]:
                - generic [ref=e452]: Store migration evidence
                - strong [ref=e453]: framework=browser_memory_preview_no_sqlite_migration_ledger; store_schema_version=0; target=0; applied_on_open=0; status=browser_memory_snapshot_no_sql_store_migrations_applicable
              - generic [ref=e454]:
                - generic [ref=e455]: Model document migration
                - strong [ref=e456]: status=migrated; source=0.1.0; target=0.2.0; framework=application_service_separate_db_and_product_schema; persistence=in_memory_only_not_yet_saved; ledger_records=0
              - generic [ref=e457]:
                - generic [ref=e458]: Persistence operations
                - strong [ref=e459]: validate=preflight_generated_preview_current; version_check=stale; migrate=browser_memory_snapshot_no_sql_store_migrations_applicable; pending operations=0; persisted editor intents=0; proposals=0; persisted proposals=0; persisted review targets=0; persisted review target ref=not_selected; persisted mechanics results=0; persisted analysis runs=0; persisted analysis run ref=not_persisted
              - generic [ref=e460]:
                - generic [ref=e461]: Validation boundary
                - strong [ref=e462]: accepted_state_mutated=false; network=false; telemetry=false; private/protected payload=false
            - generic [ref=e463]: Validation preflight records version, migration, and round-trip review evidence locally without applying queued operations.
    - complementary "Agent" [ref=e464]:
      - button "Agent" [disabled] [ref=e466]:
        - img [ref=e467]
        - generic [ref=e470]: Agent
  - generic "Workspace status" [ref=e471]:
    - generic "Analysis statuses"
    - button "3 Issues" [ref=e472] [cursor=pointer]:
      - img [ref=e473]
      - text: 3 Issues
    - generic "Selection" [ref=e475]: "project: project:invented-loop-01"
    - generic "Display units" [ref=e476]: Entered
    - button "About SWBPIPE…" [ref=e477] [cursor=pointer]:
      - img [ref=e478]
```

# Test source

```ts
  1   | import { expect, type Locator, type Page } from "@playwright/test";
  2   | 
  3   | export type TreeEntityType =
  4   |   | "project"
  5   |   | "material"
  6   |   | "section"
  7   |   | "node"
  8   |   | "pipe"
  9   |   | "support"
  10  |   | "component"
  11  |   | "load"
  12  |   | "combination"
  13  |   | "diagnostic";
  14  | 
  15  | type WorkspaceSectionId =
  16  |   | "operations"
  17  |   | "loads"
  18  |   | "libraries"
  19  |   | "rule-packs"
  20  |   | "solve"
  21  |   | "results"
  22  |   | "report"
  23  |   | "project"
  24  |   | "exports"
  25  |   | "evidence";
  26  | 
  27  | export async function openWorkspaceSection(page: Page, sectionId: WorkspaceSectionId): Promise<Locator> {
  28  |   const section = page.getByTestId(`workspace-section-${sectionId}`);
  29  |   if (!await section.isVisible()) {
  30  |     // Review changes is a tab of the Model stage's strip; from another stage it is summoned by the
  31  |     // section command, as every other section is.
  32  |     if (sectionId === "operations" && await page.getByTestId("workspace-review").isVisible()) {
> 33  |       await page.getByTestId("workspace-review").click();
      |                                                  ^ Error: locator.click: Test timeout of 120000ms exceeded.
  34  |     } else {
  35  |       await page.getByTestId("menu-view").click();
  36  |       await page.getByTestId(`menu-item-view.section.${sectionId}`).click();
  37  |     }
  38  |   }
  39  |   await expect(section).toBeVisible();
  40  |   if (sectionId === "operations") {
  41  |     const review = page.getByTestId("operation-tab-review");
  42  |     if (await review.getAttribute("aria-pressed") !== "true") await review.click();
  43  |     await expect(review).toHaveAttribute("aria-pressed", "true");
  44  |   }
  45  |   return section;
  46  | }
  47  | 
  48  | // Slice B3: the dock is gone. A page closes onto its stage by its close control;
  49  | // "no section on screen" is the Model stage's model tree, reached by the rail and the tab.
  50  | export async function closeWorkspacePanels(page: Page): Promise<void> {
  51  |   const close = page.getByTestId("workspace-dock-close");
  52  |   if (await close.isVisible()) await close.click();
  53  |   await showModelTree(page);
  54  |   await expect(page.locator('[data-testid^="workspace-section-"]:visible')).toHaveCount(0);
  55  | }
  56  | 
  57  | /** The model tree is the Model stage's first tab. */
  58  | export async function showModelTree(page: Page): Promise<void> {
  59  |   const host = page.getByTestId("shell-tree-host");
  60  |   // An open page lies over the tree without hiding it from the layout: close it first.
  61  |   const close = page.getByTestId("workspace-dock-close");
  62  |   if (await close.isVisible()) await close.click();
  63  |   if (!await host.isVisible()) {
  64  |     if (await page.getByTestId("rail-stage-model").getAttribute("aria-current") !== "page") await page.getByTestId("rail-stage-model").click();
  65  |     const tab = page.getByTestId("stage-tab-model-tree");
  66  |     if (await tab.getAttribute("aria-pressed") !== "true") await tab.click();
  67  |     await ensureRailExpanded(page, "toggle-tree");
  68  |   }
  69  |   await expect(host).toBeVisible();
  70  | }
  71  | 
  72  | /** Close the Both view inspector (table-first lending when docked, slide-over when narrow). */
  73  | export async function ensureInspectorCollapsed(page: Page): Promise<void> {
  74  |   const toggle = page.getByTestId("toggle-inspector");
  75  |   if (await toggle.getAttribute("aria-disabled") !== "true" && await toggle.getAttribute("aria-expanded") === "true") await toggle.click();
  76  | }
  77  | 
  78  | export async function ensureTreeExpanded(page: Page): Promise<void> {
  79  |   await showModelTree(page);
  80  |   await ensureRailExpanded(page, "toggle-tree");
  81  | }
  82  | 
  83  | // The inspector is docked in Model view, opened by the toolbar's toggle in Both view,
  84  | // and absent in Table view: a test that needs it in Table view asks for Both view first.
  85  | export async function ensureInspectorExpanded(page: Page): Promise<void> {
  86  |   const toggle = page.getByTestId("toggle-inspector");
  87  |   if (await toggle.getAttribute("aria-disabled") === "true" && await toggle.getAttribute("aria-expanded") !== "true") {
  88  |     await page.getByTestId("view-switch-both").click();
  89  |   }
  90  |   await ensureRailExpanded(page, "toggle-inspector");
  91  | }
  92  | 
  93  | async function ensureRailExpanded(page: Page, testId: "toggle-tree" | "toggle-inspector"): Promise<void> {
  94  |   const toggle = page.getByTestId(testId);
  95  |   if (await toggle.getAttribute("aria-expanded") !== "true") {
  96  |     // The narrow inspector overlays the table chevron. Close it through its
  97  |     // toolbar control before the pointer opens the table's successor drawer.
  98  |     if (testId === "toggle-tree" && (page.viewportSize()?.width ?? Infinity) < 1280) {
  99  |       await ensureInspectorCollapsed(page);
  100 |     }
  101 |     await toggle.click();
  102 |   }
  103 |   await expect(toggle).toHaveAttribute("aria-expanded", "true");
  104 | }
  105 | 
  106 | export function treeRowTestId(type: TreeEntityType, id: string): string {
  107 |   return `tree-row-${encodeURIComponent(type)}-${encodeURIComponent(id)}`;
  108 | }
  109 | 
  110 | export function treeEntity(page: Page, type: TreeEntityType, id: string): Locator {
  111 |   return page.getByTestId(treeRowTestId(type, id));
  112 | }
  113 | 
  114 | export async function revealTreeEntity(page: Page, type: TreeEntityType, id: string): Promise<Locator> {
  115 |   await ensureTreeExpanded(page);
  116 |   const filter = page.getByTestId("model-tree-filter-input");
  117 |   await filter.fill(id);
  118 |   const row = treeEntity(page, type, id);
  119 |   await expect(row).toBeVisible();
  120 |   return row;
  121 | }
  122 | 
  123 | export async function selectTreeEntity(page: Page, type: TreeEntityType, id: string): Promise<Locator> {
  124 |   const row = await revealTreeEntity(page, type, id);
  125 |   await row.click();
  126 |   await expect(row).toHaveAttribute("aria-selected", "true");
  127 |   return row;
  128 | }
  129 | 
  130 | export async function expectTreeEntity(
  131 |   page: Page,
  132 |   type: TreeEntityType,
  133 |   id: string,
```