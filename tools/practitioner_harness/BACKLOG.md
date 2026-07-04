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

## HB-6 — bridge-status: classify parked lanes; derive gates; warn on label drift

Provenance: owner direction 2026-07-03 ("Proceed accordingly" on the
work-scope-surfacing recommendation, items 3–5; `LOOP_RECEIPTS.md` Receipt 11).
Three detect-only upgrades to `cmd_bridge_status.py`: (a) parse the latest
receipt's parked-lanes bullet into per-lane rows and annotate each lane
`anchored` (resolves to a register row, governed brief, or open PR) or
`receipt-only` — receipt-only lanes are the fragile ones and should be
visibly so; (b) derive the live-binding gate table from the gates the
profile's own gate line names, replacing the three hardcoded register lookups
(`cmd_bridge_status.py:551` as of 2026-07-03) — a hardcoded gate list is the
hand-maintained-summary anti-pattern, one tier-0 CHANGE away from stale;
(c) report a WARN-class finding when the latest receipt lacks any of the
three canonical bullet labels the view matches by exact string
(`cmd_bridge_status.py:319`) — today a mislabeled bullet silently drops the
whole queue from the view.

## HB-7 — GEN-10: receipt-structure and parked-lane carry-forward check

Provenance: as HB-6. Self-check gains a GEN-10 over
`_DomainEngines/bridge/LOOP_RECEIPTS.md`: the latest receipt carries the
canonical bullets ("Owner direction of record" / "Gate outcome" /
"Parked lanes"), and each parked-lane token either recurs from the prior
receipt, resolves to a structural home (register row, brief, PR), or is
explicitly retired with a stated reason. Turns the carry-forward discipline —
currently held by convention alone, the single thread the handoff hangs on —
into a detected invariant (GEN-7 pointer-currency precedent). Detect, never
rewrite; severities per the D-GOV-02 model.

## HB-8 — DE-check: profile live-binding line vs register state

Provenance: as HB-6. The ADOPTED profile's "Live binding ... gated x4" line
(`_DomainEngines/profiles/open_pipe_stress.yaml:145` as of 2026-07-03) is a
hand-written summary that has already drifted (piping `D-21` cleared
2026-07-02 via `DEC-056`; the line still names four gates). The profile is
CHANGE-gated — detect, never rewrite: a DE-check cross-references each gate
the line names against its source register state and reports REVIEW on
divergence (stale-open-issue precedent). Any live-count movement carries its
conscious pin update in the same PR.

## HB-9 — Deliverable blocked-on linkage (design candidate, lower priority)

Provenance: as HB-6 (recommendation item 6). Deliverable-level residuals
blocked on decisions live as prose inside DEL working files; `next` and
`bridge-status` cannot join deliverable work to its gate. Candidate: a
machine-readable `blocked-on: D-XX` token convention in `_STATUS.md` /
`_DEPENDENCIES.md`, letting one query answer "what work does ruling D-XX
unlock?" — the question every loop's Step 0 currently reconstructs by hand.
Design decision first (token shape, which files, adapter parsing); build only
if the volume justifies it.
