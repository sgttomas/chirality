# PKG-04 package summary — SDK Adapter, Prompt Provider, and Settings

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; derived by the orchestrator
  at W2 fan-in from the claim ledgers (plan §7).
- **Ledgers:** `R2_WAVES/PKG-04/DEL-04-0{1..5}_claims.csv` (115 rows, bound at
  `fac46e33f`). Verification: `R2_WAVES/PKG-04/_VERIFICATION.md` (44 rows
  rechecked; 3 refutations accepted; 1 standing contested row).

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## Census (5 deliverables, 115 claim rows)

| Disposition | 04-01 | 04-02 | 04-03 | 04-04 | 04-05 | Total |
|---|---|---|---|---|---|---|
| ALIGNED | 14 | 16 | 18 | 15 | 22 | 85 |
| PARTIALLY_IMPLEMENTED | 7 | 4 | 1 | 2 | 1 | 15 |
| STALE_SPECIFICATION | 2 | 2 | 0 | 1 | 1 | 6 |
| REMAINING_STATE_MISMATCH | 1 | 1 | 1 | 1 | 1 | 5 |
| DOCUMENTED_UNIMPLEMENTED | 1 | 0 | 0 | 0 | 0 | 1 |
| ACCEPTED_DIVERGENCE | 1 | 0 | 0 | 0 | 0 | 1 |
| STALE_ASSESSMENT | 0 | 0 | 1 | 0 | 0 | 1 |
| IMPLEMENTED_UNDOCUMENTED | 0 | 0 | 1 | 0 | 0 | 1 |
| AUTHORITY_CONFLICT / UNKNOWN / DEFERRED_AGENT_WORKFLOW | 0 | 0 | 0 | 0 | 0 | 0 |

## Package-level picture

1. **The adapter/mapper/composer/provider chain is implemented and largely
   current** — options builder, provider-neutral message mapper, persona
   composer, and provider bridge all carry strong ALIGNED cores with
   gate-bound evidence.
2. **DEL-04-01 is the package's open decision center (7 PARTIAL rows + 1
   DOCUMENTED_UNIMPLEMENTED):** the SDK adoption verdict is genuinely open —
   live-environment probe residuals are gated on the D-APP-52 owner act, the
   adoption approver role is unassigned (ACC-002, human-owned NEW-PACKET),
   and the twelve-area residual-risk register lacks a decision-grade record.
   Downstream rows in 04-02 (REQ-012) and 04-03 (REQ014, resolved ALIGNED at
   fan-in) reference this same open verdict — one decision, not several.
3. **Documentation lag mirrors PKG-02:** REF-006 HASH_MISMATCH staleness in
   four kits + setup-era "nothing landed yet" wording (04-01 ACC-003, 04-02
   ACC-002); five `_DEPENDENCIES.md` register rows (three of them the
   Declared-TBD class under the cross-package conflict —
   `_VERIFICATION.md` §3.3).
4. **Fan-in materially tightened the scope calls:** all three unmapped-scope
   rows were refuted (surfaces already owned by DEL-08-04, DEL-05-05/08-05,
   and SPEC §12.2 + DEL-04-02-REQ-004 respectively) and were dropped/folded
   by their owners. The one surviving coverage query is the message.*/queue.*
   event lane (DEL-04-03 UNMAPPED-1).
5. **Standing contested row:** DEL-04-05 RQ-011 (error-classification test
   coverage) — ALIGNED by owner judgment with explicit contest note; the
   deciding question (per-class vs whole-requirement verification bar) is an
   R3/R4 method input.
6. Cross-package handles: max-turn terminal consumer (DEP-04-02-011),
   PKG-05 transcript/store closure, PKG-06/08 fail-closed policy closure,
   D-APP-46/48 assessment-pointer refresh sweep.

## Unknowns / conflicts

One explicitly contested row (RQ-011, recorded); zero AUTHORITY_CONFLICT /
UNKNOWN / DEFERRED_AGENT_WORKFLOW rows.
