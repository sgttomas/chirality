# P4 Pilot Integration Premerge Handoff

Snapshot status: `IMMUTABLE DERIVATIVE — PREMERGE CANDIDATE`
Closure verdict: `PASS — READY FOR REMOTE VALIDATION`
Next owner: `CHANGE-P-G`

The source branch contains one exact evidence-binding commit, ten serial
atomic replacement commits, and this premerge evidence binding. The ten live
branch states are exact accepted `SOW_V1` candidates with all four legacy
documents absent, statuses byte-identical, and lifecycle `IN_PROGRESS`.

The accepted upstream snapshot is P4 preintegration R1 at basis
`0d260eb024d8b8dada0df477b70ac880a6906ffa`. This package is derivative and
does not replace authoritative project truth. Remote PR paths, commit
architecture, required checks, and merge remain to be validated.

Blockers, material unknowns, and waivers are none. H1/H2 remain unapproved.
Piping `DEL-01-01`, lifecycle, release, reliance, and legacy retirement are
outside this tranche.

Rerun from P-F-R1 if an accepted source, candidate, status, authority,
manifest, or preintegration evidence byte changes. Before merge, stop on any
remote path, commit, check, or branch identity drift. Rollback requires an
explicit later forward commit applying the bound inverse manifest and exact
base bytes; no automatic rollback or history rewrite is authorized.
