# Run Summary

`RUN_STATUS = WARNINGS`

`AUDIT = SCA-APP-008-GATE5-POST-APPLICATION`

## Outcome

The post-application dependency corpus is fully readable and schema-valid: 51/51 registers, 564/564 populated evidence rows, 51/51 `IMPLEMENTS_NODE` anchors, and 112/112 active deliverable endpoints resolved. The four refreshed dependency registers match their pinned identities.

The accepted SCA objective-relative orderings remain intact and non-gating where specified. The live dependency-register graph independently contains one directed nine-node SCC with 10 enumerated elementary cycles and five isolated deliverables. Those findings are warnings; they are neither silently linearized nor treated as a substitute for the accepted objective-relative graph.

## Key identities

- Applied decomposition: `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
- DEL-02-05 dependency register: `c39a3d533bf5f811f35d3a3b7fbfd839e7c1baedc28607cc4d59ad9eb200b8d0`.
- DEL-08-04 dependency register: `6c838e527a0f45f26dd12ae8ff15724369be23a8fce2f15114c9abf46ad9c9ed`.
- DEL-08-05 dependency register: `70b4ef79271978b1b6d99ed34d768f8970ca67307ea819c024a2fe9138634042`.
- DEL-09-05 dependency register: `bde522ad79fb274157fe2bfa27ae527bb6c8715ed167235cf89a6576a8310afb`.
- Accepted DAG: `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996`.
- Accepted work graph: `273c14cc9abe8b2f61696757507b1879479f2ac5d0b94138b6a8fcc07d5e6428`.
- Registered analyzer: `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91`.

## Next action

SCOPE_CHANGE should consume this warning-bearing derivative package in the four-state Gate-5 handoff. Any future decision about the live nine-node SCC belongs to the cycle-resolution workflow; this audit grants no repair, activation, implementation, or release authority.
