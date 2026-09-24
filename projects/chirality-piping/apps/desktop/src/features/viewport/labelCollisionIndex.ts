import type { LabelRect } from "./labelPlacement";

// A 16px partition is comparable to picking diameters and half a typical plate
// height, reducing coarse-cell candidates; oversized entries retain the fallback.
const CELL_SIZE = 16;
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

  constructor(rectangles: readonly LabelRect[] = []) {
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
    if (this.invalid || !validRect(rect)) return true;
    const keys = cellKeys(rect);
    if (keys === null) return this.all.some((other) => labelRectsOverlap(rect, other.rect));
    if (this.oversized.some((other) => labelRectsOverlap(rect, other.rect))) return true;
    // A fresh identity cannot collide with markers retained by earlier queries.
    // Buckets share private entries; caller rectangles are never marked.
    const query = {};
    for (const key of keys) {
      for (const other of this.cells.get(key) ?? []) {
        if (other.lastQuery === query) continue;
        other.lastQuery = query;
        if (labelRectsOverlap(rect, other.rect)) return true;
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
