# A1 Integration Activation 001

Status: `ACTIVE — CHANGE RELEASED; BLANKET PR MERGE APPROVAL RECORDED`

## Accepted basis and authority

HELP_HUMAN accepted `snapshots/W_A1/preintegration/ACCEPTANCE.md` at exact
snapshot manifest SHA-256
`c8ae005ca8d1007ccf7f7ee12dc81f441ad65ae3fa094d7314249e747831a5eb`
and 12/12 acceptance bindings. The exact integration basis is synchronized
`main`, `origin/main`, and remote main at
`34b87ec77010035eeaa76f0fa65981ec57e78933`. The human has granted blanket
approval to merge PRs throughout this goal; CHANGE may create, push, and merge
the A1 PR once every declared gate passes.

## Exact integration

`CHANGE-A1-G` must consume only the accepted 75-row replacement and inverse
rollback manifests. Integrate exactly these 15 members in manifest order:

`DEL-00-01`, `DEL-00-02`, `DEL-01-01`, `DEL-01-02`, `DEL-01-03`,
`DEL-01-04`, `DEL-02-01`, `DEL-02-02`, `DEL-02-03`, `DEL-02-04`,
`DEL-02-05`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`.

For each member, one serial content commit must add the exact accepted
`ScopeOfWork.md` candidate and delete only exact `Datasheet.md`,
`Specification.md`, `Guidance.md`, and `Procedure.md` preimages. Preserve all
`_STATUS.md`, control, dependency, and unrelated bytes. Each commit must match
its exact five-row manifest slice and no other project path. Do not combine
members, reorder them, or edit candidate content.

The governed A1 preparation/reconciliation/acceptance evidence accumulated
under this run must be committed durably without `.claude-worktrees/**` or any
unrelated user path. CHANGE owns integration evidence under
`snapshots/W_A1/integration/**` and `instances/CHANGE-A1-G/**`, plus exact run
coordination closure updates. Record branch, base, each content commit hash,
tree/path hashes, checks, PR, merge, and rollback basis.

## Validation, PR, merge, and postmerge

Before push/PR and again where required after merge, prove:

- exact 15-member `SOW_V1`, zero legacy production docs, exact candidate
  hashes, and unchanged status/control hashes;
- accepted replacement application and rollback manifest identity;
- source/status/candidate/package/acceptance basis has not drifted;
- harness self-check, 264-test harness suite, App typecheck, 713+4 frontend
  test baseline, build, and live-stub premerge Section 8 8/8 plus Section 9
  report-only 16/16 all PASS;
- portability, containment, no unexpected project paths, and diff hygiene;
- branch contains no `.claude-worktrees/**` and no unrelated user changes.

Use a `codex/` branch, push it, create one A1 PR, and merge it under the
recorded blanket approval only after all gates pass. Then synchronize local
main to the remote merge, reproduce the exact merged 15-member state and full
checks, and write an immutable postmerge derivative/handoff. HELP_HUMAN
acceptance of that postmerge snapshot remains separate.

Any basis drift, missing/deviant evidence, path outside the exact manifests,
candidate/status/control mismatch, failed check, PR conflict, unexpected
remote change, or inability to preserve unrelated user state blocks before
merge or returns exact recovery requirements.

## Non-authority

This activation authorizes exact A1 Git integration and the approved PR merge
only. It does not alter lifecycle, issue/reissue, approve H1/H2, act on an
ISSUED member, release a product, retire legacy support globally, or authorize
any later wave.
