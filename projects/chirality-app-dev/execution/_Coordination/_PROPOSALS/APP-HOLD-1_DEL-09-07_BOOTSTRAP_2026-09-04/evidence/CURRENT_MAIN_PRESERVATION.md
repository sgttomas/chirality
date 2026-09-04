# Current-Main Basis Preservation

Status: `PASS`

The remediation R2 candidate is based on exact `origin/main`
`287b82f16c0d3970bac71e40b0e41fdd50569b08` (PR #700 merge). A read-only
`git ls-remote --refs origin refs/heads/main` returned exactly one matching ref
at that SHA before R2 writes. A read-only changed-path comparison from the
approved R4 basis
`77ea8aa68affdb0485134b23d55303c362a312ac` through the remediation basis
found exactly five modified plan-only paths under
`projects/chirality-app-dev/plans/shell-redesign_2026-09-04/`.

No intervening path overlaps any of the 61 future application paths. All eight
fixed MODIFY preimages and all 52 ADD absences remained exact, D-APP-104 stayed
unused, and Receipt-225 remained the physical cursor. The repaired candidate
port applied conflict-free to the clean PR #700 basis. No PR #700 byte is
removed or modified. The R1 candidate and review worktrees remain preserved
and untouched.

The preparation-basis physical receipt tail is `Receipt-225`, parented to
Receipt-224. The candidate receipt remains non-live `NEXT_AVAILABLE` and must
be reminted from the live cursor after any later rebase.

The prior approval root `4f0f72...`, artifact digest `091817...`, and owner
answer `Yes` are preserved as dated history only. The R1 approval root
`850e3457...` and artifact digest `09937723...` are failed-review candidate
evidence only. The renderer repair changes the R2 approval and artifact
identities and the new two-digest owner question; no prior answer supplies
authority for it.

This evidence is point-in-time: any movement of `origin/main`, D-APP-104
allocation, live preimage, authority postimage, pointer, receipt cursor, or
proposal file set requires fresh verification and, where identity changes, a
newly presented owner question.
