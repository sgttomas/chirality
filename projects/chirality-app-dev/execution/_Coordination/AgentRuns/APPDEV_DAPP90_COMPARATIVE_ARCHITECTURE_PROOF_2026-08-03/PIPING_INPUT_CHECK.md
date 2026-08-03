# Committed-Main Piping Input Check

Lane: first-domain UI delta inventory

Disposition: `HELD_BY_SEQUENCE`

Checked: `2026-08-03`

Committed remote-tracking ref inspected: `origin/main`

Exact commit:
`7249281e1f84ba5abee3c31c2fea3736b22000d3`

Piping coordination tree object:
`d7f8bf2f2a00329be1ed367e427c7afe45e4b030`

## Independent manager check

The manager ran these read-only checks after the source-independent proof lanes
were active and the UI-delta lane reached its external input:

```text
git rev-parse origin/main
git ls-tree -r --name-only origin/main projects/chirality-piping/execution/_Coordination |
  rg -i '(response|runtime.surface|runtime_surface|tm.runtime|product.delivery|control.plane)'
git grep -n -i -E '(runtime-surface response|runtime surface response|first-domain UI|first domain UI|TM-ROOT-105|TM-ROOT-107|TM-ROOT-109|per-domain control-plane)' origin/main -- projects/chirality-piping/execution/_Coordination
```

The filename search returned only:

- `NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`; and
- `NOTICE_2026-08-02_ROOT_TM_RUNTIME_NEEDS_RESPONSE_REQUEST.md`.

The content search returned only citations inside the inbound request. It found
no Piping-owned runtime-surface response.

The committed inbound request has:

- Git blob: `7801a274ce1cca2e3eefeecbdd2ddfb84826936a`;
- SHA-256:
  `32f943eefe80d926626c5f63ae574d6df84f461cd23f0728edf6b8a13de769f1`;
- requested reciprocal citations: `TM-ROOT-105` and `TM-ROOT-109`; and
- a return contract for a Piping-owned response naming concrete runtime
  surfaces, local-versus-generic boundaries, user-facing UI and equivalent
  agent-facing API, and exact evidence hashes.

The request is not its own response and cannot supply the required UI delta.
The earlier observation that no open Piping response PR was visible is not used
as proof; only committed-main bytes govern this lane.

## Resume condition

On resume, fetch/resolve the then-current committed `origin/main`, repeat the
tree and content searches, and accept an input only if a Piping-owned response:

1. is present in that committed tree;
2. cites the inbound request and its SHA-256;
3. reciprocally cites the named Root row IDs;
4. names the Piping UI and semantically equivalent agent-facing runtime
   surfaces with exact Piping evidence refs/hashes; and
5. preserves Piping-local versus candidate-generic ownership.

Until all five tests pass, the lane remains `HELD_BY_SEQUENCE` and no A/B/C
selection packet may issue.
