# Audit tools implementation return

Status: COMPLETE. Actual execution: delegated-harness-native TASK instance;
role, write boundary, and non-delegation were instruction-asserted. Parent:
WORKING_ITEMS. No child delegation or Git action was performed.

Implemented the two deterministic evaluation CLIs and common strict CSV/format
helpers. Dependency auditing covers complete records and exact canonical fields,
all enums, anchors, evidence population and honest empty/malformed denominators.
Structure auditing selects a declared variant or explicit production inventory,
reads Current State fields including RETIRED, and carries canonical SOW/legacy/
migration format distinctions. Successful audit execution is distinct from
subject conformity. Source-file output targets are rejected.

Repaired the existing dependency closure analyzer at its discovered actual path,
`tools/coordination/analyze_dep_closure.py`, under the parent's scope amendment.
Added scope/filter/normalization/hub/cycle/prior-summary inputs, registerless
inventory nodes, canonical row exclusion, malformed-source findings, missing
sources/targets, isolated-unit distinction, external-scope distinction,
self-loop SCCs, iterative large-graph traversal, representative cycles, and nine
explicit check statuses. Historical interfaces retain documented adapters.

`tools/evaluation/README.md` contains exact commands, schemas, status/exit
contracts, brief-field bindings, graph orientation, and compatibility changes.
Legacy shell audit entrypoints now invoke the exhaustive Python tools and emit
JSON. The former mislabeled orphan metric is explicitly schema-versioned;
historical orphan counts are excluded from prior-run delta comparison.

Validation: 12 tests passed. Fixtures cover quoted/multiline records, exact
anchors, late enum errors, malformed/empty inputs, duplicate headers, RETIRED
versus history, initialized missing content, SOW/legacy/authorized dual formats,
explicit DOMAIN/missing-unit inventories, arbitrary working directories,
source-write rejection, graph scope/status/normalization/threshold behavior,
registerless nodes, invalid graph rows, bounded cycles, self-loops, a 3,001-node
SCC, output artifacts, and prior comparison. Root execution smoke commands all
completed and accurately returned subject FAIL against its existing physical
contents; these observations do not activate historical product scope.

Files/hashes: `COVERAGE.json`. Test/smoke evidence: `VALIDATION.json`.
Recorded role basis: `ROLE_BASIS.md`.

Parent follow-on: integrate evaluation workflow invocations and manifest these
files. Shared `tools/validation/validate_enum.py` omitted RETIRED at inspection;
its owning worker has been notified through the parent. App/Runtime adoption
remains governed by the overall tranche hold.
