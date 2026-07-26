# Routed Change Notice — D-GOV-26 amendments to `docs/SPEC.md` and `docs/CONTRACT.md` (ROOT-OGC-20260725)

Routed by: root loop (Agent 0, `HELP_HUMAN` posture), 2026-07-25, per the
D-GOV-21 M6 mechanism and the `AGENTS.md` change-notice rule. This notice
is coordination, not authority: this loop adopts, amends, or declines under
its own instruments and cadence.

## What changed

Ruled by D-GOV-26 (owner, 2026-07-25; record at
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`):

1. **`docs/SPEC.md` §0.2.1** — the shared-instruction-surface enumeration
   now includes `CLAUDE.md` and `.github/workflows/`, with two sentences
   stating why; **§1.1** — one added sentence recording that `_Archive/`
   subfolders are local working state excluded by the repository ignore
   policy. No normative requirement changed; §0.2.2's write-prohibition
   list is untouched.
2. **`docs/CONTRACT.md`** — the K-WRITE-2 explanatory gloss is amended
   (checkout-boundary containment; declared-write-target bounding per
   D-GOV-21 M1). The invariant statement itself is byte-identical; no
   entry added or removed; the 34-invariant index is unchanged.

## Why this loop is notified

`execution/_Reconciliation/References/AUTHORITY_CORPUS.json` pins both
`docs/SPEC.md` and `docs/CONTRACT.md` by sha256; both hashes change with
this tranche. Corpus-drift checks remain the deterministic detection path;
this notice exists so detection does not depend on them alone.

## Follow-on for this loop (its own act, on its own cadence)

Re-pin the two files at the next corpus refresh. Note for readers of the
pinned K-WRITE-2 text: the amended gloss narrows a containment claim
(checkout boundary, not working-root boundary); it does not change any
obligation this loop relies on.
