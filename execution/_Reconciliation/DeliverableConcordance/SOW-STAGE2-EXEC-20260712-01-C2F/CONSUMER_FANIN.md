# C2 Consumer Fan-In

Overall verdict: `BLOCKED — C2G MUST REMAIN PARKED`

## Count and identity reconciliation

| Population | Expected | Classified | Changed | Retained / accepted upstream | Result |
|---|---:|---:|---:|---:|---|
| P0 exact caller rows | 64 | 64 | 52 | 12 | PASS |
| C2R-owned rows | 52 | 52 | 48 | 4 | PASS |
| C2A App rows | 9 | 9 | 4 | 5 | PASS |
| C1G canon rows | 3 | 3 | 0 | 3 | PASS |
| Unclassified callers | 0 | 0 | — | — | PASS |

The P2 root manifest partitions its 64 rows as 52 C2R, nine C2A, and three
C1G. Its dispositions reproduce 58 `ACTIVATE`, five `RETAIN_LEGACY`, and one
`DERIVATIVE_REGENERATE`. The root manifest intentionally records the nine App
rows as out-of-lane unchanged; the C2A final manifest supersedes those
out-of-lane hashes and reproduces all nine live identities with four changed
and five byte-identical rows.

All 52 C2R live post-hashes and all nine C2A final hashes reproduce. The
combined root/App changed sets match the live source diff exactly after the
parent-owned `WORK_GRAPH.json` is separately classified.

## Outcome classification

### Schema / mechanical

`PASS` for caller coverage, state vocabulary, SOW-only and legacy-only
selection, missing/partial/invalid/ordinary-dual rejection, deterministic
checklist routing, and recorded suites. C2R records 30 focused and 788 full
root tests plus agent/skill/export checks. C2A records 70 focused tests, 707
full frontend tests with four skips, typecheck, build, self-check, practitioner
pytest, and the successful registered premerge rerun.

### Content / authority

`BLOCKED` for two authority defects:

1. Root and App resolve `MIGRATION_DUAL` from any syntactically valid,
   self-matching `D-GOV-16@<7-64 lowercase hex>` token. The accepted C2A brief
   requires the exact `D-GOV-16@<accepted-sha>` authority. Root
   `tools/scope_of_work/common.py` validates only the regex and embedded marker;
   App `frontend/src/lib/workspace/filesystem.ts` does the same. Both test
   suites label `D-GOV-16@0123456` as authorized. That value is not the
   accepted D-GOV-16 ruling SHA. An unauthorized dual state can therefore be
   presented as authorized when isolation/path and a self-authored marker are
   supplied.
2. The root `ISSUED` converter checks source commit syntax, four source hashes,
   and `_STATUS.md`, but has no accepted-basis input or output binding. The
   active `scope-of-work` brief schema and D-GOV-16 item 6 require source
   commit, four source hashes, status hash, and accepted basis. The C2R
   compatibility matrix consequently overstates the proved ISSUED binding.

These are semantic authority conflicts, not test-substrate conditions. Under
the sealed C2F brief, unauthorized dual acceptance or a semantic authority
conflict blocks C2G.

### Preservation / containment

`PASS`. The 48 C2R source writes and four C2A source writes are exact-manifest
members and disjoint. The only other tracked diff is the parent-owned
coordination graph. No `projects/**/execution/PKG-*`, deliverable production,
underscore control, `_STATUS.md`, Remaining, lifecycle, receipt, release,
decision, or governed canon path changed. The pre-existing
`.claude-worktrees/` container remains outside scope and was not inspected or
modified by this fan-in.

### Execution substrate

`SUBSTRATE_FALLBACK_PASS_WITH_TRACE_NOTE`. C2R's TOOL-CORE child and C2A's
implementation child were interrupted for duration; the managers completed
bounded fallbacks and recorded passing checks. C2A's reviewer found one real
warning-only-invalid acceptance defect; the current reviewer return/status
records `PASS_AFTER_REPAIR` and the regression is present. C2A's later
handoff/backcheck narrative still says the correction-only reviewer rerun
stalled, so the package should be normalized on rerun, but this trace
inconsistency is not the authority blocker above.

## Compatibility verdict

- `SOW_V1`: supported and selected.
- `LEGACY_FOUR_DOC`: retained and supported through rollback; no retirement.
- missing, partial, invalid, and ordinary/normal-route dual: fail closed.
- isolated dual with mismatched syntax, path, isolation flag, or body marker:
  fail closed.
- isolated dual with a syntactically valid but unaccepted self-matching SHA:
  **fails the governance requirement by being accepted**.
- ISSUED preparation without source/status bindings: refused; without an
  accepted-basis binding: **not proved/refused by the deterministic tool**.

## Required rerun

C2R and C2A must repair and independently test the exact accepted-authority
binding. C2R must also bind the accepted basis for ISSUED preparation. Then
rerun all affected focused suites, applicable full/registered checks,
changed-path/hash manifests, independent review, and this C2F fan-in. Preserve
the current evidence; do not rewrite it as PASS.
