# Deliverable queries

Run from the repository with Python 3 and PyYAML:

```sh
python3 -m tools.deliverables --project projects/chirality-app-v4 check
python3 -m tools.deliverables --project projects/chirality-app-v4 neighborhood DEL-07-02
python3 -m tools.deliverables --project projects/chirality-app-v4 impact DEL-07-02
python3 -m tools.deliverables --project projects/chirality-app-v4 touches HEAD
python3 -m tools.deliverables --project projects/chirality-app-v4 touches PR:1234
python3 -m tools.deliverables --project projects/chirality-app-v4 dag-diff app-v4/deps-baseline-1
```

App v4 is the default project. Output is JSON; nothing is written. The basis
names HEAD and observed working-tree changes. Every relationship cites its
source file and need index. `dag-diff` resolves the baseline to a commit and
compares declarations there with current working files, preserving distinct
conditions and multiplicity. Metadata may live under either old phase folders
or flat deliverable folders.

`deliverable.yaml` requires `id` and `needs`. Optional `name`, `code_paths` and
`checks` describe the deliverable. Every need has `from` and `condition`, with
optional `when`, `gating` and `evidence`. Suppliers are local `DEL-nn-nn` IDs or
`external:name`, `doc:path`, `package:id`, or `unknown`. Paths and globs are
project-relative. Consumer declarations define the upstream relationships;
reverse links are generated. Migrated outward obligations to nonlocal targets
can carry `direction: downstream`; the neighborhood lists these as outputs,
not required inputs.

`neighborhood` shows direct inputs and consumers. `impact` follows consumers
transitively, including non-gating relationships. `touches` matches Git diff
paths against relevant code paths; a path can match several deliverables.
A single revision selects that commit’s change (against its first parent, or
the empty tree for a root commit), regardless of working-tree edits. Explicit
ranges are used as supplied. Use a Git revision/range or `PR:number`/GitHub PR URL (requires authenticated
`gh`). Unmapped paths and deliverables without mappings remain visible.

`check` rejects malformed YAML, duplicate IDs/keys, invalid identities and
escaping paths. Missing suppliers, planned paths and cycles are reported with
exit 0; malformed input returns exit 2 and any usable partial result. Cycles
include non-gating relationships and are not themselves execution blockers.
A present file or supplier declaration establishes only presence. Suitability
remains unknown; the tool never marks completion, interprets a merge as
acceptance, or claims a test passed. Agent judgment and appropriate checks
establish whether an input meets its condition.

Migration is explicit and dry-run by default. For the App v4 pilot's full
source-row accounting and DAG-004 comparison, run:

```sh
python3 tools/deliverables/migrate_dependencies.py --source-ref 8e95c5593fc552c277a1daa79ced73ca48d09256
```

`--summary` gives counts and unresolved facts; `--apply` writes YAML only.
Re-running against that source after flattening preserves the flat evidence
paths and seeded code/check references. No new record or graph file is emitted.
Unknown targets and differing old maturity descriptions remain evidence for
judgment, not new blockers. Row IDs occur in the migration output, not in the
ongoing deliverable format. Source Notes are retained where restrictions and
rationale cannot safely be separated mechanically.

Piping's DAG-011 is a snapshot (active/retired/anchor rows in one CSV), not
App v4's admitted/held layers. Its reproducible migration command is:

```sh
python3 tools/deliverables/migrate_dependencies.py --project projects/chirality-piping --source-ref 6228147ac5 --dag _DAG/DAG-011 --dag-format snapshot --retire-metadata --apply
```

The snapshot option filters active execution relationships and preserves empty
architecture nodes. `--retire-metadata` omits optional pointers to removed admin
files; their source content remains in Git. It does not remove need conditions.
