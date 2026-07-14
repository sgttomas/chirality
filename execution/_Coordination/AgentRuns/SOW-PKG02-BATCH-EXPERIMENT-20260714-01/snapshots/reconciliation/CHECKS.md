# Independent PKG-02 Reconciliation Checks

Verdict: `PASS_WITH_RETAINED_PROCESS_FINDINGS`.

## Sufficient-quality reproduction

The charter defines “sufficient” as faithful representation replacement:
deterministic clean finalization; valid clean `SOW_V1`; complete current-hash
source preservation; conservative scope/objective binding; deterministic
map, parity, checklist, and render outputs; fail-closed negative behavior;
exact replacement/inverse rollback; unchanged live status/control inputs; and
no new semantic obligation or lifecycle meaning. It is not substantive
engineering approval.

- All five frozen members and all 45 live input/control hashes reproduced.
  Four-document and dependency-schema checks passed 5/5, all live paths remain
  legacy-only, and the accepted Stage-2 run plus live PKG-02 paths have zero
  tracked diff from `main@3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c`.
- Aggregate evidence reproduced at 186 mappings and 2,053 source lines. All
  five evidence, clean-production, and finalization-report hashes equal the
  immutable E1 member ledger.
- Clean finalization binds both evidence and production hashes, externalizes
  migration authority to `finalization.json`, and leaves the production
  contract free of migration-only authority metadata.
- The package, manager, author, and verifier manifests rehashed 1,811/1,811
  entries: respectively 284, 53, 939, and 535 rows. Paths are unique,
  contained, existent, self-excluding, and portable. Three manifests use
  `{REPO_ROOT}`; the verifier uses portable repo-relative paths. Its retained
  compiled-cache row is hash/byte-bound but has no meaningful semantic line
  count.
- The exact 25-row replacement ledger and 25-row rollback ledger are path,
  operation, and before/after-hash inverses. Evidence candidates are not
  production replacement inputs.
- Fresh apply, target `SOW_V1` validation, and exact legacy rollback passed
  5/5 in reconciliation-local scratch. No project path was written.

## Narrowed fresh reproduction

`DEL-02-01` was selected because every member-specific exception clustered
there. `DEL-02-05` was selected because it is the numerically final clean
member and, at 455 lines, the largest by source-line count.

For both members, duplicate conversions equaled each other and E1 evidence
byte-for-byte; duplicate finalizations equaled each other and the accepted
clean contract/report byte-for-byte. Production-bound maps and parity,
checklists, and renders were deterministic. Coverage reproduced at 35/427 and
41/455 mappings/lines. Clean validation passed, clean checklists bound the
clean hash with no migration authority, and renders were hash-bound with no
script, form, iframe, or external resource.

All seven documented negative classes were freshly exercised for each selected
member: mutated-clean map, mutated-clean parity, evidence-state checklist,
evidence-state render, partial legacy input, unauthorized dual validation, and
wrong-authority checklist. All 14 probes failed closed with the expected
artifact-emission semantics. Because both full reproductions passed, the
profile's expansion condition was not triggered.

## Comparison with accepted evidence

| Evidence | Members | Mappings | Source lines | Replacement rows | Simulations | Result |
|---|---:|---:|---:|---:|---:|---|
| App ordinary waves | 47 | 1,428 | 15,386 | 235 | 47 | accepted faithful-representation population |
| PKG-01 batch experiment | 3 | 88 | 727 | 15 | 3 | `PASS_EQUIVALENT` |
| PKG-02 batch experiment | 5 | 186 | 2,053 | 25 | 5 | `PASS_EQUIVALENT` |

PKG-02 preserves the same applicable representation-migration gates and the
separation between structural preservation evidence and substantive content
authority. The App's frontend/typecheck/build checks are not Piping-content
checks; the shared practitioner harness and Piping package checks passed in E1.
The greater member count and line population therefore retain the previously
accepted sufficient-quality level for this five-member scope.

## Retained process findings

There are seven grouped findings, or nine atomic items because the verifier
restart group contains three distinct causes:

1. Author BSD-incompatible `find -printf`, rejected before output.
2. Author shell quoting defect caught by `bash -n` before harness execution.
3. Author `DEL-02-01` telemetry timestamp/replacement-integrity defect, later
   append-corrected without deterministic-artifact effect.
4. Verifier `DEL-02-01` three full restarts for claim-map, checklist, and failed
   parity-report schema assumptions; no repair or weakened gate.
5. Verifier manifest style variance and one non-semantic binary line field.
6. Manager unsupported `SESSION_START`, rejected before event output.
7. Manager wrong negative fixture at member one, followed by a fresh correct
   five-member rerun.

Excluding the non-failing manifest-style variance leaves eight atomic
runtime/process defects. None affected candidate meaning, preservation,
project state, lifecycle, or acceptance criteria. These remain real harness
maturity and efficiency costs.

## Limits

Native context occupancy was unavailable in all three root sessions. PKG-01
has no comparable root runtime ledger, and the manager interval encloses child
work, so neither timing nor token savings can be compared cleanly. This result
supports five members, not an unbounded batch size.
