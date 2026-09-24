# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: c4-label-policy.spec.ts >> C4 synthetic coincident real identities produce actual placed context overflow @explicit-viewport
- Location: e2e/c4-label-policy.scenarios.ts:168:3

# Error details

```
Error: A001 fits its unchanged visible label span

expect(received).toBeLessThanOrEqual(expected)

Expected: <= 28
Received:    29
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
            - 'generic "Selected node: B136" [ref=e226]': "Selected: B136"
            - group [ref=e227]:
              - generic "183 annotations omitted" [active] [ref=e228]
            - status "Schematic centerline geometry" [ref=e229]
            - status "View command status" [ref=e230]: Box Select disabled.
        - generic [ref=e231]:
          - generic "Three.js pipe centerline viewport" [ref=e232]
          - generic "Viewport entity selection":
            - button "Select A001 in viewport" [pressed] [ref=e234] [cursor=pointer]:
              - img [ref=e235]
              - generic [ref=e238]: A001
            - button "Select A002 in viewport" [pressed] [ref=e239] [cursor=pointer]:
              - img [ref=e240]
              - generic [ref=e243]: A002
            - button "Select A003 in viewport" [pressed] [ref=e244] [cursor=pointer]:
              - img [ref=e245]
              - generic [ref=e248]: A003
            - button "Select A004 in viewport" [pressed] [ref=e249] [cursor=pointer]:
              - img [ref=e250]
              - generic [ref=e253]: A004
            - button "Select A005 in viewport" [pressed] [ref=e254] [cursor=pointer]:
              - img [ref=e255]
              - generic [ref=e258]: A005
            - button "Select A006 in viewport" [pressed] [ref=e259] [cursor=pointer]:
              - img [ref=e260]
              - generic [ref=e263]: A006
            - button "Select A007 in viewport" [pressed] [ref=e264] [cursor=pointer]:
              - img [ref=e265]
              - generic [ref=e268]: A007
            - button "Select A008 in viewport" [pressed] [ref=e269] [cursor=pointer]:
              - img [ref=e270]
              - generic [ref=e273]: A008
            - button "Select A009 in viewport" [pressed] [ref=e274] [cursor=pointer]:
              - img [ref=e275]
              - generic [ref=e278]: A009
            - button "Select A010 in viewport" [pressed] [ref=e279] [cursor=pointer]:
              - img [ref=e280]
              - generic [ref=e283]: A010
            - button "Select A011 in viewport" [pressed] [ref=e284] [cursor=pointer]:
              - img [ref=e285]
              - generic [ref=e288]: A011
            - button "Select A012 in viewport" [pressed] [ref=e289] [cursor=pointer]:
              - img [ref=e290]
              - generic [ref=e293]: A012
            - button "Select A013 in viewport" [pressed] [ref=e294] [cursor=pointer]:
              - img [ref=e295]
              - generic [ref=e298]: A013
            - button "Select A018 in viewport" [pressed] [ref=e299] [cursor=pointer]:
              - img [ref=e300]
              - generic [ref=e303]: A018
            - button "Select A019 in viewport" [pressed] [ref=e304] [cursor=pointer]:
              - img [ref=e305]
              - generic [ref=e308]: A019
            - button "Select A020 in viewport" [pressed] [ref=e309] [cursor=pointer]:
              - img [ref=e310]
              - generic [ref=e313]: A020
            - button "Select A021 in viewport" [pressed] [ref=e314] [cursor=pointer]:
              - img [ref=e315]
              - generic [ref=e318]: A021
            - button "Select A022 in viewport" [pressed] [ref=e319] [cursor=pointer]:
              - img [ref=e320]
              - generic [ref=e323]: A022
            - button "Select A023 in viewport" [pressed] [ref=e324] [cursor=pointer]:
              - img [ref=e325]
              - generic [ref=e328]: A023
            - button "Select A024 in viewport" [pressed] [ref=e329] [cursor=pointer]:
              - img [ref=e330]
              - generic [ref=e333]: A024
            - button "Select A025 in viewport" [pressed] [ref=e334] [cursor=pointer]:
              - img [ref=e335]
              - generic [ref=e338]: A025
            - button "Select A026 in viewport" [pressed] [ref=e339] [cursor=pointer]:
              - img [ref=e340]
              - generic [ref=e343]: A026
            - button "Select A027 in viewport" [pressed] [ref=e344] [cursor=pointer]:
              - img [ref=e345]
              - generic [ref=e348]: A027
            - button "Select A028 in viewport" [pressed] [ref=e349] [cursor=pointer]:
              - img [ref=e350]
              - generic [ref=e353]: A028
            - button "Select A029 in viewport" [pressed] [ref=e354] [cursor=pointer]:
              - img [ref=e355]
              - generic [ref=e358]: A029
            - button "Select A035 in viewport" [pressed] [ref=e359] [cursor=pointer]:
              - img [ref=e360]
              - generic [ref=e363]: A035
            - button "Select A036 in viewport" [pressed] [ref=e364] [cursor=pointer]:
              - img [ref=e365]
              - generic [ref=e368]: A036
            - button "Select A037 in viewport" [pressed] [ref=e369] [cursor=pointer]:
              - img [ref=e370]
              - generic [ref=e373]: A037
            - button "Select A038 in viewport" [pressed] [ref=e374] [cursor=pointer]:
              - img [ref=e375]
              - generic [ref=e378]: A038
            - button "Select A039 in viewport" [pressed] [ref=e379] [cursor=pointer]:
              - img [ref=e380]
              - generic [ref=e383]: A039
            - button "Select A040 in viewport" [pressed] [ref=e384] [cursor=pointer]:
              - img [ref=e385]
              - generic [ref=e388]: A040
            - button "Select A041 in viewport" [pressed] [ref=e389] [cursor=pointer]:
              - img [ref=e390]
              - generic [ref=e393]: A041
            - button "Select A042 in viewport" [pressed] [ref=e394] [cursor=pointer]:
              - img [ref=e395]
              - generic [ref=e398]: A042
            - button "Select A043 in viewport" [pressed] [ref=e399] [cursor=pointer]:
              - img [ref=e400]
              - generic [ref=e403]: A043
            - button "Select A044 in viewport" [pressed] [ref=e404] [cursor=pointer]:
              - img [ref=e405]
              - generic [ref=e408]: A044
            - button "Select A045 in viewport" [pressed] [ref=e409] [cursor=pointer]:
              - img [ref=e410]
              - generic [ref=e413]: A045
            - button "Select A046 in viewport" [pressed] [ref=e414] [cursor=pointer]:
              - img [ref=e415]
              - generic [ref=e418]: A046
            - button "Select A052 in viewport" [pressed] [ref=e419] [cursor=pointer]:
              - img [ref=e420]
              - generic [ref=e423]: A052
            - button "Select A053 in viewport" [pressed] [ref=e424] [cursor=pointer]:
              - img [ref=e425]
              - generic [ref=e428]: A053
            - button "Select A054 in viewport" [pressed] [ref=e429] [cursor=pointer]:
              - img [ref=e430]
              - generic [ref=e433]: A054
            - button "Select A055 in viewport" [pressed] [ref=e434] [cursor=pointer]:
              - img [ref=e435]
              - generic [ref=e438]: A055
            - button "Select A056 in viewport" [pressed] [ref=e439] [cursor=pointer]:
              - img [ref=e440]
              - generic [ref=e443]: A056
            - button "Select A057 in viewport" [pressed] [ref=e444] [cursor=pointer]:
              - img [ref=e445]
              - generic [ref=e448]: A057
            - button "Select A058 in viewport" [pressed] [ref=e449] [cursor=pointer]:
              - img [ref=e450]
              - generic [ref=e453]: A058
            - button "Select A059 in viewport" [pressed] [ref=e454] [cursor=pointer]:
              - img [ref=e455]
              - generic [ref=e458]: A059
            - button "Select A060 in viewport" [pressed] [ref=e459] [cursor=pointer]:
              - img [ref=e460]
              - generic [ref=e463]: A060
            - button "Select A061 in viewport" [pressed] [ref=e464] [cursor=pointer]:
              - img [ref=e465]
              - generic [ref=e468]: A061
            - button "Select A062 in viewport" [pressed] [ref=e469] [cursor=pointer]:
              - img [ref=e470]
              - generic [ref=e473]: A062
            - button "Select A069 in viewport" [pressed] [ref=e474] [cursor=pointer]:
              - img [ref=e475]
              - generic [ref=e478]: A069
            - button "Select A070 in viewport" [pressed] [ref=e479] [cursor=pointer]:
              - img [ref=e480]
              - generic [ref=e483]: A070
            - button "Select A071 in viewport" [pressed] [ref=e484] [cursor=pointer]:
              - img [ref=e485]
              - generic [ref=e488]: A071
            - button "Select A072 in viewport" [pressed] [ref=e489] [cursor=pointer]:
              - img [ref=e490]
              - generic [ref=e493]: A072
            - button "Select A073 in viewport" [pressed] [ref=e494] [cursor=pointer]:
              - img [ref=e495]
              - generic [ref=e498]: A073
            - button "Select A074 in viewport" [pressed] [ref=e499] [cursor=pointer]:
              - img [ref=e500]
              - generic [ref=e503]: A074
            - button "Select A075 in viewport" [pressed] [ref=e504] [cursor=pointer]:
              - img [ref=e505]
              - generic [ref=e508]: A075
            - button "Select A076 in viewport" [pressed] [ref=e509] [cursor=pointer]:
              - img [ref=e510]
              - generic [ref=e513]: A076
            - button "Select A077 in viewport" [pressed] [ref=e514] [cursor=pointer]:
              - img [ref=e515]
              - generic [ref=e518]: A077
            - button "Select A079 in viewport" [pressed] [ref=e519] [cursor=pointer]:
              - img [ref=e520]
              - generic [ref=e523]: A079
            - button "Select A086 in viewport" [pressed] [ref=e524] [cursor=pointer]:
              - img [ref=e525]
              - generic [ref=e528]: A086
            - button "Select A087 in viewport" [pressed] [ref=e529] [cursor=pointer]:
              - img [ref=e530]
              - generic [ref=e533]: A087
            - button "Select A088 in viewport" [pressed] [ref=e534] [cursor=pointer]:
              - img [ref=e535]
              - generic [ref=e538]: A088
            - button "Select A089 in viewport" [pressed] [ref=e539] [cursor=pointer]:
              - img [ref=e540]
              - generic [ref=e543]: A089
            - button "Select A090 in viewport" [pressed] [ref=e544] [cursor=pointer]:
              - img [ref=e545]
              - generic [ref=e548]: A090
            - button "Select A091 in viewport" [pressed] [ref=e549] [cursor=pointer]:
              - img [ref=e550]
              - generic [ref=e553]: A091
            - button "Select A092 in viewport" [pressed] [ref=e554] [cursor=pointer]:
              - img [ref=e555]
              - generic [ref=e558]: A092
            - button "Select A093 in viewport" [pressed] [ref=e559] [cursor=pointer]:
              - img [ref=e560]
              - generic [ref=e563]: A093
            - button "Select A094 in viewport" [pressed] [ref=e564] [cursor=pointer]:
              - img [ref=e565]
              - generic [ref=e568]: A094
            - button "Select A096 in viewport" [pressed] [ref=e569] [cursor=pointer]:
              - img [ref=e570]
              - generic [ref=e573]: A096
            - button "Select A103 in viewport" [pressed] [ref=e574] [cursor=pointer]:
              - img [ref=e575]
              - generic [ref=e578]: A103
            - button "Select A104 in viewport" [pressed] [ref=e579] [cursor=pointer]:
              - img [ref=e580]
              - generic [ref=e583]: A104
            - button "Select A105 in viewport" [pressed] [ref=e584] [cursor=pointer]:
              - img [ref=e585]
              - generic [ref=e588]: A105
            - button "Select A106 in viewport" [pressed] [ref=e589] [cursor=pointer]:
              - img [ref=e590]
              - generic [ref=e593]: A106
            - button "Select A107 in viewport" [pressed] [ref=e594] [cursor=pointer]:
              - img [ref=e595]
              - generic [ref=e598]: A107
            - button "Select A109 in viewport" [pressed] [ref=e599] [cursor=pointer]:
              - img [ref=e600]
              - generic [ref=e603]: A109
            - button "Select A111 in viewport" [pressed] [ref=e604] [cursor=pointer]:
              - img [ref=e605]
              - generic [ref=e608]: A111
            - button "Select A113 in viewport" [pressed] [ref=e609] [cursor=pointer]:
              - img [ref=e610]
              - generic [ref=e613]: A113
            - button "Select A120 in viewport" [pressed] [ref=e614] [cursor=pointer]:
              - img [ref=e615]
              - generic [ref=e618]: A120
            - button "Select A121 in viewport" [pressed] [ref=e619] [cursor=pointer]:
              - img [ref=e620]
              - generic [ref=e623]: A121
            - button "Select A122 in viewport" [pressed] [ref=e624] [cursor=pointer]:
              - img [ref=e625]
              - generic [ref=e628]: A122
            - button "Select A124 in viewport" [pressed] [ref=e629] [cursor=pointer]:
              - img [ref=e630]
              - generic [ref=e633]: A124
            - button "Select A126 in viewport" [pressed] [ref=e634] [cursor=pointer]:
              - img [ref=e635]
              - generic [ref=e638]: A126
            - button "Select A132 in viewport" [pressed] [ref=e639] [cursor=pointer]:
              - img [ref=e640]
              - generic [ref=e643]: A132
            - button "Select B006 in viewport" [pressed] [ref=e644] [cursor=pointer]:
              - img [ref=e645]
              - generic [ref=e648]: B006
            - button "Select B018 in viewport" [pressed] [ref=e649] [cursor=pointer]:
              - img [ref=e650]
              - generic [ref=e653]: B018
            - button "Select B020 in viewport" [pressed] [ref=e654] [cursor=pointer]:
              - img [ref=e655]
              - generic [ref=e658]: B020
            - button "Select B022 in viewport" [pressed] [ref=e659] [cursor=pointer]:
              - img [ref=e660]
              - generic [ref=e663]: B022
            - button "Select B035 in viewport" [pressed] [ref=e664] [cursor=pointer]:
              - img [ref=e665]
              - generic [ref=e668]: B035
            - button "Select B037 in viewport" [pressed] [ref=e669] [cursor=pointer]:
              - img [ref=e670]
              - generic [ref=e673]: B037
            - button "Select B039 in viewport" [pressed] [ref=e674] [cursor=pointer]:
              - img [ref=e675]
              - generic [ref=e678]: B039
            - button "Select B136 in viewport" [pressed] [ref=e679] [cursor=pointer]:
              - img [ref=e680]
              - generic [ref=e683]: B136
          - img "Orientation gizmo showing X, Y, Z axes"
          - generic "View controls" [ref=e684]:
            - button "Front" [pressed] [ref=e685] [cursor=pointer]
            - button "Top" [ref=e686] [cursor=pointer]
            - button "Isometric" [ref=e687] [cursor=pointer]
          - generic:
            - generic: 1 m
        - region "Command and selection bar" [ref=e688]:
          - generic "Object creation tools" [ref=e689]:
            - button "Node" [ref=e690] [cursor=pointer]:
              - img [ref=e691]
              - text: Node
            - button "Pipe" [ref=e693] [cursor=pointer]:
              - img [ref=e694]
              - text: Pipe
            - button "Support" [ref=e698] [cursor=pointer]:
              - img [ref=e699]
              - text: Support
            - button "Component" [ref=e702] [cursor=pointer]:
              - img [ref=e703]
              - text: Component
            - button "Load" [ref=e706] [cursor=pointer]:
              - img [ref=e707]
              - text: Load
          - generic "Model focus" [ref=e709]: Select
          - group [ref=e710]:
            - generic "Selection & navigation" [ref=e711] [cursor=pointer]
      - text: ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾
    - complementary "Agent" [ref=e712]:
      - button "Agent" [disabled] [ref=e714]:
        - img [ref=e715]
        - generic [ref=e718]: Agent
  - generic "Workspace status" [ref=e719]:
    - generic "Analysis statuses"
    - button "3 Issues" [ref=e720] [cursor=pointer]:
      - img [ref=e721]
      - text: 3 Issues
    - generic "Selection" [ref=e723]: "node: B136 · 272 selected"
    - generic "Display units" [ref=e724]: Entered
    - button "About SWBPIPE…" [ref=e725] [cursor=pointer]:
      - img [ref=e726]
```

# Test source

```ts
  120 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Budget");
  121 |     await selectTreeEntity(page, "node", "A"); await mode(page, "Off");
  122 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  123 |     await page.getByTestId("viewport-select-A").hover();
  124 |     const off = await witness(page, info, "off-context-deduplicated-primary-hover"); expect(off.labels.ordinaryCount).toBe(0);
  125 |     expect(off.labels.contextCount).toBe(1); await page.mouse.move(0, 0);
  126 |     await page.getByRole("button", { name: "Isolate", exact: true }).click();
  127 |     await mode(page, "All");
  128 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("data-dimmed", "true");
  129 |     const ordinary = page.locator('.viewport-select-target[data-label-placed="true"][aria-pressed="false"]').first();
  130 |     const box = await ordinary.boundingBox(); await ordinary.hover();
  131 |     for (let i = 0; i < 3; i++) { await settle(page); expect(await ordinary.boundingBox()).toEqual(box); }
  132 |     await page.mouse.move(0, 0); await witness(page, info, "all-hover-stable");
  133 |     await page.getByRole("button", { name: "Hide", exact: true }).click();
  134 |     for (const m of ["Budget", "All", "Off"] as const) { await mode(page, m); await expect(page.getByTestId("viewport-select-A")).toHaveCount(0); }
  135 |     await expect(page.getByTestId("viewport-hidden-count")).toHaveText("1 hidden · Show all");
  136 |     await page.getByRole("button", { name: "Show All", exact: true }).click();
  137 |     await mode(page, "All"); await page.setViewportSize({ width: 1100, height: 850 });
  138 |     await page.getByTestId("viewport-fit-model").click(); await witness(page, info, "resized-front");
  139 |     for (const node of (await fixture()).nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  140 |     await page.getByRole("button", { name: "Top", exact: true }).click(); await witness(page, info, "camera-top");
  141 |     await page.getByTestId("viewport-canvas").focus(); await page.keyboard.press("l");
  142 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Off");
  143 |     expect(await invariants(page)).toEqual(before);
  144 |   });
  145 |   test("C4 current review row B remains distinct from primary A @explicit-viewport", async ({ page }, info) => {
  146 |     await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
  147 |     const before = await invariants(page); await mode(page, "Off");
  148 |     await showModelTree(page);
  149 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("layout-mode-grid").click();
  150 |     await page.getByTestId("table-cell-A-x").click();
  151 |     const deduplicatedRow = await witness(page, info, "primary-A-current-fields-row-A-deduplicated");
  152 |     expect(deduplicatedRow.labels.mode).toBe("Off");
  153 |     expect(deduplicatedRow.labels.contextCount).toBe(1);
  154 |     expect(deduplicatedRow.boxes.map(box => box.key)).toEqual([JSON.stringify(["node", "A"])]);
  155 |     await page.getByTestId("node-grid-review-disclosure").click();
  156 |     await page.getByTestId("review-cell-B-x").click();
  157 |     const current = await witness(page, info, "primary-A-review-B");
  158 |     expect(current.selection.primaryRef).toEqual({ type: "node", id: "A" });
  159 |     expect(current.selection.orderedRefs).toEqual([{ type: "node", id: "A" }]);
  160 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("aria-pressed", "false");
  161 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await expect(page.getByTestId("viewport-select-B")).toBeVisible();
  162 |     expect(current.labels.contextCount).toBe(2); expect(current.labels.ordinaryCount).toBe(0);
  163 |     await page.getByTestId("node-grid-review-disclosure").click();
  164 |     await expect(page.getByTestId("viewport-select-B")).toBeHidden();
  165 |     expect(await invariants(page)).toEqual(before);
  166 |   });
  167 |   for (const coincident of [false, true]) {
  168 |   test(coincident
  169 |     ? "C4 synthetic coincident real identities produce actual placed context overflow @explicit-viewport"
  170 |     : "C4 unique full node inventory preserves spatial omissions @explicit-viewport", async ({ page }, info) => {
  171 |     await page.setViewportSize({ width: 1440, height: 920 }); const model = await fixture(true, coincident);
  172 |     await info.attach("dense-functional-fixture", { body: JSON.stringify({
  173 |       purpose: coincident ? "Two distinct real node populations intentionally share coordinates; synthetic UI test, not engineering acceptance" : "Unique-position full inventory and finite spatial omissions",
  174 |       model }, null, 2), contentType: "application/json" });
  175 |     await load(page, model);
  176 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("viewport-fit-model").click();
  177 |     const before = await invariants(page); await mode(page, "Off");
  178 |     await page.getByTestId("viewport-selection-filter").selectOption("nodes"); await page.getByTestId("viewport-box-select").click();
  179 |     const points = [];
  180 |     for (const node of model.nodes) points.push(await projected(page, node.position));
  181 |     const preselection = await page.evaluate(() => {
  182 |       const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
  183 |       if ("status" in snapshot.viewport) throw new Error("Viewport unavailable");
  184 |       const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!.getBoundingClientRect();
  185 |       return { camera: snapshot.viewport.camera, canvas: canvas.toJSON(),
  186 |         measuredBudget: Math.floor(canvas.width * canvas.height / 3600), labels: snapshot.viewport.labels };
  187 |     });
  188 |     await info.attach("dense-projected-input-preselection", { body: JSON.stringify({
  189 |       ...preselection, nodes: model.nodes.map((node: any, i: number) => ({ id: node.id, authored: node.position, projected: points[i] }))
  190 |     }, null, 2), contentType: "application/json" });
  191 |     const left = Math.min(...points.map(p => p.x)) - 8, right = Math.max(...points.map(p => p.x)) + 8;
  192 |     const top = Math.min(...points.map(p => p.y)) - 8, bottom = Math.max(...points.map(p => p.y)) + 8;
  193 |     await page.mouse.move(left, top); await page.mouse.down(); await page.mouse.move(right, bottom, { steps: 6 }); await page.mouse.up();
  194 |     await page.getByTestId("viewport-box-select").click(); await mode(page, "Budget");
  195 |     const result = await witness(page, info, "dense-actual-placement");
  196 |     expect(result.selection.orderedRefs).toHaveLength(model.nodes.length);
  197 |     expect(await page.locator('.viewport-select-target[data-entity-key]').count()).toBe(model.nodes.length + model.pipe_segments.length);
  198 |     const expectedKeys = model.nodes.map((node: any) => JSON.stringify(["node", node.id])).sort();
  199 |     expect(new Set(expectedKeys).size).toBe(coincident ? 272 : 136);
  200 |     expect(result.selection.orderedRefs.map(ref => JSON.stringify([ref.type, ref.id])).sort()).toEqual(expectedKeys);
  201 |     const placedContextKeys = result.boxes.filter(box => expectedKeys.includes(box.key!)).map(box => box.key!);
  202 |     const unplacedContext = (result.labels.unplaced ?? []).filter(item => item.role !== "ordinary");
  203 |     expect(placedContextKeys.length).toBe(result.labels.contextCount);
  204 |     expect([...placedContextKeys, ...unplacedContext.map(item => item.key)].sort()).toEqual(expectedKeys);
  205 |     expect((result.labels.suppressed ?? []).filter(item => item.role !== "ordinary")).toEqual([]);
  206 |     expect((result.labels.ineligible ?? []).filter(item => item.role !== "ordinary")).toEqual([]);
  207 |     for (const box of result.boxes) {
  208 |       expect(model.nodes.some((node: any) => JSON.stringify(["node", node.id]) === box.key) ||
  209 |         model.pipe_segments.some((pipe: any) => JSON.stringify(["pipe", pipe.id]) === box.key)).toBe(true);
  210 |     }
  211 |     if (coincident) {
  212 |       const readableIdentities = [];
  213 |       for (const box of result.boxes) {
  214 |         const [type, id] = JSON.parse(box.key!);
  215 |         if (type !== "node") continue;
  216 |         const span = page.getByTestId(`viewport-select-${id}`).locator("span");
  217 |         await expect(span).toHaveText(id);
  218 |         const dimensions = await span.evaluate(element => ({ text: element.textContent,
  219 |           scrollWidth: element.scrollWidth, clientWidth: element.clientWidth }));
> 220 |         expect(dimensions.scrollWidth, `${id} fits its unchanged visible label span`).toBeLessThanOrEqual(dimensions.clientWidth);
      |                                                                                       ^ Error: A001 fits its unchanged visible label span
  221 |         readableIdentities.push({ key: box.key, ...dimensions });
  222 |       }
  223 |       await info.attach("dense-readable-real-identities", { body: JSON.stringify(readableIdentities, null, 2), contentType: "application/json" });
  224 |       // Rendered overflow is the gate; 272 requested identities alone prove nothing.
  225 |       expect(result.labels.contextCount).toBeGreaterThan(result.labels.budget);
  226 |       expect(result.labels.contextOverflow).toBe(result.labels.contextCount! - result.labels.budget);
  227 |       expect(result.labels.ordinaryCount).toBe(0);
  228 |       expect(result.labels.suppressed?.some(item => item.role === "ordinary" && item.reason === "budget")).toBe(true);
  229 |     } else {
  230 |       expect(unplacedContext.length).toBeGreaterThan(0);
  231 |       expect(result.labels.contextOverflow).toBe(Math.max(0, result.labels.contextCount! - result.labels.budget));
  232 |     }
  233 |     for (const node of model.nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  234 |     expect(await invariants(page)).toEqual(before);
  235 |   });
  236 |   }
  237 |   test("C4 label modes preserve Current and Historical result standing", async ({ page }) => {
  238 |     await page.goto("/"); await openWorkspaceSection(page, "solve");
  239 |     await page.getByTestId("run-mechanics-preview").click();
  240 |     await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
  241 |     await showCanvas(page); const current = await invariants(page);
  242 |     for (const m of ["Off", "All", "Budget"] as const) await mode(page, m);
  243 |     expect(await invariants(page)).toEqual(current);
  244 |     await projectCommand(page, "save-local");
  245 |     await expect(page.getByTestId("local-project-message")).toContainText("Saved");
  246 |     await projectCommand(page, "open-local"); await openWorkspaceSection(page, "results");
  247 |     await expect(page.getByTestId("historical-run-context")).toBeVisible();
  248 |     const historical = await invariants(page);
  249 |     for (const m of ["All", "Off", "Budget"] as const) await mode(page, m);
  250 |     expect(await invariants(page)).toEqual(historical);
  251 |   });
  252 |   test("C4 real WebGL loss/restoration fails closed and recovers", async ({ page }, info) => {
  253 |     await load(page, await fixture()); await selectTreeEntity(page, "node", "A");
  254 |     const before = await invariants(page); await mode(page, "Off");
  255 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  256 |     const supported = await page.evaluate(() => {
  257 |       const canvas = document.querySelector<HTMLCanvasElement>('[data-testid="viewport-canvas"] canvas')!;
  258 |       const gl = canvas.getContext("webgl2") ?? canvas.getContext("webgl");
  259 |       const extension = gl?.getExtension("WEBGL_lose_context");
  260 |       if (!extension) return false;
  261 |       (window as any).__c4ContextExtension = extension; extension.loseContext(); return true;
  262 |     });
  263 |     await info.attach("webgl-extension-availability", { body: JSON.stringify({ supported }), contentType: "application/json" });
  264 |     test.skip(!supported, "Real WEBGL_lose_context extension unavailable; loss/restoration remains unwitnessed");
  265 |     await expect(page.getByTestId("viewport-context-status")).toContainText("lost");
  266 |     const lostLabels = await labels(page);
  267 |     await info.attach("webgl-lost-label-diagnostics", { body: JSON.stringify(lostLabels, null, 2), contentType: "application/json" });
  268 |     expect(lostLabels.placementStatus).toBe("unavailable");
  269 |     expect(lostLabels.renderedCount).toBe(0);
  270 |     await expect(page.locator('.viewport-select-target[data-label-placed="true"]')).toHaveCount(0);
  271 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("tabindex", "-1");
  272 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("aria-hidden", "true");
  273 |     await page.evaluate(() => { (window as any).__c4ContextExtension.restoreContext(); delete (window as any).__c4ContextExtension; });
  274 |     await expect(page.getByTestId("viewport-context-status")).toHaveCount(0);
  275 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await witness(page, info, "restored");
  276 |     expect(await invariants(page)).toEqual(before);
  277 |   });
  278 | }
  279 | 
```