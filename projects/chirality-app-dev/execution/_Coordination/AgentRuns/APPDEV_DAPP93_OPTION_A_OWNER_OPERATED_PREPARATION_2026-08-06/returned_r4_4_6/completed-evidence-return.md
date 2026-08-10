# D-APP-93 Option A evidence-return packet

Status: `COMPLETED — POST-FIRST-WRITE/PRE-C196 TERMINAL ROUTE (R4.4.6 + CLEANUP-OBSERVATION ADDENDUM) — C1118 UNEXPECTED-PROMPT STOP — NO CAUSAL CLAIM`

Do not fill this template from memory. Enter exact bytes or `MISSING`, retain
raw files unchanged, and leave whole-file hashing to the post-form-freeze tail. Never include a token, API
key, keychain value, secret, memory dump, or environment dump. If any appears,
stop transfer, retain state safely, and request a separately governed
credential-safe redaction process; do not silently normalize it.

## Run identity

- owner/operator: `Ryan Tufts (owner-personal execution; no agent, supervisor, or delegated operator)`
- run start/end UTC: `MISSING` / `MISSING` (no per-command clock in the CONTROL transcript; anchors under Limitations)
- attach/detach monotonic ns: `NOT_RUN` / `NOT_RUN` (C196/C197 never invoked)
- attach-to-detach seconds: `NOT_RUN`
- repo HEAD/branch: `7aada3fbadf340a07ef828cc18b350c8c01b517d` / `codex/app-dapp88-evaluation-resume-20260804`
- runbook SHA-256: `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`
- command-ledger SHA-256: `4989ac38d2f6e4b9bc353fdbf842a2db98c9163914f6c79f93751fd581649fa5` (R4.4.5 ledger identity; R4.4.6 rebound the return namespace to returned_r4_4_6/)
- LLDB-script SHA-256: `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` (unused; C196 never began)
- exact owner approval token/hash: `R4.4.6 execution token adopted; cleanup-observation addendum freeze 8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf, verifier PASS 27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f`

## Input and package identities

CONTROL-only items cite returned_r4_4_6/control-transcript.txt. Seven baseline
hashes: C1078 stdout in transcript. Thirteen candidate-source/lock hashes:
C1091 stdout in transcript. Six Root projection targets: C1094-C1099 exit 0.
Local Electron archive: /private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip,
C1101 stdout ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28.
Overlay (D-APP-93-owned apply-local-electron-dist-overlay-dapp93.mjs, script
SHA-256 5ae3d79bdb711153c315920ac4f4d584f6bab2d8d9d17fa2f08c31ed9242c7b7):
executed C1102; post-overlay config hashes in returned_r4_4_6/c1103.sha256.txt
(electron-builder.runtime-helper.json 1cb9e4c7325166f69139eeba3a0bdfcfa1d4f871e03acf4af1809aa88fa02a36;
package.json b53a867e8aa7d8874cf7ce2417691a05d449babaa9bf0b905c550deb13b3ac6d);
complete post-overlay bytes in returned_r4_4_6/c1104.*. Focused-test/typecheck/
build/package transcripts: returned_r4_4_6/c1105-c1108 .output.txt and .exit.txt.
Actual package: BUILT — C1108 command_exit=0, tee_exit=0; helper bundle
dist-runtime-helper/mac-arm64 and GUI bundle dist/mac-arm64 produced; overlay
electronDist resolved to this run root; desktop:verify-dependencies PASS.

Public package results:

- helper/GUI bundle IDs: `com.chirality.app.runtime-helper` / `com.chirality.app`
- helper LSUIElement/version/asar integrity: `LSUIElement=true; CFBundleShortVersionString 2.0.0; Resources/app.asar SHA256 c2c8dc65e3015c6737b462f3c737391c96e2f9be0ac0dfc7bd655925365a7167 (C1110 plist)`
- embedded-helper count/path: `helper embedded at dist/mac-arm64/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app`
- fourteen relative symlink path/target pairs: `C1112 stdout in transcript — exactly fourteen framework symlink pairs`
- standalone/embedded comparison exact output/exit: `C1113 emitted only declared framework directory-loop diagnostics; zero "differ" lines; standalone and embedded helper byte-identical`

## Literal numbered-step outcomes

| Step | Authority ID(s) | UTC | Monotonic ns | Exact input hash | Exit/result | Raw-output file/hash | Recorded state |
|---|---|---|---|---|---|---|---|
| 1 | C1146.01 | `MISSING` | `MISSING` | `MISSING` | 0 | control-transcript.txt | RECORDED |
| 2 | C1067(returned_r4_4_6); C1068; C1069; C1146.02 | `MISSING` | `MISSING` | `MISSING` | 0; three silent passes | control-transcript.txt | RECORDED |
| 3 | C1070; C1146.03 | `MISSING` | `MISSING` | `MISSING` | 0 | control-transcript.txt | RECORDED |
| 4 | C1071-C1078; C1146.04 | `MISSING` | `MISSING` | `MISSING` | 0; seven baseline hashes | control-transcript.txt | RECORDED |
| 5 | C1079-C1091; C1146.05 | `MISSING` | `MISSING` | `MISSING` | 0; thirteen candidate hashes | control-transcript.txt | RECORDED |
| 6 | C1092-C1099; C1146.06 | `MISSING` | `MISSING` | `MISSING` | 0 (C1093 input pasted during C1092; type-ahead echo, executed once after C1092 completed; 470/470 tree verified) | control-transcript.txt | RECORDED |
| 7 | C1100-C1101; C1146.07 | `MISSING` | `MISSING` | `MISSING` | 0; archive hash ad4a0ae3…fe28 | control-transcript.txt | RECORDED |
| 8 | C1102-C1104; C1146.08 | `MISSING` | `MISSING` | `MISSING` | 0; overlay hashes 1cb9e4c7…, b53a867e… | c1103.sha256.txt; c1104.* | RECORDED |
| 9 | C1105; C1106; C1107; C1146.09 | `MISSING` | `MISSING` | `MISSING` | record 0; each sidecar command_exit=0 tee_exit=0; C1105 matched four of five named files per erratum SHA-256 f6cbfc084e769a294e082af4103569e29f79d87c87d252ffd7f2d2453b5ba0c7 | c1105-c1107 .output/.exit | RECORDED |
| 10 | C1108; C1146.10 | `MISSING` | `MISSING` | `MISSING` | sidecar command_exit=0 tee_exit=0; both app bundles packaged; dependency-boundary PASS; instruction-root integrity pass (advisory source-completeness needs_remediation) | c1108.output.txt; c1108.exit.txt | RECORDED |
| 11 | C1109-C1113; C1146.11 | `MISSING` | `MISSING` | `MISSING` | 0; five package hashes, two plists, fourteen symlinks, diff zero "differ" | control-transcript.txt | RECORDED |
| 12 | C1114; C1146.12 | `MISSING` | `MISSING` | `MISSING` | 0; helper launched, helper_pid=92988 captured to helper.pid | helper.stdout.txt; helper.pid | RECORDED |
| 13 | C1115; C1146.13 | `MISSING` | `MISSING` | `MISSING` | 0; PID 92988, PPID 90439, exact helper executable, --runtime-daemon | control-transcript.txt | RECORDED |
| 14 | C1116; C1146.14 | `MISSING` | `MISSING` | `MISSING` | 1; both /private/tmp/…/user/runtime/runtime.sock and runtime.owner.json reported "No such file or directory" at pre-GUI time | control-transcript.txt | RECORDED |
| 15 | C1117 launch + delayed C1117 gui_pid capture (per addendum); C1146.15 | `MISSING` | `MISSING` | `MISSING` | GUI launched, window appeared; PID-capture line delayed and entered under the addendum, $! still bound to the C1117 child; gui_pid=93012 to gui.pid; A1117.ID confirmed PID 93012 / PPID 90439 / exact GUI executable | gui.stdout.txt; gui.pid | DEVIATION |
| 16 | C1118 | `MISSING` | `MISSING` | `MISSING` | not performed as an owner action; execution stopped at the C1118 unexpected-prompt condition (keychain modal) | none | NOT_RUN |
| 17 | C1119 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 18 | C1120 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 19 | C196 | `MISSING` | `MISSING` | `MISSING` | not executed; approval preserved unused | none | NOT_RUN |
| 20 | C1121 | `MISSING` | `MISSING` | `MISSING` | not executed; no signal sent | none | NOT_RUN |
| 21 | C1122-C1127 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 22 | C197 | `MISSING` | `MISSING` | `MISSING` | not executed; approval preserved unused | none | NOT_RUN |
| 23 | C1147.01; C1147.02; C1146.23 | `MISSING` | `MISSING` | `MISSING` | 0; returned_r4_4_6 parent created | control-transcript.txt | RECORDED |
| 24 | C1144 | `MISSING` | `MISSING` | `MISSING` | route invokes neither C1144 nor C1130 | none | NOT_RUN |
| 25 | C1149.01-C1149.17; C1146.25 | `MISSING` | `MISSING` | `MISSING` | 0; seventeen copies silent | seventeen returned_r4_4_6 files | RECORDED |
| 26 | A1128.PRE; C1128; C1146.26 | `MISSING` | `MISSING` | `MISSING` | 0; A1128.PRE matched GUI 93012; C1128 /bin/kill -TERM "$gui_pid"; GUI window closed | control-transcript.txt | RECORDED |
| 27 | A1129.H; helper C1129; A1129.G; C1146.27 | `MISSING` | `MISSING` | `MISSING` | A1129.H matched helper 92988; helper C1129 /bin/kill -KILL "$helper_pid"; A1129.G matched zero rows (GUI already exited on C1128 TERM); GUI-target C1129 NOT applicable/not run; step record exit=1 reflects the final zero-match ps | control-transcript.txt | RECORDED |
| 28 | C1131-C1139; C1146.28 | `MISSING` | `MISSING` | `MISSING` | 0; seven baselines restored, five additions and derivatives removed | control-transcript.txt | RECORDED |
| 29 | C1140-C1141; C1146.29 | `MISSING` | `MISSING` | `MISSING` | 0; eight hashes match baseline; C1141 git status empty (clean) | control-transcript.txt | RECORDED |
| 30 | C1150.R; C1151.T; C1148; C1153.01; C1142; C1143; C1146.30; C1151.F | `MISSING` | `MISSING` | `MISSING` | 0; temp root removed and absence proved; C1146.30 final CONTROL input | control-transcript.txt; control-transcript-precleanup.txt | RECORDED |
| 31 | C1152 | `MISSING` | `MISSING` | `MISSING` | this completed form; freeze by C1154.03 pending | completed-evidence-return.md | READY_FOR_RAW_RETURN |

Allowed recorded-state values are `RECORDED`, `FAILED`, `NOT_RUN`, `DEVIATION`,
`MISSING`, and for step 31 only `READY_FOR_RAW_RETURN`. Later ingestion derives
all PASS dispositions and the terminal verdict.

## Target and trace evidence

- helper PID / PPID / PGID / executable / launch record hash: `92988 / 90439 / 92988 / dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service --runtime-daemon; launch record helper.pid returned`
- GUI PID / PPID / executable / launch record hash: `93012 / 90439 / dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality --user-data-dir=/private/tmp/chirality-dapp93-owner-operated-20260807/user; launch record gui.pid returned`
- proof helper is the exact launch direct child immediately before C196: `NOT_RUN (C196 never reached); C1115 at launch confirmed PID 92988 direct child of CONTROL shell 90439`
- GUI contact action/result/time: `C1118 owner action NOT_RUN. Independent evidence: gui.stderr records runtime.connectivity.bind attempt 1 at 2026-08-08T05:57:26.027Z returning "Unknown project: chirality-app-dev" — the R3-accepted authenticated-contact signature — followed by attempts 2-6 failing on control.sock.`
- C196 literal expanded command/hash and start time: `NOT_RUN`
- five breakpoint-resolution results: `NOT_RUN`
- first SIGTERM C1121 exact command/hash/time/exit: `NOT_RUN`
- immediate helper-survival result: `NOT_RUN`
- immediate and final socket/owner stat results: `pre-GUI C1116 (step 14) reported runtime.sock and runtime.owner.json ABSENT ("No such file or directory"); post-signal observations NOT_RUN`
- eight-second bounded observation: `NOT_RUN`
- final helper/GUI process state: `both terminated under enumerated cleanup — GUI 93012 exited on C1128 TERM; helper 92988 killed by C1129`
- GUI owner observation (responsive/transport loss/exit): `keychain modal "Keychain Not Found" raised at GUI launch; dismissed via Cancel; window later closed on C1128`
- exact raw LLDB transcript path/hash: `NOT_RUN`
- exact complete through-cut CONTROL transcript path: `returned_r4_4_6/control-transcript.txt`
- C1146.01-C1146.30 raw exit-record occurrences: `twenty-two records present once each: STEP-01 through STEP-15, STEP-23, STEP-25, STEP-26, STEP-27, STEP-28, STEP-29, STEP-30. STEP-14 and STEP-27 command_exit=1; all others 0. STEP-16 through STEP-22 and STEP-24 correctly absent.`
- C1105/C1106/C1107/C1108 output files and exit sidecars ready for post-freeze hashing: `all present in returned_r4_4_6; c1105-c1108 exits 0/0`
- trace events and bounded backtraces: `NOT_RUN`
- C197 ETX/detach/quit time and terminal result: `NOT_RUN`
- 150-second bound result: `NOT_RUN`

Do not infer a Root stop, callback, signal-delivery seam, socket cleanup, or
cause when the corresponding raw event is absent. Unresolved symbols: `NOT_RUN`.

## Cleanup, rollback, and retention

- graceful/fallback cleanup exact commands and outcomes: `A1128.PRE matched GUI 93012; C1128 /bin/kill -TERM "$gui_pid" sent, GUI exited. A1129.H matched helper 92988; C1129 /bin/kill -KILL "$helper_pid" sent. A1129.G matched zero rows; GUI-target C1129 not applicable/not run. No run-owned process remained.`
- eight post-rollback baseline/lock hashes: `exact C1140 stdout in control-transcript.txt: cli-launcher.ts 850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b; main.ts 16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f; runtime-control-ipc.ts 5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a; package.json 1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53; package-lock.json 5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56; build-electron.mjs a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558; cli-launcher.test.ts 1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9; runtime-control-ipc.test.ts f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6 — identical to the C1078 baseline plus the C1091 lock value`
- five candidate additions absent: `removed by C1138; C1141 clean`
- dependency/build derivatives absent: `removed by C1139; C1141 clean`
- frontend Git status exact bytes/hash: `C1141 empty output — frontend clean`
- fixed temporary root absent: `proven by C1143 exit 0 after C1142`
- C1148 owner inspection observations for every copied artifact: `Owner personally inspected all seventeen candidate artifacts (helper.stdout/stderr/pid, gui.stdout/stderr/pid, c1103.sha256.txt, both c1104 configs, c1105-c1108 outputs and exit sidecars). Supplemented by an agent-side read-only deterministic screen (HELP_HUMAN/Agent 0), counts and masked shapes only, never matched values. Flags resolved to: the proof:secret-scan script name; @aws-sdk credential-provider / token-provider package names in electron-builder's dependency dump; and run-owned /private/tmp path strings. Zero keychain/safeStorage secret echoes in any log. No credential-bearing content found. All seventeen artifacts cleared for C1149 copy.`
- exact returned primary raw-file paths ready for C1154-C1157 post-freeze hashing: `completed-evidence-return.md; control-transcript.txt; control-transcript-precleanup.txt; helper.stdout.txt; helper.stderr.txt; helper.pid; gui.stdout.txt; gui.stderr.txt; gui.pid; c1103.sha256.txt; c1104.electron-builder.runtime-helper.json; c1104.package.json; c1105.output.txt; c1105.exit.txt; c1106.output.txt; c1106.exit.txt; c1107.output.txt; c1107.exit.txt; c1108.output.txt; c1108.exit.txt. lldb-transcript.txt: NOT_RUN (C1154.01 inapplicable). C1155 helper/GUI hashes applicable this attempt.`
- intentionally retained state and reason: `none — every produced artifact was returned and the temp root was lawfully removed after cleanup and rollback proof; nothing required retention`

C1154.03 freezes this direct-return form after C1152; it must never be edited
afterward.

## Limitations and attestation

- missing bytes: `no per-command UTC or monotonic clock in the CONTROL transcript; exact-input hashes not separately computed (every literal input is preserved verbatim in control-transcript.txt); C1105 named five test files but matched four existing (phantom fifth name, dispositioned SHA-256 f6cbfc084e769a294e082af4103569e29f79d87c87d252ffd7f2d2453b5ba0c7)`
- timing uncertainty: `anchors only: session login 2026-08-08T02:58:45Z; gui.stderr first authenticated contact 2026-08-08T05:57:26.027Z; last bind error 2026-08-08T06:00:24.053Z; owner attests route completion and form authoring at approximately 2026-08-08T06:45Z. All step rows carry MISSING rather than reconstructed times.`
- operator deviations: `(1) C1093 pasted during C1092 (type-ahead; executed once after C1092; verified 470/470 tree). (2) C1117 gui_pid capture and STEP-15 record delayed by the intervening C1118 keychain modal; entered under the fresh-verified cleanup-observation addendum with owner attestation that no CONTROL input or background launch intervened, so $! remained the C1117 child (step 15 DEVIATION). (3) STEP-14 exit=1: pre-GUI socket/owner paths absent; forward execution continued to step 15, where the keychain modal became the operative C1118 stop.`
- credential omissions/redactions: `none required; see C1148`
- unsupported inferences expressly not made: `no attach, signal-delivery, teardown, Root-stop, socket-lifecycle, or causal claim is made or implied. The pre-GUI socket absence (step 14) and the gui.stderr control.sock bind failures are recorded raw, not interpreted. The recorded attempt-1 authenticated-contact signature is noted as evidence only; no D-APP-88 first-signal conclusion follows. The run stopped at the C1118 unexpected-prompt condition (missing keychain in the sealed HOME); no keychain was created or modified.`
- owner attestation that the recorded inputs/outcomes are literal: `I, Ryan Tufts, attest that the inputs and outcomes recorded above are literal transcriptions from the exported CONTROL transcript, the returned raw files, and observed filesystem state, not reconstructions from memory. 2026-08-08.`

Execution and a completed template are derivative evidence only. They do not
accept D-APP-88, close DEL-09-04, fire TM-APP-036, establish cause/remedy, or
authorize product/release/reliance action.
