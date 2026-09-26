# D-GOV-46 — Dependency tracking modes and the `_DEPENDENCIES.md` heading schema

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record; merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session on `claude/brave-goodall-wj3hok`, workflow-library
review wave 2b item 1, after tranche ROOT-WORKFLOW-WAVE2A-SETUP-DEPS-20260926
deferred the heading and mode alignment

AcceptedBasis: main@971ca68a15a562f6df33cf4c78d27948ad07f822 (merge of PR #935)

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/SPEC.md` `052d45d3…`;
`.agents/skills/preparation/references/scaffold-contract.md` `fa89ebe4…`;
`workflows/dependency-extract/WORKFLOW.md` `5dc7df20…`;
`workflows/dependency-extract/resources/brief.md` `466b7af7…`;
`workflows/project-setup/resources/contract.md` `5cc8c5f8…`;
`workflows/project-setup/resources/method.md` `07cfa193…`;
`workflows/content-digest/WORKFLOW.md` `e7333063…`;
`tools/validation/validate_enum.py` `d0f1dd62…`;
`tools/REGISTRY.md` `7eb19a40…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA for new `_DEPENDENCIES.md` files and new
coordination records; existing files and in-flight projects adopt by their own
loop's decision (see item 5)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation. When the agent asked:

> The _DEPENDENCIES.md format and the mode names disagree. SPEC §5.2 uses a
> 'Dependency Tracking Mode' section with modes NOT_TRACKED / DECLARED /
> TRACKED. project-setup, the preparation skill and manual §6 use
> NOT_TRACKED / DECLARED / FULL_GRAPH with different meanings, and
> dependency-extract uses a third set of headings. Which should be the single
> source of truth?

the owner selected:

> Amend SPEC to FULL_GRAPH

with the option text:

> Keep the manual's NOT_TRACKED / DECLARED / FULL_GRAPH meanings, where
> DECLARED means a partial view of critical edges, and amend SPEC §5 to
> match. Needs a governance change.

The owner then directed:

> yes, go ahead with wave 2b #1 and 2, and on #3 and 4 as recommended.

Item #1 of wave 2b is this amendment.

## The disagreement found

- `docs/SPEC.md` §5.2–§5.3 used a `## Dependency Tracking Mode` section with
  `NOT_TRACKED | DECLARED | TRACKED`, where `DECLARED` meant "no agent
  extraction" and `TRACKED` meant full extraction with `Dependencies.csv`.
- `workflows/project-setup` (contract glossary, `_COORDINATION.md` template,
  Phases 1.3, 2.2b and 3.1), the `preparation` skill and the alignment manual
  §6 used `NOT_TRACKED | DECLARED | FULL_GRAPH`, where `DECLARED` is a
  partial, human-curated view that may still use extraction (Phase 2.2b runs
  under `DECLARED` or `FULL_GRAPH`).
- The `preparation` skeleton wrote `## Coordination (human-owned)`,
  `## Run Notes & History` and `## Consumer Handoff Notes`, and said
  `dependency-extract` "must find these headings unchanged", while
  `dependency-extract` Function 4 writes `## Run Notes`, `## Run History`,
  `## Lifecycle Summary` and `## Downstream Handoff Notes`.
- `tools/validation/validate_enum.py` `TRACKING_MODE` accepted `TRACKED` and
  rejected `FULL_GRAPH`; `workflows/content-digest` reported `TRACKED`.

## Decision

1. **One mode vocabulary (SPEC §5.3).** The modes are `NOT_TRACKED`,
   `DECLARED` and `FULL_GRAPH`, with the alignment manual §6 meanings:
   - `NOT_TRACKED`: coordination occurs outside the files; no computed
     ready/blocked judgment is reported from dependencies.
   - `DECLARED`: the recorded critical edges are a partial view. Blockers
     come only from the recorded register, and edges in an unresolved
     cycle are non-gating and held, as under `FULL_GRAPH`. Agent extraction may populate
     `Dependencies.csv` when the human-confirmed dependency rules call for it
     (project-setup Phases 1.3 and 2.2b). Extraction does not make the view
     complete or replace the human-owned declarations. SPEC's earlier "no
     agent extraction" restriction is withdrawn.
   - `FULL_GRAPH`: declarations are intended to cover the selected graph
     semantics. Blockers are computed only after closure audit and cycle
     treatment. Edges in unresolved cycles are non-gating and held
     (`docs/CYCLE_DRIVEN_RESOLUTION.md` §2 rule 4).
   `TRACKED` is a legacy value read as `FULL_GRAPH`. Files that carry it are
   not rewritten.
2. **One heading schema (SPEC §5.2).** SPEC's existing structure is kept and
   is the only skeleton:
   - `## Dependency Tracking Mode`, now with `Mode`, `Register` and `Notes`
     lines;
   - `## Declared Upstream (I need these before I can proceed)`;
   - `## Declared Downstream (These need me)`;
   - `## Extracted Dependency Register`;
   - `## Lifecycle Summary`;
   - `## Run Notes`;
   - `## Run History`;
   - `## Downstream Handoff Notes`, which is added only for a run whose
     `CONSUMER_CONTEXT` is not `NONE`.

   SPEC §5.2 also states the placeholder form `preparation` writes before the
   first extraction. It adds a legacy-heading table that maps
   `## Coordination (human-owned)`, `## Coordination Mode`,
   `## Dependency Tracking`, the older upstream/downstream forms,
   `## Run Notes & History`, `## Consumer Handoff Notes (optional)` and the
   `(populated by TASK+dependency-extract)` suffix to their sections.
3. **Aligned surfaces.**
   - The `preparation` scaffold contract carries the §5.2 skeleton exactly.
     It no longer claims that `dependency-extract` requires unchanged
     headings.
   - `dependency-extract` Function 4 cites §5.2 and keeps "do not rename
     declared sections". It preserves and reads legacy headings in existing
     files, refreshing each agent-owned section under the heading the file
     already uses.
   - `project-setup` states the §5.3 meanings and the §5.2 skeleton.
   - `content-digest` reports `FULL_GRAPH`.
   - SPEC §13 no longer says tracking "always maintains the full DAG".
4. **Tool.** `validate_enum.py` `TRACKING_MODE` is
   `NOT_TRACKED | DECLARED | FULL_GRAPH`. A `LEGACY_ALIASES` map accepts
   `TRACKED` on read, reports it as `FULL_GRAPH`, and names `FULL_GRAPH` as
   the write form. A new test covers this. No live tool in `tools/` parses
   `_DEPENDENCIES.md` headings or modes. One tool writes the file:
   `tools/coordination/materialize_local_dependencies.py --refresh-pointers`
   overwrites it with a generated pointer format (`## Generated Dependency
   Register`, `## Authority Boundary`) that drops human-owned sections. That
   writer is outside this tranche and not aligned with §5.1; aligning it or
   retiring the flag is a follow-up. On 2026-09-26, no existing project
   `_DEPENDENCIES.md` recorded `TRACKED`.
5. **Adoption.**
   - Existing `_DEPENDENCIES.md` files, historical run records and in-flight
     projects keep their headings and mode values. Nothing is rewritten.
   - New files, and sections added to existing files, use the amended schema.
   - Notices go to the App, Runtime, Piping and PEC loops, and each loop
     decides its own adoption. The Runtime loop records mode `DECLARED`, whose
     meaning this amendment states. The App loop's own `docs/SPEC.md` mirror and its frontend
     scaffold template are App-owned and are named in its notice.
6. **Unchanged.**
   - The `Dependencies.csv` v3.1 schema (SPEC §6).
   - TYPES §6's coordination representations.
   - `docs/CYCLE_DRIVEN_RESOLUTION.md`, `audit-dep-closure` and
     `scc-resolution-case`, which carry no mode or heading text to align.
   - The alignment manual, which already states these meanings.
   - The thesis (`docs/thesis/07_se_design_analysis.md` §7.9.3 still lists
     `TRACKED`); it is historical exposition and is not edited here.
   - No release is granted.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-DEPENDENCY-SCHEMA-D-GOV-46-20260926.yaml`.
- The PR description records the checks run on the candidate: workflow index
  build and `--check`, workflow, agent-instruction and skill metadata
  validators, the tranche-manifest guard, and the tools test suites.
- Independent review of the pull request diff precedes merge under the
  standing Git authorization. The reviewer checks the following:
  - the quoted owner words match the conversation;
  - SPEC §5.3 says no more than the manual §6 and project-setup sources;
  - no existing `_DEPENDENCIES.md` file or historical record changed.
