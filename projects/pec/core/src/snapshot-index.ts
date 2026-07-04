/**
 * Per-snapshot derived index (PEC-NFR-003).
 *
 * The derivation layer (status.ts, conditions.ts) is called once per deliverable, and
 * naively re-scans snapshot arrays on every call — O(deliverables × work-items) overall.
 * This module memoizes a set of lookup structures ONCE per ProjectSnapshot so the inner
 * loops become O(1) map hits. It is keyed on snapshot identity (a fresh, effectively
 * immutable object is built per request in repo.snapshot) and re-validated by a cheap
 * structural fingerprint, so adding/removing rows on a reused snapshot recomputes.
 *
 * Membership is grouped by STRUCTURAL keys only (anchor, target, revision→deliverable).
 * State filters ('open'/'active') are applied at LOOKUP time on the small grouped lists,
 * so in-place field mutations (e.g. a hold going resolved) are reflected without a rebuild
 * and the results stay byte-identical to the original filter expressions.
 */

import type { Hold, HoldLink, ProjectSnapshot, WorkItem } from './types.ts'

interface SnapshotIndex {
  holdById: Map<number, Hold>
  /** `${targetType}:${targetId}` → hold links for that target, in snapshot order */
  holdLinksByTarget: Map<string, HoldLink[]>
  /** deliverableId → every work item in its sphere (anchored to it or any of its revisions), snapshot order, ALL states */
  sphereWorkItemsByDeliverable: Map<number, WorkItem[]>
  fingerprint: string
}

const CACHE = new WeakMap<ProjectSnapshot, SnapshotIndex>()

function fingerprint(snap: ProjectSnapshot): string {
  return `${snap.holds.length}:${snap.holdLinks.length}:${snap.workItems.length}:${snap.revisions.length}`
}

function build(snap: ProjectSnapshot): SnapshotIndex {
  const holdById = new Map<number, Hold>()
  for (const h of snap.holds) holdById.set(h.id, h)

  const holdLinksByTarget = new Map<string, HoldLink[]>()
  for (const l of snap.holdLinks) {
    const key = `${l.targetType}:${l.targetId}`
    const arr = holdLinksByTarget.get(key)
    if (arr) arr.push(l)
    else holdLinksByTarget.set(key, [l])
  }

  const deliverableIdByRevision = new Map<number, number>()
  for (const r of snap.revisions) deliverableIdByRevision.set(r.id, r.deliverableId)

  const sphereWorkItemsByDeliverable = new Map<number, WorkItem[]>()
  for (const w of snap.workItems) {
    let deliverableId: number | undefined
    if (w.anchorType === 'deliverable') deliverableId = w.anchorId
    else if (w.anchorType === 'revision') deliverableId = deliverableIdByRevision.get(w.anchorId)
    if (deliverableId == null) continue
    const arr = sphereWorkItemsByDeliverable.get(deliverableId)
    if (arr) arr.push(w)
    else sphereWorkItemsByDeliverable.set(deliverableId, [w])
  }

  return { holdById, holdLinksByTarget, sphereWorkItemsByDeliverable, fingerprint: fingerprint(snap) }
}

export function snapshotIndex(snap: ProjectSnapshot): SnapshotIndex {
  const cached = CACHE.get(snap)
  if (cached && cached.fingerprint === fingerprint(snap)) return cached
  const idx = build(snap)
  CACHE.set(snap, idx)
  return idx
}
