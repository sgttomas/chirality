# P1_CANON Post-Merge Handoff

Status: `C1G_PASS — CANON_INTEGRATED`
PR: `#220` — `https://github.com/sgttomas/chirality/pull/220`
Merge commit / synchronized main:
`e150c972889d05a8fc270239451a35c7512dc9a9`

## Accepted upstreams and Git binding

- P0 basis `main@c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`;
- D-GOV-16 ruling `7584718aa32b112e415331736d1a8e68c12ac176`;
- C1 activation commit
  `2404f4e92b79c41e295a9bf3102407a0cd8b54db`;
- source binding/head
  `53756b5516cfa041d782ed0012d9bfb6357a386a`;
- merge commit
  `e150c972889d05a8fc270239451a35c7512dc9a9`, whose parents are the
  prior main basis and exact source head.

PR #220 contained exactly 40 paths: the three canon paths and authorized
run/C1V evidence. GitHub `governance-harness` passed. The PR was mergeable and
merged under `HUMAN-STEER-001` using the permitted merge-commit method.

## Integrated identities and closure

| Live path | SHA-256 |
|---|---|
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| `docs/TYPES.md` | `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae` |
| `docs/SPEC.md` | `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27` |

After merge, local `main`, `origin/main`, and remote main were equal to the
merge commit with divergence `+0/-0`; tracked state was clean and the only
untracked surface remained the untouched pre-existing `.claude-worktrees/`.

C1G is closed PASS. P1_CANON is an immutable derivative integration snapshot
citing the accepted ruling and source commits; live canon at the merge commit
is authoritative for later phases. C2R and C2A preparation are released. C2F,
C2G, all conversion nodes, H1 integration, and H2 retirement remain parked.

Rollback, if human-authorized, is a non-history-rewriting revert of merge
commit `e150c972889d05a8fc270239451a35c7512dc9a9` with mainline parent 1,
followed by normal reviewed integration. Rerun C1/C1V/C1G if this Git binding,
the live hashes, or required check evidence changes.
