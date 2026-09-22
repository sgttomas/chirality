# Alignment manual undertaking work graph

Run-specific navigation as of 2026-09-22. This is an ad hoc plan under
`BRIEF.md`, not a registered workflow, scope grant, accepted production DAG,
or a replacement for any live project pointer. Basis:
`9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`.

| Node | Owner | Depends on | State and next return |
|---|---|---|---|
| Recover and preserve supplied originals | HELP_HUMAN `/root` | Owner task | Originals copied; compare final hashes with `INPUTS.json` before submission |
| Review all manuscript chapters and draft v2 | `/root/manual_review_manager` | Preserved v1, bounded chapter returns | Complete; v2 and review returned; count-precision repair independently backchecked |
| Verify App, Piping, Runtime and PEC application | `/root/project_coverage_manager` | Current project entries and pointers | Coverage notes and source returns present; final claims assessed with content review |
| Draft agent user guide | `/root/guide_author` | Owner task, verified Root/project basis, review findings | Draft complete at SHA-256 `2b749f8f…2ab2b`; Markdown is the publication source |
| Publish human-friendly HTML | `/root/html_publisher` | Integrated guide, authorized assets | Complete at SHA-256 `77bbc449…39b5`; parity and local-link checks pass; browser and print visual inspection NOT VERIFIED (URL policy and missing native Pango) |
| Prepare scope and validation preflight | WORKING_ITEMS `/root/closeout_manager` | Brief, branch, repository guards | Complete: scope, originals, 303 local-link targets, isolated rendering, live guards and 897 tests plus 48 subtests pass; committed-range checks pending |
| Independent final candidate review | `/root/content_reviewer`, `/root/publication_reviewer` | Integrated v2, guide, HTML and evidence | Complete; final hashes match; no unresolved content or publication findings |
| Validate and close through PR | WORKING_ITEMS `/root/closeout_manager` | Root closeout signal, independent review, affected checks | Authorized by root with visual limit disclosed; sole Git mutation owner; candidate, CI and final merge outcome recorded in ordinary PR/Git history |

Recovery: read `BRIEF.md`, this graph, the current working tree, source and
review returns, and `closeout-validation.md` before continuing. Determine the
current node from actual returned evidence rather than from this plan alone.
If a descendant launch fails or a return is incomplete, its owning manager
must reassign or complete the bounded work; a launch brief is not a completed
execution. Preserve original source bytes and historical evidence. Later
repairs reopen the affected validation and review, without implying owner
acceptance or release.
