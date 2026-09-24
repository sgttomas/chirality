import { describe, expect, it } from "vitest";
import { LabelCollisionIndex, labelRectsOverlap } from "./labelCollisionIndex";
import { createLabelPlacementSearch, placeMeasuredLabel, type LabelRect } from "./labelPlacement";

const rect = (left: number, top: number, width: number, height: number): LabelRect =>
  ({ left, top, right: left + width, bottom: top + height });

describe("label collision broad phase", () => {
  it("agrees with exhaustive overlap across cells, negative coordinates, edge contact and oversized paths", () => {
    const obstacles = [rect(-100, -80, 30, 12), rect(0, 0, 64, 64), rect(64, 64, 1, 1),
      rect(128, 0, 20, 300), rect(1000, 1000, 2000, 2000), rect(350, 350, 0, 0),
      { left: 1e30, top: 1e30, right: 2e30, bottom: 2e30 }];
    const index = new LabelCollisionIndex(obstacles);
    const queries = [rect(64, 0, 64, 64), rect(-70, -80, 1, 1), rect(2999, 2999, 1, 1),
      rect(-5000, -5000, 10000, 10000), rect(4000, 4000, 2000, 2000), rect(350, 350, 0, 0), rect(349, 349, 2, 2),
      { left: 1.5e30, top: 1.5e30, right: 1.6e30, bottom: 1.6e30 },
      { left: 2e30, top: 2e30, right: 3e30, bottom: 3e30 }];
    for (let x = -150; x < 400; x += 17) for (let y = -100; y < 400; y += 29) queries.push(rect(x, y, 37, 11));
    for (const query of queries) {
      expect(index.overlaps(query)).toBe(obstacles.some((other) => labelRectsOverlap(query, other)));
    }
    const added = rect(450, 450, 80, 80);
    index.insert(added);
    expect(index.overlaps(rect(500, 500, 1, 1))).toBe(true);
    expect(index.overlaps(rect(530, 530, 1, 1))).toBe(false);
  });

  it("matches exhaustive queries through dense shared cells, alternating paths and late insertions", () => {
    // Repeated coordinates are distinct insertions, each crossing several cells.
    const inputs = Array.from({ length: 512 }, (_, i) =>
      ({ ...rect(-128 + (i % 8), -128 + (i % 5), 190, 190) }));
    inputs.push(rect(1000, 1000, 2000, 2000));
    const snapshots = inputs.map((entry) => ({ ...entry }));
    const index = new LabelCollisionIndex(inputs);
    const check = (query: LabelRect) => {
      const expected = snapshots.some((other) =>
        query.left < other.right && query.right > other.left &&
        query.top < other.bottom && query.bottom > other.top);
      expect(index.overlaps(query)).toBe(expected);
    };
    // Full traversal without a hit, early hit, exact edge, oversized miss/hit.
    const queries = [rect(70, -120, 1, 180), rect(-120, -120, 10, 10),
      rect(69, -120, 1, 180), rect(4000, 4000, 2000, 2000),
      rect(-5000, -5000, 10000, 10000), rect(2999, 2999, 1, 1)];
    for (let pass = 0; pass < 8; pass++) {
      for (const query of queries) check(query);
      expect(index.overlaps({ left: NaN, top: 0, right: 1, bottom: 1 })).toBe(true);
      expect(index.overlaps({ left: 1, top: 0, right: 0, bottom: 1 })).toBe(true);
      expect(index.valid).toBe(true);
      check(queries[0]);
    }
    const late = { ...rect(70, -120, 1, 180) };
    check(late);
    index.insert(late);
    snapshots.push({ ...late });
    // Reusing and then mutating a caller object must not share stored geometry.
    late.left = 200;
    late.right = 201;
    index.insert(late);
    snapshots.push({ ...late });
    late.left = 10000;
    late.right = 10001;
    inputs[0].right = 10000;
    for (const query of [...queries, rect(200, -120, 1, 1), rect(500, -120, 1, 1)]) check(query);
    check({ left: 1e30, top: 1e30, right: 2e30, bottom: 2e30 });
    check(queries[0]);
  });

  it("copies obstacle inputs and fails closed on invalid rectangles", () => {
    const obstacle = { left: 0, top: 0, right: 20, bottom: 20 };
    const index = new LabelCollisionIndex([obstacle]);
    obstacle.left = 100;
    expect(index.overlaps(rect(5, 5, 1, 1))).toBe(true);
    index.insert({ ...obstacle, top: NaN });
    expect(index.valid).toBe(false);
    expect(index.overlaps(rect(500, 500, 1, 1))).toBe(true);
  });

  it("reused placement produces the same ordered boxes/reasons as isolated convenience calls", () => {
    const canvas = { width: 400, height: 300 };
    const targets = [rect(50, 50, 30, 30), rect(200, 0, 20, 300)];
    const place = createLabelPlacementSearch(canvas, targets);
    const occupied: LabelRect[] = [];
    for (let i = 0; i < 40; i++) {
      const label = { x: 50 + (i % 8) * 40, y: 50 + Math.floor(i / 8) * 40,
        width: 36, height: 18, inFrustum: true };
      const expected = placeMeasuredLabel(label, canvas, occupied, targets);
      expect(place(label)).toEqual(expected);
      if (expected.rect !== null) occupied.push(expected.rect);
    }
  });
});
