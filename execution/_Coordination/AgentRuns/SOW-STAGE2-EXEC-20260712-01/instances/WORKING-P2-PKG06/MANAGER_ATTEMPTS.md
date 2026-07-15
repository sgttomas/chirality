# WORKING-P2-PKG06 Manager Attempts

## Attempt 1 — inverse-operation spelling

The initial manager fan-in stopped because it compared the author's explicit
inverse spelling `RESTORE` with the verifier's equivalent canonical spelling
`ADD` literally. Paths, hashes, member identities, and operations otherwise
matched exactly. The manager retained this failed assertion, canonicalized
only `RESTORE` to `ADD` for set comparison as already established by accepted
PKG-05 practice, and reran the full fan-in from scratch. No child, candidate,
source, project, semantic, authority, lifecycle, or acceptance byte was
changed or waived.

## Closeout normalization

Before package-manifest freeze, the manager removed exactly one final LF from
13 parent-owned high-level evidence files that ended in two LFs. Exact hashes
are retained in `NORMALIZATION.tsv`; each after-image equals its before-image
minus one final LF. Child workspaces and accepted child manifests were not
changed. All manager outputs and the package manifest were rebuilt afterward.

## Disposable manager bytecode

A final syntax check generated two disposable `__pycache__` files after the
first package-manifest freeze. They were removed before the final freeze:
`build_manifest.cpython-313.pyc` at
`0df47f91c9d152484da76b485a023a56359b7c5570060305861dbd4ce0957507` and
`manager_fan_in.cpython-313.pyc` at
`9d3f7666a41b4fb1f27078f26d144db7931c64c53d35a56f822bd02da306bf95`.
The source scripts passed compilation; no governed evidence or candidate byte
changed. The package manifest was rebuilt and fully reproduced afterward.
