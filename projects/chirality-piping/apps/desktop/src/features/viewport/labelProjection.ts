import * as THREE from "three";
import type { Vec3 } from "../../types";
import type { EntityKey } from "../workspace/selectionState";
import type { LabelRect } from "./labelPlacement";
import type { PointPickPrimitive } from "./viewportSelection";

const finitePoint = (p: Readonly<Vec3>) => [p.x, p.y, p.z].every(Number.isFinite);
const vector = (p: Readonly<Vec3>) => new THREE.Vector3(p.x, p.y, p.z);

/** Read-only adapter: caller updates camera matrices before calling, as for rendering. */
function validCamera(camera: THREE.PerspectiveCamera, width: number, height: number): boolean {
  const p = camera.projectionMatrix.elements;
  const v = camera.matrixWorldInverse.elements;
  if (![width, height, camera.near, camera.far, camera.fov, ...p, ...v].every(Number.isFinite) ||
      width <= 0 || height <= 0 || camera.near <= 0 || camera.far <= camera.near ||
      camera.fov <= 0 || camera.fov >= 180 || p[0] <= 0 || p[5] <= 0 ||
      p[1] !== 0 || p[2] !== 0 || p[3] !== 0 || p[4] !== 0 || p[6] !== 0 || p[7] !== 0 ||
      p[11] !== -1 || p[12] !== 0 || p[13] !== 0 || p[15] !== 0 ||
      v[3] !== 0 || v[7] !== 0 || v[11] !== 0 || v[15] === 0) return false;
  // THREE's general inversion can produce w = 1 +/- rounding even for a
  // rigid camera. applyMatrix4 divides by this constant homogeneous w; validate
  // that same normalized linear transform rather than demanding literal w=1.
  // Non-affine bottom rows remain rejected. The pick tolerance is in world
  // units, so normalized scaled/sheared transforms must still be rejected.
  const axes = [new THREE.Vector3(v[0], v[1], v[2]), new THREE.Vector3(v[4], v[5], v[6]),
    new THREE.Vector3(v[8], v[9], v[10])].map((axis) => axis.divideScalar(v[15]));
  return axes.every((axis) => Math.abs(axis.lengthSq() - 1) < 1e-10) &&
    Math.abs(axes[0].dot(axes[1])) < 1e-10 && Math.abs(axes[0].dot(axes[2])) < 1e-10 &&
    Math.abs(axes[1].dot(axes[2])) < 1e-10;
}

/** Anchor is render-local, including any caller-applied marker offset. No clamping into view. */
export function projectLabelAnchor(anchor: Readonly<Vec3>, camera: THREE.PerspectiveCamera,
  width: number, height: number): Readonly<{ x: number; y: number; inFrustum: boolean }> {
  const invalid = { x: 0, y: 0, inFrustum: false };
  if (!finitePoint(anchor) || !validCamera(camera, width, height)) return invalid;
  const view = vector(anchor).applyMatrix4(camera.matrixWorldInverse);
  if (!finitePoint(view) || view.z >= 0) return invalid;
  const projected = view.clone().applyMatrix4(camera.projectionMatrix);
  const x = (projected.x + 1) * width / 2;
  const y = (1 - projected.y) * height / 2;
  if (![x, y, projected.z].every(Number.isFinite)) return invalid;
  return { x, y, inFrustum: -view.z >= camera.near && -view.z <= camera.far &&
    Math.abs(projected.x) <= 1 && Math.abs(projected.y) <= 1 && Math.abs(projected.z) <= 1 };
}

/** The same world-box / view-box enclosure is used for whole shapes and pieces. */
function viewEnvelope(points: readonly Readonly<Vec3>[], expansion: THREE.Vector3,
  camera: THREE.PerspectiveCamera): THREE.Box3 {
  const world = new THREE.Box3().setFromPoints(points.map(vector));
  world.min.sub(expansion); world.max.add(expansion);
  const view = new THREE.Box3();
  for (const x of [world.min.x, world.max.x]) for (const y of [world.min.y, world.max.y])
    for (const z of [world.min.z, world.max.z]) {
      const corner = new THREE.Vector3(x, y, z).applyMatrix4(camera.matrixWorldInverse);
      if (!finitePoint(corner)) throw new Error("Unrepresentable label pick envelope.");
      view.expandByPoint(corner);
    }
  return view;
}

function projectEnvelope(envelope: THREE.Box3, camera: THREE.PerspectiveCamera,
  width: number, height: number): LabelRect | null {
  const view = envelope.clone();
  view.min.z = Math.max(view.min.z, -camera.far);
  view.max.z = Math.min(view.max.z, -camera.near);
  if (view.min.z > view.max.z) return null;
  let left = Infinity, right = -Infinity, top = Infinity, bottom = -Infinity;
  for (const x of [view.min.x, view.max.x]) for (const y of [view.min.y, view.max.y])
    for (const z of [view.min.z, view.max.z]) {
      const p = new THREE.Vector3(x, y, z).applyMatrix4(camera.projectionMatrix);
      const sx = (p.x + 1) * width / 2, sy = (1 - p.y) * height / 2;
      if (![sx, sy].every(Number.isFinite)) throw new Error("Unrepresentable label pick projection.");
      left = Math.min(left, sx); right = Math.max(right, sx);
      top = Math.min(top, sy); bottom = Math.max(bottom, sy);
    }
  // Outward numerical guard, not an extra pick tolerance. Closed boundary contact stays excluded.
  const guard = 1e-7 * Math.max(1, width, height);
  left = Math.max(0, left - guard); right = Math.min(width, right + guard);
  top = Math.max(0, top - guard); bottom = Math.min(height, bottom + guard);
  return left <= right && top <= bottom ? Object.freeze({ left, right, top, bottom }) : null;
}

/**
 * Conservative enclosing rectangles of the actual picker support, O(n) time/output.
 * Capsule tolerance varies with the closest segment point; its depth cannot exceed
 * the larger endpoint depth. Expand the entire shape by that maximum tolerance,
 * enclose in camera coordinates, clip that enclosure to near/far, then project.
 * Strictly depth-interior nonzero capsules use eight contiguous full-radius
 * pieces; the union preserves support while reducing empty diagonal corners.
 * This also retains segments with both endpoints outside the viewport. Rectangles
 * deliberately over-exclude diagonal geometry and near-plane envelopes; they may
 * cover the canvas when that conservative envelope surrounds the visible frustum.
 * Invalid inputs throw: callers must suppress placement, never substitute [].
 */
export function projectLabelPickTargets(input: Readonly<{
  primitives: readonly PointPickPrimitive[];
  camera: THREE.PerspectiveCamera;
  width: number;
  height: number;
  hiddenKeys: ReadonlySet<EntityKey>;
  actualOdRadiusByPipe: ReadonlyMap<EntityKey, number>;
}>): readonly LabelRect[] {
  const { camera, width, height } = input;
  if (!validCamera(camera, width, height)) throw new Error("Invalid label projection camera or CSS dimensions.");
  const rectangles: LabelRect[] = [];
  for (const primitive of input.primitives) {
    if (input.hiddenKeys.has(primitive.key)) continue;
    const od = primitive.kind === "pipe" ? input.actualOdRadiusByPipe.get(primitive.key) ?? 0 : 0;
    if (!finitePoint(primitive.center) || ![primitive.radius, primitive.height, od].every(Number.isFinite) ||
        primitive.radius < 0 || primitive.height < 0 || od < 0 ||
        (primitive.shape === "capsule" && (!primitive.start || !primitive.end ||
          !finitePoint(primitive.start) || !finitePoint(primitive.end)))) {
      throw new Error(`Invalid label pick geometry: ${primitive.key}`);
    }
    const points = primitive.shape === "capsule" ? [primitive.start!, primitive.end!] : [primitive.center];
    const depth = Math.max(...points.map((point) => -vector(point).applyMatrix4(camera.matrixWorldInverse).z));
    if (!Number.isFinite(depth)) throw new Error("Unrepresentable label pick depth.");
    // The existing picker rejects a nonpositive primitiveDepth before intersection.
    if (depth <= 0) continue;
    const radius = Math.max(primitive.radius, od,
      6 * (2 * depth * Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2)) / height);
    const expansion = primitive.shape === "cone"
      ? new THREE.Vector3(radius, primitive.height / 2, radius)
      : new THREE.Vector3(radius, radius, radius);
    const whole = viewEnvelope(points, expansion, camera);
    let pieces: LabelRect[] | null = null;
    if (primitive.shape === "capsule" && !vector(points[0]).equals(vector(points[1])) &&
        whole.min.z > -camera.far && whole.max.z < -camera.near) {
      // D and R belong to the original primitive. Recomputing either for a
      // piece would shrink the bound on the picker's depth-varying tolerance.
      try {
        const start = vector(points[0]), end = vector(points[1]);
        const delta = end.clone().sub(start);
        if (!finitePoint(delta)) throw new Error("Unsafe capsule subdivision.");
        const joins = [start];
        for (let i = 1; i < 8; i++) {
          const join = start.clone().addScaledVector(delta, i / 8);
          if (!finitePoint(join) || join.equals(joins[i - 1]) || join.equals(end)) {
            throw new Error("Unsafe capsule subdivision.");
          }
          joins.push(join);
        }
        joins.push(end); // Exact original endpoints and shared interior joins.
        pieces = [];
        for (let i = 0; i < 8; i++) {
          const rect = projectEnvelope(viewEnvelope([joins[i], joins[i + 1]], expansion, camera),
            camera, width, height);
          if (rect) pieces.push(rect);
        }
      } catch {
        // Never publish a partial union after unsafe intermediate arithmetic.
        pieces = null;
      }
    }
    if (pieces !== null) rectangles.push(...pieces);
    else {
      const rect = projectEnvelope(whole, camera, width, height);
      if (rect) rectangles.push(rect);
    }
  }
  return Object.freeze(rectangles);
}
