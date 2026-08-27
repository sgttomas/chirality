# Validation — Root v3 R15 G2 Acceptance

Date: 2026-08-25

Status: `PASS_LOCAL`

## Identity and preservation checks

- Exact `origin/main`, parent ordering, merge tree, PR state, deleted remote
  head, and post-merge hosted harness: `PASS`.
- All six cumulative R12–R14 instrument SHA-256 identities: `PASS`.
- All five required subject pins plus the pre-transcription receipt-ledger pin:
  `PASS`.
- Candidate packet tree before and after transcription:
  `20469afce1081ec7da274a359474ddf390d979ec`, 96 files, no diff from
  `origin/main`: `PASS`.
- R15 owner-act text agrees between the ruling record and steer: `PASS`.
- Receipt 130 prefix is byte-identical to the 512089-byte pinned Receipt-129
  pre-image: `PASS`; Receipt 130 is a pure append.
- Changed-path containment to the two new `plans/steers/` files, this run
  folder, and the receipt append: `PASS`.

## Governance validators

| Check | Result |
| --- | --- |
| candidate whitespace against `origin/main` | `PASS` |
| practitioner-harness self-check | completed with no `BLOCK` findings; pre-existing REVIEW/WARN inventory reported |
| G0 root materialization fence | `PASS` |
| G1 root harness adapter | `PASS` — 53 pinned status files |
| G2 root surface ownership | `PASS` |
| G3 root work graph | `PASS` — six nodes, none active |
| agent instructions | `PASS` — 34 files, 0 errors, 0 warnings |
| instruction entrypoints | `PASS` |
| G4 commit-aware CI-form validation | `PASS` — 48 manifests; 10 changed paths; 0 instruction-surface paths; 0 covering manifests required |
| Task Management register | `PASS` — 19 rows |
| focused practitioner harness | `PASS` — 56 tests |
| `git diff --check` | `PASS` |

Commit-aware CI-form G4 was run against commit `574f7a8e2` before final
closeout amendment and passed with the same 10-path, zero-instruction-surface
shape. It is rerun after the amendment before push. Hosted governance CI is
observed after PR creation and is not inferred into this pre-push evidence.
