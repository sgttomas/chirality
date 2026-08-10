# D-APP-93 Option A evidence-return packet

Status: `COMPLETED — POST-FIRST-WRITE/PRE-C196 TERMINAL ROUTE — STEP-10 PACKAGE FAILURE RETURNED — NO CAUSAL CLAIM`

Do not fill this template from memory. Enter exact bytes or `MISSING`, retain
raw files unchanged, and leave whole-file hashing to the post-form-freeze tail. Never include a token, API
key, keychain value, secret, memory dump, or environment dump. If any appears,
stop transfer, retain state safely, and request a separately governed
credential-safe redaction process; do not silently normalize it.

## Run identity

- owner/operator: `Ryan Tufts (owner-personal execution; no agent, supervisor, or delegated operator)`
- run start/end UTC: `MISSING` / `MISSING` (no per-command clock in the CONTROL transcript; anchors recorded under Limitations)
- attach/detach monotonic ns: `NOT_RUN` / `NOT_RUN` (C196/C197 never invoked)
- attach-to-detach seconds: `NOT_RUN`
- repo HEAD/branch: `7aada3fbadf340a07ef828cc18b350c8c01b517d` / `codex/app-dapp88-evaluation-resume-20260804`
- runbook SHA-256: `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`
- command-ledger SHA-256: `4989ac38d2f6e4b9bc353fdbf842a2db98c9163914f6c79f93751fd581649fa5`
- LLDB-script SHA-256: `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` (unused; C196 never began)
- exact owner approval token/hash: `R4.4.5 owner retry token, returned in-session and adopted; adoption record R4_4_5_OWNER_RETRY_EXECUTION_AUTHORITY_ADOPTION.md SHA-256 ecbaa53a8850d59098dbf9f313189f54bb3218ffa528610b8c34beccd59373b0`

## Input and package identities

All CONTROL-only items cite the complete through-cut raw transcript at
`returned/control-transcript.txt`. Seven baseline hashes: exact C1078 stdout in
the transcript. Thirteen candidate-source/lock hashes: exact C1091 stdout in
the transcript. Six Root projection targets: C1094-C1099 as entered, exit 0.
Local Electron archive: `/private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip`,
C1101 stdout `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
Overlay: C1102 executed; its stdout and the two post-overlay configuration
hashes are in the transcript and in `returned/c1103.sha256.txt`
(`electron-builder.runtime-helper.json` `0822414929eed5ebd6c87d21db8c8c55abd991f1b946c009e64de0467c5583af`;
`package.json` `01e93e41dd8c7d90a8308e5a347d6779093f15d9fd2ae02aa4f9743159ad89ea`);
complete post-overlay config bytes in `returned/c1104.electron-builder.runtime-helper.json`
and `returned/c1104.package.json`. Focused-test/typecheck/build/package
transcripts: `returned/c1105.output.txt` + `returned/c1105.exit.txt`,
`returned/c1106.output.txt` + `returned/c1106.exit.txt`,
`returned/c1107.output.txt` + `returned/c1107.exit.txt`,
`returned/c1108.output.txt` + `returned/c1108.exit.txt`. Actual package hash:
`NOT_RUN` (C1108 failed before package construction).

Public package results:

- helper/GUI bundle IDs: `NOT_RUN` / `NOT_RUN`
- helper LSUIElement/version/asar integrity: `NOT_RUN`
- embedded-helper count/path: `NOT_RUN`
- fourteen relative symlink path/target pairs: `NOT_RUN`
- standalone/embedded comparison exact output/exit: `NOT_RUN`

## Literal numbered-step outcomes

For each runbook step 1-31 record exactly one literal row; aggregate placeholder
rows are invalid. Steps 1-30 cite their visible C1146.NN raw exit record in the
complete through-cut CONTROL transcript. Step 31 records
`READY_FOR_RAW_RETURN` or the literal non-success state. It is a pre-freeze
handoff-intent observation, not a claim of later hashing or actual receipt.
These are observations, not PASS or terminal verdicts:

| Step | Authority ID(s) | UTC | Monotonic ns | Exact input hash | Exit/result | Raw-output file/hash | Recorded state |
|---|---|---|---|---|---|---|---|
| 1 | C1146.01 | `MISSING` | `MISSING` | `MISSING` (literal input in control-transcript.txt) | 0 | control-transcript.txt | RECORDED |
| 2 | C1067; C1068; C1069; C1146.02 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; three silent passes | control-transcript.txt | RECORDED |
| 3 | C1070; C1146.03 | `MISSING` | `MISSING` | `MISSING` (literal) | 0 | control-transcript.txt | RECORDED |
| 4 | C1071-C1078; C1146.04 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; seven baseline hashes emitted | control-transcript.txt | RECORDED |
| 5 | C1079-C1091; C1146.05 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; thirteen candidate hashes emitted | control-transcript.txt | RECORDED |
| 6 | C1092-C1099; C1146.06 | `MISSING` | `MISSING` | `MISSING` (literal) | 0 | control-transcript.txt | RECORDED |
| 7 | C1100-C1101; C1146.07 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; archive hash ad4a0ae3…fe28 | control-transcript.txt | RECORDED |
| 8 | C1102-C1104; C1146.08 | `MISSING` | `MISSING` | `MISSING` (literal) | 0 | c1103.sha256.txt; c1104.* returned | RECORDED |
| 9 | C1105; C1106; C1107; C1146.09 | `MISSING` | `MISSING` | `MISSING` (literal) | record 0; each sidecar command_exit=0 tee_exit=0; C1105 matched four of five named files per disposition SHA-256 f6cbfc084e769a294e082af4103569e29f79d87c87d252ffd7f2d2453b5ba0c7 | c1105-c1107 .output.txt/.exit.txt returned | RECORDED |
| 10 | C1108; C1146.10 | `MISSING` | `MISSING` | `MISSING` (literal) | sidecar command_exit=1 tee_exit=0; electron-builder: "The specified electronDist does not exist: /private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip" | c1108.output.txt; c1108.exit.txt | FAILED |
| 11 | C1109-C1113 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 12 | C1114 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 13 | C1115 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 14 | C1116 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 15 | C1117 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 16 | C1118 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 17 | C1119 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 18 | C1120 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 19 | C196 | `MISSING` | `MISSING` | `MISSING` | not executed; approval preserved unused | none | NOT_RUN |
| 20 | C1121 | `MISSING` | `MISSING` | `MISSING` | not executed; no signal sent | none | NOT_RUN |
| 21 | C1122-C1127 | `MISSING` | `MISSING` | `MISSING` | not executed | none | NOT_RUN |
| 22 | C197 | `MISSING` | `MISSING` | `MISSING` | not executed; approval preserved unused | none | NOT_RUN |
| 23 | C1147.01; C1147.02; C1146.23 (ruled Post-first-write/pre-C196 route, disposition SHA-256 65908942 prefix) | `MISSING` | `MISSING` | `MISSING` (literal) | 0; returned parent created | control-transcript.txt | RECORDED |
| 24 | C1144 | `MISSING` | `MISSING` | `MISSING` | route invokes neither C1144 nor C1130 | none | NOT_RUN |
| 25 | C1149.07-C1149.17; C1146.25 (route substitution for C1130) | `MISSING` | `MISSING` | `MISSING` (literal) | 0; eleven copies silent | eleven returned evidence files | RECORDED |
| 26 | C1128 | `MISSING` | `MISSING` | `MISSING` | no run-owned PIDs ever existed | none | NOT_RUN |
| 27 | C1129 | `MISSING` | `MISSING` | `MISSING` | no run-owned PIDs ever existed | none | NOT_RUN |
| 28 | C1131-C1139; C1146.28 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; seven baselines restored, five additions and derivatives removed | control-transcript.txt | RECORDED |
| 29 | C1140-C1141; C1146.29 | `MISSING` | `MISSING` | `MISSING` (literal) | 0; eight hashes emitted; C1141 produced zero bytes (clean) | control-transcript.txt | RECORDED |
| 30 | pre-cut C1150.R; C1151.T; C1148; C1153.01; then C1142; C1143; C1146.30; post-cut C1151.F | `MISSING` | `MISSING` | `MISSING` (literal) | 0; temp root removed and absence proved; C1146.30 was the final CONTROL input | control-transcript.txt; control-transcript-precleanup.txt | RECORDED |
| 31 | C1152 | `MISSING` | `MISSING` | `MISSING` | this completed form; freeze by C1154.03 pending | completed-evidence-return.md | READY_FOR_RAW_RETURN |

Every failed, not-run, missing, or deviated step is explicit above. Allowed
recorded-state values are `RECORDED`, `FAILED`, `NOT_RUN`, `DEVIATION`,
`MISSING`, and for step 31 only `READY_FOR_RAW_RETURN`. Later ingestion derives
all PASS dispositions and the terminal verdict.

## Target and trace evidence

- helper PID / PPID / PGID / executable / launch record hash: `NOT_RUN`
- GUI PID / PPID / executable / launch record hash: `NOT_RUN`
- proof helper is the exact launch direct child immediately before C196: `NOT_RUN`
- GUI contact action/result/time: `NOT_RUN`
- C196 literal expanded command/hash and start time: `NOT_RUN`
- five breakpoint-resolution results: `NOT_RUN`
- first SIGTERM C1121 exact command/hash/time/exit: `NOT_RUN`
- immediate helper-survival result: `NOT_RUN`
- immediate and final socket/owner stat results: `NOT_RUN`
- eight-second bounded observation: `NOT_RUN`
- final helper/GUI process state: `NOT_RUN` (no run-owned process ever launched)
- GUI owner observation (responsive/transport loss/exit): `NOT_RUN`
- exact raw LLDB transcript path/hash: `NOT_RUN` (no LLDB session occurred)
- exact complete through-cut CONTROL transcript path: `returned/control-transcript.txt`
- C1146.01-C1146.30 raw exit-record occurrences in the complete transcript: `exactly fifteen records, once each: STEP-01 through STEP-10, STEP-23, STEP-25, STEP-28, STEP-29, STEP-30; all command_exit=0`
- C1105/C1106/C1107/C1108 complete combined-output files and literal command/tee exit sidecars ready for post-freeze hashing: `returned/c1105.output.txt, c1105.exit.txt (0/0); c1106.output.txt, c1106.exit.txt (0/0); c1107.output.txt, c1107.exit.txt (0/0); c1108.output.txt, c1108.exit.txt (command_exit=1, tee_exit=0)`
- trace events and bounded backtraces: `NOT_RUN`
- C197 ETX/detach/quit time and terminal result: `NOT_RUN`
- 150-second bound result: `NOT_RUN`

Do not infer a Root stop, callback, signal-delivery seam, socket cleanup, or
cause when the corresponding raw event is absent. Unresolved symbols:
`NOT_RUN`.

## Cleanup, rollback, and retention

- graceful/fallback cleanup exact commands and outcomes: `C1128/C1129 NOT_RUN (no PIDs existed). C1131-C1139 executed in order, all silent/exit 0. C1142 removed the exact temp root; C1143 proved absence; C1146.30 recorded exit 0.`
- eight post-rollback baseline/lock hashes: `exact C1140 stdout in control-transcript.txt: cli-launcher.ts 850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b; main.ts 16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f; runtime-control-ipc.ts 5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a; package.json 1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53; package-lock.json 5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56; build-electron.mjs a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558; cli-launcher.test.ts 1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9; runtime-control-ipc.test.ts f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6 — identical to the C1078 baseline values plus the C1091 lock value`
- five candidate additions absent: `removed by C1138; C1141 emitted zero bytes`
- dependency/build derivatives absent: `removed by C1139; C1141 emitted zero bytes`
- frontend Git status exact bytes/hash: `C1141 produced empty output (zero bytes) — frontend clean`
- fixed temporary root absent: `proven by C1143 exit 0 after C1142`
- C1148 owner inspection observations for every copied artifact: `Owner personally inspected all eleven candidate artifacts (c1103.sha256.txt, c1104.electron-builder.runtime-helper.json, c1104.package.json, c1105-c1108 .output.txt and .exit.txt). Supplemented by an agent-side read-only deterministic screen (HELP_HUMAN/Agent 0) over credential-pattern classes and high-entropy strings, reporting counts and masked shapes only, never matched values. All flags resolved to package names (@anthropic-ai/sdk, @earendil-works scope), a script name (proof:secret-scan), globs, and path-shaped strings. No credential-bearing content found. All eleven artifacts cleared for C1149 copy.`
- exact returned primary raw-file paths ready for C1154-C1157 post-freeze hashing, or explicit missing/not-run entries: `completed-evidence-return.md; control-transcript.txt; control-transcript-precleanup.txt; c1103.sha256.txt; c1104.electron-builder.runtime-helper.json; c1104.package.json; c1105.output.txt; c1105.exit.txt; c1106.output.txt; c1106.exit.txt; c1107.output.txt; c1107.exit.txt; c1108.output.txt; c1108.exit.txt. lldb-transcript.txt: NOT_RUN. helper/GUI stdout/stderr/pid files: NOT_RUN (C1155 hashes inapplicable).`
- intentionally retained state and reason: `none — every produced artifact was returned and the temp root was lawfully removed after rollback proof; nothing required retention`

The runbook creates no retained-evidence manifest, range index, completeness
file, PASS disposition, or terminal verdict. Later ingestion derives those
records from immutable returned raw bytes and this observation form. C1154.03
freezes this direct-return form after C1152; it must never be edited afterward.
The form does not and cannot contain its own hash, later hash-sidecar acts, or
actual intake receipt.

## Limitations and attestation

- missing bytes: `no per-command UTC or monotonic clock exists in the CONTROL transcript; exact-input hashes were not separately computed (every literal input is preserved verbatim in control-transcript.txt); C1105 named five test files but matched four existing files (phantom fifth name; erratum dispositioned at SHA-256 f6cbfc084e769a294e082af4103569e29f79d87c87d252ffd7f2d2453b5ba0c7)`
- timing uncertainty: `known anchors only: session login banner Fri Aug 7 20:14:32 local (2026-08-08T02:14:32Z); C1105 vitest "Start at 21:12:58" local (2026-08-08T03:12:58Z); owner attests route completion and form authoring at approximately 2026-08-08T04:31Z. All step rows carry MISSING rather than reconstructed times.`
- operator deviations: `none beyond the owner-ruled route substitutions recorded at disposition SHA-256 prefix 65908942 (Post-first-write/pre-C196 route; C1150.R before C1148 per recorded packet erratum). One earlier command-transcription slip (a stray character) was caught before entry and never executed.`
- credential omissions/redactions: `none required; see C1148 record`
- unsupported inferences expressly not made: `no packaging identity, launch, attach, signal-delivery, teardown, Root-stop, or causal claim is made or implied; the step-10 failure is attributed only to the recorded electron-builder stale-electronDist error; the D-APP-88 first-signal question remains entirely open`
- owner attestation that the recorded inputs/outcomes are literal: `I, Ryan Tufts, attest that the inputs and outcomes recorded above are literal transcriptions from the exported CONTROL transcripts, the returned raw files, and observed filesystem state, not reconstructions from memory. 2026-08-08T04:31Z.`

Execution and a completed template are derivative evidence only. They do not
accept D-APP-88, close DEL-09-04, fire TM-APP-036, establish cause/remedy, or
authorize product/release/reliance action.
