# DEL-06-05 reverse-pass notes (pass 2)

This pass covers 284 capabilities from six capability files: BUILD 41, ELECTRON 35, HARNESS 60, RTCONTRACT 53, RTCORE 50 and SHELL 45.

## Responses

- **CLAIMED_BY, 1 capability:**
  - `CAP-HARNESS-046`, the legacy shell policy, is claimed by `CLM-009.6`.
- **PARTIAL, 9 capabilities.** For each, the part DEL-06-05 owns and the key that covers it:

  | Capability | Part owned by DEL-06-05 | Key |
  |---|---|---|
  | HARNESS-043 | Bash mode gating | CLM-003 |
  | HARNESS-047 | Hook fail-closed for shell actions | CLM-009.12 |
  | HARNESS-048 | Bash output artifacts | CLM-009.8 |
  | HARNESS-032 | Mapping an interrupted Bash result to `tool.failed` | CLM-009.9 |
  | RTCONTRACT-019 | The mapping from App mode to Codex policy | CLM-009.1 |
  | RTCONTRACT-042 | Exposure of the Bash descriptor | CLM-003 |
  | RTCORE-025 | Audit events for commandExecution | CLM-009.11 |
  | RTCORE-030 | Declining a command approval | CLM-009.5 |
  | SHELL-025 | The Permissions selector | CLM-024 |

  The rest of each capability belongs to other owners: DEL-06-01 owns the overlay and the mode and approval UI, and DEL-06-06 owns hooks.
- **NOT_MINE, 274 capabilities.** No BUILD or ELECTRON capability concerns shell governance. The HINTS hits in those areas were false positives on token matches.

## Errata (3 rows)

- **What was wrong.** The sealed ledger described the live default as `ask`/undefined, which maps to `on-request` + `workspace-write`.
- **What the App actually does.** CAP-SHELL-025 led to `chat-panel.tsx:136`: the composer's `DEFAULT_OPERATOR_MODE` is `workspaceWrite`, which maps to `approvalPolicy never` + `workspace-write`. The live default therefore runs Codex shell commands with no approval prompt at all.
- **Correction.** The errata correct the Notes on `CLM-003` and `CLM-009.1`, and add the App path to the ImplementationEvidence of `CLM-009.1`. No Disposition changes; the correction strengthens the AUTHORITY_CONFLICT finding.
- **Census.** The sealed and errata-applied figures are identical: 54 rows with the same Disposition counts (see `DEL-06-05_notes.md` §1). The errata change only the Notes and ImplementationEvidence fields.

## Coverage gaps

None found. Every capability DEL-06-05 plausibly owns maps to an existing forward row.
