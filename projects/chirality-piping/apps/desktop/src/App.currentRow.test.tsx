import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { App } from "./App";
import { entityKey } from "./features/workspace/selectionState";

const observed = vi.hoisted(() => ({ props: null as Record<string, unknown> | null }));
vi.mock("./features/viewport/PipeViewport", async (importOriginal) => {
  const actual = await importOriginal<typeof import("./features/viewport/PipeViewport")>();
  return { ...actual, PipeViewport: (props: Record<string, unknown>) => { observed.props = props; return <div data-testid="viewport-prop-witness" />; } };
});

// This witnesses the real table→ModelTree→App connection, not renderer visibility.
describe("App current-row connection", () => {
  it("passes review B separately from primary A and clears on return to dormant fields", async () => {
    render(<App />); await screen.findByTestId("desktop-preview-shell");
    fireEvent.click(screen.getByTestId("view-switch-table"));
    expect(screen.getByTestId("modeling-workspace")).toHaveAttribute("data-view", "table");
    fireEvent.click(screen.getByTestId("layout-mode-grid"));
    expect(observed.props?.currentRowNodeKey).toBeNull();
    fireEvent.click(screen.getByTestId("table-cell-node:N-100-x"));
    expect(observed.props?.currentRowNodeKey).toBe(entityKey({ type: "node", id: "node:N-100" }));
    const primary = observed.props?.selection;
    expect(primary).toEqual({ type: "node", id: "node:N-100" });
    fireEvent.click(screen.getByTestId("node-grid-review-disclosure"));
    expect(observed.props?.currentRowNodeKey).toBeNull();
    const cells = screen.getAllByTestId(/^review-cell-.*-x$/);
    const other = cells.find((cell) => cell.dataset.rowKey !== entityKey({ type: "node", id: "node:N-100" }))!;
    fireEvent.pointerDown(other); fireEvent.click(other);
    await waitFor(() => expect(observed.props?.currentRowNodeKey).toBe(other.dataset.rowKey));
    expect(observed.props?.selection).toEqual(primary);
    expect(screen.getByTestId("workspace-undo")).toBeDisabled();
    fireEvent.click(screen.getByTestId("node-grid-review-disclosure"));
    expect(observed.props?.currentRowNodeKey).toBeNull();
  });
});
