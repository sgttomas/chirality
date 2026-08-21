# WORKING_ITEMS return — WI-PKG02-DAPP86-RERUN-01

Verdict: `BLOCKED / PARTIAL — AGENT 0 ACCEPTED FACTS; N2 HELD; NO RERUN`

Amendments: `CLOSEOUT_AMENDMENT_01` calibrated claims after Agent 0 fan-in;
Amendment 02 repaired terminal status, registered-check,
runtime-summary-binding, and waiver records; Amendment 03 records Agent 0's
Receipt-183 containment disposition; Amendment 04 performs candidate-whitespace
remediation and lossless deterministic-gzip materialization of four raw logs.
No product execution was rerun.

## Coverage and accepted child returns

This instance managed exactly PKG-02 / DEL-02-02. The sealed executor returned
`BLOCKED / PARTIAL`; the fresh evidence-only verifier returned
`ACCEPT_BLOCKED_FAN_IN`, meaning the failure evidence is fit for manager fan-in
but no parity claim is accepted.

- Executor return:
  `instances/A2-PKG02-PARITY-EXECUTOR-01/RETURN.md`, SHA-256
  `408eae1a1e14baafd93228f07222aebe62d78823d7ec18ac8b09c7771aa6904c`.
  Amendment 04 removed only its surplus blank EOF line; claims and outcome are
  unchanged.
- Verifier return:
  `instances/A2-PKG02-PARITY-VERIFIER-01/RETURN.md`, SHA-256
  `8b095ab1c6c2e0bf88cd8c0ecd0afdad38306e8343dc9c90c59c8f9b4d200f21`.
- Closeout-amendment verifier:
  `instances/A2-PKG02-PARITY-AMEND-VERIFIER-02/RETURN.md`, verdict
  `ACCEPT_AMENDED_FAN_IN`, SHA-256
  `aa50ab10e5788914566fc6cd1419644c9734f797b02b68c9b48361e924df431e`.
- Integrated verifier V3 returned `REJECT_REPAIRED_FAN_IN`, SHA-256
  `2ca7810a2a48667ae1f63b4350f300918334edfbc183fb1acb11e5e128bdce87`.
  Its sole blocker was an over-strict Receipt-183 containment criterion; this
  rejected provenance remains preserved.
- Integrated verifier V4 returned `ACCEPT_REPAIRED_FAN_IN_V4`, SHA-256
  `1f0bc86087a86f535276e7467d3feed55755a4953929a2bc42b950ab0f0033d5`,
  under Amendment 03's Agent 0 disposition that the parent-owned receipt is
  excluded from WI attribution and receives no semantic judgment here.
- Final run-local verifier V6 returned `ACCEPT_FINAL_RECORDS_V6`, SHA-256
  `ee22c73c02023352a438cc08000e9c584f2c21f275acafa556e756a1117f808b`.
  It accepted the exact pre-finalization candidate without repair; the manager
  then performed only the authorized V6 status/telemetry/dependent-hash fan-in.
- Six required D-APP-86 outputs exist. The original verifier matched all 12
  pre-amendment index rows; later verifiers matched the then-current corrected
  indexes. V4 independently revalidated 509/509 source and 446/446
  package-manifest rows.

## Product progress and blocker

Focused parity tests passed (6 files / 36 tests), typecheck passed, production
build completed, and a deterministic isolated daemon fixture completed with
two canonical events and one transcript item. These are partial executing-case
results only.

Before the first UI action, packaged GUI startup logged
`desktop.cli_launcher.install {status:"written",path:"/Users/ryan/.local/bin/chirality"}`.
That owner-state write violated the sealed isolation boundary and correctly
stopped execution. Live source exposes `CHIRALITY_SKIP_CLI_LAUNCHER=1` for
verification, and the instrument invocation omitted it; Agent 0 therefore
classified this as an instrument invocation defect. No trustworthy before-state exists. The launcher was not
restored, overwritten, or removed after the stop; its observed post-write
SHA-256 is
`f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`.
Exact run PIDs, listener, socket, and temp root were cleaned up.

Workbench, Pipeline, in-flight selection guard, post-completion selection,
and packaged replay rendering were not observed. Packaged premerge,
release-quality, secret scan, and executor final backcheck were not run. No
deliverable state, lifecycle, memory, or run-record surface was changed.

## Basis discrepancy

The live `desktop:pack` package does not contain the task's asserted distinct
D-APP-88 headless helper `.app`. It still runs the main
`Chirality.app/Contents/MacOS/Chirality` executable with `--runtime-daemon`.
Relative to the accepted 2026-08-03 package, `app.asar` and `Info.plist` differ
and the signal-shutdown binder is present, but the generic main executable hash
is unchanged. This proves a material payload/package change, not the
deliverable Remaining text's `distinct-helper implementation` trigger.
Agent 0 determined that N1 neither satisfies nor establishes that trigger,
held N2, and authorized no rerun on this basis.

The retained package log, losslessly materialized as deterministic gzip, also
ends at the sandboxed DNS failure. Although a
446-file package exists and revalidates, this run has no durable parent-routed
network approval or successful retry transcript. Retry authorization and the
successful package-command provenance are therefore `UNKNOWN`. Package
existence and hashes do not establish either claim.

## Validation and disposition

Manager closeout checks passed: App receipt validator; D-APP-38 corpus status
with no drift; repo self-check exit 0; App hold-integrity PASS with 53/53
contracts clear; practitioner-harness pytest `350 passed`; JSON validation;
and `git diff --check`. The final candidate-root check also runs
`git diff --no-index --check /dev/null <file>` over every run-root file with
zero findings. Four raw validation logs were preserved byte-for-byte as
deterministic gzip; all four gzip and decompressed-content hashes pass.
Existing self-check review/warn findings are unrelated pre-existing repository
findings. Receipt 183 is parent-owned fan-in state and is neither attributed to
WI nor semantically judged in this return.

Run-level registered checks are bound at `REGISTERED_CHECKS.json`, SHA-256
`0578860a8361c875eb1f60006c01fe9c6f1987700941ee1402b613e1fab6e505`,
status `BLOCKED_PARTIAL`. The ledger records the exact HEAD, commands,
outcomes, and proof references; packaged UI is `BLOCKED`, while premerge,
release-quality, and secret scan are `NOT_RUN`. None is represented as PASS.

Runtime telemetry is bound at `RUNTIME_SUMMARY.json`, SHA-256
`09c522bd33a89d78886ef3d8947ab95de50106a028069c33d7b64a7f2535f086`,
status `PASS` for ledger completeness: 27 events,
11 matched sessions, and zero
unmatched sessions. Its closeout calibration remains `BLOCKED / PARTIAL`, no
parity closure, no distinct-helper trigger, no rerun authority, launcher
untouched after the recorded write, and network/package-command provenance
`UNKNOWN`.
The append-only source ledger is `RUNTIME_EVENTS.jsonl`, SHA-256
`25cfb0fa31a0464ea954a35ac76f1508c3aff0b8cb1a4853839fc98c69ddcf25`.
V3, V4, V5, V6, Amendment 04, and Amendment 05 are explicitly recorded as
record-verification or records-remediation sessions, not product execution.

Terminal child-status records:

- E1: `instances/A2-PKG02-PARITY-EXECUTOR-01/STATUS.json`, SHA-256
  `ba5a0bc42b44a699ca081efd429c7bdc271cd9a9f789b22f575a4fb39401f079`,
  outcome `BLOCKED / PARTIAL`.
- V1: `instances/A2-PKG02-PARITY-VERIFIER-01/STATUS.json`, SHA-256
  `67cc2d6bfdff32463239f6c96861a5336c73658064f02c32d24e0168474776d1`,
  outcome `ACCEPT_BLOCKED_FAN_IN`.
- V2: `instances/A2-PKG02-PARITY-AMEND-VERIFIER-02/STATUS.json`, SHA-256
  `bc676972431d44d8ff3e090a760b76099aa74e71e2dfab0e5b442018f48b6832`,
  outcome `ACCEPT_AMENDED_FAN_IN`.
- V3: `instances/A2-PKG02-PARITY-INTEGRATED-VERIFIER-03/STATUS.json`, SHA-256
  `38bf6fd267d7f5d3be229e8db73e3dad5fa4bb87aa000a0c5deac66396d3ecfe`,
  outcome `REJECT_REPAIRED_FAN_IN`; preserved rejected provenance.
- V4: `instances/A2-PKG02-PARITY-INTEGRATED-VERIFIER-04/STATUS.json`, SHA-256
  `79322f0ef6b33cbca6a133d7862a51a59455ed36c1b715e1d4cab7fc2126d713`,
  outcome `ACCEPT_REPAIRED_FAN_IN_V4`.
- V5: `instances/A2-PKG02-PARITY-FINAL-VERIFIER-05/STATUS.json`, SHA-256
  `bebd2aeb89be96bf3c2bb662679896c14ba7e0caa958eb6e4a1a3dfd6eb987e0`,
  outcome `REJECT_FINAL_RECORDS_V5`; its sole blocker was the stale
  packaged-UI proof hash. The rejected return remains preserved at SHA-256
  `54658dbbf634280575132821db1ecdc7a487829c5811c3034c66abcc0a92d19d`.
- V6: `instances/A2-PKG02-PARITY-FINAL-VERIFIER-06/STATUS.json`, SHA-256
  `6bbe6fa72913bea0e89e51a19d53423faee36a02663ca238212860c3ff69d7eb`,
  outcome `ACCEPT_FINAL_RECORDS_V6`; no repair.

Waivers: `none`. No failed, blocked, or unrun required gate is waived.

Derivative status remains evidence-only. No authority, release, distribution,
issuance, professional-reliance, lifecycle, dependency, decision, Task
Management, receipt, completion-log, Git, or foreign-loop effect is claimed.

## Agent 0 disposition and remaining action

Agent 0 accepted the truthful blocked/partial facts, held PKG-08 N2, and
directed no rerun. No parity closure or trigger is established. The launcher
remains untouched after the recorded write. V3's rejection remains preserved;
V4 accepted the corrected records under Amendment 03 without repair. V5 later
rejected solely on one stale packaged-UI proof hash; Agent 0 authorized and the
manager applied that one-field correction while preserving V5 provenance. The
candidate remains `BLOCKED / PARTIAL`; V6 accepted the final run-local records
and no V7 is authorized. Git closeout may be routed to CHANGE only after the
separate Agent 0 integrated review accepts the final post-V6 bytes. No commit,
push, PR, or merge was performed by WORKING_ITEMS.
