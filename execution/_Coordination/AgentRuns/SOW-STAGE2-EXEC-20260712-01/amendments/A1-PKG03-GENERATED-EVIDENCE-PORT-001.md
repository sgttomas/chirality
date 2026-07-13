# A1 PKG-03 Generated-Evidence Portability Amendment 001

Status: `ACTIVE — EXACT NON-SEMANTIC GENERATED-EVIDENCE REPAIR`

## Trigger and classification

Two generated records contain local checkout-root strings while their
substantive conversion/check results are PASS.

1. `instances/WORKING-A1-PKG03/children/AUTHOR-DEL-03-02/workspace/_run_records/TASK_RUN_2026-07-13_0852.md`
   is 3,006 bytes at preimage SHA-256
   `6a5d3cb2b5159bdecd37ec0fceb5bfa84cff8f1b4b085a43c86351f7ecb1596f`
   and contains exactly two occurrences of
   `/Users/ryan/ai-env/projects/chirality/`, in generated `scope-path` and
   `resolved-skill-path` fields.
2. `instances/WORKING-A1-PKG03/PROJECT_CHECKS.json` is 46,153 bytes at
   preimage SHA-256
   `0c102a01989435831a5db8c585592da679c7027c39c1baeb71cd519eb4a99d8d`
   and contains exactly four occurrences of
   `/Users/ryan/ai-env/projects/chirality` across generated profile/root
   metadata and captured test stdout.

These are generated-evidence portability defects, not accepted source/control
literals. Candidate, source, status, mapping, parity, checklist, render,
verdict, project, and lifecycle bytes are outside this amendment.

## Exact repair

The owning `WORKING-A1-PKG03` manager may modify only the two records named
above. In the run record it may replace
`/Users/ryan/ai-env/projects/chirality/` with `~/` exactly twice. In the JSON
check record it may replace `/Users/ryan/ai-env/projects/chirality` with `~`
exactly four times.

For each file, record the exact path, pre/post byte counts and SHA-256,
substitution count, and reverse-substitution SHA-256 in a package-local repair
manifest/check record. Reverse substitution must reproduce the exact preimage
hash. The JSON postimage must parse; all command, exit-code, status, and
substantive stdout/stderr content must be unchanged modulo the authorized
literal substitution; every registered result must remain PASS. Search for
all direct child/package preimage hash or summary bindings and refresh only
bindings that directly name the repaired record, recording `NONE` when no
binding exists. Include the amendment, repair proof, refreshed bindings, and
postimages in final package MANIFEST and handoff.

Generated evidence under the affected child and package check surface must
then contain zero checkout and temp prefixes, excluding only separately
inventoried exact source/control bytes. Any different edit, failed count,
failed reverse proof, non-PASS check, candidate/input/status mutation,
additional generated-evidence prefix, or write outside package evidence scope
blocks fan-in.

This amendment changes no scope, authority, acceptance criterion, lifecycle,
risk, candidate, project truth, integration gate, H1/H2 posture, ISSUED state,
release state, or retirement state. No substantive rerun or new human ruling
is required.
