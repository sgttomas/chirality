# Attachment scope assessment

Status: read-only assessment complete; repair recommended, not implemented.
Basis: current packaged-refinement checkout, APP-HOLD reported revision
266c121bb32f9a22c072e7fb3b3f650b290bcdc6. TASK Type 2, no delegation.
Source references below are relative to projects/chirality-app-dev.

## Disposition

The outside-folder error is an intentional native-picker implementation rule,
with explicit tests, but it is not an essential limit of the existing attachment
architecture. The prior Runtime implementation explicitly supported selecting
outside files and importing their bytes into contained conversation custody.
Retain the agent's existing workspace policy and restore that contained-import
path. Do not merely delete the picker check and pass original outside paths to
the engine, and do not add a second independent importer.

There is also a separate production wiring defect affecting even files already
inside the project: the App-owned composition constructs TurnCoordinator without
its optional attachment resolver. That must be repaired first/in the same batch.

Parent direction after this assessment: source remains frozen while remaining
J07 work completes; parent intends to authorize existing-resolver wiring and
bounded picker import in the final repair batch. This report changes no source,
policy, acceptance state, or library package.

## Observations and evidence calibration

Parent-observed candidate266c native J09:

- Attach files opens a normal macOS picker. Selecting fictional
  visitor-desk-brief.txt outside J09 produces `Attachments must be inside the
  project folder: visitor-desk-brief.txt`.
- A subsequent explicit selection of a 167-byte fictional file inside the folder
  produces an attachment chip. Send creates session
  accebf04-240b-4640-b8f8-19fddf28269b and then displays Runtime Bootstrap Failed
  (SDK_FAILURE). Draft and attachment are restored. No blind retry performed.

These are parent-reported live observations, not UI actions by this assessor.
Source establishes the earlier picker refusal and the later missing-resolver
failure path. It does not establish that the generic SDK_FAILURE label alone
uniquely identifies the internal exception; a focused composition regression
should establish that link without exposing operational logs.

## Current implementation and accepted constraints

1. `frontend/electron/attachment-picker.ts:117–148` canonicalizes selections and
   rejects any file not contained within the selected canonical project root.
   Its module comment expressly calls this fail-closed behavior. The native
   handler checks sender origin, validates the root, and obtains source paths
   from the main-process dialog, not a renderer-supplied source-path list.
   `frontend/src/__tests__/electron/attachment-picker.test.ts` explicitly expects
   rejection of outside files and symlink escapes. This is deliberate behavior,
   not an accidental native-dialog malfunction.
2. `docs/PRD.md:651`, FR-036, promises attachments from the selected working root;
   it does not promise arbitrary outside-file selection. Sections 7.6/8.6,
   `docs/SPEC.md:866`, and `docs/CONTRACT.md:137` K-ATTACH-1 require server-side
   validation, supported extensions, regular readable files, symlink rejection,
   10 MiB/file and 18 MiB/turn limits. These constraints remain relevant.
   K-PATH-2 governs Runtime tool containment; explicit host-side copying of a
   selected input is distinct from giving the agent its source directory.
3. Existing run evidence explicitly records the intended broader custody path:
   `execution/_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/RUN_LOG.md:56`
   says out-of-root sources were accepted by custody copy by design. This is
   historical implementation evidence, not a new authority amendment.
4. `../chirality-runtime/packages/core/src/runtime-attachment-resolver.ts:28`
   already implements that import: canonical absolute nonsymlink source,
   extension/type/readability/byte checks, source identity checks while reading,
   at most eight files, and hashed copies beneath
   `.chirality/attachments/<sessionId>/<sha256>.<extension>`. It validates staging
   directories, preserves original basenames in history, and detects conflicting
   existing staged bytes. Its result points to copied files, not outside sources.
5. `../chirality-runtime/packages/core/src/delegated-engine-adapter.ts:147–179`
   requires attachment content-block paths to remain inside the registered root,
   verifies hash/size, labels document text untrusted, and sends images or staged
   document references through the normal Codex envelope. Do not weaken this gate.
6. The current production composition
   `../chirality-runtime/packages/daemon/src/app-owned-composition.ts:223`
   supplies only four TurnCoordinator constructor arguments. The fifth argument
   is the optional resolver (`core/src/turn-coordinator.ts:92–97`). Nonempty
   attachment requests then throw `Attachment resolver is unavailable`
   (`turn-coordinator.ts:201–218`) before engine execution. The App route already
   forwards attachment paths. A source search found RuntimeAttachmentResolver
   instantiation only in tests, not the current production composition.
7. `../chirality-runtime/tests/codex-attachment-adapter.test.ts:84` has an explicit
   outside-root staging test with text, PDF, image, hashes, contained paths,
   history names, adapter projection, and tamper rejection. This is existing test
   source, not a fresh passing run or proof of current App-owned wiring.

## Smallest sound repair and exact surfaces

- Runtime: import RuntimeAttachmentResolver in
  `packages/daemon/src/app-owned-composition.ts` and inject an instance as the
  fifth TurnCoordinator argument. Reuse the existing implementation. Add a
  production-composition test in `tests/app-owned-composition.test.ts` that sends
  real temporary selected files through the actual service/client path and fake
  stock protocol transport. Cover both in-root and outside-root inputs.
- App: in `frontend/electron/attachment-picker.ts`, admit supported regular files
  explicitly returned by the native dialog outside the active root, while
  retaining sender authorization and root validation. Keep the project as the
  dialog's initial directory. Reject symlink aliases rather than silently
  canonicalizing them into trusted regular-file selections; existing in-root
  alias acceptance also conflicts with the retained symlink requirement.
  Runtime remains the authoritative import/size check on send.
- Update `frontend/src/__tests__/electron/attachment-picker.test.ts` and
  `frontend/src/__tests__/components/chat-panel-native-attachments.test.tsx` for
  explicit outside-file chips, cancellation, negatives, and retry preservation.
  The current IPC request/result shape can remain unchanged: selection returns
  paths; send invokes Runtime custody import. No generic filesystem-access API,
  arbitrary renderer path-copy endpoint, or broader writable root is needed.
- Provide a short pre-send disclosure in the native picker, such as
  "Selected files are copied into this chat's folder when you send." This belongs
  in the dialog options and its local TypeScript shape/tests. Do not claim copying
  already happened when only a chip exists. A separate confirmation is not needed
  for ordinary Attach/Send if the behavior is clearly described.
- Coordinate precise FR-036/attachment documentation clarification with the parent
  if adopted: explicitly selected external sources are accepted via contained
  import; agent access remains under the user's existing sandbox/project policy.
  Do not silently rewrite governed acceptance or treat the historical test as a
  blanket policy waiver.

## Verification and remaining limits

Required targeted verification after authorization: outside text, image and PDF
reach stock protocol inputs through staged copies; source files remain unchanged;
inside-folder attachment still works; unsupported type, symlink, directory,
over-budget input, unsafe staging path and staged-content tampering reject;
multiple selections preserve original names; draft/chips survive failed sends;
folder changes while a picker is open cannot attach a selection to the wrong chat.
Then rerun the two native J09 cases. Existing source includes a mismatch between
fail-fast custody handling and older partial-failure prose; surface it separately
rather than broadening this repair without a disposition.

No tests, supplier processes, builds, live APIs, auth/private-state files or native
UI actions were run by this assessment. Only tracked source, instructions,
acceptance prose and existing test/evidence files were inspected. APP-HOLD-1
reliance preflight for DEL-09-06 at
APP_V3_USER_JOURNEYS_20260912:ATTACHMENT_SCOPE_ASSESSMENT passed ALLOW / CLEAR /
NOT_HELD. Register SHA d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c;
scan SHA 24fec92c47f90aa157a82cf1cba03eabcb63e3f44d524e0213839f47dda019a1.

Handoff: derivative assessment over cited source/records; no authoritative
snapshot accepted or replaced; repair and tests remain unexecuted. Parent owns
repair authorization, exact candidate review, native recheck and closure.
