# R1-CONTROL-REISSUE Launch Brief — Unique-Member Terminal Control Record

- **Role:** RECONCILIATION (Agent 1; load and obey
  `agents/AGENT_RECONCILIATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Attempt:** `R1-CONTROL-REISSUE`
- **Basis:** `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- **Routing authority:** `amendments/R1/v5.md`
- **Scope:** control record only; zero subject or derivative-package writes
- **Sole write root:** this instance directory

## Objective

Resolve only V1R2-001/GPE-001 by emitting a new additive terminal R1 control
record with exactly one structured `control_label_erratum` member. Preserve
R1-REPAIR2 and every derivative/predecessor byte; bind unchanged substantive
results and downstream blocks; validate strict and ordinary parser
equivalence; and return for a separately released fresh V1.

## Mandatory immutable-input preflight

Before updating this instance status:

1. Require HEAD/origin basis, exact 22-row manifest/order/hash, five Remaining
   populations/statuses, and no subject/authority drift.
2. Bind R1-REPAIR2 return/raw status to
   `bb520447e5923a36fca6533379ff49458dbb0fbbfcefe6edbfaf7ae4f2f4a12a`
   and
   `a48d9a634f279726f9c3cc4b23fb8e558b58f34502cd03ae6c87c5f6f4537a44`.
3. Bind sealed child brief/return to
   `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`
   and
   `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0`.
4. Bind V1-RECHECK2 return/status, protocol/report/findings/handoff, technical
   child launch/return, and governance child launch/return to
   `cfb858139539f038629d06279f2c259c6948dff7ede772dad48ea1b12515820e`,
   `af250ce853165152321c993fe3065f2df2b36ab774c1f67e8057e493875c0fe4`,
   `4e835f298071d92b7e18a449538143256174622ffe0903963c5197e5ddbbd50f`,
   `81cf1298e32e7a263fd6f01136fe29857102ac5a21d26fb25efa622a0855a0ea`,
   `43ba5e391b2a867cda1d2cea098859b757c140ff125762ef4210dd4932025f05`,
   `428afe00ead5b6130f18f9c5bea9c9986270c8203323ba8976c6181d79fbd4a0`,
   `ab2cd7ebbeffc0b9d17e5e06fb0ac644d16d7d3cd9dd2ff628af62291d35d278`,
   `32474f641ac1de6ba55ad521466bad375ff3280c0951bc1d4e636927c655682d`,
   `f234f799f8797b23f1f68275d79874e25f22d9f6ca8116da9b824b6f38e220fb`,
   and
   `f67c7707e7e705717339374d36c4469fce7aae2f37e8845d6f24088dae2aedb3`.
5. Recompute all 14 derivative hashes from the R1-REPAIR2 return, including
   ledger `b56f8773...`, mapping `a01651fb...`, slate `f6e630e9...`, and
   fidelity matrix `100445dd...`; reproduce 22×13, 22×7, 14×19 schemas, 22
   owner-class rows, nine groups, 5/5/4/0 matrix totals, EOF, and hygiene.
6. Reproduce V1R2-001 against the immutable predecessor raw bytes: exactly two
   unequal structured/string values, ordinary last-member path loss, and
   strict duplicate rejection.
7. Verify this instance directory is the only write root.

Fail closed without altering any predecessor or package if any condition
fails.

## Exact control record

Update this instance's `STATUS.json` terminally while retaining exactly one
top-level `control_label_erratum` member with this value and order:

```json
{
  "classification": "NON_CONSEQUENTIAL_CONTROL_LABEL_ERRATUM_SUSTAINED",
  "correct_paths": [
    "projects/chirality-app-dev/frontend/src/app/globals.css",
    "projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts"
  ]
}
```

Do not add another member with that name. Do not store a scalar substitute.
Record V1R2-001 as repaired by additive control reissue while preserving the
immutable predecessor finding and raw hash.

## Required parser validation

Validate the final status raw bytes with:

- an ordered-pair or equivalent duplicate-rejecting parser that rejects any
  repeated member at every object depth;
- Python ordinary `json.load`;
- Node `JSON.parse`; and
- jq ordinary parsing.

Require all four accepted representations to expose the same structured
`control_label_erratum` object with exact classification, exact two-path
array, and array order. Require exactly one raw top-level occurrence. Record
tool versions/availability, commands or deterministic method, results, and
the final status SHA-256 in `RETURN.md`.

## Unchanged substantive bindings

The return and terminal status must bind, without copying or rewriting:

- all 14 derivative hashes and package file count;
- exact manifest hash, 22 rows, 22 `OWNER_CLASS`, nine groups and population;
- 14×19 fidelity matrix and 5/5/4/0/0 totals;
- sealed child and V1-RECHECK2 hashes;
- V1-001..004 and V1R-001/002 repaired/sustained states;
- V1R2-002 earlier wrong-label erratum sustained;
- V1-005 nonblocking/unrepaired observation; and
- owner routing, W1, subject repair, lifecycle, publication, and Git holds.

## Write authorization and prohibitions

Write only `RETURN.md` and terminal `STATUS.json` within this instance. Do not
write the activated derivative package, subject/runtime, Remaining/SOW/
dependencies, prior R1/V1 instances or children, evaluation roots,
decisions/registers/receipts, plan/graph, authority, lifecycle, or Git state.
No delegation or child output is required for this deterministic control-only
attempt.

## Terminal return and next gate

Return terminally to HELP_HUMAN with preflight, unique-member, strict/ordinary
parser equivalence, final hashes, unchanged bindings, write containment,
changed-path list, blockers, waivers, and explicit request for one fresh V1
from the corrected control binding. Do not release or run V1.

Any duplicate member, parser divergence, path loss, input drift, package hash
change, write escape, or downstream release is terminal fail-closed evidence.
Owner routing and W1 remain blocked. Waivers: none.
