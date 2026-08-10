# D-APP-94 Option C R2 restoration-guard validation

Status: `PASS_STATIC_PRE_FREEZE`

- authority adoption SHA-256:
  `6452e0e29e27915ad73e25572c3767491c79ae656450d981fcdc4331269428ab`;
- predecessor driver preserved at SHA-256
  `35ceb467a30bd3736c15958b3f99203a385b5f2e8a153c80478d3663dbd481f0`;
- R2 driver SHA-256:
  `42d4206281afc0939f41c1bb03082162e4f3d978be8013e2edb37bb899f6a835`;
- `/bin/zsh -n prepared/run-dapp94-option-c-probe-r2.zsh`: PASS;
- common preamble through `MUTATED=0` digest, predecessor and R2:
  `65b00c309d0542b8214c28c5461c008dc3479284f3ec954e3ea12e655b581e90`;
- complete script from `fail_before_mutation()` through EOF digest,
  predecessor and R2:
  `a7d6071208a765a63e66dbfd4de4c196dba0bd8b1732a89b2f232e68899d4e5a`;
- ordered restoration security/cmp/write-status command digest, predecessor and
  R2:
  `1be58214f86fce0cdcf2fd78cb9b9b74f99ef51d94d0e8fea0eaf5f0be9e57a3`;
- authorized delta only: replace `RESTORING` boolean with terminal
  `RESTORE_STATE`; add the normal signal-trap arming helper; gate restoration
  entry by state; ignore INT/TERM/HUP during the active restoration; publish
  `SUCCEEDED`/`FAILED` before re-arming normal signal behavior; gate the
  fail-closed trap to `NOT_STARTED`;
- restoration success publishes `RESTORED=1` before any cleanup; restoration
  failure publishes `FAILED`, exits while retaining all state, and cannot be
  retried by EXIT; no signal can terminate the shell or restoration children
  during the active restoration;
- fixed temp root absent, return destination absent, and literal restoration
  target present at static freeze observation.

No packet command, security/keychain command, Electron launch, process action,
runtime, GUI, product, package, trace, credential, network, Git, Task
Management, foreign-loop, or other execution action occurred.
