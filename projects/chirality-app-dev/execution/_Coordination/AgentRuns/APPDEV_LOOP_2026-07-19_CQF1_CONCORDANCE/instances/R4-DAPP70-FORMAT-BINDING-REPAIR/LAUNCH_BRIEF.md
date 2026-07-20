# R4-DAPP70-FORMAT-BINDING-REPAIR Launch Brief

- **Role:** RECONCILIATION (Agent 1; load and obey
  `agents/AGENT_RECONCILIATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Instance:** `R4-DAPP70-FORMAT-BINDING-REPAIR`
- **Basis commit:** `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`
- **Repair graph:** `../../amendments/R4/FORMAT_BINDING_REPAIR_GRAPH_v1.json`
- **Repair-graph SHA-256:**
  `78a492ec999d48615e6e200d60d386f7aeb000d2cbd16ca016e1a96d7344774e`
- **Integration owner:** this serialized RECONCILIATION instance
- **Delegation:** prohibited
- **Fresh V3:** planned and held; not released
- **Git authority:** none

## Objective

Repair only the reproduced publication-format defects in the graph's exact
ten-file direct set: remove one excess terminal LF from nine files and remove
the exact two trailing spaces from each of D-APP-71 packet lines 3–6. Refresh
only the transitively affected packet, applied-manifest/handoff, Receipt-80,
W1, and V2 hash references or hash-valued claims required for current-byte
internal consistency. Preserve semantics, verdicts, status states, option
posture, and every other byte. Return terminally for a separately released
fresh V3 EVALUATION.

## Preserved diagnostic discrepancy

Current exhaustive per-file no-index reproduction yields exactly 13
diagnostics in ten files: nine `new blank line at EOF` findings and four
`trailing whitespace` findings on D-APP-71 packet lines 3–6. Prior CHANGE
reported 14 diagnostics. Preserve both facts and the unresolved discrepancy;
do not invent, infer, or normalize an eleventh file or fourteenth location.
The repair target is the exact graph-bound 13-location set only.

## Mandatory fail-closed preflight

Before any repair write:

1. require branch `codex/app-dev-dapp70-mapping-application-20260720`,
   `HEAD == 36a422ac5568a02ecf120c214f8e1fc96fd6ab45`, and the existing uncommitted
   W1/V2 tranche plus released v17 controls; perform no fetch, checkout, index,
   ref, commit, push, PR, merge, or other Git-state mutation;
2. strict-parse the repair graph with all-depth duplicate-key rejection and
   reproduce SHA-256
   `78a492ec999d48615e6e200d60d386f7aeb000d2cbd16ca016e1a96d7344774e`;
3. reproduce every direct-defect path and pre-repair hash in graph order;
4. run `git diff --no-index --check /dev/null <path>` separately for each of
   the ten direct files, preserve exact output, and require the union to be
   precisely the graph's 13 locations;
5. record the prior CHANGE count of 14 as an unresolved observation, not an
   extra repair instruction;
6. strict-parse every JSON in the direct and transitive write sets before
   mutation; reproduce W1 terminal
   `APPLICATION_COMPLETE_AWAITING_V2`, V2 terminal `ACCEPT`, D-APP-71 exactly
   `AWAITING_RULING` with selection null and four neutral options, and Receipt-80
   unique/latest with parent Receipt-79;
7. reproduce applied manifest SHA-256
   `eac0ec145d33e55c0ce5dbfe066223812a790183ae33ef7e4c33c27bd408e39c`,
   W1 RETURN/STATUS SHA-256
   `5811a5a94b39596f9e8244cc4c8ac631de87438a8e940c2b9f66d9985df4cc98` /
   `19d56061817027452a46b97ac143b0b6d24a241d0b4e4c1c33ee334ac0cff566`,
   and V2 RETURN/STATUS SHA-256
   `d7a469edf8e96a15d035ea5453be53df3ba52d0f0c0945c706e7821cafdf5160` /
   `2293506289ce27637a673680902555fb6f0139573299fe8ac79f3618eacdf22d`;
8. run the receipt validator, authority-corpus v9 status, repository
   self-check, and a complete before-write containment inventory; and
9. fail closed before partial mutation on any missing path, hash mismatch,
   diagnostic mismatch, JSON/schema failure, semantic/state drift, option
   change, receipt/corpus failure, or write-boundary ambiguity.

## Exact direct-byte repairs

Use the ten paths and pre-repair hashes in the graph as the complete direct
set.

- For each of the nine `remove_one_excess_terminal_lf` entries, remove exactly
  one terminal LF and require the result to end with exactly one LF. Every
  preceding byte must be identical except for separately authorized hash-token
  refreshes in that same file.
- In the D-APP-71 packet, remove exactly the two trailing U+0020 bytes from
  each of lines 3, 4, 5, and 6. Preserve all visible text, line order, option
  wording, `AWAITING_RULING` posture, and every other byte.
- Perform no general formatter, wrapping, heading, punctuation, spelling,
  ordering, or newline rewrite.

## Transitive binding repair

After the direct-byte repairs, calculate the old-to-new SHA-256 map and update
only current-byte hash references or mechanically dependent hash-valued claims
within the graph's seven-path transitive reference write scope. The permitted
chain is:

1. D-APP-71 packet hash into the applied handoff and manifest and Receipt-80;
2. applied handoff hash into the applied manifest;
3. packet, applied-manifest, applied-handoff, receipt-ledger, W1 STATUS, and W1
   HANDOFF hashes into the W1 terminal surfaces where currently asserted;
4. repaired W1 RETURN/STATUS/applied-manifest and repaired V2 child/output
   hashes into the current V2 report/return/status surfaces where currently
   asserted; and
5. V2 RETURN hash into V2 STATUS.

Hash substitution does not authorize prose changes. Preserve all non-hash
text and all semantic/accounting claims. Preserve v16, amendment V2, the V2
launch brief, and the pre-v17 HANDOFF_STATE prefix as historical launch-time
bindings; the R4 return must provide the exact old-to-new map rather than
rewriting those historical controls.

Receipt-80 may be edited only in its existing Pointer hash tokens required by
the corrected packet/applied manifest. Do not append Receipt-81, change any
receipt prose, reorder receipts, change Examined-Through or parentage, or edit
any earlier receipt.

## Required validation and terminal evidence

After all authorized bytes settle:

- strict-parse every JSON in the direct/transitive sets with recursive
  duplicate-key rejection and validate expected schemas/fields;
- reproduce the complete old-to-new hash map and prove every superseded hash
  has no remaining current-byte reference in the repaired W1/V2/receipt/
  applied cluster, excluding the explicitly preserved historical controls;
- run individual `git diff --no-index --check /dev/null <path>` checks for all
  ten direct files and every text file changed transitively; require zero
  diagnostics;
- run actual repository-level `git diff --check` and
  `git diff --cached --check`; require both exit zero, while separately proving
  untracked paths through the no-index checks;
- run the receipt validator, authority-corpus v9 status, repository self-check,
  applied-manifest closure, W1/V2 corpus/hash checks, and exact final write
  containment;
- byte-compare every changed path and classify every delta byte as one of the
  13 authorized whitespace deletions, an exact old-to-new hash-token
  substitution, or this instance's own terminal output;
- prove W1 remains `APPLICATION_COMPLETE_AWAITING_V2`, V2 remains `ACCEPT`,
  D-APP-71 remains `AWAITING_RULING` with selection null and unchanged options,
  all 22 mapping rows/nine groups and 21+1 treatment split remain unchanged,
  and no deliverable lifecycle/status, source, SOW, dependency, authority,
  release/publication, or hard-fence state changed; and
- write `RETURN.md`, `HANDOFF.md`, and terminal `STATUS.json` in this instance,
  including exact changed-path inventory, pre/post hashes, checks, the 13/10
  versus prior-14 discrepancy, blockers, waivers, and V3 rerun requirement.

Return exactly `FORMAT_BINDING_REPAIR_COMPLETE_AWAITING_V3 | BLOCK`.

## Write authorization

Write only:

1. the graph's exact ten direct-defect paths;
2. the graph's exact seven transitive-reference paths; and
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE/instances/R4-DAPP70-FORMAT-BINDING-REPAIR/`
   for `RETURN.md`, `HANDOFF.md`, and terminal `STATUS.json` only.

Do not write the v17 update, repair graph, this launch brief, HANDOFF_STATE,
v16/amendment-V2/V2-launch historical controls, decision register, any other
decision or receipt, frontend/runtime source, deliverable `_STATUS.md`, local
R5 records, SOW/dependencies, decomposition, authority corpus, prior R1/V1/R3
evidence, lifecycle/Approval SHA/MEMORY, or Git/index/ref/PR state. Do not
delegate. Do not execute or release V3. No waivers.
