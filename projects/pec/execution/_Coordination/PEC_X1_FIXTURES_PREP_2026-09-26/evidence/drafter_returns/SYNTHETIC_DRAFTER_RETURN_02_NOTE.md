# Synthetic drafter — revision 02 (manager note)

The synthetic drafter's second hand-back (after the manager's rulings on em dash, token
case and grammar-dependent counts) was delivered in-session, not as a file. WORKING_ITEMS
records here what it reported and what was checked:

- Em dash: 24 ` -- ` separators became U+2014 in five memory files (bullet openings and
  dated headings) and all nine work_graph titles; receipts unchanged, so the synthetic
  ledgers' marker prefix-bytes/prefix-sha256 values still verify.
- Token case restored in the manifest (states, receipt field names, cursor/folder tokens).
- 33 grammar-dependent expectations removed (node, state, entry, row, link and PR-link
  counts; `run_identity_available` in SYN-WG-04 and `receipt_id_available` in SYN-RCP-03).
  Counts fixed by construction kept (SYN-WG-04 nodes 0; SYN-MEM-04/05 entries 0;
  SYN-RCP-05/06 receipts 0; SYN-WG-05 cited PR 99999999). Contract-fixed tokens added
  (decoy tokens, the unrecognized token, the shared deliverable, link-text markers).
- Drafter's runs: candidate suite 10/10 with the drafting stub; wider copy check over 300
  feed-named blobs at d61981ee2 and 6c6cc1b00: 0 overlaps.
- The 28 git blob ids it reported equal the installed candidate files (manager check with
  `git hash-object`, no `-w`); the manifest is blob `b191bd8d5fc18e6507d793638adaf91b9f130100`.
- Scratch directory: `…/scratchpad/x1syn.Wsbloe`; no worktree writes, no branch operations.
