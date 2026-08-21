# Validation — Root cross-loop carriers (2026-08-21)

Verdict: `PASS — OWNER RULINGS RECEIVED; EXACT-BYTE AND MERGE GATES PRESERVED`

## Engineering and instruction surface

- Full Root validation suite: `319 passed`.
- Live agent-instruction validator: `34 files`, zero errors and zero warnings.
- Narrow validator-policy suite: `19 passed`.
- Instruction entrypoint validation: `PASS`.
- Governance harness G0–G4: `PASS`; 40 tranche manifests schema-valid.
- Post-commit G4 over the actual candidate base
  `e3e18d27740018efd12e73193c02395a9eca93c2..702d88a4c14a291f647c2a2e6e5fa40185839318`:
  `PASS` over 21 changed paths, four instruction-surface paths, and one
  applicable new manifest.
- App focused support checks on byte-identical inputs: `32 passed`.
- PR #602 basis repair: exactly four owner-named one-line substitutions;
  nonexistent SHA has zero target occurrences and does not resolve, corrected
  SHA has four target occurrences and resolves as a commit. G4, entrypoints,
  live agent validation, and diff hygiene pass after repair.

## Task Management closure

- Mandatory federation preflight and postflight: `COMPLETE`; four canonical
  register pairs valid; zero register writes by the federation helper.
- Root live register: `PASS`, 21 rows (`OPEN=11`, `DEFERRED=10`).
- Root archive: `PASS`, 104 rows.
- Continuation mutation: only `TM-ROOT-117`, from live `OPEN` to archived
  `CLOSED / RESOLVED_BY_DECISION`.
- Closure evidence SHA-256:
  `1768e9a8c1d98babf28662b31d5e9fb63a042d532e8cd909e4577062dd3bea34`.
- TM-ROOT-117 closure evidence SHA-256:
  `20421d4b7b06bcdab8f27e6bb01cbc6fced7d0a535375ca838128104309dd1b4`.
- Final mandatory federation: `COMPLETE`, four canonical register pairs,
  zero federation writes.

## Integration hygiene

- `git diff --check`: `PASS`.
- Current `origin/main` is 15 commits ahead of the run basis; changed-path
  intersection between this branch and those upstream commits is empty.
- The literal two-dot `origin/main..HEAD` G4 invocation reports four
  upstream-only instruction paths because the branch is behind. That is a
  range-shape limitation, not candidate-tranche evidence; the common-ancestor
  candidate range passes. No sync merge, rebase, or history rewrite is
  authorized or inferred.

## Preserved gates

- PR review and merge remain owner acts; no merge is performed.
- No artifact-proof label applies.
- TM-ROOT-117 Option R and DEL-02-06 epoch/preparation are owner-ruled. The
  future prepared exact-byte acceptance remains human-only.
- App adoption, exact-byte acceptance, implementation, lifecycle, release,
  publication, reliance, and foreign-register effects remain outside this
  tranche.
