# WORKING-A1-PKG01 Package Checks

Overall verdict: PASS.

## Basis and live rows

- Dispatch basis local HEAD, main, origin/main, and remote main was
  34b87ec77010035eeaa76f0fa65981ec57e78933 at activation.
- Accepted row basis is 0724f26f6ef79d733c8f1c513b29d837fd43c8eb;
  the intervening delta is evidence-only and contains zero projects/** path.
- All four exact manifest members remain IN_PROGRESS, non-pilot, non-ISSUED,
  exact live LEGACY_FOUR_DOC, and have no live ScopeOfWork.md.
- All 36 frozen source/status/control hashes match the accepted manifest and
  live project at package close. Status hashes remain exact.

## Author/verifier fan-in

All four authors and all four fresh separate verifiers have terminal PASS
returns accepted by the manager. No child delegated or contacted a sibling.
Every verifier ran only after manager acceptance of its author dependency.

| Member | Candidate SHA-256 | Mappings | Source lines | Author | Verifier |
|---|---|---:|---:|---|---|
| DEL-01-01 | 34e41b8e7efe65ea58eb36856bde2bbd7e2e0d21052331c676d245b106813b65 | 26 | 281 | PASS | PASS |
| DEL-01-02 | a6c04d568d83dee81af68815fe5b2adaa13cbe771b3788b6a73d5571e0722b64 | 60 | 560 | PASS after exact portability repair | PASS |
| DEL-01-03 | 8eeb463884aa9549a8ebf79d8c454bf60fdc6e0dd5a5e7359734ead1d23e47b0 | 31 | 365 | PASS | PASS |
| DEL-01-04 | 13a2a49d1cb74fc83b9c64dc39c25f8ae98107b5b666b5b7352a95b4e626a068 | 28 | 333 | PASS | PASS |

Aggregate coverage is 145 mappings over all 1,539 source lines. All
dispositions are PRESERVED and parity has zero drop or mismatch. Each
candidate directory contains exactly ScopeOfWork.md and validates as SOW_V1.
Each author and verifier workspace validates as authorized isolated
MIGRATION_DUAL under exact D-GOV-16 authority.

Independent verifier gates pass for exact source/status/control/candidate
identity, schema, map and target resolution, parity and line coverage,
conservative OUT/AC/VER authority, duplicate checklist/render stability and
safety, partial and unauthorized-dual fail-closed fixtures, exact five-row
replacement manifests, and write containment. Schema, project-content
authority, preservation, and execution substrate separately pass for all four
members.

## Evidence portability and preserved source

- A1-PKG01-AUTHOR02-PORT-001 authorized one exact three-occurrence run-record
  repair. PORT_REPAIR_MANIFEST.tsv proves exact pre/post/reverse hashes and
  direct binding NONE. No substantive author output changed.
- Parent disposition PRESERVED_SOURCE_LITERAL is frozen in
  PRESERVED_SOURCE_LITERAL_INVENTORY.md. Marker-bound legacy text is preserved
  exactly and is not treated as generated path authority.
- Generated metadata, run records, returns, statuses, checks, and manifests
  have zero checkout-root and local-temp prefixes.
- PROJECT_CHECKS.json and PROJECT_CHECKS_PREMERGE.json were mechanically
  normalized after tool completion; CHECK_NORMALIZATION_MANIFEST.tsv proves
  exact pre/post and reverse hashes.
- RECON-A1-F later identified one generated workspace_root still present in
  each R1 postimage. Under A1-PKG01-CHECK-EVIDENCE-PORT-R2-001, each field was
  changed exactly once to portable ~. CHECK_NORMALIZATION_R2_MANIFEST.tsv and
  CHECK_NORMALIZATION_R2_CHECKS.md prove exact pre/post/reverse hashes, JSON
  validity, semantic equivalence, all-six-PASS preservation, and zero
  remaining generated checkout/temp prefixes. The R1 proof remains unchanged
  as the intermediate chain.

## Replacement and rollback

- REPLACEMENT_MANIFEST.tsv has exactly 20 rows: four ADD ScopeOfWork.md and
  sixteen DELETE legacy-source rows.
- ROLLBACK_MANIFEST.tsv is the exact 20-row inverse with identical paths and
  hashes.
- No _STATUS.md, control, dependency, or lifecycle path appears in either.
- All live preimage hashes and candidate postimage hashes reproduce exactly.

## Registered project checks

| Check | Result |
|---|---|
| harness-self-check | PASS |
| harness-pytest | PASS — 264 tests |
| frontend-typecheck | PASS |
| frontend-test | PASS — 713 passed, 4 skipped |
| frontend-build | PASS |
| frontend-premerge | PASS — Section 8: 8; Section 9 report-only: 16 |

Premerge ran against a temporary local Next API pinned to the keyless stub
provider; the server was stopped after PASS. Generated ignored build/test
residue is not governed evidence. Root Git status has zero project-tree
tracked, staged, or visible untracked drift.

## Final containment and closure

- Writes are confined to candidates/W_A1/APP-PKG01/** and
  instances/WORKING-A1-PKG01/**.
- Project paths remain read-only; .claude-worktrees was untouched.
- Git, integration, lifecycle, H1/H2, ISSUED, release, and retirement actions:
  none.
- Diff hygiene passes.
- Blockers, waivers, conflicts, and rerun requirements: none at the accepted
  basis. Rerun if any bound basis, row, source/status/control, candidate,
  tool/skill/authority, or project-check byte changes.

RECON-A1-F rerun is required against this R2 package; the prior aggregate
result is not accepted.
