import { expect, test, type Page } from "@playwright/test";
import { attachBrowserIdentity, currentModelHashThroughVisibleExport, gotoModel, readFixture } from "./ui-foundation-workflows";
import { ensureTreeExpanded, openWorkspaceSection, showModelTree } from "./workspace-driver";

async function openPipes(page: Page, model: any) {
  await gotoModel(page, model); await page.getByTestId("view-switch-table").click(); await ensureTreeExpanded(page);
  await page.getByTestId("layout-mode-grid").click(); await page.getByTestId("entity-grid-type-pipes").click();
}

test("B4 Pipes absent zero, entered unit, material ID and history use real operation routes", async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json");
  const pipe = model.pipe_segments[0]; delete pipe.section.mill_tolerance;
  model.materials.push({ ...structuredClone(model.materials[0]), id: "material:B4-pipe-alternate", label: "Invented alternate" });
  await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  for (const key of ["from", "to", "section-ref"]) await expect(table.getByTestId(`table-cell-${pipe.id}-${key}`).locator("..")).toHaveAttribute("aria-readonly", "true");
  await cell.dblclick(); const input = table.getByRole("textbox"); await input.fill("0"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  await expect(table.getByRole("alert")).toContainText("value and unit"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  await input.fill("0 mm"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0");
  await page.getByTestId("workspace-undo").click(); await expect(cell).toHaveText("TBD"); await page.getByTestId("workspace-redo").click(); await expect(cell).toHaveText("0");
  await cell.dblclick(); await expect(input).toHaveAccessibleName(`${pipe.id} Mill tol. (absent: value unit) [mm]`); await input.fill("0.1");
  await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0.1");
  const material = table.getByTestId(`table-cell-${pipe.id}-material`); await material.dblclick(); const ref = table.getByRole("combobox"); await ref.fill("material:B4-pipe-alternate");
  await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(material).toHaveText("material:B4-pipe-alternate");
  await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material); await page.getByTestId("workspace-redo").click(); await expect(material).toHaveText("material:B4-pipe-alternate");
  await info.attach("pipe-final-model-hash", { body: await currentModelHashThroughVisibleExport(page), contentType: "text/plain" });
});

test("B4 Pipes shared section effective-wall rejection preserves model and history", async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  model.sections = [...(model.sections ?? []), { id: "section:B4-pipe", name: "Invented section", section_type: "pipe", properties: { outside_diameter: { value: 100, unit: "mm" }, wall_thickness: { value: 10, unit: "mm" } }, provenance: "invented Pipe browser fixture" }];
  pipe.section_ref = "section:B4-pipe"; pipe.section.outside_diameter = { value: 100, unit: "mm" }; pipe.section.wall_thickness = { value: 10, unit: "mm" }; pipe.section.mill_tolerance = { value: 0, unit: "mm" };
  await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  const before = await currentModelHashThroughVisibleExport(page); await cell.dblclick(); await table.getByRole("textbox").fill("10"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  await expect(table.getByRole("alert")).toContainText("Engine rejected"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  await table.getByRole("button", { name: "Cancel", exact: true }).click(); expect(await currentModelHashThroughVisibleExport(page)).toBe(before); await expect(cell).toHaveText("0");
});


test("B4 Pipes direct and review author the same optional quantity with retained incomplete drafts", async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0]; delete pipe.section.mill_tolerance;
  await openPipes(page, model); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  await cell.dblclick(); await table.getByRole("textbox").fill("0 mm"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0");
  const directHash = await currentModelHashThroughVisibleExport(page); await page.getByTestId("workspace-undo").click(); await expect(cell).toHaveText("TBD");
  await page.getByTestId("pipe-grid-review-disclosure").click(); const review = page.getByTestId("pipe-engineering-table-review"), draft = review.getByTestId(`review-cell-${pipe.id}-mill-tolerance`);
  await draft.dblclick(); await review.getByRole("textbox").fill("0"); await review.getByRole("button", { name: "Keep draft", exact: true }).click(); await expect(page.getByTestId("queue-entity-grid-intents")).toBeDisabled();
  await page.getByTestId("entity-grid-type-nodes").click(); await page.getByTestId("entity-grid-type-pipes").click(); await expect(draft).toHaveText("0");
  await page.getByTestId("clear-entity-grid-drafts").click(); await expect(draft).toHaveText("TBD");
  await draft.dblclick(); await review.getByRole("textbox").fill("0 mm"); await review.getByRole("button", { name: "Keep draft", exact: true }).click();
  await page.getByTestId("queue-entity-grid-intents").click(); await expect(page.getByTestId("operation-apply-row-editor-intent-1")).toContainText('"unit":"mm"');
  await page.getByTestId("apply-intent-editor-intent-1").click(); await expect(page.getByTestId("operation-apply-summary")).toContainText("2 applied");
  await showModelTree(page); await page.getByTestId("pipe-grid-review-disclosure").click(); await expect(cell).toHaveText("0");
  expect(await currentModelHashThroughVisibleExport(page)).toBe(directHash);
});


for (const reduction of [10, 11]) test(`B4 Pipes unbound mill tolerance ${reduction} rejects exhausted effective wall`, async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info); const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  delete pipe.section_ref; pipe.section.outside_diameter = { value: 100, unit: "mm" }; pipe.section.wall_thickness = { value: 10, unit: "mm" }; pipe.section.mill_tolerance = { value: 0, unit: "mm" };
  await openPipes(page, model); const before = await currentModelHashThroughVisibleExport(page); const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId(`table-cell-${pipe.id}-mill-tolerance`);
  await cell.dblclick(); await table.getByRole("textbox").fill(String(reduction)); await table.getByRole("button", { name: "Apply", exact: true }).click();
  await expect(table.getByRole("alert")).toContainText("Engine rejected"); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  await table.getByRole("button", { name: "Cancel", exact: true }).click(); await expect(cell).toHaveText("0"); expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
});

test("B4 Pipes compact label provenance and material completion retain editor ownership", async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info);
  await page.addInitScript(() => localStorage.setItem("chirality.desktop.ui-preferences.v1", JSON.stringify({ version: 1, density: "compact", tableDrawerPx: 227 })));
  const { model } = await readFixture("precision-origin-base.model.json"); const pipe = model.pipe_segments[0];
  model.materials.push({ ...structuredClone(model.materials[0]), id: "material:B4-compact-choice", label: "Invented choice" });
  await gotoModel(page, model); await page.getByTestId("view-switch-model").click(); await ensureTreeExpanded(page); await page.getByTestId("layout-mode-grid").click();
  await page.getByRole("combobox", { name: "Grid family" }).selectOption("pipes"); const table = page.getByTestId("pipe-engineering-table");
  const label = table.getByTestId(`table-cell-${pipe.id}-label`); await label.dblclick(); const input = table.getByRole("textbox"); await input.fill("Invented pipe label"); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(label).toHaveText("Invented pipe label");
  const later = page.getByRole("button", { name: "Later columns", exact: true }); while (await later.isEnabled()) await later.click();
  const provenance = table.getByTestId(`table-cell-${pipe.id}-provenance`); await provenance.dblclick(); await input.fill("Invented source note");
  const earlier = page.getByRole("button", { name: "Earlier columns", exact: true }); await earlier.click(); await expect(input).toHaveValue("Invented source note");
  while (await later.isEnabled()) await later.click(); await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(provenance).toHaveText("Invented source note");
  const material = table.getByTestId(`table-cell-${pipe.id}-material`); await material.dblclick(); const ref = table.getByRole("combobox"); await ref.fill("material:B4-compact");
  await page.getByRole("option", { name: "material:B4-compact-choice", exact: true }).click(); await expect(ref).toHaveValue("material:B4-compact-choice");
  await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(material).toHaveText("material:B4-compact-choice");
  await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material);
  await material.dblclick(); await ref.fill("material:B4-compact"); await ref.press("Enter"); await expect(material).toHaveText("material:B4-compact-choice");
  await page.getByTestId("workspace-undo").click(); await expect(material).toHaveText(pipe.material);
  await page.getByTestId("workspace-undo").click(); await expect(provenance).toHaveText(pipe.provenance);
});


test("B4 Pipes equivalent explicit-unit edits preserve model and history", async ({ page, browser }, info) => {
  await attachBrowserIdentity(browser, info);
  // Keep the service's default fixture unmodified: routing a replacement model also
  // replaces its fixture comparison basis and cannot exercise the edited-model route.
  await page.goto("/"); await expect(page.getByTestId("desktop-preview-shell")).toBeVisible();
  await page.getByTestId("view-switch-table").click(); await ensureTreeExpanded(page); await page.getByTestId("layout-mode-grid").click();
  await page.getByTestId("entity-grid-type-pipes").click();
  const table = page.getByTestId("pipe-engineering-table"), cell = table.getByTestId("table-cell-pipe:P-100-mill-tolerance");
  await expect(cell).toHaveText("TBD"); await cell.dblclick(); await table.getByRole("textbox").fill("0 mm");
  await table.getByRole("button", { name: "Apply", exact: true }).click(); await expect(cell).toHaveText("0");
  await expect(page.getByTestId("workspace-undo")).toBeEnabled();
  await openWorkspaceSection(page, "project"); await page.getByRole("button", { name: "Save local", exact: true }).click();
  await expect(page.getByTestId("local-project-message")).toContainText("Saved local browser-preview project");
  await page.getByRole("button", { name: "Open local", exact: true }).click();
  await expect(page.getByTestId("local-project-message")).toContainText("Opened local browser-preview project");
  await showModelTree(page); await page.getByTestId("layout-mode-grid").click(); await page.getByTestId("entity-grid-type-pipes").click();
  await expect(cell).toHaveText("0"); await expect(page.getByTestId("workspace-undo")).toBeDisabled(); await expect(page.getByTestId("project-edited")).toHaveCount(0);
  // The authored model retains the default project's two load cases and receives
  // the real browser's blocked result, not bundled or synthetic solved rows.
  await openWorkspaceSection(page, "solve"); await page.getByTestId("run-mechanics-preview").click();
  await expect(page.getByTestId("solve-job-summary")).toContainText("state=completed");
  const resultConsent = page.getByTestId("solve-job-export-link-local-private-intent"); await resultConsent.check();
  const runReceipt = await page.getByTestId("solve-job-export-link").getAttribute("href"); expect(runReceipt).toBeTruthy();
  const packet = JSON.parse(decodeURIComponent(runReceipt!.slice(runReceipt!.indexOf(",") + 1)));
  expect(packet.project_ref).toBe("project:invented-loop-01");
  expect(packet.model_state_ref).toEqual({ object_type: "ModelState", ref: "state:project:invented-loop-01:preview" });
  expect(packet.analysis_status).toContain("MODEL_INCOMPLETE");
  expect(packet.summary).toMatchObject({ job_state: "completed", result_row_count: 0, running: false });
  expect(packet.analysis_run_ref.ref).toBe("run:preview-linear-static-browser-blocked:project-invented-loop-01");
  expect(packet.diagnostics).toEqual(expect.arrayContaining([expect.objectContaining({ code: "BROWSER_SOLVE_BACKEND_REQUIRED_FOR_EDITED_MODEL", affected_refs: ["project:invented-loop-01"] })]));
  await expect(page.getByTestId("readiness-mechanics")).toContainText("MODEL_INCOMPLETE");
  const readiness = await page.getByTestId("readiness-mechanics").textContent();
  await info.attach("actual-blocked-run-receipt", { body: JSON.stringify(packet, null, 2), contentType: "application/json" });
  await showModelTree(page);
  const before = await currentModelHashThroughVisibleExport(page);
  for (const value of ["0 mm", "0.0 mm"]) {
    await cell.dblclick(); await table.getByRole("textbox").fill(value); await table.getByRole("button", { name: "Apply", exact: true }).click();
    await expect(table.getByRole("textbox")).toHaveCount(0); await expect(cell).toBeFocused(); await expect(cell).toHaveText("0");
    await expect(page.getByTestId("workspace-undo")).toBeDisabled(); await expect(page.getByTestId("workspace-redo")).toBeDisabled(); await expect(page.getByTestId("project-edited")).toHaveCount(0);
    expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
    await openWorkspaceSection(page, "solve"); if (!await resultConsent.isChecked()) await resultConsent.check();
    expect(await page.getByTestId("solve-job-export-link").getAttribute("href")).toBe(runReceipt);
    expect(await page.getByTestId("readiness-mechanics").textContent()).toBe(readiness); await showModelTree(page);
  }
  await cell.dblclick(); await table.getByRole("textbox").fill("0 m"); await table.getByRole("button", { name: "Apply", exact: true }).click();
  await expect(table.getByRole("alert")).toContainText("existing unit"); await expect(table.getByRole("textbox")).toHaveValue("0 m");
  await table.getByRole("button", { name: "Cancel", exact: true }).click(); await expect(page.getByTestId("workspace-undo")).toBeDisabled();
  expect(await currentModelHashThroughVisibleExport(page)).toBe(before);
});
