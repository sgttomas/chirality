# Practitioner Harness — Development Backlog

> **Epistemic status: queued work — not authority, not a status surface.**
> Items here are candidate harness development, recorded so intent survives
> across sessions. Execution follows the established harness pattern: branch +
> PR, owner merges (PR #12/#13 precedent); any change that moves a pinned live
> measurement carries its conscious pin update in the same PR
> (`test_live_baseline.py`'s own convention). Remove an item by PR when done
> or when the owner declines it. Provenance: bridge-loop reflection of
> 2026-07-02 (`_DomainEngines/bridge/LOOP_RECEIPTS.md`, Receipt 0) unless
> noted.

## HB-9 — Deliverable blocked-on linkage (design candidate, lower priority)

Provenance: as HB-6 (recommendation item 6). Deliverable-level residuals
blocked on decisions live as prose inside DEL working files; `next` and
`bridge-status` cannot join deliverable work to its gate. Candidate: a
machine-readable `blocked-on: D-XX` token convention in `_STATUS.md` /
`_DEPENDENCIES.md`, letting one query answer "what work does ruling D-XX
unlock?" — the question every loop's Step 0 currently reconstructs by hand.
Design decision first (token shape, which files, adapter parsing); build only
if the volume justifies it.
