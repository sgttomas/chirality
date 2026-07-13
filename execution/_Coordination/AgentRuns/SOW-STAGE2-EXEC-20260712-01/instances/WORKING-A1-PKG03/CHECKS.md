# WORKING-A1-PKG03 Package Checks

Overall verdict: `PASS`.

## Frozen basis

Local HEAD, local main, origin/main, and remote main are synchronized at
`34b87ec77010035eeaa76f0fa65981ec57e78933`. The exact row basis is
`0724f26f6ef79d733c8f1c513b29d837fd43c8eb`; the delta is accepted
evidence-only activation state with zero project-path change. All four exact
PKG-03 members remain IN_PROGRESS, non-pilot, non-ISSUED, exact
LEGACY_FOUR_DOC with no live ScopeOfWork.md. All frozen source, status,
control, decomposition, authority, tool, and profile hashes reproduce.

## Author/verifier fan-in

Four authors and four fresh independent verifiers are terminal PASS and
manager-accepted.

| Member | Candidate SHA-256 | Mappings | Source lines | Author | Verifier |
|---|---|---:|---:|---|---|
| DEL-03-01 | `763dc5f45a1b1b9e18240a79fcf77588f4a7490b52176aa48a9b77696c639f52` | 26 | 308 | PASS, manifest R1 | PASS |
| DEL-03-02 | `fa2694dc3b1e7145587c3ba48074122884c234e3461d2134b83f7fb82bccbfab` | 25 | 353 | PASS, run-record reconciled | PASS |
| DEL-03-03 | `9231e130a981f58a58bd1f0e87bab2dbc417f2121263e4aa425e2a40109e0d40` | 27 | 290 | PASS | PASS |
| DEL-03-04 | `3ae8810ad33dec6323804d5177344b0c5da05858ec776698b93a524ca0bf0f22` | 31 | 360 | PASS | PASS |

Aggregate coverage is 109 mappings over all 1,311 source lines. All
dispositions and source markers are preserved; parity has zero drop or text
mismatch. Candidate directories each contain exactly ScopeOfWork.md and
resolve as SOW_V1. Author and verifier isolated workspaces resolve as
authorized MIGRATION_DUAL under exact D-GOV-16 authority.

Every verifier independently passed exact identity, schema, map, parity,
complete line coverage, conservative OUT/AC/VER content authority, duplicate
checklist identity/linkage, duplicate render identity/safety, partial and
unauthorized-dual fail-closed fixtures, replacement paths, containment, and
separate schema/content-authority/preservation/substrate verdicts. All four
verifier five-row replacement manifests normalize exactly to the matching
manager slice.

## Evidence repairs and reconciliation

- AUTHOR-DEL-03-01's first generated manifest had 29 correct ordered paths but
  empty digest/byte cells. Under
  `A1-PKG03-AUTHOR01-MANIFEST-R1-001`, exactly 58 cells were regenerated;
  all 29 artifacts reproduce, the path-column hash is unchanged, and blanking
  those cells reconstructs the exact malformed preimage.
- AUTHOR-DEL-03-02 and the initial project-check record had generated local
  prefixes. Under `A1-PKG03-GENERATED-EVIDENCE-PORT-001`, exact literal
  substitutions passed count and reverse-preimage proof.
- The AUTHOR-DEL-03-02 run record was then normally finalized from portable
  PENDING to terminal SUCCESS after manager resume. Under
  `A1-PKG03-AUTHOR02-RUN-RECORD-RECON-001`, its final frozen identity is
  4,705 bytes / 93 lines /
  `cfbf9d1fcc0369d800766974d883ebfda3f11498816c7a8b1244b71237f80d16`;
  required TASK finalization sections, final claims, and direct bindings
  reproduce. It has zero machine-specific prefix.
- The premerge runner's planned scratch-to-accepted normalization replaced 23
  checkout and four temp-root strings before promotion. Reverse proof,
  JSON parse, PASS status, and substantive equality passed.

No repair changed candidate, source, status, map, parity, checklist, render,
verdict, project, lifecycle, authority, or acceptance semantics.

## Required App checks

| Check | Result |
|---|---|
| harness-self-check | PASS |
| harness-pytest | PASS — 264 tests |
| frontend-typecheck | PASS |
| frontend-test | PASS — 97 files / 713 tests; 1 file / 4 tests skipped |
| frontend-build | PASS |
| frontend-premerge | PASS — Section 8: 8; Section 9 report-only: 16 |

## Replacement, rollback, portability, containment

- REPLACEMENT_MANIFEST has exactly 20 rows: one ADD ScopeOfWork.md and four
  DELETE legacy-production rows per member.
- ROLLBACK_MANIFEST is the exact 20-row inverse with the same paths and hashes.
  Neither manifest contains status or control paths.
- Exact 13 accepted source/control checkout strings are inventoried as
  PRESERVED_SOURCE_LITERAL. Candidates and generated evidence contain zero
  checkout-root, machine-temp, or local-file URI strings.
- Project tracked/untracked dirty paths: zero. Candidate directories contain
  only the four authorized SOW files. All writes are within manager candidate
  and evidence scopes. Diff hygiene passes.

Blockers, conflicts, unknowns, waivers, and human rulings needed: none. This is
a derivative candidate recommendation only; RECONCILIATION remains mandatory
before any CHANGE integration.

