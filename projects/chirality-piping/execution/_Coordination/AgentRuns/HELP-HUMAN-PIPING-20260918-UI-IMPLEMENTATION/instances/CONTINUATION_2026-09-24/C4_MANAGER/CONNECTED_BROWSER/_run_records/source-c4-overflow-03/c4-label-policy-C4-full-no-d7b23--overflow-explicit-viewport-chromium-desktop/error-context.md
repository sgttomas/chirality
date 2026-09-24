# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: c4-label-policy.spec.ts >> C4 full node inventory and actual placed context overflow @explicit-viewport
- Location: e2e/c4-label-policy.scenarios.ts:155:3

# Error details

```
Error: expect(received).toBeGreaterThan(expected)

Expected: > 113
Received:   83
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
          - button "Results" [disabled] [pressed] [ref=e101]:
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
    - region "Modeling workspace" [ref=e134]:
      - generic [ref=e135]:
        - group "Tables" [ref=e136]:
          - button "Results" [pressed] [ref=e137] [cursor=pointer]
          - button "Evidence" [ref=e138] [cursor=pointer]
          - button "Collapse table drawer" [disabled] [expanded] [ref=e141]:
            - img [ref=e142]
        - region "Results section" [ref=e146]:
          - region "Results" [ref=e147]:
            - generic [ref=e148]: Results
            - paragraph [ref=e149]: Run the bounded preview mechanics path to populate result summaries.
          - region "Comparison workspace" [ref=e150]:
            - generic [ref=e151]:
              - img [ref=e152]
              - text: Comparison
            - paragraph [ref=e157]: Run mechanics preview to populate the local comparison workspace from stable result IDs and explicit source result references.
          - region "Design-authoring workspace" [ref=e158]:
            - generic [ref=e159]:
              - img [ref=e160]
              - text: Design Workspace
            - generic [ref=e165]:
              - generic [ref=e166]:
                - generic [ref=e167]:
                  - checkbox "Include known private values in this local export" [ref=e168]
                  - text: Include known private values in this local export
                - generic [ref=e169]: decisions=112; findings=112; blocked=true
                - group [ref=e170]:
                  - generic "Details" [ref=e171] [cursor=pointer]
                - generic [ref=e172]:
                  - img [ref=e173]
                  - text: Workspace JSON
              - generic [ref=e176]: knowledge=3; states=0; runs=0; comparisons=0; operations=0
            - generic [ref=e177]:
              - generic [ref=e178]:
                - generic [ref=e179]: Core contract
                - strong [ref=e180]: records=2; warnings=1; states=2; runs=2; overlays=5
              - generic [ref=e181]:
                - generic [ref=e182]: Current browser
                - strong [ref=e183]: analysis_run=not generated; comparison=not generated; result_rows=0
              - generic [ref=e184]:
                - generic [ref=e185]: Operation review
                - strong [ref=e186]: records=0; accepted_mutation=false; application=empty_operation_queue
              - generic [ref=e187]:
                - generic [ref=e188]: Routing
                - strong [ref=e189]: selected=none; route=no_selected_review_target
              - generic [ref=e190]:
                - generic [ref=e191]: Units
                - strong [ref=e192]: model=angle=rad,force=N,length=m,pressure=Pa,stress=MPa,temperature=degC; results=none; comparison=none; conversion=false
              - generic [ref=e193]:
                - generic [ref=e194]: Boundary
                - strong [ref=e195]: private_payload=false; protected=false; professional_claim=false
            - generic [ref=e196]: Design workspace evidence is a local composition of GUI state, comparison context, and operation-review metadata. It does not apply operations or mutate accepted model state.
      - separator "Resize table and canvas" [ref=e197]
      - generic [ref=e199]:
        - generic [ref=e200]:
          - group "Viewport controls" [ref=e201]:
            - generic [ref=e202]: 3D Centerline
            - group "Viewport deformation overlay status" [ref=e203]:
              - generic "Deformation · unavailable" [ref=e204] [cursor=pointer]
            - group "Viewport display toggles" [ref=e205]:
              - 'button "Labels: Budget. Cycle Budget, All, Off" [ref=e206]': "Labels: Budget"
              - button "Loads" [pressed] [ref=e207]
              - button "Grid" [pressed] [ref=e208]
            - group "Viewport selection tools" [ref=e209]:
              - button "Box Select" [ref=e210]
              - generic [ref=e211]:
                - generic [ref=e212]: Selection filter
                - combobox "Selection filter" [ref=e213]:
                  - option "All"
                  - option "Pipes"
                  - option "Nodes" [selected]
                  - option "Supports"
                  - option "Components"
              - button "Hide" [ref=e214]
              - button "Isolate" [ref=e215]
              - button "Show All" [disabled] [ref=e216]
              - generic [ref=e217]: Isolate captures the selected geometry. Other shown geometry is dimmed to 20% and remains available to click, hover and box selection; nearer dimmed geometry can be picked before farther undimmed geometry. Selection does not change the snapshot. Hide takes precedence. Show All clears both. I and H apply while focus is in the viewport.
              - button "Fit Model" [ref=e218]
              - button "Fit Visible" [ref=e219]
              - button "Fit Selection" [ref=e220]
            - group "Viewport geometry" [ref=e221]:
              - button "Schematic" [pressed] [ref=e222]
              - button "Actual OD" [ref=e223]
              - button "Measure" [ref=e224]
          - generic "Viewport status" [ref=e225]:
            - 'generic "Selected node: n135" [ref=e226]': "Selected: n135"
            - group [ref=e227]:
              - generic "54 annotations omitted" [active] [ref=e228]
            - status "Schematic centerline geometry" [ref=e229]
            - status "View command status" [ref=e230]: Box Select disabled.
        - generic [ref=e231]:
          - generic "Three.js pipe centerline viewport" [ref=e232]
          - generic "Viewport entity selection":
            - button "Select n0 in viewport" [pressed] [ref=e234] [cursor=pointer]:
              - img [ref=e235]
              - generic [ref=e238]: n0
            - button "Select n1 in viewport" [pressed] [ref=e239] [cursor=pointer]:
              - img [ref=e240]
              - generic [ref=e243]: n1
            - button "Select n2 in viewport" [pressed] [ref=e244] [cursor=pointer]:
              - img [ref=e245]
              - generic [ref=e248]: n2
            - button "Select n3 in viewport" [pressed] [ref=e249] [cursor=pointer]:
              - img [ref=e250]
              - generic [ref=e253]: n3
            - button "Select n4 in viewport" [pressed] [ref=e254] [cursor=pointer]:
              - img [ref=e255]
              - generic [ref=e258]: n4
            - button "Select n5 in viewport" [pressed] [ref=e259] [cursor=pointer]:
              - img [ref=e260]
              - generic [ref=e263]: n5
            - button "Select n6 in viewport" [pressed] [ref=e264] [cursor=pointer]:
              - img [ref=e265]
              - generic [ref=e268]: n6
            - button "Select n7 in viewport" [pressed] [ref=e269] [cursor=pointer]:
              - img [ref=e270]
              - generic [ref=e273]: n7
            - button "Select n8 in viewport" [pressed] [ref=e274] [cursor=pointer]:
              - img [ref=e275]
              - generic [ref=e278]: n8
            - button "Select n9 in viewport" [pressed] [ref=e279] [cursor=pointer]:
              - img [ref=e280]
              - generic [ref=e283]: n9
            - button "Select n10 in viewport" [pressed] [ref=e284] [cursor=pointer]:
              - img [ref=e285]
              - generic [ref=e288]: n10
            - button "Select n11 in viewport" [pressed] [ref=e289] [cursor=pointer]:
              - img [ref=e290]
              - generic [ref=e293]: n11
            - button "Select n12 in viewport" [pressed] [ref=e294] [cursor=pointer]:
              - img [ref=e295]
              - generic [ref=e298]: n12
            - button "Select n17 in viewport" [pressed] [ref=e299] [cursor=pointer]:
              - img [ref=e300]
              - generic [ref=e303]: n17
            - button "Select n18 in viewport" [pressed] [ref=e304] [cursor=pointer]:
              - img [ref=e305]
              - generic [ref=e308]: n18
            - button "Select n19 in viewport" [pressed] [ref=e309] [cursor=pointer]:
              - img [ref=e310]
              - generic [ref=e313]: n19
            - button "Select n20 in viewport" [pressed] [ref=e314] [cursor=pointer]:
              - img [ref=e315]
              - generic [ref=e318]: n20
            - button "Select n21 in viewport" [pressed] [ref=e319] [cursor=pointer]:
              - img [ref=e320]
              - generic [ref=e323]: n21
            - button "Select n22 in viewport" [pressed] [ref=e324] [cursor=pointer]:
              - img [ref=e325]
              - generic [ref=e328]: n22
            - button "Select n23 in viewport" [pressed] [ref=e329] [cursor=pointer]:
              - img [ref=e330]
              - generic [ref=e333]: n23
            - button "Select n24 in viewport" [pressed] [ref=e334] [cursor=pointer]:
              - img [ref=e335]
              - generic [ref=e338]: n24
            - button "Select n25 in viewport" [pressed] [ref=e339] [cursor=pointer]:
              - img [ref=e340]
              - generic [ref=e343]: n25
            - button "Select n26 in viewport" [pressed] [ref=e344] [cursor=pointer]:
              - img [ref=e345]
              - generic [ref=e348]: n26
            - button "Select n27 in viewport" [pressed] [ref=e349] [cursor=pointer]:
              - img [ref=e350]
              - generic [ref=e353]: n27
            - button "Select n28 in viewport" [pressed] [ref=e354] [cursor=pointer]:
              - img [ref=e355]
              - generic [ref=e358]: n28
            - button "Select n34 in viewport" [pressed] [ref=e359] [cursor=pointer]:
              - img [ref=e360]
              - generic [ref=e363]: n34
            - button "Select n35 in viewport" [pressed] [ref=e364] [cursor=pointer]:
              - img [ref=e365]
              - generic [ref=e368]: n35
            - button "Select n36 in viewport" [pressed] [ref=e369] [cursor=pointer]:
              - img [ref=e370]
              - generic [ref=e373]: n36
            - button "Select n37 in viewport" [pressed] [ref=e374] [cursor=pointer]:
              - img [ref=e375]
              - generic [ref=e378]: n37
            - button "Select n38 in viewport" [pressed] [ref=e379] [cursor=pointer]:
              - img [ref=e380]
              - generic [ref=e383]: n38
            - button "Select n39 in viewport" [pressed] [ref=e384] [cursor=pointer]:
              - img [ref=e385]
              - generic [ref=e388]: n39
            - button "Select n40 in viewport" [pressed] [ref=e389] [cursor=pointer]:
              - img [ref=e390]
              - generic [ref=e393]: n40
            - button "Select n41 in viewport" [pressed] [ref=e394] [cursor=pointer]:
              - img [ref=e395]
              - generic [ref=e398]: n41
            - button "Select n42 in viewport" [pressed] [ref=e399] [cursor=pointer]:
              - img [ref=e400]
              - generic [ref=e403]: n42
            - button "Select n43 in viewport" [pressed] [ref=e404] [cursor=pointer]:
              - img [ref=e405]
              - generic [ref=e408]: n43
            - button "Select n44 in viewport" [pressed] [ref=e409] [cursor=pointer]:
              - img [ref=e410]
              - generic [ref=e413]: n44
            - button "Select n45 in viewport" [pressed] [ref=e414] [cursor=pointer]:
              - img [ref=e415]
              - generic [ref=e418]: n45
            - button "Select n51 in viewport" [pressed] [ref=e419] [cursor=pointer]:
              - img [ref=e420]
              - generic [ref=e423]: n51
            - button "Select n52 in viewport" [pressed] [ref=e424] [cursor=pointer]:
              - img [ref=e425]
              - generic [ref=e428]: n52
            - button "Select n53 in viewport" [pressed] [ref=e429] [cursor=pointer]:
              - img [ref=e430]
              - generic [ref=e433]: n53
            - button "Select n54 in viewport" [pressed] [ref=e434] [cursor=pointer]:
              - img [ref=e435]
              - generic [ref=e438]: n54
            - button "Select n55 in viewport" [pressed] [ref=e439] [cursor=pointer]:
              - img [ref=e440]
              - generic [ref=e443]: n55
            - button "Select n56 in viewport" [pressed] [ref=e444] [cursor=pointer]:
              - img [ref=e445]
              - generic [ref=e448]: n56
            - button "Select n57 in viewport" [pressed] [ref=e449] [cursor=pointer]:
              - img [ref=e450]
              - generic [ref=e453]: n57
            - button "Select n58 in viewport" [pressed] [ref=e454] [cursor=pointer]:
              - img [ref=e455]
              - generic [ref=e458]: n58
            - button "Select n59 in viewport" [pressed] [ref=e459] [cursor=pointer]:
              - img [ref=e460]
              - generic [ref=e463]: n59
            - button "Select n60 in viewport" [pressed] [ref=e464] [cursor=pointer]:
              - img [ref=e465]
              - generic [ref=e468]: n60
            - button "Select n61 in viewport" [pressed] [ref=e469] [cursor=pointer]:
              - img [ref=e470]
              - generic [ref=e473]: n61
            - button "Select n68 in viewport" [pressed] [ref=e474] [cursor=pointer]:
              - img [ref=e475]
              - generic [ref=e478]: n68
            - button "Select n69 in viewport" [pressed] [ref=e479] [cursor=pointer]:
              - img [ref=e480]
              - generic [ref=e483]: n69
            - button "Select n70 in viewport" [pressed] [ref=e484] [cursor=pointer]:
              - img [ref=e485]
              - generic [ref=e488]: n70
            - button "Select n71 in viewport" [pressed] [ref=e489] [cursor=pointer]:
              - img [ref=e490]
              - generic [ref=e493]: n71
            - button "Select n72 in viewport" [pressed] [ref=e494] [cursor=pointer]:
              - img [ref=e495]
              - generic [ref=e498]: n72
            - button "Select n73 in viewport" [pressed] [ref=e499] [cursor=pointer]:
              - img [ref=e500]
              - generic [ref=e503]: n73
            - button "Select n74 in viewport" [pressed] [ref=e504] [cursor=pointer]:
              - img [ref=e505]
              - generic [ref=e508]: n74
            - button "Select n75 in viewport" [pressed] [ref=e509] [cursor=pointer]:
              - img [ref=e510]
              - generic [ref=e513]: n75
            - button "Select n76 in viewport" [pressed] [ref=e514] [cursor=pointer]:
              - img [ref=e515]
              - generic [ref=e518]: n76
            - button "Select n78 in viewport" [pressed] [ref=e519] [cursor=pointer]:
              - img [ref=e520]
              - generic [ref=e523]: n78
            - button "Select n85 in viewport" [pressed] [ref=e524] [cursor=pointer]:
              - img [ref=e525]
              - generic [ref=e528]: n85
            - button "Select n86 in viewport" [pressed] [ref=e529] [cursor=pointer]:
              - img [ref=e530]
              - generic [ref=e533]: n86
            - button "Select n87 in viewport" [pressed] [ref=e534] [cursor=pointer]:
              - img [ref=e535]
              - generic [ref=e538]: n87
            - button "Select n88 in viewport" [pressed] [ref=e539] [cursor=pointer]:
              - img [ref=e540]
              - generic [ref=e543]: n88
            - button "Select n89 in viewport" [pressed] [ref=e544] [cursor=pointer]:
              - img [ref=e545]
              - generic [ref=e548]: n89
            - button "Select n90 in viewport" [pressed] [ref=e549] [cursor=pointer]:
              - img [ref=e550]
              - generic [ref=e553]: n90
            - button "Select n91 in viewport" [pressed] [ref=e554] [cursor=pointer]:
              - img [ref=e555]
              - generic [ref=e558]: n91
            - button "Select n92 in viewport" [pressed] [ref=e559] [cursor=pointer]:
              - img [ref=e560]
              - generic [ref=e563]: n92
            - button "Select n93 in viewport" [pressed] [ref=e564] [cursor=pointer]:
              - img [ref=e565]
              - generic [ref=e568]: n93
            - button "Select n95 in viewport" [pressed] [ref=e569] [cursor=pointer]:
              - img [ref=e570]
              - generic [ref=e573]: n95
            - button "Select n102 in viewport" [pressed] [ref=e574] [cursor=pointer]:
              - img [ref=e575]
              - generic [ref=e578]: n102
            - button "Select n103 in viewport" [pressed] [ref=e579] [cursor=pointer]:
              - img [ref=e580]
              - generic [ref=e583]: n103
            - button "Select n104 in viewport" [pressed] [ref=e584] [cursor=pointer]:
              - img [ref=e585]
              - generic [ref=e588]: n104
            - button "Select n105 in viewport" [pressed] [ref=e589] [cursor=pointer]:
              - img [ref=e590]
              - generic [ref=e593]: n105
            - button "Select n106 in viewport" [pressed] [ref=e594] [cursor=pointer]:
              - img [ref=e595]
              - generic [ref=e598]: n106
            - button "Select n108 in viewport" [pressed] [ref=e599] [cursor=pointer]:
              - img [ref=e600]
              - generic [ref=e603]: n108
            - button "Select n110 in viewport" [pressed] [ref=e604] [cursor=pointer]:
              - img [ref=e605]
              - generic [ref=e608]: n110
            - button "Select n112 in viewport" [pressed] [ref=e609] [cursor=pointer]:
              - img [ref=e610]
              - generic [ref=e613]: n112
            - button "Select n119 in viewport" [pressed] [ref=e614] [cursor=pointer]:
              - img [ref=e615]
              - generic [ref=e618]: n119
            - button "Select n120 in viewport" [pressed] [ref=e619] [cursor=pointer]:
              - img [ref=e620]
              - generic [ref=e623]: n120
            - button "Select n121 in viewport" [pressed] [ref=e624] [cursor=pointer]:
              - img [ref=e625]
              - generic [ref=e628]: n121
            - button "Select n123 in viewport" [pressed] [ref=e629] [cursor=pointer]:
              - img [ref=e630]
              - generic [ref=e633]: n123
            - button "Select n125 in viewport" [pressed] [ref=e634] [cursor=pointer]:
              - img [ref=e635]
              - generic [ref=e638]: n125
            - button "Select n131 in viewport" [pressed] [ref=e639] [cursor=pointer]:
              - img [ref=e640]
              - generic [ref=e643]: n131
            - button "Select n135 in viewport" [pressed] [ref=e644] [cursor=pointer]:
              - img [ref=e645]
              - generic [ref=e648]: n135
          - img "Orientation gizmo showing X, Y, Z axes"
          - generic "View controls" [ref=e649]:
            - button "Front" [pressed] [ref=e650] [cursor=pointer]
            - button "Top" [ref=e651] [cursor=pointer]
            - button "Isometric" [ref=e652] [cursor=pointer]
          - generic:
            - generic: 1 m
        - region "Command and selection bar" [ref=e653]:
          - generic "Object creation tools" [ref=e654]:
            - button "Node" [ref=e655] [cursor=pointer]:
              - img [ref=e656]
              - text: Node
            - button "Pipe" [ref=e658] [cursor=pointer]:
              - img [ref=e659]
              - text: Pipe
            - button "Support" [ref=e663] [cursor=pointer]:
              - img [ref=e664]
              - text: Support
            - button "Component" [ref=e667] [cursor=pointer]:
              - img [ref=e668]
              - text: Component
            - button "Load" [ref=e671] [cursor=pointer]:
              - img [ref=e672]
              - text: Load
          - generic "Model focus" [ref=e674]: Select
          - group [ref=e675]:
            - generic "Selection & navigation" [ref=e676] [cursor=pointer]
      - text: ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾
    - complementary "Agent" [ref=e677]:
      - button "Agent" [disabled] [ref=e679]:
        - img [ref=e680]
        - generic [ref=e683]: Agent
  - generic "Workspace status" [ref=e684]:
    - generic "Analysis statuses"
    - button "3 Issues" [ref=e685] [cursor=pointer]:
      - img [ref=e686]
      - text: 3 Issues
    - generic "Selection" [ref=e688]: "node: n135 · 136 selected"
    - generic "Display units" [ref=e689]: Entered
    - button "About SWBPIPE…" [ref=e690] [cursor=pointer]:
      - img [ref=e691]
```

# Test source

```ts
  80  |   expect(evidence.labels.renderedCount).toBe(evidence.boxes.length);
  81  |   expect(evidence.labels.budget).toBe(Math.floor(evidence.canvas.width * evidence.canvas.height / 3600));
  82  |   expect(new Set(evidence.boxes.map(b => b.key)).size).toBe(evidence.boxes.length);
  83  |   for (const [i, { rect: a }] of evidence.boxes.entries()) {
  84  |     expect(a.left).toBeGreaterThanOrEqual(evidence.canvas.left); expect(a.right).toBeLessThanOrEqual(evidence.canvas.right);
  85  |     expect(a.top).toBeGreaterThanOrEqual(evidence.canvas.top); expect(a.bottom).toBeLessThanOrEqual(evidence.canvas.bottom);
  86  |     for (const { rect: b } of evidence.boxes.slice(i + 1)) expect(a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top).toBe(false);
  87  |   }
  88  |   const omissions = page.getByTestId("viewport-label-omissions");
  89  |   await omissions.locator("summary").click();
  90  |   const omitted = [...(evidence.labels.suppressed ?? []), ...(evidence.labels.unplaced ?? [])];
  91  |   await expect(omissions.locator("li")).toHaveCount(omitted.length);
  92  |   for (const item of omitted) await expect(omissions).toContainText(item.key);
  93  |   await omissions.locator("summary").click();
  94  |   return evidence;
  95  | }
  96  | async function projected(page: Page, position: { x: number; y: number; z: number }) {
  97  |   await settle(page);
  98  |   return page.evaluate(position => {
  99  |     const api = globalThis.__openPipeStressUiDiagnosticsV1, s = api.readCurrent();
  100 |     if ("status" in s.viewport || s.model.generation === null) throw new Error("Viewport unavailable");
  101 |     const p = api.projectAuthoredPoint({ modelGeneration: s.model.generation, cameraSequence: s.viewport.camera.sequence, authoredPoint: position });
  102 |     if (p.status !== "available" || !p.insideCanvasCss) throw new Error("Required real geometry pick outside canvas");
  103 |     const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!, b = canvas.getBoundingClientRect();
  104 |     const x = b.left + p.canvasCssPoint.x, y = b.top + p.canvasCssPoint.y;
  105 |     return { x, y, unobscured: document.elementFromPoint(x, y) === canvas };
  106 |   }, position);
  107 | }
  108 | export function registerC4LabelScenarios() {
  109 |   test("C4 modes, dedup, Hide/Isolate, hover, camera, resize and nonmutation @explicit-viewport", async ({ page }, info) => {
  110 |     await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
  111 |     const before = await invariants(page);
  112 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Budget");
  113 |     await selectTreeEntity(page, "node", "A"); await mode(page, "Off");
  114 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  115 |     await page.getByTestId("viewport-select-A").hover();
  116 |     const off = await witness(page, info, "off-context-deduplicated-primary-hover-row"); expect(off.labels.ordinaryCount).toBe(0);
  117 |     expect(off.labels.contextCount).toBe(1); await page.mouse.move(0, 0);
  118 |     await page.getByRole("button", { name: "Isolate", exact: true }).click();
  119 |     await mode(page, "All");
  120 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("data-dimmed", "true");
  121 |     const ordinary = page.locator('.viewport-select-target[data-label-placed="true"][aria-pressed="false"]').first();
  122 |     const box = await ordinary.boundingBox(); await ordinary.hover();
  123 |     for (let i = 0; i < 3; i++) { await settle(page); expect(await ordinary.boundingBox()).toEqual(box); }
  124 |     await page.mouse.move(0, 0); await witness(page, info, "all-hover-stable");
  125 |     await page.getByRole("button", { name: "Hide", exact: true }).click();
  126 |     for (const m of ["Budget", "All", "Off"] as const) { await mode(page, m); await expect(page.getByTestId("viewport-select-A")).toHaveCount(0); }
  127 |     await expect(page.getByTestId("viewport-hidden-count")).toHaveText("1 hidden · Show all");
  128 |     await page.getByRole("button", { name: "Show All", exact: true }).click();
  129 |     await mode(page, "All"); await page.setViewportSize({ width: 1100, height: 850 });
  130 |     await page.getByTestId("viewport-fit-model").click(); await witness(page, info, "resized-front");
  131 |     for (const node of (await fixture()).nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  132 |     await page.getByRole("button", { name: "Top", exact: true }).click(); await witness(page, info, "camera-top");
  133 |     await page.getByTestId("viewport-canvas").focus(); await page.keyboard.press("l");
  134 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Off");
  135 |     expect(await invariants(page)).toEqual(before);
  136 |   });
  137 |   test("C4 current review row B remains distinct from primary A @explicit-viewport", async ({ page }, info) => {
  138 |     await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
  139 |     const before = await invariants(page); await mode(page, "Off");
  140 |     await showModelTree(page);
  141 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("layout-mode-grid").click();
  142 |     await page.getByTestId("table-cell-A-x").click();
  143 |     await page.getByTestId("node-grid-review-disclosure").click();
  144 |     await page.getByTestId("review-cell-B-x").click();
  145 |     const current = await witness(page, info, "primary-A-review-B");
  146 |     expect(current.selection.primaryRef).toEqual({ type: "node", id: "A" });
  147 |     expect(current.selection.orderedRefs).toEqual([{ type: "node", id: "A" }]);
  148 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("aria-pressed", "false");
  149 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await expect(page.getByTestId("viewport-select-B")).toBeVisible();
  150 |     expect(current.labels.contextCount).toBe(2); expect(current.labels.ordinaryCount).toBe(0);
  151 |     await page.getByTestId("node-grid-review-disclosure").click();
  152 |     await expect(page.getByTestId("viewport-select-B")).toBeHidden();
  153 |     expect(await invariants(page)).toEqual(before);
  154 |   });
  155 |   test("C4 full node inventory and actual placed context overflow @explicit-viewport", async ({ page }, info) => {
  156 |     await page.setViewportSize({ width: 1440, height: 920 }); const model = await fixture(true); await load(page, model);
  157 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("viewport-fit-model").click();
  158 |     const before = await invariants(page); await mode(page, "Off");
  159 |     await page.getByTestId("viewport-selection-filter").selectOption("nodes"); await page.getByTestId("viewport-box-select").click();
  160 |     const points = [];
  161 |     for (const node of model.nodes) points.push(await projected(page, node.position));
  162 |     const preselection = await page.evaluate(() => {
  163 |       const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
  164 |       if ("status" in snapshot.viewport) throw new Error("Viewport unavailable");
  165 |       const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!.getBoundingClientRect();
  166 |       return { camera: snapshot.viewport.camera, canvas: canvas.toJSON(),
  167 |         measuredBudget: Math.floor(canvas.width * canvas.height / 3600), labels: snapshot.viewport.labels };
  168 |     });
  169 |     await info.attach("dense-projected-input-preselection", { body: JSON.stringify({
  170 |       ...preselection, nodes: model.nodes.map((node: any, i: number) => ({ id: node.id, authored: node.position, projected: points[i] }))
  171 |     }, null, 2), contentType: "application/json" });
  172 |     const left = Math.min(...points.map(p => p.x)) - 8, right = Math.max(...points.map(p => p.x)) + 8;
  173 |     const top = Math.min(...points.map(p => p.y)) - 8, bottom = Math.max(...points.map(p => p.y)) + 8;
  174 |     await page.mouse.move(left, top); await page.mouse.down(); await page.mouse.move(right, bottom, { steps: 6 }); await page.mouse.up();
  175 |     await page.getByTestId("viewport-box-select").click(); await mode(page, "Budget");
  176 |     const result = await witness(page, info, "dense-actual-placement");
  177 |     expect(result.selection.orderedRefs).toHaveLength(model.nodes.length);
  178 |     expect(await page.locator('.viewport-select-target[data-entity-key]').count()).toBe(model.nodes.length + model.pipe_segments.length);
  179 |     // This is deliberately a rendered-overflow assertion, never just requested > budget.
> 180 |     expect(result.labels.contextCount).toBeGreaterThan(result.labels.budget);
      |                                        ^ Error: expect(received).toBeGreaterThan(expected)
  181 |     expect(result.labels.contextOverflow).toBe(result.labels.contextCount! - result.labels.budget);
  182 |     expect(result.labels.ordinaryCount).toBe(0);
  183 |     expect(result.labels.suppressed?.some(item => item.role === "ordinary" && item.reason === "budget")).toBe(true);
  184 |     for (const node of model.nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  185 |     expect(await invariants(page)).toEqual(before);
  186 |   });
  187 |   test("C4 label modes preserve Current and Historical result standing", async ({ page }) => {
  188 |     await page.goto("/"); await openWorkspaceSection(page, "solve");
  189 |     await page.getByTestId("run-mechanics-preview").click();
  190 |     await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
  191 |     await showCanvas(page); const current = await invariants(page);
  192 |     for (const m of ["Off", "All", "Budget"] as const) await mode(page, m);
  193 |     expect(await invariants(page)).toEqual(current);
  194 |     await projectCommand(page, "save-local");
  195 |     await expect(page.getByTestId("local-project-message")).toContainText("Saved");
  196 |     await projectCommand(page, "open-local"); await openWorkspaceSection(page, "results");
  197 |     await expect(page.getByTestId("historical-run-context")).toBeVisible();
  198 |     const historical = await invariants(page);
  199 |     for (const m of ["All", "Off", "Budget"] as const) await mode(page, m);
  200 |     expect(await invariants(page)).toEqual(historical);
  201 |   });
  202 |   test("C4 real WebGL loss/restoration fails closed and recovers", async ({ page }, info) => {
  203 |     await load(page, await fixture()); await selectTreeEntity(page, "node", "A");
  204 |     const before = await invariants(page); await mode(page, "Off");
  205 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  206 |     const supported = await page.evaluate(() => {
  207 |       const canvas = document.querySelector<HTMLCanvasElement>('[data-testid="viewport-canvas"] canvas')!;
  208 |       const gl = canvas.getContext("webgl2") ?? canvas.getContext("webgl");
  209 |       const extension = gl?.getExtension("WEBGL_lose_context");
  210 |       if (!extension) return false;
  211 |       (window as any).__c4ContextExtension = extension; extension.loseContext(); return true;
  212 |     });
  213 |     await info.attach("webgl-extension-availability", { body: JSON.stringify({ supported }), contentType: "application/json" });
  214 |     test.skip(!supported, "Real WEBGL_lose_context extension unavailable; loss/restoration remains unwitnessed");
  215 |     await expect(page.getByTestId("viewport-context-status")).toContainText("lost");
  216 |     const lostLabels = await labels(page);
  217 |     await info.attach("webgl-lost-label-diagnostics", { body: JSON.stringify(lostLabels, null, 2), contentType: "application/json" });
  218 |     expect(lostLabels.placementStatus).toBe("unavailable");
  219 |     expect(lostLabels.renderedCount).toBe(0);
  220 |     await expect(page.locator('.viewport-select-target[data-label-placed="true"]')).toHaveCount(0);
  221 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("tabindex", "-1");
  222 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("aria-hidden", "true");
  223 |     await page.evaluate(() => { (window as any).__c4ContextExtension.restoreContext(); delete (window as any).__c4ContextExtension; });
  224 |     await expect(page.getByTestId("viewport-context-status")).toHaveCount(0);
  225 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await witness(page, info, "restored");
  226 |     expect(await invariants(page)).toEqual(before);
  227 |   });
  228 | }
  229 | 
```