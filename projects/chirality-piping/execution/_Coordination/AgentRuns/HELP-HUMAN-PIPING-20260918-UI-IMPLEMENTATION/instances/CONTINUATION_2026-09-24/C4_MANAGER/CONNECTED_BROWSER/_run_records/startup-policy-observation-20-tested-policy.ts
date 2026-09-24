import type { Vec3 } from "../../types";
import type { ModelIndex } from "../workspace/modelIndex";
import type { EntityKey } from "../workspace/selectionState";
import { createLabelPlacementSearch, type LabelPlacementFailure, type LabelRect, type MeasuredLabel } from "./labelPlacement";

export type LabelMode = "Budget" | "All" | "Off";
export const DEFAULT_LABEL_MODE: LabelMode = "Budget";
export type LabelRole = "primary" | "hover" | "current-row" | "selected" | "ordinary";
export type LabelPolicyInput = Readonly<{
  mode: LabelMode;
  width: number;
  height: number;
  primaryKey: EntityKey | null;
  hoverKey: EntityKey | null;
  /** Previous rendered CSS center for this hover only; revalidated by placement. */
  preferredHoverCenter?: Readonly<{ key: EntityKey; x: number; y: number }>;
  /** Resolved independently by the shell; never inferred from primary selection. */
  currentRowNodeKey: EntityKey | null;
  selectedKeys: readonly EntityKey[];
  /** Effective visibility projection, including node-Hide attachment expansion. */
  hiddenKeys: ReadonlySet<EntityKey>;
  cameraTarget?: Readonly<Vec3>;
  measurements: ReadonlyMap<EntityKey, MeasuredLabel>;
  /** Caller supplies all required geometry picking areas, including the label's own entity. */
  pickTargets: readonly LabelRect[];
}>;
export type LabelIdentity = Readonly<{ key: EntityKey; role: LabelRole }>;
export type LabelPolicyResult = Readonly<{
  mode: LabelMode;
  nominalBudget: number;
  rendered: readonly (LabelIdentity & { rect: LabelRect })[];
  suppressed: readonly (LabelIdentity & { reason: "mode" | "budget" })[];
  ineligible: readonly (LabelIdentity & { reason: "hidden" | "unsupported" | "geometry" | "not-node" })[];
  unplaced: readonly (LabelIdentity & { reasons: readonly (LabelPlacementFailure | "missing-measurement")[] })[];
  counts: Readonly<{ context: number; ordinary: number; total: number; contextOverflow: number;
    suppressed: number; ineligible: number; unplaced: number }>;
}>;

export function nominalLabelBudget(width: number, height: number): number {
  if (!Number.isFinite(width) || !Number.isFinite(height) || width < 0 || height < 0 ||
      !Number.isFinite(width * height)) return 0;
  return Math.floor(width * height / 3600);
}

/** Pure policy for existing node/pipe/support/component identity labels, not engineering plates. */
export function layoutViewportLabels(index: ModelIndex, input: LabelPolicyInput): LabelPolicyResult {
  const __observations = (globalThis as any).__c4PolicyObservation as unknown[] | undefined;
  const __entry: Record<string, unknown> = { started: performance.now(), primitives: input.pickTargets.length, measurements: input.measurements.size, mode: input.mode, completed: false };
  if (__observations) __observations.push(__entry);
  try {
  const nominalBudget = nominalLabelBudget(input.width, input.height);
  const candidates: LabelIdentity[] = [];
  const seen = new Set<EntityKey>();
  const ineligible: Array<LabelPolicyResult["ineligible"][number]> = [];
  const add = (key: EntityKey | null, role: LabelRole) => {
    if (key === null || seen.has(key)) return;
    const entity = index.entities.get(key);
    // A malformed current-row publication must not steal an ordinary/selected identity.
    if (role === "current-row" && entity?.ref.type !== "node") {
      ineligible.push({ key, role, reason: "not-node" }); return;
    }
    seen.add(key);
    const reason = input.hiddenKeys.has(key) ? "hidden" :
      !entity || !["node", "pipe", "support", "component"].includes(entity.ref.type) ? "unsupported" :
      !entity.anchor || entity.geometryIssue || !index.visibilityEligibleKeys.has(key) ? "geometry" : null;
    if (reason) ineligible.push({ key, role, reason });
    else candidates.push({ key, role });
  };
  add(input.primaryKey, "primary");
  add(input.hoverKey, "hover");
  add(input.currentRowNodeKey, "current-row");
  for (const key of input.selectedKeys) add(key, "selected");
  const bounds = index.geometryBounds;
  const target = input.cameraTarget ?? (bounds ? {
    x: bounds.min.x / 2 + bounds.max.x / 2, y: bounds.min.y / 2 + bounds.max.y / 2,
    z: bounds.min.z / 2 + bounds.max.z / 2
  } : { x: 0, y: 0, z: 0 });
  const distance = (key: EntityKey) => {
    const anchor = index.entities.get(key)?.anchor;
    return anchor ? Math.hypot(anchor.x - target.x, anchor.y - target.y, anchor.z - target.z) : Infinity;
  };
  // Preserve the retained model-index anchor/distance ordering, with typed-key ties.
  const ordinary = [...index.visibilityEligibleKeys].sort((a, b) => {
    const delta = distance(a) - distance(b);
    return (Number.isFinite(delta) && delta !== 0) ? delta : a < b ? -1 : a > b ? 1 : 0;
  });
  for (const key of ordinary) add(key, "ordinary");
  const rendered: Array<LabelPolicyResult["rendered"][number]> = [];
  const suppressed: Array<LabelPolicyResult["suppressed"][number]> = [];
  const unplaced: Array<LabelPolicyResult["unplaced"][number]> = [];
  __entry.preIndex = performance.now();
  const place = createLabelPlacementSearch(input, input.pickTargets);
  __entry.postIndex = performance.now();
  let context = 0;
  let ordinaryCount = 0;
  for (const identity of candidates) {
    if (identity.role === "ordinary" && (input.mode === "Off" ||
        input.mode === "Budget" && rendered.length >= nominalBudget)) {
      suppressed.push({ ...identity, reason: input.mode === "Off" ? "mode" : "budget" }); continue;
    }
    const measurement = input.measurements.get(identity.key);
    if (!measurement) { unplaced.push({ ...identity, reasons: ["missing-measurement"] }); continue; }
    const preferred = input.preferredHoverCenter;
    const placed = place(measurement, preferred && preferred.key === input.hoverKey && preferred.key === identity.key
      ? preferred : undefined);
    if (placed.rect === null) { unplaced.push({ ...identity, reasons: placed.reasons }); continue; }
    rendered.push({ ...identity, rect: placed.rect });
    if (identity.role === "ordinary") ordinaryCount++; else context++;
  }
  __entry.ended = performance.now(); __entry.completed = true;
  __entry.candidates = candidates.length; __entry.rendered = rendered.length; __entry.unplaced = unplaced.length; __entry.suppressed = suppressed.length;
  return { mode: input.mode, nominalBudget, rendered, suppressed, ineligible, unplaced,
    counts: { context, ordinary: ordinaryCount, total: rendered.length,
      contextOverflow: input.mode === "Budget" ? Math.max(context - nominalBudget, 0) : 0,
      suppressed: suppressed.length, ineligible: ineligible.length, unplaced: unplaced.length } };
  } catch (error) { __entry.ended = performance.now(); __entry.error = String(error); throw error; }
}
