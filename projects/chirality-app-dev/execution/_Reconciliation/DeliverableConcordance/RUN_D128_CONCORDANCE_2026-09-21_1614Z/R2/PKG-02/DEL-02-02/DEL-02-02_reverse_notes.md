# DEL-02-02 — reverse-pass notes

- **Input:** `REVERSE_INPUT_capabilities.csv`, 402 rows from 9 areas: BUILD, ELECTRON, HARNESS,
  ROUTES, RTCONTRACT, SETTINGS, SHELL, WORKSPACE, WOVEN.
- **Responses:** 13 CLAIMED_BY, 21 PARTIAL, 368 NOT_MINE.
- **Sealed ledger:** unchanged, SHA-256 `f7121ede…6bd98af`.
- **Errata:** none. No capability contradicts a sealed forward row.

## How ownership was assigned

- **CLAIMED_BY or PARTIAL** where the capability is DEL-02-02 presentation:
  - the Who is working / Agents view, recorded hierarchy and Work projection (SEC-3, SEC-4);
  - the Workflows view parts (REM-3);
  - the retired Workbench/Pipeline forms and helpers (CLM-003, CLM-010.x, CLM-014.1);
  - the matrix replacement (CLM-010.2).
- **PARTIAL instead of CLAIMED_BY** where the applied row names another semantic owner: DEL-08-02
  (routing and guarded selection), DEL-08-03 (dispatch), DEL-07-03 (the workflow file contract),
  DEL-02-03 (the view switcher) and DEL-05-04 (replay). PARTIAL is also used where the seating is
  contested: role entry and posture labels (SHELL-036, SETTINGS-017/018).
- **Capabilities on the retired Workbench/Pipeline surfaces** (WORKSPACE-025..034, SHELL-001/002,
  ROUTES-043) are claimed by the sealed rows marked RETIRED_BY_RULING. Their code stays in the
  deliverable's scope as retained history.

## Coverage gaps (for R3)

These are live right-panel or Workflows behaviours with no DEL-02-02 forward row that owns them. No
errata are possible for them.

1. **Plan tab** (CAP-WOVEN-028, CAP-SHELL-030). It is a live right-panel view, but it is not in the
   applied row L308 or in any DEL-02-02 unit. Its owner is unclear; candidates are DEL-02-03 (views)
   and the native plan owner.
2. **Recorded session panel menu** (CAP-WOVEN-029): Open parent chat, copy the session id and
   metadata. It is coordination presentation over recorded parentage, so it is plausibly Who is
   working scope, but no unit specifies it.
3. **Workflow selection in the composer** (CAP-SHELL-028): method chips and "open Workflows panel".
   This is where the live Workflows view actually leads the user. No DEL-02-02 unit covers it.
4. **Skills browsing** (CAP-WOVEN-031). The live Workflows view now redirects it to workflows. It
   appears in no deliverable unit here.
5. **Mode-scoped Navigator groups by surface** (CAP-WOVEN-039: dialogue/workbench/pipeline
   attribution). The retired surfaces still carry this persisted attribution. It is outside
   DEL-02-02's units, but it relates to the REMTXT-1 "All sessions (N)" history.

## Observation

CAP-ROUTES-042 describes the `/pipeline` and `/workbench` routes as "opening a named Woven surface".
At `00115c719` the shell ignores `defaultSurface` and always renders `data-woven-surface="dialogue"`
(`woven-dialogue-shell.tsx:822`). CAP-WOVEN-001 states this correctly. This affects the ROUTES
capability file only; it is not an error in this ledger.
