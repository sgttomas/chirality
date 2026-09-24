import { fireEvent, render, within } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { loadPreviewModel } from "../../services/previewService";
import { modelIndexFor } from "../workspace/modelIndex";
import { PipeViewport } from "./PipeViewport";

const emptySelection = Object.freeze({ orderedKeys: [], primaryKey: null, rangeAnchorKey: null,
  focusKey: null, preparationEpoch: 0 });

describe("viewport label mode integration", () => {
  it("shares click/L cycling, guards edits and modifiers, retains mode across edits, resets at a project generation", async () => {
    const model = await loadPreviewModel();
    const props = { model, modelIndex: modelIndexFor(model, 1, 0), armedCreationTool: "node" as const,
      selection: { type: "node" as const, id: model.nodes[0].id }, selectionState: emptySelection,
      onSelect: vi.fn(() => emptySelection) };
    const view = render(<PipeViewport {...props} />);
    const ui = within(view.container);
    const toggle = ui.getByTestId("toggle-viewport-labels");
    const canvas = ui.getByTestId("viewport-canvas");
    expect(toggle).toHaveAttribute("data-label-mode", "Budget");
    fireEvent.click(toggle);
    expect(toggle).toHaveAttribute("data-label-mode", "All");
    fireEvent.keyDown(canvas, { key: "l" });
    expect(toggle).toHaveAttribute("data-label-mode", "Off");
    for (const modifier of ["ctrlKey", "metaKey", "altKey", "shiftKey", "repeat"]) {
      fireEvent.keyDown(canvas, { key: "l", [modifier]: true });
      expect(toggle).toHaveAttribute("data-label-mode", "Off");
    }
    fireEvent.keyDown(ui.getByTestId("viewport-create-node-id"), { key: "l" });
    expect(toggle).toHaveAttribute("data-label-mode", "Off");
    view.rerender(<PipeViewport {...props} modelIndex={modelIndexFor(model, 1, 1)} />);
    expect(toggle).toHaveAttribute("data-label-mode", "Off");
    view.rerender(<PipeViewport {...props} modelIndex={modelIndexFor(model, 2, 0)} />);
    expect(toggle).toHaveAttribute("data-label-mode", "Budget");
    expect(props.onSelect).not.toHaveBeenCalled();
  });
});
