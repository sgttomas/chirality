# SYN Loop Receipts -- ZEBRA-PROSE-RCP01-TITLE invented ledger

> ZEBRA-PROSE-RCP01-HEADER Invented ledger for parser fixtures only; nothing
> here describes a real loop, decision, run or merge.

## Rules

1. ZEBRA-PROSE-RCP01-RULE-ONE pointers over narrative, in invented form.
2. ZEBRA-PROSE-RCP01-RULE-TWO entries after the marker comment carry cursor fields.

- **2026-08-01 -- Receipt 1** (ZEBRA-PROSE-RCP01-E1-TITLE first invented entry).
  - Pointers: `projects/syn/execution/_Coordination/SYN_NOTE_0001.md`; PR #9901.
  - Checks: ZEBRA-PROSE-RCP01-E1-CHECKS the kettle test passed.
  - Gate outcome: ZEBRA-PROSE-RCP01-E1-GATE stopped after the first key.

- **2026-08-02 -- Receipt 2** (ZEBRA-PROSE-RCP01-E2-TITLE second invented entry).
  - Pointers: PR #9902 at `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`.
  - Gate outcome: ZEBRA-PROSE-RCP01-E2-GATE parked for an invented owner.
<!-- receipt-contract-v2 frozen-through=Receipt-2 prefix-bytes=890 prefix-sha256=936296a7d4b8fbe0b359b88e1e4540de5d0294a3e2c7d72749a540b8fd94525d -->

- **2026-08-03 -- Receipt 3** (ZEBRA-PROSE-RCP01-E3-TITLE first governed entry).
  - Receipt-ID: `Receipt-3`
  - Examined-Through: `cccccccccccccccccccccccccccccccccccccccc`
  - Parent-Receipt: `Receipt-2`
  - Pointers: PR #9903.
  - Gate-Outcome: `SYN-EXECUTED`

- **2026-08-04 -- Receipt 4** (ZEBRA-PROSE-RCP01-E4-TITLE second governed entry).
  - Receipt-ID: `Receipt-4`
  - Examined-Through: `dddddddddddddddddddddddddddddddddddddddd`
  - Parent-Receipt: `Receipt-3`
  - Gate-Outcome: ZEBRA-PROSE-RCP01-E4-GATE the invented gate closed after a
    long sentence about kettles, which is prose and not a token.
