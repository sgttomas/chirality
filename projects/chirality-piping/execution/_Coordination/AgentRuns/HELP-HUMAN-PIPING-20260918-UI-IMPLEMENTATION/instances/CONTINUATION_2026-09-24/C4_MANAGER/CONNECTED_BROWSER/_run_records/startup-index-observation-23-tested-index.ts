import type { LabelRect } from "./labelPlacement";

const CELL_SIZE = 64;
const MAX_CELLS = 256;

type CollisionEntry = {
  readonly rect: LabelRect;
  lastQuery: object | null;
};

export function labelRectsOverlap(a: LabelRect, b: LabelRect): boolean {
  return a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;
}

function validRect(rect: LabelRect): boolean {
  return [rect.left, rect.top, rect.right, rect.bottom].every(Number.isFinite) &&
    rect.left <= rect.right && rect.top <= rect.bottom;
}

/**
 * CSS broad phase shared across all plates in one layout. Every inserted rectangle
 * is copied/validated once. At most 256 grid references per rectangle/query;
 * oversized rectangles use a fallback list. Dense cells or oversized queries can
 * still scan all obstacles: this is not a worst-case sublinear packing guarantee.
 */
export class LabelCollisionIndex {
  private readonly cells = new Map<string, CollisionEntry[]>();
  private readonly oversized: CollisionEntry[] = [];
  private readonly all: CollisionEntry[] = [];
  private invalid = false;
  private __stats: Record<string, number> | null = null;

  constructor(rectangles: readonly LabelRect[] = []) {
    const observations = (globalThis as any).__c4IndexObservation as unknown[] | undefined;
    if (observations) {
      this.__stats = { initialRectangles: rectangles.length, queries: 0, invalidQueries: 0, allTests: 0, oversizedTests: 0, cells: 0, maxBucket: 0, bucketEntries: 0, visits: 0, duplicateSkips: 0, narrowTests: 0, normalHits: 0 };
      observations.push(this.__stats);
    }
    for (const rect of rectangles) this.insert(rect);
  }

  get valid(): boolean { return !this.invalid; }

  insert(rect: LabelRect): void {
    if (!validRect(rect)) { this.invalid = true; return; }
    const snapshot = { ...rect };
    const entry: CollisionEntry = { rect: snapshot, lastQuery: null };
    this.all.push(entry);
    const keys = cellKeys(snapshot);
    if (keys === null) { this.oversized.push(entry); return; }
    for (const key of keys) {
      const bucket = this.cells.get(key);
      if (bucket) bucket.push(entry);
      else this.cells.set(key, [entry]);
    }
  }

  overlaps(rect: LabelRect): boolean {
    // Invalid obstacles/queries must never become an accidental clear placement.
    const stats = this.__stats; if (stats) stats.queries++;
    if (this.invalid || !validRect(rect)) { if (stats) stats.invalidQueries++; return true; }
    const keys = cellKeys(rect);
    if (keys === null) return this.all.some((other) => { if (stats) stats.allTests++; return labelRectsOverlap(rect, other.rect); });
    if (this.oversized.some((other) => { if (stats) stats.oversizedTests++; return labelRectsOverlap(rect, other.rect); })) return true;
    // A fresh identity cannot collide with markers retained by earlier queries.
    // Buckets share private entries; caller rectangles are never marked.
    const query = {};
    for (const key of keys) {
      const bucket = this.cells.get(key) ?? [];
      if (stats) { stats.cells++; stats.maxBucket = Math.max(stats.maxBucket, bucket.length); stats.bucketEntries += bucket.length; }
      for (const other of bucket) {
        if (stats) stats.visits++;
        if (other.lastQuery === query) { if (stats) stats.duplicateSkips++; continue; }
        other.lastQuery = query;
        if (stats) stats.narrowTests++;
        if (labelRectsOverlap(rect, other.rect)) { if (stats) stats.normalHits++; return true; }
      }
    }
    return false;
  }
}

function cellKeys(rect: LabelRect): string[] | null {
  const left = Math.floor(rect.left / CELL_SIZE);
  const top = Math.floor(rect.top / CELL_SIZE);
  // Including the far edge is conservative and preserves exact edge semantics
  // in the narrow-phase overlap predicate.
  const right = Math.floor(rect.right / CELL_SIZE);
  const bottom = Math.floor(rect.bottom / CELL_SIZE);
  if (![left, top, right, bottom].every(Number.isSafeInteger)) return null;
  const columns = right - left + 1;
  const rows = bottom - top + 1;
  if (columns * rows > MAX_CELLS) return null;
  const keys: string[] = [];
  for (let y = 0; y < rows; y++) for (let x = 0; x < columns; x++) keys.push(`${left + x}:${top + y}`);
  return keys;
}
