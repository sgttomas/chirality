# R5 repair summary

- Authority: `D-PEC-69` R4, including owner-approved amendment 1.
- Applied repairs: 57 claim-local corrections across 11 contracts.
- Changed contracts: `DEL-00-01`, `DEL-03-06`, `DEL-04-01`,
  `DEL-04-02`, `DEL-04-03`, `DEL-08-01`, `DEL-08-03`, `DEL-08-04`,
  `DEL-10-01`, `DEL-10-10`, and `DEL-10-11`.
- Repair boundary: current PRD v2.2 / decomposition revision 1.3 semantics,
  accepted-basis metadata, and embedded lifecycle facts in the selected
  contracts only.
- Preserved: all stable claim IDs, explicit unknowns, topology, dependency
  registers, implementation, runtime, `_STATUS.md`, `_CONTEXT.md`,
  `_REFERENCES.md`, estimates, schedules, release state, and reliance state.
- Hold: `PEC-HOLD-001` remains active; held `DEL-00-01` claims `CLM-005` and
  `REQ-004` were preserved byte-for-byte.

The row-level record is `REPAIR_MANIFEST.csv`. It contains exactly one row for
each effective R4 repair and records pre/post claim hashes, the repair
instruction, and authority.
