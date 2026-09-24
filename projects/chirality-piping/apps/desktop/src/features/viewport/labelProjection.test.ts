import { describe, expect, it } from "vitest";
import * as THREE from "three";
import type { PreviewModel } from "../../types";
import { buildModelIndex } from "../workspace/modelIndex";
import { entityKey } from "../workspace/selectionState";
import { authoredToLocal, pickPointPrimitive, pointPickPrimitives, type PointPickPrimitive } from "./viewportSelection";
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
    expect(target(primitive(), camera).length).toBe(1);
    // A homogeneous rescaling denotes exactly the same affine transform.
    // Check normalization explicitly, independent of THREE version rounding.
    camera.matrixWorldInverse.multiplyScalar(2);
    const equivalent = projectLabelAnchor(origin, camera, width, height);
    expect(equivalent.inFrustum).toBe(true);
    expect(equivalent.x).toBeCloseTo(projected.x);
    expect(equivalent.y).toBeCloseTo(projected.y);
    expect(target(primitive(), camera).length).toBe(1);
    camera.matrixWorldInverse.elements[3] = 1e-8;
    expect(() => target(primitive(), camera)).toThrow(/camera/);
  });

  it("retains an offscreen-endpoint capsule crossing the canvas and expands actual OD", () => {
    const p = { ...primitive(), start: { x: -100, y: 0, z: 0 }, end: { x: 100, y: 0, z: 0 } };
    const [rect] = target(p);
    expect(rect.left).toBe(0); expect(rect.right).toBe(width);
    expect(rect.top).toBeLessThan(194); expect(rect.bottom).toBeGreaterThan(206);
    const [thick] = target(p, cameraAt(), 1);
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
});
