# WI-PKG06 Terminal Return — PKG-06 Ownership and Timeout Repairs

- **Outcome:** ACCEPT for HELP_HUMAN fan-in
- **Role:** WORKING_ITEMS
- **Package:** PKG-06 only; DEL-06-01 through DEL-06-05
- **Basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`
- **Authority:** D-APP-68 chronology items 3 and 6
- **Manifest slice:** 20 exact paths; SHA-256
  `d52e897a3944e3cdeb95bce0279a1da2338384fe22108551bd096643845264ab`
- **Execution posture:** serialized direct package integration; no Agent 2 was
  used because the five ownership notes and timeout reconciliation form one
  tightly coupled mapping with one SOW integration owner.

## Coverage and accepted outputs

All 20 manifest paths are present and changed exactly once in the WI-PKG06
slice. Each deliverable received `ScopeOfWork.md`, `MEMORY.md`, one `_STATUS.md`
History append, and one new run record:

1. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/ScopeOfWork.md`
2. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/MEMORY.md`
3. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/_STATUS.md`
4. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
5. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/ScopeOfWork.md`
6. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/MEMORY.md`
7. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_STATUS.md`
8. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
9. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/ScopeOfWork.md`
10. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/MEMORY.md`
11. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_STATUS.md`
12. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
13. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/ScopeOfWork.md`
14. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/MEMORY.md`
15. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_STATUS.md`
16. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`
17. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/ScopeOfWork.md`
18. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/MEMORY.md`
19. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/_STATUS.md`
20. `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy/_run_records/TASK_RUN_2026-07-19_DAPP68_managed_orchestration_mapping.md`

There were no Agent 2 returns to fan in. The package manager validated the
integrated slice directly.

## Ruling and claim disposition

| Deliverable | D-APP-68 mapping applied | Boundary preserved |
|---|---|---|
| DEL-06-01 | `coordination` descriptor permission class and `harness-permission.v7.coordination-mode`; hard deny outside `workspaceWrite` | Descriptor, MCP composition, path, Bash, and child-record owners unchanged |
| DEL-06-02 | Four coordination descriptors, canonical/allowed names, aliases, schemas, catalog entries, and registry validation | DEL-06-03 retains in-process MCP composition |
| DEL-06-03 | Co-location/composition of the four coordination tools on the in-process Chirality MCP server | Legacy read-tool slice not expanded; DEL-06-02 retains descriptors/catalog |
| DEL-06-04 | Managed-child declared read/write path enforcement with project-root containment and symlink-safe denial | DEL-06-05 retains arbitrary-Bash full-root gate |
| DEL-06-05 | Managed-child Bash requires full project-root read and write scope and remains serialized | Bounded file path policy remains DEL-06-04 |
| DEL-06-05 | Default `120000` ms and maximum `600000` ms ratified | Unrelated TBDs preserved |

The stale live timeout assertions were repaired in five places: Conditions,
Documentation, Procedure Prerequisites, Procedure Records, and Guidance. The
dated resolved conflict row remains history and now records D-APP-68
reaffirmation. No runtime behavior changed.

## Validation

- Five `chirality-deliverable-sow/v1` validations: PASS.
- Mapping content: PASS, 5/5 owners.
- Mapping uniqueness: PASS, 5/5 primary surfaces occur under one owner.
- Coordination roster: PASS, 4/4 canonical and SDK-facing names.
- Numeric timeout stale-assertion search: PASS; `120000`/`600000` values present.
- Runtime citation existence: PASS, 10/10 paths.
- Manifest containment: PASS, 20/20 exact paths; frozen slice hash reproduced.
- `_STATUS.md`: only one History line appended per deliverable; all remain
  `IN_PROGRESS`; Approval SHA and Remaining content unchanged.
- D-APP-38 authority corpus: v9, no drift.
- App-dev receipt validator: VALID.
- Whitespace/newline and `git diff --check`: PASS.

No frontend test suite was required because the authorized work is documentary
and frontend runtime source was excluded and unchanged.

## Exclusions, derivative disposition, and blockers

No other package, frontend runtime, shared decision/register, dependency,
decomposition, receipt, completion-log, lifecycle, Approval-SHA, or hard-fence
surface was edited by WI-PKG06. The accepted R1B manifest was consumed as a
derivative execution map and was not modified. Deliverable SOW/Memory/History
updates are current package truth; the new run records and this return are run
evidence. No runtime telemetry ledger was required for this bounded,
non-delegated documentary integration.

Notices: none. Waivers: none. Reruns required: none. Blockers: none.

## Requested Agent 0 action

Accept WI-PKG06 and release its dependency edge for V1 after the remaining
package-manager returns are accepted.
