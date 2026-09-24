import { act, renderHook } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { useCurrentRowPresentation } from "./currentRowPresentation";
import { entityKey } from "./selectionState";
import { buildModelIndex } from "./modelIndex";
import type { PreviewModel } from "../../types";

const a = entityKey({ type: "node", id: "a" }), b = entityKey({ type: "node", id: "b" });
const pipe = entityKey({ type: "pipe", id: "p" });
const invalid = entityKey({ type: "node", id: "invalid" });
function index(keys = [a, b]) {
  const model: PreviewModel = {
    schema_version: "test", document_kind: "test", data_boundary: {},
    project: { id: "same", name: "Current row", description: "", units: { length: "m" } },
    analysis_status: { mechanics: "TBD", rule_check: "TBD", professional_acceptance: "TBD" },
    materials: [], sections: [],
    nodes: [
      { id: "a", label: "A", position: { x: 0, y: 0, z: 0 }, provenance: "test" },
      { id: "b", label: "B", position: { x: 1, y: 0, z: 0 }, provenance: "test" }
    ].filter((node) => keys.includes(entityKey({ type: "node", id: node.id }))).concat([
      { id: "invalid", label: "Invalid", position: { x: NaN, y: 0, z: 0 }, provenance: "test" }
    ]),
    pipe_segments: [{ id: "p", label: "Pipe", from: "a", to: "b", section: {}, material: "m", provenance: "test" }],
    supports: [], components: [], load_cases: [], diagnostics: []
  };
  return buildModelIndex(model, 1, 1);
}
describe("current-row presentation ownership", () => {
  it("ignores a late clear from another source and old callbacks after same-ID replacement", () => {
    const { result, rerender } = renderHook(({ generation, modelIndex }) => useCurrentRowPresentation(generation, modelIndex), { initialProps: { generation: '["same",1]', modelIndex: index() } });
    const publish = result.current.publishCurrentRow;
    act(() => publish({ source: "node-review", generation: '["same",1]', rowKey: b }));
    expect(result.current.currentRowNodeKey).toBe(b);
    act(() => publish({ source: "node-fields", generation: '["same",1]', rowKey: a }));
    act(() => publish({ source: "node-review", generation: '["same",1]', rowKey: null }));
    expect(result.current.currentRowNodeKey).toBe(a);
    rerender({ generation: '["same",2]', modelIndex: index() });
    expect(result.current.currentRowNodeKey).toBeNull();
    act(() => publish({ source: "node-review", generation: '["same",2]', rowKey: b }));
    act(() => publish({ source: "node-fields", generation: '["same",1]', rowKey: a }));
    expect(result.current.currentRowNodeKey).toBe(b);
    rerender({ generation: '["same",2]', modelIndex: index([a]) });
    expect(result.current.currentRowNodeKey).toBeNull();
    act(() => publish({ source: "node-review", generation: '["same",2]', rowKey: b }));
    expect(result.current.currentRowNodeKey).toBeNull();
    expect(index().entities.get(pipe)?.ref.type).toBe("pipe");
    expect(index().entities.has(invalid)).toBe(true);
    expect(index().invalidGeometry.has(invalid)).toBe(true);
    act(() => publish({ source: "node-review", generation: '["same",2]', rowKey: invalid }));
    expect(result.current.currentRowNodeKey).toBeNull();
    act(() => publish({ source: "node-review", generation: '["same",2]', rowKey: pipe }));
    expect(result.current.currentRowNodeKey).toBeNull();
    rerender({ generation: '["same",2]', modelIndex: index() });
    expect(result.current.currentRowNodeKey).toBeNull();
  });
});
