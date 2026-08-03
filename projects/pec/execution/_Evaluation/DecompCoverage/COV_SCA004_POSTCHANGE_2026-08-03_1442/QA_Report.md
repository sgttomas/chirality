# QA Report — COV_SCA004_POSTCHANGE

## Inputs and exact bindings

- `SOFTWARE_DECOMP.md`: SHA-256
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`.
- `ScopeLedger.csv`: SHA-256
  `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25`.
- `Deliverables.csv`: SHA-256
  `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72`.
- Unchanged `ContextBudgetQA.csv`: SHA-256
  `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef`.
- Unchanged `Companion_Inventory.csv`: SHA-256
  `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23`.
- DEL-01-06 `_CONTEXT.md`: SHA-256
  `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2`.

## Scan and comparison

Heading-text binding resolved `Packages`, `Deliverables`, and `Scope Ledger`.
The audit scanned all 11 package folders, 64 deliverable folders, 64 contexts,
64 status files, 32 SOW contracts, four companion registers, the Gate 5
candidate, and the immutable pre-change baseline.

- Forward/reverse coverage and ID consistency: PASS.
- Context fidelity: 64/64 PASS, including the exact DEL-01-06 revision-1.4
  mirror.
- Ledger integrity: 94 rows; `72/14/8`; zero unassigned IN rows; zero IN rows
  without a deliverable; 11 IN rows intentionally lack objective mapping.
- Objective evidence: all six objectives retain filesystem-backed support;
  scope-item counts are OBJ-001 20, OBJ-002 12, OBJ-003 12, OBJ-004 11,
  OBJ-005 7, OBJ-006 9.
- Package shape: PASS; companion roles remain explicit.
- Gate 5 change containment: stable IDs, package, deliverable name/path/type,
  envelope, phase, anticipated artifacts, objective, lifecycle, source, and
  dependency topology are unchanged.
- Strict dependency-register validation: 64 registers / 254 rows / zero
  findings.

Check 10 observes the deliberately serialized pre-pointer state: revision 1.3
/ SCA-003 remains the active pointer while this audit and the complete SCA-004
handoff are assembled. The Gate 5 integration owner must verify pointer parity
after both pointers move; this sequencing is the approved rollback control,
not an audit blocker.

## Limits

Anticipated-artifact matching remains deliverable-folder-local. The unchanged
DEL-08-02 warning is retained honestly. This derivative audit accepts no
artifact, lifecycle state, downstream repair, release, or professional
reliance.
