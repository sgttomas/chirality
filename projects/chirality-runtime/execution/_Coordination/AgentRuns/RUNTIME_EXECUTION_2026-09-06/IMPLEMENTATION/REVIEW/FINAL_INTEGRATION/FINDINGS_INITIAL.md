# Final integration review: initial findings

Reviewer: OpenAI GPT-6, exact model ID unavailable; ephemeral Agent 2, role not mechanically enforced. No delegation. Sources read-only; outputs only REVIEW/FINAL_INTEGRATION. Prior review seals preserved.

Status: repair/backcheck pending. Initial independent offline/fixture/socket suite passed 109 tests across 9 files; these passing cases do not establish absence of the following scheduling/contract defects.

1. Ephemeral thread/start conflicts with cross-process persisted thread/resume after every worker is killed. Persist threads explicitly in the root-private home or disallow resumability claims.
2. Selected role/settings digest is emitted but not bound to journal/previous-thread continuity. The old fixed binding policyDigest allows role changes to reuse a previous thread. Bind effective role/settings or fence resume across recorded role-policy changes.
3. Newly added interrupt turnId and approval requestId interpolate untyped wire fields before validation, reproducing prior TypeError instead of typed rejection.
4. Broker shutdown does not cancel/drain login start or active login in the supervisor. Define/test deliberate supervisor ownership or cancel/drain at broker stop.
5. Interrupt preflight re-runs hosted launch/account checks; auth drift during active work prevents obtaining an admission to stop that work. Permit precisely scoped live-turn interruption without requiring launch qualifications, retaining compatibility/auth/project gates.
6. Separate association publication can race terminal publication: terminal commits without threadDigest, then thread file appears, and all later reads reject a previously committed terminal. Preserve committed terminal authority under this interleaving and test explicitly.

Limits: no live login, account use or model request executed. Exact binary positive offline handshake is parent-reported, not reviewer execution. Containment nested-profile issue remains under parent investigation; no general host prohibition or bypass recommendation is inferred. Approval results deliberately report applied:false and are durable decisions only. Role evidence remains instruction-asserted, not mechanism-proven.
