# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: c4-label-policy.spec.ts >> C4 full node inventory and actual placed context overflow @explicit-viewport
- Location: e2e/c4-label-policy.scenarios.ts:153:3

# Error details

```
Error: expect(received).toBeGreaterThan(expected)

Expected: > 113
Received:   15
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
            - 'generic "Selected node: n143" [ref=e226]': "Selected: n143"
            - group [ref=e227]:
              - generic "130 annotations omitted" [active] [ref=e228]
            - status "Schematic centerline geometry" [ref=e229]
            - status "View command status" [ref=e230]: Box Select disabled.
        - generic [ref=e231]:
          - generic "Three.js pipe centerline viewport" [ref=e232]
          - generic "Viewport entity selection":
            - button "Select n0 in viewport" [pressed] [ref=e234] [cursor=pointer]:
              - img [ref=e235]
              - generic [ref=e238]: n0
            - button "Select n2 in viewport" [pressed] [ref=e239] [cursor=pointer]:
              - img [ref=e240]
              - generic [ref=e243]: n2
            - button "Select n3 in viewport" [pressed] [ref=e244] [cursor=pointer]:
              - img [ref=e245]
              - generic [ref=e248]: n3
            - button "Select n4 in viewport" [pressed] [ref=e249] [cursor=pointer]:
              - img [ref=e250]
              - generic [ref=e253]: n4
            - button "Select n6 in viewport" [pressed] [ref=e254] [cursor=pointer]:
              - img [ref=e255]
              - generic [ref=e258]: n6
            - button "Select n8 in viewport" [pressed] [ref=e259] [cursor=pointer]:
              - img [ref=e260]
              - generic [ref=e263]: n8
            - button "Select n15 in viewport" [pressed] [ref=e264] [cursor=pointer]:
              - img [ref=e265]
              - generic [ref=e268]: n15
            - button "Select n20 in viewport" [pressed] [ref=e269] [cursor=pointer]:
              - img [ref=e270]
              - generic [ref=e273]: n20
            - button "Select n120 in viewport" [pressed] [ref=e274] [cursor=pointer]:
              - img [ref=e275]
              - generic [ref=e278]: n120
            - button "Select n121 in viewport" [pressed] [ref=e279] [cursor=pointer]:
              - img [ref=e280]
              - generic [ref=e283]: n121
            - button "Select n122 in viewport" [pressed] [ref=e284] [cursor=pointer]:
              - img [ref=e285]
              - generic [ref=e288]: n122
            - button "Select n123 in viewport" [pressed] [ref=e289] [cursor=pointer]:
              - img [ref=e290]
              - generic [ref=e293]: n123
            - button "Select n127 in viewport" [pressed] [ref=e294] [cursor=pointer]:
              - img [ref=e295]
              - generic [ref=e298]: n127
            - button "Select n131 in viewport" [pressed] [ref=e299] [cursor=pointer]:
              - img [ref=e300]
              - generic [ref=e303]: n131
            - button "Select n143 in viewport" [pressed] [ref=e304] [cursor=pointer]:
              - img [ref=e305]
              - generic [ref=e308]: n143
          - img "Orientation gizmo showing X, Y, Z axes"
          - generic "View controls" [ref=e309]:
            - button "Front" [pressed] [ref=e310] [cursor=pointer]
            - button "Top" [ref=e311] [cursor=pointer]
            - button "Isometric" [ref=e312] [cursor=pointer]
          - generic:
            - generic: 1 m
        - region "Command and selection bar" [ref=e313]:
          - generic "Object creation tools" [ref=e314]:
            - button "Node" [ref=e315] [cursor=pointer]:
              - img [ref=e316]
              - text: Node
            - button "Pipe" [ref=e318] [cursor=pointer]:
              - img [ref=e319]
              - text: Pipe
            - button "Support" [ref=e323] [cursor=pointer]:
              - img [ref=e324]
              - text: Support
            - button "Component" [ref=e327] [cursor=pointer]:
              - img [ref=e328]
              - text: Component
            - button "Load" [ref=e331] [cursor=pointer]:
              - img [ref=e332]
              - text: Load
          - generic "Model focus" [ref=e334]: Select
          - group [ref=e335]:
            - generic "Selection & navigation" [ref=e336] [cursor=pointer]
      - text: ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾
    - complementary "Agent" [ref=e337]:
      - button "Agent" [disabled] [ref=e339]:
        - img [ref=e340]
        - generic [ref=e343]: Agent
  - generic "Workspace status" [ref=e344]:
    - generic "Analysis statuses"
    - button "3 Issues" [ref=e345] [cursor=pointer]:
      - img [ref=e346]
      - text: 3 Issues
    - generic "Selection" [ref=e348]: "node: n143 · 144 selected"
    - generic "Display units" [ref=e349]: Entered
    - button "About SWBPIPE…" [ref=e350] [cursor=pointer]:
      - img [ref=e351]
```

# Test source

```ts
  68  |   const evidence = await page.evaluate(() => {
  69  |     const s = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
  70  |     if ("status" in s.viewport) throw new Error("Viewport unavailable");
  71  |     const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!.getBoundingClientRect();
  72  |     const boxes = [...document.querySelectorAll<HTMLElement>('.viewport-select-target[data-label-placed="true"]')].map(el => ({
  73  |       key: el.dataset.entityKey, rect: el.getBoundingClientRect().toJSON(), pressed: el.getAttribute("aria-pressed") }));
  74  |     return { labels: s.viewport.labels, selection: s.viewport.selection, canvas: canvas.toJSON(), boxes };
  75  |   });
  76  |   await info.attach(name, { body: JSON.stringify(evidence, null, 2), contentType: "application/json" });
  77  |   expect(evidence.labels.placementStatus).toBe("applied");
  78  |   expect(evidence.labels.renderedCount).toBe(evidence.boxes.length);
  79  |   expect(evidence.labels.budget).toBe(Math.floor(evidence.canvas.width * evidence.canvas.height / 3600));
  80  |   expect(new Set(evidence.boxes.map(b => b.key)).size).toBe(evidence.boxes.length);
  81  |   for (const [i, { rect: a }] of evidence.boxes.entries()) {
  82  |     expect(a.left).toBeGreaterThanOrEqual(evidence.canvas.left); expect(a.right).toBeLessThanOrEqual(evidence.canvas.right);
  83  |     expect(a.top).toBeGreaterThanOrEqual(evidence.canvas.top); expect(a.bottom).toBeLessThanOrEqual(evidence.canvas.bottom);
  84  |     for (const { rect: b } of evidence.boxes.slice(i + 1)) expect(a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top).toBe(false);
  85  |   }
  86  |   const omissions = page.getByTestId("viewport-label-omissions");
  87  |   await omissions.locator("summary").click();
  88  |   const omitted = [...(evidence.labels.suppressed ?? []), ...(evidence.labels.unplaced ?? [])];
  89  |   await expect(omissions.locator("li")).toHaveCount(omitted.length);
  90  |   for (const item of omitted) await expect(omissions).toContainText(item.key);
  91  |   await omissions.locator("summary").click();
  92  |   return evidence;
  93  | }
  94  | async function projected(page: Page, position: { x: number; y: number; z: number }) {
  95  |   await settle(page);
  96  |   return page.evaluate(position => {
  97  |     const api = globalThis.__openPipeStressUiDiagnosticsV1, s = api.readCurrent();
  98  |     if ("status" in s.viewport || s.model.generation === null) throw new Error("Viewport unavailable");
  99  |     const p = api.projectAuthoredPoint({ modelGeneration: s.model.generation, cameraSequence: s.viewport.camera.sequence, authoredPoint: position });
  100 |     if (p.status !== "available" || !p.insideCanvasCss) throw new Error("Required real geometry pick outside canvas");
  101 |     const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!, b = canvas.getBoundingClientRect();
  102 |     const x = b.left + p.canvasCssPoint.x, y = b.top + p.canvasCssPoint.y;
  103 |     return { x, y, unobscured: document.elementFromPoint(x, y) === canvas };
  104 |   }, position);
  105 | }
  106 | export function registerC4LabelScenarios() {
  107 |   test("C4 modes, dedup, Hide/Isolate, hover, camera, resize and nonmutation @explicit-viewport", async ({ page }, info) => {
  108 |     await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
  109 |     const before = await invariants(page);
  110 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Budget");
  111 |     await selectTreeEntity(page, "node", "A"); await mode(page, "Off");
  112 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  113 |     await page.getByTestId("viewport-select-A").hover();
  114 |     const off = await witness(page, info, "off-context-deduplicated-primary-hover-row"); expect(off.labels.ordinaryCount).toBe(0);
  115 |     expect(off.labels.contextCount).toBe(1); await page.mouse.move(0, 0);
  116 |     await page.getByRole("button", { name: "Isolate", exact: true }).click();
  117 |     await mode(page, "All");
  118 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("data-dimmed", "true");
  119 |     const ordinary = page.locator('.viewport-select-target[data-label-placed="true"][aria-pressed="false"]').first();
  120 |     const box = await ordinary.boundingBox(); await ordinary.hover();
  121 |     for (let i = 0; i < 3; i++) { await settle(page); expect(await ordinary.boundingBox()).toEqual(box); }
  122 |     await page.mouse.move(0, 0); await witness(page, info, "all-hover-stable");
  123 |     await page.getByRole("button", { name: "Hide", exact: true }).click();
  124 |     for (const m of ["Budget", "All", "Off"] as const) { await mode(page, m); await expect(page.getByTestId("viewport-select-A")).toHaveCount(0); }
  125 |     await expect(page.getByTestId("viewport-hidden-count")).toHaveText("1 hidden · Show all");
  126 |     await page.getByRole("button", { name: "Show All", exact: true }).click();
  127 |     await mode(page, "All"); await page.setViewportSize({ width: 1100, height: 850 });
  128 |     await page.getByTestId("viewport-fit-model").click(); await witness(page, info, "resized-front");
  129 |     for (const node of (await fixture()).nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  130 |     await page.getByRole("button", { name: "Top", exact: true }).click(); await witness(page, info, "camera-top");
  131 |     await page.getByTestId("viewport-canvas").focus(); await page.keyboard.press("l");
  132 |     await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Off");
  133 |     expect(await invariants(page)).toEqual(before);
  134 |   });
  135 |   test("C4 current review row B remains distinct from primary A @explicit-viewport", async ({ page }, info) => {
  136 |     await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
  137 |     const before = await invariants(page); await mode(page, "Off");
  138 |     await showModelTree(page);
  139 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("layout-mode-grid").click();
  140 |     await page.getByTestId("table-cell-A-x").click();
  141 |     await page.getByTestId("node-grid-review-disclosure").click();
  142 |     await page.getByTestId("review-cell-B-x").click();
  143 |     const current = await witness(page, info, "primary-A-review-B");
  144 |     expect(current.selection.primaryRef).toEqual({ type: "node", id: "A" });
  145 |     expect(current.selection.orderedRefs).toEqual([{ type: "node", id: "A" }]);
  146 |     await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("aria-pressed", "false");
  147 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await expect(page.getByTestId("viewport-select-B")).toBeVisible();
  148 |     expect(current.labels.contextCount).toBe(2); expect(current.labels.ordinaryCount).toBe(0);
  149 |     await page.getByTestId("node-grid-review-disclosure").click();
  150 |     await expect(page.getByTestId("viewport-select-B")).toBeHidden();
  151 |     expect(await invariants(page)).toEqual(before);
  152 |   });
  153 |   test("C4 full node inventory and actual placed context overflow @explicit-viewport", async ({ page }, info) => {
  154 |     await page.setViewportSize({ width: 1440, height: 920 }); const model = await fixture(true); await load(page, model);
  155 |     await page.getByTestId("view-switch-both").click(); await page.getByTestId("viewport-fit-model").click();
  156 |     const before = await invariants(page); await mode(page, "Off");
  157 |     await page.getByTestId("viewport-selection-filter").selectOption("nodes"); await page.getByTestId("viewport-box-select").click();
  158 |     const points = [];
  159 |     for (const node of model.nodes) points.push(await projected(page, node.position));
  160 |     const left = Math.min(...points.map(p => p.x)) - 8, right = Math.max(...points.map(p => p.x)) + 8;
  161 |     const top = Math.min(...points.map(p => p.y)) - 8, bottom = Math.max(...points.map(p => p.y)) + 8;
  162 |     await page.mouse.move(left, top); await page.mouse.down(); await page.mouse.move(right, bottom, { steps: 6 }); await page.mouse.up();
  163 |     await page.getByTestId("viewport-box-select").click(); await mode(page, "Budget");
  164 |     const result = await witness(page, info, "dense-actual-placement");
  165 |     expect(result.selection.orderedRefs).toHaveLength(model.nodes.length);
  166 |     expect(await page.locator('.viewport-select-target[data-entity-key]').count()).toBe(model.nodes.length + model.pipe_segments.length);
  167 |     // This is deliberately a rendered-overflow assertion, never just requested > budget.
> 168 |     expect(result.labels.contextCount).toBeGreaterThan(result.labels.budget);
      |                                        ^ Error: expect(received).toBeGreaterThan(expected)
  169 |     expect(result.labels.contextOverflow).toBe(result.labels.contextCount! - result.labels.budget);
  170 |     expect(result.labels.ordinaryCount).toBe(0);
  171 |     expect(result.labels.suppressed?.some(item => item.role === "ordinary" && item.reason === "budget")).toBe(true);
  172 |     for (const node of model.nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
  173 |     expect(await invariants(page)).toEqual(before);
  174 |   });
  175 |   test("C4 label modes preserve Current and Historical result standing", async ({ page }) => {
  176 |     await page.goto("/"); await openWorkspaceSection(page, "solve");
  177 |     await page.getByTestId("run-mechanics-preview").click();
  178 |     await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
  179 |     await showCanvas(page); const current = await invariants(page);
  180 |     for (const m of ["Off", "All", "Budget"] as const) await mode(page, m);
  181 |     expect(await invariants(page)).toEqual(current);
  182 |     await projectCommand(page, "save-local");
  183 |     await expect(page.getByTestId("local-project-message")).toContainText("Saved");
  184 |     await projectCommand(page, "open-local"); await openWorkspaceSection(page, "results");
  185 |     await expect(page.getByTestId("historical-run-context")).toBeVisible();
  186 |     const historical = await invariants(page);
  187 |     for (const m of ["All", "Off", "Budget"] as const) await mode(page, m);
  188 |     expect(await invariants(page)).toEqual(historical);
  189 |   });
  190 |   test("C4 real WebGL loss/restoration fails closed and recovers", async ({ page }, info) => {
  191 |     await load(page, await fixture()); await selectTreeEntity(page, "node", "A");
  192 |     const before = await invariants(page); await mode(page, "Off");
  193 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible();
  194 |     const supported = await page.evaluate(() => {
  195 |       const canvas = document.querySelector<HTMLCanvasElement>('[data-testid="viewport-canvas"] canvas')!;
  196 |       const gl = canvas.getContext("webgl2") ?? canvas.getContext("webgl");
  197 |       const extension = gl?.getExtension("WEBGL_lose_context");
  198 |       if (!extension) return false;
  199 |       (window as any).__c4ContextExtension = extension; extension.loseContext(); return true;
  200 |     });
  201 |     await info.attach("webgl-extension-availability", { body: JSON.stringify({ supported }), contentType: "application/json" });
  202 |     test.skip(!supported, "Real WEBGL_lose_context extension unavailable; loss/restoration remains unwitnessed");
  203 |     await expect(page.getByTestId("viewport-context-status")).toContainText("lost");
  204 |     const lostLabels = await labels(page);
  205 |     await info.attach("webgl-lost-label-diagnostics", { body: JSON.stringify(lostLabels, null, 2), contentType: "application/json" });
  206 |     expect(lostLabels.placementStatus).toBe("unavailable");
  207 |     expect(lostLabels.renderedCount).toBe(0);
  208 |     await expect(page.locator('.viewport-select-target[data-label-placed="true"]')).toHaveCount(0);
  209 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("tabindex", "-1");
  210 |     await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("aria-hidden", "true");
  211 |     await page.evaluate(() => { (window as any).__c4ContextExtension.restoreContext(); delete (window as any).__c4ContextExtension; });
  212 |     await expect(page.getByTestId("viewport-context-status")).toHaveCount(0);
  213 |     await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await witness(page, info, "restored");
  214 |     expect(await invariants(page)).toEqual(before);
  215 |   });
  216 | }
  217 | 
```