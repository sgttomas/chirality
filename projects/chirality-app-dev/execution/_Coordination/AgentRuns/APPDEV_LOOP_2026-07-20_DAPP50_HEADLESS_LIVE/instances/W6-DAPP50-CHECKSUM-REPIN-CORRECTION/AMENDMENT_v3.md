# W6 Amendment v3 — Minimal Missing-Baseline Recovery

The fresh recovery owner has read-only project scope. It must:

1. reproduce G2 HEAD/topology, frozen W6 project hashes from update v13,
   Receipt-85 ledger hash
   `c8a7ab466fc694b6743310a8a5cd6f75c4280c49fb67baac1c6717da442bb0e8`,
   unchanged Receipts 83/84, empty index, and absent `frontend/dist`;
2. run exactly `python3 -m pytest -q tools/practitioner_harness` once and retain
   exact exit/count output;
3. inspect the interrupted owner's reported evidence for every other original
   gate and disclose that provenance in the terminal return;
4. write W6 `RETURN.md`, `HANDOFF.md`, and terminal `STATUS.json`.

No project-content edit, Receipt change, other test rerun, Git action, cleanup,
delegation, or downstream release. Return ACCEPT only if the missing baseline
passes and all frozen-state checks reproduce; otherwise BLOCK.
