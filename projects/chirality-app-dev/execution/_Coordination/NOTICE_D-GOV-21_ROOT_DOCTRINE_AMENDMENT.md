# Coordination Notice — D-GOV-21 root doctrine amendment (2026-07-25)

**This notice is coordination, not authority** (AGENTS.md change-notice rule;
D-GOV-21 mechanism M6). The App Dev loop adopts, amends, or declines under its
own instruments and cadence. Detection remains this loop's own deterministic
checks; this notice exists so detection does not depend on them alone.

## What changed

Owner ruling D-GOV-21 (RULED 2026-07-25, O-A against exact candidate
`c038c493e871c95871823281b45890ba9404624b`; record:
`docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`)
amended root governance doctrine in its implementation tranche:

- `docs/DIRECTIVE.md` — §1 (:13), §2 praxiology (:76), §2.6 (:199, :202,
  :204), §5 constraint rows (:300, :301): the repository root is now, as a
  single narrow exception, the working root for the root product itself; the
  instruction/working-root separation remains in force for every other
  working root.
- `docs/SPEC.md` — §0.2.1 context (:44 unchanged, still load-bearing),
  §0.2.2 (:48, :52), §0.3 path-anchor table (`{WORKING_ROOT}` row), §1
  (:97): `WORKING_ROOT` may resolve to `REPO_ROOT` for the root product
  only; instruction-surface writes still require a separately-authorized
  repo-wide instruction change (root-product changes route through the
  D-GOV-21 M2 gate, which supplies containment/evidence conditions but does
  not grant authorization).
- `docs/TYPES.md` — §1.4 Working Root / Execution Root definitions.
- `README.md` — Core Architecture separation description.
- Root `execution/` is the root product's execution root, eligible for
  `PKG-*`/`DEL-*` structure only after the D-GOV-21 §5.3 gate closes
  (guards G0–G4; the G0 materialization fence is live in
  governance-harness CI). Nothing is materialized at ruling time.

## What this does NOT change for this loop

- No change to any `projects/*` or `domains/*` working root, its fences, or
  its instruments. The exception does not extend beyond the root product.
- No change to K-* invariants, ratification mechanics, human gates,
  lifecycle states, or the decision-record system.
- No change to the public-export boundary.

## Follow-on for this loop

If this loop pins or mirrors any of the amended root `docs/` surfaces
(authority-reference corpus snapshots, SHA-pinned mirrors, export staging),
those pins now trail the amended doctrine. Any carry-forward, pin update, or
rebaseline is this loop's own gated act against the D-GOV-21 EffectiveSHA
(the merged implementation-tranche commit). No action is required by this
notice itself.
