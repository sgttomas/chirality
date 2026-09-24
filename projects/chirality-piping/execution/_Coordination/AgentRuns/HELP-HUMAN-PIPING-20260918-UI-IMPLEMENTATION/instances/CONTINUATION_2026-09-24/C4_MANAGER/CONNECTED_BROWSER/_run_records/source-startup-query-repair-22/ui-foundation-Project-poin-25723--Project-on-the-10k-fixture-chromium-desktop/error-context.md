# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: ui-foundation.spec.ts >> Project pointer click followed by Shift-node preserves the displayed entity range and excludes Project on the 10k fixture
- Location: e2e/ui-foundation.spec.ts:270:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('desktop-preview-shell')
Expected: visible
Timeout: 10000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 10000ms
  - waiting for getByTestId('desktop-preview-shell')

```

```yaml
- text: Loading local SWBPIPE preview fixture.
```

# Test source

```ts
  1   | import { createHash } from "node:crypto";
  2   | import { createReadStream, existsSync } from "node:fs";
  3   | import { readFile } from "node:fs/promises";
  4   | import path from "node:path";
  5   | import { expect, type Browser, type Locator, type Page, type TestInfo } from "@playwright/test";
  6   | import {
  7   |   installInstrumentation,
  8   |   routeModelFixture,
  9   |   settledRafState,
  10  |   treeRowTestId,
  11  | } from "./ui-foundation/benchmark-harness";
  12  | 
  13  | export type AppearanceTheme = "light" | "dark";
  14  | export type AppearanceDensity = "comfortable" | "compact";
  15  | export type ViewportSize = Readonly<{ width: number; height: number }>;
  16  | 
  17  | export const APPEARANCE_THEMES: readonly AppearanceTheme[] = ["light", "dark"];
  18  | export const APPEARANCE_DENSITIES: readonly AppearanceDensity[] = ["comfortable", "compact"];
  19  | export const APPEARANCE_VIEWPORTS: readonly ViewportSize[] = [
  20  |   { width: 1024, height: 768 },
  21  |   { width: 1280, height: 800 },
  22  |   { width: 1440, height: 920 },
  23  | ];
  24  | 
  25  | export async function attachBrowserIdentity(browser: Browser, testInfo: TestInfo): Promise<void> {
  26  |   const session = await browser.newBrowserCDPSession();
  27  |   let cdpVersion: unknown;
  28  |   try {
  29  |     cdpVersion = await session.send("Browser.getVersion");
  30  |   } finally {
  31  |     await session.detach();
  32  |   }
  33  |   const configuredChrome = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH;
  34  |   const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  35  |   const executablePath = configuredChrome && existsSync(configuredChrome)
  36  |     ? configuredChrome
  37  |     : existsSync(macChrome) ? macChrome : null;
  38  |   await testInfo.attach("browser-identity", {
  39  |     body: JSON.stringify({
  40  |       cdpVersion,
  41  |       playwrightBrowserVersion: browser.version(),
  42  |       executablePath,
  43  |       executableSha256: executablePath ? await sha256File(executablePath) : null,
  44  |     }, null, 2),
  45  |     contentType: "application/json",
  46  |   });
  47  | }
  48  | 
  49  | function sha256File(filePath: string): Promise<string> {
  50  |   return new Promise((resolve, reject) => {
  51  |     const digest = createHash("sha256");
  52  |     const stream = createReadStream(filePath);
  53  |     stream.on("data", (chunk) => digest.update(chunk));
  54  |     stream.on("error", reject);
  55  |     stream.on("end", () => resolve(digest.digest("hex")));
  56  |   });
  57  | }
  58  | 
  59  | // Keep the two late writer bindings here. The final source-release intake only
  60  | // has to rebind this small surface if the visible group IDs or measurement
  61  | // labels change; the qualification assertions remain unchanged.
  62  | export const COMMAND_GROUPS = [
  63  |   "Build",
  64  |   "Supports",
  65  |   "Properties",
  66  |   "Loads",
  67  |   "Edit",
  68  |   "Select and View",
  69  |   "Review",
  70  | ] as const;
  71  | 
  72  | export function commandGroupControl(page: Page, group: typeof COMMAND_GROUPS[number]): Locator {
  73  |   const slug = group.toLowerCase().replace(/\s+and\s+/g, "-").replace(/\s+/g, "-");
  74  |   return page.getByTestId(`toolkit-group-${slug}`);
  75  | }
  76  | 
  77  | const fixtureRoot = path.join(import.meta.dirname, "ui-foundation", "fixtures");
  78  | 
  79  | export async function readFixture(name: string): Promise<{ bytes: string; model: any }> {
  80  |   const bytes = await readFile(path.join(fixtureRoot, name), "utf8");
  81  |   return { bytes, model: JSON.parse(bytes) };
  82  | }
  83  | 
  84  | export async function gotoRoutedFixture(
  85  |   page: Page,
  86  |   name = "precision-origin-base.model.json",
  87  |   options: Readonly<{ captureGlobalRaf?: boolean }> = {},
  88  | ): Promise<any> {
  89  |   const fixture = await readFixture(name);
  90  |   await installInstrumentation(page, { captureGlobalRaf: options.captureGlobalRaf === true });
  91  |   await routeModelFixture(page, fixture);
  92  |   await page.goto("/");
> 93  |   await expect(page.getByTestId("desktop-preview-shell")).toBeVisible();
      |                                                           ^ Error: expect(locator).toBeVisible() failed
  94  |   await expect(page.getByTestId("viewport-canvas").locator("canvas")).toHaveCount(1);
  95  |   return fixture.model;
  96  | }
  97  | 
  98  | export async function waitForSettledGlobalRaf(page: Page, timeoutMs = 5_000): Promise<any> {
  99  |   return settledRafState(page, timeoutMs);
  100 | }
  101 | 
  102 | export async function gotoModel(page: Page, model: any): Promise<void> {
  103 |   await installInstrumentation(page, { captureGlobalRaf: false });
  104 |   await routeModelFixture(page, { bytes: JSON.stringify(model) });
  105 |   await page.goto("/");
  106 |   await expect(page.getByTestId("desktop-preview-shell")).toBeVisible();
  107 |   await expect(page.getByTestId("viewport-canvas").locator("canvas")).toHaveCount(1);
  108 | }
  109 | 
  110 | export function typedTreeRow(page: Page, type: string, id: string): Locator {
  111 |   return page.getByTestId(treeRowTestId({ type, id }, "candidate"));
  112 | }
  113 | 
  114 | // Slice B3: "tree" is the table pane (its collapse chevron keeps `toggle-tree`; the pane is a
  115 | // drawer in Model view and below 1280 px, and always open elsewhere) and "inspector" is the
  116 | // docked inspector (the toolbar's Inspector toggle keeps `toggle-inspector`; it acts in Both view).
  117 | export async function ensureRail(page: Page, side: "tree" | "inspector", open: boolean): Promise<void> {
  118 |   const toggle = page.getByTestId(side === "tree" ? "toggle-tree" : "toggle-inspector");
  119 |   const expected = String(open);
  120 |   if (await toggle.getAttribute("aria-expanded") !== expected) {
  121 |     await activateWithKeyboard(page, toggle);
  122 |   }
  123 |   await expect(toggle).toHaveAttribute("aria-expanded", expected);
  124 | }
  125 | 
  126 | /** The model tree is the Model stage's first tab. */
  127 | export async function showModelTree(page: Page): Promise<void> {
  128 |   const host = page.getByTestId("shell-tree-host");
  129 |   // An open page lies over the tree without hiding it from the layout: close it first.
  130 |   const close = page.getByTestId("workspace-dock-close");
  131 |   if (await close.isVisible()) await activateWithKeyboard(page, close);
  132 |   if (!await host.isVisible()) {
  133 |     const stage = page.getByTestId("rail-stage-model");
  134 |     if (await stage.getAttribute("aria-current") !== "page") await activateWithKeyboard(page, stage);
  135 |     const tab = page.getByTestId("stage-tab-model-tree");
  136 |     if (await tab.getAttribute("aria-pressed") !== "true") await activateWithKeyboard(page, tab);
  137 |     await ensureRail(page, "tree", true);
  138 |   }
  139 |   await expect(host).toBeVisible();
  140 | }
  141 | 
  142 | export async function revealTreeRow(page: Page, type: string, id: string): Promise<Locator> {
  143 |   await showModelTree(page);
  144 |   await ensureRail(page, "tree", true);
  145 |   const filter = page.getByTestId("model-tree-filter-input");
  146 |   await filter.fill(id);
  147 |   const row = typedTreeRow(page, type, id);
  148 |   await expect(row).toBeVisible();
  149 |   return row;
  150 | }
  151 | 
  152 | export async function selectTreeRow(
  153 |   page: Page,
  154 |   type: string,
  155 |   id: string,
  156 |   modifiers: Readonly<{ shift?: boolean; toggle?: boolean }> = {},
  157 | ): Promise<Locator> {
  158 |   const row = await revealTreeRow(page, type, id);
  159 |   await row.click({
  160 |     modifiers: [
  161 |       ...(modifiers.shift ? ["Shift" as const] : []),
  162 |       ...(modifiers.toggle ? [process.platform === "darwin" ? "Meta" as const : "Control" as const] : []),
  163 |     ],
  164 |   });
  165 |   return row;
  166 | }
  167 | 
  168 | export async function clearTreeFilter(page: Page): Promise<void> {
  169 |   const clear = page.getByTestId("clear-model-tree-filter");
  170 |   if (await clear.isEnabled()) await activateWithKeyboard(page, clear);
  171 |   await expect(page.getByTestId("model-tree-filter-input")).toHaveValue("");
  172 | }
  173 | 
  174 | export async function activateWithKeyboard(page: Page, control: Locator): Promise<void> {
  175 |   await control.focus();
  176 |   await expect(control).toBeFocused();
  177 |   await page.keyboard.press("Enter");
  178 | }
  179 | 
  180 | export async function setAppearance(
  181 |   page: Page,
  182 |   theme: AppearanceTheme,
  183 |   density: AppearanceDensity,
  184 | ): Promise<void> {
  185 |   // Slice B3: the two labelled selects live in the toolbar's Appearance disclosure.
  186 |   const appearance = page.getByTestId("toolbar-appearance");
  187 |   if (await appearance.getAttribute("open") === null) await appearance.locator("summary").click();
  188 |   await page.getByLabel("Appearance theme").selectOption(theme);
  189 |   await page.getByLabel("Workspace density").selectOption(density);
  190 |   await appearance.locator("summary").click();
  191 |   await expect(page.getByLabel("Appearance theme")).toBeHidden();
  192 |   const shell = page.getByTestId("desktop-preview-shell");
  193 |   await expect(shell).toHaveAttribute("data-theme", theme);
```