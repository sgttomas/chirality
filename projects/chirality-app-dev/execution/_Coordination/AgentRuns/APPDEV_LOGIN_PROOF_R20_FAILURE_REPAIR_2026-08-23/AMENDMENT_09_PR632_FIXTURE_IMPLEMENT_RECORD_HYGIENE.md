# Amendment 09 — fixture implementation evidence hygiene cycle 1

- Authority: owner-directed failure-rule cycle for exact candidate-whitespace findings.
- Findings: one surplus terminal blank-line LF in each implementation-instance `ACTIVATION.md`, `CHECKS_AND_LINEAGE.md`, `IMPLEMENTATION_MODE_INVENTORY.md`, and `RETURN.md`.
- Repair: remove exactly the final LF from each named record, leaving one terminal newline; record pre→post byte/SHA-256 lineage and prove `postimage + LF == preimage` byte-for-byte.
- Preserve: focused test SHA-256 `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e`, unchanged proof-script identity, gzip evidence, and every substantive gate result.
- Rerun only candidate whitespace plus immutable-hash, App containment, and empty-index postchecks. Any additional finding stops.
- No source/product/guard change, prior gate rerun, build/package/proof, network, or Git action.
