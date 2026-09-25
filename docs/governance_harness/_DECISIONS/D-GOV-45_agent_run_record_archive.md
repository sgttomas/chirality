# D-GOV-45 — Agent run records are history: rolling archive and leak-only checks

Status: RATIFIED 2026-09-25 — “ratified, merge when green.”; application
carried in the same pull request as this record

Date: 2026-09-25 (America/Edmonton)

FramedBy: HELP_HUMAN (Claude Code session on hosted-CI burden reduction, after
tranches ROOT-CI-BURDEN-REDUCTION-20260925 and ROOT-CI-BURDEN-FOLLOWUPS-20260925)

AcceptedBasis: main@8007c59270bc83035eac8ec6eab65926cfe8668c (merge of PR #907)

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

## Owner direction (verbatim)

Owner Ryan Tufts, 2026-09-25, in the active session, when shown that
`_Coordination/AgentRuns` held about 2.2 GB and 69,000 of the repository's
files:

> I'm guessing a lot of legacy files.  The Deliverables folders with their
> typical contents are a must.  The _Coordination folder contains a lot of
> historical data that I don't want to get rid of but it has no bearing on the
> functionality of anything.  There may be some linters that work over that
> content but mostly as run evidence it can be diminished in terms of testing.
> It's useful context sometimes (infrequently) when agents are scoping work.
> In future instances of a project I will have a much leaner set of run
> records.  This was accumulation through months of learning how to execute
> projects at scale with agents.

> ... I don't need previous agent runs tested in any manner whatsoever, and I
> figure the testing here is basically linters and checking for exposed
> secrets and stuff like that we don't want to leak out?  If you need a
> governance record, I'm here to provide it.

> OH I hadn't read your proposal for archiving old agent runs.  That would
> make it easier to focus on just what was recent or directly applicable.

On the four open choices (closed-run rule, binaries in active runs, rollout,
this record):

> 1. 14 days.
> 2. Yes.
> 3. All five at once.
> 4. ok, proceed accordingly.

## Owner ratification (verbatim)

Owner Ryan Tufts, 2026-09-25, on reviewing this record in pull request #910:

> ratified, merge when green.  I also updated the Advanced Security,
> additionally I've restricted to PR merging to collaborators only.

Item 5's owner action is complete: the repository API reported
`secret_scanning=enabled` and `secret_scanning_push_protection=enabled` on
2026-09-25.

## Decision

1. **Run records are history.** A run folder is a direct child of
   `<execution>/_Coordination/AgentRuns/` in Root, App, Piping, PEC or
   Runtime. Run records are preserved but are not tested, linted or re-verified.
   No check may newly depend on the content of an archived run record.
2. **Rolling archive.** `tools/archive_agent_runs.py` applies
   `tools/agent_runs_archive_policy.json`:
   - A run folder that no commit has touched for **14 days** is archived whole.
   - In folders still in use, binary evidence (traces, screenshots, archives,
     databases) that no commit has touched for **7 days** is archived file by
     file.
   - "Touched" is measured by committer date from 00:00 local time on the
     cutoff date, so a run's result depends only on its as-of date. A policy
     `containers` entry (Runtime's `AgentRuns/runtime/`) holds one run per
     child directory.

   Archiving removes paths from the working tree only. The exact bytes stay in
   Git history at an immutable annotated tag `archive/agent-runs-<date>`, whose
   commit must hold every archived path. Nothing is deleted from history, and
   no commit SHA changes. Each `AgentRuns/` directory carries
   `ARCHIVE_INDEX.json` (machine-readable) and `ARCHIVE.md` (how to read or
   restore). The tool is re-run at milestones or monthly, and each run adds a
   new tag.
3. **References resolve to the archive.** A reference to an archived run
   folder, a path inside one, or an archived file resolves as preserved history.
   This applies to the self-check's GEN-5 source references and to portability
   policy targets. Historical abs-path exceptions for archived targets are not
   re-verified.
4. **Governance state does not belong in run folders.** The policy `keep` list
   holds nine run folders whose files the root governance gates and tests read
   as current state: the Root runtime-migration, effective-state and successor
   adoptions, and the Runtime stage-2 records. They were identified by tracing
   the gates and tests on 2026-09-25. New governance state is filed under
   `execution/_harness/` or a decision directory, never in a run folder. The
   keep list shrinks as the existing state is relocated by later changes.
5. **Leak checks only for new run records.** governance-harness scans only the
   run records a change adds or modifies (`tools/validation/validate_run_record_leaks.py`),
   because the repository is public:
   - a credential pattern is BLOCK;
   - a file larger than 5 MB is WARN (keep large evidence as CI artifacts).

   GitHub secret scanning and push protection, enabled by the owner on
   2026-09-25, block a credential before it is pushed at all.
6. **Unchanged.** This decision leaves the following as they are:
   - Deliverable folders (`execution/PKG-*`) and their contents;
   - `_Reconciliation`, `_ScopeChange`, decision records, and `_Coordination`
     files outside `AgentRuns/`;
   - Git history;
   - each project loop's acceptance evidence obligations.

   A loop that needs an archived record reads it from the tag. It restores the
   record into the tree only to reopen the run.

## Application and assurance (first archive, 2026-09-25)

- **Archived:** 323 run folders (53,393 files) and 229 binary files from
  active folders, about 1.14 GB, across all five execution roots, at tag
  `archive/agent-runs-2026-09-25` (commit
  8007c59270bc83035eac8ec6eab65926cfe8668c).
- **Checked on the archived tree:**
  - gates G0–G4 exit 0;
  - the self-check reports the same finding counts as the full tree;
  - the full tools suite passes with `CHIRALITY_REQUIRE_LIVE_TESTS=1`, including
    a live check that every indexed path is held by its tag and no longer
    tracked;
  - the Runtime (407), App (2,274), PEC and Piping Python (1,209) suites pass.
- **Leak-pattern calibration:** across all 72,902 existing run-record files,
  the only match was a deliberately fake test value.
