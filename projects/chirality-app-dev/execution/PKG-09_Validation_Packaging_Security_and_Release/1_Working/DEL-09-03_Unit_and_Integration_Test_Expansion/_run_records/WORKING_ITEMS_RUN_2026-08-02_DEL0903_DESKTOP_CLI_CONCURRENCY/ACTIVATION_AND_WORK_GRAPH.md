# DEL-09-03 Desktop/CLI Shared-Daemon Proof — Activation and Work Graph

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY`

InstanceID: `appdev_del0903_shared_daemon_proof`

Manager: `WORKING_ITEMS`

PackageID: `PKG-09`

SelectedDeliverables: `DEL-09-03`

AcceptedBasis: repository `HEAD` `72300e75a688b2ef2d1d0c86865577d7d8d2779c`;
accepted App decomposition v3.2; D-APP-85 executed R6 closeout; C04/C16
current-evidence rows; Root C06 coordination notice.

Objective: add a direct App-owned integration test proving the existing Desktop
compatibility adapter and a generic CLI client use one authenticated runtime
daemon/session boundary against fake oMLX, without changing implementation bytes.

CompletionCriteria:

- Desktop and CLI clients resolve the same daemon/socket identity and address the
  same session.
- A competing turn on that session is rejected as
  `SESSION_TURN_IN_PROGRESS` at the generic runtime boundary.
- A second daemon/runtime owner cannot acquire the live socket.
- Cancellation produces exactly one durable terminal event.
- Distinct sessions can coexist.
- No model-drain or daemon-crash recovery claim is made.
- Focused and full validation passes, and DEL-09-03 state is reconciled only if
  the complete fake-oMLX Desktop/CLI test conjunct is directly proved.

Exclusions: `runtime/**`; Electron/App implementation source; dependency CSVs;
decomposition; lifecycle or Checking Approval; decisions; Task Management;
parity; D-APP-84; the six historical UNKNOWN relations; other packages; shared
loop receipts and completion log; generic runtime semantics; C06 daemon-crash or
model-drain recovery.

## Work graph v1

SelectionAuthority: HELP_HUMAN launch brief under the live App loop.

Posture: `TERMINAL_FAN_OUT_IN` with one serialized Bash-bearing integration
owner.

| Node | Role | Dependencies | Concurrency | Write ownership | Return gate |
|---|---|---|---|---|---|
| A2-DEL0903 | ephemeral Agent 2 generalist | activation accepted | serialized | one App integration test; existing App-owned fake-oMLX fixture only if indispensable; this run directory; DEL-09-03 `_STATUS.md` and `MEMORY.md` | direct five-conjunct proof or evidence-backed blocker; focused/full checks; containment and preservation |

FanInGate: accept only a scope-contained test-only return with executable direct
evidence. If public seams cannot prove the objective, retain the Remaining item
and return a minimal App-owned seam proposal without implementing it.

CrossPackageNotice: C04 reconciliation belongs to HELP_HUMAN/PKG-03 after this
package-local return. C06 remains Root DEL-02-06 work and is not a dependency of
this proof.
