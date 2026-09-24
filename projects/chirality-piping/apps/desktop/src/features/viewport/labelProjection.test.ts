import previewModelJson from "../../../../../fixtures/product_preview/invented_preview_model.json";
import { describe, expect, it, vi } from "vitest";
import * as THREE from "three";
import type { PreviewModel } from "../../types";
import { buildModelIndex } from "../workspace/modelIndex";
import { entityKey } from "../workspace/selectionState";
import { authoredToLocal, pickPointPrimitive, pointPickPrimitives, type PointPickPrimitive } from "./viewportSelection";
import { labelRectsOverlap, placeMeasuredLabel } from "./labelPlacement";
import { projectLabelAnchor, projectLabelPickTargets } from "./labelProjection";

const width = 600, height = 400;
function cameraAt(x = 0, y = 0, z = 10) {
  const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 100);
  camera.position.set(x, y, z); camera.lookAt(0, 0, 0); camera.updateMatrixWorld();
  return camera;
}
function model(): PreviewModel {
  return {
    schema_version: "test", document_kind: "test", data_boundary: {},
    project: { id: "p", name: "projection", description: "", units: { length: "m" } },
    analysis_status: { mechanics: "TBD", rule_check: "TBD", professional_acceptance: "TBD" },
    nodes: [{ id: "a", label: "A", position: { x: -4, y: 0, z: 0 }, provenance: "test" },
      { id: "b", label: "B", position: { x: 4, y: 0, z: 0 }, provenance: "test" }],
    pipe_segments: [{ id: "p", label: "P", from: "a", to: "b", section: {}, material: "m", provenance: "test" }],
    supports: [], components: [], load_cases: [], diagnostics: []
  };
}
const origin = { x: 0, y: 0, z: 0 };
function target(primitive: PointPickPrimitive, camera = cameraAt(), radius = 0) {
  return projectLabelPickTargets({ primitives: [primitive], camera, width, height,
    hiddenKeys: new Set(), actualOdRadiusByPipe: new Map([[primitive.key, radius]]) });
}
function primitive(): PointPickPrimitive {
  const source = model();
  return pointPickPrimitives(buildModelIndex(source, 1, 0), source, origin)[0];
}

describe("label projection", () => {
  it("projects render-local anchors into CSS pixels with caller-owned origin and marker offsets", () => {
    const camera = cameraAt();
    expect(projectLabelAnchor(authoredToLocal({ x: 1e9, y: 2e9, z: 3e9 },
      { x: 1e9, y: 2e9, z: 3e9 }), camera, width, height)).toEqual({ x: 300, y: 200, inFrustum: true });
    const shifted = projectLabelAnchor({ x: 1, y: 0.2, z: 0 }, camera, width, height);
    expect(shifted.x).toBeCloseTo(300 + 20 * Math.sqrt(3));
    expect(shifted.y).toBeCloseTo(200 - 4 * Math.sqrt(3));
    expect(projectLabelAnchor({ x: 100, y: 0, z: 0 }, camera, width, height).inFrustum).toBe(false);
    expect(projectLabelAnchor({ x: 0, y: 0, z: 11 }, camera, width, height).inFrustum).toBe(false);
    expect(projectLabelAnchor({ x: NaN, y: 0, z: 0 }, camera, width, height)).toEqual({ x: 0, y: 0, inFrustum: false });
  });

  it("accepts a rigid orbit camera with rounded homogeneous inverse scale", () => {
    const camera = cameraAt(6, 5, 9);
    const projected = projectLabelAnchor(origin, camera, width, height);
    expect(projected.inFrustum).toBe(true);
    expect(projected.x).toBeCloseTo(width / 2);
    expect(projected.y).toBeCloseTo(height / 2);
    expect(target(primitive(), camera).length).toBe(8);
    // A homogeneous rescaling denotes exactly the same affine transform.
    // Check normalization explicitly, independent of THREE version rounding.
    camera.matrixWorldInverse.multiplyScalar(2);
    const equivalent = projectLabelAnchor(origin, camera, width, height);
    expect(equivalent.inFrustum).toBe(true);
    expect(equivalent.x).toBeCloseTo(projected.x);
    expect(equivalent.y).toBeCloseTo(projected.y);
    expect(target(primitive(), camera).length).toBe(8);
    camera.matrixWorldInverse.elements[3] = 1e-8;
    expect(() => target(primitive(), camera)).toThrow(/camera/);
  });

  it("retains an offscreen-endpoint capsule crossing the canvas and expands actual OD", () => {
    const p = { ...primitive(), start: { x: -100, y: 0, z: 0 }, end: { x: 100, y: 0, z: 0 } };
    const rects = target(p);
    expect(rects.length).toBeLessThanOrEqual(8);
    const rect = { left: Math.min(...rects.map((r) => r.left)), right: Math.max(...rects.map((r) => r.right)),
      top: Math.min(...rects.map((r) => r.top)), bottom: Math.max(...rects.map((r) => r.bottom)) };
    for (let x = 0; x <= width; x++) {
      expect(rects.some((r) => x >= r.left && x <= r.right && r.top < 194 && r.bottom > 206)).toBe(true);
    }
    expect(rect.left).toBe(0); expect(rect.right).toBe(width);
    expect(rect.top).toBeLessThan(194); expect(rect.bottom).toBeGreaterThan(206);
    const thickRects = target(p, cameraAt(), 1);
    const thick = { top: Math.min(...thickRects.map((r) => r.top)), bottom: Math.max(...thickRects.map((r) => r.bottom)) };
    for (const r of rects) expect(thickRects.some((t) => t.left <= r.left && t.right >= r.right &&
      t.top < r.top && t.bottom > r.bottom)).toBe(true);
    expect(thick.top).toBeLessThan(rect.top); expect(thick.bottom).toBeGreaterThan(rect.bottom);
  });

  it("clips envelopes at near/far and omits only wholly clipped or hidden support", () => {
    const p = primitive();
    const camera = cameraAt();
    expect(target({ ...p, start: { x: -1, y: 0, z: 9.95 }, end: { x: 1, y: 0, z: 0 } }, camera).length).toBe(1);
    const behind = { ...p, start: { x: -1, y: 0, z: 12 }, end: { x: 1, y: 0, z: 12 } };
    expect(target(behind, camera)).toEqual([]);
    expect(target({ ...p, start: { x: -1, y: 0, z: -200 }, end: { x: 1, y: 0, z: -200 } }, camera)).toEqual([]);
    expect(projectLabelPickTargets({ primitives: [p], camera, width, height,
      hiddenKeys: new Set([p.key]), actualOdRadiusByPipe: new Map() })).toEqual([]);
  });

  it("fails closed on malformed geometry, dimensions and scaled cameras without mutating camera", () => {
    const camera = cameraAt(); const before = camera.matrixWorld.toArray();
    target(primitive(), camera); expect(camera.matrixWorld.toArray()).toEqual(before);
    expect(() => target({ ...primitive(), radius: NaN }, camera)).toThrow(/geometry/);
    expect(() => target({ ...primitive(), start: null }, camera)).toThrow(/geometry/);
    expect(() => projectLabelPickTargets({ primitives: [], camera, width: 0, height,
      hiddenKeys: new Set(), actualOdRadiusByPipe: new Map() })).toThrow(/dimensions/);
    camera.scale.setScalar(2); camera.updateMatrixWorld();
    expect(() => target(primitive(), camera)).toThrow(/camera/);
    const sheared = cameraAt();
    sheared.matrixWorldInverse.elements[4] = 0.2;
    expect(() => target(primitive(), sheared)).toThrow(/camera/);
  });

  it("contains every sampled actual picker hit across orbit, clipping, capsule, sphere, cone and OD variants", () => {
    const standard = model();
    const supported = model();
    supported.supports.push({ id: "s", label: "S", node: "a", restraints: [], provenance: "test" });
    const component = model();
    component.components.push({ id: "c", label: "C", kind: "valve", node: "a", provenance: "test" });
    const crossing = model();
    crossing.nodes[0].position.x = -40; crossing.nodes[1].position.x = 40;
    const near = model(); near.nodes[0].position.z = 9.95;
    const variants = [
      { source: standard, kind: "pipe" }, { source: standard, kind: "node" },
      { source: supported, kind: "support" }, { source: component, kind: "component" },
      { source: crossing, kind: "pipe" }, { source: near, kind: "pipe" }
    ];
    const canvas = { getBoundingClientRect: () => ({ left: 17, top: 23, width, height }),
      clientWidth: width, clientHeight: height } as HTMLCanvasElement;
    for (const camera of [cameraAt(), cameraAt(6, 5, 9), cameraAt(0, 10, 0)]) {
      for (const { source, kind } of variants) for (const od of [0, 0.8]) {
        const index = buildModelIndex(source, 1, 0);
        const primitives = pointPickPrimitives(index, source, origin).filter((p) => p.kind === kind);
        let hits = 0;
        const actualOdRadiusByPipe = new Map([[entityKey({ type: "pipe", id: "p" }), od]]);
        const rects = projectLabelPickTargets({ primitives, camera, width, height,
          hiddenKeys: new Set(), actualOdRadiusByPipe });
        for (let y = 0; y <= height; y += 8) for (let x = 0; x <= width; x += 8) {
          const hit = pickPointPrimitive(primitives, { index, renderOrigin: origin, camera, canvas,
            clientX: x + 17, clientY: y + 23, actualOdRadiusByPipe });
          if (!hit) continue;
          hits++;
          expect(rects.some((r) => x >= r.left && x <= r.right && y >= r.top && y <= r.bottom),
            `${hit.type}:${hit.id} at ${x},${y}`).toBe(true);
        }
        expect(hits, `${kind} visible reference samples, OD ${od}`).toBeGreaterThan(0);
      }
    }
  });

  it("bounds output and retains whole-envelope fallback for depth boundaries, zero and unsafe joins", () => {
    const p = primitive();
    expect(target(p)).toHaveLength(8);
    for (const z of [9.9 - 1, -90 + 1]) {
      // Radius 1 touches the near or far plane exactly; strict interior only.
      expect(target({ ...p, radius: 1, start: { x: -1, y: 0, z }, end: { x: 1, y: 0, z } })).toHaveLength(1);
    }
    expect(target({ ...p, start: origin, end: origin })).toHaveLength(1);
    expect(target({ ...p, start: origin, end: { x: Number.MIN_VALUE, y: 0, z: 0 } })).toHaveLength(1);
    expect(() => target({ ...p, radius: Number.MAX_VALUE })).toThrow(/Unrepresentable/);
    expect(() => target({ ...p, end: { x: Infinity, y: 0, z: 0 } })).toThrow(/geometry/);
    const duplicate = { ...p, start: { x: -4, y: 2, z: 0 }, end: { x: 4, y: 2, z: 0 } };
    const args = { primitives: [p, duplicate], camera: cameraAt(), width, height,
      hiddenKeys: new Set<typeof p.key>(), actualOdRadiusByPipe: new Map() };
    expect(projectLabelPickTargets(args)).toEqual([...target(p), ...target(duplicate)]);
    expect(projectLabelPickTargets(args)).toHaveLength(16);
    expect(projectLabelPickTargets({ ...args, hiddenKeys: new Set([p.key]) })).toEqual([]);
  });

  it("discards a partial subdivision after unsafe arithmetic and returns the original envelope", () => {
    const p = primitive(), camera = cameraAt();
    const radius = 6 * (2 * 10 * Math.tan(Math.PI / 6)) / height;
    const boundaryCamera = cameraAt(); boundaryCamera.far = 10 + radius; boundaryCamera.updateProjectionMatrix();
    const whole = target(p, boundaryCamera);
    expect(whole).toHaveLength(1);
    const apply = THREE.Vector3.prototype.applyMatrix4;
    let projectedCorners = 0;
    const spy = vi.spyOn(THREE.Vector3.prototype, "applyMatrix4").mockImplementation(function (this: THREE.Vector3, matrix) {
      const result = apply.call(this, matrix);
      // First piece completed; second piece fails. The fallback is then safe.
      if (matrix === camera.projectionMatrix && ++projectedCorners === 9) result.x = Infinity;
      return result;
    });
    try { expect(target(p, camera)).toEqual(whole); } finally { spy.mockRestore(); }
  });

  it("covers actual picker hits for skew depth, camera/far crossing, joints, caps, tangency, zero and duplicate keys", () => {
    const cases = [
      [{ x: -3, y: -1, z: 8 }, { x: 3, y: 1, z: -12 }],
      [{ x: -1, y: 0, z: 12 }, { x: 1, y: 0, z: 0 }],
      [{ x: -1, y: 0, z: 0 }, { x: 1, y: 0, z: -100 }],
      [{ x: -4, y: 0, z: 0 }, { x: 4, y: 0, z: 0 }],
      [origin, origin]
    ];
    for (const [start, end] of cases) for (const od of [0, 0.8]) {
      const source = model();
      if (start !== end) { source.nodes[0].position = start; source.nodes[1].position = end; }
      const index = buildModelIndex(source, 1, 0);
      const indexed = pointPickPrimitives(index, source, origin).find((p) => p.kind === "pipe")!;
      // The producer rightly omits invalid zero-length model pipes; exercise
      // the public picker primitive contract inside a valid indexed pipe bound.
      const p = { ...indexed, start, end };
      // Repeated keys must retain every supplied shape; this second capsule
      // shares an indexed endpoint so broad-phase lookup remains representative.
      const primitives = [p, { ...p, start: end, end }];
      const camera = cameraAt(), actualOdRadiusByPipe = new Map([[p.key, od]]);
      const canvas = { getBoundingClientRect: () => ({ left: 0, top: 0, width, height }),
        clientWidth: width, clientHeight: height } as HTMLCanvasElement;
      const rects = projectLabelPickTargets({ primitives, camera, width, height,
        hiddenKeys: new Set(), actualOdRadiusByPipe });
      expect(rects.length).toBeLessThanOrEqual(16);
      let hits = 0;
      const sample = (x: number, y: number) => {
        const hit = pickPointPrimitive(primitives, { index, renderOrigin: origin, camera, canvas,
          clientX: x, clientY: y, actualOdRadiusByPipe });
        if (hit) {
          hits++;
          expect(rects.some((r) => x >= r.left && x <= r.right && y >= r.top && y <= r.bottom),
            `picker hit ${x},${y}, OD ${od}`).toBe(true);
        }
        expect(pickPointPrimitive(primitives, { index, renderOrigin: origin, camera, canvas,
          clientX: x, clientY: y, actualOdRadiusByPipe, hiddenKeys: new Set([p.key]) })).toBeNull();
      };
      for (let y = 0; y <= height; y += 8) for (let x = 0; x <= width; x += 8) sample(x, y);
      // Exact piece joins and endcaps, with samples immediately inside/outside
      // the six-pixel silhouette for the horizontal constant-depth case.
      for (let i = 0; i <= 8; i++) {
        const point = new THREE.Vector3(start.x, start.y, start.z).lerp(new THREE.Vector3(end.x, end.y, end.z), i / 8);
        const anchor = projectLabelAnchor(point, camera, width, height);
        if (!anchor.inFrustum) continue;
        for (const offset of [0, 6 - 1e-6, 6, 6 + 1e-6, -6 + 1e-6]) sample(anchor.x, anchor.y + offset);
      }
      expect(hits, `visible capsule ${JSON.stringify([start, end])}, OD ${od}`).toBeGreaterThan(0);
      if (start.z > 10 || end.z < -90) expect(target(p, camera, od)).toHaveLength(1);
    }
  });

  it("places retained default-model P-100 at 924x540 and 58x32 against all geometry", () => {
    // Maintained product-preview fixture. Camera/measurement provenance: C4
    // diagnostic 15 before selected-pipe keyboard measurement, 2026-09-24;
    // raw reconstruction model SHA256 986c055944776ca8d0d849d552678e1f2bfb6c4559bbb9ff8a1928157a4f871c.
    // Constants are retained here; this test never reads dated run artifacts.
    const source = previewModelJson as PreviewModel;
    const index = buildModelIndex(source, 1, 1), renderOrigin = { x: 3.8, y: 1.2, z: 1.1 };
    const width = 924, height = 540;
    const camera = new THREE.PerspectiveCamera(42, width / height, 0.001, 1000);
    camera.position.set(5.033617520924543, 3.4336175209245434, 3.433617520924543).sub(new THREE.Vector3(renderOrigin.x, renderOrigin.y, renderOrigin.z));
    camera.lookAt(new THREE.Vector3(1.6, 0, 0).sub(new THREE.Vector3(renderOrigin.x, renderOrigin.y, renderOrigin.z))); camera.updateMatrixWorld();
    const primitives = pointPickPrimitives(index, source, renderOrigin);
    const key = entityKey({ type: "pipe", id: "pipe:P-100" });
    const anchor = projectLabelAnchor(authoredToLocal(index.entities.get(key)!.anchor!, renderOrigin), camera, width, height);
    expect(anchor.x).toBeCloseTo(462); expect(anchor.y).toBeCloseTo(270); expect(anchor.inFrustum).toBe(true);
    const rects = projectLabelPickTargets({ primitives, camera, width, height,
      hiddenKeys: new Set(), actualOdRadiusByPipe: new Map() });
    const placement = placeMeasuredLabel({ ...anchor, width: 58, height: 32 }, { width, height }, [], rects);
    expect(placement.rect).not.toBeNull();
    expect(placement.reasons).toEqual([]);
    expect(rects.every((rect) => !labelRectsOverlap(placement.rect!, rect))).toBe(true);
    const canvas = { getBoundingClientRect: () => ({ left: 0, top: 0, width, height }),
      clientWidth: width, clientHeight: height } as HTMLCanvasElement;
    let hits = 0, ownHits = 0;
    for (let y = 0; y <= height; y += 4) for (let x = 0; x <= width; x += 4) {
      const hit = pickPointPrimitive(primitives, { index, renderOrigin, camera, canvas, clientX: x, clientY: y });
      if (!hit) continue;
      hits++; if (entityKey(hit) === key) ownHits++;
      expect(rects.some((r) => x >= r.left && x <= r.right && y >= r.top && y <= r.bottom)).toBe(true);
    }
    expect(hits).toBeGreaterThan(0); expect(ownHits).toBeGreaterThan(0);
  });

});
