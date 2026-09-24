# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: b4-pipes.spec.ts >> B4 Pipes equivalent explicit-unit edits preserve model and history
- Location: e2e/b4-pipes.spec.ts:87:1

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: getByTestId('solve-job-summary')
Expected substring: "state=completed"
Received string:    "state=failed; events=3; result_rows=0; cancellation_requested=false"
Timeout: 10000ms

Call log:
  - Expect "toContainText" with timeout 10000ms
  - waiting for getByTestId('solve-job-summary')
    24 × locator resolved to <span data-testid="solve-job-summary">…</span>
       - unexpected value "state=failed; events=3; result_rows=0; cancellation_requested=false"

```

```yaml
- text: state=failed; events=3; result_rows=0; cancellation_requested=false
```

# Test source

```ts
  1   | import { expect, test, type Page } from "@playwright/test";
  2   | import { attachBrowserIdentity, currentModelHashThroughVisibleExport, gotoModel, readFixture } from "./ui-foundation-workflows";
  3   | import { ensureTreeExpanded, openWorkspaceSection, showModelTree } from "./workspace-driver";
  4   | 
  5   | async function openPipes(page: Page, model: any) {
  6   |   await gotoModel(page, model); await page.getByTestId("view-switch-table").click(); await ensureTreeExpanded(page);
  7   |   await page.getByTestId("layout-mode-grid").click(); await page.getByTestId("entity-grid-type-pipes").click();
  8   | }
  9   | 
  10  | test("B4 Pipes absent zero, entered unit, material ID and history use real operation routes", async ({ page, browser }, info) => {
  11  |   await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json");
  12  |   const pipe = model.pipe_segments[0]; delete pipe.section.mill_tolerance;
  13  |   model.materials.push({ ...structuredClone(model.materials[0]), id: "material:B4-pipe-alternate", label: "Invented alternate" });
  14  |   await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  15  |   for (const key of ["from", "to", "section-ref"]) await expect(table.getByTestId(`table-cell-${pipe.id}-${key}`).locator("..")).toHaveAttribute("aria-readonly", "true");
  16  |   await cell.dblclick(); const input = table.getByRole("textbox"); await input.fill("0"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  17  |   await expect(table.getByRole("alert")).toContainText("value and unit"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  18  |   await input.fill("0 mm"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0");
  19  |   await page.getByTestId("workspace-undo").click(); await expect(cell).toHaveText("TBD"); await page.getByTestId("workspace-redo").click(); await expect(cell).toHaveText("0");
  20  |   await cell.dblclick(); await expect(input).toHaveAccessibleName(`${pipe.id} Mill tol. (absent: value unit) [mm]`); await input.fill("0.1");
  21  |   await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0.1");
  22  |   const material = table.getByTestId(`table-cell-${pipe.id}-material`); await material.dblclick(); const ref = table.getByRole("combobox"); await ref.fill("material:B4-pipe-alternate");
  23  |   await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(material).toHaveText("material:B4-pipe-alternate");
  24  |   await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material); await page.getByTestId("workspace-redo").click(); await expect(material).toHaveText("material:B4-pipe-alternate");
  25  |   await info.attach("pipe-final-model-hash", { body: await currentModelHashThroughVisibleExport(page), contentType: "text/plain" });
  26  | });
  27  | 
  28  | test("B4 Pipes shared section effective-wall rejection preserves model and history", async ({ page, browser }, info) => {
  29  |   await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  30  |   model.sections = [...(model.sections ?? []), { id: "section:B4-pipe", name: "Invented section", section_type: "pipe", properties: { outside_diameter: { value: 100, unit: "mm" }, wall_thickness: { value: 10, unit: "mm" } }, provenance: "invented Pipe browser fixture" }];
  31  |   pipe.section_ref = "section:B4-pipe"; pipe.section.outside_diameter = { value: 100, unit: "mm" }; pipe.section.wall_thickness = { value: 10, unit: "mm" }; pipe.section.mill_tolerance = { value: 0, unit: "mm" };
  32  |   await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  33  |   const before = await currentModelHashThroughVisibleExport(page); await cell.dblclick(); await table.getByRole("textbox").fill("10"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  34  |   await expect(table.getByRole("alert")).toContainText("Engine rejected"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  35  |   await table.getByRole("button", { name: "Cancel", exact: true }).click(); expect(await currentModelHashThroughVisibleExport(page)).toBe(before); await expect(cell).toHaveText("0");
  36  | });
  37  | 
  38  | 
  39  | test("B4 Pipes direct and review author the same optional quantity with retained incomplete drafts", async ({ page, browser }, info) => {
  40  |   await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0]; delete pipe.section.mill_tolerance;
  41  |   await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  42  |   await cell.dblclick(); await table.getByRole("textbox").fill("0 mm"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0");
  43  |   const directHash = await currentModelHashThroughVisibleExport(page); await page.getByTestId("workspace-undo").click(); await expect(cell).toHaveText("TBD");
  44  |   await page.getByTestId("pipe-grid-review-disclosure").click(); const review = page.getByTestId("pipe-engineering-table-review"), draft = review.getByTestId(`review-cell-${pipe.id}-mill-tolerance`);
  45  |   await draft.dblclick(); await review.getByRole("textbox").fill("0"); await review.getByRole("button", { name: "Keep draft", exact: true }).click(); await expect(page.getByTestId("queue-entity-grid-intents")).toBeDisabled();
  46  |   await page.getByTestId("entity-grid-type-nodes").click(); await page.getByTestId("entity-grid-type-pipes").click(); await expect(draft).toHaveText("0");
  47  |   await page.getByTestId("clear-entity-grid-drafts").click(); await expect(draft).toHaveText("TBD");
  48  |   await draft.dblclick(); await review.getByRole("textbox").fill("0 mm"); await review.getByRole("button", { name: "Keep draft", exact: true }).click();
  49  |   await page.getByTestId("queue-entity-grid-intents").click(); await expect(page.getByTestId("operation-apply-row-editor-intent-1")).toContainText('"unit":"mm"');
  50  |   await page.getByTestId("apply-intent-editor-intent-1").click(); await expect(page.getByTestId("operation-apply-summary")).toContainText("2 applied");
  51  |   await showModelTree(page); await page.getByTestId("pipe-grid-review-disclosure").click(); await expect(cell).toHaveText("0");
  52  |   expect(await currentModelHashThroughVisibleExport(page)).toBe(directHash);
  53  | });
  54  | 
  55  | 
  56  | for (const reduction of [10, 11]) test(`B4 Pipes unbound mill tolerance ${reduction} rejects exhausted effective wall`, async ({ page, browser }, info) => {
  57  |   await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  58  |   delete pipe.section_ref; pipe.section.outside_diameter = { value: 100, unit: "mm" }; pipe.section.wall_thickness = { value: 10, unit: "mm" }; pipe.section.mill_tolerance = { value: 0, unit: "mm" };
  59  |   await openPipes(page, model); const before = await currentModelHashThroughVisibleExport(page); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  60  |   await cell.dblclick(); await table.getByRole("textbox").fill(String(reduction)); await table.getByRole("button", { name: "Apply", exact: true }).click();
  61  |   await expect(table.getByRole("alert")).toContainText("Engine rejected"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  62  |   await table.getByRole("button", { name: "Cancel", exact: true }).click(); await expect(cell).toHaveText("0"); expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
  63  | });
  64  | 
  65  | test("B4 Pipes compact label provenance and material completion retain editor ownership", async ({ page, browser }, info) => {
  66  |   await attachBrowserIdentity(browser, info);
  67  |   await page.addInitScript(() => localStorage.setItem("chirality.desktop.ui-preferences.v1", JSON.stringify({ version: 1, density: "compact", tableDrawerPx: 227 })));
  68  |   const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  69  |   model.materials.push({ ...structuredClone(model.materials[0]), id: "material:B4-compact-choice", label: "Invented choice" });
  70  |   await gotoModel(page, model); await page.getByTestId("view-switch-model").click(); await ensureTreeExpanded(page); await page.getByTestId("layout-mode-grid").click();
  71  |   await page.getByRole("combobox", { name: "Grid family" }).selectOption("pipes"); const table = page.getByTestId("pipe-engineering-table");
  72  |   const label = table.getByTestId(`table-cell-${pipe.id}-label`); await label.dblclick(); const input = table.getByRole("textbox"); await input.fill("Invented pipe label"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(label).toHaveText("Invented pipe label");
  73  |   const later = page.getByRole("button", { name: "Later columns", exact: true }); while (await later.isEnabled()) await later.click();
  74  |   const provenance = table.getByTestId(`table-cell-${pipe.id}-provenance`); await provenance.dblclick(); await input.fill("Invented source note");
  75  |   const earlier = page.getByRole("button", { name: "Earlier columns", exact: true }); await earlier.click(); await expect(input).toHaveValue("Invented source note");
  76  |   while (await later.isEnabled()) await later.click(); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(provenance).toHaveText("Invented source note");
  77  |   const material = table.getByTestId(`table-cell-${pipe.id}-material`); await material.dblclick(); const ref = table.getByRole("combobox"); await ref.fill("material:B4-compact");
  78  |   await page.getByRole("option", { name: "material:B4-compact-choice", exact: true }).click(); await expect(ref).toHaveValue("material:B4-compact-choice");
  79  |   await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(material).toHaveText("material:B4-compact-choice");
  80  |   await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material);
  81  |   await material.dblclick(); await ref.fill("material:B4-compact"); await ref.press("Enter"); await expect(material).toHaveText("material:B4-compact-choice");
  82  |   await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material);
  83  |   await page.getByTestId("workspace-undo").click(); await expect(provenance).toHaveText(pipe.provenance);
  84  | });
  85  | 
  86  | 
  87  | test("B4 Pipes equivalent explicit-unit edits preserve model and history", async ({ page, browser }, info) => {
  88  |   await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  89  |   pipe.section.mill_tolerance = { value: 0, unit: "mm" }; await openPipes(page, model);
  90  |   // This edited model receives the real browser's blocked result, not synthetic solved rows.
  91  |   await openWorkspaceSection(page, "solve"); await page.getByTestId("run-mechanics-preview").click();
> 92  |   await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
      |                                                       ^ Error: expect(locator).toContainText(expected) failed
  93  |   const resultConsent = page.getByTestId("solve-job-export-link-local-private-intent"); await resultConsent.check();
  94  |   const runReceipt = await page.getByTestId("solve-job-export-link").getAttribute("href"); expect(runReceipt).toBeTruthy();
  95  |   const readiness = await page.getByTestId("readiness-mechanics").textContent();
  96  |   await showModelTree(page);
  97  |   const before = await currentModelHashThroughVisibleExport(page); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  98  |   for (const value of ["0 mm", "0.0 mm"]) {
  99  |     await cell.dblclick(); await table.getByRole("textbox").fill(value); await table.getByRole("button", { name: "Apply", exact: true }).click();
  100 |     await expect(table.getByRole("textbox")).toHaveCount(0); await expect(cell).toBeFocused(); await expect(cell).toHaveText("0");
  101 |     await expect(page.getByTestId("workspace-undo")).toBeDisabled(); await expect(page.getByTestId("workspace-redo")).toBeDisabled(); await expect(page.getByTestId("project-edited")).toHaveCount(0);
  102 |     expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
  103 |     await openWorkspaceSection(page, "solve"); if (!await resultConsent.isChecked()) await resultConsent.check();
  104 |     expect(await page.getByTestId("solve-job-export-link").getAttribute("href")).toBe(runReceipt);
  105 |     expect(await page.getByTestId("readiness-mechanics").textContent()).toBe(readiness); await showModelTree(page);
  106 |   }
  107 |   await cell.dblclick(); await table.getByRole("textbox").fill("0 m"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  108 |   await expect(table.getByRole("alert")).toContainText("existing unit"); await expect(table.getByRole("textbox")).toHaveValue("0 m");
  109 |   await table.getByRole("button", { name: "Cancel", exact: true }).click(); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  110 |   expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
  111 | });
  112 | 
```