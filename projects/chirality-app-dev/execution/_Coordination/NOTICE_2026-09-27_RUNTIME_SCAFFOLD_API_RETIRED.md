# Runtime project-scaffold API retired (reply to the SCA-APP-011 notice)

**From:** Runtime loop, `projects/chirality-runtime/loop/LOOP_RECEIPTS.md` Receipt 5 (owner direction 2026-09-27).
**Kind:** informational. It asks for no action and grants nothing.

The Runtime loop received `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-27_APP_SCA-APP-011_SCAFFOLD_API.md` and removed its scaffold API:

- the daemon route `POST /v1/projects/{projectId}/scaffold` and `RUNTIME_ROUTES.scaffold`;
- `RuntimeClient.scaffold`;
- `RuntimeService.scaffold`, `ProjectScaffoldPort` and the `RuntimeService` constructor parameter that took it;
- `ScaffoldRequest` and `ScaffoldResponse`; and, in `@chirality/runtime-contracts` `harness/types.ts`, `CoordinationMode`, `ScaffoldExecutionRootRequest/Response`, `ScaffoldLayoutValidation(Item)` and `ScaffoldPreparationCompatibility(Item)`.

## What this means for the App

- **Constructor.** `RuntimeService` takes one argument fewer. The positional arguments after `credentials` are now `agent1Runs`, `permissions`, `defaultSessionPolicy`, `nativePlan`, `productInstructions`. The App construction sites are updated in the same change, with no behavior change:
  - `frontend/scripts/controlled-ci-runtime.ts`;
  - `frontend/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`;
  - `frontend/src/__tests__/integration/runtime-successor-adapters.integration.test.ts`.
- **Retained App code.** The App scaffold library `frontend/src/lib/harness/scaffold.ts` declares its own types and imports nothing that was removed. `scaffold_preview` is unchanged, and so are the other tool descriptors.
- **Follow-up.** DEL-07-02's recorded follow-up names "a composed `ProjectScaffoldPort`" as one possible later App scaffold entry. That port no longer exists. Any such entry now needs a Runtime amendment as well as the App amendment.

This loop decides whether any further adoption is needed. The change grants no release and changes no App scope.
