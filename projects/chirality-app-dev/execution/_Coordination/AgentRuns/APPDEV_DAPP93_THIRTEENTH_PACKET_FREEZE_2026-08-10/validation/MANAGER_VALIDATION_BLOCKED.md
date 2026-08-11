# Manager validation — blocked at total-invocation preflight

Verdict: `BLOCK_DAPP93_THIRTEENTH_MANAGER_INVENTORY_INTERPRETER_REALPATH_MISMATCH`

The manager materialized and hash-pinned the total invocation inventory as the first substantive lineage artifact. Its first required self-probe then failed closed before citation verification, candidate salvage, or any child dispatch.

The literal invocation used the cataloged path
`/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13`, but the
interpreter resolved its executable identity to
`/Users/ryan/.local/share/mise/installs/python/3.13.14/bin/python3.13`. The
inventory therefore did not pin the actual real absolute interpreter path as
the owner required. The controller returned exit 1 with
`UNFROZEN_MANAGER_INVOCATION` before running any phase logic.

This is not repaired in place. Amending the already frozen inventory or its
pinned controller would erase the evidence that the preflight was designed to
surface. The lineage stops before all historical reads, packet copies, packet
probes, freeze mechanics, verifier dispatch, and closeout command execution.

No historical root beyond the governance/preparation reads preceding the run
was read by the thirteenth controller. No candidate packet byte exists in this
run root. No packet was accepted, frozen, or executed.
