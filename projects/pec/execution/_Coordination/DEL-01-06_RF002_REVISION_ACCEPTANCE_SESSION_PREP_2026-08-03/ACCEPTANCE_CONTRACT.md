# Acceptance contract — DEL-01-06 RF-002 successor SOW

## Allowed SOW-only currency diff

The future WORKING_ITEMS author may change only DEL-01-06 `ScopeOfWork.md` and
only to reconcile accepted revision-1.4 / D-PEC-78 O-A truth:

1. bind `decomposition_basis` to revision 1.4 and set
   `project_scope_refs: [SOW-077, SOW-094]`, preserving `OBJ-004`;
2. trace both SOW-077 and SOW-094 through purpose/objective prose and the
   output/evaluation matrix;
3. replace CLM-003, CON-001, AX-003, REQ-001, and REQ-005 premises that say
   OI-003/home/shape/path remains open or TBD with D-PEC-78 O-A's settled
   strict-version-1 JSON/schema path and core-owned typed-port boundaries;
4. retire TBD-002's now-resolved path/shape uncertainty without renumbering or
   repurposing unrelated IDs;
5. reflect the current three-row non-gating ANCHOR posture, including SOW-077,
   without creating or changing an execution dependency; and
6. preserve graceful absence, file authority, loop-local authority, owner-gated
   registry-row changes, adapter/port replaceability, future-production
   posture, and every source/product boundary.

No source, test, configuration, dependency, context, reference, decomposition,
objective, or product artifact byte is part of this diff.

## Exact preservation requirements

- Preserve OUT-001..003 identities and semantics.
- Preserve AC-001..006 text, IDs, order, and meaning byte-for-byte.
- Preserve VER-001..006 text, IDs, order, AC linkage, and method semantics
  byte-for-byte.
- Preserve every unaffected CLM/REQ/CON/AX/TBD identifier and its meaning.
- The deterministic checklist must contain exactly six source-ordered AC rows
  and bind the candidate SOW SHA; no criterion may be invented, removed,
  paraphrased, or reordered.

## Deterministic checks

Run against the candidate deliverable folder:

```text
python3 tools/scope_of_work/validate_scope_of_work.py <DEL-01-06-folder>
python3 tools/scope_of_work/derive_review_checklist.py <DEL-01-06-folder>
python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict
python3 tools/coordination/analyze_dep_closure.py projects/pec/execution
```

Expected unchanged structural baseline: 64 registers / 255 rows / zero
findings; 136 ANCHOR / 119 EXECUTION; topology 119 edges / zero SCCs / zero
bidirectional pairs.

## Producer evidence

The revision changes no product byte. REVIEW must nevertheless bind or rerun
the current evidence against the candidate checklist:

- `D-PEC-75_ACTIVATION.md`, SHA-256
  `50c732553f3b4176ebfe0e2d287ece561e43f97fdb7f88185a2648dc28b0e277`;
- `D-PEC-75_REGISTERED_CHECKS.json`, SHA-256
  `690ea5141051d6cbe68545d46512e641b20ddcea5e16cd8b363588ed7ca954ec`;
- `D-PEC-77_VER005_RERUN.json`, SHA-256
  `1e0bd26f5bcda92996ed66e6373a6c67f2fe23270e48c98688c5cf6d488a1210`;
- prior review summary `REV_DEL-01-06_2026-08-03_1458/Review_Summary.md`,
  SHA-256 `6c6bf929f15b5fd15466b304cf28911da7fa129ed8fc13d319de5cf3ad45661c`.

Stale, missing, or non-reproducible producer evidence blocks acceptance; it is
not repaired or silently substituted in this contract-revision session.

## REVIEW Gates 1–4 and owner acceptance

- Gate 1: confirm exact identity, `INITIALIZED` state, existing SELF_CHECK
  continuation authority, revision-1.4 context consistency, candidate SOW_V1
  validity, and no write beyond the allowed SOW diff.
- Gate 2: consume the registered six-row checklist bound to the candidate SHA.
- Gate 3: evaluate all six criteria against reproduced producer evidence and
  record any new mechanical finding separately from RF-002.
- Gate 4: present every `TBD` disposition. The owner-adopted `REVISE` direction
  becomes RF-002's final resolved disposition only if the exact successor SOW
  is accepted; until then `HumanDisposition=TBD / Status=OPEN` remains.

The acceptance question must identify one exact candidate SOW SHA and ask only
whether those revised contract bytes are accepted as the DEL-01-06 production
contract. Acceptance does not accept product/source bytes, satisfy a lifecycle
gate, advance Gate 5, issue or release DEL-01-06, open another P1 node, or
authorize professional reliance. Gate 5 remains HOLD and lifecycle remains
`INITIALIZED` even after exact SOW acceptance.

## Failure, rollback, and rerun

- Any guard mismatch, validator/checklist failure, AC/VER change, evidence
  failure, unauthorized diff, new finding, or structural-baseline drift stops
  before acceptance.
- Before accepted Git closeout, rollback is restoration of SOW SHA-256
  `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`
  and removal of unaccepted review-candidate evidence; the live accepted
  contract/finding/lifecycle state remains the preimage.
- Rerun if any owner record, SOW/review/finding/status hash, revision-1.4/SCA
  hash, PROJECT_SETUP metadata handoff, dependency baseline, producer evidence,
  or allowed-path set changes.
- After exact acceptance and validation, hand off only the accepted SOW,
  REVIEW/finding evidence, immutable snapshot, preparation package, and required
  current-map/receipt evidence to CHANGE. CHANGE owns staging/commit/push/PR;
  merge remains the owner's gate.
