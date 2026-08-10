# Work-graph amendment v1.8 — final successor rejection recovery

Parent: `HELP_HUMAN`

Status: `ADOPTED — C1156/C1157 MECHANICAL CLOSURE ONLY`

HELP_HUMAN rejected successor freeze `MANAGER_FREEZE_R4_1.md` SHA-256
`5a23e4152cf53bf5d90b1e84eca2ab8200314b6d17344278c7f02da0d25daac9`.
It remains immutable rejected history and is not verifier or presentation
basis.

Two material defects remained: no enumerated producer for the required
step-1-through-30 CONTROL byte-range/hash index, and a C1155 path that could
emit `PASS_COMPLETE` for a preserved failure packet or without required LLDB /
ordinary-path files. Final recovery may add only contiguous C1156-C1157 and
update the already authorized affected packet/control surfaces.

C1156 must literally produce a returned byte-range index from the final
CONTROL transcript, prove exactly one ordered BEGIN/END pair for steps 01-30,
record exact byte offsets/count/SHA-256, and be independently rechecked by
C1155. C1157 must materialize exact returned-file screening results so C1154
and C1155 mechanically cross-check rather than assert screening.

`PASS_COMPLETE` must require PASS for executable step rows 1-30, exact
`READY_TO_HANDOFF` for row 31, required LLDB/CONTROL/form/range/screen/runtime/
build/manifest objects, all manifest identities, and exact range-index
verification. Every early, failure, STOP, DEVIATION, MISSING, or SKIPPED path
must yield `STOP_INCOMPLETE`.

No other command ID, design expansion, runtime, debugger, package, helper/GUI,
signal, credential, product, release, reliance, Git, Task Management,
foreign-loop, or verifier action is authorized or taken.
