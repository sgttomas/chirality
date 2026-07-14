# W-P1 Ordinary Piping Preflight Basis

Status: `IMMUTABLE CANDIDATE — DECISION REQUIRED`

This derivative read-only preflight package cites accepted upstream truth and
does not replace decomposition, P3 membership, P4/A1/A2/A3 acceptance,
deliverable, lifecycle, or Git truth. It releases no manager and authorizes no
candidate generation, conversion, repair, project mutation, integration,
lifecycle act, H1/H2 act, release, or retirement.

## Ref and accepted-snapshot basis

- Dispatch and synchronized main: local `HEAD`, local `main`, local
  `origin/main`, and remote `refs/heads/main` all equal
  `69ac259a7113d5a838fb22aa2e84df0e0f109713`.
- The dispatch commit contains the HELP_HUMAN W-A3 phase-boundary acceptance.
  Accepted W-A3 integration-evidence main
  `f46452902e8b2fd78800b4bca3b1b0acccd3c892`, accepted W-A2 evidence main
  `80cce868f8922bac7910bb15cab24f7303e5e2a8`, P4 accepted main
  `b4efb8e554354399aadf1f624c107f63ede3230d`, and
  `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` are ancestors.
- Accepted membership is
  `snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv`, SHA-256
  `804938634127b1c81467bc6ad2792618106b12e5093cd5d7ddafc0740ef12979`.
- Accepted Piping-pilot post-state is bound by
  `snapshots/P4_PILOTS/ACCEPTANCE.md` and its four Piping rows in the postmerge
  ledger, SHA-256
  `08340cf09c4356a97456c1bb5db6b53cb98cd37f426ac0d3fc1ab83642bd119b`.
- W-A3 phase acceptance SHA-256 is
  `0ea6a06381052c6657305fcd60140725d4e694c6ca1ed7814eead4242749f17e`;
  its postmerge manifest is
  `ed8d02e101e8daaab14a4e697dab0e94be17a7a8d565cdc820ef6a70407e487e`.
- The active work graph is v31. H1 and H2 remain `UNAPPROVED`.

## Exact population and live-state reproduction

`P1_MANIFEST.tsv` freezes 30 ordinary Piping members from PKG-00 through
PKG-04, excluding only `DEL-01-01`, split exactly 8/3/5/8/6. They are all
non-pilot, non-issued, `IN_PROGRESS`, valid `LEGACY_FOUR_DOC`, and have zero
live `ScopeOfWork.md`.

All 120 legacy source hashes and all 30 `_STATUS.md` hashes reproduce the
accepted P3 rows. Membership, package ownership, lifecycle, pilot/issued
classification, path, source bytes, status bytes, and live format show no
drift. The Piping decomposition is
`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md`,
SHA-256 `9b110bd0a38189ea4a5707fe5a1cc0b411d1d29b4a4721559ca9d26a6c9e8c7c`,
bound at dispatch.

The selected members should expose 270 live bindings: nine per member across
four legacy sources, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, and `Dependencies.csv`. `EXPECTED_LIVE_BINDINGS.tsv`
records all 270 expected rows. Only 262 are present: every source, status,
context, reference, and dependency-summary path exists, but all eight PKG-00
`Dependencies.csv` paths are absent. The 22 present dependency registers
contain 278 data rows total.

This is not silent scope drift: the absence is made explicit as `MISSING` in
the manifest. It conflicts with the sealed 270-present-binding fan-in gate and
cannot be repaired or waived by ORCHESTRATOR.

## ISSUED exclusion and predecessor non-absorption

`EXCLUDED_ISSUED.tsv` freezes `DEL-01-01` separately. It remains exact P3
`ISSUED`, valid `LEGACY_FOUR_DOC`, SOW-absent, with all four source and status
hashes unchanged, all four control files plus `Dependencies.csv` present, and
13 dependency rows. It is read-only, excluded from all package scopes, and
parked for the later isolated H1 evidence lane.

`PREDECESSOR_RESULTS.tsv` confirms all four accepted Piping PKG-13 pilots
remain exact `SOW_V1`, status-identical, `IN_PROGRESS`, and legacy-free. The
101-member P3 Piping population partitions into these 30 P1 members, the one
ISSUED exclusion, four accepted pilots, and 66 later-wave ordinary members,
with no overlap or unclassified remainder.

## Method, checks, ownership, and disjointness

`METHOD_BINDINGS.tsv` freezes the active standard, resolver, validator,
converter, mapper, parity reporter, checklist compiler, renderer, skill
package, ratified software workflow contract, Piping instructions/profile, and
accepted root caller prerequisite. The converter requires isolated migration
and exact D-GOV-16 path-scoped authority. The accepted root caller prerequisite
keeps legacy/SOW support and invalid/partial/unauthorized-dual fail-closed
behavior in force.

`PACKAGE_PLAN.tsv`, `PACKAGE_EXECUTION_CONTRACT.md`, and five sealed package
briefs define a strict sequential chain PKG-00 → 01 → 02 → 03 → 04. Candidate
and evidence scopes are pairwise disjoint, every member has unique author and
verifier targets, and `DEL-01-01` has no target. All managers remain parked.

The applicable profile checks are `harness-self-check` always and
`harness-pytest` for future `execution/**` replacements, plus current/candidate
format validation, four-document checks, and dependency-register validation
as resolved by the human decision. This read-only preflight ran only the
active format validator; it did not run conversion, build, repair, project-
writing checks, or candidate generation.

The four unrelated Piping domain-audit files and the parent-owned work graph
edit are inventoried read-only in `FENCED_EXTERNAL_STATE.tsv`. The pre-existing
`.claude-worktrees/` container was neither inspected nor modified. Project and
Git state were not mutated.

## Decision required

HELP_HUMAN must obtain and record a human ruling before manager release:

1. restore and accept exact dependency registers for the eight PKG-00 members
   through an authorized predecessor, then rerun P1-B0; or
2. explicitly amend the P1 live-binding acceptance contract to define the
   absent PKG-00 registers as an accepted, checkable state and state the
   package/reconciliation consequences, then rerun P1-B0.

ORCHESTRATOR does not recommend one semantic dependency state over another.
No package may start on silence or an inferred waiver.
