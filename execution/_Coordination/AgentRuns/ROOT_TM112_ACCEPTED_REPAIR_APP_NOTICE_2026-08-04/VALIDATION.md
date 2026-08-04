# Validation — TM-ROOT-112 accepted-repair App notice

RunID: `ROOT_TM112_ACCEPTED_REPAIR_APP_NOTICE_2026-08-04`

Verdict: `PASS`

## Authority and product identity

- Signed acceptance transcript SHA-256:
  `a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`.
- `docs/SPEC.md` SHA-256:
  `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f`.
- `runtime/packages/daemon/src/runtime-daemon.ts` SHA-256:
  `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2`.
- `runtime/tests/daemon.test.ts` SHA-256:
  `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352`.

All four identities reproduce the signed-return and Receipt 96 basis.

## Register and handoff currentness

- Root live-register validation: `PASS`, 23 rows; parsed status counts are 12
  `OPEN` and 11 `DEFERRED`.
- Root archive validation: `PASS`, 99 rows.
- `HANDOFF_STATE.md` records 23/99 as current and retains Receipt 91's 27/95
  and Receipt 92's 24/98 states as historical transitions.
- Receipt continuity ends with exactly one Receipt 97 after Receipt 96.

## Notice identity and content

Root-origin notice SHA-256:
`1029648d039edd3c0449d0bea867853b033cc457a4b1f477c458dd4e127a6ed3`.

The notice contains `D-APP-88`, `TM-APP-036`, the mandatory non-blocking
parity-rerun rider, all three exact accepted product hashes, the accepted
Node 24 evidence summary, and the unexecuted Node 22.19 compatibility gap. It
assigns rerun and evaluation ownership to App and expressly disclaims App R2
causality, process/SIGTERM proof, App parity acceptance, lifecycle/reliance,
foreign disposition, merge, publication, and Git authority.

## Containment and form

- Scoped status shows changes only to the two authorized existing Root files,
  the new Root-origin notice, and this RunID.
- `projects/chirality-app-dev/` has no change from this run.
- Root registers and accepted product files were read and verified, not
  written by this manager.
- `git diff --check` passes for every authorized path.

Structural and hash validation do not create an App-local disposition or
acceptance.
