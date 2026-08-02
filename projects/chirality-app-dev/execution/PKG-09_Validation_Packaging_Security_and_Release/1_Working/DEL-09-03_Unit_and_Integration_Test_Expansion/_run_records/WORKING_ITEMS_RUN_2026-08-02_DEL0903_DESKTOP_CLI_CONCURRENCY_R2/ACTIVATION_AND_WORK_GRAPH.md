# DEL-09-03 Desktop/CLI Shared-Daemon Proof — R2 Activation and Work Graph

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY_R2`

InstanceID: `appdev_del0903_shared_daemon_proof_r2`

Manager: `WORKING_ITEMS`

PackageID: `PKG-09`

SelectedDeliverables: `DEL-09-03`

AcceptedBasis: repository `HEAD` `72300e75a688b2ef2d1d0c86865577d7d8d2779c`;
accepted App decomposition v3.2; D-APP-85 executed R6 closeout; C04/C16
current-evidence rows; prior run process records and its blocked manager return.

Objective: execute one fresh implementation-first test-only retry that directly
proves the existing Desktop compatibility adapter and a generic CLI client use
one authenticated runtime daemon/session boundary against fake oMLX, without
changing implementation bytes.

CompletionCriteria:

- Milestone 1 first produces a compileable smallest test at the frozen target,
  starts one `RuntimeDaemon`, registers `chirality-app-dev`, creates two
  authenticated `RuntimeClient` instances over the same socket/project
  credential, wraps one in `RuntimeDaemonHarnessPort`, and proves shared daemon,
  project, and session visibility with a focused Vitest result.
- Later small patches use established runtime and App fake-oMLX patterns to
  prove same-session `SESSION_TURN_IN_PROGRESS`, second-owner rejection,
  Desktop cancellation with exactly one replayed terminal, and distinct-session
  coexistence through the real `PiAgentEngineAdapter` against fake oMLX.
- Full registered validation and preservation checks pass.
- DEL-09-03 state/records change only after every required conjunct passes.

Exclusions: `runtime/**` writes; Electron/App implementation source;
dependency CSVs; decomposition; lifecycle or Checking Approval; decisions;
Task Management; parity; D-APP-84; the six historical UNKNOWN relations; other
packages; shared loop receipts and completion log; generic runtime semantics;
C06 daemon-crash or model-drain recovery.

## Work graph v1

SelectionAuthority: HELP_HUMAN launch brief authorizing one fresh serialized
implementation-first retry.

Posture: `TERMINAL_FAN_OUT_IN` with one serialized Bash-bearing integration
owner and a mandatory supervised milestone before refinement.

| Node | Role | Dependencies | Concurrency | Write ownership | Return gate |
|---|---|---|---|---|---|
| A2-DEL0903-R2 | ephemeral Agent 2 generalist | activation accepted | serialized | frozen App integration test; App fake-oMLX fixture only if indispensable; this R2 run directory; DEL-09-03 `_STATUS.md` and `MEMORY.md` only after complete proof | Milestone 1 compile/focused result, then direct five-conjunct proof or exact evidence-backed blocker; full checks; containment and preservation |

MilestoneGate: after writing the smallest compileable test, the child must run
focused Vitest and report the result to WORKING_ITEMS before adding complexity.
WORKING_ITEMS will accept the milestone, relay a bounded correction, or stop.

FanInGate: accept only a scope-contained test-only return with executable direct
evidence. If an existing seam makes a conjunct impossible, retain the Remaining
item and return exact compiler/runtime evidence without speculative source work.

CrossPackageNotice: C04/C16 reconciliation belongs to HELP_HUMAN after this
package-local return. C06 remains Root DEL-02-06 work, is excluded, and is not a
dependency of this proof.
