# WORKING_ITEMS brief amendment v2 — shipped Electron integration

Authorized by HELP_HUMAN under the owner's original product-source/test scope after review of the frozen v1 graph. The runtime implementer remains byte-fenced to its original targets and acknowledged that it will not edit Electron.

After `A2-RUNTIME-STOP-IMPLEMENT-01` returns and its runtime bytes freeze, add a serialized node:

- `A2-RUNTIME-STOP-INTEGRATE-01` owns exactly `projects/chirality-app-dev/frontend/electron/main.ts`, one focused test under `projects/chirality-app-dev/frontend/src/__tests__/electron/**`, and its run record under this run root.
- Objective: make the shipped runtime-daemon helper consume the new one-shot signal binder while preserving the existing shutdown funnel and GUI behavior, with no duplicate signal handling or double stop.
- Unavoidable build/type-config edits require escalation before any write.
- Acceptance: the shipped helper path invokes the binder; the prior signal loop is removed or coherently reconciled; a focused test pins the integration; focused frontend test and frontend typecheck pass.

The fresh read-only reviewer moves after this node and covers the complete runtime plus Electron diff and process regression. All original exclusions remain unchanged.
