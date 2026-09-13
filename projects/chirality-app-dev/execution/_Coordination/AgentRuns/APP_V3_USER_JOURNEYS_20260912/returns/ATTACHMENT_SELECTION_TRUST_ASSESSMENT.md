# Attachment selection trust assessment

Status: read-only finding after basic repair; no further source changes.
This finding qualifies the earlier ATTACHMENT_REPAIR_RETURN.md no-blocker
statement. Parent and independent reviewer own disposition before freeze.

## Answer

Yes. A forged attachment path submitted by code running in the renderer's
permitted origin can currently cause the App-owned Runtime to copy a readable,
canonical, supported outside file into the project without any native selection.
The request must still reach the authenticated project turn client and pass
file/type/size/custody validation. This is not a claim that an arbitrary remote
website can reach the private Runtime socket, or that any file type is accepted.
It is a gap between authenticated client identity and explicit user selection.

The earlier native picker restriction did not enforce this property at the
Runtime boundary. With the resolver disconnected, attachment requests failed;
connecting it makes this existing raw-path trust assumption reachable in the
current production composition. Keeping the old native picker restriction alone
would not repair a forged turn payload.

## Concrete source chain

Paths are relative to projects/chirality-app-dev.

- `frontend/electron/attachment-picker.ts`, createAttachmentSelectionHandler:
  verifies native IPC sender, validates project root, opens the native dialog,
  validates its returned file paths and returns plain paths. There is no recorded
  selection grant or proof exported to the turn path.
- `frontend/electron/attachment-ipc-contract.ts`: request is `{projectRoot}`;
  successful result is `{cancelled:false, paths:string[]}`. No opaque receipt,
  scoped source handle, staged-only reference or selection identity is carried.
- `frontend/src/app/api/harness/turn/route.ts:13–18`: reads the JSON turn body and
  directly forwards it to the daemon harness port. No native-selection lookup.
- `frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts:314–328`:
  validates the configured project and forwards `request.attachments` unchanged
  through RuntimeClient.turnSession. It supplies the App server's Runtime client
  authority; the renderer need not read the private token itself.
- `../chirality-runtime/packages/daemon/src/runtime-daemon.ts:779–784`:
  authenticates `sessions:write` for the project, reads the turn body and starts
  it through the turn registry. Its bearer authorization (`:819–829`) authenticates
  client/project scope, not a native user file-selection act.
- `../chirality-runtime/packages/core/src/turn-coordinator.ts:201–218`:
  feeds `request.attachments` into the resolver with trusted session/project root.
- `../chirality-runtime/packages/core/src/runtime-attachment-resolver.ts:52–70`:
  accepts normalized absolute, canonical nonsymlink supported readable regular
  files within budgets. It imposes no source containment or grant lookup. The
  containment checks apply to destination custody, not the source. It reads the
  bytes before any stock Codex turn/sandbox executes.
- The newly passing composition regression uses the project client with paths
  directly; it does not open the native picker. This is valid evidence of the
  functional pipeline but cannot establish a user-selection boundary. No forged
  request was sent to the live App for this assessment.

## Authority interpretation and recommendation

The inspected current PRD/SPEC clarification says explicitly selected files;
K-ATTACH-1 treats client metadata as non-authoritative. Historical custody tests
show outside-source copying by design, but none of the inspected instruments
expressly makes every renderer turn-path string a user selection or grants
arbitrary supported host-file import to that renderer. Native sender checks,
CSP and project bearer scope reduce other attack surfaces; they do not establish
selection provenance for this path. Stock Codex's chosen workspace/sandbox policy
also cannot constrain a host-side pre-turn copy.

Recommend a contained selection handoff before landing outside raw-path import.
Reuse RuntimeAttachmentResolver's byte validation/copy logic; avoid a second
importer and do not expand Codex permissions. Concrete acceptable shapes are:

1. Native main, after the actual dialog, registers the selected canonical sources
   through a trusted host-only channel and returns opaque project-bound handles.
   The turn path resolves only those handles for outside sources and rejects
   unsupported/unregistered external strings. Binding and revalidation need to
   survive the existing draft/retry behavior without turning handles into broad
   directory grants.
2. Native main performs a trusted contained import using existing resolver logic
   and returns only contained attachment references, while the ordinary turn
   endpoint refuses outside raw paths. Session/custody timing must be resolved
   explicitly because selection currently precedes session creation.

These are repair options for the existing explicit-selection promise, not new
human approval or governance gates. An extra confirmation dialog is unnecessary.
A renderer-callable “register this arbitrary path” method would reproduce the
same gap. A normal in-root file path may retain its existing root-bounded path
semantics; an outside source needs proof of native selection or an already
contained copy. Do not silently change accepted history to confuse original
source names/paths with imported engine paths.

Focused acceptance for the chosen handoff should prove: forged external raw
paths fail before source read, real native-selected external inputs succeed,
selection cannot cross projects/drafts unexpectedly, changed/replaced source
files are revalidated, and retry/history retain contracted behavior. Existing
source/custody and sandbox tests remain necessary but are not this proof.

No additional implementation, test execution, native UI, live APIs, supplier
process, auth/private-state access or new policy edits occurred during this
read-only follow-up. Parent owns the next bounded scope and reviewer fan-in.
