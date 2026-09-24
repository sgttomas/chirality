import { expect, test, type Page, type TestInfo } from "@playwright/test";
import { readFile } from "node:fs/promises";
import { openWorkspaceSection, projectCommand, selectTreeEntity, showCanvas, showModelTree } from "./workspace-driver";

// Functional invented inputs only: no frozen benchmark helpers, caps or instrumentation.
async function fixture(dense = false, coincident = false) {
  const model = JSON.parse(await readFile(new URL("../../../fixtures/product_preview/invented_preview_model.json", import.meta.url), "utf8"));
  const node = (id: string, x: number, y: number) => ({ ...model.nodes[0], id, label: id, position: { x, y, z: 0 } });
  // Wide row spacing leaves real gaps for bounded vertical placement offsets;
  // this invented population is independent of protected performance fixtures.
  model.nodes = dense ? Array.from({ length: 136 }, (_, i) => node(`n${i}`, i % 17, Math.floor(i / 17) * 2.25))
    : [node("A", -4, -3), node("B", 4, 3), node("C", -4, 3), node("D", 4, -3)];
  model.pipe_segments = [{ ...model.pipe_segments[0], id: "P", label: "P", from: dense ? "n0" : "C", to: dense ? "n1" : "B" }];
  if (coincident) {
    // Two genuine, distinct identity populations intentionally share coordinates.
    // Synthetic UI multiplicity only; no solver-readiness/engineering claim.
    const positions = model.nodes.map((entry: any) => entry.position);
    model.nodes = ["A", "B"].flatMap(prefix => positions.map((position: any, i: number) =>
      node(`${prefix}${String(i + 1).padStart(3, "0")}`, position.x, position.y)));
    model.pipe_segments[0].from = "A001"; model.pipe_segments[0].to = "A002";
  }
  model.supports = []; model.components = []; model.load_cases = []; model.combinations = []; model.diagnostics = [];
  return model;
}
async function load(page: Page, model: any) {
  await page.route(/(?:invented_preview_model-[^/]+\.js|fixtures\/product_preview\/invented_preview_model\.json)(?:\?.*)?$/, route =>
    route.fulfill({ status: 200, contentType: "application/javascript", body: `export default ${JSON.stringify(model)};` }));
  await page.goto("/");
  await expect(page.getByTestId("viewport-canvas").locator("canvas")).toHaveCount(1);
  // Exercise normal visible project save/reopen with this disclosed input fixture.
  await projectCommand(page, "new-local");
  await expect(page.getByTestId("local-project-message")).toContainText("Created");
  await projectCommand(page, "save-local");
  await expect(page.getByTestId("local-project-message")).toContainText("Saved");
  await projectCommand(page, "open-local");
  await showCanvas(page);
  await page.getByRole("button", { name: "Front", exact: true }).click();
  await page.getByTestId("viewport-fit-model").click();
  await settle(page);
}
async function state(page: Page) {
  return page.evaluate(() => {
    const s = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
    if ("status" in s.viewport) throw new Error("Viewport diagnostics unavailable");
    return s;
  });
}
async function settle(page: Page) {
  await expect.poll(async () => { const s = await state(page); return "status" in s.viewport ? null : s.viewport.resources.ownedPendingRafCount; }).toBe(0);
}
async function labels(page: Page) {
  const s = await state(page); if ("status" in s.viewport) throw new Error("Viewport unavailable"); return s.viewport.labels;
}
async function mode(page: Page, desired: "Budget" | "All" | "Off") {
  const control = page.getByTestId("toggle-viewport-labels");
  for (let i = 0; i < 3 && await control.getAttribute("data-label-mode") !== desired; i++) await control.click();
  await expect(control).toHaveAttribute("data-label-mode", desired); await settle(page);
}
async function invariants(page: Page) {
  await openWorkspaceSection(page, "project");
  await page.getByTestId("project-validation-export-link-local-private-intent").check();
  const link = page.getByTestId("project-validation-export-link");
  await expect(link).toHaveAttribute("href", /^data:/);
  const href = (await link.getAttribute("href"))!;
  const hash = JSON.parse(decodeURIComponent(href.slice(href.indexOf(",") + 1))).model_hash.value;
  // Project is an overlay: close it through the visible page control before
  // the operations helper targets the underlying workspace review tab.
  await showCanvas(page);
  await openWorkspaceSection(page, "operations");
  const history = await page.getByTestId("session-history-chip").innerText();
  await openWorkspaceSection(page, "results");
  const results = await page.getByTestId("results-panel").allTextContents();
  const historical = await page.getByTestId("historical-run-context").allTextContents();
  await showCanvas(page); return { hash, history, results, historical };
}
async function witness(page: Page, info: TestInfo, name: string) {
  await settle(page);
  const evidence = await page.evaluate(() => {
    const s = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
    if ("status" in s.viewport) throw new Error("Viewport unavailable");
    const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!.getBoundingClientRect();
    const boxes = [...document.querySelectorAll<HTMLElement>('.viewport-select-target[data-label-placed="true"]')].map(el => ({
      key: el.dataset.entityKey, rect: el.getBoundingClientRect().toJSON(), pressed: el.getAttribute("aria-pressed") }));
    return { labels: s.viewport.labels, selection: s.viewport.selection, camera: s.viewport.camera, canvas: canvas.toJSON(), boxes };
  });
  await info.attach(name, { body: JSON.stringify(evidence, null, 2), contentType: "application/json" });
  expect(evidence.labels.placementStatus).toBe("applied");
  expect(evidence.labels.renderedCount).toBe(evidence.boxes.length);
  expect(evidence.labels.budget).toBe(Math.floor(evidence.canvas.width * evidence.canvas.height / 3600));
  expect(new Set(evidence.boxes.map(b => b.key)).size).toBe(evidence.boxes.length);
  for (const [i, { rect: a }] of evidence.boxes.entries()) {
    expect(a.left).toBeGreaterThanOrEqual(evidence.canvas.left); expect(a.right).toBeLessThanOrEqual(evidence.canvas.right);
    expect(a.top).toBeGreaterThanOrEqual(evidence.canvas.top); expect(a.bottom).toBeLessThanOrEqual(evidence.canvas.bottom);
    for (const { rect: b } of evidence.boxes.slice(i + 1)) expect(a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top).toBe(false);
  }
  const omissions = page.getByTestId("viewport-label-omissions");
  await omissions.locator("summary").click();
  const omitted = [...(evidence.labels.suppressed ?? []), ...(evidence.labels.unplaced ?? [])];
  await expect(omissions.locator("li")).toHaveCount(omitted.length);
  for (const item of omitted) await expect(omissions).toContainText(item.key);
  await omissions.locator("summary").click();
  return evidence;
}
async function projected(page: Page, position: { x: number; y: number; z: number }) {
  await settle(page);
  return page.evaluate(position => {
    const api = globalThis.__openPipeStressUiDiagnosticsV1, s = api.readCurrent();
    if ("status" in s.viewport || s.model.generation === null) throw new Error("Viewport unavailable");
    const p = api.projectAuthoredPoint({ modelGeneration: s.model.generation, cameraSequence: s.viewport.camera.sequence, authoredPoint: position });
    if (p.status !== "available" || !p.insideCanvasCss) throw new Error("Required real geometry pick outside canvas");
    const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!, b = canvas.getBoundingClientRect();
    const x = b.left + p.canvasCssPoint.x, y = b.top + p.canvasCssPoint.y;
    return { x, y, unobscured: document.elementFromPoint(x, y) === canvas };
  }, position);
}
export function registerC4LabelScenarios() {
  test("C4 modes, dedup, Hide/Isolate, hover, camera, resize and nonmutation @explicit-viewport", async ({ page }, info) => {
    await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
    const before = await invariants(page);
    await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Budget");
    await selectTreeEntity(page, "node", "A"); await mode(page, "Off");
    await expect(page.getByTestId("viewport-select-A")).toBeVisible();
    await page.getByTestId("viewport-select-A").hover();
    const off = await witness(page, info, "off-context-deduplicated-primary-hover"); expect(off.labels.ordinaryCount).toBe(0);
    expect(off.labels.contextCount).toBe(1); await page.mouse.move(0, 0);
    await page.getByRole("button", { name: "Isolate", exact: true }).click();
    await mode(page, "All");
    await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("data-dimmed", "true");
    const ordinary = page.locator('.viewport-select-target[data-label-placed="true"][aria-pressed="false"]').first();
    const box = await ordinary.boundingBox(); await ordinary.hover();
    for (let i = 0; i < 3; i++) { await settle(page); expect(await ordinary.boundingBox()).toEqual(box); }
    await page.mouse.move(0, 0); await witness(page, info, "all-hover-stable");
    await page.getByRole("button", { name: "Hide", exact: true }).click();
    for (const m of ["Budget", "All", "Off"] as const) { await mode(page, m); await expect(page.getByTestId("viewport-select-A")).toHaveCount(0); }
    await expect(page.getByTestId("viewport-hidden-count")).toHaveText("1 hidden · Show all");
    await page.getByRole("button", { name: "Show All", exact: true }).click();
    await mode(page, "All"); await page.setViewportSize({ width: 1100, height: 850 });
    await page.getByTestId("viewport-fit-model").click(); await witness(page, info, "resized-front");
    for (const node of (await fixture()).nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
    await page.getByRole("button", { name: "Top", exact: true }).click(); await witness(page, info, "camera-top");
    await page.getByTestId("viewport-canvas").focus(); await page.keyboard.press("l");
    await expect(page.getByTestId("toggle-viewport-labels")).toHaveAttribute("data-label-mode", "Off");
    expect(await invariants(page)).toEqual(before);
  });
  test("C4 current review row B remains distinct from primary A @explicit-viewport", async ({ page }, info) => {
    await page.setViewportSize({ width: 1440, height: 920 }); await load(page, await fixture());
    const before = await invariants(page); await mode(page, "Off");
    await showModelTree(page);
    await page.getByTestId("view-switch-both").click(); await page.getByTestId("layout-mode-grid").click();
    await page.getByTestId("table-cell-A-x").click();
    const deduplicatedRow = await witness(page, info, "primary-A-current-fields-row-A-deduplicated");
    expect(deduplicatedRow.labels.mode).toBe("Off");
    expect(deduplicatedRow.labels.contextCount).toBe(1);
    expect(deduplicatedRow.boxes.map(box => box.key)).toEqual([JSON.stringify(["node", "A"])]);
    await page.getByTestId("node-grid-review-disclosure").click();
    await page.getByTestId("review-cell-B-x").click();
    const current = await witness(page, info, "primary-A-review-B");
    expect(current.selection.primaryRef).toEqual({ type: "node", id: "A" });
    expect(current.selection.orderedRefs).toEqual([{ type: "node", id: "A" }]);
    await expect(page.getByTestId("viewport-select-B")).toHaveAttribute("aria-pressed", "false");
    await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await expect(page.getByTestId("viewport-select-B")).toBeVisible();
    expect(current.labels.contextCount).toBe(2); expect(current.labels.ordinaryCount).toBe(0);
    await page.getByTestId("node-grid-review-disclosure").click();
    await expect(page.getByTestId("viewport-select-B")).toBeHidden();
    expect(await invariants(page)).toEqual(before);
  });
  for (const coincident of [false, true]) {
  test(coincident
    ? "C4 synthetic coincident real identities produce actual placed context overflow @explicit-viewport"
    : "C4 unique full node inventory preserves spatial omissions @explicit-viewport", async ({ page }, info) => {
    await page.setViewportSize({ width: 1440, height: 920 }); const model = await fixture(true, coincident);
    await info.attach("dense-functional-fixture", { body: JSON.stringify({
      purpose: coincident ? "Two distinct real node populations intentionally share coordinates; synthetic UI test, not engineering acceptance" : "Unique-position full inventory and finite spatial omissions",
      model }, null, 2), contentType: "application/json" });
    await load(page, model);
    await page.getByTestId("view-switch-both").click(); await page.getByTestId("viewport-fit-model").click();
    const before = await invariants(page); await mode(page, "Off");
    await page.getByTestId("viewport-selection-filter").selectOption("nodes"); await page.getByTestId("viewport-box-select").click();
    const points = [];
    for (const node of model.nodes) points.push(await projected(page, node.position));
    const preselection = await page.evaluate(() => {
      const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
      if ("status" in snapshot.viewport) throw new Error("Viewport unavailable");
      const canvas = document.querySelector('[data-testid="viewport-canvas"] canvas')!.getBoundingClientRect();
      return { camera: snapshot.viewport.camera, canvas: canvas.toJSON(),
        measuredBudget: Math.floor(canvas.width * canvas.height / 3600), labels: snapshot.viewport.labels };
    });
    await info.attach("dense-projected-input-preselection", { body: JSON.stringify({
      ...preselection, nodes: model.nodes.map((node: any, i: number) => ({ id: node.id, authored: node.position, projected: points[i] }))
    }, null, 2), contentType: "application/json" });
    const left = Math.min(...points.map(p => p.x)) - 8, right = Math.max(...points.map(p => p.x)) + 8;
    const top = Math.min(...points.map(p => p.y)) - 8, bottom = Math.max(...points.map(p => p.y)) + 8;
    await page.mouse.move(left, top); await page.mouse.down(); await page.mouse.move(right, bottom, { steps: 6 }); await page.mouse.up();
    await page.getByTestId("viewport-box-select").click(); await mode(page, "Budget");
    const result = await witness(page, info, "dense-actual-placement");
    expect(result.selection.orderedRefs).toHaveLength(model.nodes.length);
    expect(await page.locator('.viewport-select-target[data-entity-key]').count()).toBe(model.nodes.length + model.pipe_segments.length);
    const expectedKeys = model.nodes.map((node: any) => JSON.stringify(["node", node.id])).sort();
    expect(new Set(expectedKeys).size).toBe(coincident ? 272 : 136);
    expect(result.selection.orderedRefs.map(ref => JSON.stringify([ref.type, ref.id])).sort()).toEqual(expectedKeys);
    const placedContextKeys = result.boxes.filter(box => expectedKeys.includes(box.key!)).map(box => box.key!);
    const unplacedContext = (result.labels.unplaced ?? []).filter(item => item.role !== "ordinary");
    expect(placedContextKeys.length).toBe(result.labels.contextCount);
    expect([...placedContextKeys, ...unplacedContext.map(item => item.key)].sort()).toEqual(expectedKeys);
    expect((result.labels.suppressed ?? []).filter(item => item.role !== "ordinary")).toEqual([]);
    expect((result.labels.ineligible ?? []).filter(item => item.role !== "ordinary")).toEqual([]);
    for (const box of result.boxes) {
      expect(model.nodes.some((node: any) => JSON.stringify(["node", node.id]) === box.key) ||
        model.pipe_segments.some((pipe: any) => JSON.stringify(["pipe", pipe.id]) === box.key)).toBe(true);
    }
    if (coincident) {
      const readableIdentities = [];
      for (const box of result.boxes) {
        const [type, id] = JSON.parse(box.key!);
        if (type !== "node") continue;
        const span = page.getByTestId(`viewport-select-${id}`).locator("span");
        await expect(span).toHaveText(id);
        const dimensions = await span.evaluate(element => ({ text: element.textContent,
          scrollWidth: element.scrollWidth, clientWidth: element.clientWidth }));
        expect(dimensions.scrollWidth, `${id} fits its unchanged visible label span`).toBeLessThanOrEqual(dimensions.clientWidth);
        readableIdentities.push({ key: box.key, ...dimensions });
      }
      await info.attach("dense-readable-real-identities", { body: JSON.stringify(readableIdentities, null, 2), contentType: "application/json" });
      // Rendered overflow is the gate; 272 requested identities alone prove nothing.
      expect(result.labels.contextCount).toBeGreaterThan(result.labels.budget);
      expect(result.labels.contextOverflow).toBe(result.labels.contextCount! - result.labels.budget);
      expect(result.labels.ordinaryCount).toBe(0);
      expect(result.labels.suppressed?.some(item => item.role === "ordinary" && item.reason === "budget")).toBe(true);
    } else {
      expect(unplacedContext.length).toBeGreaterThan(0);
      expect(result.labels.contextOverflow).toBe(Math.max(0, result.labels.contextCount! - result.labels.budget));
    }
    for (const node of model.nodes) expect((await projected(page, node.position)).unobscured).toBe(true);
    expect(await invariants(page)).toEqual(before);
  });
  }
  test("C4 label modes preserve Current and Historical result standing", async ({ page }) => {
    await page.goto("/"); await openWorkspaceSection(page, "solve");
    await page.getByTestId("run-mechanics-preview").click();
    await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
    await showCanvas(page); const current = await invariants(page);
    for (const m of ["Off", "All", "Budget"] as const) await mode(page, m);
    expect(await invariants(page)).toEqual(current);
    await projectCommand(page, "save-local");
    await expect(page.getByTestId("local-project-message")).toContainText("Saved");
    await projectCommand(page, "open-local"); await openWorkspaceSection(page, "results");
    await expect(page.getByTestId("historical-run-context")).toBeVisible();
    const historical = await invariants(page);
    for (const m of ["All", "Off", "Budget"] as const) await mode(page, m);
    expect(await invariants(page)).toEqual(historical);
  });
  test("C4 real WebGL loss/restoration fails closed and recovers", async ({ page }, info) => {
    await load(page, await fixture()); await selectTreeEntity(page, "node", "A");
    const before = await invariants(page); await mode(page, "Off");
    await expect(page.getByTestId("viewport-select-A")).toBeVisible();
    const supported = await page.evaluate(() => {
      const canvas = document.querySelector<HTMLCanvasElement>('[data-testid="viewport-canvas"] canvas')!;
      const gl = canvas.getContext("webgl2") ?? canvas.getContext("webgl");
      const extension = gl?.getExtension("WEBGL_lose_context");
      if (!extension) return false;
      (window as any).__c4ContextExtension = extension; extension.loseContext(); return true;
    });
    await info.attach("webgl-extension-availability", { body: JSON.stringify({ supported }), contentType: "application/json" });
    test.skip(!supported, "Real WEBGL_lose_context extension unavailable; loss/restoration remains unwitnessed");
    await expect(page.getByTestId("viewport-context-status")).toContainText("lost");
    const lostLabels = await labels(page);
    await info.attach("webgl-lost-label-diagnostics", { body: JSON.stringify(lostLabels, null, 2), contentType: "application/json" });
    expect(lostLabels.placementStatus).toBe("unavailable");
    expect(lostLabels.renderedCount).toBe(0);
    await expect(page.locator('.viewport-select-target[data-label-placed="true"]')).toHaveCount(0);
    await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("tabindex", "-1");
    await expect(page.getByTestId("viewport-select-A")).toHaveAttribute("aria-hidden", "true");
    await page.evaluate(() => { (window as any).__c4ContextExtension.restoreContext(); delete (window as any).__c4ContextExtension; });
    await expect(page.getByTestId("viewport-context-status")).toHaveCount(0);
    await expect(page.getByTestId("viewport-select-A")).toBeVisible(); await witness(page, info, "restored");
    expect(await invariants(page)).toEqual(before);
  });
}
