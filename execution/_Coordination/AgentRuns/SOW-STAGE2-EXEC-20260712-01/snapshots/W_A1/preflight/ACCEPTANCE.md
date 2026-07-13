# W-A1 Preflight Acceptance

Status: `IMMUTABLE DERIVATIVE — A1-B0 PASS`

Accepted: `2026-07-13`

Accepted basis: `main@0724f26f6ef79d733c8f1c513b29d837fd43c8eb`

HELP_HUMAN accepts the read-only A1 preflight after independently reproducing
the exact live basis. The accepted ordinary population is 15 App members:
PKG-00=2, PKG-01=4, PKG-02=5, and PKG-03=4. All 60 legacy production source
hashes and 15 `_STATUS.md` hashes match P3 and current main; all members are
IN_PROGRESS, non-pilot, non-ISSUED, and exactly `LEGACY_FOUR_DOC`, with zero
live SOW. The ten accepted pilots remain exact `SOW_V1` and are excluded.

The decomposition/control, active standard/tool/skill/caller, App profile,
package ownership, author/verifier sequencing, candidate/evidence target,
future five-path replacement, rollback, and project-check bases are frozen in
the accepted preflight. Package candidate and evidence write scopes are
pairwise disjoint; all project deliverable directories remain read-only.

Schema, portability, containment, and diff hygiene pass. Drift, blockers,
material unknowns, and waivers are none. Exact snapshot and manager hashes are
recorded in `ACCEPTANCE_MANIFEST.tsv`.

This acceptance releases the four named WORKING_ITEMS managers only under
`A1-PACKAGE-ACTIVATION-001`. It does not accept a candidate, write a project
path, integrate a deliverable, alter lifecycle, approve H1 or H2, act on an
ISSUED member, release a product, or retire legacy support. RECONCILIATION and
later CHANGE remain mandatory before any A1 project truth changes.

Rerun A1-B0 if any accepted ref/snapshot, member/source/status/control,
lifecycle/exclusion/format, decomposition, standard/tool/skill/caller/profile,
ownership, target, gate, or manager activation byte changes before package
completion.
