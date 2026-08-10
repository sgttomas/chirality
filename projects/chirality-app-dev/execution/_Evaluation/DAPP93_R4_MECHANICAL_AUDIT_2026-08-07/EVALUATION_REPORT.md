# D-APP-93 R4 mechanical audit — evaluation report

Verdict: `REPAIR_REQUIRED`

Evaluation type: strictly read-only pre-repair mechanical audit; this is not the post-freeze verifier.

## 1. Frozen basis, scope, and decision rule

The accepted basis reproduced at entry:

| Object | Required SHA-256 | Reproduced SHA-256 | Result |
|---|---|---|---|
| `MANAGER_FREEZE_R3.md` | `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963` | same | MATCH |
| `reviews/A2_DAPP93_OPTION_A_R3_VERIFIER_ONLY_RETURN.md` | `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006` | same | MATCH |
| `R4_PACKET_REPAIR_AUTHORITY_ADOPTION.md` | `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e` | same | MATCH |

All nine `prepared/` identities bound at `MANAGER_FREEZE_R3.md:8-18` also reproduced exactly:

| Prepared object | SHA-256 |
|---|---|
| `PACKAGE_RECONSTRUCTION_MANIFEST.md` | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` |
| `lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `COMMAND_AUTHORITY_LEDGER.md` | `234c7f0ebb4863f834433059e6cb3dd913123c44f1f89026d27ab56639ab1533` |
| `OWNER_OPERATED_RUNBOOK.md` | `65b1c53e4ef7232ad381a6cb25a184d871741ecadf4a92bac3291d378d5907f8` |
| `EVIDENCE_RETURN_PACKET.md` | `e07b673d62d2fbe55f9d28d723b846e65be53255e1e7ee9acb1a78c62b703399` |
| `INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `65ca74577adce82b412f722bbaca20aed402b5590c6a48f01c1605cd05d60cfe` |
| `FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `3c7641058f5032e91d2bdb2313319b148084f5ac85716c9e9d32c27d376a417f` |
| `PREPARED_PACKET_INDEX.md` | `070ac6163588abff012c56bcdafd3b2e6bfdeb515924b4925161c54f47915a7d` |

Decision rule: flag only (A) a command invoked on a branch where its stated prerequisite cannot hold, or (B) a declared required evidence byte/object with no enumerated capture or return/inclusion action. Dynamic runtime results remain `UNKNOWN`; their nonexistence before execution is not a defect. Static command/evidence plumbing is auditable now.

Coverage: 31/31 numbered steps, 15/15 distinct branch/terminal-path classes, all 81 unique ledger rows (C196, C197, C1067-C1145), and 40 grouped evidence requirements covering every declaration in the prepared packet.

## 2. Matrix A — runbook step / branch / command / prerequisite

`YES` means the stated prerequisite can hold on that path; it does not predict runtime success. `NO` is an authorized class-A defect. `N/A` means no ledger command is invoked.

| Row | Step/path | Invoked IDs | Stated prerequisites at invocation | Can hold? | Evidence / disposition |
|---|---|---|---|---|---|
| A01 | Step 1, open session | none | returned owner token globally; one login session; CONTROL/LLDB tabs | N/A | Runbook `:30-32`; setup actions have no C-ID, an evidence issue addressed in Matrix B only. |
| A02 | Step 2, preflight | C1067-C1069 | fixed temp root, `node_modules`, and all named derivatives absent | YES | Ledger `:17-19`; runbook `:33-34`. Any mismatch stops before mutation. |
| A03 | Step 3, roots | C1070 | A02 passed; named parent absent | YES | Ledger `:20`; runbook `:35-36`. |
| A04 | Step 4, baseline | C1071-C1078 | C1070 tree exists; seven source bytes exist; C1078 matches D-APP-89 | YES | Ledger `:21-28`; runbook `:37-38`. |
| A05 | Step 5, reconstruction | C1079-C1091 | A04 complete; 12 sources and lock exist; destinations writable; C1091 matches manifest | YES on forward path | Ledger `:29-41`; runbook `:39-41`. Failure branch is A32. |
| A06 | Step 6, dependencies | C1092-C1099 | C1091 passed; local exact-lock tree exists; copied six entries exist before removal; local Root targets exist | YES | Ledger `:42-49`; runbook `:42-44`. |
| A07 | Step 7, archive | C1100-C1101 | local archive exists; evidence tree exists; hash matches declared value | YES | Ledger `:50-51`; runbook `:45-46`. |
| A08 | Step 8, overlay | C1102-C1104 | frontend candidate/config bytes and script exist; archive bound; exact cwd; two hashes/one match per file | YES | Ledger `:52-54`; runbook `:47-49`. |
| A09 | Step 9, checks | C1105-C1107 | overlay passed; dependency projection exists; each predecessor passed | YES | Ledger `:55-57`; runbook `:50-51`. Output preservation is B14-B16. |
| A10 | Step 10, package | C1108 | C1105-C1107 passed; exact offline environment; single invocation; no network indicator | YES | Ledger `:58`; runbook `:52-53`. Output preservation is B17. |
| A11 | Step 11, package identity | C1109-C1113 | package completed and named package paths exist | YES | Ledger `:59-63`; runbook `:54-58`. |
| A12 | Step 12, helper launch | C1114 | exact helper package exists; run-owned HOME/user/evidence exist; CONTROL shell owns `$!` | YES | Ledger `:64`; runbook `:59-60`. |
| A13 | Step 13, helper identity | C1115 | C1114 assigned `helper_pid`; child still exists; PID equals record | YES | Ledger `:65`; runbook `:61-63`. |
| A14 | Step 14, initial ownership | C1116 | exact runtime paths created by launched helper | YES (dynamic) | Ledger `:66`; runbook `:64-65`. Missing paths cause stop, not prerequisite contradiction. |
| A15 | Step 15, GUI launch | C1117 | package and run-owned HOME/user/evidence exist; CONTROL shell owns `$!` | YES | Ledger `:67`; runbook `:66-67`. |
| A16 | Step 16, coexistence | C1118 | visible GUI exists; bounded action is available; no credential/prompt | YES (dynamic) | Ledger `:68`; runbook `:68-70`. |
| A17 | Step 17, revalidate | C1119 | both exact PIDs captured; helper identity still equals C1115 | YES (dynamic) | Ledger `:69`; runbook `:71-72`. Failure correctly prevents C196. |
| A18 | Step 18, deadline | C1120 | LLDB tab ready; immediately before C196 | YES | Ledger `:70`; runbook `:73-75`. |
| A19 | Step 19, attach | C196 | exact numeric C1114/C1115/C1119 child; original script; LLDB tab; five command blocks resolve | YES (runtime resolution unknown) | Ledger `:15`; runbook `:76-80`; static limits `LLDB_STATIC_REVALIDATION.md:28-35`. |
| A20 | Step 20, first signal | C1121 | C196 visibly loaded/resumed; same exact live helper PID; exactly one signal | YES | Ledger `:71`; runbook `:81-83`. |
| A21 | Step 21, bounded evidence | C1122-C1127 | C196 active; exact PIDs/paths; single bounded observation window | YES | Ledger `:72-77`; runbook `:84-86`. |
| A22 | Step 22, detach | C197 | same existing C196 PTY; before 150 seconds; one ETX then exact detach/quit bytes | YES | Ledger `:16`; runbook `:87-90`. |
| A23 | Step 23, returned parent | C1145 | exact `returned` path absent; immediately before C1144 | YES on normal/post-C196 path | Ledger `:95,97-101`; runbook `:91-93`. |
| A24 | Step 24, raw trace | C1144 | C197 attempted/completed in same PTY; C1145 just created destination; before C1128; screen for prohibited content | YES on ordinary post-C196 path | Ledger `:94-100`; runbook `:94-96`. |
| A25 | Step 25, runtime files | C1130 | C1144 completed; six source files exist; screen passed; exact destination exists | YES only after helper+GUI launch and C1144 | Ledger `:80,97-101`; runbook `:97-99`. Pre-C196 branch is A32/A33. |
| A26 | Step 26, graceful cleanup | C1128 if GUI live | C197 terminal; evidence frozen; exact GUI PID still identifies run-owned process | YES conditionally | Ledger `:78`; runbook `:100-101`. |
| A27 | Step 27, fallback | applicable C1129 subcommand(s) | evidence frozen; exact PID remains live and still matches frozen record | YES conditionally | Ledger `:79`; runbook `:102-104`; mismatch means do not invoke. |
| A28 | Step 28, rollback | C1131-C1139 | any reconstruction write occurred; step 4 baseline completed; applicable files/derivatives may exist | YES after step-5-or-later mutation | Ledger `:81-89`; runbook `:105-106`. `rm -f/-rf` tolerates absent additions/derivatives. |
| A29 | Step 29, rollback proof | C1140-C1141 | rollback commands completed; eight source/lock bytes exist; repo is available | YES | Ledger `:90-91`; runbook `:107-109`. |
| A30 | Step 30, temp removal | C1142-C1143 | returned evidence exists; A29 passed; exact temp root is the target | YES | Ledger `:92-93`; runbook `:110-111`. |
| A31 | Step 31, handoff | none | completed evidence packet and exact returned directory exist | N/A | Runbook `:112-115`. No C-ID; its missing schema disposition/return action is B22/B40. |
| A32 | Explicit step-5 C1091 mismatch route | steps 25-28, therefore C1130 then C1128/C1129 as applicable and C1131-C1139 | C1130 requires prior C1144; C1144 requires post-C197 transcript; branch is pre-C196/pre-C197 | **NO** | Runbook `:39-41,97-106`; ledger `:80,94-101`. Confirmed known defect. Route must invoke neither C1144 nor C1130. |
| A33 | Other pre-C196 stops after reconstruction starts (steps 6-18) | universal “approved evidence preservation and rollback”; sole current runtime-file return is C1130, then C1128/C1129 as applicable, C1131-C1139 | C1130 requires C1144 after C197, but C196/C197 never occurred | **NO if C1130 is used** | Runbook `:18-25,42-75`; ledger `:80,94-101`. This is the additional same-class branch defect; an explicit pre-C196 route is required for all such stops, not step 5 alone. |
| A34a | Stop before C1070 (step-2 absence mismatch) | universal preservation/rollback prose; no literal route | temp/evidence/baseline trees do not exist; C1131-C1137 baseline sources cannot exist | YES only if C1131-C1139 are not invoked | Runbook `:18-25,33-36,105-106`. A literal failure-record/handoff route is required; invoking step 28 here would violate its source prerequisites. |
| A34b | Partial C1070 failure | universal preservation/rollback prose; no literal route | only an unknown subset of run-root directories may exist; no baseline file is guaranteed | **NO if C1131-C1139 are invoked** | Ledger `:20,81-89`; runbook `:35-38,105-106`. Use partial-root evidence/disposition and exact-root cleanup, not baseline restoration. |
| A34c | Failure during C1071-C1077 or C1078 mismatch before baseline acceptance | universal preservation/rollback prose; no literal route | zero to seven baseline copies may exist; product reconstruction has not begun; C1131-C1137 sources are not all guaranteed | **NO if C1131-C1139 are invoked before all seven copies exist** | Ledger `:21-28,81-89`; runbook `:37-41,105-106`. A C1078 mismatch after all seven copies exists still needs no product rollback because no reconstruction write occurred. |
| A35 | Step 9/10 build or package failure | pre-C196 preservation plus rollback | C1131-C1139 can hold because baseline completed; C1130 cannot hold because no C197/C1144 | **NO if C1130 is used** | Runbook `:50-53`; same structural defect as A33 and known C1105-C1108 return gap. |
| A36 | Steps 12-18 launch/identity/contact/revalidation failure | pre-C196 preservation, applicable exact-PID cleanup, rollback | exact-PID cleanup can hold only for captured/revalidated PIDs; C1130 still cannot hold | **NO for C1130; YES for applicable cleanup** | Runbook `:59-75,102-106`; ledger `:78-80`. |
| A37 | Step 19 breakpoint/setup failure after C196 begins | C197, C1145, C1144, C1130, cleanup, rollback | same C196 PTY exists; C197 before bound; then returned path absent; transcript and six runtime sources exist | YES when safely possible | Runbook `:18-25,76-80`; ledger `:15-16,80,94-101`. |
| A38 | Steps 20-21 post-attach failure | C197 then C1145→C1144→C1130 and cleanup/rollback | same as A37 | YES when safely possible | Runbook `:18-25,81-86`. |
| A39 | C197/detach failure | attempted C197, then preservation when safe | C1144 can export the attempted C196/C197 tab after C1145; evidence is invalid but capturable | YES | Runbook `:87-90`; ingestion rejects duration/state defects at ingestion contract `:13-17`. |
| A40 | C1145 absence-test failure | no C1144/C1130; retain state and stop | fail-closed rule expressly prohibits alternate destination | YES for non-invocation | Ledger `:95,97-101`. Required transcript has no current return path: B29/B40, not class A. |
| A41 | C1144 prohibited-content branch | no C1130; retain state for separately governed redaction | current transfer must stop | YES for non-invocation | Ledger `:94`; evidence packet `:5-9`. Current packet has no return action: B40. |
| A42 | C1130 copy/screen failure | no forward deletion; retain state | source/destination may be incomplete; C1128-C1143 must not erase unpreserved evidence | YES only if stop preserves state | Universal stop `OWNER_OPERATED_RUNBOOK.md:18-26`; ordering fence ledger `:97-101`. |
| A43 | Exact-PID cleanup conditional | C1128 and/or applicable C1129 only | live PID and frozen identity match | YES; otherwise command is not invoked | Runbook `:100-104`; ledger `:78-79`. |
| A44 | Rollback/proof failure or evidence incomplete | stop; do not invoke C1142; retain temp root | C1142 requires evidence frozen and A29 pass | YES for non-invocation | Runbook `:107-111`; ledger `:92-93,100-101`. |

Class-A count: **6 flagged rows representing two root defects**: invalid post-C196-only C1130 use on the step-5 route and all other post-reconstruction/pre-C196 stop scopes (A32, A33, A35, A36), and unavailable baseline sources if generic rollback is invoked during partial C1070 or incomplete baseline capture (A34b, A34c). A34a is conforming only when rollback copy commands are not invoked. No post-C196 prerequisite contradiction was found. C196 and C197 remain separate, exact, valid, and unused (`COMMAND_AUTHORITY_LEDGER.md:11,15-16`; `LLDB_STATIC_REVALIDATION.md:37-49`). The normal chain C1145→C1144→C1130 is correct (`COMMAND_AUTHORITY_LEDGER.md:94-101`; runbook `:91-99`).

## 3. Matrix B — required evidence capture and return

`COMPLETE` means both enumerated capture/production and return/inclusion exist. `INCOMPLETE` is class B. `DYNAMIC-UNKNOWN` means the capture route exists but the runtime fact may legitimately be absent.

| Row | Declared required byte/object | Exact producer/capture | Exact return/inclusion | Status |
|---|---|---|---|---|
| B01 | owner/operator | step-1 manual record (`OWNER_OPERATED_RUNBOOK.md:30-32`) | completed form is named at step 31 but no enumerated file creation/copy | **INCOMPLETE — no enumerated return** |
| B02 | run start/end UTC | step 1 / step 31 manual record | no enumerated completed-form return | **INCOMPLETE** |
| B03 | attach/detach monotonic ns and duration | C1120 start; C1121 says record time; C197/step 22 says record stop (`ledger:70-71`; runbook `:73-90`) | LLDB transcript C1144 contains terminal bytes but not an enumerated monotonic capture/returned form | **INCOMPLETE — detach/derived timing capture and form return absent** |
| B04 | OS, repo HEAD and branch | step 1 says record (`runbook:30-32`) | none | **INCOMPLETE — no exact capture command or return** |
| B05 | runbook SHA | none in ledger | form field only (`EVIDENCE_RETURN_PACKET.md:18`) | **INCOMPLETE — no capture/return action** |
| B06 | command-ledger SHA | none in ledger | form field only (`:19`) | **INCOMPLETE** |
| B07 | LLDB-script SHA | static C196 path is bound, but no future hash command | form field only (`:20`) | **INCOMPLETE** |
| B08 | exact approval token/hash | owner return is prerequisite; no enumerated capture/hash | form field only (`:21`) | **INCOMPLETE** |
| B09 | 12 candidate sources plus lock identities | C1091 prints hashes (`ledger:41`) | no raw-output capture/export or form-return action | **INCOMPLETE** |
| B10 | seven baseline identities | C1078 prints hashes (`ledger:28`) | no raw-output capture/export or form-return action | **INCOMPLETE** |
| B11 | six Root projection paths/targets plus facade | C1093-C1099 create; step 6 says record (`runbook:42-44`) | no enumerated listing/capture or returned form | **INCOMPLETE** |
| B12 | archive path/size/hash | C1100-C1101 copy/hash (`ledger:50-51`) | no output capture/return; size has no capture command | **INCOMPLETE** |
| B13 | overlay input/script, two output hashes, two grep results | static manifest; C1102-C1104 (`ledger:52-54`) | no raw-output capture/return | **INCOMPLETE** |
| B14 | complete focused-test output | C1105 emits to terminal only (`ledger:55`) | none; C1130 copies only six helper/GUI files (`ledger:80`) | **INCOMPLETE — known defect** |
| B15 | complete typecheck output | C1106 emits to terminal only (`ledger:56`) | none | **INCOMPLETE — known defect** |
| B16 | complete build output | C1107 emits to terminal only (`ledger:57`) | none | **INCOMPLETE — known defect** |
| B17 | complete package output | C1108 emits to terminal only (`ledger:58`) | none | **INCOMPLETE — known defect** |
| B18 | five fresh package hashes | C1109 prints hashes (`ledger:59`) | no raw-output capture/return | **INCOMPLETE** |
| B19 | bundle IDs, helper LSUIElement/version/asar integrity | C1110-C1111 print plist bytes (`ledger:60-61`) | no raw-output capture/return | **INCOMPLETE** |
| B20 | fourteen relative symlink path/target pairs | C1112 prints topology (`ledger:62`) | no raw-output capture/return | **INCOMPLETE** |
| B21 | standalone/embedded exact comparison output/exit | C1113 (`ledger:63`) | no raw-output capture/return | **INCOMPLETE** |
| B22 | exactly one disposition for every runbook step 1-31 | form only declares steps 1-30 and a `1-30` row (`EVIDENCE_RETURN_PACKET.md:38-46`) | step 31 handoff has no schema row | **INCOMPLETE — known defect; 30/31 declared** |
| B23 | every skipped step and deviation | manual form entry (`evidence packet:46`) | completed form has no enumerated returned-file action | **INCOMPLETE** |
| B24 | helper PID/PPID/PGID/executable, launch record and immediate revalidation | C1114 writes `helper.pid`, stdout/stderr; C1115/C1119 print process state (`ledger:64-65,69`) | C1130 returns PID/log files only; C1115/C1119 outputs and hashes not returned | **INCOMPLETE** |
| B25 | GUI PID/PPID/executable, contact action/result/time | C1117 writes PID/logs; C1118 manual record; C1119 prints state (`ledger:67-69`) | C1130 returns PID/logs only; process/contact record has no enumerated returned form | **INCOMPLETE** |
| B26 | expanded C196 bytes, start, five breakpoint-resolution results | C196/LLDB produces bytes; C1144 exports and hashes complete LLDB tab (`ledger:15,94`) | C1144 writes directly to exact `returned/lldb-transcript.txt` | **COMPLETE capture/return mechanism; runtime resolution DYNAMIC-UNKNOWN** |
| B27 | exact C1121 command/hash/time/exit | C1121 executes kill; runbook says record (`ledger:71`; runbook `:81-83`) | no CONTROL transcript export or returned form action | **INCOMPLETE** |
| B28 | immediate/final process, socket/owner, eight-second, GUI observations | C1122-C1127 produce terminal/manual observations (`ledger:72-77`) | no CONTROL transcript export or returned form action | **INCOMPLETE; results DYNAMIC-UNKNOWN** |
| B29 | raw LLDB transcript, trace events/backtraces, C197 result, bound | C197 and C1144 (`ledger:16,94`) | C1144 direct return and hash | **COMPLETE mechanism on ordinary post-C196 path; DYNAMIC-UNKNOWN events; no return on A40/A41 terminal branches** |
| B30 | helper/gui stdout, stderr and PID raw files | C1114/C1117 create six files (`ledger:64,67`) | C1130 copies six after C1144 (`ledger:80`) | **INCOMPLETE — capture/return exists on post-C196 path, but required per-file hashes/manifest are not enumerated and pre-C196 return is absent** |
| B31 | graceful/fallback cleanup exact commands/outcomes | C1128/C1129 execute; runbook says record (`ledger:78-79`; runbook `:100-104`) | no CONTROL transcript export or completed-form return | **INCOMPLETE** |
| B32 | eight post-rollback baseline/lock hashes | C1140 prints hashes (`ledger:90`) | no raw-output capture/return | **INCOMPLETE** |
| B33 | five additions absent and dependency/build derivatives absent | C1138-C1139 remove; C1141 Git status is aggregate proof (`ledger:88-91`) | no captured/hashed C1141 bytes | **INCOMPLETE** |
| B34 | frontend Git-status exact bytes/hash | C1141 emits expected zero bytes/exit (`ledger:91`) | no file capture/hash/return | **INCOMPLETE** |
| B35 | fixed temporary-root absence | C1142 removes; C1143 tests absence (`ledger:92-93`) | no enumerated exit/result record return | **INCOMPLETE** |
| B36 | retained-evidence manifest: every path, size, SHA, provenance, credential-screen result | no manifest-generation/hash command; C1144 hashes only LLDB transcript | none | **INCOMPLETE** |
| B37 | intentionally retained state and reason | runbook/ledger say retain on certain stops | no exact record/returned-form action | **INCOMPLETE** |
| B38 | missing bytes, timing uncertainty, deviations, redactions, unsupported inferences, owner attestation | blank form fields (`evidence packet:84-91`) | no enumerated completed-form creation/return | **INCOMPLETE** |
| B39 | causal-matrix supporting/contradicting bytes for all nine propositions | consumers use B18-B30; matrix remains `UNKNOWN` until runtime (`INGESTION...:44-60`) | later intake/matrix, not current capture | **DYNAMIC-UNKNOWN is valid, but upstream missing returns B18-B30 prevent complete intake** |
| B40 | completed evidence packet and exact returned directory handoff | step 1 says “start” form; step 25 says populate; step 31 says complete and hand off (`runbook:30-32,97-99,112-115`) | C1144 returns one transcript and C1130 six files; no command creates/returns completed form or hashes the directory | **INCOMPLETE** |

Class-B count: **37 incomplete grouped rows**, **2 complete conditional mechanisms** (B26, B29), and **1 downstream dynamic row** (B39) whose runtime result is correctly `UNKNOWN` but whose upstream return chain is incomplete. This count groups repeated fields rather than inflating one missing CONTROL transcript into one finding per command.

## 4. Findings limited to the two authorized classes

### F-A1 — pre-C196 preservation route violates C1130's prerequisite

The explicit step-5 route jumps to steps 25-28 (`OWNER_OPERATED_RUNBOOK.md:39-41`). Step 25 invokes C1130 (`:97-99`), whose ledger row requires it to occur after C1144 (`COMMAND_AUTHORITY_LEDGER.md:80`); C1144 is the post-C197 LLDB transcript export (`:94`), and the ordering fence repeats C1145→C1144→C1130 (`:97-101`). C196/C197 cannot have occurred on that branch. The same defect applies to all post-reconstruction pre-C196 stops through step 18 if “approved evidence preservation” is implemented using the only current return-copy command, C1130. Consequence: the packet cannot both obey its stop route and obey the invoked command prerequisite.

Required repair: replace the step-5 jump and universal pre-C196 branch with a literal fail-closed pre-C196/pre-C197 preservation, applicable exact-PID cleanup, rollback, proof, and handoff route that invokes neither C1144 nor C1130.

The route must also distinguish four early phases: before C1070 (no temp tree), partial C1070 (partial tree only), C1071-C1078 before accepted complete baseline (no product mutation and incomplete rollback sources possible), and after the first C1079 reconstruction write through pre-C196 (complete baseline and product rollback required). C1131-C1137 are legal only in the fourth phase, or after all seven baseline sources are proved present; they cannot be a generic early-stop action.

### F-B1 — step 31 has no required disposition row

The runbook contains 31 numbered steps (`OWNER_OPERATED_RUNBOOK.md:30-115`), while the evidence schema requires only 1-30 and provides a `1-30` row (`EVIDENCE_RETURN_PACKET.md:38-46`). Ingestion requires exactly one disposition for every step (`INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md:23-26`). Consequence: complete ingestion cannot validate step 31.

Required repair: change the schema and instructions to steps 1-31 and require one literal row per step; no range placeholder.

### F-B2 — C1105-C1108 outputs have no capture or return operation

C1105-C1108 write only to the terminal (`COMMAND_AUTHORITY_LEDGER.md:55-58`); steps 9-10 require complete output retention (`OWNER_OPERATED_RUNBOOK.md:50-53`); the evidence packet requires those transcripts (`EVIDENCE_RETURN_PACKET.md:23-28`). C1130 copies only six helper/GUI files (`COMMAND_AUTHORITY_LEDGER.md:80`), and C1144 exports only LLDB. Consequence: supplying the required outputs would require an unenumerated action.

Required repair: enumerate exact, hash-bound capture and return of the complete combined stdout/stderr and exit status for each C1105-C1108 invocation, including failure paths.

### F-B3 — additional CONTROL-output requirements have the same missing capture/return class

The same mechanism gap affects the static/runtime outputs identified in B04-B21, B24-B25, B27-B28, and B31-B35: identity hashes, projection topology, archive/overlay output, package identity/topology, PID/process/stat/signal/GUI observations, cleanup results, rollback hashes, Git status, and final absence. The schema also requires a raw-output file/hash per numbered step (`EVIDENCE_RETURN_PACKET.md:38-44`), but there is no CONTROL-tab transcript capture/export in the ledger. This is one shared plumbing defect, not a claim that each dynamic fact must be positive.

Required repair: enumerate one complete CONTROL-tab transcript capture/export with exact command boundaries, path and SHA-256, preserved on every terminal path; retain separate C1105-C1108 files only if the owner requires per-command artifacts.

### F-B4 — completed form and retained-evidence manifest have no production/return action

The runbook asks the owner to start/populate/complete a form (`OWNER_OPERATED_RUNBOOK.md:30-32,97-99,112-115`), and the form requires every retained path/size/hash/provenance/screen result (`EVIDENCE_RETURN_PACKET.md:80-81`), but no ledger row creates a writable form copy, returns it, enumerates all returned files, or hashes the returned package. C1144 hashes only the LLDB transcript; C1130 does not hash the six copied files. Consequence: the “exact returned directory” cannot meet its own inclusion and hash-binding contract without unenumerated operations.

Required repair: enumerate form materialization/completion, credential screening, per-file manifest generation, return copy, and final directory completeness/hash verification on normal and failure paths.

### F-B5 — pre-C196 and two post-C196 stop branches lack a complete return action

All pre-C196 stops lack a legal evidence-copy route because C1130 is post-C1144 only. If C1145 fails, the packet correctly stops but has no alternate enumerated return for the required LLDB transcript; if C1144 discovers prohibited content, it correctly halts transfer but has only a future separately governed redaction statement, not a current return action (`COMMAND_AUTHORITY_LEDGER.md:94-101`; `EVIDENCE_RETURN_PACKET.md:5-9`). These branches may legitimately return `MISSING`, but the branch disposition and safe retained-state manifest still require an enumerated action.

Required repair: make every terminal path explicitly produce either (a) the allowed returned objects plus hashes, or (b) a returned failure/disposition record naming safely retained, not-transferred state and the required separately governed rerun/redaction.

## 5. Minimal sequential new command allocation

The smallest coherent allocation is **C1146-C1151** (six new IDs, no gap or reuse). Existing C196/C197 and C1145→C1144→C1130 remain byte-preserved. Exact shell/operator bytes must be authored and frozen by the repair owner; this audit specifies placement and purpose without inventing executable bytes.

| New ID | Exact placement | Bounded purpose |
|---|---|---|
| C1146 | Arm before step 2; finalize on every terminal path after the last CONTROL action and before handoff | Enumerate transcript start, stop/export, credential screen, exact return path, and SHA-256 for one complete unedited CONTROL-tab transcript. Record a byte-range/hash/disposition for every runbook step. Prove that the C1105, C1106, C1107, and C1108 command boundaries, complete combined outputs, and exit results are each wholly included; capture must survive a failing command. |
| C1147 | First operation on any pre-C196 terminal path, mutually exclusive with C1145 | Exact absent-path test plus creation of the literal `returned` parent for pre-C196 evidence only. This path invokes neither C1144 nor C1130. |
| C1148 | Pre-C196 path after credential screening and before any cleanup that could destroy bytes | Copy the enumerated, extant run-owned evidence set (including C1146 transcript and any helper/GUI logs/PIDs already created) to `returned`; record missing conditional sources rather than failing on legitimately not-yet-created files. This is the pre-C196 alternative to C1130. |
| C1149 | Step 1 creates the run-local writable copy; every terminal path finalizes it after outcomes are known | Materialize and return `EVIDENCE_RETURN_PACKET.md` with 31 literal disposition rows, exact skipped/deviation entries, static identities, dynamic observations, and `MISSING` where applicable. The ledger row must enumerate the writable source and exact final returned path. |
| C1150 | After C1144/C1130 on post-C196 paths or after C1148 on pre-C196 paths, and after C1146/C1149 finalization | Generate the retained-evidence manifest over every returned file with path, size, SHA-256, provenance, credential-screen result, and inclusion/disposition. |
| C1151 | Last operation before step-31 handoff; before deleting any still-required source state | Verify the exact returned allowlist, manifest self-consistency, hashes, step-1-through-31 dispositions, CONTROL-transcript per-step byte ranges/hashes, complete C1105-C1108 inclusion, and presence or explicit `MISSING` disposition for every required object; emit/hash the final completeness result. |

Required cross-reference repairs within the owner-adopted scope: ledger status/range; universal stop rule; step-5 route; steps 9-10 and 23-31; evidence-return schema; ingestion mapping/range; token/range; index and new freeze. If a single CONTROL transcript is not accepted as the exact per-command artifact for C1105-C1108, allocate four additional contiguous IDs C1152-C1155 for per-command transcript capture/hash; do not rerun any command merely to create evidence.

## 6. Mechanical conclusions

- Known defect coverage: step disposition through 31 — confirmed missing; step-5 route must be pre-C196/pre-C197 and invoke neither C1144 nor C1130 — confirmed; complete C1105-C1108 capture/return — confirmed missing.
- Additional same-class defects: the same invalid C1130 route affects all other post-reconstruction pre-C196 stops; the same missing capture/return plumbing affects the enumerated CONTROL outputs, completed form, per-file hashes/manifest, and failure dispositions.
- Preserved invariants: C196/C197 are separate, exact, valid, and unused. The LLDB script remains byte-identical and statically limited; runtime symbol resolution is `UNKNOWN`, not a repair finding. On the ordinary post-C196 path, C1145→C1144→C1130 is correctly ordered.
- No runtime, debugger, package, helper/GUI, signal, credential, product, release, reliance, Git, Task Management, foreign-loop, or post-freeze verifier action was taken. No prepared/frozen packet byte was modified.

Final verdict: `REPAIR_REQUIRED`.
