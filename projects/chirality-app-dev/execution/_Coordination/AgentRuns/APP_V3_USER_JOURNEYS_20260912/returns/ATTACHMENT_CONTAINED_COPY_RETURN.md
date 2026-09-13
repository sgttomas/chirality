# Contained native attachment handoff — final author return

Status: source frozen for independent review; focused checks pass. TASK Type 2,
Astra/medium per dispatch, no delegation. This implementation supersedes the
raw-external-path design in ATTACHMENT_REPAIR_RETURN.md and addresses the
ATTACHMENT_SELECTION_TRUST_ASSESSMENT.md finding. Parent accepted this bounded
design before implementation; no additional policy/permission gate introduced.

## Final behavior

The authorized native dialog selects sources. Native main captures canonical
project identity before showing the dialog, then rechecks sender authorization
and the same project identity after it returns. It validates and copies selected
bytes into:

`.chirality/attachment-inputs/<host-random-per-file>/<original-basename>`

Only those contained paths return to the renderer. Different same-basename files
get different host-generated directories. The native disclosure is exactly:
“Selected files are copied into this project folder when attached.”

On Send, Runtime rejects every external raw input against the trusted session
root before reading/resolving any source in the batch. It then reuses the shared
byte validation and atomic-copy primitive to create existing immutable final
session custody. A staged input from another project also fails that boundary.
No receipt system, new API, endpoint, source-folder permission or fake session ID.

The chip and accepted-turn attachment reference now identify the selected
contained copy; its basename remains the original filename. Final custody/history
retain original readable names and hash identities; engine file references point
to final session copies. Edits to the original outside file after Attach cannot
change the selected snapshot. Pending copies survive retry, restart and removal
from the chip list for this MVP; no cleanup behavior was added. Actual native
restart/removal journey execution remains parent-owned.

## Exact changed files in this trust repair

Runtime paths relative to projects/chirality-runtime:

- `packages/core/src/attachment-copy.ts` (new): shared source/byte/budget checks,
  directory identity guards and no-overwrite atomic publishing. Sources and
  existing destinations are lstat-checked as regular nonsymlink files before
  open; descriptor identity is checked against that observation. Existing
  mismatched content is never overwritten.
- `packages/core/src/runtime-attachment-resolver.ts`: external-source batch
  rejection before source access; shared primitives used for contained final
  custody; existing session history/name/hash behavior retained.
- `packages/core/src/index.ts`: exports the shared primitives.
- `tests/attachment-copy.test.ts` (new): forged external batch and cross-project
  source rejection before source open/realpath, symlink rejection, immutable
  existing-copy handling, and real FIFO source/destination no-open checks.
- `tests/app-owned-composition.test.ts`: connecting test calls actual native
  selection handler, passes contained copies through actual App-owned service
  and fake stock protocol transport, checks text/PDF/image projection, readable
  names, changed-original isolation, retry, and unchanged cwd/sandbox policy.
  Negative input fixtures now live inside the project so validation tests reach
  file/type/budget gates rather than stopping at external-source containment.
- `tests/codex-attachment-adapter.test.ts`: prior direct outside-source custody
  fixture corrected to the final contained-source contract. Native external
  selection is covered by the connecting test above.

App paths relative to projects/chirality-app-dev:

- `frontend/electron/attachment-picker.ts`: actual native-selection copy into
  captured project; sender/root revalidation; immediate-copy disclosure; shared
  validation/copy implementation instead of a duplicate importer.
- `frontend/electron/preload.ts`: comment corrected to describe contained copied
  paths; no bridge shape/behavior change.
- `frontend/src/__tests__/electron/attachment-picker.test.ts`: native copy timing,
  readable names, duplicate path and same-basename behavior, source untouched,
  source edit isolation, sender/root replacement, source and destination
  symlinks, regular-file and count/size budgets, cancellation and error handling.
- `frontend/src/__tests__/components/chat-panel-native-attachments.test.tsx`:
  fixtures now model returned contained selection paths, including failed-send
  recovery and stale picker outcomes. The existing native_app_author ChatPanel
  generation/root/draft guard is preserved; no ChatPanel source edit in this
  trust repair.

The App-owned composition's existing resolver injection remains from the earlier
basic repair. Parent owns the accompanying PRD/SPEC clarification.

## Final verification

Runtime:

`npm run build`

PASS — ordinary `tsc -b` emission, explicitly authorized by parent for the new
core export and connecting tests. No App/Electron/package/installer build.

`npm test -- tests/attachment-copy.test.ts tests/app-owned-composition.test.ts tests/codex-attachment-adapter.test.ts`

PASS — 3 files, 24 tests. Includes actual temporary source/copy files, fake Codex
transport, and synthetic FIFOs created by local mkfifo. No supplier execution or
real account/profile/credential access. Negative source-access assertions spy on
open/realpath and prove the external raw-source batch fails before those calls.

App frontend:

`npm test -- src/__tests__/electron/attachment-picker.test.ts src/__tests__/components/chat-panel-native-attachments.test.tsx src/__tests__/api/harness/turn-route-attachments.test.ts src/__tests__/lib/harness-ui-attachments.test.ts`

PASS — 4 files, 22 tests. Count changed because native-picker tests were rewritten
to cover staged-copy behavior instead of obsolete raw-path return cases.

`npm run typecheck`

PASS — renderer and Electron no-emit checks. This ran before the final internal
regular-file pre-open checks; no exported types changed afterward, and Runtime
`tsc -b` plus both focused suites passed on the final source.

## Handoff

Derivative implementation/test evidence, no governed acceptance or release.
APP-HOLD reliance basis remains the preceding passing DEL-09-06 assessment
preflight; no lifecycle or held-contract change. Parent identified special-file
prechecks during source review; those checks are retained and now have a FIFO
regression. No remaining blocking finding identified by this author.

No native actions, protected state, new credential/receipt machinery, Git,
publication, package launch or delegation. Parent owns independent review of the
frozen source, consolidated packaging, and native inside/outside selection,
same-name, retry and history rechecks. Prior failing journeys remain preserved.
