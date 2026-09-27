# SCA-APP-011 — Group-3 corrections, basis refresh and disclosed deviations

These are group-3 findings about the accepted group-2 exact text and the
integrated candidate. They follow the method.md rule: reopen only what an
actual change affects. The group-2 bound evidence is not rewritten. That
evidence is the edit data, `PREIMAGE_POSTIMAGE.csv`,
`build_amendment_preview.py` and `Propagation_Plan.md`, all bound in
`checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/ACCEPTED_MANIFEST.csv`.
Each item below is recorded as data in `Evidence/Group3/group3_corrections.py`
and presented for the owner's group-3 act.

## G3C-01 — correction of accepted text (DEL-07-04 Scope of Work)

| Field | Value |
|---|---|
| File | `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-04_Status_Transition_API_and_MCP_Tool/ScopeOfWork.md`, line 24 |
| Accepted edit | E13 (the DEL-07-04 SCA-APP-011 controlling section), `Amendment_Preview.md` line 411 |
| Group-2 candidate SHA-256 | `7300d7f8ec533cbd6facc7dd882c0c06ad822b689f2f926be749c258e547aec9` |
| Corrected candidate SHA-256 | `df03ef53fe679a7e4a4e49f0959c1f49cf8d620afe872da800de55b3385107ba` |

Old text (accepted at group 2):

```text
with each HTTP status expectation restated as the library's `WorkspaceValidationError` code and status.
```

New text (group-3 candidate):

```text
with each HTTP status expectation restated as the thrown workspace error's code and status (`WorkspaceOperationError` for most refusals, `WorkspaceValidationError` for path validation).
```

**Why.** The accepted sentence names the wrong error class. In
`frontend/src/lib/workspace/deliverable-contracts.ts`, 31 throws are
`WorkspaceOperationError` and 4 are `WorkspaceValidationError`. The
operation errors cover the gate, ruling, amendment and dependency-write
refusals, including the symlink writes. The validation errors cover path
validation only. Both classes are defined in `frontend/src/lib/workspace/filesystem.ts`
with `code` and `status`. The ported test
`frontend/src/__tests__/lib/deliverable-contracts.test.ts` accepts either
class (its helper at lines 95–102) and asserts `code` and `status`, for
example `toMatchObject({ status: 400, code: 'UNAUTHORIZED_ACTOR' })`.

**What is reopened.** Only this one sentence of E13. Its substance is
unchanged: the verification hook, the ported cases and the retired
`INVALID_REQUEST` rows all stay as accepted. The same wrong class name appears
in the accepted `Propagation_Plan.md` §4 at line 314. That is the code
specification, not scope text. It is not rewritten; this record supersedes
it for the class name. The code agent's receipt states the correct classes.

**Scan of the other 15 candidate files.** No other candidate file names a
workspace error class; the class name appears only in this line. Every
backticked path and identifier in the 127 accepted edits was also checked
against the integrated code. The paths that no longer exist are all named as
retired. `ProjectScaffoldPort` is Runtime-owned. `scaffoldHarnessExecutionRoot`
is named as retired. The rest resolve.

## G3B-01 — basis refresh (App SPEC)

| Field | Value |
|---|---|
| File | `projects/chirality-app-dev/docs/SPEC.md` |
| Group-2 preimage / candidate | `4c8c9da1…08c2` / `af38a442…94fd` |
| Integrated basis (`origin/main` `4087a4f8c`) preimage | `41ba57b0a8fa76a80add9f203f0be9289547fe122759412dbf8c8dcbd416da05` |
| Group-3 candidate | `5a6fcf1577e4d481ad9d25845ac1a1194241cf5c4a696d7da18f8d05946e017f` |

After the group-2 basis, main merged `3d40c0836` and `387b43972` (Receipt-270,
2026-09-27). They rewrote one App SPEC paragraph on the recorded-register read,
which now resolves the execution root instead of inferring it. That paragraph
lies outside every SCA-APP-011 edit and names no retired route or form. The
other 15 files are byte-identical to their group-2 preimages on the integrated
basis.

The accepted SPEC edits (E68–E74, E110, E111) each still occur exactly once
in the new basis. Applying them to it gives the group-3 candidate byte for byte;
`validate_candidate.py` re-derives this from `git show 4087a4f8c:…`. No
accepted text changes. Only the SPEC preimage and candidate hashes move.

## Finalize path after group-3 acceptance

`build_amendment_preview.py --finalize` (group 2) rechecks every file against
the group-2 candidate hash. It would therefore refuse both files above. Use
instead:

```text
python3 <SCA folder>/Evidence/Group3/group3_corrections.py --finalize --date {date} \
  --group3-decision projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_{date}/DECISION.md
```

It applies the same decision gate: the folder date, the same `--date`, and the
"accepted" heading. It rechecks each file against its expected group-3
candidate hash:
- the group-2 candidate hash for 14 files;
- the refreshed hash for SPEC;
- the corrected hash for DEL-07-04.

Then it applies only E47, from the accepted edit data.

`Evidence/Group3/check_group3_finalize.py` shows this works on a scratch
copy, with 15/15 checks passing:
- `--check` fails on the group-2 state and passes after `--apply`;
- a second `--apply` is refused;
- the group-2 finalize refuses the candidate;
- the group-3 finalize refuses a draft heading, a date mismatch and a wrong
  path;
- it applies E47 only, changing the decomposition and nothing else;
- a rerun is refused;
- the repository tree is unchanged.

## Disclosed deviations from `Propagation_Plan.md` §4 (records only, no text change)

1. **Line numbers.** §4's line numbers are against the group-2 basis. Before
   the port, Receipt-270 changed the route test, and the ported version is the
   current one.
2. **Rebase conflicts.** §4 expected only `exports/chirality-app/export-report.md`
   to conflict. `loop/LOOP_RECEIPTS.md` also conflicted. Receipt-269 now sits
   before Receipt-270 and keeps Parent-Receipt 268, as Receipt-269 records.
3. **`RouteAdapterTestIndex.md`.** Its scaffold rows (lines 24 and 46 at
   basis) were dropped, which is one of the two options §4 allowed.
4. **Dependency register.** `DEL-07-05/Dependencies.csv` row DEP-07-05-025
   still names `/api/working-root/deliverable/dependencies` (three
   occurrences). It belongs to the §8 item 2 `dependency-extract` handoff:
   "no dependency register is written by this amendment".
