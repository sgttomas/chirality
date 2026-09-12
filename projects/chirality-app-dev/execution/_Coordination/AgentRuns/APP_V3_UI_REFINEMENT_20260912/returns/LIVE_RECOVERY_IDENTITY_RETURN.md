# Identity repair author return

Author: `/root/live_reconnect_diagnosis`, Type 2, gpt-6-astra, medium.
Received by HELP_HUMAN on 2026-09-12. Verbatim return follows.

Identity repair complete and source frozen for review. No commit.

- UUID is generated before POST and forwarded through both App request types and the Runtime port.
- Optional `turnId` attachment matching is atomic in Runtime’s registry; omitted IDs preserve legacy behavior.
- Matching starts still awaiting their first frame remain retryable.
- State, replay text, events, and terminal selection are restricted to the submitted identity.
- Unmatched recovery preserves the message, leaves the composer empty, sends once, and reports Outcome unknown.
- Supplier protocol and explicit Stop are unchanged.

Validation:

- Frontend: **123/123 passed**, six affected suites.
- Runtime client/daemon/registry: **40/40 passed**.
- Actual Codex composition identity and service-shutdown assertions passed.
- Combined Runtime run: **49/50**; the previously reported intermittent restart-simulation `STOPPED_DEGRADED` failure remains surfaced.
- Runtime dist rebuilt; `git diff --check` passed.

The 18 changed source/test files are confined to App request/attachment plumbing, ChatPanel, Runtime client/daemon/registry, and their affected tests. Parent coordination files were not edited. Full suites, fresh independent review, and the direct UUID/reload check remain with the parent.
