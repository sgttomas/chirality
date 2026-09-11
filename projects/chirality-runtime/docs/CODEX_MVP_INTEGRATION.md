# Codex MVP integration

The ordinary Codex session path uses Runtime project registration and session
creation, `TurnCoordinator`, `createDelegatedEngineAdapter`, `DelegatedRuntime`,
and the authenticated supervisor socket. `CodexSupervisor` owns the provider
transport and worker lifetime. The adapter does not launch a supplier directly.

Codex supplies its native file and shell capabilities inside the selected
permission profile, which Codex applies through its own Seatbelt for every file
read and command. The worker supplier launches directly from its verified staged
executable: macOS refuses to apply a second Seatbelt profile inside a process
already running under a profile with any deny rule, so an outer profile around
the worker would break the supplier's own file sandbox. Login and keyring-only
purposes never start a thread and keep the outer profile. Only
Chirality-specific catalog and context tools cross the Runtime callback bridge. Historical tool descriptors
for other adapters do not establish Codex tool availability or enforcement.
Interaction mode (`chat` or `native-plan`) is separate from permission mode and
command-network posture. Unsupported permission combinations must fail before
execution rather than silently select a broader profile.
The current Codex MVP supervisor supports only `workspaceWrite` (Project
access). Saved `ask`, `readOnly`, and `bypass` values are retained but cannot
execute through this composition. Project access does not promise approval for
each write; command-network approval remains independently configured.

Native Plan turns send Codex `collaborationMode` with built-in mode instructions.
Completed native plan items supply authoritative plan text; streamed deltas and
progress checklists do not create accepted plan revisions. The registry binds
capture to the Runtime project, session, accepted turn and live worker generation,
and retains native provider thread and turn provenance with each new revision.
Earlier revisions remain immutable history. Text plans export as readable text;
structured historical values retain a JSON representation.

Clients use the existing session turn API to discuss, revise, or implement a
plan. The following routes inspect native state:

- `GET /v1/projects/:projectId/sessions/:sessionId/native-plan/capability`
- `GET /v1/projects/:projectId/sessions/:sessionId/native-plan/revisions`
- `GET /v1/projects/:projectId/sessions/:sessionId/native-plan/clarifications`
- `POST /v1/projects/:projectId/sessions/:sessionId/native-plan/clarifications/reply`
- `POST /v1/projects/:projectId/sessions/:sessionId/native-plan/export`

A clarification reply contains `requestId` in its JSON body to preserve the
provider's string or numeric identity, plus `answers` mapping each question ID
to `{ "answers": ["..."] }`. Clarifications are separate from permission
approval. Reply bodies are transient provider responses, not ordinary chat
messages or instruction history.

Workflow creation and revision happen through conversation and native file
tools, followed by catalog refresh. Project and user workflows remain available
under source-qualified identities. Ordinary App skill discovery and loading use
trusted bundled roots only. Excluded historical skill selections remain visible
through frozen history but cannot be silently selected for a new turn. Runtime
catalog filtering alone does not prove the provider's automatic skill discovery
policy; exact supplier context and containment checks remain necessary.

Qualification is supplied only by trusted host composition after the applicable
native adapter and admission evidence exists. Configuration flags, source hashes,
controlled transport tests and a compiled addon are not substitutes. The
standalone registry is connected even when qualification is absent and reports
that state explicitly. Current production sign-in and supplier admission guards
remain closed pending their separate qualification work.

Native addon packaging injects an absolute `nativeAddonPath` into the hosted
`codex-authenticated-transport` grouped-supplier path. `loadNativeAdmissionBinding` has no working
directory, module-relative or import-time fallback. The host owns resource
placement and exact addon qualification.

Controlled tests exercise the connecting API and transport behavior. They do not
qualify live login, native filesystem effects, native skill discovery, supplier
identity continuity, packaging, or product release.

## Account bootstrap dependencies

The host entry `startHostedBootstrapRuntimeHost` accepts explicit Runtime storage,
socket, and trusted instruction-root paths before a project or account is bound.
The dedicated bootstrap client has project registration, Runtime read, and
credential-control scopes. Explicit project registration creates a separate
project-scoped client. Token files and their resolver helpers remain server-side;
the public registration result contains only `projectId` and `manifestHash`.

The bootstrap API supports explicit initialization of a selected folder when its
`chirality.project.json` is absent. It creates only the minimal Codex v2 project
manifest and registers it. Existing configuration is never overwritten. Status
reads do not initialize or register projects. Login starts only after explicit
provider-network consent. Its coarse ceremony and admission states distinguish
`signed-in` from `ready`; the latter requires private work admission.

The host must first obtain explicit project registration through
`ProjectRegistry.register`; hosted startup checks `requireAuthorized` and the
canonical root. A project selection is not an account identity.

The production entry `startHostedPrivateBootstrapRuntimeHost` constructs the
private factory and passes it into the ordinary bootstrap host. Its strict
owner-private configuration reader accepts an absent configuration as unbound
setup; an explicitly invalid configuration fails without an admitted fallback.
The Electron host supplies the exact packaged native, instruction and artifact
inventory paths. Development source UI remains available, but source-tree
inventory cannot activate trusted native instruction reads.

Login startup validation and native qualification are separate. The factory
requires an externally accepted account-free D36 purpose record bound to the
exact supplier, policy and artifact identities before starting the nonexecuting
supplier-owned login ceremony. A flag, branded object or compiled addon does
not replace the required observations and acceptance. Credentials remain in
the trusted supplier's custody; Runtime does not transfer tokens to tools.

Work admission uses a fresh candidate's own transport for initialization proof,
private identity snapshot, policy/account checks and authenticated authority.
The first admitted candidate is retained for the first turn; subsequent turns
acquire fresh candidate identity and authority. The shared Supervisor owns this
path. The host admission lease is borrowed by candidates and closes only after
children retire. Supplier Stage A/B alone do not implement or qualify the
remaining positive production producer; the bounded successor source work and
native acceptance remain separate prerequisites.

The private continuity store uses a durable random Runtime handle and local
invalidation epoch. It compares the supplier account/workspace pair privately
only after fresh live authority validation; the handle and epoch are not supplier
identity or generation. Same-pair restart can preserve eligible completed-chat
continuity, while explicit lifecycle fencing advances the epoch.

Normal completed turns release authority and retire transport without revoking
account continuity. Explicit revocation, cancellation, protocol failure or
release failure fences continuity. Project-local sign-out durably fences first,
attempts all local retirement, then uses a fresh same-home supplier actor whose
private principal matches the retained project binding. Unknown supplier or
cleanup outcomes remain failures; this is not global account sign-out or
successor recovery closure.

Controlled public bootstrap tests exercise the real factory, launcher,
Supervisor, session, authority transcript and private continuity store with a
retained first candidate and fresh second candidate. Native I/O, provider peers
and external conformance are controlled; these tests do not establish real
supplier or credential behavior. Provider thread and turn IDs remain conversation
provenance, not account identity. Native Plan qualification and effective
filesystem, network and skill-discovery evidence remain separate requirements.

## Attachment and deployment evidence

Selected documents and images, including explicitly selected files outside the
project, are copied into contained per-session attachment storage. Supplier
inputs use hash-named staged files, never unrestricted outside paths. Small text
is labelled as untrusted document content; PDF and large-text references do not
claim extraction. The retained limits are 10 MiB per file and 18 MiB total.
Connecting source checks cover generated readable, non-writable native staging
permissions. Actual PDF/image handling and native enforcement remain separate
qualification checks.

A bundled host cannot use a repository-layout conformance inventory. Its trusted
deployment composition must bind the actual packaged artifact closure and
external acceptance record. Source-map presence and successful bundling alone
do not establish runtime conformance or supplier admission.

The artifact inventory has two explicit modes: `source-tree` with `sourceRoot`,
and `packaged-resources` with `resourcesRoot` and `manifestPath`. Trusted native
bundle reads require the latter and the exact manifest-covered
`Resources/instruction-root`; admission revalidates its content. Declared
`toolRoot` and `workingRoot` distinguish reviewed bundled tools from the project
working directory without granting access to the entire Runtime private tree.

Native role configuration supplies actual role bodies and supported depth for
HELP_HUMAN, manager and TASK entry. Role declarations remain instruction-asserted.
The retained supplier's fresh-child tool inheritance/lineage and native skill
exclusion gaps require the separately scoped supplier source correction; role
configuration and Runtime catalog filtering do not close those gaps.
