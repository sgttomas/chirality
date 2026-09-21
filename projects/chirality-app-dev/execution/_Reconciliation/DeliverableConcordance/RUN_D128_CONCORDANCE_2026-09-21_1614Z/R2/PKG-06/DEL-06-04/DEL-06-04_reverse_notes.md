# DEL-06-04 reverse-pass notes (pass 2)

- **Capability files answered, in order:**
  - BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS, SHELL, WORKSPACE.
  - 365 rows in total.
- **Responses:** 3 CLAIMED_BY, 12 PARTIAL, 350 NOT_MINE.
- **CLAIMED_BY:**

  | Capability | What it is | Owning claim |
  |---|---|---|
  | CAP-HARNESS-045 | Path containment | CLM-009.2 |
  | CAP-HARNESS-047 | Write hooks | CLM-009.1 |
  | CAP-SETTINGS-026 | Atomic write | CLM-009.11 |

- **PARTIAL.** These are live-path mechanisms that stand in for the legacy hook path, or adjacent owners' surfaces where DEL-06-04 owns one slice:
  - HARNESS-031, 043, 048, 051, 056;
  - RTCONTRACT-019, 042, 044;
  - RTCORE-028, 029, 030;
  - SHELL-025.
- **Validator:** passes once per capability file (8 of 8), with 0 errors and 0 warnings.
- **Errata:** none. No sealed forward row was found wrong, so no errata file was written.
- **Sealed ledger:** unchanged, SHA-256 `b9add1f7f08d6e6738d0a6ea86e82e78692358587b70acb700a42964529f9cd2`.
- **Coverage gaps.** None requires a new forward row. Observations for the manager:
  - **CAP-HARNESS-046 (shell policy).** It also denies instruction-root and symlink redirection for Bash. That part belongs to DEL-06-05, so I answered NOT_MINE.
  - **CAP-WORKSPACE-019 (deliverable path containment for contract routes).** It is the App-owned write-route containment. It belongs to the PKG-07 contract deliverables, so I answered NOT_MINE. DEL-06-04's SoW does not name App-owned write routes. If the owner wants App-owned controlled writes in DEL-06-04's containment scope (REQ-002 "or equivalent gate"), that would be a forward coverage gap.
  - **CAP-RTCORE-033 (application-owned dynamic tools).** It is a future write surface that K-MCP-1 parity would govern if the App ever registers write-capable application tools. At the frozen basis the App registers none, so I answered NOT_MINE.
