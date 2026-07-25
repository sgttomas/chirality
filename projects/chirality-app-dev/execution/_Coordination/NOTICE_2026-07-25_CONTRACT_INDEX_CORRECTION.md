# Coordination Notice — CONTRACT K-* index correction (C-2), 2026-07-25

**This notice is coordination, not authority** (AGENTS.md change-notice rule;
D-GOV-21 mechanism M6). The App Dev loop adopts, amends, or declines under
its own instruments and cadence. Detection remains this loop's own
deterministic checks; this notice exists so detection does not depend on
them alone.

## What changed

At explicit owner direction (2026-07-25, in-session: "proceed with C-2 and
C-4"), the root loop corrected conflict **C-2** recorded in the adopted
root PRD (`docs/PRD_ROOT.md` §10.2): the `docs/CONTRACT.md` §1 K-* Invariant
Index claimed "**27 stable invariants** across 12 subsections" while the
live catalog holds **34 across 13** — the index predated the D-GOV-20
§1.13 Shared Runtime family. The correction:

- Count line updated to "**34 stable invariants** across 13 subsections".
- Seven index rows added for §1.13 (K-RUNTIME-1, K-CONTROL-1, K-PROJECT-1,
  K-STORE-2, K-RESIDENCY-1, K-ROLE-2, K-EXPORT-1).

No invariant definition changed; the correction is index arithmetic only,
mechanically verified against the catalog rows. (`README.md` also gained
its missing `runtime/` description — conflict C-4 — but README is not a
pinned surface for this loop.)

## What follows for this loop

- The `AUTHORITY_CORPUS.json` sha256 pin for `docs/CONTRACT.md` is now
  stale and re-pins on this loop's own cadence.
- No obligation arises from this notice.
