# D-APP-93 R4.4.6 cleanup-observation addendum fresh-verifier return

Verdict: `PASS`

Instance statement: I was the sole genuinely fresh read-only ephemeral Agent 2
verifier for this gate. I did not delegate, repair, inspect live process or
runtime state, execute or simulate any operational command, signal, rollback,
cleanup, product, credential, Git, Task Management, or foreign-loop action.
This file is my sole write.

## Sealed scope and authority

The sealed brief reproduced at
`8694571a2822d47e6b6d59fee268d16a70586516562a11ccdf9fb21e38f573c0`.
The authority adoption reproduces the owner's instruction verbatim and limits
this tranche to preparation, hashing, freezing, and one read-only verifier.
It grants this verifier no operational authority. The addendum token is exact,
withheld pending this PASS, owner-personal, current-attempt-only, and states
that partial, paraphrased, or changed text grants no authority.

## Static audit evidence

- Delayed C1117 closure begins with the byte-exact frozen second C1117 input:
  `gui_pid=$!; printf '%s\n' "$gui_pid" > /private/tmp/chirality-dapp93-owner-operated-20260807/evidence/gui.pid`.
  It is immediately followed by unchanged C1146.15:
  `d93_rc=$?; /usr/bin/printf 'DAPP93-CONTROL|STEP-15|command_exit=%d\\n' "$d93_rc"`.
  The addendum requires step 15 `DEVIATION`, step 16 `NOT_RUN`, prohibits
  C1146.16, and authorizes none of C1146.16-.22 or C1146.24.
- `$!` provenance is explicitly limited to the attested unchanged CONTROL
  shell with no intervening CONTROL input or background launch. A1117.ID then
  fails closed unless exactly one row matches the captured decimal PID,
  `gui.pid`, unchanged CONTROL-shell PPID, and the exact frozen C1117 GUI
  executable and arguments.
- Exactly four distinct read-only exact-PID observations are enumerated:
  A1117.ID, A1128.PRE, A1129.H, and A1129.G. Each is the literal
  `/bin/ps -o pid=,ppid=,command= -p ...` form over its frozen PID only. No
  name search, alternate PID, C1119 reuse, or C1125 reuse is authorized.
- A1128.PRE is immediately adjacent to unchanged C1128
  `/bin/kill -TERM "$gui_pid"`; A1129.H is immediately adjacent to unchanged
  helper C1129 `/bin/kill -KILL "$helper_pid"`; and, only when applicable,
  A1129.G is immediately adjacent to unchanged GUI C1129
  `/bin/kill -KILL "$gui_pid"`. Any nonzero, absent, extra, stale, or
  mismatching observation prohibits its signal and selects the existing
  cleanup-failure retention route without retry.
- The complete future order preserves the pre-C196 return path and source
  lifetimes: C1147.01-.02 and immediate C1146.23; direct blank-form return,
  C1151.T, form-recorded C1148 inspection, applicable C1149.01-.17 in order,
  immediate C1146.25, and C1153.01 while its source remains live. Cleanup is
  then observation-adjacent and followed by immediate C1146.26/C1146.27;
  mandatory C1131-C1139 rollback and C1146.28; C1140-C1141 and C1146.29;
  prerequisite-gated C1142-C1143 and terminal C1146.30; C1151.F with no
  further CONTROL input; then outside CONTROL C1152, C1154.03 first,
  C1154.02, applicable C1155-C1157. C1154.01 remains `NOT_RUN` because
  C196/C197 and an LLDB transcript did not occur.
- C1118-C1127, C196/C197, C1130, C1144, causal signaling, retries, PID search,
  alternate targets, and authority expansion are expressly prohibited. Every
  occupied/prohibited/copy/identity/signal/rollback/cleanup/hash failure
  retains state and follows the frozen fail-closed route.

## Initial and final freeze reproduction

Initial and final pre-return identities were identical:

| Object | SHA-256 |
|---|---|
| addendum freeze | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |
| authority adoption | `f2f441ae79fc8fe7646a61e77d24f9aa889af0796eba30aac8e385b237e548da` |
| cleanup-observation addendum | `d109cfdc489f5ce679a696d8def4a599f90d8700c63891991778f6c605da7e33` |
| addendum execution token | `8e6dff6b587b37cfbab4b23f1e29ecbe01bb7c301b432c796cfa3cec80118fc8` |
| addendum backcheck | `5558604c069afd42c6b4ad0f58cae9404a0366620de3d07be049c6ee42bc4986` |
| unchanged R4.4.6 freeze | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| unchanged R4.4.6 verifier PASS | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` |
| unchanged command ledger | `1630f2c569f8aad3a91109ff70e5ca4cac597b619e47dbdd35b282dd94474824` |
| unchanged runbook | `9fda14d73d3eca1a0b055ea727853ecec11e824d8cc17fd57161a4ab9f2193d8` |
| unchanged prepared owner token | `b3f917f7c1b0fe7d4a1a99a00e5371a86fb049ff7417d63acc009e7ca2023b4b` |

Stability: `PASS — NO FREEZE DRIFT`.

`PASS_R4_4_6_CLEANUP_OBSERVATION_ADDENDUM_FREEZE`
