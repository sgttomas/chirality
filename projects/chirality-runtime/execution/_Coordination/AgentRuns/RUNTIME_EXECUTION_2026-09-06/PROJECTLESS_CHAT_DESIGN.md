# D120 B1 — bounded projectless-chat design assessment

Status: DECISION_SUPPORT_ONLY. Nothing selected or implemented. Incoming App coordination from task 01a07329-a74d-7170-b896-d474916d868b requested this assessment under owner-selected D120 B1. Current Runtime implementation does not gain projectless scope from that routing request.

## Verified basis and ownership

Read the exact public D-APP-120 ruling at commit c34bca30c57ef0f36de25d8065b8c1944431d48c, projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-120_RULING_PRESENTATION_SEAM_AND_NO_FOLDER_ROUTING_2026-09-06.md. It retains disabled composer/send without a folder and explicitly approves no new schema, endpoint, default root, registration mode or filesystem permission.

At current implementation base 92ca3f1a639cda4dcb7544f1f59dfc78d7acf377, RuntimeSessionRecord and CreateSessionRequest in packages/contracts/src/session.ts require projectId; records also carry projectRoot. RuntimeService.createSession calls projects.requireAuthorized. RegisteredProject and AuthRegistry scopes bind clients to registered canonical roots. Migration acceptance assigns generic runtime contracts to Runtime and shared boundary governance to Root. Therefore removing a UI guard or making projectId optional alone does not produce projectless chat.

## Options

1. Keep the restriction. This is the currently authorized behavior, with truthful explanation. No new Runtime work is required.
2. Add an explicit text-only projectless conversation principal. Recommended candidate for a first bounded feature. The daemon remains the broker. An explicit context discriminant distinguishes project-bound sessions from projectless conversations; no hidden project registration, default root, cwd inheritance or filesystem authority is created. Initial projectless capabilities exclude filesystem, shell, tools, project instructions, governed agents and delegation. Private transcript/account storage is operational data, not a project working root. Account/provider consent and conversation/client authorization require their own explicit scope key rather than borrowing the most recent project's root consent. A technical empty scratch cwd, if the provider requires one, grants no project access and must be contained with tools disabled by an actual mechanism. Provider feasibility must be proved before acceptance.
3. Add tool-capable projectless sessions. This needs an explicit resource-capability and instruction-context model, account/consent principal, attachment permissions, tool/process/network enforcement and later folder-attachment semantics. It is a materially larger policy/product amendment; do not fold it into the first text-only feature.

## Proposed boundary contract for option 2

Use a new versioned discriminated session context, conceptually project(projectId) or projectless(conversationId), not a nullable root on legacy routes. Exact public names/endpoints remain design candidates. Keep existing project routes fail-closed and isolate projectless authorization/storage. Emit the chosen context and capabilities to the App so it can explain the actual state. Do not load Root or the last project as an invisible instruction/work root.

Folder attachment is a separate explicit transition. Prefer creating a new project-bound session after registration/consent and offering selected transcript import as context, with provenance; never silently broaden an existing conversation's authority or replay earlier actions. History import does not import approval, credentials, role authority or write scope. Retention/deletion and account switching need explicit behavior and tests.

## Required acceptance steps

1. Owner selects the intended capability envelope (retain restriction, text-only candidate, or larger tool-capable design). This record supplies no selection.
2. Runtime SCOPE_CHANGE assesses and prepares exact contract/PRD/decomposition changes, compatibility identity impact, consent principal and storage/lifecycle changes. Root decides any required D-GOV-20/shared-boundary amendment; Runtime cannot amend shared instructions or Root governance by implication.
3. Review the exact versioned API, capability/permission contract, account separation, folder-attachment behavior, migration/backward compatibility and conformance matrix. Existing runtime migration and implementation grants do not accept this new feature.
4. After the owning acceptance, Runtime implements and demonstrates no implicit registration/root/credential leakage, no project tool or file access, cross-context denial, account change invalidation, explicit attachment and unchanged project-session regression behavior. The actual provider must support the promised text-only mechanism; a UI label or prompt is not enforcement.
5. Route the accepted versioned contract and actual Runtime conformance evidence to App. App adopts through its own scope/implementation/testing and owner acceptance. Until then D120 B1's unavailable composer/send remains the correct behavior.

Root governance and Runtime product decisions remain separately owned. This is a derivative design assessment, not an authoritative scope snapshot, accepted API, implementation grant or release. No sibling or Root file was edited. Prepared by /root HELP_HUMAN, OpenAI GPT-6; exact serving model ID unavailable; Agent0 role not mechanically enforced.
