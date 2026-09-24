# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: c4-replacement-diagnostic.spec.ts >> captured Box lifetime >> same-ID Open retires old captured Box before delayed pointer up
- Location: e2e/c4-replacement-diagnostic.spec.ts:2162:1

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 0
Received: 1

Call Log:
- Timeout 10000ms exceeded while waiting on the predicate
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
      - paragraph [ref=e18]: Generated UI local-render-origin precision probe
    - group "Editing tools" [ref=e19]:
      - button "Undo model edit" [disabled] [ref=e20]:
        - img [ref=e21]
      - button "Redo model edit" [disabled] [ref=e24]:
        - img [ref=e25]
      - button "Select (⎋)" [pressed] [ref=e28] [cursor=pointer]:
        - img [ref=e29]
    - group "View" [ref=e31]:
      - button "Table" [ref=e33] [cursor=pointer]:
        - img [ref=e34]
        - generic [ref=e36]: Table
      - button "Model" [ref=e38] [cursor=pointer]:
        - img [ref=e39]
        - generic [ref=e42]: Model
      - button "Both" [pressed] [ref=e44] [cursor=pointer]:
        - img [ref=e45]
        - generic [ref=e47]: Both
    - generic [ref=e48]:
      - button "Run" [ref=e49] [cursor=pointer]:
        - img [ref=e50]
        - generic [ref=e52]: Run
      - button "Issues, 2" [ref=e53] [cursor=pointer]:
        - img [ref=e54]
        - generic [ref=e56]: Issues
        - generic [ref=e57]: "2"
    - group "Panels" [ref=e58]:
      - button "Inspector" [ref=e60] [cursor=pointer]:
        - img [ref=e61]
      - button "Agent" [disabled] [ref=e64]:
        - img [ref=e65]
    - generic "Display units" [ref=e68]:
      - combobox "Display units" [ref=e69]:
        - option "Entered" [selected]
        - option "SI"
        - option "US"
    - group [ref=e70]:
      - generic "Appearance" [ref=e71] [cursor=pointer]:
        - img [ref=e72]
      - option "System" [selected]
      - option "Light"
      - option "Dark"
      - option "Comfortable" [selected]
      - option "Compact"
    - region "Human toolkit" [ref=e74]:
      - button "Find modeling commands" [ref=e75] [cursor=pointer]:
        - img [ref=e76]
        - generic [ref=e79]: Search or command…
        - generic "Command K" [ref=e80]: ⌘K
  - generic [ref=e81]:
    - navigation "Stages" [ref=e82]:
      - list [ref=e83]:
        - listitem [ref=e84]:
          - button "Model" [pressed] [ref=e85] [cursor=pointer]:
            - img [ref=e86]
            - generic [ref=e89]: Model
        - listitem [ref=e90]:
          - button "Loads" [ref=e91] [cursor=pointer]:
            - img [ref=e92]
            - generic [ref=e96]: Loads
        - listitem [ref=e97]:
          - button "Results" [disabled] [ref=e98]:
            - img [ref=e99]
            - generic [ref=e102]: Results
        - listitem [ref=e103]:
          - button "Review" [disabled] [ref=e104]:
            - img [ref=e105]
            - generic [ref=e109]: Review
      - separator [ref=e110]
      - list [ref=e111]:
        - listitem [ref=e112]:
          - button "Libraries" [ref=e113] [cursor=pointer]:
            - img [ref=e114]
            - generic [ref=e116]: Libraries
        - listitem [ref=e117]:
          - button "Rules" [ref=e118] [cursor=pointer]:
            - img [ref=e119]
            - generic [ref=e123]: Rules
        - listitem [ref=e124]:
          - button "Issues, 2" [ref=e125] [cursor=pointer]:
            - img [ref=e126]
            - generic [ref=e128]: Issues
            - generic [ref=e129]: "2"
    - region "Modeling workspace" [ref=e131]:
      - generic [ref=e132]:
        - group "Tables" [ref=e133]:
          - button "Model" [pressed] [ref=e134] [cursor=pointer]
          - button "Review changes" [ref=e135] [cursor=pointer]
          - button "Collapse table drawer" [disabled] [expanded] [ref=e138]:
            - img [ref=e139]
        - generic "Model tree" [ref=e143]:
          - generic [ref=e144]: Model
          - generic [ref=e148]:
            - region "Layout grid mode" [ref=e149]:
              - button "Tree" [pressed] [ref=e150]:
                - img [ref=e151]
                - text: Tree
              - button "Grid" [ref=e154]:
                - img [ref=e155]
                - text: Grid
            - region "Model tree filtering" [ref=e157]:
              - generic [ref=e158]:
                - img [ref=e159]
                - generic [ref=e162]: Filter model
                - searchbox "Filter model tree" [ref=e163]: node:UIF-PRECISION-00010
              - generic [ref=e164]: 3 of 48 model entities visible
              - button "Clear model tree filter" [ref=e165] [cursor=pointer]:
                - img [ref=e166]
          - tree "Model" [ref=e169]:
            - generic [ref=e170]:
              - treeitem "Nodes" [expanded] [level=1] [ref=e172] [cursor=pointer]:
                - generic [ref=e173]: ▾
                - strong [ref=e174]: Nodes
              - treeitem "UI benchmark node 00010 node:UIF-PRECISION-00010" [level=2] [ref=e176] [cursor=pointer]:
                - img [ref=e177]
                - generic [ref=e180]:
                  - strong [ref=e181]: UI benchmark node 00010
                  - generic [ref=e182]: node:UIF-PRECISION-00010
              - treeitem "Pipes" [expanded] [level=1] [ref=e184] [cursor=pointer]:
                - generic [ref=e185]: ▾
                - strong [ref=e186]: Pipes
              - treeitem "UI benchmark pipe 00010 pipe:UIF-PRECISION-00010" [level=2] [ref=e188] [cursor=pointer]:
                - img [ref=e189]
                - generic [ref=e193]:
                  - strong [ref=e194]: UI benchmark pipe 00010
                  - generic [ref=e195]: pipe:UIF-PRECISION-00010
              - treeitem "UI benchmark pipe 00011 pipe:UIF-PRECISION-00011" [level=2] [ref=e197] [cursor=pointer]:
                - img [ref=e198]
                - generic [ref=e202]:
                  - strong [ref=e203]: UI benchmark pipe 00011
                  - generic [ref=e204]: pipe:UIF-PRECISION-00011
      - separator "Resize table and canvas" [ref=e205]
      - generic [ref=e207]:
        - generic [ref=e208]:
          - group "Viewport controls" [ref=e209]:
            - generic [ref=e210]: 3D Centerline
            - group "Viewport deformation overlay status" [ref=e211]:
              - generic "Deformation · unavailable" [ref=e212] [cursor=pointer]
            - group "Viewport display toggles" [ref=e213]:
              - 'button "Labels: Budget. Cycle Budget, All, Off" [ref=e214]': "Labels: Budget"
              - button "Loads" [pressed] [ref=e215]
              - button "Grid" [pressed] [ref=e216]
            - group "Viewport selection tools" [ref=e217]:
              - button "Box Select" [ref=e218]
              - generic [ref=e219]:
                - generic [ref=e220]: Selection filter
                - combobox "Selection filter" [ref=e221]:
                  - option "All"
                  - option "Pipes"
                  - option "Nodes"
                  - option "Supports"
                  - option "Components" [selected]
              - button "Hide" [disabled] [ref=e222]
              - button "Isolate" [disabled] [ref=e223]
              - button "Show All" [disabled] [ref=e224]
              - generic [ref=e225]: Isolate captures the selected geometry. Other shown geometry is dimmed to 20% and remains available to click, hover and box selection; nearer dimmed geometry can be picked before farther undimmed geometry. Selection does not change the snapshot. Hide takes precedence. Show All clears both. I and H apply while focus is in the viewport.
              - button "Fit Model" [ref=e226]
              - button "Fit Visible" [ref=e227]
              - button "Fit Selection" [disabled] [ref=e228]
            - group "Viewport geometry" [ref=e229]:
              - button "Schematic" [pressed] [ref=e230]
              - button "Actual OD" [ref=e231]
              - button "Measure" [ref=e232]
          - generic "Viewport status" [ref=e233]:
            - 'generic "Selected project: project:UIF-PRECISION-ORIGIN" [ref=e234]': "Selected: project:UIF-PRECISION-ORIGIN"
            - group [ref=e235]:
              - generic "20 annotations omitted" [ref=e236]
            - status "Schematic centerline geometry" [ref=e237]
            - status "View command status" [ref=e238]: Selection filter set to components.
        - generic [ref=e239]:
          - generic "Three.js pipe centerline viewport" [ref=e240]
          - generic "Viewport entity selection":
            - button "Select UI benchmark node 00002 in viewport" [ref=e242] [cursor=pointer]:
              - img [ref=e243]
              - generic [ref=e246]: UIF-PRECISION-00002
            - button "Select UI benchmark node 00004 in viewport" [ref=e247] [cursor=pointer]:
              - img [ref=e248]
              - generic [ref=e251]: UIF-PRECISION-00004
            - button "Select UI benchmark node 00008 in viewport" [ref=e252] [cursor=pointer]:
              - img [ref=e253]
              - generic [ref=e256]: UIF-PRECISION-00008
            - button "Select UI benchmark node 00009 in viewport" [ref=e257] [cursor=pointer]:
              - img [ref=e258]
              - generic [ref=e261]: UIF-PRECISION-00009
            - button "Select UI benchmark node 00010 in viewport" [ref=e262] [cursor=pointer]:
              - img [ref=e263]
              - generic [ref=e266]: UIF-PRECISION-00010
            - button "Select UI benchmark node 00011 in viewport" [ref=e267] [cursor=pointer]:
              - img [ref=e268]
              - generic [ref=e271]: UIF-PRECISION-00011
            - button "Select UI benchmark node 00012 in viewport" [ref=e272] [cursor=pointer]:
              - img [ref=e273]
              - generic [ref=e276]: UIF-PRECISION-00012
            - button "Select UI benchmark node 00014 in viewport" [ref=e277] [cursor=pointer]:
              - img [ref=e278]
              - generic [ref=e281]: UIF-PRECISION-00014
            - button "Select UI benchmark node 00019 in viewport" [ref=e282] [cursor=pointer]:
              - img [ref=e283]
              - generic [ref=e286]: UIF-PRECISION-00019
            - button "Select UI benchmark pipe 00004 in viewport" [ref=e287] [cursor=pointer]:
              - img [ref=e288]
              - generic [ref=e292]: UIF-PRECISION-00004
            - button "Select UI benchmark pipe 00005 in viewport" [ref=e293] [cursor=pointer]:
              - img [ref=e294]
              - generic [ref=e298]: UIF-PRECISION-00005
            - button "Select UI benchmark pipe 00006 in viewport" [ref=e299] [cursor=pointer]:
              - img [ref=e300]
              - generic [ref=e304]: UIF-PRECISION-00006
            - button "Select UI benchmark pipe 00007 in viewport" [ref=e305] [cursor=pointer]:
              - img [ref=e306]
              - generic [ref=e310]: UIF-PRECISION-00007
            - button "Select UI benchmark pipe 00008 in viewport" [ref=e311] [cursor=pointer]:
              - img [ref=e312]
              - generic [ref=e316]: UIF-PRECISION-00008
            - button "Select UI benchmark pipe 00009 in viewport" [ref=e317] [cursor=pointer]:
              - img [ref=e318]
              - generic [ref=e322]: UIF-PRECISION-00009
            - button "Select UI benchmark pipe 00010 in viewport" [ref=e323] [cursor=pointer]:
              - img [ref=e324]
              - generic [ref=e328]: UIF-PRECISION-00010
            - button "Select UI benchmark pipe 00011 in viewport" [ref=e329] [cursor=pointer]:
              - img [ref=e330]
              - generic [ref=e334]: UIF-PRECISION-00011
            - button "Select UI benchmark pipe 00012 in viewport" [ref=e335] [cursor=pointer]:
              - img [ref=e336]
              - generic [ref=e340]: UIF-PRECISION-00012
            - button "Select UI benchmark pipe 00013 in viewport" [ref=e341] [cursor=pointer]:
              - img [ref=e342]
              - generic [ref=e346]: UIF-PRECISION-00013
            - button "Select UI benchmark pipe 00016 in viewport" [ref=e347] [cursor=pointer]:
              - img [ref=e348]
              - generic [ref=e352]: UIF-PRECISION-00016
            - button "Select UI benchmark pipe 00020 in viewport" [ref=e353] [cursor=pointer]:
              - img [ref=e354]
              - generic [ref=e358]: UIF-PRECISION-00020
            - button "Select UI benchmark support 00020 in viewport" [ref=e359] [cursor=pointer]:
              - img [ref=e360]
              - generic [ref=e363]: UIF-PRECISION-00020
          - img "Orientation gizmo showing X, Y, Z axes"
          - generic "View controls" [ref=e364]:
            - button "Front" [ref=e365] [cursor=pointer]
            - button "Top" [ref=e366] [cursor=pointer]
            - button "Isometric" [pressed] [ref=e367] [cursor=pointer]
          - generic:
            - generic: 1 m
        - region "Command and selection bar" [ref=e368]:
          - generic "Object creation tools" [ref=e369]:
            - button "Node" [ref=e370] [cursor=pointer]:
              - img [ref=e371]
              - text: Node
            - button "Pipe" [ref=e373] [cursor=pointer]:
              - img [ref=e374]
              - text: Pipe
            - button "Support" [ref=e378] [cursor=pointer]:
              - img [ref=e379]
              - text: Support
            - button "Component" [ref=e382] [cursor=pointer]:
              - img [ref=e383]
              - text: Component
            - button "Load" [ref=e386] [cursor=pointer]:
              - img [ref=e387]
              - text: Load
          - generic "Model focus" [ref=e389]: Select
          - group [ref=e390]:
            - generic "Selection & navigation" [ref=e391] [cursor=pointer]
      - text: ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾ ▾
    - complementary "Agent" [ref=e392]:
      - button "Agent" [disabled] [ref=e394]:
        - img [ref=e395]
        - generic [ref=e398]: Agent
  - generic "Workspace status" [ref=e399]:
    - generic "Analysis statuses" [ref=e400]:
      - button "Solver · Not solved" [ref=e402] [cursor=pointer]
    - button "2 Issues" [ref=e403] [cursor=pointer]:
      - img [ref=e404]
      - text: 2 Issues
    - generic "Selection" [ref=e406]: "project: project:UIF-PRECISION-ORIGIN"
    - generic "Display units" [ref=e407]: Entered
    - button "About SWBPIPE…" [ref=e408] [cursor=pointer]:
      - img [ref=e409]
```

# Test source

```ts
  2002 |   const end = { x: rect.x + rect.width * 0.08, y: rect.y + rect.height * 0.81 };
  2003 |   const scalePoint = { x: scaleRect.x + scaleRect.width / 2, y: scaleRect.y + scaleRect.height / 2 };
  2004 |   expect(end.x).toBeGreaterThan(axisRect.x); expect(end.x).toBeLessThan(axisRect.x + axisRect.width);
  2005 |   expect(end.y).toBeGreaterThan(axisRect.y); expect(end.y).toBeLessThan(axisRect.y + axisRect.height);
  2006 |   await page.evaluate(() => {
  2007 |     const records: any[] = []; (globalThis as any).__decorativePointerWitness = records;
  2008 |     for (const type of ["pointerdown", "pointerup", "wheel"]) document.addEventListener(type, (event) => {
  2009 |       const target = event.target as HTMLElement;
  2010 |       const pointer = event as MouseEvent;
  2011 |       records.push({ type, trusted: event.isTrusted, x: pointer.clientX, y: pointer.clientY,
  2012 |         mainCanvas: target === document.querySelector('[data-testid="viewport-canvas"] canvas'),
  2013 |         targetTag: target.tagName, targetTestId: target.dataset.testid ?? null });
  2014 |     }, { capture: true, passive: true });
  2015 |   });
  2016 |   const hits = await page.evaluate((points) => points.map((point) => {
  2017 |     const target = document.elementFromPoint(point.x, point.y) as HTMLElement | null;
  2018 |     return { point, mainCanvas: target === document.querySelector('[data-testid="viewport-canvas"] canvas'),
  2019 |       tag: target?.tagName, testId: target?.dataset.testid ?? null };
  2020 |   }), [start, end, scalePoint]);
  2021 |   // Record trusted events at both decorative surfaces before asserting passthrough,
  2022 |   // so the unpatched failure includes actual pointer ownership, not CSS inspection.
  2023 |   for (const point of [end, scalePoint]) { await page.mouse.move(point.x, point.y); await page.mouse.down(); await page.mouse.up(); }
  2024 |   const pointerPreconditions = await page.evaluate(() => (globalThis as any).__decorativePointerWitness);
  2025 |   await testInfo.attach("decorative-pointer-preconditions", { body: JSON.stringify({ rect, axisRect, scaleRect, hits, pointerPreconditions }, null, 2), contentType: "application/json" });
  2026 |   expect(hits.every((hit) => hit.mainCanvas), JSON.stringify(hits)).toBe(true);
  2027 |   expect(pointerPreconditions.every((event: any) => event.trusted && event.mainCanvas)).toBe(true);
  2028 |   const read = async () => page.evaluate(() => {
  2029 |     const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
  2030 |     if ("status" in snapshot.viewport) throw new Error("Viewport unavailable");
  2031 |     return snapshot.viewport;
  2032 |   });
  2033 |   const settled = async () => {
  2034 |     await expect.poll(async () => (await read()).resources.ownedPendingRafCount).toBe(0);
  2035 |     return read();
  2036 |   };
  2037 |   await activateWithKeyboard(page, page.getByTestId("viewport-box-select"));
  2038 |   await page.getByTestId("viewport-selection-filter").selectOption("components");
  2039 |   const beforeBox = await settled();
  2040 |   await page.mouse.move(start.x, start.y); await page.mouse.down();
  2041 |   await page.mouse.move(end.x, end.y, { steps: 6 }); await page.mouse.up();
  2042 |   await expect.poll(async () => { const box = (await read()).box; return "status" in box ? null : box.orderedRefs; }).toEqual([]);
  2043 |   const afterBox = await settled();
  2044 |   expect(afterBox.box).toMatchObject({ orderedRefs: [], primaryRef: null, direction: "right-to-left", filter: "components" });
  2045 |   expect(afterBox.selection.orderedRefs).toEqual([]); expect(afterBox.selection.primaryRef).toBeNull();
  2046 |   expect(afterBox.camera).toEqual(beforeBox.camera); expect(afterBox.canvas).toEqual(beforeBox.canvas);
  2047 |   await activateWithKeyboard(page, page.getByTestId("viewport-box-select"));
  2048 |   const orbitBefore = await settled();
  2049 |   await page.mouse.move(end.x, end.y); await page.mouse.down();
  2050 |   await page.mouse.move(end.x + 42, end.y - 28, { steps: 8 }); await page.mouse.up();
  2051 |   const orbitAfter = await settled();
  2052 |   expect(orbitAfter.camera.position).not.toEqual(orbitBefore.camera.position);
  2053 |   expect(orbitAfter.camera.target).toEqual(orbitBefore.camera.target);
  2054 |   await page.mouse.move(scalePoint.x, scalePoint.y); await page.mouse.down({ button: "right" });
  2055 |   await page.mouse.move(scalePoint.x - 40, scalePoint.y - 25, { steps: 8 }); await page.mouse.up({ button: "right" });
  2056 |   const panAfter = await settled();
  2057 |   expect(panAfter.camera.target).not.toEqual(orbitAfter.camera.target);
  2058 |   panAfter.camera.position.forEach((value, i) => expect(value - orbitAfter.camera.position[i]).toBeCloseTo(panAfter.camera.target[i] - orbitAfter.camera.target[i], 8));
  2059 |   const distance = (state: typeof panAfter) => Math.hypot(...state.camera.position.map((value, i) => value - state.camera.target[i]));
  2060 |   await page.mouse.move(scalePoint.x, scalePoint.y); await page.mouse.wheel(0, -120);
  2061 |   await expect.poll(async () => distance(await read())).toBeLessThan(distance(panAfter));
  2062 |   const wheelAfter = await settled();
  2063 |   // Active OrbitControls updates normalize/rescale the target even without a
  2064 |   // target-radius constraint. Allow binary64 roundoff from that arithmetic and
  2065 |   // the local/authored translation; idle and Box invariants stay exact above.
  2066 |   const targetScale = Math.max(1, ...panAfter.camera.target.map(Math.abs), ...panAfter.camera.localRenderOrigin.map(Math.abs));
  2067 |   const targetRoundoff = 16 * Number.EPSILON * targetScale;
  2068 |   wheelAfter.camera.target.forEach((value, i) => {
  2069 |     expect(Number.isFinite(value)).toBe(true);
  2070 |     expect(Math.abs(value - panAfter.camera.target[i])).toBeLessThanOrEqual(targetRoundoff);
  2071 |   });
  2072 |   const front = page.getByRole("button", { name: "Front", exact: true });
  2073 |   await front.click(); await expect(front).toHaveAttribute("aria-pressed", "true");
  2074 |   const frontAfter = await settled(); expect(frontAfter.camera.position).not.toEqual(wheelAfter.camera.position);
  2075 |   await page.getByTestId("viewport-view-isometric").click(); await settled();
  2076 |   await setCurrentLabelMode(page, "Budget");
  2077 |   const node = model.nodes[10]; await selectTreeRow(page, "node", node.id);
  2078 |   const label = page.getByRole("button", { name: `Select ${node.label} in viewport`, exact: true });
  2079 |   await expect(label).toBeVisible(); await label.click();
  2080 |   await expect(page.getByTestId("command-selection-readout")).toContainText(`node: ${node.id}`);
  2081 |   await expect(axis).toBeVisible(); await expect(scale).toHaveText(/1\s*m/);
  2082 |   const events = await page.evaluate(() => (globalThis as any).__decorativePointerWitness);
  2083 |   expect(events.filter((event: any) => event.type === "wheel")).toEqual(expect.arrayContaining([expect.objectContaining({ trusted: true, mainCanvas: true })]));
  2084 |   await testInfo.attach("decorative-pointer-gesture-results", { body: JSON.stringify({ beforeBox, afterBox, orbitBefore, orbitAfter, panAfter, wheelAfter, frontAfter, events }, null, 2), contentType: "application/json" });
  2085 |   await page.screenshot({ path: testInfo.outputPath("decorative-overlays-and-view-controls.png") });
  2086 | });
  2087 | 
  2088 | // V30: genuine captured-pointer lifetime, including independent normal Open control.
  2089 | test.describe("captured Box lifetime", () => {
  2090 | async function read(page: Page) {
  2091 |   return page.evaluate(() => {
  2092 |     const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
  2093 |     if ("status" in snapshot.viewport) throw new Error("Viewport unavailable");
  2094 |     return { snapshot, rectangleCount: document.querySelectorAll(".viewport-box-rect").length,
  2095 |       readout: document.querySelector('[data-testid="command-selection-readout"]')?.textContent,
  2096 |       inspector: document.querySelector('[data-testid="property-inspector"] h2')?.textContent,
  2097 |       publicPreparationControls: [...document.querySelectorAll<HTMLElement>('[data-testid*="draft-review"], [data-testid*="direct-review"]')].map(e => ({ id: e.dataset.testid, text: e.textContent })),
  2098 |       events: (globalThis as any).__boxGestureEvents };
  2099 |   });
  2100 | }
  2101 | async function settle(page: Page) {
> 2102 |   await expect.poll(async () => (await read(page)).snapshot.viewport.resources.ownedPendingRafCount).toBe(0);
       |                                                                                                      ^ Error: expect(received).toBe(expected) // Object.is equality
  2103 |   return read(page);
  2104 | }
  2105 | async function setup(page: Page) {
  2106 |   const model = await gotoRoutedFixture(page); expect(model.components ?? []).toHaveLength(0);
  2107 |   await setCurrentLabelMode(page, "Off");
  2108 |   await selectTreeRow(page, "node", model.nodes[10].id);
  2109 |   await expect.poll(async () => (await read(page)).snapshot.viewport.selection.orderedRefs).toEqual([{ type: "node", id: model.nodes[10].id }]);
  2110 |   await page.evaluate(() => {
  2111 |     const events: any[] = []; (globalThis as any).__boxGestureEvents = events;
  2112 |     for (const type of ["pointerdown", "pointermove", "pointerup", "pointercancel", "lostpointercapture", "keydown"]) document.addEventListener(type, event => {
  2113 |       const e = event as PointerEvent & KeyboardEvent;
  2114 |       events.push({ type, trusted: event.isTrusted, key: e.key ?? null, pointerId: e.pointerId ?? null, buttons: e.buttons ?? null,
  2115 |         targetTag: (event.target as Element).tagName, mainCanvas: event.target === document.querySelector('[data-testid="viewport-canvas"] canvas') });
  2116 |     }, true);
  2117 |   });
  2118 |   return model;
  2119 | }
  2120 | async function begin(page: Page) {
  2121 |   await activateWithKeyboard(page, page.getByTestId("viewport-box-select"));
  2122 |   await page.getByTestId("viewport-selection-filter").selectOption("components");
  2123 |   const rect = (await page.getByTestId("viewport-canvas").locator("canvas").boundingBox())!;
  2124 |   const start = { x: rect.x + .29 * rect.width, y: rect.y + .58 * rect.height };
  2125 |   const end = { x: rect.x + .08 * rect.width, y: rect.y + .81 * rect.height };
  2126 |   for (const point of [start, end]) expect(await page.evaluate(({ x, y }) => document.elementFromPoint(x, y) === document.querySelector('[data-testid="viewport-canvas"] canvas'), point)).toBe(true);
  2127 |   const before = await settle(page);
  2128 |   await page.mouse.move(start.x, start.y); await page.mouse.down();
  2129 |   await page.mouse.move((start.x + end.x) / 2, (start.y + end.y) / 2, { steps: 5 });
  2130 |   expect(await page.locator(".viewport-box-rect").count()).toBe(1);
  2131 |   return { before, start, end, rect };
  2132 | }
  2133 | async function finish(page: Page, end: { x: number; y: number }) {
  2134 |   await page.mouse.move(end.x, end.y, { steps: 5 }); await page.mouse.up();
  2135 |   return settle(page);
  2136 | }
  2137 | 
  2138 | test("ordinary real Box applies independent empty Components membership", async ({ page }, info) => {
  2139 |   await setup(page); const input = await begin(page); const after = await finish(page, input.end);
  2140 |   await info.attach("ordinary-box", { body: JSON.stringify({ input, after }, null, 2), contentType: "application/json" });
  2141 |   expect(after.snapshot.viewport.selection.orderedRefs).toEqual([]); expect(after.snapshot.viewport.selection.primaryRef).toBeNull();
  2142 |   expect(after.snapshot.viewport.box).toMatchObject({ orderedRefs: [], primaryRef: null, filter: "components" });
  2143 |   expect(after.snapshot.viewport.camera).toEqual(input.before.snapshot.viewport.camera);
  2144 | });
  2145 | 
  2146 | test("Escape retires captured Box before delayed pointer up", async ({ page }, info) => {
  2147 |   await setup(page); const input = await begin(page);
  2148 |   await page.keyboard.press("Escape"); const afterEscape = await read(page);
  2149 |   await page.screenshot({ path: info.outputPath("after-escape-before-up.png") });
  2150 |   const after = await finish(page, input.end);
  2151 |   await info.attach("escape-reproduction", { body: JSON.stringify({ input, afterEscape, after }, null, 2), contentType: "application/json" });
  2152 |   await page.screenshot({ path: info.outputPath("after-delayed-up.png") });
  2153 |   expect.soft(afterEscape.rectangleCount).toBe(0);
  2154 |   expect.soft(after.snapshot.viewport.selection.orderedRefs).toEqual(input.before.snapshot.viewport.selection.orderedRefs);
  2155 |   expect.soft(after.snapshot.viewport.selection.primaryRef).toEqual(input.before.snapshot.viewport.selection.primaryRef);
  2156 |   expect.soft(after.snapshot.viewport.selection.actionSequence).toBe(input.before.snapshot.viewport.selection.actionSequence);
  2157 |   expect.soft(after.snapshot.viewport.box).toEqual(input.before.snapshot.viewport.box);
  2158 |   expect.soft(after.publicPreparationControls).toEqual(input.before.publicPreparationControls);
  2159 |   expect(after.snapshot.viewport.camera).toEqual(input.before.snapshot.viewport.camera);
  2160 | });
  2161 | 
  2162 | test("same-ID Open retires old captured Box before delayed pointer up", async ({ page }, info) => {
  2163 |   await page.addInitScript(() => {
  2164 |     const journal: unknown[] = []; (globalThis as any).__c4BoundaryJournal = journal;
  2165 |     const key = (target: EventTarget | null) => target instanceof Element ? target.closest<HTMLElement>("[data-entity-key]")?.dataset.entityKey ?? target.tagName : null;
  2166 |     for (const type of ["pointerover", "pointerout", "pointerenter", "pointerleave", "gotpointercapture", "lostpointercapture"]) document.addEventListener(type, event => {
  2167 |       const e = event as PointerEvent, target = e.target as Element;
  2168 |       const api = (globalThis as any).__openPipeStressUiDiagnosticsV1;
  2169 |       const snapshot = api?.readCurrent();
  2170 |       if (journal.length < 160) journal.push({ type, target: key(e.target), related: key(e.relatedTarget),
  2171 |         x: e.clientX, y: e.clientY, buttons: e.buttons, time: performance.now(),
  2172 |         rect: target instanceof Element ? target.getBoundingClientRect().toJSON() : null,
  2173 |         hit: key(document.elementFromPoint(e.clientX, e.clientY)),
  2174 |         viewport: snapshot && !("status" in snapshot.viewport) ? {
  2175 |           camera: snapshot.viewport.camera, labels: snapshot.viewport.labels, resources: snapshot.viewport.resources
  2176 |         } : null });
  2177 |     }, true);
  2178 |   });
  2179 |   const model = await setup(page); const project = { type: "project", id: model.project.id };
  2180 |   await projectCommand(page, "save-local");
  2181 |   await expect(page.getByTestId("local-project-message")).toContainText("Saved");
  2182 |   const beforeOrdinaryOpen = await settle(page);
  2183 |   await projectCommand(page, "open-local", true);
  2184 |   await expect.poll(async () => (await read(page)).snapshot.model.projectSessionGeneration).toBe(beforeOrdinaryOpen.snapshot.model.projectSessionGeneration + 1);
  2185 |   await expect.poll(async () => (await read(page)).snapshot.viewport.selection.orderedRefs).toEqual([project]);
  2186 |   const ordinaryOpen = await settle(page);
  2187 |   expect(ordinaryOpen.snapshot.viewport.selection.primaryRef).toEqual(project);
  2188 |   expect(ordinaryOpen.snapshot.viewport.inspector.ref).toEqual(project);
  2189 |   await selectTreeRow(page, "node", model.nodes[10].id);
  2190 |   const input = await begin(page);
  2191 |   // Public keyboard route: keep the genuine mouse button held and captured.
  2192 |   await projectCommand(page, "open-local", true);
  2193 |   await expect.poll(async () => (await read(page)).snapshot.model.projectSessionGeneration).toBe(input.before.snapshot.model.projectSessionGeneration + 1);
  2194 |   await expect.poll(async () => (await read(page)).snapshot.viewport.selection.orderedRefs).toEqual([project]);
  2195 |   const replaced = await settle(page).catch(async error => {
  2196 |     await info.attach("c4-stationary-pointer-boundaries", { body: JSON.stringify(await page.evaluate(() => (globalThis as any).__c4BoundaryJournal), null, 2), contentType: "application/json" });
  2197 |     throw error;
  2198 |   });
  2199 |   expect(replaced.snapshot.viewport.selection.primaryRef).toEqual(project);
  2200 |   expect(replaced.snapshot.viewport.inspector.ref).toEqual(project);
  2201 |   expect(replaced.snapshot.model.identityHash).toBe(ordinaryOpen.snapshot.model.identityHash);
  2202 |   await page.mouse.move(input.end.x, input.end.y, { steps: 5 });
```