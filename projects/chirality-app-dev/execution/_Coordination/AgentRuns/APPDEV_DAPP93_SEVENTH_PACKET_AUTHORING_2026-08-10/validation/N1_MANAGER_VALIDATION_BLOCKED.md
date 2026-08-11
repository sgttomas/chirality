# N1 manager fan-in validation — BLOCK

Verdict: `BLOCK_DAPP93_SEVENTH_NPM_INTERPRETER_CHAIN_UNPINNED`

## Accepted checks

- Citation reuse, 66-path allowlist, non-circular intake, and frozen F01–F09
  manager preflight passed before N1.
- Child stayed within 15 exact write targets and produced 10 durable partial
  files / 103,699 bytes; no historical authored packet was read or reused.
- Stage 2 contains 80 fresh structural mappings; no full-pattern historical
  command identity occurs in any of the 10 child files.
- `/usr/bin/readlink` is used instead of absent `/bin/readlink`; shell `wait`
  is expressed as a zsh builtin rather than a fake absolute binary.
- All 29 approved external operands passed child `test -x` and byte-hash
  checks. Pinned zsh syntax parsing passed.
- Checkpoint 1 observed 4 child files / 26,164 bytes, up from 0/0; later
  durable probe growth reached 9 files / 100,652 bytes. The child was not
  interrupted for quietness. Native context telemetry was unavailable.
- No packet operation, security/keychain/runtime/product/system mutation,
  Git/receipt/register/lifecycle action, or eighth lineage occurred.

## Blocking evidence

The approved npm operand is not a self-contained binary:

- path: `/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/npm`;
- bytes: 1,831;
- SHA-256:
  `a74679065974f6fd0a02f7ea8d4690d7bccd6437981924201ed37fc010112e22`;
- first line: `#!/usr/bin/env bash`.

The approved probe catalog pinned the wrapper, `/usr/bin/env`, and node but
did not enumerate or pin the shebang-resolved `/bin/bash` interpreter. In the
fresh child F08 environment, the required exact `npm --version` probe exited
127 and durably recorded `env: bash: No such file or directory`; the terminal
marker `N1_SAFE_PROBES_COMPLETE` is absent.

The manager independently observed `/bin/bash` exists at 1,290,128 bytes,
SHA-256
`a4c638ae036d92d55661de7d50896ec630145acaa3afeb1818ef4fc4e0ee45a7`,
and the same npm version probe returns 11.16.0 / exit 0 in the manager
environment. That does not cure N1: the frozen approved surface omitted the
interpreter pin, the child probe failed, Stage 3 was never written, and the
graph authorizes no replacement/repair child.

## Fan-in disposition

N1 correctly returned terminal BLOCK. Present Stages 1/2/4/5, partial packet
counterparts, syntax/probe scripts, and failed output remain unaccepted
blocked evidence. Stages 3/6/7, evidence return, packet index, complete author
return, manager freeze, freeze hash, and N2 verifier are absent.

No alternate npm launcher, PATH widening, `/bin/bash` catalog amendment, or
continuation is made. Final manager verdict:
`BLOCK — COMPLETE INTERPRETER CHAIN WAS NOT FROZEN AND THE MANDATORY CHILD SAFE PROBE FAILED; HOLD FREEZE AND VERIFIER`.
