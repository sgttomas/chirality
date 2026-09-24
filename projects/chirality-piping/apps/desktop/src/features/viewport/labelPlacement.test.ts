import { describe, expect, it } from "vitest";
import { labelRectsOverlap, placeMeasuredLabel, type MeasuredLabel } from "./labelPlacement";

const plate: MeasuredLabel = { x: 50, y: 50, width: 34, height: 16, inFrustum: true };
const canvas = { width: 200, height: 160 };
const entireCanvas = { left: 0, top: 0, right: 200, bottom: 160 };

describe("measured label placement", () => {
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
