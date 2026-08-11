# Ninth-lineage executable non-circular two-tier preflight

Status: `PASS — N1 RELEASED`

Native context telemetry was unavailable and is not inferred.

## Identity, intake, and fence gates

- baseline and Receipt 156: PASS;
- receipt validator: exit 0;
- fifth citation identities 8/8, third ledger, and allowed sixth/seventh/
  eighth template identities: PASS;
- read allowlist: 57/57 exact unique files exist;
- all eight historical roots excluded beyond exact authorized citations;
- declared F03 searches target one child-created file only; pre-dispatch
  allowlist/search-shape validation PASS;
- five F01 whole-file intake reads: exit 0 and complete;
- five F02 re-hashes: PASS;
- no rule exists only in inaccessible material.

Sealed intake identities:

| File | SHA-256 |
|---|---|
| capsule | `f6a8d4acc8166298dc286583476727017aa1ff95455a6367212b8b29e1878d80` |
| brief | `d687b4e3182857679c0f3ee3b74a896a5cd294a6d53b5ff4e4acd9bdd27a4d6c` |
| read allowlist | `ac362652db2434e0b6d0ad79bcce6174544c4157c128942f0ac6d8ce1d58aebc` |
| historical fence | `f84b6f027fee8f6f8eaead4ee35166340458a7e838e69c32793eb516d16ab155` |
| diagnostic catalog | `2d20bb90ae5e5ce982b9ea599681129ae97cba7760b1583bdfab78c616871c49` |

## Frozen tool and syntax gates

- F03 full-pattern scratch scan: exit 1, stdout 0: PASS;
- F04/F05: 54 bytes both: PASS;
- F06: 23/23 resolved absolute executables exist and are executable; catalog
  byte counts and SHA pins match: PASS;
- transitive chains: `shasum -> /usr/bin/perl` and
  `xcrun -> exact Xcode LLDB` close to pinned binaries: PASS;
- F07 BSD/zsh command syntax: exit 0;
- F08 exact `env -i`, `PATH=/nonexistent`, no-rc zsh: exact `SAFE_ENV_OK`,
  exit 0.

## Unified two-tier classification

F09 ran once from the ninth root in the exact restricted environment and the
script exited 0 after recording every command-level result.

- `AGENT_PROVEN`: printf, test, mkdir, sw_vers, uname, shasum/perl, security
  help, awk, date, xcrun/LLDB neutral version, tee, kill signal-zero, sleep,
  and rm probes all exit 0. Their operative state-changing forms remain
  eligible for precise `REVIEWED_NOT_EXECUTED` rows.
- `OWNER_PREFLIGHT`: `/bin/ps -p $$ -o pid=,ppid=,comm=` returned exit 127
  with exact sandbox evidence `operation not permitted: /bin/ps`.

The `/bin/ps` tier assignment satisfies all three owner criteria: the Mach-O
binary exists, is readable/executable, and matches absolute-path SHA-256
`a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c`;
the observed failure is an entitlement sandbox denial rather than missing
tool or syntax; and process-parent observation is directly necessary to prove
that the traced helper PID is the expected direct child. It therefore does
not block. N1 must place this exact form in packet Step 0 with expected owner
exit 0, exactly one row with three non-empty fields in PID/PPID/COMM shape,
pin confirmation, evidence record, and STOP-before-operation on mismatch.

No missing tool, syntax failure, ambiguous denial, or weak necessity is
sheltered by OWNER_PREFLIGHT. No operative packet act occurred.
