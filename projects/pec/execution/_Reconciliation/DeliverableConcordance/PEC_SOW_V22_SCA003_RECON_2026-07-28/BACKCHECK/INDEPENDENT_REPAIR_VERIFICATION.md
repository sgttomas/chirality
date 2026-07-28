---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
phase: R4_REPAIR_INDEPENDENT_VERIFICATION
role: independent_agent_2_verifier
result: FAIL
status_policy: NO_STATUS_TOUCH
effective_claim_repairs: 57
contracts_examined: 11
unknowns_preserved: 22
authority_conflicts: 0
---

# Independent repair verification

## Verdict

**FAIL.**

All 57 approved claim IDs are present, and the approved edits within those
claims accurately express the current PRD v2.2 / SCA-003 authority without
creating a consumer duty. The repair tranche nevertheless does not pass
fan-in:

1. `DEL-10-10` retains a stale v2.1 `SOW-064` source-reference statement and
   omits `D-PEC-68` from its ordered source chain.
2. `DEL-10-11` still describes its lifecycle as `OPEN`, although its accepted
   `_STATUS.md` is `INITIALIZED`.
3. `DEL-10-11/AX-001`, which is outside the effective 57-ID repair set, gained
   a new semantic sentence. The sentence is source-accurate and creates no
   consumer duty, but neither the original disposition nor amendment 1
   authorized changing that local definition.

The first two findings are missed whole-contract current-source/lifecycle
bookkeeping explicitly inside the R4 repair boundary. The third violates the
exact-set containment rule. No contract or status file was changed by this
verification.

## Effective authority set

The immutable W1 ledgers identify 56 `RepairNeeded=YES` rows. The accepted
`W1_DISPOSITION_AMENDMENT_1.md` and owner-approved
`DECISION_PACKETS/R4_AMENDMENT_1.md` add `DEL-10-11/CLM-002`, yielding the
effective set of **57 claim repairs across 11 contracts**. The original
ledgers remain valid discovery evidence and were not rewritten.

The amendment directs that `DEL-10-11/CLM-002` preserve the parity statement,
per-reconcile denominator, silences, and unknowns; replace only the stale §11
heading quotation; and create no polling, contact, cadence, injection,
consumer-use, or receiving-loop-conformance duty.

## Reproduced positive checks

- **Approved-ID coverage:** 57/57 approved local IDs are present in the
  repaired contracts; none is omitted.
- **Approved-block change coverage:** every one of the 57 approved definition
  blocks differs from its pre-repair contract block. Three approved repairs
  (`DEL-08-04/CLM-002`, `DEL-08-04/CLM-008`, and
  `DEL-10-10/CLM-001`) place the repaired material in continuation text rather
  than changing the first definition line.
- **Amendment repair:** `DEL-10-11/CLM-002` now quotes the exact PRD v2.2
  heading, “Success metrics (measured in observable system and use
  behavior).” Its parity population, `per reconcile` denominator, and stated
  silences remain intact.
- **Structural stability:** local-definition IDs, classes, source order, and
  per-contract counts are unchanged across all 11 contracts. The aggregate
  definition/ledger population remains 794/794.
- **Unknown preservation:** all 22 W1 `UNKNOWN` definitions remain present and
  unchanged; no repair silently resolves them.
- **Authority and duty boundary:** no approved repaired claim introduces an
  authority conflict, PEC self-polling, external scheduling, unsolicited
  injection, receiving-loop conformance, or a consumer-owned mode/cadence duty
  for PEC. Pipeline/unscoped use can still have zero contact; enabled
  consumers own use, mode, cadence, and optional injection; P2-B retains only
  owner use/non-use evidence; directed bootstrap remains PEC's own build graph.
- **Historical/live posture:** the repaired claims retain ADR-002 as live and
  ADR-014 as historical only.

## Effective per-deliverable claim set

| Deliverable | Approved repaired local IDs |
|---|---|
| `DEL-00-01` | `OUT-002`, `CLM-002`, `REQ-005`, `AC-003`, `VER-002`, `AX-002`, `AX-004`, `AX-006` |
| `DEL-03-06` | `CLM-016`, `CLM-020`, `AX-012` |
| `DEL-04-01` | `CLM-016`, `CLM-018`, `REQ-010`, `AX-007`, `AX-012`, `AX-013` |
| `DEL-04-02` | `CLM-016`, `CLM-017`, `REQ-013`, `AX-013` |
| `DEL-04-03` | `CLM-016`, `CLM-017`, `AX-011` |
| `DEL-08-01` | `CLM-003`, `CLM-004`, `AX-004`, `AX-006` |
| `DEL-08-03` | `CLM-011`, `REQ-005`, `CON-001`, `CON-003`, `AX-006`, `AX-010` |
| `DEL-08-04` | `CLM-002`, `CLM-008`, `CLM-010`, `CLM-014`, `CON-005`, `AX-012` |
| `DEL-10-01` | `CLM-004`, `CLM-007`, `AX-005`, `AX-007` |
| `DEL-10-10` | `CLM-001`, `CLM-002`, `CLM-004`, `CLM-005`, `CLM-020`, `AX-011` |
| `DEL-10-11` | `CLM-002`, `CLM-003`, `CLM-015`, `CLM-017`, `CON-003`, `AC-015`, `AX-009` |

## Exact blocking findings

### 1. `DEL-10-10` retains stale and incomplete source bookkeeping

`DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md:84`
states:

> `SOW-064`'s `SourceRef` is "PRD v2.1 §12, D-PEC-61"

That is false for the current accepted row. The contract itself quotes the
current `SOW-064` row at line 109 and attributes its current `SourceRef` at
line 114 as:

> `PRD v2.2 §12, D-PEC-61, D-PEC-68`

The ordered source chain at lines 89–98 likewise names PRD v2.2 and
`D-PEC-61` but has no `D-PEC-68` entry. This leaves the introductory authority
account internally inconsistent and incomplete. The approved DEL-10-10 repair
notes expressly required updating the opening SourceRef and ordered source
chain to PRD v2.2 plus `D-PEC-68`; the repair did not land.

### 2. `DEL-10-11` retains a stale lifecycle statement

`DEL-10-11_Parity_metric_DriftFindings_per_reconcile/ScopeOfWork.md:270-271`
states:

> inspections and exercises over fixture inputs, because at `OPEN` no measured
> population exists

The accepted deliverable lifecycle is `INITIALIZED`, not `OPEN`. R4 included
correction of embedded lifecycle prose in the whole-contract bookkeeping
boundary. This stale statement therefore fails current-source accuracy even
though it is outside a bold local definition.

### 3. `DEL-10-11/AX-001` changed outside the approved set

`DEL-10-11/AX-001` was not one of the original 56 approved IDs and was not the
single ID added by amendment 1. Its repaired definition adds:

> The current `PRD.md` §11 heading refines the measurement posture to
> "observable system and use behavior".

The addition is accurate and does not impose a consumer obligation. It is
nevertheless a semantic change to an unaffected local definition. Amendment 1
authorizes that heading correction only for `DEL-10-11/CLM-002` and says
“replace only” there. Under the exact 57-ID repair boundary, `AX-001` must
either be restored to its prior definition or added through another versioned,
owner-approved disposition amendment.

Five other apparent extra block diffs do not constitute unauthorized
local-definition edits: their definition lines are unchanged and their
differences occur in adjacent lifecycle, quotation-record, or output-matrix
bookkeeping. The `DEL-08-03/CLM-005` continuation updates a stale statement
that `DEL-08-04` had no accepted contract; the correction is current-source
bookkeeping and does not change the claim's duty boundary.

## Required correction before a passing rerun

1. Correct the DEL-10-10 introductory `SOW-064` SourceRef to
   `PRD v2.2 §12, D-PEC-61, D-PEC-68` and add `D-PEC-68` to the ordered source
   chain.
2. Replace the stale DEL-10-11 production-method lifecycle reference `OPEN`
   with `INITIALIZED`, without asserting that a measured population exists.
3. Restore DEL-10-11/AX-001 to its pre-repair definition, or obtain a
   versioned owner-approved amendment that adds it to the repair set.
4. Re-run structural validation, exact repair-set containment, current-source
   backcheck, and independent fan-in verification.

The hold must remain in force until those corrections pass a fresh independent
verification.

## Evidence identity and preservation

The 11 contract SHA-256 values examined were:

| Deliverable | SHA-256 |
|---|---|
| `DEL-00-01` | `ddb4e1df36b74401172d930c230daa75637b8d4bdaee2b584d4749eb707ed223` |
| `DEL-03-06` | `b526ddb373ae8fee2695ca789622f5df8725e948e75c311bf6ce718b27ac102b` |
| `DEL-04-01` | `9620646f511eaa102046fce26dfd767cbee8b719c6094d8a5c77bb3a839e8e28` |
| `DEL-04-02` | `153085c7fe440c51b1fd8dc42dd760647dd3f8a31aa5e7bd8d4878b2157931a8` |
| `DEL-04-03` | `f1a5831e1d14aea2a1a189035a9586c4af56573d508f37e175dc4382933364d2` |
| `DEL-08-01` | `3087aeab6d7eb49bb912e3bec4d052280ae72bf69791a8b739042d117530d315` |
| `DEL-08-03` | `e7a4eafdec3210e6ccc4352ed895ce1db4f7839ee4c8b3cb3a892752c7dbd6dd` |
| `DEL-08-04` | `1b0b1feb86ff34331a469e26019b7ee5f5bf34ee8564a9f1fec8c30d93213814` |
| `DEL-10-01` | `7e80787bc17634728fad2a084c422daecbc3936e552d05761c43628865672ae6` |
| `DEL-10-10` | `b614f3be77253fe49edec31c2b6d48bdba9c410ec1ed33472dc46172b342fc71` |
| `DEL-10-11` | `8e8cf46a3cf93d96cf32d53673838508131cb3bb8ab51037f079721b734b71d5` |

`WAVES/W1/W1_LEDGER_VERIFICATION.md`, the immutable W1 ledgers, both accepted
amendment instruments, all contracts, and all status surfaces were read only.
The initial failed W1 verification remains preserved. This report is the sole
file written by this rerun.
