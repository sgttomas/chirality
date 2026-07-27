# Basis Refresh Validation — c487b7dd5

- **Prior admitted basis:**
  `4214915d9fcfecdc2952626421bf50b0e5f7845b`
- **Refreshed accepted basis:**
  `c487b7dd57a378e2f74417118e78e7f61a161629`
- **Refreshed tree:** `ff71da5d822902ddd04ff00523e21c88c8d66edf`
- **Audit basis:** `fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
- **Audit return SHA-256:**
  `18e0ca3f98b05f793e5b21e65ba28eb6ae90ecadd1865a7212d2fd21707cc47a`
- **Selected packet SHA-256:**
  `c6d7b3bd8041eb19e38e7b09f8c9cdb2325bbc02368afbadd73de28195b31f54`

## Refresh result

`PASS — F1/E1 PREMISE AND AUTHORITY BOUNDARIES PRESERVED`

The prior admitted basis and the SCA-APP-005 subject commit are ancestors of
the refreshed basis. Every D-APP-48/49 subject path remains byte-identical to
the audit basis. Of the selected packet's broader 31-path premise list, 30
remain byte-identical and one changed: Piping `SOFTWARE_DECOMP.md`.
Its complete diff is the front-matter revision value `0.9` to `0.10`.

The refreshed basis preserves the D-APP-48 ruling/live-JSON mismatch:

- ruling and D-30 pin:
  `ee290e22a8c19d46fb8004114d2ede55b805fba4`;
- live JSON pin:
  `55a066fdff6877d8aa2a49ce08a545ac98872848`;
- both objects resolve and the first is an ancestor of the second; and
- the combined validator exits `1` with
  `ERROR: consumption source.commitSha mismatch`.

App source-reference counts remain 67 production files and 39 test files.
The admitted audit return remains byte-identical. The D-APP-75 effective
closeout and OD7 Piping notice now present at the refreshed basis create no
repin, runtime-client scope, successor identity, or F1/E1 authority change.

## Historical recheck boundary

The preserved Agent 2 admission rechecks remain immutable records of their
dispatch population at `4214915d9...`. This refresh does not rewrite their
briefs, returns, or run records. EVALUATION independently repeated the
basis-sensitive Git, hash, path, schema, D-30, authority, whitespace, and
package-population checks at `c487b7dd5...`.

## Non-effects

This refresh creates no activation, preparation write, identity, version,
commit, implementation, repin, facade retirement, lifecycle transition,
release, or professional-reliance authority.
