# Chirality v3 integrated acceptance matrix

Status is evidence based as of the Root V2 catalog freeze. `PASS` means the
named owner has supplied a controlled offline check. `PENDING` preserves work
owned by another lane or supplier; it is not inferred from this Root candidate.

| Acceptance statement | Owner | Evidence or current result | Status |
|---|---|---|---|
| Exactly four registered roles, three direct-entry choices, HELP_HUMAN default | Root catalog; Runtime; App UI | `agents/registry.json`; Root catalog tests and agent validator pass. Runtime and App integrated projection remains separately owned. | ROOT PASS; INTEGRATED PENDING |
| Context contains active role and selected material, excluding other roles and unselected bodies | Runtime; App backend (`app_redesign_plan`) | Root doctrine and `docs/AGENT_WORKFLOW_RUNTIME.md` define the contract. Runtime selective-context tests and App proxy/replay evidence are owned by sibling managers. | ROOT CONTRACT PASS; PRODUCT PENDING |
| Project/user/bundled discovery, collisions, malformed packages, containment, legacy aliases | Root catalog; Runtime | Shared discovery fixture; generated index 79 methods; Root focused tests 136 pass; Runtime catalog suite reported 8 pass. | OFFLINE PASS |
| HELP_HUMAN can select a manager-compatible workflow and coordinate without silent role replacement | Runtime; App backend | Root contract distinguishes selection, compatibility, coordination, and execution. Runtime/App end-to-end evidence remains sibling-owned. | ROOT CONTRACT PASS; PRODUCT PENDING |
| Human or agent method invocation, combinations, stop/change, intact history | Runtime; App backend/UI | Ordered references, safe-boundary replacement, basis history, and provider continuation are defined in Root. Product behavior and replay remain sibling-owned. | ROOT CONTRACT PASS; PRODUCT PENDING |
| Ordinary attachments cannot masquerade as selected method instructions | Runtime; App backend/UI | Root separates method references and attachments. Concrete API/UI negative test remains sibling-owned. | PRODUCT PENDING |
| Native Plan, permission posture, revisions, unsupported handling, restart, replay stay distinct | Runtime adapters; App backend/UI; supplier qualification | Root defines separate `interactionMode` and `permissionMode`, typed unsupported handling, same-conversation revision history, and explicit export. Offline adapter tests are sibling-owned; supplier evidence remains required. | ROOT CONTRACT PASS; OFFLINE PRODUCT PENDING; NATIVE QUALIFICATION PENDING |
| Grouped checkpoints retain acceptance, independent checks, and affected-decision reopening | Root governance/workflows | Decomposition Standard and four affected workflow contracts use the approved groups; author suite passes; independent Root full-diff review is active. | AUTHOR PASS; REVIEW PENDING |
| Attachments, file navigation, PDF fallback, concise attribution regressions | App UI | App tests and integrated verification are separately owned by `/root/app_adoption`. | APP PENDING |
| Packaged instructions match registry, methods, resources, compatibility | Distribution; Runtime; Root catalog | Root V2 freeze binds 15 metadata/policy inputs; public catalog is 78 methods and excludes only project-specific `chirality-change`. Distribution exact staging/manifests remain owned by `/root/distribution_adoption`. | ROOT INPUT PASS; DISTRIBUTION PENDING |

The remaining program milestones are still a qualified App for owner trial,
the final system-prompt discussion, and explicit publishing approval. Offline
mocks do not qualify a native supplier feature.
