# D-APP-93 R4.4.5 host-path fresh verifier return

Verdict: `PASS`

Instance statement: I was the sole genuinely fresh read-only ephemeral Agent 2
verifier for this gate. I did not delegate, repair, execute or simulate any
packet/runtime/debugger/package/helper/GUI/signal/product operation, use Git or
Task Management, or inspect the owner-retained CONTROL bytes. This file is my
sole write.

## Freeze and identity audit

The sealed brief reproduced SHA-256
`6bcf52b82bc5bc7a533c8dfdde3365f13fe23b29cc2b6b27b2b33956c2c152b9`.
The accepted R4.4.5 freeze reproduced before inspection and after the complete
read-only audit at
`ddfbf431772526df6f884474c0dad84d57ce7c7aacede73ec72c4ed5751670c4`.

Every bound same-run identity reproduced exactly:

- step-1 stop / authority adoption
  `4352747755ae49e8189685874d77ca8e62f94324c37fdd875d7424956ff5063d`;
- work graph v1.14
  `f5ab40b4067ce19f0312d820595cd0b2f9f1cc34595d7788bbbb9592cea439b5`;
- host executable audit
  `69ecdb7a9342803a67e5dc25c663f2ea48127580064f4562289c5f3ed4f26d2a`;
- repair backcheck
  `11fa200f6e30674ba02d113e96b8a395ad8fc577ed16652297a713002e9acea8`;
- manifest `4ea7a6340e2a24727af496c830ffd4e38b3b619e1c0c58cd06897a908a13b874`,
  LLDB script `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`,
  and static revalidation
  `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459`;
- repaired ledger `4989ac38d2f6e4b9bc353fdbf842a2db98c9163914f6c79f93751fd581649fa5`,
  runbook `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`,
  evidence form `4457d1185a45cf112cc1e137e5def73166f0fc4554d4c40da94217d3eab692cc`,
  and ingestion contract
  `dc3c5c7b8fbb2edb61c0046cc82934c8b64c18ba820bac70fb188e57d6ecdad7`;
- repaired owner token
  `72d8091dc57b2eaab36d646cd5599648ea1a1bddb6c2e57a600a359c40cf0857`
  and packet index
  `ca85dae738b44e2d59ff86b2b67314d99162850496c45937d795145ce76aebea`;
- command inventory
  `f3ee970eefeea900527ec83a12e395343678c283f2adbfa10ccce12d0ec524bc`,
  branch/raw matrix
  `fef3fc1ca92797389108ad0d1267ea0b040de80ac8f3a5098a3708f2c7c21531`,
  validation `b9b00c1c152602b5789989e8de0455bc43bced55c527998e92f2552b3fff4a52`,
  manager return
  `0c572c69dd50689d8249d9e80fe5dc728951658fd3d16c43fb54f6d270dc9d30`,
  and handoff `f4819b5c783c5c4ed273e8df9815c91edc52b66ff0af0d04377674d3a26fb9c3`.

The accepted predecessor basis also reproduced: R4.4.4 freeze
`4f655120a009bb27167c7d4334aaf46755626b8c0b3a03e688905e62ec8d6954`,
sole verifier PASS
`74dfb4a813115fe22f19535e8561b5e8fe646b6244732d5622997620408e952c`,
owner token `3e907635a53cca4c6c5539252dbf9186ac976fd886384fd9c7aa75132914b9a0`,
exact-token adoption
`541a7c4bafe64e2a6a6ccd3b2716cc8d79569f7b4f5fd8ab45aae1fe24a58e66`,
ready handoff `ed17051d51ba68dd6a80ef29b8dfd7138e5a69d189a934b7a4980455c3c55c92`,
and `LOOP_RECEIPTS.md` through Receipt 142
`5f389b638f195f4be8fbe782bd15a2d53a2daec76db03635acc3991ea3549c2a`.

## Independent ledger and host-path audit

- The ledger contains exactly 93 unique primary rows: C196, C197, and the
  complete contiguous C1067-C1157 range, with no duplicate or missing ID.
- It contains exactly 87 independently enumerated subinputs: 17 C1130, 30
  C1146, 17 C1149, one C1150.R, one C1153.01, three C1154, six C1155, eight
  C1156, and four C1157 inputs. Their ordered, code-fence-stripped,
  LF-delimited digest is
  `6bf71985b45520231c7a7405728280c196af2cb504ddd5b7cb9d9242fb28e683`.
- The exact newline-terminated C196 and C197 row hashes are respectively
  `9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb`
  and `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52`;
  their state remains `OWNER_APPROVED — VALID — UNUSED`.
- Independent executable-position classification covered command starts,
  shell separators and pipelines, `exec`, `find -exec`, and the payload after
  `/usr/bin/env -i` assignments across all 180 cells/subinputs. PATH entries,
  placeholders, shell builtins, arguments, data sources, and redirection
  destinations were excluded.
- The resulting 24 unique host tools are the mise Node and npm executables;
  `/bin/cp`, `/bin/kill`, `/bin/ln`, `/bin/ls`, `/bin/mkdir`, `/bin/ps`,
  `/bin/rm`, `/bin/sleep`, `/bin/test`, `/bin/zsh`; and `/usr/bin/diff`,
  `/usr/bin/ditto`, `/usr/bin/env`, `/usr/bin/find`, `/usr/bin/git`,
  `/usr/bin/plutil`, `/usr/bin/printf`, `/usr/bin/readlink`,
  `/usr/bin/shasum`, `/usr/bin/stat`, `/usr/bin/tee`, `/usr/bin/xcrun`.
  Every one is currently both a regular file and executable: 24/24 PASS,
  missing count zero.
- The two absolute application executable paths in C1114/C1117 are correctly
  phase-classified as C1108-generated outputs, not installed host tools. Both
  are absent before packaging, as required.

## Exact authorized-delta proof

The repaired ledger contains exactly 34 `/usr/bin/printf` strings: one in
each C1105-C1108 primary operation cell and one in each C1146.01-C1146.30
subinput. No other occurrence exists and there is zero standalone
`/bin/printf`. In-memory reverse normalization of all 34 strings reproduces
the predecessor ledger byte-for-byte at
`34cdde1a1c6ee9660e7b15e20b7112b7306fc94b26758404acdc30d497da6aa6`.
This proves that no other ledger byte changed.

The unaffected manifest, LLDB script/static review, runbook, evidence form,
ingestion contract, and branch/raw matrix retain the exact predecessor hashes.
Only the ledger and its mechanically affected inventory, owner token, packet
index, successor freeze, audit/backcheck, and same-run control records have
successor identities. Inspection of each affected record binds only the
authorized host-path substitution and its mechanically necessary references;
no other command or packet semantic change is present.

## Packet invariants and stopped-attempt facts

The owner authority is exact and bounded. Its accepted durable record states
that C1146.01 was the sole attempted literal and failed only because
`/bin/printf` is absent; C1067 was never entered; no C1067-C1157 operation,
C196, or C197 ran; and the short CONTROL bytes remain with the owner outside
this verifier's scope. The successor controls neither imply nor claim later
operational state.

The packet retains all prior invariants: hash-bound reconstruction inputs;
ordinary C1145→C1144→C1130 order; C1146.30 as the terminal CONTROL input;
pre-cut C1150.R and applicable C1153.01 source-lifetime preservation; C1151.F
as the non-input through-cut export; C1152 as post-cut observation/crosscheck;
C1154.03 first form-freeze hash and C1154-C1157 as the finite post-cut tail;
phase-valid route prerequisites and retained-state failure routes; 21 ordinary
primary raw objects plus 21 adjacent untouched SHA-256 stdout sidecars; and
complete C1105-C1108 combined output plus immediate two-record
command/tee-exit sidecars with enforcement reserved to later ingestion.
Neither the runbook nor returned form derives a manifest, ranges, hash
comparisons, completeness, PASS disposition, or terminal verdict.

The exact fixed root
`/private/tmp/chirality-dapp93-owner-operated-20260807`, the same-run
`returned` directory, `frontend/node_modules`, `dist`,
`dist-runtime-helper`, `dist-electron`, `dist-runtime`, and `.next` are all
absent. Thus no fixed-root state, returned evidence directory, frontend
dependency/build/package derivative, or generated application executable is
present.

No execution authority issued and no prohibited operational action occurred
during this audit.

`PASS_PACKET_HOST_PATH_REPAIR`
