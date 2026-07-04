/**
 * Record-graph helpers around a deliverable's sphere — shared by the health rules
 * (status.ts) and the planning derivations (plan.ts) without a module cycle.
 */

import type { Deliverable, Hold, ProjectSnapshot, Revision, WorkItem } from './types.ts'
import { activeHoldsFor } from './conditions.ts'
import { snapshotIndex } from './snapshot-index.ts'

/** Latest non-superseded revision; falls back to the latest revision when all are superseded. */
export function currentRevision(snap: ProjectSnapshot, deliverableId: number): Revision | null {
  const revs = snap.revisions
    .filter((r) => r.deliverableId === deliverableId)
    .sort((a, b) => a.id - b.id)
  if (revs.length === 0) return null
  const live = revs.filter((r) => r.state !== 'superseded')
  return (live.length > 0 ? live[live.length - 1] : revs[revs.length - 1]) ?? null
}

/**
 * Open work items in a deliverable's sphere: anchored directly to the deliverable, or to
 * ANY of its revisions (I-1 — a work item on a prior/superseded revision is still the
 * deliverable's open work and must count toward its health, not vanish). Rollups still use
 * the primary anchor to avoid double counting (§13.4).
 */
export function openWorkItemsFor(snap: ProjectSnapshot, d: Deliverable, _rev: Revision | null): WorkItem[] {
  const sphere = snapshotIndex(snap).sphereWorkItemsByDeliverable.get(d.id)
  if (!sphere) return []
  return sphere.filter((w) => w.state === 'open' || w.state === 'in_work')
}

/** Active holds in the deliverable's sphere: the deliverable, its current revision, open items, conditions and checks on it. */
export function activeHoldsInSphere(snap: ProjectSnapshot, d: Deliverable, rev: Revision | null): Hold[] {
  const holds = new Map<number, Hold>()
  const add = (hs: Hold[]) => { for (const h of hs) holds.set(h.id, h) }
  add(activeHoldsFor(snap, 'deliverable', d.id))
  if (rev) {
    add(activeHoldsFor(snap, 'revision', rev.id))
    for (const c of snap.conditions.filter((x) => x.parentType === 'revision' && x.parentId === rev.id)) {
      add(activeHoldsFor(snap, 'condition', c.id))
    }
    for (const c of snap.checks.filter((x) => x.revisionId === rev.id)) {
      add(activeHoldsFor(snap, 'check', c.id))
    }
  }
  for (const w of openWorkItemsFor(snap, d, rev)) add(activeHoldsFor(snap, 'work_item', w.id))
  return [...holds.values()]
}
