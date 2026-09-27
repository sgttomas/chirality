# SYN Loop Receipts -- ZEBRA-PROSE-RCP04-TITLE invented malformed ledger

> ZEBRA-PROSE-RCP04-HEADER Invented ledger whose structure is broken on purpose:
> orphaned cursor bullets, an empty Receipt-ID, a doubled Examined-Through with
> conflicting values, an unclosed entry heading and a field without its colon.

<!-- receipt-contract-v2 frozen-through=Receipt-0 -->

  - Receipt-ID: `Receipt-1`
  - Examined-Through: `ffffffffffffffffffffffffffffffffffffffff`

- **2026-08-12 -- Receipt 2** (ZEBRA-PROSE-RCP04-E2-TITLE doubled field).
  - Receipt-ID:
  - Examined-Through: `abababababababababababababababababababab`
  - Examined-Through: `cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd`
  - Parent-Receipt: `Receipt-1`
  - Gate-Outcome: `SYN-EXECUTED`

- **2026-08-13 -- Receipt 3 (ZEBRA-PROSE-RCP04-E3-TITLE unclosed heading
  - Receipt-ID: `Receipt-3`
  - Parent-Receipt `Receipt-2`
  - Gate-Outcome: `SYN-EXECUTED`
