import { LabelCollisionIndex } from "./labelCollisionIndex";
export { labelRectsOverlap } from "./labelCollisionIndex";

/** All coordinates and dimensions are drawable-canvas CSS pixels. */
export type LabelRect = Readonly<{ left: number; top: number; right: number; bottom: number }>;
export type LabelCenter = Readonly<{ x: number; y: number }>;
export type MeasuredLabel = Readonly<{ x: number; y: number; width: number; height: number; inFrustum: boolean }>;
export type LabelPlacementFailure = "invalid-measurement" | "invalid-obstacle" | "outside-frustum" | "containment" | "collision" | "picking";
export type LabelPlacement = Readonly<{ rect: LabelRect; reasons: readonly [] }> |
  Readonly<{ rect: null; reasons: readonly LabelPlacementFailure[] }>;

/** Fixed 24-position search; no global packing/capacity guarantee is implied. */
export function placeMeasuredLabel(
  label: MeasuredLabel,
  canvas: Readonly<{ width: number; height: number }>,
  occupied: readonly LabelRect[],
  pickTargets: readonly LabelRect[],
  preferredCenter?: LabelCenter
): LabelPlacement {
  return placeWithIndexes(label, canvas, new LabelCollisionIndex(occupied), new LabelCollisionIndex(pickTargets), preferredCenter);
}

/** Reuses validated obstacle indexes; each successful placement becomes occupied. */
export function createLabelPlacementSearch(
  canvas: Readonly<{ width: number; height: number }>,
  pickTargets: readonly LabelRect[]
): (label: MeasuredLabel, preferredCenter?: LabelCenter) => LabelPlacement {
  const occupied = new LabelCollisionIndex();
  const picking = new LabelCollisionIndex(pickTargets);
  return (label, preferredCenter) => {
    const result = placeWithIndexes(label, canvas, occupied, picking, preferredCenter);
    if (result.rect !== null) occupied.insert(result.rect);
    return result;
  };
}

function placeWithIndexes(
  label: MeasuredLabel,
  canvas: Readonly<{ width: number; height: number }>,
  occupied: LabelCollisionIndex,
  pickTargets: LabelCollisionIndex,
  preferredCenter?: LabelCenter
): LabelPlacement {
  if (![label.x, label.y, label.width, label.height, canvas.width, canvas.height].every(Number.isFinite) ||
      label.width <= 0 || label.height <= 0 || canvas.width < 0 || canvas.height < 0) {
    return { rect: null, reasons: ["invalid-measurement"] };
  }
  if (!occupied.valid || !pickTargets.valid) {
    return { rect: null, reasons: ["invalid-obstacle"] };
  }
  // Frustum membership and projected anchor coordinates must agree.
  if (!label.inFrustum || label.x < 0 || label.x > canvas.width || label.y < 0 || label.y > canvas.height) return { rect: null, reasons: ["outside-frustum"] };
  const reasons = new Set<LabelPlacementFailure>();
  const boxAt = ({ x, y }: LabelCenter): LabelRect => ({ left: x - label.width / 2, right: x + label.width / 2,
    top: y - label.height / 2, bottom: y + label.height / 2 });
  const contained = (rect: LabelRect) => rect.left >= 0 && rect.top >= 0 &&
    rect.right <= canvas.width && rect.bottom <= canvas.height;
  // Stale dimensions/resize and nonfinite hints are ignored, not label failures.
  const preferred = preferredCenter && Number.isFinite(preferredCenter.x) && Number.isFinite(preferredCenter.y) &&
    contained(boxAt(preferredCenter)) ? preferredCenter : undefined;
  const centers: LabelCenter[] = preferred ? [preferred] : [];
  const directions = [[1, -1], [1, 1], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [-1, 0]] as const;
  for (const ring of [1, 2, 3]) {
    for (const [dx, dy] of directions) {
      const x = label.x + dx * (label.width / 2 + 4 + (ring - 1) * (label.width + 4));
      const y = label.y + dy * (label.height / 2 + 4 + (ring - 1) * (label.height + 4));
      if (preferred?.x === x && preferred.y === y) continue;
      if (centers.length < 24) centers.push({ x, y });
    }
  }
  // A valid hint replaces one normal candidate; it never adds a 25th attempt.
  for (const center of centers) {
    const rect = boxAt(center);
    if (![rect.left, rect.top, rect.right, rect.bottom].every(Number.isFinite)) {
      reasons.add("invalid-measurement"); continue;
    }
    let blocked = false;
    if (!contained(rect)) { reasons.add("containment"); blocked = true; }
    if (occupied.overlaps(rect)) { reasons.add("collision"); blocked = true; }
    if (pickTargets.overlaps(rect)) { reasons.add("picking"); blocked = true; }
    if (!blocked) return { rect, reasons: [] };
  }
  return { rect: null, reasons: [...reasons] };
}
