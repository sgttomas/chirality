# TOOL POLICY — scope-of-work

## Required order

1. Read and hash the authoritative source kit and `_STATUS.md`.
2. Run `convert_four_documents_to_scope_of_work.py` only under the accepted
   pilot variance.
3. Refine content through bounded reasoning without removing source markers.
4. Run `validate_scope_of_work.py` with the same variance reference.
5. Run `map_scope_of_work_claims.py` and
   `report_scope_of_work_parity.py` independently of the authoring judgment.
6. Run `render_scope_of_work.py` only when a derivative was requested.

## Allowed tools

- `tools/scope_of_work/convert_four_documents_to_scope_of_work.py`
- `tools/scope_of_work/validate_scope_of_work.py`
- `tools/scope_of_work/map_scope_of_work_claims.py`
- `tools/scope_of_work/report_scope_of_work_parity.py`
- `tools/scope_of_work/render_scope_of_work.py`

The tools are deterministic and local. They do not use a network or LLM and
do not modify lifecycle state. The converter alone writes
`ScopeOfWork.md`; report tools write only their explicit output paths.

## Disallowed use

- No `--force` unless the brief explicitly authorizes replacement of a
  candidate in the same isolated pilot worktree.
- No converter use on `ISSUED`, unknown, or non-`IN_PROGRESS` state.
- No write to legacy production documents or underscore files.
- No HTML tracking as canonical or accepted truth.
- No removal of `skills/four-documents` or its callers during Stage 1.

