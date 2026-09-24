import { describe, expect, it } from "vitest";
import type { PreviewModel } from "../../types";
import { buildModelIndex } from "../workspace/modelIndex";
import { entityKey } from "../workspace/selectionState";
import { layoutViewportLabels, nominalLabelBudget, type LabelPolicyInput } from "./labelPolicy";
import { labelRectsOverlap, type MeasuredLabel } from "./labelPlacement";

const key = (id: string) => entityKey({ type: "node", id });
function fixture(count = 5): PreviewModel {
  return {
    schema_version: "test", document_kind: "test", data_boundary: {},
    project: { id: "project", name: "Labels", description: "", units: { length: "m" } },
    analysis_status: { mechanics: "TBD", rule_check: "TBD", professional_acceptance: "TBD" },
    nodes: Array.from({ length: count }, (_, i) => ({ id: `${i}`, label: `Node ${i}`,
      position: { x: i, y: 0, z: 0 }, provenance: "test" })),
    pipe_segments: [], supports: [], components: [], load_cases: [], diagnostics: []
  };
}
function input(count = 5): LabelPolicyInput {
  return { mode: "Budget", width: 603, height: 828, primaryKey: null, hoverKey: null,
    currentRowNodeKey: null, selectedKeys: [], hiddenKeys: new Set(), pickTargets: [],
    measurements: new Map(Array.from({ length: count }, (_, i) => [key(`${i}`), {
      x: 10 + (i % 20) * 25, y: 20 + Math.floor(i / 20) * 25,
      width: 10, height: 8, inFrustum: true
    }])) };
}

describe("viewport label policy", () => {
  it("uses drawable CSS area without a DPR input and tolerates invalid extents", () => {
    expect(nominalLabelBudget(603, 828)).toBe(138);
    expect(nominalLabelBudget(1000, 828)).toBe(230);
    expect(nominalLabelBudget(59.99, 60)).toBe(0);
    for (const width of [-1, NaN, Infinity]) expect(nominalLabelBudget(width, 828)).toBe(0);
  });

  it("deduplicates roles, retains selection order and keeps current row independent in Off", () => {
    const index = buildModelIndex(fixture(), 1, 1);
    const state = { ...input(), mode: "Off" as const, primaryKey: key("2"), hoverKey: key("1"),
      currentRowNodeKey: key("3"), selectedKeys: [key("4"), key("1"), key("2"), key("4")] };
    const result = layoutViewportLabels(index, state);
    expect(result.rendered.map(({ key: k, role }) => [k, role])).toEqual([
      [key("2"), "primary"], [key("1"), "hover"], [key("3"), "current-row"], [key("4"), "selected"]
    ]);
    expect(result.suppressed).toEqual([{ key: key("0"), role: "ordinary", reason: "mode" }]);
    expect(layoutViewportLabels(index, { ...state, currentRowNodeKey: key("0") }).rendered[2].key).toBe(key("0"));
    expect(state.primaryKey).toBe(key("2"));
  });

  it("allows 139 context labels over B=138 without the legacy 80 truncation", () => {
    const index = buildModelIndex(fixture(141), 1, 1);
    const result = layoutViewportLabels(index, { ...input(141),
      selectedKeys: Array.from({ length: 139 }, (_, i) => key(`${i}`)) });
    expect(result.counts).toEqual({ context: 139, ordinary: 0, total: 139, contextOverflow: 1,
      suppressed: 2, ineligible: 0, unplaced: 0 });
    for (let i = 0; i < result.rendered.length; i++) {
      for (let j = i + 1; j < result.rendered.length; j++) {
        expect(labelRectsOverlap(result.rendered[i].rect, result.rendered[j].rect)).toBe(false);
      }
    }
  });

  it("fills B minus successful context even when 19 of 139 context requests fail", () => {
    const index = buildModelIndex(fixture(169), 1, 1);
    const state = input(169);
    const measurements = new Map(state.measurements);
    for (let i = 0; i < 19; i++) measurements.set(key(`${i}`), {
      ...measurements.get(key(`${i}`))!, width: 604
    });
    const result = layoutViewportLabels(index, { ...state, measurements,
      selectedKeys: Array.from({ length: 139 }, (_, i) => key(`${i}`)) });
    expect(result.counts).toEqual({ context: 120, ordinary: 18, total: 138,
      contextOverflow: 0, suppressed: 12, ineligible: 0, unplaced: 19 });
    expect(result.unplaced.map((item) => item.key)).toEqual(
      Array.from({ length: 19 }, (_, i) => key(`${i}`)));
  });

  it("allocates only successful context and ordinary placements against nominal slots", () => {
    const index = buildModelIndex(fixture(4), 1, 1);
    const measurements = new Map<string, MeasuredLabel>([
      [key("0"), { x: 10, y: 10, width: 200, height: 200, inFrustum: true }],
      [key("1"), { x: 30, y: 30, width: 4, height: 4, inFrustum: true }],
      [key("2"), { x: 50, y: 50, width: 4, height: 4, inFrustum: true }]
    ]);
    const state = { ...input(4), width: 60, height: 60, primaryKey: key("0"),
      cameraTarget: { x: 1, y: 0, z: 0 }, measurements: new Map(
        [...measurements].map(([id, value]) => [id as ReturnType<typeof key>, value])) };
    const result = layoutViewportLabels(index, state);
    expect(result.unplaced).toEqual([{ key: key("0"), role: "primary", reasons: ["containment"] }]);
    expect(result.rendered.map((item) => item.key)).toEqual([key("1")]);
    expect(result.counts.ordinary).toBe(1);
    expect(result.suppressed).toHaveLength(2);
    const all = layoutViewportLabels(index, { ...state, mode: "All" });
    expect(all.rendered).toHaveLength(2);
    expect(all.suppressed).toHaveLength(0);
    expect(all.unplaced).toContainEqual({ key: key("3"), role: "ordinary", reasons: ["missing-measurement"] });
  });

  it("distinguishes Hide, unsupported identities and invalid geometry from placement omissions", () => {
    const model = fixture();
    model.nodes[1].position.x = NaN;
    const index = buildModelIndex(model, 1, 1);
    const project = entityKey({ type: "project", id: "project" });
    const state = { ...input(), primaryKey: key("0"), hoverKey: key("1"),
      selectedKeys: [project], hiddenKeys: new Set([key("0")]) };
    const result = layoutViewportLabels(index, state);
    expect(result.ineligible).toEqual([
      { key: key("0"), role: "primary", reason: "hidden" },
      { key: key("1"), role: "hover", reason: "geometry" },
      { key: project, role: "selected", reason: "unsupported" }
    ]);
    expect(result.rendered.every((item) => !state.hiddenKeys.has(item.key))).toBe(true);
  });

  it("retains supported typed identities sharing a raw id, with Hide winning in every mode", () => {
    const model = fixture(2);
    const pipe = entityKey({ type: "pipe", id: "0" });
    const support = entityKey({ type: "support", id: "0" });
    const component = entityKey({ type: "component", id: "0" });
    model.pipe_segments = [{ id: "0", label: "Pipe", from: "0", to: "1",
      section: {}, material: "m", provenance: "test" }];
    model.supports = [{ id: "0", label: "Support", node: "0", restraints: [], provenance: "test" }];
    model.components = [{ id: "0", label: "Component", node: "0", kind: "generic", provenance: "test" }];
    const index = buildModelIndex(model, 1, 1);
    const state = input(2);
    const measurements = new Map(state.measurements);
    for (const [i, id] of [pipe, support, component].entries()) measurements.set(id, {
      x: 100 + i * 50, y: 100, width: 10, height: 8, inFrustum: true
    });
    for (const mode of ["Budget", "All", "Off"] as const) {
      const request = { ...state, mode, measurements, primaryKey: key("0"), hoverKey: pipe,
        currentRowNodeKey: support, selectedKeys: [support, component, pipe, key("0")] };
      const visible = layoutViewportLabels(index, request);
      expect(visible.rendered.filter((item) => item.role !== "ordinary").map((item) => item.key))
        .toEqual([key("0"), pipe, support, component]);
      expect(visible.ineligible).toEqual([{ key: support, role: "current-row", reason: "not-node" }]);
      expect(visible.rendered.find((item) => item.key === support)?.role).toBe("selected");
      const hidden = layoutViewportLabels(index, { ...request, hiddenKeys: new Set([pipe, support, component]) });
      expect(hidden.rendered.some((item) => [pipe, support, component].includes(item.key))).toBe(false);
      expect(hidden.rendered.some((item) => item.key === key("0"))).toBe(true);
      expect(hidden.ineligible.filter((item) => item.reason === "hidden").map((item) => item.key))
        .toEqual([pipe, support, component]);
    }
  });

  it("keeps distance/typed identity ordinary ordering deterministic without mutating inputs", () => {
    const index = buildModelIndex(fixture(3), 1, 1);
    const state = { ...input(3), cameraTarget: { x: 1, y: 0, z: 0 } };
    const before = [...state.measurements];
    const first = layoutViewportLabels(index, state);
    expect(first.rendered.map((item) => item.key)).toEqual([key("1"), key("0"), key("2")]);
    expect(layoutViewportLabels(index, state)).toEqual(first);
    expect([...state.measurements]).toEqual(before);
  });
});
