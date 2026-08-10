# D-APP-93 R4.4.5 intake validation and terminal verdict

Verdict: `STOP_INCOMPLETE`

## Accepted basis and identity checks

| Check | Result |
|---|---|
| R4.4.5 freeze | PASS — `ddfbf431772526df6f884474c0dad84d57ce7c7aacede73ec72c4ed5751670c4` |
| sole predecessor verifier | PASS identity — `fffd3c4f56162e3624dfca5ad012c4af4af209dbd349271a82bd344c9d7268bb` |
| ruling | reproduced — `513c4f64c8ec5049a11788e3bacb898a7be52c273bcd09a120a6fa1cecb483fe` |
| owner token | reproduced — `72d8091dc57b2eaab36d646cd5599648ea1a1bddb6c2e57a600a359c40cf0857` |
| command ledger/runbook/LLDB script | reproduced — `4989ac38...49fa5` / `6f825681...e5ac` / `720ad198...f8` |
| 12 candidate sources + lock | PASS — C1091 values equal the reconstruction manifest, including lock `5c8fce2a...1a56` |
| seven baselines | PASS — C1078 values match the frozen baseline inputs |
| local Electron archive | PASS — C1101 `ad4a0ae3...fe28` |
| failed-run overlay/configs | PASS as executed-input identity only — overlay `ba5142bf...208b`; configs `08224149...83af` and `01e93e41...89ea` |
| rollback | PASS — C1140 reproduces the seven baseline hashes plus the lock exactly; C1141 is empty; frontend is clean |

## Contract checks

- Returned receipt is exact: 28 files, comprising 14 selected-branch
  primaries and 14 adjacent sidecars; there are no extras. Every sidecar
  reproduces its complete primary.
- CONTROL is 40,008 bytes with fifteen ordered unique raw records: steps
  1-10, 23, 25, and 28-30. Every record is zero; C1146.30 is last. Missing
  step numbers are route-inapplicable `NOT_RUN`, not missing/unclosed ranges.
- C1105, C1106, and C1107 are exactly `0/0`; C1108 is exactly `1/0` and its
  complete output records the stale D-APP-92 electronDist error. Therefore
  step 10 is FAIL even though the immediate C1146.10 print itself exited zero.
- The selected `Post-first-write/pre-C196` route is satisfied: C1147;
  ruled C1150.R-before-C1148; C1149.07-.17; C1151.T/C1153.01; no C1128/1129;
  C1131-C1141 rollback; C1142/C1143; terminal C1146.30; C1151.F; then C1152,
  C1154.03 first, remaining applicable hashes, and intake receipt. C1144,
  C1130, C196, C197, LLDB, launch, signal, retry, and alternate target are absent.
- The precleanup primary is byte-identical to its returned result. The complete
  transcript adds only the lawful later cleanup/cut content. C1141 has zero
  bytes; temp root absence and frontend cleanliness are proven.
- No attach-to-detach timing, five breakpoint blocks, first signal,
  direct-child binding, package topology, or runtime process evidence exists;
  these checks are `NOT_RUN`, not narratively repaired.
- Exact UTC/monotonic per-step ordering is unavailable. Available anchors are
  the login banner, C1105 test time, and owner attestation; all finer timing
  remains unknown. Structural byte order proves the required command order.

## Terminal ruling

`PASS_COMPLETE` is prohibited because C1108 has nonzero `command_exit`, step
10 derives FAIL, and the ordinary post-C196 evidence set was never produced.
The exhaustive matrix therefore requires `STOP_INCOMPLETE`. D-APP-88,
DEL-09-04, TM-APP-036, product, remedy, release, and reliance remain unchanged.
This accepted derivative intake unlocks only the already-held bounded
D-APP-93 preparation repair; it supplies no execution or verifier authority.
