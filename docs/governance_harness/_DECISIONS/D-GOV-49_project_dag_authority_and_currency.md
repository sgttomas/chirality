# D-GOV-49 — One accepted DAG per project; authority from acceptance while current

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record, for merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session, workflow-library review wave 3, while revising
the unpushed `project-dag` workflow on local branch `wave3-project-dag`. That
draft treated the accepted project DAG as a "derived view" only, because
CONTRACT K-DEP-1 said "There is no central dependency graph". The owner
clarified the intent of that sentence and ruled on the model below.

AcceptedBasis: main@53145aaebb23b617e7ba1d2c626a6218d2be9176 (merge of PR #947;
PR #942 carried D-GOV-48)

Amends: `docs/CONTRACT.md` K-DEP-1 (rewritten; K-DEP-2 unchanged) and K-SNAP-1
(a `_DAG/` working-records clause added); `docs/PRD_ROOT.md` O-8 and N-5. No earlier
D-GOV record is superseded.

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/CONTRACT.md` `bbd3ff81…`;
`docs/SPEC.md` `73223c0b…`;
`docs/DIRECTIVE.md` `78e3d5f1…`;
`docs/PRD_ROOT.md` `b4bdf91f…`;
`workflows/scc-resolution-case/WORKFLOW.md` `2f44ed46…`;
`workflows/scc-resolution-case/resources/brief.md` `ee9c1cd8…`;
`workflows/scc-resolution-case/resources/checks.md` `62db4f43…`;
`workflows/construct-local-work-graph/WORKFLOW.md` `c528053e…`;
`workflows/project-setup/WORKFLOW.md` `5177aed9…`;
`workflows/project-setup/resources/method.md` `3ba16fd8…`;
`workflows/catalog.yaml` `00e9bb05…`;
`workflows/index.json` `f701e3d4…`;
`tools/validation/build_workflow_index.py` `470439d5…`;
`tools/validation/test_workflow_catalog.py` `9579a643…`;
`docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.md` `ade71852…`;
`docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v3.html` `94bc808e…`;
`docs/alignment-manual/README.md` `76733d82…`;
`docs/governance_harness/_DECISIONS/_REGISTER.md` `be4e4cb5…`.
The `workflows/project-dag/` package is new in this change.

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA for projects that accept a project DAG
after it; project loops with existing DAG or case records adopt by their own
ruling (see Adoption)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation.

On the meaning of K-DEP-1:

> The "no central dependency graph" was only meant to be about the Chirality repo as a whole, because it's made up of projects and each of those projects will have it's own DAG for that project as a whole. And then each development loop will build a work graph for some tranche of work within that DAG. That should be how the governance is written and should be consistent with how the projects are being developed now.

On local files that disagree with the DAG:

> local files that break the DAG need to trigger an audit but the DAG can't be its own authority, so maybe I'm not getting this still?

The agent then proposed the model recorded under Decision items 1 to 5. The
owner answered:

> yes, write D-GOV-49 that way.

On a home for SCC cases:

> We should make that `_DAG/cases` be the place where all projects work from going forward, and allow for PKG-00 to still be used for legacy projects. We may retire that backwards compatibility eventually once it ages out.

The agent added conditions: `_DAG/cases/` must be an allowed write location in
SPEC's tool-root and containment rules; each project uses one home for its
cases; existing PKG-00 cases stay where they are and are not migrated; and
retiring the legacy home is a later decision, once no active project uses it.
The owner agreed.

The owner also approved, in the same conversation, registering `_DAG/` in SPEC
§1.2 as the home for accepted project DAG versions, with snapshots and a
`_LATEST.md` pointer, following Piping's practice
(`projects/chirality-piping/execution/_DAG/_LATEST.md`), and making REQUIRED for
an accepted DAG version the three fields that `audit_dag.py --strict` rejects
but SPEC marks only as recommended. Of the new workflows, the owner said they
"can become core".

On the charter restatement of K-DEP-1:

> PRD_ROOT item O-8 should be revised to match D-GOV-49

On the working-records exception to K-SNAP-1 for `_DAG/cases/` and
`_DAG/_Candidates/`, and the matching PRD_ROOT N-5 text:

> yes, approve the exception, including N-5

## Decision

1. **Neither side is self-authorizing.** Neither the project DAG nor the local
   dependency files authorize themselves. Authority comes from the human's
   acceptance, as with an accepted decomposition snapshot.
2. **The local files are the evidence.** `_DEPENDENCIES.md` and
   `Dependencies.csv` hold the dependency evidence: human declarations and
   agent extractions. They may change at any time.
3. **An accepted version is accepted evidence.** An accepted project DAG
   version is a snapshot of that evidence that the human reviewed and
   accepted. It carries authority only through its acceptance record, and only
   while it is current with the evidence.
4. **Departures are decided, not absorbed.** When a local file departs from
   the accepted version (a new edge, a removed edge, or a cycle), neither side
   silently wins:
   1. a currency audit flags the DAG stale for the affected deliverables;
   2. a candidate new version is prepared;
   3. the human accepts it or rejects the change.

   Until the human decides, unaffected work uses the accepted version.
   Affected deliverables get a `DAG pending` status instead of a ready or
   blocked verdict. The flag clears when a new version is accepted or the
   change is rejected.
5. **Blockers.** A project that has an accepted DAG computes blockers from the
   accepted current version, with `DAG pending` for mismatches. A project
   without an accepted DAG uses its recorded registers (SPEC §5.3).
6. **Scope.** The Chirality repository has no cross-project dependency graph.
   Each project may accept its own project DAG. Each development loop builds
   work graphs (`construct-local-work-graph`) for a tranche of work within
   that DAG.
7. **`_DAG/` tool root.** `{EXECUTION_ROOT}/_DAG/` is registered in SPEC §1.2
   (and as `{DAG_ROOT}` in §0.3) as the home for accepted project DAG versions:
   immutable `DAG-NNN/` snapshots, a `_LATEST.md` pointer that names only an
   accepted version, and candidates under `_Candidates/`. Currency audits are
   observations under `_Evaluation/DAGCurrency/`.
8. **Required fields.** `tools/coordination/audit_dag.py --canonical --strict`
   rejects a blank or non-canonical `Explicitness`, `SatisfactionStatus`, or
   `Confidence`, which SPEC §6.2 marks SHOULD for a register. These three are
   REQUIRED in every edge row of an accepted DAG version (SPEC §5.4; §6.2
   annotated). A blank is completed in the local file by its owner before
   acceptance; it is not an acceptable exception.
9. **SCC case home.** `_DAG/cases/<CASE-ID>/` is where all projects hold SCC
   resolution cases from this decision on. It is an allowed write location in
   SPEC §0.2.3, §0.3 and §1.2. A project whose cases are already held in a
   PKG-00 control deliverable may keep that legacy home. Each project uses one
   home and does not split its cases. Existing PKG-00 cases, for example the
   App's
   `projects/chirality-app-dev/execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure/`,
   stay where they are and are not migrated. Retiring the legacy home is a
   later decision, once no active project uses it.

   A case folder is keyed by a stable `CASE_ID`, not by the SCC ID of a
   closure run, because `analyze_dep_closure.py` numbers SCCs by position in
   each run. A new case takes `SCC-CASE-NNN`, the next unused three-digit
   number in the project's case home, assigned when the case opens and never
   reused. `Case_Datasheet.md` records the originating closure snapshot, the
   SCC ID there, and the member node set. A later closure snapshot's SCC is
   matched to an existing case by member node set: a changed membership is
   recorded in that case, not given a new folder, unless the human rules it a
   different cycle. Legacy PKG-00 case IDs are unchanged.
10. **Working records in `_DAG/`.** Within `_DAG/`, `cases/<CASE-ID>/` and
    `_Candidates/DAG-NNN/` are working records, updated in place under their
    workflow's brief, with Git history as their revision record. Accepted
    `DAG-NNN/` versions and `_Evaluation/DAGCurrency/` snapshots remain
    immutable snapshots; a candidate becomes immutable when it is accepted as
    a version. CONTRACT K-SNAP-1, SPEC §1.2 and SPEC §11.1 carry this clause.
    It is a consequence of the owner's `_DAG/cases` ruling (an SCC case is
    updated over time), and the owner confirmed it: "yes, approve the
    exception, including N-5". PRD_ROOT N-5, which transcribes K-SNAP-1,
    carries the same exception.
11. **Surfaces.** CONTRACT K-DEP-1 is rewritten to items 1 to 6, and K-DEP-1
    joins the human-review enforcement row. K-SNAP-1 gains the item 10
    clause. SPEC gains §5.4 (Accepted Project DAG, with the DAG-current and
    DAG-pending blocker rule), a §5.3 note that its blocker rules apply to
    projects without an accepted DAG, the `_DAG/` tree entry (with
    `_Candidates/`), tool-root row and paragraph, the `{DAG_ROOT}` token, the
    containment note, the §6.2 annotations, the item 10 working-records clause
    in §1.2 and §11.1, and a §11.2 note. The DIRECTIVE structural constraint
    reads "at most one accepted DAG per project" instead of "no central
    dependency graph to maintain". The agent manual v3 §8 is aligned and its
    HTML regenerated. `docs/PRD_ROOT.md` O-8, which transcribed the earlier
    K-DEP-1, is revised to this decision, and N-5, which transcribes K-SNAP-1,
    carries the item 10 exception, with an owner amendment note at the top of
    the file.
12. **Workflows.** `project-dag` drops its "derived view" framing and applies
    items 1 to 10: currency audit, `DAG pending`, successor or rejection,
    `_DAG/_LATEST.md`, `_DAG/cases/`, and the required fields. Its fallback of
    holding cycle edges only as non-gating candidates when no PKG-00 control
    deliverable exists is removed; every held SCC edge cites its case. It
    joins the catalog's core navigation list (not `centralWorkflowNames` and
    not the Root `AGENTS.md` table). `construct-local-work-graph` works within
    the accepted current version and respects `DAG pending`.
    `scc-resolution-case` defaults to `_DAG/cases/<CASE-ID>/`, defines the
    `SCC-CASE-NNN` identity and node-set matching of item 9, writes run
    records under the case folder, and allows the legacy PKG-00 home.
    `project-setup` changes only at its SCC routing and DAG handoff lines and
    adds the accepted-DAG blocker rule to its Phase 3.1 scan.

## Adoption

Nothing is retrofitted. Existing DAG records, pointers and case folders are not
edited. Each project loop decides its own adoption.

- **Piping.** Piping keeps `execution/_DAG/DAG-001` to `DAG-011` and
  `_DAG/_LATEST.md`. Its records call the approved DAG the "dependency graph
  authority" (`docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`; decision D-56) or its
  "dependency authority" (`_DAG/_LATEST.md` for DAG-011), and the local
  registers "synchronized mirrors, not independent sequencing authority" (for
  example `_DAG/DAG-010/DAG_Audit.md`). That wording is stronger than D-GOV-49,
  under which a DAG carries authority only through acceptance while it is
  current with the local evidence, and departures are decided by the human
  rather than resolved in the DAG's favour. Whether and how to change that
  wording is left to the Piping loop.
- **App.** The App holds its SCC cases in
  `PKG-00_DAG_Closure_and_Project_Control`; that legacy home continues and its
  cases are not migrated. The App has no `execution/_DAG/` yet.
- **Runtime.** Runtime records tracking mode `DECLARED` and has neither
  `_DAG/` nor a PKG-00 case home. It resolves and packages the catalog, in
  which `project-dag` is now a core entry.
- **PEC.** PEC is being redeveloped, and the owner is deferring action there.
  Its notice is informational only.

## Unchanged

- K-DEP-2, the v3.1 register schema other than the §6.2 annotations, and the
  §5.3 tracking modes and their meanings.
- `docs/CYCLE_DRIVEN_RESOLUTION.md`: unresolved cycle edges stay non-gating.
- `tools/coordination/audit_dag.py`, `tools/validation/validate_scc_resolution_case.py`,
  `tools/coordination/materialize_local_dependencies.py`, the
  `dependency-extract` mirroring, and the `review` workflow. The last three
  belong to a separate held branch.
- Historical records, earlier manual editions, the thesis and proposals.
- The Root `AGENTS.md` central-workflow table and `centralWorkflowNames`.
- `tools/coordination/analyze_dep_closure.py` and its positional SCC numbering.
- Root product historical files restating the old O-8
  (`execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` SOW-033 and
  `execution/PKG-03_*/.../DEL-03-03_*/ScopeOfWork.md`) are not edited.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-PROJECT-DAG-D-GOV-49-20260926.yaml`.
- `tools/validation/test_workflow_catalog.py` checks the K-DEP-1 text, SPEC
  §5.4, the `_DAG/` registration and `{DAG_ROOT}` token, the `_DAG/cases/`
  home, the three REQUIRED field annotations, that `project-dag` is core but
  not central and no longer a derived view, that its no-PKG-00 fallback is
  gone, that `scc-resolution-case` names `_DAG/cases/<CASE-ID>/` with the
  `SCC-CASE-NNN` identity and node-set matching, and the K-SNAP-1 and SPEC
  §11.1 working-records clause. The core navigation list in
  `tools/validation/build_workflow_index.py` gains `project-dag`, and
  `workflows/index.json` is regenerated.
- `validate_scc_resolution_case.py` checks for a `Dependencies.csv` only under
  the App's legacy PKG-00 path; for `_DAG/cases/`, the
  `scc-resolution-case` checks record that as a manual check until the
  validator is generalized.
- The register fills D-GOV-48's publication SHA
  (`7bfdcfa9d74d83f5a334fe71595d2a2e6eab6f75`, merge of PR #942).
- Notices are routed to the App, Runtime, Piping and PEC loops. No release is
  made.
