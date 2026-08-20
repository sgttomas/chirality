# Network Policy Proof Run Summary

- Generated: 2026-08-20T06:56:24.194Z
- Output directory: /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20/Remediation_01/source-network-policy-attempt-2
- Run count: 1
- Provider mode: agentSdk
- Scripted agentSdk subprocess: yes
- Idle window per run: 5 seconds

## Aggregate Verdict

- Overall: FAIL
- Failed runs: 1

## Per-Run Results

| Run | Scenario Completed | Blocked Diagnostics | Probe Payloads | Non-Allowlisted Endpoints | Verdict |
|---|---|---|---|---|---|
| run-01 | yes | 1 | 1 | 1 | FAIL |

## Notes

- CONF-002 (OCSP/CRL carve-out wording) remains unresolved; this summary reports explicit non-allowlisted TCP endpoints and renderer policy diagnostics only.
