# Agent 2 Brief R5 — Candidate-Whitespace Repair Verification

## Role and objective

Act as a genuinely fresh bounded adversarial verifier. Determine whether the
single-byte terminal-blank repair to `APP_CORPUS_MANIFEST.sha256` preserves the
accepted D-APP-90 derivative package and whether its current pointer surfaces
may be rebound without creating an A/B/C selection or D-APP-91 ruling.

Return exactly one verdict: `ACCEPT`, `ACCEPT_WITH_NONBLOCKING_NOTES`, or
`BLOCK`.

## Sealed scope

Read-only scope is limited to:

- this R5 brief;
- `WHITESPACE_REPAIR_BACKCHECK.md`;
- the repaired `APP_CORPUS_MANIFEST.sha256`;
- current `VALIDATION.md`, `MANAGER_RETURN.md`, and `HANDOFF_STATE.md`;
- D-APP-91 proposal packet and its single register row; and
- historical R4 brief/return/`REPAIR_BACKCHECK.md` only to confirm that those
  files remain historical and unmodified.

The verifier may use read-only filesystem and Git inspection needed to test
these claims. It must not write files, mutate Git, access the network, invoke
native Pi, delegate, select A/B/C, record a ruling, or inspect unrelated
product/coordination scope.

## Bound facts to challenge

1. The manifest changed from SHA-256
   `66b6f32e75eed66dd63a2ac7b0712bc317e3c59f15dac3d5edcb7eda316b79be`
   to
   `864d04e7ebdbe4f112fc9145445e718338b82e2524d45d6838ed609182b15956`.
2. Its byte count changed from `26365` to `26364`, solely by deleting one
   terminal LF; the repaired file ends in exactly one LF and no blank line.
3. It still contains exactly 185 data lines with unchanged data-line digest
   `ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`.
4. All 185 selected current paths reproduce their recorded hashes with zero
   mismatches.
5. Historical R4 artifacts remain untouched and must not be represented as
   verification of the repaired bytes.
6. Rebinding current validation/manager/handoff and the D-APP-91 packet and
   register to the accepted R5 return is derivative pointer maintenance only.
7. D-APP-91 remains `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`; no
   D-APP-91 ruling, Receipt 116, Task Management, Root, source/product, or Git
   action belongs in this repair.

## Required checks

- independently confirm facts 1–4 against the actual repaired bytes and Git
  parent/base bytes;
- confirm the diff contains no manifest data-line change;
- confirm the R4 historical files are not in the repair diff;
- identify every current pointer that must be rebound from the stale R4 or
  pre-repair identity;
- confirm the proposed pointer-only rebind cannot be misconstrued as a human
  selection or ruling; and
- report any blocking discrepancy with exact path and evidence.

## Return contract

Return a compact durable report containing:

- verdict and verifier freshness/tool declaration;
- exact old/new manifest hashes, byte counts, line count, data-line digest,
  and selected-path reproduction result;
- historical-R4 preservation result;
- required current-pointer rebind list;
- no-selection/no-ruling finding; and
- blocking findings or exact nonblocking notes.

The manager will preserve the return under
`reviews/A2_ADVERSARIAL_VERIFIER_RETURN_R5.md`, compute its SHA-256, and only
then perform the mechanical current-pointer rebind and final validation.
