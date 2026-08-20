# Frozen work graph v1

Status: `FROZEN BEFORE DISPATCH`

Selection authority: HELP_HUMAN launch direction and D-APP-97 C1.

Posture: `TERMINAL_FAN_OUT_IN`. Exactly one engineering node is selected. Fresh review is the node's mandatory validation stage, not another engineering target.

1. `A2-DEL0904-PACKAGED-SDK-IMPLEMENT-01` — one bounded `TASK + software-bounded-implementation` child owns the workflow/test/necessary-manifest integration and its truthful pre-CI DEL-09-04 evidence/state update.
2. `A2-DEL0904-PACKAGED-SDK-REVIEW-01` — after the manager freezes the complete diff, one fresh read-only `TASK + software-code-review` child reviews 100% of that diff and its verification evidence.
3. Manager fan-in — validates the returns, evidence, containment, derivative disposition, and CHANGE handoff. Shared loop receipt and completion log remain reserved for Agent 0 fan-in after CI proof.

Edges: `IMPLEMENT-01 -> REVIEW-01 -> manager fan-in`. Any actionable review finding requires serialized bounded remediation and a new fresh review. No concurrent writes exist.

## Write ownership

- Implementer: `.github/workflows/desktop-release-template.yml`; focused workflow tests; narrowly necessary verifier script only if a real defect blocks integration; candidate-range tranche manifest only if required; DEL-09-04 `MEMORY.md`, `_STATUS.md`, and `_run_records/**`; run-local implementer return/status.
- Reviewer: read-only, no write target; the runtime-owned immutable launch/status/return record is the durable record.
- Manager: this run root plus fan-in validation/return/handoff; no shared receipt or completion-log write.

## Check placement

- In-session: focused workflow/verifier tests; YAML parse; every workflow `run:` block Bash syntax; frontend/Electron typecheck; full Vitest if feasible; build only if materially affected; root-workflow candidate-range G4 validation; repo self-check; practitioner pytest; authority corpus status; APP-HOLD scan/register match; receipt validator unchanged; diff hygiene and write containment.
- PR CI: actual unsigned macOS `desktop:dist`, existing verifier execution against staged app resources, the same verifier against the read-only mounted DMG app resources, stable JSON evidence production, DMG/staged/mounted identity/posture checks, and artifact upload. `REQUIRED / PR-CI-OWED` at this initial handoff.
- Host-capability: none is required for Step-0 selection because the authoritative actual package proof surface is the named PR workflow.

## Fan-in gates

1. Both packaged app resource roots are verified with scripted no-live-provider mode.
2. Separate stable parseable JSON summaries are retained and uploaded with the unsigned artifact.
3. Mounted verification occurs before detach and proves read-only-DMG packaged bytes, not a copied or staged substitute.
4. Existing unsigned/no-notarization/no-publication and provider/network/credential fences remain intact.
5. Focused and proportional deterministic checks pass.
6. Fresh read-only review reports `PASS` with no actionable findings over 100% of the frozen diff.
7. DEL-09-04 remains `IN_PROGRESS`; the open R4-P49 Remaining scope stays present until external PR-CI proof passes.

## Escalation points

Any dependency/lockfile, release, signing/notarization/publication, provider/network, credential, runtime contract, additional engineering node, lifecycle/Checking Approval SHA, owner-machine deployment, or foreign-loop need returns to HELP_HUMAN rather than expanding this graph.
