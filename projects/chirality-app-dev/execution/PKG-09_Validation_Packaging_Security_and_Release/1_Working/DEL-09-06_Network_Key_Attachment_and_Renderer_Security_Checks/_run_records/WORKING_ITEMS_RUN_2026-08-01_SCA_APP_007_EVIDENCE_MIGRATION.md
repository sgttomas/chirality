# WORKING_ITEMS Return — SCA-APP-007 Evidence Migration

**RunID:** `WORKING_ITEMS_SCA_APP_007_DEL0906_EVIDENCE_MIGRATION_2026-08-01`

**Parent:** `HELP_HUMAN`

**Manager:** `WORKING_ITEMS`

**Package:** `PKG-09_Validation_Packaging_Security_and_Release`

**Selected deliverable:** `DEL-09-06`

**State:** `IMPLEMENTED_VALIDATED_WITH_TOOLCHAIN_NOTE`

**Authority:** owner-approved SCA-APP-007 Gates 1–4, 2026-08-01

## Activation and work graph

The accepted owner is PKG-09 / DEL-09-06. The retired PKG-03 physical path
was a bounded migration source, not an activated decomposition member.
Accepted basis: SCA-APP-007 `Propagation_Plan.md`,
`Operational_Migration_Actions.csv`, and `Decision_Log.md`; accepted
decomposition SHA-256
`dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`.

Work graph version 1 was selected by the human and HELP_HUMAN. Posture was
serialized single-manager integration: pre-audit -> Git-aware move -> runner
routing repair -> provenance/paired metadata -> validation. No Agent 2 was
required. Shared reads were allowed; this manager was the sole writer for the
listed migration surfaces. Runtime telemetry was not required for this
single-member, short-lived activation; token/context occupancy was not
exposed by the runtime.

## Accepted outputs

- Git-aware, byte-preserving move of both historical proof bundles and all 38
  tracked evidence files from the retired DEL-03-06 physical container into
  `Evidence/Historical_DEL-03-06/` under DEL-09-06.
- `Evidence/Historical_DEL-03-06/PROVENANCE.md` records ownership basis,
  old/new roots, source commits `4412157d1` and `deed6f58f`, historical tree
  `a5ba2c806734feeb68f6160f2961c6597d44b40d`, and aggregate parity.
- `Evidence/Historical_DEL-03-06/MIGRATION_SHA256_MANIFEST.csv` records 38
  old/new path mappings, byte counts, pre/post SHA-256 values, and 38 `MATCH`
  results.
- `frontend/scripts/run-network-policy-proof.mjs` now uses the accepted
  DEL-09-06 output root, `NETWORK_POLICY_PROOF_`, the message label
  `DEL-09-06 network-policy proof run`, and the summary title
  `Network Policy Proof Run Summary`.
- DEL-09-06 `_STATUS.md` and `MEMORY.md` each received one provenance-only
  2026-08-01 history entry. `IN_PROGRESS`, Remaining items, authorization
  basis, lifecycle, approval state, and Checking Approval SHA are unchanged.

## Validation

| Check | Result |
|---|---|
| Source inventory | PASS — exactly 38 tracked files before move |
| Per-file pre/post SHA-256 | PASS — 38/38 `MATCH` |
| Pre/post evidence bytes | PASS — 97,817 / 97,817 |
| Aggregate canonical SHA-256 | PASS — `e27ca076ec3fdaeb4f6ba6cba6e716aa50497e130e5b0e3feab5dbc800aca4ff` before and after canonical path substitution |
| Git rename review | PASS — 38 renames detected at 100% similarity |
| Retired live physical root | PASS — `execution/PKG-03_Harness_Runtime_Core` absent |
| Current runner route and generated labels | PASS — exact four approved replacements present; retired route/generated labels absent from current implementation surfaces |
| CONF-002 limitation strings | PASS — both existing OCSP/CRL limitation notes remain byte-identical |
| JavaScript syntax | PASS — `node --check frontend/scripts/run-network-policy-proof.mjs` |
| Focused contract-pin manifest entry | PASS — exact `scripts/run-network-policy-proof.mjs` manifest target, 6/6 pins, executed directly with Node's TypeScript loader |
| Additional frozen routing pins | PASS — 14/14 presence/absence assertions |
| Accepted decomposition identity | PASS — `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` |
| Six-UNKNOWN historical file identity | PASS — `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8` |
| Authority corpus status | PASS — v18, all eight sources `MATCH`, no drift |
| App loop receipt validator | PASS — frozen through Receipt-52; versioned contract satisfied |
| Whitespace | PASS — `git diff --check` and staged diff check |

The canonical `npm test -- src/__tests__/contract-pins.test.ts` wrapper could
not start because this checkout has no installed `vitest` binary. An offline
`npx` attempt was also unavailable from the local cache. The exact manifest
entry and its test semantics were therefore executed directly against the
same source manifest and passed 6/6; no dependency installation or live proof
run was performed. Rerun the canonical wrapper when the frontend dependency
tree is installed.

## Containment, derivative status, and handoff

No SCA-APP-007 file, decomposition, Scope Ledger, objective, dependency,
estimate, schedule, lifecycle state, `_ScopeChange/_LATEST.md`, audit pointer,
authority corpus, PRD, decision/task register, loop receipt, immutable
historical proof byte, or UNKNOWN relation was edited by this run. Existing
unrelated working-tree changes were preserved.

The migrated proof bundles remain historical derivative evidence. Their
internal names and claims are preserved but do not authorize a current
DEL-03-06 identity. No blocker remains for the evidence migration itself.
The next owner is HELP_HUMAN/SCOPE_CHANGE for post-change decomposition audit,
Gate-5 confirmation, candidate closeout, and Git routing. No commit or push
was made.
