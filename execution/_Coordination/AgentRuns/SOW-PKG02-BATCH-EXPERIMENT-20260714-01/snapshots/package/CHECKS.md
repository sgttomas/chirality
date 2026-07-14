# PKG-02 Batch Experiment Package Checks

Verdict: `PASS — READY FOR INDEPENDENT EXPERIMENTAL RECONCILIATION`

## Sufficient-quality result

Exactly `DEL-02-01` through `DEL-02-05` were processed by one batch-author
Agent-2 session followed by one fresh batch-verifier Agent-2 session. The
accepted candidate family is:

| Member | Evidence SHA-256 | Clean production SHA-256 | Mappings | Source lines |
|---|---|---|---:|---:|
| DEL-02-01 | `efb5b12d27a142a8f0236b75b70cf8f0d066a8eca04670425bb1fe4eb095763c` | `4493b30fc0758de2f34654f5eb36316644caee1b66ca3c2c20026856f66b13bf` | 35 | 427 |
| DEL-02-02 | `6ded4d111577a9c2d1beb510b28c91f094309aa4eafec3c205d25723995ae068` | `3fd8885d931066726f2d0b4e380510b48c91a7ea72c6c3060f1287612ae02afa` | 48 | 419 |
| DEL-02-03 | `63e5d86ec14d5b29715c5f5d1ab22bceb888935b5aff31581f447786b1b4bca8` | `d9b119d9bb5eb79a7e6f24eb9dfa51d9c4d545bee979d8dbdc4332a57847661e` | 29 | 383 |
| DEL-02-04 | `f261f677304743baca6fa3d091fd67ed2b8067b50966eedcfdf99e25cce6bd01` | `50ad507737d966be4a7fea39f921a8fb0e614c9c3124b733c27a873e9c1fe062` | 33 | 369 |
| DEL-02-05 | `7623258d2abc1a9857513af409c891a5650101773cac50242fd1550148761713` | `aa49dc1617c489649e8b311043a3e7fae9d8a9a71d902709ba24d9db5edfe5b7` | 41 | 455 |

Aggregate coverage is 186/186 mappings over 2,053/2,053 source lines. Author,
fresh verifier, and manager reproduction agree on every evidence candidate,
clean finalization, finalization report, mapping, parity result, checklist, and
render. Clean contracts validate as standalone `SOW_V1`, retain literal source
as blockquotes, and contain no migration-only metadata. Evidence candidates
remain derivative and are absent from the replacement manifest.

This is sufficient evidence for faithful representation replacement only. It
does not approve the underlying engineering content or lifecycle state.

## Strict fan-in and package checks

- Author manifest: 939/939 rows rehashed with exact self-exclusion and allowed
  containment; author verdict 5/5 PASS with retained process findings.
- Verifier manifest: 535/535 rows rehashed with exact self-exclusion and
  verifier-folder containment; verifier verdict 5/5 PASS_UNCHANGED.
- Candidate preservation: all 15 candidate files and all 45 live input/control
  files rehashed unchanged after verification.
- Deterministic evidence: 10 author conversions, 10 author finalizations, 10
  verifier conversions, and 10 verifier finalizations match their accepted
  member artifacts; all repeated consumer outputs are byte-stable.
- Negative behavior: 35 author, 35 verifier, and 35 manager probes fail closed
  under the registered schemas without gate weakening.
- Manager reproduction: five fresh conversions/finalizations, production-bound
  mapping/parity, clean checklist/render, four-document checks, and dependency
  schema checks pass.
- Replacement manifest: exactly 25 rows—five clean production adds and twenty
  legacy-document deletes. The rollback manifest is its exact path/hash inverse.
- Apply / target validation / rollback simulation: 5/5 PASS without project
  writes.
- Manager evidence portability: 153 machine-root occurrences in 53 generated
  files were reversibly normalized to `{REPO_ROOT}`; no clean candidate changed.
- Practitioner self-check: exit 0, no BLOCK, unchanged baseline `INFO=15`,
  `NOT_APPLICABLE=2`, `REVIEW=27`, `WARN=6`.
- Full practitioner harness: 264 passed in 69.31 seconds.
- DEC-025: not applicable because no project code path changed.

## Retained execution findings

1. Author inventory used unsupported BSD `find -printf`; it failed before
   output and used a portable inspection instead.
2. Author `bash -n` caught one shell-quote defect before harness execution.
3. Author initially wrote the DEL-02-01 progress time twelve hours ahead, then
   improperly replaced the row. The original and correction are retained.
4. Verifier member 1 restarted three times for local schema assumptions:
   claim-map column names, checklist hash location, and failed-parity report
   emission. No candidate was repaired; positions 2–5 had zero retry.
5. Verifier manifest paths are portable repo-relative strings rather than the
   preferred literal `{REPO_ROOT}` form. One compiled cache row is binary, so
   only its hash/byte count—not a semantic line count—is binding.
6. Manager telemetry first used unsupported event type `SESSION_START`; the
   tool rejected it before output and the schema-correct `START` succeeded.
7. Manager reproduction first tested a candidate-only evidence file when the
   intended forbidden consumer state was complete unauthorized dual. It
   stopped at member 1, selected the correct fixture, and reran all five fresh.

These findings are runtime/harness maturity costs. None changed a candidate,
project path, lifecycle, acceptance criterion, or quality gate.

## Scope and closure

No project, active Stage-2 plan/run, lifecycle, Git, H1/H2, PKG-00, PKG-01,
integration, release, retirement, excluded domain-audit, or
`.claude-worktrees/**` path was written. Blockers / waivers / unknowns:
`none / none / none`. The package derivative is current at the hashes above
and requires the chartered independent RECONCILIATION verdict.
