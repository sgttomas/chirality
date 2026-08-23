# Sealed repair brief — final cycle 2

- RequestedBy / Parent: `WI-PKG09-R20-REPAIR-01`
- Executor: resume `A2-PKG09-R20-IMPLEMENT-01`, sole overlapping source write owner.
- Role: delegated-harness-native explicit ephemeral-generalist Agent 2; role not mechanically enforced; evidence instruction-asserted; no delegation.
- Basis: cycle-1 `RETURN.md` SHA-256 `9394bb4533e087cb32344ad18c6d6e23c9a3fc18387fd215a8fb43146c17e4f5`; current script `fac760879e199145e4dc0dac8c39f334cb777f3e3d44faf5e24db4eaa5220600`; test `6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18`; fixture unchanged at required SHA-256.
- Objective: final repair of F-01 through F-05, limited to replacing the nonportable F-02 mechanism and revalidating the other authored repairs.
- Exact F-02 design:
  1. Do not use `/dev/fd` directory traversal.
  2. Canonicalize every expected ancestor with `realpath`; require exact lexical equality, containment, and non-symlink directories.
  3. Open each final token/log path with `O_NOFOLLOW` and hold all descriptors.
  4. `fstat` each held descriptor as a safe regular file with required ownership/mode; compare path `lstat` dev/ino identity to the open descriptor.
  5. Revalidate all ancestor canonical/non-symlink conditions and final path identity after all opens, before reading only from the held descriptors.
  6. Any race, symlink, containment, ownership, mode, missing file, or identity mismatch copies neither, reports private-only diagnostic preservation, and prohibits runtime removal.
- F-01: final PASS becomes irrevocable before best-effort failed-log deletion; deletion failure may leave copies but cannot retroactively create FAIL or lose non-PASS evidence.
- F-03: prepare/install-attempt cleanup may admit both absent logs where source semantics require it; capture requires both, and zero/one missing is private-only with no runtime deletion.
- Preserve F-04 exact empty/whitespace rejection and F-05 distinct job-still-loaded test.
- Complexity gate: delete cycle-1-only nonportable helpers; avoid new modules or unrelated refactors; explain each remaining helper and the net script/test diff.
- Write scope: same exact three frontend targets plus `instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-2/**` only.
- Checks in order: syntax; exact focused Vitest; only on PASS, typecheck, fixture identity/cmp, candidate hashes/diff, `git diff --check`, App containment, empty index.
- Evidence: `repair-cycle-2/REPAIR.md`, `CHECKS.md`, `RETURN.md` with F-01..F-05 closure, helper-complexity accounting, commands/results, hashes, inventory, and fences.
- Fences: unchanged. No full suite/build/package/network/Git/proof/operator/private-root/Desktop/default surface. This is the final allowed repair cycle; any gate failure freezes exact output and stops Phase A.
