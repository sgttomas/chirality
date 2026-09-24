import { describe, expect, it, vi } from "vitest";
import { LabelCollisionIndex } from "./labelCollisionIndex";
import { labelRectsOverlap, placeMeasuredLabel, type MeasuredLabel } from "./labelPlacement";

const plate: MeasuredLabel = { x: 50, y: 50, width: 34, height: 16, inFrustum: true };
const canvas = { width: 200, height: 160 };
const entireCanvas = { left: 0, top: 0, right: 200, bottom: 160 };

describe("measured label placement", () => {
  it("revalidates a preferred center against current dimensions, bounds and obstacles", () => {
    const center = { x: 100, y: 100 };
    const preferredBox = { left: 83, right: 117, top: 92, bottom: 108 };
    expect(placeMeasuredLabel(plate, canvas, [], [], center).rect).toEqual(preferredBox);
    expect(placeMeasuredLabel({ ...plate, width: 40, height: 20 }, canvas, [], [], center).rect)
      .toEqual({ left: 80, right: 120, top: 90, bottom: 110 });
    const normal = placeMeasuredLabel(plate, canvas, [], []);
    for (const invalid of [{ x: NaN, y: 100 }, { x: 100, y: Infinity }, { x: -1, y: 100 }, { x: 200, y: 100 }]) {
      expect(placeMeasuredLabel(plate, canvas, [], [], invalid)).toEqual(normal);
    }
    const resized = { width: 90, height: 90 };
    expect(placeMeasuredLabel(plate, resized, [], [], center)).toEqual(placeMeasuredLabel(plate, resized, [], []));
    // The center fits, but the changed measured width invalidates its box.
    const wide = { ...plate, width: 60 };
    expect(placeMeasuredLabel(wide, canvas, [], [], { x: 20, y: 100 })).toEqual(placeMeasuredLabel(wide, canvas, [], []));
    for (const [occupied, picking] of [[[preferredBox], []], [[], [preferredBox]]]) {
      const fallback = placeMeasuredLabel(plate, canvas, occupied, picking, center);
      expect(fallback.rect).not.toBeNull();
      expect(labelRectsOverlap(fallback.rect!, preferredBox)).toBe(false);
    }
    expect(placeMeasuredLabel({ ...plate, inFrustum: false }, canvas, [], [], center).reasons).toEqual(["outside-frustum"]);
  });

  it("keeps at most 24 distinct attempts with both novel and duplicate preferred centers", () => {
    const overlap = vi.spyOn(LabelCollisionIndex.prototype, "overlaps").mockReturnValue(true);
    try {
      for (const center of [{ x: 100, y: 100 }, { x: 71, y: 38 }]) {
        overlap.mockClear();
        expect(placeMeasuredLabel(plate, canvas, [], [], center).rect).toBeNull();
        // One occupied and one picking query for each candidate, including failures.
        expect(overlap).toHaveBeenCalledTimes(48);
        const boxes = overlap.mock.calls.filter((_, i) => i % 2 === 0).map(([box]) => JSON.stringify(box));
        expect(new Set(boxes).size).toBe(24);
      }
    } finally { overlap.mockRestore(); }
  });

  it("uses actual plate dimensions and protects supplied pick rectangles including its own anchor", () => {
    const target = { left: 44, top: 44, right: 70, bottom: 70 };
    const result = placeMeasuredLabel(plate, canvas, [], [target]);
    expect(result.rect).not.toBeNull();
    const rect = result.rect!;
    expect(rect.right - rect.left).toBe(34);
    expect(rect.bottom - rect.top).toBe(16);
    expect(labelRectsOverlap(rect, target)).toBe(false);
    expect(rect.left).toBeGreaterThanOrEqual(0);
    expect(rect.top).toBeGreaterThanOrEqual(0);
    expect(rect.right).toBeLessThanOrEqual(canvas.width);
    expect(rect.bottom).toBeLessThanOrEqual(canvas.height);
    expect(placeMeasuredLabel(plate, canvas, [], [target])).toEqual(result);
  });

  it("avoids placed labels and reports a bounded search failure with actual blocking causes", () => {
    const first = placeMeasuredLabel(plate, canvas, [], []).rect!;
    const second = placeMeasuredLabel(plate, canvas, [first], []).rect!;
    expect(labelRectsOverlap(first, second)).toBe(false);
    const blocked = placeMeasuredLabel(plate, canvas, [entireCanvas], [entireCanvas]);
    expect(blocked.rect).toBeNull();
    expect(blocked.reasons).toContain("collision");
    expect(blocked.reasons).toContain("picking");
  });

  it("fails closed on invalid obstacles instead of silently allowing covered pick targets", () => {
    for (const obstacle of [
      { ...entireCanvas, left: NaN }, { ...entireCanvas, right: -1 },
      { ...entireCanvas, bottom: Infinity }
    ]) {
      expect(placeMeasuredLabel(plate, canvas, [], [obstacle]).reasons).toEqual(["invalid-obstacle"]);
      expect(placeMeasuredLabel(plate, canvas, [obstacle], []).reasons).toEqual(["invalid-obstacle"]);
    }
    expect(placeMeasuredLabel({ ...plate, x: 201 }, canvas, [], []).reasons).toEqual(["outside-frustum"]);
  });

  it("rejects invalid measurements and off-frustum anchors without clamping them onto the canvas", () => {
    expect(placeMeasuredLabel({ ...plate, width: 0 }, canvas, [], []).reasons).toEqual(["invalid-measurement"]);
    expect(placeMeasuredLabel({ ...plate, x: NaN }, canvas, [], []).reasons).toEqual(["invalid-measurement"]);
    expect(placeMeasuredLabel({ ...plate, inFrustum: false }, canvas, [], []).reasons).toEqual(["outside-frustum"]);
    const tooLarge = placeMeasuredLabel({ ...plate, width: 201 }, canvas, [], []);
    expect(tooLarge).toEqual({ rect: null, reasons: ["containment"] });
  });
});
