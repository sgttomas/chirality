# A1 PKG-01 AUTHOR-DEL-01-02 Portability Amendment 001

Status: `ACTIVE — EXACT NON-SEMANTIC EVIDENCE REPAIR`

## Trigger and classification

AUTHOR-DEL-01-02 is substantively terminal PASS, but its generated TASK run
record contains three occurrences of the checkout prefix
`/Users/ryan/ai-env/projects/chirality/` in `scope-path`,
`resolved-skill-path`, and `RuntimeOverrides.DELIVERABLE_PATH`.

Two additional checkout-prefix occurrences in the isolated workspace are not
defects: they are inside byte-exact copied live source/control inputs
`_DEPENDENCIES.md` and `Dependencies.csv`. Those files must remain identical to
the accepted manifest-bound project sources and are expressly excluded from
normalization. Portability applies to generated run/evidence surfaces, not to
rewriting authoritative input bytes.

## Exact repair

The owning WORKING-A1-PKG01 manager may replace only
`/Users/ryan/ai-env/projects/chirality/` with `~/` exactly three times in:

`instances/WORKING-A1-PKG01/children/AUTHOR-DEL-01-02/workspace/_run_records/TASK_RUN_2026-07-13_0657.md`.

Before repair, record the file's path, occurrence count, byte count, and
SHA-256. After repair, prove reverse substitution reproduces the exact preimage
hash. Search for and refresh only a direct package-local hash or summary binding
that names this run record; if none exists, record `NONE`. Preserve the author
RETURN/STATUS and all candidate, source, status, mapping, parity, checklist,
render, verdict, and containment results unchanged. Write a package-local
repair manifest/check record and include it in final package MANIFEST/fan-in.

Generated evidence under this author must then have zero checkout and temp
prefixes. The two named source/control inputs remain permitted exact-source
exceptions and must retain their accepted hashes. Any different edit,
candidate/input/status change, additional generated-evidence prefix, failed
reverse proof, or required write outside package evidence blocks fan-in.

This amendment changes no scope, authority, acceptance criterion, lifecycle,
risk, candidate, project truth, integration gate, H1/H2 posture, ISSUED state,
release state, or retirement state. No substantive author rerun or new human
ruling is required.
