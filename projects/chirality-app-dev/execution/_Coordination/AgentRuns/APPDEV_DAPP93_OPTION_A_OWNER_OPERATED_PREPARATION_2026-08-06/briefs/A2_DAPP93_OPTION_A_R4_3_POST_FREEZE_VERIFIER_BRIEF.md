# Sealed brief — D-APP-93 R4.3 post-freeze verifier

Instance type: genuinely fresh ephemeral Agent 2 generalist, read-only audit

Parent: WORKING_ITEMS

Objective: independently audit the frozen D-APP-93 Option A owner-operated
packet repair and emit exactly one evidence-first verdict return.

## Frozen scope

Repository root:
`/Users/ryan/.codex/worktrees/7388/chirality`

Run root:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06`

Accepted current freeze:

- `MANAGER_FREEZE_R4_3.md`
- SHA-256 `7f4a9858f8ba2947ce1db522f82669678369b0a4ac3f09a20a5c66bc7747ddf1`

Frozen prepared identities:

| Object | Required SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` |
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `254fb53f09fed4d58b602b011ca6fcb9aad371cf39528bd70c9449db59ecdf9c` |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `970ad67370f12e9c1a5ef865da09bfe402b87495f5d1dcd1258df7f770d011dd` |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `cef1cf5a14ddfa6486aadddfe629c763e775514d59aeddd57ee564d90316b44a` |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `a41d945a362bef91c79618ee1f5cc689236d7264cc3045533ee1291c4101c8ee` |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `800325abfb000c221f4f2177158778058903c8c233bd99378ce8751d4f715a10` |
| `prepared/PREPARED_PACKET_INDEX.md` | `88d6396293a77e9e4e6a2968b33845cb1095ff1c2d0ce701913c9822e8e72bac` |

Frozen control identities:

| Object | Required SHA-256 |
|---|---|
| `MANAGER_FREEZE_R3.md` | `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963` |
| `reviews/A2_DAPP93_OPTION_A_R3_VERIFIER_ONLY_RETURN.md` | `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006` |
| `R4_PACKET_REPAIR_AUTHORITY_ADOPTION.md` | `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e` |
| `WORK_GRAPH_AMENDMENT_V1_5.md` | `e2bbe7d5b38ea14f24e068e25b22226d104ee285dcd3505ed0590575626381d5` |
| `WORK_GRAPH_AMENDMENT_V1_6.md` | `ab80a6b27d22ca788833643777399b41291a8bff9179e551b3f3665b89a52809` |
| `WORK_GRAPH_AMENDMENT_V1_7.md` | `5415ab986aab9acb16fb365b7e49a51eb828ad8238dee94086c139627a9d772d` |
| `WORK_GRAPH_AMENDMENT_V1_8.md` | `fb5a04f5b5ba45c6bfe9a3b9e6a5e0c3e46e0ea7846f68a014fa5976c0ff07eb` |
| `WORK_GRAPH_AMENDMENT_V1_9.md` | `8b2196042a09716ea4e0b23e5eff22ea83543964bf15b5303002faac86897c1d` |
| `C1155_ORDINARY_PATH_PRODUCER_TRACE.md` | `e3a0a1ecebf9c9f71f5a94315233fa5e0f0420109c1d9272a6d30c4e1531b24e` |
| `R4_PACKET_REPAIR_BACKCHECK_R4.md` | `a1c38706436389a47409071244802a40674cae5314c94d684a94a2526a9af0ea` |
| `execution/_Evaluation/DAPP93_R4_MECHANICAL_AUDIT_2026-08-07/EVALUATION_REPORT.md` from project root | `9b4992a285e18040e2ef9ae2d6af4d34fabdb392277d606a587f82efe8d4f2a5` |
| `execution/_Evaluation/DAPP93_R4_MECHANICAL_AUDIT_2026-08-07/HANDOFF_STATE.md` from project root | `0b5607afa53151a1f730a3c53a899fa85d321270e820bf97d81435656c2849ff` |

The rejected freezes with SHAs beginning `b741231b`, `5a23e415`, and
`ea2dd68f` are immutable history, not current packet authority.

## Permissions and prohibitions

Read only the repository files needed for this audit. Use only read-only,
non-effecting static inspection such as `shasum`, `rg`, `sed`, `awk`, `wc`,
`cmp`, `diff`, `test`, and syntax parsing that does not execute packet bytes.

The sole authorized write is creation of exactly this file:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_OPTION_A_OWNER_OPERATED_PREPARATION_2026-08-06/reviews/A2_DAPP93_OPTION_A_R4_3_POST_FREEZE_VERIFIER_RETURN.md`

Do not modify, delete, rename, normalize, or regenerate any existing byte. Do
not delegate. Do not execute or simulate any proposed packet command. No
runtime, debugger, package, helper, GUI, signal, credential, product, release,
reliance, Git, Task Management, foreign-loop, network, or other action.

## Mandatory audit sequence

1. Before substantive review, independently reproduce the R4.3 freeze hash
   and every prepared/control identity above. Any mismatch is a blocking
   finding; continue static review where safe and report it.
2. Read the exact owner authority, accepted EVALUATION report/handoff, frozen
   packet, recovery amendments, trace, backcheck, R3 freeze, and R3 verifier
   BLOCK. Do not accept manager conclusions without checking live bytes.
3. Re-run every branch/precondition matrix row A01-A44 individually. The
   return must contain an explicit A01 through A44 result, including the
   A34a/A34b/A34c subcases from the accepted evaluation. Check phase-specific
   early stops, valid rollback prerequisites, occupied/no-safe-destination
   paths, terminal failures, cleanup retention, and that no command is invoked
   where its stated precondition cannot hold.
4. Re-run every evidence matrix row B01-B40 individually. The return must
   contain an explicit B01 through B40 result. Check every required byte/object
   against an exact producer/capture and exact return/inclusion action; no
   orphan requirement is allowed.
5. Independently verify all of these mechanical facts:
   - exactly 93 unique ledger rows: C196, C197, and contiguous C1067-C1157;
     no duplicate, gap, hidden operation, or out-of-range command;
   - the approval request/token, command range, runbook, evidence packet,
     ingestion contract, index, and freeze agree exactly;
   - all eight index members reproduce and the index identity reproduces;
   - every operation introduced for repair has exact literal bytes/operator
     input and honest prerequisites;
   - C196/C197 bytes and semantics are preserved from R3;
   - ordinary order is exactly C1145→C1144→C1130, while pre-C196/pre-C197
     routes invoke neither C1144 nor C1130;
   - C1105-C1108 preserve complete combined output plus actual command and tee
     exits even when the underlying command fails, without rerun;
   - 31 runbook steps and 31 literal disposition rows exist, with step 31 an
     honest terminal handoff disposition rather than a cyclic CONTROL range;
   - C1156 has exact, unambiguous ordered byte-range/SHA-256 semantics for
     steps 01-30, rejects duplicate/missing/out-of-order markers, and its
     range index is returned/screened/manifested/rechecked;
   - C1148 source screening and C1157 final returned-file screening produce
     exact result records that C1154/C1155 mechanically consume;
   - C1154 includes every required ordinary-path returned object and exact
     per-file identities without self-reference;
   - C1155 emits `PASS_COMPLETE` only for the full ordinary path with step 31
     `READY_TO_HANDOFF`, no STOP/DEVIATION/MISSING/SKIPPED required evidence,
     LLDB present, all required objects present, screens passing, range index
     verified, and manifest identities exact; every honest early/failure path
     deterministically emits `STOP_INCOMPLETE`;
   - independently trace every C1155 required member to its producer and its
     one ordinary-path direct return or C1130 copy. Require exactly 21/21 and
     specifically prove C1148 → C1130 source fifteen → returned
     `SOURCE_SCREEN_RESULTS.txt` → C1157/C1154/C1155;
   - credential-neutrality, causal `UNKNOWN` calibration, no acceptance or
     release/reliance claim, future-only authority, and no-effect boundaries
     remain explicit and coherent;
   - no trailing whitespace or stale current-freeze ambiguity exists in the
     current frozen/control-successor surfaces.
6. Immediately before writing the verdict, reproduce the R4.3 freeze and all
   bound prepared/control hashes again and report the final reproduction.

## Return contract

Write exactly one Markdown return at the sole path. It must include:

- instance statement confirming fresh/no delegation/read-only conduct;
- first and final identity tables with every bound object, observed SHA, and
  PASS/BLOCK;
- evidence-first findings ordered by severity and pinpointing file/row;
- an explicit A01-A44 table, preserving A34a-c;
- an explicit B01-B40 table;
- mechanical results for every item in step 5, including the independently
  derived 21/21 producer/copy table;
- an authority/effect-boundary result;
- exactly one terminal verdict token:
  `PASS_FOR_DAPP93_OPTION_A_OWNER_PACKET_PRESENTATION` or
  `BLOCK_PACKET_REPAIR_REQUIRED`.

If any required check cannot be completed, return
`BLOCK_PACKET_REPAIR_REQUIRED` with exact gaps. Do not repair and do not ask
for or dispatch a second verifier.
