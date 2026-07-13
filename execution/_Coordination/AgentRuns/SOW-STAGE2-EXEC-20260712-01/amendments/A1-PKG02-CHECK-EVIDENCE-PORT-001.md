# A1 PKG-02 Check-Evidence Portability Amendment 001

Status: `ACTIVE — EXACT NON-SEMANTIC GENERATED-EVIDENCE REPAIR`

## Trigger and classification

The registered App checks are substantively PASS, but the two generated JSON
check records retain machine-specific strings emitted by the local check
substrate. `PROJECT_CHECKS.json` contains four occurrences of
`/Users/ryan/ai-env/projects/chirality`; its exact preimage is 46,041 bytes at
SHA-256 `6389ce4b75b949c51dedacef934d136cb09fc49d5281e5c6fe1c36d2fb273045`.
`PROJECT_CHECKS_PREMERGE.json` contains 23 occurrences of that checkout root
and four occurrences of
`/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T`; its exact preimage is
13,852 bytes at SHA-256
`28d7194ad2d12497e96c03a4df78f56904f00da97e82f21f0e42a3c8b8a710cf`.

These are generated check-evidence portability defects. They are not accepted
source/control literals and do not occur in candidate, source, status,
mapping, parity, checklist, render, or child verdict authority.

## Exact repair

The owning `WORKING-A1-PKG02` manager may modify only:

- `instances/WORKING-A1-PKG02/PROJECT_CHECKS.json`
- `instances/WORKING-A1-PKG02/PROJECT_CHECKS_PREMERGE.json`

It may replace `/Users/ryan/ai-env/projects/chirality` with `~` exactly 27
times across those files and replace
`/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T` with `${TMPDIR}` exactly
four times in the premerge file. Before and after repair it must record exact
paths, byte counts, hashes, and substitution counts in
`CHECK_NORMALIZATION_MANIFEST.tsv`; reverse substitution must reproduce each
exact preimage hash. It must prove both JSON files still parse, their command,
exit-code, status, and substantive stdout/stderr content are unchanged modulo
the two authorized literal substitutions, and every check remains PASS.

The manager must search for direct package-local preimage hash/summary
bindings and refresh only bindings that directly name these two records; if
none exists, record `NONE`. It must include the amendment, normalization
manifest/check record, and exact postimages in the package manifest and
handoff. Any different edit, failed count, failed reverse proof, non-PASS
check, candidate/input/status mutation, extra generated-evidence prefix, or
write outside the package evidence scope blocks fan-in.

This amendment changes no scope, authority, acceptance criterion, lifecycle,
risk, candidate, project truth, integration gate, H1/H2 posture, ISSUED state,
release state, or retirement state. No substantive check rerun or new human
ruling is required.
