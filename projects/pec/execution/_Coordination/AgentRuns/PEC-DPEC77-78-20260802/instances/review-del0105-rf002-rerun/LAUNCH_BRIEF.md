# REVIEW launch brief — DEL-01-05 RF-002 independent rerun

RequestedBy: HELP_HUMAN  
RunID: PEC-DPEC77-78-20260802  
InstanceID: review-del0105-rf002-rerun  
DeliverableID: DEL-01-05  
ReviewType: INDEPENDENT_VERIFICATION

## Activation condition

Do not begin until `working-items-del0105-rf002` has returned a complete
bounded repair. The owner expressly authorizes a fresh independent review from
`INITIALIZED` against the revised candidate, including novel-form probes.

The producer prerequisite is now satisfied. Bind the rerun to revised
`D-PEC-77_ACTIVATION.md` SHA-256
`111203c7fb3da9d8efc8d95765e0ecce8cddeafbd59a61f71599ab6d9b26448e`
and execution handoff SHA-256
`3e5a7d586181eb7f8c6040286586743e0a42efcbef6c74b3673fe04f75f72476`.

## Objective

Independently verify the revised checker and exact candidate inventory under
formal REVIEW. Re-run the complete deterministic eleven-item SOW checklist,
the independent-verification checks, and CU-001 containment. Specifically:

- reproduce the three owner-bound regression source hashes and require BLOCK;
- create fresh temporary novel-form probes not present in the producer tests,
  covering additional import aliases, imported symbols, assigned socket
  instances, and inline socket constructors;
- preserve Unix-domain and loopback-only PASS behavior;
- verify the repair is general AST/import-binding resolution rather than a
  spelling patch;
- verify checker SHA-256
  `3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643`
  and locality-test SHA-256
  `69051b4c127009c821886c4cc6aea70222f57c3ad51013bdebe53a6211d92d20`;
- evaluate RF-002 resolution on exact revised hashes;
- retain RF-001 as open until Agent 0 performs the final manifest reseal; and
- verify no path/act fence breach and no lifecycle change.

## Write scope

Only DEL-01-05 `_REVIEW.md`, `Review_Findings.csv`, a new immutable
`REV_DEL-01-05_*` snapshot, Reviews `_LATEST.md`, and this instance's
`RETURN.md`/`STATUS.json`. Candidate product, evidence, manifest, lifecycle,
decomposition, Task Management, and foreign surfaces are read-only.

Return exact hashes, novel probe sources/hashes/outcomes, RF-002 status,
RF-001 status, and the next owner interface. No artifact acceptance or
lifecycle act is inferred.
