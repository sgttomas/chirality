// <stdin>
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import * as THREE3 from "three";

// projects/chirality-piping/apps/desktop/src/features/workspace/selectionState.ts
function entityKey(ref) {
  return JSON.stringify([ref.type, ref.id]);
}

// projects/chirality-piping/apps/desktop/src/features/workspace/modelIndex.ts
var CHUNK_SIZE = 128;
function buildModelIndex(model2, sessionGeneration, modelRevision) {
  const entities = /* @__PURE__ */ new Map();
  const labels = /* @__PURE__ */ new Map();
  const treeChildren = /* @__PURE__ */ new Map();
  const pipeKeysByNode = /* @__PURE__ */ new Map();
  const sectionBindings = /* @__PURE__ */ new Map();
  const visibilityEligibleKeys = /* @__PURE__ */ new Set();
  const invalidGeometry = /* @__PURE__ */ new Map();
  const projectRef = { type: "project", id: model2.project.id };
  const projectKey = entityKey(projectRef);
  const treeOrder = [projectKey];
  const spatialEntries = [];
  const add = (ref, label2, record, geometryBounds2 = null, anchor2 = null, geometryIssue = null) => {
    const key2 = entityKey(ref);
    const frozenAnchor = anchor2 ? freezeVec(anchor2) : null;
    const entry = Object.freeze({
      key: key2,
      ref: Object.freeze({ ...ref }),
      label: label2,
      record,
      parentKey: ref.type === "project" ? null : projectKey,
      geometryBounds: geometryBounds2,
      anchor: frozenAnchor,
      geometryIssue
    });
    if (!entities.has(key2)) {
      entities.set(key2, entry);
      labels.set(key2, label2);
      if (ref.type !== "project") {
        treeOrder.push(key2);
        const children = treeChildren.get(projectKey) ?? [];
        children.push(key2);
        treeChildren.set(projectKey, children);
      }
    }
    if (geometryIssue) invalidGeometry.set(key2, geometryIssue);
    if (geometryBounds2 && !geometryIssue) {
      visibilityEligibleKeys.add(key2);
      spatialEntries.push({ key: key2, bounds: geometryBounds2 });
    }
    return key2;
  };
  add(projectRef, model2.project.name || model2.project.id, model2);
  for (const material of model2.materials ?? []) {
    add({ type: "material", id: material.id }, material.label || material.id, material);
  }
  const duplicateSectionIds = duplicateIds(model2.sections ?? []);
  const uniqueSections = new Map(
    (model2.sections ?? []).filter((section) => !duplicateSectionIds.has(section.id)).map((section) => [section.id, section])
  );
  for (const section of model2.sections ?? []) {
    add({ type: "section", id: section.id }, section.name || section.id, section);
  }
  const duplicateNodeIds = duplicateIds(model2.nodes);
  const duplicatePipeIds = duplicateIds(model2.pipe_segments);
  const duplicateSupportIds = duplicateIds(model2.supports);
  const duplicateComponentIds = duplicateIds(model2.components);
  const nodesById = new Map(
    model2.nodes.filter((node) => !duplicateNodeIds.has(node.id) && authoredPointDisplayIssue(node.position) === null).map((node) => [node.id, node])
  );
  for (const node of model2.nodes) {
    const issue = duplicateNodeIds.has(node.id) ? `Node ${node.id} has a duplicate same-type identifier; its authored geometry is ambiguous.` : authoredPointDisplayIssue(node.position);
    const bounds = issue ? null : pointBounds(node.position);
    add({ type: "node", id: node.id }, node.label || node.id, node, bounds, issue ? null : node.position, issue);
  }
  for (const pipe of model2.pipe_segments) {
    const from = nodesById.get(pipe.from)?.position;
    const to = nodesById.get(pipe.to)?.position;
    let issue = null;
    if (duplicatePipeIds.has(pipe.id)) {
      issue = `Pipe ${pipe.id} has a duplicate same-type identifier; its authored geometry is ambiguous.`;
    } else if (duplicateNodeIds.has(pipe.from) || duplicateNodeIds.has(pipe.to)) {
      issue = `Pipe ${pipe.id} references an ambiguous duplicate node endpoint.`;
    } else if (!from || !to) issue = `Pipe ${pipe.id} references a missing or viewport-unrepresentable endpoint.`;
    else if (!finiteVec(from) || !finiteVec(to)) issue = `Pipe ${pipe.id} has a non-finite endpoint.`;
    else if (!finiteNumber(distanceSquared(from, to)) || distanceSquared(from, to) <= 0) {
      issue = `Pipe ${pipe.id} has an unrepresentable or zero authored span.`;
    }
    const bounds = issue || !from || !to ? null : boundsFromPoints([from, to]);
    const anchor2 = issue || !from || !to ? null : midpoint(from, to);
    const pipeKey = add({ type: "pipe", id: pipe.id }, pipe.label || pipe.id, pipe, bounds, anchor2, issue);
    for (const endpointId of [pipe.from, pipe.to]) {
      const nodeKey = entityKey({ type: "node", id: endpointId });
      const adjacent = pipeKeysByNode.get(nodeKey) ?? [];
      adjacent.push(pipeKey);
      pipeKeysByNode.set(nodeKey, adjacent);
    }
    const hasSectionRef = pipe.section_ref !== void 0;
    const sectionRef = pipe.section_ref?.trim() ?? "";
    const sectionKey = sectionRef ? entityKey({ type: "section", id: sectionRef }) : null;
    const sharedSection = sectionRef ? uniqueSections.get(sectionRef) : null;
    const shared = sharedSection && sectionKey ? entities.get(sectionKey) : null;
    const sectionIssue = !hasSectionRef ? null : !sectionRef ? `Pipe ${pipe.id} has a blank shared section reference.` : duplicateSectionIds.has(sectionRef) ? `Pipe ${pipe.id} references duplicate shared section ${sectionRef}.` : !sharedSection || !shared ? `Pipe ${pipe.id} references missing shared section ${sectionRef}.` : sharedSection.section_type !== "pipe" ? `Pipe ${pipe.id} references shared section ${sectionRef} with unsupported type ${sharedSection.section_type}.` : sharedSectionBindingIssue(pipe, sharedSection);
    sectionBindings.set(pipeKey, Object.freeze({
      source: hasSectionRef ? "shared" : "inline",
      sectionKey: shared ? sectionKey : null,
      record: shared ? shared.record.properties : pipe.section,
      issue: sectionIssue
    }));
  }
  for (const support of model2.supports) {
    const position = nodesById.get(support.node)?.position;
    const issue = duplicateSupportIds.has(support.id) ? `Support ${support.id} has a duplicate same-type identifier; its authored geometry is ambiguous.` : duplicateNodeIds.has(support.node) ? `Support ${support.id} references an ambiguous duplicate node.` : !position ? `Support ${support.id} references a missing node.` : !finiteVec(position) ? `Support ${support.id} is anchored to a non-finite node.` : null;
    add(
      { type: "support", id: support.id },
      support.label || support.id,
      support,
      issue || !position ? null : pointBounds(position),
      issue ? null : position ?? null,
      issue
    );
  }
  for (const component of model2.components) {
    const position = nodesById.get(component.node)?.position;
    const issue = duplicateComponentIds.has(component.id) ? `Component ${component.id} has a duplicate same-type identifier; its authored geometry is ambiguous.` : duplicateNodeIds.has(component.node) ? `Component ${component.id} references an ambiguous duplicate node.` : !position ? `Component ${component.id} references a missing node.` : !finiteVec(position) ? `Component ${component.id} is anchored to a non-finite node.` : null;
    add(
      { type: "component", id: component.id },
      component.label || component.id,
      component,
      issue || !position ? null : pointBounds(position),
      issue ? null : position ?? null,
      issue
    );
  }
  for (const load of model2.load_cases) {
    add({ type: "load", id: load.id }, load.label || load.id, load);
  }
  for (const combination of model2.combinations ?? []) {
    add({ type: "combination", id: combination.id }, combination.label || combination.id, combination);
  }
  model2.diagnostics.forEach((diagnostic, index2) => {
    const id = diagnostic.id ?? `${diagnostic.code}:${index2}`;
    add({ type: "diagnostic", id }, diagnostic.code, diagnostic);
  });
  const spatialChunks = chunkSpatialEntries(spatialEntries);
  const geometryBounds = unionBounds(spatialEntries.map((entry) => entry.bounds));
  for (const [key2, children] of treeChildren) treeChildren.set(key2, Object.freeze([...children]));
  for (const [key2, adjacent] of pipeKeysByNode) pipeKeysByNode.set(key2, Object.freeze([...adjacent]));
  return Object.freeze({
    generation: `${sessionGeneration}:${modelRevision}`,
    sessionGeneration,
    modelRevision,
    projectKey,
    entities,
    labels,
    treeOrder: Object.freeze(treeOrder),
    treeChildren,
    pipeKeysByNode,
    sectionBindings,
    visibilityEligibleKeys,
    spatialChunks,
    geometryBounds,
    invalidGeometry,
    summaries: Object.freeze({
      entityCount: entities.size,
      nodeCount: model2.nodes.length,
      pipeCount: model2.pipe_segments.length,
      supportCount: model2.supports.length,
      componentCount: model2.components.length,
      invalidGeometryCount: invalidGeometry.size
    })
  });
}
function boundsFromPoints(points) {
  if (points.length === 0 || points.some((point) => !finiteVec(point))) return null;
  const min = { ...points[0] };
  const max = { ...points[0] };
  for (const point of points.slice(1)) {
    min.x = Math.min(min.x, point.x);
    min.y = Math.min(min.y, point.y);
    min.z = Math.min(min.z, point.z);
    max.x = Math.max(max.x, point.x);
    max.y = Math.max(max.y, point.y);
    max.z = Math.max(max.z, point.z);
  }
  return freezeBounds({ min, max });
}
function pointBounds(point) {
  return freezeBounds({ min: point, max: point });
}
function chunkSpatialEntries(entries) {
  const overall = unionBounds(entries.map((entry) => entry.bounds));
  const span = overall ? Math.max(
    overall.max.x - overall.min.x,
    overall.max.y - overall.min.y,
    overall.max.z - overall.min.z,
    1
  ) : 1;
  const cell = span / Math.max(1, Math.ceil(Math.cbrt(entries.length / CHUNK_SIZE)));
  const spatial = [...entries].sort((a, b) => {
    const ac = boundsCenter(a.bounds);
    const bc = boundsCenter(b.bounds);
    const ax = Math.floor((ac.x - (overall?.min.x ?? 0)) / cell);
    const bx = Math.floor((bc.x - (overall?.min.x ?? 0)) / cell);
    if (ax !== bx) return ax - bx;
    const ay = Math.floor((ac.y - (overall?.min.y ?? 0)) / cell);
    const by = Math.floor((bc.y - (overall?.min.y ?? 0)) / cell);
    if (ay !== by) return ay - by;
    const az = Math.floor((ac.z - (overall?.min.z ?? 0)) / cell);
    const bz = Math.floor((bc.z - (overall?.min.z ?? 0)) / cell);
    return az !== bz ? az - bz : String(a.key).localeCompare(String(b.key));
  });
  const chunks = [];
  for (let offset = 0; offset < spatial.length; offset += CHUNK_SIZE) {
    const slice = spatial.slice(offset, offset + CHUNK_SIZE);
    const bounds = unionBounds(slice.map((entry) => entry.bounds));
    if (!bounds) continue;
    chunks.push(Object.freeze({
      id: chunks.length,
      bounds,
      entityKeys: Object.freeze(slice.map((entry) => entry.key))
    }));
  }
  return Object.freeze(chunks);
}
function duplicateIds(items) {
  const counts = /* @__PURE__ */ new Map();
  for (const item of items) counts.set(item.id, (counts.get(item.id) ?? 0) + 1);
  return new Set([...counts].filter(([, count]) => count > 1).map(([id]) => id));
}
function boundsCenter(bounds) {
  return {
    x: safeMidpoint(bounds.min.x, bounds.max.x),
    y: safeMidpoint(bounds.min.y, bounds.max.y),
    z: safeMidpoint(bounds.min.z, bounds.max.z)
  };
}
function sharedSectionBindingIssue(pipe, section) {
  const definedKeys = Object.keys(section.properties).filter((key2) => section.properties[key2] !== void 0);
  if (definedKeys.some((key2) => key2 !== "outside_diameter" && key2 !== "wall_thickness")) {
    return `Shared section ${section.id} contains unsupported properties for Actual OD resolution.`;
  }
  const outside = section.properties.outside_diameter;
  const wall = section.properties.wall_thickness;
  if (!validPositiveQuantity(outside) || !validPositiveQuantity(wall)) {
    return `Shared section ${section.id} has an invalid OD or wall-thickness envelope.`;
  }
  const inlineOutside = pipe.section.outside_diameter;
  const inlineWall = pipe.section.wall_thickness;
  if (!validPositiveQuantity(inlineOutside) || !validPositiveQuantity(inlineWall)) {
    return `Pipe ${pipe.id} has no explicit valid inline OD/wall values to verify against shared section ${section.id}.`;
  }
  return null;
}
function validPositiveQuantity(value) {
  return Boolean(value && Number.isFinite(value.value) && value.value > 0 && value.unit.trim());
}
function unionBounds(bounds) {
  if (bounds.length === 0) return null;
  return boundsFromPoints(bounds.flatMap((item) => [item.min, item.max]));
}
function freezeBounds(bounds) {
  return Object.freeze({ min: freezeVec(bounds.min), max: freezeVec(bounds.max) });
}
function freezeVec(value) {
  return Object.freeze({ x: value.x, y: value.y, z: value.z });
}
function finiteVec(value) {
  return finiteNumber(value.x) && finiteNumber(value.y) && finiteNumber(value.z);
}
function finiteNumber(value) {
  return Number.isFinite(value);
}
function distanceSquared(a, b) {
  const x = b.x - a.x;
  const y = b.y - a.y;
  const z = b.z - a.z;
  return x * x + y * y + z * z;
}
function midpoint(a, b) {
  return { x: safeMidpoint(a.x, b.x), y: safeMidpoint(a.y, b.y), z: safeMidpoint(a.z, b.z) };
}
function safeMidpoint(left, right) {
  return left / 2 + right / 2;
}
function authoredPointDisplayIssue(point) {
  if (!finiteVec(point)) return "Authored node has a non-finite coordinate.";
  if (![point.x, point.y, point.z].every((value) => Number.isFinite(Math.fround(value)))) {
    return "Authored node coordinate exceeds the viewport Float32 presentation range.";
  }
  return null;
}

// projects/chirality-piping/apps/desktop/src/features/viewport/viewportSelection.ts
import * as THREE from "three";
function authoredToLocal(authored, origin2) {
  const local = {
    x: authored.x - origin2.x,
    y: authored.y - origin2.y,
    z: authored.z - origin2.z
  };
  if (!finiteVec2(authored) || !finiteVec2(origin2) || !finiteVec2(local)) {
    throw new Error("Authored coordinate cannot be represented in the viewport.");
  }
  return local;
}
function pointPickPrimitives(index2, model2, origin2) {
  const order = new Map(index2.treeOrder.map((key2, position) => [key2, position]));
  const nodes = new Map(model2.nodes.map((node) => [node.id, node.position]));
  const primitives2 = [];
  for (const pipe of model2.pipe_segments) {
    const key2 = entityKeyFor("pipe", pipe.id);
    const from = nodes.get(pipe.from);
    const to = nodes.get(pipe.to);
    if (!from || !to || index2.invalidGeometry.has(key2)) continue;
    primitives2.push(freezePrimitive({
      key: key2,
      ref: { type: "pipe", id: pipe.id },
      kind: "pipe",
      shape: "capsule",
      center: authoredToLocal(midpoint2(from, to), origin2),
      start: authoredToLocal(from, origin2),
      end: authoredToLocal(to, origin2),
      radius: 0.052,
      height: 0,
      displayOrder: order.get(key2) ?? Number.MAX_SAFE_INTEGER
    }));
  }
  for (const node of model2.nodes) {
    const key2 = entityKeyFor("node", node.id);
    if (index2.invalidGeometry.has(key2)) continue;
    primitives2.push(freezePrimitive({
      key: key2,
      ref: { type: "node", id: node.id },
      kind: "node",
      shape: "sphere",
      center: authoredToLocal(node.position, origin2),
      start: null,
      end: null,
      radius: 0.095,
      height: 0,
      displayOrder: order.get(key2) ?? Number.MAX_SAFE_INTEGER
    }));
  }
  for (const support of model2.supports) {
    const key2 = entityKeyFor("support", support.id);
    const node = nodes.get(support.node);
    if (!node || index2.invalidGeometry.has(key2)) continue;
    primitives2.push(freezePrimitive({
      key: key2,
      ref: { type: "support", id: support.id },
      kind: "support",
      shape: "cone",
      center: authoredToLocal({ x: node.x, y: node.y - 0.26, z: node.z }, origin2),
      start: null,
      end: null,
      radius: 0.18,
      height: 0.34,
      displayOrder: order.get(key2) ?? Number.MAX_SAFE_INTEGER
    }));
  }
  for (const component of model2.components) {
    const key2 = entityKeyFor("component", component.id);
    const node = nodes.get(component.node);
    if (!node || index2.invalidGeometry.has(key2)) continue;
    primitives2.push(freezePrimitive({
      key: key2,
      ref: { type: "component", id: component.id },
      kind: "component",
      shape: "sphere",
      center: authoredToLocal({ x: node.x, y: node.y + 0.2, z: node.z }, origin2),
      start: null,
      end: null,
      radius: componentPickExtent(component),
      height: 0,
      displayOrder: order.get(key2) ?? Number.MAX_SAFE_INTEGER
    }));
  }
  return Object.freeze(primitives2);
}
function safeMidpoint2(min, max) {
  return min / 2 + max / 2;
}
function midpoint2(a, b) {
  return {
    x: safeMidpoint2(a.x, b.x),
    y: safeMidpoint2(a.y, b.y),
    z: safeMidpoint2(a.z, b.z)
  };
}
function finiteVec2(value) {
  return Number.isFinite(value.x) && Number.isFinite(value.y) && Number.isFinite(value.z);
}
function freezeVec2(value) {
  return Object.freeze({ x: value.x, y: value.y, z: value.z });
}
function freezePrimitive(primitive) {
  return Object.freeze({
    ...primitive,
    ref: Object.freeze({ ...primitive.ref }),
    center: freezeVec2(primitive.center),
    start: primitive.start ? freezeVec2(primitive.start) : null,
    end: primitive.end ? freezeVec2(primitive.end) : null
  });
}
function entityKeyFor(type, id) {
  return JSON.stringify([type, id]);
}
function componentPickExtent(component) {
  if (["bend", "elbow", "branch", "tee", "branch_connection"].includes(component.kind)) return 0.3;
  if (["valve", "flange", "reducer", "rigid", "specialty", "expansion_joint"].includes(component.kind)) return 0.25;
  return Math.hypot(0.12, 0.12, 0.12);
}
var PICK_TYPE_ORDER = Object.freeze({
  component: 0,
  support: 1,
  node: 2,
  pipe: 3
});

// projects/chirality-piping/apps/desktop/src/features/viewport/labelProjection.ts
import * as THREE2 from "three";
var finitePoint = (p) => [p.x, p.y, p.z].every(Number.isFinite);
var vector = (p) => new THREE2.Vector3(p.x, p.y, p.z);
function validCamera(camera2, width2, height2) {
  const p = camera2.projectionMatrix.elements;
  const v2 = camera2.matrixWorldInverse.elements;
  if (![width2, height2, camera2.near, camera2.far, camera2.fov, ...p, ...v2].every(Number.isFinite) || width2 <= 0 || height2 <= 0 || camera2.near <= 0 || camera2.far <= camera2.near || camera2.fov <= 0 || camera2.fov >= 180 || p[0] <= 0 || p[5] <= 0 || p[1] !== 0 || p[2] !== 0 || p[3] !== 0 || p[4] !== 0 || p[6] !== 0 || p[7] !== 0 || p[11] !== -1 || p[12] !== 0 || p[13] !== 0 || p[15] !== 0 || v2[3] !== 0 || v2[7] !== 0 || v2[11] !== 0 || v2[15] === 0) return false;
  const axes = [
    new THREE2.Vector3(v2[0], v2[1], v2[2]),
    new THREE2.Vector3(v2[4], v2[5], v2[6]),
    new THREE2.Vector3(v2[8], v2[9], v2[10])
  ].map((axis) => axis.divideScalar(v2[15]));
  return axes.every((axis) => Math.abs(axis.lengthSq() - 1) < 1e-10) && Math.abs(axes[0].dot(axes[1])) < 1e-10 && Math.abs(axes[0].dot(axes[2])) < 1e-10 && Math.abs(axes[1].dot(axes[2])) < 1e-10;
}
function projectLabelAnchor(anchor2, camera2, width2, height2) {
  const invalid = { x: 0, y: 0, inFrustum: false };
  if (!finitePoint(anchor2) || !validCamera(camera2, width2, height2)) return invalid;
  const view = vector(anchor2).applyMatrix4(camera2.matrixWorldInverse);
  if (!finitePoint(view) || view.z >= 0) return invalid;
  const projected2 = view.clone().applyMatrix4(camera2.projectionMatrix);
  const x = (projected2.x + 1) * width2 / 2;
  const y = (1 - projected2.y) * height2 / 2;
  if (![x, y, projected2.z].every(Number.isFinite)) return invalid;
  return { x, y, inFrustum: -view.z >= camera2.near && -view.z <= camera2.far && Math.abs(projected2.x) <= 1 && Math.abs(projected2.y) <= 1 && Math.abs(projected2.z) <= 1 };
}
function projectLabelPickTargets(input) {
  const { camera: camera2, width: width2, height: height2 } = input;
  if (!validCamera(camera2, width2, height2)) throw new Error("Invalid label projection camera or CSS dimensions.");
  const rectangles = [];
  for (const primitive of input.primitives) {
    if (input.hiddenKeys.has(primitive.key)) continue;
    const od = primitive.kind === "pipe" ? input.actualOdRadiusByPipe.get(primitive.key) ?? 0 : 0;
    if (!finitePoint(primitive.center) || ![primitive.radius, primitive.height, od].every(Number.isFinite) || primitive.radius < 0 || primitive.height < 0 || od < 0 || primitive.shape === "capsule" && (!primitive.start || !primitive.end || !finitePoint(primitive.start) || !finitePoint(primitive.end))) {
      throw new Error(`Invalid label pick geometry: ${primitive.key}`);
    }
    const points = primitive.shape === "capsule" ? [primitive.start, primitive.end] : [primitive.center];
    const depth = Math.max(...points.map((point) => -vector(point).applyMatrix4(camera2.matrixWorldInverse).z));
    if (!Number.isFinite(depth)) throw new Error("Unrepresentable label pick depth.");
    if (depth <= 0) continue;
    const radius = Math.max(
      primitive.radius,
      od,
      6 * (2 * depth * Math.tan(THREE2.MathUtils.degToRad(camera2.fov) / 2)) / height2
    );
    const world = new THREE2.Box3().setFromPoints(points.map(vector));
    const expansion = primitive.shape === "cone" ? new THREE2.Vector3(radius, primitive.height / 2, radius) : new THREE2.Vector3(radius, radius, radius);
    world.min.sub(expansion);
    world.max.add(expansion);
    const view = new THREE2.Box3();
    for (const x of [world.min.x, world.max.x]) for (const y of [world.min.y, world.max.y])
      for (const z of [world.min.z, world.max.z]) {
        const corner = new THREE2.Vector3(x, y, z).applyMatrix4(camera2.matrixWorldInverse);
        if (!finitePoint(corner)) throw new Error("Unrepresentable label pick envelope.");
        view.expandByPoint(corner);
      }
    view.min.z = Math.max(view.min.z, -camera2.far);
    view.max.z = Math.min(view.max.z, -camera2.near);
    if (view.min.z > view.max.z) continue;
    let left = Infinity, right = -Infinity, top = Infinity, bottom = -Infinity;
    for (const x of [view.min.x, view.max.x]) for (const y of [view.min.y, view.max.y])
      for (const z of [view.min.z, view.max.z]) {
        const p = new THREE2.Vector3(x, y, z).applyMatrix4(camera2.projectionMatrix);
        const sx = (p.x + 1) * width2 / 2, sy = (1 - p.y) * height2 / 2;
        if (![sx, sy].every(Number.isFinite)) throw new Error("Unrepresentable label pick projection.");
        left = Math.min(left, sx);
        right = Math.max(right, sx);
        top = Math.min(top, sy);
        bottom = Math.max(bottom, sy);
      }
    const guard = 1e-7 * Math.max(1, width2, height2);
    left = Math.max(0, left - guard);
    right = Math.min(width2, right + guard);
    top = Math.max(0, top - guard);
    bottom = Math.min(height2, bottom + guard);
    if (left <= right && top <= bottom) rectangles.push(Object.freeze({ left, right, top, bottom }));
  }
  return Object.freeze(rectangles);
}

// projects/chirality-piping/apps/desktop/src/features/viewport/labelCollisionIndex.ts
var CELL_SIZE = 64;
var MAX_CELLS = 256;
function labelRectsOverlap(a, b) {
  return a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;
}
function validRect(rect) {
  return [rect.left, rect.top, rect.right, rect.bottom].every(Number.isFinite) && rect.left <= rect.right && rect.top <= rect.bottom;
}
var LabelCollisionIndex = class {
  cells = /* @__PURE__ */ new Map();
  oversized = [];
  all = [];
  invalid = false;
  constructor(rectangles = []) {
    for (const rect of rectangles) this.insert(rect);
  }
  get valid() {
    return !this.invalid;
  }
  insert(rect) {
    if (!validRect(rect)) {
      this.invalid = true;
      return;
    }
    const snapshot = { ...rect };
    this.all.push(snapshot);
    const keys = cellKeys(snapshot);
    if (keys === null) {
      this.oversized.push(snapshot);
      return;
    }
    for (const key2 of keys) {
      const bucket = this.cells.get(key2);
      if (bucket) bucket.push(snapshot);
      else this.cells.set(key2, [snapshot]);
    }
  }
  overlaps(rect) {
    if (this.invalid || !validRect(rect)) return true;
    const keys = cellKeys(rect);
    if (keys === null) return this.all.some((other) => labelRectsOverlap(rect, other));
    if (this.oversized.some((other) => labelRectsOverlap(rect, other))) return true;
    const seen = /* @__PURE__ */ new Set();
    for (const key2 of keys) {
      for (const other of this.cells.get(key2) ?? []) {
        if (seen.has(other)) continue;
        seen.add(other);
        if (labelRectsOverlap(rect, other)) return true;
      }
    }
    return false;
  }
};
function cellKeys(rect) {
  const left = Math.floor(rect.left / CELL_SIZE);
  const top = Math.floor(rect.top / CELL_SIZE);
  const right = Math.floor(rect.right / CELL_SIZE);
  const bottom = Math.floor(rect.bottom / CELL_SIZE);
  if (![left, top, right, bottom].every(Number.isSafeInteger)) return null;
  const columns = right - left + 1;
  const rows = bottom - top + 1;
  if (columns * rows > MAX_CELLS) return null;
  const keys = [];
  for (let y = 0; y < rows; y++) for (let x = 0; x < columns; x++) keys.push(`${left + x}:${top + y}`);
  return keys;
}

// projects/chirality-piping/apps/desktop/src/features/viewport/labelPlacement.ts
function placeMeasuredLabel(label2, canvas, occupied, pickTargets, preferredCenter) {
  return placeWithIndexes(label2, canvas, new LabelCollisionIndex(occupied), new LabelCollisionIndex(pickTargets), preferredCenter);
}
function placeWithIndexes(label2, canvas, occupied, pickTargets, preferredCenter) {
  if (![label2.x, label2.y, label2.width, label2.height, canvas.width, canvas.height].every(Number.isFinite) || label2.width <= 0 || label2.height <= 0 || canvas.width < 0 || canvas.height < 0) {
    return { rect: null, reasons: ["invalid-measurement"] };
  }
  if (!occupied.valid || !pickTargets.valid) {
    return { rect: null, reasons: ["invalid-obstacle"] };
  }
  if (!label2.inFrustum || label2.x < 0 || label2.x > canvas.width || label2.y < 0 || label2.y > canvas.height) return { rect: null, reasons: ["outside-frustum"] };
  const reasons = /* @__PURE__ */ new Set();
  const boxAt = ({ x, y }) => ({
    left: x - label2.width / 2,
    right: x + label2.width / 2,
    top: y - label2.height / 2,
    bottom: y + label2.height / 2
  });
  const contained = (rect) => rect.left >= 0 && rect.top >= 0 && rect.right <= canvas.width && rect.bottom <= canvas.height;
  const preferred = preferredCenter && Number.isFinite(preferredCenter.x) && Number.isFinite(preferredCenter.y) && contained(boxAt(preferredCenter)) ? preferredCenter : void 0;
  const centers = preferred ? [preferred] : [];
  const directions2 = [[1, -1], [1, 1], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [-1, 0]];
  for (const ring of [1, 2, 3]) {
    for (const [dx, dy] of directions2) {
      const x = label2.x + dx * (label2.width / 2 + 4 + (ring - 1) * (label2.width + 4));
      const y = label2.y + dy * (label2.height / 2 + 4 + (ring - 1) * (label2.height + 4));
      if (preferred?.x === x && preferred.y === y) continue;
      if (centers.length < 24) centers.push({ x, y });
    }
  }
  for (const center of centers) {
    const rect = boxAt(center);
    if (![rect.left, rect.top, rect.right, rect.bottom].every(Number.isFinite)) {
      reasons.add("invalid-measurement");
      continue;
    }
    let blocked = false;
    if (!contained(rect)) {
      reasons.add("containment");
      blocked = true;
    }
    if (occupied.overlaps(rect)) {
      reasons.add("collision");
      blocked = true;
    }
    if (pickTargets.overlaps(rect)) {
      reasons.add("picking");
      blocked = true;
    }
    if (!blocked) return { rect, reasons: [] };
  }
  return { rect: null, reasons: [...reasons] };
}

// <stdin>
var root = process.cwd();
var records = process.argv[2];
var read = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
var sha = (p) => crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
var modelPath = path.join(root, "projects/chirality-piping/fixtures/product_preview/invented_preview_model.json");
var model = read(modelPath);
var index = buildModelIndex(model, 1, 1);
var d = read(path.join(records, "dist-content-diagnostic-15-before-selected-pipe-keyboard-measurement.json"));
var v = d.snapshot.viewport;
var c = v.camera;
var origin = { x: c.localRenderOrigin[0], y: c.localRenderOrigin[1], z: c.localRenderOrigin[2] };
var width = v.canvas.cssWidth;
var height = v.canvas.cssHeight;
var camera = new THREE3.PerspectiveCamera(c.fovDegrees, c.aspect, c.near, c.far);
camera.position.fromArray(c.position).sub(new THREE3.Vector3(...c.localRenderOrigin));
camera.up.fromArray(c.up);
camera.lookAt(new THREE3.Vector3(...c.target).sub(new THREE3.Vector3(...c.localRenderOrigin)));
camera.updateMatrixWorld();
var primitives = pointPickPrimitives(index, model, origin);
var exclusions = primitives.map((p) => ({ key: p.key, primitive: p, rects: projectLabelPickTargets({ primitives: [p], camera, width, height, hiddenKeys: /* @__PURE__ */ new Set(), actualOdRadiusByPipe: /* @__PURE__ */ new Map() }) }));
var key = JSON.stringify(["pipe", "pipe:P-100"]);
var dom = d.labels.find((x) => x.key === key);
var anchor = authoredToLocal(index.entities.get(key).anchor, origin);
var projected = projectLabelAnchor(anchor, camera, width, height);
var label = { ...projected, width: dom.rect.width, height: dom.rect.height };
var directions = [[1, -1], [1, 1], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [-1, 0]];
var candidates = [];
for (const ring of [1, 2, 3]) for (const [dx, dy] of directions) {
  const x = label.x + dx * (label.width / 2 + 4 + (ring - 1) * (label.width + 4)), y = label.y + dy * (label.height / 2 + 4 + (ring - 1) * (label.height + 4));
  const rect = { left: x - label.width / 2, right: x + label.width / 2, top: y - label.height / 2, bottom: y + label.height / 2 };
  candidates.push({ ring, dx, dy, rect, blockedBy: exclusions.filter((e) => e.rects.some((r) => labelRectsOverlap(rect, r))).map((e) => e.key) });
}
var sourcePaths = ["modelIndex.ts"].map(() => "projects/chirality-piping/apps/desktop/src/features/workspace/modelIndex.ts").concat(["viewportSelection.ts", "labelProjection.ts", "labelPlacement.ts", "labelCollisionIndex.ts"].map((x) => "projects/chirality-piping/apps/desktop/src/features/viewport/" + x));
var result = { kind: "offline reconstruction from exact observed camera/model/DOM dimensions; no browser or product mutation", sourceHashes: Object.fromEntries(sourcePaths.map((p) => [p, sha(path.join(root, p))])), modelHash: sha(modelPath), diagnosticHash: sha(path.join(records, "dist-content-diagnostic-15-before-selected-pipe-keyboard-measurement.json")), camera: c, width, height, label, dom, exclusions, candidates, all: placeMeasuredLabel(label, { width, height }, [], exclusions.flatMap((e) => e.rects)), withoutOwn: placeMeasuredLabel(label, { width, height }, [], exclusions.filter((e) => e.key !== key).flatMap((e) => e.rects)), byPrimitive: exclusions.map((e) => ({ key: e.key, result: placeMeasuredLabel(label, { width, height }, [], e.rects) })) };
fs.writeFileSync(path.join(records, "dist-content-projection-probe-result.json"), JSON.stringify(result, null, 2) + "\n");
console.log(JSON.stringify({ label, all: result.all, withoutOwn: result.withoutOwn, blockers: result.byPrimitive.filter((x) => !x.result.rect), candidateBlockers: candidates.map((x) => x.blockedBy) }, null, 2));
