# Work graph — D-APP-93 Option A owner-operated preparation

Version: `v1`

Selection authority: D-APP-93 Option A owner ruling.

Posture: `TERMINAL_FAN_OUT_IN` with serialized author → manager freeze → fresh
read-only verifier.

| Node | Agent | Objective | Writes | Dependency | Gate |
|---|---|---|---|---|---|
| N1 | ephemeral Agent 2 author | Author the complete preparation-only owner packet and durable return | this run root except `reviews/**`, manager closeout, and Receipt 134 | accepted activation | terminal return; author stops |
| N2 | WORKING_ITEMS | validate N1, compute identities, and freeze the stable object | manager freeze only | accepted N1 | exact stable hashes |
| N3 | genuinely fresh ephemeral Agent 2 verifier | adversarial read-only verification | one `reviews/**` return only | N2 | `PASS` or `BLOCK` |
| N4 | WORKING_ITEMS | close validation, manager return, handoff, and Receipt 134 | manager closeout plus Receipt 134 | accepted N3 | standard loop checks |

One documentation/static-script repair cycle is permitted after `BLOCK`, with
a new bounded author brief and a genuinely fresh verifier. No operational
command may be executed in any node.
