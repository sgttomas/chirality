# Application-owned dynamic tools

Runtime hosts the Codex conversation and tool-call lifecycle. The application
supplies tool descriptions, argument schemas and handlers. Domain checks,
live workspace state, human review and commits remain with the application.
The initial SWBPIPE consumer is still subject to its owning-loop adoption;
this API does not enable that client or change its acceptance rules.

## Register before the first turn

Use the authenticated owning application client, not an ordinary project client.
After `createSession`, before boot or the first turn, call
`registerApplicationTools(projectId, sessionId, registration)` with:

```ts
{
  applicationId: "swbpipe",
  workspaceId: "workspace-123",
  workspaceGeneration: "generation-456",
  timeoutMs: 30000,
  tools: [{
    type: "function",
    name: "swbpipe_inspect_selection",
    description: "Inspect selected objects in the workspace bound to this conversation.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false }
  }]
}
```

This is an interface example, not an implemented Piping handler. Tools may also
use the pinned Codex namespace form. `deferLoading` is optional. Function
identity is `(namespace, name)`; flat functions have a null namespace. Avoid
reserved Codex names; application prefixes make origin clear. Descriptions and
schemas should explain the operation sufficiently for correct selection.

Stock Codex 0.154.0 accepts `dynamicTools` on `thread/start` only. It does not
accept a replacement catalog on `thread/resume`. Runtime therefore stores an
immutable catalog, including application/workspace identity, beside the session.
A used tool-free conversation or a changed catalog requires a new conversation
in this implementation. Identical registration is idempotent. Schemas and
namespace/function descriptors are retained and supplied without rewriting.

The returned binding has a Runtime-generated `bindingId`, application/workspace
identity, workspace generation, catalog digest and application-selected timeout.
Handlers and binding identities are volatile. After a service restart, the host
must explicitly rebind the same catalog; a persisted catalog alone cannot run
application tools. Renewing a workspace generation is an idle-boundary operation.
A conversation stays bound to its original workspace identity.

## Dispatch and completion

These host-only methods use the existing authenticated Unix socket:

| Client method | Route suffix under `/v1/projects/{P}/sessions/{S}` |
|---|---|
| `registerApplicationTools` | `PUT /application-tools` |
| `applicationTools` | `GET /application-tools` |
| `releaseApplicationTools` | `DELETE /application-tools`, body `{ bindingId }` |
| `listApplicationToolCalls` | `GET /application-tools/calls?bindingId=...` |
| `completeApplicationToolCall` | `POST /application-tools/calls/{invocationId}/result` |

The application observes native tool requests in the existing conversation
stream and retrieves queued calls through the host API. A host may poll this
bounded list while a turn is active; record invocation IDs locally so repeated
observations do not execute a handler twice. A stream notification is not an
application commit. Runtime does not accept executable paths, scripts or
callback URLs through registration.

Every invocation includes the Runtime project/session/turn identity, original
provider thread/turn/call identity, JSON-RPC request ID, and bound application,
workspace and generation. The host routes by registered namespace and tool,
validates arguments against its schema/domain contract, and uses this trusted
connection context rather than model-supplied author claims. Runtime validates
bounded JSON and descriptor shapes; it does not implement full JSON Schema or
Piping semantic validation. It does not modify the user's Codex tool policy or
claim isolation from independently enabled filesystem tools.

Complete with the exact upstream result shape:

```ts
await client.completeApplicationToolCall(projectId, sessionId, call.invocationId, {
  bindingId: binding.bindingId,
  result: {
    success: true,
    contentItems: [{ type: "inputText", text: JSON.stringify(applicationResult) }]
  }
});
```

The pinned protocol also supports `inputImage/imageUrl` and `inputAudio/audioUrl`.
Runtime relays these values; it does not fetch the resources. `success` reports
tool execution, not human acceptance or professional approval. A submit tool
must report "queued" until the application has actually committed the change.

## Stop, stale results and replay

Closing the conversation stream only detaches observation. Explicit Stop,
provider turn/request settlement, handler release, timeout or service shutdown
settles affected calls. Pending/terminal call status is inspectable by the host.
A host must check cancellation and its own original workspace basis immediately
before publishing a change; it must not silently capture a newer basis at queue
time. Runtime cancellation cannot roll back effects already performed by a host.

Identical completion retries are acknowledged while retained, including after
the turn ends. Conflicting results, old bindings and cancelled calls are refused.
Repeated provider requests cannot dispatch another handler execution within the
same supervised turn. The application must also deduplicate its domain operation
using its proposal/request identity and Runtime-supplied caller context: loss of
an acknowledgment after a commit is not proof that nothing happened.

Call records are volatile and retained until the next prepared turn. Codex request
and resolution evidence remains in the normal Runtime conversation history;
replay does not invoke handlers. Applications retain the supplied caller and
workspace context with their own operation receipts when that evidence is needed.
After restart, new bindings do not restore old pending tool execution or authorize
automatic mutation retries. Native descendant routing preserves observed child
identities, but actual stock descendant tool inheritance is not yet qualified.

Transport limits: canonical JSON 256 KiB, depth 32, 16,384 nodes; at most 128
catalog descriptors/functions and 128 result content items; 64-character ASCII
names; bounded identity/description strings; timeout 1 second through 1 hour.
At most 1,024 calls are retained per turn rather than evicted and redispatched.
Applications should keep reads/results bounded and return references or explicit
continuation operations for larger work.

## SWBPIPE first consumer

The proposed tools are inspect selection, preview operations, submit proposal
and get proposal status. Piping owns their final names, schemas and handlers.
There is no agent-facing Apply in the initial journey. The human's Apply action
uses Piping's workspace controller, including validation, history, undo/redo and
analysis invalidation.

An inspection basis must include workspace generation, project/workspace identity,
revision AND canonical model hash. Selection identifies explicit objects; later
selection must not retarget a proposal. Validate before queueing and at acceptance.
Test stale-before-arrival, stale-after-preview, undo to identical content with a
new revision, project switch, duplicate delivery and delayed completion. Runtime
tool permission and Piping model acceptance remain different decisions.

Application-specific skills can explain tool use and interpretation. Workflows
can organize reusable multi-step work. They use existing instruction discovery;
loading them grants no additional tool capability or acceptance authority. Prove
the initial ad hoc journey before expanding the reusable workflow library.

## Verification boundary

Controlled composition tests exercise the actual Runtime client, socket, session
store, registry and supervisor with a fake Codex transport. An offline stock
0.154.0 probe accepted a function descriptor on thread/start under denied network
access. A zero-turn thread could not resume because no rollout existed. No live
model turn, native descendant inheritance, or SWBPIPE mutation is established by
those checks. Those production-path witnesses belong to consumer integration.
