# Basic attachment repair return

Status: implemented and focused tests pass; independent review and native recheck
remain with parent. TASK Type 2, Astra/medium per dispatch, no delegation.
Checkout: chirality-ui-refinement-packaged-20260912/chirality.

## Changes

- Runtime `packages/daemon/src/app-owned-composition.ts`: injects the existing
  RuntimeAttachmentResolver into the production TurnCoordinator. No resolver
  implementation, supplier, permission, sandbox or root-access changes.
- Runtime `tests/app-owned-composition.test.ts`: new real-file tests through the
  App-owned service/client composition and fake Codex transport. The positive
  regression failed before wiring (process exit 1) and passes after wiring.
  It exercises inside text and external text/PDF/image selections, contained
  hashed bytes, source preservation, original names in custody history, original
  source references in turn.accepted, and only safe copies/documents in native
  input. It asserts unchanged project cwd/workspace-write policy. The negative
  test rejects source symlinks, directories, unsupported/missing files,
  over-10-MiB files, over-18-MiB batches and over-eight-item lists before stock
  turn dispatch.
- App `frontend/electron/attachment-picker.ts`: permits explicitly selected
  external files from the existing authorized native dialog. Keeps canonical
  root validation, initial project directory, file extension/type validation,
  and whole-selection failure. Rejects noncanonical/symlink aliases and malformed
  source paths rather than turning aliases into trusted selections. Runtime
  remains authoritative for source identity and byte-budget checks on Send.
  Native dialog says: “Selected files are copied into this chat’s folder when
  you send.” No extra confirmation, importer or filesystem endpoint.
- App `frontend/src/__tests__/electron/attachment-picker.test.ts`: updated native
  dialog and external-selection expectations; preserves sender/root/cancel/type
  negatives and adds final/parent symlink and malformed-path cases.
- App `frontend/src/__tests__/components/chat-panel-native-attachments.test.tsx`:
  external original path goes into chip and send payload; known rejected send
  restores draft and chip; pending picker success/cancellation errors/rejections
  cannot contaminate a newly selected root.
- App `frontend/src/components/shell/chat-panel.tsx`: small shared hunk authored
  by native_app_author at parent's direction, not this author. Captures binding
  generation and project/draft identity at picker launch and discards stale
  outcomes, including errors. Updates the old containment comment. The new
  root-switch regression failed before that hunk and passes afterwards.

Original selected paths remain UI/accepted-turn references; original basenames
remain custody history names. Imported hash paths remain engine file inputs.
This intentionally preserves the existing distinct source/custody semantics.
Changing a source after selection is revalidated by Runtime at send time. No
copy is claimed before send and no source folder becomes agent workspace.

## Exact focused checks

From projects/chirality-runtime:

`npm test -- tests/app-owned-composition.test.ts tests/codex-attachment-adapter.test.ts`

PASS: 2 files, 20 tests. Includes existing adapter containment, untrusted-document
projection, outside-source custody, transport-size handling and tamper tests.
Tests use synthetic temporary files and a fake stock protocol transport; they
launch no supplier and read no real account files. Existing Runtime package
outputs provide unchanged dependency code; the new composition test imports
its edited production composition source directly. No build was run.

From projects/chirality-app-dev/frontend:

`npm test -- src/__tests__/electron/attachment-picker.test.ts src/__tests__/components/chat-panel-native-attachments.test.tsx src/__tests__/api/harness/turn-route-attachments.test.ts src/__tests__/lib/harness-ui-attachments.test.ts`

PASS: 4 files, 27 tests.

The first retry test fixture used an ambiguous transport failure and correctly
left the message in history; it was corrected to a typed pre-acceptance HTTP
rejection to test the contracted draft-restoration case. Product handling of
ambiguous turns was not changed.

One initial App npm invocation used the project directory instead of frontend
and exited ENOENT without running tests; the exact successful command above ran
from frontend. No build, packaging, native actions, live API, Git or delegation
performed. Typecheck/full-suite checks remain parent-owned under this brief's
focused-tests-only instruction.

## Basis and handoff

Read current Root/App/TASK instructions plus Runtime entry, loop entry, migration
acceptance, current handoff with D-GOV-43 supersession, PRD authority/PRD and its
D-GOV-43 reading. Owner-directed basic attachment repair is the activation basis;
no lifecycle acceptance or release is claimed. Parent separately updated App
FR-036/SPEC16.1 for this behavior and retained current Codex validation semantics.
APP-HOLD reliance preflight recorded by the preceding assessment: DEL-09-06,
APP_V3_USER_JOURNEYS_20260912:ATTACHMENT_SCOPE_ASSESSMENT, ALLOW/CLEAR/NOT_HELD;
register d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c,
scan 24fec92c47f90aa157a82cf1cba03eabcb63e3f44d524e0213839f47dda019a1.

Derivative implementation/test return; prior assessment and parent-observed J09
failures remain preserved. Closure verdict: bounded source repair complete,
product journey not yet rechecked. Parent owns frozen-candidate independent
review, ordinary integration/type checks, and native J09 inside/outside-file
recheck in the consolidated build. No blocker found within this slice.
