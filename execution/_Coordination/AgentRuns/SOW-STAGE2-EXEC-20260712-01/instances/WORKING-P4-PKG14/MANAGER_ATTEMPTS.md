# WORKING-P4-PKG14 Manager Attempts

## PRE-1 — failed, retained

`manager_preflight.py` initially resolved `ROOT` one parent too shallow and
attempted to read `execution/execution/.../MANIFEST.tsv`. It failed before any
result or candidate write. This was a path-only mechanical defect.

## PRE-2 — failed, retained

The root anchor was changed from `parents[5]` to `parents[6]`. All preflight
bindings were rerun from the corrected root. The second attempt exposed that
the frozen manifest schema uses `artifact`, not `path`; it failed before any
result or candidate write.

## PRE-3 — repaired

Manifest resolution now binds `preflight/<artifact>` exactly. All preflight
bindings are rerun; `PREFLIGHT_REPRODUCTION.json` is the rebuilt direct
binding for the successful attempt.

## FANIN-1 — failed, retained

The first manager fan-in treated verifier manifest paths containing `/` as
repository-relative, while that manifest is uniformly verifier-directory
relative. The assertion failed before terminal artifacts were written. This
was a path-resolution-only mechanical defect.

## FANIN-2 — repaired

Manifest base semantics are now explicit per child: author paths are root
relative and verifier paths are verifier-directory relative. Both manifests
and every downstream package binding are rebuilt and rechecked.
