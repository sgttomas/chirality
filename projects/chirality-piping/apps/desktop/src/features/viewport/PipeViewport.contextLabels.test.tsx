import { act, fireEvent, render, within } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import * as THREE from "three";
import { loadPreviewModel } from "../../services/previewService";
import { modelIndexFor } from "../workspace/modelIndex";
import { entityKey } from "../workspace/selectionState";
import { PipeViewport } from "./PipeViewport";
import { ViewportResource } from "./viewportResource";

// Simulated lifecycle: actual component, resource, event bindings, Three geometry/math,
// label policy and diagnostics; only GPU rendering and browser layout are inert fixtures.
// This is not evidence of real WebGL context restoration or native rendering.
vi.mock("three", async (importOriginal) => {
  const actual = await importOriginal<typeof import("three")>();
  class InertRenderer {
    domElement = document.createElement("canvas");
    autoClear = true;
    info = { memory: { geometries: 0, textures: 0 }, render: { calls: 0, triangles: 0, points: 0, lines: 0 } };
    renderLists = { dispose: vi.fn() };
    private ratio = 1;
    private viewport = new actual.Vector4();
    private scissor = new actual.Vector4();
    private scissorTest = false;
    setPixelRatio(ratio: number) { this.ratio = ratio; }
    getPixelRatio() { return this.ratio; }
    setSize(width: number, height: number) { this.domElement.width = width; this.domElement.height = height; }
    getDrawingBufferSize(target: THREE.Vector2) { return target.set(this.domElement.width, this.domElement.height); }
    setViewport(x: number | THREE.Vector4, y?: number, width?: number, height?: number) {
      if (typeof x === "number") this.viewport.set(x, y!, width!, height!); else this.viewport.copy(x);
    }
    getViewport(target: THREE.Vector4) { return target.copy(this.viewport); }
    setScissor(x: number | THREE.Vector4, y?: number, width?: number, height?: number) {
      if (typeof x === "number") this.scissor.set(x, y!, width!, height!); else this.scissor.copy(x);
    }
    getScissor(target: THREE.Vector4) { return target.copy(this.scissor); }
    setScissorTest(value: boolean) { this.scissorTest = value; }
    getScissorTest() { return this.scissorTest; }
    clearDepth() {}
    render(scene: THREE.Scene, camera: THREE.Camera) { scene.updateMatrixWorld(); camera.updateMatrixWorld(); }
    dispose() {}
    forceContextLoss() {}
  }
  return { ...actual, WebGLRenderer: InertRenderer };
});

afterEach(() => { vi.restoreAllMocks(); vi.unstubAllGlobals(); });

describe("applied labels across context loss and restoration", () => {
  it("retires plates and applied diagnostics synchronously, restores only with projection, then releases ownership", async () => {
    const frames = new Map<number, FrameRequestCallback>();
    let sequence = 0;
    vi.stubGlobal("requestAnimationFrame", (callback: FrameRequestCallback) => { frames.set(++sequence, callback); return sequence; });
    vi.stubGlobal("cancelAnimationFrame", (handle: number) => frames.delete(handle));
    vi.stubGlobal("ResizeObserver", class { observe() {} disconnect() {} });
    vi.spyOn(HTMLCanvasElement.prototype, "getContext").mockReturnValue(null);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(800);
    vi.spyOn(HTMLElement.prototype, "clientHeight", "get").mockReturnValue(600);
    vi.spyOn(HTMLElement.prototype, "getBoundingClientRect").mockImplementation(function (this: HTMLElement) {
      const plate = this.classList.contains("viewport-select-target");
      return new DOMRect(10 + (plate ? parseFloat(this.style.left) || 0 : 0),
        20 + (plate ? parseFloat(this.style.top) || 0 : 0), plate ? 58 : 800, plate ? 26 : 600);
    });
    const flushFrames = () => {
      for (let turn = 0; turn < 5 && frames.size; turn++) {
        const pending = [...frames]; frames.clear();
        for (const [, callback] of pending) callback(performance.now());
      }
    };
    const readLabels = () => {
      const snapshot = globalThis.__openPipeStressUiDiagnosticsV1.readCurrent();
      if ("status" in snapshot.viewport) throw new Error("Expected committed viewport diagnostics");
      return snapshot.viewport.labels;
    };
    let resource: ViewportResource | null = null;
    const unavailableUpdates: Array<{ placed: number; rendered: number; status: string | undefined }> = [];
    const originalUpdater = ViewportResource.prototype.setLabelUpdater;
    vi.spyOn(ViewportResource.prototype, "setLabelUpdater").mockImplementation(function (this: ViewportResource, updater) {
      resource = this;
      originalUpdater.call(this, updater === null ? null : () => {
        updater();
        if (!this.projectionAvailable) {
          const labels = readLabels();
          unavailableUpdates.push({ placed: document.querySelectorAll('[data-label-placed="true"]').length,
            rendered: labels.renderedCount, status: labels.placementStatus });
        }
      });
    });
    const loaded = await loadPreviewModel();
    const model = { ...loaded, nodes: [{ ...loaded.nodes[0], position: { x: 0, y: 0, z: 0 } },
      { ...loaded.nodes[0], id: "node:omitted-a", position: { x: -2, y: 0, z: 0 } },
      { ...loaded.nodes[0], id: "node:omitted-b", position: { x: 2, y: 0, z: 0 } }],
      pipe_segments: [], supports: [], components: [], load_cases: [], combinations: [], diagnostics: [] };
    const index = modelIndexFor(model, 42, 1);
    const selection = { type: "node" as const, id: model.nodes[0].id };
    const key = entityKey(selection);
    const selected = { orderedKeys: [key], primaryKey: key, rangeAnchorKey: key, focusKey: key, preparationEpoch: 0 };
    const view = render(<PipeViewport model={model} modelIndex={index} selection={selection} selectionState={selected}
      onSelect={() => selected} assignment={{ status: "committed", generation: 1, indexGeneration: index.generation,
        identityHash: "test-context", startedAt: 0, committedAt: 1 }} />);
    await act(async () => { flushFrames(); });
    const ui = within(view.container);
    fireEvent.click(ui.getByTestId("toggle-viewport-labels"));
    fireEvent.click(ui.getByTestId("toggle-viewport-labels"));
    await act(async () => { flushFrames(); });
    const disclosure = () => ui.getByTestId("viewport-label-omissions") as HTMLDetailsElement;
    const toggleDisclosure = (open: boolean) => act(() => {
      disclosure().open = open;
      fireEvent(disclosure(), new Event("toggle"));
    });
    const omissions = readLabels();
    const expectedRows = [...(omissions.suppressed ?? []).map(item => `${item.key}: ${item.reason}`),
      ...(omissions.unplaced ?? []).map(item => `${item.key}: ${item.reasons.join(", ")}`)];
    expect(expectedRows).toHaveLength(2);
    expect(disclosure().open).toBe(false);
    expect(disclosure().querySelectorAll("li")).toHaveLength(0);
    toggleDisclosure(true);
    expect([...disclosure().querySelectorAll("li")].map(row => row.textContent)).toEqual(expectedRows);
    expect(readLabels()).toEqual(omissions);
    fireEvent.click(ui.getByTestId("toggle-viewport-labels")); // Off → Budget while open
    const updatedOmissions = readLabels();
    expect(disclosure().open).toBe(true);
    expect([...disclosure().querySelectorAll("li")].map(row => row.textContent)).toEqual([
      ...(updatedOmissions.suppressed ?? []).map(item => `${item.key}: ${item.reason}`),
      ...(updatedOmissions.unplaced ?? []).map(item => `${item.key}: ${item.reasons.join(", ")}`)
    ]);
    fireEvent.click(ui.getByTestId("toggle-viewport-labels")); // Budget → All
    fireEvent.click(ui.getByTestId("toggle-viewport-labels")); // All → Off
    expect([...disclosure().querySelectorAll("li")].map(row => row.textContent)).toEqual(expectedRows);
    toggleDisclosure(false);
    expect(disclosure().querySelectorAll("li")).toHaveLength(0);
    expect(readLabels()).toEqual(omissions);
    toggleDisclosure(true);
    const plate = ui.getByTestId(`viewport-select-${selection.id}`);
    const host = ui.getByTestId("viewport-canvas");
    const canvas = host.querySelector("canvas")!;
    expect(canvas).not.toBeNull();
    expect(plate).toHaveAttribute("data-label-placed", "true");
    expect(plate).toHaveAttribute("aria-hidden", "false");
    expect(plate.tabIndex).toBe(0);
    expect(readLabels()).toMatchObject({ placementStatus: "applied", renderedCount: 1 });
    plate.focus();
    expect(plate).toHaveFocus();
    // Keep pending work so pause's RAF-count notification is part of the exercised path.
    (resource as unknown as ViewportResource).invalidate();
    const loss = new Event("webglcontextlost", { cancelable: true });
    act(() => {
      canvas.dispatchEvent(loss);
      // These assertions precede React's act commit and any subsequent frame.
      expect(loss.defaultPrevented).toBe(true);
      expect(plate).toHaveAttribute("data-label-placed", "false");
      expect(plate).toHaveAttribute("aria-hidden", "true");
      expect(plate.tabIndex).toBe(-1);
      expect(host).toHaveFocus();
      expect(ui.getByTestId("viewport-label-omissions")).not.toBeVisible();
      expect(readLabels()).toMatchObject({ placementStatus: "unavailable", renderedCount: 0,
        contextCount: 0, ordinaryCount: 0, suppressed: [], ineligible: [], unplaced: [] });
      expect(readLabels().projectionError).toBeTruthy();
    });
    expect(ui.queryByTestId("viewport-label-omissions")).toBeNull();
    expect(frames.size).toBe(0);
    act(() => { canvas.dispatchEvent(new Event("webglcontextrestored")); });
    await act(async () => { flushFrames(); });
    expect(unavailableUpdates.length).toBeGreaterThanOrEqual(2); // loss and restoring
    for (const update of unavailableUpdates) expect(update).toEqual({ placed: 0, rendered: 0, status: "unavailable" });
    expect(plate).toHaveAttribute("data-label-placed", "true");
    expect(plate).toHaveAttribute("aria-hidden", "false");
    expect(plate.tabIndex).toBe(0);
    expect(readLabels()).toMatchObject({ placementStatus: "applied", renderedCount: 1, projectionError: null });
    expect(disclosure().open).toBe(false);
    expect(disclosure().querySelectorAll("li")).toHaveLength(0);
    toggleDisclosure(true);
    const replacement = { ...model, nodes: model.nodes.map((node, i) => i === 0 ? node : { ...node, id: `${node.id}-replacement` }) };
    const replacementIndex = modelIndexFor(replacement, 43, 0);
    view.rerender(<PipeViewport model={replacement} modelIndex={replacementIndex} selection={selection} selectionState={selected}
      onSelect={() => selected} assignment={{ status: "committed", generation: 2, indexGeneration: replacementIndex.generation,
        identityHash: "test-replacement", startedAt: 2, committedAt: 3 }} />);
    await act(async () => { flushFrames(); });
    expect(disclosure().open).toBe(false);
    expect(disclosure().querySelectorAll("li")).toHaveLength(0);
    expect(disclosure().textContent).not.toContain("node:omitted-a:");
    fireEvent.click(ui.getByTestId("toggle-viewport-labels")); // replacement Budget → All
    fireEvent.click(ui.getByTestId("toggle-viewport-labels")); // All → Off
    toggleDisclosure(true);
    const replacementOmissions = readLabels();
    const replacementRows = [...(replacementOmissions.suppressed ?? []).map(item => `${item.key}: ${item.reason}`),
      ...(replacementOmissions.unplaced ?? []).map(item => `${item.key}: ${item.reasons.join(", ")}`)];
    expect(replacementRows).toHaveLength(2);
    expect([...disclosure().querySelectorAll("li")].map(row => row.textContent)).toEqual(replacementRows);
    for (const oldRow of expectedRows) expect(replacementRows).not.toContain(oldRow);
    const owner = resource as unknown as ViewportResource;
    view.unmount();
    expect(frames.size).toBe(0);
    expect(owner.ownershipSnapshot.live).toMatchObject({ controls: 0, eventBindings: 0, resizeObservers: 0 });
    expect(owner.projectionAvailable).toBe(false);
    const afterUnmount = unavailableUpdates.length;
    canvas.dispatchEvent(new Event("webglcontextlost", { cancelable: true }));
    canvas.dispatchEvent(new Event("webglcontextrestored"));
    expect(unavailableUpdates).toHaveLength(afterUnmount);
  });
});
