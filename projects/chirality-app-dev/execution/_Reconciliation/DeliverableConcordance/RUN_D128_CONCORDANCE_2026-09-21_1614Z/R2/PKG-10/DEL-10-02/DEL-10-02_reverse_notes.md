# DEL-10-02 reverse-pass notes (R2, PKG-10)

The reverse pass answers 281 capabilities from six area files, in this order: BUILD, ELECTRON,
HARNESS, RTCONTRACT, RTCORE, SETTINGS.

- **PARTIAL (1):** CAP-RTCONTRACT-040, the domain profile contract, maps to `DEL-10-02#CLM-003.2`.
  - The contract's `protected_write_paths` and `agent_writable_paths` fields are the data this policy relies on.
  - The contract itself belongs to DEL-10-01.
- **NOT_MINE (280).**
- **CLAIMED_BY (0).** DEL-10-02 is a doc-only future-boundary policy (D-APP-37), and no capability at the frozen basis implements protected-path or proposal-path enforcement. That matches the forward finding that no live-path guard exists (CLM-003.4).

## Coverage

No forward coverage gap was found. None of the six areas holds a capability that enforces a domain protected-path deny, a proposal-path write allowance, or a gated domain apply.

Two capabilities give live-path context for the enforcement question in CLM-010.9 (R4-Q1), but DEL-10-02 does not own them:
- CAP-RTCONTRACT-019: the mapping from permission mode to Codex approval and sandbox policy.
- CAP-HARNESS-047: the legacy audit hooks.

## Errata

There are no errata, so the sealed and errata-applied census figures are the same (see `DEL-10-02_notes.md` §1).

## Observation for the manager (REACH granularity)

For two modules, a capability file and the evidence pack's `REACHABILITY.csv` give different reach. The ledger follows the evidence-pack map as the rulebook requires (CONVENTIONS §2.3 [INTEG], §9), so I raised no errata. The verifier may want to reconcile the two sources.

| Module | Capability file | Evidence pack (module-level) | Why they differ |
|---|---|---|---|
| `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts` | CAP-RTCONTRACT-040: `REACH=TEST_ONLY` | `LIVE` | The capability file says the module is live "only via contracts barrel; no non-test consumer" |
| `projects/chirality-runtime/packages/core/src/agent1-run-coordinator.ts` | CAP-RTCORE-024: `REACH=TEST_ONLY` | `LIVE` | Not stated in the capability file |

Neither difference changes a DEL-10-02 disposition:
- The contract types are cited only as inert data.
- `agent1-run-coordinator.ts` is cited only to show that its `protectedPaths` option does not cover domain paths.
