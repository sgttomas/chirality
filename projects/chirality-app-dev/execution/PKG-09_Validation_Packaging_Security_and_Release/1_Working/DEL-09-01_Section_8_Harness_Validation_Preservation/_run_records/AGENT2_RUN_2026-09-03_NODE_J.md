# Node J run record — review candidate

This record describes the frozen implementation candidate. Independent review and deliverable closeout are pending; no item is removed or revised by this record alone.

## Identity and authority

- Run: `APPDEV_V3_NODE_J_2026-09-03`
- Executor: bounded ephemeral Agent 2 generalist; provider OpenAI, engine Codex, GPT-5 family (exact model identifier unavailable)
- Owner direction: Ryan Tufts selected slate 3's recommended two-wave sequence; Node J follows merged nodes K and L
- Accepted basis: `ede175910c67b384332324622b17695f69e6a715` (`origin/main`, PR #692 merge)
- Items: DEL-09-01-V3-02, then DEL-09-01-V3-01 revision 2
- Control record: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_J_2026-09-03/`

The original TASK form stopped before project-content writes because the delegated shell did not expose `CHIRALITY_INSTRUCTION_ROOT`; no TASK compliance is claimed. HELP_HUMAN's Brief Amendment V2 changed only the execution form to a bounded ephemeral Agent 2 generalist. Basis, objective, write boundary, checks, no-delegation rule, independent-review gate, and return contract were unchanged.

## Implementation

- Hardened `Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh` and added `section8-process-group-controller.py`. Each daemon/Next tree runs in an isolated POSIX session/process group whose controller remains as an unreaped group leader until the final atomic group signal. The controller keeps its PID/PGID non-reusable across the controlled lifetime; no descendant PID is signal authority.
- Round-3 review proved that a descendant can call `setsid()` and leave that group. The replacement outer supervisor runs the complete proof as one uniquely labelled transient per-user LaunchAgent. That job receives a distinct resource-and-jetsam coalition pair inherited across fork, exec, group changes, and `setsid()`. The inner PGID cleanup remains a graceful first line; authoritative outer cleanup enumerates both coalition IDs and signals every member with `proc_signal_with_audittoken`, which atomically validates PID plus kernel pidversion. Repeated TERM then STOP/KILL sweeps require three consecutive empty scans. No bare PID or command match is signal authority.
- Removed all command-line `pgrep -f` and individual-descendant signalling. Process inspection is diagnostic and tri-state; the Electron process that owns the control socket is identified by `lsof` on that exact socket.
- Moved the occupied-port precondition ahead of the environment record, build, daemon start, and registration. A negative run returned 72, wrote no build/daemon log, and left the foreign listener alive.
- Cleanup now preserves the incoming proof status, accumulates signal/invariant/state/evidence failures, writes `UNKNOWN` rather than inferring zero when process or port inspection fails, and explicitly exits 74 when cleanup fails after a successful proof. The script-written manifest remains the final teardown act.
- Added `section8-coalition-supervisor.py` and extended `test-rerun-section8-cleanup.sh`. The pre-build behavioral test proves that TERM-resistant `setsid()` children, including a forker-created `setsid()` grandchild, survive ordinary bootout and are removed by the coalition sweep; a same-command/same-second foreign process survives; a stale pidversion token returns ESRCH; and required enumeration, unique-ID, coalition, signal, bootstrap, and bootout failures each exit 74 with disposable state removed. GUI spawn remains disabled as defense in depth, not as the containment mechanism. The replacement retained proof from the clean runner passed.

The experimental basis is `/private/tmp/chirality-app-v3-slate3-20260903/reviews/nodeJ/CONTAINMENT_PROTOTYPE_2026-09-04.md`, SHA-256 `6ccc89b1e4e3a7be196b208624f3b8e298c7d62d5f8f43a08885025e4ef4c5e6`. This is a host-pinned evidence helper, not product/runtime containment. It validates private Darwin ABI sizes and behavior before any build or daemon start; any unavailable, ambiguous, or failed observation/launch/signal operation stops or fails cleanup without a PGID-only or bare-PID fallback. Target binaries carrying the private coalition-spawn entitlement are rejected.

## Revision-2 proof

- Application/product snapshot basis: `ede175910c67b384332324622b17695f69e6a715`; exact evaluator/product mapping: `EVALUATOR_BYTES_revision2.tsv`
- Clean runner commits: coalition implementation `8e7abdad286a80865f7e5f4f6fbf9842402e1f36`, then final clean runner head `9dfbb7962cd22b56b1899d10c05c3e97f2a10d2f` after removing the unnecessary launchd `ProcessType=Background` throttle; both precede generated evidence
- Retained run: `Evidence/Node_H_Section8_Preservation_2026-09-03/run-app-ede175910-runner-9dfbb7962-revision2/`
- Invocation: clean runner worktree (`git_status_before=0 dirty paths`), port 51849, `WITH_RELEASE_QUALITY=0`, disposable user-data, mock keychain, live daemon registration, bound Next server, premerge wrapper
- Result: premerge exit 0; stable Section 8 summary `pass`, testCount 8, all accepted rows `pass`; Section 9 report-only status `pass`
- Cleanup: daemon and Next controller-anchored process groups remaining 0; LaunchAgent job bootout and audit-token coalition sweep pass; three consecutive empty coalition scans; control socket absent; port listener count 0; script-created user-data, harness temporary root, and transient LaunchAgent root removed; cleanup failure false
- Per-run manifest: verifies every retained artifact and log
- Current comparison: `COMPARE_RESULT_revision2.txt` exits 0 with `BEHAVIOUR_PROJECTIONS_EQUAL=true` across the revision-2 run and all five retained revision-1 sources
- Current source mapping: `EVALUATOR_BYTES_revision2.tsv` proves all twelve Section 8 evaluator/workflow/package surfaces are unchanged since revision 1 and pins the three expected changed trigger surfaces; `FRONTEND_TRIGGER_PATHS_CHANGED_e59efa483..ede175910.txt` lists those trigger paths
- Superseded generated candidates: `run-superseded-candidate-26a1e43/` (false/dirty provenance) and `run-superseded-candidate-2c42f919/` (PGID-only recursive-cleanup gap), each with `SUPERSEDED.md` and excluded from the current comparison/claim
- External-only diagnostics: the first 9df proof launch failed closed before build because an explicit test PATH omitted `/usr/sbin`; a pre-final-runner 8e7 proof passed but is superseded; two 8e7 release-quality checks exposed an unnecessary launchd background-throttling class through the same Pi/oMLX mock timeout. None is imported or represented as a pass for the final runner.
- Final-runner release-quality check: exact clean head `9dfbb7962`, premerge exit 0, release-quality exit 0, coalition cleanup pass, per-check manifest verified
- Bundle manifest: regenerated in pathname order and verifies every bundle member except itself

## Checks before review freeze

| Check | Result |
|---|---|
| Script `bash -n` | PASS |
| Script `shellcheck -S warning` | PASS |
| Deterministic cleanup hardening proof | PASS — inner PGID fail-closed cases preserved; coalition preflight removed TERM-resistant setsid and forker-created setsid descendants after ordinary bootout; same-command/same-second foreign process survived; stale pidversion returned ESRCH; six injected authority/inspection failures exited 74; process-table and `lsof` failures remained `UNKNOWN`; incoming status 23 preserved; diagnostic manifests verified |
| Occupied-port negative proof | PASS — exit 72 before build/daemon; foreign listener survived |
| Revision-2 daemon-bound premerge | PASS |
| Revision-2 per-run manifest | PASS |
| Revision-2 behavior projection | PASS |
| Bundle manifest | PASS |
| Runtime build | PASS |
| Frontend typecheck | PASS |
| Full frontend Vitest | PASS after host rerun; the sandbox attempt failed only on denied loopback/Unix-socket binds and was not treated as a pass |
| Frontend build | PASS |
| Daemon-bound release-quality | PASS; temporary check run manifest verified and teardown/cleanup passed |
| Registered `harness-self-check` | PASS at unchanged INFO/NOT_APPLICABLE/REVIEW/WARN baseline using the host Python with declared dependencies |
| Registered `app-hold-integrity` | PASS |
| Registered `harness-pytest` | PASS |
| APP-HOLD dispatch preflight | ALLOW |
| DEL-09-01 Scope of Work | PASS |
| Authority corpus | PASS — v20, no drift |
| Receipt validator | PASS |
| `git diff --check` | PASS |
| Strict JSON | PASS |

## Review round 1 disposition (historical; superseded by round 2)

Reviewed freeze: `9dd4b4ed04f5b99f6aa42a34ecd8ad6545e23089`. Review report SHA-256: `0c0372bdb2ade320bf086e808a7d23c053f89bd7285da0a00244db84bfa808b7`. The verbatim report is retained by HELP_HUMAN for filing after review acceptance.

| Finding | Disposition | Exact proof |
|---|---|---|
| J1-F1 — bare-PID reuse and overwritten early Next capture | SUPERSEDED | Round 1's identity-record remediation was implemented and tested, but round 2 correctly found that its same-second identity could collide and its check-to-signal boundary remained unsafe. J2-F1 replaces this design with controller-anchored process groups. |
| J1-F2 — cleanup failure could still exit zero | SUPERSEDED | Round 1's status propagation was implemented, but round 2 correctly found fail-open inspection paths. J2-F2 replaces zero-by-default observations with tri-state, fail-closed inspection. |

## Review round 2 disposition

Reviewed freeze: `26a1e43cd3177bb1fef9eff7ddf02310e413fb89`. Review report SHA-256: `e48e5c6e86698c32d778224a0ff65d813a2b8c05b6672846efb5775dca9a4601`. The verbatim report is retained by HELP_HUMAN for filing after review acceptance.

| Finding | Disposition | Exact proof |
|---|---|---|
| J2-F1 — non-unique identity and signal-boundary race | REMEDIATED | Runner commit `b1f0d71f128e31fb2f0d10b579abf6523bae7d3c` replaces individual-PID signalling with retained controller-anchored POSIX process groups. `CLEANUP_HARDENING_PROOF.txt` records that same-command/same-second foreign processes survived, individual PID signal authority is absent, and a TERM-resistant controlled descendant changed from present to absent across atomic group KILL. |
| J2-F2 — observation failures inferred as clean | REMEDIATED | Required process-table and `lsof` observations are tri-state. The deterministic proof forces each failure class; both exit 74 and record `UNKNOWN`, while an incoming status 23 remains 23. The retained live proof reports group counts and the port at zero only after successful inspection and exits 0 with cleanup failure 0. |
| J2-F3 — false exact-HEAD provenance | REMEDIATED | Two-phase topology: clean runner commit `b1f0d71f128e31fb2f0d10b579abf6523bae7d3c`, then this evidence commit. The accepted run's environment records that runner HEAD and zero dirty paths before execution. `EVALUATOR_BYTES_revision2.tsv` separately maps application/product bytes to basis `ede175910c67b384332324622b17695f69e6a715`. The old generated folder is preserved and explicitly marked never accepted; it is excluded from the current comparator. |

## Review round 3 disposition

Reviewed freeze: `2c42f919aa38546c5a4ad9eb692b450aa5c13d06`. Review report SHA-256: `3b66f126fb9270206b201306ff1bfbbaf56e81543996ffe5ea78affc1555de83`. The verbatim report is retained by HELP_HUMAN for filing after review acceptance.

| Finding | Disposition | Exact proof |
|---|---|---|
| J3-F1 — a `setsid()` descendant escapes the anchored PGID | REMEDIATED; ROUND-4 REVIEW PENDING | The outer supervisor uses a uniquely labelled LaunchAgent coalition inherited by `setsid()` descendants and exact audit-token signals tied to kernel pidversion. The host preflight proved six TERM-resistant setsid descendants survived ordinary bootout, coalition sweep removed all target members with three consecutive empty scans, and a same-command/same-second foreign process survived. A wrong pidversion returned ESRCH. Forced enumeration, flavor-17 unique-ID, flavor-20 coalition, signal, bootstrap, and bootout failures each exited 74 and removed probe state. The retained premerge proof and separate release-quality lifecycle passed from clean runner `9dfbb7962`; each final coalition was empty and each manifest verified. The verified prototype memo SHA-256 is `6ccc89b1e4e3a7be196b208624f3b8e298c7d62d5f8f43a08885025e4ef4c5e6`. Round-4 review remains mandatory. |

The registered-check runner's first attempt used `/usr/bin/python3`, which lacked PyYAML and pytest; those outcomes were not treated as passes. The recorded rerun prepended the existing host Python 3.13 environment and passed all three selected checks. A non-selected direct `instruction-root:integrity` probe against the unpackaged build reported the expected missing packaged instruction bundle and SDK files; packaging was outside this evidence-only tranche, so no package/release act was taken and the result is not represented as a pass or as a selected gate.

## A1 and fences

The execution mutated gitignored/generated paths under `frontend/`. A1 therefore applies: historical R20 remains historical only; any future proof claim requires a newly staged revision and fresh owner execution. No tracked `frontend/`, runtime, evaluator, fixture, workflow, package, or configuration byte changed in this tranche.

This is validation evidence only. It makes no signing, notarization, publication, distribution, lifecycle, G5-acceptance, release-readiness, professional, or certification claim. No credential, token value, or private account material is retained.

## Review state

Round-3 review failed on J3-F1. The coalition/audit-token replacement now has the required two-phase topology: runner/helper/test/control bytes through clean runner `9dfbb7962`, followed by this generated-evidence commit. A fresh round-4 read-only review over 100% of the resulting diff is mandatory. DEL-09-01-V3-02 removal, DEL-09-01-V3-01 revision, `_STATUS.md` History, `MEMORY.md`, review filing, final AgentRuns handoff/checks/manifest, and the loop receipt are all deferred until HELP_HUMAN sends `REVIEW_PASS`.
