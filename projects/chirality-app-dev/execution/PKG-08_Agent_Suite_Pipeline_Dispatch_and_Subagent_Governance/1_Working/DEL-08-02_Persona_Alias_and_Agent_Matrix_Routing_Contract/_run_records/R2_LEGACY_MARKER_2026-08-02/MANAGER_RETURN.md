# WORKING_ITEMS Manager Return — DEL-08-02 Legacy Route Marker

- RunID: `APPDEV-PKG08-DEL0802-LEGACY-MARKER-2026-08-02`
- Manager: `WORKING_ITEMS`
- Package: `PKG-08`
- Selected deliverable: `DEL-08-02` only
- Basis: Git `1d4abf1cf1a23a33bd7fec59971251f86c010210`
- Result: `ACCEPTED_WITH_EXTERNAL_INTEGRATION_RERUN_ADVISORY`
- Lifecycle effect: none; state remains `IN_PROGRESS`
- Derivative disposition: package-local run evidence only; no authoritative
  decomposition, dependency, decision, or Task Management state changed

## Accepted fan-in

The one bounded Agent 2 return is accepted. `WovenDialogueRoute` now owns one
real `data-legacy="true"` boundary on the `legacy=1` branch. The boundary uses
`display: contents`, so it creates no layout box and supports an arbitrary
injected `ReactNode`; the focused test injects an unmarked `<main>` and proves
the component supplies exactly one marker. The default Woven branch stays
unmarked. No persona, alias, guard, replay, route-shape, or legacy-shell
semantics changed.

Agent 2 return:

- `AGENT2_RETURN.md` SHA-256
  `e336446ce2b916627b5ab022fd2c6f8592d27df3784bbb2587bb1d7d3e597b98`
- accepted source SHA-256
  `3c23b857727b1911c25bd1027089520e8f102a445a689e6a7677713f840ad10b`
- accepted focused-test SHA-256
  `83847096d8a0e3949ead1dbacce98b7a62cc691c252bfd3f0c24335eb5a426d8`

## Validation

- Focused route Vitest: PASS, 2/2, rerun by manager.
- Typecheck: PASS in Agent 2 return.
- Production Next/Electron build: PASS in Agent 2 return.
- Real in-app-browser DOM check, independently repeated by WORKING_ITEMS and
  HELP_HUMAN: PASS on `/`, `/chat`, `/workbench`, and `/pipeline`.
  Every `?legacy=1&unknown=kept` route had exactly one marker, computed
  `display: contents`, a `MAIN` child, preserved query, and no horizontal
  overflow. Every default route had zero markers, exactly one expected
  `[data-woven-surface]`, preserved query, and no horizontal overflow.
- Targeted screenshot/manual review of all four legacy routes: PASS; shell
  layout remained intact. Browser error log: empty.
- Practitioner harness: PASS, 349 tests.
- Receipt validator: PASS, frozen through Receipt 52.
- Authority corpus v18: PASS, no drift.
- App status: PASS, 53/53 `IN_PROGRESS`, no findings before this residual-only
  status edit.
- Repository self-check: exit 0 with known cross-root findings only.
- `git diff --check`: PASS before manager closeout edits; rerun required at
  serialized Agent 0 fan-in.

The child full frontend suite had 1095 passing tests and one failure in the
concurrently modified, out-of-package navigator test (`self is not defined`).
That is owned by the serialized PKG-02 repair and does not contradict this
focused return. A managed premerge attempt reached a ready isolated server but
served `_not-found`/404 for the harness routes; `PREMERGE_CHECK.json` records
that environment/profile failure. HELP_HUMAN owns the combined full-suite and
premerge rerun after serialized PKG-02 fan-in.

## Deliverable effect and residual

Only the resolved `[data-legacy]` bullet was removed from `_STATUS.md`
`## Remaining`. The packaged Desktop smoke evidence for the guarded navigator
selection path remains open exactly as required. Historical lifecycle state,
Checking Approval SHA, dependencies, D-APP-84, parity, the six UNKNOWN
relations, and both Task Management registers are unchanged.

## Notices, blockers, and next owner

- Cross-package notice: the combined full frontend suite currently depends on
  the concurrent PKG-02 navigator test repair. This package did not alter that
  work.
- Package blocker: none for the marker repair.
- Rerun advisory: HELP_HUMAN performs combined full frontend and premerge
  checks after PKG-02 fan-in.
- Next owner: HELP_HUMAN for serialized cross-package validation and CHANGE
  routing. No commit, push, or merge was performed here.
