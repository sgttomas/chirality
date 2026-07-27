# Gate 3 Concordance Result

**Date:** 2026-07-27
**Command:** `bash projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/check_gate3_concordance.sh`

```text
PASS: SCA-APP-005 Gate-3 source and entity concordance
PASS: 31 SOW; 5 PKG; 17 DEL; 5 OBJ; 25 contexts; U1-U5 preserved
```

The check verifies the D-GOV-20 source sentences, the complete entity set,
context count and boundary parity, topology counts, DEC-021, U1–U5, and
removal of the stale App semantic-ownership sentence.

Additional deterministic checks:

```text
PASS: 25/25 contexts have package parity; 17/17 directly modified contexts have deliverable parity
PASS: 78 SOW, 10 PKG, 51 DEL, 10 OBJ; IDs, status, mappings, types, envelopes, and source refs unchanged
```

Commands:

```sh
node projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/check_context_parity.mjs
node projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/check_topology_invariants.mjs
```
