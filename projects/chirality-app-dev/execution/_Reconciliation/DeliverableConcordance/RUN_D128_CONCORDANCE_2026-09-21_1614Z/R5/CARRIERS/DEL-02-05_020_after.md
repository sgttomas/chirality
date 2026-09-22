### Current responsibility

Provide the App account and runtime-feedback experience, selected-project attachment controls, typed errors, and retry-preserving failure state. Codex owns credentials and the account login/logout methods. Chirality presents its own sign-in state without reading, copying, or relaying credentials; its sign-out must leave other Codex clients unchanged.

The effective Codex home shares the user configuration and resources by reference while keeping authentication and model-cache state private to Chirality. The user selects approval and sandbox policy for each project/turn. Retired hosted admission, root-private account consent, brokerage generations, model residency, and external local-model-server status are not current live-login prerequisites.

The account row and right-panel Settings retain their accepted presentation ownership. Labels and current state must be truthful, with unavailable or fixture state distinguished from verified live login. DEL-09-06 retains attachment, credential-IPC, renderer, and other surviving security verification. Broader role and exact account-indicator conflicts are accounted separately; this repair does not silently decide those rows.

Verification hooks: the production S-8 account check in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md` and `projects/chirality-runtime/tests/app-owned-composition.test.ts`. Native outcomes require their actual recorded evidence.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

