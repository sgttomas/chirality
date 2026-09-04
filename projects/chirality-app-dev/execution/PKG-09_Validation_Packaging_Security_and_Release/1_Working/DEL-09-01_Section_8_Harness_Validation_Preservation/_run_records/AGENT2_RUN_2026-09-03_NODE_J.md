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

- Hardened `Evidence/Node_H_Section8_Preservation_2026-09-03/rerun-section8-local.sh` so teardown carries PID plus start/uid/executable identity for every recursively captured tree member, revalidates identity immediately before each TERM/KILL, and derives KILL targets only from verified post-TERM survivors. Early and teardown-time captures are merged, preserving the bounded set if a child reparents without ever accepting a stale or reused PID.
- Removed all command-line `pgrep -f` matching. Process inspection and cleanup stay inside identity-bound trees; the Electron process that owns the control socket is identified by `lsof` on that exact socket.
- Moved the occupied-port precondition ahead of the environment record, build, daemon start, and registration. A negative run returned 72, wrote no build/daemon log, and left the foreign listener alive.
- Cleanup now preserves the incoming proof status, accumulates signal/invariant/state/evidence failures, writes diagnostics where possible, and explicitly exits 74 when cleanup fails after a successful proof. The script-written manifest remains the final teardown act.
- Added `test-rerun-section8-cleanup.sh` plus its retained `CLEANUP_HARDENING_PROOF.txt`; the exact sourced cleanup helpers reject stale identities, build KILL from verified survivors, merge early/current records, and turn a controlled cleanup failure into exit 74.

## Revision-2 proof

- Retained run: `Evidence/Node_H_Section8_Preservation_2026-09-03/run-head-ede175910-revision2/`
- Invocation: exact accepted-basis worktree, port 51845, `WITH_RELEASE_QUALITY=0`, disposable user-data, mock keychain, live daemon registration, bound Next server, premerge wrapper
- Result: premerge exit 0; stable Section 8 summary `pass`, testCount 8, all accepted rows `pass`; Section 9 report-only status `pass`
- Cleanup: daemon and Next identity-bound process trees remaining 0; recorded root identities not alive; control socket absent; port listener count 0; script-created user-data, harness temporary root, and private registration directory removed; cleanup failure flag 0
- Per-run manifest: verifies every retained artifact and log
- Current comparison: `COMPARE_RESULT_revision2.txt` exits 0 with `BEHAVIOUR_PROJECTIONS_EQUAL=true` across the revision-2 run and all five retained revision-1 sources
- Current source mapping: `EVALUATOR_BYTES_revision2.tsv` proves all twelve Section 8 evaluator/workflow/package surfaces are unchanged since revision 1 and pins the three expected changed trigger surfaces; `FRONTEND_TRIGGER_PATHS_CHANGED_e59efa483..ede175910.txt` lists those trigger paths
- Bundle manifest: regenerated in pathname order, includes all four per-run manifests, and verifies every bundle member except itself

## Checks before review freeze

| Check | Result |
|---|---|
| Script `bash -n` | PASS |
| Script `shellcheck -S warning` | PASS |
| Deterministic cleanup hardening proof | PASS — stale identities not signalled; KILL survivor-only; captures merged; forced cleanup failure exit 74; incoming failure status 23 preserved; diagnostic manifests verified |
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

## Review round 1 disposition

Reviewed freeze: `9dd4b4ed04f5b99f6aa42a34ecd8ad6545e23089`. Review report SHA-256: `0c0372bdb2ade320bf086e808a7d23c053f89bd7285da0a00244db84bfa808b7`. The verbatim report is retained by HELP_HUMAN for filing after review acceptance.

| Finding | Disposition | Exact proof |
|---|---|---|
| J1-F1 — bare-PID reuse and overwritten early Next capture | REMEDIATED | Every record now carries PID plus hashed start/uid/executable identity; identity is re-read immediately before every signal; KILL input is the verified-live post-TERM set; early/current captures merge. `CLEANUP_HARDENING_PROOF.txt` shows `stale_identity_signalled=no`, `kill_targets=identity-verified-survivors-only`, and `early_and_teardown_records=merged`. The rerun retained evidence reports both identity-bound trees at 0 and both root identities dead. |
| J1-F2 — cleanup failure could still exit zero | REMEDIATED | Teardown preserves its incoming status, accumulates signal/invariant/removal/write/manifest failures, and exits 74 when cleanup alone failed. The controlled injected paths report `forced_cleanup_failure_exit=74` and `incoming_failure_status_preserved=23` and verify their diagnostic manifests. The fresh retained live proof exits 0 only with `cleanup_failed=0`, zero processes/listeners, absent socket, and removed disposable state. |

The registered-check runner's first attempt used `/usr/bin/python3`, which lacked PyYAML and pytest; those outcomes were not treated as passes. The recorded rerun prepended the existing host Python 3.13 environment and passed all three selected checks. A non-selected direct `instruction-root:integrity` probe against the unpackaged build reported the expected missing packaged instruction bundle and SDK files; packaging was outside this evidence-only tranche, so no package/release act was taken and the result is not represented as a pass or as a selected gate.

## A1 and fences

The execution mutated gitignored/generated paths under `frontend/`. A1 therefore applies: historical R20 remains historical only; any future proof claim requires a newly staged revision and fresh owner execution. No tracked `frontend/`, runtime, evaluator, fixture, workflow, package, or configuration byte changed in this tranche.

This is validation evidence only. It makes no signing, notarization, publication, distribution, lifecycle, G5-acceptance, release-readiness, professional, or certification claim. No credential, token value, or private account material is retained.

## Review state

Pending fresh round-2 read-only review over 100% of the new frozen diff, with the round-1 disposition above. DEL-09-01-V3-02 removal, DEL-09-01-V3-01 revision, `_STATUS.md` History, `MEMORY.md`, review filing, final AgentRuns handoff/checks/manifest, and the loop receipt are all deferred until HELP_HUMAN sends `REVIEW_PASS`.
