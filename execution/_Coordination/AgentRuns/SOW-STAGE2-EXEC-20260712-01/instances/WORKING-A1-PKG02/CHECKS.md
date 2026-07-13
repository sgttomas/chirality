# WORKING-A1-PKG02 Package Checks

Overall verdict: `PASS`.

## Basis and live rows

- Dispatch basis local main is 34b87ec77010035eeaa76f0fa65981ec57e78933.
- Exact row basis is 0724f26f6ef79d733c8f1c513b29d837fd43c8eb;
  the intervening evidence-only delta has zero projects/** path.
- All five manifest members remain IN_PROGRESS, non-pilot, non-ISSUED,
  exact live LEGACY_FOUR_DOC, with no live ScopeOfWork.md.
- All 45 frozen source/status/control hashes reproduce against live project
  truth and isolated author/verifier workspaces. Status hashes remain exact.

## Author/verifier fan-in

All five authors and five fresh verifiers are terminal PASS and manager
accepted. DEL-02-03 verifier Attempt 0 is a preserved pre-execution
FAILED_INPUTS substrate event; unchanged R1 passed every gate.

| Member | Candidate SHA-256 | Mappings | Source lines | Author | Verifier |
|---|---|---:|---:|---|---|
| DEL-02-01 | 6e47e1c1e7528f13f8ed0240a9c3f1c425999d70b70ddb83a2c4a6dc9893e378 | 30 | 270 | PASS | PASS |
| DEL-02-02 | 6146778246cb79838073b9fa268b7067b8ac5f9d94f9e424dc4540962ae30846 | 28 | 279 | PASS | PASS |
| DEL-02-03 | 090a041bfda14f2ff1397378d74c79e9b394d4986bc3356a6e5243547d90f173 | 32 | 316 | PASS | R1 PASS |
| DEL-02-04 | 73afaf56db4dc000688eeaedb4e7c688029e07986bb01f390b85701169e0114a | 29 | 297 | PASS | PASS |
| DEL-02-05 | 5b158b9ef5f6922abe8a56bf84b55dd6af55df42ea5546b4caa42d3487742446 | 27 | 279 | PASS | PASS |

Aggregate coverage is 146 mappings over all 1,441 source lines. Every
disposition is PRESERVED with zero silent drop or text mismatch. Each
candidate validates as SOW_V1 and each child workspace validates as exact
authorized isolated MIGRATION_DUAL under D-GOV-16.

Independent verifier gates pass for exact source/status/control/candidate
identity, schema, map/parity/target resolution, line coverage, conservative
OUT/AC/VER authority, duplicate checklist/render stability and safety,
partial and unauthorized-dual fail-closed fixtures, exact five-row replacement
manifests, and containment. Schema, project-content authority, preservation,
and execution substrate separately pass for all five members.

## Portability and preserved execution evidence

- `A1-PKG02-CHECK-EVIDENCE-PORT-001.md` authorizes exactly 27 checkout-root
  and four temp-root substitutions in the two project-check JSON records.
- `CHECK_NORMALIZATION_MANIFEST.tsv` and
  `CHECK_NORMALIZATION_CHECKS.md` prove pre/post/reverse hashes, JSON parse,
  substantive equivalence, all-PASS results, and direct bindings `NONE`.
- `PRESERVED_SOURCE_LITERAL_INVENTORY.md` freezes 34 occurrences in 24 exact
  copied source-control files; candidates/renders/generated metadata have zero.
- DEL-02-03 Attempt 0 manager/verifier records are both bound and provenance
  classified in `COORDINATION_NOTICE-001.md`; no contradictory claim exists.

## Replacement and rollback

- `REPLACEMENT_MANIFEST.tsv` has exactly 25 rows: five ADD ScopeOfWork.md and
  twenty DELETE legacy-source rows.
- `ROLLBACK_MANIFEST.tsv` is the exact 25-row inverse with identical paths and
  hashes. No status, control, dependency, or lifecycle path appears.
- All live preimage and candidate postimage hashes reproduce exactly.

## Registered project checks

| Check | Result |
|---|---|
| harness-self-check | PASS |
| harness-pytest | PASS — 264 tests |
| frontend-typecheck | PASS |
| frontend-test | PASS — 713 passed, 4 skipped |
| frontend-build | PASS |
| frontend-premerge | PASS — Section 8: 8; Section 9 report-only: 16 |

Premerge ran against a temporary local Next API explicitly pinned to the
keyless stub provider and the server was stopped after PASS. Generated ignored
build/test residue is not governed evidence. Root Git status has zero project
tree tracked, staged, or visible untracked drift.

## Final containment and closure

- Writes are confined to candidates/W_A1/APP-PKG02/** and
  instances/WORKING-A1-PKG02/**.
- Project paths remain read-only; .claude-worktrees was untouched.
- Git, integration, lifecycle, H1/H2, ISSUED, release, retirement: none.
- Diff hygiene passes. Blockers, waivers, conflicts, and human rulings: none.
- Rerun if any bound basis, row, input, candidate, child return, authority,
  tool/skill, check postimage, manifest, or project byte changes.
