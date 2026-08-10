# D-APP-94 Option C R3 signal-continuity validation

Status: `PASS_STATIC_PRE_FREEZE`

- verbatim R3 authority adoption SHA-256:
  `24e7c061dd2952e25f578864ad79326afb118b10e28467f7c6ec21063970fabe`;
- immutable R2 driver SHA-256:
  `42d4206281afc0939f41c1bb03082162e4f3d978be8013e2edb37bb899f6a835`;
- R3 driver SHA-256:
  `91396b2549a4c93910864c513467dd79dc73d197659fe6299137d634e7134a3f`;
- `/bin/zsh -n prepared/run-dapp94-option-c-probe-r3.zsh`: PASS;
- exact R2-to-R3 unified diff contains one adjacent-line reordering only:
  `trap '' INT TERM HUP` moves immediately before
  `RESTORE_STATE=IN_PROGRESS`; no line is added, removed, or otherwise changed;
- signal continuity: after state validation, ignore dispositions are installed
  before `IN_PROGRESS` is published and before the first restoration command;
  unchanged terminal publication occurs before normal signal traps are
  re-armed;
- single restoration: unchanged state validation admits only `NOT_STARTED`;
  `IN_PROGRESS`/`FAILED` reject and `SUCCEEDED` returns without commands;
- failure: unchanged `FAILED` publication prevents EXIT retry and retains all
  isolated state; success: unchanged `RESTORED=1`/`SUCCEEDED` publication
  precedes evidence copy and cleanup;
- static gates at validation: R2 hash stable; fixed temp root absent; return
  destination absent; literal owner restoration target present.

No candidate command, security/keychain command, Electron launch, process
action, runtime, GUI, product, package, trace, credential, network, Git, Task
Management, foreign-loop, or other execution action occurred.
