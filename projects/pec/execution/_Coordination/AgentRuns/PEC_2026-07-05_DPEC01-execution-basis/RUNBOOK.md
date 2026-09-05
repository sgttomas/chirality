# D-PEC-01 Evidence Runbook - Template

> **Epistemic status:** derivative runbook template, not authority. Do not run
> this workflow until the owner supplies the execution basis listed in
> `OWNER_INPUTS.md`. The governing authority is D-PEC-01 O-A plus that supplied
> basis.

## Preconditions

Before any command is run, verify all of the following:

- PR containing this runbook has merged to `main`; work starts from a clean
  branch off the then-current `origin/main`.
- `OWNER_INPUTS.md` has concrete owner-supplied values for the in-scope files,
  actor/visibility basis, scratch DB paths, backup paths, and capture limits.
- No value is `TBD`.
- Real input files may be hashed with SHA-256; raw real file content must not
  be copied into the repo unless the owner explicitly permits that exact
  artifact class.
- `force=true` is not used.
- Every `PEC_DB` path is scratch/restoration-target only, never
  `projects/pec/pec.db`.

## Setup

1. Create a new immutable evidence directory under `_DomainEngines/pec/`, for
   example `PEC_YYYY-MM-DD_DPEC01-pilot-evidence-01/`.
2. Copy `MANIFEST_TEMPLATE.md` into that directory as `MANIFEST.md`.
3. Fill the owner-supplied basis section before running commands.
4. Create local scratch directories outside the repo or under an owner-approved
   scratch location.

## Hash Inputs

Record SHA-256 hashes for every real input file named by the owner. Do not copy
the input files into the evidence directory unless separately permitted.

Example command shape:

```sh
shasum -a 256 "$MDL_PATH" "$RAIL_PATH" "$DECISIONS_PATH" "$RISKS_PATH"
```

Only include paths, filenames, hashes, byte sizes if permitted, and owner
visibility basis in the manifest.

## Import Rehearsal

The expected command shape is PEC's pilot drill against owner-supplied files and
a scratch database:

```sh
PEC_DB="$SCRATCH_PEC_DB" \
node --disable-warning=ExperimentalWarning projects/pec/tools/pilot-drill.ts \
  --mdl "$MDL_PATH" \
  --rail "$RAIL_PATH" \
  --decisions "$DECISIONS_PATH" \
  --risks "$RISKS_PATH"
```

Scope rules:

- Use only owner-supplied file paths.
- Capture command, exit code, accepted/updated/conflict/rejected counts,
  timings, and row-level reject summaries.
- Do not commit scratch databases, real spreadsheets, or raw row content unless
  the owner separately permits the exact artifact.
- Stop and record a blocker if any command would require `force=true`.

## Restore Rehearsal

If the owner includes a real backup artifact in scope, restore only into a
scratch target path and record the source/target hashes and checks.

Expected command shape:

```sh
PEC_DB="$SCRATCH_RESTORE_PEC_DB" \
PEC_BACKUP_DIR="$SCRATCH_BACKUP_DIR" \
node --disable-warning=ExperimentalWarning projects/pec/tools/backup.ts restore "$BACKUP_FILE"
```

The manifest should record whether the restore tool preserved the pre-restore
scratch DB aside and what spot checks were performed. Do not start a production
server or mutate the real pilot DB.

## Optional API Captures

Authenticated API/export/report captures require the owner-supplied actor and
visibility basis. Capture only the artifact classes named by the owner.

Default permitted manifest facts:

- endpoint or report/export name;
- actor identity and visibility basis;
- status code;
- counts, timings, hashes of captured derivative artifacts;
- limitations and redactions.

## Closeout

The evidence branch must close with:

- completed `MANIFEST.md`;
- no raw real input files or DB files committed unless explicitly permitted;
- profile validator still VALID;
- repo self-check pass;
- full practitioner harness pytest pass;
- PEC `npm run typecheck && npm test && npm run build && npm run drill` pass;
- `git diff --check` pass;
- explicit statement that no Gate 2 adoption, L3 design/execution, pilot
  readiness, go-live, professional approval, check acceptance, decision
  outcome, revision issue, or `force=true` act occurred.
