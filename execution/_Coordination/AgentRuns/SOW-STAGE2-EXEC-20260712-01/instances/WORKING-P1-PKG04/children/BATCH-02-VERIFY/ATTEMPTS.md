# Verifier Attempts

## Attempt 1 — complete preterminal run

The first complete run passed every member checkpoint and reproduced the three
accepted candidate hashes, 33 mappings, 276 source lines, and seven negative
probes. Its inherited aggregate constants still reported five completed
members and 35 probes. The complete evidence is retained under
`attempts/preterminal-aggregate-binding/`.

Classification: `VERIFIER_HARNESS_BINDING`; reason code:
`BATCH_AGGREGATE_CONSTANTS`. This was not a source, candidate, semantic, tool,
or member-check discrepancy. No candidate or project file was written.

## Attempt 2 — expected fail-closed rerun

After mechanically narrowing the aggregate counters to `len(EXPECTED)`, the
accepted harness refused to overwrite the existing member evidence directory
with `FileExistsError`. The error is retained at
`attempts/rerun-fileexists/ERROR.txt`.

## Remediation and attempt 3

The complete prior evidence was moved intact to the retained-attempt folder,
leaving a fresh active member target. Attempt 3 then completed the single
member and all required checkpoints with exact aggregate counters and no
member failure, repair, retry, candidate change, or project write.

## Terminal audit path correction

The first read-only terminal audit referenced shorthand reproduction paths
that are not used by this harness and failed before mutation. The exact error
and corrected path binding are retained at
`attempts/terminal-audit-path-correction/ERROR.txt`.

## Closeout manifest rebind

Manager fan-in sampled `ATTEMPTS.md` after its final narrative edit but before
the corresponding manifest freeze and correctly reported the stale 1,215-byte
binding. The self-excluding manifest was rebuilt after all narrative edits and
then verified row-for-row for exact hash, byte count, membership, and zero
warnings. This was closeout ordering only; no semantic or candidate issue was
present.
