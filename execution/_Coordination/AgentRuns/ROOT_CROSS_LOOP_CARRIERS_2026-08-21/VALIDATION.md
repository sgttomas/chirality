# Validation — Root cross-loop carriers (2026-08-21)

Verdict: `PASS WITH HUMAN DECISION GATES PRESERVED`

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

## Task Management closure

- Mandatory federation preflight and postflight: `COMPLETE`; four canonical
  register pairs valid; zero register writes by the federation helper.
- Root live register: `PASS`, 22 rows (`OPEN=12`, `DEFERRED=10`).
- Root archive: `PASS`, 103 rows.
- Exact mutation: only `TM-ROOT-125`, from live `OPEN` to archived `CLOSED /
  RESOLVED_WITH_CHANGE`.
- Closure evidence SHA-256:
  `1768e9a8c1d98babf28662b31d5e9fb63a042d532e8cd909e4577062dd3bea34`.
- `TM-ROOT-117` remains `OPEN`; no owner-only decision was selected.

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
- The TM-ROOT-117 and DEL-02-06 choices remain human-only.
- App adoption, exact-byte acceptance, implementation, lifecycle, release,
  publication, reliance, and foreign-register effects remain outside this
  tranche.
