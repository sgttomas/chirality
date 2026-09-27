# Supersession note

This snapshot supersedes
`projects/chirality-app-dev/execution/_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_1701`.
The superseded snapshot's bytes are unchanged. It in turn superseded the
pre-setup snapshot `..._0505`.

## Reason

Independent review of `0ca5ffcca..1d5909491` found that the 1701 snapshot
judged export regeneration by searching the last eight commit subjects for
`exports(app)`. That result depends on where HEAD is: at 1701 it reported
COMPLETED, 13 of 13, but a rerun at `1d5909491` gives NO_EVIDENCE, 12 of 13.
The review also changed dependency rows in place, so the closure evidence had
to be rebound.

## What changed in inputs and evidence binding

- **Export freshness is now deterministic and read-only.**
  - The export stage is rebuilt with `exports/chirality-app/export_public.py`'s
    own `build_stage`, in a temporary directory outside the repository.
  - Its manifest (path, size, SHA-256) is compared byte-for-byte with the
    committed `export-manifest.csv`.
  - Result: the two match, over 1,880 files.
- **Closure evidence.** The post-extraction closure evidence is now
  `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725/`.
  It binds the current registers after the ESR-1 re-evidence. Its topology is
  unchanged: 107 edges, 0 SCC.
- **Changed inputs.** The registers and `_DEPENDENCIES.md` indexes of the
  affected deliverables:
  - eight ESR-1 rows re-evidenced in place;
  - DEP-08-02-003's `TargetName` shortened to a name;
  - indexes regenerated under their existing headings.

  All the other inputs are unchanged. Their hashes are in
  `INPUT_MANIFEST.sha256`.

## Result

`CLOSED_WITH_OBSERVATIONS`: 0 critical, 0 major, 0 minor and 1 observation
(the DEL-02-03-REQ-009 residual, DX-15).
- All 29 actions are verified.
- All 13 downstream reruns are COMPLETED.
- All 16 expected extraction outcomes are VERIFIED.
- A rerun of `audit_scope_closure_run.py` reproduces this snapshot
  byte-for-byte.
