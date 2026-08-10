# D-APP-94 Option C R4 trap-entry validation

Status: `PASS_STATIC_PRE_FREEZE`

- verbatim R4 authority adoption SHA-256:
  `66a6ec9178494d98d0c0fb86ae0b2a24e5900d1802c73ba3d3a1fad476cf52cb`;
- immutable R3 driver SHA-256:
  `91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`;
- R4 driver SHA-256:
  `1d87db1d5f0d283a231c78dd8a84160844cc28f0467dfa324b7eb9053f233538`;
- `/bin/zsh -n prepared/run-dapp94-option-c-probe-r4.zsh`: PASS;
- exact R3-to-R4 unified diff replaces only
  `trap - EXIT INT TERM HUP` with `trap '' INT TERM HUP` followed immediately
  by `trap - EXIT`; no other driver line changes;
- EXIT-triggered entry ignores INT/TERM/HUP before evidence/state/call work;
  signal-triggered entry does the same before a further signal can interrupt;
- R3 restoration entry continues to ignore signals before `IN_PROGRESS`; the
  unchanged state machine admits one restoration only, publishes terminal
  success/failure before re-arming signals, prevents EXIT retry, and retains
  all state on failure;
- static gates: R3 hash stable; fixed temp root absent; return destination
  absent; literal owner restoration target present.

No candidate command, security/keychain command, Electron launch, process
action, runtime, GUI, product, package, trace, credential, network, Git, Task
Management, foreign-loop, or other execution action occurred.
